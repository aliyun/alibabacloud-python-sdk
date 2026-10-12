# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any, List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class CreateSkillRequest(DaraModel):
    def __init__(
        self,
        bundle_url: str = None,
        description: str = None,
        extra: Dict[str, Any] = None,
        name: str = None,
        skill_md_override: str = None,
        version_note: str = None,
        visibility: str = None,
        visibility_scope: main_models.CreateSkillRequestVisibilityScope = None,
    ):
        # The **download URL of the bundle.zip file** (HTTP or HTTPS). This parameter and SkillMdOverride are mutually exclusive.
        self.bundle_url = bundle_url
        # The **skill description**.
        self.description = description
        # The extended metadata in key-value pairs.
        self.extra = extra
        # The **skill name**. The name must be unique within the current account.
        # 
        # This parameter is required.
        self.name = name
        # The content of the SKILL.md file. This parameter and BundleUrl are mutually exclusive. If you do not provide a bundle, use this parameter to create a lightweight skill that contains only the SKILL.md file.
        self.skill_md_override = skill_md_override
        # The **version note**.
        self.version_note = version_note
        # The **visibility level**. Valid values: TENANT (visible to the entire tenant), PROJECT (visible to specific projects), and USER (visible to specific users).
        self.visibility = visibility
        # The visibility scope. Specify the corresponding field based on the value of Visibility.
        self.visibility_scope = visibility_scope

    def validate(self):
        if self.visibility_scope:
            self.visibility_scope.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bundle_url is not None:
            result['BundleUrl'] = self.bundle_url

        if self.description is not None:
            result['Description'] = self.description

        if self.extra is not None:
            result['Extra'] = self.extra

        if self.name is not None:
            result['Name'] = self.name

        if self.skill_md_override is not None:
            result['SkillMdOverride'] = self.skill_md_override

        if self.version_note is not None:
            result['VersionNote'] = self.version_note

        if self.visibility is not None:
            result['Visibility'] = self.visibility

        if self.visibility_scope is not None:
            result['VisibilityScope'] = self.visibility_scope.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BundleUrl') is not None:
            self.bundle_url = m.get('BundleUrl')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Extra') is not None:
            self.extra = m.get('Extra')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('SkillMdOverride') is not None:
            self.skill_md_override = m.get('SkillMdOverride')

        if m.get('VersionNote') is not None:
            self.version_note = m.get('VersionNote')

        if m.get('Visibility') is not None:
            self.visibility = m.get('Visibility')

        if m.get('VisibilityScope') is not None:
            temp_model = main_models.CreateSkillRequestVisibilityScope()
            self.visibility_scope = temp_model.from_map(m.get('VisibilityScope'))

        return self

class CreateSkillRequestVisibilityScope(DaraModel):
    def __init__(
        self,
        project_ids: List[str] = None,
        user_ids: List[str] = None,
    ):
        # The IDs of the visible projects. This parameter takes effect only when Visibility is set to PROJECT.
        self.project_ids = project_ids
        # The IDs of the visible users. This parameter takes effect only when Visibility is set to USER.
        self.user_ids = user_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.project_ids is not None:
            result['ProjectIds'] = self.project_ids

        if self.user_ids is not None:
            result['UserIds'] = self.user_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectIds') is not None:
            self.project_ids = m.get('ProjectIds')

        if m.get('UserIds') is not None:
            self.user_ids = m.get('UserIds')

        return self

