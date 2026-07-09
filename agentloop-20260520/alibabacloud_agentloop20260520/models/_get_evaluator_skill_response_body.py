# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agentloop20260520 import models as main_models
from darabonba.model import DaraModel

class GetEvaluatorSkillResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        skill: main_models.GetEvaluatorSkillResponseBodySkill = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The skill details.
        self.skill = skill

    def validate(self):
        if self.skill:
            self.skill.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.skill is not None:
            result['skill'] = self.skill.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('skill') is not None:
            temp_model = main_models.GetEvaluatorSkillResponseBodySkill()
            self.skill = temp_model.from_map(m.get('skill'))

        return self

class GetEvaluatorSkillResponseBodySkill(DaraModel):
    def __init__(
        self,
        created_at: int = None,
        current_version: str = None,
        description: str = None,
        display_name: str = None,
        enable: bool = None,
        files: List[main_models.GetEvaluatorSkillResponseBodySkillFiles] = None,
        latest_version: str = None,
        skill_name: str = None,
        updated_at: int = None,
        versions: List[main_models.GetEvaluatorSkillResponseBodySkillVersions] = None,
    ):
        # The time when the skill was created. This value is a UNIX timestamp in seconds.
        self.created_at = created_at
        # The current version.
        self.current_version = current_version
        # The skill description.
        self.description = description
        # The display name.
        self.display_name = display_name
        # Indicates whether the skill is enabled.
        self.enable = enable
        # The list of skill files.
        self.files = files
        # The latest version.
        self.latest_version = latest_version
        # The skill name.
        self.skill_name = skill_name
        # The time when the skill was last updated. This value is a UNIX timestamp in seconds.
        self.updated_at = updated_at
        # The list of skill versions.
        self.versions = versions

    def validate(self):
        if self.files:
            for v1 in self.files:
                 if v1:
                    v1.validate()
        if self.versions:
            for v1 in self.versions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.current_version is not None:
            result['currentVersion'] = self.current_version

        if self.description is not None:
            result['description'] = self.description

        if self.display_name is not None:
            result['displayName'] = self.display_name

        if self.enable is not None:
            result['enable'] = self.enable

        result['files'] = []
        if self.files is not None:
            for k1 in self.files:
                result['files'].append(k1.to_map() if k1 else None)

        if self.latest_version is not None:
            result['latestVersion'] = self.latest_version

        if self.skill_name is not None:
            result['skillName'] = self.skill_name

        if self.updated_at is not None:
            result['updatedAt'] = self.updated_at

        result['versions'] = []
        if self.versions is not None:
            for k1 in self.versions:
                result['versions'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('currentVersion') is not None:
            self.current_version = m.get('currentVersion')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')

        if m.get('enable') is not None:
            self.enable = m.get('enable')

        self.files = []
        if m.get('files') is not None:
            for k1 in m.get('files'):
                temp_model = main_models.GetEvaluatorSkillResponseBodySkillFiles()
                self.files.append(temp_model.from_map(k1))

        if m.get('latestVersion') is not None:
            self.latest_version = m.get('latestVersion')

        if m.get('skillName') is not None:
            self.skill_name = m.get('skillName')

        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')

        self.versions = []
        if m.get('versions') is not None:
            for k1 in m.get('versions'):
                temp_model = main_models.GetEvaluatorSkillResponseBodySkillVersions()
                self.versions.append(temp_model.from_map(k1))

        return self

class GetEvaluatorSkillResponseBodySkillVersions(DaraModel):
    def __init__(
        self,
        created_at: int = None,
        version: str = None,
        version_description: str = None,
    ):
        # The time when the version was created. This value is a UNIX timestamp in seconds.
        self.created_at = created_at
        # The version number.
        self.version = version
        # The version description.
        self.version_description = version_description

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.version is not None:
            result['version'] = self.version

        if self.version_description is not None:
            result['versionDescription'] = self.version_description

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('version') is not None:
            self.version = m.get('version')

        if m.get('versionDescription') is not None:
            self.version_description = m.get('versionDescription')

        return self

class GetEvaluatorSkillResponseBodySkillFiles(DaraModel):
    def __init__(
        self,
        content: str = None,
        name: str = None,
        remark: str = None,
    ):
        # The file content.
        self.content = content
        # The file name.
        self.name = name
        # The file remarks.
        self.remark = remark

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['content'] = self.content

        if self.name is not None:
            result['name'] = self.name

        if self.remark is not None:
            result['remark'] = self.remark

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('remark') is not None:
            self.remark = m.get('remark')

        return self

