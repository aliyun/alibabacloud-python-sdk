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
        # The information about the artifact versions.
        self.artifacts = artifacts
        # The number of entries returned per page. The maximum value is 100. The default value is 20.
        self.max_results = max_results
        # The token that is used to retrieve the next page of results. If the results are not complete, this token is returned. To retrieve the next page of results, include this token in the next request.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The total number of entries that meet the query criteria.
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
        # The content used to build the artifact. This parameter is used for managed artifact builds.
        self.artifact_build_property = artifact_build_property
        # The artifact build type.
        self.artifact_build_type = artifact_build_type
        # The artifact ID.
        self.artifact_id = artifact_id
        # The properties of the artifact.
        self.artifact_property = artifact_property
        # The artifact type.
        self.artifact_type = artifact_type
        # The version of the artifact.
        self.artifact_version = artifact_version
        # The time when the artifact was created.
        self.gmt_create = gmt_create
        # The time when the artifact was last modified.
        self.gmt_modified = gmt_modified
        # The result of the image distribution.
        self.image_delivery = image_delivery
        # The distribution progress of the artifact.
        self.progress = progress
        # The file that contains the security scan results.
        self.result_file = result_file
        # The security scan result.
        # 
        # Valid values:
        # 
        # - Normal: The artifact is normal and has no threats.
        # 
        # - AtRisk: The artifact has security threats.
        # 
        # - Processing: The security scan is in progress.
        self.security_audit_result = security_audit_result
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

