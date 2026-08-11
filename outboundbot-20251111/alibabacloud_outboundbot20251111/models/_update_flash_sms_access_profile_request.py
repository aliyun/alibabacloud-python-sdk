# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_outboundbot20251111 import models as main_models
from darabonba.model import DaraModel

class UpdateFlashSmsAccessProfileRequest(DaraModel):
    def __init__(
        self,
        access_profile: main_models.UpdateFlashSmsAccessProfileRequestAccessProfile = None,
        access_profile_id: str = None,
        instance_id: str = None,
        provider_id: str = None,
    ):
        # The access configuration.
        self.access_profile = access_profile
        # The access configuration ID.
        self.access_profile_id = access_profile_id
        # The instance ID.
        self.instance_id = instance_id
        # The provider ID. Valid values:
        # - Uincall: Beijing Youyin Communication Co., Ltd.
        # - ChuangLan: Beijing Chuanglan Cloud Intelligence Information Co., Ltd.
        # - ChinaMobile: China Mobile.
        # - ShangHaiTianNan: Shanghai Tiannan.
        # - HeDao: Galaxis.
        # - DySms: Alibaba Communication.
        self.provider_id = provider_id

    def validate(self):
        if self.access_profile:
            self.access_profile.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_profile is not None:
            result['AccessProfile'] = self.access_profile.to_map()

        if self.access_profile_id is not None:
            result['AccessProfileId'] = self.access_profile_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.provider_id is not None:
            result['ProviderId'] = self.provider_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessProfile') is not None:
            temp_model = main_models.UpdateFlashSmsAccessProfileRequestAccessProfile()
            self.access_profile = temp_model.from_map(m.get('AccessProfile'))

        if m.get('AccessProfileId') is not None:
            self.access_profile_id = m.get('AccessProfileId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('ProviderId') is not None:
            self.provider_id = m.get('ProviderId')

        return self

class UpdateFlashSmsAccessProfileRequestAccessProfile(DaraModel):
    def __init__(
        self,
        account: str = None,
        aes_key: str = None,
        api_account: str = None,
        api_id: str = None,
        api_key: str = None,
        api_password: str = None,
        cap_app_id: str = None,
        dy_sms_access_profiles: List[main_models.UpdateFlashSmsAccessProfileRequestAccessProfileDySmsAccessProfiles] = None,
        extno: str = None,
        management_password: str = None,
        management_sub_user_id: str = None,
        management_username: str = None,
        password: str = None,
        pwd: str = None,
        user: str = None,
        user_name: str = None,
    ):
        # Required when ProviderId is set to ShangHaiTianNan or Uincall.
        self.account = account
        # Required when ProviderId is set to ChinaMobile.
        self.aes_key = aes_key
        # Required when ProviderId is set to ChuangLan.
        self.api_account = api_account
        # Required when ProviderId is set to ChinaMobile.
        self.api_id = api_id
        # Required when ProviderId is set to ChinaMobile.
        self.api_key = api_key
        # Required when ProviderId is set to ChuangLan.
        self.api_password = api_password
        # Required when ProviderId is set to ChinaMobile.
        self.cap_app_id = cap_app_id
        # The list of Alibaba Communication configurations. Required when ProviderId is set to DySms.
        self.dy_sms_access_profiles = dy_sms_access_profiles
        # Required when ProviderId is set to ShangHaiTianNan.
        self.extno = extno
        # Required when ProviderId is set to ChuangLan.
        self.management_password = management_password
        # Required when ProviderId is set to ChuangLan.
        self.management_sub_user_id = management_sub_user_id
        # Required when ProviderId is set to ChuangLan.
        self.management_username = management_username
        # Required when ProviderId is set to ShangHaiTianNan or HeDao.
        self.password = password
        # Required when ProviderId is set to Uincall.
        self.pwd = pwd
        # Required when ProviderId is set to Uincall.
        self.user = user
        # Required when ProviderId is set to HeDao.
        self.user_name = user_name

    def validate(self):
        if self.dy_sms_access_profiles:
            for v1 in self.dy_sms_access_profiles:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account is not None:
            result['Account'] = self.account

        if self.aes_key is not None:
            result['AesKey'] = self.aes_key

        if self.api_account is not None:
            result['ApiAccount'] = self.api_account

        if self.api_id is not None:
            result['ApiId'] = self.api_id

        if self.api_key is not None:
            result['ApiKey'] = self.api_key

        if self.api_password is not None:
            result['ApiPassword'] = self.api_password

        if self.cap_app_id is not None:
            result['CapAppId'] = self.cap_app_id

        result['DySmsAccessProfiles'] = []
        if self.dy_sms_access_profiles is not None:
            for k1 in self.dy_sms_access_profiles:
                result['DySmsAccessProfiles'].append(k1.to_map() if k1 else None)

        if self.extno is not None:
            result['Extno'] = self.extno

        if self.management_password is not None:
            result['ManagementPassword'] = self.management_password

        if self.management_sub_user_id is not None:
            result['ManagementSubUserId'] = self.management_sub_user_id

        if self.management_username is not None:
            result['ManagementUsername'] = self.management_username

        if self.password is not None:
            result['Password'] = self.password

        if self.pwd is not None:
            result['Pwd'] = self.pwd

        if self.user is not None:
            result['User'] = self.user

        if self.user_name is not None:
            result['UserName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Account') is not None:
            self.account = m.get('Account')

        if m.get('AesKey') is not None:
            self.aes_key = m.get('AesKey')

        if m.get('ApiAccount') is not None:
            self.api_account = m.get('ApiAccount')

        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')

        if m.get('ApiKey') is not None:
            self.api_key = m.get('ApiKey')

        if m.get('ApiPassword') is not None:
            self.api_password = m.get('ApiPassword')

        if m.get('CapAppId') is not None:
            self.cap_app_id = m.get('CapAppId')

        self.dy_sms_access_profiles = []
        if m.get('DySmsAccessProfiles') is not None:
            for k1 in m.get('DySmsAccessProfiles'):
                temp_model = main_models.UpdateFlashSmsAccessProfileRequestAccessProfileDySmsAccessProfiles()
                self.dy_sms_access_profiles.append(temp_model.from_map(k1))

        if m.get('Extno') is not None:
            self.extno = m.get('Extno')

        if m.get('ManagementPassword') is not None:
            self.management_password = m.get('ManagementPassword')

        if m.get('ManagementSubUserId') is not None:
            self.management_sub_user_id = m.get('ManagementSubUserId')

        if m.get('ManagementUsername') is not None:
            self.management_username = m.get('ManagementUsername')

        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('Pwd') is not None:
            self.pwd = m.get('Pwd')

        if m.get('User') is not None:
            self.user = m.get('User')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        return self

class UpdateFlashSmsAccessProfileRequestAccessProfileDySmsAccessProfiles(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        sign_name: str = None,
        template_code: str = None,
    ):
        # The template content.
        self.description = description
        # The template name.
        self.name = name
        # The signature name.
        self.sign_name = sign_name
        # The template code.
        self.template_code = template_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.sign_name is not None:
            result['SignName'] = self.sign_name

        if self.template_code is not None:
            result['TemplateCode'] = self.template_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('SignName') is not None:
            self.sign_name = m.get('SignName')

        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')

        return self

