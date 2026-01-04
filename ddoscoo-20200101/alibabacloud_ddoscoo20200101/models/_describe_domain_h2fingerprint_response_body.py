# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ddoscoo20200101 import models as main_models
from darabonba.model import DaraModel

class DescribeDomainH2FingerprintResponseBody(DaraModel):
    def __init__(
        self,
        domain_h2fp: List[main_models.DescribeDomainH2FingerprintResponseBodyDomainH2Fp] = None,
        request_id: str = None,
    ):
        # The information about top N HTTP/2 fingerprints.
        self.domain_h2fp = domain_h2fp
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.domain_h2fp:
            for v1 in self.domain_h2fp:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DomainH2Fp'] = []
        if self.domain_h2fp is not None:
            for k1 in self.domain_h2fp:
                result['DomainH2Fp'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.domain_h2fp = []
        if m.get('DomainH2Fp') is not None:
            for k1 in m.get('DomainH2Fp'):
                temp_model = main_models.DescribeDomainH2FingerprintResponseBodyDomainH2Fp()
                self.domain_h2fp.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeDomainH2FingerprintResponseBodyDomainH2Fp(DaraModel):
    def __init__(
        self,
        domain: str = None,
        h_2fingerprint: str = None,
        pv: int = None,
    ):
        # The domain name of the website.
        self.domain = domain
        # The HTTP/2 fingerprint.
        self.h_2fingerprint = h_2fingerprint
        # The page views.
        self.pv = pv

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain is not None:
            result['Domain'] = self.domain

        if self.h_2fingerprint is not None:
            result['H2Fingerprint'] = self.h_2fingerprint

        if self.pv is not None:
            result['Pv'] = self.pv

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('H2Fingerprint') is not None:
            self.h_2fingerprint = m.get('H2Fingerprint')

        if m.get('Pv') is not None:
            self.pv = m.get('Pv')

        return self

