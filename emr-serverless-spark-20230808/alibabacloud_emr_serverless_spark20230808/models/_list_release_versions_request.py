# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListReleaseVersionsRequest(DaraModel):
    def __init__(
        self,
        region_id: str = None,
        release_type: str = None,
        release_version: str = None,
        release_version_status: str = None,
        service_filter: str = None,
        workspace_id: str = None,
    ):
        # The region ID.
        self.region_id = region_id
        # The type of the version.
        # 
        # Valid values:
        # 
        # *   stable
        # *   Beta
        self.release_type = release_type
        # The version of EMR Serverless Spark.
        self.release_version = release_version
        # The status of the version.
        # 
        # Valid values:
        # 
        # *   ONLINE
        # *   OFFLINE
        self.release_version_status = release_version_status
        self.service_filter = service_filter
        # The workspace ID.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region_id is not None:
            result['regionId'] = self.region_id

        if self.release_type is not None:
            result['releaseType'] = self.release_type

        if self.release_version is not None:
            result['releaseVersion'] = self.release_version

        if self.release_version_status is not None:
            result['releaseVersionStatus'] = self.release_version_status

        if self.service_filter is not None:
            result['serviceFilter'] = self.service_filter

        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('releaseType') is not None:
            self.release_type = m.get('releaseType')

        if m.get('releaseVersion') is not None:
            self.release_version = m.get('releaseVersion')

        if m.get('releaseVersionStatus') is not None:
            self.release_version_status = m.get('releaseVersionStatus')

        if m.get('serviceFilter') is not None:
            self.service_filter = m.get('serviceFilter')

        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')

        return self

