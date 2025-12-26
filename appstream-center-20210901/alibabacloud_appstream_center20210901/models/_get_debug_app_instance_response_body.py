# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetDebugAppInstanceResponseBody(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        app_instance_group_id: str = None,
        app_instance_id: str = None,
        app_version: str = None,
        auth_code: str = None,
        request_id: str = None,
        user_id: str = None,
    ):
        # The application ID.
        self.app_id = app_id
        # The ID of the delivery group.
        self.app_instance_group_id = app_instance_group_id
        # The ID of the application instance.
        self.app_instance_id = app_instance_id
        # The ID of the application version.
        self.app_version = app_version
        # The authorization code. This authorization code is valid for 3 minutes and can be used only once, regardless of whether the authentication succeeds. If multiple authentication codes are generated for a user, only the latest authentication code takes effect.
        self.auth_code = auth_code
        # The request ID.
        self.request_id = request_id
        # The user ID.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id

        if self.app_instance_id is not None:
            result['AppInstanceId'] = self.app_instance_id

        if self.app_version is not None:
            result['AppVersion'] = self.app_version

        if self.auth_code is not None:
            result['AuthCode'] = self.auth_code

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')

        if m.get('AppInstanceId') is not None:
            self.app_instance_id = m.get('AppInstanceId')

        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')

        if m.get('AuthCode') is not None:
            self.auth_code = m.get('AuthCode')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

