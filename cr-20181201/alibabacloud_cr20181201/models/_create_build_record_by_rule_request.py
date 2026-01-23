# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateBuildRecordByRuleRequest(DaraModel):
    def __init__(
        self,
        build_rule_id: str = None,
        instance_id: str = None,
        repo_id: str = None,
    ):
        # The ID of the image building rule.
        # 
        # This parameter is required.
        self.build_rule_id = build_rule_id
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The ID of the image repository.
        # 
        # This parameter is required.
        self.repo_id = repo_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.build_rule_id is not None:
            result['BuildRuleId'] = self.build_rule_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.repo_id is not None:
            result['RepoId'] = self.repo_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BuildRuleId') is not None:
            self.build_rule_id = m.get('BuildRuleId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')

        return self

