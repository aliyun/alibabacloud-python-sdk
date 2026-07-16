# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateArtifactResponseBody(DaraModel):
    def __init__(
        self,
        artifact_build_property: str = None,
        artifact_build_type: str = None,
        artifact_id: str = None,
        artifact_property: str = None,
        artifact_type: str = None,
        artifact_version: str = None,
        description: str = None,
        gmt_modified: str = None,
        max_version: int = None,
        name: str = None,
        request_id: str = None,
        status: str = None,
        status_detail: str = None,
        support_region_ids: str = None,
        version_name: str = None,
    ):
        # The content used to build the artifact. This parameter is used for managed artifact builds.
        self.artifact_build_property = artifact_build_property
        # The type of the built artifact.
        self.artifact_build_type = artifact_build_type
        # The artifact ID.
        self.artifact_id = artifact_id
        # The content of the artifact.
        self.artifact_property = artifact_property
        # The artifact type.
        self.artifact_type = artifact_type
        # The artifact version.
        self.artifact_version = artifact_version
        # The description of the artifact.
        self.description = description
        # The time when the artifact was modified.
        self.gmt_modified = gmt_modified
        # The latest version of the artifact.
        self.max_version = max_version
        # The artifact name.
        self.name = name
        # The request ID.
        self.request_id = request_id
        # The status of the artifact.
        self.status = status
        # The description of the artifact status.
        self.status_detail = status_detail
        # The IDs of the regions to which the artifact is distributed.
        self.support_region_ids = support_region_ids
        # The name of the artifact version.
        self.version_name = version_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.artifact_build_property is not None:
            result['ArtifactBuildProperty'] = self.artifact_build_property

        if self.artifact_build_type is not None:
            result['ArtifactBuildType'] = self.artifact_build_type

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

        if self.max_version is not None:
            result['MaxVersion'] = self.max_version

        if self.name is not None:
            result['Name'] = self.name

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status is not None:
            result['Status'] = self.status

        if self.status_detail is not None:
            result['StatusDetail'] = self.status_detail

        if self.support_region_ids is not None:
            result['SupportRegionIds'] = self.support_region_ids

        if self.version_name is not None:
            result['VersionName'] = self.version_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArtifactBuildProperty') is not None:
            self.artifact_build_property = m.get('ArtifactBuildProperty')

        if m.get('ArtifactBuildType') is not None:
            self.artifact_build_type = m.get('ArtifactBuildType')

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

        if m.get('MaxVersion') is not None:
            self.max_version = m.get('MaxVersion')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StatusDetail') is not None:
            self.status_detail = m.get('StatusDetail')

        if m.get('SupportRegionIds') is not None:
            self.support_region_ids = m.get('SupportRegionIds')

        if m.get('VersionName') is not None:
            self.version_name = m.get('VersionName')

        return self

