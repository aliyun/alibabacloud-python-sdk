# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateSkillShrinkRequest(DaraModel):
    def __init__(
        self,
        bundle_url: str = None,
        description: str = None,
        extra_shrink: str = None,
        name: str = None,
        skill_md_override: str = None,
        version_note: str = None,
        visibility: str = None,
        visibility_scope_shrink: str = None,
    ):
        self.bundle_url = bundle_url
        self.description = description
        self.extra_shrink = extra_shrink
        # This parameter is required.
        self.name = name
        self.skill_md_override = skill_md_override
        self.version_note = version_note
        self.visibility = visibility
        self.visibility_scope_shrink = visibility_scope_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bundle_url is not None:
            result['BundleUrl'] = self.bundle_url

        if self.description is not None:
            result['Description'] = self.description

        if self.extra_shrink is not None:
            result['Extra'] = self.extra_shrink

        if self.name is not None:
            result['Name'] = self.name

        if self.skill_md_override is not None:
            result['SkillMdOverride'] = self.skill_md_override

        if self.version_note is not None:
            result['VersionNote'] = self.version_note

        if self.visibility is not None:
            result['Visibility'] = self.visibility

        if self.visibility_scope_shrink is not None:
            result['VisibilityScope'] = self.visibility_scope_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BundleUrl') is not None:
            self.bundle_url = m.get('BundleUrl')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Extra') is not None:
            self.extra_shrink = m.get('Extra')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('SkillMdOverride') is not None:
            self.skill_md_override = m.get('SkillMdOverride')

        if m.get('VersionNote') is not None:
            self.version_note = m.get('VersionNote')

        if m.get('Visibility') is not None:
            self.visibility = m.get('Visibility')

        if m.get('VisibilityScope') is not None:
            self.visibility_scope_shrink = m.get('VisibilityScope')

        return self

