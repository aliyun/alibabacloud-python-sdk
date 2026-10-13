# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from alibabacloud_rdsai20250507 import models as main_models
from darabonba.model import DaraModel

class GetContextDatabaseSyncConnectionAuthorizationResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetContextDatabaseSyncConnectionAuthorizationResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The error code.
        self.code = code
        # The returned data.
        self.data = data
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request is successful.
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
            temp_model = main_models.GetContextDatabaseSyncConnectionAuthorizationResponseBodyData()
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

class GetContextDatabaseSyncConnectionAuthorizationResponseBodyData(DaraModel):
    def __init__(
        self,
        auth_kind: str = None,
        auth_state: str = None,
        created_at: str = None,
        display_name: str = None,
        id: str = None,
        plugin_id: str = None,
        remediation: str = None,
        scope_report: Dict[str, Any] = None,
        secret_fingerprint: str = None,
        secret_updated_at: str = None,
        updated_at: str = None,
        verified_at: str = None,
    ):
        # The authorization method. Valid values: app, pasted-url, static-secret, and none.
        self.auth_kind = auth_kind
        # The authorization status.
        self.auth_state = auth_state
        # The creation time.
        self.created_at = created_at
        # The display name.
        self.display_name = display_name
        # The connection ID, which is a system-generated UUID.
        self.id = id
        # The plugin ID.
        self.plugin_id = plugin_id
        # The remediation suggestion.
        self.remediation = remediation
        # The authorization scope report.
        self.scope_report = scope_report
        # The credential fingerprint.
        self.secret_fingerprint = secret_fingerprint
        # The credential update time.
        self.secret_updated_at = secret_updated_at
        # The update time.
        self.updated_at = updated_at
        # The verification time.
        self.verified_at = verified_at

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_kind is not None:
            result['AuthKind'] = self.auth_kind

        if self.auth_state is not None:
            result['AuthState'] = self.auth_state

        if self.created_at is not None:
            result['CreatedAt'] = self.created_at

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.id is not None:
            result['Id'] = self.id

        if self.plugin_id is not None:
            result['PluginId'] = self.plugin_id

        if self.remediation is not None:
            result['Remediation'] = self.remediation

        if self.scope_report is not None:
            result['ScopeReport'] = self.scope_report

        if self.secret_fingerprint is not None:
            result['SecretFingerprint'] = self.secret_fingerprint

        if self.secret_updated_at is not None:
            result['SecretUpdatedAt'] = self.secret_updated_at

        if self.updated_at is not None:
            result['UpdatedAt'] = self.updated_at

        if self.verified_at is not None:
            result['VerifiedAt'] = self.verified_at

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthKind') is not None:
            self.auth_kind = m.get('AuthKind')

        if m.get('AuthState') is not None:
            self.auth_state = m.get('AuthState')

        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('PluginId') is not None:
            self.plugin_id = m.get('PluginId')

        if m.get('Remediation') is not None:
            self.remediation = m.get('Remediation')

        if m.get('ScopeReport') is not None:
            self.scope_report = m.get('ScopeReport')

        if m.get('SecretFingerprint') is not None:
            self.secret_fingerprint = m.get('SecretFingerprint')

        if m.get('SecretUpdatedAt') is not None:
            self.secret_updated_at = m.get('SecretUpdatedAt')

        if m.get('UpdatedAt') is not None:
            self.updated_at = m.get('UpdatedAt')

        if m.get('VerifiedAt') is not None:
            self.verified_at = m.get('VerifiedAt')

        return self

