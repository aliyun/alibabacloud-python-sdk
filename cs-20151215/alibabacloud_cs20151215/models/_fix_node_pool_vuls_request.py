# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cs20151215 import models as main_models
from darabonba.model import DaraModel

class FixNodePoolVulsRequest(DaraModel):
    def __init__(
        self,
        auto_restart: bool = None,
        nodes: List[str] = None,
        rollout_policy: main_models.FixNodePoolVulsRequestRolloutPolicy = None,
        vuls: List[str] = None,
    ):
        # Specifies whether to allow the nodes to restart.
        self.auto_restart = auto_restart
        # The names of the nodes to be patched.
        self.nodes = nodes
        # The batch patching policy.
        self.rollout_policy = rollout_policy
        # The list of vulnerabilities.
        self.vuls = vuls

    def validate(self):
        if self.rollout_policy:
            self.rollout_policy.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_restart is not None:
            result['auto_restart'] = self.auto_restart

        if self.nodes is not None:
            result['nodes'] = self.nodes

        if self.rollout_policy is not None:
            result['rollout_policy'] = self.rollout_policy.to_map()

        if self.vuls is not None:
            result['vuls'] = self.vuls

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auto_restart') is not None:
            self.auto_restart = m.get('auto_restart')

        if m.get('nodes') is not None:
            self.nodes = m.get('nodes')

        if m.get('rollout_policy') is not None:
            temp_model = main_models.FixNodePoolVulsRequestRolloutPolicy()
            self.rollout_policy = temp_model.from_map(m.get('rollout_policy'))

        if m.get('vuls') is not None:
            self.vuls = m.get('vuls')

        return self

class FixNodePoolVulsRequestRolloutPolicy(DaraModel):
    def __init__(
        self,
        max_parallelism: int = None,
    ):
        # The maximum concurrency for batch patching. Minimum value: 1. The maximum value equals the number of nodes in the node pool.
        self.max_parallelism = max_parallelism

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_parallelism is not None:
            result['max_parallelism'] = self.max_parallelism

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('max_parallelism') is not None:
            self.max_parallelism = m.get('max_parallelism')

        return self

