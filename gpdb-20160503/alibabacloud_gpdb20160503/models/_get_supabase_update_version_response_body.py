# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetSupabaseUpdateVersionResponseBody(DaraModel):
    def __init__(
        self,
        latest_version: str = None,
        project_id: str = None,
        request_id: str = None,
        stable_version: str = None,
    ):
        # The latest upgradable version.
        self.latest_version = latest_version
        # The ID of the Supabase project.
        self.project_id = project_id
        # The request ID.
        self.request_id = request_id
        # The recommended stable version for upgrade.
        self.stable_version = stable_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.latest_version is not None:
            result['LatestVersion'] = self.latest_version

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.stable_version is not None:
            result['StableVersion'] = self.stable_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LatestVersion') is not None:
            self.latest_version = m.get('LatestVersion')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StableVersion') is not None:
            self.stable_version = m.get('StableVersion')

        return self

