# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cloudsso20210515 import models as main_models
from darabonba.model import DaraModel

class GetLoginPreferenceResponseBody(DaraModel):
    def __init__(
        self,
        login_preference: main_models.GetLoginPreferenceResponseBodyLoginPreference = None,
        request_id: str = None,
    ):
        # The logon preference.
        self.login_preference = login_preference
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.login_preference:
            self.login_preference.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.login_preference is not None:
            result['LoginPreference'] = self.login_preference.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LoginPreference') is not None:
            temp_model = main_models.GetLoginPreferenceResponseBodyLoginPreference()
            self.login_preference = temp_model.from_map(m.get('LoginPreference'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetLoginPreferenceResponseBodyLoginPreference(DaraModel):
    def __init__(
        self,
        allow_user_to_get_credentials: bool = None,
        login_network_masks: str = None,
    ):
        # Indicates whether a user can obtain the application access credential after logon to the portal. Valid values:
        # 
        # *   True
        # *   False (default)
        self.allow_user_to_get_credentials = allow_user_to_get_credentials
        # The IP address whitelist. CloudSSO users can log on to the CloudSSO user portal only by using the IP addresses in the whitelist.
        # 
        # The IP address whitelist takes effect only on CloudSSO users who want to log on to the CloudSSO user portal by using the username-password logon or single sign-on (SSO) method. The IP address whitelist does not take effect on CloudSSO users who access accounts in a resource directory from the CloudSSO user portal.
        # 
        # If the return value of this parameter is empty, no IP address whitelists are configured.
        self.login_network_masks = login_network_masks

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allow_user_to_get_credentials is not None:
            result['AllowUserToGetCredentials'] = self.allow_user_to_get_credentials

        if self.login_network_masks is not None:
            result['LoginNetworkMasks'] = self.login_network_masks

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowUserToGetCredentials') is not None:
            self.allow_user_to_get_credentials = m.get('AllowUserToGetCredentials')

        if m.get('LoginNetworkMasks') is not None:
            self.login_network_masks = m.get('LoginNetworkMasks')

        return self

