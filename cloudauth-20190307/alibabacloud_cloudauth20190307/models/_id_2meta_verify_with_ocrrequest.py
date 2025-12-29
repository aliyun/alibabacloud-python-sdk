# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class Id2MetaVerifyWithOCRRequest(DaraModel):
    def __init__(
        self,
        cert_file: str = None,
        cert_national_file: str = None,
        cert_national_url: str = None,
        cert_url: str = None,
    ):
        # Input stream for the portrait side of the ID card image.
        # Choose one between CertUrl and CertFile.
        self.cert_file = cert_file
        # National emblem side of the ID card image address.
        # Choose one between CertNationalUrl and CertNationalFile, or omit both.
        self.cert_national_file = cert_national_file
        # National emblem side of the ID card image URL. National emblem side
        # A publicly accessible HTTP or HTTPS link.
        # Choose one between CertNationalUrl and CertNationalFile, or omit both.
        self.cert_national_url = cert_national_url
        # Portrait side of the ID card image.
        # A publicly accessible HTTP or HTTPS link.
        # Choose one between CertUrl and CertFile.
        self.cert_url = cert_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cert_file is not None:
            result['CertFile'] = self.cert_file

        if self.cert_national_file is not None:
            result['CertNationalFile'] = self.cert_national_file

        if self.cert_national_url is not None:
            result['CertNationalUrl'] = self.cert_national_url

        if self.cert_url is not None:
            result['CertUrl'] = self.cert_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertFile') is not None:
            self.cert_file = m.get('CertFile')

        if m.get('CertNationalFile') is not None:
            self.cert_national_file = m.get('CertNationalFile')

        if m.get('CertNationalUrl') is not None:
            self.cert_national_url = m.get('CertNationalUrl')

        if m.get('CertUrl') is not None:
            self.cert_url = m.get('CertUrl')

        return self

