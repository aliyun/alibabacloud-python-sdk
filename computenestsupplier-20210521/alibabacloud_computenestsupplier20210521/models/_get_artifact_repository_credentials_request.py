# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetArtifactRepositoryCredentialsRequest(DaraModel):
    def __init__(
        self,
        artifact_type: str = None,
        deploy_region_id: str = None,
    ):
        # The type of the deployment package. Valid values:
        # 
        # *   File: Object Storage Service (OSS) object.
        # *   AcrImage: container image.
        # 
        # This parameter is required.
        self.artifact_type = artifact_type
        # The region ID.
        self.deploy_region_id = deploy_region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.artifact_type is not None:
            result['ArtifactType'] = self.artifact_type

        if self.deploy_region_id is not None:
            result['DeployRegionId'] = self.deploy_region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArtifactType') is not None:
            self.artifact_type = m.get('ArtifactType')

        if m.get('DeployRegionId') is not None:
            self.deploy_region_id = m.get('DeployRegionId')

        return self

