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
        artifact_compression: main_models.GetArtifactBuildTaskResponseBodyArtifactCompression = None,
        build_task_id: str = None,
        code: str = None,
        end_time: int = None,
        instructions: List[str] = None,
        is_success: bool = None,
        priority: int = None,
        request_id: str = None,
        source_artifact: main_models.GetArtifactBuildTaskResponseBodySourceArtifact = None,
        start_time: int = None,
        target_artifact: main_models.GetArtifactBuildTaskResponseBodyTargetArtifact = None,
        task_status: str = None,
    ):
        # The artifact build type. Valid values:
        # 
        # - `IMAGE_TO_ACCELERATED_IMAGE`: Accelerated image creation optimized for ACK scenarios.
        # 
        # - `IMAGE_TO_ECI_ACCELERATED_IMAGE`: Accelerated image artifact optimized for ECI scenarios.
        self.artifact_build_type = artifact_build_type
        # The artifact compression parameters.
        self.artifact_compression = artifact_compression
        # The ID of the artifact build task.
        self.build_task_id = build_task_id
        # The return code.
        self.code = code
        # The end time. The value is a UNIX timestamp in seconds.
        self.end_time = end_time
        # The reserved field list of the artifact build task. The list elements should be empty.
        self.instructions = instructions
        # Indicates whether the request is successful.
        self.is_success = is_success
        self.priority = priority
        # The request ID.
        self.request_id = request_id
        # The source artifact.
        self.source_artifact = source_artifact
        # The start time. The value is a UNIX timestamp in seconds.
        self.start_time = start_time
        # The target artifact.
        self.target_artifact = target_artifact
        # The artifact build status. Valid values:
        # - `PENDING`: Scheduling in progress.
        # 
        # - `BUILDING`: Building in progress.
        # 
        # - `SUCCESS`: Build succeeded.
        # 
        # - `FAILED`: Build failed.
        self.task_status = task_status

    def validate(self):
        if self.artifact_compression:
            self.artifact_compression.validate()
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

        if self.artifact_compression is not None:
            result['ArtifactCompression'] = self.artifact_compression.to_map()

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

        if self.priority is not None:
            result['Priority'] = self.priority

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

        if m.get('ArtifactCompression') is not None:
            temp_model = main_models.GetArtifactBuildTaskResponseBodyArtifactCompression()
            self.artifact_compression = temp_model.from_map(m.get('ArtifactCompression'))

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

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

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
        layer_count: int = None,
        repo_id: str = None,
        size: int = None,
        version: str = None,
    ):
        # The artifact type. Only IMAGE is supported.
        self.artifact_type = artifact_type
        # The number of artifact layers.
        self.layer_count = layer_count
        # The repository ID. Only image repositories are supported. The repository ID of the target artifact must be the same as that of the source artifact.
        self.repo_id = repo_id
        # The artifact size, in bytes.
        self.size = size
        # The artifact version. Only images are supported.
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

        if self.layer_count is not None:
            result['LayerCount'] = self.layer_count

        if self.repo_id is not None:
            result['RepoId'] = self.repo_id

        if self.size is not None:
            result['Size'] = self.size

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArtifactType') is not None:
            self.artifact_type = m.get('ArtifactType')

        if m.get('LayerCount') is not None:
            self.layer_count = m.get('LayerCount')

        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

class GetArtifactBuildTaskResponseBodySourceArtifact(DaraModel):
    def __init__(
        self,
        artifact_type: str = None,
        layer_count: int = None,
        repo_id: str = None,
        size: int = None,
        version: str = None,
    ):
        # The artifact type. Only IMAGE is supported.
        self.artifact_type = artifact_type
        # The number of artifact layers.
        self.layer_count = layer_count
        # The repository ID. Only image repositories are supported.
        self.repo_id = repo_id
        # The artifact size, in bytes.
        self.size = size
        # The artifact version. Only image versions are supported.
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

        if self.layer_count is not None:
            result['LayerCount'] = self.layer_count

        if self.repo_id is not None:
            result['RepoId'] = self.repo_id

        if self.size is not None:
            result['Size'] = self.size

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArtifactType') is not None:
            self.artifact_type = m.get('ArtifactType')

        if m.get('LayerCount') is not None:
            self.layer_count = m.get('LayerCount')

        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

class GetArtifactBuildTaskResponseBodyArtifactCompression(DaraModel):
    def __init__(
        self,
        platform: str = None,
        squash_keep_layers: int = None,
        start_layer_digest: str = None,
    ):
        # The operating system and architecture.
        self.platform = platform
        # The number of layers to retain after compression.
        self.squash_keep_layers = squash_keep_layers
        # The digest of the starting layer for compression.
        self.start_layer_digest = start_layer_digest

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.platform is not None:
            result['Platform'] = self.platform

        if self.squash_keep_layers is not None:
            result['SquashKeepLayers'] = self.squash_keep_layers

        if self.start_layer_digest is not None:
            result['StartLayerDigest'] = self.start_layer_digest

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')

        if m.get('SquashKeepLayers') is not None:
            self.squash_keep_layers = m.get('SquashKeepLayers')

        if m.get('StartLayerDigest') is not None:
            self.start_layer_digest = m.get('StartLayerDigest')

        return self

