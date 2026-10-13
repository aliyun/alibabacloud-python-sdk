# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any, List

from darabonba.model import DaraModel

class UpdateSkillResponseBody(DaraModel):
    def __init__(
        self,
        action: str = None,
        bundle_hash: str = None,
        content: Dict[str, Any] = None,
        dbtypes: List[str] = None,
        description: str = None,
        id: str = None,
        name: str = None,
        request_id: str = None,
        skill_id: str = None,
        skill_type: str = None,
        updated_at: str = None,
        version_id: str = None,
    ):
        # The update action performed.
        self.action = action
        # The content digest of the Skill package.
        self.bundle_hash = bundle_hash
        # The content.
        self.content = content
        # The list of database types.
        self.dbtypes = dbtypes
        # The description of the Skill. The description can be up to 1000 characters in length.
        self.description = description
        # The unique identifier of the Skill.
        self.id = id
        # The name of the Skill. The name can contain only lowercase letters, digits, and hyphens.
        self.name = name
        # The unique identifier of the request.
        self.request_id = request_id
        # The ID of the updated Skill.
        self.skill_id = skill_id
        # The Skill type.
        self.skill_type = skill_type
        # The time when the Skill was updated.
        self.updated_at = updated_at
        # The ID of the Skill version created in this update.
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['Action'] = self.action

        if self.bundle_hash is not None:
            result['BundleHash'] = self.bundle_hash

        if self.content is not None:
            result['Content'] = self.content

        if self.dbtypes is not None:
            result['Dbtypes'] = self.dbtypes

        if self.description is not None:
            result['Description'] = self.description

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.skill_id is not None:
            result['SkillId'] = self.skill_id

        if self.skill_type is not None:
            result['SkillType'] = self.skill_type

        if self.updated_at is not None:
            result['UpdatedAt'] = self.updated_at

        if self.version_id is not None:
            result['VersionId'] = self.version_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')

        if m.get('BundleHash') is not None:
            self.bundle_hash = m.get('BundleHash')

        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('Dbtypes') is not None:
            self.dbtypes = m.get('Dbtypes')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SkillId') is not None:
            self.skill_id = m.get('SkillId')

        if m.get('SkillType') is not None:
            self.skill_type = m.get('SkillType')

        if m.get('UpdatedAt') is not None:
            self.updated_at = m.get('UpdatedAt')

        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')

        return self

