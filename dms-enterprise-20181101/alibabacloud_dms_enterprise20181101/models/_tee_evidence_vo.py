# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class TeeEvidenceVO(DaraModel):
    def __init__(
        self,
        cipher_suite: str = None,
        enclave_data: str = None,
        encrypt_public_key_pem: str = None,
        encrypt_public_key_type: str = None,
        modified_date: str = None,
        public_key: str = None,
        public_key_ra_base_64: str = None,
        public_key_ra_type: str = None,
        quote_report: str = None,
        sign_public_key_pem: str = None,
        sign_public_key_type: str = None,
        trusted_mr_enclave: List[str] = None,
    ):
        self.cipher_suite = cipher_suite
        self.enclave_data = enclave_data
        self.encrypt_public_key_pem = encrypt_public_key_pem
        self.encrypt_public_key_type = encrypt_public_key_type
        self.modified_date = modified_date
        self.public_key = public_key
        self.public_key_ra_base_64 = public_key_ra_base_64
        self.public_key_ra_type = public_key_ra_type
        self.quote_report = quote_report
        self.sign_public_key_pem = sign_public_key_pem
        self.sign_public_key_type = sign_public_key_type
        self.trusted_mr_enclave = trusted_mr_enclave

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cipher_suite is not None:
            result['CipherSuite'] = self.cipher_suite

        if self.enclave_data is not None:
            result['EnclaveData'] = self.enclave_data

        if self.encrypt_public_key_pem is not None:
            result['EncryptPublicKeyPem'] = self.encrypt_public_key_pem

        if self.encrypt_public_key_type is not None:
            result['EncryptPublicKeyType'] = self.encrypt_public_key_type

        if self.modified_date is not None:
            result['ModifiedDate'] = self.modified_date

        if self.public_key is not None:
            result['PublicKey'] = self.public_key

        if self.public_key_ra_base_64 is not None:
            result['PublicKeyRaBase64'] = self.public_key_ra_base_64

        if self.public_key_ra_type is not None:
            result['PublicKeyRaType'] = self.public_key_ra_type

        if self.quote_report is not None:
            result['QuoteReport'] = self.quote_report

        if self.sign_public_key_pem is not None:
            result['SignPublicKeyPem'] = self.sign_public_key_pem

        if self.sign_public_key_type is not None:
            result['SignPublicKeyType'] = self.sign_public_key_type

        if self.trusted_mr_enclave is not None:
            result['TrustedMrEnclave'] = self.trusted_mr_enclave

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CipherSuite') is not None:
            self.cipher_suite = m.get('CipherSuite')

        if m.get('EnclaveData') is not None:
            self.enclave_data = m.get('EnclaveData')

        if m.get('EncryptPublicKeyPem') is not None:
            self.encrypt_public_key_pem = m.get('EncryptPublicKeyPem')

        if m.get('EncryptPublicKeyType') is not None:
            self.encrypt_public_key_type = m.get('EncryptPublicKeyType')

        if m.get('ModifiedDate') is not None:
            self.modified_date = m.get('ModifiedDate')

        if m.get('PublicKey') is not None:
            self.public_key = m.get('PublicKey')

        if m.get('PublicKeyRaBase64') is not None:
            self.public_key_ra_base_64 = m.get('PublicKeyRaBase64')

        if m.get('PublicKeyRaType') is not None:
            self.public_key_ra_type = m.get('PublicKeyRaType')

        if m.get('QuoteReport') is not None:
            self.quote_report = m.get('QuoteReport')

        if m.get('SignPublicKeyPem') is not None:
            self.sign_public_key_pem = m.get('SignPublicKeyPem')

        if m.get('SignPublicKeyType') is not None:
            self.sign_public_key_type = m.get('SignPublicKeyType')

        if m.get('TrustedMrEnclave') is not None:
            self.trusted_mr_enclave = m.get('TrustedMrEnclave')

        return self

