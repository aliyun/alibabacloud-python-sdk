# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateSkillDraftRequest(DaraModel):
    def __init__(
        self,
        based_on_version: str = None,
        commit_msg: str = None,
        namespace_id: str = None,
        skill_card: str = None,
        skill_name: str = None,
        target_version: str = None,
    ):
        self.based_on_version = based_on_version
        self.commit_msg = commit_msg
        # This parameter is required.
        self.namespace_id = namespace_id
        self.skill_card = skill_card
        # This parameter is required.
        self.skill_name = skill_name
        self.target_version = target_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.based_on_version is not None:
            result['BasedOnVersion'] = self.based_on_version

        if self.commit_msg is not None:
            result['CommitMsg'] = self.commit_msg

        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id

        if self.skill_card is not None:
            result['SkillCard'] = self.skill_card

        if self.skill_name is not None:
            result['SkillName'] = self.skill_name

        if self.target_version is not None:
            result['TargetVersion'] = self.target_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BasedOnVersion') is not None:
            self.based_on_version = m.get('BasedOnVersion')

        if m.get('CommitMsg') is not None:
            self.commit_msg = m.get('CommitMsg')

        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')

        if m.get('SkillCard') is not None:
            self.skill_card = m.get('SkillCard')

        if m.get('SkillName') is not None:
            self.skill_name = m.get('SkillName')

        if m.get('TargetVersion') is not None:
            self.target_version = m.get('TargetVersion')

        return self

