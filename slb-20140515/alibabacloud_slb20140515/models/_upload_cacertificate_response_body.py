# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UploadCACertificateResponseBody(DaraModel):
    def __init__(
        self,
        cacertificate_id: str = None,
        cacertificate_name: str = None,
        common_name: str = None,
        create_time: str = None,
        create_time_stamp: int = None,
        expire_time: str = None,
        expire_time_stamp: int = None,
        fingerprint: str = None,
        request_id: str = None,
        resource_group_id: str = None,
    ):
        # The ID of the CA certificate.
        self.cacertificate_id = cacertificate_id
        # The CA certificate name.
        self.cacertificate_name = cacertificate_name
        # The domain name on the CA certificate.
        self.common_name = common_name
        # The time when the CA certificate was created.
        self.create_time = create_time
        # The timestamp when the CA certificate was created.
        self.create_time_stamp = create_time_stamp
        # The time when the CA certificate expires.
        self.expire_time = expire_time
        # The timestamp when the server certificate expires.
        self.expire_time_stamp = expire_time_stamp
        # The fingerprint of the server certificate.
        self.fingerprint = fingerprint
        # The request ID.
        self.request_id = request_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cacertificate_id is not None:
            result['CACertificateId'] = self.cacertificate_id

        if self.cacertificate_name is not None:
            result['CACertificateName'] = self.cacertificate_name

        if self.common_name is not None:
            result['CommonName'] = self.common_name

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.create_time_stamp is not None:
            result['CreateTimeStamp'] = self.create_time_stamp

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.expire_time_stamp is not None:
            result['ExpireTimeStamp'] = self.expire_time_stamp

        if self.fingerprint is not None:
            result['Fingerprint'] = self.fingerprint

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CACertificateId') is not None:
            self.cacertificate_id = m.get('CACertificateId')

        if m.get('CACertificateName') is not None:
            self.cacertificate_name = m.get('CACertificateName')

        if m.get('CommonName') is not None:
            self.common_name = m.get('CommonName')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CreateTimeStamp') is not None:
            self.create_time_stamp = m.get('CreateTimeStamp')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('ExpireTimeStamp') is not None:
            self.expire_time_stamp = m.get('ExpireTimeStamp')

        if m.get('Fingerprint') is not None:
            self.fingerprint = m.get('Fingerprint')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        return self

