# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class TransportCertificateInfo(DaraModel):
    def __init__(
        self,
        algorithm: str = None,
        cert_identifier: str = None,
        cert_name: str = None,
        certificate_match_status: str = None,
        common_name: str = None,
        covered_domains: List[str] = None,
        issuer: str = None,
        matched_domains: List[str] = None,
        not_after_timestamp: int = None,
        not_before_timestamp: int = None,
        sans: str = None,
    ):
        self.algorithm = algorithm
        self.cert_identifier = cert_identifier
        self.cert_name = cert_name
        self.certificate_match_status = certificate_match_status
        self.common_name = common_name
        self.covered_domains = covered_domains
        self.issuer = issuer
        self.matched_domains = matched_domains
        self.not_after_timestamp = not_after_timestamp
        self.not_before_timestamp = not_before_timestamp
        self.sans = sans

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.algorithm is not None:
            result['algorithm'] = self.algorithm

        if self.cert_identifier is not None:
            result['certIdentifier'] = self.cert_identifier

        if self.cert_name is not None:
            result['certName'] = self.cert_name

        if self.certificate_match_status is not None:
            result['certificateMatchStatus'] = self.certificate_match_status

        if self.common_name is not None:
            result['commonName'] = self.common_name

        if self.covered_domains is not None:
            result['coveredDomains'] = self.covered_domains

        if self.issuer is not None:
            result['issuer'] = self.issuer

        if self.matched_domains is not None:
            result['matchedDomains'] = self.matched_domains

        if self.not_after_timestamp is not None:
            result['notAfterTimestamp'] = self.not_after_timestamp

        if self.not_before_timestamp is not None:
            result['notBeforeTimestamp'] = self.not_before_timestamp

        if self.sans is not None:
            result['sans'] = self.sans

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('algorithm') is not None:
            self.algorithm = m.get('algorithm')

        if m.get('certIdentifier') is not None:
            self.cert_identifier = m.get('certIdentifier')

        if m.get('certName') is not None:
            self.cert_name = m.get('certName')

        if m.get('certificateMatchStatus') is not None:
            self.certificate_match_status = m.get('certificateMatchStatus')

        if m.get('commonName') is not None:
            self.common_name = m.get('commonName')

        if m.get('coveredDomains') is not None:
            self.covered_domains = m.get('coveredDomains')

        if m.get('issuer') is not None:
            self.issuer = m.get('issuer')

        if m.get('matchedDomains') is not None:
            self.matched_domains = m.get('matchedDomains')

        if m.get('notAfterTimestamp') is not None:
            self.not_after_timestamp = m.get('notAfterTimestamp')

        if m.get('notBeforeTimestamp') is not None:
            self.not_before_timestamp = m.get('notBeforeTimestamp')

        if m.get('sans') is not None:
            self.sans = m.get('sans')

        return self

