# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_computenestsupplier20210521 import models as main_models
from darabonba.model import DaraModel

class ListArtifactVersionsResponseBody(DaraModel):
    def __init__(
        self,
        artifacts: List[main_models.ListArtifactVersionsResponseBodyArtifacts] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The version information about the deployment package.
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
                temp_model = main_models.ListArtifactVersionsResponseBodyArtifacts()
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

class ListArtifactVersionsResponseBodyArtifacts(DaraModel):
    def __init__(
        self,
        artifact_build_property: str = None,
        artifact_build_type: str = None,
        artifact_id: str = None,
        artifact_property: str = None,
        artifact_type: str = None,
        artifact_version: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        image_delivery: Dict[str, str] = None,
        progress: str = None,
        result_file: str = None,
        security_audit_result: str = None,
        status: str = None,
        status_detail: str = None,
        support_region_ids: str = None,
        version_name: str = None,
    ):
        # The build properties of the artifact, utilized for hosting and building the deployment package.
        self.artifact_build_property = artifact_build_property
        # The type of the deployment package to be built.
        self.artifact_build_type = artifact_build_type
        # The ID of the deployment package.
        self.artifact_id = artifact_id
        # The properties of the deployment package.
        self.artifact_property = artifact_property
        # The type of the deployment package.
        self.artifact_type = artifact_type
        # The version of the deployment package.
        self.artifact_version = artifact_version
        # The time when the certificate was created.
        self.gmt_create = gmt_create
        # The time when the deployment package was modified.
        self.gmt_modified = gmt_modified
        # The distribution result of the image.
        self.image_delivery = image_delivery
        # The distribution progress of the deployment package.
        self.progress = progress
        # The result file of the security scan.
        self.result_file = result_file
        # The result of the security scan. Valid values:
        # 
        # *   Normal: No risks exist on the deployment package.
        # *   AtRisk: Risks exist on the deployment package.
        # *   Processing: The deployment package is being scanned.
        self.security_audit_result = security_audit_result
        # The status of the deployment package. Valid values:
        # 
        # *   Created: The deployment package is created.
        # *   Scanning: The deployment package is being scanned.
        # *   ScanFailed: The deployment package failed to be scanned.
        # *   Delivering: The deployment package is being distributed.
        # *   Available: The deployment package is available.
        # *   Deleted: The deployment package is deleted.
        self.status = status
        # The description of the deployment package.
        self.status_detail = status_detail
        # The ID of the region that supports the deployment package.
        self.support_region_ids = support_region_ids
        # The version name of the deployment package.
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

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.image_delivery is not None:
            result['ImageDelivery'] = self.image_delivery

        if self.progress is not None:
            result['Progress'] = self.progress

        if self.result_file is not None:
            result['ResultFile'] = self.result_file

        if self.security_audit_result is not None:
            result['SecurityAuditResult'] = self.security_audit_result

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

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('ImageDelivery') is not None:
            self.image_delivery = m.get('ImageDelivery')

        if m.get('Progress') is not None:
            self.progress = m.get('Progress')

        if m.get('ResultFile') is not None:
            self.result_file = m.get('ResultFile')

        if m.get('SecurityAuditResult') is not None:
            self.security_audit_result = m.get('SecurityAuditResult')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StatusDetail') is not None:
            self.status_detail = m.get('StatusDetail')

        if m.get('SupportRegionIds') is not None:
            self.support_region_ids = m.get('SupportRegionIds')

        if m.get('VersionName') is not None:
            self.version_name = m.get('VersionName')

        return self

