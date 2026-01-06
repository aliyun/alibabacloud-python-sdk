# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aiworkspace20210204 import models as main_models
from darabonba.model import DaraModel

class CreateExperimentRequest(DaraModel):
    def __init__(
        self,
        accessibility: str = None,
        artifact_uri: str = None,
        labels: List[main_models.LabelInfo] = None,
        name: str = None,
        workspace_id: str = None,
    ):
        # The visibility of the experiment. Valid values: PRIVATE (the experiment is visible only to the creator and the Alibaba Cloud account) and PUBLIC (the experiment is visible to all users). This parameter is optional and the default value is PRIVATE.
        self.accessibility = accessibility
        # The default artifact output path of all jobs that are associated with the experiment. Only Object Storage Service (OSS) paths are supported.
        self.artifact_uri = artifact_uri
        # The tags.
        self.labels = labels
        # The experiment name. The name must meet the following requirements:
        # 
        # *   The name must start with a letter.
        # *   The name can contain letters, digits, underscores (_), and hyphens (-).
        # *   The name must be 1 to 63 characters in length.
        # 
        # This parameter is required.
        self.name = name
        # The workspace ID.
        # 
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        if self.labels:
            for v1 in self.labels:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accessibility is not None:
            result['Accessibility'] = self.accessibility

        if self.artifact_uri is not None:
            result['ArtifactUri'] = self.artifact_uri

        result['Labels'] = []
        if self.labels is not None:
            for k1 in self.labels:
                result['Labels'].append(k1.to_map() if k1 else None)

        if self.name is not None:
            result['Name'] = self.name

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accessibility') is not None:
            self.accessibility = m.get('Accessibility')

        if m.get('ArtifactUri') is not None:
            self.artifact_uri = m.get('ArtifactUri')

        self.labels = []
        if m.get('Labels') is not None:
            for k1 in m.get('Labels'):
                temp_model = main_models.LabelInfo()
                self.labels.append(temp_model.from_map(k1))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

