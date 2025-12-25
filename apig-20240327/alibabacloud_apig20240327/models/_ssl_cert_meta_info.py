# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SslCertMetaInfo(DaraModel):
    def __init__(
        self,
        algorithm: str = None,
        cert_id: int = None,
        cert_identifier: str = None,
        cert_name: str = None,
        common_name: str = None,
        domain: str = None,
        domain_match_cert: bool = None,
        fingerprint: str = None,
        instance_id: str = None,
        is_chain_completed: bool = None,
        issuer: str = None,
        key_size: str = None,
        md_5: str = None,
        not_after_timestamp: int = None,
        not_before_timestamp: int = None,
        sans: str = None,
        serial_no: str = None,
        sha_2: str = None,
        sign_algorithm: str = None,
    ):
        self.algorithm = algorithm
        self.cert_id = cert_id
        self.cert_identifier = cert_identifier
        self.cert_name = cert_name
        self.common_name = common_name
        self.domain = domain
        self.domain_match_cert = domain_match_cert
        self.fingerprint = fingerprint
        self.instance_id = instance_id
        self.is_chain_completed = is_chain_completed
        self.issuer = issuer
        self.key_size = key_size
        self.md_5 = md_5
        self.not_after_timestamp = not_after_timestamp
        self.not_before_timestamp = not_before_timestamp
        self.sans = sans
        self.serial_no = serial_no
        self.sha_2 = sha_2
        self.sign_algorithm = sign_algorithm

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.algorithm is not None:
            result['algorithm'] = self.algorithm

        if self.cert_id is not None:
            result['certId'] = self.cert_id

        if self.cert_identifier is not None:
            result['certIdentifier'] = self.cert_identifier

        if self.cert_name is not None:
            result['certName'] = self.cert_name

        if self.common_name is not None:
            result['commonName'] = self.common_name

        if self.domain is not None:
            result['domain'] = self.domain

        if self.domain_match_cert is not None:
            result['domainMatchCert'] = self.domain_match_cert

        if self.fingerprint is not None:
            result['fingerprint'] = self.fingerprint

        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        if self.is_chain_completed is not None:
            result['isChainCompleted'] = self.is_chain_completed

        if self.issuer is not None:
            result['issuer'] = self.issuer

        if self.key_size is not None:
            result['keySize'] = self.key_size

        if self.md_5 is not None:
            result['md5'] = self.md_5

        if self.not_after_timestamp is not None:
            result['notAfterTimestamp'] = self.not_after_timestamp

        if self.not_before_timestamp is not None:
            result['notBeforeTimestamp'] = self.not_before_timestamp

        if self.sans is not None:
            result['sans'] = self.sans

        if self.serial_no is not None:
            result['serialNo'] = self.serial_no

        if self.sha_2 is not None:
            result['sha2'] = self.sha_2

        if self.sign_algorithm is not None:
            result['signAlgorithm'] = self.sign_algorithm

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('algorithm') is not None:
            self.algorithm = m.get('algorithm')

        if m.get('certId') is not None:
            self.cert_id = m.get('certId')

        if m.get('certIdentifier') is not None:
            self.cert_identifier = m.get('certIdentifier')

        if m.get('certName') is not None:
            self.cert_name = m.get('certName')

        if m.get('commonName') is not None:
            self.common_name = m.get('commonName')

        if m.get('domain') is not None:
            self.domain = m.get('domain')

        if m.get('domainMatchCert') is not None:
            self.domain_match_cert = m.get('domainMatchCert')

        if m.get('fingerprint') is not None:
            self.fingerprint = m.get('fingerprint')

        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        if m.get('isChainCompleted') is not None:
            self.is_chain_completed = m.get('isChainCompleted')

        if m.get('issuer') is not None:
            self.issuer = m.get('issuer')

        if m.get('keySize') is not None:
            self.key_size = m.get('keySize')

        if m.get('md5') is not None:
            self.md_5 = m.get('md5')

        if m.get('notAfterTimestamp') is not None:
            self.not_after_timestamp = m.get('notAfterTimestamp')

        if m.get('notBeforeTimestamp') is not None:
            self.not_before_timestamp = m.get('notBeforeTimestamp')

        if m.get('sans') is not None:
            self.sans = m.get('sans')

        if m.get('serialNo') is not None:
            self.serial_no = m.get('serialNo')

        if m.get('sha2') is not None:
            self.sha_2 = m.get('sha2')

        if m.get('signAlgorithm') is not None:
            self.sign_algorithm = m.get('signAlgorithm')

        return self

