# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_csas20230120 import models as main_models
from darabonba.model import DaraModel

class GetIdpConfigResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetIdpConfigResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.GetIdpConfigResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetIdpConfigResponseBodyData(DaraModel):
    def __init__(
        self,
        access_key: str = None,
        access_key_secret: str = None,
        description: str = None,
        get_group_url: str = None,
        id: str = None,
        idp_metadata: str = None,
        mfa_config_type: str = None,
        mobile_login_type: str = None,
        mobile_mfa_config_type: str = None,
        multi_idp_info: str = None,
        name: str = None,
        pc_login_type: str = None,
        status: str = None,
        type: str = None,
        update_time: str = None,
        verify_aes_key: str = None,
        verify_token: str = None,
        verify_url: str = None,
    ):
        # AccessKey ID
        self.access_key = access_key
        # AccessKey Secret
        self.access_key_secret = access_key_secret
        self.description = description
        self.get_group_url = get_group_url
        self.id = id
        self.idp_metadata = idp_metadata
        self.mfa_config_type = mfa_config_type
        self.mobile_login_type = mobile_login_type
        self.mobile_mfa_config_type = mobile_mfa_config_type
        self.multi_idp_info = multi_idp_info
        self.name = name
        self.pc_login_type = pc_login_type
        self.status = status
        self.type = type
        self.update_time = update_time
        self.verify_aes_key = verify_aes_key
        self.verify_token = verify_token
        self.verify_url = verify_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_key is not None:
            result['AccessKey'] = self.access_key

        if self.access_key_secret is not None:
            result['AccessKeySecret'] = self.access_key_secret

        if self.description is not None:
            result['Description'] = self.description

        if self.get_group_url is not None:
            result['GetGroupUrl'] = self.get_group_url

        if self.id is not None:
            result['Id'] = self.id

        if self.idp_metadata is not None:
            result['IdpMetadata'] = self.idp_metadata

        if self.mfa_config_type is not None:
            result['MfaConfigType'] = self.mfa_config_type

        if self.mobile_login_type is not None:
            result['MobileLoginType'] = self.mobile_login_type

        if self.mobile_mfa_config_type is not None:
            result['MobileMfaConfigType'] = self.mobile_mfa_config_type

        if self.multi_idp_info is not None:
            result['MultiIdpInfo'] = self.multi_idp_info

        if self.name is not None:
            result['Name'] = self.name

        if self.pc_login_type is not None:
            result['PcLoginType'] = self.pc_login_type

        if self.status is not None:
            result['Status'] = self.status

        if self.type is not None:
            result['Type'] = self.type

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.verify_aes_key is not None:
            result['VerifyAesKey'] = self.verify_aes_key

        if self.verify_token is not None:
            result['VerifyToken'] = self.verify_token

        if self.verify_url is not None:
            result['VerifyUrl'] = self.verify_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessKey') is not None:
            self.access_key = m.get('AccessKey')

        if m.get('AccessKeySecret') is not None:
            self.access_key_secret = m.get('AccessKeySecret')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('GetGroupUrl') is not None:
            self.get_group_url = m.get('GetGroupUrl')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('IdpMetadata') is not None:
            self.idp_metadata = m.get('IdpMetadata')

        if m.get('MfaConfigType') is not None:
            self.mfa_config_type = m.get('MfaConfigType')

        if m.get('MobileLoginType') is not None:
            self.mobile_login_type = m.get('MobileLoginType')

        if m.get('MobileMfaConfigType') is not None:
            self.mobile_mfa_config_type = m.get('MobileMfaConfigType')

        if m.get('MultiIdpInfo') is not None:
            self.multi_idp_info = m.get('MultiIdpInfo')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PcLoginType') is not None:
            self.pc_login_type = m.get('PcLoginType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('VerifyAesKey') is not None:
            self.verify_aes_key = m.get('VerifyAesKey')

        if m.get('VerifyToken') is not None:
            self.verify_token = m.get('VerifyToken')

        if m.get('VerifyUrl') is not None:
            self.verify_url = m.get('VerifyUrl')

        return self

