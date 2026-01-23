# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cr20181201 import models as main_models
from darabonba.model import DaraModel

class GetArtifactBuildTaskResponseBody(DaraModel):
    def __init__(
        self,
        artifact_build_type: str = None,
        build_task_id: str = None,
        code: str = None,
        end_time: int = None,
        instructions: List[str] = None,
        is_success: bool = None,
        request_id: str = None,
        source_artifact: main_models.GetArtifactBuildTaskResponseBodySourceArtifact = None,
        start_time: int = None,
        target_artifact: main_models.GetArtifactBuildTaskResponseBodyTargetArtifact = None,
        task_status: str = None,
    ):
        # The type of the artifact building task. Valid values:
        # 
        # *   `IMAGE_TO_ACCELERATED_IMAGE`: builds accelerated images for Container Service for Kubernetes (ACK) clusters.
        # *   `IMAGE_TO_ECI_ACCELERATED_IMAGE`: builds accelerated images for elastic container instances.
        self.artifact_build_type = artifact_build_type
        # The ID of the artifact building task.
        self.build_task_id = build_task_id
        # The return value.
        self.code = code
        # The time when the artifact building task ends.
        self.end_time = end_time
        self.instructions = instructions
        # Indicates whether the request is successful.
        self.is_success = is_success
        # The ID of the request.
        self.request_id = request_id
        # The information about the source artifact.
        self.source_artifact = source_artifact
        # The time when the artifact building task starts.
        self.start_time = start_time
        # The artifact that is built in the task.
        self.target_artifact = target_artifact
        # The status of the artifact that is built in the task. Valid values:
        # 
        # *   `PENDING`: The artifact is being scheduled.
        # *   `BUILDING`: The artifact is being built.
        # *   `SUCCESS`: The artifact is built.
        # *   `FAILED`: The artifact fails to be built.
        self.task_status = task_status

    def validate(self):
        if self.source_artifact:
            self.source_artifact.validate()
        if self.target_artifact:
            self.target_artifact.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.artifact_build_type is not None:
            result['ArtifactBuildType'] = self.artifact_build_type

        if self.build_task_id is not None:
            result['BuildTaskId'] = self.build_task_id

        if self.code is not None:
            result['Code'] = self.code

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.instructions is not None:
            result['Instructions'] = self.instructions

        if self.is_success is not None:
            result['IsSuccess'] = self.is_success

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.source_artifact is not None:
            result['SourceArtifact'] = self.source_artifact.to_map()

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.target_artifact is not None:
            result['TargetArtifact'] = self.target_artifact.to_map()

        if self.task_status is not None:
            result['TaskStatus'] = self.task_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArtifactBuildType') is not None:
            self.artifact_build_type = m.get('ArtifactBuildType')

        if m.get('BuildTaskId') is not None:
            self.build_task_id = m.get('BuildTaskId')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Instructions') is not None:
            self.instructions = m.get('Instructions')

        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SourceArtifact') is not None:
            temp_model = main_models.GetArtifactBuildTaskResponseBodySourceArtifact()
            self.source_artifact = temp_model.from_map(m.get('SourceArtifact'))

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('TargetArtifact') is not None:
            temp_model = main_models.GetArtifactBuildTaskResponseBodyTargetArtifact()
            self.target_artifact = temp_model.from_map(m.get('TargetArtifact'))

        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')

        return self

class GetArtifactBuildTaskResponseBodyTargetArtifact(DaraModel):
    def __init__(
        self,
        artifact_type: str = None,
        repo_id: str = None,
        version: str = None,
    ):
        # The type of the artifact that is built in the task. The value can only be IMAGE.
        self.artifact_type = artifact_type
        # The ID of the repository to which the artifact that is built in the task belongs. The repository can only be an image repository. The value is the same as the ID of the repository to which the source artifact belongs.
        self.repo_id = repo_id
        # The version of the artifact that is built in the task. The artifact can only be an image.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.artifact_type is not None:
            result['ArtifactType'] = self.artifact_type

        if self.repo_id is not None:
            result['RepoId'] = self.repo_id

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArtifactType') is not None:
            self.artifact_type = m.get('ArtifactType')

        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

class GetArtifactBuildTaskResponseBodySourceArtifact(DaraModel):
    def __init__(
        self,
        artifact_type: str = None,
        repo_id: str = None,
        version: str = None,
    ):
        # The type of the artifact that is built in the task. The value can only be IMAGE.
        self.artifact_type = artifact_type
        # The ID of the repository to which the source artifact belongs. The repository can only be an image repository.
        self.repo_id = repo_id
        # The version of the artifact. The artifact can only be an image.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.artifact_type is not None:
            result['ArtifactType'] = self.artifact_type

        if self.repo_id is not None:
            result['RepoId'] = self.repo_id

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArtifactType') is not None:
            self.artifact_type = m.get('ArtifactType')

        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

