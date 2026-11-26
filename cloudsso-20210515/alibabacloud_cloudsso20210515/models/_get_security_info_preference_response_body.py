# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cloudsso20210515 import models as main_models
from darabonba.model import DaraModel

class GetSecurityInfoPreferenceResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        security_info_preference: main_models.GetSecurityInfoPreferenceResponseBodySecurityInfoPreference = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The security information management preferences.
        self.security_info_preference = security_info_preference

    def validate(self):
        if self.security_info_preference:
            self.security_info_preference.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.security_info_preference is not None:
            result['SecurityInfoPreference'] = self.security_info_preference.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SecurityInfoPreference') is not None:
            temp_model = main_models.GetSecurityInfoPreferenceResponseBodySecurityInfoPreference()
            self.security_info_preference = temp_model.from_map(m.get('SecurityInfoPreference'))

        return self

class GetSecurityInfoPreferenceResponseBodySecurityInfoPreference(DaraModel):
    def __init__(
        self,
        allow_user_manage_security_email: bool = None,
    ):
        # Indicates whether CloudSSO users in the directory are allowed to manage their security email addresses in the CloudSSO user portal. Valid values:
        # 
        # - true: Allowed.
        # - false: Not allowed. This is the default value.
        self.allow_user_manage_security_email = allow_user_manage_security_email

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allow_user_manage_security_email is not None:
            result['AllowUserManageSecurityEmail'] = self.allow_user_manage_security_email

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowUserManageSecurityEmail') is not None:
            self.allow_user_manage_security_email = m.get('AllowUserManageSecurityEmail')

        return self

