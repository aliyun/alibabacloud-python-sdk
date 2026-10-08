# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_domain20180129 import models as main_models
from darabonba.model import DaraModel

class QueryDSRecordResponseBody(DaraModel):
    def __init__(
        self,
        dsrecord_list: List[main_models.QueryDSRecordResponseBodyDSRecordList] = None,
        request_id: str = None,
    ):
        # List of DS records.
        self.dsrecord_list = dsrecord_list
        # Unique request ID.
        self.request_id = request_id

    def validate(self):
        if self.dsrecord_list:
            for v1 in self.dsrecord_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DSRecordList'] = []
        if self.dsrecord_list is not None:
            for k1 in self.dsrecord_list:
                result['DSRecordList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dsrecord_list = []
        if m.get('DSRecordList') is not None:
            for k1 in m.get('DSRecordList'):
                temp_model = main_models.QueryDSRecordResponseBodyDSRecordList()
                self.dsrecord_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class QueryDSRecordResponseBodyDSRecordList(DaraModel):
    def __init__(
        self,
        algorithm: int = None,
        digest: str = None,
        digest_type: int = None,
        key_tag: int = None,
    ):
        # Encryption algorithm number. For more information, see [Domain Name System Security (DNSSEC) Algorithm Numbers](https://www.iana.org/assignments/dns-sec-alg-numbers/dns-sec-alg-numbers.xhtml). Valid values:
        #  - **1**: RSA/MD5;
        #  - **2**: Diffie-Hellman;
        #  - **3**: DSA/SHA-1;
        #  - **5**: RSA/SHA-1;
        #  - **6**: DSA-NSEC3-SHA1;
        #  - **7**: RSASHA1-NSEC3-SHA1;
        #  - **8**: RSA/SHA-256;
        #  - **10**: RSA/SHA-512;
        #  - **12**: GOST R 34.10-2001;
        #  - **13**: ECDSA Curve P-256 with SHA-256;
        #  - **14**: ECDSA Curve P-384 with SHA-384;
        #  - **15**: Ed25519;
        #  - **16**: Ed448;
        #  - **252**: Reserved for Indirect Keys;
        #  - **253**: private algorithm;
        #  - **254**: private algorithm OID.
        self.algorithm = algorithm
        # Digest value.
        self.digest = digest
        # Digest algorithm type. For more information, see [Delegation Signer (DS) Resource Record (RR) Type Digest Algorithms](https://www.iana.org/assignments/ds-rr-types/ds-rr-types.xhtml). Valid values:
        #  - **1**: SHA-1;
        #  - **2**: SHA-256;
        #  - **3**: GOST R 34.11-94;
        #  - **4**: SHA-384.
        self.digest_type = digest_type
        # Key tag used to identify DNSSEC records. It is an integer less than 65536.
        self.key_tag = key_tag

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

        if self.key_tag is not None:
            result['KeyTag'] = self.key_tag

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')

        if m.get('Digest') is not None:
            self.digest = m.get('Digest')

        if m.get('DigestType') is not None:
            self.digest_type = m.get('DigestType')

        if m.get('KeyTag') is not None:
            self.key_tag = m.get('KeyTag')

        return self

