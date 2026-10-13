# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetSkillRequest(DaraModel):
    def __init__(
        self,
        download: bool = None,
        language: str = None,
        path: str = None,
        skill_id: str = None,
        version_id: str = None,
        workspace_id: str = None,
    ):
        # Specifies whether to obtain a temporary download URL for the specified version. Default value: false.
        self.download = download
        # The supported language. Valid values:
        # * zh-CN: Simplified Chinese
        # * zh-TW: Traditional Chinese
        # * en-US: English
        # * ja-JP: Japanese
        self.language = language
        # The file path within the package, such as SKILL.md. The body is in File.text, and the full Markdown is in SkillMarkdown.
        self.path = path
        # The unique identifier of the skill.
        # 
        # This parameter is required.
        self.skill_id = skill_id
        # The version UUID (Versions[].Id), not a version number such as 1.0.0. If omitted, the currently active version is read.
        self.version_id = version_id
        # The ContextDB workspace ID.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.download is not None:
            result['Download'] = self.download

        if self.language is not None:
            result['Language'] = self.language

        if self.path is not None:
            result['Path'] = self.path

        if self.skill_id is not None:
            result['SkillId'] = self.skill_id

        if self.version_id is not None:
            result['VersionId'] = self.version_id

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Download') is not None:
            self.download = m.get('Download')

        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('Path') is not None:
            self.path = m.get('Path')

        if m.get('SkillId') is not None:
            self.skill_id = m.get('SkillId')

        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

