# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateVerifySchemeRequest(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        auth_type: str = None,
        bundle_id: str = None,
        cm_api_code: int = None,
        ct_api_code: int = None,
        cu_api_code: int = None,
        email: str = None,
        hm_app_identifier: str = None,
        hm_package_name: str = None,
        hm_sign_name: str = None,
        ip_white_list: str = None,
        origin: str = None,
        os_type: str = None,
        owner_id: int = None,
        pack_name: str = None,
        pack_sign: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        scene_type: str = None,
        scheme_name: str = None,
        sms_sign_name: str = None,
        url: str = None,
    ):
        # This parameter is required.
        self.app_name = app_name
        self.auth_type = auth_type
        self.bundle_id = bundle_id
        self.cm_api_code = cm_api_code
        self.ct_api_code = ct_api_code
        self.cu_api_code = cu_api_code
        self.email = email
        self.hm_app_identifier = hm_app_identifier
        self.hm_package_name = hm_package_name
        self.hm_sign_name = hm_sign_name
        self.ip_white_list = ip_white_list
        self.origin = origin
        # This parameter is required.
        self.os_type = os_type
        self.owner_id = owner_id
        self.pack_name = pack_name
        self.pack_sign = pack_sign
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.scene_type = scene_type
        # This parameter is required.
        self.scheme_name = scheme_name
        self.sms_sign_name = sms_sign_name
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.auth_type is not None:
            result['AuthType'] = self.auth_type

        if self.bundle_id is not None:
            result['BundleId'] = self.bundle_id

        if self.cm_api_code is not None:
            result['CmApiCode'] = self.cm_api_code

        if self.ct_api_code is not None:
            result['CtApiCode'] = self.ct_api_code

        if self.cu_api_code is not None:
            result['CuApiCode'] = self.cu_api_code

        if self.email is not None:
            result['Email'] = self.email

        if self.hm_app_identifier is not None:
            result['HmAppIdentifier'] = self.hm_app_identifier

        if self.hm_package_name is not None:
            result['HmPackageName'] = self.hm_package_name

        if self.hm_sign_name is not None:
            result['HmSignName'] = self.hm_sign_name

        if self.ip_white_list is not None:
            result['IpWhiteList'] = self.ip_white_list

        if self.origin is not None:
            result['Origin'] = self.origin

        if self.os_type is not None:
            result['OsType'] = self.os_type

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.pack_name is not None:
            result['PackName'] = self.pack_name

        if self.pack_sign is not None:
            result['PackSign'] = self.pack_sign

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.scene_type is not None:
            result['SceneType'] = self.scene_type

        if self.scheme_name is not None:
            result['SchemeName'] = self.scheme_name

        if self.sms_sign_name is not None:
            result['SmsSignName'] = self.sms_sign_name

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('AuthType') is not None:
            self.auth_type = m.get('AuthType')

        if m.get('BundleId') is not None:
            self.bundle_id = m.get('BundleId')

        if m.get('CmApiCode') is not None:
            self.cm_api_code = m.get('CmApiCode')

        if m.get('CtApiCode') is not None:
            self.ct_api_code = m.get('CtApiCode')

        if m.get('CuApiCode') is not None:
            self.cu_api_code = m.get('CuApiCode')

        if m.get('Email') is not None:
            self.email = m.get('Email')

        if m.get('HmAppIdentifier') is not None:
            self.hm_app_identifier = m.get('HmAppIdentifier')

        if m.get('HmPackageName') is not None:
            self.hm_package_name = m.get('HmPackageName')

        if m.get('HmSignName') is not None:
            self.hm_sign_name = m.get('HmSignName')

        if m.get('IpWhiteList') is not None:
            self.ip_white_list = m.get('IpWhiteList')

        if m.get('Origin') is not None:
            self.origin = m.get('Origin')

        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PackName') is not None:
            self.pack_name = m.get('PackName')

        if m.get('PackSign') is not None:
            self.pack_sign = m.get('PackSign')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SceneType') is not None:
            self.scene_type = m.get('SceneType')

        if m.get('SchemeName') is not None:
            self.scheme_name = m.get('SchemeName')

        if m.get('SmsSignName') is not None:
            self.sms_sign_name = m.get('SmsSignName')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

