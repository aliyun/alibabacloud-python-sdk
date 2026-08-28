# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agentcore20260804 import models as main_models
from darabonba.model import DaraModel

class PrecheckSkillUploadViaOssResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.PrecheckSkillUploadViaOssResponseBodyData] = None,
        request_id: str = None,
    ):
        # The returned data.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['data'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k1 in m.get('data'):
                temp_model = main_models.PrecheckSkillUploadViaOssResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class PrecheckSkillUploadViaOssResponseBodyData(DaraModel):
    def __init__(
        self,
        editing_version: str = None,
        entry_path: str = None,
        exists: bool = None,
        max_published_version: str = None,
        owner: str = None,
        parsed_version: str = None,
        precheck_code: str = None,
        reason: str = None,
        reviewing_version: str = None,
        skill_name: str = None,
        target_version: str = None,
        workspace_id: str = None,
    ):
        # The version currently being edited.
        self.editing_version = editing_version
        # The entry path of the Skill package.
        self.entry_path = entry_path
        # Indicates whether the Skill already exists.
        self.exists = exists
        # The highest published version.
        self.max_published_version = max_published_version
        # The resource owner.
        self.owner = owner
        # The version parsed from the uploaded content.
        self.parsed_version = parsed_version
        # The pre-check result code.
        self.precheck_code = precheck_code
        # The reason description.
        self.reason = reason
        # The version currently under review.
        self.reviewing_version = reviewing_version
        # The Skill name.
        self.skill_name = skill_name
        # The target version.
        self.target_version = target_version
        # The workspace ID.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.editing_version is not None:
            result['editingVersion'] = self.editing_version

        if self.entry_path is not None:
            result['entryPath'] = self.entry_path

        if self.exists is not None:
            result['exists'] = self.exists

        if self.max_published_version is not None:
            result['maxPublishedVersion'] = self.max_published_version

        if self.owner is not None:
            result['owner'] = self.owner

        if self.parsed_version is not None:
            result['parsedVersion'] = self.parsed_version

        if self.precheck_code is not None:
            result['precheckCode'] = self.precheck_code

        if self.reason is not None:
            result['reason'] = self.reason

        if self.reviewing_version is not None:
            result['reviewingVersion'] = self.reviewing_version

        if self.skill_name is not None:
            result['skillName'] = self.skill_name

        if self.target_version is not None:
            result['targetVersion'] = self.target_version

        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('editingVersion') is not None:
            self.editing_version = m.get('editingVersion')

        if m.get('entryPath') is not None:
            self.entry_path = m.get('entryPath')

        if m.get('exists') is not None:
            self.exists = m.get('exists')

        if m.get('maxPublishedVersion') is not None:
            self.max_published_version = m.get('maxPublishedVersion')

        if m.get('owner') is not None:
            self.owner = m.get('owner')

        if m.get('parsedVersion') is not None:
            self.parsed_version = m.get('parsedVersion')

        if m.get('precheckCode') is not None:
            self.precheck_code = m.get('precheckCode')

        if m.get('reason') is not None:
            self.reason = m.get('reason')

        if m.get('reviewingVersion') is not None:
            self.reviewing_version = m.get('reviewingVersion')

        if m.get('skillName') is not None:
            self.skill_name = m.get('skillName')

        if m.get('targetVersion') is not None:
            self.target_version = m.get('targetVersion')

        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')

        return self

