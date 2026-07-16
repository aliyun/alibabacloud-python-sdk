# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_computenestsupplier20210521 import models as main_models
from darabonba.model import DaraModel

class GetArtifactResponseBody(DaraModel):
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
        permission_type: str = None,
        progress: str = None,
        request_id: str = None,
        resource_group_id: str = None,
        status: str = None,
        status_detail: str = None,
        support_region_ids: str = None,
        tags: List[main_models.GetArtifactResponseBodyTags] = None,
        version_name: str = None,
    ):
        # The content used to build the artifact. This parameter is used for managed artifact builds.
        self.artifact_build_property = artifact_build_property
        # The type of the artifact build.
        self.artifact_build_type = artifact_build_type
        # The ID of the artifact.
        self.artifact_id = artifact_id
        # The properties of the artifact.
        self.artifact_property = artifact_property
        # The type of the artifact.
        self.artifact_type = artifact_type
        # The version of the artifact.
        self.artifact_version = artifact_version
        # The description of the artifact.
        self.description = description
        # The time when the artifact was last modified.
        self.gmt_modified = gmt_modified
        # The latest version of the artifact.
        self.max_version = max_version
        # The name of the artifact.
        self.name = name
        # The permission type. This parameter is valid for artifacts of the ContainerImage and HelmChart types. Valid values:
        # 
        # - Public
        # 
        # - Automatic
        self.permission_type = permission_type
        # The distribution progress of the artifact.
        self.progress = progress
        # The request ID.
        self.request_id = request_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The status of the artifact.
        self.status = status
        # The description of the artifact status.
        self.status_detail = status_detail
        # The IDs of the regions where the artifact is supported.
        self.support_region_ids = support_region_ids
        # The tags of the artifact.
        self.tags = tags
        # The version name of the artifact.
        self.version_name = version_name

    def validate(self):
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

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

        if self.permission_type is not None:
            result['PermissionType'] = self.permission_type

        if self.progress is not None:
            result['Progress'] = self.progress

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.status is not None:
            result['Status'] = self.status

        if self.status_detail is not None:
            result['StatusDetail'] = self.status_detail

        if self.support_region_ids is not None:
            result['SupportRegionIds'] = self.support_region_ids

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

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

        if m.get('PermissionType') is not None:
            self.permission_type = m.get('PermissionType')

        if m.get('Progress') is not None:
            self.progress = m.get('Progress')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StatusDetail') is not None:
            self.status_detail = m.get('StatusDetail')

        if m.get('SupportRegionIds') is not None:
            self.support_region_ids = m.get('SupportRegionIds')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.GetArtifactResponseBodyTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('VersionName') is not None:
            self.version_name = m.get('VersionName')

        return self

class GetArtifactResponseBodyTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key of the artifact.
        self.key = key
        # The tag value of the artifact.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

