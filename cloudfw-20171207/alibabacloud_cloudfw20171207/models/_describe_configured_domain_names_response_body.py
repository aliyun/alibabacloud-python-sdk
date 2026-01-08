# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class DescribeConfiguredDomainNamesResponseBody(DaraModel):
    def __init__(
        self,
        domain_names: List[main_models.DescribeConfiguredDomainNamesResponseBodyDomainNames] = None,
        module: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.domain_names = domain_names
        self.module = module
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.domain_names:
            for v1 in self.domain_names:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DomainNames'] = []
        if self.domain_names is not None:
            for k1 in self.domain_names:
                result['DomainNames'].append(k1.to_map() if k1 else None)

        if self.module is not None:
            result['Module'] = self.module

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.domain_names = []
        if m.get('DomainNames') is not None:
            for k1 in m.get('DomainNames'):
                temp_model = main_models.DescribeConfiguredDomainNamesResponseBodyDomainNames()
                self.domain_names.append(temp_model.from_map(k1))

        if m.get('Module') is not None:
            self.module = m.get('Module')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeConfiguredDomainNamesResponseBodyDomainNames(DaraModel):
    def __init__(
        self,
        comment: str = None,
        domain_name: str = None,
        is_malicious: bool = None,
        operation_time: int = None,
    ):
        self.comment = comment
        self.domain_name = domain_name
        self.is_malicious = is_malicious
        self.operation_time = operation_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comment is not None:
            result['Comment'] = self.comment

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.is_malicious is not None:
            result['IsMalicious'] = self.is_malicious

        if self.operation_time is not None:
            result['OperationTime'] = self.operation_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('IsMalicious') is not None:
            self.is_malicious = m.get('IsMalicious')

        if m.get('OperationTime') is not None:
            self.operation_time = m.get('OperationTime')

        return self

