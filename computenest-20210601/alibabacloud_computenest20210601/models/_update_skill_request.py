# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UpdateSkillRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        oss_url: str = None,
        skill_description: str = None,
        skill_id: str = None,
        skill_labels: List[str] = None,
        skill_name: str = None,
        source_skill_id: str = None,
        source_type: str = None,
    ):
        # A unique, client-generated token to ensure request idempotence. **ClientToken** can contain only ASCII characters and must not exceed 64 characters in length.
        self.client_token = client_token
        # This parameter is required if `SourceType` is set to `UPLOAD`. It specifies the Object Storage Service (OSS) URL of the compressed skill package to upload.
        self.oss_url = oss_url
        # The skill description.
        self.skill_description = skill_description
        # The ID of the skill to update.
        # 
        # This parameter is required.
        self.skill_id = skill_id
        # An array of skill labels.
        self.skill_labels = skill_labels
        # The skill name.
        self.skill_name = skill_name
        # This parameter is required if `SourceType` is set to `COPY`. It specifies the ID of the public skill.
        self.source_skill_id = source_skill_id
        # The source type for the skill update.
        # 
        # This parameter is required.
        self.source_type = source_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.oss_url is not None:
            result['OssUrl'] = self.oss_url

        if self.skill_description is not None:
            result['SkillDescription'] = self.skill_description

        if self.skill_id is not None:
            result['SkillId'] = self.skill_id

        if self.skill_labels is not None:
            result['SkillLabels'] = self.skill_labels

        if self.skill_name is not None:
            result['SkillName'] = self.skill_name

        if self.source_skill_id is not None:
            result['SourceSkillId'] = self.source_skill_id

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('OssUrl') is not None:
            self.oss_url = m.get('OssUrl')

        if m.get('SkillDescription') is not None:
            self.skill_description = m.get('SkillDescription')

        if m.get('SkillId') is not None:
            self.skill_id = m.get('SkillId')

        if m.get('SkillLabels') is not None:
            self.skill_labels = m.get('SkillLabels')

        if m.get('SkillName') is not None:
            self.skill_name = m.get('SkillName')

        if m.get('SourceSkillId') is not None:
            self.source_skill_id = m.get('SourceSkillId')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        return self

