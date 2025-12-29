# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import BinaryIO

from darabonba.model import DaraModel

class Id3MetaVerifyWithOCRAdvanceRequest(DaraModel):
    def __init__(
        self,
        cert_file_object: BinaryIO = None,
        cert_national_file_object: BinaryIO = None,
        cert_national_url: str = None,
        cert_url: str = None,
    ):
        # Input stream for the portrait side of the ID card image. Choose either CertUrl or CertFile.
        self.cert_file_object = cert_file_object
        # URL for the national emblem side of the ID card image. Choose either CertNationalUrl or CertNationalFile, or omit both.
        self.cert_national_file_object = cert_national_file_object
        # National emblem side of the ID card image URL. A publicly accessible HTTP or HTTPS link. You can choose either CertNationalUrl or CertNationalFile, or omit both.
        self.cert_national_url = cert_national_url
        # Portrait side of the ID card image. A publicly accessible HTTP or HTTPS link. Choose either CertUrl or CertFile.
        self.cert_url = cert_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cert_file_object is not None:
            result['CertFile'] = self.cert_file_object

        if self.cert_national_file_object is not None:
            result['CertNationalFile'] = self.cert_national_file_object

        if self.cert_national_url is not None:
            result['CertNationalUrl'] = self.cert_national_url

        if self.cert_url is not None:
            result['CertUrl'] = self.cert_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertFile') is not None:
            self.cert_file_object = m.get('CertFile')

        if m.get('CertNationalFile') is not None:
            self.cert_national_file_object = m.get('CertNationalFile')

        if m.get('CertNationalUrl') is not None:
            self.cert_national_url = m.get('CertNationalUrl')

        if m.get('CertUrl') is not None:
            self.cert_url = m.get('CertUrl')

        return self

