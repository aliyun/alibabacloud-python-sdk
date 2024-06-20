# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, Any, List


class ChaincodePackage(TeaModel):
    def __init__(
        self,
        chaincode_package_id: str = None,
        checksum: str = None,
        delete_time: str = None,
        deleted: bool = None,
        install_time: str = None,
        label: str = None,
        md_5sum: str = None,
        message: str = None,
        organization_id: str = None,
        oss_url: str = None,
        provider_bid: str = None,
        provider_uid: str = None,
        state: str = None,
        type: int = None,
        type_name: str = None,
        upload_time: str = None,
    ):
        self.chaincode_package_id = chaincode_package_id
        self.checksum = checksum
        self.delete_time = delete_time
        self.deleted = deleted
        self.install_time = install_time
        self.label = label
        self.md_5sum = md_5sum
        self.message = message
        self.organization_id = organization_id
        self.oss_url = oss_url
        self.provider_bid = provider_bid
        self.provider_uid = provider_uid
        self.state = state
        self.type = type
        self.type_name = type_name
        self.upload_time = upload_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.chaincode_package_id is not None:
            result['ChaincodePackageId'] = self.chaincode_package_id
        if self.checksum is not None:
            result['Checksum'] = self.checksum
        if self.delete_time is not None:
            result['DeleteTime'] = self.delete_time
        if self.deleted is not None:
            result['Deleted'] = self.deleted
        if self.install_time is not None:
            result['InstallTime'] = self.install_time
        if self.label is not None:
            result['Label'] = self.label
        if self.md_5sum is not None:
            result['Md5sum'] = self.md_5sum
        if self.message is not None:
            result['Message'] = self.message
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.oss_url is not None:
            result['OssURL'] = self.oss_url
        if self.provider_bid is not None:
            result['ProviderBid'] = self.provider_bid
        if self.provider_uid is not None:
            result['ProviderUid'] = self.provider_uid
        if self.state is not None:
            result['State'] = self.state
        if self.type is not None:
            result['Type'] = self.type
        if self.type_name is not None:
            result['TypeName'] = self.type_name
        if self.upload_time is not None:
            result['UploadTime'] = self.upload_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChaincodePackageId') is not None:
            self.chaincode_package_id = m.get('ChaincodePackageId')
        if m.get('Checksum') is not None:
            self.checksum = m.get('Checksum')
        if m.get('DeleteTime') is not None:
            self.delete_time = m.get('DeleteTime')
        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')
        if m.get('InstallTime') is not None:
            self.install_time = m.get('InstallTime')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Md5sum') is not None:
            self.md_5sum = m.get('Md5sum')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('OssURL') is not None:
            self.oss_url = m.get('OssURL')
        if m.get('ProviderBid') is not None:
            self.provider_bid = m.get('ProviderBid')
        if m.get('ProviderUid') is not None:
            self.provider_uid = m.get('ProviderUid')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('TypeName') is not None:
            self.type_name = m.get('TypeName')
        if m.get('UploadTime') is not None:
            self.upload_time = m.get('UploadTime')
        return self


class ChaincodeVO(TeaModel):
    def __init__(
        self,
        chaincode_definition_id: str = None,
        chaincode_id: str = None,
        chaincode_package_id: str = None,
        channel_id: str = None,
        channel_name: str = None,
        consortium_id: str = None,
        create_time: str = None,
        deploy_time: str = None,
        endorse_policy: str = None,
        init_required: bool = None,
        input: str = None,
        install: bool = None,
        management: bool = None,
        message: str = None,
        name: str = None,
        path: str = None,
        provider_id: str = None,
        provider_name: str = None,
        state: str = None,
        type: int = None,
        version: str = None,
    ):
        self.chaincode_definition_id = chaincode_definition_id
        self.chaincode_id = chaincode_id
        self.chaincode_package_id = chaincode_package_id
        self.channel_id = channel_id
        self.channel_name = channel_name
        self.consortium_id = consortium_id
        self.create_time = create_time
        self.deploy_time = deploy_time
        self.endorse_policy = endorse_policy
        self.init_required = init_required
        self.input = input
        self.install = install
        self.management = management
        self.message = message
        self.name = name
        self.path = path
        self.provider_id = provider_id
        self.provider_name = provider_name
        self.state = state
        self.type = type
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.chaincode_definition_id is not None:
            result['ChaincodeDefinitionId'] = self.chaincode_definition_id
        if self.chaincode_id is not None:
            result['ChaincodeId'] = self.chaincode_id
        if self.chaincode_package_id is not None:
            result['ChaincodePackageId'] = self.chaincode_package_id
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.channel_name is not None:
            result['ChannelName'] = self.channel_name
        if self.consortium_id is not None:
            result['ConsortiumId'] = self.consortium_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.deploy_time is not None:
            result['DeployTime'] = self.deploy_time
        if self.endorse_policy is not None:
            result['EndorsePolicy'] = self.endorse_policy
        if self.init_required is not None:
            result['InitRequired'] = self.init_required
        if self.input is not None:
            result['Input'] = self.input
        if self.install is not None:
            result['Install'] = self.install
        if self.management is not None:
            result['Management'] = self.management
        if self.message is not None:
            result['Message'] = self.message
        if self.name is not None:
            result['Name'] = self.name
        if self.path is not None:
            result['Path'] = self.path
        if self.provider_id is not None:
            result['ProviderId'] = self.provider_id
        if self.provider_name is not None:
            result['ProviderName'] = self.provider_name
        if self.state is not None:
            result['State'] = self.state
        if self.type is not None:
            result['Type'] = self.type
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChaincodeDefinitionId') is not None:
            self.chaincode_definition_id = m.get('ChaincodeDefinitionId')
        if m.get('ChaincodeId') is not None:
            self.chaincode_id = m.get('ChaincodeId')
        if m.get('ChaincodePackageId') is not None:
            self.chaincode_package_id = m.get('ChaincodePackageId')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('ChannelName') is not None:
            self.channel_name = m.get('ChannelName')
        if m.get('ConsortiumId') is not None:
            self.consortium_id = m.get('ConsortiumId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DeployTime') is not None:
            self.deploy_time = m.get('DeployTime')
        if m.get('EndorsePolicy') is not None:
            self.endorse_policy = m.get('EndorsePolicy')
        if m.get('InitRequired') is not None:
            self.init_required = m.get('InitRequired')
        if m.get('Input') is not None:
            self.input = m.get('Input')
        if m.get('Install') is not None:
            self.install = m.get('Install')
        if m.get('Management') is not None:
            self.management = m.get('Management')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('ProviderId') is not None:
            self.provider_id = m.get('ProviderId')
        if m.get('ProviderName') is not None:
            self.provider_name = m.get('ProviderName')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class AcceptFabricInvitationRequest(TeaModel):
    def __init__(
        self,
        code: str = None,
        is_accepted: bool = None,
    ):
        # This parameter is required.
        self.code = code
        self.is_accepted = is_accepted

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        error_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AcceptFabricInvitationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AcceptFabricInvitationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
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
        # This parameter is required.
        self.ant_chain_id = ant_chain_id
        # This parameter is required.
        self.upload_req = upload_req

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        status_code: int = None,
        body: ApplyAntChainCertificateResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ApplyAntChainCertificateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ApplyAntChainCertificateWithKeyAutoCreationRequest(TeaModel):
    def __init__(
        self,
        ant_chain_id: str = None,
        common_name: str = None,
        consortium_id: str = None,
        country_name: str = None,
        locality_name: str = None,
        organization_name: str = None,
        organization_unit_name: str = None,
        password: str = None,
        state_or_province_name: str = None,
    ):
        # This parameter is required.
        self.ant_chain_id = ant_chain_id
        # This parameter is required.
        self.common_name = common_name
        # This parameter is required.
        self.consortium_id = consortium_id
        # This parameter is required.
        self.country_name = country_name
        # This parameter is required.
        self.locality_name = locality_name
        # This parameter is required.
        self.organization_name = organization_name
        # This parameter is required.
        self.organization_unit_name = organization_unit_name
        # This parameter is required.
        self.password = password
        # This parameter is required.
        self.state_or_province_name = state_or_province_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ant_chain_id is not None:
            result['AntChainId'] = self.ant_chain_id
        if self.common_name is not None:
            result['CommonName'] = self.common_name
        if self.consortium_id is not None:
            result['ConsortiumId'] = self.consortium_id
        if self.country_name is not None:
            result['CountryName'] = self.country_name
        if self.locality_name is not None:
            result['LocalityName'] = self.locality_name
        if self.organization_name is not None:
            result['OrganizationName'] = self.organization_name
        if self.organization_unit_name is not None:
            result['OrganizationUnitName'] = self.organization_unit_name
        if self.password is not None:
            result['Password'] = self.password
        if self.state_or_province_name is not None:
            result['StateOrProvinceName'] = self.state_or_province_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AntChainId') is not None:
            self.ant_chain_id = m.get('AntChainId')
        if m.get('CommonName') is not None:
            self.common_name = m.get('CommonName')
        if m.get('ConsortiumId') is not None:
            self.consortium_id = m.get('ConsortiumId')
        if m.get('CountryName') is not None:
            self.country_name = m.get('CountryName')
        if m.get('LocalityName') is not None:
            self.locality_name = m.get('LocalityName')
        if m.get('OrganizationName') is not None:
            self.organization_name = m.get('OrganizationName')
        if m.get('OrganizationUnitName') is not None:
            self.organization_unit_name = m.get('OrganizationUnitName')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('StateOrProvinceName') is not None:
            self.state_or_province_name = m.get('StateOrProvinceName')
        return self


class ApplyAntChainCertificateWithKeyAutoCreationResponseBodyResultDownloadPath(TeaModel):
    def __init__(
        self,
        ca_crt_url: str = None,
        client_crt_url: str = None,
        sdk_url: str = None,
        trust_ca_url: str = None,
    ):
        self.ca_crt_url = ca_crt_url
        self.client_crt_url = client_crt_url
        self.sdk_url = sdk_url
        self.trust_ca_url = trust_ca_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ca_crt_url is not None:
            result['CaCrtUrl'] = self.ca_crt_url
        if self.client_crt_url is not None:
            result['ClientCrtUrl'] = self.client_crt_url
        if self.sdk_url is not None:
            result['SdkUrl'] = self.sdk_url
        if self.trust_ca_url is not None:
            result['TrustCaUrl'] = self.trust_ca_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CaCrtUrl') is not None:
            self.ca_crt_url = m.get('CaCrtUrl')
        if m.get('ClientCrtUrl') is not None:
            self.client_crt_url = m.get('ClientCrtUrl')
        if m.get('SdkUrl') is not None:
            self.sdk_url = m.get('SdkUrl')
        if m.get('TrustCaUrl') is not None:
            self.trust_ca_url = m.get('TrustCaUrl')
        return self


class ApplyAntChainCertificateWithKeyAutoCreationResponseBodyResult(TeaModel):
    def __init__(
        self,
        download_path: ApplyAntChainCertificateWithKeyAutoCreationResponseBodyResultDownloadPath = None,
        private_key: str = None,
    ):
        self.download_path = download_path
        self.private_key = private_key

    def validate(self):
        if self.download_path:
            self.download_path.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.download_path is not None:
            result['DownloadPath'] = self.download_path.to_map()
        if self.private_key is not None:
            result['PrivateKey'] = self.private_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DownloadPath') is not None:
            temp_model = ApplyAntChainCertificateWithKeyAutoCreationResponseBodyResultDownloadPath()
            self.download_path = temp_model.from_map(m['DownloadPath'])
        if m.get('PrivateKey') is not None:
            self.private_key = m.get('PrivateKey')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        status_code: int = None,
        body: ApplyAntChainCertificateWithKeyAutoCreationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ApplyAntChainCertificateWithKeyAutoCreationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ApproveFabricChaincodeDefinitionRequest(TeaModel):
    def __init__(
        self,
        chaincode_id: str = None,
        chaincode_package_id: str = None,
        location: str = None,
        organization_id: str = None,
    ):
        # This parameter is required.
        self.chaincode_id = chaincode_id
        self.chaincode_package_id = chaincode_package_id
        self.location = location
        # This parameter is required.
        self.organization_id = organization_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.chaincode_id is not None:
            result['ChaincodeId'] = self.chaincode_id
        if self.chaincode_package_id is not None:
            result['ChaincodePackageId'] = self.chaincode_package_id
        if self.location is not None:
            result['Location'] = self.location
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChaincodeId') is not None:
            self.chaincode_id = m.get('ChaincodeId')
        if m.get('ChaincodePackageId') is not None:
            self.chaincode_package_id = m.get('ChaincodePackageId')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class ApproveFabricChaincodeDefinitionResponseBody(TeaModel):
    def __init__(
        self,
        error_code: int = None,
        message: str = None,
        request_id: str = None,
        result: ChaincodeVO = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.result = result
        self.success = success

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = ChaincodeVO()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ApproveFabricChaincodeDefinitionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ApproveFabricChaincodeDefinitionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ApproveFabricChaincodeDefinitionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchAddAntChainMiniAppQRCodeAuthorizedUsersRequest(TeaModel):
    def __init__(
        self,
        ant_chain_id: str = None,
        phone_list: Dict[str, Any] = None,
    ):
        # This parameter is required.
        self.ant_chain_id = ant_chain_id
        # This parameter is required.
        self.phone_list = phone_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        # This parameter is required.
        self.ant_chain_id = ant_chain_id
        # This parameter is required.
        self.phone_list_shrink = phone_list_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        status_code: int = None,
        body: BatchAddAntChainMiniAppQRCodeAuthorizedUsersResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = BatchAddAntChainMiniAppQRCodeAuthorizedUsersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckFabricConsortiumDomainRequest(TeaModel):
    def __init__(
        self,
        domain_code: str = None,
    ):
        # This parameter is required.
        self.domain_code = domain_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        prompt: str = None,
        valid: bool = None,
    ):
        self.domain = domain
        self.prompt = prompt
        self.valid = valid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.prompt is not None:
            result['Prompt'] = self.prompt
        if self.valid is not None:
            result['Valid'] = self.valid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Prompt') is not None:
            self.prompt = m.get('Prompt')
        if m.get('Valid') is not None:
            self.valid = m.get('Valid')
        return self


class CheckFabricConsortiumDomainResponseBody(TeaModel):
    def __init__(
        self,
        error_code: int = None,
        request_id: str = None,
        result: CheckFabricConsortiumDomainResponseBodyResult = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.request_id = request_id
        self.result = result
        self.success = success

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = CheckFabricConsortiumDomainResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CheckFabricConsortiumDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CheckFabricConsortiumDomainResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CheckFabricConsortiumDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckFabricOrganizationDomainRequest(TeaModel):
    def __init__(
        self,
        domain: str = None,
        domain_code: str = None,
    ):
        self.domain = domain
        self.domain_code = domain_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.domain_code is not None:
            result['DomainCode'] = self.domain_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('DomainCode') is not None:
            self.domain_code = m.get('DomainCode')
        return self


class CheckFabricOrganizationDomainResponseBodyResult(TeaModel):
    def __init__(
        self,
        domain: str = None,
        prompt: str = None,
        valid: bool = None,
    ):
        self.domain = domain
        self.prompt = prompt
        self.valid = valid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.prompt is not None:
            result['Prompt'] = self.prompt
        if self.valid is not None:
            result['Valid'] = self.valid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Prompt') is not None:
            self.prompt = m.get('Prompt')
        if m.get('Valid') is not None:
            self.valid = m.get('Valid')
        return self


class CheckFabricOrganizationDomainResponseBody(TeaModel):
    def __init__(
        self,
        error_code: int = None,
        request_id: str = None,
        result: CheckFabricOrganizationDomainResponseBodyResult = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.request_id = request_id
        self.result = result
        self.success = success

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = CheckFabricOrganizationDomainResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CheckFabricOrganizationDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CheckFabricOrganizationDomainResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CheckFabricOrganizationDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConfirmFabricConsortiumMemberRequestOrganization(TeaModel):
    def __init__(
        self,
        organization_id: str = None,
    ):
        # This parameter is required.
        self.organization_id = organization_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        # This parameter is required.
        self.consortium_id = consortium_id
        # This parameter is required.
        self.organization = organization

    def validate(self):
        if self.organization:
            for k in self.organization:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        error_code: int = None,
        request_id: str = None,
        result: bool = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.request_id = request_id
        self.result = result
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ConfirmFabricConsortiumMemberResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ConfirmFabricConsortiumMemberResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ConfirmFabricConsortiumMemberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CopyAntChainContractProjectRequest(TeaModel):
    def __init__(
        self,
        project_description: str = None,
        project_id: str = None,
        project_name: str = None,
        project_version: str = None,
    ):
        self.project_description = project_description
        # This parameter is required.
        self.project_id = project_id
        # This parameter is required.
        self.project_name = project_name
        # This parameter is required.
        self.project_version = project_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_description is not None:
            result['ProjectDescription'] = self.project_description
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.project_version is not None:
            result['ProjectVersion'] = self.project_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectDescription') is not None:
            self.project_description = m.get('ProjectDescription')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('ProjectVersion') is not None:
            self.project_version = m.get('ProjectVersion')
        return self


class CopyAntChainContractProjectResponseBodyResult(TeaModel):
    def __init__(
        self,
        consortium_id: str = None,
        create_time: int = None,
        project_description: str = None,
        project_id: str = None,
        project_name: str = None,
        project_version: str = None,
        update_time: int = None,
    ):
        self.consortium_id = consortium_id
        self.create_time = create_time
        self.project_description = project_description
        self.project_id = project_id
        self.project_name = project_name
        self.project_version = project_version
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consortium_id is not None:
            result['ConsortiumId'] = self.consortium_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.project_description is not None:
            result['ProjectDescription'] = self.project_description
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.project_version is not None:
            result['ProjectVersion'] = self.project_version
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsortiumId') is not None:
            self.consortium_id = m.get('ConsortiumId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ProjectDescription') is not None:
            self.project_description = m.get('ProjectDescription')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('ProjectVersion') is not None:
            self.project_version = m.get('ProjectVersion')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        status_code: int = None,
        body: CopyAntChainContractProjectResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CopyAntChainContractProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAntChainAccountRequest(TeaModel):
    def __init__(
        self,
        account: str = None,
        account_pub_key: str = None,
        account_recover_pub_key: str = None,
        ant_chain_id: str = None,
    ):
        # This parameter is required.
        self.account = account
        # This parameter is required.
        self.account_pub_key = account_pub_key
        # This parameter is required.
        self.account_recover_pub_key = account_recover_pub_key
        # This parameter is required.
        self.ant_chain_id = ant_chain_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account is not None:
            result['Account'] = self.account
        if self.account_pub_key is not None:
            result['AccountPubKey'] = self.account_pub_key
        if self.account_recover_pub_key is not None:
            result['AccountRecoverPubKey'] = self.account_recover_pub_key
        if self.ant_chain_id is not None:
            result['AntChainId'] = self.ant_chain_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Account') is not None:
            self.account = m.get('Account')
        if m.get('AccountPubKey') is not None:
            self.account_pub_key = m.get('AccountPubKey')
        if m.get('AccountRecoverPubKey') is not None:
            self.account_recover_pub_key = m.get('AccountRecoverPubKey')
        if m.get('AntChainId') is not None:
            self.ant_chain_id = m.get('AntChainId')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        status_code: int = None,
        body: CreateAntChainAccountResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateAntChainAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAntChainAccountWithKeyPairAutoCreationRequest(TeaModel):
    def __init__(
        self,
        account: str = None,
        ant_chain_id: str = None,
        password: str = None,
        recover_password: str = None,
    ):
        # This parameter is required.
        self.account = account
        # This parameter is required.
        self.ant_chain_id = ant_chain_id
        # This parameter is required.
        self.password = password
        # This parameter is required.
        self.recover_password = recover_password

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account is not None:
            result['Account'] = self.account
        if self.ant_chain_id is not None:
            result['AntChainId'] = self.ant_chain_id
        if self.password is not None:
            result['Password'] = self.password
        if self.recover_password is not None:
            result['RecoverPassword'] = self.recover_password
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Account') is not None:
            self.account = m.get('Account')
        if m.get('AntChainId') is not None:
            self.ant_chain_id = m.get('AntChainId')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('RecoverPassword') is not None:
            self.recover_password = m.get('RecoverPassword')
        return self


class CreateAntChainAccountWithKeyPairAutoCreationResponseBodyResult(TeaModel):
    def __init__(
        self,
        account: str = None,
        account_private_key: str = None,
        account_public_key: str = None,
        account_recover_private_key: str = None,
        account_recover_public_key: str = None,
        ant_chain_id: str = None,
    ):
        self.account = account
        self.account_private_key = account_private_key
        self.account_public_key = account_public_key
        self.account_recover_private_key = account_recover_private_key
        self.account_recover_public_key = account_recover_public_key
        self.ant_chain_id = ant_chain_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account is not None:
            result['Account'] = self.account
        if self.account_private_key is not None:
            result['AccountPrivateKey'] = self.account_private_key
        if self.account_public_key is not None:
            result['AccountPublicKey'] = self.account_public_key
        if self.account_recover_private_key is not None:
            result['AccountRecoverPrivateKey'] = self.account_recover_private_key
        if self.account_recover_public_key is not None:
            result['AccountRecoverPublicKey'] = self.account_recover_public_key
        if self.ant_chain_id is not None:
            result['AntChainId'] = self.ant_chain_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Account') is not None:
            self.account = m.get('Account')
        if m.get('AccountPrivateKey') is not None:
            self.account_private_key = m.get('AccountPrivateKey')
        if m.get('AccountPublicKey') is not None:
            self.account_public_key = m.get('AccountPublicKey')
        if m.get('AccountRecoverPrivateKey') is not None:
            self.account_recover_private_key = m.get('AccountRecoverPrivateKey')
        if m.get('AccountRecoverPublicKey') is not None:
            self.account_recover_public_key = m.get('AccountRecoverPublicKey')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        status_code: int = None,
        body: CreateAntChainAccountWithKeyPairAutoCreationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateAntChainAccountWithKeyPairAutoCreationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAntChainConsortiumRequest(TeaModel):
    def __init__(
        self,
        consortium_description: str = None,
        consortium_name: str = None,
    ):
        self.consortium_description = consortium_description
        # This parameter is required.
        self.consortium_name = consortium_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consortium_description is not None:
            result['ConsortiumDescription'] = self.consortium_description
        if self.consortium_name is not None:
            result['ConsortiumName'] = self.consortium_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsortiumDescription') is not None:
            self.consortium_description = m.get('ConsortiumDescription')
        if m.get('ConsortiumName') is not None:
            self.consortium_name = m.get('ConsortiumName')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        status_code: int = None,
        body: CreateAntChainConsortiumResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateAntChainConsortiumResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAntChainContractContentRequest(TeaModel):
    def __init__(
        self,
        content: str = None,
        content_name: str = None,
        is_directory: bool = None,
        parent_content_id: str = None,
        project_id: str = None,
    ):
        self.content = content
        # This parameter is required.
        self.content_name = content_name
        # This parameter is required.
        self.is_directory = is_directory
        self.parent_content_id = parent_content_id
        # This parameter is required.
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.content_name is not None:
            result['ContentName'] = self.content_name
        if self.is_directory is not None:
            result['IsDirectory'] = self.is_directory
        if self.parent_content_id is not None:
            result['ParentContentId'] = self.parent_content_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('ContentName') is not None:
            self.content_name = m.get('ContentName')
        if m.get('IsDirectory') is not None:
            self.is_directory = m.get('IsDirectory')
        if m.get('ParentContentId') is not None:
            self.parent_content_id = m.get('ParentContentId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class CreateAntChainContractContentResponseBodyResult(TeaModel):
    def __init__(
        self,
        content: str = None,
        content_id: str = None,
        content_name: str = None,
        create_time: str = None,
        is_directory: bool = None,
        parent_content_id: str = None,
        project_id: str = None,
        update_time: str = None,
    ):
        self.content = content
        self.content_id = content_id
        self.content_name = content_name
        self.create_time = create_time
        self.is_directory = is_directory
        self.parent_content_id = parent_content_id
        self.project_id = project_id
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.content_id is not None:
            result['ContentId'] = self.content_id
        if self.content_name is not None:
            result['ContentName'] = self.content_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.is_directory is not None:
            result['IsDirectory'] = self.is_directory
        if self.parent_content_id is not None:
            result['ParentContentId'] = self.parent_content_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('ContentId') is not None:
            self.content_id = m.get('ContentId')
        if m.get('ContentName') is not None:
            self.content_name = m.get('ContentName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('IsDirectory') is not None:
            self.is_directory = m.get('IsDirectory')
        if m.get('ParentContentId') is not None:
            self.parent_content_id = m.get('ParentContentId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        status_code: int = None,
        body: CreateAntChainContractContentResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateAntChainContractContentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAntChainContractProjectRequest(TeaModel):
    def __init__(
        self,
        consortium_id: str = None,
        project_description: str = None,
        project_name: str = None,
        project_version: str = None,
    ):
        # This parameter is required.
        self.consortium_id = consortium_id
        self.project_description = project_description
        # This parameter is required.
        self.project_name = project_name
        # This parameter is required.
        self.project_version = project_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consortium_id is not None:
            result['ConsortiumId'] = self.consortium_id
        if self.project_description is not None:
            result['ProjectDescription'] = self.project_description
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.project_version is not None:
            result['ProjectVersion'] = self.project_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsortiumId') is not None:
            self.consortium_id = m.get('ConsortiumId')
        if m.get('ProjectDescription') is not None:
            self.project_description = m.get('ProjectDescription')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('ProjectVersion') is not None:
            self.project_version = m.get('ProjectVersion')
        return self


class CreateAntChainContractProjectResponseBodyResult(TeaModel):
    def __init__(
        self,
        consortium_id: str = None,
        create_time: int = None,
        project_description: str = None,
        project_id: str = None,
        project_name: str = None,
        project_version: str = None,
        update_time: int = None,
    ):
        self.consortium_id = consortium_id
        self.create_time = create_time
        self.project_description = project_description
        self.project_id = project_id
        self.project_name = project_name
        self.project_version = project_version
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consortium_id is not None:
            result['ConsortiumId'] = self.consortium_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.project_description is not None:
            result['ProjectDescription'] = self.project_description
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.project_version is not None:
            result['ProjectVersion'] = self.project_version
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsortiumId') is not None:
            self.consortium_id = m.get('ConsortiumId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ProjectDescription') is not None:
            self.project_description = m.get('ProjectDescription')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('ProjectVersion') is not None:
            self.project_version = m.get('ProjectVersion')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        status_code: int = None,
        body: CreateAntChainContractProjectResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateAntChainContractProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAntChainKmsAccountNewRequest(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

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


class CreateAntChainKmsAccountNewResponseBodyResult(TeaModel):
    def __init__(
        self,
        my_kms_key_id: str = None,
        pub_key: str = None,
    ):
        self.my_kms_key_id = my_kms_key_id
        self.pub_key = pub_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.my_kms_key_id is not None:
            result['MyKmsKeyId'] = self.my_kms_key_id
        if self.pub_key is not None:
            result['PubKey'] = self.pub_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MyKmsKeyId') is not None:
            self.my_kms_key_id = m.get('MyKmsKeyId')
        if m.get('PubKey') is not None:
            self.pub_key = m.get('PubKey')
        return self


class CreateAntChainKmsAccountNewResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: str = None,
        message: str = None,
        request_id: str = None,
        result: CreateAntChainKmsAccountNewResponseBodyResult = None,
        result_code: str = None,
        result_message: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.result = result
        self.result_code = result_code
        self.result_message = result_message
        self.success = success

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        if self.result_message is not None:
            result['ResultMessage'] = self.result_message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = CreateAntChainKmsAccountNewResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateAntChainKmsAccountNewResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateAntChainKmsAccountNewResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateAntChainKmsAccountNewResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFabricChaincodeRequest(TeaModel):
    def __init__(
        self,
        channel_id: str = None,
        consortium_id: str = None,
        endorse_policy: str = None,
        location: str = None,
        organization_id: str = None,
        oss_bucket: str = None,
        oss_url: str = None,
    ):
        # This parameter is required.
        self.channel_id = channel_id
        # This parameter is required.
        self.consortium_id = consortium_id
        self.endorse_policy = endorse_policy
        self.location = location
        # This parameter is required.
        self.organization_id = organization_id
        # This parameter is required.
        self.oss_bucket = oss_bucket
        # This parameter is required.
        self.oss_url = oss_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.consortium_id is not None:
            result['ConsortiumId'] = self.consortium_id
        if self.endorse_policy is not None:
            result['EndorsePolicy'] = self.endorse_policy
        if self.location is not None:
            result['Location'] = self.location
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.oss_bucket is not None:
            result['OssBucket'] = self.oss_bucket
        if self.oss_url is not None:
            result['OssUrl'] = self.oss_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('ConsortiumId') is not None:
            self.consortium_id = m.get('ConsortiumId')
        if m.get('EndorsePolicy') is not None:
            self.endorse_policy = m.get('EndorsePolicy')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('OssBucket') is not None:
            self.oss_bucket = m.get('OssBucket')
        if m.get('OssUrl') is not None:
            self.oss_url = m.get('OssUrl')
        return self


class CreateFabricChaincodeResponseBodyResult(TeaModel):
    def __init__(
        self,
        chaincode_id: str = None,
        chaincode_name: str = None,
        chaincode_version: str = None,
        channel_name: str = None,
        consortium_id: str = None,
        create_time: str = None,
        deploy_time: str = None,
        endorse_policy: str = None,
        input: str = None,
        install: bool = None,
        message: str = None,
        path: str = None,
        provider_id: str = None,
        provider_name: str = None,
        state: str = None,
        type: int = None,
    ):
        self.chaincode_id = chaincode_id
        self.chaincode_name = chaincode_name
        self.chaincode_version = chaincode_version
        self.channel_name = channel_name
        self.consortium_id = consortium_id
        self.create_time = create_time
        self.deploy_time = deploy_time
        self.endorse_policy = endorse_policy
        self.input = input
        self.install = install
        self.message = message
        self.path = path
        self.provider_id = provider_id
        self.provider_name = provider_name
        self.state = state
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.chaincode_id is not None:
            result['ChaincodeId'] = self.chaincode_id
        if self.chaincode_name is not None:
            result['ChaincodeName'] = self.chaincode_name
        if self.chaincode_version is not None:
            result['ChaincodeVersion'] = self.chaincode_version
        if self.channel_name is not None:
            result['ChannelName'] = self.channel_name
        if self.consortium_id is not None:
            result['ConsortiumId'] = self.consortium_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.deploy_time is not None:
            result['DeployTime'] = self.deploy_time
        if self.endorse_policy is not None:
            result['EndorsePolicy'] = self.endorse_policy
        if self.input is not None:
            result['Input'] = self.input
        if self.install is not None:
            result['Install'] = self.install
        if self.message is not None:
            result['Message'] = self.message
        if self.path is not None:
            result['Path'] = self.path
        if self.provider_id is not None:
            result['ProviderId'] = self.provider_id
        if self.provider_name is not None:
            result['ProviderName'] = self.provider_name
        if self.state is not None:
            result['State'] = self.state
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChaincodeId') is not None:
            self.chaincode_id = m.get('ChaincodeId')
        if m.get('ChaincodeName') is not None:
            self.chaincode_name = m.get('ChaincodeName')
        if m.get('ChaincodeVersion') is not None:
            self.chaincode_version = m.get('ChaincodeVersion')
        if m.get('ChannelName') is not None:
            self.channel_name = m.get('ChannelName')
        if m.get('ConsortiumId') is not None:
            self.consortium_id = m.get('ConsortiumId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DeployTime') is not None:
            self.deploy_time = m.get('DeployTime')
        if m.get('EndorsePolicy') is not None:
            self.endorse_policy = m.get('EndorsePolicy')
        if m.get('Input') is not None:
            self.input = m.get('Input')
        if m.get('Install') is not None:
            self.install = m.get('Install')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('ProviderId') is not None:
            self.provider_id = m.get('ProviderId')
        if m.get('ProviderName') is not None:
            self.provider_name = m.get('ProviderName')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreateFabricChaincodeResponseBody(TeaModel):
    def __init__(
        self,
        error_code: int = None,
        request_id: str = None,
        result: CreateFabricChaincodeResponseBodyResult = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.request_id = request_id
        self.result = result
        self.success = success

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = CreateFabricChaincodeResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateFabricChaincodeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateFabricChaincodeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateFabricChaincodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFabricChaincodePackageRequest(TeaModel):
    def __init__(
        self,
        location: str = None,
        organization_id: str = None,
        oss_url: str = None,
    ):
        self.location = location
        # This parameter is required.
        self.organization_id = organization_id
        # This parameter is required.
        self.oss_url = oss_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.location is not None:
            result['Location'] = self.location
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.oss_url is not None:
            result['OssUrl'] = self.oss_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('OssUrl') is not None:
            self.oss_url = m.get('OssUrl')
        return self


class CreateFabricChaincodePackageResponseBody(TeaModel):
    def __init__(
        self,
        error_code: int = None,
        message: str = None,
        request_id: str = None,
        result: ChaincodePackage = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.result = result
        self.success = success

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = ChaincodePackage()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateFabricChaincodePackageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateFabricChaincodePackageResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateFabricChaincodePackageResponseBody()
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        batch_timeout: int = None,
        channel_name: str = None,
        consortium_id: str = None,
        max_message_count: int = None,
        organization: List[CreateFabricChannelRequestOrganization] = None,
        preferred_max_bytes: int = None,
    ):
        self.batch_timeout = batch_timeout
        # This parameter is required.
        self.channel_name = channel_name
        # This parameter is required.
        self.consortium_id = consortium_id
        self.max_message_count = max_message_count
        # This parameter is required.
        self.organization = organization
        self.preferred_max_bytes = preferred_max_bytes

    def validate(self):
        if self.organization:
            for k in self.organization:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.batch_timeout is not None:
            result['BatchTimeout'] = self.batch_timeout
        if self.channel_name is not None:
            result['ChannelName'] = self.channel_name
        if self.consortium_id is not None:
            result['ConsortiumId'] = self.consortium_id
        if self.max_message_count is not None:
            result['MaxMessageCount'] = self.max_message_count
        result['Organization'] = []
        if self.organization is not None:
            for k in self.organization:
                result['Organization'].append(k.to_map() if k else None)
        if self.preferred_max_bytes is not None:
            result['PreferredMaxBytes'] = self.preferred_max_bytes
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BatchTimeout') is not None:
            self.batch_timeout = m.get('BatchTimeout')
        if m.get('ChannelName') is not None:
            self.channel_name = m.get('ChannelName')
        if m.get('ConsortiumId') is not None:
            self.consortium_id = m.get('ConsortiumId')
        if m.get('MaxMessageCount') is not None:
            self.max_message_count = m.get('MaxMessageCount')
        self.organization = []
        if m.get('Organization') is not None:
            for k in m.get('Organization'):
                temp_model = CreateFabricChannelRequestOrganization()
                self.organization.append(temp_model.from_map(k))
        if m.get('PreferredMaxBytes') is not None:
            self.preferred_max_bytes = m.get('PreferredMaxBytes')
        return self


class CreateFabricChannelResponseBodyResult(TeaModel):
    def __init__(
        self,
        batch_timeout: int = None,
        block_count: int = None,
        chaincode_count: int = None,
        channel_id: str = None,
        channel_name: str = None,
        consortium_id: str = None,
        consortium_name: str = None,
        create_time: str = None,
        max_message_count: int = None,
        member_count: int = None,
        owner_bid: str = None,
        owner_name: str = None,
        owner_uid: int = None,
        preferred_max_bytes: int = None,
        request_id: str = None,
        state: str = None,
        support_config: bool = None,
        update_time: str = None,
    ):
        self.batch_timeout = batch_timeout
        self.block_count = block_count
        self.chaincode_count = chaincode_count
        self.channel_id = channel_id
        self.channel_name = channel_name
        self.consortium_id = consortium_id
        self.consortium_name = consortium_name
        self.create_time = create_time
        self.max_message_count = max_message_count
        self.member_count = member_count
        self.owner_bid = owner_bid
        self.owner_name = owner_name
        self.owner_uid = owner_uid
        self.preferred_max_bytes = preferred_max_bytes
        self.request_id = request_id
        self.state = state
        self.support_config = support_config
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.batch_timeout is not None:
            result['BatchTimeout'] = self.batch_timeout
        if self.block_count is not None:
            result['BlockCount'] = self.block_count
        if self.chaincode_count is not None:
            result['ChaincodeCount'] = self.chaincode_count
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.channel_name is not None:
            result['ChannelName'] = self.channel_name
        if self.consortium_id is not None:
            result['ConsortiumId'] = self.consortium_id
        if self.consortium_name is not None:
            result['ConsortiumName'] = self.consortium_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.max_message_count is not None:
            result['MaxMessageCount'] = self.max_message_count
        if self.member_count is not None:
            result['MemberCount'] = self.member_count
        if self.owner_bid is not None:
            result['OwnerBid'] = self.owner_bid
        if self.owner_name is not None:
            result['OwnerName'] = self.owner_name
        if self.owner_uid is not None:
            result['OwnerUid'] = self.owner_uid
        if self.preferred_max_bytes is not None:
            result['PreferredMaxBytes'] = self.preferred_max_bytes
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.state is not None:
            result['State'] = self.state
        if self.support_config is not None:
            result['SupportConfig'] = self.support_config
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BatchTimeout') is not None:
            self.batch_timeout = m.get('BatchTimeout')
        if m.get('BlockCount') is not None:
            self.block_count = m.get('BlockCount')
        if m.get('ChaincodeCount') is not None:
            self.chaincode_count = m.get('ChaincodeCount')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('ChannelName') is not None:
            self.channel_name = m.get('ChannelName')
        if m.get('ConsortiumId') is not None:
            self.consortium_id = m.get('ConsortiumId')
        if m.get('ConsortiumName') is not None:
            self.consortium_name = m.get('ConsortiumName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('MaxMessageCount') is not None:
            self.max_message_count = m.get('MaxMessageCount')
        if m.get('MemberCount') is not None:
            self.member_count = m.get('MemberCount')
        if m.get('OwnerBid') is not None:
            self.owner_bid = m.get('OwnerBid')
        if m.get('OwnerName') is not None:
            self.owner_name = m.get('OwnerName')
        if m.get('OwnerUid') is not None:
            self.owner_uid = m.get('OwnerUid')
        if m.get('PreferredMaxBytes') is not None:
            self.preferred_max_bytes = m.get('PreferredMaxBytes')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('SupportConfig') is not None:
            self.support_config = m.get('SupportConfig')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class CreateFabricChannelResponseBody(TeaModel):
    def __init__(
        self,
        error_code: int = None,
        request_id: str = None,
        result: CreateFabricChannelResponseBodyResult = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.request_id = request_id
        self.result = result
        self.success = success

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = CreateFabricChannelResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateFabricChannelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateFabricChannelResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateFabricChannelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFabricChannelMemberRequestOrganization(TeaModel):
    def __init__(
        self,
        organization_id: str = None,
    ):
        # This parameter is required.
        self.organization_id = organization_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        # This parameter is required.
        self.channel_id = channel_id
        # This parameter is required.
        self.organization = organization

    def validate(self):
        if self.organization:
            for k in self.organization:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        error_code: int = None,
        request_id: str = None,
        result: bool = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.request_id = request_id
        self.result = result
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateFabricChannelMemberResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateFabricChannelMemberResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        channel_policy: str = None,
        consortium_description: str = None,
        consortium_name: str = None,
        domain: str = None,
        location: str = None,
        orderer_type: str = None,
        orderers_count: int = None,
        organization: List[CreateFabricConsortiumRequestOrganization] = None,
        payment_duration: int = None,
        payment_duration_unit: str = None,
        peers_count: int = None,
        spec_name: str = None,
        zone_id: str = None,
    ):
        # This parameter is required.
        self.channel_policy = channel_policy
        self.consortium_description = consortium_description
        # This parameter is required.
        self.consortium_name = consortium_name
        # This parameter is required.
        self.domain = domain
        # This parameter is required.
        self.location = location
        # This parameter is required.
        self.orderer_type = orderer_type
        self.orderers_count = orderers_count
        self.organization = organization
        # This parameter is required.
        self.payment_duration = payment_duration
        # This parameter is required.
        self.payment_duration_unit = payment_duration_unit
        self.peers_count = peers_count
        # This parameter is required.
        self.spec_name = spec_name
        self.zone_id = zone_id

    def validate(self):
        if self.organization:
            for k in self.organization:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel_policy is not None:
            result['ChannelPolicy'] = self.channel_policy
        if self.consortium_description is not None:
            result['ConsortiumDescription'] = self.consortium_description
        if self.consortium_name is not None:
            result['ConsortiumName'] = self.consortium_name
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.location is not None:
            result['Location'] = self.location
        if self.orderer_type is not None:
            result['OrdererType'] = self.orderer_type
        if self.orderers_count is not None:
            result['OrderersCount'] = self.orderers_count
        result['Organization'] = []
        if self.organization is not None:
            for k in self.organization:
                result['Organization'].append(k.to_map() if k else None)
        if self.payment_duration is not None:
            result['PaymentDuration'] = self.payment_duration
        if self.payment_duration_unit is not None:
            result['PaymentDurationUnit'] = self.payment_duration_unit
        if self.peers_count is not None:
            result['PeersCount'] = self.peers_count
        if self.spec_name is not None:
            result['SpecName'] = self.spec_name
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChannelPolicy') is not None:
            self.channel_policy = m.get('ChannelPolicy')
        if m.get('ConsortiumDescription') is not None:
            self.consortium_description = m.get('ConsortiumDescription')
        if m.get('ConsortiumName') is not None:
            self.consortium_name = m.get('ConsortiumName')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('OrdererType') is not None:
            self.orderer_type = m.get('OrdererType')
        if m.get('OrderersCount') is not None:
            self.orderers_count = m.get('OrderersCount')
        self.organization = []
        if m.get('Organization') is not None:
            for k in m.get('Organization'):
                temp_model = CreateFabricConsortiumRequestOrganization()
                self.organization.append(temp_model.from_map(k))
        if m.get('PaymentDuration') is not None:
            self.payment_duration = m.get('PaymentDuration')
        if m.get('PaymentDurationUnit') is not None:
            self.payment_duration_unit = m.get('PaymentDurationUnit')
        if m.get('PeersCount') is not None:
            self.peers_count = m.get('PeersCount')
        if m.get('SpecName') is not None:
            self.spec_name = m.get('SpecName')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class CreateFabricConsortiumResponseBodyResult(TeaModel):
    def __init__(
        self,
        channel_count: int = None,
        channel_policy: str = None,
        cluster_state: str = None,
        code_name: str = None,
        consortium_id: str = None,
        consortium_name: str = None,
        create_time: str = None,
        description: str = None,
        domain: str = None,
        member_count: int = None,
        orderer_count: int = None,
        orderer_type: str = None,
        owner_bid: str = None,
        owner_uid: int = None,
        region_id: str = None,
        service_state: str = None,
        spec_name: str = None,
        zone_id: str = None,
    ):
        self.channel_count = channel_count
        self.channel_policy = channel_policy
        self.cluster_state = cluster_state
        self.code_name = code_name
        self.consortium_id = consortium_id
        self.consortium_name = consortium_name
        self.create_time = create_time
        self.description = description
        self.domain = domain
        self.member_count = member_count
        self.orderer_count = orderer_count
        self.orderer_type = orderer_type
        self.owner_bid = owner_bid
        self.owner_uid = owner_uid
        self.region_id = region_id
        self.service_state = service_state
        self.spec_name = spec_name
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel_count is not None:
            result['ChannelCount'] = self.channel_count
        if self.channel_policy is not None:
            result['ChannelPolicy'] = self.channel_policy
        if self.cluster_state is not None:
            result['ClusterState'] = self.cluster_state
        if self.code_name is not None:
            result['CodeName'] = self.code_name
        if self.consortium_id is not None:
            result['ConsortiumId'] = self.consortium_id
        if self.consortium_name is not None:
            result['ConsortiumName'] = self.consortium_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.member_count is not None:
            result['MemberCount'] = self.member_count
        if self.orderer_count is not None:
            result['OrdererCount'] = self.orderer_count
        if self.orderer_type is not None:
            result['OrdererType'] = self.orderer_type
        if self.owner_bid is not None:
            result['OwnerBid'] = self.owner_bid
        if self.owner_uid is not None:
            result['OwnerUid'] = self.owner_uid
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.service_state is not None:
            result['ServiceState'] = self.service_state
        if self.spec_name is not None:
            result['SpecName'] = self.spec_name
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChannelCount') is not None:
            self.channel_count = m.get('ChannelCount')
        if m.get('ChannelPolicy') is not None:
            self.channel_policy = m.get('ChannelPolicy')
        if m.get('ClusterState') is not None:
            self.cluster_state = m.get('ClusterState')
        if m.get('CodeName') is not None:
            self.code_name = m.get('CodeName')
        if m.get('ConsortiumId') is not None:
            self.consortium_id = m.get('ConsortiumId')
        if m.get('ConsortiumName') is not None:
            self.consortium_name = m.get('ConsortiumName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('MemberCount') is not None:
            self.member_count = m.get('MemberCount')
        if m.get('OrdererCount') is not None:
            self.orderer_count = m.get('OrdererCount')
        if m.get('OrdererType') is not None:
            self.orderer_type = m.get('OrdererType')
        if m.get('OwnerBid') is not None:
            self.owner_bid = m.get('OwnerBid')
        if m.get('OwnerUid') is not None:
            self.owner_uid = m.get('OwnerUid')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceState') is not None:
            self.service_state = m.get('ServiceState')
        if m.get('SpecName') is not None:
            self.spec_name = m.get('SpecName')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class CreateFabricConsortiumResponseBody(TeaModel):
    def __init__(
        self,
        error_code: int = None,
        request_id: str = None,
        result: CreateFabricConsortiumResponseBodyResult = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.request_id = request_id
        self.result = result
        self.success = success

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = CreateFabricConsortiumResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateFabricConsortiumResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateFabricConsortiumResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        code: str = None,
        consortium_id: str = None,
        organization: List[CreateFabricConsortiumMemberRequestOrganization] = None,
    ):
        # This parameter is required.
        self.code = code
        # This parameter is required.
        self.consortium_id = consortium_id
        # This parameter is required.
        self.organization = organization

    def validate(self):
        if self.organization:
            for k in self.organization:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.consortium_id is not None:
            result['ConsortiumId'] = self.consortium_id
        result['Organization'] = []
        if self.organization is not None:
            for k in self.organization:
                result['Organization'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ConsortiumId') is not None:
            self.consortium_id = m.get('ConsortiumId')
        self.organization = []
        if m.get('Organization') is not None:
            for k in m.get('Organization'):
                temp_model = CreateFabricConsortiumMemberRequestOrganization()
                self.organization.append(temp_model.from_map(k))
        return self


class CreateFabricConsortiumMemberResponseBody(TeaModel):
    def __init__(
        self,
        error_code: int = None,
        request_id: str = None,
        result: bool = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.request_id = request_id
        self.result = result
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateFabricConsortiumMemberResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateFabricConsortiumMemberResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateFabricConsortiumMemberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFabricOrganizationRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        domain: str = None,
        location: str = None,
        organization_name: str = None,
        payment_duration: int = None,
        payment_duration_unit: str = None,
        peers_count: int = None,
        spec_name: str = None,
    ):
        self.description = description
        # This parameter is required.
        self.domain = domain
        # This parameter is required.
        self.location = location
        # This parameter is required.
        self.organization_name = organization_name
        # This parameter is required.
        self.payment_duration = payment_duration
        # This parameter is required.
        self.payment_duration_unit = payment_duration_unit
        self.peers_count = peers_count
        # This parameter is required.
        self.spec_name = spec_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.location is not None:
            result['Location'] = self.location
        if self.organization_name is not None:
            result['OrganizationName'] = self.organization_name
        if self.payment_duration is not None:
            result['PaymentDuration'] = self.payment_duration
        if self.payment_duration_unit is not None:
            result['PaymentDurationUnit'] = self.payment_duration_unit
        if self.peers_count is not None:
            result['PeersCount'] = self.peers_count
        if self.spec_name is not None:
            result['SpecName'] = self.spec_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('OrganizationName') is not None:
            self.organization_name = m.get('OrganizationName')
        if m.get('PaymentDuration') is not None:
            self.payment_duration = m.get('PaymentDuration')
        if m.get('PaymentDurationUnit') is not None:
            self.payment_duration_unit = m.get('PaymentDurationUnit')
        if m.get('PeersCount') is not None:
            self.peers_count = m.get('PeersCount')
        if m.get('SpecName') is not None:
            self.spec_name = m.get('SpecName')
        return self


class CreateFabricOrganizationResponseBodyResult(TeaModel):
    def __init__(
        self,
        cluster_state: str = None,
        code_name: str = None,
        consortium_count: int = None,
        create_time: str = None,
        domain: str = None,
        organization_description: str = None,
        organization_id: str = None,
        organization_name: str = None,
        owner_bid: str = None,
        owner_name: str = None,
        owner_uid: int = None,
        peer_count: int = None,
        region_id: str = None,
        request_id: str = None,
        service_state: str = None,
        spec_name: str = None,
        user_count: int = None,
        zone_id: str = None,
    ):
        self.cluster_state = cluster_state
        self.code_name = code_name
        self.consortium_count = consortium_count
        self.create_time = create_time
        self.domain = domain
        self.organization_description = organization_description
        self.organization_id = organization_id
        self.organization_name = organization_name
        self.owner_bid = owner_bid
        self.owner_name = owner_name
        self.owner_uid = owner_uid
        self.peer_count = peer_count
        self.region_id = region_id
        self.request_id = request_id
        self.service_state = service_state
        self.spec_name = spec_name
        self.user_count = user_count
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_state is not None:
            result['ClusterState'] = self.cluster_state
        if self.code_name is not None:
            result['CodeName'] = self.code_name
        if self.consortium_count is not None:
            result['ConsortiumCount'] = self.consortium_count
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.organization_description is not None:
            result['OrganizationDescription'] = self.organization_description
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.organization_name is not None:
            result['OrganizationName'] = self.organization_name
        if self.owner_bid is not None:
            result['OwnerBid'] = self.owner_bid
        if self.owner_name is not None:
            result['OwnerName'] = self.owner_name
        if self.owner_uid is not None:
            result['OwnerUid'] = self.owner_uid
        if self.peer_count is not None:
            result['PeerCount'] = self.peer_count
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.service_state is not None:
            result['ServiceState'] = self.service_state
        if self.spec_name is not None:
            result['SpecName'] = self.spec_name
        if self.user_count is not None:
            result['UserCount'] = self.user_count
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterState') is not None:
            self.cluster_state = m.get('ClusterState')
        if m.get('CodeName') is not None:
            self.code_name = m.get('CodeName')
        if m.get('ConsortiumCount') is not None:
            self.consortium_count = m.get('ConsortiumCount')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('OrganizationDescription') is not None:
            self.organization_description = m.get('OrganizationDescription')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('OrganizationName') is not None:
            self.organization_name = m.get('OrganizationName')
        if m.get('OwnerBid') is not None:
            self.owner_bid = m.get('OwnerBid')
        if m.get('OwnerName') is not None:
            self.owner_name = m.get('OwnerName')
        if m.get('OwnerUid') is not None:
            self.owner_uid = m.get('OwnerUid')
        if m.get('PeerCount') is not None:
            self.peer_count = m.get('PeerCount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ServiceState') is not None:
            self.service_state = m.get('ServiceState')
        if m.get('SpecName') is not None:
            self.spec_name = m.get('SpecName')
        if m.get('UserCount') is not None:
            self.user_count = m.get('UserCount')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class CreateFabricOrganizationResponseBody(TeaModel):
    def __init__(
        self,
        error_code: int = None,
        request_id: str = None,
        result: CreateFabricOrganizationResponseBodyResult = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.request_id = request_id
        self.result = result
        self.success = success

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = CreateFabricOrganizationResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateFabricOrganizationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateFabricOrganizationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateFabricOrganizationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFabricOrganizationUserRequest(TeaModel):
    def __init__(
        self,
        attrs: str = None,
        organization_id: str = None,
        password: str = None,
        username: str = None,
    ):
        self.attrs = attrs
        # This parameter is required.
        self.organization_id = organization_id
        # This parameter is required.
        self.password = password
        # This parameter is required.
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attrs is not None:
            result['Attrs'] = self.attrs
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.password is not None:
            result['Password'] = self.password
        if self.username is not None:
            result['Username'] = self.username
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Attrs') is not None:
            self.attrs = m.get('Attrs')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        return self


class CreateFabricOrganizationUserResponseBodyResult(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        expire_time: str = None,
        fullname: str = None,
        organization_id: str = None,
        password: str = None,
        username: str = None,
    ):
        self.create_time = create_time
        self.expire_time = expire_time
        self.fullname = fullname
        self.organization_id = organization_id
        self.password = password
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.fullname is not None:
            result['Fullname'] = self.fullname
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.password is not None:
            result['Password'] = self.password
        if self.username is not None:
            result['Username'] = self.username
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('Fullname') is not None:
            self.fullname = m.get('Fullname')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        return self


class CreateFabricOrganizationUserResponseBody(TeaModel):
    def __init__(
        self,
        error_code: int = None,
        request_id: str = None,
        result: CreateFabricOrganizationUserResponseBodyResult = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.request_id = request_id
        self.result = result
        self.success = success

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = CreateFabricOrganizationUserResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateFabricOrganizationUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateFabricOrganizationUserResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateFabricOrganizationUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAntChainConsortiumRequest(TeaModel):
    def __init__(
        self,
        consortium_id: str = None,
    ):
        # This parameter is required.
        self.consortium_id = consortium_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        status_code: int = None,
        body: DeleteAntChainConsortiumResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteAntChainConsortiumResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAntChainContractContentRequest(TeaModel):
    def __init__(
        self,
        content_id: str = None,
    ):
        # This parameter is required.
        self.content_id = content_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        status_code: int = None,
        body: DeleteAntChainContractContentResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteAntChainContractContentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAntChainContractProjectRequest(TeaModel):
    def __init__(
        self,
        project_id: str = None,
    ):
        # This parameter is required.
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        status_code: int = None,
        body: DeleteAntChainContractProjectResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
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
        # This parameter is required.
        self.ant_chain_id = ant_chain_id
        # This parameter is required.
        self.phone = phone

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        status_code: int = None,
        body: DeleteAntChainMiniAppQRCodeAuthorizedUserResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteAntChainMiniAppQRCodeAuthorizedUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteFabricChaincodeRequest(TeaModel):
    def __init__(
        self,
        chaincode_id: str = None,
    ):
        # This parameter is required.
        self.chaincode_id = chaincode_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        error_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteFabricChaincodeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteFabricChaincodeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteFabricChaincodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAntChainAccountsRequest(TeaModel):
    def __init__(
        self,
        ant_chain_id: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # This parameter is required.
        self.ant_chain_id = ant_chain_id
        self.page_number = page_number
        # This parameter is required.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ant_chain_id is not None:
            result['AntChainId'] = self.ant_chain_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AntChainId') is not None:
            self.ant_chain_id = m.get('AntChainId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeAntChainAccountsResponseBodyResultAccounts(TeaModel):
    def __init__(
        self,
        account: str = None,
        account_public_key: str = None,
        account_recovery_key: str = None,
        account_status: str = None,
        ant_chain_id: str = None,
    ):
        self.account = account
        self.account_public_key = account_public_key
        self.account_recovery_key = account_recovery_key
        self.account_status = account_status
        self.ant_chain_id = ant_chain_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account is not None:
            result['Account'] = self.account
        if self.account_public_key is not None:
            result['AccountPublicKey'] = self.account_public_key
        if self.account_recovery_key is not None:
            result['AccountRecoveryKey'] = self.account_recovery_key
        if self.account_status is not None:
            result['AccountStatus'] = self.account_status
        if self.ant_chain_id is not None:
            result['AntChainId'] = self.ant_chain_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Account') is not None:
            self.account = m.get('Account')
        if m.get('AccountPublicKey') is not None:
            self.account_public_key = m.get('AccountPublicKey')
        if m.get('AccountRecoveryKey') is not None:
            self.account_recovery_key = m.get('AccountRecoveryKey')
        if m.get('AccountStatus') is not None:
            self.account_status = m.get('AccountStatus')
        if m.get('AntChainId') is not None:
            self.ant_chain_id = m.get('AntChainId')
        return self


class DescribeAntChainAccountsResponseBodyResultPagination(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

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


class DescribeAntChainAccountsResponseBodyResult(TeaModel):
    def __init__(
        self,
        accounts: List[DescribeAntChainAccountsResponseBodyResultAccounts] = None,
        pagination: DescribeAntChainAccountsResponseBodyResultPagination = None,
    ):
        self.accounts = accounts
        self.pagination = pagination

    def validate(self):
        if self.accounts:
            for k in self.accounts:
                if k:
                    k.validate()
        if self.pagination:
            self.pagination.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Accounts'] = []
        if self.accounts is not None:
            for k in self.accounts:
                result['Accounts'].append(k.to_map() if k else None)
        if self.pagination is not None:
            result['Pagination'] = self.pagination.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.accounts = []
        if m.get('Accounts') is not None:
            for k in m.get('Accounts'):
                temp_model = DescribeAntChainAccountsResponseBodyResultAccounts()
                self.accounts.append(temp_model.from_map(k))
        if m.get('Pagination') is not None:
            temp_model = DescribeAntChainAccountsResponseBodyResultPagination()
            self.pagination = temp_model.from_map(m['Pagination'])
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        status_code: int = None,
        body: DescribeAntChainAccountsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeAntChainAccountsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAntChainAccountsV2Request(TeaModel):
    def __init__(
        self,
        ant_chain_id: str = None,
        consortium_id: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # This parameter is required.
        self.ant_chain_id = ant_chain_id
        self.consortium_id = consortium_id
        self.page_number = page_number
        # This parameter is required.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ant_chain_id is not None:
            result['AntChainId'] = self.ant_chain_id
        if self.consortium_id is not None:
            result['ConsortiumId'] = self.consortium_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AntChainId') is not None:
            self.ant_chain_id = m.get('AntChainId')
        if m.get('ConsortiumId') is not None:
            self.consortium_id = m.get('ConsortiumId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeAntChainAccountsV2ResponseBodyResultAccounts(TeaModel):
    def __init__(
        self,
        account: str = None,
        account_public_key: str = None,
        account_recovery_key: str = None,
        account_status: str = None,
        ant_chain_id: str = None,
    ):
        self.account = account
        self.account_public_key = account_public_key
        self.account_recovery_key = account_recovery_key
        self.account_status = account_status
        self.ant_chain_id = ant_chain_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account is not None:
            result['Account'] = self.account
        if self.account_public_key is not None:
            result['AccountPublicKey'] = self.account_public_key
        if self.account_recovery_key is not None:
            result['AccountRecoveryKey'] = self.account_recovery_key
        if self.account_status is not None:
            result['AccountStatus'] = self.account_status
        if self.ant_chain_id is not None:
            result['AntChainId'] = self.ant_chain_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Account') is not None:
            self.account = m.get('Account')
        if m.get('AccountPublicKey') is not None:
            self.account_public_key = m.get('AccountPublicKey')
        if m.get('AccountRecoveryKey') is not None:
            self.account_recovery_key = m.get('AccountRecoveryKey')
        if m.get('AccountStatus') is not None:
            self.account_status = m.get('AccountStatus')
        if m.get('AntChainId') is not None:
            self.ant_chain_id = m.get('AntChainId')
        return self


class DescribeAntChainAccountsV2ResponseBodyResultPagination(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

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


class DescribeAntChainAccountsV2ResponseBodyResult(TeaModel):
    def __init__(
        self,
        accounts: List[DescribeAntChainAccountsV2ResponseBodyResultAccounts] = None,
        pagination: DescribeAntChainAccountsV2ResponseBodyResultPagination = None,
    ):
        self.accounts = accounts
        self.pagination = pagination

    def validate(self):
        if self.accounts:
            for k in self.accounts:
                if k:
                    k.validate()
        if self.pagination:
            self.pagination.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Accounts'] = []
        if self.accounts is not None:
            for k in self.accounts:
                result['Accounts'].append(k.to_map() if k else None)
        if self.pagination is not None:
            result['Pagination'] = self.pagination.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.accounts = []
        if m.get('Accounts') is not None:
            for k in m.get('Accounts'):
                temp_model = DescribeAntChainAccountsV2ResponseBodyResultAccounts()
                self.accounts.append(temp_model.from_map(k))
        if m.get('Pagination') is not None:
            temp_model = DescribeAntChainAccountsV2ResponseBodyResultPagination()
            self.pagination = temp_model.from_map(m['Pagination'])
        return self


class DescribeAntChainAccountsV2ResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: str = None,
        message: str = None,
        request_id: str = None,
        result: DescribeAntChainAccountsV2ResponseBodyResult = None,
        result_code: str = None,
        result_message: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.result = result
        self.result_code = result_code
        self.result_message = result_message
        self.success = success

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        if self.result_message is not None:
            result['ResultMessage'] = self.result_message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = DescribeAntChainAccountsV2ResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeAntChainAccountsV2Response(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAntChainAccountsV2ResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeAntChainAccountsV2ResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAntChainBlockRequest(TeaModel):
    def __init__(
        self,
        ant_chain_id: str = None,
        height: int = None,
    ):
        # This parameter is required.
        self.ant_chain_id = ant_chain_id
        # This parameter is required.
        self.height = height

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        ant_chain_id: str = None,
        block_hash: str = None,
        create_time: int = None,
        height: int = None,
        previous_hash: str = None,
        root_tx_hash: str = None,
        trans_summary_list: str = None,
        transaction_size: int = None,
        version: int = None,
    ):
        self.ant_chain_id = ant_chain_id
        self.block_hash = block_hash
        self.create_time = create_time
        self.height = height
        self.previous_hash = previous_hash
        self.root_tx_hash = root_tx_hash
        self.trans_summary_list = trans_summary_list
        self.transaction_size = transaction_size
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ant_chain_id is not None:
            result['AntChainId'] = self.ant_chain_id
        if self.block_hash is not None:
            result['BlockHash'] = self.block_hash
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.height is not None:
            result['Height'] = self.height
        if self.previous_hash is not None:
            result['PreviousHash'] = self.previous_hash
        if self.root_tx_hash is not None:
            result['RootTxHash'] = self.root_tx_hash
        if self.trans_summary_list is not None:
            result['TransSummaryList'] = self.trans_summary_list
        if self.transaction_size is not None:
            result['TransactionSize'] = self.transaction_size
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AntChainId') is not None:
            self.ant_chain_id = m.get('AntChainId')
        if m.get('BlockHash') is not None:
            self.block_hash = m.get('BlockHash')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('PreviousHash') is not None:
            self.previous_hash = m.get('PreviousHash')
        if m.get('RootTxHash') is not None:
            self.root_tx_hash = m.get('RootTxHash')
        if m.get('TransSummaryList') is not None:
            self.trans_summary_list = m.get('TransSummaryList')
        if m.get('TransactionSize') is not None:
            self.transaction_size = m.get('TransactionSize')
        if m.get('Version') is not None:
            self.version = m.get('Version')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        status_code: int = None,
        body: DescribeAntChainBlockResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeAntChainBlockResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAntChainBlockV2Request(TeaModel):
    def __init__(
        self,
        ant_chain_id: str = None,
        consortium_id: str = None,
        height: int = None,
    ):
        # This parameter is required.
        self.ant_chain_id = ant_chain_id
        self.consortium_id = consortium_id
        # This parameter is required.
        self.height = height

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ant_chain_id is not None:
            result['AntChainId'] = self.ant_chain_id
        if self.consortium_id is not None:
            result['ConsortiumId'] = self.consortium_id
        if self.height is not None:
            result['Height'] = self.height
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AntChainId') is not None:
            self.ant_chain_id = m.get('AntChainId')
        if m.get('ConsortiumId') is not None:
            self.consortium_id = m.get('ConsortiumId')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        return self


class DescribeAntChainBlockV2ResponseBodyResultTransSummaryList(TeaModel):
    def __init__(
        self,
        alias: str = None,
        block_hash: str = None,
        category: int = None,
        create_time: int = None,
        from_: str = None,
        gas_used: int = None,
        hash: str = None,
        height: int = None,
        reference_count: int = None,
        to: str = None,
        trans_type_v10: str = None,
        trans_type_v6: str = None,
    ):
        self.alias = alias
        self.block_hash = block_hash
        self.category = category
        self.create_time = create_time
        self.from_ = from_
        self.gas_used = gas_used
        self.hash = hash
        self.height = height
        self.reference_count = reference_count
        self.to = to
        self.trans_type_v10 = trans_type_v10
        self.trans_type_v6 = trans_type_v6

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias is not None:
            result['Alias'] = self.alias
        if self.block_hash is not None:
            result['BlockHash'] = self.block_hash
        if self.category is not None:
            result['Category'] = self.category
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.from_ is not None:
            result['From'] = self.from_
        if self.gas_used is not None:
            result['GasUsed'] = self.gas_used
        if self.hash is not None:
            result['Hash'] = self.hash
        if self.height is not None:
            result['Height'] = self.height
        if self.reference_count is not None:
            result['ReferenceCount'] = self.reference_count
        if self.to is not None:
            result['To'] = self.to
        if self.trans_type_v10 is not None:
            result['TransTypeV10'] = self.trans_type_v10
        if self.trans_type_v6 is not None:
            result['TransTypeV6'] = self.trans_type_v6
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Alias') is not None:
            self.alias = m.get('Alias')
        if m.get('BlockHash') is not None:
            self.block_hash = m.get('BlockHash')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('From') is not None:
            self.from_ = m.get('From')
        if m.get('GasUsed') is not None:
            self.gas_used = m.get('GasUsed')
        if m.get('Hash') is not None:
            self.hash = m.get('Hash')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('ReferenceCount') is not None:
            self.reference_count = m.get('ReferenceCount')
        if m.get('To') is not None:
            self.to = m.get('To')
        if m.get('TransTypeV10') is not None:
            self.trans_type_v10 = m.get('TransTypeV10')
        if m.get('TransTypeV6') is not None:
            self.trans_type_v6 = m.get('TransTypeV6')
        return self


class DescribeAntChainBlockV2ResponseBodyResult(TeaModel):
    def __init__(
        self,
        ant_chain_id: str = None,
        block_hash: str = None,
        create_time: int = None,
        height: int = None,
        previous_hash: str = None,
        root_tx_hash: str = None,
        trans_summary_list: List[DescribeAntChainBlockV2ResponseBodyResultTransSummaryList] = None,
        transaction_size: int = None,
        version: int = None,
    ):
        self.ant_chain_id = ant_chain_id
        self.block_hash = block_hash
        self.create_time = create_time
        self.height = height
        self.previous_hash = previous_hash
        self.root_tx_hash = root_tx_hash
        self.trans_summary_list = trans_summary_list
        self.transaction_size = transaction_size
        self.version = version

    def validate(self):
        if self.trans_summary_list:
            for k in self.trans_summary_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ant_chain_id is not None:
            result['AntChainId'] = self.ant_chain_id
        if self.block_hash is not None:
            result['BlockHash'] = self.block_hash
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.height is not None:
            result['Height'] = self.height
        if self.previous_hash is not None:
            result['PreviousHash'] = self.previous_hash
        if self.root_tx_hash is not None:
            result['RootTxHash'] = self.root_tx_hash
        result['TransSummaryList'] = []
        if self.trans_summary_list is not None:
            for k in self.trans_summary_list:
                result['TransSummaryList'].append(k.to_map() if k else None)
        if self.transaction_size is not None:
            result['TransactionSize'] = self.transaction_size
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AntChainId') is not None:
            self.ant_chain_id = m.get('AntChainId')
        if m.get('BlockHash') is not None:
            self.block_hash = m.get('BlockHash')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('PreviousHash') is not None:
            self.previous_hash = m.get('PreviousHash')
        if m.get('RootTxHash') is not None:
            self.root_tx_hash = m.get('RootTxHash')
        self.trans_summary_list = []
        if m.get('TransSummaryList') is not None:
            for k in m.get('TransSummaryList'):
                temp_model = DescribeAntChainBlockV2ResponseBodyResultTransSummaryList()
                self.trans_summary_list.append(temp_model.from_map(k))
        if m.get('TransactionSize') is not None:
            self.transaction_size = m.get('TransactionSize')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class DescribeAntChainBlockV2ResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: str = None,
        message: str = None,
        request_id: str = None,
        result: DescribeAntChainBlockV2ResponseBodyResult = None,
        result_code: str = None,
        result_message: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.result = result
        self.result_code = result_code
        self.result_message = result_message
        self.success = success

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        if self.result_message is not None:
            result['ResultMessage'] = self.result_message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = DescribeAntChainBlockV2ResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeAntChainBlockV2Response(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAntChainBlockV2ResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeAntChainBlockV2ResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAntChainCertificateApplicationsRequest(TeaModel):
    def __init__(
        self,
        ant_chain_id: str = None,
        page_number: int = None,
        page_size: int = None,
        status: str = None,
    ):
        # This parameter is required.
        self.ant_chain_id = ant_chain_id
        # This parameter is required.
        self.page_number = page_number
        # This parameter is required.
        self.page_size = page_size
        # This parameter is required.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ant_chain_id is not None:
            result['AntChainId'] = self.ant_chain_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AntChainId') is not None:
            self.ant_chain_id = m.get('AntChainId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeAntChainCertificateApplicationsResponseBodyResultCertificateApplications(TeaModel):
    def __init__(
        self,
        ant_chain_id: str = None,
        bid: str = None,
        createtime: int = None,
        status: str = None,
        updatetime: int = None,
        username: str = None,
    ):
        self.ant_chain_id = ant_chain_id
        # Bid
        self.bid = bid
        self.createtime = createtime
        self.status = status
        self.updatetime = updatetime
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ant_chain_id is not None:
            result['AntChainId'] = self.ant_chain_id
        if self.bid is not None:
            result['Bid'] = self.bid
        if self.createtime is not None:
            result['Createtime'] = self.createtime
        if self.status is not None:
            result['Status'] = self.status
        if self.updatetime is not None:
            result['Updatetime'] = self.updatetime
        if self.username is not None:
            result['Username'] = self.username
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AntChainId') is not None:
            self.ant_chain_id = m.get('AntChainId')
        if m.get('Bid') is not None:
            self.bid = m.get('Bid')
        if m.get('Createtime') is not None:
            self.createtime = m.get('Createtime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Updatetime') is not None:
            self.updatetime = m.get('Updatetime')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        return self


class DescribeAntChainCertificateApplicationsResponseBodyResultPagination(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

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


class DescribeAntChainCertificateApplicationsResponseBodyResult(TeaModel):
    def __init__(
        self,
        certificate_applications: List[DescribeAntChainCertificateApplicationsResponseBodyResultCertificateApplications] = None,
        pagination: DescribeAntChainCertificateApplicationsResponseBodyResultPagination = None,
    ):
        self.certificate_applications = certificate_applications
        self.pagination = pagination

    def validate(self):
        if self.certificate_applications:
            for k in self.certificate_applications:
                if k:
                    k.validate()
        if self.pagination:
            self.pagination.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CertificateApplications'] = []
        if self.certificate_applications is not None:
            for k in self.certificate_applications:
                result['CertificateApplications'].append(k.to_map() if k else None)
        if self.pagination is not None:
            result['Pagination'] = self.pagination.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.certificate_applications = []
        if m.get('CertificateApplications') is not None:
            for k in m.get('CertificateApplications'):
                temp_model = DescribeAntChainCertificateApplicationsResponseBodyResultCertificateApplications()
                self.certificate_applications.append(temp_model.from_map(k))
        if m.get('Pagination') is not None:
            temp_model = DescribeAntChainCertificateApplicationsResponseBodyResultPagination()
            self.pagination = temp_model.from_map(m['Pagination'])
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        status_code: int = None,
        body: DescribeAntChainCertificateApplicationsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeAntChainCertificateApplicationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAntChainCertificateApplicationsV2Request(TeaModel):
    def __init__(
        self,
        ant_chain_id: str = None,
        consortium_id: str = None,
        page_number: int = None,
        page_size: int = None,
        status: str = None,
    ):
        # This parameter is required.
        self.ant_chain_id = ant_chain_id
        self.consortium_id = consortium_id
        # This parameter is required.
        self.page_number = page_number
        # This parameter is required.
        self.page_size = page_size
        # This parameter is required.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ant_chain_id is not None:
            result['AntChainId'] = self.ant_chain_id
        if self.consortium_id is not None:
            result['ConsortiumId'] = self.consortium_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AntChainId') is not None:
            self.ant_chain_id = m.get('AntChainId')
        if m.get('ConsortiumId') is not None:
            self.consortium_id = m.get('ConsortiumId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeAntChainCertificateApplicationsV2ResponseBodyResultCertificateApplications(TeaModel):
    def __init__(
        self,
        ant_chain_id: str = None,
        bid: str = None,
        createtime: int = None,
        status: str = None,
        updatetime: int = None,
        username: str = None,
    ):
        self.ant_chain_id = ant_chain_id
        self.bid = bid
        self.createtime = createtime
        self.status = status
        self.updatetime = updatetime
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ant_chain_id is not None:
            result['AntChainId'] = self.ant_chain_id
        if self.bid is not None:
            result['Bid'] = self.bid
        if self.createtime is not None:
            result['Createtime'] = self.createtime
        if self.status is not None:
            result['Status'] = self.status
        if self.updatetime is not None:
            result['Updatetime'] = self.updatetime
        if self.username is not None:
            result['Username'] = self.username
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AntChainId') is not None:
            self.ant_chain_id = m.get('AntChainId')
        if m.get('Bid') is not None:
            self.bid = m.get('Bid')
        if m.get('Createtime') is not None:
            self.createtime = m.get('Createtime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Updatetime') is not None:
            self.updatetime = m.get('Updatetime')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        return self


class DescribeAntChainCertificateApplicationsV2ResponseBodyResultPagination(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

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


class DescribeAntChainCertificateApplicationsV2ResponseBodyResult(TeaModel):
    def __init__(
        self,
        certificate_applications: List[DescribeAntChainCertificateApplicationsV2ResponseBodyResultCertificateApplications] = None,
        pagination: DescribeAntChainCertificateApplicationsV2ResponseBodyResultPagination = None,
    ):
        self.certificate_applications = certificate_applications
        self.pagination = pagination

    def validate(self):
        if self.certificate_applications:
            for k in self.certificate_applications:
                if k:
                    k.validate()
        if self.pagination:
            self.pagination.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CertificateApplications'] = []
        if self.certificate_applications is not None:
            for k in self.certificate_applications:
                result['CertificateApplications'].append(k.to_map() if k else None)
        if self.pagination is not None:
            result['Pagination'] = self.pagination.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.certificate_applications = []
        if m.get('CertificateApplications') is not None:
            for k in m.get('CertificateApplications'):
                temp_model = DescribeAntChainCertificateApplicationsV2ResponseBodyResultCertificateApplications()
                self.certificate_applications.append(temp_model.from_map(k))
        if m.get('Pagination') is not None:
            temp_model = DescribeAntChainCertificateApplicationsV2ResponseBodyResultPagination()
            self.pagination = temp_model.from_map(m['Pagination'])
        return self


class DescribeAntChainCertificateApplicationsV2ResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: str = None,
        message: str = None,
        request_id: str = None,
        result: DescribeAntChainCertificateApplicationsV2ResponseBodyResult = None,
        result_code: str = None,
        result_message: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.result = result
        self.result_code = result_code
        self.result_message = result_message
        self.success = success

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        if self.result_message is not None:
            result['ResultMessage'] = self.result_message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = DescribeAntChainCertificateApplicationsV2ResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeAntChainCertificateApplicationsV2Response(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAntChainCertificateApplicationsV2ResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeAntChainCertificateApplicationsV2ResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAntChainConsortiumsRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
    ):
        self.page_number = page_number
        # This parameter is required.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeAntChainConsortiumsResponseBodyResultAntConsortiums(TeaModel):
    def __init__(
        self,
        chain_num: int = None,
        consortium_description: str = None,
        consortium_id: str = None,
        consortium_name: str = None,
        create_time: int = None,
        member_num: int = None,
        role: str = None,
        status: str = None,
    ):
        self.chain_num = chain_num
        self.consortium_description = consortium_description
        self.consortium_id = consortium_id
        self.consortium_name = consortium_name
        self.create_time = create_time
        self.member_num = member_num
        self.role = role
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.chain_num is not None:
            result['ChainNum'] = self.chain_num
        if self.consortium_description is not None:
            result['ConsortiumDescription'] = self.consortium_description
        if self.consortium_id is not None:
            result['ConsortiumId'] = self.consortium_id
        if self.consortium_name is not None:
            result['ConsortiumName'] = self.consortium_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.member_num is not None:
            result['MemberNum'] = self.member_num
        if self.role is not None:
            result['Role'] = self.role
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChainNum') is not None:
            self.chain_num = m.get('ChainNum')
        if m.get('ConsortiumDescription') is not None:
            self.consortium_description = m.get('ConsortiumDescription')
        if m.get('ConsortiumId') is not None:
            self.consortium_id = m.get('ConsortiumId')
        if m.get('ConsortiumName') is not None:
            self.consortium_name = m.get('ConsortiumName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('MemberNum') is not None:
            self.member_num = m.get('MemberNum')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeAntChainConsortiumsResponseBodyResultPagination(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        status_code: int = None,
        body: DescribeAntChainConsortiumsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeAntChainConsortiumsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAntChainConsortiumsV2Request(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
    ):
        self.page_number = page_number
        # This parameter is required.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeAntChainConsortiumsV2ResponseBodyResultAntConsortiums(TeaModel):
    def __init__(
        self,
        chain_num: int = None,
        consortium_description: str = None,
        consortium_id: str = None,
        consortium_name: str = None,
        create_time: int = None,
        is_empty_consortium: bool = None,
        member_num: int = None,
        role: str = None,
        status: str = None,
    ):
        self.chain_num = chain_num
        self.consortium_description = consortium_description
        self.consortium_id = consortium_id
        self.consortium_name = consortium_name
        self.create_time = create_time
        self.is_empty_consortium = is_empty_consortium
        self.member_num = member_num
        self.role = role
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.chain_num is not None:
            result['ChainNum'] = self.chain_num
        if self.consortium_description is not None:
            result['ConsortiumDescription'] = self.consortium_description
        if self.consortium_id is not None:
            result['ConsortiumId'] = self.consortium_id
        if self.consortium_name is not None:
            result['ConsortiumName'] = self.consortium_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.is_empty_consortium is not None:
            result['IsEmptyConsortium'] = self.is_empty_consortium
        if self.member_num is not None:
            result['MemberNum'] = self.member_num
        if self.role is not None:
            result['Role'] = self.role
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChainNum') is not None:
            self.chain_num = m.get('ChainNum')
        if m.get('ConsortiumDescription') is not None:
            self.consortium_description = m.get('ConsortiumDescription')
        if m.get('ConsortiumId') is not None:
            self.consortium_id = m.get('ConsortiumId')
        if m.get('ConsortiumName') is not None:
            self.consortium_name = m.get('ConsortiumName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('IsEmptyConsortium') is not None:
            self.is_empty_consortium = m.get('IsEmptyConsortium')
        if m.get('MemberNum') is not None:
            self.member_num = m.get('MemberNum')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeAntChainConsortiumsV2ResponseBodyResultPagination(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

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


class DescribeAntChainConsortiumsV2ResponseBodyResult(TeaModel):
    def __init__(
        self,
        ant_consortiums: List[DescribeAntChainConsortiumsV2ResponseBodyResultAntConsortiums] = None,
        pagination: DescribeAntChainConsortiumsV2ResponseBodyResultPagination = None,
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
                temp_model = DescribeAntChainConsortiumsV2ResponseBodyResultAntConsortiums()
                self.ant_consortiums.append(temp_model.from_map(k))
        if m.get('Pagination') is not None:
            temp_model = DescribeAntChainConsortiumsV2ResponseBodyResultPagination()
            self.pagination = temp_model.from_map(m['Pagination'])
        return self


class DescribeAntChainConsortiumsV2ResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: str = None,
        message: str = None,
        request_id: str = None,
        result: DescribeAntChainConsortiumsV2ResponseBodyResult = None,
        result_code: str = None,
        result_message: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.result = result
        self.result_code = result_code
        self.result_message = result_message
        self.success = success

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        if self.result_message is not None:
            result['ResultMessage'] = self.result_message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = DescribeAntChainConsortiumsV2ResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeAntChainConsortiumsV2Response(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAntChainConsortiumsV2ResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeAntChainConsortiumsV2ResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAntChainContractProjectContentTreeRequest(TeaModel):
    def __init__(
        self,
        project_id: str = None,
    ):
        # This parameter is required.
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        project_description: str = None,
        project_id: str = None,
        project_name: str = None,
        project_version: str = None,
    ):
        self.children = children
        self.project_description = project_description
        self.project_id = project_id
        self.project_name = project_name
        self.project_version = project_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.children is not None:
            result['Children'] = self.children
        if self.project_description is not None:
            result['ProjectDescription'] = self.project_description
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.project_version is not None:
            result['ProjectVersion'] = self.project_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Children') is not None:
            self.children = m.get('Children')
        if m.get('ProjectDescription') is not None:
            self.project_description = m.get('ProjectDescription')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('ProjectVersion') is not None:
            self.project_version = m.get('ProjectVersion')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        status_code: int = None,
        body: DescribeAntChainContractProjectContentTreeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeAntChainContractProjectContentTreeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAntChainContractProjectContentTreeV2Request(TeaModel):
    def __init__(
        self,
        consortium_id: str = None,
        project_id: str = None,
    ):
        # This parameter is required.
        self.consortium_id = consortium_id
        # This parameter is required.
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consortium_id is not None:
            result['ConsortiumId'] = self.consortium_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsortiumId') is not None:
            self.consortium_id = m.get('ConsortiumId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class DescribeAntChainContractProjectContentTreeV2ResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: str = None,
        message: str = None,
        request_id: str = None,
        result: str = None,
        result_code: str = None,
        result_message: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.result = result
        self.result_code = result_code
        self.result_message = result_message
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        if self.result_message is not None:
            result['ResultMessage'] = self.result_message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeAntChainContractProjectContentTreeV2Response(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAntChainContractProjectContentTreeV2ResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeAntChainContractProjectContentTreeV2ResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAntChainContractProjectsRequest(TeaModel):
    def __init__(
        self,
        consortium_id: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # This parameter is required.
        self.consortium_id = consortium_id
        # This parameter is required.
        self.page_number = page_number
        # This parameter is required.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consortium_id is not None:
            result['ConsortiumId'] = self.consortium_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsortiumId') is not None:
            self.consortium_id = m.get('ConsortiumId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeAntChainContractProjectsResponseBodyResultContractProjects(TeaModel):
    def __init__(
        self,
        consortium_id: str = None,
        create_time: int = None,
        project_description: str = None,
        project_id: str = None,
        project_name: str = None,
        project_version: str = None,
        update_time: int = None,
    ):
        self.consortium_id = consortium_id
        self.create_time = create_time
        self.project_description = project_description
        self.project_id = project_id
        self.project_name = project_name
        self.project_version = project_version
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consortium_id is not None:
            result['ConsortiumId'] = self.consortium_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.project_description is not None:
            result['ProjectDescription'] = self.project_description
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.project_version is not None:
            result['ProjectVersion'] = self.project_version
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsortiumId') is not None:
            self.consortium_id = m.get('ConsortiumId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ProjectDescription') is not None:
            self.project_description = m.get('ProjectDescription')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('ProjectVersion') is not None:
            self.project_version = m.get('ProjectVersion')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class DescribeAntChainContractProjectsResponseBodyResultPagination(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

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


class DescribeAntChainContractProjectsResponseBodyResult(TeaModel):
    def __init__(
        self,
        contract_projects: List[DescribeAntChainContractProjectsResponseBodyResultContractProjects] = None,
        pagination: DescribeAntChainContractProjectsResponseBodyResultPagination = None,
    ):
        self.contract_projects = contract_projects
        self.pagination = pagination

    def validate(self):
        if self.contract_projects:
            for k in self.contract_projects:
                if k:
                    k.validate()
        if self.pagination:
            self.pagination.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ContractProjects'] = []
        if self.contract_projects is not None:
            for k in self.contract_projects:
                result['ContractProjects'].append(k.to_map() if k else None)
        if self.pagination is not None:
            result['Pagination'] = self.pagination.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.contract_projects = []
        if m.get('ContractProjects') is not None:
            for k in m.get('ContractProjects'):
                temp_model = DescribeAntChainContractProjectsResponseBodyResultContractProjects()
                self.contract_projects.append(temp_model.from_map(k))
        if m.get('Pagination') is not None:
            temp_model = DescribeAntChainContractProjectsResponseBodyResultPagination()
            self.pagination = temp_model.from_map(m['Pagination'])
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        status_code: int = None,
        body: DescribeAntChainContractProjectsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeAntChainContractProjectsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAntChainContractProjectsV2Request(TeaModel):
    def __init__(
        self,
        consortium_id: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # This parameter is required.
        self.consortium_id = consortium_id
        # This parameter is required.
        self.page_number = page_number
        # This parameter is required.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consortium_id is not None:
            result['ConsortiumId'] = self.consortium_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsortiumId') is not None:
            self.consortium_id = m.get('ConsortiumId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeAntChainContractProjectsV2ResponseBodyResultContractProjects(TeaModel):
    def __init__(
        self,
        consortium_id: str = None,
        create_time: int = None,
        project_description: str = None,
        project_id: str = None,
        project_name: str = None,
        project_version: str = None,
        update_time: int = None,
    ):
        self.consortium_id = consortium_id
        self.create_time = create_time
        self.project_description = project_description
        self.project_id = project_id
        self.project_name = project_name
        self.project_version = project_version
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consortium_id is not None:
            result['ConsortiumId'] = self.consortium_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.project_description is not None:
            result['ProjectDescription'] = self.project_description
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.project_version is not None:
            result['ProjectVersion'] = self.project_version
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsortiumId') is not None:
            self.consortium_id = m.get('ConsortiumId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ProjectDescription') is not None:
            self.project_description = m.get('ProjectDescription')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('ProjectVersion') is not None:
            self.project_version = m.get('ProjectVersion')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class DescribeAntChainContractProjectsV2ResponseBodyResultPagination(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

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


class DescribeAntChainContractProjectsV2ResponseBodyResult(TeaModel):
    def __init__(
        self,
        contract_projects: List[DescribeAntChainContractProjectsV2ResponseBodyResultContractProjects] = None,
        pagination: DescribeAntChainContractProjectsV2ResponseBodyResultPagination = None,
    ):
        self.contract_projects = contract_projects
        self.pagination = pagination

    def validate(self):
        if self.contract_projects:
            for k in self.contract_projects:
                if k:
                    k.validate()
        if self.pagination:
            self.pagination.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ContractProjects'] = []
        if self.contract_projects is not None:
            for k in self.contract_projects:
                result['ContractProjects'].append(k.to_map() if k else None)
        if self.pagination is not None:
            result['Pagination'] = self.pagination.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.contract_projects = []
        if m.get('ContractProjects') is not None:
            for k in m.get('ContractProjects'):
                temp_model = DescribeAntChainContractProjectsV2ResponseBodyResultContractProjects()
                self.contract_projects.append(temp_model.from_map(k))
        if m.get('Pagination') is not None:
            temp_model = DescribeAntChainContractProjectsV2ResponseBodyResultPagination()
            self.pagination = temp_model.from_map(m['Pagination'])
        return self


class DescribeAntChainContractProjectsV2ResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: str = None,
        message: str = None,
        request_id: str = None,
        result: DescribeAntChainContractProjectsV2ResponseBodyResult = None,
        result_code: str = None,
        result_message: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.result = result
        self.result_code = result_code
        self.result_message = result_message
        self.success = success

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        if self.result_message is not None:
            result['ResultMessage'] = self.result_message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = DescribeAntChainContractProjectsV2ResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeAntChainContractProjectsV2Response(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAntChainContractProjectsV2ResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeAntChainContractProjectsV2ResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAntChainDownloadPathsRequest(TeaModel):
    def __init__(
        self,
        ant_chain_id: str = None,
    ):
        # This parameter is required.
        self.ant_chain_id = ant_chain_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        client_crt_url: str = None,
        sdk_url: str = None,
        trust_ca_url: str = None,
    ):
        self.ca_crt_url = ca_crt_url
        self.client_crt_url = client_crt_url
        self.sdk_url = sdk_url
        self.trust_ca_url = trust_ca_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ca_crt_url is not None:
            result['CaCrtUrl'] = self.ca_crt_url
        if self.client_crt_url is not None:
            result['ClientCrtUrl'] = self.client_crt_url
        if self.sdk_url is not None:
            result['SdkUrl'] = self.sdk_url
        if self.trust_ca_url is not None:
            result['TrustCaUrl'] = self.trust_ca_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CaCrtUrl') is not None:
            self.ca_crt_url = m.get('CaCrtUrl')
        if m.get('ClientCrtUrl') is not None:
            self.client_crt_url = m.get('ClientCrtUrl')
        if m.get('SdkUrl') is not None:
            self.sdk_url = m.get('SdkUrl')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        status_code: int = None,
        body: DescribeAntChainDownloadPathsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeAntChainDownloadPathsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAntChainDownloadPathsV2Request(TeaModel):
    def __init__(
        self,
        ant_chain_id: str = None,
        consortium_id: str = None,
    ):
        # This parameter is required.
        self.ant_chain_id = ant_chain_id
        self.consortium_id = consortium_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ant_chain_id is not None:
            result['AntChainId'] = self.ant_chain_id
        if self.consortium_id is not None:
            result['ConsortiumId'] = self.consortium_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AntChainId') is not None:
            self.ant_chain_id = m.get('AntChainId')
        if m.get('ConsortiumId') is not None:
            self.consortium_id = m.get('ConsortiumId')
        return self


class DescribeAntChainDownloadPathsV2ResponseBodyResult(TeaModel):
    def __init__(
        self,
        ca_crt_url: str = None,
        client_crt_url: str = None,
        sdk_url: str = None,
        trust_ca_url: str = None,
    ):
        self.ca_crt_url = ca_crt_url
        self.client_crt_url = client_crt_url
        self.sdk_url = sdk_url
        self.trust_ca_url = trust_ca_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ca_crt_url is not None:
            result['CaCrtUrl'] = self.ca_crt_url
        if self.client_crt_url is not None:
            result['ClientCrtUrl'] = self.client_crt_url
        if self.sdk_url is not None:
            result['SdkUrl'] = self.sdk_url
        if self.trust_ca_url is not None:
            result['TrustCaUrl'] = self.trust_ca_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CaCrtUrl') is not None:
            self.ca_crt_url = m.get('CaCrtUrl')
        if m.get('ClientCrtUrl') is not None:
            self.client_crt_url = m.get('ClientCrtUrl')
        if m.get('SdkUrl') is not None:
            self.sdk_url = m.get('SdkUrl')
        if m.get('TrustCaUrl') is not None:
            self.trust_ca_url = m.get('TrustCaUrl')
        return self


class DescribeAntChainDownloadPathsV2ResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: str = None,
        message: str = None,
        request_id: str = None,
        result: DescribeAntChainDownloadPathsV2ResponseBodyResult = None,
        result_code: str = None,
        result_message: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.result = result
        self.result_code = result_code
        self.result_message = result_message
        self.success = success

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        if self.result_message is not None:
            result['ResultMessage'] = self.result_message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = DescribeAntChainDownloadPathsV2ResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeAntChainDownloadPathsV2Response(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAntChainDownloadPathsV2ResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeAntChainDownloadPathsV2ResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAntChainInformationRequest(TeaModel):
    def __init__(
        self,
        ant_chain_id: str = None,
    ):
        # This parameter is required.
        self.ant_chain_id = ant_chain_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        block_height: int = None,
        node_name: str = None,
        status: bool = None,
        version: str = None,
    ):
        self.block_height = block_height
        self.node_name = node_name
        self.status = status
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.block_height is not None:
            result['BlockHeight'] = self.block_height
        if self.node_name is not None:
            result['NodeName'] = self.node_name
        if self.status is not None:
            result['Status'] = self.status
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BlockHeight') is not None:
            self.block_height = m.get('BlockHeight')
        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class DescribeAntChainInformationResponseBodyResult(TeaModel):
    def __init__(
        self,
        abnormal_nodes: int = None,
        ant_chain_id: str = None,
        block_height: int = None,
        create_time: int = None,
        node_infos: List[DescribeAntChainInformationResponseBodyResultNodeInfos] = None,
        node_number: int = None,
        normal: bool = None,
        transaction_sum: int = None,
        version: str = None,
    ):
        self.abnormal_nodes = abnormal_nodes
        self.ant_chain_id = ant_chain_id
        self.block_height = block_height
        self.create_time = create_time
        self.node_infos = node_infos
        self.node_number = node_number
        self.normal = normal
        self.transaction_sum = transaction_sum
        self.version = version

    def validate(self):
        if self.node_infos:
            for k in self.node_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.abnormal_nodes is not None:
            result['AbnormalNodes'] = self.abnormal_nodes
        if self.ant_chain_id is not None:
            result['AntChainId'] = self.ant_chain_id
        if self.block_height is not None:
            result['BlockHeight'] = self.block_height
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        result['NodeInfos'] = []
        if self.node_infos is not None:
            for k in self.node_infos:
                result['NodeInfos'].append(k.to_map() if k else None)
        if self.node_number is not None:
            result['NodeNumber'] = self.node_number
        if self.normal is not None:
            result['Normal'] = self.normal
        if self.transaction_sum is not None:
            result['TransactionSum'] = self.transaction_sum
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AbnormalNodes') is not None:
            self.abnormal_nodes = m.get('AbnormalNodes')
        if m.get('AntChainId') is not None:
            self.ant_chain_id = m.get('AntChainId')
        if m.get('BlockHeight') is not None:
            self.block_height = m.get('BlockHeight')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        self.node_infos = []
        if m.get('NodeInfos') is not None:
            for k in m.get('NodeInfos'):
                temp_model = DescribeAntChainInformationResponseBodyResultNodeInfos()
                self.node_infos.append(temp_model.from_map(k))
        if m.get('NodeNumber') is not None:
            self.node_number = m.get('NodeNumber')
        if m.get('Normal') is not None:
            self.normal = m.get('Normal')
        if m.get('TransactionSum') is not None:
            self.transaction_sum = m.get('TransactionSum')
        if m.get('Version') is not None:
            self.version = m.get('Version')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        status_code: int = None,
        body: DescribeAntChainInformationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeAntChainInformationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAntChainInformationV2Request(TeaModel):
    def __init__(
        self,
        ant_chain_id: str = None,
        consortium_id: str = None,
    ):
        # This parameter is required.
        self.ant_chain_id = ant_chain_id
        self.consortium_id = consortium_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ant_chain_id is not None:
            result['AntChainId'] = self.ant_chain_id
        if self.consortium_id is not None:
            result['ConsortiumId'] = self.consortium_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AntChainId') is not None:
            self.ant_chain_id = m.get('AntChainId')
        if m.get('ConsortiumId') is not None:
            self.consortium_id = m.get('ConsortiumId')
        return self


class DescribeAntChainInformationV2ResponseBodyResultNodeInfos(TeaModel):
    def __init__(
        self,
        block_height: int = None,
        node_name: str = None,
        status: bool = None,
        version: str = None,
    ):
        self.block_height = block_height
        self.node_name = node_name
        self.status = status
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.block_height is not None:
            result['BlockHeight'] = self.block_height
        if self.node_name is not None:
            result['NodeName'] = self.node_name
        if self.status is not None:
            result['Status'] = self.status
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BlockHeight') is not None:
            self.block_height = m.get('BlockHeight')
        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class DescribeAntChainInformationV2ResponseBodyResult(TeaModel):
    def __init__(
        self,
        abnormal_nodes: int = None,
        ant_chain_id: str = None,
        block_height: int = None,
        create_time: int = None,
        is_role: bool = None,
        node_infos: List[DescribeAntChainInformationV2ResponseBodyResultNodeInfos] = None,
        node_number: int = None,
        normal: bool = None,
        transaction_sum: int = None,
        version: str = None,
    ):
        self.abnormal_nodes = abnormal_nodes
        self.ant_chain_id = ant_chain_id
        self.block_height = block_height
        self.create_time = create_time
        self.is_role = is_role
        self.node_infos = node_infos
        self.node_number = node_number
        self.normal = normal
        self.transaction_sum = transaction_sum
        self.version = version

    def validate(self):
        if self.node_infos:
            for k in self.node_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.abnormal_nodes is not None:
            result['AbnormalNodes'] = self.abnormal_nodes
        if self.ant_chain_id is not None:
            result['AntChainId'] = self.ant_chain_id
        if self.block_height is not None:
            result['BlockHeight'] = self.block_height
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.is_role is not None:
            result['IsRole'] = self.is_role
        result['NodeInfos'] = []
        if self.node_infos is not None:
            for k in self.node_infos:
                result['NodeInfos'].append(k.to_map() if k else None)
        if self.node_number is not None:
            result['NodeNumber'] = self.node_number
        if self.normal is not None:
            result['Normal'] = self.normal
        if self.transaction_sum is not None:
            result['TransactionSum'] = self.transaction_sum
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AbnormalNodes') is not None:
            self.abnormal_nodes = m.get('AbnormalNodes')
        if m.get('AntChainId') is not None:
            self.ant_chain_id = m.get('AntChainId')
        if m.get('BlockHeight') is not None:
            self.block_height = m.get('BlockHeight')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('IsRole') is not None:
            self.is_role = m.get('IsRole')
        self.node_infos = []
        if m.get('NodeInfos') is not None:
            for k in m.get('NodeInfos'):
                temp_model = DescribeAntChainInformationV2ResponseBodyResultNodeInfos()
                self.node_infos.append(temp_model.from_map(k))
        if m.get('NodeNumber') is not None:
            self.node_number = m.get('NodeNumber')
        if m.get('Normal') is not None:
            self.normal = m.get('Normal')
        if m.get('TransactionSum') is not None:
            self.transaction_sum = m.get('TransactionSum')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class DescribeAntChainInformationV2ResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: str = None,
        message: str = None,
        request_id: str = None,
        result: DescribeAntChainInformationV2ResponseBodyResult = None,
        result_code: str = None,
        result_message: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.result = result
        self.result_code = result_code
        self.result_message = result_message
        self.success = success

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        if self.result_message is not None:
            result['ResultMessage'] = self.result_message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = DescribeAntChainInformationV2ResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeAntChainInformationV2Response(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAntChainInformationV2ResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeAntChainInformationV2ResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAntChainLatestBlocksRequest(TeaModel):
    def __init__(
        self,
        ant_chain_id: str = None,
    ):
        # This parameter is required.
        self.ant_chain_id = ant_chain_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        status_code: int = None,
        body: DescribeAntChainLatestBlocksResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeAntChainLatestBlocksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAntChainLatestBlocksV2Request(TeaModel):
    def __init__(
        self,
        ant_chain_id: str = None,
        consortium_id: str = None,
    ):
        # This parameter is required.
        self.ant_chain_id = ant_chain_id
        self.consortium_id = consortium_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ant_chain_id is not None:
            result['AntChainId'] = self.ant_chain_id
        if self.consortium_id is not None:
            result['ConsortiumId'] = self.consortium_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AntChainId') is not None:
            self.ant_chain_id = m.get('AntChainId')
        if m.get('ConsortiumId') is not None:
            self.consortium_id = m.get('ConsortiumId')
        return self


class DescribeAntChainLatestBlocksV2ResponseBodyResult(TeaModel):
    def __init__(
        self,
        alias: str = None,
        biz_data: str = None,
        block_hash: str = None,
        create_time: int = None,
        height: int = None,
        previous_hash: str = None,
        root_tx_hash: str = None,
        size: int = None,
        transaction_size: int = None,
        version: int = None,
    ):
        self.alias = alias
        self.biz_data = biz_data
        self.block_hash = block_hash
        self.create_time = create_time
        self.height = height
        self.previous_hash = previous_hash
        self.root_tx_hash = root_tx_hash
        self.size = size
        self.transaction_size = transaction_size
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias is not None:
            result['Alias'] = self.alias
        if self.biz_data is not None:
            result['BizData'] = self.biz_data
        if self.block_hash is not None:
            result['BlockHash'] = self.block_hash
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.height is not None:
            result['Height'] = self.height
        if self.previous_hash is not None:
            result['PreviousHash'] = self.previous_hash
        if self.root_tx_hash is not None:
            result['RootTxHash'] = self.root_tx_hash
        if self.size is not None:
            result['Size'] = self.size
        if self.transaction_size is not None:
            result['TransactionSize'] = self.transaction_size
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Alias') is not None:
            self.alias = m.get('Alias')
        if m.get('BizData') is not None:
            self.biz_data = m.get('BizData')
        if m.get('BlockHash') is not None:
            self.block_hash = m.get('BlockHash')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('PreviousHash') is not None:
            self.previous_hash = m.get('PreviousHash')
        if m.get('RootTxHash') is not None:
            self.root_tx_hash = m.get('RootTxHash')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('TransactionSize') is not None:
            self.transaction_size = m.get('TransactionSize')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class DescribeAntChainLatestBlocksV2ResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: str = None,
        message: str = None,
        request_id: str = None,
        result: List[DescribeAntChainLatestBlocksV2ResponseBodyResult] = None,
        result_code: str = None,
        result_message: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.result = result
        self.result_code = result_code
        self.result_message = result_message
        self.success = success

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        if self.result_message is not None:
            result['ResultMessage'] = self.result_message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = DescribeAntChainLatestBlocksV2ResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeAntChainLatestBlocksV2Response(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAntChainLatestBlocksV2ResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeAntChainLatestBlocksV2ResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAntChainLatestTransactionDigestsRequest(TeaModel):
    def __init__(
        self,
        ant_chain_id: str = None,
    ):
        # This parameter is required.
        self.ant_chain_id = ant_chain_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        status_code: int = None,
        body: DescribeAntChainLatestTransactionDigestsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeAntChainLatestTransactionDigestsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAntChainLatestTransactionDigestsV2Request(TeaModel):
    def __init__(
        self,
        ant_chain_id: str = None,
        consortium_id: str = None,
    ):
        # This parameter is required.
        self.ant_chain_id = ant_chain_id
        self.consortium_id = consortium_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ant_chain_id is not None:
            result['AntChainId'] = self.ant_chain_id
        if self.consortium_id is not None:
            result['ConsortiumId'] = self.consortium_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AntChainId') is not None:
            self.ant_chain_id = m.get('AntChainId')
        if m.get('ConsortiumId') is not None:
            self.consortium_id = m.get('ConsortiumId')
        return self


class DescribeAntChainLatestTransactionDigestsV2ResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: str = None,
        message: str = None,
        request_id: str = None,
        result: List[str] = None,
        result_code: str = None,
        result_message: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.result = result
        self.result_code = result_code
        self.result_message = result_message
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        if self.result_message is not None:
            result['ResultMessage'] = self.result_message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeAntChainLatestTransactionDigestsV2Response(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAntChainLatestTransactionDigestsV2ResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeAntChainLatestTransactionDigestsV2ResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAntChainMembersRequest(TeaModel):
    def __init__(
        self,
        consortium_id: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # This parameter is required.
        self.consortium_id = consortium_id
        self.page_number = page_number
        # This parameter is required.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consortium_id is not None:
            result['ConsortiumId'] = self.consortium_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsortiumId') is not None:
            self.consortium_id = m.get('ConsortiumId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeAntChainMembersResponseBodyResultMembers(TeaModel):
    def __init__(
        self,
        join_time: int = None,
        member_id: str = None,
        member_name: str = None,
        role: str = None,
        status: str = None,
    ):
        self.join_time = join_time
        self.member_id = member_id
        self.member_name = member_name
        self.role = role
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.join_time is not None:
            result['JoinTime'] = self.join_time
        if self.member_id is not None:
            result['MemberId'] = self.member_id
        if self.member_name is not None:
            result['MemberName'] = self.member_name
        if self.role is not None:
            result['Role'] = self.role
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JoinTime') is not None:
            self.join_time = m.get('JoinTime')
        if m.get('MemberId') is not None:
            self.member_id = m.get('MemberId')
        if m.get('MemberName') is not None:
            self.member_name = m.get('MemberName')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeAntChainMembersResponseBodyResultPagination(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        status_code: int = None,
        body: DescribeAntChainMembersResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeAntChainMembersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAntChainMembersV2Request(TeaModel):
    def __init__(
        self,
        consortium_id: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # This parameter is required.
        self.consortium_id = consortium_id
        self.page_number = page_number
        # This parameter is required.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consortium_id is not None:
            result['ConsortiumId'] = self.consortium_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsortiumId') is not None:
            self.consortium_id = m.get('ConsortiumId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeAntChainMembersV2ResponseBodyResultMembers(TeaModel):
    def __init__(
        self,
        join_time: int = None,
        member_id: str = None,
        member_name: str = None,
        role: str = None,
        status: str = None,
    ):
        self.join_time = join_time
        self.member_id = member_id
        self.member_name = member_name
        self.role = role
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.join_time is not None:
            result['JoinTime'] = self.join_time
        if self.member_id is not None:
            result['MemberId'] = self.member_id
        if self.member_name is not None:
            result['MemberName'] = self.member_name
        if self.role is not None:
            result['Role'] = self.role
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JoinTime') is not None:
            self.join_time = m.get('JoinTime')
        if m.get('MemberId') is not None:
            self.member_id = m.get('MemberId')
        if m.get('MemberName') is not None:
            self.member_name = m.get('MemberName')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeAntChainMembersV2ResponseBodyResultPagination(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

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


class DescribeAntChainMembersV2ResponseBodyResult(TeaModel):
    def __init__(
        self,
        members: List[DescribeAntChainMembersV2ResponseBodyResultMembers] = None,
        pagination: DescribeAntChainMembersV2ResponseBodyResultPagination = None,
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
                temp_model = DescribeAntChainMembersV2ResponseBodyResultMembers()
                self.members.append(temp_model.from_map(k))
        if m.get('Pagination') is not None:
            temp_model = DescribeAntChainMembersV2ResponseBodyResultPagination()
            self.pagination = temp_model.from_map(m['Pagination'])
        return self


class DescribeAntChainMembersV2ResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: str = None,
        message: str = None,
        request_id: str = None,
        result: DescribeAntChainMembersV2ResponseBodyResult = None,
        result_code: str = None,
        result_message: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.result = result
        self.result_code = result_code
        self.result_message = result_message
        self.success = success

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        if self.result_message is not None:
            result['ResultMessage'] = self.result_message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = DescribeAntChainMembersV2ResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeAntChainMembersV2Response(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAntChainMembersV2ResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeAntChainMembersV2ResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAntChainMiniAppBrowserQRCodeAccessLogRequest(TeaModel):
    def __init__(
        self,
        ant_chain_id: str = None,
        qrcode_type: str = None,
    ):
        # This parameter is required.
        self.ant_chain_id = ant_chain_id
        # This parameter is required.
        self.qrcode_type = qrcode_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        access_alipay_account_count: int = None,
        access_count: int = None,
    ):
        self.access_alipay_account_count = access_alipay_account_count
        self.access_count = access_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_alipay_account_count is not None:
            result['AccessAlipayAccountCount'] = self.access_alipay_account_count
        if self.access_count is not None:
            result['AccessCount'] = self.access_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessAlipayAccountCount') is not None:
            self.access_alipay_account_count = m.get('AccessAlipayAccountCount')
        if m.get('AccessCount') is not None:
            self.access_count = m.get('AccessCount')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        status_code: int = None,
        body: DescribeAntChainMiniAppBrowserQRCodeAccessLogResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeAntChainMiniAppBrowserQRCodeAccessLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAntChainMiniAppBrowserQRCodeAccessLogV2Request(TeaModel):
    def __init__(
        self,
        ant_chain_id: str = None,
        qrcode_type: str = None,
    ):
        # This parameter is required.
        self.ant_chain_id = ant_chain_id
        # This parameter is required.
        self.qrcode_type = qrcode_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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


class DescribeAntChainMiniAppBrowserQRCodeAccessLogV2ResponseBodyResult(TeaModel):
    def __init__(
        self,
        access_alipay_account_count: int = None,
        access_count: int = None,
    ):
        self.access_alipay_account_count = access_alipay_account_count
        self.access_count = access_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_alipay_account_count is not None:
            result['AccessAlipayAccountCount'] = self.access_alipay_account_count
        if self.access_count is not None:
            result['AccessCount'] = self.access_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessAlipayAccountCount') is not None:
            self.access_alipay_account_count = m.get('AccessAlipayAccountCount')
        if m.get('AccessCount') is not None:
            self.access_count = m.get('AccessCount')
        return self


class DescribeAntChainMiniAppBrowserQRCodeAccessLogV2ResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: str = None,
        message: str = None,
        request_id: str = None,
        result: DescribeAntChainMiniAppBrowserQRCodeAccessLogV2ResponseBodyResult = None,
        result_code: str = None,
        result_message: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.result = result
        self.result_code = result_code
        self.result_message = result_message
        self.success = success

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        if self.result_message is not None:
            result['ResultMessage'] = self.result_message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = DescribeAntChainMiniAppBrowserQRCodeAccessLogV2ResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeAntChainMiniAppBrowserQRCodeAccessLogV2Response(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAntChainMiniAppBrowserQRCodeAccessLogV2ResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeAntChainMiniAppBrowserQRCodeAccessLogV2ResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAntChainMiniAppBrowserQRCodeAuthorizedUsersRequest(TeaModel):
    def __init__(
        self,
        ant_chain_id: str = None,
        page_number: int = None,
        page_size: int = None,
        qrcode_type: str = None,
    ):
        # This parameter is required.
        self.ant_chain_id = ant_chain_id
        # This parameter is required.
        self.page_number = page_number
        # This parameter is required.
        self.page_size = page_size
        # This parameter is required.
        self.qrcode_type = qrcode_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ant_chain_id is not None:
            result['AntChainId'] = self.ant_chain_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.qrcode_type is not None:
            result['QRCodeType'] = self.qrcode_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AntChainId') is not None:
            self.ant_chain_id = m.get('AntChainId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('QRCodeType') is not None:
            self.qrcode_type = m.get('QRCodeType')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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


class DescribeAntChainMiniAppBrowserQRCodeAuthorizedUsersResponseBodyResult(TeaModel):
    def __init__(
        self,
        ant_chain_id: str = None,
        authorization_type: str = None,
        authorized_user_list: List[DescribeAntChainMiniAppBrowserQRCodeAuthorizedUsersResponseBodyResultAuthorizedUserList] = None,
        pagination: DescribeAntChainMiniAppBrowserQRCodeAuthorizedUsersResponseBodyResultPagination = None,
        qrcode_type: str = None,
    ):
        self.ant_chain_id = ant_chain_id
        self.authorization_type = authorization_type
        self.authorized_user_list = authorized_user_list
        self.pagination = pagination
        self.qrcode_type = qrcode_type

    def validate(self):
        if self.authorized_user_list:
            for k in self.authorized_user_list:
                if k:
                    k.validate()
        if self.pagination:
            self.pagination.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ant_chain_id is not None:
            result['AntChainId'] = self.ant_chain_id
        if self.authorization_type is not None:
            result['AuthorizationType'] = self.authorization_type
        result['AuthorizedUserList'] = []
        if self.authorized_user_list is not None:
            for k in self.authorized_user_list:
                result['AuthorizedUserList'].append(k.to_map() if k else None)
        if self.pagination is not None:
            result['Pagination'] = self.pagination.to_map()
        if self.qrcode_type is not None:
            result['QRCodeType'] = self.qrcode_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AntChainId') is not None:
            self.ant_chain_id = m.get('AntChainId')
        if m.get('AuthorizationType') is not None:
            self.authorization_type = m.get('AuthorizationType')
        self.authorized_user_list = []
        if m.get('AuthorizedUserList') is not None:
            for k in m.get('AuthorizedUserList'):
                temp_model = DescribeAntChainMiniAppBrowserQRCodeAuthorizedUsersResponseBodyResultAuthorizedUserList()
                self.authorized_user_list.append(temp_model.from_map(k))
        if m.get('Pagination') is not None:
            temp_model = DescribeAntChainMiniAppBrowserQRCodeAuthorizedUsersResponseBodyResultPagination()
            self.pagination = temp_model.from_map(m['Pagination'])
        if m.get('QRCodeType') is not None:
            self.qrcode_type = m.get('QRCodeType')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        status_code: int = None,
        body: DescribeAntChainMiniAppBrowserQRCodeAuthorizedUsersResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeAntChainMiniAppBrowserQRCodeAuthorizedUsersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAntChainMiniAppBrowserQRCodeAuthorizedUsersV2Request(TeaModel):
    def __init__(
        self,
        ant_chain_id: str = None,
        page_number: int = None,
        page_size: int = None,
        qrcode_type: str = None,
    ):
        # This parameter is required.
        self.ant_chain_id = ant_chain_id
        # This parameter is required.
        self.page_number = page_number
        # This parameter is required.
        self.page_size = page_size
        # This parameter is required.
        self.qrcode_type = qrcode_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ant_chain_id is not None:
            result['AntChainId'] = self.ant_chain_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.qrcode_type is not None:
            result['QRCodeType'] = self.qrcode_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AntChainId') is not None:
            self.ant_chain_id = m.get('AntChainId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('QRCodeType') is not None:
            self.qrcode_type = m.get('QRCodeType')
        return self


class DescribeAntChainMiniAppBrowserQRCodeAuthorizedUsersV2ResponseBodyResultAuthorizedUserList(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

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


class DescribeAntChainMiniAppBrowserQRCodeAuthorizedUsersV2ResponseBodyResultPagination(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

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


class DescribeAntChainMiniAppBrowserQRCodeAuthorizedUsersV2ResponseBodyResult(TeaModel):
    def __init__(
        self,
        ant_chain_id: str = None,
        authorization_type: str = None,
        authorized_user_list: List[DescribeAntChainMiniAppBrowserQRCodeAuthorizedUsersV2ResponseBodyResultAuthorizedUserList] = None,
        pagination: DescribeAntChainMiniAppBrowserQRCodeAuthorizedUsersV2ResponseBodyResultPagination = None,
        qrcode_type: str = None,
    ):
        self.ant_chain_id = ant_chain_id
        self.authorization_type = authorization_type
        self.authorized_user_list = authorized_user_list
        self.pagination = pagination
        self.qrcode_type = qrcode_type

    def validate(self):
        if self.authorized_user_list:
            for k in self.authorized_user_list:
                if k:
                    k.validate()
        if self.pagination:
            self.pagination.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ant_chain_id is not None:
            result['AntChainId'] = self.ant_chain_id
        if self.authorization_type is not None:
            result['AuthorizationType'] = self.authorization_type
        result['AuthorizedUserList'] = []
        if self.authorized_user_list is not None:
            for k in self.authorized_user_list:
                result['AuthorizedUserList'].append(k.to_map() if k else None)
        if self.pagination is not None:
            result['Pagination'] = self.pagination.to_map()
        if self.qrcode_type is not None:
            result['QRCodeType'] = self.qrcode_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AntChainId') is not None:
            self.ant_chain_id = m.get('AntChainId')
        if m.get('AuthorizationType') is not None:
            self.authorization_type = m.get('AuthorizationType')
        self.authorized_user_list = []
        if m.get('AuthorizedUserList') is not None:
            for k in m.get('AuthorizedUserList'):
                temp_model = DescribeAntChainMiniAppBrowserQRCodeAuthorizedUsersV2ResponseBodyResultAuthorizedUserList()
                self.authorized_user_list.append(temp_model.from_map(k))
        if m.get('Pagination') is not None:
            temp_model = DescribeAntChainMiniAppBrowserQRCodeAuthorizedUsersV2ResponseBodyResultPagination()
            self.pagination = temp_model.from_map(m['Pagination'])
        if m.get('QRCodeType') is not None:
            self.qrcode_type = m.get('QRCodeType')
        return self


class DescribeAntChainMiniAppBrowserQRCodeAuthorizedUsersV2ResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: str = None,
        message: str = None,
        request_id: str = None,
        result: DescribeAntChainMiniAppBrowserQRCodeAuthorizedUsersV2ResponseBodyResult = None,
        result_code: str = None,
        result_message: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.result = result
        self.result_code = result_code
        self.result_message = result_message
        self.success = success

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        if self.result_message is not None:
            result['ResultMessage'] = self.result_message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = DescribeAntChainMiniAppBrowserQRCodeAuthorizedUsersV2ResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeAntChainMiniAppBrowserQRCodeAuthorizedUsersV2Response(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAntChainMiniAppBrowserQRCodeAuthorizedUsersV2ResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeAntChainMiniAppBrowserQRCodeAuthorizedUsersV2ResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAntChainMiniAppBrowserTransactionQRCodeRequest(TeaModel):
    def __init__(
        self,
        ant_chain_id: str = None,
        transaction_hash: str = None,
    ):
        # This parameter is required.
        self.ant_chain_id = ant_chain_id
        # This parameter is required.
        self.transaction_hash = transaction_hash

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        ant_chain_id: str = None,
        base_64qrcode_png: str = None,
        qrcode_content: str = None,
        transaction_hash: str = None,
    ):
        self.ant_chain_id = ant_chain_id
        self.base_64qrcode_png = base_64qrcode_png
        self.qrcode_content = qrcode_content
        self.transaction_hash = transaction_hash

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ant_chain_id is not None:
            result['AntChainId'] = self.ant_chain_id
        if self.base_64qrcode_png is not None:
            result['Base64QRCodePNG'] = self.base_64qrcode_png
        if self.qrcode_content is not None:
            result['QRCodeContent'] = self.qrcode_content
        if self.transaction_hash is not None:
            result['TransactionHash'] = self.transaction_hash
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AntChainId') is not None:
            self.ant_chain_id = m.get('AntChainId')
        if m.get('Base64QRCodePNG') is not None:
            self.base_64qrcode_png = m.get('Base64QRCodePNG')
        if m.get('QRCodeContent') is not None:
            self.qrcode_content = m.get('QRCodeContent')
        if m.get('TransactionHash') is not None:
            self.transaction_hash = m.get('TransactionHash')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        status_code: int = None,
        body: DescribeAntChainMiniAppBrowserTransactionQRCodeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeAntChainMiniAppBrowserTransactionQRCodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAntChainMiniAppBrowserTransactionQRCodeNewRequest(TeaModel):
    def __init__(
        self,
        ant_chain_id: str = None,
        contract_id: str = None,
        transaction_hash: str = None,
    ):
        # This parameter is required.
        self.ant_chain_id = ant_chain_id
        self.contract_id = contract_id
        # This parameter is required.
        self.transaction_hash = transaction_hash

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ant_chain_id is not None:
            result['AntChainId'] = self.ant_chain_id
        if self.contract_id is not None:
            result['ContractId'] = self.contract_id
        if self.transaction_hash is not None:
            result['TransactionHash'] = self.transaction_hash
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AntChainId') is not None:
            self.ant_chain_id = m.get('AntChainId')
        if m.get('ContractId') is not None:
            self.contract_id = m.get('ContractId')
        if m.get('TransactionHash') is not None:
            self.transaction_hash = m.get('TransactionHash')
        return self


class DescribeAntChainMiniAppBrowserTransactionQRCodeNewResponseBodyResult(TeaModel):
    def __init__(
        self,
        ant_chain_id: str = None,
        base_64qrcode_png: str = None,
        qrcode_content: str = None,
        transaction_hash: str = None,
    ):
        self.ant_chain_id = ant_chain_id
        self.base_64qrcode_png = base_64qrcode_png
        self.qrcode_content = qrcode_content
        self.transaction_hash = transaction_hash

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ant_chain_id is not None:
            result['AntChainId'] = self.ant_chain_id
        if self.base_64qrcode_png is not None:
            result['Base64QRCodePNG'] = self.base_64qrcode_png
        if self.qrcode_content is not None:
            result['QRCodeContent'] = self.qrcode_content
        if self.transaction_hash is not None:
            result['TransactionHash'] = self.transaction_hash
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AntChainId') is not None:
            self.ant_chain_id = m.get('AntChainId')
        if m.get('Base64QRCodePNG') is not None:
            self.base_64qrcode_png = m.get('Base64QRCodePNG')
        if m.get('QRCodeContent') is not None:
            self.qrcode_content = m.get('QRCodeContent')
        if m.get('TransactionHash') is not None:
            self.transaction_hash = m.get('TransactionHash')
        return self


class DescribeAntChainMiniAppBrowserTransactionQRCodeNewResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: str = None,
        message: str = None,
        request_id: str = None,
        result: DescribeAntChainMiniAppBrowserTransactionQRCodeNewResponseBodyResult = None,
        result_code: str = None,
        result_message: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.result = result
        self.result_code = result_code
        self.result_message = result_message
        self.success = success

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        if self.result_message is not None:
            result['ResultMessage'] = self.result_message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = DescribeAntChainMiniAppBrowserTransactionQRCodeNewResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeAntChainMiniAppBrowserTransactionQRCodeNewResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAntChainMiniAppBrowserTransactionQRCodeNewResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeAntChainMiniAppBrowserTransactionQRCodeNewResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAntChainNodesRequest(TeaModel):
    def __init__(
        self,
        ant_chain_id: str = None,
    ):
        # This parameter is required.
        self.ant_chain_id = ant_chain_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        status_code: int = None,
        body: DescribeAntChainNodesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeAntChainNodesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAntChainNodesV2Request(TeaModel):
    def __init__(
        self,
        ant_chain_id: str = None,
        consortium_id: str = None,
    ):
        # This parameter is required.
        self.ant_chain_id = ant_chain_id
        self.consortium_id = consortium_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ant_chain_id is not None:
            result['AntChainId'] = self.ant_chain_id
        if self.consortium_id is not None:
            result['ConsortiumId'] = self.consortium_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AntChainId') is not None:
            self.ant_chain_id = m.get('AntChainId')
        if m.get('ConsortiumId') is not None:
            self.consortium_id = m.get('ConsortiumId')
        return self


class DescribeAntChainNodesV2ResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: str = None,
        message: str = None,
        request_id: str = None,
        result: List[str] = None,
        result_code: str = None,
        result_message: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.result = result
        self.result_code = result_code
        self.result_message = result_message
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        if self.result_message is not None:
            result['ResultMessage'] = self.result_message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeAntChainNodesV2Response(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAntChainNodesV2ResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeAntChainNodesV2ResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAntChainQRCodeAuthorizationRequest(TeaModel):
    def __init__(
        self,
        ant_chain_id: str = None,
        qrcode_type: str = None,
    ):
        # This parameter is required.
        self.ant_chain_id = ant_chain_id
        # This parameter is required.
        self.qrcode_type = qrcode_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        ant_chain_id: str = None,
        authorization_type: str = None,
        qrcode_type: str = None,
    ):
        self.ant_chain_id = ant_chain_id
        self.authorization_type = authorization_type
        self.qrcode_type = qrcode_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ant_chain_id is not None:
            result['AntChainId'] = self.ant_chain_id
        if self.authorization_type is not None:
            result['AuthorizationType'] = self.authorization_type
        if self.qrcode_type is not None:
            result['QRCodeType'] = self.qrcode_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AntChainId') is not None:
            self.ant_chain_id = m.get('AntChainId')
        if m.get('AuthorizationType') is not None:
            self.authorization_type = m.get('AuthorizationType')
        if m.get('QRCodeType') is not None:
            self.qrcode_type = m.get('QRCodeType')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        status_code: int = None,
        body: DescribeAntChainQRCodeAuthorizationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeAntChainQRCodeAuthorizationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAntChainQRCodeAuthorizationV2Request(TeaModel):
    def __init__(
        self,
        ant_chain_id: str = None,
        qrcode_type: str = None,
    ):
        # This parameter is required.
        self.ant_chain_id = ant_chain_id
        # This parameter is required.
        self.qrcode_type = qrcode_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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


class DescribeAntChainQRCodeAuthorizationV2ResponseBodyResult(TeaModel):
    def __init__(
        self,
        ant_chain_id: str = None,
        authorization_type: str = None,
        qrcode_type: str = None,
    ):
        self.ant_chain_id = ant_chain_id
        self.authorization_type = authorization_type
        self.qrcode_type = qrcode_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ant_chain_id is not None:
            result['AntChainId'] = self.ant_chain_id
        if self.authorization_type is not None:
            result['AuthorizationType'] = self.authorization_type
        if self.qrcode_type is not None:
            result['QRCodeType'] = self.qrcode_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AntChainId') is not None:
            self.ant_chain_id = m.get('AntChainId')
        if m.get('AuthorizationType') is not None:
            self.authorization_type = m.get('AuthorizationType')
        if m.get('QRCodeType') is not None:
            self.qrcode_type = m.get('QRCodeType')
        return self


class DescribeAntChainQRCodeAuthorizationV2ResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: str = None,
        message: str = None,
        request_id: str = None,
        result: DescribeAntChainQRCodeAuthorizationV2ResponseBodyResult = None,
        result_code: str = None,
        result_message: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.result = result
        self.result_code = result_code
        self.result_message = result_message
        self.success = success

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        if self.result_message is not None:
            result['ResultMessage'] = self.result_message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = DescribeAntChainQRCodeAuthorizationV2ResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeAntChainQRCodeAuthorizationV2Response(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAntChainQRCodeAuthorizationV2ResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeAntChainQRCodeAuthorizationV2ResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAntChainTransactionRequest(TeaModel):
    def __init__(
        self,
        ant_chain_id: str = None,
        hash: str = None,
    ):
        # This parameter is required.
        self.ant_chain_id = ant_chain_id
        # This parameter is required.
        self.hash = hash

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        data: str = None,
        extentions: List[str] = None,
        from_: str = None,
        gas: str = None,
        hash: str = None,
        nonce: str = None,
        period: int = None,
        signatures: List[str] = None,
        timestamp: int = None,
        to: str = None,
        tx_type: str = None,
        value: str = None,
    ):
        self.data = data
        self.extentions = extentions
        self.from_ = from_
        self.gas = gas
        self.hash = hash
        self.nonce = nonce
        # Period
        self.period = period
        self.signatures = signatures
        self.timestamp = timestamp
        self.to = to
        self.tx_type = tx_type
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.extentions is not None:
            result['Extentions'] = self.extentions
        if self.from_ is not None:
            result['From'] = self.from_
        if self.gas is not None:
            result['Gas'] = self.gas
        if self.hash is not None:
            result['Hash'] = self.hash
        if self.nonce is not None:
            result['Nonce'] = self.nonce
        if self.period is not None:
            result['Period'] = self.period
        if self.signatures is not None:
            result['Signatures'] = self.signatures
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.to is not None:
            result['To'] = self.to
        if self.tx_type is not None:
            result['TxType'] = self.tx_type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Extentions') is not None:
            self.extentions = m.get('Extentions')
        if m.get('From') is not None:
            self.from_ = m.get('From')
        if m.get('Gas') is not None:
            self.gas = m.get('Gas')
        if m.get('Hash') is not None:
            self.hash = m.get('Hash')
        if m.get('Nonce') is not None:
            self.nonce = m.get('Nonce')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('Signatures') is not None:
            self.signatures = m.get('Signatures')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('To') is not None:
            self.to = m.get('To')
        if m.get('TxType') is not None:
            self.tx_type = m.get('TxType')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeAntChainTransactionResponseBodyResult(TeaModel):
    def __init__(
        self,
        block_hash: str = None,
        block_height: int = None,
        block_version: str = None,
        create_time: int = None,
        hash: str = None,
        transaction: DescribeAntChainTransactionResponseBodyResultTransaction = None,
    ):
        self.block_hash = block_hash
        self.block_height = block_height
        self.block_version = block_version
        self.create_time = create_time
        self.hash = hash
        self.transaction = transaction

    def validate(self):
        if self.transaction:
            self.transaction.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.block_hash is not None:
            result['BlockHash'] = self.block_hash
        if self.block_height is not None:
            result['BlockHeight'] = self.block_height
        if self.block_version is not None:
            result['BlockVersion'] = self.block_version
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.hash is not None:
            result['Hash'] = self.hash
        if self.transaction is not None:
            result['Transaction'] = self.transaction.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BlockHash') is not None:
            self.block_hash = m.get('BlockHash')
        if m.get('BlockHeight') is not None:
            self.block_height = m.get('BlockHeight')
        if m.get('BlockVersion') is not None:
            self.block_version = m.get('BlockVersion')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Hash') is not None:
            self.hash = m.get('Hash')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        status_code: int = None,
        body: DescribeAntChainTransactionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
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
        # This parameter is required.
        self.ant_chain_id = ant_chain_id
        # This parameter is required.
        self.hash = hash

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        gas_used: str = None,
        logs: List[str] = None,
        result: int = None,
    ):
        self.data = data
        self.gas_used = gas_used
        self.logs = logs
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.gas_used is not None:
            result['GasUsed'] = self.gas_used
        if self.logs is not None:
            result['Logs'] = self.logs
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('GasUsed') is not None:
            self.gas_used = m.get('GasUsed')
        if m.get('Logs') is not None:
            self.logs = m.get('Logs')
        if m.get('Result') is not None:
            self.result = m.get('Result')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        status_code: int = None,
        body: DescribeAntChainTransactionReceiptResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeAntChainTransactionReceiptResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAntChainTransactionReceiptV2Request(TeaModel):
    def __init__(
        self,
        ant_chain_id: str = None,
        consortium_id: str = None,
        hash: str = None,
    ):
        # This parameter is required.
        self.ant_chain_id = ant_chain_id
        self.consortium_id = consortium_id
        # This parameter is required.
        self.hash = hash

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ant_chain_id is not None:
            result['AntChainId'] = self.ant_chain_id
        if self.consortium_id is not None:
            result['ConsortiumId'] = self.consortium_id
        if self.hash is not None:
            result['Hash'] = self.hash
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AntChainId') is not None:
            self.ant_chain_id = m.get('AntChainId')
        if m.get('ConsortiumId') is not None:
            self.consortium_id = m.get('ConsortiumId')
        if m.get('Hash') is not None:
            self.hash = m.get('Hash')
        return self


class DescribeAntChainTransactionReceiptV2ResponseBodyResult(TeaModel):
    def __init__(
        self,
        data: str = None,
        gas_used: str = None,
        logs: List[str] = None,
        result: int = None,
    ):
        self.data = data
        self.gas_used = gas_used
        self.logs = logs
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.gas_used is not None:
            result['GasUsed'] = self.gas_used
        if self.logs is not None:
            result['Logs'] = self.logs
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('GasUsed') is not None:
            self.gas_used = m.get('GasUsed')
        if m.get('Logs') is not None:
            self.logs = m.get('Logs')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class DescribeAntChainTransactionReceiptV2ResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: str = None,
        message: str = None,
        request_id: str = None,
        result: DescribeAntChainTransactionReceiptV2ResponseBodyResult = None,
        result_code: str = None,
        result_message: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.result = result
        self.result_code = result_code
        self.result_message = result_message
        self.success = success

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        if self.result_message is not None:
            result['ResultMessage'] = self.result_message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = DescribeAntChainTransactionReceiptV2ResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeAntChainTransactionReceiptV2Response(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAntChainTransactionReceiptV2ResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeAntChainTransactionReceiptV2ResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAntChainTransactionStatisticsRequest(TeaModel):
    def __init__(
        self,
        ant_chain_id: str = None,
        end: int = None,
        start: int = None,
    ):
        # This parameter is required.
        self.ant_chain_id = ant_chain_id
        # This parameter is required.
        self.end = end
        # This parameter is required.
        self.start = start

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ant_chain_id is not None:
            result['AntChainId'] = self.ant_chain_id
        if self.end is not None:
            result['End'] = self.end
        if self.start is not None:
            result['Start'] = self.start
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AntChainId') is not None:
            self.ant_chain_id = m.get('AntChainId')
        if m.get('End') is not None:
            self.end = m.get('End')
        if m.get('Start') is not None:
            self.start = m.get('Start')
        return self


class DescribeAntChainTransactionStatisticsResponseBodyResult(TeaModel):
    def __init__(
        self,
        ant_chain_id: str = None,
        creat_time: int = None,
        dt: str = None,
        last_sum_block_height: int = None,
        trans_count: int = None,
    ):
        self.ant_chain_id = ant_chain_id
        self.creat_time = creat_time
        self.dt = dt
        self.last_sum_block_height = last_sum_block_height
        self.trans_count = trans_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ant_chain_id is not None:
            result['AntChainId'] = self.ant_chain_id
        if self.creat_time is not None:
            result['CreatTime'] = self.creat_time
        if self.dt is not None:
            result['Dt'] = self.dt
        if self.last_sum_block_height is not None:
            result['LastSumBlockHeight'] = self.last_sum_block_height
        if self.trans_count is not None:
            result['TransCount'] = self.trans_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AntChainId') is not None:
            self.ant_chain_id = m.get('AntChainId')
        if m.get('CreatTime') is not None:
            self.creat_time = m.get('CreatTime')
        if m.get('Dt') is not None:
            self.dt = m.get('Dt')
        if m.get('LastSumBlockHeight') is not None:
            self.last_sum_block_height = m.get('LastSumBlockHeight')
        if m.get('TransCount') is not None:
            self.trans_count = m.get('TransCount')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        status_code: int = None,
        body: DescribeAntChainTransactionStatisticsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeAntChainTransactionStatisticsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAntChainTransactionStatisticsV2Request(TeaModel):
    def __init__(
        self,
        ant_chain_id: str = None,
        consortium_id: str = None,
        end: int = None,
        start: int = None,
    ):
        # This parameter is required.
        self.ant_chain_id = ant_chain_id
        self.consortium_id = consortium_id
        self.end = end
        self.start = start

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ant_chain_id is not None:
            result['AntChainId'] = self.ant_chain_id
        if self.consortium_id is not None:
            result['ConsortiumId'] = self.consortium_id
        if self.end is not None:
            result['End'] = self.end
        if self.start is not None:
            result['Start'] = self.start
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AntChainId') is not None:
            self.ant_chain_id = m.get('AntChainId')
        if m.get('ConsortiumId') is not None:
            self.consortium_id = m.get('ConsortiumId')
        if m.get('End') is not None:
            self.end = m.get('End')
        if m.get('Start') is not None:
            self.start = m.get('Start')
        return self


class DescribeAntChainTransactionStatisticsV2ResponseBodyResult(TeaModel):
    def __init__(
        self,
        ant_chain_id: str = None,
        creat_time: int = None,
        dt: int = None,
        last_sum_block_height: int = None,
        trans_count: int = None,
    ):
        self.ant_chain_id = ant_chain_id
        self.creat_time = creat_time
        self.dt = dt
        self.last_sum_block_height = last_sum_block_height
        self.trans_count = trans_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ant_chain_id is not None:
            result['AntChainId'] = self.ant_chain_id
        if self.creat_time is not None:
            result['CreatTime'] = self.creat_time
        if self.dt is not None:
            result['Dt'] = self.dt
        if self.last_sum_block_height is not None:
            result['LastSumBlockHeight'] = self.last_sum_block_height
        if self.trans_count is not None:
            result['TransCount'] = self.trans_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AntChainId') is not None:
            self.ant_chain_id = m.get('AntChainId')
        if m.get('CreatTime') is not None:
            self.creat_time = m.get('CreatTime')
        if m.get('Dt') is not None:
            self.dt = m.get('Dt')
        if m.get('LastSumBlockHeight') is not None:
            self.last_sum_block_height = m.get('LastSumBlockHeight')
        if m.get('TransCount') is not None:
            self.trans_count = m.get('TransCount')
        return self


class DescribeAntChainTransactionStatisticsV2ResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: str = None,
        message: str = None,
        request_id: str = None,
        result: List[DescribeAntChainTransactionStatisticsV2ResponseBodyResult] = None,
        result_code: str = None,
        result_message: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.result = result
        self.result_code = result_code
        self.result_message = result_message
        self.success = success

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        if self.result_message is not None:
            result['ResultMessage'] = self.result_message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = DescribeAntChainTransactionStatisticsV2ResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeAntChainTransactionStatisticsV2Response(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAntChainTransactionStatisticsV2ResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeAntChainTransactionStatisticsV2ResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAntChainTransactionV2Request(TeaModel):
    def __init__(
        self,
        ant_chain_id: str = None,
        consortium_id: str = None,
        hash: str = None,
    ):
        # This parameter is required.
        self.ant_chain_id = ant_chain_id
        self.consortium_id = consortium_id
        # This parameter is required.
        self.hash = hash

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ant_chain_id is not None:
            result['AntChainId'] = self.ant_chain_id
        if self.consortium_id is not None:
            result['ConsortiumId'] = self.consortium_id
        if self.hash is not None:
            result['Hash'] = self.hash
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AntChainId') is not None:
            self.ant_chain_id = m.get('AntChainId')
        if m.get('ConsortiumId') is not None:
            self.consortium_id = m.get('ConsortiumId')
        if m.get('Hash') is not None:
            self.hash = m.get('Hash')
        return self


class DescribeAntChainTransactionV2ResponseBodyResultTransaction(TeaModel):
    def __init__(
        self,
        data: str = None,
        extentions: List[str] = None,
        from_: str = None,
        gas: str = None,
        hash: str = None,
        nonce: str = None,
        period: int = None,
        signatures: List[str] = None,
        timestamp: int = None,
        to: str = None,
        tx_type: str = None,
        value: str = None,
    ):
        self.data = data
        self.extentions = extentions
        self.from_ = from_
        self.gas = gas
        self.hash = hash
        self.nonce = nonce
        self.period = period
        self.signatures = signatures
        self.timestamp = timestamp
        self.to = to
        self.tx_type = tx_type
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.extentions is not None:
            result['Extentions'] = self.extentions
        if self.from_ is not None:
            result['From'] = self.from_
        if self.gas is not None:
            result['Gas'] = self.gas
        if self.hash is not None:
            result['Hash'] = self.hash
        if self.nonce is not None:
            result['Nonce'] = self.nonce
        if self.period is not None:
            result['Period'] = self.period
        if self.signatures is not None:
            result['Signatures'] = self.signatures
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.to is not None:
            result['To'] = self.to
        if self.tx_type is not None:
            result['TxType'] = self.tx_type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Extentions') is not None:
            self.extentions = m.get('Extentions')
        if m.get('From') is not None:
            self.from_ = m.get('From')
        if m.get('Gas') is not None:
            self.gas = m.get('Gas')
        if m.get('Hash') is not None:
            self.hash = m.get('Hash')
        if m.get('Nonce') is not None:
            self.nonce = m.get('Nonce')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('Signatures') is not None:
            self.signatures = m.get('Signatures')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('To') is not None:
            self.to = m.get('To')
        if m.get('TxType') is not None:
            self.tx_type = m.get('TxType')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeAntChainTransactionV2ResponseBodyResult(TeaModel):
    def __init__(
        self,
        block_hash: str = None,
        block_height: int = None,
        block_version: str = None,
        create_time: int = None,
        hash: str = None,
        transaction: DescribeAntChainTransactionV2ResponseBodyResultTransaction = None,
    ):
        self.block_hash = block_hash
        self.block_height = block_height
        self.block_version = block_version
        self.create_time = create_time
        self.hash = hash
        self.transaction = transaction

    def validate(self):
        if self.transaction:
            self.transaction.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.block_hash is not None:
            result['BlockHash'] = self.block_hash
        if self.block_height is not None:
            result['BlockHeight'] = self.block_height
        if self.block_version is not None:
            result['BlockVersion'] = self.block_version
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.hash is not None:
            result['Hash'] = self.hash
        if self.transaction is not None:
            result['Transaction'] = self.transaction.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BlockHash') is not None:
            self.block_hash = m.get('BlockHash')
        if m.get('BlockHeight') is not None:
            self.block_height = m.get('BlockHeight')
        if m.get('BlockVersion') is not None:
            self.block_version = m.get('BlockVersion')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Hash') is not None:
            self.hash = m.get('Hash')
        if m.get('Transaction') is not None:
            temp_model = DescribeAntChainTransactionV2ResponseBodyResultTransaction()
            self.transaction = temp_model.from_map(m['Transaction'])
        return self


class DescribeAntChainTransactionV2ResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: str = None,
        message: str = None,
        request_id: str = None,
        result: DescribeAntChainTransactionV2ResponseBodyResult = None,
        result_code: str = None,
        result_message: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.result = result
        self.result_code = result_code
        self.result_message = result_message
        self.success = success

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        if self.result_message is not None:
            result['ResultMessage'] = self.result_message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = DescribeAntChainTransactionV2ResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeAntChainTransactionV2Response(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAntChainTransactionV2ResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeAntChainTransactionV2ResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAntChainsRequest(TeaModel):
    def __init__(
        self,
        consortium_id: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # This parameter is required.
        self.consortium_id = consortium_id
        # This parameter is required.
        self.page_number = page_number
        # This parameter is required.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consortium_id is not None:
            result['ConsortiumId'] = self.consortium_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsortiumId') is not None:
            self.consortium_id = m.get('ConsortiumId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeAntChainsResponseBodyResultAntChains(TeaModel):
    def __init__(
        self,
        ant_chain_id: str = None,
        ant_chain_name: str = None,
        chain_type: str = None,
        cipher_suit: str = None,
        create_time: int = None,
        expire_time: int = None,
        is_admin: bool = None,
        member_status: str = None,
        merkle_tree_suit: str = None,
        network: str = None,
        node_num: int = None,
        region_id: str = None,
        resource_size: str = None,
        tls_algo: str = None,
        version: str = None,
    ):
        self.ant_chain_id = ant_chain_id
        self.ant_chain_name = ant_chain_name
        self.chain_type = chain_type
        self.cipher_suit = cipher_suit
        self.create_time = create_time
        self.expire_time = expire_time
        self.is_admin = is_admin
        self.member_status = member_status
        self.merkle_tree_suit = merkle_tree_suit
        self.network = network
        self.node_num = node_num
        self.region_id = region_id
        self.resource_size = resource_size
        self.tls_algo = tls_algo
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ant_chain_id is not None:
            result['AntChainId'] = self.ant_chain_id
        if self.ant_chain_name is not None:
            result['AntChainName'] = self.ant_chain_name
        if self.chain_type is not None:
            result['ChainType'] = self.chain_type
        if self.cipher_suit is not None:
            result['CipherSuit'] = self.cipher_suit
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.is_admin is not None:
            result['IsAdmin'] = self.is_admin
        if self.member_status is not None:
            result['MemberStatus'] = self.member_status
        if self.merkle_tree_suit is not None:
            result['MerkleTreeSuit'] = self.merkle_tree_suit
        if self.network is not None:
            result['Network'] = self.network
        if self.node_num is not None:
            result['NodeNum'] = self.node_num
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_size is not None:
            result['ResourceSize'] = self.resource_size
        if self.tls_algo is not None:
            result['TlsAlgo'] = self.tls_algo
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AntChainId') is not None:
            self.ant_chain_id = m.get('AntChainId')
        if m.get('AntChainName') is not None:
            self.ant_chain_name = m.get('AntChainName')
        if m.get('ChainType') is not None:
            self.chain_type = m.get('ChainType')
        if m.get('CipherSuit') is not None:
            self.cipher_suit = m.get('CipherSuit')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('IsAdmin') is not None:
            self.is_admin = m.get('IsAdmin')
        if m.get('MemberStatus') is not None:
            self.member_status = m.get('MemberStatus')
        if m.get('MerkleTreeSuit') is not None:
            self.merkle_tree_suit = m.get('MerkleTreeSuit')
        if m.get('Network') is not None:
            self.network = m.get('Network')
        if m.get('NodeNum') is not None:
            self.node_num = m.get('NodeNum')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceSize') is not None:
            self.resource_size = m.get('ResourceSize')
        if m.get('TlsAlgo') is not None:
            self.tls_algo = m.get('TlsAlgo')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class DescribeAntChainsResponseBodyResultPagination(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

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


class DescribeAntChainsResponseBodyResult(TeaModel):
    def __init__(
        self,
        ant_chains: List[DescribeAntChainsResponseBodyResultAntChains] = None,
        is_exist: bool = None,
        pagination: DescribeAntChainsResponseBodyResultPagination = None,
    ):
        self.ant_chains = ant_chains
        self.is_exist = is_exist
        self.pagination = pagination

    def validate(self):
        if self.ant_chains:
            for k in self.ant_chains:
                if k:
                    k.validate()
        if self.pagination:
            self.pagination.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AntChains'] = []
        if self.ant_chains is not None:
            for k in self.ant_chains:
                result['AntChains'].append(k.to_map() if k else None)
        if self.is_exist is not None:
            result['IsExist'] = self.is_exist
        if self.pagination is not None:
            result['Pagination'] = self.pagination.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ant_chains = []
        if m.get('AntChains') is not None:
            for k in m.get('AntChains'):
                temp_model = DescribeAntChainsResponseBodyResultAntChains()
                self.ant_chains.append(temp_model.from_map(k))
        if m.get('IsExist') is not None:
            self.is_exist = m.get('IsExist')
        if m.get('Pagination') is not None:
            temp_model = DescribeAntChainsResponseBodyResultPagination()
            self.pagination = temp_model.from_map(m['Pagination'])
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        status_code: int = None,
        body: DescribeAntChainsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeAntChainsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAntChainsV2Request(TeaModel):
    def __init__(
        self,
        consortium_id: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # This parameter is required.
        self.consortium_id = consortium_id
        self.page_number = page_number
        # This parameter is required.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consortium_id is not None:
            result['ConsortiumId'] = self.consortium_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsortiumId') is not None:
            self.consortium_id = m.get('ConsortiumId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeAntChainsV2ResponseBodyResultAntChains(TeaModel):
    def __init__(
        self,
        ant_chain_id: str = None,
        ant_chain_name: str = None,
        chain_type: str = None,
        cipher_suit: str = None,
        create_time: int = None,
        expire_time: int = None,
        instance_id: str = None,
        is_admin: bool = None,
        member_status: str = None,
        merkle_tree_suit: str = None,
        monitor_status: bool = None,
        network: str = None,
        node_num: int = None,
        region_id: str = None,
        resource_size: str = None,
        rest_status: str = None,
        tls_algo: str = None,
        version: str = None,
    ):
        self.ant_chain_id = ant_chain_id
        self.ant_chain_name = ant_chain_name
        self.chain_type = chain_type
        self.cipher_suit = cipher_suit
        self.create_time = create_time
        self.expire_time = expire_time
        self.instance_id = instance_id
        self.is_admin = is_admin
        self.member_status = member_status
        self.merkle_tree_suit = merkle_tree_suit
        self.monitor_status = monitor_status
        self.network = network
        self.node_num = node_num
        self.region_id = region_id
        self.resource_size = resource_size
        self.rest_status = rest_status
        self.tls_algo = tls_algo
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ant_chain_id is not None:
            result['AntChainId'] = self.ant_chain_id
        if self.ant_chain_name is not None:
            result['AntChainName'] = self.ant_chain_name
        if self.chain_type is not None:
            result['ChainType'] = self.chain_type
        if self.cipher_suit is not None:
            result['CipherSuit'] = self.cipher_suit
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.is_admin is not None:
            result['IsAdmin'] = self.is_admin
        if self.member_status is not None:
            result['MemberStatus'] = self.member_status
        if self.merkle_tree_suit is not None:
            result['MerkleTreeSuit'] = self.merkle_tree_suit
        if self.monitor_status is not None:
            result['MonitorStatus'] = self.monitor_status
        if self.network is not None:
            result['Network'] = self.network
        if self.node_num is not None:
            result['NodeNum'] = self.node_num
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_size is not None:
            result['ResourceSize'] = self.resource_size
        if self.rest_status is not None:
            result['RestStatus'] = self.rest_status
        if self.tls_algo is not None:
            result['TlsAlgo'] = self.tls_algo
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AntChainId') is not None:
            self.ant_chain_id = m.get('AntChainId')
        if m.get('AntChainName') is not None:
            self.ant_chain_name = m.get('AntChainName')
        if m.get('ChainType') is not None:
            self.chain_type = m.get('ChainType')
        if m.get('CipherSuit') is not None:
            self.cipher_suit = m.get('CipherSuit')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('IsAdmin') is not None:
            self.is_admin = m.get('IsAdmin')
        if m.get('MemberStatus') is not None:
            self.member_status = m.get('MemberStatus')
        if m.get('MerkleTreeSuit') is not None:
            self.merkle_tree_suit = m.get('MerkleTreeSuit')
        if m.get('MonitorStatus') is not None:
            self.monitor_status = m.get('MonitorStatus')
        if m.get('Network') is not None:
            self.network = m.get('Network')
        if m.get('NodeNum') is not None:
            self.node_num = m.get('NodeNum')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceSize') is not None:
            self.resource_size = m.get('ResourceSize')
        if m.get('RestStatus') is not None:
            self.rest_status = m.get('RestStatus')
        if m.get('TlsAlgo') is not None:
            self.tls_algo = m.get('TlsAlgo')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class DescribeAntChainsV2ResponseBodyResultPagination(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

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


class DescribeAntChainsV2ResponseBodyResult(TeaModel):
    def __init__(
        self,
        ant_chains: List[DescribeAntChainsV2ResponseBodyResultAntChains] = None,
        is_exist: bool = None,
        pagination: DescribeAntChainsV2ResponseBodyResultPagination = None,
    ):
        self.ant_chains = ant_chains
        self.is_exist = is_exist
        self.pagination = pagination

    def validate(self):
        if self.ant_chains:
            for k in self.ant_chains:
                if k:
                    k.validate()
        if self.pagination:
            self.pagination.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AntChains'] = []
        if self.ant_chains is not None:
            for k in self.ant_chains:
                result['AntChains'].append(k.to_map() if k else None)
        if self.is_exist is not None:
            result['IsExist'] = self.is_exist
        if self.pagination is not None:
            result['Pagination'] = self.pagination.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ant_chains = []
        if m.get('AntChains') is not None:
            for k in m.get('AntChains'):
                temp_model = DescribeAntChainsV2ResponseBodyResultAntChains()
                self.ant_chains.append(temp_model.from_map(k))
        if m.get('IsExist') is not None:
            self.is_exist = m.get('IsExist')
        if m.get('Pagination') is not None:
            temp_model = DescribeAntChainsV2ResponseBodyResultPagination()
            self.pagination = temp_model.from_map(m['Pagination'])
        return self


class DescribeAntChainsV2ResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: str = None,
        message: str = None,
        request_id: str = None,
        result: DescribeAntChainsV2ResponseBodyResult = None,
        result_code: str = None,
        result_message: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.result = result
        self.result_code = result_code
        self.result_message = result_message
        self.success = success

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        if self.result_message is not None:
            result['ResultMessage'] = self.result_message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = DescribeAntChainsV2ResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeAntChainsV2Response(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAntChainsV2ResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeAntChainsV2ResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeEthereumDeletableRequest(TeaModel):
    def __init__(
        self,
        ethereum_id: str = None,
    ):
        # This parameter is required.
        self.ethereum_id = ethereum_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        error_code: int = None,
        request_id: str = None,
        result: DescribeEthereumDeletableResponseBodyResult = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.request_id = request_id
        self.result = result
        self.success = success

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = DescribeEthereumDeletableResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeEthereumDeletableResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeEthereumDeletableResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        cluster_state: str = None,
        organization_id: str = None,
        organization_name: str = None,
        service_state: str = None,
    ):
        self.cluster_state = cluster_state
        self.organization_id = organization_id
        self.organization_name = organization_name
        self.service_state = service_state

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_state is not None:
            result['ClusterState'] = self.cluster_state
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.organization_name is not None:
            result['OrganizationName'] = self.organization_name
        if self.service_state is not None:
            result['ServiceState'] = self.service_state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterState') is not None:
            self.cluster_state = m.get('ClusterState')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('OrganizationName') is not None:
            self.organization_name = m.get('OrganizationName')
        if m.get('ServiceState') is not None:
            self.service_state = m.get('ServiceState')
        return self


class DescribeFabricCandidateOrganizationsResponseBody(TeaModel):
    def __init__(
        self,
        error_code: int = None,
        request_id: str = None,
        result: List[DescribeFabricCandidateOrganizationsResponseBodyResult] = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.request_id = request_id
        self.result = result
        self.success = success

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = DescribeFabricCandidateOrganizationsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeFabricCandidateOrganizationsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeFabricCandidateOrganizationsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeFabricCandidateOrganizationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFabricChaincodeDefinitionTaskRequest(TeaModel):
    def __init__(
        self,
        chaincode_id: str = None,
        organization_id: str = None,
    ):
        # This parameter is required.
        self.chaincode_id = chaincode_id
        # This parameter is required.
        self.organization_id = organization_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.chaincode_id is not None:
            result['ChaincodeId'] = self.chaincode_id
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChaincodeId') is not None:
            self.chaincode_id = m.get('ChaincodeId')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class DescribeFabricChaincodeDefinitionTaskResponseBodyResultContentChaincodeDefinition(TeaModel):
    def __init__(
        self,
        chaincode_package_id: str = None,
        collection_config: str = None,
        endorsement_policy: str = None,
        init_required: bool = None,
        name: str = None,
        sequence: int = None,
        uid: str = None,
        version: str = None,
    ):
        self.chaincode_package_id = chaincode_package_id
        self.collection_config = collection_config
        self.endorsement_policy = endorsement_policy
        self.init_required = init_required
        self.name = name
        self.sequence = sequence
        self.uid = uid
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.chaincode_package_id is not None:
            result['ChaincodePackageId'] = self.chaincode_package_id
        if self.collection_config is not None:
            result['CollectionConfig'] = self.collection_config
        if self.endorsement_policy is not None:
            result['EndorsementPolicy'] = self.endorsement_policy
        if self.init_required is not None:
            result['InitRequired'] = self.init_required
        if self.name is not None:
            result['Name'] = self.name
        if self.sequence is not None:
            result['Sequence'] = self.sequence
        if self.uid is not None:
            result['Uid'] = self.uid
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChaincodePackageId') is not None:
            self.chaincode_package_id = m.get('ChaincodePackageId')
        if m.get('CollectionConfig') is not None:
            self.collection_config = m.get('CollectionConfig')
        if m.get('EndorsementPolicy') is not None:
            self.endorsement_policy = m.get('EndorsementPolicy')
        if m.get('InitRequired') is not None:
            self.init_required = m.get('InitRequired')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Sequence') is not None:
            self.sequence = m.get('Sequence')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class DescribeFabricChaincodeDefinitionTaskResponseBodyResultContent(TeaModel):
    def __init__(
        self,
        chaincode_definition: DescribeFabricChaincodeDefinitionTaskResponseBodyResultContentChaincodeDefinition = None,
    ):
        self.chaincode_definition = chaincode_definition

    def validate(self):
        if self.chaincode_definition:
            self.chaincode_definition.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.chaincode_definition is not None:
            result['ChaincodeDefinition'] = self.chaincode_definition.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChaincodeDefinition') is not None:
            temp_model = DescribeFabricChaincodeDefinitionTaskResponseBodyResultContentChaincodeDefinition()
            self.chaincode_definition = temp_model.from_map(m['ChaincodeDefinition'])
        return self


class DescribeFabricChaincodeDefinitionTaskResponseBodyResult(TeaModel):
    def __init__(
        self,
        approvers: List[str] = None,
        channel_name: str = None,
        content: DescribeFabricChaincodeDefinitionTaskResponseBodyResultContent = None,
        create_time: int = None,
        creator: str = None,
        description: str = None,
        status: str = None,
        task_id: str = None,
        type: str = None,
    ):
        self.approvers = approvers
        self.channel_name = channel_name
        self.content = content
        self.create_time = create_time
        self.creator = creator
        self.description = description
        self.status = status
        self.task_id = task_id
        self.type = type

    def validate(self):
        if self.content:
            self.content.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.approvers is not None:
            result['Approvers'] = self.approvers
        if self.channel_name is not None:
            result['ChannelName'] = self.channel_name
        if self.content is not None:
            result['Content'] = self.content.to_map()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.creator is not None:
            result['Creator'] = self.creator
        if self.description is not None:
            result['Description'] = self.description
        if self.status is not None:
            result['Status'] = self.status
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Approvers') is not None:
            self.approvers = m.get('Approvers')
        if m.get('ChannelName') is not None:
            self.channel_name = m.get('ChannelName')
        if m.get('Content') is not None:
            temp_model = DescribeFabricChaincodeDefinitionTaskResponseBodyResultContent()
            self.content = temp_model.from_map(m['Content'])
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeFabricChaincodeDefinitionTaskResponseBody(TeaModel):
    def __init__(
        self,
        error_code: int = None,
        request_id: str = None,
        result: DescribeFabricChaincodeDefinitionTaskResponseBodyResult = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.request_id = request_id
        self.result = result
        self.success = success

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = DescribeFabricChaincodeDefinitionTaskResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeFabricChaincodeDefinitionTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeFabricChaincodeDefinitionTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeFabricChaincodeDefinitionTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFabricChaincodeUploadPolicyRequest(TeaModel):
    def __init__(
        self,
        organization_id: str = None,
    ):
        # This parameter is required.
        self.organization_id = organization_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        access_id: str = None,
        dir: str = None,
        expire: int = None,
        host: str = None,
        policy: str = None,
        signature: str = None,
    ):
        self.access_id = access_id
        self.dir = dir
        self.expire = expire
        self.host = host
        self.policy = policy
        self.signature = signature

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_id is not None:
            result['AccessId'] = self.access_id
        if self.dir is not None:
            result['Dir'] = self.dir
        if self.expire is not None:
            result['Expire'] = self.expire
        if self.host is not None:
            result['Host'] = self.host
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.signature is not None:
            result['Signature'] = self.signature
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessId') is not None:
            self.access_id = m.get('AccessId')
        if m.get('Dir') is not None:
            self.dir = m.get('Dir')
        if m.get('Expire') is not None:
            self.expire = m.get('Expire')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('Signature') is not None:
            self.signature = m.get('Signature')
        return self


class DescribeFabricChaincodeUploadPolicyResponseBody(TeaModel):
    def __init__(
        self,
        error_code: int = None,
        request_id: str = None,
        result: DescribeFabricChaincodeUploadPolicyResponseBodyResult = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.request_id = request_id
        self.result = result
        self.success = success

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = DescribeFabricChaincodeUploadPolicyResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeFabricChaincodeUploadPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeFabricChaincodeUploadPolicyResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeFabricChaincodeUploadPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFabricChannelMembersRequest(TeaModel):
    def __init__(
        self,
        channel_id: str = None,
    ):
        # This parameter is required.
        self.channel_id = channel_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        accept_time: str = None,
        channel_id: str = None,
        invite_time: str = None,
        organization_description: str = None,
        organization_domain: str = None,
        organization_id: str = None,
        organization_name: str = None,
        state: str = None,
        with_peer: bool = None,
    ):
        self.accept_time = accept_time
        self.channel_id = channel_id
        self.invite_time = invite_time
        self.organization_description = organization_description
        self.organization_domain = organization_domain
        self.organization_id = organization_id
        self.organization_name = organization_name
        self.state = state
        self.with_peer = with_peer

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_time is not None:
            result['AcceptTime'] = self.accept_time
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.invite_time is not None:
            result['InviteTime'] = self.invite_time
        if self.organization_description is not None:
            result['OrganizationDescription'] = self.organization_description
        if self.organization_domain is not None:
            result['OrganizationDomain'] = self.organization_domain
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.organization_name is not None:
            result['OrganizationName'] = self.organization_name
        if self.state is not None:
            result['State'] = self.state
        if self.with_peer is not None:
            result['WithPeer'] = self.with_peer
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptTime') is not None:
            self.accept_time = m.get('AcceptTime')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('InviteTime') is not None:
            self.invite_time = m.get('InviteTime')
        if m.get('OrganizationDescription') is not None:
            self.organization_description = m.get('OrganizationDescription')
        if m.get('OrganizationDomain') is not None:
            self.organization_domain = m.get('OrganizationDomain')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('OrganizationName') is not None:
            self.organization_name = m.get('OrganizationName')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('WithPeer') is not None:
            self.with_peer = m.get('WithPeer')
        return self


class DescribeFabricChannelMembersResponseBody(TeaModel):
    def __init__(
        self,
        error_code: int = None,
        request_id: str = None,
        result: List[DescribeFabricChannelMembersResponseBodyResult] = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.request_id = request_id
        self.result = result
        self.success = success

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = DescribeFabricChannelMembersResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeFabricChannelMembersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeFabricChannelMembersResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        consortium_administrator: bool = None,
        consortium_id: str = None,
    ):
        self.consortium_administrator = consortium_administrator
        self.consortium_id = consortium_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consortium_administrator is not None:
            result['ConsortiumAdministrator'] = self.consortium_administrator
        if self.consortium_id is not None:
            result['ConsortiumId'] = self.consortium_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsortiumAdministrator') is not None:
            self.consortium_administrator = m.get('ConsortiumAdministrator')
        if m.get('ConsortiumId') is not None:
            self.consortium_id = m.get('ConsortiumId')
        return self


class DescribeFabricConsortiumAdminStatusResponseBody(TeaModel):
    def __init__(
        self,
        error_code: int = None,
        request_id: str = None,
        result: List[DescribeFabricConsortiumAdminStatusResponseBodyResult] = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.request_id = request_id
        self.result = result
        self.success = success

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = DescribeFabricConsortiumAdminStatusResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeFabricConsortiumAdminStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeFabricConsortiumAdminStatusResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
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
        # This parameter is required.
        self.consortium_id = consortium_id
        self.location = location

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        chaincode_id: str = None,
        chaincode_name: str = None,
        chaincode_version: str = None,
        channel_id: str = None,
        channel_name: str = None,
        consortium_id: str = None,
        create_time: str = None,
        deploy_time: str = None,
        endorse_policy: str = None,
        input: str = None,
        install: bool = None,
        message: str = None,
        path: str = None,
        provider_id: str = None,
        provider_name: str = None,
        state: str = None,
        type: int = None,
    ):
        self.chaincode_id = chaincode_id
        self.chaincode_name = chaincode_name
        self.chaincode_version = chaincode_version
        self.channel_id = channel_id
        self.channel_name = channel_name
        self.consortium_id = consortium_id
        self.create_time = create_time
        self.deploy_time = deploy_time
        self.endorse_policy = endorse_policy
        self.input = input
        self.install = install
        self.message = message
        self.path = path
        self.provider_id = provider_id
        self.provider_name = provider_name
        self.state = state
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.chaincode_id is not None:
            result['ChaincodeId'] = self.chaincode_id
        if self.chaincode_name is not None:
            result['ChaincodeName'] = self.chaincode_name
        if self.chaincode_version is not None:
            result['ChaincodeVersion'] = self.chaincode_version
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.channel_name is not None:
            result['ChannelName'] = self.channel_name
        if self.consortium_id is not None:
            result['ConsortiumId'] = self.consortium_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.deploy_time is not None:
            result['DeployTime'] = self.deploy_time
        if self.endorse_policy is not None:
            result['EndorsePolicy'] = self.endorse_policy
        if self.input is not None:
            result['Input'] = self.input
        if self.install is not None:
            result['Install'] = self.install
        if self.message is not None:
            result['Message'] = self.message
        if self.path is not None:
            result['Path'] = self.path
        if self.provider_id is not None:
            result['ProviderId'] = self.provider_id
        if self.provider_name is not None:
            result['ProviderName'] = self.provider_name
        if self.state is not None:
            result['State'] = self.state
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChaincodeId') is not None:
            self.chaincode_id = m.get('ChaincodeId')
        if m.get('ChaincodeName') is not None:
            self.chaincode_name = m.get('ChaincodeName')
        if m.get('ChaincodeVersion') is not None:
            self.chaincode_version = m.get('ChaincodeVersion')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('ChannelName') is not None:
            self.channel_name = m.get('ChannelName')
        if m.get('ConsortiumId') is not None:
            self.consortium_id = m.get('ConsortiumId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DeployTime') is not None:
            self.deploy_time = m.get('DeployTime')
        if m.get('EndorsePolicy') is not None:
            self.endorse_policy = m.get('EndorsePolicy')
        if m.get('Input') is not None:
            self.input = m.get('Input')
        if m.get('Install') is not None:
            self.install = m.get('Install')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('ProviderId') is not None:
            self.provider_id = m.get('ProviderId')
        if m.get('ProviderName') is not None:
            self.provider_name = m.get('ProviderName')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeFabricConsortiumChaincodesResponseBody(TeaModel):
    def __init__(
        self,
        error_code: int = None,
        request_id: str = None,
        result: List[DescribeFabricConsortiumChaincodesResponseBodyResult] = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.request_id = request_id
        self.result = result
        self.success = success

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = DescribeFabricConsortiumChaincodesResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeFabricConsortiumChaincodesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeFabricConsortiumChaincodesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
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
        # This parameter is required.
        self.consortium_id = consortium_id
        self.location = location

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        block_count: int = None,
        chaincode_count: int = None,
        channel_id: str = None,
        channel_name: str = None,
        consortium_channel_id: int = None,
        consortium_id: str = None,
        consortium_name: str = None,
        create_time: str = None,
        delete_time: str = None,
        deleted: bool = None,
        max_message_count: int = None,
        member_count: int = None,
        member_joined_count: str = None,
        need_joined: bool = None,
        owner_bid: str = None,
        owner_name: str = None,
        owner_uid: int = None,
        preferred_max_bytes: int = None,
        request_id: str = None,
        state: str = None,
        support_channel_config: bool = None,
        update_time: str = None,
    ):
        self.batch_timeout = batch_timeout
        self.block_count = block_count
        self.chaincode_count = chaincode_count
        self.channel_id = channel_id
        self.channel_name = channel_name
        self.consortium_channel_id = consortium_channel_id
        self.consortium_id = consortium_id
        self.consortium_name = consortium_name
        self.create_time = create_time
        self.delete_time = delete_time
        self.deleted = deleted
        self.max_message_count = max_message_count
        self.member_count = member_count
        self.member_joined_count = member_joined_count
        self.need_joined = need_joined
        self.owner_bid = owner_bid
        self.owner_name = owner_name
        self.owner_uid = owner_uid
        self.preferred_max_bytes = preferred_max_bytes
        self.request_id = request_id
        self.state = state
        self.support_channel_config = support_channel_config
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.batch_timeout is not None:
            result['BatchTimeout'] = self.batch_timeout
        if self.block_count is not None:
            result['BlockCount'] = self.block_count
        if self.chaincode_count is not None:
            result['ChaincodeCount'] = self.chaincode_count
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.channel_name is not None:
            result['ChannelName'] = self.channel_name
        if self.consortium_channel_id is not None:
            result['ConsortiumChannelId'] = self.consortium_channel_id
        if self.consortium_id is not None:
            result['ConsortiumId'] = self.consortium_id
        if self.consortium_name is not None:
            result['ConsortiumName'] = self.consortium_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.delete_time is not None:
            result['DeleteTime'] = self.delete_time
        if self.deleted is not None:
            result['Deleted'] = self.deleted
        if self.max_message_count is not None:
            result['MaxMessageCount'] = self.max_message_count
        if self.member_count is not None:
            result['MemberCount'] = self.member_count
        if self.member_joined_count is not None:
            result['MemberJoinedCount'] = self.member_joined_count
        if self.need_joined is not None:
            result['NeedJoined'] = self.need_joined
        if self.owner_bid is not None:
            result['OwnerBid'] = self.owner_bid
        if self.owner_name is not None:
            result['OwnerName'] = self.owner_name
        if self.owner_uid is not None:
            result['OwnerUid'] = self.owner_uid
        if self.preferred_max_bytes is not None:
            result['PreferredMaxBytes'] = self.preferred_max_bytes
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.state is not None:
            result['State'] = self.state
        if self.support_channel_config is not None:
            result['SupportChannelConfig'] = self.support_channel_config
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BatchTimeout') is not None:
            self.batch_timeout = m.get('BatchTimeout')
        if m.get('BlockCount') is not None:
            self.block_count = m.get('BlockCount')
        if m.get('ChaincodeCount') is not None:
            self.chaincode_count = m.get('ChaincodeCount')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('ChannelName') is not None:
            self.channel_name = m.get('ChannelName')
        if m.get('ConsortiumChannelId') is not None:
            self.consortium_channel_id = m.get('ConsortiumChannelId')
        if m.get('ConsortiumId') is not None:
            self.consortium_id = m.get('ConsortiumId')
        if m.get('ConsortiumName') is not None:
            self.consortium_name = m.get('ConsortiumName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DeleteTime') is not None:
            self.delete_time = m.get('DeleteTime')
        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')
        if m.get('MaxMessageCount') is not None:
            self.max_message_count = m.get('MaxMessageCount')
        if m.get('MemberCount') is not None:
            self.member_count = m.get('MemberCount')
        if m.get('MemberJoinedCount') is not None:
            self.member_joined_count = m.get('MemberJoinedCount')
        if m.get('NeedJoined') is not None:
            self.need_joined = m.get('NeedJoined')
        if m.get('OwnerBid') is not None:
            self.owner_bid = m.get('OwnerBid')
        if m.get('OwnerName') is not None:
            self.owner_name = m.get('OwnerName')
        if m.get('OwnerUid') is not None:
            self.owner_uid = m.get('OwnerUid')
        if m.get('PreferredMaxBytes') is not None:
            self.preferred_max_bytes = m.get('PreferredMaxBytes')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('SupportChannelConfig') is not None:
            self.support_channel_config = m.get('SupportChannelConfig')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class DescribeFabricConsortiumChannelsResponseBody(TeaModel):
    def __init__(
        self,
        error_code: int = None,
        request_id: str = None,
        result: List[DescribeFabricConsortiumChannelsResponseBodyResult] = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.request_id = request_id
        self.result = result
        self.success = success

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = DescribeFabricConsortiumChannelsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeFabricConsortiumChannelsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeFabricConsortiumChannelsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        error_code: int = None,
        request_id: str = None,
        result: DescribeFabricConsortiumConfigResponseBodyResult = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.request_id = request_id
        self.result = result
        self.success = success

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = DescribeFabricConsortiumConfigResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeFabricConsortiumConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeFabricConsortiumConfigResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
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
        # This parameter is required.
        self.consortium_id = consortium_id
        self.location = location

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        code_name: str = None,
        consortium_id: str = None,
        consortium_name: str = None,
        deletable: bool = None,
        description: str = None,
        domain: str = None,
        region_id: str = None,
        state: str = None,
        zone_id: str = None,
    ):
        self.code_name = code_name
        self.consortium_id = consortium_id
        self.consortium_name = consortium_name
        self.deletable = deletable
        self.description = description
        self.domain = domain
        self.region_id = region_id
        self.state = state
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code_name is not None:
            result['CodeName'] = self.code_name
        if self.consortium_id is not None:
            result['ConsortiumId'] = self.consortium_id
        if self.consortium_name is not None:
            result['ConsortiumName'] = self.consortium_name
        if self.deletable is not None:
            result['Deletable'] = self.deletable
        if self.description is not None:
            result['Description'] = self.description
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.state is not None:
            result['State'] = self.state
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CodeName') is not None:
            self.code_name = m.get('CodeName')
        if m.get('ConsortiumId') is not None:
            self.consortium_id = m.get('ConsortiumId')
        if m.get('ConsortiumName') is not None:
            self.consortium_name = m.get('ConsortiumName')
        if m.get('Deletable') is not None:
            self.deletable = m.get('Deletable')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeFabricConsortiumDeletableResponseBody(TeaModel):
    def __init__(
        self,
        error_code: int = None,
        request_id: str = None,
        result: DescribeFabricConsortiumDeletableResponseBodyResult = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.request_id = request_id
        self.result = result
        self.success = success

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = DescribeFabricConsortiumDeletableResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeFabricConsortiumDeletableResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeFabricConsortiumDeletableResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
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
        # This parameter is required.
        self.consortium_id = consortium_id
        self.location = location

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        channel_create_policy: str = None,
        confirm_time: str = None,
        consortium_id: str = None,
        consortium_name: str = None,
        domain_name: str = None,
        organization_id: str = None,
        organization_name: str = None,
        state: str = None,
    ):
        self.channel_create_policy = channel_create_policy
        self.confirm_time = confirm_time
        self.consortium_id = consortium_id
        self.consortium_name = consortium_name
        self.domain_name = domain_name
        self.organization_id = organization_id
        self.organization_name = organization_name
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel_create_policy is not None:
            result['ChannelCreatePolicy'] = self.channel_create_policy
        if self.confirm_time is not None:
            result['ConfirmTime'] = self.confirm_time
        if self.consortium_id is not None:
            result['ConsortiumId'] = self.consortium_id
        if self.consortium_name is not None:
            result['ConsortiumName'] = self.consortium_name
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.organization_name is not None:
            result['OrganizationName'] = self.organization_name
        if self.state is not None:
            result['State'] = self.state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChannelCreatePolicy') is not None:
            self.channel_create_policy = m.get('ChannelCreatePolicy')
        if m.get('ConfirmTime') is not None:
            self.confirm_time = m.get('ConfirmTime')
        if m.get('ConsortiumId') is not None:
            self.consortium_id = m.get('ConsortiumId')
        if m.get('ConsortiumName') is not None:
            self.consortium_name = m.get('ConsortiumName')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('OrganizationName') is not None:
            self.organization_name = m.get('OrganizationName')
        if m.get('State') is not None:
            self.state = m.get('State')
        return self


class DescribeFabricConsortiumMemberApprovalResponseBody(TeaModel):
    def __init__(
        self,
        error_code: int = None,
        request_id: str = None,
        result: List[DescribeFabricConsortiumMemberApprovalResponseBodyResult] = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.request_id = request_id
        self.result = result
        self.success = success

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = DescribeFabricConsortiumMemberApprovalResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeFabricConsortiumMemberApprovalResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeFabricConsortiumMemberApprovalResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
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
        # This parameter is required.
        self.consortium_id = consortium_id
        self.location = location

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        consortium_id: str = None,
        description: str = None,
        domain: str = None,
        joined_time: str = None,
        organization_id: str = None,
        organization_name: str = None,
    ):
        self.consortium_id = consortium_id
        self.description = description
        self.domain = domain
        self.joined_time = joined_time
        self.organization_id = organization_id
        self.organization_name = organization_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consortium_id is not None:
            result['ConsortiumId'] = self.consortium_id
        if self.description is not None:
            result['Description'] = self.description
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.joined_time is not None:
            result['JoinedTime'] = self.joined_time
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.organization_name is not None:
            result['OrganizationName'] = self.organization_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsortiumId') is not None:
            self.consortium_id = m.get('ConsortiumId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('JoinedTime') is not None:
            self.joined_time = m.get('JoinedTime')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('OrganizationName') is not None:
            self.organization_name = m.get('OrganizationName')
        return self


class DescribeFabricConsortiumMembersResponseBody(TeaModel):
    def __init__(
        self,
        error_code: int = None,
        request_id: str = None,
        result: List[DescribeFabricConsortiumMembersResponseBodyResult] = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.request_id = request_id
        self.result = result
        self.success = success

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = DescribeFabricConsortiumMembersResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeFabricConsortiumMembersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeFabricConsortiumMembersResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
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
        # This parameter is required.
        self.consortium_id = consortium_id
        self.location = location

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        create_time: str = None,
        domain: str = None,
        instance_type: str = None,
        orderer_name: str = None,
        port: int = None,
        update_time: str = None,
    ):
        self.create_time = create_time
        self.domain = domain
        self.instance_type = instance_type
        self.orderer_name = orderer_name
        self.port = port
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.orderer_name is not None:
            result['OrdererName'] = self.orderer_name
        if self.port is not None:
            result['Port'] = self.port
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('OrdererName') is not None:
            self.orderer_name = m.get('OrdererName')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class DescribeFabricConsortiumOrderersResponseBody(TeaModel):
    def __init__(
        self,
        error_code: int = None,
        request_id: str = None,
        result: List[DescribeFabricConsortiumOrderersResponseBodyResult] = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.request_id = request_id
        self.result = result
        self.success = success

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = DescribeFabricConsortiumOrderersResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeFabricConsortiumOrderersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeFabricConsortiumOrderersResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeFabricConsortiumOrderersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFabricConsortiumSpecsResponseBodyResult(TeaModel):
    def __init__(
        self,
        enable: bool = None,
        spec_name: str = None,
        spec_title: str = None,
    ):
        self.enable = enable
        self.spec_name = spec_name
        self.spec_title = spec_title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.spec_name is not None:
            result['SpecName'] = self.spec_name
        if self.spec_title is not None:
            result['SpecTitle'] = self.spec_title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('SpecName') is not None:
            self.spec_name = m.get('SpecName')
        if m.get('SpecTitle') is not None:
            self.spec_title = m.get('SpecTitle')
        return self


class DescribeFabricConsortiumSpecsResponseBody(TeaModel):
    def __init__(
        self,
        error_code: int = None,
        request_id: str = None,
        result: List[DescribeFabricConsortiumSpecsResponseBodyResult] = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.request_id = request_id
        self.result = result
        self.success = success

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = DescribeFabricConsortiumSpecsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeFabricConsortiumSpecsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeFabricConsortiumSpecsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeFabricConsortiumSpecsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFabricConsortiumsRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # This parameter is required.
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        channel_policy: str = None,
        code_name: str = None,
        consortium_id: str = None,
        consortium_name: str = None,
        create_time: str = None,
        domain: str = None,
        expired_time: str = None,
        major_version: str = None,
        organization_count: int = None,
        owner_bid: str = None,
        owner_name: str = None,
        owner_uid: int = None,
        region_id: str = None,
        request_id: str = None,
        spec_name: str = None,
        state: str = None,
        support_channel_config: bool = None,
        tags: List[DescribeFabricConsortiumsResponseBodyResultTags] = None,
    ):
        self.channel_count = channel_count
        self.channel_policy = channel_policy
        self.code_name = code_name
        self.consortium_id = consortium_id
        self.consortium_name = consortium_name
        self.create_time = create_time
        self.domain = domain
        self.expired_time = expired_time
        self.major_version = major_version
        self.organization_count = organization_count
        self.owner_bid = owner_bid
        self.owner_name = owner_name
        self.owner_uid = owner_uid
        self.region_id = region_id
        self.request_id = request_id
        self.spec_name = spec_name
        self.state = state
        self.support_channel_config = support_channel_config
        self.tags = tags

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel_count is not None:
            result['ChannelCount'] = self.channel_count
        if self.channel_policy is not None:
            result['ChannelPolicy'] = self.channel_policy
        if self.code_name is not None:
            result['CodeName'] = self.code_name
        if self.consortium_id is not None:
            result['ConsortiumId'] = self.consortium_id
        if self.consortium_name is not None:
            result['ConsortiumName'] = self.consortium_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.major_version is not None:
            result['MajorVersion'] = self.major_version
        if self.organization_count is not None:
            result['OrganizationCount'] = self.organization_count
        if self.owner_bid is not None:
            result['OwnerBid'] = self.owner_bid
        if self.owner_name is not None:
            result['OwnerName'] = self.owner_name
        if self.owner_uid is not None:
            result['OwnerUid'] = self.owner_uid
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.spec_name is not None:
            result['SpecName'] = self.spec_name
        if self.state is not None:
            result['State'] = self.state
        if self.support_channel_config is not None:
            result['SupportChannelConfig'] = self.support_channel_config
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChannelCount') is not None:
            self.channel_count = m.get('ChannelCount')
        if m.get('ChannelPolicy') is not None:
            self.channel_policy = m.get('ChannelPolicy')
        if m.get('CodeName') is not None:
            self.code_name = m.get('CodeName')
        if m.get('ConsortiumId') is not None:
            self.consortium_id = m.get('ConsortiumId')
        if m.get('ConsortiumName') is not None:
            self.consortium_name = m.get('ConsortiumName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('MajorVersion') is not None:
            self.major_version = m.get('MajorVersion')
        if m.get('OrganizationCount') is not None:
            self.organization_count = m.get('OrganizationCount')
        if m.get('OwnerBid') is not None:
            self.owner_bid = m.get('OwnerBid')
        if m.get('OwnerName') is not None:
            self.owner_name = m.get('OwnerName')
        if m.get('OwnerUid') is not None:
            self.owner_uid = m.get('OwnerUid')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SpecName') is not None:
            self.spec_name = m.get('SpecName')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('SupportChannelConfig') is not None:
            self.support_channel_config = m.get('SupportChannelConfig')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = DescribeFabricConsortiumsResponseBodyResultTags()
                self.tags.append(temp_model.from_map(k))
        return self


class DescribeFabricConsortiumsResponseBody(TeaModel):
    def __init__(
        self,
        error_code: int = None,
        request_id: str = None,
        result: List[DescribeFabricConsortiumsResponseBodyResult] = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.request_id = request_id
        self.result = result
        self.success = success

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = DescribeFabricConsortiumsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeFabricConsortiumsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeFabricConsortiumsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeFabricConsortiumsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFabricExplorerRequest(TeaModel):
    def __init__(
        self,
        ex_body: str = None,
        ex_method: str = None,
        ex_url: str = None,
        organization_id: str = None,
    ):
        self.ex_body = ex_body
        # This parameter is required.
        self.ex_method = ex_method
        # This parameter is required.
        self.ex_url = ex_url
        # This parameter is required.
        self.organization_id = organization_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ex_body is not None:
            result['ExBody'] = self.ex_body
        if self.ex_method is not None:
            result['ExMethod'] = self.ex_method
        if self.ex_url is not None:
            result['ExUrl'] = self.ex_url
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExBody') is not None:
            self.ex_body = m.get('ExBody')
        if m.get('ExMethod') is not None:
            self.ex_method = m.get('ExMethod')
        if m.get('ExUrl') is not None:
            self.ex_url = m.get('ExUrl')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class DescribeFabricExplorerResponseBody(TeaModel):
    def __init__(
        self,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_code: int = None,
        request_id: str = None,
        result: str = None,
        success: bool = None,
    ):
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.error_code = error_code
        self.request_id = request_id
        self.result = result
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeFabricExplorerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeFabricExplorerResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeFabricExplorerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFabricInvitationCodeRequest(TeaModel):
    def __init__(
        self,
        consortium_id: str = None,
    ):
        # This parameter is required.
        self.consortium_id = consortium_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        accepted: bool = None,
        code: str = None,
        consortium_id: str = None,
        email: str = None,
        expire_time: str = None,
        invitation_id: int = None,
        send_time: str = None,
        sender_bid: str = None,
        sender_id: int = None,
        sender_name: str = None,
        url: str = None,
    ):
        self.accepted = accepted
        self.code = code
        self.consortium_id = consortium_id
        self.email = email
        self.expire_time = expire_time
        self.invitation_id = invitation_id
        self.send_time = send_time
        self.sender_bid = sender_bid
        self.sender_id = sender_id
        self.sender_name = sender_name
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accepted is not None:
            result['Accepted'] = self.accepted
        if self.code is not None:
            result['Code'] = self.code
        if self.consortium_id is not None:
            result['ConsortiumId'] = self.consortium_id
        if self.email is not None:
            result['Email'] = self.email
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.invitation_id is not None:
            result['InvitationId'] = self.invitation_id
        if self.send_time is not None:
            result['SendTime'] = self.send_time
        if self.sender_bid is not None:
            result['SenderBid'] = self.sender_bid
        if self.sender_id is not None:
            result['SenderId'] = self.sender_id
        if self.sender_name is not None:
            result['SenderName'] = self.sender_name
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accepted') is not None:
            self.accepted = m.get('Accepted')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ConsortiumId') is not None:
            self.consortium_id = m.get('ConsortiumId')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('InvitationId') is not None:
            self.invitation_id = m.get('InvitationId')
        if m.get('SendTime') is not None:
            self.send_time = m.get('SendTime')
        if m.get('SenderBid') is not None:
            self.sender_bid = m.get('SenderBid')
        if m.get('SenderId') is not None:
            self.sender_id = m.get('SenderId')
        if m.get('SenderName') is not None:
            self.sender_name = m.get('SenderName')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class DescribeFabricInvitationCodeResponseBody(TeaModel):
    def __init__(
        self,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_code: int = None,
        request_id: str = None,
        result: DescribeFabricInvitationCodeResponseBodyResult = None,
        success: bool = None,
    ):
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.error_code = error_code
        self.request_id = request_id
        self.result = result
        self.success = success

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = DescribeFabricInvitationCodeResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeFabricInvitationCodeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeFabricInvitationCodeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeFabricInvitationCodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFabricInviterRequest(TeaModel):
    def __init__(
        self,
        code: str = None,
    ):
        # This parameter is required.
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        consortium_id: str = None,
        consortium_name: str = None,
        expire_time: str = None,
        inviter_id: int = None,
        inviter_name: str = None,
    ):
        self.consortium_id = consortium_id
        self.consortium_name = consortium_name
        self.expire_time = expire_time
        self.inviter_id = inviter_id
        self.inviter_name = inviter_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consortium_id is not None:
            result['ConsortiumId'] = self.consortium_id
        if self.consortium_name is not None:
            result['ConsortiumName'] = self.consortium_name
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.inviter_id is not None:
            result['InviterId'] = self.inviter_id
        if self.inviter_name is not None:
            result['InviterName'] = self.inviter_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsortiumId') is not None:
            self.consortium_id = m.get('ConsortiumId')
        if m.get('ConsortiumName') is not None:
            self.consortium_name = m.get('ConsortiumName')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('InviterId') is not None:
            self.inviter_id = m.get('InviterId')
        if m.get('InviterName') is not None:
            self.inviter_name = m.get('InviterName')
        return self


class DescribeFabricInviterResponseBody(TeaModel):
    def __init__(
        self,
        error_code: int = None,
        request_id: str = None,
        result: DescribeFabricInviterResponseBodyResult = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.request_id = request_id
        self.result = result
        self.success = success

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = DescribeFabricInviterResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeFabricInviterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeFabricInviterResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeFabricInviterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFabricOrdererLogsRequest(TeaModel):
    def __init__(
        self,
        consortium_id: str = None,
        lines: str = None,
        orderer_name: str = None,
    ):
        # This parameter is required.
        self.consortium_id = consortium_id
        self.lines = lines
        # This parameter is required.
        self.orderer_name = orderer_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consortium_id is not None:
            result['ConsortiumId'] = self.consortium_id
        if self.lines is not None:
            result['Lines'] = self.lines
        if self.orderer_name is not None:
            result['OrdererName'] = self.orderer_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsortiumId') is not None:
            self.consortium_id = m.get('ConsortiumId')
        if m.get('Lines') is not None:
            self.lines = m.get('Lines')
        if m.get('OrdererName') is not None:
            self.orderer_name = m.get('OrdererName')
        return self


class DescribeFabricOrdererLogsResponseBody(TeaModel):
    def __init__(
        self,
        error_code: int = None,
        request_id: str = None,
        result: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.request_id = request_id
        self.result = result
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeFabricOrdererLogsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeFabricOrdererLogsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
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
        # This parameter is required.
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        location: str = None,
        organization_id: str = None,
        tag: List[DescribeFabricOrganizationRequestTag] = None,
    ):
        self.location = location
        # This parameter is required.
        self.organization_id = organization_id
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.location is not None:
            result['Location'] = self.location
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        caname: str = None,
        caurl: str = None,
        code_name: str = None,
        consortium_count: int = None,
        create_time: str = None,
        domain: str = None,
        msp: str = None,
        organization_description: str = None,
        organization_id: str = None,
        organization_name: str = None,
        owner_bid: str = None,
        owner_name: str = None,
        owner_uid: int = None,
        peer_count: int = None,
        region_id: str = None,
        request_id: str = None,
        spec_name: str = None,
        state: str = None,
        tags: List[DescribeFabricOrganizationResponseBodyResultTags] = None,
        user_count: int = None,
        zone_id: str = None,
    ):
        self.caname = caname
        self.caurl = caurl
        self.code_name = code_name
        self.consortium_count = consortium_count
        self.create_time = create_time
        self.domain = domain
        self.msp = msp
        self.organization_description = organization_description
        self.organization_id = organization_id
        self.organization_name = organization_name
        self.owner_bid = owner_bid
        self.owner_name = owner_name
        self.owner_uid = owner_uid
        self.peer_count = peer_count
        self.region_id = region_id
        self.request_id = request_id
        self.spec_name = spec_name
        self.state = state
        self.tags = tags
        self.user_count = user_count
        self.zone_id = zone_id

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.caname is not None:
            result['CANAME'] = self.caname
        if self.caurl is not None:
            result['CAUrl'] = self.caurl
        if self.code_name is not None:
            result['CodeName'] = self.code_name
        if self.consortium_count is not None:
            result['ConsortiumCount'] = self.consortium_count
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.msp is not None:
            result['MSP'] = self.msp
        if self.organization_description is not None:
            result['OrganizationDescription'] = self.organization_description
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.organization_name is not None:
            result['OrganizationName'] = self.organization_name
        if self.owner_bid is not None:
            result['OwnerBid'] = self.owner_bid
        if self.owner_name is not None:
            result['OwnerName'] = self.owner_name
        if self.owner_uid is not None:
            result['OwnerUid'] = self.owner_uid
        if self.peer_count is not None:
            result['PeerCount'] = self.peer_count
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.spec_name is not None:
            result['SpecName'] = self.spec_name
        if self.state is not None:
            result['State'] = self.state
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.user_count is not None:
            result['UserCount'] = self.user_count
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CANAME') is not None:
            self.caname = m.get('CANAME')
        if m.get('CAUrl') is not None:
            self.caurl = m.get('CAUrl')
        if m.get('CodeName') is not None:
            self.code_name = m.get('CodeName')
        if m.get('ConsortiumCount') is not None:
            self.consortium_count = m.get('ConsortiumCount')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('MSP') is not None:
            self.msp = m.get('MSP')
        if m.get('OrganizationDescription') is not None:
            self.organization_description = m.get('OrganizationDescription')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('OrganizationName') is not None:
            self.organization_name = m.get('OrganizationName')
        if m.get('OwnerBid') is not None:
            self.owner_bid = m.get('OwnerBid')
        if m.get('OwnerName') is not None:
            self.owner_name = m.get('OwnerName')
        if m.get('OwnerUid') is not None:
            self.owner_uid = m.get('OwnerUid')
        if m.get('PeerCount') is not None:
            self.peer_count = m.get('PeerCount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SpecName') is not None:
            self.spec_name = m.get('SpecName')
        if m.get('State') is not None:
            self.state = m.get('State')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = DescribeFabricOrganizationResponseBodyResultTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('UserCount') is not None:
            self.user_count = m.get('UserCount')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeFabricOrganizationResponseBody(TeaModel):
    def __init__(
        self,
        error_code: int = None,
        request_id: str = None,
        result: DescribeFabricOrganizationResponseBodyResult = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.request_id = request_id
        self.result = result
        self.success = success

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = DescribeFabricOrganizationResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeFabricOrganizationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeFabricOrganizationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeFabricOrganizationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFabricOrganizationChaincodePackageRequest(TeaModel):
    def __init__(
        self,
        organization_id: str = None,
    ):
        # This parameter is required.
        self.organization_id = organization_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class DescribeFabricOrganizationChaincodePackageResponseBody(TeaModel):
    def __init__(
        self,
        error_code: int = None,
        message: str = None,
        request_id: str = None,
        result: List[ChaincodePackage] = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.result = result
        self.success = success

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ChaincodePackage()
                self.result.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeFabricOrganizationChaincodePackageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeFabricOrganizationChaincodePackageResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeFabricOrganizationChaincodePackageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFabricOrganizationChaincodesRequest(TeaModel):
    def __init__(
        self,
        location: str = None,
        organization_id: str = None,
    ):
        self.location = location
        # This parameter is required.
        self.organization_id = organization_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.location is not None:
            result['Location'] = self.location
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class DescribeFabricOrganizationChaincodesResponseBodyResult(TeaModel):
    def __init__(
        self,
        chaincode_id: str = None,
        chaincode_name: str = None,
        chaincode_version: str = None,
        channel_id: str = None,
        channel_name: str = None,
        consortium_id: str = None,
        create_time: str = None,
        creator: str = None,
        deploy_time: str = None,
        endorse_policy: str = None,
        installed: str = None,
        message: str = None,
        state: str = None,
    ):
        self.chaincode_id = chaincode_id
        self.chaincode_name = chaincode_name
        self.chaincode_version = chaincode_version
        self.channel_id = channel_id
        self.channel_name = channel_name
        self.consortium_id = consortium_id
        self.create_time = create_time
        self.creator = creator
        self.deploy_time = deploy_time
        self.endorse_policy = endorse_policy
        self.installed = installed
        self.message = message
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.chaincode_id is not None:
            result['ChaincodeId'] = self.chaincode_id
        if self.chaincode_name is not None:
            result['ChaincodeName'] = self.chaincode_name
        if self.chaincode_version is not None:
            result['ChaincodeVersion'] = self.chaincode_version
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.channel_name is not None:
            result['ChannelName'] = self.channel_name
        if self.consortium_id is not None:
            result['ConsortiumId'] = self.consortium_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.creator is not None:
            result['Creator'] = self.creator
        if self.deploy_time is not None:
            result['DeployTime'] = self.deploy_time
        if self.endorse_policy is not None:
            result['EndorsePolicy'] = self.endorse_policy
        if self.installed is not None:
            result['Installed'] = self.installed
        if self.message is not None:
            result['Message'] = self.message
        if self.state is not None:
            result['State'] = self.state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChaincodeId') is not None:
            self.chaincode_id = m.get('ChaincodeId')
        if m.get('ChaincodeName') is not None:
            self.chaincode_name = m.get('ChaincodeName')
        if m.get('ChaincodeVersion') is not None:
            self.chaincode_version = m.get('ChaincodeVersion')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('ChannelName') is not None:
            self.channel_name = m.get('ChannelName')
        if m.get('ConsortiumId') is not None:
            self.consortium_id = m.get('ConsortiumId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')
        if m.get('DeployTime') is not None:
            self.deploy_time = m.get('DeployTime')
        if m.get('EndorsePolicy') is not None:
            self.endorse_policy = m.get('EndorsePolicy')
        if m.get('Installed') is not None:
            self.installed = m.get('Installed')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('State') is not None:
            self.state = m.get('State')
        return self


class DescribeFabricOrganizationChaincodesResponseBody(TeaModel):
    def __init__(
        self,
        error_code: int = None,
        request_id: str = None,
        result: List[DescribeFabricOrganizationChaincodesResponseBodyResult] = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.request_id = request_id
        self.result = result
        self.success = success

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = DescribeFabricOrganizationChaincodesResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeFabricOrganizationChaincodesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeFabricOrganizationChaincodesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeFabricOrganizationChaincodesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFabricOrganizationChannelsRequest(TeaModel):
    def __init__(
        self,
        location: str = None,
        organization_id: str = None,
    ):
        self.location = location
        # This parameter is required.
        self.organization_id = organization_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.location is not None:
            result['Location'] = self.location
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class DescribeFabricOrganizationChannelsResponseBodyResult(TeaModel):
    def __init__(
        self,
        batch_timeout: int = None,
        block_count: int = None,
        chaincode_count: int = None,
        channel_id: str = None,
        channel_name: str = None,
        consortium_id: str = None,
        consortium_name: str = None,
        create_time: str = None,
        delete_time: str = None,
        deleted: bool = None,
        max_message_count: int = None,
        member_count: int = None,
        owner_bid: str = None,
        owner_name: str = None,
        owner_uid: int = None,
        preferred_max_bytes: int = None,
        request_id: str = None,
        state: str = None,
        support_channel_config: bool = None,
        update_time: str = None,
    ):
        self.batch_timeout = batch_timeout
        self.block_count = block_count
        self.chaincode_count = chaincode_count
        self.channel_id = channel_id
        self.channel_name = channel_name
        self.consortium_id = consortium_id
        self.consortium_name = consortium_name
        self.create_time = create_time
        self.delete_time = delete_time
        self.deleted = deleted
        self.max_message_count = max_message_count
        self.member_count = member_count
        self.owner_bid = owner_bid
        self.owner_name = owner_name
        self.owner_uid = owner_uid
        self.preferred_max_bytes = preferred_max_bytes
        self.request_id = request_id
        self.state = state
        self.support_channel_config = support_channel_config
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.batch_timeout is not None:
            result['BatchTimeout'] = self.batch_timeout
        if self.block_count is not None:
            result['BlockCount'] = self.block_count
        if self.chaincode_count is not None:
            result['ChaincodeCount'] = self.chaincode_count
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.channel_name is not None:
            result['ChannelName'] = self.channel_name
        if self.consortium_id is not None:
            result['ConsortiumId'] = self.consortium_id
        if self.consortium_name is not None:
            result['ConsortiumName'] = self.consortium_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.delete_time is not None:
            result['DeleteTime'] = self.delete_time
        if self.deleted is not None:
            result['Deleted'] = self.deleted
        if self.max_message_count is not None:
            result['MaxMessageCount'] = self.max_message_count
        if self.member_count is not None:
            result['MemberCount'] = self.member_count
        if self.owner_bid is not None:
            result['OwnerBid'] = self.owner_bid
        if self.owner_name is not None:
            result['OwnerName'] = self.owner_name
        if self.owner_uid is not None:
            result['OwnerUid'] = self.owner_uid
        if self.preferred_max_bytes is not None:
            result['PreferredMaxBytes'] = self.preferred_max_bytes
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.state is not None:
            result['State'] = self.state
        if self.support_channel_config is not None:
            result['SupportChannelConfig'] = self.support_channel_config
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BatchTimeout') is not None:
            self.batch_timeout = m.get('BatchTimeout')
        if m.get('BlockCount') is not None:
            self.block_count = m.get('BlockCount')
        if m.get('ChaincodeCount') is not None:
            self.chaincode_count = m.get('ChaincodeCount')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('ChannelName') is not None:
            self.channel_name = m.get('ChannelName')
        if m.get('ConsortiumId') is not None:
            self.consortium_id = m.get('ConsortiumId')
        if m.get('ConsortiumName') is not None:
            self.consortium_name = m.get('ConsortiumName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DeleteTime') is not None:
            self.delete_time = m.get('DeleteTime')
        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')
        if m.get('MaxMessageCount') is not None:
            self.max_message_count = m.get('MaxMessageCount')
        if m.get('MemberCount') is not None:
            self.member_count = m.get('MemberCount')
        if m.get('OwnerBid') is not None:
            self.owner_bid = m.get('OwnerBid')
        if m.get('OwnerName') is not None:
            self.owner_name = m.get('OwnerName')
        if m.get('OwnerUid') is not None:
            self.owner_uid = m.get('OwnerUid')
        if m.get('PreferredMaxBytes') is not None:
            self.preferred_max_bytes = m.get('PreferredMaxBytes')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('SupportChannelConfig') is not None:
            self.support_channel_config = m.get('SupportChannelConfig')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class DescribeFabricOrganizationChannelsResponseBody(TeaModel):
    def __init__(
        self,
        error_code: int = None,
        request_id: str = None,
        result: List[DescribeFabricOrganizationChannelsResponseBodyResult] = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.request_id = request_id
        self.result = result
        self.success = success

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = DescribeFabricOrganizationChannelsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeFabricOrganizationChannelsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeFabricOrganizationChannelsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeFabricOrganizationChannelsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFabricOrganizationDeletableRequest(TeaModel):
    def __init__(
        self,
        location: str = None,
        organization_id: str = None,
    ):
        self.location = location
        # This parameter is required.
        self.organization_id = organization_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.location is not None:
            result['Location'] = self.location
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class DescribeFabricOrganizationDeletableResponseBodyResult(TeaModel):
    def __init__(
        self,
        code_name: str = None,
        deletable: bool = None,
        domain: str = None,
        organization_description: str = None,
        organization_id: str = None,
        organization_name: str = None,
        region_id: str = None,
        state: str = None,
        zone_id: str = None,
    ):
        self.code_name = code_name
        self.deletable = deletable
        self.domain = domain
        self.organization_description = organization_description
        self.organization_id = organization_id
        self.organization_name = organization_name
        self.region_id = region_id
        self.state = state
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code_name is not None:
            result['CodeName'] = self.code_name
        if self.deletable is not None:
            result['Deletable'] = self.deletable
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.organization_description is not None:
            result['OrganizationDescription'] = self.organization_description
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.organization_name is not None:
            result['OrganizationName'] = self.organization_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.state is not None:
            result['State'] = self.state
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CodeName') is not None:
            self.code_name = m.get('CodeName')
        if m.get('Deletable') is not None:
            self.deletable = m.get('Deletable')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('OrganizationDescription') is not None:
            self.organization_description = m.get('OrganizationDescription')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('OrganizationName') is not None:
            self.organization_name = m.get('OrganizationName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeFabricOrganizationDeletableResponseBody(TeaModel):
    def __init__(
        self,
        error_code: int = None,
        request_id: str = None,
        result: DescribeFabricOrganizationDeletableResponseBodyResult = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.request_id = request_id
        self.result = result
        self.success = success

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = DescribeFabricOrganizationDeletableResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeFabricOrganizationDeletableResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeFabricOrganizationDeletableResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeFabricOrganizationDeletableResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFabricOrganizationMembersRequest(TeaModel):
    def __init__(
        self,
        location: str = None,
        organization_id: str = None,
    ):
        self.location = location
        # This parameter is required.
        self.organization_id = organization_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.location is not None:
            result['Location'] = self.location
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class DescribeFabricOrganizationMembersResponseBodyResult(TeaModel):
    def __init__(
        self,
        consortium_id: str = None,
        consortium_name: str = None,
        description: str = None,
        domain: str = None,
        joined_time: str = None,
        organization_id: str = None,
        organization_name: str = None,
        state: str = None,
    ):
        self.consortium_id = consortium_id
        self.consortium_name = consortium_name
        self.description = description
        self.domain = domain
        self.joined_time = joined_time
        self.organization_id = organization_id
        self.organization_name = organization_name
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consortium_id is not None:
            result['ConsortiumId'] = self.consortium_id
        if self.consortium_name is not None:
            result['ConsortiumName'] = self.consortium_name
        if self.description is not None:
            result['Description'] = self.description
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.joined_time is not None:
            result['JoinedTime'] = self.joined_time
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.organization_name is not None:
            result['OrganizationName'] = self.organization_name
        if self.state is not None:
            result['State'] = self.state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsortiumId') is not None:
            self.consortium_id = m.get('ConsortiumId')
        if m.get('ConsortiumName') is not None:
            self.consortium_name = m.get('ConsortiumName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('JoinedTime') is not None:
            self.joined_time = m.get('JoinedTime')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('OrganizationName') is not None:
            self.organization_name = m.get('OrganizationName')
        if m.get('State') is not None:
            self.state = m.get('State')
        return self


class DescribeFabricOrganizationMembersResponseBody(TeaModel):
    def __init__(
        self,
        error_code: int = None,
        request_id: str = None,
        result: List[DescribeFabricOrganizationMembersResponseBodyResult] = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.request_id = request_id
        self.result = result
        self.success = success

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = DescribeFabricOrganizationMembersResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeFabricOrganizationMembersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeFabricOrganizationMembersResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeFabricOrganizationMembersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFabricOrganizationPeersRequest(TeaModel):
    def __init__(
        self,
        location: str = None,
        organization_id: str = None,
    ):
        self.location = location
        # This parameter is required.
        self.organization_id = organization_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.location is not None:
            result['Location'] = self.location
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class DescribeFabricOrganizationPeersResponseBodyResult(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        domain: str = None,
        instance_type: str = None,
        internet_ip: str = None,
        intranet_ip: str = None,
        is_anchor: bool = None,
        organization_peer_name: str = None,
        port: int = None,
        update_time: str = None,
    ):
        self.create_time = create_time
        self.domain = domain
        self.instance_type = instance_type
        self.internet_ip = internet_ip
        self.intranet_ip = intranet_ip
        self.is_anchor = is_anchor
        self.organization_peer_name = organization_peer_name
        self.port = port
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.internet_ip is not None:
            result['InternetIp'] = self.internet_ip
        if self.intranet_ip is not None:
            result['IntranetIp'] = self.intranet_ip
        if self.is_anchor is not None:
            result['IsAnchor'] = self.is_anchor
        if self.organization_peer_name is not None:
            result['OrganizationPeerName'] = self.organization_peer_name
        if self.port is not None:
            result['Port'] = self.port
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('InternetIp') is not None:
            self.internet_ip = m.get('InternetIp')
        if m.get('IntranetIp') is not None:
            self.intranet_ip = m.get('IntranetIp')
        if m.get('IsAnchor') is not None:
            self.is_anchor = m.get('IsAnchor')
        if m.get('OrganizationPeerName') is not None:
            self.organization_peer_name = m.get('OrganizationPeerName')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class DescribeFabricOrganizationPeersResponseBody(TeaModel):
    def __init__(
        self,
        error_code: int = None,
        request_id: str = None,
        result: List[DescribeFabricOrganizationPeersResponseBodyResult] = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.request_id = request_id
        self.result = result
        self.success = success

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = DescribeFabricOrganizationPeersResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeFabricOrganizationPeersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeFabricOrganizationPeersResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeFabricOrganizationPeersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFabricOrganizationSpecsResponseBodyResult(TeaModel):
    def __init__(
        self,
        enable: bool = None,
        organization_specs_name: str = None,
        title: str = None,
    ):
        self.enable = enable
        self.organization_specs_name = organization_specs_name
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.organization_specs_name is not None:
            result['OrganizationSpecsName'] = self.organization_specs_name
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('OrganizationSpecsName') is not None:
            self.organization_specs_name = m.get('OrganizationSpecsName')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class DescribeFabricOrganizationSpecsResponseBody(TeaModel):
    def __init__(
        self,
        error_code: int = None,
        request_id: str = None,
        result: List[DescribeFabricOrganizationSpecsResponseBodyResult] = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.request_id = request_id
        self.result = result
        self.success = success

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = DescribeFabricOrganizationSpecsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeFabricOrganizationSpecsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeFabricOrganizationSpecsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeFabricOrganizationSpecsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFabricOrganizationUsersRequest(TeaModel):
    def __init__(
        self,
        location: str = None,
        organization_id: str = None,
    ):
        self.location = location
        # This parameter is required.
        self.organization_id = organization_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.location is not None:
            result['Location'] = self.location
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class DescribeFabricOrganizationUsersResponseBodyResult(TeaModel):
    def __init__(
        self,
        attrs: str = None,
        caller_bid: str = None,
        caller_uid: int = None,
        create_time: str = None,
        expire_time: str = None,
        full_name: str = None,
        organization_id: str = None,
        region_id: str = None,
        username: str = None,
    ):
        self.attrs = attrs
        self.caller_bid = caller_bid
        self.caller_uid = caller_uid
        self.create_time = create_time
        self.expire_time = expire_time
        self.full_name = full_name
        self.organization_id = organization_id
        self.region_id = region_id
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attrs is not None:
            result['Attrs'] = self.attrs
        if self.caller_bid is not None:
            result['CallerBid'] = self.caller_bid
        if self.caller_uid is not None:
            result['CallerUid'] = self.caller_uid
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.full_name is not None:
            result['FullName'] = self.full_name
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.username is not None:
            result['Username'] = self.username
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Attrs') is not None:
            self.attrs = m.get('Attrs')
        if m.get('CallerBid') is not None:
            self.caller_bid = m.get('CallerBid')
        if m.get('CallerUid') is not None:
            self.caller_uid = m.get('CallerUid')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('FullName') is not None:
            self.full_name = m.get('FullName')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        return self


class DescribeFabricOrganizationUsersResponseBody(TeaModel):
    def __init__(
        self,
        error_code: int = None,
        request_id: str = None,
        result: List[DescribeFabricOrganizationUsersResponseBodyResult] = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.request_id = request_id
        self.result = result
        self.success = success

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = DescribeFabricOrganizationUsersResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeFabricOrganizationUsersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeFabricOrganizationUsersResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeFabricOrganizationUsersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFabricOrganizationsRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # This parameter is required.
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        code_name: str = None,
        consortium_count: int = None,
        create_time: str = None,
        domain: str = None,
        major_version: str = None,
        organization_description: str = None,
        organization_id: str = None,
        organization_name: str = None,
        owner_bid: str = None,
        owner_name: str = None,
        owner_uid: int = None,
        peer_count: int = None,
        region_id: str = None,
        request_id: str = None,
        spec_name: str = None,
        state: str = None,
        tags: List[DescribeFabricOrganizationsResponseBodyResultTags] = None,
        user_count: int = None,
        zone_id: str = None,
    ):
        self.code_name = code_name
        self.consortium_count = consortium_count
        self.create_time = create_time
        self.domain = domain
        self.major_version = major_version
        self.organization_description = organization_description
        self.organization_id = organization_id
        self.organization_name = organization_name
        self.owner_bid = owner_bid
        self.owner_name = owner_name
        self.owner_uid = owner_uid
        self.peer_count = peer_count
        self.region_id = region_id
        self.request_id = request_id
        self.spec_name = spec_name
        self.state = state
        self.tags = tags
        self.user_count = user_count
        self.zone_id = zone_id

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code_name is not None:
            result['CodeName'] = self.code_name
        if self.consortium_count is not None:
            result['ConsortiumCount'] = self.consortium_count
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.major_version is not None:
            result['MajorVersion'] = self.major_version
        if self.organization_description is not None:
            result['OrganizationDescription'] = self.organization_description
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.organization_name is not None:
            result['OrganizationName'] = self.organization_name
        if self.owner_bid is not None:
            result['OwnerBid'] = self.owner_bid
        if self.owner_name is not None:
            result['OwnerName'] = self.owner_name
        if self.owner_uid is not None:
            result['OwnerUid'] = self.owner_uid
        if self.peer_count is not None:
            result['PeerCount'] = self.peer_count
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.spec_name is not None:
            result['SpecName'] = self.spec_name
        if self.state is not None:
            result['State'] = self.state
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.user_count is not None:
            result['UserCount'] = self.user_count
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CodeName') is not None:
            self.code_name = m.get('CodeName')
        if m.get('ConsortiumCount') is not None:
            self.consortium_count = m.get('ConsortiumCount')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('MajorVersion') is not None:
            self.major_version = m.get('MajorVersion')
        if m.get('OrganizationDescription') is not None:
            self.organization_description = m.get('OrganizationDescription')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('OrganizationName') is not None:
            self.organization_name = m.get('OrganizationName')
        if m.get('OwnerBid') is not None:
            self.owner_bid = m.get('OwnerBid')
        if m.get('OwnerName') is not None:
            self.owner_name = m.get('OwnerName')
        if m.get('OwnerUid') is not None:
            self.owner_uid = m.get('OwnerUid')
        if m.get('PeerCount') is not None:
            self.peer_count = m.get('PeerCount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SpecName') is not None:
            self.spec_name = m.get('SpecName')
        if m.get('State') is not None:
            self.state = m.get('State')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = DescribeFabricOrganizationsResponseBodyResultTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('UserCount') is not None:
            self.user_count = m.get('UserCount')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeFabricOrganizationsResponseBody(TeaModel):
    def __init__(
        self,
        error_code: int = None,
        request_id: str = None,
        result: List[DescribeFabricOrganizationsResponseBodyResult] = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.request_id = request_id
        self.result = result
        self.success = success

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = DescribeFabricOrganizationsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeFabricOrganizationsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeFabricOrganizationsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeFabricOrganizationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFabricPeerLogsRequest(TeaModel):
    def __init__(
        self,
        lines: str = None,
        organization_id: str = None,
        peer_name: str = None,
    ):
        self.lines = lines
        # This parameter is required.
        self.organization_id = organization_id
        # This parameter is required.
        self.peer_name = peer_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lines is not None:
            result['Lines'] = self.lines
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.peer_name is not None:
            result['PeerName'] = self.peer_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lines') is not None:
            self.lines = m.get('Lines')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('PeerName') is not None:
            self.peer_name = m.get('PeerName')
        return self


class DescribeFabricPeerLogsResponseBody(TeaModel):
    def __init__(
        self,
        error_code: int = None,
        request_id: str = None,
        result: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.request_id = request_id
        self.result = result
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeFabricPeerLogsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeFabricPeerLogsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeFabricPeerLogsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRegionsRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        region_id: str = None,
    ):
        self.accept_language = accept_language
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        error_code: int = None,
        regions: List[DescribeRegionsResponseBodyRegions] = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.regions = regions
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.regions:
            for k in self.regions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        result['Regions'] = []
        if self.regions is not None:
            for k in self.regions:
                result['Regions'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        self.regions = []
        if m.get('Regions') is not None:
            for k in m.get('Regions'):
                temp_model = DescribeRegionsResponseBodyRegions()
                self.regions.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeRegionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeRegionsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRootDomainResponseBody(TeaModel):
    def __init__(
        self,
        error_code: int = None,
        request_id: str = None,
        result: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.request_id = request_id
        self.result = result
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeRootDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeRootDomainResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeRootDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTasksResponseBodyResult(TeaModel):
    def __init__(
        self,
        action: str = None,
        handled: bool = None,
        operation_type: str = None,
        request_time: int = None,
        response_time: str = None,
        result: str = None,
        sender: str = None,
        target: str = None,
        task_id: int = None,
    ):
        self.action = action
        self.handled = handled
        self.operation_type = operation_type
        self.request_time = request_time
        self.response_time = response_time
        self.result = result
        self.sender = sender
        self.target = target
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.handled is not None:
            result['Handled'] = self.handled
        if self.operation_type is not None:
            result['OperationType'] = self.operation_type
        if self.request_time is not None:
            result['RequestTime'] = self.request_time
        if self.response_time is not None:
            result['ResponseTime'] = self.response_time
        if self.result is not None:
            result['Result'] = self.result
        if self.sender is not None:
            result['Sender'] = self.sender
        if self.target is not None:
            result['Target'] = self.target
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('Handled') is not None:
            self.handled = m.get('Handled')
        if m.get('OperationType') is not None:
            self.operation_type = m.get('OperationType')
        if m.get('RequestTime') is not None:
            self.request_time = m.get('RequestTime')
        if m.get('ResponseTime') is not None:
            self.response_time = m.get('ResponseTime')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Sender') is not None:
            self.sender = m.get('Sender')
        if m.get('Target') is not None:
            self.target = m.get('Target')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DescribeTasksResponseBody(TeaModel):
    def __init__(
        self,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_code: int = None,
        request_id: str = None,
        result: List[DescribeTasksResponseBodyResult] = None,
        success: bool = None,
    ):
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.error_code = error_code
        self.request_id = request_id
        self.result = result
        self.success = success

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = DescribeTasksResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeTasksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeTasksResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DownloadFabricOrganizationSDKRequest(TeaModel):
    def __init__(
        self,
        location: str = None,
        organization_id: str = None,
        username: str = None,
    ):
        self.location = location
        # This parameter is required.
        self.organization_id = organization_id
        # This parameter is required.
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.location is not None:
            result['Location'] = self.location
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.username is not None:
            result['Username'] = self.username
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        return self


class DownloadFabricOrganizationSDKResponseBodyResult(TeaModel):
    def __init__(
        self,
        content: str = None,
        path: str = None,
    ):
        self.content = content
        self.path = path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.path is not None:
            result['Path'] = self.path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        return self


class DownloadFabricOrganizationSDKResponseBody(TeaModel):
    def __init__(
        self,
        error_code: int = None,
        request_id: str = None,
        result: List[DownloadFabricOrganizationSDKResponseBodyResult] = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.request_id = request_id
        self.result = result
        self.success = success

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = DownloadFabricOrganizationSDKResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DownloadFabricOrganizationSDKResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DownloadFabricOrganizationSDKResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DownloadFabricOrganizationSDKResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FreezeAntChainAccountRequest(TeaModel):
    def __init__(
        self,
        account: str = None,
        ant_chain_id: str = None,
    ):
        # This parameter is required.
        self.account = account
        # This parameter is required.
        self.ant_chain_id = ant_chain_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        status_code: int = None,
        body: FreezeAntChainAccountResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = FreezeAntChainAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InstallFabricChaincodeRequest(TeaModel):
    def __init__(
        self,
        chaincode_id: str = None,
        location: str = None,
        organization_id: str = None,
    ):
        # This parameter is required.
        self.chaincode_id = chaincode_id
        self.location = location
        # This parameter is required.
        self.organization_id = organization_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.chaincode_id is not None:
            result['ChaincodeId'] = self.chaincode_id
        if self.location is not None:
            result['Location'] = self.location
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChaincodeId') is not None:
            self.chaincode_id = m.get('ChaincodeId')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class InstallFabricChaincodeResponseBodyResult(TeaModel):
    def __init__(
        self,
        chaincode_id: str = None,
        chaincode_name: str = None,
        chaincode_version: str = None,
        channel_name: str = None,
        consortium_id: str = None,
        create_time: str = None,
        deploy_time: str = None,
        endorse_policy: str = None,
        input: str = None,
        install: bool = None,
        message: str = None,
        path: str = None,
        provider_id: str = None,
        provider_name: str = None,
        state: str = None,
        type: int = None,
    ):
        self.chaincode_id = chaincode_id
        self.chaincode_name = chaincode_name
        self.chaincode_version = chaincode_version
        self.channel_name = channel_name
        self.consortium_id = consortium_id
        self.create_time = create_time
        self.deploy_time = deploy_time
        self.endorse_policy = endorse_policy
        self.input = input
        self.install = install
        self.message = message
        self.path = path
        self.provider_id = provider_id
        self.provider_name = provider_name
        self.state = state
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.chaincode_id is not None:
            result['ChaincodeId'] = self.chaincode_id
        if self.chaincode_name is not None:
            result['ChaincodeName'] = self.chaincode_name
        if self.chaincode_version is not None:
            result['ChaincodeVersion'] = self.chaincode_version
        if self.channel_name is not None:
            result['ChannelName'] = self.channel_name
        if self.consortium_id is not None:
            result['ConsortiumId'] = self.consortium_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.deploy_time is not None:
            result['DeployTime'] = self.deploy_time
        if self.endorse_policy is not None:
            result['EndorsePolicy'] = self.endorse_policy
        if self.input is not None:
            result['Input'] = self.input
        if self.install is not None:
            result['Install'] = self.install
        if self.message is not None:
            result['Message'] = self.message
        if self.path is not None:
            result['Path'] = self.path
        if self.provider_id is not None:
            result['ProviderId'] = self.provider_id
        if self.provider_name is not None:
            result['ProviderName'] = self.provider_name
        if self.state is not None:
            result['State'] = self.state
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChaincodeId') is not None:
            self.chaincode_id = m.get('ChaincodeId')
        if m.get('ChaincodeName') is not None:
            self.chaincode_name = m.get('ChaincodeName')
        if m.get('ChaincodeVersion') is not None:
            self.chaincode_version = m.get('ChaincodeVersion')
        if m.get('ChannelName') is not None:
            self.channel_name = m.get('ChannelName')
        if m.get('ConsortiumId') is not None:
            self.consortium_id = m.get('ConsortiumId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DeployTime') is not None:
            self.deploy_time = m.get('DeployTime')
        if m.get('EndorsePolicy') is not None:
            self.endorse_policy = m.get('EndorsePolicy')
        if m.get('Input') is not None:
            self.input = m.get('Input')
        if m.get('Install') is not None:
            self.install = m.get('Install')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('ProviderId') is not None:
            self.provider_id = m.get('ProviderId')
        if m.get('ProviderName') is not None:
            self.provider_name = m.get('ProviderName')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class InstallFabricChaincodeResponseBody(TeaModel):
    def __init__(
        self,
        error_code: int = None,
        request_id: str = None,
        result: InstallFabricChaincodeResponseBodyResult = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.request_id = request_id
        self.result = result
        self.success = success

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = InstallFabricChaincodeResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class InstallFabricChaincodeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: InstallFabricChaincodeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = InstallFabricChaincodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InstallFabricChaincodePackageRequest(TeaModel):
    def __init__(
        self,
        chaincode_package_id: str = None,
        location: str = None,
        organization_id: str = None,
    ):
        # This parameter is required.
        self.chaincode_package_id = chaincode_package_id
        self.location = location
        # This parameter is required.
        self.organization_id = organization_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.chaincode_package_id is not None:
            result['ChaincodePackageId'] = self.chaincode_package_id
        if self.location is not None:
            result['Location'] = self.location
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChaincodePackageId') is not None:
            self.chaincode_package_id = m.get('ChaincodePackageId')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class InstallFabricChaincodePackageResponseBody(TeaModel):
    def __init__(
        self,
        error_code: int = None,
        message: str = None,
        request_id: str = None,
        result: ChaincodePackage = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.result = result
        self.success = success

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = ChaincodePackage()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class InstallFabricChaincodePackageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: InstallFabricChaincodePackageResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = InstallFabricChaincodePackageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InstantiateFabricChaincodeRequest(TeaModel):
    def __init__(
        self,
        chaincode_id: str = None,
        collection_config: str = None,
        endorse_policy: str = None,
        location: str = None,
        organization_id: str = None,
    ):
        # This parameter is required.
        self.chaincode_id = chaincode_id
        self.collection_config = collection_config
        self.endorse_policy = endorse_policy
        self.location = location
        # This parameter is required.
        self.organization_id = organization_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.chaincode_id is not None:
            result['ChaincodeId'] = self.chaincode_id
        if self.collection_config is not None:
            result['CollectionConfig'] = self.collection_config
        if self.endorse_policy is not None:
            result['EndorsePolicy'] = self.endorse_policy
        if self.location is not None:
            result['Location'] = self.location
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChaincodeId') is not None:
            self.chaincode_id = m.get('ChaincodeId')
        if m.get('CollectionConfig') is not None:
            self.collection_config = m.get('CollectionConfig')
        if m.get('EndorsePolicy') is not None:
            self.endorse_policy = m.get('EndorsePolicy')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class InstantiateFabricChaincodeResponseBodyResult(TeaModel):
    def __init__(
        self,
        chaincode_id: str = None,
        chaincode_name: str = None,
        chaincode_version: str = None,
        channel_name: str = None,
        consortium_id: str = None,
        create_time: str = None,
        deploy_time: str = None,
        endorse_policy: str = None,
        input: str = None,
        install: bool = None,
        message: str = None,
        path: str = None,
        provider_id: str = None,
        provider_name: str = None,
        state: str = None,
        type: int = None,
    ):
        self.chaincode_id = chaincode_id
        self.chaincode_name = chaincode_name
        self.chaincode_version = chaincode_version
        self.channel_name = channel_name
        self.consortium_id = consortium_id
        self.create_time = create_time
        self.deploy_time = deploy_time
        self.endorse_policy = endorse_policy
        self.input = input
        self.install = install
        self.message = message
        self.path = path
        self.provider_id = provider_id
        self.provider_name = provider_name
        self.state = state
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.chaincode_id is not None:
            result['ChaincodeId'] = self.chaincode_id
        if self.chaincode_name is not None:
            result['ChaincodeName'] = self.chaincode_name
        if self.chaincode_version is not None:
            result['ChaincodeVersion'] = self.chaincode_version
        if self.channel_name is not None:
            result['ChannelName'] = self.channel_name
        if self.consortium_id is not None:
            result['ConsortiumId'] = self.consortium_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.deploy_time is not None:
            result['DeployTime'] = self.deploy_time
        if self.endorse_policy is not None:
            result['EndorsePolicy'] = self.endorse_policy
        if self.input is not None:
            result['Input'] = self.input
        if self.install is not None:
            result['Install'] = self.install
        if self.message is not None:
            result['Message'] = self.message
        if self.path is not None:
            result['Path'] = self.path
        if self.provider_id is not None:
            result['ProviderId'] = self.provider_id
        if self.provider_name is not None:
            result['ProviderName'] = self.provider_name
        if self.state is not None:
            result['State'] = self.state
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChaincodeId') is not None:
            self.chaincode_id = m.get('ChaincodeId')
        if m.get('ChaincodeName') is not None:
            self.chaincode_name = m.get('ChaincodeName')
        if m.get('ChaincodeVersion') is not None:
            self.chaincode_version = m.get('ChaincodeVersion')
        if m.get('ChannelName') is not None:
            self.channel_name = m.get('ChannelName')
        if m.get('ConsortiumId') is not None:
            self.consortium_id = m.get('ConsortiumId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DeployTime') is not None:
            self.deploy_time = m.get('DeployTime')
        if m.get('EndorsePolicy') is not None:
            self.endorse_policy = m.get('EndorsePolicy')
        if m.get('Input') is not None:
            self.input = m.get('Input')
        if m.get('Install') is not None:
            self.install = m.get('Install')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('ProviderId') is not None:
            self.provider_id = m.get('ProviderId')
        if m.get('ProviderName') is not None:
            self.provider_name = m.get('ProviderName')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class InstantiateFabricChaincodeResponseBody(TeaModel):
    def __init__(
        self,
        error_code: int = None,
        request_id: str = None,
        result: InstantiateFabricChaincodeResponseBodyResult = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.request_id = request_id
        self.result = result
        self.success = success

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = InstantiateFabricChaincodeResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class InstantiateFabricChaincodeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: InstantiateFabricChaincodeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
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
        # This parameter is required.
        self.channel_id = channel_id
        # This parameter is required.
        self.do = do
        self.location = location

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        accept_time: str = None,
        approve_time: str = None,
        channel_id: str = None,
        confirm_time: str = None,
        destroy_time: str = None,
        invite_time: str = None,
        organization_id: str = None,
        state: str = None,
        with_peer: bool = None,
    ):
        self.accept_time = accept_time
        self.approve_time = approve_time
        self.channel_id = channel_id
        self.confirm_time = confirm_time
        self.destroy_time = destroy_time
        self.invite_time = invite_time
        self.organization_id = organization_id
        self.state = state
        self.with_peer = with_peer

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_time is not None:
            result['AcceptTime'] = self.accept_time
        if self.approve_time is not None:
            result['ApproveTime'] = self.approve_time
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.confirm_time is not None:
            result['ConfirmTime'] = self.confirm_time
        if self.destroy_time is not None:
            result['DestroyTime'] = self.destroy_time
        if self.invite_time is not None:
            result['InviteTime'] = self.invite_time
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.state is not None:
            result['State'] = self.state
        if self.with_peer is not None:
            result['WithPeer'] = self.with_peer
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptTime') is not None:
            self.accept_time = m.get('AcceptTime')
        if m.get('ApproveTime') is not None:
            self.approve_time = m.get('ApproveTime')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('ConfirmTime') is not None:
            self.confirm_time = m.get('ConfirmTime')
        if m.get('DestroyTime') is not None:
            self.destroy_time = m.get('DestroyTime')
        if m.get('InviteTime') is not None:
            self.invite_time = m.get('InviteTime')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('WithPeer') is not None:
            self.with_peer = m.get('WithPeer')
        return self


class JoinFabricChannelResponseBody(TeaModel):
    def __init__(
        self,
        error_code: int = None,
        request_id: str = None,
        result: List[JoinFabricChannelResponseBodyResult] = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.request_id = request_id
        self.result = result
        self.success = success

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = JoinFabricChannelResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class JoinFabricChannelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: JoinFabricChannelResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        next_token: str = None,
        resource_id: List[str] = None,
        resource_type: str = None,
        tag: List[ListTagResourcesRequestTag] = None,
    ):
        self.next_token = next_token
        self.resource_id = resource_id
        # This parameter is required.
        self.resource_type = resource_type
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListTagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponseBodyTagResources(TeaModel):
    def __init__(
        self,
        resource_id: str = None,
        resource_type: str = None,
        tag_key: str = None,
        tag_value: str = None,
    ):
        self.resource_id = resource_id
        self.resource_type = resource_type
        self.tag_key = tag_key
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        status_code: int = None,
        body: ListTagResourcesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListTagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResetAntChainCertificateRequest(TeaModel):
    def __init__(
        self,
        ant_chain_id: str = None,
    ):
        # This parameter is required.
        self.ant_chain_id = ant_chain_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        status_code: int = None,
        body: ResetAntChainCertificateResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
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
        # This parameter is required.
        self.ant_chain_id = ant_chain_id
        # This parameter is required.
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        status_code: int = None,
        body: ResetAntChainUserCertificateResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ResetAntChainUserCertificateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResetFabricOrganizationUserPasswordRequest(TeaModel):
    def __init__(
        self,
        location: str = None,
        organization_id: str = None,
        password: str = None,
        username: str = None,
    ):
        self.location = location
        # This parameter is required.
        self.organization_id = organization_id
        # This parameter is required.
        self.password = password
        # This parameter is required.
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.location is not None:
            result['Location'] = self.location
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.password is not None:
            result['Password'] = self.password
        if self.username is not None:
            result['Username'] = self.username
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        return self


class ResetFabricOrganizationUserPasswordResponseBodyResult(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        expire_time: str = None,
        fullname: str = None,
        organization_id: str = None,
        password: str = None,
        username: str = None,
    ):
        self.create_time = create_time
        self.expire_time = expire_time
        self.fullname = fullname
        self.organization_id = organization_id
        self.password = password
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.fullname is not None:
            result['Fullname'] = self.fullname
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.password is not None:
            result['Password'] = self.password
        if self.username is not None:
            result['Username'] = self.username
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('Fullname') is not None:
            self.fullname = m.get('Fullname')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        return self


class ResetFabricOrganizationUserPasswordResponseBody(TeaModel):
    def __init__(
        self,
        error_code: int = None,
        request_id: str = None,
        result: ResetFabricOrganizationUserPasswordResponseBodyResult = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.request_id = request_id
        self.result = result
        self.success = success

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = ResetFabricOrganizationUserPasswordResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ResetFabricOrganizationUserPasswordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ResetFabricOrganizationUserPasswordResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ResetFabricOrganizationUserPasswordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitFabricChaincodeDefinitionRequest(TeaModel):
    def __init__(
        self,
        chaincode_package_id: str = None,
        chaincode_version: str = None,
        channel_id: str = None,
        collection_config: str = None,
        endorse_policy: str = None,
        init_required: bool = None,
        location: str = None,
        name: str = None,
        organization_id: str = None,
    ):
        # This parameter is required.
        self.chaincode_package_id = chaincode_package_id
        # This parameter is required.
        self.chaincode_version = chaincode_version
        # This parameter is required.
        self.channel_id = channel_id
        self.collection_config = collection_config
        # This parameter is required.
        self.endorse_policy = endorse_policy
        self.init_required = init_required
        self.location = location
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.organization_id = organization_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.chaincode_package_id is not None:
            result['ChaincodePackageId'] = self.chaincode_package_id
        if self.chaincode_version is not None:
            result['ChaincodeVersion'] = self.chaincode_version
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.collection_config is not None:
            result['CollectionConfig'] = self.collection_config
        if self.endorse_policy is not None:
            result['EndorsePolicy'] = self.endorse_policy
        if self.init_required is not None:
            result['InitRequired'] = self.init_required
        if self.location is not None:
            result['Location'] = self.location
        if self.name is not None:
            result['Name'] = self.name
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChaincodePackageId') is not None:
            self.chaincode_package_id = m.get('ChaincodePackageId')
        if m.get('ChaincodeVersion') is not None:
            self.chaincode_version = m.get('ChaincodeVersion')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('CollectionConfig') is not None:
            self.collection_config = m.get('CollectionConfig')
        if m.get('EndorsePolicy') is not None:
            self.endorse_policy = m.get('EndorsePolicy')
        if m.get('InitRequired') is not None:
            self.init_required = m.get('InitRequired')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class SubmitFabricChaincodeDefinitionResponseBody(TeaModel):
    def __init__(
        self,
        error_code: int = None,
        message: str = None,
        request_id: str = None,
        result: ChaincodeVO = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.result = result
        self.success = success

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = ChaincodeVO()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SubmitFabricChaincodeDefinitionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SubmitFabricChaincodeDefinitionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SubmitFabricChaincodeDefinitionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SynchronizeFabricChaincodeRequest(TeaModel):
    def __init__(
        self,
        chaincode_id: str = None,
        organization_id: str = None,
    ):
        # This parameter is required.
        self.chaincode_id = chaincode_id
        # This parameter is required.
        self.organization_id = organization_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.chaincode_id is not None:
            result['ChaincodeId'] = self.chaincode_id
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChaincodeId') is not None:
            self.chaincode_id = m.get('ChaincodeId')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class SynchronizeFabricChaincodeResponseBodyResult(TeaModel):
    def __init__(
        self,
        chaincode_id: str = None,
        chaincode_name: str = None,
        chaincode_version: str = None,
        channel_name: str = None,
        consortium_id: str = None,
        create_time: str = None,
        deploy_time: str = None,
        endorse_policy: str = None,
        input: str = None,
        install: bool = None,
        message: str = None,
        path: str = None,
        provider_id: str = None,
        provider_name: str = None,
        state: str = None,
        type: int = None,
    ):
        self.chaincode_id = chaincode_id
        self.chaincode_name = chaincode_name
        self.chaincode_version = chaincode_version
        self.channel_name = channel_name
        self.consortium_id = consortium_id
        self.create_time = create_time
        self.deploy_time = deploy_time
        self.endorse_policy = endorse_policy
        self.input = input
        self.install = install
        self.message = message
        self.path = path
        self.provider_id = provider_id
        self.provider_name = provider_name
        self.state = state
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.chaincode_id is not None:
            result['ChaincodeId'] = self.chaincode_id
        if self.chaincode_name is not None:
            result['ChaincodeName'] = self.chaincode_name
        if self.chaincode_version is not None:
            result['ChaincodeVersion'] = self.chaincode_version
        if self.channel_name is not None:
            result['ChannelName'] = self.channel_name
        if self.consortium_id is not None:
            result['ConsortiumId'] = self.consortium_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.deploy_time is not None:
            result['DeployTime'] = self.deploy_time
        if self.endorse_policy is not None:
            result['EndorsePolicy'] = self.endorse_policy
        if self.input is not None:
            result['Input'] = self.input
        if self.install is not None:
            result['Install'] = self.install
        if self.message is not None:
            result['Message'] = self.message
        if self.path is not None:
            result['Path'] = self.path
        if self.provider_id is not None:
            result['ProviderId'] = self.provider_id
        if self.provider_name is not None:
            result['ProviderName'] = self.provider_name
        if self.state is not None:
            result['State'] = self.state
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChaincodeId') is not None:
            self.chaincode_id = m.get('ChaincodeId')
        if m.get('ChaincodeName') is not None:
            self.chaincode_name = m.get('ChaincodeName')
        if m.get('ChaincodeVersion') is not None:
            self.chaincode_version = m.get('ChaincodeVersion')
        if m.get('ChannelName') is not None:
            self.channel_name = m.get('ChannelName')
        if m.get('ConsortiumId') is not None:
            self.consortium_id = m.get('ConsortiumId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DeployTime') is not None:
            self.deploy_time = m.get('DeployTime')
        if m.get('EndorsePolicy') is not None:
            self.endorse_policy = m.get('EndorsePolicy')
        if m.get('Input') is not None:
            self.input = m.get('Input')
        if m.get('Install') is not None:
            self.install = m.get('Install')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('ProviderId') is not None:
            self.provider_id = m.get('ProviderId')
        if m.get('ProviderName') is not None:
            self.provider_name = m.get('ProviderName')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class SynchronizeFabricChaincodeResponseBody(TeaModel):
    def __init__(
        self,
        error_code: int = None,
        request_id: str = None,
        result: SynchronizeFabricChaincodeResponseBodyResult = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.request_id = request_id
        self.result = result
        self.success = success

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = SynchronizeFabricChaincodeResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SynchronizeFabricChaincodeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SynchronizeFabricChaincodeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        resource_id: List[str] = None,
        resource_type: str = None,
        tag: List[TagResourcesRequestTag] = None,
    ):
        self.resource_id = resource_id
        # This parameter is required.
        self.resource_type = resource_type
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = TagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class TagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        error_code: int = None,
        request_id: str = None,
        result: bool = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.request_id = request_id
        self.result = result
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class TagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: TagResourcesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = TagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnfreezeAntChainAccountRequest(TeaModel):
    def __init__(
        self,
        account: str = None,
        ant_chain_id: str = None,
    ):
        # This parameter is required.
        self.account = account
        # This parameter is required.
        self.ant_chain_id = ant_chain_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        status_code: int = None,
        body: UnfreezeAntChainAccountResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UnfreezeAntChainAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UntagResourcesRequest(TeaModel):
    def __init__(
        self,
        all: bool = None,
        resource_id: List[str] = None,
        resource_type: str = None,
        tag_key: List[str] = None,
    ):
        self.all = all
        self.resource_id = resource_id
        # This parameter is required.
        self.resource_type = resource_type
        self.tag_key = tag_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all is not None:
            result['All'] = self.all
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('All') is not None:
            self.all = m.get('All')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        return self


class UntagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        error_code: int = None,
        request_id: str = None,
        result: bool = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.request_id = request_id
        self.result = result
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UntagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UntagResourcesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
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
        # This parameter is required.
        self.ant_chain_id = ant_chain_id
        # This parameter is required.
        self.ant_chain_name = ant_chain_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        status_code: int = None,
        body: UpdateAntChainResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateAntChainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAntChainConsortiumRequest(TeaModel):
    def __init__(
        self,
        consortium_description: str = None,
        consortium_id: str = None,
        consortium_name: str = None,
    ):
        self.consortium_description = consortium_description
        # This parameter is required.
        self.consortium_id = consortium_id
        # This parameter is required.
        self.consortium_name = consortium_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consortium_description is not None:
            result['ConsortiumDescription'] = self.consortium_description
        if self.consortium_id is not None:
            result['ConsortiumId'] = self.consortium_id
        if self.consortium_name is not None:
            result['ConsortiumName'] = self.consortium_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsortiumDescription') is not None:
            self.consortium_description = m.get('ConsortiumDescription')
        if m.get('ConsortiumId') is not None:
            self.consortium_id = m.get('ConsortiumId')
        if m.get('ConsortiumName') is not None:
            self.consortium_name = m.get('ConsortiumName')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        status_code: int = None,
        body: UpdateAntChainConsortiumResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateAntChainConsortiumResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAntChainContractContentRequest(TeaModel):
    def __init__(
        self,
        content: str = None,
        content_id: str = None,
        content_name: str = None,
        parent_content_id: str = None,
    ):
        self.content = content
        # This parameter is required.
        self.content_id = content_id
        self.content_name = content_name
        self.parent_content_id = parent_content_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.content_id is not None:
            result['ContentId'] = self.content_id
        if self.content_name is not None:
            result['ContentName'] = self.content_name
        if self.parent_content_id is not None:
            result['ParentContentId'] = self.parent_content_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('ContentId') is not None:
            self.content_id = m.get('ContentId')
        if m.get('ContentName') is not None:
            self.content_name = m.get('ContentName')
        if m.get('ParentContentId') is not None:
            self.parent_content_id = m.get('ParentContentId')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        status_code: int = None,
        body: UpdateAntChainContractContentResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateAntChainContractContentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAntChainContractProjectRequest(TeaModel):
    def __init__(
        self,
        project_description: str = None,
        project_id: str = None,
        project_name: str = None,
        project_version: str = None,
    ):
        self.project_description = project_description
        # This parameter is required.
        self.project_id = project_id
        self.project_name = project_name
        self.project_version = project_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_description is not None:
            result['ProjectDescription'] = self.project_description
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.project_version is not None:
            result['ProjectVersion'] = self.project_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectDescription') is not None:
            self.project_description = m.get('ProjectDescription')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('ProjectVersion') is not None:
            self.project_version = m.get('ProjectVersion')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        status_code: int = None,
        body: UpdateAntChainContractProjectResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateAntChainContractProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAntChainMemberRequest(TeaModel):
    def __init__(
        self,
        consortium_id: str = None,
        member_id: str = None,
        member_name: str = None,
    ):
        # This parameter is required.
        self.consortium_id = consortium_id
        # This parameter is required.
        self.member_id = member_id
        # This parameter is required.
        self.member_name = member_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consortium_id is not None:
            result['ConsortiumId'] = self.consortium_id
        if self.member_id is not None:
            result['MemberId'] = self.member_id
        if self.member_name is not None:
            result['MemberName'] = self.member_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsortiumId') is not None:
            self.consortium_id = m.get('ConsortiumId')
        if m.get('MemberId') is not None:
            self.member_id = m.get('MemberId')
        if m.get('MemberName') is not None:
            self.member_name = m.get('MemberName')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        status_code: int = None,
        body: UpdateAntChainMemberResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateAntChainMemberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAntChainQRCodeAuthorizationRequest(TeaModel):
    def __init__(
        self,
        ant_chain_id: str = None,
        authorization_type: str = None,
        qrcode_type: str = None,
    ):
        # This parameter is required.
        self.ant_chain_id = ant_chain_id
        # This parameter is required.
        self.authorization_type = authorization_type
        # This parameter is required.
        self.qrcode_type = qrcode_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ant_chain_id is not None:
            result['AntChainId'] = self.ant_chain_id
        if self.authorization_type is not None:
            result['AuthorizationType'] = self.authorization_type
        if self.qrcode_type is not None:
            result['QRCodeType'] = self.qrcode_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AntChainId') is not None:
            self.ant_chain_id = m.get('AntChainId')
        if m.get('AuthorizationType') is not None:
            self.authorization_type = m.get('AuthorizationType')
        if m.get('QRCodeType') is not None:
            self.qrcode_type = m.get('QRCodeType')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        status_code: int = None,
        body: UpdateAntChainQRCodeAuthorizationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateAntChainQRCodeAuthorizationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpgradeFabricChaincodeRequest(TeaModel):
    def __init__(
        self,
        chaincode_id: str = None,
        collection_config: str = None,
        endorse_policy: str = None,
        location: str = None,
        organization_id: str = None,
    ):
        # This parameter is required.
        self.chaincode_id = chaincode_id
        self.collection_config = collection_config
        self.endorse_policy = endorse_policy
        self.location = location
        # This parameter is required.
        self.organization_id = organization_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.chaincode_id is not None:
            result['ChaincodeId'] = self.chaincode_id
        if self.collection_config is not None:
            result['CollectionConfig'] = self.collection_config
        if self.endorse_policy is not None:
            result['EndorsePolicy'] = self.endorse_policy
        if self.location is not None:
            result['Location'] = self.location
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChaincodeId') is not None:
            self.chaincode_id = m.get('ChaincodeId')
        if m.get('CollectionConfig') is not None:
            self.collection_config = m.get('CollectionConfig')
        if m.get('EndorsePolicy') is not None:
            self.endorse_policy = m.get('EndorsePolicy')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class UpgradeFabricChaincodeResponseBodyResult(TeaModel):
    def __init__(
        self,
        chaincode_id: str = None,
        chaincode_name: str = None,
        chaincode_version: str = None,
        channel_name: str = None,
        consortium_id: str = None,
        create_time: str = None,
        deploy_time: str = None,
        endorse_policy: str = None,
        input: str = None,
        install: bool = None,
        message: str = None,
        path: str = None,
        provider_id: str = None,
        provider_name: str = None,
        state: str = None,
        type: int = None,
    ):
        self.chaincode_id = chaincode_id
        self.chaincode_name = chaincode_name
        self.chaincode_version = chaincode_version
        self.channel_name = channel_name
        self.consortium_id = consortium_id
        self.create_time = create_time
        self.deploy_time = deploy_time
        self.endorse_policy = endorse_policy
        self.input = input
        self.install = install
        self.message = message
        self.path = path
        self.provider_id = provider_id
        self.provider_name = provider_name
        self.state = state
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.chaincode_id is not None:
            result['ChaincodeId'] = self.chaincode_id
        if self.chaincode_name is not None:
            result['ChaincodeName'] = self.chaincode_name
        if self.chaincode_version is not None:
            result['ChaincodeVersion'] = self.chaincode_version
        if self.channel_name is not None:
            result['ChannelName'] = self.channel_name
        if self.consortium_id is not None:
            result['ConsortiumId'] = self.consortium_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.deploy_time is not None:
            result['DeployTime'] = self.deploy_time
        if self.endorse_policy is not None:
            result['EndorsePolicy'] = self.endorse_policy
        if self.input is not None:
            result['Input'] = self.input
        if self.install is not None:
            result['Install'] = self.install
        if self.message is not None:
            result['Message'] = self.message
        if self.path is not None:
            result['Path'] = self.path
        if self.provider_id is not None:
            result['ProviderId'] = self.provider_id
        if self.provider_name is not None:
            result['ProviderName'] = self.provider_name
        if self.state is not None:
            result['State'] = self.state
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChaincodeId') is not None:
            self.chaincode_id = m.get('ChaincodeId')
        if m.get('ChaincodeName') is not None:
            self.chaincode_name = m.get('ChaincodeName')
        if m.get('ChaincodeVersion') is not None:
            self.chaincode_version = m.get('ChaincodeVersion')
        if m.get('ChannelName') is not None:
            self.channel_name = m.get('ChannelName')
        if m.get('ConsortiumId') is not None:
            self.consortium_id = m.get('ConsortiumId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DeployTime') is not None:
            self.deploy_time = m.get('DeployTime')
        if m.get('EndorsePolicy') is not None:
            self.endorse_policy = m.get('EndorsePolicy')
        if m.get('Input') is not None:
            self.input = m.get('Input')
        if m.get('Install') is not None:
            self.install = m.get('Install')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('ProviderId') is not None:
            self.provider_id = m.get('ProviderId')
        if m.get('ProviderName') is not None:
            self.provider_name = m.get('ProviderName')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class UpgradeFabricChaincodeResponseBody(TeaModel):
    def __init__(
        self,
        error_code: int = None,
        request_id: str = None,
        result: UpgradeFabricChaincodeResponseBodyResult = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.request_id = request_id
        self.result = result
        self.success = success

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = UpgradeFabricChaincodeResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpgradeFabricChaincodeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpgradeFabricChaincodeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpgradeFabricChaincodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpgradeFabricChaincodeDefinitionRequest(TeaModel):
    def __init__(
        self,
        chaincode_id: str = None,
        chaincode_package_id: str = None,
        chaincode_version: str = None,
        collection_config: str = None,
        endorse_policy: str = None,
        init_required: bool = None,
        location: str = None,
        organization_id: str = None,
    ):
        # This parameter is required.
        self.chaincode_id = chaincode_id
        # This parameter is required.
        self.chaincode_package_id = chaincode_package_id
        # This parameter is required.
        self.chaincode_version = chaincode_version
        self.collection_config = collection_config
        # This parameter is required.
        self.endorse_policy = endorse_policy
        self.init_required = init_required
        self.location = location
        # This parameter is required.
        self.organization_id = organization_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.chaincode_id is not None:
            result['ChaincodeId'] = self.chaincode_id
        if self.chaincode_package_id is not None:
            result['ChaincodePackageId'] = self.chaincode_package_id
        if self.chaincode_version is not None:
            result['ChaincodeVersion'] = self.chaincode_version
        if self.collection_config is not None:
            result['CollectionConfig'] = self.collection_config
        if self.endorse_policy is not None:
            result['EndorsePolicy'] = self.endorse_policy
        if self.init_required is not None:
            result['InitRequired'] = self.init_required
        if self.location is not None:
            result['Location'] = self.location
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChaincodeId') is not None:
            self.chaincode_id = m.get('ChaincodeId')
        if m.get('ChaincodePackageId') is not None:
            self.chaincode_package_id = m.get('ChaincodePackageId')
        if m.get('ChaincodeVersion') is not None:
            self.chaincode_version = m.get('ChaincodeVersion')
        if m.get('CollectionConfig') is not None:
            self.collection_config = m.get('CollectionConfig')
        if m.get('EndorsePolicy') is not None:
            self.endorse_policy = m.get('EndorsePolicy')
        if m.get('InitRequired') is not None:
            self.init_required = m.get('InitRequired')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class UpgradeFabricChaincodeDefinitionResponseBody(TeaModel):
    def __init__(
        self,
        error_code: int = None,
        message: str = None,
        request_id: str = None,
        result: ChaincodeVO = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.result = result
        self.success = success

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = ChaincodeVO()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpgradeFabricChaincodeDefinitionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpgradeFabricChaincodeDefinitionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpgradeFabricChaincodeDefinitionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


