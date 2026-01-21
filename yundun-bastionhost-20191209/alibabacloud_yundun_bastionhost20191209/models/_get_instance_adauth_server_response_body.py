# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_yundun_bastionhost20191209 import models as main_models
from darabonba.model import DaraModel

class GetInstanceADAuthServerResponseBody(DaraModel):
    def __init__(
        self,
        ad: main_models.GetInstanceADAuthServerResponseBodyAD = None,
        request_id: str = None,
    ):
        # The settings of AD authentication.
        self.ad = ad
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.ad:
            self.ad.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ad is not None:
            result['AD'] = self.ad.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AD') is not None:
            temp_model = main_models.GetInstanceADAuthServerResponseBodyAD()
            self.ad = temp_model.from_map(m.get('AD'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetInstanceADAuthServerResponseBodyAD(DaraModel):
    def __init__(
        self,
        account: str = None,
        base_dn: str = None,
        domain: str = None,
        email_mapping: str = None,
        filter: str = None,
        has_password: bool = None,
        is_ssl: bool = None,
        mobile_mapping: str = None,
        name_mapping: str = None,
        port: int = None,
        server: str = None,
        standby_server: str = None,
    ):
        # The distinguished name (DN) of the AD server account.
        self.account = account
        # The Base DN of the AD server.
        self.base_dn = base_dn
        # The domain on the AD server.
        self.domain = domain
        # The field that is used to indicate the email address of a user on the AD server.
        self.email_mapping = email_mapping
        # The condition that is used to filter users.
        self.filter = filter
        # Indicates whether passwords are required. Valid values:
        # 
        # *   **true**:
        # *   **false**
        self.has_password = has_password
        # Indicates whether SSL is supported. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.is_ssl = is_ssl
        # The field that is used to indicate the mobile phone number of a user on the AD server.
        self.mobile_mapping = mobile_mapping
        # The field that is used to indicate the name of a user on the AD server.
        self.name_mapping = name_mapping
        # The port that is used to access the AD server.
        self.port = port
        # The address of the AD server.
        self.server = server
        # The address of the secondary AD server.
        self.standby_server = standby_server

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account is not None:
            result['Account'] = self.account

        if self.base_dn is not None:
            result['BaseDN'] = self.base_dn

        if self.domain is not None:
            result['Domain'] = self.domain

        if self.email_mapping is not None:
            result['EmailMapping'] = self.email_mapping

        if self.filter is not None:
            result['Filter'] = self.filter

        if self.has_password is not None:
            result['HasPassword'] = self.has_password

        if self.is_ssl is not None:
            result['IsSSL'] = self.is_ssl

        if self.mobile_mapping is not None:
            result['MobileMapping'] = self.mobile_mapping

        if self.name_mapping is not None:
            result['NameMapping'] = self.name_mapping

        if self.port is not None:
            result['Port'] = self.port

        if self.server is not None:
            result['Server'] = self.server

        if self.standby_server is not None:
            result['StandbyServer'] = self.standby_server

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Account') is not None:
            self.account = m.get('Account')

        if m.get('BaseDN') is not None:
            self.base_dn = m.get('BaseDN')

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('EmailMapping') is not None:
            self.email_mapping = m.get('EmailMapping')

        if m.get('Filter') is not None:
            self.filter = m.get('Filter')

        if m.get('HasPassword') is not None:
            self.has_password = m.get('HasPassword')

        if m.get('IsSSL') is not None:
            self.is_ssl = m.get('IsSSL')

        if m.get('MobileMapping') is not None:
            self.mobile_mapping = m.get('MobileMapping')

        if m.get('NameMapping') is not None:
            self.name_mapping = m.get('NameMapping')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('Server') is not None:
            self.server = m.get('Server')

        if m.get('StandbyServer') is not None:
            self.standby_server = m.get('StandbyServer')

        return self

