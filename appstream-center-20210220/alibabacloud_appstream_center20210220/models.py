# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class FindIdpListByLoginIdentifierRequest(TeaModel):
    def __init__(
        self,
        available_features: Dict[str, str] = None,
        client_channel: str = None,
        client_id: str = None,
        client_ip: str = None,
        client_os: str = None,
        client_version: str = None,
        login_identifier: str = None,
        support_types: List[str] = None,
        uuid: str = None,
    ):
        self.available_features = available_features
        self.client_channel = client_channel
        self.client_id = client_id
        self.client_ip = client_ip
        self.client_os = client_os
        self.client_version = client_version
        # This parameter is required.
        self.login_identifier = login_identifier
        self.support_types = support_types
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.available_features is not None:
            result['AvailableFeatures'] = self.available_features
        if self.client_channel is not None:
            result['ClientChannel'] = self.client_channel
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.client_ip is not None:
            result['ClientIp'] = self.client_ip
        if self.client_os is not None:
            result['ClientOS'] = self.client_os
        if self.client_version is not None:
            result['ClientVersion'] = self.client_version
        if self.login_identifier is not None:
            result['LoginIdentifier'] = self.login_identifier
        if self.support_types is not None:
            result['SupportTypes'] = self.support_types
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvailableFeatures') is not None:
            self.available_features = m.get('AvailableFeatures')
        if m.get('ClientChannel') is not None:
            self.client_channel = m.get('ClientChannel')
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('ClientIp') is not None:
            self.client_ip = m.get('ClientIp')
        if m.get('ClientOS') is not None:
            self.client_os = m.get('ClientOS')
        if m.get('ClientVersion') is not None:
            self.client_version = m.get('ClientVersion')
        if m.get('LoginIdentifier') is not None:
            self.login_identifier = m.get('LoginIdentifier')
        if m.get('SupportTypes') is not None:
            self.support_types = m.get('SupportTypes')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class FindIdpListByLoginIdentifierShrinkRequest(TeaModel):
    def __init__(
        self,
        available_features_shrink: str = None,
        client_channel: str = None,
        client_id: str = None,
        client_ip: str = None,
        client_os: str = None,
        client_version: str = None,
        login_identifier: str = None,
        support_types: List[str] = None,
        uuid: str = None,
    ):
        self.available_features_shrink = available_features_shrink
        self.client_channel = client_channel
        self.client_id = client_id
        self.client_ip = client_ip
        self.client_os = client_os
        self.client_version = client_version
        # This parameter is required.
        self.login_identifier = login_identifier
        self.support_types = support_types
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.available_features_shrink is not None:
            result['AvailableFeatures'] = self.available_features_shrink
        if self.client_channel is not None:
            result['ClientChannel'] = self.client_channel
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.client_ip is not None:
            result['ClientIp'] = self.client_ip
        if self.client_os is not None:
            result['ClientOS'] = self.client_os
        if self.client_version is not None:
            result['ClientVersion'] = self.client_version
        if self.login_identifier is not None:
            result['LoginIdentifier'] = self.login_identifier
        if self.support_types is not None:
            result['SupportTypes'] = self.support_types
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvailableFeatures') is not None:
            self.available_features_shrink = m.get('AvailableFeatures')
        if m.get('ClientChannel') is not None:
            self.client_channel = m.get('ClientChannel')
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('ClientIp') is not None:
            self.client_ip = m.get('ClientIp')
        if m.get('ClientOS') is not None:
            self.client_os = m.get('ClientOS')
        if m.get('ClientVersion') is not None:
            self.client_version = m.get('ClientVersion')
        if m.get('LoginIdentifier') is not None:
            self.login_identifier = m.get('LoginIdentifier')
        if m.get('SupportTypes') is not None:
            self.support_types = m.get('SupportTypes')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class FindIdpListByLoginIdentifierResponseBodyIdpInfos(TeaModel):
    def __init__(
        self,
        account_type: str = None,
        cookies: str = None,
        idp_id: str = None,
        idp_name: str = None,
        idp_name_en: str = None,
        idp_provider: str = None,
        jump_switch: str = None,
        sso_protocol: str = None,
        sso_service_url: str = None,
    ):
        self.account_type = account_type
        self.cookies = cookies
        self.idp_id = idp_id
        self.idp_name = idp_name
        self.idp_name_en = idp_name_en
        self.idp_provider = idp_provider
        self.jump_switch = jump_switch
        self.sso_protocol = sso_protocol
        self.sso_service_url = sso_service_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_type is not None:
            result['AccountType'] = self.account_type
        if self.cookies is not None:
            result['Cookies'] = self.cookies
        if self.idp_id is not None:
            result['IdpId'] = self.idp_id
        if self.idp_name is not None:
            result['IdpName'] = self.idp_name
        if self.idp_name_en is not None:
            result['IdpNameEN'] = self.idp_name_en
        if self.idp_provider is not None:
            result['IdpProvider'] = self.idp_provider
        if self.jump_switch is not None:
            result['JumpSwitch'] = self.jump_switch
        if self.sso_protocol is not None:
            result['SsoProtocol'] = self.sso_protocol
        if self.sso_service_url is not None:
            result['SsoServiceUrl'] = self.sso_service_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')
        if m.get('Cookies') is not None:
            self.cookies = m.get('Cookies')
        if m.get('IdpId') is not None:
            self.idp_id = m.get('IdpId')
        if m.get('IdpName') is not None:
            self.idp_name = m.get('IdpName')
        if m.get('IdpNameEN') is not None:
            self.idp_name_en = m.get('IdpNameEN')
        if m.get('IdpProvider') is not None:
            self.idp_provider = m.get('IdpProvider')
        if m.get('JumpSwitch') is not None:
            self.jump_switch = m.get('JumpSwitch')
        if m.get('SsoProtocol') is not None:
            self.sso_protocol = m.get('SsoProtocol')
        if m.get('SsoServiceUrl') is not None:
            self.sso_service_url = m.get('SsoServiceUrl')
        return self


class FindIdpListByLoginIdentifierResponseBodyOfficeSiteInfo(TeaModel):
    def __init__(
        self,
        access_type: str = None,
        office_site_id: str = None,
        provider_id: str = None,
        region_id: str = None,
        sso_service_url: str = None,
    ):
        self.access_type = access_type
        self.office_site_id = office_site_id
        self.provider_id = provider_id
        self.region_id = region_id
        self.sso_service_url = sso_service_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_type is not None:
            result['AccessType'] = self.access_type
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.provider_id is not None:
            result['ProviderId'] = self.provider_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.sso_service_url is not None:
            result['SsoServiceUrl'] = self.sso_service_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessType') is not None:
            self.access_type = m.get('AccessType')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('ProviderId') is not None:
            self.provider_id = m.get('ProviderId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SsoServiceUrl') is not None:
            self.sso_service_url = m.get('SsoServiceUrl')
        return self


class FindIdpListByLoginIdentifierResponseBodyTenantAliasInfo(TeaModel):
    def __init__(
        self,
        access_type: str = None,
        tenant_alias: str = None,
    ):
        self.access_type = access_type
        self.tenant_alias = tenant_alias

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_type is not None:
            result['AccessType'] = self.access_type
        if self.tenant_alias is not None:
            result['TenantAlias'] = self.tenant_alias
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessType') is not None:
            self.access_type = m.get('AccessType')
        if m.get('TenantAlias') is not None:
            self.tenant_alias = m.get('TenantAlias')
        return self


class FindIdpListByLoginIdentifierResponseBody(TeaModel):
    def __init__(
        self,
        idp_infos: List[FindIdpListByLoginIdentifierResponseBodyIdpInfos] = None,
        office_site_info: FindIdpListByLoginIdentifierResponseBodyOfficeSiteInfo = None,
        pop_region_config: Dict[str, str] = None,
        profile_region: str = None,
        request_id: str = None,
        tenant_alias_info: FindIdpListByLoginIdentifierResponseBodyTenantAliasInfo = None,
    ):
        self.idp_infos = idp_infos
        self.office_site_info = office_site_info
        self.pop_region_config = pop_region_config
        self.profile_region = profile_region
        self.request_id = request_id
        self.tenant_alias_info = tenant_alias_info

    def validate(self):
        if self.idp_infos:
            for k in self.idp_infos:
                if k:
                    k.validate()
        if self.office_site_info:
            self.office_site_info.validate()
        if self.tenant_alias_info:
            self.tenant_alias_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['IdpInfos'] = []
        if self.idp_infos is not None:
            for k in self.idp_infos:
                result['IdpInfos'].append(k.to_map() if k else None)
        if self.office_site_info is not None:
            result['OfficeSiteInfo'] = self.office_site_info.to_map()
        if self.pop_region_config is not None:
            result['PopRegionConfig'] = self.pop_region_config
        if self.profile_region is not None:
            result['ProfileRegion'] = self.profile_region
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tenant_alias_info is not None:
            result['TenantAliasInfo'] = self.tenant_alias_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.idp_infos = []
        if m.get('IdpInfos') is not None:
            for k in m.get('IdpInfos'):
                temp_model = FindIdpListByLoginIdentifierResponseBodyIdpInfos()
                self.idp_infos.append(temp_model.from_map(k))
        if m.get('OfficeSiteInfo') is not None:
            temp_model = FindIdpListByLoginIdentifierResponseBodyOfficeSiteInfo()
            self.office_site_info = temp_model.from_map(m['OfficeSiteInfo'])
        if m.get('PopRegionConfig') is not None:
            self.pop_region_config = m.get('PopRegionConfig')
        if m.get('ProfileRegion') is not None:
            self.profile_region = m.get('ProfileRegion')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TenantAliasInfo') is not None:
            temp_model = FindIdpListByLoginIdentifierResponseBodyTenantAliasInfo()
            self.tenant_alias_info = temp_model.from_map(m['TenantAliasInfo'])
        return self


class FindIdpListByLoginIdentifierResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: FindIdpListByLoginIdentifierResponseBody = None,
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
            temp_model = FindIdpListByLoginIdentifierResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLoginTokenRequest(TeaModel):
    def __init__(
        self,
        authentication_code: str = None,
        available_features: Dict[str, str] = None,
        client_id: str = None,
        client_name: str = None,
        client_os: str = None,
        client_type: str = None,
        client_version: str = None,
        current_stage: str = None,
        directory_id: str = None,
        encrypted_finger_print_data: str = None,
        encrypted_key: str = None,
        encrypted_password: str = None,
        end_user_id: str = None,
        finger_print_data: str = None,
        idp_id: str = None,
        image_url: str = None,
        keep_alive: bool = None,
        keep_alive_token: str = None,
        login_identifier: str = None,
        login_name: str = None,
        mfa_type: str = None,
        network_type: str = None,
        new_password: str = None,
        office_site_id: str = None,
        old_password: str = None,
        password: str = None,
        phone: str = None,
        phone_verify_code: str = None,
        profile_region: str = None,
        region_id: str = None,
        session_id: str = None,
        sso_extends_cookies: str = None,
        sso_session_token: str = None,
        token_code: str = None,
        umid_token: str = None,
        uuid: str = None,
    ):
        self.authentication_code = authentication_code
        self.available_features = available_features
        # This parameter is required.
        self.client_id = client_id
        self.client_name = client_name
        self.client_os = client_os
        self.client_type = client_type
        self.client_version = client_version
        self.current_stage = current_stage
        self.directory_id = directory_id
        self.encrypted_finger_print_data = encrypted_finger_print_data
        self.encrypted_key = encrypted_key
        self.encrypted_password = encrypted_password
        self.end_user_id = end_user_id
        self.finger_print_data = finger_print_data
        self.idp_id = idp_id
        self.image_url = image_url
        self.keep_alive = keep_alive
        self.keep_alive_token = keep_alive_token
        self.login_identifier = login_identifier
        self.login_name = login_name
        self.mfa_type = mfa_type
        self.network_type = network_type
        self.new_password = new_password
        self.office_site_id = office_site_id
        self.old_password = old_password
        self.password = password
        self.phone = phone
        self.phone_verify_code = phone_verify_code
        self.profile_region = profile_region
        self.region_id = region_id
        self.session_id = session_id
        self.sso_extends_cookies = sso_extends_cookies
        self.sso_session_token = sso_session_token
        self.token_code = token_code
        self.umid_token = umid_token
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authentication_code is not None:
            result['AuthenticationCode'] = self.authentication_code
        if self.available_features is not None:
            result['AvailableFeatures'] = self.available_features
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.client_name is not None:
            result['ClientName'] = self.client_name
        if self.client_os is not None:
            result['ClientOS'] = self.client_os
        if self.client_type is not None:
            result['ClientType'] = self.client_type
        if self.client_version is not None:
            result['ClientVersion'] = self.client_version
        if self.current_stage is not None:
            result['CurrentStage'] = self.current_stage
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.encrypted_finger_print_data is not None:
            result['EncryptedFingerPrintData'] = self.encrypted_finger_print_data
        if self.encrypted_key is not None:
            result['EncryptedKey'] = self.encrypted_key
        if self.encrypted_password is not None:
            result['EncryptedPassword'] = self.encrypted_password
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id
        if self.finger_print_data is not None:
            result['FingerPrintData'] = self.finger_print_data
        if self.idp_id is not None:
            result['IdpId'] = self.idp_id
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        if self.keep_alive is not None:
            result['KeepAlive'] = self.keep_alive
        if self.keep_alive_token is not None:
            result['KeepAliveToken'] = self.keep_alive_token
        if self.login_identifier is not None:
            result['LoginIdentifier'] = self.login_identifier
        if self.login_name is not None:
            result['LoginName'] = self.login_name
        if self.mfa_type is not None:
            result['MfaType'] = self.mfa_type
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        if self.new_password is not None:
            result['NewPassword'] = self.new_password
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.old_password is not None:
            result['OldPassword'] = self.old_password
        if self.password is not None:
            result['Password'] = self.password
        if self.phone is not None:
            result['Phone'] = self.phone
        if self.phone_verify_code is not None:
            result['PhoneVerifyCode'] = self.phone_verify_code
        if self.profile_region is not None:
            result['ProfileRegion'] = self.profile_region
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.sso_extends_cookies is not None:
            result['SsoExtendsCookies'] = self.sso_extends_cookies
        if self.sso_session_token is not None:
            result['SsoSessionToken'] = self.sso_session_token
        if self.token_code is not None:
            result['TokenCode'] = self.token_code
        if self.umid_token is not None:
            result['UmidToken'] = self.umid_token
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthenticationCode') is not None:
            self.authentication_code = m.get('AuthenticationCode')
        if m.get('AvailableFeatures') is not None:
            self.available_features = m.get('AvailableFeatures')
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('ClientName') is not None:
            self.client_name = m.get('ClientName')
        if m.get('ClientOS') is not None:
            self.client_os = m.get('ClientOS')
        if m.get('ClientType') is not None:
            self.client_type = m.get('ClientType')
        if m.get('ClientVersion') is not None:
            self.client_version = m.get('ClientVersion')
        if m.get('CurrentStage') is not None:
            self.current_stage = m.get('CurrentStage')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('EncryptedFingerPrintData') is not None:
            self.encrypted_finger_print_data = m.get('EncryptedFingerPrintData')
        if m.get('EncryptedKey') is not None:
            self.encrypted_key = m.get('EncryptedKey')
        if m.get('EncryptedPassword') is not None:
            self.encrypted_password = m.get('EncryptedPassword')
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        if m.get('FingerPrintData') is not None:
            self.finger_print_data = m.get('FingerPrintData')
        if m.get('IdpId') is not None:
            self.idp_id = m.get('IdpId')
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        if m.get('KeepAlive') is not None:
            self.keep_alive = m.get('KeepAlive')
        if m.get('KeepAliveToken') is not None:
            self.keep_alive_token = m.get('KeepAliveToken')
        if m.get('LoginIdentifier') is not None:
            self.login_identifier = m.get('LoginIdentifier')
        if m.get('LoginName') is not None:
            self.login_name = m.get('LoginName')
        if m.get('MfaType') is not None:
            self.mfa_type = m.get('MfaType')
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
        if m.get('NewPassword') is not None:
            self.new_password = m.get('NewPassword')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('OldPassword') is not None:
            self.old_password = m.get('OldPassword')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('Phone') is not None:
            self.phone = m.get('Phone')
        if m.get('PhoneVerifyCode') is not None:
            self.phone_verify_code = m.get('PhoneVerifyCode')
        if m.get('ProfileRegion') is not None:
            self.profile_region = m.get('ProfileRegion')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('SsoExtendsCookies') is not None:
            self.sso_extends_cookies = m.get('SsoExtendsCookies')
        if m.get('SsoSessionToken') is not None:
            self.sso_session_token = m.get('SsoSessionToken')
        if m.get('TokenCode') is not None:
            self.token_code = m.get('TokenCode')
        if m.get('UmidToken') is not None:
            self.umid_token = m.get('UmidToken')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class GetLoginTokenShrinkRequest(TeaModel):
    def __init__(
        self,
        authentication_code: str = None,
        available_features_shrink: str = None,
        client_id: str = None,
        client_name: str = None,
        client_os: str = None,
        client_type: str = None,
        client_version: str = None,
        current_stage: str = None,
        directory_id: str = None,
        encrypted_finger_print_data: str = None,
        encrypted_key: str = None,
        encrypted_password: str = None,
        end_user_id: str = None,
        finger_print_data: str = None,
        idp_id: str = None,
        image_url: str = None,
        keep_alive: bool = None,
        keep_alive_token: str = None,
        login_identifier: str = None,
        login_name: str = None,
        mfa_type: str = None,
        network_type: str = None,
        new_password: str = None,
        office_site_id: str = None,
        old_password: str = None,
        password: str = None,
        phone: str = None,
        phone_verify_code: str = None,
        profile_region: str = None,
        region_id: str = None,
        session_id: str = None,
        sso_extends_cookies: str = None,
        sso_session_token: str = None,
        token_code: str = None,
        umid_token: str = None,
        uuid: str = None,
    ):
        self.authentication_code = authentication_code
        self.available_features_shrink = available_features_shrink
        # This parameter is required.
        self.client_id = client_id
        self.client_name = client_name
        self.client_os = client_os
        self.client_type = client_type
        self.client_version = client_version
        self.current_stage = current_stage
        self.directory_id = directory_id
        self.encrypted_finger_print_data = encrypted_finger_print_data
        self.encrypted_key = encrypted_key
        self.encrypted_password = encrypted_password
        self.end_user_id = end_user_id
        self.finger_print_data = finger_print_data
        self.idp_id = idp_id
        self.image_url = image_url
        self.keep_alive = keep_alive
        self.keep_alive_token = keep_alive_token
        self.login_identifier = login_identifier
        self.login_name = login_name
        self.mfa_type = mfa_type
        self.network_type = network_type
        self.new_password = new_password
        self.office_site_id = office_site_id
        self.old_password = old_password
        self.password = password
        self.phone = phone
        self.phone_verify_code = phone_verify_code
        self.profile_region = profile_region
        self.region_id = region_id
        self.session_id = session_id
        self.sso_extends_cookies = sso_extends_cookies
        self.sso_session_token = sso_session_token
        self.token_code = token_code
        self.umid_token = umid_token
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authentication_code is not None:
            result['AuthenticationCode'] = self.authentication_code
        if self.available_features_shrink is not None:
            result['AvailableFeatures'] = self.available_features_shrink
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.client_name is not None:
            result['ClientName'] = self.client_name
        if self.client_os is not None:
            result['ClientOS'] = self.client_os
        if self.client_type is not None:
            result['ClientType'] = self.client_type
        if self.client_version is not None:
            result['ClientVersion'] = self.client_version
        if self.current_stage is not None:
            result['CurrentStage'] = self.current_stage
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.encrypted_finger_print_data is not None:
            result['EncryptedFingerPrintData'] = self.encrypted_finger_print_data
        if self.encrypted_key is not None:
            result['EncryptedKey'] = self.encrypted_key
        if self.encrypted_password is not None:
            result['EncryptedPassword'] = self.encrypted_password
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id
        if self.finger_print_data is not None:
            result['FingerPrintData'] = self.finger_print_data
        if self.idp_id is not None:
            result['IdpId'] = self.idp_id
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        if self.keep_alive is not None:
            result['KeepAlive'] = self.keep_alive
        if self.keep_alive_token is not None:
            result['KeepAliveToken'] = self.keep_alive_token
        if self.login_identifier is not None:
            result['LoginIdentifier'] = self.login_identifier
        if self.login_name is not None:
            result['LoginName'] = self.login_name
        if self.mfa_type is not None:
            result['MfaType'] = self.mfa_type
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        if self.new_password is not None:
            result['NewPassword'] = self.new_password
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.old_password is not None:
            result['OldPassword'] = self.old_password
        if self.password is not None:
            result['Password'] = self.password
        if self.phone is not None:
            result['Phone'] = self.phone
        if self.phone_verify_code is not None:
            result['PhoneVerifyCode'] = self.phone_verify_code
        if self.profile_region is not None:
            result['ProfileRegion'] = self.profile_region
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.sso_extends_cookies is not None:
            result['SsoExtendsCookies'] = self.sso_extends_cookies
        if self.sso_session_token is not None:
            result['SsoSessionToken'] = self.sso_session_token
        if self.token_code is not None:
            result['TokenCode'] = self.token_code
        if self.umid_token is not None:
            result['UmidToken'] = self.umid_token
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthenticationCode') is not None:
            self.authentication_code = m.get('AuthenticationCode')
        if m.get('AvailableFeatures') is not None:
            self.available_features_shrink = m.get('AvailableFeatures')
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('ClientName') is not None:
            self.client_name = m.get('ClientName')
        if m.get('ClientOS') is not None:
            self.client_os = m.get('ClientOS')
        if m.get('ClientType') is not None:
            self.client_type = m.get('ClientType')
        if m.get('ClientVersion') is not None:
            self.client_version = m.get('ClientVersion')
        if m.get('CurrentStage') is not None:
            self.current_stage = m.get('CurrentStage')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('EncryptedFingerPrintData') is not None:
            self.encrypted_finger_print_data = m.get('EncryptedFingerPrintData')
        if m.get('EncryptedKey') is not None:
            self.encrypted_key = m.get('EncryptedKey')
        if m.get('EncryptedPassword') is not None:
            self.encrypted_password = m.get('EncryptedPassword')
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        if m.get('FingerPrintData') is not None:
            self.finger_print_data = m.get('FingerPrintData')
        if m.get('IdpId') is not None:
            self.idp_id = m.get('IdpId')
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        if m.get('KeepAlive') is not None:
            self.keep_alive = m.get('KeepAlive')
        if m.get('KeepAliveToken') is not None:
            self.keep_alive_token = m.get('KeepAliveToken')
        if m.get('LoginIdentifier') is not None:
            self.login_identifier = m.get('LoginIdentifier')
        if m.get('LoginName') is not None:
            self.login_name = m.get('LoginName')
        if m.get('MfaType') is not None:
            self.mfa_type = m.get('MfaType')
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
        if m.get('NewPassword') is not None:
            self.new_password = m.get('NewPassword')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('OldPassword') is not None:
            self.old_password = m.get('OldPassword')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('Phone') is not None:
            self.phone = m.get('Phone')
        if m.get('PhoneVerifyCode') is not None:
            self.phone_verify_code = m.get('PhoneVerifyCode')
        if m.get('ProfileRegion') is not None:
            self.profile_region = m.get('ProfileRegion')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('SsoExtendsCookies') is not None:
            self.sso_extends_cookies = m.get('SsoExtendsCookies')
        if m.get('SsoSessionToken') is not None:
            self.sso_session_token = m.get('SsoSessionToken')
        if m.get('TokenCode') is not None:
            self.token_code = m.get('TokenCode')
        if m.get('UmidToken') is not None:
            self.umid_token = m.get('UmidToken')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class GetLoginTokenResponseBodyMfaTypeList(TeaModel):
    def __init__(
        self,
        name: str = None,
        stage: str = None,
    ):
        self.name = name
        self.stage = stage

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.stage is not None:
            result['Stage'] = self.stage
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Stage') is not None:
            self.stage = m.get('Stage')
        return self


class GetLoginTokenResponseBodyPasswordStrategy(TeaModel):
    def __init__(
        self,
        tenant_alternative_chars: List[str] = None,
        tenant_password_length: int = None,
    ):
        self.tenant_alternative_chars = tenant_alternative_chars
        self.tenant_password_length = tenant_password_length

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tenant_alternative_chars is not None:
            result['TenantAlternativeChars'] = self.tenant_alternative_chars
        if self.tenant_password_length is not None:
            result['TenantPasswordLength'] = self.tenant_password_length
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TenantAlternativeChars') is not None:
            self.tenant_alternative_chars = m.get('TenantAlternativeChars')
        if m.get('TenantPasswordLength') is not None:
            self.tenant_password_length = m.get('TenantPasswordLength')
        return self


class GetLoginTokenResponseBodyRiskVerifyInfo(TeaModel):
    def __init__(
        self,
        email: str = None,
        last_lock_duration: int = None,
        locked: bool = None,
        phone: str = None,
    ):
        self.email = email
        self.last_lock_duration = last_lock_duration
        self.locked = locked
        self.phone = phone

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.email is not None:
            result['Email'] = self.email
        if self.last_lock_duration is not None:
            result['LastLockDuration'] = self.last_lock_duration
        if self.locked is not None:
            result['Locked'] = self.locked
        if self.phone is not None:
            result['Phone'] = self.phone
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('LastLockDuration') is not None:
            self.last_lock_duration = m.get('LastLockDuration')
        if m.get('Locked') is not None:
            self.locked = m.get('Locked')
        if m.get('Phone') is not None:
            self.phone = m.get('Phone')
        return self


class GetLoginTokenResponseBodyTenantInfos(TeaModel):
    def __init__(
        self,
        access_type: str = None,
        tenant_alias: str = None,
    ):
        self.access_type = access_type
        self.tenant_alias = tenant_alias

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_type is not None:
            result['AccessType'] = self.access_type
        if self.tenant_alias is not None:
            result['TenantAlias'] = self.tenant_alias
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessType') is not None:
            self.access_type = m.get('AccessType')
        if m.get('TenantAlias') is not None:
            self.tenant_alias = m.get('TenantAlias')
        return self


class GetLoginTokenResponseBody(TeaModel):
    def __init__(
        self,
        access_type: str = None,
        account_type: str = None,
        ad_domain: str = None,
        email: str = None,
        end_user_id: str = None,
        idp_id: str = None,
        industry: str = None,
        keep_alive_token: str = None,
        label: str = None,
        login_token: str = None,
        mfa_type_list: List[GetLoginTokenResponseBodyMfaTypeList] = None,
        next_stage: str = None,
        nick_name: str = None,
        office_sites: List[str] = None,
        password_strategy: GetLoginTokenResponseBodyPasswordStrategy = None,
        phone: str = None,
        props: Dict[str, str] = None,
        qr_code_png: str = None,
        reason: str = None,
        request_id: str = None,
        risk_verify_info: GetLoginTokenResponseBodyRiskVerifyInfo = None,
        secret: str = None,
        session_id: str = None,
        tenant_alias: str = None,
        tenant_id: int = None,
        tenant_infos: List[GetLoginTokenResponseBodyTenantInfos] = None,
        vpc_region_id: str = None,
        window_display_mode: str = None,
        wy_id: str = None,
    ):
        self.access_type = access_type
        self.account_type = account_type
        self.ad_domain = ad_domain
        self.email = email
        self.end_user_id = end_user_id
        self.idp_id = idp_id
        self.industry = industry
        self.keep_alive_token = keep_alive_token
        self.label = label
        self.login_token = login_token
        self.mfa_type_list = mfa_type_list
        self.next_stage = next_stage
        self.nick_name = nick_name
        self.office_sites = office_sites
        self.password_strategy = password_strategy
        self.phone = phone
        self.props = props
        self.qr_code_png = qr_code_png
        self.reason = reason
        self.request_id = request_id
        self.risk_verify_info = risk_verify_info
        self.secret = secret
        self.session_id = session_id
        self.tenant_alias = tenant_alias
        self.tenant_id = tenant_id
        self.tenant_infos = tenant_infos
        self.vpc_region_id = vpc_region_id
        self.window_display_mode = window_display_mode
        self.wy_id = wy_id

    def validate(self):
        if self.mfa_type_list:
            for k in self.mfa_type_list:
                if k:
                    k.validate()
        if self.password_strategy:
            self.password_strategy.validate()
        if self.risk_verify_info:
            self.risk_verify_info.validate()
        if self.tenant_infos:
            for k in self.tenant_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_type is not None:
            result['AccessType'] = self.access_type
        if self.account_type is not None:
            result['AccountType'] = self.account_type
        if self.ad_domain is not None:
            result['AdDomain'] = self.ad_domain
        if self.email is not None:
            result['Email'] = self.email
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id
        if self.idp_id is not None:
            result['IdpId'] = self.idp_id
        if self.industry is not None:
            result['Industry'] = self.industry
        if self.keep_alive_token is not None:
            result['KeepAliveToken'] = self.keep_alive_token
        if self.label is not None:
            result['Label'] = self.label
        if self.login_token is not None:
            result['LoginToken'] = self.login_token
        result['MfaTypeList'] = []
        if self.mfa_type_list is not None:
            for k in self.mfa_type_list:
                result['MfaTypeList'].append(k.to_map() if k else None)
        if self.next_stage is not None:
            result['NextStage'] = self.next_stage
        if self.nick_name is not None:
            result['NickName'] = self.nick_name
        if self.office_sites is not None:
            result['OfficeSites'] = self.office_sites
        if self.password_strategy is not None:
            result['PasswordStrategy'] = self.password_strategy.to_map()
        if self.phone is not None:
            result['Phone'] = self.phone
        if self.props is not None:
            result['Props'] = self.props
        if self.qr_code_png is not None:
            result['QrCodePng'] = self.qr_code_png
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.risk_verify_info is not None:
            result['RiskVerifyInfo'] = self.risk_verify_info.to_map()
        if self.secret is not None:
            result['Secret'] = self.secret
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.tenant_alias is not None:
            result['TenantAlias'] = self.tenant_alias
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        result['TenantInfos'] = []
        if self.tenant_infos is not None:
            for k in self.tenant_infos:
                result['TenantInfos'].append(k.to_map() if k else None)
        if self.vpc_region_id is not None:
            result['VpcRegionId'] = self.vpc_region_id
        if self.window_display_mode is not None:
            result['WindowDisplayMode'] = self.window_display_mode
        if self.wy_id is not None:
            result['WyId'] = self.wy_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessType') is not None:
            self.access_type = m.get('AccessType')
        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')
        if m.get('AdDomain') is not None:
            self.ad_domain = m.get('AdDomain')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        if m.get('IdpId') is not None:
            self.idp_id = m.get('IdpId')
        if m.get('Industry') is not None:
            self.industry = m.get('Industry')
        if m.get('KeepAliveToken') is not None:
            self.keep_alive_token = m.get('KeepAliveToken')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('LoginToken') is not None:
            self.login_token = m.get('LoginToken')
        self.mfa_type_list = []
        if m.get('MfaTypeList') is not None:
            for k in m.get('MfaTypeList'):
                temp_model = GetLoginTokenResponseBodyMfaTypeList()
                self.mfa_type_list.append(temp_model.from_map(k))
        if m.get('NextStage') is not None:
            self.next_stage = m.get('NextStage')
        if m.get('NickName') is not None:
            self.nick_name = m.get('NickName')
        if m.get('OfficeSites') is not None:
            self.office_sites = m.get('OfficeSites')
        if m.get('PasswordStrategy') is not None:
            temp_model = GetLoginTokenResponseBodyPasswordStrategy()
            self.password_strategy = temp_model.from_map(m['PasswordStrategy'])
        if m.get('Phone') is not None:
            self.phone = m.get('Phone')
        if m.get('Props') is not None:
            self.props = m.get('Props')
        if m.get('QrCodePng') is not None:
            self.qr_code_png = m.get('QrCodePng')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RiskVerifyInfo') is not None:
            temp_model = GetLoginTokenResponseBodyRiskVerifyInfo()
            self.risk_verify_info = temp_model.from_map(m['RiskVerifyInfo'])
        if m.get('Secret') is not None:
            self.secret = m.get('Secret')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('TenantAlias') is not None:
            self.tenant_alias = m.get('TenantAlias')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        self.tenant_infos = []
        if m.get('TenantInfos') is not None:
            for k in m.get('TenantInfos'):
                temp_model = GetLoginTokenResponseBodyTenantInfos()
                self.tenant_infos.append(temp_model.from_map(k))
        if m.get('VpcRegionId') is not None:
            self.vpc_region_id = m.get('VpcRegionId')
        if m.get('WindowDisplayMode') is not None:
            self.window_display_mode = m.get('WindowDisplayMode')
        if m.get('WyId') is not None:
            self.wy_id = m.get('WyId')
        return self


class GetLoginTokenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetLoginTokenResponseBody = None,
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
            temp_model = GetLoginTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetStsTokenRequest(TeaModel):
    def __init__(
        self,
        auth_code: str = None,
        client_id: str = None,
        client_ip: str = None,
        client_os: str = None,
        client_version: str = None,
        uuid: str = None,
    ):
        # This parameter is required.
        self.auth_code = auth_code
        self.client_id = client_id
        self.client_ip = client_ip
        self.client_os = client_os
        self.client_version = client_version
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_code is not None:
            result['AuthCode'] = self.auth_code
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.client_ip is not None:
            result['ClientIp'] = self.client_ip
        if self.client_os is not None:
            result['ClientOS'] = self.client_os
        if self.client_version is not None:
            result['ClientVersion'] = self.client_version
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthCode') is not None:
            self.auth_code = m.get('AuthCode')
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('ClientIp') is not None:
            self.client_ip = m.get('ClientIp')
        if m.get('ClientOS') is not None:
            self.client_os = m.get('ClientOS')
        if m.get('ClientVersion') is not None:
            self.client_version = m.get('ClientVersion')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class GetStsTokenResponseBodyStsTokenModel(TeaModel):
    def __init__(
        self,
        session_id: str = None,
        sts_token: str = None,
        tenant_id: int = None,
    ):
        self.session_id = session_id
        self.sts_token = sts_token
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.sts_token is not None:
            result['StsToken'] = self.sts_token
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('StsToken') is not None:
            self.sts_token = m.get('StsToken')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class GetStsTokenResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        sts_token_model: GetStsTokenResponseBodyStsTokenModel = None,
    ):
        self.request_id = request_id
        self.sts_token_model = sts_token_model

    def validate(self):
        if self.sts_token_model:
            self.sts_token_model.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sts_token_model is not None:
            result['StsTokenModel'] = self.sts_token_model.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StsTokenModel') is not None:
            temp_model = GetStsTokenResponseBodyStsTokenModel()
            self.sts_token_model = temp_model.from_map(m['StsTokenModel'])
        return self


class GetStsTokenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetStsTokenResponseBody = None,
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
            temp_model = GetStsTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RefreshLoginTokenRequest(TeaModel):
    def __init__(
        self,
        client_id: str = None,
        client_type: str = None,
        end_user_id: str = None,
        login_identifier: str = None,
        login_token: str = None,
        office_site_id: str = None,
        profile_region: str = None,
        session_id: str = None,
        uuid: str = None,
    ):
        # This parameter is required.
        self.client_id = client_id
        self.client_type = client_type
        self.end_user_id = end_user_id
        self.login_identifier = login_identifier
        # This parameter is required.
        self.login_token = login_token
        self.office_site_id = office_site_id
        self.profile_region = profile_region
        # This parameter is required.
        self.session_id = session_id
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.client_type is not None:
            result['ClientType'] = self.client_type
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id
        if self.login_identifier is not None:
            result['LoginIdentifier'] = self.login_identifier
        if self.login_token is not None:
            result['LoginToken'] = self.login_token
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.profile_region is not None:
            result['ProfileRegion'] = self.profile_region
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('ClientType') is not None:
            self.client_type = m.get('ClientType')
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        if m.get('LoginIdentifier') is not None:
            self.login_identifier = m.get('LoginIdentifier')
        if m.get('LoginToken') is not None:
            self.login_token = m.get('LoginToken')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('ProfileRegion') is not None:
            self.profile_region = m.get('ProfileRegion')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class RefreshLoginTokenResponseBody(TeaModel):
    def __init__(
        self,
        login_token: str = None,
        request_id: str = None,
    ):
        self.login_token = login_token
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.login_token is not None:
            result['LoginToken'] = self.login_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LoginToken') is not None:
            self.login_token = m.get('LoginToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RefreshLoginTokenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RefreshLoginTokenResponseBody = None,
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
            temp_model = RefreshLoginTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


