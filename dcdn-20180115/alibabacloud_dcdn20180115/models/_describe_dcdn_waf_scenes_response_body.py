# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dcdn20180115 import models as main_models
from darabonba.model import DaraModel

class DescribeDcdnWafScenesResponseBody(DaraModel):
    def __init__(
        self,
        defense_scenes: List[main_models.DescribeDcdnWafScenesResponseBodyDefenseScenes] = None,
        request_id: str = None,
    ):
        # The types of the protection policies.
        self.defense_scenes = defense_scenes
        # The ID of the request.
        self.request_id = request_id

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

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.defense_scenes = []
        if m.get('DefenseScenes') is not None:
            for k1 in m.get('DefenseScenes'):
                temp_model = main_models.DescribeDcdnWafScenesResponseBodyDefenseScenes()
                self.defense_scenes.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeDcdnWafScenesResponseBodyDefenseScenes(DaraModel):
    def __init__(
        self,
        defense_scene: str = None,
        policy_count: int = None,
        rule_count: int = None,
    ):
        # The type of the protection policy, which is the same as the DefenseScenes parameter in request parameters.
        self.defense_scene = defense_scene
        # The total number of policies of this type that were configured.
        self.policy_count = policy_count
        # The total number of protection rules that were configured in this type of the policy.
        self.rule_count = rule_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.defense_scene is not None:
            result['DefenseScene'] = self.defense_scene

        if self.policy_count is not None:
            result['PolicyCount'] = self.policy_count

        if self.rule_count is not None:
            result['RuleCount'] = self.rule_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefenseScene') is not None:
            self.defense_scene = m.get('DefenseScene')

        if m.get('PolicyCount') is not None:
            self.policy_count = m.get('PolicyCount')

        if m.get('RuleCount') is not None:
            self.rule_count = m.get('RuleCount')

        return self

