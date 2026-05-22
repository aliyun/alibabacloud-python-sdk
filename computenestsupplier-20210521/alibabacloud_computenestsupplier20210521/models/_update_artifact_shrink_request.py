# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UpdateArtifactShrinkRequest(DaraModel):
    def __init__(
        self,
        artifact_build_property_shrink: str = None,
        artifact_id: str = None,
        artifact_property_shrink: str = None,
        client_token: str = None,
        description: str = None,
        permission_type: str = None,
        support_region_ids: List[str] = None,
        version_name: str = None,
    ):
        # The build properties of the artifact, utilized for hosting and building the deployment package.
        self.artifact_build_property_shrink = artifact_build_property_shrink
        # The ID of the deployment package.
        # 
        # This parameter is required.
        self.artifact_id = artifact_id
        # The properties of the deployment package.
        self.artifact_property_shrink = artifact_property_shrink
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The description of the deployment package.
        self.description = description
        # Permission fields are applicable to container image artifact and Helm Chart artifact. They can only change from Automatic to Public. Options:
        # 
        # Public
        # 
        # Automatic
        self.permission_type = permission_type
        # The IDs of the regions that support the deployment package.
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
        if self.artifact_build_property_shrink is not None:
            result['ArtifactBuildProperty'] = self.artifact_build_property_shrink

        if self.artifact_id is not None:
            result['ArtifactId'] = self.artifact_id

        if self.artifact_property_shrink is not None:
            result['ArtifactProperty'] = self.artifact_property_shrink

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.description is not None:
            result['Description'] = self.description

        if self.permission_type is not None:
            result['PermissionType'] = self.permission_type

        if self.support_region_ids is not None:
            result['SupportRegionIds'] = self.support_region_ids

        if self.version_name is not None:
            result['VersionName'] = self.version_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArtifactBuildProperty') is not None:
            self.artifact_build_property_shrink = m.get('ArtifactBuildProperty')

        if m.get('ArtifactId') is not None:
            self.artifact_id = m.get('ArtifactId')

        if m.get('ArtifactProperty') is not None:
            self.artifact_property_shrink = m.get('ArtifactProperty')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('PermissionType') is not None:
            self.permission_type = m.get('PermissionType')

        if m.get('SupportRegionIds') is not None:
            self.support_region_ids = m.get('SupportRegionIds')

        if m.get('VersionName') is not None:
            self.version_name = m.get('VersionName')

        return self

