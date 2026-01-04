# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ddoscoo20200101 import models as main_models
from darabonba.model import DaraModel

class DescribeDomainTopAttackListResponseBody(DaraModel):
    def __init__(
        self,
        attack_list: List[main_models.DescribeDomainTopAttackListResponseBodyAttackList] = None,
        request_id: str = None,
    ):
        # The peak QPS of the website.
        self.attack_list = attack_list
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.attack_list:
            for v1 in self.attack_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AttackList'] = []
        if self.attack_list is not None:
            for k1 in self.attack_list:
                result['AttackList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.attack_list = []
        if m.get('AttackList') is not None:
            for k1 in m.get('AttackList'):
                temp_model = main_models.DescribeDomainTopAttackListResponseBodyAttackList()
                self.attack_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeDomainTopAttackListResponseBodyAttackList(DaraModel):
    def __init__(
        self,
        attack: int = None,
        count: int = None,
        domain: str = None,
    ):
        # The attack QPS. Unit: QPS
        self.attack = attack
        # The number of all QPS, which includes normal and attack QPS. Unit: QPS.
        self.count = count
        # The domain name of the website.
        self.domain = domain

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attack is not None:
            result['Attack'] = self.attack

        if self.count is not None:
            result['Count'] = self.count

        if self.domain is not None:
            result['Domain'] = self.domain

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Attack') is not None:
            self.attack = m.get('Attack')

        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        return self

