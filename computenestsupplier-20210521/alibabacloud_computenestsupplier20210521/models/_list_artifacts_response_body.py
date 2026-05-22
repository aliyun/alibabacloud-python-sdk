# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_computenestsupplier20210521 import models as main_models
from darabonba.model import DaraModel

class ListArtifactsResponseBody(DaraModel):
    def __init__(
        self,
        artifacts: List[main_models.ListArtifactsResponseBodyArtifacts] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The information about deployment packages.
        self.artifacts = artifacts
        # The number of entries per page. Valid values: 1 to 100. Default value: 20.
        self.max_results = max_results
        # The returned value of NextToken is a pagination token, which can be used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.artifacts:
            for v1 in self.artifacts:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Artifacts'] = []
        if self.artifacts is not None:
            for k1 in self.artifacts:
                result['Artifacts'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.artifacts = []
        if m.get('Artifacts') is not None:
            for k1 in m.get('Artifacts'):
                temp_model = main_models.ListArtifactsResponseBodyArtifacts()
                self.artifacts.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListArtifactsResponseBodyArtifacts(DaraModel):
    def __init__(
        self,
        artifact_build_property: str = None,
        artifact_id: str = None,
        artifact_type: str = None,
        description: str = None,
        gmt_modified: str = None,
        max_version: str = None,
        name: str = None,
        permission_type: str = None,
        resource_group_id: str = None,
        status: str = None,
        tags: List[main_models.ListArtifactsResponseBodyArtifactsTags] = None,
    ):
        # The build properties of the artifact, utilized for hosting and building the deployment package.
        self.artifact_build_property = artifact_build_property
        # The ID of the deployment package.
        self.artifact_id = artifact_id
        # The type of the deployment package.
        self.artifact_type = artifact_type
        # The description of the deployment package.
        self.description = description
        # The time when the deployment package was modified.
        self.gmt_modified = gmt_modified
        # The latest version of the deployment package.
        self.max_version = max_version
        # The name of the deployment package.
        self.name = name
        # Permission fields are applicable to container image artifact and Helm Chart artifact They can only change from Automatic to Public. Options:
        # - Public
        # - Automatic
        self.permission_type = permission_type
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The status of the deployment package. Valid values:
        # 
        # *   Created: The deployment package is created.
        # *   Scanning: The deployment package is being scanned.
        # *   ScanFailed: The deployment package failed to be scanned.
        # *   Delivering: The deployment package is being distributed.
        # *   Available: The deployment package is available.
        # *   Deleted: The deployment package is deleted.
        self.status = status
        # The tags.
        self.tags = tags

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

        if self.artifact_id is not None:
            result['ArtifactId'] = self.artifact_id

        if self.artifact_type is not None:
            result['ArtifactType'] = self.artifact_type

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

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.status is not None:
            result['Status'] = self.status

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArtifactBuildProperty') is not None:
            self.artifact_build_property = m.get('ArtifactBuildProperty')

        if m.get('ArtifactId') is not None:
            self.artifact_id = m.get('ArtifactId')

        if m.get('ArtifactType') is not None:
            self.artifact_type = m.get('ArtifactType')

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

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.ListArtifactsResponseBodyArtifactsTags()
                self.tags.append(temp_model.from_map(k1))

        return self

class ListArtifactsResponseBodyArtifactsTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
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

