# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations
from Tea.model import TeaModel
from typing import List, Dict, Any


class BriefPipelineRun(TeaModel):
    def __init__(
        self,
        accessibility: str = None,
        duration: int = None,
        finished_at: str = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        message: str = None,
        name: str = None,
        node_id: str = None,
        parent_user_id: str = None,
        pipeline_id: str = None,
        pipeline_run_id: str = None,
        source_id: str = None,
        source_type: str = None,
        started_at: str = None,
        status: str = None,
        user_id: str = None,
        workspace_id: str = None,
    ):
        self.accessibility = accessibility
        self.duration = duration
        self.finished_at = finished_at
        self.gmt_create_time = gmt_create_time
        self.gmt_modified_time = gmt_modified_time
        self.message = message
        self.name = name
        self.node_id = node_id
        self.parent_user_id = parent_user_id
        self.pipeline_id = pipeline_id
        self.pipeline_run_id = pipeline_run_id
        self.source_id = source_id
        self.source_type = source_type
        self.started_at = started_at
        self.status = status
        self.user_id = user_id
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accessibility is not None:
            result['Accessibility'] = self.accessibility
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.finished_at is not None:
            result['FinishedAt'] = self.finished_at
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.message is not None:
            result['Message'] = self.message
        if self.name is not None:
            result['Name'] = self.name
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.parent_user_id is not None:
            result['ParentUserId'] = self.parent_user_id
        if self.pipeline_id is not None:
            result['PipelineId'] = self.pipeline_id
        if self.pipeline_run_id is not None:
            result['PipelineRunId'] = self.pipeline_run_id
        if self.source_id is not None:
            result['SourceId'] = self.source_id
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.started_at is not None:
            result['StartedAt'] = self.started_at
        if self.status is not None:
            result['Status'] = self.status
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accessibility') is not None:
            self.accessibility = m.get('Accessibility')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('FinishedAt') is not None:
            self.finished_at = m.get('FinishedAt')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('ParentUserId') is not None:
            self.parent_user_id = m.get('ParentUserId')
        if m.get('PipelineId') is not None:
            self.pipeline_id = m.get('PipelineId')
        if m.get('PipelineRunId') is not None:
            self.pipeline_run_id = m.get('PipelineRunId')
        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('StartedAt') is not None:
            self.started_at = m.get('StartedAt')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class FullPipelineRun(TeaModel):
    def __init__(
        self,
        accessibility: str = None,
        arguments: str = None,
        duration: int = None,
        finished_at: str = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        manifest: str = None,
        message: str = None,
        name: str = None,
        node_id: str = None,
        options: str = None,
        parent_user_id: str = None,
        pipeline_id: str = None,
        pipeline_run_id: str = None,
        source_id: str = None,
        source_type: str = None,
        started_at: str = None,
        status: str = None,
        user_id: str = None,
        workspace_id: str = None,
    ):
        self.accessibility = accessibility
        self.arguments = arguments
        self.duration = duration
        self.finished_at = finished_at
        self.gmt_create_time = gmt_create_time
        self.gmt_modified_time = gmt_modified_time
        self.manifest = manifest
        self.message = message
        self.name = name
        self.node_id = node_id
        self.options = options
        self.parent_user_id = parent_user_id
        self.pipeline_id = pipeline_id
        self.pipeline_run_id = pipeline_run_id
        self.source_id = source_id
        self.source_type = source_type
        self.started_at = started_at
        self.status = status
        self.user_id = user_id
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accessibility is not None:
            result['Accessibility'] = self.accessibility
        if self.arguments is not None:
            result['Arguments'] = self.arguments
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.finished_at is not None:
            result['FinishedAt'] = self.finished_at
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.manifest is not None:
            result['Manifest'] = self.manifest
        if self.message is not None:
            result['Message'] = self.message
        if self.name is not None:
            result['Name'] = self.name
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.options is not None:
            result['Options'] = self.options
        if self.parent_user_id is not None:
            result['ParentUserId'] = self.parent_user_id
        if self.pipeline_id is not None:
            result['PipelineId'] = self.pipeline_id
        if self.pipeline_run_id is not None:
            result['PipelineRunId'] = self.pipeline_run_id
        if self.source_id is not None:
            result['SourceId'] = self.source_id
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.started_at is not None:
            result['StartedAt'] = self.started_at
        if self.status is not None:
            result['Status'] = self.status
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accessibility') is not None:
            self.accessibility = m.get('Accessibility')
        if m.get('Arguments') is not None:
            self.arguments = m.get('Arguments')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('FinishedAt') is not None:
            self.finished_at = m.get('FinishedAt')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('Manifest') is not None:
            self.manifest = m.get('Manifest')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('Options') is not None:
            self.options = m.get('Options')
        if m.get('ParentUserId') is not None:
            self.parent_user_id = m.get('ParentUserId')
        if m.get('PipelineId') is not None:
            self.pipeline_id = m.get('PipelineId')
        if m.get('PipelineRunId') is not None:
            self.pipeline_run_id = m.get('PipelineRunId')
        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('StartedAt') is not None:
            self.started_at = m.get('StartedAt')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class NodeMetadata(TeaModel):
    def __init__(
        self,
        display_name: str = None,
        identifier: str = None,
        name: str = None,
        node_id: str = None,
        node_type: str = None,
        provider: str = None,
        related_node_ids: List[str] = None,
        version: str = None,
    ):
        self.display_name = display_name
        self.identifier = identifier
        self.name = name
        self.node_id = node_id
        self.node_type = node_type
        self.provider = provider
        self.related_node_ids = related_node_ids
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.identifier is not None:
            result['Identifier'] = self.identifier
        if self.name is not None:
            result['Name'] = self.name
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.node_type is not None:
            result['NodeType'] = self.node_type
        if self.provider is not None:
            result['Provider'] = self.provider
        if self.related_node_ids is not None:
            result['RelatedNodeIds'] = self.related_node_ids
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Identifier') is not None:
            self.identifier = m.get('Identifier')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')
        if m.get('Provider') is not None:
            self.provider = m.get('Provider')
        if m.get('RelatedNodeIds') is not None:
            self.related_node_ids = m.get('RelatedNodeIds')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class NodeSpecWithSequence(TeaModel):
    def __init__(
        self,
        end: int = None,
        format: str = None,
        start: int = None,
    ):
        self.end = end
        self.format = format
        self.start = start

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end is not None:
            result['End'] = self.end
        if self.format is not None:
            result['Format'] = self.format
        if self.start is not None:
            result['Start'] = self.start
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('End') is not None:
            self.end = m.get('End')
        if m.get('Format') is not None:
            self.format = m.get('Format')
        if m.get('Start') is not None:
            self.start = m.get('Start')
        return self


class NodeIO(TeaModel):
    def __init__(
        self,
        artifacts: List[Dict[str, Any]] = None,
        parameters: List[Dict[str, Any]] = None,
    ):
        self.artifacts = artifacts
        self.parameters = parameters

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.artifacts is not None:
            result['Artifacts'] = self.artifacts
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Artifacts') is not None:
            self.artifacts = m.get('Artifacts')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        return self


class NodeSpec(TeaModel):
    def __init__(
        self,
        dependencies: List[str] = None,
        has_pipelines: bool = None,
        inputs: NodeIO = None,
        outputs: NodeIO = None,
        parallelism: int = None,
        pipelines: List[Node] = None,
        when: str = None,
        with_items: List[str] = None,
        with_param: str = None,
        with_sequence: NodeSpecWithSequence = None,
    ):
        self.dependencies = dependencies
        self.has_pipelines = has_pipelines
        self.inputs = inputs
        self.outputs = outputs
        self.parallelism = parallelism
        self.pipelines = pipelines
        self.when = when
        self.with_items = with_items
        self.with_param = with_param
        self.with_sequence = with_sequence

    def validate(self):
        if self.inputs:
            self.inputs.validate()
        if self.outputs:
            self.outputs.validate()
        if self.pipelines:
            for k in self.pipelines:
                if k:
                    k.validate()
        if self.with_sequence:
            self.with_sequence.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dependencies is not None:
            result['Dependencies'] = self.dependencies
        if self.has_pipelines is not None:
            result['HasPipelines'] = self.has_pipelines
        if self.inputs is not None:
            result['Inputs'] = self.inputs.to_map()
        if self.outputs is not None:
            result['Outputs'] = self.outputs.to_map()
        if self.parallelism is not None:
            result['Parallelism'] = self.parallelism
        result['Pipelines'] = []
        if self.pipelines is not None:
            for k in self.pipelines:
                result['Pipelines'].append(k.to_map() if k else None)
        if self.when is not None:
            result['When'] = self.when
        if self.with_items is not None:
            result['WithItems'] = self.with_items
        if self.with_param is not None:
            result['WithParam'] = self.with_param
        if self.with_sequence is not None:
            result['WithSequence'] = self.with_sequence.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Dependencies') is not None:
            self.dependencies = m.get('Dependencies')
        if m.get('HasPipelines') is not None:
            self.has_pipelines = m.get('HasPipelines')
        if m.get('Inputs') is not None:
            temp_model = NodeIO()
            self.inputs = temp_model.from_map(m['Inputs'])
        if m.get('Outputs') is not None:
            temp_model = NodeIO()
            self.outputs = temp_model.from_map(m['Outputs'])
        if m.get('Parallelism') is not None:
            self.parallelism = m.get('Parallelism')
        self.pipelines = []
        if m.get('Pipelines') is not None:
            for k in m.get('Pipelines'):
                temp_model = Node()
                self.pipelines.append(temp_model.from_map(k))
        if m.get('When') is not None:
            self.when = m.get('When')
        if m.get('WithItems') is not None:
            self.with_items = m.get('WithItems')
        if m.get('WithParam') is not None:
            self.with_param = m.get('WithParam')
        if m.get('WithSequence') is not None:
            temp_model = NodeSpecWithSequence()
            self.with_sequence = temp_model.from_map(m['WithSequence'])
        return self


class NodeStatusInfoConditions(TeaModel):
    def __init__(
        self,
        status: str = None,
        type: str = None,
    ):
        self.status = status
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class NodeStatusInfo(TeaModel):
    def __init__(
        self,
        conditions: List[NodeStatusInfoConditions] = None,
        finished_at: str = None,
        progress: str = None,
        started_at: str = None,
        status: str = None,
    ):
        self.conditions = conditions
        self.finished_at = finished_at
        self.progress = progress
        self.started_at = started_at
        self.status = status

    def validate(self):
        if self.conditions:
            for k in self.conditions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Conditions'] = []
        if self.conditions is not None:
            for k in self.conditions:
                result['Conditions'].append(k.to_map() if k else None)
        if self.finished_at is not None:
            result['FinishedAt'] = self.finished_at
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.started_at is not None:
            result['StartedAt'] = self.started_at
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.conditions = []
        if m.get('Conditions') is not None:
            for k in m.get('Conditions'):
                temp_model = NodeStatusInfoConditions()
                self.conditions.append(temp_model.from_map(k))
        if m.get('FinishedAt') is not None:
            self.finished_at = m.get('FinishedAt')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('StartedAt') is not None:
            self.started_at = m.get('StartedAt')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class Node(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        metadata: NodeMetadata = None,
        spec: NodeSpec = None,
        status_info: NodeStatusInfo = None,
    ):
        self.api_version = api_version
        self.metadata = metadata
        self.spec = spec
        self.status_info = status_info

    def validate(self):
        if self.metadata:
            self.metadata.validate()
        if self.spec:
            self.spec.validate()
        if self.status_info:
            self.status_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_version is not None:
            result['ApiVersion'] = self.api_version
        if self.metadata is not None:
            result['Metadata'] = self.metadata.to_map()
        if self.spec is not None:
            result['Spec'] = self.spec.to_map()
        if self.status_info is not None:
            result['StatusInfo'] = self.status_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiVersion') is not None:
            self.api_version = m.get('ApiVersion')
        if m.get('Metadata') is not None:
            temp_model = NodeMetadata()
            self.metadata = temp_model.from_map(m['Metadata'])
        if m.get('Spec') is not None:
            temp_model = NodeSpec()
            self.spec = temp_model.from_map(m['Spec'])
        if m.get('StatusInfo') is not None:
            temp_model = NodeStatusInfo()
            self.status_info = temp_model.from_map(m['StatusInfo'])
        return self


class Pipeline(TeaModel):
    def __init__(
        self,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        identifier: str = None,
        pipeline_id: str = None,
        provider: str = None,
        uuid: str = None,
        version: str = None,
        workspace_id: str = None,
    ):
        self.gmt_create_time = gmt_create_time
        self.gmt_modified_time = gmt_modified_time
        self.identifier = identifier
        self.pipeline_id = pipeline_id
        self.provider = provider
        self.uuid = uuid
        self.version = version
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.identifier is not None:
            result['Identifier'] = self.identifier
        if self.pipeline_id is not None:
            result['PipelineId'] = self.pipeline_id
        if self.provider is not None:
            result['Provider'] = self.provider
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        if self.version is not None:
            result['Version'] = self.version
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('Identifier') is not None:
            self.identifier = m.get('Identifier')
        if m.get('PipelineId') is not None:
            self.pipeline_id = m.get('PipelineId')
        if m.get('Provider') is not None:
            self.provider = m.get('Provider')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class Run(TeaModel):
    def __init__(
        self,
        accessibility: str = None,
        duration: int = None,
        experiment_id: str = None,
        finished_at: int = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        message: str = None,
        name: str = None,
        node_id: str = None,
        parent_user_id: str = None,
        run_id: str = None,
        source: str = None,
        started_at: int = None,
        status: str = None,
        user_id: str = None,
        workspace_id: str = None,
    ):
        self.accessibility = accessibility
        self.duration = duration
        self.experiment_id = experiment_id
        self.finished_at = finished_at
        self.gmt_create_time = gmt_create_time
        self.gmt_modified_time = gmt_modified_time
        self.message = message
        self.name = name
        self.node_id = node_id
        self.parent_user_id = parent_user_id
        self.run_id = run_id
        self.source = source
        self.started_at = started_at
        self.status = status
        self.user_id = user_id
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accessibility is not None:
            result['Accessibility'] = self.accessibility
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.experiment_id is not None:
            result['ExperimentId'] = self.experiment_id
        if self.finished_at is not None:
            result['FinishedAt'] = self.finished_at
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.message is not None:
            result['Message'] = self.message
        if self.name is not None:
            result['Name'] = self.name
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.parent_user_id is not None:
            result['ParentUserId'] = self.parent_user_id
        if self.run_id is not None:
            result['RunId'] = self.run_id
        if self.source is not None:
            result['Source'] = self.source
        if self.started_at is not None:
            result['StartedAt'] = self.started_at
        if self.status is not None:
            result['Status'] = self.status
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accessibility') is not None:
            self.accessibility = m.get('Accessibility')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('ExperimentId') is not None:
            self.experiment_id = m.get('ExperimentId')
        if m.get('FinishedAt') is not None:
            self.finished_at = m.get('FinishedAt')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('ParentUserId') is not None:
            self.parent_user_id = m.get('ParentUserId')
        if m.get('RunId') is not None:
            self.run_id = m.get('RunId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('StartedAt') is not None:
            self.started_at = m.get('StartedAt')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class CreatePipelineRequest(TeaModel):
    def __init__(
        self,
        manifest: str = None,
        workspace_id: str = None,
    ):
        self.manifest = manifest
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.manifest is not None:
            result['Manifest'] = self.manifest
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Manifest') is not None:
            self.manifest = m.get('Manifest')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class CreatePipelineResponseBody(TeaModel):
    def __init__(
        self,
        pipeline_id: str = None,
        request_id: str = None,
    ):
        self.pipeline_id = pipeline_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pipeline_id is not None:
            result['PipelineId'] = self.pipeline_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PipelineId') is not None:
            self.pipeline_id = m.get('PipelineId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreatePipelineResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreatePipelineResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreatePipelineResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatePipelineRunRequest(TeaModel):
    def __init__(
        self,
        accessibility: str = None,
        arguments: str = None,
        name: str = None,
        no_confirm_required: bool = None,
        options: str = None,
        pipeline_id: str = None,
        pipeline_manifest: str = None,
        source_id: str = None,
        source_type: str = None,
        workspace_id: str = None,
    ):
        self.accessibility = accessibility
        self.arguments = arguments
        self.name = name
        self.no_confirm_required = no_confirm_required
        self.options = options
        self.pipeline_id = pipeline_id
        self.pipeline_manifest = pipeline_manifest
        self.source_id = source_id
        self.source_type = source_type
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accessibility is not None:
            result['Accessibility'] = self.accessibility
        if self.arguments is not None:
            result['Arguments'] = self.arguments
        if self.name is not None:
            result['Name'] = self.name
        if self.no_confirm_required is not None:
            result['NoConfirmRequired'] = self.no_confirm_required
        if self.options is not None:
            result['Options'] = self.options
        if self.pipeline_id is not None:
            result['PipelineId'] = self.pipeline_id
        if self.pipeline_manifest is not None:
            result['PipelineManifest'] = self.pipeline_manifest
        if self.source_id is not None:
            result['SourceId'] = self.source_id
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accessibility') is not None:
            self.accessibility = m.get('Accessibility')
        if m.get('Arguments') is not None:
            self.arguments = m.get('Arguments')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NoConfirmRequired') is not None:
            self.no_confirm_required = m.get('NoConfirmRequired')
        if m.get('Options') is not None:
            self.options = m.get('Options')
        if m.get('PipelineId') is not None:
            self.pipeline_id = m.get('PipelineId')
        if m.get('PipelineManifest') is not None:
            self.pipeline_manifest = m.get('PipelineManifest')
        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class CreatePipelineRunResponseBody(TeaModel):
    def __init__(
        self,
        pipeline_run_id: str = None,
        request_id: str = None,
    ):
        self.pipeline_run_id = pipeline_run_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pipeline_run_id is not None:
            result['PipelineRunId'] = self.pipeline_run_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PipelineRunId') is not None:
            self.pipeline_run_id = m.get('PipelineRunId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreatePipelineRunResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreatePipelineRunResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreatePipelineRunResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeletePipelineResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeletePipelineResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeletePipelineResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeletePipelineResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeletePipelineRunResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeletePipelineRunResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeletePipelineRunResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeletePipelineRunResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPipelineResponseBody(TeaModel):
    def __init__(
        self,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        identifier: str = None,
        manifest: str = None,
        pipeline_id: str = None,
        provider: str = None,
        request_id: str = None,
        uuid: str = None,
        version: str = None,
        workspace_id: str = None,
    ):
        self.gmt_create_time = gmt_create_time
        self.gmt_modified_time = gmt_modified_time
        self.identifier = identifier
        self.manifest = manifest
        self.pipeline_id = pipeline_id
        self.provider = provider
        self.request_id = request_id
        self.uuid = uuid
        self.version = version
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.identifier is not None:
            result['Identifier'] = self.identifier
        if self.manifest is not None:
            result['Manifest'] = self.manifest
        if self.pipeline_id is not None:
            result['PipelineId'] = self.pipeline_id
        if self.provider is not None:
            result['Provider'] = self.provider
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        if self.version is not None:
            result['Version'] = self.version
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('Identifier') is not None:
            self.identifier = m.get('Identifier')
        if m.get('Manifest') is not None:
            self.manifest = m.get('Manifest')
        if m.get('PipelineId') is not None:
            self.pipeline_id = m.get('PipelineId')
        if m.get('Provider') is not None:
            self.provider = m.get('Provider')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class GetPipelineResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetPipelineResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetPipelineResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPipelineRunRequest(TeaModel):
    def __init__(
        self,
        manifest_type: str = None,
        token_id: str = None,
        verbose: bool = None,
    ):
        self.manifest_type = manifest_type
        self.token_id = token_id
        self.verbose = verbose

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.manifest_type is not None:
            result['ManifestType'] = self.manifest_type
        if self.token_id is not None:
            result['TokenId'] = self.token_id
        if self.verbose is not None:
            result['Verbose'] = self.verbose
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ManifestType') is not None:
            self.manifest_type = m.get('ManifestType')
        if m.get('TokenId') is not None:
            self.token_id = m.get('TokenId')
        if m.get('Verbose') is not None:
            self.verbose = m.get('Verbose')
        return self


class GetPipelineRunResponseBody(TeaModel):
    def __init__(
        self,
        accessibility: str = None,
        arguments: str = None,
        duration: int = None,
        finished_at: str = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        manifest: str = None,
        message: str = None,
        name: str = None,
        node_id: str = None,
        options: str = None,
        parent_user_id: str = None,
        pipeline_id: str = None,
        pipeline_run_id: str = None,
        pipeline_run_uri: str = None,
        request_id: str = None,
        source_id: str = None,
        source_type: str = None,
        started_at: str = None,
        status: str = None,
        user_id: str = None,
        workspace_id: str = None,
    ):
        self.accessibility = accessibility
        self.arguments = arguments
        self.duration = duration
        self.finished_at = finished_at
        self.gmt_create_time = gmt_create_time
        self.gmt_modified_time = gmt_modified_time
        self.manifest = manifest
        self.message = message
        self.name = name
        self.node_id = node_id
        self.options = options
        self.parent_user_id = parent_user_id
        self.pipeline_id = pipeline_id
        self.pipeline_run_id = pipeline_run_id
        self.pipeline_run_uri = pipeline_run_uri
        self.request_id = request_id
        self.source_id = source_id
        self.source_type = source_type
        self.started_at = started_at
        self.status = status
        self.user_id = user_id
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accessibility is not None:
            result['Accessibility'] = self.accessibility
        if self.arguments is not None:
            result['Arguments'] = self.arguments
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.finished_at is not None:
            result['FinishedAt'] = self.finished_at
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.manifest is not None:
            result['Manifest'] = self.manifest
        if self.message is not None:
            result['Message'] = self.message
        if self.name is not None:
            result['Name'] = self.name
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.options is not None:
            result['Options'] = self.options
        if self.parent_user_id is not None:
            result['ParentUserId'] = self.parent_user_id
        if self.pipeline_id is not None:
            result['PipelineId'] = self.pipeline_id
        if self.pipeline_run_id is not None:
            result['PipelineRunId'] = self.pipeline_run_id
        if self.pipeline_run_uri is not None:
            result['PipelineRunUri'] = self.pipeline_run_uri
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.source_id is not None:
            result['SourceId'] = self.source_id
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.started_at is not None:
            result['StartedAt'] = self.started_at
        if self.status is not None:
            result['Status'] = self.status
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accessibility') is not None:
            self.accessibility = m.get('Accessibility')
        if m.get('Arguments') is not None:
            self.arguments = m.get('Arguments')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('FinishedAt') is not None:
            self.finished_at = m.get('FinishedAt')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('Manifest') is not None:
            self.manifest = m.get('Manifest')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('Options') is not None:
            self.options = m.get('Options')
        if m.get('ParentUserId') is not None:
            self.parent_user_id = m.get('ParentUserId')
        if m.get('PipelineId') is not None:
            self.pipeline_id = m.get('PipelineId')
        if m.get('PipelineRunId') is not None:
            self.pipeline_run_id = m.get('PipelineRunId')
        if m.get('PipelineRunUri') is not None:
            self.pipeline_run_uri = m.get('PipelineRunUri')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('StartedAt') is not None:
            self.started_at = m.get('StartedAt')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class GetPipelineRunResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetPipelineRunResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetPipelineRunResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPipelineRunNodeRequest(TeaModel):
    def __init__(
        self,
        depth: int = None,
        token_id: str = None,
        type: str = None,
    ):
        self.depth = depth
        self.token_id = token_id
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.depth is not None:
            result['Depth'] = self.depth
        if self.token_id is not None:
            result['TokenId'] = self.token_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Depth') is not None:
            self.depth = m.get('Depth')
        if m.get('TokenId') is not None:
            self.token_id = m.get('TokenId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetPipelineRunNodeResponseBodyMetadata(TeaModel):
    def __init__(
        self,
        display_name: str = None,
        identifier: str = None,
        name: str = None,
        node_id: str = None,
        node_type: str = None,
        provider: str = None,
        related_node_ids: List[str] = None,
        version: str = None,
    ):
        self.display_name = display_name
        self.identifier = identifier
        self.name = name
        self.node_id = node_id
        self.node_type = node_type
        self.provider = provider
        self.related_node_ids = related_node_ids
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.identifier is not None:
            result['Identifier'] = self.identifier
        if self.name is not None:
            result['Name'] = self.name
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.node_type is not None:
            result['NodeType'] = self.node_type
        if self.provider is not None:
            result['Provider'] = self.provider
        if self.related_node_ids is not None:
            result['RelatedNodeIds'] = self.related_node_ids
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Identifier') is not None:
            self.identifier = m.get('Identifier')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')
        if m.get('Provider') is not None:
            self.provider = m.get('Provider')
        if m.get('RelatedNodeIds') is not None:
            self.related_node_ids = m.get('RelatedNodeIds')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class GetPipelineRunNodeResponseBodySpecInputs(TeaModel):
    def __init__(
        self,
        artifacts: List[Dict[str, Any]] = None,
        parameters: List[Dict[str, Any]] = None,
    ):
        self.artifacts = artifacts
        self.parameters = parameters

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.artifacts is not None:
            result['Artifacts'] = self.artifacts
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Artifacts') is not None:
            self.artifacts = m.get('Artifacts')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        return self


class GetPipelineRunNodeResponseBodySpecOutputs(TeaModel):
    def __init__(
        self,
        artifacts: List[Dict[str, Any]] = None,
        parameters: List[Dict[str, Any]] = None,
    ):
        self.artifacts = artifacts
        self.parameters = parameters

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.artifacts is not None:
            result['Artifacts'] = self.artifacts
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Artifacts') is not None:
            self.artifacts = m.get('Artifacts')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        return self


class GetPipelineRunNodeResponseBodySpecWithSequence(TeaModel):
    def __init__(
        self,
        end: int = None,
        format: str = None,
        start: int = None,
    ):
        self.end = end
        self.format = format
        self.start = start

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end is not None:
            result['End'] = self.end
        if self.format is not None:
            result['Format'] = self.format
        if self.start is not None:
            result['Start'] = self.start
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('End') is not None:
            self.end = m.get('End')
        if m.get('Format') is not None:
            self.format = m.get('Format')
        if m.get('Start') is not None:
            self.start = m.get('Start')
        return self


class GetPipelineRunNodeResponseBodySpec(TeaModel):
    def __init__(
        self,
        dependencies: List[str] = None,
        has_pipelines: bool = None,
        inputs: GetPipelineRunNodeResponseBodySpecInputs = None,
        outputs: GetPipelineRunNodeResponseBodySpecOutputs = None,
        parallelism: int = None,
        pipelines: List[Dict[str, Any]] = None,
        when: str = None,
        with_items: List[str] = None,
        with_param: str = None,
        with_sequence: GetPipelineRunNodeResponseBodySpecWithSequence = None,
    ):
        self.dependencies = dependencies
        self.has_pipelines = has_pipelines
        self.inputs = inputs
        self.outputs = outputs
        self.parallelism = parallelism
        self.pipelines = pipelines
        self.when = when
        self.with_items = with_items
        self.with_param = with_param
        self.with_sequence = with_sequence

    def validate(self):
        if self.inputs:
            self.inputs.validate()
        if self.outputs:
            self.outputs.validate()
        if self.with_sequence:
            self.with_sequence.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dependencies is not None:
            result['Dependencies'] = self.dependencies
        if self.has_pipelines is not None:
            result['HasPipelines'] = self.has_pipelines
        if self.inputs is not None:
            result['Inputs'] = self.inputs.to_map()
        if self.outputs is not None:
            result['Outputs'] = self.outputs.to_map()
        if self.parallelism is not None:
            result['Parallelism'] = self.parallelism
        if self.pipelines is not None:
            result['Pipelines'] = self.pipelines
        if self.when is not None:
            result['When'] = self.when
        if self.with_items is not None:
            result['WithItems'] = self.with_items
        if self.with_param is not None:
            result['WithParam'] = self.with_param
        if self.with_sequence is not None:
            result['WithSequence'] = self.with_sequence.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Dependencies') is not None:
            self.dependencies = m.get('Dependencies')
        if m.get('HasPipelines') is not None:
            self.has_pipelines = m.get('HasPipelines')
        if m.get('Inputs') is not None:
            temp_model = GetPipelineRunNodeResponseBodySpecInputs()
            self.inputs = temp_model.from_map(m['Inputs'])
        if m.get('Outputs') is not None:
            temp_model = GetPipelineRunNodeResponseBodySpecOutputs()
            self.outputs = temp_model.from_map(m['Outputs'])
        if m.get('Parallelism') is not None:
            self.parallelism = m.get('Parallelism')
        if m.get('Pipelines') is not None:
            self.pipelines = m.get('Pipelines')
        if m.get('When') is not None:
            self.when = m.get('When')
        if m.get('WithItems') is not None:
            self.with_items = m.get('WithItems')
        if m.get('WithParam') is not None:
            self.with_param = m.get('WithParam')
        if m.get('WithSequence') is not None:
            temp_model = GetPipelineRunNodeResponseBodySpecWithSequence()
            self.with_sequence = temp_model.from_map(m['WithSequence'])
        return self


class GetPipelineRunNodeResponseBodyStatusInfo(TeaModel):
    def __init__(
        self,
        conditions: List[Dict[str, Any]] = None,
        finished_at: str = None,
        progress: str = None,
        started_at: str = None,
        status: str = None,
    ):
        self.conditions = conditions
        self.finished_at = finished_at
        self.progress = progress
        self.started_at = started_at
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.conditions is not None:
            result['Conditions'] = self.conditions
        if self.finished_at is not None:
            result['FinishedAt'] = self.finished_at
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.started_at is not None:
            result['StartedAt'] = self.started_at
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Conditions') is not None:
            self.conditions = m.get('Conditions')
        if m.get('FinishedAt') is not None:
            self.finished_at = m.get('FinishedAt')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('StartedAt') is not None:
            self.started_at = m.get('StartedAt')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetPipelineRunNodeResponseBody(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        metadata: GetPipelineRunNodeResponseBodyMetadata = None,
        request_id: str = None,
        spec: GetPipelineRunNodeResponseBodySpec = None,
        status_info: GetPipelineRunNodeResponseBodyStatusInfo = None,
    ):
        self.api_version = api_version
        self.metadata = metadata
        self.request_id = request_id
        self.spec = spec
        self.status_info = status_info

    def validate(self):
        if self.metadata:
            self.metadata.validate()
        if self.spec:
            self.spec.validate()
        if self.status_info:
            self.status_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_version is not None:
            result['ApiVersion'] = self.api_version
        if self.metadata is not None:
            result['Metadata'] = self.metadata.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.spec is not None:
            result['Spec'] = self.spec.to_map()
        if self.status_info is not None:
            result['StatusInfo'] = self.status_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiVersion') is not None:
            self.api_version = m.get('ApiVersion')
        if m.get('Metadata') is not None:
            temp_model = GetPipelineRunNodeResponseBodyMetadata()
            self.metadata = temp_model.from_map(m['Metadata'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Spec') is not None:
            temp_model = GetPipelineRunNodeResponseBodySpec()
            self.spec = temp_model.from_map(m['Spec'])
        if m.get('StatusInfo') is not None:
            temp_model = GetPipelineRunNodeResponseBodyStatusInfo()
            self.status_info = temp_model.from_map(m['StatusInfo'])
        return self


class GetPipelineRunNodeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetPipelineRunNodeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetPipelineRunNodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPipelineRunNodeLogsRequest(TeaModel):
    def __init__(
        self,
        from_time_in_seconds: int = None,
        keyword: str = None,
        offset: int = None,
        page_size: int = None,
        reverse: bool = None,
        to_time_in_seconds: int = None,
        token_id: str = None,
    ):
        self.from_time_in_seconds = from_time_in_seconds
        self.keyword = keyword
        self.offset = offset
        self.page_size = page_size
        self.reverse = reverse
        self.to_time_in_seconds = to_time_in_seconds
        self.token_id = token_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.from_time_in_seconds is not None:
            result['FromTimeInSeconds'] = self.from_time_in_seconds
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.offset is not None:
            result['Offset'] = self.offset
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.reverse is not None:
            result['Reverse'] = self.reverse
        if self.to_time_in_seconds is not None:
            result['ToTimeInSeconds'] = self.to_time_in_seconds
        if self.token_id is not None:
            result['TokenId'] = self.token_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FromTimeInSeconds') is not None:
            self.from_time_in_seconds = m.get('FromTimeInSeconds')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('Offset') is not None:
            self.offset = m.get('Offset')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Reverse') is not None:
            self.reverse = m.get('Reverse')
        if m.get('ToTimeInSeconds') is not None:
            self.to_time_in_seconds = m.get('ToTimeInSeconds')
        if m.get('TokenId') is not None:
            self.token_id = m.get('TokenId')
        return self


class ListPipelineRunNodeLogsResponseBody(TeaModel):
    def __init__(
        self,
        logs: List[str] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.logs = logs
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.logs is not None:
            result['Logs'] = self.logs
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Logs') is not None:
            self.logs = m.get('Logs')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListPipelineRunNodeLogsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListPipelineRunNodeLogsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListPipelineRunNodeLogsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPipelineRunNodeOutputsRequest(TeaModel):
    def __init__(
        self,
        depth: int = None,
        name: str = None,
        order: str = None,
        page_number: int = None,
        page_size: int = None,
        sort_by: str = None,
        token_id: str = None,
        type: str = None,
    ):
        self.depth = depth
        self.name = name
        self.order = order
        self.page_number = page_number
        self.page_size = page_size
        self.sort_by = sort_by
        self.token_id = token_id
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.depth is not None:
            result['Depth'] = self.depth
        if self.name is not None:
            result['Name'] = self.name
        if self.order is not None:
            result['Order'] = self.order
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.token_id is not None:
            result['TokenId'] = self.token_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Depth') is not None:
            self.depth = m.get('Depth')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('TokenId') is not None:
            self.token_id = m.get('TokenId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListPipelineRunNodeOutputsResponseBodyOutputs(TeaModel):
    def __init__(
        self,
        expandable_artifact_name: str = None,
        expanded_artifact_index: int = None,
        gmt_create_time: str = None,
        id: str = None,
        info: Dict[str, Any] = None,
        name: str = None,
        node_id: str = None,
        producer: str = None,
        type: str = None,
    ):
        self.expandable_artifact_name = expandable_artifact_name
        self.expanded_artifact_index = expanded_artifact_index
        self.gmt_create_time = gmt_create_time
        self.id = id
        self.info = info
        self.name = name
        self.node_id = node_id
        self.producer = producer
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expandable_artifact_name is not None:
            result['ExpandableArtifactName'] = self.expandable_artifact_name
        if self.expanded_artifact_index is not None:
            result['ExpandedArtifactIndex'] = self.expanded_artifact_index
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.id is not None:
            result['Id'] = self.id
        if self.info is not None:
            result['Info'] = self.info
        if self.name is not None:
            result['Name'] = self.name
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.producer is not None:
            result['Producer'] = self.producer
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExpandableArtifactName') is not None:
            self.expandable_artifact_name = m.get('ExpandableArtifactName')
        if m.get('ExpandedArtifactIndex') is not None:
            self.expanded_artifact_index = m.get('ExpandedArtifactIndex')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Info') is not None:
            self.info = m.get('Info')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('Producer') is not None:
            self.producer = m.get('Producer')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListPipelineRunNodeOutputsResponseBody(TeaModel):
    def __init__(
        self,
        outputs: List[ListPipelineRunNodeOutputsResponseBodyOutputs] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.outputs = outputs
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.outputs:
            for k in self.outputs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Outputs'] = []
        if self.outputs is not None:
            for k in self.outputs:
                result['Outputs'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.outputs = []
        if m.get('Outputs') is not None:
            for k in m.get('Outputs'):
                temp_model = ListPipelineRunNodeOutputsResponseBodyOutputs()
                self.outputs.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListPipelineRunNodeOutputsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListPipelineRunNodeOutputsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListPipelineRunNodeOutputsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPipelineRunNodeStatusRequest(TeaModel):
    def __init__(
        self,
        depth: int = None,
        token_id: str = None,
        type: str = None,
    ):
        self.depth = depth
        self.token_id = token_id
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.depth is not None:
            result['Depth'] = self.depth
        if self.token_id is not None:
            result['TokenId'] = self.token_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Depth') is not None:
            self.depth = m.get('Depth')
        if m.get('TokenId') is not None:
            self.token_id = m.get('TokenId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListPipelineRunNodeStatusResponseBodyStatus(TeaModel):
    def __init__(
        self,
        finished_at: str = None,
        node_id: str = None,
        node_name: str = None,
        runtime_info: str = None,
        started_at: str = None,
        status: str = None,
    ):
        self.finished_at = finished_at
        self.node_id = node_id
        self.node_name = node_name
        self.runtime_info = runtime_info
        self.started_at = started_at
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.finished_at is not None:
            result['FinishedAt'] = self.finished_at
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.node_name is not None:
            result['NodeName'] = self.node_name
        if self.runtime_info is not None:
            result['RuntimeInfo'] = self.runtime_info
        if self.started_at is not None:
            result['StartedAt'] = self.started_at
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FinishedAt') is not None:
            self.finished_at = m.get('FinishedAt')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')
        if m.get('RuntimeInfo') is not None:
            self.runtime_info = m.get('RuntimeInfo')
        if m.get('StartedAt') is not None:
            self.started_at = m.get('StartedAt')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListPipelineRunNodeStatusResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        status: List[ListPipelineRunNodeStatusResponseBodyStatus] = None,
    ):
        self.request_id = request_id
        self.status = status

    def validate(self):
        if self.status:
            for k in self.status:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Status'] = []
        if self.status is not None:
            for k in self.status:
                result['Status'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.status = []
        if m.get('Status') is not None:
            for k in m.get('Status'):
                temp_model = ListPipelineRunNodeStatusResponseBodyStatus()
                self.status.append(temp_model.from_map(k))
        return self


class ListPipelineRunNodeStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListPipelineRunNodeStatusResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListPipelineRunNodeStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPipelineRunsRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        order: str = None,
        page_number: int = None,
        page_size: int = None,
        pipeline_ids: str = None,
        pipeline_run_id: str = None,
        sort_by: str = None,
        source_id: str = None,
        source_type: str = None,
        status: str = None,
        user_id: str = None,
        workspace_id: str = None,
    ):
        self.name = name
        self.order = order
        self.page_number = page_number
        self.page_size = page_size
        self.pipeline_ids = pipeline_ids
        self.pipeline_run_id = pipeline_run_id
        self.sort_by = sort_by
        self.source_id = source_id
        self.source_type = source_type
        self.status = status
        self.user_id = user_id
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.order is not None:
            result['Order'] = self.order
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.pipeline_ids is not None:
            result['PipelineIds'] = self.pipeline_ids
        if self.pipeline_run_id is not None:
            result['PipelineRunId'] = self.pipeline_run_id
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.source_id is not None:
            result['SourceId'] = self.source_id
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.status is not None:
            result['Status'] = self.status
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PipelineIds') is not None:
            self.pipeline_ids = m.get('PipelineIds')
        if m.get('PipelineRunId') is not None:
            self.pipeline_run_id = m.get('PipelineRunId')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class ListPipelineRunsResponseBodyPipelineRuns(TeaModel):
    def __init__(
        self,
        accessibility: str = None,
        duration: int = None,
        finished_at: str = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        message: str = None,
        name: str = None,
        node_id: str = None,
        parent_user_id: str = None,
        pipeline_id: str = None,
        pipeline_run_id: str = None,
        pipeline_run_uri: str = None,
        source_id: str = None,
        source_type: str = None,
        started_at: str = None,
        status: str = None,
        user_id: str = None,
        workspace_id: str = None,
    ):
        self.accessibility = accessibility
        self.duration = duration
        self.finished_at = finished_at
        self.gmt_create_time = gmt_create_time
        self.gmt_modified_time = gmt_modified_time
        self.message = message
        self.name = name
        self.node_id = node_id
        self.parent_user_id = parent_user_id
        self.pipeline_id = pipeline_id
        self.pipeline_run_id = pipeline_run_id
        self.pipeline_run_uri = pipeline_run_uri
        self.source_id = source_id
        self.source_type = source_type
        self.started_at = started_at
        self.status = status
        self.user_id = user_id
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accessibility is not None:
            result['Accessibility'] = self.accessibility
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.finished_at is not None:
            result['FinishedAt'] = self.finished_at
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.message is not None:
            result['Message'] = self.message
        if self.name is not None:
            result['Name'] = self.name
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.parent_user_id is not None:
            result['ParentUserId'] = self.parent_user_id
        if self.pipeline_id is not None:
            result['PipelineId'] = self.pipeline_id
        if self.pipeline_run_id is not None:
            result['PipelineRunId'] = self.pipeline_run_id
        if self.pipeline_run_uri is not None:
            result['PipelineRunUri'] = self.pipeline_run_uri
        if self.source_id is not None:
            result['SourceId'] = self.source_id
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.started_at is not None:
            result['StartedAt'] = self.started_at
        if self.status is not None:
            result['Status'] = self.status
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accessibility') is not None:
            self.accessibility = m.get('Accessibility')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('FinishedAt') is not None:
            self.finished_at = m.get('FinishedAt')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('ParentUserId') is not None:
            self.parent_user_id = m.get('ParentUserId')
        if m.get('PipelineId') is not None:
            self.pipeline_id = m.get('PipelineId')
        if m.get('PipelineRunId') is not None:
            self.pipeline_run_id = m.get('PipelineRunId')
        if m.get('PipelineRunUri') is not None:
            self.pipeline_run_uri = m.get('PipelineRunUri')
        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('StartedAt') is not None:
            self.started_at = m.get('StartedAt')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class ListPipelineRunsResponseBody(TeaModel):
    def __init__(
        self,
        pipeline_runs: List[ListPipelineRunsResponseBodyPipelineRuns] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.pipeline_runs = pipeline_runs
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.pipeline_runs:
            for k in self.pipeline_runs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PipelineRuns'] = []
        if self.pipeline_runs is not None:
            for k in self.pipeline_runs:
                result['PipelineRuns'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.pipeline_runs = []
        if m.get('PipelineRuns') is not None:
            for k in m.get('PipelineRuns'):
                temp_model = ListPipelineRunsResponseBodyPipelineRuns()
                self.pipeline_runs.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListPipelineRunsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListPipelineRunsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListPipelineRunsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPipelineRunsStatusRequestNodes(TeaModel):
    def __init__(
        self,
        node_id: str = None,
        pipeline_run_id: str = None,
    ):
        self.node_id = node_id
        self.pipeline_run_id = pipeline_run_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.pipeline_run_id is not None:
            result['PipelineRunId'] = self.pipeline_run_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('PipelineRunId') is not None:
            self.pipeline_run_id = m.get('PipelineRunId')
        return self


class ListPipelineRunsStatusRequest(TeaModel):
    def __init__(
        self,
        nodes: List[ListPipelineRunsStatusRequestNodes] = None,
        output_type: str = None,
        pipeline_runs: List[str] = None,
        workspace_id: str = None,
    ):
        self.nodes = nodes
        self.output_type = output_type
        self.pipeline_runs = pipeline_runs
        self.workspace_id = workspace_id

    def validate(self):
        if self.nodes:
            for k in self.nodes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Nodes'] = []
        if self.nodes is not None:
            for k in self.nodes:
                result['Nodes'].append(k.to_map() if k else None)
        if self.output_type is not None:
            result['OutputType'] = self.output_type
        if self.pipeline_runs is not None:
            result['PipelineRuns'] = self.pipeline_runs
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.nodes = []
        if m.get('Nodes') is not None:
            for k in m.get('Nodes'):
                temp_model = ListPipelineRunsStatusRequestNodes()
                self.nodes.append(temp_model.from_map(k))
        if m.get('OutputType') is not None:
            self.output_type = m.get('OutputType')
        if m.get('PipelineRuns') is not None:
            self.pipeline_runs = m.get('PipelineRuns')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class ListPipelineRunsStatusResponseBodyNodes(TeaModel):
    def __init__(
        self,
        finished_at: str = None,
        input_artifact_archived: bool = None,
        node_id: str = None,
        node_name: str = None,
        output_artifact_archived: bool = None,
        pipeline_run_id: str = None,
        started_at: str = None,
        status: str = None,
    ):
        self.finished_at = finished_at
        self.input_artifact_archived = input_artifact_archived
        self.node_id = node_id
        self.node_name = node_name
        self.output_artifact_archived = output_artifact_archived
        self.pipeline_run_id = pipeline_run_id
        self.started_at = started_at
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.finished_at is not None:
            result['FinishedAt'] = self.finished_at
        if self.input_artifact_archived is not None:
            result['InputArtifactArchived'] = self.input_artifact_archived
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.node_name is not None:
            result['NodeName'] = self.node_name
        if self.output_artifact_archived is not None:
            result['OutputArtifactArchived'] = self.output_artifact_archived
        if self.pipeline_run_id is not None:
            result['PipelineRunId'] = self.pipeline_run_id
        if self.started_at is not None:
            result['StartedAt'] = self.started_at
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FinishedAt') is not None:
            self.finished_at = m.get('FinishedAt')
        if m.get('InputArtifactArchived') is not None:
            self.input_artifact_archived = m.get('InputArtifactArchived')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')
        if m.get('OutputArtifactArchived') is not None:
            self.output_artifact_archived = m.get('OutputArtifactArchived')
        if m.get('PipelineRunId') is not None:
            self.pipeline_run_id = m.get('PipelineRunId')
        if m.get('StartedAt') is not None:
            self.started_at = m.get('StartedAt')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListPipelineRunsStatusResponseBodyOutputs(TeaModel):
    def __init__(
        self,
        expandable_artifact_name: str = None,
        expanded_artifact_index: int = None,
        gmt_create_time: str = None,
        id: str = None,
        metadata: Dict[str, Any] = None,
        name: str = None,
        node_id: str = None,
        pipeline_run_id: str = None,
        producer: str = None,
        type: str = None,
        value: str = None,
    ):
        self.expandable_artifact_name = expandable_artifact_name
        self.expanded_artifact_index = expanded_artifact_index
        self.gmt_create_time = gmt_create_time
        self.id = id
        self.metadata = metadata
        self.name = name
        self.node_id = node_id
        self.pipeline_run_id = pipeline_run_id
        self.producer = producer
        self.type = type
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expandable_artifact_name is not None:
            result['ExpandableArtifactName'] = self.expandable_artifact_name
        if self.expanded_artifact_index is not None:
            result['ExpandedArtifactIndex'] = self.expanded_artifact_index
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.id is not None:
            result['Id'] = self.id
        if self.metadata is not None:
            result['Metadata'] = self.metadata
        if self.name is not None:
            result['Name'] = self.name
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.pipeline_run_id is not None:
            result['PipelineRunId'] = self.pipeline_run_id
        if self.producer is not None:
            result['Producer'] = self.producer
        if self.type is not None:
            result['Type'] = self.type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExpandableArtifactName') is not None:
            self.expandable_artifact_name = m.get('ExpandableArtifactName')
        if m.get('ExpandedArtifactIndex') is not None:
            self.expanded_artifact_index = m.get('ExpandedArtifactIndex')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('PipelineRunId') is not None:
            self.pipeline_run_id = m.get('PipelineRunId')
        if m.get('Producer') is not None:
            self.producer = m.get('Producer')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListPipelineRunsStatusResponseBodyPipelineRuns(TeaModel):
    def __init__(
        self,
        is_deleted: bool = None,
        name: str = None,
        node_id: str = None,
        parent_user_id: str = None,
        pipeline_run_id: str = None,
        source_id: str = None,
        status: str = None,
        user_id: str = None,
    ):
        self.is_deleted = is_deleted
        self.name = name
        self.node_id = node_id
        self.parent_user_id = parent_user_id
        self.pipeline_run_id = pipeline_run_id
        self.source_id = source_id
        self.status = status
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_deleted is not None:
            result['IsDeleted'] = self.is_deleted
        if self.name is not None:
            result['Name'] = self.name
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.parent_user_id is not None:
            result['ParentUserId'] = self.parent_user_id
        if self.pipeline_run_id is not None:
            result['PipelineRunId'] = self.pipeline_run_id
        if self.source_id is not None:
            result['SourceId'] = self.source_id
        if self.status is not None:
            result['Status'] = self.status
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsDeleted') is not None:
            self.is_deleted = m.get('IsDeleted')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('ParentUserId') is not None:
            self.parent_user_id = m.get('ParentUserId')
        if m.get('PipelineRunId') is not None:
            self.pipeline_run_id = m.get('PipelineRunId')
        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class ListPipelineRunsStatusResponseBody(TeaModel):
    def __init__(
        self,
        nodes: List[ListPipelineRunsStatusResponseBodyNodes] = None,
        outputs: List[ListPipelineRunsStatusResponseBodyOutputs] = None,
        pipeline_runs: List[ListPipelineRunsStatusResponseBodyPipelineRuns] = None,
        request_id: str = None,
    ):
        self.nodes = nodes
        self.outputs = outputs
        self.pipeline_runs = pipeline_runs
        self.request_id = request_id

    def validate(self):
        if self.nodes:
            for k in self.nodes:
                if k:
                    k.validate()
        if self.outputs:
            for k in self.outputs:
                if k:
                    k.validate()
        if self.pipeline_runs:
            for k in self.pipeline_runs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Nodes'] = []
        if self.nodes is not None:
            for k in self.nodes:
                result['Nodes'].append(k.to_map() if k else None)
        result['Outputs'] = []
        if self.outputs is not None:
            for k in self.outputs:
                result['Outputs'].append(k.to_map() if k else None)
        result['PipelineRuns'] = []
        if self.pipeline_runs is not None:
            for k in self.pipeline_runs:
                result['PipelineRuns'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.nodes = []
        if m.get('Nodes') is not None:
            for k in m.get('Nodes'):
                temp_model = ListPipelineRunsStatusResponseBodyNodes()
                self.nodes.append(temp_model.from_map(k))
        self.outputs = []
        if m.get('Outputs') is not None:
            for k in m.get('Outputs'):
                temp_model = ListPipelineRunsStatusResponseBodyOutputs()
                self.outputs.append(temp_model.from_map(k))
        self.pipeline_runs = []
        if m.get('PipelineRuns') is not None:
            for k in m.get('PipelineRuns'):
                temp_model = ListPipelineRunsStatusResponseBodyPipelineRuns()
                self.pipeline_runs.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListPipelineRunsStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListPipelineRunsStatusResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListPipelineRunsStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPipelinesRequest(TeaModel):
    def __init__(
        self,
        fuzzy_matching: bool = None,
        page_number: int = None,
        page_size: int = None,
        pipeline_identifier: str = None,
        pipeline_provider: str = None,
        pipeline_version: str = None,
        workspace_id: str = None,
    ):
        self.fuzzy_matching = fuzzy_matching
        self.page_number = page_number
        self.page_size = page_size
        self.pipeline_identifier = pipeline_identifier
        self.pipeline_provider = pipeline_provider
        self.pipeline_version = pipeline_version
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fuzzy_matching is not None:
            result['FuzzyMatching'] = self.fuzzy_matching
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.pipeline_identifier is not None:
            result['PipelineIdentifier'] = self.pipeline_identifier
        if self.pipeline_provider is not None:
            result['PipelineProvider'] = self.pipeline_provider
        if self.pipeline_version is not None:
            result['PipelineVersion'] = self.pipeline_version
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FuzzyMatching') is not None:
            self.fuzzy_matching = m.get('FuzzyMatching')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PipelineIdentifier') is not None:
            self.pipeline_identifier = m.get('PipelineIdentifier')
        if m.get('PipelineProvider') is not None:
            self.pipeline_provider = m.get('PipelineProvider')
        if m.get('PipelineVersion') is not None:
            self.pipeline_version = m.get('PipelineVersion')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class ListPipelinesResponseBodyPipelines(TeaModel):
    def __init__(
        self,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        identifier: str = None,
        pipeline_id: str = None,
        provider: str = None,
        uuid: str = None,
        version: str = None,
        workspace_id: str = None,
    ):
        self.gmt_create_time = gmt_create_time
        self.gmt_modified_time = gmt_modified_time
        self.identifier = identifier
        self.pipeline_id = pipeline_id
        self.provider = provider
        self.uuid = uuid
        self.version = version
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.identifier is not None:
            result['Identifier'] = self.identifier
        if self.pipeline_id is not None:
            result['PipelineId'] = self.pipeline_id
        if self.provider is not None:
            result['Provider'] = self.provider
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        if self.version is not None:
            result['Version'] = self.version
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('Identifier') is not None:
            self.identifier = m.get('Identifier')
        if m.get('PipelineId') is not None:
            self.pipeline_id = m.get('PipelineId')
        if m.get('Provider') is not None:
            self.provider = m.get('Provider')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class ListPipelinesResponseBody(TeaModel):
    def __init__(
        self,
        pipelines: List[ListPipelinesResponseBodyPipelines] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.pipelines = pipelines
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.pipelines:
            for k in self.pipelines:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Pipelines'] = []
        if self.pipelines is not None:
            for k in self.pipelines:
                result['Pipelines'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.pipelines = []
        if m.get('Pipelines') is not None:
            for k in m.get('Pipelines'):
                temp_model = ListPipelinesResponseBodyPipelines()
                self.pipelines.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListPipelinesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListPipelinesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListPipelinesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RerunPipelineRunResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RerunPipelineRunResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RerunPipelineRunResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RerunPipelineRunResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartPipelineRunResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StartPipelineRunResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StartPipelineRunResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = StartPipelineRunResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TerminatePipelineRunResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class TerminatePipelineRunResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: TerminatePipelineRunResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = TerminatePipelineRunResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdatePipelineRequest(TeaModel):
    def __init__(
        self,
        manifest: str = None,
    ):
        self.manifest = manifest

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.manifest is not None:
            result['Manifest'] = self.manifest
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Manifest') is not None:
            self.manifest = m.get('Manifest')
        return self


class UpdatePipelineResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdatePipelineResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdatePipelineResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdatePipelineResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdatePipelineRunRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
    ):
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class UpdatePipelineRunResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdatePipelineRunResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdatePipelineRunResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdatePipelineRunResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


