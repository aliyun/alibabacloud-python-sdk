# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDomainDnssecInfoResponseBody(DaraModel):
    def __init__(
        self,
        algorithm: str = None,
        digest: str = None,
        digest_type: str = None,
        domain_name: str = None,
        ds_record: str = None,
        flags: str = None,
        key_tag: str = None,
        public_key: str = None,
        request_id: str = None,
        status: str = None,
    ):
        # The algorithm type. This parameter is returned if DNSSEC is enabled.
        self.algorithm = algorithm
        # The digest. This parameter is returned if DNSSEC is enabled.
        self.digest = digest
        # The digest type. This parameter is returned if DNSSEC is enabled.
        self.digest_type = digest_type
        # The domain name.
        self.domain_name = domain_name
        # The delegation signer (DS) record. This parameter is returned if DNSSEC is enabled.
        self.ds_record = ds_record
        # The flag. This parameter is returned if DNSSEC is enabled.
        self.flags = flags
        # The key tag. This parameter is returned if DNSSEC is enabled.
        self.key_tag = key_tag
        # The public key. This parameter is returned if DNSSEC is enabled.
        self.public_key = public_key
        # The request ID.
        self.request_id = request_id
        # The state of the DNSSEC. Valid values:
        # 
        # *   ON
        # *   OFF
        self.status = status

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

        if self.ds_record is not None:
            result['DsRecord'] = self.ds_record

        if self.flags is not None:
            result['Flags'] = self.flags

        if self.key_tag is not None:
            result['KeyTag'] = self.key_tag

        if self.public_key is not None:
            result['PublicKey'] = self.public_key

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status is not None:
            result['Status'] = self.status

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

        if m.get('DsRecord') is not None:
            self.ds_record = m.get('DsRecord')

        if m.get('Flags') is not None:
            self.flags = m.get('Flags')

        if m.get('KeyTag') is not None:
            self.key_tag = m.get('KeyTag')

        if m.get('PublicKey') is not None:
            self.public_key = m.get('PublicKey')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

