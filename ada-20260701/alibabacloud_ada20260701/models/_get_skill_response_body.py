# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Any

from darabonba.model import DaraModel

class GetSkillResponseBody(DaraModel):
    def __init__(
        self,
        can_delete: bool = None,
        can_modify: bool = None,
        created_at: int = None,
        description: str = None,
        download_url: str = None,
        download_url_network: str = None,
        icon_url: str = None,
        metadata: Any = None,
        name: str = None,
        official: bool = None,
        request_id: str = None,
        skill_id: str = None,
        status: str = None,
        updated_at: int = None,
        visibility: str = None,
    ):
        # Indicates whether the current caller can delete the Skill.
        self.can_delete = can_delete
        # Indicates whether the current caller can modify the Skill.
        self.can_modify = can_modify
        # The creation time of the Skill, in Unix millisecond timestamp.
        self.created_at = created_at
        # The description in the current Skill main record.
        self.description = description
        # The bundle download URL. Returned when a network type is specified, an accessible Artifact exists, and pre-signing succeeds.
        self.download_url = download_url
        # The network type used to generate the download URL.
        self.download_url_network = download_url_network
        # The Skill icon URL, sourced from the iconUrl in the metadata. This field may be empty if no icon is configured.
        self.icon_url = icon_url
        # The Skill metadata, mapped to the metadata field in the backend response.
        self.metadata = metadata
        # The Skill name.
        self.name = name
        # Indicates whether the Skill is an official Skill.
        self.official = official
        # The request ID, used for Tracing Analysis and troubleshooting.
        self.request_id = request_id
        # Skill ID。
        self.skill_id = skill_id
        # The current Skill status. Common values are DRAFT and PUBLISHED.
        self.status = status
        # The update time of the Skill, in Unix millisecond timestamp.
        self.updated_at = updated_at
        # The visibility of the current Skill. Common values are user and tenant.
        self.visibility = visibility

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.can_delete is not None:
            result['CanDelete'] = self.can_delete

        if self.can_modify is not None:
            result['CanModify'] = self.can_modify

        if self.created_at is not None:
            result['CreatedAt'] = self.created_at

        if self.description is not None:
            result['Description'] = self.description

        if self.download_url is not None:
            result['DownloadUrl'] = self.download_url

        if self.download_url_network is not None:
            result['DownloadUrlNetwork'] = self.download_url_network

        if self.icon_url is not None:
            result['IconUrl'] = self.icon_url

        if self.metadata is not None:
            result['Metadata'] = self.metadata

        if self.name is not None:
            result['Name'] = self.name

        if self.official is not None:
            result['Official'] = self.official

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.skill_id is not None:
            result['SkillId'] = self.skill_id

        if self.status is not None:
            result['Status'] = self.status

        if self.updated_at is not None:
            result['UpdatedAt'] = self.updated_at

        if self.visibility is not None:
            result['Visibility'] = self.visibility

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CanDelete') is not None:
            self.can_delete = m.get('CanDelete')

        if m.get('CanModify') is not None:
            self.can_modify = m.get('CanModify')

        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DownloadUrl') is not None:
            self.download_url = m.get('DownloadUrl')

        if m.get('DownloadUrlNetwork') is not None:
            self.download_url_network = m.get('DownloadUrlNetwork')

        if m.get('IconUrl') is not None:
            self.icon_url = m.get('IconUrl')

        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Official') is not None:
            self.official = m.get('Official')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SkillId') is not None:
            self.skill_id = m.get('SkillId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UpdatedAt') is not None:
            self.updated_at = m.get('UpdatedAt')

        if m.get('Visibility') is not None:
            self.visibility = m.get('Visibility')

        return self

