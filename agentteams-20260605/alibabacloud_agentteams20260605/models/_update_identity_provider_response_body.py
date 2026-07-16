# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_agentteams20260605 import models as main_models
from darabonba.model import DaraModel

class UpdateIdentityProviderResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.UpdateIdentityProviderResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.UpdateIdentityProviderResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class UpdateIdentityProviderResponseBodyData(DaraModel):
    def __init__(
        self,
        binding_id: int = None,
        identity_provider_type: str = None,
        instance_id: str = None,
        login_enabled: bool = None,
        sync_enabled: bool = None,
    ):
        self.binding_id = binding_id
        self.identity_provider_type = identity_provider_type
        self.instance_id = instance_id
        self.login_enabled = login_enabled
        self.sync_enabled = sync_enabled

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.binding_id is not None:
            result['BindingId'] = self.binding_id

        if self.identity_provider_type is not None:
            result['IdentityProviderType'] = self.identity_provider_type

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.login_enabled is not None:
            result['LoginEnabled'] = self.login_enabled

        if self.sync_enabled is not None:
            result['SyncEnabled'] = self.sync_enabled

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BindingId') is not None:
            self.binding_id = m.get('BindingId')

        if m.get('IdentityProviderType') is not None:
            self.identity_provider_type = m.get('IdentityProviderType')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('LoginEnabled') is not None:
            self.login_enabled = m.get('LoginEnabled')

        if m.get('SyncEnabled') is not None:
            self.sync_enabled = m.get('SyncEnabled')

        return self

