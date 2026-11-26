# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cloudsso20210515 import models as main_models
from darabonba.model import DaraModel

class GetSecurityInfoResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        security_email: main_models.GetSecurityInfoResponseBodySecurityEmail = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The security email information of the user.
        # 
        # > If the user has not configured a security email address, this field is not returned.
        self.security_email = security_email

    def validate(self):
        if self.security_email:
            self.security_email.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.security_email is not None:
            result['SecurityEmail'] = self.security_email.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SecurityEmail') is not None:
            temp_model = main_models.GetSecurityInfoResponseBodySecurityEmail()
            self.security_email = temp_model.from_map(m.get('SecurityEmail'))

        return self

class GetSecurityInfoResponseBodySecurityEmail(DaraModel):
    def __init__(
        self,
        email: str = None,
        status: str = None,
    ):
        # The security email address of the user.
        self.email = email
        # The verification status of the security email address. Valid values:
        # 
        # - active: Verified.
        # - pending: Pending verification.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.email is not None:
            result['Email'] = self.email

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Email') is not None:
            self.email = m.get('Email')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

