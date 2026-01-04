# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ddoscoo20200101 import models as main_models
from darabonba.model import DaraModel

class DescribeDomainTopFingerprintResponseBody(DaraModel):
    def __init__(
        self,
        domain_top_fp: List[main_models.DescribeDomainTopFingerprintResponseBodyDomainTopFp] = None,
        request_id: str = None,
    ):
        # The information about the fingerprints of the clients.
        self.domain_top_fp = domain_top_fp
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.domain_top_fp:
            for v1 in self.domain_top_fp:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DomainTopFp'] = []
        if self.domain_top_fp is not None:
            for k1 in self.domain_top_fp:
                result['DomainTopFp'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.domain_top_fp = []
        if m.get('DomainTopFp') is not None:
            for k1 in m.get('DomainTopFp'):
                temp_model = main_models.DescribeDomainTopFingerprintResponseBodyDomainTopFp()
                self.domain_top_fp.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeDomainTopFingerprintResponseBodyDomainTopFp(DaraModel):
    def __init__(
        self,
        domain: str = None,
        fingerprinting: str = None,
        pv: int = None,
    ):
        # The domain name of the website.
        self.domain = domain
        # The fingerprint of the client.
        self.fingerprinting = fingerprinting
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

        if self.fingerprinting is not None:
            result['Fingerprinting'] = self.fingerprinting

        if self.pv is not None:
            result['Pv'] = self.pv

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('Fingerprinting') is not None:
            self.fingerprinting = m.get('Fingerprinting')

        if m.get('Pv') is not None:
            self.pv = m.get('Pv')

        return self

