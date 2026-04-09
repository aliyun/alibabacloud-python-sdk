# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetLoginTokenShrinkRequest(DaraModel):
    def __init__(
        self,
        area_site: str = None,
        authentication_code: str = None,
        available_features_shrink: str = None,
        channel: str = None,
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
        self.area_site = area_site
        self.authentication_code = authentication_code
        self.available_features_shrink = available_features_shrink
        self.channel = channel
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
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.area_site is not None:
            result['AreaSite'] = self.area_site

        if self.authentication_code is not None:
            result['AuthenticationCode'] = self.authentication_code

        if self.available_features_shrink is not None:
            result['AvailableFeatures'] = self.available_features_shrink

        if self.channel is not None:
            result['Channel'] = self.channel

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
        if m.get('AreaSite') is not None:
            self.area_site = m.get('AreaSite')

        if m.get('AuthenticationCode') is not None:
            self.authentication_code = m.get('AuthenticationCode')

        if m.get('AvailableFeatures') is not None:
            self.available_features_shrink = m.get('AvailableFeatures')

        if m.get('Channel') is not None:
            self.channel = m.get('Channel')

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

