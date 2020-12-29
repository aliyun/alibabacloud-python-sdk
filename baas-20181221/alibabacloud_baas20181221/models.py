# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, Any, List


class AcceptFabricInvitationRequest(TeaModel):
    def __init__(
        self,
        code: str = None,
        is_accepted: bool = None,
    ):
        self.code = code
        self.is_accepted = is_accepted

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.is_accepted is not None:
            result['IsAccepted'] = self.is_accepted
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsAccepted') is not None:
            self.is_accepted = m.get('IsAccepted')
        return self


class AcceptFabricInvitationResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_code: int = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.error_code = error_code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AcceptFabricInvitationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AcceptFabricInvitationResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AcceptFabricInvitationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ApplyAntChainCertificateRequest(TeaModel):
    def __init__(
        self,
        ant_chain_id: str = None,
        upload_req: str = None,
    ):
        self.ant_chain_id = ant_chain_id
        self.upload_req = upload_req

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.ant_chain_id is not None:
            result['AntChainId'] = self.ant_chain_id
        if self.upload_req is not None:
            result['UploadReq'] = self.upload_req
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AntChainId') is not None:
            self.ant_chain_id = m.get('AntChainId')
        if m.get('UploadReq') is not None:
            self.upload_req = m.get('UploadReq')
        return self


class ApplyAntChainCertificateResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: str = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class ApplyAntChainCertificateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ApplyAntChainCertificateResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ApplyAntChainCertificateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ApplyAntChainCertificateWithKeyAutoCreationRequest(TeaModel):
    def __init__(
        self,
        ant_chain_id: str = None,
        consortium_id: str = None,
        password: str = None,
        country_name: str = None,
        state_or_province_name: str = None,
        locality_name: str = None,
        organization_name: str = None,
        organization_unit_name: str = None,
        common_name: str = None,
    ):
        self.ant_chain_id = ant_chain_id
        self.consortium_id = consortium_id
        self.password = password
        self.country_name = country_name
        self.state_or_province_name = state_or_province_name
        self.locality_name = locality_name
        self.organization_name = organization_name
        self.organization_unit_name = organization_unit_name
        self.common_name = common_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.ant_chain_id is not None:
            result['AntChainId'] = self.ant_chain_id
        if self.consortium_id is not None:
            result['ConsortiumId'] = self.consortium_id
        if self.password is not None:
            result['Password'] = self.password
        if self.country_name is not None:
            result['CountryName'] = self.country_name
        if self.state_or_province_name is not None:
            result['StateOrProvinceName'] = self.state_or_province_name
        if self.locality_name is not None:
            result['LocalityName'] = self.locality_name
        if self.organization_name is not None:
            result['OrganizationName'] = self.organization_name
        if self.organization_unit_name is not None:
            result['OrganizationUnitName'] = self.organization_unit_name
        if self.common_name is not None:
            result['CommonName'] = self.common_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AntChainId') is not None:
            self.ant_chain_id = m.get('AntChainId')
        if m.get('ConsortiumId') is not None:
            self.consortium_id = m.get('ConsortiumId')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('CountryName') is not None:
            self.country_name = m.get('CountryName')
        if m.get('StateOrProvinceName') is not None:
            self.state_or_province_name = m.get('StateOrProvinceName')
        if m.get('LocalityName') is not None:
            self.locality_name = m.get('LocalityName')
        if m.get('OrganizationName') is not None:
            self.organization_name = m.get('OrganizationName')
        if m.get('OrganizationUnitName') is not None:
            self.organization_unit_name = m.get('OrganizationUnitName')
        if m.get('CommonName') is not None:
            self.common_name = m.get('CommonName')
        return self


class ApplyAntChainCertificateWithKeyAutoCreationResponseBodyResultDownloadPath(TeaModel):
    def __init__(
        self,
        ca_crt_url: str = None,
        sdk_url: str = None,
        client_crt_url: str = None,
        trust_ca_url: str = None,
    ):
        self.ca_crt_url = ca_crt_url
        self.sdk_url = sdk_url
        self.client_crt_url = client_crt_url
        self.trust_ca_url = trust_ca_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.ca_crt_url is not None:
            result['CaCrtUrl'] = self.ca_crt_url
        if self.sdk_url is not None:
            result['SdkUrl'] = self.sdk_url
        if self.client_crt_url is not None:
            result['ClientCrtUrl'] = self.client_crt_url
        if self.trust_ca_url is not None:
            result['TrustCaUrl'] = self.trust_ca_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CaCrtUrl') is not None:
            self.ca_crt_url = m.get('CaCrtUrl')
        if m.get('SdkUrl') is not None:
            self.sdk_url = m.get('SdkUrl')
        if m.get('ClientCrtUrl') is not None:
            self.client_crt_url = m.get('ClientCrtUrl')
        if m.get('TrustCaUrl') is not None:
            self.trust_ca_url = m.get('TrustCaUrl')
        return self


class ApplyAntChainCertificateWithKeyAutoCreationResponseBodyResult(TeaModel):
    def __init__(
        self,
        private_key: str = None,
        download_path: ApplyAntChainCertificateWithKeyAutoCreationResponseBodyResultDownloadPath = None,
    ):
        self.private_key = private_key
        self.download_path = download_path

    def validate(self):
        if self.download_path:
            self.download_path.validate()

    def to_map(self):
        result = dict()
        if self.private_key is not None:
            result['PrivateKey'] = self.private_key
        if self.download_path is not None:
            result['DownloadPath'] = self.download_path.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PrivateKey') is not None:
            self.private_key = m.get('PrivateKey')
        if m.get('DownloadPath') is not None:
            temp_model = ApplyAntChainCertificateWithKeyAutoCreationResponseBodyResultDownloadPath()
            self.download_path = temp_model.from_map(m['DownloadPath'])
        return self


class ApplyAntChainCertificateWithKeyAutoCreationResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: ApplyAntChainCertificateWithKeyAutoCreationResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = ApplyAntChainCertificateWithKeyAutoCreationResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class ApplyAntChainCertificateWithKeyAutoCreationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ApplyAntChainCertificateWithKeyAutoCreationResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ApplyAntChainCertificateWithKeyAutoCreationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchAddAntChainMiniAppQRCodeAuthorizedUsersRequest(TeaModel):
    def __init__(
        self,
        ant_chain_id: str = None,
        phone_list: Dict[str, Any] = None,
    ):
        self.ant_chain_id = ant_chain_id
        self.phone_list = phone_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.ant_chain_id is not None:
            result['AntChainId'] = self.ant_chain_id
        if self.phone_list is not None:
            result['PhoneList'] = self.phone_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AntChainId') is not None:
            self.ant_chain_id = m.get('AntChainId')
        if m.get('PhoneList') is not None:
            self.phone_list = m.get('PhoneList')
        return self


class BatchAddAntChainMiniAppQRCodeAuthorizedUsersShrinkRequest(TeaModel):
    def __init__(
        self,
        ant_chain_id: str = None,
        phone_list_shrink: str = None,
    ):
        self.ant_chain_id = ant_chain_id
        self.phone_list_shrink = phone_list_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.ant_chain_id is not None:
            result['AntChainId'] = self.ant_chain_id
        if self.phone_list_shrink is not None:
            result['PhoneList'] = self.phone_list_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AntChainId') is not None:
            self.ant_chain_id = m.get('AntChainId')
        if m.get('PhoneList') is not None:
            self.phone_list_shrink = m.get('PhoneList')
        return self


class BatchAddAntChainMiniAppQRCodeAuthorizedUsersResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: str = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class BatchAddAntChainMiniAppQRCodeAuthorizedUsersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: BatchAddAntChainMiniAppQRCodeAuthorizedUsersResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = BatchAddAntChainMiniAppQRCodeAuthorizedUsersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckFabricConsortiumDomainRequest(TeaModel):
    def __init__(
        self,
        domain_code: str = None,
    ):
        self.domain_code = domain_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.domain_code is not None:
            result['DomainCode'] = self.domain_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainCode') is not None:
            self.domain_code = m.get('DomainCode')
        return self


class CheckFabricConsortiumDomainResponseBodyResult(TeaModel):
    def __init__(
        self,
        domain: str = None,
        valid: bool = None,
        prompt: str = None,
    ):
        self.domain = domain
        self.valid = valid
        self.prompt = prompt

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.valid is not None:
            result['Valid'] = self.valid
        if self.prompt is not None:
            result['Prompt'] = self.prompt
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Valid') is not None:
            self.valid = m.get('Valid')
        if m.get('Prompt') is not None:
            self.prompt = m.get('Prompt')
        return self


class CheckFabricConsortiumDomainResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_code: int = None,
        success: bool = None,
        result: CheckFabricConsortiumDomainResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.error_code = error_code
        self.success = success
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Result') is not None:
            temp_model = CheckFabricConsortiumDomainResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class CheckFabricConsortiumDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CheckFabricConsortiumDomainResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CheckFabricConsortiumDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckFabricOrganizationDomainRequest(TeaModel):
    def __init__(
        self,
        domain_code: str = None,
        domain: str = None,
    ):
        self.domain_code = domain_code
        self.domain = domain

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.domain_code is not None:
            result['DomainCode'] = self.domain_code
        if self.domain is not None:
            result['Domain'] = self.domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainCode') is not None:
            self.domain_code = m.get('DomainCode')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        return self


class CheckFabricOrganizationDomainResponseBodyResult(TeaModel):
    def __init__(
        self,
        domain: str = None,
        valid: bool = None,
        prompt: str = None,
    ):
        self.domain = domain
        self.valid = valid
        self.prompt = prompt

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.valid is not None:
            result['Valid'] = self.valid
        if self.prompt is not None:
            result['Prompt'] = self.prompt
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Valid') is not None:
            self.valid = m.get('Valid')
        if m.get('Prompt') is not None:
            self.prompt = m.get('Prompt')
        return self


class CheckFabricOrganizationDomainResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_code: int = None,
        success: bool = None,
        result: CheckFabricOrganizationDomainResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.error_code = error_code
        self.success = success
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Result') is not None:
            temp_model = CheckFabricOrganizationDomainResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class CheckFabricOrganizationDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CheckFabricOrganizationDomainResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CheckFabricOrganizationDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConfirmFabricConsortiumMemberRequestOrganization(TeaModel):
    def __init__(
        self,
        organization_id: str = None,
    ):
        self.organization_id = organization_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class ConfirmFabricConsortiumMemberRequest(TeaModel):
    def __init__(
        self,
        consortium_id: str = None,
        organization: List[ConfirmFabricConsortiumMemberRequestOrganization] = None,
    ):
        self.consortium_id = consortium_id
        self.organization = organization

    def validate(self):
        if self.organization:
            for k in self.organization:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.consortium_id is not None:
            result['ConsortiumId'] = self.consortium_id
        result['Organization'] = []
        if self.organization is not None:
            for k in self.organization:
                result['Organization'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsortiumId') is not None:
            self.consortium_id = m.get('ConsortiumId')
        self.organization = []
        if m.get('Organization') is not None:
            for k in m.get('Organization'):
                temp_model = ConfirmFabricConsortiumMemberRequestOrganization()
                self.organization.append(temp_model.from_map(k))
        return self


class ConfirmFabricConsortiumMemberResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_code: int = None,
        success: bool = None,
        result: bool = None,
    ):
        self.request_id = request_id
        self.error_code = error_code
        self.success = success
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class ConfirmFabricConsortiumMemberResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ConfirmFabricConsortiumMemberResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ConfirmFabricConsortiumMemberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CopyAntChainContractProjectRequest(TeaModel):
    def __init__(
        self,
        project_id: str = None,
        project_name: str = None,
        project_version: str = None,
        project_description: str = None,
    ):
        self.project_id = project_id
        self.project_name = project_name
        self.project_version = project_version
        self.project_description = project_description

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.project_version is not None:
            result['ProjectVersion'] = self.project_version
        if self.project_description is not None:
            result['ProjectDescription'] = self.project_description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('ProjectVersion') is not None:
            self.project_version = m.get('ProjectVersion')
        if m.get('ProjectDescription') is not None:
            self.project_description = m.get('ProjectDescription')
        return self


class CopyAntChainContractProjectResponseBodyResult(TeaModel):
    def __init__(
        self,
        update_time: int = None,
        consortium_id: str = None,
        create_time: int = None,
        project_id: str = None,
        project_name: str = None,
        project_version: str = None,
        project_description: str = None,
    ):
        self.update_time = update_time
        self.consortium_id = consortium_id
        self.create_time = create_time
        self.project_id = project_id
        self.project_name = project_name
        self.project_version = project_version
        self.project_description = project_description

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.consortium_id is not None:
            result['ConsortiumId'] = self.consortium_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.project_version is not None:
            result['ProjectVersion'] = self.project_version
        if self.project_description is not None:
            result['ProjectDescription'] = self.project_description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('ConsortiumId') is not None:
            self.consortium_id = m.get('ConsortiumId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('ProjectVersion') is not None:
            self.project_version = m.get('ProjectVersion')
        if m.get('ProjectDescription') is not None:
            self.project_description = m.get('ProjectDescription')
        return self


class CopyAntChainContractProjectResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: CopyAntChainContractProjectResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = CopyAntChainContractProjectResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class CopyAntChainContractProjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CopyAntChainContractProjectResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CopyAntChainContractProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAntChainAccountRequest(TeaModel):
    def __init__(
        self,
        ant_chain_id: str = None,
        account: str = None,
        account_pub_key: str = None,
        account_recover_pub_key: str = None,
    ):
        self.ant_chain_id = ant_chain_id
        self.account = account
        self.account_pub_key = account_pub_key
        self.account_recover_pub_key = account_recover_pub_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.ant_chain_id is not None:
            result['AntChainId'] = self.ant_chain_id
        if self.account is not None:
            result['Account'] = self.account
        if self.account_pub_key is not None:
            result['AccountPubKey'] = self.account_pub_key
        if self.account_recover_pub_key is not None:
            result['AccountRecoverPubKey'] = self.account_recover_pub_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AntChainId') is not None:
            self.ant_chain_id = m.get('AntChainId')
        if m.get('Account') is not None:
            self.account = m.get('Account')
        if m.get('AccountPubKey') is not None:
            self.account_pub_key = m.get('AccountPubKey')
        if m.get('AccountRecoverPubKey') is not None:
            self.account_recover_pub_key = m.get('AccountRecoverPubKey')
        return self


class CreateAntChainAccountResponseBodyResult(TeaModel):
    def __init__(
        self,
        account: str = None,
        ant_chain_id: str = None,
    ):
        self.account = account
        self.ant_chain_id = ant_chain_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.account is not None:
            result['Account'] = self.account
        if self.ant_chain_id is not None:
            result['AntChainId'] = self.ant_chain_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Account') is not None:
            self.account = m.get('Account')
        if m.get('AntChainId') is not None:
            self.ant_chain_id = m.get('AntChainId')
        return self


class CreateAntChainAccountResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: CreateAntChainAccountResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = CreateAntChainAccountResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class CreateAntChainAccountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateAntChainAccountResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateAntChainAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAntChainAccountWithKeyPairAutoCreationRequest(TeaModel):
    def __init__(
        self,
        ant_chain_id: str = None,
        account: str = None,
        password: str = None,
        recover_password: str = None,
    ):
        self.ant_chain_id = ant_chain_id
        self.account = account
        self.password = password
        self.recover_password = recover_password

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.ant_chain_id is not None:
            result['AntChainId'] = self.ant_chain_id
        if self.account is not None:
            result['Account'] = self.account
        if self.password is not None:
            result['Password'] = self.password
        if self.recover_password is not None:
            result['RecoverPassword'] = self.recover_password
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AntChainId') is not None:
            self.ant_chain_id = m.get('AntChainId')
        if m.get('Account') is not None:
            self.account = m.get('Account')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('RecoverPassword') is not None:
            self.recover_password = m.get('RecoverPassword')
        return self


class CreateAntChainAccountWithKeyPairAutoCreationResponseBodyResult(TeaModel):
    def __init__(
        self,
        account_public_key: str = None,
        account: str = None,
        account_recover_private_key: str = None,
        account_recover_public_key: str = None,
        account_private_key: str = None,
        ant_chain_id: str = None,
    ):
        self.account_public_key = account_public_key
        self.account = account
        self.account_recover_private_key = account_recover_private_key
        self.account_recover_public_key = account_recover_public_key
        self.account_private_key = account_private_key
        self.ant_chain_id = ant_chain_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.account_public_key is not None:
            result['AccountPublicKey'] = self.account_public_key
        if self.account is not None:
            result['Account'] = self.account
        if self.account_recover_private_key is not None:
            result['AccountRecoverPrivateKey'] = self.account_recover_private_key
        if self.account_recover_public_key is not None:
            result['AccountRecoverPublicKey'] = self.account_recover_public_key
        if self.account_private_key is not None:
            result['AccountPrivateKey'] = self.account_private_key
        if self.ant_chain_id is not None:
            result['AntChainId'] = self.ant_chain_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountPublicKey') is not None:
            self.account_public_key = m.get('AccountPublicKey')
        if m.get('Account') is not None:
            self.account = m.get('Account')
        if m.get('AccountRecoverPrivateKey') is not None:
            self.account_recover_private_key = m.get('AccountRecoverPrivateKey')
        if m.get('AccountRecoverPublicKey') is not None:
            self.account_recover_public_key = m.get('AccountRecoverPublicKey')
        if m.get('AccountPrivateKey') is not None:
            self.account_private_key = m.get('AccountPrivateKey')
        if m.get('AntChainId') is not None:
            self.ant_chain_id = m.get('AntChainId')
        return self


class CreateAntChainAccountWithKeyPairAutoCreationResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: CreateAntChainAccountWithKeyPairAutoCreationResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = CreateAntChainAccountWithKeyPairAutoCreationResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class CreateAntChainAccountWithKeyPairAutoCreationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateAntChainAccountWithKeyPairAutoCreationResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateAntChainAccountWithKeyPairAutoCreationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAntChainConsortiumRequest(TeaModel):
    def __init__(
        self,
        consortium_name: str = None,
        consortium_description: str = None,
    ):
        self.consortium_name = consortium_name
        self.consortium_description = consortium_description

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.consortium_name is not None:
            result['ConsortiumName'] = self.consortium_name
        if self.consortium_description is not None:
            result['ConsortiumDescription'] = self.consortium_description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsortiumName') is not None:
            self.consortium_name = m.get('ConsortiumName')
        if m.get('ConsortiumDescription') is not None:
            self.consortium_description = m.get('ConsortiumDescription')
        return self


class CreateAntChainConsortiumResponseBodyResult(TeaModel):
    def __init__(
        self,
        consortium_id: str = None,
    ):
        self.consortium_id = consortium_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.consortium_id is not None:
            result['ConsortiumId'] = self.consortium_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsortiumId') is not None:
            self.consortium_id = m.get('ConsortiumId')
        return self


class CreateAntChainConsortiumResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: CreateAntChainConsortiumResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = CreateAntChainConsortiumResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class CreateAntChainConsortiumResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateAntChainConsortiumResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateAntChainConsortiumResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAntChainContractContentRequest(TeaModel):
    def __init__(
        self,
        project_id: str = None,
        parent_content_id: str = None,
        content_name: str = None,
        is_directory: bool = None,
        content: str = None,
    ):
        self.project_id = project_id
        self.parent_content_id = parent_content_id
        self.content_name = content_name
        self.is_directory = is_directory
        self.content = content

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.parent_content_id is not None:
            result['ParentContentId'] = self.parent_content_id
        if self.content_name is not None:
            result['ContentName'] = self.content_name
        if self.is_directory is not None:
            result['IsDirectory'] = self.is_directory
        if self.content is not None:
            result['Content'] = self.content
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ParentContentId') is not None:
            self.parent_content_id = m.get('ParentContentId')
        if m.get('ContentName') is not None:
            self.content_name = m.get('ContentName')
        if m.get('IsDirectory') is not None:
            self.is_directory = m.get('IsDirectory')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        return self


class CreateAntChainContractContentResponseBodyResult(TeaModel):
    def __init__(
        self,
        content_name: str = None,
        parent_content_id: str = None,
        update_time: str = None,
        create_time: str = None,
        project_id: str = None,
        is_directory: bool = None,
        content: str = None,
        content_id: str = None,
    ):
        self.content_name = content_name
        self.parent_content_id = parent_content_id
        self.update_time = update_time
        self.create_time = create_time
        self.project_id = project_id
        self.is_directory = is_directory
        self.content = content
        self.content_id = content_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.content_name is not None:
            result['ContentName'] = self.content_name
        if self.parent_content_id is not None:
            result['ParentContentId'] = self.parent_content_id
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.is_directory is not None:
            result['IsDirectory'] = self.is_directory
        if self.content is not None:
            result['Content'] = self.content
        if self.content_id is not None:
            result['ContentId'] = self.content_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContentName') is not None:
            self.content_name = m.get('ContentName')
        if m.get('ParentContentId') is not None:
            self.parent_content_id = m.get('ParentContentId')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('IsDirectory') is not None:
            self.is_directory = m.get('IsDirectory')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('ContentId') is not None:
            self.content_id = m.get('ContentId')
        return self


class CreateAntChainContractContentResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: CreateAntChainContractContentResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = CreateAntChainContractContentResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class CreateAntChainContractContentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateAntChainContractContentResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateAntChainContractContentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAntChainContractProjectRequest(TeaModel):
    def __init__(
        self,
        consortium_id: str = None,
        project_name: str = None,
        project_version: str = None,
        project_description: str = None,
    ):
        self.consortium_id = consortium_id
        self.project_name = project_name
        self.project_version = project_version
        self.project_description = project_description

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.consortium_id is not None:
            result['ConsortiumId'] = self.consortium_id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.project_version is not None:
            result['ProjectVersion'] = self.project_version
        if self.project_description is not None:
            result['ProjectDescription'] = self.project_description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsortiumId') is not None:
            self.consortium_id = m.get('ConsortiumId')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('ProjectVersion') is not None:
            self.project_version = m.get('ProjectVersion')
        if m.get('ProjectDescription') is not None:
            self.project_description = m.get('ProjectDescription')
        return self


class CreateAntChainContractProjectResponseBodyResult(TeaModel):
    def __init__(
        self,
        update_time: int = None,
        consortium_id: str = None,
        create_time: int = None,
        project_id: str = None,
        project_name: str = None,
        project_version: str = None,
        project_description: str = None,
    ):
        self.update_time = update_time
        self.consortium_id = consortium_id
        self.create_time = create_time
        self.project_id = project_id
        self.project_name = project_name
        self.project_version = project_version
        self.project_description = project_description

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.consortium_id is not None:
            result['ConsortiumId'] = self.consortium_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.project_version is not None:
            result['ProjectVersion'] = self.project_version
        if self.project_description is not None:
            result['ProjectDescription'] = self.project_description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('ConsortiumId') is not None:
            self.consortium_id = m.get('ConsortiumId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('ProjectVersion') is not None:
            self.project_version = m.get('ProjectVersion')
        if m.get('ProjectDescription') is not None:
            self.project_description = m.get('ProjectDescription')
        return self


class CreateAntChainContractProjectResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: CreateAntChainContractProjectResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = CreateAntChainContractProjectResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class CreateAntChainContractProjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateAntChainContractProjectResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateAntChainContractProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFabricChaincodeRequest(TeaModel):
    def __init__(
        self,
        organization_id: str = None,
        channel_id: str = None,
        consortium_id: str = None,
        oss_bucket: str = None,
        oss_url: str = None,
        endorse_policy: str = None,
        location: str = None,
    ):
        self.organization_id = organization_id
        self.channel_id = channel_id
        self.consortium_id = consortium_id
        self.oss_bucket = oss_bucket
        self.oss_url = oss_url
        self.endorse_policy = endorse_policy
        self.location = location

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.consortium_id is not None:
            result['ConsortiumId'] = self.consortium_id
        if self.oss_bucket is not None:
            result['OssBucket'] = self.oss_bucket
        if self.oss_url is not None:
            result['OssUrl'] = self.oss_url
        if self.endorse_policy is not None:
            result['EndorsePolicy'] = self.endorse_policy
        if self.location is not None:
            result['Location'] = self.location
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('ConsortiumId') is not None:
            self.consortium_id = m.get('ConsortiumId')
        if m.get('OssBucket') is not None:
            self.oss_bucket = m.get('OssBucket')
        if m.get('OssUrl') is not None:
            self.oss_url = m.get('OssUrl')
        if m.get('EndorsePolicy') is not None:
            self.endorse_policy = m.get('EndorsePolicy')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        return self


class CreateFabricChaincodeResponseBodyResult(TeaModel):
    def __init__(
        self,
        type: int = None,
        endorse_policy: str = None,
        state: str = None,
        create_time: str = None,
        chaincode_id: str = None,
        message: str = None,
        provider_name: str = None,
        chaincode_name: str = None,
        install: bool = None,
        input: str = None,
        provider_id: str = None,
        deploy_time: str = None,
        chaincode_version: str = None,
        consortium_id: str = None,
        channel_name: str = None,
        path: str = None,
    ):
        self.type = type
        self.endorse_policy = endorse_policy
        self.state = state
        self.create_time = create_time
        self.chaincode_id = chaincode_id
        self.message = message
        self.provider_name = provider_name
        self.chaincode_name = chaincode_name
        self.install = install
        self.input = input
        self.provider_id = provider_id
        self.deploy_time = deploy_time
        self.chaincode_version = chaincode_version
        self.consortium_id = consortium_id
        self.channel_name = channel_name
        self.path = path

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.endorse_policy is not None:
            result['EndorsePolicy'] = self.endorse_policy
        if self.state is not None:
            result['State'] = self.state
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.chaincode_id is not None:
            result['ChaincodeId'] = self.chaincode_id
        if self.message is not None:
            result['Message'] = self.message
        if self.provider_name is not None:
            result['ProviderName'] = self.provider_name
        if self.chaincode_name is not None:
            result['ChaincodeName'] = self.chaincode_name
        if self.install is not None:
            result['Install'] = self.install
        if self.input is not None:
            result['Input'] = self.input
        if self.provider_id is not None:
            result['ProviderId'] = self.provider_id
        if self.deploy_time is not None:
            result['DeployTime'] = self.deploy_time
        if self.chaincode_version is not None:
            result['ChaincodeVersion'] = self.chaincode_version
        if self.consortium_id is not None:
            result['ConsortiumId'] = self.consortium_id
        if self.channel_name is not None:
            result['ChannelName'] = self.channel_name
        if self.path is not None:
            result['Path'] = self.path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('EndorsePolicy') is not None:
            self.endorse_policy = m.get('EndorsePolicy')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ChaincodeId') is not None:
            self.chaincode_id = m.get('ChaincodeId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('ProviderName') is not None:
            self.provider_name = m.get('ProviderName')
        if m.get('ChaincodeName') is not None:
            self.chaincode_name = m.get('ChaincodeName')
        if m.get('Install') is not None:
            self.install = m.get('Install')
        if m.get('Input') is not None:
            self.input = m.get('Input')
        if m.get('ProviderId') is not None:
            self.provider_id = m.get('ProviderId')
        if m.get('DeployTime') is not None:
            self.deploy_time = m.get('DeployTime')
        if m.get('ChaincodeVersion') is not None:
            self.chaincode_version = m.get('ChaincodeVersion')
        if m.get('ConsortiumId') is not None:
            self.consortium_id = m.get('ConsortiumId')
        if m.get('ChannelName') is not None:
            self.channel_name = m.get('ChannelName')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        return self


class CreateFabricChaincodeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_code: int = None,
        success: bool = None,
        result: CreateFabricChaincodeResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.error_code = error_code
        self.success = success
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Result') is not None:
            temp_model = CreateFabricChaincodeResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class CreateFabricChaincodeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateFabricChaincodeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateFabricChaincodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFabricChannelRequestOrganization(TeaModel):
    def __init__(
        self,
        id: str = None,
    ):
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class CreateFabricChannelRequest(TeaModel):
    def __init__(
        self,
        consortium_id: str = None,
        channel_name: str = None,
        batch_timeout: int = None,
        max_message_count: int = None,
        preferred_max_bytes: int = None,
        organization: List[CreateFabricChannelRequestOrganization] = None,
    ):
        self.consortium_id = consortium_id
        self.channel_name = channel_name
        self.batch_timeout = batch_timeout
        self.max_message_count = max_message_count
        self.preferred_max_bytes = preferred_max_bytes
        self.organization = organization

    def validate(self):
        if self.organization:
            for k in self.organization:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.consortium_id is not None:
            result['ConsortiumId'] = self.consortium_id
        if self.channel_name is not None:
            result['ChannelName'] = self.channel_name
        if self.batch_timeout is not None:
            result['BatchTimeout'] = self.batch_timeout
        if self.max_message_count is not None:
            result['MaxMessageCount'] = self.max_message_count
        if self.preferred_max_bytes is not None:
            result['PreferredMaxBytes'] = self.preferred_max_bytes
        result['Organization'] = []
        if self.organization is not None:
            for k in self.organization:
                result['Organization'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsortiumId') is not None:
            self.consortium_id = m.get('ConsortiumId')
        if m.get('ChannelName') is not None:
            self.channel_name = m.get('ChannelName')
        if m.get('BatchTimeout') is not None:
            self.batch_timeout = m.get('BatchTimeout')
        if m.get('MaxMessageCount') is not None:
            self.max_message_count = m.get('MaxMessageCount')
        if m.get('PreferredMaxBytes') is not None:
            self.preferred_max_bytes = m.get('PreferredMaxBytes')
        self.organization = []
        if m.get('Organization') is not None:
            for k in m.get('Organization'):
                temp_model = CreateFabricChannelRequestOrganization()
                self.organization.append(temp_model.from_map(k))
        return self


class CreateFabricChannelResponseBodyResult(TeaModel):
    def __init__(
        self,
        batch_timeout: int = None,
        update_time: str = None,
        chaincode_count: int = None,
        state: str = None,
        preferred_max_bytes: int = None,
        create_time: str = None,
        owner_name: str = None,
        owner_uid: int = None,
        owner_bid: str = None,
        max_message_count: int = None,
        member_count: int = None,
        request_id: str = None,
        consortium_id: str = None,
        channel_name: str = None,
        support_config: bool = None,
        channel_id: str = None,
        consortium_name: str = None,
        block_count: int = None,
    ):
        self.batch_timeout = batch_timeout
        self.update_time = update_time
        self.chaincode_count = chaincode_count
        self.state = state
        self.preferred_max_bytes = preferred_max_bytes
        self.create_time = create_time
        self.owner_name = owner_name
        self.owner_uid = owner_uid
        self.owner_bid = owner_bid
        self.max_message_count = max_message_count
        self.member_count = member_count
        self.request_id = request_id
        self.consortium_id = consortium_id
        self.channel_name = channel_name
        self.support_config = support_config
        self.channel_id = channel_id
        self.consortium_name = consortium_name
        self.block_count = block_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.batch_timeout is not None:
            result['BatchTimeout'] = self.batch_timeout
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.chaincode_count is not None:
            result['ChaincodeCount'] = self.chaincode_count
        if self.state is not None:
            result['State'] = self.state
        if self.preferred_max_bytes is not None:
            result['PreferredMaxBytes'] = self.preferred_max_bytes
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.owner_name is not None:
            result['OwnerName'] = self.owner_name
        if self.owner_uid is not None:
            result['OwnerUid'] = self.owner_uid
        if self.owner_bid is not None:
            result['OwnerBid'] = self.owner_bid
        if self.max_message_count is not None:
            result['MaxMessageCount'] = self.max_message_count
        if self.member_count is not None:
            result['MemberCount'] = self.member_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.consortium_id is not None:
            result['ConsortiumId'] = self.consortium_id
        if self.channel_name is not None:
            result['ChannelName'] = self.channel_name
        if self.support_config is not None:
            result['SupportConfig'] = self.support_config
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.consortium_name is not None:
            result['ConsortiumName'] = self.consortium_name
        if self.block_count is not None:
            result['BlockCount'] = self.block_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BatchTimeout') is not None:
            self.batch_timeout = m.get('BatchTimeout')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('ChaincodeCount') is not None:
            self.chaincode_count = m.get('ChaincodeCount')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('PreferredMaxBytes') is not None:
            self.preferred_max_bytes = m.get('PreferredMaxBytes')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('OwnerName') is not None:
            self.owner_name = m.get('OwnerName')
        if m.get('OwnerUid') is not None:
            self.owner_uid = m.get('OwnerUid')
        if m.get('OwnerBid') is not None:
            self.owner_bid = m.get('OwnerBid')
        if m.get('MaxMessageCount') is not None:
            self.max_message_count = m.get('MaxMessageCount')
        if m.get('MemberCount') is not None:
            self.member_count = m.get('MemberCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ConsortiumId') is not None:
            self.consortium_id = m.get('ConsortiumId')
        if m.get('ChannelName') is not None:
            self.channel_name = m.get('ChannelName')
        if m.get('SupportConfig') is not None:
            self.support_config = m.get('SupportConfig')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('ConsortiumName') is not None:
            self.consortium_name = m.get('ConsortiumName')
        if m.get('BlockCount') is not None:
            self.block_count = m.get('BlockCount')
        return self


class CreateFabricChannelResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_code: int = None,
        success: bool = None,
        result: CreateFabricChannelResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.error_code = error_code
        self.success = success
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Result') is not None:
            temp_model = CreateFabricChannelResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class CreateFabricChannelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateFabricChannelResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateFabricChannelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFabricChannelMemberRequestOrganization(TeaModel):
    def __init__(
        self,
        organization_id: str = None,
    ):
        self.organization_id = organization_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class CreateFabricChannelMemberRequest(TeaModel):
    def __init__(
        self,
        channel_id: str = None,
        organization: List[CreateFabricChannelMemberRequestOrganization] = None,
    ):
        self.channel_id = channel_id
        self.organization = organization

    def validate(self):
        if self.organization:
            for k in self.organization:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        result['Organization'] = []
        if self.organization is not None:
            for k in self.organization:
                result['Organization'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        self.organization = []
        if m.get('Organization') is not None:
            for k in m.get('Organization'):
                temp_model = CreateFabricChannelMemberRequestOrganization()
                self.organization.append(temp_model.from_map(k))
        return self


class CreateFabricChannelMemberResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_code: int = None,
        success: bool = None,
        result: bool = None,
    ):
        self.request_id = request_id
        self.error_code = error_code
        self.success = success
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class CreateFabricChannelMemberResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateFabricChannelMemberResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateFabricChannelMemberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFabricConsortiumRequestOrganization(TeaModel):
    def __init__(
        self,
        organization_id: str = None,
    ):
        self.organization_id = organization_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class CreateFabricConsortiumRequest(TeaModel):
    def __init__(
        self,
        location: str = None,
        orderer_type: str = None,
        zone_id: str = None,
        consortium_name: str = None,
        domain: str = None,
        consortium_description: str = None,
        channel_policy: str = None,
        spec_name: str = None,
        orderers_count: int = None,
        peers_count: int = None,
        payment_duration_unit: str = None,
        payment_duration: int = None,
        organization: List[CreateFabricConsortiumRequestOrganization] = None,
    ):
        self.location = location
        self.orderer_type = orderer_type
        self.zone_id = zone_id
        self.consortium_name = consortium_name
        self.domain = domain
        self.consortium_description = consortium_description
        self.channel_policy = channel_policy
        self.spec_name = spec_name
        self.orderers_count = orderers_count
        self.peers_count = peers_count
        self.payment_duration_unit = payment_duration_unit
        self.payment_duration = payment_duration
        self.organization = organization

    def validate(self):
        if self.organization:
            for k in self.organization:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.location is not None:
            result['Location'] = self.location
        if self.orderer_type is not None:
            result['OrdererType'] = self.orderer_type
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.consortium_name is not None:
            result['ConsortiumName'] = self.consortium_name
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.consortium_description is not None:
            result['ConsortiumDescription'] = self.consortium_description
        if self.channel_policy is not None:
            result['ChannelPolicy'] = self.channel_policy
        if self.spec_name is not None:
            result['SpecName'] = self.spec_name
        if self.orderers_count is not None:
            result['OrderersCount'] = self.orderers_count
        if self.peers_count is not None:
            result['PeersCount'] = self.peers_count
        if self.payment_duration_unit is not None:
            result['PaymentDurationUnit'] = self.payment_duration_unit
        if self.payment_duration is not None:
            result['PaymentDuration'] = self.payment_duration
        result['Organization'] = []
        if self.organization is not None:
            for k in self.organization:
                result['Organization'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('OrdererType') is not None:
            self.orderer_type = m.get('OrdererType')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('ConsortiumName') is not None:
            self.consortium_name = m.get('ConsortiumName')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('ConsortiumDescription') is not None:
            self.consortium_description = m.get('ConsortiumDescription')
        if m.get('ChannelPolicy') is not None:
            self.channel_policy = m.get('ChannelPolicy')
        if m.get('SpecName') is not None:
            self.spec_name = m.get('SpecName')
        if m.get('OrderersCount') is not None:
            self.orderers_count = m.get('OrderersCount')
        if m.get('PeersCount') is not None:
            self.peers_count = m.get('PeersCount')
        if m.get('PaymentDurationUnit') is not None:
            self.payment_duration_unit = m.get('PaymentDurationUnit')
        if m.get('PaymentDuration') is not None:
            self.payment_duration = m.get('PaymentDuration')
        self.organization = []
        if m.get('Organization') is not None:
            for k in m.get('Organization'):
                temp_model = CreateFabricConsortiumRequestOrganization()
                self.organization.append(temp_model.from_map(k))
        return self


class CreateFabricConsortiumResponseBodyResult(TeaModel):
    def __init__(
        self,
        channel_count: int = None,
        domain: str = None,
        create_time: str = None,
        spec_name: str = None,
        orderer_count: int = None,
        service_state: str = None,
        owner_uid: int = None,
        cluster_state: str = None,
        code_name: str = None,
        owner_bid: str = None,
        region_id: str = None,
        member_count: int = None,
        channel_policy: str = None,
        orderer_type: str = None,
        description: str = None,
        consortium_id: str = None,
        zone_id: str = None,
        consortium_name: str = None,
    ):
        self.channel_count = channel_count
        self.domain = domain
        self.create_time = create_time
        self.spec_name = spec_name
        self.orderer_count = orderer_count
        self.service_state = service_state
        self.owner_uid = owner_uid
        self.cluster_state = cluster_state
        self.code_name = code_name
        self.owner_bid = owner_bid
        self.region_id = region_id
        self.member_count = member_count
        self.channel_policy = channel_policy
        self.orderer_type = orderer_type
        self.description = description
        self.consortium_id = consortium_id
        self.zone_id = zone_id
        self.consortium_name = consortium_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.channel_count is not None:
            result['ChannelCount'] = self.channel_count
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.spec_name is not None:
            result['SpecName'] = self.spec_name
        if self.orderer_count is not None:
            result['OrdererCount'] = self.orderer_count
        if self.service_state is not None:
            result['ServiceState'] = self.service_state
        if self.owner_uid is not None:
            result['OwnerUid'] = self.owner_uid
        if self.cluster_state is not None:
            result['ClusterState'] = self.cluster_state
        if self.code_name is not None:
            result['CodeName'] = self.code_name
        if self.owner_bid is not None:
            result['OwnerBid'] = self.owner_bid
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.member_count is not None:
            result['MemberCount'] = self.member_count
        if self.channel_policy is not None:
            result['ChannelPolicy'] = self.channel_policy
        if self.orderer_type is not None:
            result['OrdererType'] = self.orderer_type
        if self.description is not None:
            result['Description'] = self.description
        if self.consortium_id is not None:
            result['ConsortiumId'] = self.consortium_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.consortium_name is not None:
            result['ConsortiumName'] = self.consortium_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChannelCount') is not None:
            self.channel_count = m.get('ChannelCount')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('SpecName') is not None:
            self.spec_name = m.get('SpecName')
        if m.get('OrdererCount') is not None:
            self.orderer_count = m.get('OrdererCount')
        if m.get('ServiceState') is not None:
            self.service_state = m.get('ServiceState')
        if m.get('OwnerUid') is not None:
            self.owner_uid = m.get('OwnerUid')
        if m.get('ClusterState') is not None:
            self.cluster_state = m.get('ClusterState')
        if m.get('CodeName') is not None:
            self.code_name = m.get('CodeName')
        if m.get('OwnerBid') is not None:
            self.owner_bid = m.get('OwnerBid')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('MemberCount') is not None:
            self.member_count = m.get('MemberCount')
        if m.get('ChannelPolicy') is not None:
            self.channel_policy = m.get('ChannelPolicy')
        if m.get('OrdererType') is not None:
            self.orderer_type = m.get('OrdererType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ConsortiumId') is not None:
            self.consortium_id = m.get('ConsortiumId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('ConsortiumName') is not None:
            self.consortium_name = m.get('ConsortiumName')
        return self


class CreateFabricConsortiumResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_code: int = None,
        success: bool = None,
        result: CreateFabricConsortiumResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.error_code = error_code
        self.success = success
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Result') is not None:
            temp_model = CreateFabricConsortiumResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class CreateFabricConsortiumResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateFabricConsortiumResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateFabricConsortiumResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFabricConsortiumMemberRequestOrganization(TeaModel):
    def __init__(
        self,
        organization_id: str = None,
    ):
        self.organization_id = organization_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class CreateFabricConsortiumMemberRequest(TeaModel):
    def __init__(
        self,
        consortium_id: str = None,
        code: str = None,
        organization: List[CreateFabricConsortiumMemberRequestOrganization] = None,
    ):
        self.consortium_id = consortium_id
        self.code = code
        self.organization = organization

    def validate(self):
        if self.organization:
            for k in self.organization:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.consortium_id is not None:
            result['ConsortiumId'] = self.consortium_id
        if self.code is not None:
            result['Code'] = self.code
        result['Organization'] = []
        if self.organization is not None:
            for k in self.organization:
                result['Organization'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsortiumId') is not None:
            self.consortium_id = m.get('ConsortiumId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.organization = []
        if m.get('Organization') is not None:
            for k in m.get('Organization'):
                temp_model = CreateFabricConsortiumMemberRequestOrganization()
                self.organization.append(temp_model.from_map(k))
        return self


class CreateFabricConsortiumMemberResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_code: int = None,
        success: bool = None,
        result: bool = None,
    ):
        self.request_id = request_id
        self.error_code = error_code
        self.success = success
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class CreateFabricConsortiumMemberResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateFabricConsortiumMemberResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateFabricConsortiumMemberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFabricOrganizationRequest(TeaModel):
    def __init__(
        self,
        organization_name: str = None,
        location: str = None,
        domain: str = None,
        description: str = None,
        spec_name: str = None,
        peers_count: int = None,
        payment_duration: int = None,
        payment_duration_unit: str = None,
    ):
        self.organization_name = organization_name
        self.location = location
        self.domain = domain
        self.description = description
        self.spec_name = spec_name
        self.peers_count = peers_count
        self.payment_duration = payment_duration
        self.payment_duration_unit = payment_duration_unit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.organization_name is not None:
            result['OrganizationName'] = self.organization_name
        if self.location is not None:
            result['Location'] = self.location
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.description is not None:
            result['Description'] = self.description
        if self.spec_name is not None:
            result['SpecName'] = self.spec_name
        if self.peers_count is not None:
            result['PeersCount'] = self.peers_count
        if self.payment_duration is not None:
            result['PaymentDuration'] = self.payment_duration
        if self.payment_duration_unit is not None:
            result['PaymentDurationUnit'] = self.payment_duration_unit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrganizationName') is not None:
            self.organization_name = m.get('OrganizationName')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('SpecName') is not None:
            self.spec_name = m.get('SpecName')
        if m.get('PeersCount') is not None:
            self.peers_count = m.get('PeersCount')
        if m.get('PaymentDuration') is not None:
            self.payment_duration = m.get('PaymentDuration')
        if m.get('PaymentDurationUnit') is not None:
            self.payment_duration_unit = m.get('PaymentDurationUnit')
        return self


class CreateFabricOrganizationResponseBodyResult(TeaModel):
    def __init__(
        self,
        domain: str = None,
        peer_count: int = None,
        create_time: str = None,
        consortium_count: int = None,
        spec_name: str = None,
        owner_name: str = None,
        service_state: str = None,
        owner_uid: int = None,
        cluster_state: str = None,
        code_name: str = None,
        owner_bid: str = None,
        organization_description: str = None,
        region_id: str = None,
        organization_id: str = None,
        request_id: str = None,
        zone_id: str = None,
        user_count: int = None,
        organization_name: str = None,
    ):
        self.domain = domain
        self.peer_count = peer_count
        self.create_time = create_time
        self.consortium_count = consortium_count
        self.spec_name = spec_name
        self.owner_name = owner_name
        self.service_state = service_state
        self.owner_uid = owner_uid
        self.cluster_state = cluster_state
        self.code_name = code_name
        self.owner_bid = owner_bid
        self.organization_description = organization_description
        self.region_id = region_id
        self.organization_id = organization_id
        self.request_id = request_id
        self.zone_id = zone_id
        self.user_count = user_count
        self.organization_name = organization_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.peer_count is not None:
            result['PeerCount'] = self.peer_count
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.consortium_count is not None:
            result['ConsortiumCount'] = self.consortium_count
        if self.spec_name is not None:
            result['SpecName'] = self.spec_name
        if self.owner_name is not None:
            result['OwnerName'] = self.owner_name
        if self.service_state is not None:
            result['ServiceState'] = self.service_state
        if self.owner_uid is not None:
            result['OwnerUid'] = self.owner_uid
        if self.cluster_state is not None:
            result['ClusterState'] = self.cluster_state
        if self.code_name is not None:
            result['CodeName'] = self.code_name
        if self.owner_bid is not None:
            result['OwnerBid'] = self.owner_bid
        if self.organization_description is not None:
            result['OrganizationDescription'] = self.organization_description
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.user_count is not None:
            result['UserCount'] = self.user_count
        if self.organization_name is not None:
            result['OrganizationName'] = self.organization_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('PeerCount') is not None:
            self.peer_count = m.get('PeerCount')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ConsortiumCount') is not None:
            self.consortium_count = m.get('ConsortiumCount')
        if m.get('SpecName') is not None:
            self.spec_name = m.get('SpecName')
        if m.get('OwnerName') is not None:
            self.owner_name = m.get('OwnerName')
        if m.get('ServiceState') is not None:
            self.service_state = m.get('ServiceState')
        if m.get('OwnerUid') is not None:
            self.owner_uid = m.get('OwnerUid')
        if m.get('ClusterState') is not None:
            self.cluster_state = m.get('ClusterState')
        if m.get('CodeName') is not None:
            self.code_name = m.get('CodeName')
        if m.get('OwnerBid') is not None:
            self.owner_bid = m.get('OwnerBid')
        if m.get('OrganizationDescription') is not None:
            self.organization_description = m.get('OrganizationDescription')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('UserCount') is not None:
            self.user_count = m.get('UserCount')
        if m.get('OrganizationName') is not None:
            self.organization_name = m.get('OrganizationName')
        return self


class CreateFabricOrganizationResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_code: int = None,
        success: bool = None,
        result: CreateFabricOrganizationResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.error_code = error_code
        self.success = success
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Result') is not None:
            temp_model = CreateFabricOrganizationResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class CreateFabricOrganizationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateFabricOrganizationResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateFabricOrganizationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFabricOrganizationUserRequest(TeaModel):
    def __init__(
        self,
        organization_id: str = None,
        username: str = None,
        password: str = None,
        attrs: str = None,
    ):
        self.organization_id = organization_id
        self.username = username
        self.password = password
        self.attrs = attrs

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.username is not None:
            result['Username'] = self.username
        if self.password is not None:
            result['Password'] = self.password
        if self.attrs is not None:
            result['Attrs'] = self.attrs
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('Attrs') is not None:
            self.attrs = m.get('Attrs')
        return self


class CreateFabricOrganizationUserResponseBodyResult(TeaModel):
    def __init__(
        self,
        password: str = None,
        expire_time: str = None,
        create_time: str = None,
        organization_id: str = None,
        username: str = None,
        fullname: str = None,
    ):
        self.password = password
        self.expire_time = expire_time
        self.create_time = create_time
        self.organization_id = organization_id
        self.username = username
        self.fullname = fullname

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.password is not None:
            result['Password'] = self.password
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.username is not None:
            result['Username'] = self.username
        if self.fullname is not None:
            result['Fullname'] = self.fullname
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        if m.get('Fullname') is not None:
            self.fullname = m.get('Fullname')
        return self


class CreateFabricOrganizationUserResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_code: int = None,
        success: bool = None,
        result: CreateFabricOrganizationUserResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.error_code = error_code
        self.success = success
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Result') is not None:
            temp_model = CreateFabricOrganizationUserResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class CreateFabricOrganizationUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateFabricOrganizationUserResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateFabricOrganizationUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAntChainConsortiumRequest(TeaModel):
    def __init__(
        self,
        consortium_id: str = None,
    ):
        self.consortium_id = consortium_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.consortium_id is not None:
            result['ConsortiumId'] = self.consortium_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsortiumId') is not None:
            self.consortium_id = m.get('ConsortiumId')
        return self


class DeleteAntChainConsortiumResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: str = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class DeleteAntChainConsortiumResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteAntChainConsortiumResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteAntChainConsortiumResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAntChainContractContentRequest(TeaModel):
    def __init__(
        self,
        content_id: str = None,
    ):
        self.content_id = content_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.content_id is not None:
            result['ContentId'] = self.content_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContentId') is not None:
            self.content_id = m.get('ContentId')
        return self


class DeleteAntChainContractContentResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: str = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class DeleteAntChainContractContentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteAntChainContractContentResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteAntChainContractContentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAntChainContractProjectRequest(TeaModel):
    def __init__(
        self,
        project_id: str = None,
    ):
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class DeleteAntChainContractProjectResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: str = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class DeleteAntChainContractProjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteAntChainContractProjectResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteAntChainContractProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAntChainMiniAppQRCodeAuthorizedUserRequest(TeaModel):
    def __init__(
        self,
        ant_chain_id: str = None,
        phone: str = None,
    ):
        self.ant_chain_id = ant_chain_id
        self.phone = phone

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.ant_chain_id is not None:
            result['AntChainId'] = self.ant_chain_id
        if self.phone is not None:
            result['Phone'] = self.phone
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AntChainId') is not None:
            self.ant_chain_id = m.get('AntChainId')
        if m.get('Phone') is not None:
            self.phone = m.get('Phone')
        return self


class DeleteAntChainMiniAppQRCodeAuthorizedUserResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: str = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class DeleteAntChainMiniAppQRCodeAuthorizedUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteAntChainMiniAppQRCodeAuthorizedUserResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteAntChainMiniAppQRCodeAuthorizedUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteFabricChaincodeRequest(TeaModel):
    def __init__(
        self,
        chaincode_id: str = None,
    ):
        self.chaincode_id = chaincode_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.chaincode_id is not None:
            result['ChaincodeId'] = self.chaincode_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChaincodeId') is not None:
            self.chaincode_id = m.get('ChaincodeId')
        return self


class DeleteFabricChaincodeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_code: int = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.error_code = error_code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteFabricChaincodeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteFabricChaincodeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteFabricChaincodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAntChainAccountsRequest(TeaModel):
    def __init__(
        self,
        page_size: int = None,
        page_number: int = None,
        ant_chain_id: str = None,
    ):
        self.page_size = page_size
        self.page_number = page_number
        self.ant_chain_id = ant_chain_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.ant_chain_id is not None:
            result['AntChainId'] = self.ant_chain_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('AntChainId') is not None:
            self.ant_chain_id = m.get('AntChainId')
        return self


class DescribeAntChainAccountsResponseBodyResultPagination(TeaModel):
    def __init__(
        self,
        page_size: int = None,
        page_number: int = None,
        total_count: int = None,
    ):
        self.page_size = page_size
        self.page_number = page_number
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeAntChainAccountsResponseBodyResultAccounts(TeaModel):
    def __init__(
        self,
        account_public_key: str = None,
        account: str = None,
        account_status: str = None,
        account_recovery_key: str = None,
        ant_chain_id: str = None,
    ):
        self.account_public_key = account_public_key
        self.account = account
        self.account_status = account_status
        self.account_recovery_key = account_recovery_key
        self.ant_chain_id = ant_chain_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.account_public_key is not None:
            result['AccountPublicKey'] = self.account_public_key
        if self.account is not None:
            result['Account'] = self.account
        if self.account_status is not None:
            result['AccountStatus'] = self.account_status
        if self.account_recovery_key is not None:
            result['AccountRecoveryKey'] = self.account_recovery_key
        if self.ant_chain_id is not None:
            result['AntChainId'] = self.ant_chain_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountPublicKey') is not None:
            self.account_public_key = m.get('AccountPublicKey')
        if m.get('Account') is not None:
            self.account = m.get('Account')
        if m.get('AccountStatus') is not None:
            self.account_status = m.get('AccountStatus')
        if m.get('AccountRecoveryKey') is not None:
            self.account_recovery_key = m.get('AccountRecoveryKey')
        if m.get('AntChainId') is not None:
            self.ant_chain_id = m.get('AntChainId')
        return self


class DescribeAntChainAccountsResponseBodyResult(TeaModel):
    def __init__(
        self,
        pagination: DescribeAntChainAccountsResponseBodyResultPagination = None,
        accounts: List[DescribeAntChainAccountsResponseBodyResultAccounts] = None,
    ):
        self.pagination = pagination
        self.accounts = accounts

    def validate(self):
        if self.pagination:
            self.pagination.validate()
        if self.accounts:
            for k in self.accounts:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.pagination is not None:
            result['Pagination'] = self.pagination.to_map()
        result['Accounts'] = []
        if self.accounts is not None:
            for k in self.accounts:
                result['Accounts'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Pagination') is not None:
            temp_model = DescribeAntChainAccountsResponseBodyResultPagination()
            self.pagination = temp_model.from_map(m['Pagination'])
        self.accounts = []
        if m.get('Accounts') is not None:
            for k in m.get('Accounts'):
                temp_model = DescribeAntChainAccountsResponseBodyResultAccounts()
                self.accounts.append(temp_model.from_map(k))
        return self


class DescribeAntChainAccountsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: DescribeAntChainAccountsResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = DescribeAntChainAccountsResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class DescribeAntChainAccountsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeAntChainAccountsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeAntChainAccountsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAntChainBlockRequest(TeaModel):
    def __init__(
        self,
        ant_chain_id: str = None,
        height: int = None,
    ):
        self.ant_chain_id = ant_chain_id
        self.height = height

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.ant_chain_id is not None:
            result['AntChainId'] = self.ant_chain_id
        if self.height is not None:
            result['Height'] = self.height
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AntChainId') is not None:
            self.ant_chain_id = m.get('AntChainId')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        return self


class DescribeAntChainBlockResponseBodyResult(TeaModel):
    def __init__(
        self,
        previous_hash: str = None,
        version: int = None,
        transaction_size: int = None,
        create_time: int = None,
        root_tx_hash: str = None,
        height: int = None,
        block_hash: str = None,
        ant_chain_id: str = None,
        trans_summary_list: str = None,
    ):
        self.previous_hash = previous_hash
        self.version = version
        self.transaction_size = transaction_size
        self.create_time = create_time
        self.root_tx_hash = root_tx_hash
        self.height = height
        self.block_hash = block_hash
        self.ant_chain_id = ant_chain_id
        self.trans_summary_list = trans_summary_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.previous_hash is not None:
            result['PreviousHash'] = self.previous_hash
        if self.version is not None:
            result['Version'] = self.version
        if self.transaction_size is not None:
            result['TransactionSize'] = self.transaction_size
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.root_tx_hash is not None:
            result['RootTxHash'] = self.root_tx_hash
        if self.height is not None:
            result['Height'] = self.height
        if self.block_hash is not None:
            result['BlockHash'] = self.block_hash
        if self.ant_chain_id is not None:
            result['AntChainId'] = self.ant_chain_id
        if self.trans_summary_list is not None:
            result['TransSummaryList'] = self.trans_summary_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PreviousHash') is not None:
            self.previous_hash = m.get('PreviousHash')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('TransactionSize') is not None:
            self.transaction_size = m.get('TransactionSize')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('RootTxHash') is not None:
            self.root_tx_hash = m.get('RootTxHash')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('BlockHash') is not None:
            self.block_hash = m.get('BlockHash')
        if m.get('AntChainId') is not None:
            self.ant_chain_id = m.get('AntChainId')
        if m.get('TransSummaryList') is not None:
            self.trans_summary_list = m.get('TransSummaryList')
        return self


class DescribeAntChainBlockResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: DescribeAntChainBlockResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = DescribeAntChainBlockResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class DescribeAntChainBlockResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeAntChainBlockResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeAntChainBlockResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAntChainCertificateApplicationsRequest(TeaModel):
    def __init__(
        self,
        ant_chain_id: str = None,
        status: str = None,
        page_size: int = None,
        page_number: int = None,
    ):
        self.ant_chain_id = ant_chain_id
        self.status = status
        self.page_size = page_size
        self.page_number = page_number

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.ant_chain_id is not None:
            result['AntChainId'] = self.ant_chain_id
        if self.status is not None:
            result['Status'] = self.status
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AntChainId') is not None:
            self.ant_chain_id = m.get('AntChainId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        return self


class DescribeAntChainCertificateApplicationsResponseBodyResultPagination(TeaModel):
    def __init__(
        self,
        page_size: int = None,
        page_number: int = None,
        total_count: int = None,
    ):
        self.page_size = page_size
        self.page_number = page_number
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeAntChainCertificateApplicationsResponseBodyResultCertificateApplications(TeaModel):
    def __init__(
        self,
        status: str = None,
        updatetime: int = None,
        createtime: int = None,
        bid: str = None,
        ant_chain_id: str = None,
        username: str = None,
    ):
        self.status = status
        self.updatetime = updatetime
        self.createtime = createtime
        self.bid = bid
        self.ant_chain_id = ant_chain_id
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.updatetime is not None:
            result['Updatetime'] = self.updatetime
        if self.createtime is not None:
            result['Createtime'] = self.createtime
        if self.bid is not None:
            result['Bid'] = self.bid
        if self.ant_chain_id is not None:
            result['AntChainId'] = self.ant_chain_id
        if self.username is not None:
            result['Username'] = self.username
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Updatetime') is not None:
            self.updatetime = m.get('Updatetime')
        if m.get('Createtime') is not None:
            self.createtime = m.get('Createtime')
        if m.get('Bid') is not None:
            self.bid = m.get('Bid')
        if m.get('AntChainId') is not None:
            self.ant_chain_id = m.get('AntChainId')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        return self


class DescribeAntChainCertificateApplicationsResponseBodyResult(TeaModel):
    def __init__(
        self,
        pagination: DescribeAntChainCertificateApplicationsResponseBodyResultPagination = None,
        certificate_applications: List[DescribeAntChainCertificateApplicationsResponseBodyResultCertificateApplications] = None,
    ):
        self.pagination = pagination
        self.certificate_applications = certificate_applications

    def validate(self):
        if self.pagination:
            self.pagination.validate()
        if self.certificate_applications:
            for k in self.certificate_applications:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.pagination is not None:
            result['Pagination'] = self.pagination.to_map()
        result['CertificateApplications'] = []
        if self.certificate_applications is not None:
            for k in self.certificate_applications:
                result['CertificateApplications'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Pagination') is not None:
            temp_model = DescribeAntChainCertificateApplicationsResponseBodyResultPagination()
            self.pagination = temp_model.from_map(m['Pagination'])
        self.certificate_applications = []
        if m.get('CertificateApplications') is not None:
            for k in m.get('CertificateApplications'):
                temp_model = DescribeAntChainCertificateApplicationsResponseBodyResultCertificateApplications()
                self.certificate_applications.append(temp_model.from_map(k))
        return self


class DescribeAntChainCertificateApplicationsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: DescribeAntChainCertificateApplicationsResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = DescribeAntChainCertificateApplicationsResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class DescribeAntChainCertificateApplicationsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeAntChainCertificateApplicationsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeAntChainCertificateApplicationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAntChainConsortiumsRequest(TeaModel):
    def __init__(
        self,
        page_size: int = None,
        page_number: int = None,
    ):
        self.page_size = page_size
        self.page_number = page_number

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        return self


class DescribeAntChainConsortiumsResponseBodyResultAntConsortiums(TeaModel):
    def __init__(
        self,
        consortium_description: str = None,
        status: str = None,
        consortium_id: str = None,
        create_time: int = None,
        member_num: int = None,
        role: str = None,
        consortium_name: str = None,
        chain_num: int = None,
    ):
        self.consortium_description = consortium_description
        self.status = status
        self.consortium_id = consortium_id
        self.create_time = create_time
        self.member_num = member_num
        self.role = role
        self.consortium_name = consortium_name
        self.chain_num = chain_num

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.consortium_description is not None:
            result['ConsortiumDescription'] = self.consortium_description
        if self.status is not None:
            result['Status'] = self.status
        if self.consortium_id is not None:
            result['ConsortiumId'] = self.consortium_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.member_num is not None:
            result['MemberNum'] = self.member_num
        if self.role is not None:
            result['Role'] = self.role
        if self.consortium_name is not None:
            result['ConsortiumName'] = self.consortium_name
        if self.chain_num is not None:
            result['ChainNum'] = self.chain_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsortiumDescription') is not None:
            self.consortium_description = m.get('ConsortiumDescription')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ConsortiumId') is not None:
            self.consortium_id = m.get('ConsortiumId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('MemberNum') is not None:
            self.member_num = m.get('MemberNum')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('ConsortiumName') is not None:
            self.consortium_name = m.get('ConsortiumName')
        if m.get('ChainNum') is not None:
            self.chain_num = m.get('ChainNum')
        return self


class DescribeAntChainConsortiumsResponseBodyResultPagination(TeaModel):
    def __init__(
        self,
        page_size: int = None,
        page_number: int = None,
        total_count: int = None,
    ):
        self.page_size = page_size
        self.page_number = page_number
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeAntChainConsortiumsResponseBodyResult(TeaModel):
    def __init__(
        self,
        ant_consortiums: List[DescribeAntChainConsortiumsResponseBodyResultAntConsortiums] = None,
        pagination: DescribeAntChainConsortiumsResponseBodyResultPagination = None,
    ):
        self.ant_consortiums = ant_consortiums
        self.pagination = pagination

    def validate(self):
        if self.ant_consortiums:
            for k in self.ant_consortiums:
                if k:
                    k.validate()
        if self.pagination:
            self.pagination.validate()

    def to_map(self):
        result = dict()
        result['AntConsortiums'] = []
        if self.ant_consortiums is not None:
            for k in self.ant_consortiums:
                result['AntConsortiums'].append(k.to_map() if k else None)
        if self.pagination is not None:
            result['Pagination'] = self.pagination.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ant_consortiums = []
        if m.get('AntConsortiums') is not None:
            for k in m.get('AntConsortiums'):
                temp_model = DescribeAntChainConsortiumsResponseBodyResultAntConsortiums()
                self.ant_consortiums.append(temp_model.from_map(k))
        if m.get('Pagination') is not None:
            temp_model = DescribeAntChainConsortiumsResponseBodyResultPagination()
            self.pagination = temp_model.from_map(m['Pagination'])
        return self


class DescribeAntChainConsortiumsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: DescribeAntChainConsortiumsResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = DescribeAntChainConsortiumsResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class DescribeAntChainConsortiumsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeAntChainConsortiumsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeAntChainConsortiumsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAntChainContractProjectContentTreeRequest(TeaModel):
    def __init__(
        self,
        project_id: str = None,
    ):
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class DescribeAntChainContractProjectContentTreeResponseBodyResult(TeaModel):
    def __init__(
        self,
        children: List[Dict[str, Any]] = None,
        project_id: str = None,
        project_name: str = None,
        project_version: str = None,
        project_description: str = None,
    ):
        self.children = children
        self.project_id = project_id
        self.project_name = project_name
        self.project_version = project_version
        self.project_description = project_description

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.children is not None:
            result['Children'] = self.children
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.project_version is not None:
            result['ProjectVersion'] = self.project_version
        if self.project_description is not None:
            result['ProjectDescription'] = self.project_description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Children') is not None:
            self.children = m.get('Children')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('ProjectVersion') is not None:
            self.project_version = m.get('ProjectVersion')
        if m.get('ProjectDescription') is not None:
            self.project_description = m.get('ProjectDescription')
        return self


class DescribeAntChainContractProjectContentTreeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: DescribeAntChainContractProjectContentTreeResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = DescribeAntChainContractProjectContentTreeResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class DescribeAntChainContractProjectContentTreeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeAntChainContractProjectContentTreeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeAntChainContractProjectContentTreeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAntChainContractProjectsRequest(TeaModel):
    def __init__(
        self,
        consortium_id: str = None,
        page_size: int = None,
        page_number: int = None,
    ):
        self.consortium_id = consortium_id
        self.page_size = page_size
        self.page_number = page_number

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.consortium_id is not None:
            result['ConsortiumId'] = self.consortium_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsortiumId') is not None:
            self.consortium_id = m.get('ConsortiumId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        return self


class DescribeAntChainContractProjectsResponseBodyResultPagination(TeaModel):
    def __init__(
        self,
        page_size: int = None,
        page_number: int = None,
        total_count: int = None,
    ):
        self.page_size = page_size
        self.page_number = page_number
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeAntChainContractProjectsResponseBodyResultContractProjects(TeaModel):
    def __init__(
        self,
        update_time: int = None,
        consortium_id: str = None,
        create_time: int = None,
        project_id: str = None,
        project_name: str = None,
        project_version: str = None,
        project_description: str = None,
    ):
        self.update_time = update_time
        self.consortium_id = consortium_id
        self.create_time = create_time
        self.project_id = project_id
        self.project_name = project_name
        self.project_version = project_version
        self.project_description = project_description

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.consortium_id is not None:
            result['ConsortiumId'] = self.consortium_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.project_version is not None:
            result['ProjectVersion'] = self.project_version
        if self.project_description is not None:
            result['ProjectDescription'] = self.project_description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('ConsortiumId') is not None:
            self.consortium_id = m.get('ConsortiumId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('ProjectVersion') is not None:
            self.project_version = m.get('ProjectVersion')
        if m.get('ProjectDescription') is not None:
            self.project_description = m.get('ProjectDescription')
        return self


class DescribeAntChainContractProjectsResponseBodyResult(TeaModel):
    def __init__(
        self,
        pagination: DescribeAntChainContractProjectsResponseBodyResultPagination = None,
        contract_projects: List[DescribeAntChainContractProjectsResponseBodyResultContractProjects] = None,
    ):
        self.pagination = pagination
        self.contract_projects = contract_projects

    def validate(self):
        if self.pagination:
            self.pagination.validate()
        if self.contract_projects:
            for k in self.contract_projects:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.pagination is not None:
            result['Pagination'] = self.pagination.to_map()
        result['ContractProjects'] = []
        if self.contract_projects is not None:
            for k in self.contract_projects:
                result['ContractProjects'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Pagination') is not None:
            temp_model = DescribeAntChainContractProjectsResponseBodyResultPagination()
            self.pagination = temp_model.from_map(m['Pagination'])
        self.contract_projects = []
        if m.get('ContractProjects') is not None:
            for k in m.get('ContractProjects'):
                temp_model = DescribeAntChainContractProjectsResponseBodyResultContractProjects()
                self.contract_projects.append(temp_model.from_map(k))
        return self


class DescribeAntChainContractProjectsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: DescribeAntChainContractProjectsResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = DescribeAntChainContractProjectsResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class DescribeAntChainContractProjectsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeAntChainContractProjectsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeAntChainContractProjectsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAntChainDownloadPathsRequest(TeaModel):
    def __init__(
        self,
        ant_chain_id: str = None,
    ):
        self.ant_chain_id = ant_chain_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.ant_chain_id is not None:
            result['AntChainId'] = self.ant_chain_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AntChainId') is not None:
            self.ant_chain_id = m.get('AntChainId')
        return self


class DescribeAntChainDownloadPathsResponseBodyResult(TeaModel):
    def __init__(
        self,
        ca_crt_url: str = None,
        sdk_url: str = None,
        client_crt_url: str = None,
        trust_ca_url: str = None,
    ):
        self.ca_crt_url = ca_crt_url
        self.sdk_url = sdk_url
        self.client_crt_url = client_crt_url
        self.trust_ca_url = trust_ca_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.ca_crt_url is not None:
            result['CaCrtUrl'] = self.ca_crt_url
        if self.sdk_url is not None:
            result['SdkUrl'] = self.sdk_url
        if self.client_crt_url is not None:
            result['ClientCrtUrl'] = self.client_crt_url
        if self.trust_ca_url is not None:
            result['TrustCaUrl'] = self.trust_ca_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CaCrtUrl') is not None:
            self.ca_crt_url = m.get('CaCrtUrl')
        if m.get('SdkUrl') is not None:
            self.sdk_url = m.get('SdkUrl')
        if m.get('ClientCrtUrl') is not None:
            self.client_crt_url = m.get('ClientCrtUrl')
        if m.get('TrustCaUrl') is not None:
            self.trust_ca_url = m.get('TrustCaUrl')
        return self


class DescribeAntChainDownloadPathsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: DescribeAntChainDownloadPathsResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = DescribeAntChainDownloadPathsResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class DescribeAntChainDownloadPathsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeAntChainDownloadPathsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeAntChainDownloadPathsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAntChainInformationRequest(TeaModel):
    def __init__(
        self,
        ant_chain_id: str = None,
    ):
        self.ant_chain_id = ant_chain_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.ant_chain_id is not None:
            result['AntChainId'] = self.ant_chain_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AntChainId') is not None:
            self.ant_chain_id = m.get('AntChainId')
        return self


class DescribeAntChainInformationResponseBodyResultNodeInfos(TeaModel):
    def __init__(
        self,
        status: bool = None,
        node_name: str = None,
        version: str = None,
        block_height: int = None,
    ):
        self.status = status
        self.node_name = node_name
        self.version = version
        self.block_height = block_height

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.node_name is not None:
            result['NodeName'] = self.node_name
        if self.version is not None:
            result['Version'] = self.version
        if self.block_height is not None:
            result['BlockHeight'] = self.block_height
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('BlockHeight') is not None:
            self.block_height = m.get('BlockHeight')
        return self


class DescribeAntChainInformationResponseBodyResult(TeaModel):
    def __init__(
        self,
        transaction_sum: int = None,
        version: str = None,
        block_height: int = None,
        create_time: int = None,
        node_number: int = None,
        abnormal_nodes: int = None,
        node_infos: List[DescribeAntChainInformationResponseBodyResultNodeInfos] = None,
        ant_chain_id: str = None,
        normal: bool = None,
    ):
        self.transaction_sum = transaction_sum
        self.version = version
        self.block_height = block_height
        self.create_time = create_time
        self.node_number = node_number
        self.abnormal_nodes = abnormal_nodes
        self.node_infos = node_infos
        self.ant_chain_id = ant_chain_id
        self.normal = normal

    def validate(self):
        if self.node_infos:
            for k in self.node_infos:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.transaction_sum is not None:
            result['TransactionSum'] = self.transaction_sum
        if self.version is not None:
            result['Version'] = self.version
        if self.block_height is not None:
            result['BlockHeight'] = self.block_height
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.node_number is not None:
            result['NodeNumber'] = self.node_number
        if self.abnormal_nodes is not None:
            result['AbnormalNodes'] = self.abnormal_nodes
        result['NodeInfos'] = []
        if self.node_infos is not None:
            for k in self.node_infos:
                result['NodeInfos'].append(k.to_map() if k else None)
        if self.ant_chain_id is not None:
            result['AntChainId'] = self.ant_chain_id
        if self.normal is not None:
            result['Normal'] = self.normal
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TransactionSum') is not None:
            self.transaction_sum = m.get('TransactionSum')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('BlockHeight') is not None:
            self.block_height = m.get('BlockHeight')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('NodeNumber') is not None:
            self.node_number = m.get('NodeNumber')
        if m.get('AbnormalNodes') is not None:
            self.abnormal_nodes = m.get('AbnormalNodes')
        self.node_infos = []
        if m.get('NodeInfos') is not None:
            for k in m.get('NodeInfos'):
                temp_model = DescribeAntChainInformationResponseBodyResultNodeInfos()
                self.node_infos.append(temp_model.from_map(k))
        if m.get('AntChainId') is not None:
            self.ant_chain_id = m.get('AntChainId')
        if m.get('Normal') is not None:
            self.normal = m.get('Normal')
        return self


class DescribeAntChainInformationResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: DescribeAntChainInformationResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = DescribeAntChainInformationResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class DescribeAntChainInformationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeAntChainInformationResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeAntChainInformationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAntChainLatestBlocksRequest(TeaModel):
    def __init__(
        self,
        ant_chain_id: str = None,
    ):
        self.ant_chain_id = ant_chain_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.ant_chain_id is not None:
            result['AntChainId'] = self.ant_chain_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AntChainId') is not None:
            self.ant_chain_id = m.get('AntChainId')
        return self


class DescribeAntChainLatestBlocksResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[Dict[str, Any]] = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class DescribeAntChainLatestBlocksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeAntChainLatestBlocksResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeAntChainLatestBlocksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAntChainLatestTransactionDigestsRequest(TeaModel):
    def __init__(
        self,
        ant_chain_id: str = None,
    ):
        self.ant_chain_id = ant_chain_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.ant_chain_id is not None:
            result['AntChainId'] = self.ant_chain_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AntChainId') is not None:
            self.ant_chain_id = m.get('AntChainId')
        return self


class DescribeAntChainLatestTransactionDigestsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[Dict[str, Any]] = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class DescribeAntChainLatestTransactionDigestsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeAntChainLatestTransactionDigestsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeAntChainLatestTransactionDigestsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAntChainMembersRequest(TeaModel):
    def __init__(
        self,
        page_size: int = None,
        page_number: int = None,
        consortium_id: str = None,
    ):
        self.page_size = page_size
        self.page_number = page_number
        self.consortium_id = consortium_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.consortium_id is not None:
            result['ConsortiumId'] = self.consortium_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('ConsortiumId') is not None:
            self.consortium_id = m.get('ConsortiumId')
        return self


class DescribeAntChainMembersResponseBodyResultMembers(TeaModel):
    def __init__(
        self,
        status: str = None,
        member_name: str = None,
        join_time: int = None,
        member_id: str = None,
        role: str = None,
    ):
        self.status = status
        self.member_name = member_name
        self.join_time = join_time
        self.member_id = member_id
        self.role = role

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.member_name is not None:
            result['MemberName'] = self.member_name
        if self.join_time is not None:
            result['JoinTime'] = self.join_time
        if self.member_id is not None:
            result['MemberId'] = self.member_id
        if self.role is not None:
            result['Role'] = self.role
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('MemberName') is not None:
            self.member_name = m.get('MemberName')
        if m.get('JoinTime') is not None:
            self.join_time = m.get('JoinTime')
        if m.get('MemberId') is not None:
            self.member_id = m.get('MemberId')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        return self


class DescribeAntChainMembersResponseBodyResultPagination(TeaModel):
    def __init__(
        self,
        page_size: int = None,
        page_number: int = None,
        total_count: int = None,
    ):
        self.page_size = page_size
        self.page_number = page_number
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeAntChainMembersResponseBodyResult(TeaModel):
    def __init__(
        self,
        members: List[DescribeAntChainMembersResponseBodyResultMembers] = None,
        pagination: DescribeAntChainMembersResponseBodyResultPagination = None,
    ):
        self.members = members
        self.pagination = pagination

    def validate(self):
        if self.members:
            for k in self.members:
                if k:
                    k.validate()
        if self.pagination:
            self.pagination.validate()

    def to_map(self):
        result = dict()
        result['Members'] = []
        if self.members is not None:
            for k in self.members:
                result['Members'].append(k.to_map() if k else None)
        if self.pagination is not None:
            result['Pagination'] = self.pagination.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.members = []
        if m.get('Members') is not None:
            for k in m.get('Members'):
                temp_model = DescribeAntChainMembersResponseBodyResultMembers()
                self.members.append(temp_model.from_map(k))
        if m.get('Pagination') is not None:
            temp_model = DescribeAntChainMembersResponseBodyResultPagination()
            self.pagination = temp_model.from_map(m['Pagination'])
        return self


class DescribeAntChainMembersResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: DescribeAntChainMembersResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = DescribeAntChainMembersResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class DescribeAntChainMembersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeAntChainMembersResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeAntChainMembersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAntChainMiniAppBrowserQRCodeAccessLogRequest(TeaModel):
    def __init__(
        self,
        ant_chain_id: str = None,
        qrcode_type: str = None,
    ):
        self.ant_chain_id = ant_chain_id
        self.qrcode_type = qrcode_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.ant_chain_id is not None:
            result['AntChainId'] = self.ant_chain_id
        if self.qrcode_type is not None:
            result['QRCodeType'] = self.qrcode_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AntChainId') is not None:
            self.ant_chain_id = m.get('AntChainId')
        if m.get('QRCodeType') is not None:
            self.qrcode_type = m.get('QRCodeType')
        return self


class DescribeAntChainMiniAppBrowserQRCodeAccessLogResponseBodyResult(TeaModel):
    def __init__(
        self,
        access_count: int = None,
        access_alipay_account_count: int = None,
    ):
        self.access_count = access_count
        self.access_alipay_account_count = access_alipay_account_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.access_count is not None:
            result['AccessCount'] = self.access_count
        if self.access_alipay_account_count is not None:
            result['AccessAlipayAccountCount'] = self.access_alipay_account_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessCount') is not None:
            self.access_count = m.get('AccessCount')
        if m.get('AccessAlipayAccountCount') is not None:
            self.access_alipay_account_count = m.get('AccessAlipayAccountCount')
        return self


class DescribeAntChainMiniAppBrowserQRCodeAccessLogResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: DescribeAntChainMiniAppBrowserQRCodeAccessLogResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = DescribeAntChainMiniAppBrowserQRCodeAccessLogResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class DescribeAntChainMiniAppBrowserQRCodeAccessLogResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeAntChainMiniAppBrowserQRCodeAccessLogResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeAntChainMiniAppBrowserQRCodeAccessLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAntChainMiniAppBrowserQRCodeAuthorizedUsersRequest(TeaModel):
    def __init__(
        self,
        ant_chain_id: str = None,
        qrcode_type: str = None,
        page_size: int = None,
        page_number: int = None,
    ):
        self.ant_chain_id = ant_chain_id
        self.qrcode_type = qrcode_type
        self.page_size = page_size
        self.page_number = page_number

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.ant_chain_id is not None:
            result['AntChainId'] = self.ant_chain_id
        if self.qrcode_type is not None:
            result['QRCodeType'] = self.qrcode_type
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AntChainId') is not None:
            self.ant_chain_id = m.get('AntChainId')
        if m.get('QRCodeType') is not None:
            self.qrcode_type = m.get('QRCodeType')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        return self


class DescribeAntChainMiniAppBrowserQRCodeAuthorizedUsersResponseBodyResultPagination(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeAntChainMiniAppBrowserQRCodeAuthorizedUsersResponseBodyResultAuthorizedUserList(TeaModel):
    def __init__(
        self,
        gmt_authorized: str = None,
        phone: str = None,
    ):
        self.gmt_authorized = gmt_authorized
        self.phone = phone

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.gmt_authorized is not None:
            result['GmtAuthorized'] = self.gmt_authorized
        if self.phone is not None:
            result['Phone'] = self.phone
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtAuthorized') is not None:
            self.gmt_authorized = m.get('GmtAuthorized')
        if m.get('Phone') is not None:
            self.phone = m.get('Phone')
        return self


class DescribeAntChainMiniAppBrowserQRCodeAuthorizedUsersResponseBodyResult(TeaModel):
    def __init__(
        self,
        qrcode_type: str = None,
        pagination: DescribeAntChainMiniAppBrowserQRCodeAuthorizedUsersResponseBodyResultPagination = None,
        authorization_type: str = None,
        authorized_user_list: List[DescribeAntChainMiniAppBrowserQRCodeAuthorizedUsersResponseBodyResultAuthorizedUserList] = None,
        ant_chain_id: str = None,
    ):
        self.qrcode_type = qrcode_type
        self.pagination = pagination
        self.authorization_type = authorization_type
        self.authorized_user_list = authorized_user_list
        self.ant_chain_id = ant_chain_id

    def validate(self):
        if self.pagination:
            self.pagination.validate()
        if self.authorized_user_list:
            for k in self.authorized_user_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.qrcode_type is not None:
            result['QRCodeType'] = self.qrcode_type
        if self.pagination is not None:
            result['Pagination'] = self.pagination.to_map()
        if self.authorization_type is not None:
            result['AuthorizationType'] = self.authorization_type
        result['AuthorizedUserList'] = []
        if self.authorized_user_list is not None:
            for k in self.authorized_user_list:
                result['AuthorizedUserList'].append(k.to_map() if k else None)
        if self.ant_chain_id is not None:
            result['AntChainId'] = self.ant_chain_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('QRCodeType') is not None:
            self.qrcode_type = m.get('QRCodeType')
        if m.get('Pagination') is not None:
            temp_model = DescribeAntChainMiniAppBrowserQRCodeAuthorizedUsersResponseBodyResultPagination()
            self.pagination = temp_model.from_map(m['Pagination'])
        if m.get('AuthorizationType') is not None:
            self.authorization_type = m.get('AuthorizationType')
        self.authorized_user_list = []
        if m.get('AuthorizedUserList') is not None:
            for k in m.get('AuthorizedUserList'):
                temp_model = DescribeAntChainMiniAppBrowserQRCodeAuthorizedUsersResponseBodyResultAuthorizedUserList()
                self.authorized_user_list.append(temp_model.from_map(k))
        if m.get('AntChainId') is not None:
            self.ant_chain_id = m.get('AntChainId')
        return self


class DescribeAntChainMiniAppBrowserQRCodeAuthorizedUsersResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: DescribeAntChainMiniAppBrowserQRCodeAuthorizedUsersResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = DescribeAntChainMiniAppBrowserQRCodeAuthorizedUsersResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class DescribeAntChainMiniAppBrowserQRCodeAuthorizedUsersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeAntChainMiniAppBrowserQRCodeAuthorizedUsersResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeAntChainMiniAppBrowserQRCodeAuthorizedUsersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAntChainMiniAppBrowserTransactionQRCodeRequest(TeaModel):
    def __init__(
        self,
        ant_chain_id: str = None,
        transaction_hash: str = None,
    ):
        self.ant_chain_id = ant_chain_id
        self.transaction_hash = transaction_hash

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.ant_chain_id is not None:
            result['AntChainId'] = self.ant_chain_id
        if self.transaction_hash is not None:
            result['TransactionHash'] = self.transaction_hash
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AntChainId') is not None:
            self.ant_chain_id = m.get('AntChainId')
        if m.get('TransactionHash') is not None:
            self.transaction_hash = m.get('TransactionHash')
        return self


class DescribeAntChainMiniAppBrowserTransactionQRCodeResponseBodyResult(TeaModel):
    def __init__(
        self,
        base_64qrcode_png: str = None,
        transaction_hash: str = None,
        qrcode_content: str = None,
        ant_chain_id: str = None,
    ):
        self.base_64qrcode_png = base_64qrcode_png
        self.transaction_hash = transaction_hash
        self.qrcode_content = qrcode_content
        self.ant_chain_id = ant_chain_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.base_64qrcode_png is not None:
            result['Base64QRCodePNG'] = self.base_64qrcode_png
        if self.transaction_hash is not None:
            result['TransactionHash'] = self.transaction_hash
        if self.qrcode_content is not None:
            result['QRCodeContent'] = self.qrcode_content
        if self.ant_chain_id is not None:
            result['AntChainId'] = self.ant_chain_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Base64QRCodePNG') is not None:
            self.base_64qrcode_png = m.get('Base64QRCodePNG')
        if m.get('TransactionHash') is not None:
            self.transaction_hash = m.get('TransactionHash')
        if m.get('QRCodeContent') is not None:
            self.qrcode_content = m.get('QRCodeContent')
        if m.get('AntChainId') is not None:
            self.ant_chain_id = m.get('AntChainId')
        return self


class DescribeAntChainMiniAppBrowserTransactionQRCodeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: DescribeAntChainMiniAppBrowserTransactionQRCodeResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = DescribeAntChainMiniAppBrowserTransactionQRCodeResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class DescribeAntChainMiniAppBrowserTransactionQRCodeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeAntChainMiniAppBrowserTransactionQRCodeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeAntChainMiniAppBrowserTransactionQRCodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAntChainNodesRequest(TeaModel):
    def __init__(
        self,
        ant_chain_id: str = None,
    ):
        self.ant_chain_id = ant_chain_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.ant_chain_id is not None:
            result['AntChainId'] = self.ant_chain_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AntChainId') is not None:
            self.ant_chain_id = m.get('AntChainId')
        return self


class DescribeAntChainNodesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[Dict[str, Any]] = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class DescribeAntChainNodesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeAntChainNodesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeAntChainNodesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAntChainQRCodeAuthorizationRequest(TeaModel):
    def __init__(
        self,
        ant_chain_id: str = None,
        qrcode_type: str = None,
    ):
        self.ant_chain_id = ant_chain_id
        self.qrcode_type = qrcode_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.ant_chain_id is not None:
            result['AntChainId'] = self.ant_chain_id
        if self.qrcode_type is not None:
            result['QRCodeType'] = self.qrcode_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AntChainId') is not None:
            self.ant_chain_id = m.get('AntChainId')
        if m.get('QRCodeType') is not None:
            self.qrcode_type = m.get('QRCodeType')
        return self


class DescribeAntChainQRCodeAuthorizationResponseBodyResult(TeaModel):
    def __init__(
        self,
        qrcode_type: str = None,
        authorization_type: str = None,
        ant_chain_id: str = None,
    ):
        self.qrcode_type = qrcode_type
        self.authorization_type = authorization_type
        self.ant_chain_id = ant_chain_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.qrcode_type is not None:
            result['QRCodeType'] = self.qrcode_type
        if self.authorization_type is not None:
            result['AuthorizationType'] = self.authorization_type
        if self.ant_chain_id is not None:
            result['AntChainId'] = self.ant_chain_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('QRCodeType') is not None:
            self.qrcode_type = m.get('QRCodeType')
        if m.get('AuthorizationType') is not None:
            self.authorization_type = m.get('AuthorizationType')
        if m.get('AntChainId') is not None:
            self.ant_chain_id = m.get('AntChainId')
        return self


class DescribeAntChainQRCodeAuthorizationResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: DescribeAntChainQRCodeAuthorizationResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = DescribeAntChainQRCodeAuthorizationResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class DescribeAntChainQRCodeAuthorizationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeAntChainQRCodeAuthorizationResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeAntChainQRCodeAuthorizationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAntChainsRequest(TeaModel):
    def __init__(
        self,
        page_size: int = None,
        page_number: int = None,
        consortium_id: str = None,
    ):
        self.page_size = page_size
        self.page_number = page_number
        self.consortium_id = consortium_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.consortium_id is not None:
            result['ConsortiumId'] = self.consortium_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('ConsortiumId') is not None:
            self.consortium_id = m.get('ConsortiumId')
        return self


class DescribeAntChainsResponseBodyResultPagination(TeaModel):
    def __init__(
        self,
        page_size: int = None,
        page_number: int = None,
        total_count: int = None,
    ):
        self.page_size = page_size
        self.page_number = page_number
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeAntChainsResponseBodyResultAntChains(TeaModel):
    def __init__(
        self,
        expire_time: int = None,
        create_time: int = None,
        chain_type: str = None,
        is_admin: bool = None,
        merkle_tree_suit: str = None,
        member_status: str = None,
        region_id: str = None,
        ant_chain_name: str = None,
        network: str = None,
        tls_algo: str = None,
        version: str = None,
        cipher_suit: str = None,
        resource_size: str = None,
        node_num: int = None,
        ant_chain_id: str = None,
    ):
        self.expire_time = expire_time
        self.create_time = create_time
        self.chain_type = chain_type
        self.is_admin = is_admin
        self.merkle_tree_suit = merkle_tree_suit
        self.member_status = member_status
        self.region_id = region_id
        self.ant_chain_name = ant_chain_name
        self.network = network
        self.tls_algo = tls_algo
        self.version = version
        self.cipher_suit = cipher_suit
        self.resource_size = resource_size
        self.node_num = node_num
        self.ant_chain_id = ant_chain_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.chain_type is not None:
            result['ChainType'] = self.chain_type
        if self.is_admin is not None:
            result['IsAdmin'] = self.is_admin
        if self.merkle_tree_suit is not None:
            result['MerkleTreeSuit'] = self.merkle_tree_suit
        if self.member_status is not None:
            result['MemberStatus'] = self.member_status
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.ant_chain_name is not None:
            result['AntChainName'] = self.ant_chain_name
        if self.network is not None:
            result['Network'] = self.network
        if self.tls_algo is not None:
            result['TlsAlgo'] = self.tls_algo
        if self.version is not None:
            result['Version'] = self.version
        if self.cipher_suit is not None:
            result['CipherSuit'] = self.cipher_suit
        if self.resource_size is not None:
            result['ResourceSize'] = self.resource_size
        if self.node_num is not None:
            result['NodeNum'] = self.node_num
        if self.ant_chain_id is not None:
            result['AntChainId'] = self.ant_chain_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ChainType') is not None:
            self.chain_type = m.get('ChainType')
        if m.get('IsAdmin') is not None:
            self.is_admin = m.get('IsAdmin')
        if m.get('MerkleTreeSuit') is not None:
            self.merkle_tree_suit = m.get('MerkleTreeSuit')
        if m.get('MemberStatus') is not None:
            self.member_status = m.get('MemberStatus')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('AntChainName') is not None:
            self.ant_chain_name = m.get('AntChainName')
        if m.get('Network') is not None:
            self.network = m.get('Network')
        if m.get('TlsAlgo') is not None:
            self.tls_algo = m.get('TlsAlgo')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('CipherSuit') is not None:
            self.cipher_suit = m.get('CipherSuit')
        if m.get('ResourceSize') is not None:
            self.resource_size = m.get('ResourceSize')
        if m.get('NodeNum') is not None:
            self.node_num = m.get('NodeNum')
        if m.get('AntChainId') is not None:
            self.ant_chain_id = m.get('AntChainId')
        return self


class DescribeAntChainsResponseBodyResult(TeaModel):
    def __init__(
        self,
        pagination: DescribeAntChainsResponseBodyResultPagination = None,
        ant_chains: List[DescribeAntChainsResponseBodyResultAntChains] = None,
        is_exist: bool = None,
    ):
        self.pagination = pagination
        self.ant_chains = ant_chains
        self.is_exist = is_exist

    def validate(self):
        if self.pagination:
            self.pagination.validate()
        if self.ant_chains:
            for k in self.ant_chains:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.pagination is not None:
            result['Pagination'] = self.pagination.to_map()
        result['AntChains'] = []
        if self.ant_chains is not None:
            for k in self.ant_chains:
                result['AntChains'].append(k.to_map() if k else None)
        if self.is_exist is not None:
            result['IsExist'] = self.is_exist
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Pagination') is not None:
            temp_model = DescribeAntChainsResponseBodyResultPagination()
            self.pagination = temp_model.from_map(m['Pagination'])
        self.ant_chains = []
        if m.get('AntChains') is not None:
            for k in m.get('AntChains'):
                temp_model = DescribeAntChainsResponseBodyResultAntChains()
                self.ant_chains.append(temp_model.from_map(k))
        if m.get('IsExist') is not None:
            self.is_exist = m.get('IsExist')
        return self


class DescribeAntChainsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: DescribeAntChainsResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = DescribeAntChainsResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class DescribeAntChainsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeAntChainsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeAntChainsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAntChainTransactionRequest(TeaModel):
    def __init__(
        self,
        ant_chain_id: str = None,
        hash: str = None,
    ):
        self.ant_chain_id = ant_chain_id
        self.hash = hash

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.ant_chain_id is not None:
            result['AntChainId'] = self.ant_chain_id
        if self.hash is not None:
            result['Hash'] = self.hash
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AntChainId') is not None:
            self.ant_chain_id = m.get('AntChainId')
        if m.get('Hash') is not None:
            self.hash = m.get('Hash')
        return self


class DescribeAntChainTransactionResponseBodyResultTransaction(TeaModel):
    def __init__(
        self,
        hash: str = None,
        from_: str = None,
        data: str = None,
        nonce: str = None,
        to: str = None,
        timestamp: int = None,
        gas: str = None,
        period: int = None,
        value: str = None,
        extentions: List[str] = None,
        tx_type: str = None,
        signatures: List[str] = None,
    ):
        self.hash = hash
        self.from_ = from_
        self.data = data
        self.nonce = nonce
        self.to = to
        self.timestamp = timestamp
        self.gas = gas
        self.period = period
        self.value = value
        self.extentions = extentions
        self.tx_type = tx_type
        self.signatures = signatures

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.hash is not None:
            result['Hash'] = self.hash
        if self.from_ is not None:
            result['From'] = self.from_
        if self.data is not None:
            result['Data'] = self.data
        if self.nonce is not None:
            result['Nonce'] = self.nonce
        if self.to is not None:
            result['To'] = self.to
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.gas is not None:
            result['Gas'] = self.gas
        if self.period is not None:
            result['Period'] = self.period
        if self.value is not None:
            result['Value'] = self.value
        if self.extentions is not None:
            result['Extentions'] = self.extentions
        if self.tx_type is not None:
            result['TxType'] = self.tx_type
        if self.signatures is not None:
            result['Signatures'] = self.signatures
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Hash') is not None:
            self.hash = m.get('Hash')
        if m.get('From') is not None:
            self.from_ = m.get('From')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Nonce') is not None:
            self.nonce = m.get('Nonce')
        if m.get('To') is not None:
            self.to = m.get('To')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('Gas') is not None:
            self.gas = m.get('Gas')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('Extentions') is not None:
            self.extentions = m.get('Extentions')
        if m.get('TxType') is not None:
            self.tx_type = m.get('TxType')
        if m.get('Signatures') is not None:
            self.signatures = m.get('Signatures')
        return self


class DescribeAntChainTransactionResponseBodyResult(TeaModel):
    def __init__(
        self,
        hash: str = None,
        block_version: str = None,
        block_height: int = None,
        create_time: int = None,
        block_hash: str = None,
        transaction: DescribeAntChainTransactionResponseBodyResultTransaction = None,
    ):
        self.hash = hash
        self.block_version = block_version
        self.block_height = block_height
        self.create_time = create_time
        self.block_hash = block_hash
        self.transaction = transaction

    def validate(self):
        if self.transaction:
            self.transaction.validate()

    def to_map(self):
        result = dict()
        if self.hash is not None:
            result['Hash'] = self.hash
        if self.block_version is not None:
            result['BlockVersion'] = self.block_version
        if self.block_height is not None:
            result['BlockHeight'] = self.block_height
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.block_hash is not None:
            result['BlockHash'] = self.block_hash
        if self.transaction is not None:
            result['Transaction'] = self.transaction.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Hash') is not None:
            self.hash = m.get('Hash')
        if m.get('BlockVersion') is not None:
            self.block_version = m.get('BlockVersion')
        if m.get('BlockHeight') is not None:
            self.block_height = m.get('BlockHeight')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('BlockHash') is not None:
            self.block_hash = m.get('BlockHash')
        if m.get('Transaction') is not None:
            temp_model = DescribeAntChainTransactionResponseBodyResultTransaction()
            self.transaction = temp_model.from_map(m['Transaction'])
        return self


class DescribeAntChainTransactionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: DescribeAntChainTransactionResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = DescribeAntChainTransactionResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class DescribeAntChainTransactionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeAntChainTransactionResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeAntChainTransactionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAntChainTransactionReceiptRequest(TeaModel):
    def __init__(
        self,
        ant_chain_id: str = None,
        hash: str = None,
    ):
        self.ant_chain_id = ant_chain_id
        self.hash = hash

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.ant_chain_id is not None:
            result['AntChainId'] = self.ant_chain_id
        if self.hash is not None:
            result['Hash'] = self.hash
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AntChainId') is not None:
            self.ant_chain_id = m.get('AntChainId')
        if m.get('Hash') is not None:
            self.hash = m.get('Hash')
        return self


class DescribeAntChainTransactionReceiptResponseBodyResult(TeaModel):
    def __init__(
        self,
        data: str = None,
        result: int = None,
        logs: List[str] = None,
        gas_used: str = None,
    ):
        self.data = data
        self.result = result
        self.logs = logs
        self.gas_used = gas_used

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.result is not None:
            result['Result'] = self.result
        if self.logs is not None:
            result['Logs'] = self.logs
        if self.gas_used is not None:
            result['GasUsed'] = self.gas_used
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Logs') is not None:
            self.logs = m.get('Logs')
        if m.get('GasUsed') is not None:
            self.gas_used = m.get('GasUsed')
        return self


class DescribeAntChainTransactionReceiptResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: DescribeAntChainTransactionReceiptResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = DescribeAntChainTransactionReceiptResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class DescribeAntChainTransactionReceiptResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeAntChainTransactionReceiptResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeAntChainTransactionReceiptResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAntChainTransactionStatisticsRequest(TeaModel):
    def __init__(
        self,
        ant_chain_id: str = None,
        start: int = None,
        end: int = None,
    ):
        self.ant_chain_id = ant_chain_id
        self.start = start
        self.end = end

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.ant_chain_id is not None:
            result['AntChainId'] = self.ant_chain_id
        if self.start is not None:
            result['Start'] = self.start
        if self.end is not None:
            result['End'] = self.end
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AntChainId') is not None:
            self.ant_chain_id = m.get('AntChainId')
        if m.get('Start') is not None:
            self.start = m.get('Start')
        if m.get('End') is not None:
            self.end = m.get('End')
        return self


class DescribeAntChainTransactionStatisticsResponseBodyResult(TeaModel):
    def __init__(
        self,
        creat_time: int = None,
        trans_count: int = None,
        dt: str = None,
        last_sum_block_height: int = None,
        ant_chain_id: str = None,
    ):
        self.creat_time = creat_time
        self.trans_count = trans_count
        self.dt = dt
        self.last_sum_block_height = last_sum_block_height
        self.ant_chain_id = ant_chain_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.creat_time is not None:
            result['CreatTime'] = self.creat_time
        if self.trans_count is not None:
            result['TransCount'] = self.trans_count
        if self.dt is not None:
            result['Dt'] = self.dt
        if self.last_sum_block_height is not None:
            result['LastSumBlockHeight'] = self.last_sum_block_height
        if self.ant_chain_id is not None:
            result['AntChainId'] = self.ant_chain_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatTime') is not None:
            self.creat_time = m.get('CreatTime')
        if m.get('TransCount') is not None:
            self.trans_count = m.get('TransCount')
        if m.get('Dt') is not None:
            self.dt = m.get('Dt')
        if m.get('LastSumBlockHeight') is not None:
            self.last_sum_block_height = m.get('LastSumBlockHeight')
        if m.get('AntChainId') is not None:
            self.ant_chain_id = m.get('AntChainId')
        return self


class DescribeAntChainTransactionStatisticsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[DescribeAntChainTransactionStatisticsResponseBodyResult] = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = DescribeAntChainTransactionStatisticsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class DescribeAntChainTransactionStatisticsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeAntChainTransactionStatisticsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeAntChainTransactionStatisticsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeEthereumDeletableRequest(TeaModel):
    def __init__(
        self,
        ethereum_id: str = None,
    ):
        self.ethereum_id = ethereum_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.ethereum_id is not None:
            result['EthereumId'] = self.ethereum_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EthereumId') is not None:
            self.ethereum_id = m.get('EthereumId')
        return self


class DescribeEthereumDeletableResponseBodyResult(TeaModel):
    def __init__(
        self,
        deletable: bool = None,
        ethereum_id: str = None,
    ):
        self.deletable = deletable
        self.ethereum_id = ethereum_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.deletable is not None:
            result['Deletable'] = self.deletable
        if self.ethereum_id is not None:
            result['EthereumId'] = self.ethereum_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Deletable') is not None:
            self.deletable = m.get('Deletable')
        if m.get('EthereumId') is not None:
            self.ethereum_id = m.get('EthereumId')
        return self


class DescribeEthereumDeletableResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_code: int = None,
        success: bool = None,
        result: DescribeEthereumDeletableResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.error_code = error_code
        self.success = success
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Result') is not None:
            temp_model = DescribeEthereumDeletableResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class DescribeEthereumDeletableResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeEthereumDeletableResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeEthereumDeletableResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFabricCandidateOrganizationsRequest(TeaModel):
    def __init__(
        self,
        location: str = None,
    ):
        self.location = location

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.location is not None:
            result['Location'] = self.location
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Location') is not None:
            self.location = m.get('Location')
        return self


class DescribeFabricCandidateOrganizationsResponseBodyResult(TeaModel):
    def __init__(
        self,
        service_state: str = None,
        organization_name: str = None,
        cluster_state: str = None,
        organization_id: str = None,
    ):
        self.service_state = service_state
        self.organization_name = organization_name
        self.cluster_state = cluster_state
        self.organization_id = organization_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.service_state is not None:
            result['ServiceState'] = self.service_state
        if self.organization_name is not None:
            result['OrganizationName'] = self.organization_name
        if self.cluster_state is not None:
            result['ClusterState'] = self.cluster_state
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceState') is not None:
            self.service_state = m.get('ServiceState')
        if m.get('OrganizationName') is not None:
            self.organization_name = m.get('OrganizationName')
        if m.get('ClusterState') is not None:
            self.cluster_state = m.get('ClusterState')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class DescribeFabricCandidateOrganizationsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_code: int = None,
        success: bool = None,
        result: List[DescribeFabricCandidateOrganizationsResponseBodyResult] = None,
    ):
        self.request_id = request_id
        self.error_code = error_code
        self.success = success
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = DescribeFabricCandidateOrganizationsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class DescribeFabricCandidateOrganizationsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeFabricCandidateOrganizationsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeFabricCandidateOrganizationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFabricChaincodeUploadPolicyRequest(TeaModel):
    def __init__(
        self,
        organization_id: str = None,
    ):
        self.organization_id = organization_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class DescribeFabricChaincodeUploadPolicyResponseBodyResult(TeaModel):
    def __init__(
        self,
        signature: str = None,
        host: str = None,
        policy: str = None,
        dir: str = None,
        access_id: str = None,
        expire: int = None,
    ):
        self.signature = signature
        self.host = host
        self.policy = policy
        self.dir = dir
        self.access_id = access_id
        self.expire = expire

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.signature is not None:
            result['Signature'] = self.signature
        if self.host is not None:
            result['Host'] = self.host
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.dir is not None:
            result['Dir'] = self.dir
        if self.access_id is not None:
            result['AccessId'] = self.access_id
        if self.expire is not None:
            result['Expire'] = self.expire
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Signature') is not None:
            self.signature = m.get('Signature')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('Dir') is not None:
            self.dir = m.get('Dir')
        if m.get('AccessId') is not None:
            self.access_id = m.get('AccessId')
        if m.get('Expire') is not None:
            self.expire = m.get('Expire')
        return self


class DescribeFabricChaincodeUploadPolicyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_code: int = None,
        success: bool = None,
        result: DescribeFabricChaincodeUploadPolicyResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.error_code = error_code
        self.success = success
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Result') is not None:
            temp_model = DescribeFabricChaincodeUploadPolicyResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class DescribeFabricChaincodeUploadPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeFabricChaincodeUploadPolicyResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeFabricChaincodeUploadPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFabricChannelMembersRequest(TeaModel):
    def __init__(
        self,
        channel_id: str = None,
    ):
        self.channel_id = channel_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        return self


class DescribeFabricChannelMembersResponseBodyResult(TeaModel):
    def __init__(
        self,
        with_peer: bool = None,
        accept_time: str = None,
        organization_domain: str = None,
        state: str = None,
        invite_time: str = None,
        channel_id: str = None,
        organization_name: str = None,
        organization_description: str = None,
        organization_id: str = None,
    ):
        self.with_peer = with_peer
        self.accept_time = accept_time
        self.organization_domain = organization_domain
        self.state = state
        self.invite_time = invite_time
        self.channel_id = channel_id
        self.organization_name = organization_name
        self.organization_description = organization_description
        self.organization_id = organization_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.with_peer is not None:
            result['WithPeer'] = self.with_peer
        if self.accept_time is not None:
            result['AcceptTime'] = self.accept_time
        if self.organization_domain is not None:
            result['OrganizationDomain'] = self.organization_domain
        if self.state is not None:
            result['State'] = self.state
        if self.invite_time is not None:
            result['InviteTime'] = self.invite_time
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.organization_name is not None:
            result['OrganizationName'] = self.organization_name
        if self.organization_description is not None:
            result['OrganizationDescription'] = self.organization_description
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('WithPeer') is not None:
            self.with_peer = m.get('WithPeer')
        if m.get('AcceptTime') is not None:
            self.accept_time = m.get('AcceptTime')
        if m.get('OrganizationDomain') is not None:
            self.organization_domain = m.get('OrganizationDomain')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('InviteTime') is not None:
            self.invite_time = m.get('InviteTime')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('OrganizationName') is not None:
            self.organization_name = m.get('OrganizationName')
        if m.get('OrganizationDescription') is not None:
            self.organization_description = m.get('OrganizationDescription')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class DescribeFabricChannelMembersResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_code: int = None,
        success: bool = None,
        result: List[DescribeFabricChannelMembersResponseBodyResult] = None,
    ):
        self.request_id = request_id
        self.error_code = error_code
        self.success = success
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = DescribeFabricChannelMembersResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class DescribeFabricChannelMembersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeFabricChannelMembersResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeFabricChannelMembersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFabricConsortiumAdminStatusRequest(TeaModel):
    def __init__(
        self,
        location: str = None,
    ):
        self.location = location

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.location is not None:
            result['Location'] = self.location
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Location') is not None:
            self.location = m.get('Location')
        return self


class DescribeFabricConsortiumAdminStatusResponseBodyResult(TeaModel):
    def __init__(
        self,
        consortium_id: str = None,
        consortium_administrator: bool = None,
    ):
        self.consortium_id = consortium_id
        self.consortium_administrator = consortium_administrator

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.consortium_id is not None:
            result['ConsortiumId'] = self.consortium_id
        if self.consortium_administrator is not None:
            result['ConsortiumAdministrator'] = self.consortium_administrator
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsortiumId') is not None:
            self.consortium_id = m.get('ConsortiumId')
        if m.get('ConsortiumAdministrator') is not None:
            self.consortium_administrator = m.get('ConsortiumAdministrator')
        return self


class DescribeFabricConsortiumAdminStatusResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_code: int = None,
        success: bool = None,
        result: List[DescribeFabricConsortiumAdminStatusResponseBodyResult] = None,
    ):
        self.request_id = request_id
        self.error_code = error_code
        self.success = success
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = DescribeFabricConsortiumAdminStatusResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class DescribeFabricConsortiumAdminStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeFabricConsortiumAdminStatusResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeFabricConsortiumAdminStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFabricConsortiumChaincodesRequest(TeaModel):
    def __init__(
        self,
        consortium_id: str = None,
        location: str = None,
    ):
        self.consortium_id = consortium_id
        self.location = location

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.consortium_id is not None:
            result['ConsortiumId'] = self.consortium_id
        if self.location is not None:
            result['Location'] = self.location
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsortiumId') is not None:
            self.consortium_id = m.get('ConsortiumId')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        return self


class DescribeFabricConsortiumChaincodesResponseBodyResult(TeaModel):
    def __init__(
        self,
        type: int = None,
        endorse_policy: str = None,
        state: str = None,
        create_time: str = None,
        chaincode_id: str = None,
        message: str = None,
        provider_name: str = None,
        chaincode_name: str = None,
        input: str = None,
        install: bool = None,
        provider_id: str = None,
        deploy_time: str = None,
        chaincode_version: str = None,
        consortium_id: str = None,
        channel_name: str = None,
        channel_id: str = None,
        path: str = None,
    ):
        self.type = type
        self.endorse_policy = endorse_policy
        self.state = state
        self.create_time = create_time
        self.chaincode_id = chaincode_id
        self.message = message
        self.provider_name = provider_name
        self.chaincode_name = chaincode_name
        self.input = input
        self.install = install
        self.provider_id = provider_id
        self.deploy_time = deploy_time
        self.chaincode_version = chaincode_version
        self.consortium_id = consortium_id
        self.channel_name = channel_name
        self.channel_id = channel_id
        self.path = path

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.endorse_policy is not None:
            result['EndorsePolicy'] = self.endorse_policy
        if self.state is not None:
            result['State'] = self.state
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.chaincode_id is not None:
            result['ChaincodeId'] = self.chaincode_id
        if self.message is not None:
            result['Message'] = self.message
        if self.provider_name is not None:
            result['ProviderName'] = self.provider_name
        if self.chaincode_name is not None:
            result['ChaincodeName'] = self.chaincode_name
        if self.input is not None:
            result['Input'] = self.input
        if self.install is not None:
            result['Install'] = self.install
        if self.provider_id is not None:
            result['ProviderId'] = self.provider_id
        if self.deploy_time is not None:
            result['DeployTime'] = self.deploy_time
        if self.chaincode_version is not None:
            result['ChaincodeVersion'] = self.chaincode_version
        if self.consortium_id is not None:
            result['ConsortiumId'] = self.consortium_id
        if self.channel_name is not None:
            result['ChannelName'] = self.channel_name
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.path is not None:
            result['Path'] = self.path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('EndorsePolicy') is not None:
            self.endorse_policy = m.get('EndorsePolicy')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ChaincodeId') is not None:
            self.chaincode_id = m.get('ChaincodeId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('ProviderName') is not None:
            self.provider_name = m.get('ProviderName')
        if m.get('ChaincodeName') is not None:
            self.chaincode_name = m.get('ChaincodeName')
        if m.get('Input') is not None:
            self.input = m.get('Input')
        if m.get('Install') is not None:
            self.install = m.get('Install')
        if m.get('ProviderId') is not None:
            self.provider_id = m.get('ProviderId')
        if m.get('DeployTime') is not None:
            self.deploy_time = m.get('DeployTime')
        if m.get('ChaincodeVersion') is not None:
            self.chaincode_version = m.get('ChaincodeVersion')
        if m.get('ConsortiumId') is not None:
            self.consortium_id = m.get('ConsortiumId')
        if m.get('ChannelName') is not None:
            self.channel_name = m.get('ChannelName')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        return self


class DescribeFabricConsortiumChaincodesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_code: int = None,
        success: bool = None,
        result: List[DescribeFabricConsortiumChaincodesResponseBodyResult] = None,
    ):
        self.request_id = request_id
        self.error_code = error_code
        self.success = success
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = DescribeFabricConsortiumChaincodesResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class DescribeFabricConsortiumChaincodesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeFabricConsortiumChaincodesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeFabricConsortiumChaincodesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFabricConsortiumChannelsRequest(TeaModel):
    def __init__(
        self,
        consortium_id: str = None,
        location: str = None,
    ):
        self.consortium_id = consortium_id
        self.location = location

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.consortium_id is not None:
            result['ConsortiumId'] = self.consortium_id
        if self.location is not None:
            result['Location'] = self.location
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsortiumId') is not None:
            self.consortium_id = m.get('ConsortiumId')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        return self


class DescribeFabricConsortiumChannelsResponseBodyResult(TeaModel):
    def __init__(
        self,
        batch_timeout: int = None,
        update_time: str = None,
        chaincode_count: int = None,
        state: str = None,
        member_joined_count: str = None,
        preferred_max_bytes: int = None,
        create_time: str = None,
        support_channel_config: bool = None,
        owner_name: str = None,
        owner_uid: int = None,
        owner_bid: str = None,
        max_message_count: int = None,
        member_count: int = None,
        need_joined: bool = None,
        request_id: str = None,
        consortium_id: str = None,
        channel_name: str = None,
        delete_time: str = None,
        channel_id: str = None,
        consortium_channel_id: int = None,
        deleted: bool = None,
        consortium_name: str = None,
        block_count: int = None,
    ):
        self.batch_timeout = batch_timeout
        self.update_time = update_time
        self.chaincode_count = chaincode_count
        self.state = state
        self.member_joined_count = member_joined_count
        self.preferred_max_bytes = preferred_max_bytes
        self.create_time = create_time
        self.support_channel_config = support_channel_config
        self.owner_name = owner_name
        self.owner_uid = owner_uid
        self.owner_bid = owner_bid
        self.max_message_count = max_message_count
        self.member_count = member_count
        self.need_joined = need_joined
        self.request_id = request_id
        self.consortium_id = consortium_id
        self.channel_name = channel_name
        self.delete_time = delete_time
        self.channel_id = channel_id
        self.consortium_channel_id = consortium_channel_id
        self.deleted = deleted
        self.consortium_name = consortium_name
        self.block_count = block_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.batch_timeout is not None:
            result['BatchTimeout'] = self.batch_timeout
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.chaincode_count is not None:
            result['ChaincodeCount'] = self.chaincode_count
        if self.state is not None:
            result['State'] = self.state
        if self.member_joined_count is not None:
            result['MemberJoinedCount'] = self.member_joined_count
        if self.preferred_max_bytes is not None:
            result['PreferredMaxBytes'] = self.preferred_max_bytes
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.support_channel_config is not None:
            result['SupportChannelConfig'] = self.support_channel_config
        if self.owner_name is not None:
            result['OwnerName'] = self.owner_name
        if self.owner_uid is not None:
            result['OwnerUid'] = self.owner_uid
        if self.owner_bid is not None:
            result['OwnerBid'] = self.owner_bid
        if self.max_message_count is not None:
            result['MaxMessageCount'] = self.max_message_count
        if self.member_count is not None:
            result['MemberCount'] = self.member_count
        if self.need_joined is not None:
            result['NeedJoined'] = self.need_joined
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.consortium_id is not None:
            result['ConsortiumId'] = self.consortium_id
        if self.channel_name is not None:
            result['ChannelName'] = self.channel_name
        if self.delete_time is not None:
            result['DeleteTime'] = self.delete_time
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.consortium_channel_id is not None:
            result['ConsortiumChannelId'] = self.consortium_channel_id
        if self.deleted is not None:
            result['Deleted'] = self.deleted
        if self.consortium_name is not None:
            result['ConsortiumName'] = self.consortium_name
        if self.block_count is not None:
            result['BlockCount'] = self.block_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BatchTimeout') is not None:
            self.batch_timeout = m.get('BatchTimeout')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('ChaincodeCount') is not None:
            self.chaincode_count = m.get('ChaincodeCount')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('MemberJoinedCount') is not None:
            self.member_joined_count = m.get('MemberJoinedCount')
        if m.get('PreferredMaxBytes') is not None:
            self.preferred_max_bytes = m.get('PreferredMaxBytes')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('SupportChannelConfig') is not None:
            self.support_channel_config = m.get('SupportChannelConfig')
        if m.get('OwnerName') is not None:
            self.owner_name = m.get('OwnerName')
        if m.get('OwnerUid') is not None:
            self.owner_uid = m.get('OwnerUid')
        if m.get('OwnerBid') is not None:
            self.owner_bid = m.get('OwnerBid')
        if m.get('MaxMessageCount') is not None:
            self.max_message_count = m.get('MaxMessageCount')
        if m.get('MemberCount') is not None:
            self.member_count = m.get('MemberCount')
        if m.get('NeedJoined') is not None:
            self.need_joined = m.get('NeedJoined')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ConsortiumId') is not None:
            self.consortium_id = m.get('ConsortiumId')
        if m.get('ChannelName') is not None:
            self.channel_name = m.get('ChannelName')
        if m.get('DeleteTime') is not None:
            self.delete_time = m.get('DeleteTime')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('ConsortiumChannelId') is not None:
            self.consortium_channel_id = m.get('ConsortiumChannelId')
        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')
        if m.get('ConsortiumName') is not None:
            self.consortium_name = m.get('ConsortiumName')
        if m.get('BlockCount') is not None:
            self.block_count = m.get('BlockCount')
        return self


class DescribeFabricConsortiumChannelsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_code: int = None,
        success: bool = None,
        result: List[DescribeFabricConsortiumChannelsResponseBodyResult] = None,
    ):
        self.request_id = request_id
        self.error_code = error_code
        self.success = success
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = DescribeFabricConsortiumChannelsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class DescribeFabricConsortiumChannelsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeFabricConsortiumChannelsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeFabricConsortiumChannelsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFabricConsortiumConfigResponseBodyResult(TeaModel):
    def __init__(
        self,
        channel_policy: List[str] = None,
        orderer_type: List[str] = None,
    ):
        self.channel_policy = channel_policy
        self.orderer_type = orderer_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.channel_policy is not None:
            result['ChannelPolicy'] = self.channel_policy
        if self.orderer_type is not None:
            result['OrdererType'] = self.orderer_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChannelPolicy') is not None:
            self.channel_policy = m.get('ChannelPolicy')
        if m.get('OrdererType') is not None:
            self.orderer_type = m.get('OrdererType')
        return self


class DescribeFabricConsortiumConfigResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_code: int = None,
        success: bool = None,
        result: DescribeFabricConsortiumConfigResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.error_code = error_code
        self.success = success
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Result') is not None:
            temp_model = DescribeFabricConsortiumConfigResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class DescribeFabricConsortiumConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeFabricConsortiumConfigResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeFabricConsortiumConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFabricConsortiumDeletableRequest(TeaModel):
    def __init__(
        self,
        consortium_id: str = None,
        location: str = None,
    ):
        self.consortium_id = consortium_id
        self.location = location

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.consortium_id is not None:
            result['ConsortiumId'] = self.consortium_id
        if self.location is not None:
            result['Location'] = self.location
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsortiumId') is not None:
            self.consortium_id = m.get('ConsortiumId')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        return self


class DescribeFabricConsortiumDeletableResponseBodyResult(TeaModel):
    def __init__(
        self,
        deletable: bool = None,
        domain: str = None,
        description: str = None,
        consortium_id: str = None,
        state: str = None,
        zone_id: str = None,
        code_name: str = None,
        consortium_name: str = None,
        region_id: str = None,
    ):
        self.deletable = deletable
        self.domain = domain
        self.description = description
        self.consortium_id = consortium_id
        self.state = state
        self.zone_id = zone_id
        self.code_name = code_name
        self.consortium_name = consortium_name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.deletable is not None:
            result['Deletable'] = self.deletable
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.description is not None:
            result['Description'] = self.description
        if self.consortium_id is not None:
            result['ConsortiumId'] = self.consortium_id
        if self.state is not None:
            result['State'] = self.state
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.code_name is not None:
            result['CodeName'] = self.code_name
        if self.consortium_name is not None:
            result['ConsortiumName'] = self.consortium_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Deletable') is not None:
            self.deletable = m.get('Deletable')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ConsortiumId') is not None:
            self.consortium_id = m.get('ConsortiumId')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('CodeName') is not None:
            self.code_name = m.get('CodeName')
        if m.get('ConsortiumName') is not None:
            self.consortium_name = m.get('ConsortiumName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeFabricConsortiumDeletableResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_code: int = None,
        success: bool = None,
        result: DescribeFabricConsortiumDeletableResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.error_code = error_code
        self.success = success
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Result') is not None:
            temp_model = DescribeFabricConsortiumDeletableResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class DescribeFabricConsortiumDeletableResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeFabricConsortiumDeletableResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeFabricConsortiumDeletableResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFabricConsortiumMemberApprovalRequest(TeaModel):
    def __init__(
        self,
        consortium_id: str = None,
        location: str = None,
    ):
        self.consortium_id = consortium_id
        self.location = location

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.consortium_id is not None:
            result['ConsortiumId'] = self.consortium_id
        if self.location is not None:
            result['Location'] = self.location
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsortiumId') is not None:
            self.consortium_id = m.get('ConsortiumId')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        return self


class DescribeFabricConsortiumMemberApprovalResponseBodyResult(TeaModel):
    def __init__(
        self,
        consortium_id: str = None,
        state: str = None,
        channel_create_policy: str = None,
        confirm_time: str = None,
        organization_name: str = None,
        consortium_name: str = None,
        domain_name: str = None,
        organization_id: str = None,
    ):
        self.consortium_id = consortium_id
        self.state = state
        self.channel_create_policy = channel_create_policy
        self.confirm_time = confirm_time
        self.organization_name = organization_name
        self.consortium_name = consortium_name
        self.domain_name = domain_name
        self.organization_id = organization_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.consortium_id is not None:
            result['ConsortiumId'] = self.consortium_id
        if self.state is not None:
            result['State'] = self.state
        if self.channel_create_policy is not None:
            result['ChannelCreatePolicy'] = self.channel_create_policy
        if self.confirm_time is not None:
            result['ConfirmTime'] = self.confirm_time
        if self.organization_name is not None:
            result['OrganizationName'] = self.organization_name
        if self.consortium_name is not None:
            result['ConsortiumName'] = self.consortium_name
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsortiumId') is not None:
            self.consortium_id = m.get('ConsortiumId')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('ChannelCreatePolicy') is not None:
            self.channel_create_policy = m.get('ChannelCreatePolicy')
        if m.get('ConfirmTime') is not None:
            self.confirm_time = m.get('ConfirmTime')
        if m.get('OrganizationName') is not None:
            self.organization_name = m.get('OrganizationName')
        if m.get('ConsortiumName') is not None:
            self.consortium_name = m.get('ConsortiumName')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class DescribeFabricConsortiumMemberApprovalResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_code: int = None,
        success: bool = None,
        result: List[DescribeFabricConsortiumMemberApprovalResponseBodyResult] = None,
    ):
        self.request_id = request_id
        self.error_code = error_code
        self.success = success
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = DescribeFabricConsortiumMemberApprovalResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class DescribeFabricConsortiumMemberApprovalResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeFabricConsortiumMemberApprovalResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeFabricConsortiumMemberApprovalResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFabricConsortiumMembersRequest(TeaModel):
    def __init__(
        self,
        consortium_id: str = None,
        location: str = None,
    ):
        self.consortium_id = consortium_id
        self.location = location

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.consortium_id is not None:
            result['ConsortiumId'] = self.consortium_id
        if self.location is not None:
            result['Location'] = self.location
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsortiumId') is not None:
            self.consortium_id = m.get('ConsortiumId')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        return self


class DescribeFabricConsortiumMembersResponseBodyResult(TeaModel):
    def __init__(
        self,
        domain: str = None,
        description: str = None,
        consortium_id: str = None,
        organization_name: str = None,
        joined_time: str = None,
        organization_id: str = None,
    ):
        self.domain = domain
        self.description = description
        self.consortium_id = consortium_id
        self.organization_name = organization_name
        self.joined_time = joined_time
        self.organization_id = organization_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.description is not None:
            result['Description'] = self.description
        if self.consortium_id is not None:
            result['ConsortiumId'] = self.consortium_id
        if self.organization_name is not None:
            result['OrganizationName'] = self.organization_name
        if self.joined_time is not None:
            result['JoinedTime'] = self.joined_time
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ConsortiumId') is not None:
            self.consortium_id = m.get('ConsortiumId')
        if m.get('OrganizationName') is not None:
            self.organization_name = m.get('OrganizationName')
        if m.get('JoinedTime') is not None:
            self.joined_time = m.get('JoinedTime')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class DescribeFabricConsortiumMembersResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_code: int = None,
        success: bool = None,
        result: List[DescribeFabricConsortiumMembersResponseBodyResult] = None,
    ):
        self.request_id = request_id
        self.error_code = error_code
        self.success = success
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = DescribeFabricConsortiumMembersResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class DescribeFabricConsortiumMembersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeFabricConsortiumMembersResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeFabricConsortiumMembersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFabricConsortiumOrderersRequest(TeaModel):
    def __init__(
        self,
        consortium_id: str = None,
        location: str = None,
    ):
        self.consortium_id = consortium_id
        self.location = location

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.consortium_id is not None:
            result['ConsortiumId'] = self.consortium_id
        if self.location is not None:
            result['Location'] = self.location
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsortiumId') is not None:
            self.consortium_id = m.get('ConsortiumId')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        return self


class DescribeFabricConsortiumOrderersResponseBodyResult(TeaModel):
    def __init__(
        self,
        domain: str = None,
        update_time: str = None,
        orderer_name: str = None,
        create_time: str = None,
        port: int = None,
        instance_type: str = None,
    ):
        self.domain = domain
        self.update_time = update_time
        self.orderer_name = orderer_name
        self.create_time = create_time
        self.port = port
        self.instance_type = instance_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.orderer_name is not None:
            result['OrdererName'] = self.orderer_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.port is not None:
            result['Port'] = self.port
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('OrdererName') is not None:
            self.orderer_name = m.get('OrdererName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        return self


class DescribeFabricConsortiumOrderersResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_code: int = None,
        success: bool = None,
        result: List[DescribeFabricConsortiumOrderersResponseBodyResult] = None,
    ):
        self.request_id = request_id
        self.error_code = error_code
        self.success = success
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = DescribeFabricConsortiumOrderersResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class DescribeFabricConsortiumOrderersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeFabricConsortiumOrderersResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeFabricConsortiumOrderersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFabricConsortiumsRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeFabricConsortiumsRequest(TeaModel):
    def __init__(
        self,
        consortium_id: str = None,
        location: str = None,
        tag: List[DescribeFabricConsortiumsRequestTag] = None,
    ):
        self.consortium_id = consortium_id
        self.location = location
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.consortium_id is not None:
            result['ConsortiumId'] = self.consortium_id
        if self.location is not None:
            result['Location'] = self.location
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsortiumId') is not None:
            self.consortium_id = m.get('ConsortiumId')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeFabricConsortiumsRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeFabricConsortiumsResponseBodyResultTags(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeFabricConsortiumsResponseBodyResult(TeaModel):
    def __init__(
        self,
        channel_count: int = None,
        domain: str = None,
        state: str = None,
        create_time: str = None,
        tags: List[DescribeFabricConsortiumsResponseBodyResultTags] = None,
        spec_name: str = None,
        support_channel_config: bool = None,
        owner_name: str = None,
        owner_uid: int = None,
        code_name: str = None,
        owner_bid: str = None,
        region_id: str = None,
        channel_policy: str = None,
        request_id: str = None,
        consortium_id: str = None,
        expired_time: str = None,
        organization_count: int = None,
        consortium_name: str = None,
    ):
        self.channel_count = channel_count
        self.domain = domain
        self.state = state
        self.create_time = create_time
        self.tags = tags
        self.spec_name = spec_name
        self.support_channel_config = support_channel_config
        self.owner_name = owner_name
        self.owner_uid = owner_uid
        self.code_name = code_name
        self.owner_bid = owner_bid
        self.region_id = region_id
        self.channel_policy = channel_policy
        self.request_id = request_id
        self.consortium_id = consortium_id
        self.expired_time = expired_time
        self.organization_count = organization_count
        self.consortium_name = consortium_name

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.channel_count is not None:
            result['ChannelCount'] = self.channel_count
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.state is not None:
            result['State'] = self.state
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.spec_name is not None:
            result['SpecName'] = self.spec_name
        if self.support_channel_config is not None:
            result['SupportChannelConfig'] = self.support_channel_config
        if self.owner_name is not None:
            result['OwnerName'] = self.owner_name
        if self.owner_uid is not None:
            result['OwnerUid'] = self.owner_uid
        if self.code_name is not None:
            result['CodeName'] = self.code_name
        if self.owner_bid is not None:
            result['OwnerBid'] = self.owner_bid
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.channel_policy is not None:
            result['ChannelPolicy'] = self.channel_policy
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.consortium_id is not None:
            result['ConsortiumId'] = self.consortium_id
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.organization_count is not None:
            result['OrganizationCount'] = self.organization_count
        if self.consortium_name is not None:
            result['ConsortiumName'] = self.consortium_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChannelCount') is not None:
            self.channel_count = m.get('ChannelCount')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = DescribeFabricConsortiumsResponseBodyResultTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('SpecName') is not None:
            self.spec_name = m.get('SpecName')
        if m.get('SupportChannelConfig') is not None:
            self.support_channel_config = m.get('SupportChannelConfig')
        if m.get('OwnerName') is not None:
            self.owner_name = m.get('OwnerName')
        if m.get('OwnerUid') is not None:
            self.owner_uid = m.get('OwnerUid')
        if m.get('CodeName') is not None:
            self.code_name = m.get('CodeName')
        if m.get('OwnerBid') is not None:
            self.owner_bid = m.get('OwnerBid')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ChannelPolicy') is not None:
            self.channel_policy = m.get('ChannelPolicy')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ConsortiumId') is not None:
            self.consortium_id = m.get('ConsortiumId')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('OrganizationCount') is not None:
            self.organization_count = m.get('OrganizationCount')
        if m.get('ConsortiumName') is not None:
            self.consortium_name = m.get('ConsortiumName')
        return self


class DescribeFabricConsortiumsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_code: int = None,
        success: bool = None,
        result: List[DescribeFabricConsortiumsResponseBodyResult] = None,
    ):
        self.request_id = request_id
        self.error_code = error_code
        self.success = success
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = DescribeFabricConsortiumsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class DescribeFabricConsortiumsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeFabricConsortiumsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeFabricConsortiumsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFabricConsortiumSpecsResponseBodyResult(TeaModel):
    def __init__(
        self,
        spec_name: str = None,
        spec_title: str = None,
        enable: bool = None,
    ):
        self.spec_name = spec_name
        self.spec_title = spec_title
        self.enable = enable

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.spec_name is not None:
            result['SpecName'] = self.spec_name
        if self.spec_title is not None:
            result['SpecTitle'] = self.spec_title
        if self.enable is not None:
            result['Enable'] = self.enable
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SpecName') is not None:
            self.spec_name = m.get('SpecName')
        if m.get('SpecTitle') is not None:
            self.spec_title = m.get('SpecTitle')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        return self


class DescribeFabricConsortiumSpecsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_code: int = None,
        success: bool = None,
        result: List[DescribeFabricConsortiumSpecsResponseBodyResult] = None,
    ):
        self.request_id = request_id
        self.error_code = error_code
        self.success = success
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = DescribeFabricConsortiumSpecsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class DescribeFabricConsortiumSpecsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeFabricConsortiumSpecsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeFabricConsortiumSpecsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFabricExplorerRequest(TeaModel):
    def __init__(
        self,
        organization_id: str = None,
        ex_method: str = None,
        ex_url: str = None,
        ex_body: str = None,
    ):
        self.organization_id = organization_id
        self.ex_method = ex_method
        self.ex_url = ex_url
        self.ex_body = ex_body

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.ex_method is not None:
            result['ExMethod'] = self.ex_method
        if self.ex_url is not None:
            result['ExUrl'] = self.ex_url
        if self.ex_body is not None:
            result['ExBody'] = self.ex_body
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('ExMethod') is not None:
            self.ex_method = m.get('ExMethod')
        if m.get('ExUrl') is not None:
            self.ex_url = m.get('ExUrl')
        if m.get('ExBody') is not None:
            self.ex_body = m.get('ExBody')
        return self


class DescribeFabricExplorerResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        dynamic_code: str = None,
        error_code: int = None,
        dynamic_message: str = None,
        success: bool = None,
        result: str = None,
    ):
        self.request_id = request_id
        self.dynamic_code = dynamic_code
        self.error_code = error_code
        self.dynamic_message = dynamic_message
        self.success = success
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.success is not None:
            result['Success'] = self.success
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class DescribeFabricExplorerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeFabricExplorerResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeFabricExplorerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFabricInvitationCodeRequest(TeaModel):
    def __init__(
        self,
        consortium_id: str = None,
    ):
        self.consortium_id = consortium_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.consortium_id is not None:
            result['ConsortiumId'] = self.consortium_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsortiumId') is not None:
            self.consortium_id = m.get('ConsortiumId')
        return self


class DescribeFabricInvitationCodeResponseBodyResult(TeaModel):
    def __init__(
        self,
        sender_id: int = None,
        email: str = None,
        sender_bid: str = None,
        expire_time: str = None,
        consortium_id: str = None,
        invitation_id: int = None,
        sender_name: str = None,
        code: str = None,
        url: str = None,
        accepted: bool = None,
        send_time: str = None,
    ):
        self.sender_id = sender_id
        self.email = email
        self.sender_bid = sender_bid
        self.expire_time = expire_time
        self.consortium_id = consortium_id
        self.invitation_id = invitation_id
        self.sender_name = sender_name
        self.code = code
        self.url = url
        self.accepted = accepted
        self.send_time = send_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.sender_id is not None:
            result['SenderId'] = self.sender_id
        if self.email is not None:
            result['Email'] = self.email
        if self.sender_bid is not None:
            result['SenderBid'] = self.sender_bid
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.consortium_id is not None:
            result['ConsortiumId'] = self.consortium_id
        if self.invitation_id is not None:
            result['InvitationId'] = self.invitation_id
        if self.sender_name is not None:
            result['SenderName'] = self.sender_name
        if self.code is not None:
            result['Code'] = self.code
        if self.url is not None:
            result['Url'] = self.url
        if self.accepted is not None:
            result['Accepted'] = self.accepted
        if self.send_time is not None:
            result['SendTime'] = self.send_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SenderId') is not None:
            self.sender_id = m.get('SenderId')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('SenderBid') is not None:
            self.sender_bid = m.get('SenderBid')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('ConsortiumId') is not None:
            self.consortium_id = m.get('ConsortiumId')
        if m.get('InvitationId') is not None:
            self.invitation_id = m.get('InvitationId')
        if m.get('SenderName') is not None:
            self.sender_name = m.get('SenderName')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('Accepted') is not None:
            self.accepted = m.get('Accepted')
        if m.get('SendTime') is not None:
            self.send_time = m.get('SendTime')
        return self


class DescribeFabricInvitationCodeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_code: int = None,
        success: bool = None,
        result: DescribeFabricInvitationCodeResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.error_code = error_code
        self.success = success
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Result') is not None:
            temp_model = DescribeFabricInvitationCodeResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class DescribeFabricInvitationCodeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeFabricInvitationCodeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeFabricInvitationCodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFabricInviterRequest(TeaModel):
    def __init__(
        self,
        code: str = None,
    ):
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class DescribeFabricInviterResponseBodyResult(TeaModel):
    def __init__(
        self,
        inviter_id: int = None,
        expire_time: str = None,
        consortium_id: str = None,
        inviter_name: str = None,
        consortium_name: str = None,
    ):
        self.inviter_id = inviter_id
        self.expire_time = expire_time
        self.consortium_id = consortium_id
        self.inviter_name = inviter_name
        self.consortium_name = consortium_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.inviter_id is not None:
            result['InviterId'] = self.inviter_id
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.consortium_id is not None:
            result['ConsortiumId'] = self.consortium_id
        if self.inviter_name is not None:
            result['InviterName'] = self.inviter_name
        if self.consortium_name is not None:
            result['ConsortiumName'] = self.consortium_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InviterId') is not None:
            self.inviter_id = m.get('InviterId')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('ConsortiumId') is not None:
            self.consortium_id = m.get('ConsortiumId')
        if m.get('InviterName') is not None:
            self.inviter_name = m.get('InviterName')
        if m.get('ConsortiumName') is not None:
            self.consortium_name = m.get('ConsortiumName')
        return self


class DescribeFabricInviterResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_code: int = None,
        success: bool = None,
        result: DescribeFabricInviterResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.error_code = error_code
        self.success = success
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Result') is not None:
            temp_model = DescribeFabricInviterResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class DescribeFabricInviterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeFabricInviterResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeFabricInviterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFabricOrdererLogsRequest(TeaModel):
    def __init__(
        self,
        consortium_id: str = None,
        orderer_name: str = None,
        lines: str = None,
    ):
        self.consortium_id = consortium_id
        self.orderer_name = orderer_name
        self.lines = lines

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.consortium_id is not None:
            result['ConsortiumId'] = self.consortium_id
        if self.orderer_name is not None:
            result['OrdererName'] = self.orderer_name
        if self.lines is not None:
            result['Lines'] = self.lines
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsortiumId') is not None:
            self.consortium_id = m.get('ConsortiumId')
        if m.get('OrdererName') is not None:
            self.orderer_name = m.get('OrdererName')
        if m.get('Lines') is not None:
            self.lines = m.get('Lines')
        return self


class DescribeFabricOrdererLogsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_code: int = None,
        success: bool = None,
        result: str = None,
    ):
        self.request_id = request_id
        self.error_code = error_code
        self.success = success
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class DescribeFabricOrdererLogsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeFabricOrdererLogsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeFabricOrdererLogsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFabricOrganizationRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeFabricOrganizationRequest(TeaModel):
    def __init__(
        self,
        organization_id: str = None,
        location: str = None,
        tag: List[DescribeFabricOrganizationRequestTag] = None,
    ):
        self.organization_id = organization_id
        self.location = location
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.location is not None:
            result['Location'] = self.location
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeFabricOrganizationRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeFabricOrganizationResponseBodyResultTags(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeFabricOrganizationResponseBodyResult(TeaModel):
    def __init__(
        self,
        domain: str = None,
        peer_count: int = None,
        state: str = None,
        create_time: str = None,
        consortium_count: int = None,
        tags: List[DescribeFabricOrganizationResponseBodyResultTags] = None,
        spec_name: str = None,
        owner_name: str = None,
        owner_uid: int = None,
        code_name: str = None,
        owner_bid: str = None,
        organization_description: str = None,
        region_id: str = None,
        organization_id: str = None,
        msp: str = None,
        request_id: str = None,
        caurl: str = None,
        caname: str = None,
        zone_id: str = None,
        user_count: int = None,
        organization_name: str = None,
    ):
        self.domain = domain
        self.peer_count = peer_count
        self.state = state
        self.create_time = create_time
        self.consortium_count = consortium_count
        self.tags = tags
        self.spec_name = spec_name
        self.owner_name = owner_name
        self.owner_uid = owner_uid
        self.code_name = code_name
        self.owner_bid = owner_bid
        self.organization_description = organization_description
        self.region_id = region_id
        self.organization_id = organization_id
        self.msp = msp
        self.request_id = request_id
        self.caurl = caurl
        self.caname = caname
        self.zone_id = zone_id
        self.user_count = user_count
        self.organization_name = organization_name

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.peer_count is not None:
            result['PeerCount'] = self.peer_count
        if self.state is not None:
            result['State'] = self.state
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.consortium_count is not None:
            result['ConsortiumCount'] = self.consortium_count
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.spec_name is not None:
            result['SpecName'] = self.spec_name
        if self.owner_name is not None:
            result['OwnerName'] = self.owner_name
        if self.owner_uid is not None:
            result['OwnerUid'] = self.owner_uid
        if self.code_name is not None:
            result['CodeName'] = self.code_name
        if self.owner_bid is not None:
            result['OwnerBid'] = self.owner_bid
        if self.organization_description is not None:
            result['OrganizationDescription'] = self.organization_description
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.msp is not None:
            result['MSP'] = self.msp
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.caurl is not None:
            result['CAUrl'] = self.caurl
        if self.caname is not None:
            result['CANAME'] = self.caname
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.user_count is not None:
            result['UserCount'] = self.user_count
        if self.organization_name is not None:
            result['OrganizationName'] = self.organization_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('PeerCount') is not None:
            self.peer_count = m.get('PeerCount')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ConsortiumCount') is not None:
            self.consortium_count = m.get('ConsortiumCount')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = DescribeFabricOrganizationResponseBodyResultTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('SpecName') is not None:
            self.spec_name = m.get('SpecName')
        if m.get('OwnerName') is not None:
            self.owner_name = m.get('OwnerName')
        if m.get('OwnerUid') is not None:
            self.owner_uid = m.get('OwnerUid')
        if m.get('CodeName') is not None:
            self.code_name = m.get('CodeName')
        if m.get('OwnerBid') is not None:
            self.owner_bid = m.get('OwnerBid')
        if m.get('OrganizationDescription') is not None:
            self.organization_description = m.get('OrganizationDescription')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('MSP') is not None:
            self.msp = m.get('MSP')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CAUrl') is not None:
            self.caurl = m.get('CAUrl')
        if m.get('CANAME') is not None:
            self.caname = m.get('CANAME')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('UserCount') is not None:
            self.user_count = m.get('UserCount')
        if m.get('OrganizationName') is not None:
            self.organization_name = m.get('OrganizationName')
        return self


class DescribeFabricOrganizationResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_code: int = None,
        success: bool = None,
        result: DescribeFabricOrganizationResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.error_code = error_code
        self.success = success
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Result') is not None:
            temp_model = DescribeFabricOrganizationResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class DescribeFabricOrganizationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeFabricOrganizationResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeFabricOrganizationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFabricOrganizationChaincodesRequest(TeaModel):
    def __init__(
        self,
        organization_id: str = None,
        location: str = None,
    ):
        self.organization_id = organization_id
        self.location = location

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.location is not None:
            result['Location'] = self.location
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        return self


class DescribeFabricOrganizationChaincodesResponseBodyResult(TeaModel):
    def __init__(
        self,
        endorse_policy: str = None,
        state: str = None,
        create_time: str = None,
        chaincode_id: str = None,
        message: str = None,
        chaincode_name: str = None,
        installed: str = None,
        creator: str = None,
        deploy_time: str = None,
        chaincode_version: str = None,
        channel_name: str = None,
        consortium_id: str = None,
        channel_id: str = None,
    ):
        self.endorse_policy = endorse_policy
        self.state = state
        self.create_time = create_time
        self.chaincode_id = chaincode_id
        self.message = message
        self.chaincode_name = chaincode_name
        self.installed = installed
        self.creator = creator
        self.deploy_time = deploy_time
        self.chaincode_version = chaincode_version
        self.channel_name = channel_name
        self.consortium_id = consortium_id
        self.channel_id = channel_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.endorse_policy is not None:
            result['EndorsePolicy'] = self.endorse_policy
        if self.state is not None:
            result['State'] = self.state
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.chaincode_id is not None:
            result['ChaincodeId'] = self.chaincode_id
        if self.message is not None:
            result['Message'] = self.message
        if self.chaincode_name is not None:
            result['ChaincodeName'] = self.chaincode_name
        if self.installed is not None:
            result['Installed'] = self.installed
        if self.creator is not None:
            result['Creator'] = self.creator
        if self.deploy_time is not None:
            result['DeployTime'] = self.deploy_time
        if self.chaincode_version is not None:
            result['ChaincodeVersion'] = self.chaincode_version
        if self.channel_name is not None:
            result['ChannelName'] = self.channel_name
        if self.consortium_id is not None:
            result['ConsortiumId'] = self.consortium_id
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndorsePolicy') is not None:
            self.endorse_policy = m.get('EndorsePolicy')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ChaincodeId') is not None:
            self.chaincode_id = m.get('ChaincodeId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('ChaincodeName') is not None:
            self.chaincode_name = m.get('ChaincodeName')
        if m.get('Installed') is not None:
            self.installed = m.get('Installed')
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')
        if m.get('DeployTime') is not None:
            self.deploy_time = m.get('DeployTime')
        if m.get('ChaincodeVersion') is not None:
            self.chaincode_version = m.get('ChaincodeVersion')
        if m.get('ChannelName') is not None:
            self.channel_name = m.get('ChannelName')
        if m.get('ConsortiumId') is not None:
            self.consortium_id = m.get('ConsortiumId')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        return self


class DescribeFabricOrganizationChaincodesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_code: int = None,
        success: bool = None,
        result: List[DescribeFabricOrganizationChaincodesResponseBodyResult] = None,
    ):
        self.request_id = request_id
        self.error_code = error_code
        self.success = success
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = DescribeFabricOrganizationChaincodesResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class DescribeFabricOrganizationChaincodesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeFabricOrganizationChaincodesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeFabricOrganizationChaincodesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFabricOrganizationDeletableRequest(TeaModel):
    def __init__(
        self,
        organization_id: str = None,
        location: str = None,
    ):
        self.organization_id = organization_id
        self.location = location

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.location is not None:
            result['Location'] = self.location
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        return self


class DescribeFabricOrganizationDeletableResponseBodyResult(TeaModel):
    def __init__(
        self,
        deletable: bool = None,
        domain: str = None,
        state: str = None,
        zone_id: str = None,
        organization_name: str = None,
        code_name: str = None,
        organization_description: str = None,
        region_id: str = None,
        organization_id: str = None,
    ):
        self.deletable = deletable
        self.domain = domain
        self.state = state
        self.zone_id = zone_id
        self.organization_name = organization_name
        self.code_name = code_name
        self.organization_description = organization_description
        self.region_id = region_id
        self.organization_id = organization_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.deletable is not None:
            result['Deletable'] = self.deletable
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.state is not None:
            result['State'] = self.state
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.organization_name is not None:
            result['OrganizationName'] = self.organization_name
        if self.code_name is not None:
            result['CodeName'] = self.code_name
        if self.organization_description is not None:
            result['OrganizationDescription'] = self.organization_description
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Deletable') is not None:
            self.deletable = m.get('Deletable')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('OrganizationName') is not None:
            self.organization_name = m.get('OrganizationName')
        if m.get('CodeName') is not None:
            self.code_name = m.get('CodeName')
        if m.get('OrganizationDescription') is not None:
            self.organization_description = m.get('OrganizationDescription')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class DescribeFabricOrganizationDeletableResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_code: int = None,
        success: bool = None,
        result: DescribeFabricOrganizationDeletableResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.error_code = error_code
        self.success = success
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Result') is not None:
            temp_model = DescribeFabricOrganizationDeletableResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class DescribeFabricOrganizationDeletableResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeFabricOrganizationDeletableResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeFabricOrganizationDeletableResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFabricOrganizationMembersRequest(TeaModel):
    def __init__(
        self,
        organization_id: str = None,
        location: str = None,
    ):
        self.organization_id = organization_id
        self.location = location

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.location is not None:
            result['Location'] = self.location
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        return self


class DescribeFabricOrganizationMembersResponseBodyResult(TeaModel):
    def __init__(
        self,
        domain: str = None,
        consortium_id: str = None,
        description: str = None,
        state: str = None,
        organization_name: str = None,
        joined_time: str = None,
        consortium_name: str = None,
        organization_id: str = None,
    ):
        self.domain = domain
        self.consortium_id = consortium_id
        self.description = description
        self.state = state
        self.organization_name = organization_name
        self.joined_time = joined_time
        self.consortium_name = consortium_name
        self.organization_id = organization_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.consortium_id is not None:
            result['ConsortiumId'] = self.consortium_id
        if self.description is not None:
            result['Description'] = self.description
        if self.state is not None:
            result['State'] = self.state
        if self.organization_name is not None:
            result['OrganizationName'] = self.organization_name
        if self.joined_time is not None:
            result['JoinedTime'] = self.joined_time
        if self.consortium_name is not None:
            result['ConsortiumName'] = self.consortium_name
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('ConsortiumId') is not None:
            self.consortium_id = m.get('ConsortiumId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('OrganizationName') is not None:
            self.organization_name = m.get('OrganizationName')
        if m.get('JoinedTime') is not None:
            self.joined_time = m.get('JoinedTime')
        if m.get('ConsortiumName') is not None:
            self.consortium_name = m.get('ConsortiumName')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class DescribeFabricOrganizationMembersResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_code: int = None,
        success: bool = None,
        result: List[DescribeFabricOrganizationMembersResponseBodyResult] = None,
    ):
        self.request_id = request_id
        self.error_code = error_code
        self.success = success
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = DescribeFabricOrganizationMembersResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class DescribeFabricOrganizationMembersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeFabricOrganizationMembersResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeFabricOrganizationMembersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFabricOrganizationPeersRequest(TeaModel):
    def __init__(
        self,
        organization_id: str = None,
        location: str = None,
    ):
        self.organization_id = organization_id
        self.location = location

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.location is not None:
            result['Location'] = self.location
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        return self


class DescribeFabricOrganizationPeersResponseBodyResult(TeaModel):
    def __init__(
        self,
        update_time: str = None,
        domain: str = None,
        internet_ip: str = None,
        create_time: str = None,
        is_anchor: bool = None,
        instance_type: str = None,
        port: int = None,
        organization_peer_name: str = None,
        intranet_ip: str = None,
    ):
        self.update_time = update_time
        self.domain = domain
        self.internet_ip = internet_ip
        self.create_time = create_time
        self.is_anchor = is_anchor
        self.instance_type = instance_type
        self.port = port
        self.organization_peer_name = organization_peer_name
        self.intranet_ip = intranet_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.internet_ip is not None:
            result['InternetIp'] = self.internet_ip
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.is_anchor is not None:
            result['IsAnchor'] = self.is_anchor
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.port is not None:
            result['Port'] = self.port
        if self.organization_peer_name is not None:
            result['OrganizationPeerName'] = self.organization_peer_name
        if self.intranet_ip is not None:
            result['IntranetIp'] = self.intranet_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('InternetIp') is not None:
            self.internet_ip = m.get('InternetIp')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('IsAnchor') is not None:
            self.is_anchor = m.get('IsAnchor')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('OrganizationPeerName') is not None:
            self.organization_peer_name = m.get('OrganizationPeerName')
        if m.get('IntranetIp') is not None:
            self.intranet_ip = m.get('IntranetIp')
        return self


class DescribeFabricOrganizationPeersResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_code: int = None,
        success: bool = None,
        result: List[DescribeFabricOrganizationPeersResponseBodyResult] = None,
    ):
        self.request_id = request_id
        self.error_code = error_code
        self.success = success
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = DescribeFabricOrganizationPeersResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class DescribeFabricOrganizationPeersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeFabricOrganizationPeersResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeFabricOrganizationPeersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFabricOrganizationsRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeFabricOrganizationsRequest(TeaModel):
    def __init__(
        self,
        location: str = None,
        tag: List[DescribeFabricOrganizationsRequestTag] = None,
    ):
        self.location = location
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.location is not None:
            result['Location'] = self.location
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Location') is not None:
            self.location = m.get('Location')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeFabricOrganizationsRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeFabricOrganizationsResponseBodyResultTags(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeFabricOrganizationsResponseBodyResult(TeaModel):
    def __init__(
        self,
        domain: str = None,
        peer_count: int = None,
        state: str = None,
        create_time: str = None,
        consortium_count: int = None,
        tags: List[DescribeFabricOrganizationsResponseBodyResultTags] = None,
        spec_name: str = None,
        owner_name: str = None,
        owner_uid: int = None,
        code_name: str = None,
        owner_bid: str = None,
        organization_description: str = None,
        region_id: str = None,
        organization_id: str = None,
        request_id: str = None,
        zone_id: str = None,
        user_count: int = None,
        organization_name: str = None,
    ):
        self.domain = domain
        self.peer_count = peer_count
        self.state = state
        self.create_time = create_time
        self.consortium_count = consortium_count
        self.tags = tags
        self.spec_name = spec_name
        self.owner_name = owner_name
        self.owner_uid = owner_uid
        self.code_name = code_name
        self.owner_bid = owner_bid
        self.organization_description = organization_description
        self.region_id = region_id
        self.organization_id = organization_id
        self.request_id = request_id
        self.zone_id = zone_id
        self.user_count = user_count
        self.organization_name = organization_name

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.peer_count is not None:
            result['PeerCount'] = self.peer_count
        if self.state is not None:
            result['State'] = self.state
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.consortium_count is not None:
            result['ConsortiumCount'] = self.consortium_count
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.spec_name is not None:
            result['SpecName'] = self.spec_name
        if self.owner_name is not None:
            result['OwnerName'] = self.owner_name
        if self.owner_uid is not None:
            result['OwnerUid'] = self.owner_uid
        if self.code_name is not None:
            result['CodeName'] = self.code_name
        if self.owner_bid is not None:
            result['OwnerBid'] = self.owner_bid
        if self.organization_description is not None:
            result['OrganizationDescription'] = self.organization_description
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.user_count is not None:
            result['UserCount'] = self.user_count
        if self.organization_name is not None:
            result['OrganizationName'] = self.organization_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('PeerCount') is not None:
            self.peer_count = m.get('PeerCount')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ConsortiumCount') is not None:
            self.consortium_count = m.get('ConsortiumCount')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = DescribeFabricOrganizationsResponseBodyResultTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('SpecName') is not None:
            self.spec_name = m.get('SpecName')
        if m.get('OwnerName') is not None:
            self.owner_name = m.get('OwnerName')
        if m.get('OwnerUid') is not None:
            self.owner_uid = m.get('OwnerUid')
        if m.get('CodeName') is not None:
            self.code_name = m.get('CodeName')
        if m.get('OwnerBid') is not None:
            self.owner_bid = m.get('OwnerBid')
        if m.get('OrganizationDescription') is not None:
            self.organization_description = m.get('OrganizationDescription')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('UserCount') is not None:
            self.user_count = m.get('UserCount')
        if m.get('OrganizationName') is not None:
            self.organization_name = m.get('OrganizationName')
        return self


class DescribeFabricOrganizationsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_code: int = None,
        success: bool = None,
        result: List[DescribeFabricOrganizationsResponseBodyResult] = None,
    ):
        self.request_id = request_id
        self.error_code = error_code
        self.success = success
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = DescribeFabricOrganizationsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class DescribeFabricOrganizationsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeFabricOrganizationsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeFabricOrganizationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFabricOrganizationSpecsResponseBodyResult(TeaModel):
    def __init__(
        self,
        title: str = None,
        organization_specs_name: str = None,
        enable: bool = None,
    ):
        self.title = title
        self.organization_specs_name = organization_specs_name
        self.enable = enable

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.title is not None:
            result['Title'] = self.title
        if self.organization_specs_name is not None:
            result['OrganizationSpecsName'] = self.organization_specs_name
        if self.enable is not None:
            result['Enable'] = self.enable
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('OrganizationSpecsName') is not None:
            self.organization_specs_name = m.get('OrganizationSpecsName')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        return self


class DescribeFabricOrganizationSpecsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_code: int = None,
        success: bool = None,
        result: List[DescribeFabricOrganizationSpecsResponseBodyResult] = None,
    ):
        self.request_id = request_id
        self.error_code = error_code
        self.success = success
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = DescribeFabricOrganizationSpecsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class DescribeFabricOrganizationSpecsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeFabricOrganizationSpecsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeFabricOrganizationSpecsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFabricOrganizationUsersRequest(TeaModel):
    def __init__(
        self,
        organization_id: str = None,
        location: str = None,
    ):
        self.organization_id = organization_id
        self.location = location

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.location is not None:
            result['Location'] = self.location
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        return self


class DescribeFabricOrganizationUsersResponseBodyResult(TeaModel):
    def __init__(
        self,
        expire_time: str = None,
        attrs: str = None,
        caller_bid: str = None,
        create_time: str = None,
        full_name: str = None,
        caller_uid: int = None,
        username: str = None,
        organization_id: str = None,
        region_id: str = None,
    ):
        self.expire_time = expire_time
        self.attrs = attrs
        self.caller_bid = caller_bid
        self.create_time = create_time
        self.full_name = full_name
        self.caller_uid = caller_uid
        self.username = username
        self.organization_id = organization_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.attrs is not None:
            result['Attrs'] = self.attrs
        if self.caller_bid is not None:
            result['CallerBid'] = self.caller_bid
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.full_name is not None:
            result['FullName'] = self.full_name
        if self.caller_uid is not None:
            result['CallerUid'] = self.caller_uid
        if self.username is not None:
            result['Username'] = self.username
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('Attrs') is not None:
            self.attrs = m.get('Attrs')
        if m.get('CallerBid') is not None:
            self.caller_bid = m.get('CallerBid')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('FullName') is not None:
            self.full_name = m.get('FullName')
        if m.get('CallerUid') is not None:
            self.caller_uid = m.get('CallerUid')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeFabricOrganizationUsersResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_code: int = None,
        success: bool = None,
        result: List[DescribeFabricOrganizationUsersResponseBodyResult] = None,
    ):
        self.request_id = request_id
        self.error_code = error_code
        self.success = success
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = DescribeFabricOrganizationUsersResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class DescribeFabricOrganizationUsersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeFabricOrganizationUsersResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeFabricOrganizationUsersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFabricPeerLogsRequest(TeaModel):
    def __init__(
        self,
        organization_id: str = None,
        peer_name: str = None,
        lines: str = None,
    ):
        self.organization_id = organization_id
        self.peer_name = peer_name
        self.lines = lines

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.peer_name is not None:
            result['PeerName'] = self.peer_name
        if self.lines is not None:
            result['Lines'] = self.lines
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('PeerName') is not None:
            self.peer_name = m.get('PeerName')
        if m.get('Lines') is not None:
            self.lines = m.get('Lines')
        return self


class DescribeFabricPeerLogsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_code: int = None,
        success: bool = None,
        result: str = None,
    ):
        self.request_id = request_id
        self.error_code = error_code
        self.success = success
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class DescribeFabricPeerLogsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeFabricPeerLogsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeFabricPeerLogsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRegionsRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        accept_language: str = None,
    ):
        self.region_id = region_id
        self.accept_language = accept_language

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        return self


class DescribeRegionsResponseBodyRegions(TeaModel):
    def __init__(
        self,
        local_name: str = None,
        region_endpoint: str = None,
        region_id: str = None,
    ):
        self.local_name = local_name
        self.region_endpoint = region_endpoint
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.local_name is not None:
            result['LocalName'] = self.local_name
        if self.region_endpoint is not None:
            result['RegionEndpoint'] = self.region_endpoint
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')
        if m.get('RegionEndpoint') is not None:
            self.region_endpoint = m.get('RegionEndpoint')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeRegionsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        regions: List[DescribeRegionsResponseBodyRegions] = None,
        error_code: int = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.regions = regions
        self.error_code = error_code
        self.success = success

    def validate(self):
        if self.regions:
            for k in self.regions:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Regions'] = []
        if self.regions is not None:
            for k in self.regions:
                result['Regions'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.regions = []
        if m.get('Regions') is not None:
            for k in m.get('Regions'):
                temp_model = DescribeRegionsResponseBodyRegions()
                self.regions.append(temp_model.from_map(k))
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeRegionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeRegionsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRootDomainResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_code: int = None,
        success: bool = None,
        result: str = None,
    ):
        self.request_id = request_id
        self.error_code = error_code
        self.success = success
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class DescribeRootDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeRootDomainResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeRootDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTasksResponseBodyResult(TeaModel):
    def __init__(
        self,
        action: str = None,
        result: str = None,
        sender: str = None,
        operation_type: str = None,
        handled: bool = None,
        response_time: str = None,
        target: str = None,
        task_id: int = None,
        request_time: int = None,
    ):
        self.action = action
        self.result = result
        self.sender = sender
        self.operation_type = operation_type
        self.handled = handled
        self.response_time = response_time
        self.target = target
        self.task_id = task_id
        self.request_time = request_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.result is not None:
            result['Result'] = self.result
        if self.sender is not None:
            result['Sender'] = self.sender
        if self.operation_type is not None:
            result['OperationType'] = self.operation_type
        if self.handled is not None:
            result['Handled'] = self.handled
        if self.response_time is not None:
            result['ResponseTime'] = self.response_time
        if self.target is not None:
            result['Target'] = self.target
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.request_time is not None:
            result['RequestTime'] = self.request_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Sender') is not None:
            self.sender = m.get('Sender')
        if m.get('OperationType') is not None:
            self.operation_type = m.get('OperationType')
        if m.get('Handled') is not None:
            self.handled = m.get('Handled')
        if m.get('ResponseTime') is not None:
            self.response_time = m.get('ResponseTime')
        if m.get('Target') is not None:
            self.target = m.get('Target')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('RequestTime') is not None:
            self.request_time = m.get('RequestTime')
        return self


class DescribeTasksResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_code: int = None,
        success: bool = None,
        result: List[DescribeTasksResponseBodyResult] = None,
    ):
        self.request_id = request_id
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.error_code = error_code
        self.success = success
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = DescribeTasksResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class DescribeTasksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeTasksResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DownloadFabricOrganizationSDKRequest(TeaModel):
    def __init__(
        self,
        organization_id: str = None,
        username: str = None,
        location: str = None,
    ):
        self.organization_id = organization_id
        self.username = username
        self.location = location

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.username is not None:
            result['Username'] = self.username
        if self.location is not None:
            result['Location'] = self.location
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        return self


class DownloadFabricOrganizationSDKResponseBodyResult(TeaModel):
    def __init__(
        self,
        path: str = None,
        content: str = None,
    ):
        self.path = path
        self.content = content

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.path is not None:
            result['Path'] = self.path
        if self.content is not None:
            result['Content'] = self.content
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        return self


class DownloadFabricOrganizationSDKResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_code: int = None,
        success: bool = None,
        result: List[DownloadFabricOrganizationSDKResponseBodyResult] = None,
    ):
        self.request_id = request_id
        self.error_code = error_code
        self.success = success
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = DownloadFabricOrganizationSDKResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class DownloadFabricOrganizationSDKResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DownloadFabricOrganizationSDKResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DownloadFabricOrganizationSDKResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FreezeAntChainAccountRequest(TeaModel):
    def __init__(
        self,
        ant_chain_id: str = None,
        account: str = None,
    ):
        self.ant_chain_id = ant_chain_id
        self.account = account

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.ant_chain_id is not None:
            result['AntChainId'] = self.ant_chain_id
        if self.account is not None:
            result['Account'] = self.account
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AntChainId') is not None:
            self.ant_chain_id = m.get('AntChainId')
        if m.get('Account') is not None:
            self.account = m.get('Account')
        return self


class FreezeAntChainAccountResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: str = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class FreezeAntChainAccountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: FreezeAntChainAccountResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = FreezeAntChainAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InstallFabricChaincodeRequest(TeaModel):
    def __init__(
        self,
        organization_id: str = None,
        chaincode_id: str = None,
        location: str = None,
    ):
        self.organization_id = organization_id
        self.chaincode_id = chaincode_id
        self.location = location

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.chaincode_id is not None:
            result['ChaincodeId'] = self.chaincode_id
        if self.location is not None:
            result['Location'] = self.location
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('ChaincodeId') is not None:
            self.chaincode_id = m.get('ChaincodeId')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        return self


class InstallFabricChaincodeResponseBodyResult(TeaModel):
    def __init__(
        self,
        type: int = None,
        endorse_policy: str = None,
        state: str = None,
        create_time: str = None,
        chaincode_id: str = None,
        message: str = None,
        provider_name: str = None,
        chaincode_name: str = None,
        install: bool = None,
        input: str = None,
        provider_id: str = None,
        deploy_time: str = None,
        chaincode_version: str = None,
        consortium_id: str = None,
        channel_name: str = None,
        path: str = None,
    ):
        self.type = type
        self.endorse_policy = endorse_policy
        self.state = state
        self.create_time = create_time
        self.chaincode_id = chaincode_id
        self.message = message
        self.provider_name = provider_name
        self.chaincode_name = chaincode_name
        self.install = install
        self.input = input
        self.provider_id = provider_id
        self.deploy_time = deploy_time
        self.chaincode_version = chaincode_version
        self.consortium_id = consortium_id
        self.channel_name = channel_name
        self.path = path

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.endorse_policy is not None:
            result['EndorsePolicy'] = self.endorse_policy
        if self.state is not None:
            result['State'] = self.state
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.chaincode_id is not None:
            result['ChaincodeId'] = self.chaincode_id
        if self.message is not None:
            result['Message'] = self.message
        if self.provider_name is not None:
            result['ProviderName'] = self.provider_name
        if self.chaincode_name is not None:
            result['ChaincodeName'] = self.chaincode_name
        if self.install is not None:
            result['Install'] = self.install
        if self.input is not None:
            result['Input'] = self.input
        if self.provider_id is not None:
            result['ProviderId'] = self.provider_id
        if self.deploy_time is not None:
            result['DeployTime'] = self.deploy_time
        if self.chaincode_version is not None:
            result['ChaincodeVersion'] = self.chaincode_version
        if self.consortium_id is not None:
            result['ConsortiumId'] = self.consortium_id
        if self.channel_name is not None:
            result['ChannelName'] = self.channel_name
        if self.path is not None:
            result['Path'] = self.path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('EndorsePolicy') is not None:
            self.endorse_policy = m.get('EndorsePolicy')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ChaincodeId') is not None:
            self.chaincode_id = m.get('ChaincodeId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('ProviderName') is not None:
            self.provider_name = m.get('ProviderName')
        if m.get('ChaincodeName') is not None:
            self.chaincode_name = m.get('ChaincodeName')
        if m.get('Install') is not None:
            self.install = m.get('Install')
        if m.get('Input') is not None:
            self.input = m.get('Input')
        if m.get('ProviderId') is not None:
            self.provider_id = m.get('ProviderId')
        if m.get('DeployTime') is not None:
            self.deploy_time = m.get('DeployTime')
        if m.get('ChaincodeVersion') is not None:
            self.chaincode_version = m.get('ChaincodeVersion')
        if m.get('ConsortiumId') is not None:
            self.consortium_id = m.get('ConsortiumId')
        if m.get('ChannelName') is not None:
            self.channel_name = m.get('ChannelName')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        return self


class InstallFabricChaincodeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_code: int = None,
        success: bool = None,
        result: InstallFabricChaincodeResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.error_code = error_code
        self.success = success
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Result') is not None:
            temp_model = InstallFabricChaincodeResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class InstallFabricChaincodeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: InstallFabricChaincodeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = InstallFabricChaincodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InstantiateFabricChaincodeRequest(TeaModel):
    def __init__(
        self,
        organization_id: str = None,
        chaincode_id: str = None,
        endorse_policy: str = None,
        location: str = None,
        collection_config: str = None,
    ):
        self.organization_id = organization_id
        self.chaincode_id = chaincode_id
        self.endorse_policy = endorse_policy
        self.location = location
        self.collection_config = collection_config

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.chaincode_id is not None:
            result['ChaincodeId'] = self.chaincode_id
        if self.endorse_policy is not None:
            result['EndorsePolicy'] = self.endorse_policy
        if self.location is not None:
            result['Location'] = self.location
        if self.collection_config is not None:
            result['CollectionConfig'] = self.collection_config
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('ChaincodeId') is not None:
            self.chaincode_id = m.get('ChaincodeId')
        if m.get('EndorsePolicy') is not None:
            self.endorse_policy = m.get('EndorsePolicy')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('CollectionConfig') is not None:
            self.collection_config = m.get('CollectionConfig')
        return self


class InstantiateFabricChaincodeResponseBodyResult(TeaModel):
    def __init__(
        self,
        type: int = None,
        endorse_policy: str = None,
        state: str = None,
        create_time: str = None,
        chaincode_id: str = None,
        message: str = None,
        provider_name: str = None,
        chaincode_name: str = None,
        install: bool = None,
        input: str = None,
        provider_id: str = None,
        deploy_time: str = None,
        chaincode_version: str = None,
        consortium_id: str = None,
        channel_name: str = None,
        path: str = None,
    ):
        self.type = type
        self.endorse_policy = endorse_policy
        self.state = state
        self.create_time = create_time
        self.chaincode_id = chaincode_id
        self.message = message
        self.provider_name = provider_name
        self.chaincode_name = chaincode_name
        self.install = install
        self.input = input
        self.provider_id = provider_id
        self.deploy_time = deploy_time
        self.chaincode_version = chaincode_version
        self.consortium_id = consortium_id
        self.channel_name = channel_name
        self.path = path

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.endorse_policy is not None:
            result['EndorsePolicy'] = self.endorse_policy
        if self.state is not None:
            result['State'] = self.state
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.chaincode_id is not None:
            result['ChaincodeId'] = self.chaincode_id
        if self.message is not None:
            result['Message'] = self.message
        if self.provider_name is not None:
            result['ProviderName'] = self.provider_name
        if self.chaincode_name is not None:
            result['ChaincodeName'] = self.chaincode_name
        if self.install is not None:
            result['Install'] = self.install
        if self.input is not None:
            result['Input'] = self.input
        if self.provider_id is not None:
            result['ProviderId'] = self.provider_id
        if self.deploy_time is not None:
            result['DeployTime'] = self.deploy_time
        if self.chaincode_version is not None:
            result['ChaincodeVersion'] = self.chaincode_version
        if self.consortium_id is not None:
            result['ConsortiumId'] = self.consortium_id
        if self.channel_name is not None:
            result['ChannelName'] = self.channel_name
        if self.path is not None:
            result['Path'] = self.path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('EndorsePolicy') is not None:
            self.endorse_policy = m.get('EndorsePolicy')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ChaincodeId') is not None:
            self.chaincode_id = m.get('ChaincodeId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('ProviderName') is not None:
            self.provider_name = m.get('ProviderName')
        if m.get('ChaincodeName') is not None:
            self.chaincode_name = m.get('ChaincodeName')
        if m.get('Install') is not None:
            self.install = m.get('Install')
        if m.get('Input') is not None:
            self.input = m.get('Input')
        if m.get('ProviderId') is not None:
            self.provider_id = m.get('ProviderId')
        if m.get('DeployTime') is not None:
            self.deploy_time = m.get('DeployTime')
        if m.get('ChaincodeVersion') is not None:
            self.chaincode_version = m.get('ChaincodeVersion')
        if m.get('ConsortiumId') is not None:
            self.consortium_id = m.get('ConsortiumId')
        if m.get('ChannelName') is not None:
            self.channel_name = m.get('ChannelName')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        return self


class InstantiateFabricChaincodeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_code: int = None,
        success: bool = None,
        result: InstantiateFabricChaincodeResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.error_code = error_code
        self.success = success
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Result') is not None:
            temp_model = InstantiateFabricChaincodeResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class InstantiateFabricChaincodeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: InstantiateFabricChaincodeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = InstantiateFabricChaincodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class JoinFabricChannelRequest(TeaModel):
    def __init__(
        self,
        channel_id: str = None,
        do: str = None,
        location: str = None,
    ):
        self.channel_id = channel_id
        self.do = do
        self.location = location

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.do is not None:
            result['Do'] = self.do
        if self.location is not None:
            result['Location'] = self.location
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('Do') is not None:
            self.do = m.get('Do')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        return self


class JoinFabricChannelResponseBodyResult(TeaModel):
    def __init__(
        self,
        with_peer: bool = None,
        accept_time: str = None,
        state: str = None,
        destroy_time: str = None,
        invite_time: str = None,
        channel_id: str = None,
        confirm_time: str = None,
        approve_time: str = None,
        organization_id: str = None,
    ):
        self.with_peer = with_peer
        self.accept_time = accept_time
        self.state = state
        self.destroy_time = destroy_time
        self.invite_time = invite_time
        self.channel_id = channel_id
        self.confirm_time = confirm_time
        self.approve_time = approve_time
        self.organization_id = organization_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.with_peer is not None:
            result['WithPeer'] = self.with_peer
        if self.accept_time is not None:
            result['AcceptTime'] = self.accept_time
        if self.state is not None:
            result['State'] = self.state
        if self.destroy_time is not None:
            result['DestroyTime'] = self.destroy_time
        if self.invite_time is not None:
            result['InviteTime'] = self.invite_time
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.confirm_time is not None:
            result['ConfirmTime'] = self.confirm_time
        if self.approve_time is not None:
            result['ApproveTime'] = self.approve_time
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('WithPeer') is not None:
            self.with_peer = m.get('WithPeer')
        if m.get('AcceptTime') is not None:
            self.accept_time = m.get('AcceptTime')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('DestroyTime') is not None:
            self.destroy_time = m.get('DestroyTime')
        if m.get('InviteTime') is not None:
            self.invite_time = m.get('InviteTime')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('ConfirmTime') is not None:
            self.confirm_time = m.get('ConfirmTime')
        if m.get('ApproveTime') is not None:
            self.approve_time = m.get('ApproveTime')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class JoinFabricChannelResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_code: int = None,
        success: bool = None,
        result: List[JoinFabricChannelResponseBodyResult] = None,
    ):
        self.request_id = request_id
        self.error_code = error_code
        self.success = success
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = JoinFabricChannelResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class JoinFabricChannelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: JoinFabricChannelResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = JoinFabricChannelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagResourcesRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListTagResourcesRequest(TeaModel):
    def __init__(
        self,
        resource_type: str = None,
        next_token: str = None,
        resource_id: List[str] = None,
        tag: List[ListTagResourcesRequestTag] = None,
    ):
        self.resource_type = resource_type
        self.next_token = next_token
        self.resource_id = resource_id
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListTagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponseBodyTagResources(TeaModel):
    def __init__(
        self,
        resource_type: str = None,
        tag_value: str = None,
        resource_id: str = None,
        tag_key: str = None,
    ):
        self.resource_type = resource_type
        self.tag_value = tag_value
        self.resource_id = resource_id
        self.tag_key = tag_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        return self


class ListTagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        tag_resources: List[ListTagResourcesResponseBodyTagResources] = None,
    ):
        self.next_token = next_token
        self.request_id = request_id
        self.tag_resources = tag_resources

    def validate(self):
        if self.tag_resources:
            for k in self.tag_resources:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['TagResources'] = []
        if self.tag_resources is not None:
            for k in self.tag_resources:
                result['TagResources'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.tag_resources = []
        if m.get('TagResources') is not None:
            for k in m.get('TagResources'):
                temp_model = ListTagResourcesResponseBodyTagResources()
                self.tag_resources.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListTagResourcesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListTagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResetAntChainCertificateRequest(TeaModel):
    def __init__(
        self,
        ant_chain_id: str = None,
    ):
        self.ant_chain_id = ant_chain_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.ant_chain_id is not None:
            result['AntChainId'] = self.ant_chain_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AntChainId') is not None:
            self.ant_chain_id = m.get('AntChainId')
        return self


class ResetAntChainCertificateResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: str = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class ResetAntChainCertificateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ResetAntChainCertificateResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ResetAntChainCertificateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResetAntChainUserCertificateRequest(TeaModel):
    def __init__(
        self,
        ant_chain_id: str = None,
        username: str = None,
    ):
        self.ant_chain_id = ant_chain_id
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.ant_chain_id is not None:
            result['AntChainId'] = self.ant_chain_id
        if self.username is not None:
            result['Username'] = self.username
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AntChainId') is not None:
            self.ant_chain_id = m.get('AntChainId')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        return self


class ResetAntChainUserCertificateResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: str = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class ResetAntChainUserCertificateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ResetAntChainUserCertificateResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ResetAntChainUserCertificateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResetFabricOrganizationUserPasswordRequest(TeaModel):
    def __init__(
        self,
        organization_id: str = None,
        username: str = None,
        password: str = None,
        location: str = None,
    ):
        self.organization_id = organization_id
        self.username = username
        self.password = password
        self.location = location

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.username is not None:
            result['Username'] = self.username
        if self.password is not None:
            result['Password'] = self.password
        if self.location is not None:
            result['Location'] = self.location
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        return self


class ResetFabricOrganizationUserPasswordResponseBodyResult(TeaModel):
    def __init__(
        self,
        password: str = None,
        expire_time: str = None,
        create_time: str = None,
        organization_id: str = None,
        username: str = None,
        fullname: str = None,
    ):
        self.password = password
        self.expire_time = expire_time
        self.create_time = create_time
        self.organization_id = organization_id
        self.username = username
        self.fullname = fullname

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.password is not None:
            result['Password'] = self.password
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.username is not None:
            result['Username'] = self.username
        if self.fullname is not None:
            result['Fullname'] = self.fullname
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        if m.get('Fullname') is not None:
            self.fullname = m.get('Fullname')
        return self


class ResetFabricOrganizationUserPasswordResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_code: int = None,
        success: bool = None,
        result: ResetFabricOrganizationUserPasswordResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.error_code = error_code
        self.success = success
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Result') is not None:
            temp_model = ResetFabricOrganizationUserPasswordResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class ResetFabricOrganizationUserPasswordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ResetFabricOrganizationUserPasswordResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ResetFabricOrganizationUserPasswordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SynchronizeFabricChaincodeRequest(TeaModel):
    def __init__(
        self,
        organization_id: str = None,
        chaincode_id: str = None,
    ):
        self.organization_id = organization_id
        self.chaincode_id = chaincode_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.chaincode_id is not None:
            result['ChaincodeId'] = self.chaincode_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('ChaincodeId') is not None:
            self.chaincode_id = m.get('ChaincodeId')
        return self


class SynchronizeFabricChaincodeResponseBodyResult(TeaModel):
    def __init__(
        self,
        type: int = None,
        endorse_policy: str = None,
        state: str = None,
        create_time: str = None,
        chaincode_id: str = None,
        message: str = None,
        provider_name: str = None,
        chaincode_name: str = None,
        install: bool = None,
        input: str = None,
        provider_id: str = None,
        deploy_time: str = None,
        chaincode_version: str = None,
        consortium_id: str = None,
        channel_name: str = None,
        path: str = None,
    ):
        self.type = type
        self.endorse_policy = endorse_policy
        self.state = state
        self.create_time = create_time
        self.chaincode_id = chaincode_id
        self.message = message
        self.provider_name = provider_name
        self.chaincode_name = chaincode_name
        self.install = install
        self.input = input
        self.provider_id = provider_id
        self.deploy_time = deploy_time
        self.chaincode_version = chaincode_version
        self.consortium_id = consortium_id
        self.channel_name = channel_name
        self.path = path

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.endorse_policy is not None:
            result['EndorsePolicy'] = self.endorse_policy
        if self.state is not None:
            result['State'] = self.state
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.chaincode_id is not None:
            result['ChaincodeId'] = self.chaincode_id
        if self.message is not None:
            result['Message'] = self.message
        if self.provider_name is not None:
            result['ProviderName'] = self.provider_name
        if self.chaincode_name is not None:
            result['ChaincodeName'] = self.chaincode_name
        if self.install is not None:
            result['Install'] = self.install
        if self.input is not None:
            result['Input'] = self.input
        if self.provider_id is not None:
            result['ProviderId'] = self.provider_id
        if self.deploy_time is not None:
            result['DeployTime'] = self.deploy_time
        if self.chaincode_version is not None:
            result['ChaincodeVersion'] = self.chaincode_version
        if self.consortium_id is not None:
            result['ConsortiumId'] = self.consortium_id
        if self.channel_name is not None:
            result['ChannelName'] = self.channel_name
        if self.path is not None:
            result['Path'] = self.path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('EndorsePolicy') is not None:
            self.endorse_policy = m.get('EndorsePolicy')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ChaincodeId') is not None:
            self.chaincode_id = m.get('ChaincodeId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('ProviderName') is not None:
            self.provider_name = m.get('ProviderName')
        if m.get('ChaincodeName') is not None:
            self.chaincode_name = m.get('ChaincodeName')
        if m.get('Install') is not None:
            self.install = m.get('Install')
        if m.get('Input') is not None:
            self.input = m.get('Input')
        if m.get('ProviderId') is not None:
            self.provider_id = m.get('ProviderId')
        if m.get('DeployTime') is not None:
            self.deploy_time = m.get('DeployTime')
        if m.get('ChaincodeVersion') is not None:
            self.chaincode_version = m.get('ChaincodeVersion')
        if m.get('ConsortiumId') is not None:
            self.consortium_id = m.get('ConsortiumId')
        if m.get('ChannelName') is not None:
            self.channel_name = m.get('ChannelName')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        return self


class SynchronizeFabricChaincodeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_code: int = None,
        success: bool = None,
        result: SynchronizeFabricChaincodeResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.error_code = error_code
        self.success = success
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Result') is not None:
            temp_model = SynchronizeFabricChaincodeResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class SynchronizeFabricChaincodeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SynchronizeFabricChaincodeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SynchronizeFabricChaincodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TagResourcesRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class TagResourcesRequest(TeaModel):
    def __init__(
        self,
        resource_type: str = None,
        resource_id: List[str] = None,
        tag: List[TagResourcesRequestTag] = None,
    ):
        self.resource_type = resource_type
        self.resource_id = resource_id
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = TagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class TagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_code: int = None,
        success: bool = None,
        result: bool = None,
    ):
        self.request_id = request_id
        self.error_code = error_code
        self.success = success
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class TagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: TagResourcesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = TagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnfreezeAntChainAccountRequest(TeaModel):
    def __init__(
        self,
        ant_chain_id: str = None,
        account: str = None,
    ):
        self.ant_chain_id = ant_chain_id
        self.account = account

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.ant_chain_id is not None:
            result['AntChainId'] = self.ant_chain_id
        if self.account is not None:
            result['Account'] = self.account
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AntChainId') is not None:
            self.ant_chain_id = m.get('AntChainId')
        if m.get('Account') is not None:
            self.account = m.get('Account')
        return self


class UnfreezeAntChainAccountResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: str = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class UnfreezeAntChainAccountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UnfreezeAntChainAccountResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UnfreezeAntChainAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UntagResourcesRequest(TeaModel):
    def __init__(
        self,
        resource_type: str = None,
        all: bool = None,
        resource_id: List[str] = None,
        tag_key: List[str] = None,
    ):
        self.resource_type = resource_type
        self.all = all
        self.resource_id = resource_id
        self.tag_key = tag_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.all is not None:
            result['All'] = self.all
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('All') is not None:
            self.all = m.get('All')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        return self


class UntagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_code: int = None,
        success: bool = None,
        result: bool = None,
    ):
        self.request_id = request_id
        self.error_code = error_code
        self.success = success
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class UntagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UntagResourcesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UntagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAntChainRequest(TeaModel):
    def __init__(
        self,
        ant_chain_id: str = None,
        ant_chain_name: str = None,
    ):
        self.ant_chain_id = ant_chain_id
        self.ant_chain_name = ant_chain_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.ant_chain_id is not None:
            result['AntChainId'] = self.ant_chain_id
        if self.ant_chain_name is not None:
            result['AntChainName'] = self.ant_chain_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AntChainId') is not None:
            self.ant_chain_id = m.get('AntChainId')
        if m.get('AntChainName') is not None:
            self.ant_chain_name = m.get('AntChainName')
        return self


class UpdateAntChainResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: str = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class UpdateAntChainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateAntChainResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateAntChainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAntChainConsortiumRequest(TeaModel):
    def __init__(
        self,
        consortium_id: str = None,
        consortium_name: str = None,
        consortium_description: str = None,
    ):
        self.consortium_id = consortium_id
        self.consortium_name = consortium_name
        self.consortium_description = consortium_description

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.consortium_id is not None:
            result['ConsortiumId'] = self.consortium_id
        if self.consortium_name is not None:
            result['ConsortiumName'] = self.consortium_name
        if self.consortium_description is not None:
            result['ConsortiumDescription'] = self.consortium_description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsortiumId') is not None:
            self.consortium_id = m.get('ConsortiumId')
        if m.get('ConsortiumName') is not None:
            self.consortium_name = m.get('ConsortiumName')
        if m.get('ConsortiumDescription') is not None:
            self.consortium_description = m.get('ConsortiumDescription')
        return self


class UpdateAntChainConsortiumResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: str = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class UpdateAntChainConsortiumResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateAntChainConsortiumResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateAntChainConsortiumResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAntChainContractContentRequest(TeaModel):
    def __init__(
        self,
        content_id: str = None,
        parent_content_id: str = None,
        content_name: str = None,
        content: str = None,
    ):
        self.content_id = content_id
        self.parent_content_id = parent_content_id
        self.content_name = content_name
        self.content = content

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.content_id is not None:
            result['ContentId'] = self.content_id
        if self.parent_content_id is not None:
            result['ParentContentId'] = self.parent_content_id
        if self.content_name is not None:
            result['ContentName'] = self.content_name
        if self.content is not None:
            result['Content'] = self.content
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContentId') is not None:
            self.content_id = m.get('ContentId')
        if m.get('ParentContentId') is not None:
            self.parent_content_id = m.get('ParentContentId')
        if m.get('ContentName') is not None:
            self.content_name = m.get('ContentName')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        return self


class UpdateAntChainContractContentResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: str = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class UpdateAntChainContractContentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateAntChainContractContentResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateAntChainContractContentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAntChainContractProjectRequest(TeaModel):
    def __init__(
        self,
        project_id: str = None,
        project_name: str = None,
        project_version: str = None,
        project_description: str = None,
    ):
        self.project_id = project_id
        self.project_name = project_name
        self.project_version = project_version
        self.project_description = project_description

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.project_version is not None:
            result['ProjectVersion'] = self.project_version
        if self.project_description is not None:
            result['ProjectDescription'] = self.project_description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('ProjectVersion') is not None:
            self.project_version = m.get('ProjectVersion')
        if m.get('ProjectDescription') is not None:
            self.project_description = m.get('ProjectDescription')
        return self


class UpdateAntChainContractProjectResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: str = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class UpdateAntChainContractProjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateAntChainContractProjectResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateAntChainContractProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAntChainMemberRequest(TeaModel):
    def __init__(
        self,
        member_name: str = None,
        consortium_id: str = None,
        member_id: str = None,
    ):
        self.member_name = member_name
        self.consortium_id = consortium_id
        self.member_id = member_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.member_name is not None:
            result['MemberName'] = self.member_name
        if self.consortium_id is not None:
            result['ConsortiumId'] = self.consortium_id
        if self.member_id is not None:
            result['MemberId'] = self.member_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MemberName') is not None:
            self.member_name = m.get('MemberName')
        if m.get('ConsortiumId') is not None:
            self.consortium_id = m.get('ConsortiumId')
        if m.get('MemberId') is not None:
            self.member_id = m.get('MemberId')
        return self


class UpdateAntChainMemberResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: str = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class UpdateAntChainMemberResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateAntChainMemberResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateAntChainMemberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAntChainQRCodeAuthorizationRequest(TeaModel):
    def __init__(
        self,
        ant_chain_id: str = None,
        qrcode_type: str = None,
        authorization_type: str = None,
    ):
        self.ant_chain_id = ant_chain_id
        self.qrcode_type = qrcode_type
        self.authorization_type = authorization_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.ant_chain_id is not None:
            result['AntChainId'] = self.ant_chain_id
        if self.qrcode_type is not None:
            result['QRCodeType'] = self.qrcode_type
        if self.authorization_type is not None:
            result['AuthorizationType'] = self.authorization_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AntChainId') is not None:
            self.ant_chain_id = m.get('AntChainId')
        if m.get('QRCodeType') is not None:
            self.qrcode_type = m.get('QRCodeType')
        if m.get('AuthorizationType') is not None:
            self.authorization_type = m.get('AuthorizationType')
        return self


class UpdateAntChainQRCodeAuthorizationResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: str = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class UpdateAntChainQRCodeAuthorizationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateAntChainQRCodeAuthorizationResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateAntChainQRCodeAuthorizationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpgradeFabricChaincodeRequest(TeaModel):
    def __init__(
        self,
        organization_id: str = None,
        chaincode_id: str = None,
        endorse_policy: str = None,
        location: str = None,
        collection_config: str = None,
    ):
        self.organization_id = organization_id
        self.chaincode_id = chaincode_id
        self.endorse_policy = endorse_policy
        self.location = location
        self.collection_config = collection_config

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.chaincode_id is not None:
            result['ChaincodeId'] = self.chaincode_id
        if self.endorse_policy is not None:
            result['EndorsePolicy'] = self.endorse_policy
        if self.location is not None:
            result['Location'] = self.location
        if self.collection_config is not None:
            result['CollectionConfig'] = self.collection_config
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('ChaincodeId') is not None:
            self.chaincode_id = m.get('ChaincodeId')
        if m.get('EndorsePolicy') is not None:
            self.endorse_policy = m.get('EndorsePolicy')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('CollectionConfig') is not None:
            self.collection_config = m.get('CollectionConfig')
        return self


class UpgradeFabricChaincodeResponseBodyResult(TeaModel):
    def __init__(
        self,
        type: int = None,
        endorse_policy: str = None,
        state: str = None,
        create_time: str = None,
        chaincode_id: str = None,
        message: str = None,
        provider_name: str = None,
        chaincode_name: str = None,
        install: bool = None,
        input: str = None,
        provider_id: str = None,
        deploy_time: str = None,
        chaincode_version: str = None,
        consortium_id: str = None,
        channel_name: str = None,
        path: str = None,
    ):
        self.type = type
        self.endorse_policy = endorse_policy
        self.state = state
        self.create_time = create_time
        self.chaincode_id = chaincode_id
        self.message = message
        self.provider_name = provider_name
        self.chaincode_name = chaincode_name
        self.install = install
        self.input = input
        self.provider_id = provider_id
        self.deploy_time = deploy_time
        self.chaincode_version = chaincode_version
        self.consortium_id = consortium_id
        self.channel_name = channel_name
        self.path = path

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.endorse_policy is not None:
            result['EndorsePolicy'] = self.endorse_policy
        if self.state is not None:
            result['State'] = self.state
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.chaincode_id is not None:
            result['ChaincodeId'] = self.chaincode_id
        if self.message is not None:
            result['Message'] = self.message
        if self.provider_name is not None:
            result['ProviderName'] = self.provider_name
        if self.chaincode_name is not None:
            result['ChaincodeName'] = self.chaincode_name
        if self.install is not None:
            result['Install'] = self.install
        if self.input is not None:
            result['Input'] = self.input
        if self.provider_id is not None:
            result['ProviderId'] = self.provider_id
        if self.deploy_time is not None:
            result['DeployTime'] = self.deploy_time
        if self.chaincode_version is not None:
            result['ChaincodeVersion'] = self.chaincode_version
        if self.consortium_id is not None:
            result['ConsortiumId'] = self.consortium_id
        if self.channel_name is not None:
            result['ChannelName'] = self.channel_name
        if self.path is not None:
            result['Path'] = self.path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('EndorsePolicy') is not None:
            self.endorse_policy = m.get('EndorsePolicy')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ChaincodeId') is not None:
            self.chaincode_id = m.get('ChaincodeId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('ProviderName') is not None:
            self.provider_name = m.get('ProviderName')
        if m.get('ChaincodeName') is not None:
            self.chaincode_name = m.get('ChaincodeName')
        if m.get('Install') is not None:
            self.install = m.get('Install')
        if m.get('Input') is not None:
            self.input = m.get('Input')
        if m.get('ProviderId') is not None:
            self.provider_id = m.get('ProviderId')
        if m.get('DeployTime') is not None:
            self.deploy_time = m.get('DeployTime')
        if m.get('ChaincodeVersion') is not None:
            self.chaincode_version = m.get('ChaincodeVersion')
        if m.get('ConsortiumId') is not None:
            self.consortium_id = m.get('ConsortiumId')
        if m.get('ChannelName') is not None:
            self.channel_name = m.get('ChannelName')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        return self


class UpgradeFabricChaincodeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_code: int = None,
        success: bool = None,
        result: UpgradeFabricChaincodeResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.error_code = error_code
        self.success = success
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Result') is not None:
            temp_model = UpgradeFabricChaincodeResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class UpgradeFabricChaincodeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpgradeFabricChaincodeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpgradeFabricChaincodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


