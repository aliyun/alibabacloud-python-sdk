# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PublicTemplateCache(DaraModel):
    def __init__(
        self,
        created_time: str = None,
        image_digest: str = None,
        image_size_mb: int = None,
        progress: int = None,
        ready_time: str = None,
        status: str = None,
        status_reason: str = None,
        team_id: str = None,
        template_id: str = None,
    ):
        # The creation time in UTC.
        self.created_time = created_time
        # The digest of the cached image.
        self.image_digest = image_digest
        # The size of the cached image. Unit: MB.
        self.image_size_mb = image_size_mb
        # The prefetch progress percentage.
        self.progress = progress
        # The ready time in UTC.
        self.ready_time = ready_time
        # The cache status. Valid values: InProgress, Success, Failed, Deleting, and Evicted.
        self.status = status
        # The reason for the status. This parameter is backfilled when the status is not Success.
        self.status_reason = status_reason
        # The team ID.
        self.team_id = team_id
        # The unique identifier of the template.
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_time is not None:
            result['createdTime'] = self.created_time

        if self.image_digest is not None:
            result['imageDigest'] = self.image_digest

        if self.image_size_mb is not None:
            result['imageSizeMB'] = self.image_size_mb

        if self.progress is not None:
            result['progress'] = self.progress

        if self.ready_time is not None:
            result['readyTime'] = self.ready_time

        if self.status is not None:
            result['status'] = self.status

        if self.status_reason is not None:
            result['statusReason'] = self.status_reason

        if self.team_id is not None:
            result['teamID'] = self.team_id

        if self.template_id is not None:
            result['templateID'] = self.template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')

        if m.get('imageDigest') is not None:
            self.image_digest = m.get('imageDigest')

        if m.get('imageSizeMB') is not None:
            self.image_size_mb = m.get('imageSizeMB')

        if m.get('progress') is not None:
            self.progress = m.get('progress')

        if m.get('readyTime') is not None:
            self.ready_time = m.get('readyTime')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('statusReason') is not None:
            self.status_reason = m.get('statusReason')

        if m.get('teamID') is not None:
            self.team_id = m.get('teamID')

        if m.get('templateID') is not None:
            self.template_id = m.get('templateID')

        return self

