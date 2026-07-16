# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreateSkillRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        oss_url: str = None,
        skill_description: str = None,
        skill_display_name: str = None,
        skill_labels: List[str] = None,
        skill_name: str = None,
        skill_space_id: str = None,
        source_skill_id: str = None,
        source_type: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The value of **ClientToken** can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The OSS URL of the Skill package to upload. This parameter is required when SourceType is set to UPLOAD.
        self.oss_url = oss_url
        # The Skill description.
        self.skill_description = skill_description
        self.skill_display_name = skill_display_name
        # The Skill labels.
        self.skill_labels = skill_labels
        # The Skill name.
        self.skill_name = skill_name
        # The ID of the SkillSpace to which the Skill belongs.
        # 
        # This parameter is required.
        self.skill_space_id = skill_space_id
        # The public Skill ID. This parameter is required when SourceType is set to COPY.
        self.source_skill_id = source_skill_id
        # The source type used when creating the Skill.
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

        if self.skill_display_name is not None:
            result['SkillDisplayName'] = self.skill_display_name

        if self.skill_labels is not None:
            result['SkillLabels'] = self.skill_labels

        if self.skill_name is not None:
            result['SkillName'] = self.skill_name

        if self.skill_space_id is not None:
            result['SkillSpaceId'] = self.skill_space_id

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

        if m.get('SkillDisplayName') is not None:
            self.skill_display_name = m.get('SkillDisplayName')

        if m.get('SkillLabels') is not None:
            self.skill_labels = m.get('SkillLabels')

        if m.get('SkillName') is not None:
            self.skill_name = m.get('SkillName')

        if m.get('SkillSpaceId') is not None:
            self.skill_space_id = m.get('SkillSpaceId')

        if m.get('SourceSkillId') is not None:
            self.source_skill_id = m.get('SourceSkillId')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        return self

