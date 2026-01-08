# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class DescribeControlPolicyDomainResolveResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        resolve_result: List[main_models.DescribeControlPolicyDomainResolveResponseBodyResolveResult] = None,
    ):
        self.request_id = request_id
        self.resolve_result = resolve_result

    def validate(self):
        if self.resolve_result:
            for v1 in self.resolve_result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['ResolveResult'] = []
        if self.resolve_result is not None:
            for k1 in self.resolve_result:
                result['ResolveResult'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.resolve_result = []
        if m.get('ResolveResult') is not None:
            for k1 in m.get('ResolveResult'):
                temp_model = main_models.DescribeControlPolicyDomainResolveResponseBodyResolveResult()
                self.resolve_result.append(temp_model.from_map(k1))

        return self

class DescribeControlPolicyDomainResolveResponseBodyResolveResult(DaraModel):
    def __init__(
        self,
        domain: str = None,
        ip_addr_list: List[str] = None,
        ip_version: int = None,
        update_time: int = None,
    ):
        self.domain = domain
        self.ip_addr_list = ip_addr_list
        self.ip_version = ip_version
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain is not None:
            result['Domain'] = self.domain

        if self.ip_addr_list is not None:
            result['IpAddrList'] = self.ip_addr_list

        if self.ip_version is not None:
            result['IpVersion'] = self.ip_version

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('IpAddrList') is not None:
            self.ip_addr_list = m.get('IpAddrList')

        if m.get('IpVersion') is not None:
            self.ip_version = m.get('IpVersion')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

