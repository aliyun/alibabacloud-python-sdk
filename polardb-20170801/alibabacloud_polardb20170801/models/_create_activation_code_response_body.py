# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateActivationCodeResponseBody(DaraModel):
    def __init__(
        self,
        activate_at: str = None,
        cert_content_b64: str = None,
        description: str = None,
        expire_at: str = None,
        gmt_created: str = None,
        gmt_modified: str = None,
        id: int = None,
        mac_address: str = None,
        name: str = None,
        request_id: str = None,
        system_identifier: str = None,
    ):
        # The time when the activation code takes effect.
        self.activate_at = activate_at
        # The activation code in the base64 format. The activation code is decoded and stored into a file named license.lic. PolarDB can access and read the license.lic file upon startup to validate the license or perform related operations.
        self.cert_content_b64 = cert_content_b64
        # The description of the activation code.
        self.description = description
        # The time when the activation code expires.
        self.expire_at = expire_at
        # The time when the activation code was created.
        self.gmt_created = gmt_created
        # The time when the activation code was last updated.
        self.gmt_modified = gmt_modified
        # The activation code ID.
        self.id = id
        # The MAC address.
        self.mac_address = mac_address
        # The name of the activation code.
        self.name = name
        # The request ID.
        self.request_id = request_id
        # The system identifier of the database.
        self.system_identifier = system_identifier

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.activate_at is not None:
            result['ActivateAt'] = self.activate_at

        if self.cert_content_b64 is not None:
            result['CertContentB64'] = self.cert_content_b64

        if self.description is not None:
            result['Description'] = self.description

        if self.expire_at is not None:
            result['ExpireAt'] = self.expire_at

        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.id is not None:
            result['Id'] = self.id

        if self.mac_address is not None:
            result['MacAddress'] = self.mac_address

        if self.name is not None:
            result['Name'] = self.name

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.system_identifier is not None:
            result['SystemIdentifier'] = self.system_identifier

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActivateAt') is not None:
            self.activate_at = m.get('ActivateAt')

        if m.get('CertContentB64') is not None:
            self.cert_content_b64 = m.get('CertContentB64')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ExpireAt') is not None:
            self.expire_at = m.get('ExpireAt')

        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('MacAddress') is not None:
            self.mac_address = m.get('MacAddress')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SystemIdentifier') is not None:
            self.system_identifier = m.get('SystemIdentifier')

        return self

