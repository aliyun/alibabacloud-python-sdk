# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeAntAndCloudAuthUserStatusResponseBody(DaraModel):
    def __init__(
        self,
        antcloudauth_enabled: bool = None,
        cloudauth_enabled: bool = None,
        cloudauthst_enabled: bool = None,
        inforverify_enabled: bool = None,
        request_id: str = None,
    ):
        # Indicates whether financial-grade real-person authentication is activated. Values:
        # - **true**: Activated
        # - **false**: Not activated
        self.antcloudauth_enabled = antcloudauth_enabled
        # Indicates whether real-person authentication is activated. Values:
        # - **true**: Activated
        # - **false**: Not activated
        self.cloudauth_enabled = cloudauth_enabled
        # Indicates whether the enhanced version of real-person authentication is activated. Values:
        # - **true**: Activated
        # - **false**: Not activated
        self.cloudauthst_enabled = cloudauthst_enabled
        # Indicates whether information verification is activated. Values:
        # - **true**: Activated
        # - **false**: Not activated
        self.inforverify_enabled = inforverify_enabled
        # The ID of this request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.antcloudauth_enabled is not None:
            result['AntcloudauthEnabled'] = self.antcloudauth_enabled

        if self.cloudauth_enabled is not None:
            result['CloudauthEnabled'] = self.cloudauth_enabled

        if self.cloudauthst_enabled is not None:
            result['CloudauthstEnabled'] = self.cloudauthst_enabled

        if self.inforverify_enabled is not None:
            result['InforverifyEnabled'] = self.inforverify_enabled

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AntcloudauthEnabled') is not None:
            self.antcloudauth_enabled = m.get('AntcloudauthEnabled')

        if m.get('CloudauthEnabled') is not None:
            self.cloudauth_enabled = m.get('CloudauthEnabled')

        if m.get('CloudauthstEnabled') is not None:
            self.cloudauthst_enabled = m.get('CloudauthstEnabled')

        if m.get('InforverifyEnabled') is not None:
            self.inforverify_enabled = m.get('InforverifyEnabled')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

