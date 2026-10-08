# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SaveSingleTaskForModifyingDSRecordRequest(DaraModel):
    def __init__(
        self,
        algorithm: int = None,
        digest: str = None,
        digest_type: int = None,
        domain_name: str = None,
        key_tag: int = None,
        lang: str = None,
        user_client_ip: str = None,
    ):
        # Encryption algorithm number. For more information, see [Domain Name System Security (DNSSEC) Algorithm Numbers](https://www.iana.org/assignments/dns-sec-alg-numbers/dns-sec-alg-numbers.xhtml). Valid values:  
        # - **1**: RSA/MD5  
        # - **2**: Diffie-Hellman  
        # - **3**: DSA/SHA-1  
        # - **5**: RSA/SHA-1  
        # - **6**: DSA-NSEC3-SHA1  
        # - **7**: RSASHA1-NSEC3-SHA1  
        # - **8**: RSA/SHA-256  
        # - **10**: RSA/SHA-512  
        # - **12**: GOST R 34.10-2001  
        # - **13**: ECDSA Curve P-256 with SHA-256  
        # - **14**: ECDSA Curve P-384 with SHA-384  
        # - **15**: Ed2551916 Ed448  
        # - **252**: Reserved for Indirect Keys  
        # - **253**: private algorithm  
        # - **254**: private algorithm OID
        # 
        # This parameter is required.
        self.algorithm = algorithm
        # Summary value.
        # 
        # This parameter is required.
        self.digest = digest
        # Digest algorithm type. For more information, see [Delegation Signer (DS) Resource Record (RR) Type Digest Algorithms](https://www.iana.org/assignments/ds-rr-types/ds-rr-types.xhtml). Valid values:  
        # - **1**: SHA-1  
        # - **2**: SHA-256  
        # - **3**: GOST R 34.11-94  
        # - **4**: SHA-384
        # 
        # This parameter is required.
        self.digest_type = digest_type
        # Domain name.
        # 
        # This parameter is required.
        self.domain_name = domain_name
        # Key tag used to identify DNSSEC records. It is an integer less than 65536.
        # 
        # This parameter is required.
        self.key_tag = key_tag
        # Language of error messages returned by the API. Valid values:  
        # - **zh**: Chinese  
        # - **en**: English  
        # 
        # Default value: **en**.
        self.lang = lang
        # User IP address.
        self.user_client_ip = user_client_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm

        if self.digest is not None:
            result['Digest'] = self.digest

        if self.digest_type is not None:
            result['DigestType'] = self.digest_type

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.key_tag is not None:
            result['KeyTag'] = self.key_tag

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')

        if m.get('Digest') is not None:
            self.digest = m.get('Digest')

        if m.get('DigestType') is not None:
            self.digest_type = m.get('DigestType')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('KeyTag') is not None:
            self.key_tag = m.get('KeyTag')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')

        return self

