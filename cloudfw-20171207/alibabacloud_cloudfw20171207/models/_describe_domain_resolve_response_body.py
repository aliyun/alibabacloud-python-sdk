# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class DescribeDomainResolveResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        resolve_result: main_models.DescribeDomainResolveResponseBodyResolveResult = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The details about the DNS record of the domain name.
        self.resolve_result = resolve_result

    def validate(self):
        if self.resolve_result:
            self.resolve_result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resolve_result is not None:
            result['ResolveResult'] = self.resolve_result.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResolveResult') is not None:
            temp_model = main_models.DescribeDomainResolveResponseBodyResolveResult()
            self.resolve_result = temp_model.from_map(m.get('ResolveResult'))

        return self

class DescribeDomainResolveResponseBodyResolveResult(DaraModel):
    def __init__(
        self,
        ip_addrs: str = None,
        update_time: int = None,
    ):
        # The IP address to which the domain name is resolved. Multiple IP addresses are separated by commas (,).
        self.ip_addrs = ip_addrs
        # The time when the domain name was resolved. The value of this parameter is a timestamp. Unit: seconds.
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ip_addrs is not None:
            result['IpAddrs'] = self.ip_addrs

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IpAddrs') is not None:
            self.ip_addrs = m.get('IpAddrs')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

