# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_agentteams20260605 import models as main_models
from darabonba.model import DaraModel

class GetIdentityProviderResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetIdentityProviderResponseBodyData = None,
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
            temp_model = main_models.GetIdentityProviderResponseBodyData()
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

class GetIdentityProviderResponseBodyData(DaraModel):
    def __init__(
        self,
        event_subscription_callback_url: str = None,
        identity_provider_type: str = None,
        idp_metadata: Dict[str, str] = None,
        instance_id: str = None,
        login_callback_url: str = None,
        login_enabled: bool = None,
        status: str = None,
        sync_enabled: bool = None,
    ):
        self.event_subscription_callback_url = event_subscription_callback_url
        self.identity_provider_type = identity_provider_type
        self.idp_metadata = idp_metadata
        self.instance_id = instance_id
        self.login_callback_url = login_callback_url
        self.login_enabled = login_enabled
        self.status = status
        self.sync_enabled = sync_enabled

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.event_subscription_callback_url is not None:
            result['EventSubscriptionCallbackUrl'] = self.event_subscription_callback_url

        if self.identity_provider_type is not None:
            result['IdentityProviderType'] = self.identity_provider_type

        if self.idp_metadata is not None:
            result['IdpMetadata'] = self.idp_metadata

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.login_callback_url is not None:
            result['LoginCallbackUrl'] = self.login_callback_url

        if self.login_enabled is not None:
            result['LoginEnabled'] = self.login_enabled

        if self.status is not None:
            result['Status'] = self.status

        if self.sync_enabled is not None:
            result['SyncEnabled'] = self.sync_enabled

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventSubscriptionCallbackUrl') is not None:
            self.event_subscription_callback_url = m.get('EventSubscriptionCallbackUrl')

        if m.get('IdentityProviderType') is not None:
            self.identity_provider_type = m.get('IdentityProviderType')

        if m.get('IdpMetadata') is not None:
            self.idp_metadata = m.get('IdpMetadata')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('LoginCallbackUrl') is not None:
            self.login_callback_url = m.get('LoginCallbackUrl')

        if m.get('LoginEnabled') is not None:
            self.login_enabled = m.get('LoginEnabled')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SyncEnabled') is not None:
            self.sync_enabled = m.get('SyncEnabled')

        return self

