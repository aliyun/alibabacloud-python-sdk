# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class SetWebAuthnConfigurationRequest(DaraModel):
    def __init__(
        self,
        aaguids: List[main_models.SetWebAuthnConfigurationRequestAaguids] = None,
        enable_aaguid_verification: bool = None,
        enable_metadata_service_verification: bool = None,
        enable_user_self_registration: bool = None,
        instance_id: str = None,
    ):
        # AAGUID及其名称列表
        self.aaguids = aaguids
        # 是否开启AAGUID校验
        self.enable_aaguid_verification = enable_aaguid_verification
        # 是否开启WebAuthn认证器MDS校验
        self.enable_metadata_service_verification = enable_metadata_service_verification
        # 是否允许用户自注册WebAuthn认证器
        # 
        # This parameter is required.
        self.enable_user_self_registration = enable_user_self_registration
        # IDaaS EIAM实例的ID。
        # 
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        if self.aaguids:
            for v1 in self.aaguids:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Aaguids'] = []
        if self.aaguids is not None:
            for k1 in self.aaguids:
                result['Aaguids'].append(k1.to_map() if k1 else None)

        if self.enable_aaguid_verification is not None:
            result['EnableAaguidVerification'] = self.enable_aaguid_verification

        if self.enable_metadata_service_verification is not None:
            result['EnableMetadataServiceVerification'] = self.enable_metadata_service_verification

        if self.enable_user_self_registration is not None:
            result['EnableUserSelfRegistration'] = self.enable_user_self_registration

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.aaguids = []
        if m.get('Aaguids') is not None:
            for k1 in m.get('Aaguids'):
                temp_model = main_models.SetWebAuthnConfigurationRequestAaguids()
                self.aaguids.append(temp_model.from_map(k1))

        if m.get('EnableAaguidVerification') is not None:
            self.enable_aaguid_verification = m.get('EnableAaguidVerification')

        if m.get('EnableMetadataServiceVerification') is not None:
            self.enable_metadata_service_verification = m.get('EnableMetadataServiceVerification')

        if m.get('EnableUserSelfRegistration') is not None:
            self.enable_user_self_registration = m.get('EnableUserSelfRegistration')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

class SetWebAuthnConfigurationRequestAaguids(DaraModel):
    def __init__(
        self,
        aaguid: str = None,
        name: str = None,
    ):
        # AAGUID
        self.aaguid = aaguid
        # AAGUID名称
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aaguid is not None:
            result['Aaguid'] = self.aaguid

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Aaguid') is not None:
            self.aaguid = m.get('Aaguid')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

