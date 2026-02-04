# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dcdn20180115 import models as main_models
from darabonba.model import DaraModel

class DescribeDcdnWafDomainDetailResponseBody(DaraModel):
    def __init__(
        self,
        domain: main_models.DescribeDcdnWafDomainDetailResponseBodyDomain = None,
        request_id: str = None,
    ):
        # The information about the accelerated domain name.
        self.domain = domain
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.domain:
            self.domain.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain is not None:
            result['Domain'] = self.domain.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            temp_model = main_models.DescribeDcdnWafDomainDetailResponseBodyDomain()
            self.domain = temp_model.from_map(m.get('Domain'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeDcdnWafDomainDetailResponseBodyDomain(DaraModel):
    def __init__(
        self,
        defense_scenes: List[main_models.DescribeDcdnWafDomainDetailResponseBodyDomainDefenseScenes] = None,
        domain_name: str = None,
    ):
        # The types of the protection policies.
        self.defense_scenes = defense_scenes
        # The accelerated domain name.
        self.domain_name = domain_name

    def validate(self):
        if self.defense_scenes:
            for v1 in self.defense_scenes:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DefenseScenes'] = []
        if self.defense_scenes is not None:
            for k1 in self.defense_scenes:
                result['DefenseScenes'].append(k1.to_map() if k1 else None)

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.defense_scenes = []
        if m.get('DefenseScenes') is not None:
            for k1 in m.get('DefenseScenes'):
                temp_model = main_models.DescribeDcdnWafDomainDetailResponseBodyDomainDefenseScenes()
                self.defense_scenes.append(temp_model.from_map(k1))

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        return self

class DescribeDcdnWafDomainDetailResponseBodyDomainDefenseScenes(DaraModel):
    def __init__(
        self,
        defense_scene: str = None,
        policy_id: int = None,
        policy_ids: str = None,
    ):
        # The type of the protection policy. Valid values:
        # 
        # *   waf_group: basic web protection
        # *   custom_acl: custom protection
        # *   whitelist: whitelist
        self.defense_scene = defense_scene
        # The ID of the protection policy.
        self.policy_id = policy_id
        # The IDs of the protection policy.
        self.policy_ids = policy_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.defense_scene is not None:
            result['DefenseScene'] = self.defense_scene

        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id

        if self.policy_ids is not None:
            result['PolicyIds'] = self.policy_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefenseScene') is not None:
            self.defense_scene = m.get('DefenseScene')

        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')

        if m.get('PolicyIds') is not None:
            self.policy_ids = m.get('PolicyIds')

        return self

