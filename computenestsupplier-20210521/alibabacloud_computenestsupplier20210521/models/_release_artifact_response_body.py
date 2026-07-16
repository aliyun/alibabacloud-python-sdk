# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ReleaseArtifactResponseBody(DaraModel):
    def __init__(
        self,
        artifact_id: str = None,
        artifact_property: str = None,
        artifact_type: str = None,
        artifact_version: str = None,
        description: str = None,
        gmt_modified: str = None,
        request_id: str = None,
        status: str = None,
        version_name: str = None,
    ):
        # The artifact ID.
        self.artifact_id = artifact_id
        # The content of the artifact.
        self.artifact_property = artifact_property
        # The artifact type.
        self.artifact_type = artifact_type
        # The artifact version.
        self.artifact_version = artifact_version
        # The artifact description.
        self.description = description
        # The time when the artifact was last modified.
        self.gmt_modified = gmt_modified
        # The request ID.
        self.request_id = request_id
        # The status of the artifact.
        # 
        # Valid values:
        # 
        # - Created: The artifact is created.
        # 
        # - Scanning: The artifact is being scanned.
        # 
        # - ScanFailed: The artifact failed to be scanned.
        # 
        # - Delivering: The artifact is being distributed.
        # 
        # - Available: The artifact is available.
        # 
        # - Deleted: The artifact is deleted.
        self.status = status
        # The name of the artifact version.
        self.version_name = version_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.artifact_id is not None:
            result['ArtifactId'] = self.artifact_id

        if self.artifact_property is not None:
            result['ArtifactProperty'] = self.artifact_property

        if self.artifact_type is not None:
            result['ArtifactType'] = self.artifact_type

        if self.artifact_version is not None:
            result['ArtifactVersion'] = self.artifact_version

        if self.description is not None:
            result['Description'] = self.description

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status is not None:
            result['Status'] = self.status

        if self.version_name is not None:
            result['VersionName'] = self.version_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArtifactId') is not None:
            self.artifact_id = m.get('ArtifactId')

        if m.get('ArtifactProperty') is not None:
            self.artifact_property = m.get('ArtifactProperty')

        if m.get('ArtifactType') is not None:
            self.artifact_type = m.get('ArtifactType')

        if m.get('ArtifactVersion') is not None:
            self.artifact_version = m.get('ArtifactVersion')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('VersionName') is not None:
            self.version_name = m.get('VersionName')

        return self

