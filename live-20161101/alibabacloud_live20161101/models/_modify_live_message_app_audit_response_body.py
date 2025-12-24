# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyLiveMessageAppAuditResponseBody(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        app_sign: str = None,
        audit_need_authentication: bool = None,
        audit_type: int = None,
        audit_url: str = None,
        request_id: str = None,
    ):
        # The ID of the interactive messaging application.
        self.app_id = app_id
        # The signature of the interactive messaging application. It is required by the interactive messaging SDK.
        self.app_sign = app_sign
        # Indicates whether authentication is enabled. If custom content moderation is used, the value of this parameter is true by default.
        self.audit_need_authentication = audit_need_authentication
        # The content moderation method.
        self.audit_type = audit_type
        # The URL for content moderation. This parameter is returned when the value of AuditType is 2.
        self.audit_url = audit_url
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.app_sign is not None:
            result['AppSign'] = self.app_sign

        if self.audit_need_authentication is not None:
            result['AuditNeedAuthentication'] = self.audit_need_authentication

        if self.audit_type is not None:
            result['AuditType'] = self.audit_type

        if self.audit_url is not None:
            result['AuditUrl'] = self.audit_url

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppSign') is not None:
            self.app_sign = m.get('AppSign')

        if m.get('AuditNeedAuthentication') is not None:
            self.audit_need_authentication = m.get('AuditNeedAuthentication')

        if m.get('AuditType') is not None:
            self.audit_type = m.get('AuditType')

        if m.get('AuditUrl') is not None:
            self.audit_url = m.get('AuditUrl')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

