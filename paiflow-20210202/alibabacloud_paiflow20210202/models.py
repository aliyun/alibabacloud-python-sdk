# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List, Any


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
        # 创建UTC时间，日期格式iso8601。
        self.gmt_create_time = gmt_create_time
        # 修改UTC时间，日期格式iso8601。
        self.gmt_modified_time = gmt_modified_time
        # Pipeline标识。
        self.identifier = identifier
        # Pipeline ID。
        self.pipeline_id = pipeline_id
        # 用户自定义Pipeline时，为用户ID。 官方Pipeline为pai。
        self.provider = provider
        # Pipeline当前版本标识，用户每次更新，会生成该uuid。
        self.uuid = uuid
        # Pipeline版本。
        self.version = version
        # AI工作空间ID。
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
        # 实验可见度，目前有PUBLIC（公开）、PRIVATE（私有）。
        self.accessibility = accessibility
        # 运行时长，单位为秒。
        self.duration = duration
        # 实验ID。
        self.experiment_id = experiment_id
        # Run运行完成时间。
        self.finished_at = finished_at
        # Run的创建UTC时间，格式iso8601。
        self.gmt_create_time = gmt_create_time
        # Run最近修改的UTC时间，格式iso8601。
        self.gmt_modified_time = gmt_modified_time
        # 错误信息。
        self.message = message
        # Run的名称。
        self.name = name
        # 节点ID。
        self.node_id = node_id
        # Owner ID。
        self.parent_user_id = parent_user_id
        # Run ID。
        self.run_id = run_id
        # 来源。
        self.source = source
        # Run运行开始时间。
        self.started_at = started_at
        # Run的状态，目前如下几种状态。  Initialized Running Succeeded Failed Suspended Terminated Unknown Skipped Terminating
        self.status = status
        # 创建人ID。
        self.user_id = user_id
        # 所属工作空间ID。
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
        # Id of the request
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
        body: CreatePipelineResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreatePipelineResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatePipelineReleaseRequest(TeaModel):
    def __init__(
        self,
        target_pipeline_provider: str = None,
    ):
        self.target_pipeline_provider = target_pipeline_provider

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.target_pipeline_provider is not None:
            result['TargetPipelineProvider'] = self.target_pipeline_provider
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TargetPipelineProvider') is not None:
            self.target_pipeline_provider = m.get('TargetPipelineProvider')
        return self


class CreatePipelineReleaseResponseBody(TeaModel):
    def __init__(
        self,
        pipeline_id: str = None,
        request_id: str = None,
    ):
        self.pipeline_id = pipeline_id
        # Id of the request
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


class CreatePipelineReleaseResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreatePipelineReleaseResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreatePipelineReleaseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRunRequest(TeaModel):
    def __init__(
        self,
        accessibility: str = None,
        arguments: str = None,
        experiment_id: str = None,
        name: str = None,
        no_confirm_required: bool = None,
        options: str = None,
        pipeline_id: str = None,
        pipeline_manifest: str = None,
        source: str = None,
        workspace_id: str = None,
    ):
        # PUBLIC 公开；PRIVATE 私有
        self.accessibility = accessibility
        # 参数
        self.arguments = arguments
        # 实验id
        self.experiment_id = experiment_id
        # Run的名字，若为空，则自动生成名字
        self.name = name
        # true代表直接启动; false代表只创建run但先不启动
        self.no_confirm_required = no_confirm_required
        # 选项，json格式
        self.options = options
        # Pipeline的id; PipelineId和PipelineManifest 二选一
        self.pipeline_id = pipeline_id
        # Pipeline内容; PipelineId和PipelineManifest 二选一一
        self.pipeline_manifest = pipeline_manifest
        # 来源，支持如下值：SDK; PAI_STUDIO; M6; UNKNOWN;
        self.source = source
        # 项目空间id
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
        if self.experiment_id is not None:
            result['ExperimentId'] = self.experiment_id
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
        if self.source is not None:
            result['Source'] = self.source
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accessibility') is not None:
            self.accessibility = m.get('Accessibility')
        if m.get('Arguments') is not None:
            self.arguments = m.get('Arguments')
        if m.get('ExperimentId') is not None:
            self.experiment_id = m.get('ExperimentId')
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
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class CreateRunResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        run_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        # run的id
        self.run_id = run_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.run_id is not None:
            result['RunId'] = self.run_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RunId') is not None:
            self.run_id = m.get('RunId')
        return self


class CreateRunResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateRunResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateRunResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeletePipelineResponseBody(TeaModel):
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


class DeletePipelineResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeletePipelineResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeletePipelineResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteRunResponseBody(TeaModel):
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


class DeleteRunResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteRunResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteRunResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCallerProviderResponseBody(TeaModel):
    def __init__(
        self,
        provider: str = None,
        request_id: str = None,
    ):
        self.provider = provider
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.provider is not None:
            result['Provider'] = self.provider
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Provider') is not None:
            self.provider = m.get('Provider')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetCallerProviderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetCallerProviderResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetCallerProviderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetNodeRequest(TeaModel):
    def __init__(
        self,
        depth: int = None,
    ):
        # 查询深度
        self.depth = depth

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.depth is not None:
            result['Depth'] = self.depth
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Depth') is not None:
            self.depth = m.get('Depth')
        return self


class GetNodeResponseBodyMetadata(TeaModel):
    def __init__(
        self,
        display_name: str = None,
        identifier: str = None,
        name: str = None,
        namespace: str = None,
        node_id: str = None,
        node_type: str = None,
        provider: str = None,
        related_node_ids: List[str] = None,
        version: str = None,
    ):
        # 展示名称
        self.display_name = display_name
        # 标识符
        self.identifier = identifier
        # 名字
        self.name = name
        # 所在命名空间
        self.namespace = namespace
        # 节点 id
        self.node_id = node_id
        # 节点类型
        self.node_type = node_type
        # 提供方
        self.provider = provider
        # Alink逻辑节点所对应的物理节点ID / Alink物理节点所对应的逻辑节点ID
        self.related_node_ids = related_node_ids
        # 版本
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
        if self.namespace is not None:
            result['Namespace'] = self.namespace
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
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
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


class GetNodeResponseBodySpecInputs(TeaModel):
    def __init__(
        self,
        artifacts: List[Dict[str, Any]] = None,
        parameters: List[Dict[str, Any]] = None,
    ):
        # 产物
        self.artifacts = artifacts
        # 参数
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


class GetNodeResponseBodySpecOutputs(TeaModel):
    def __init__(
        self,
        artifacts: List[Dict[str, Any]] = None,
        parameters: List[Dict[str, Any]] = None,
    ):
        # 产物
        self.artifacts = artifacts
        # 参数
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


class GetNodeResponseBodySpec(TeaModel):
    def __init__(
        self,
        dependencies: List[str] = None,
        has_pipelines: bool = None,
        inputs: GetNodeResponseBodySpecInputs = None,
        outputs: GetNodeResponseBodySpecOutputs = None,
        pipelines: List[Dict[str, Any]] = None,
    ):
        # 依赖
        self.dependencies = dependencies
        # 是否有子 pipeline
        self.has_pipelines = has_pipelines
        # 输入
        self.inputs = inputs
        # 输出
        self.outputs = outputs
        # 子 pipeline 列表
        self.pipelines = pipelines

    def validate(self):
        if self.inputs:
            self.inputs.validate()
        if self.outputs:
            self.outputs.validate()

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
        if self.pipelines is not None:
            result['Pipelines'] = self.pipelines
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Dependencies') is not None:
            self.dependencies = m.get('Dependencies')
        if m.get('HasPipelines') is not None:
            self.has_pipelines = m.get('HasPipelines')
        if m.get('Inputs') is not None:
            temp_model = GetNodeResponseBodySpecInputs()
            self.inputs = temp_model.from_map(m['Inputs'])
        if m.get('Outputs') is not None:
            temp_model = GetNodeResponseBodySpecOutputs()
            self.outputs = temp_model.from_map(m['Outputs'])
        if m.get('Pipelines') is not None:
            self.pipelines = m.get('Pipelines')
        return self


class GetNodeResponseBodyStatusInfo(TeaModel):
    def __init__(
        self,
        finished_at: str = None,
        started_at: str = None,
        status: str = None,
    ):
        # 结束时间
        self.finished_at = finished_at
        # 开始时间
        self.started_at = started_at
        # 状态
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
        if self.started_at is not None:
            result['StartedAt'] = self.started_at
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FinishedAt') is not None:
            self.finished_at = m.get('FinishedAt')
        if m.get('StartedAt') is not None:
            self.started_at = m.get('StartedAt')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetNodeResponseBody(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        metadata: GetNodeResponseBodyMetadata = None,
        request_id: str = None,
        spec: GetNodeResponseBodySpec = None,
        status_info: GetNodeResponseBodyStatusInfo = None,
    ):
        # api 版本
        self.api_version = api_version
        # node 的元信息
        self.metadata = metadata
        # 请求 id
        self.request_id = request_id
        # 算法体
        self.spec = spec
        # node 运行状态
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
            temp_model = GetNodeResponseBodyMetadata()
            self.metadata = temp_model.from_map(m['Metadata'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Spec') is not None:
            temp_model = GetNodeResponseBodySpec()
            self.spec = temp_model.from_map(m['Spec'])
        if m.get('StatusInfo') is not None:
            temp_model = GetNodeResponseBodyStatusInfo()
            self.status_info = temp_model.from_map(m['StatusInfo'])
        return self


class GetNodeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetNodeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetNodeResponseBody()
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
        # Id of the request
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
        body: GetPipelineResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetPipelineResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPipelineSchemaResponseBody(TeaModel):
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
        # Id of the request
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


class GetPipelineSchemaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetPipelineSchemaResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetPipelineSchemaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRunRequest(TeaModel):
    def __init__(
        self,
        manifest_type: str = None,
        verbose: bool = None,
    ):
        self.manifest_type = manifest_type
        # 是否返回详细信息，目前详细信息包含： RuntimeManifest
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
        if self.verbose is not None:
            result['Verbose'] = self.verbose
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ManifestType') is not None:
            self.manifest_type = m.get('ManifestType')
        if m.get('Verbose') is not None:
            self.verbose = m.get('Verbose')
        return self


class GetRunResponseBody(TeaModel):
    def __init__(
        self,
        arguments: str = None,
        duration: int = None,
        experiment_id: str = None,
        finished_at: int = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        manifest: str = None,
        message: str = None,
        name: str = None,
        node_id: str = None,
        options: str = None,
        parent_user_id: str = None,
        pipeline_id: str = None,
        request_id: str = None,
        run_id: str = None,
        source: str = None,
        started_at: int = None,
        status: str = None,
        user_id: str = None,
        workspace_id: str = None,
    ):
        # run的参数
        self.arguments = arguments
        # run的运行时长，以s为单位
        self.duration = duration
        # run关联的实验id
        self.experiment_id = experiment_id
        # run的结束 UTC 时间，格式 iso8601
        self.finished_at = finished_at
        # 创建时间
        self.gmt_create_time = gmt_create_time
        # 修改时间
        self.gmt_modified_time = gmt_modified_time
        # run的manifest
        self.manifest = manifest
        # 错误消息
        self.message = message
        # run的名字
        self.name = name
        # run的根节点id
        self.node_id = node_id
        # 选项
        self.options = options
        # 用户主账户的uid
        self.parent_user_id = parent_user_id
        # pipeline的id
        self.pipeline_id = pipeline_id
        # Id of the request
        self.request_id = request_id
        # run的id
        self.run_id = run_id
        # run的来源
        self.source = source
        # run的开始 UTC 时间，格式 iso8601
        self.started_at = started_at
        # run的状态
        self.status = status
        # 用户uid
        self.user_id = user_id
        # 工作空间id
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arguments is not None:
            result['Arguments'] = self.arguments
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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
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
        if m.get('Arguments') is not None:
            self.arguments = m.get('Arguments')
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
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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


class GetRunResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetRunResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetRunResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRunStatisticsRequest(TeaModel):
    def __init__(
        self,
        experiment_id: str = None,
        is_show_all: bool = None,
        name: str = None,
        pipeline_id: str = None,
        scope: str = None,
        source: str = None,
        status: List[str] = None,
        workspace_id: str = None,
    ):
        # 实验的id
        self.experiment_id = experiment_id
        # 是否统计主账户下所有子账户的数据
        self.is_show_all = is_show_all
        # run的名字
        self.name = name
        # pipeline的id
        self.pipeline_id = pipeline_id
        # run的范围
        self.scope = scope
        # run的来源
        self.source = source
        # run的状态
        self.status = status
        # 工作空间id 该字段仅对Scope为User有效，统计该用户在该工作空间下的数据
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.experiment_id is not None:
            result['ExperimentId'] = self.experiment_id
        if self.is_show_all is not None:
            result['IsShowAll'] = self.is_show_all
        if self.name is not None:
            result['Name'] = self.name
        if self.pipeline_id is not None:
            result['PipelineId'] = self.pipeline_id
        if self.scope is not None:
            result['Scope'] = self.scope
        if self.source is not None:
            result['Source'] = self.source
        if self.status is not None:
            result['Status'] = self.status
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExperimentId') is not None:
            self.experiment_id = m.get('ExperimentId')
        if m.get('IsShowAll') is not None:
            self.is_show_all = m.get('IsShowAll')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PipelineId') is not None:
            self.pipeline_id = m.get('PipelineId')
        if m.get('Scope') is not None:
            self.scope = m.get('Scope')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class GetRunStatisticsShrinkRequest(TeaModel):
    def __init__(
        self,
        experiment_id: str = None,
        is_show_all: bool = None,
        name: str = None,
        pipeline_id: str = None,
        scope: str = None,
        source: str = None,
        status_shrink: str = None,
        workspace_id: str = None,
    ):
        # 实验的id
        self.experiment_id = experiment_id
        # 是否统计主账户下所有子账户的数据
        self.is_show_all = is_show_all
        # run的名字
        self.name = name
        # pipeline的id
        self.pipeline_id = pipeline_id
        # run的范围
        self.scope = scope
        # run的来源
        self.source = source
        # run的状态
        self.status_shrink = status_shrink
        # 工作空间id 该字段仅对Scope为User有效，统计该用户在该工作空间下的数据
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.experiment_id is not None:
            result['ExperimentId'] = self.experiment_id
        if self.is_show_all is not None:
            result['IsShowAll'] = self.is_show_all
        if self.name is not None:
            result['Name'] = self.name
        if self.pipeline_id is not None:
            result['PipelineId'] = self.pipeline_id
        if self.scope is not None:
            result['Scope'] = self.scope
        if self.source is not None:
            result['Source'] = self.source
        if self.status_shrink is not None:
            result['Status'] = self.status_shrink
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExperimentId') is not None:
            self.experiment_id = m.get('ExperimentId')
        if m.get('IsShowAll') is not None:
            self.is_show_all = m.get('IsShowAll')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PipelineId') is not None:
            self.pipeline_id = m.get('PipelineId')
        if m.get('Scope') is not None:
            self.scope = m.get('Scope')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Status') is not None:
            self.status_shrink = m.get('Status')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class GetRunStatisticsResponseBody(TeaModel):
    def __init__(
        self,
        failed: int = None,
        running: int = None,
        request_id: str = None,
    ):
        # 失败run的个数
        self.failed = failed
        # 运行中run的个数
        self.running = running
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.failed is not None:
            result['Failed'] = self.failed
        if self.running is not None:
            result['Running'] = self.running
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Failed') is not None:
            self.failed = m.get('Failed')
        if m.get('Running') is not None:
            self.running = m.get('Running')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetRunStatisticsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetRunStatisticsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetRunStatisticsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListNodeLogsRequest(TeaModel):
    def __init__(
        self,
        from_time_in_seconds: int = None,
        keyword: str = None,
        offset: int = None,
        page_size: int = None,
        reverse: bool = None,
        to_time_in_seconds: int = None,
    ):
        # 开始时间
        self.from_time_in_seconds = from_time_in_seconds
        # 搜索词
        self.keyword = keyword
        # 当前偏移量
        self.offset = offset
        # 每页返回的log数目
        self.page_size = page_size
        # 是否倒排
        self.reverse = reverse
        # 结束时间
        self.to_time_in_seconds = to_time_in_seconds

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
        return self


class ListNodeLogsResponseBody(TeaModel):
    def __init__(
        self,
        logs: List[str] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # 日志列表
        self.logs = logs
        # 请求 ID
        self.request_id = request_id
        # 符合过滤条件的作业数量
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


class ListNodeLogsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListNodeLogsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListNodeLogsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListNodeOutputsRequest(TeaModel):
    def __init__(
        self,
        depth: int = None,
        name: str = None,
        order: str = None,
        page_number: int = None,
        page_size: int = None,
        sort_by: str = None,
        type: str = None,
    ):
        # 节点往下拿多少层子节点
        self.depth = depth
        # 节点名字
        self.name = name
        # 排序顺序， 顺序：ASC，倒序：DESC
        self.order = order
        # 当前页，页码从1开始
        self.page_number = page_number
        # 每页返回的输出数目
        self.page_size = page_size
        # 排序字段
        self.sort_by = sort_by
        # artifact 类型
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
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListNodeOutputsResponseBodyOutputs(TeaModel):
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
        value: str = None,
    ):
        # 可扩展artifact的名字
        self.expandable_artifact_name = expandable_artifact_name
        # 被扩展artifact的索引号，以0开始
        self.expanded_artifact_index = expanded_artifact_index
        # 创建时间
        self.gmt_create_time = gmt_create_time
        # id
        self.id = id
        # artifact内容
        self.info = info
        # 名字
        self.name = name
        # 输出所属节点 id
        self.node_id = node_id
        # rtifact生产者
        self.producer = producer
        # 类型
        self.type = type
        # 输出内容
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
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListNodeOutputsResponseBody(TeaModel):
    def __init__(
        self,
        outputs: List[ListNodeOutputsResponseBodyOutputs] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # 输出列表
        self.outputs = outputs
        # 请求ID
        self.request_id = request_id
        # 符合过滤条件的作业数量
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
                temp_model = ListNodeOutputsResponseBodyOutputs()
                self.outputs.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListNodeOutputsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListNodeOutputsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListNodeOutputsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListNodeStatusRequest(TeaModel):
    def __init__(
        self,
        depth: int = None,
        type: str = None,
    ):
        # 深度
        self.depth = depth
        # 类型
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
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Depth') is not None:
            self.depth = m.get('Depth')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListNodeStatusResponseBodyStatus(TeaModel):
    def __init__(
        self,
        finished_at: str = None,
        node_id: str = None,
        node_name: str = None,
        runtime_info: str = None,
        started_at: str = None,
        status: str = None,
    ):
        # 节点结束运行时间
        self.finished_at = finished_at
        # 工作流中节点ID
        self.node_id = node_id
        # 工作流中节点名字
        self.node_name = node_name
        # 节点运行时信息
        self.runtime_info = runtime_info
        # 节点开始运行时间
        self.started_at = started_at
        # 节点运行状态
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


class ListNodeStatusResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        status: List[ListNodeStatusResponseBodyStatus] = None,
    ):
        # 请求ID
        self.request_id = request_id
        # 工作流任务的节点状态列表
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
                temp_model = ListNodeStatusResponseBodyStatus()
                self.status.append(temp_model.from_map(k))
        return self


class ListNodeStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListNodeStatusResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListNodeStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPipelinePrivilegesResponseBody(TeaModel):
    def __init__(
        self,
        actions: List[str] = None,
        pipeline_id: str = None,
        request_id: str = None,
        users: List[str] = None,
    ):
        # [     "DescribeRun",     "PutRun",     "ListPipeline",     "GetPipeline"  ]
        self.actions = actions
        self.pipeline_id = pipeline_id
        # Id of the request
        self.request_id = request_id
        # [ "*" ]
        self.users = users

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.actions is not None:
            result['Actions'] = self.actions
        if self.pipeline_id is not None:
            result['PipelineId'] = self.pipeline_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.users is not None:
            result['Users'] = self.users
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Actions') is not None:
            self.actions = m.get('Actions')
        if m.get('PipelineId') is not None:
            self.pipeline_id = m.get('PipelineId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Users') is not None:
            self.users = m.get('Users')
        return self


class ListPipelinePrivilegesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListPipelinePrivilegesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListPipelinePrivilegesResponseBody()
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
        # 模糊匹配
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
        # Id of the request
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
        body: ListPipelinesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListPipelinesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRunsRequest(TeaModel):
    def __init__(
        self,
        experiment_id: str = None,
        name: str = None,
        order: str = None,
        page_number: int = None,
        page_size: int = None,
        pipeline_id: str = None,
        pipeline_ids: str = None,
        run_id: str = None,
        sort_by: str = None,
        source: str = None,
        status: str = None,
        user_id: str = None,
        workspace_id: str = None,
    ):
        self.experiment_id = experiment_id
        self.name = name
        self.order = order
        self.page_number = page_number
        self.page_size = page_size
        self.pipeline_id = pipeline_id
        # Pipeline的id集合，只有Source为M6可以使用该参数
        self.pipeline_ids = pipeline_ids
        self.run_id = run_id
        self.sort_by = sort_by
        self.source = source
        self.status = status
        # 用户id
        self.user_id = user_id
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.experiment_id is not None:
            result['ExperimentId'] = self.experiment_id
        if self.name is not None:
            result['Name'] = self.name
        if self.order is not None:
            result['Order'] = self.order
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.pipeline_id is not None:
            result['PipelineId'] = self.pipeline_id
        if self.pipeline_ids is not None:
            result['PipelineIds'] = self.pipeline_ids
        if self.run_id is not None:
            result['RunId'] = self.run_id
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.source is not None:
            result['Source'] = self.source
        if self.status is not None:
            result['Status'] = self.status
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExperimentId') is not None:
            self.experiment_id = m.get('ExperimentId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PipelineId') is not None:
            self.pipeline_id = m.get('PipelineId')
        if m.get('PipelineIds') is not None:
            self.pipeline_ids = m.get('PipelineIds')
        if m.get('RunId') is not None:
            self.run_id = m.get('RunId')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class ListRunsResponseBodyRuns(TeaModel):
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
        # PUBLIC 公开；PRIVATE 私有
        self.accessibility = accessibility
        self.duration = duration
        self.experiment_id = experiment_id
        self.finished_at = finished_at
        # 创建时间
        self.gmt_create_time = gmt_create_time
        # 修改时间
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


class ListRunsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        runs: List[ListRunsResponseBodyRuns] = None,
        total_count: int = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.runs = runs
        self.total_count = total_count

    def validate(self):
        if self.runs:
            for k in self.runs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Runs'] = []
        if self.runs is not None:
            for k in self.runs:
                result['Runs'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.runs = []
        if m.get('Runs') is not None:
            for k in m.get('Runs'):
                temp_model = ListRunsResponseBodyRuns()
                self.runs.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListRunsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListRunsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListRunsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRunsStatusRequestNodes(TeaModel):
    def __init__(
        self,
        node_id: str = None,
        run_id: str = None,
    ):
        self.node_id = node_id
        self.run_id = run_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.run_id is not None:
            result['RunId'] = self.run_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('RunId') is not None:
            self.run_id = m.get('RunId')
        return self


class ListRunsStatusRequest(TeaModel):
    def __init__(
        self,
        nodes: List[ListRunsStatusRequestNodes] = None,
        runs: List[str] = None,
        workspace_id: str = None,
    ):
        self.nodes = nodes
        self.runs = runs
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
        if self.runs is not None:
            result['Runs'] = self.runs
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.nodes = []
        if m.get('Nodes') is not None:
            for k in m.get('Nodes'):
                temp_model = ListRunsStatusRequestNodes()
                self.nodes.append(temp_model.from_map(k))
        if m.get('Runs') is not None:
            self.runs = m.get('Runs')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class ListRunsStatusResponseBodyNodes(TeaModel):
    def __init__(
        self,
        finished_at: str = None,
        input_artifact_archived: bool = None,
        node_id: str = None,
        node_name: str = None,
        output_artifact_archived: bool = None,
        run_id: str = None,
        started_at: str = None,
        status: str = None,
    ):
        # 修改 UTC 时间，日期格式 iso8601
        self.finished_at = finished_at
        # 输入artifact是否已保存
        self.input_artifact_archived = input_artifact_archived
        # 节点Id
        self.node_id = node_id
        # 节点名
        self.node_name = node_name
        # 输出artifact是否已保存
        self.output_artifact_archived = output_artifact_archived
        # 运行Id
        self.run_id = run_id
        # 修改 UTC 时间，日期格式 iso8601
        self.started_at = started_at
        # 状态
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
        if self.run_id is not None:
            result['RunId'] = self.run_id
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
        if m.get('RunId') is not None:
            self.run_id = m.get('RunId')
        if m.get('StartedAt') is not None:
            self.started_at = m.get('StartedAt')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListRunsStatusResponseBodyRuns(TeaModel):
    def __init__(
        self,
        experiment_id: str = None,
        is_deleted: bool = None,
        name: str = None,
        node_id: str = None,
        parent_user_id: str = None,
        run_id: str = None,
        status: str = None,
        user_id: str = None,
    ):
        # 实验id
        self.experiment_id = experiment_id
        # 是否被删除
        self.is_deleted = is_deleted
        # run名字
        self.name = name
        # 节点id
        self.node_id = node_id
        # 父账户id
        self.parent_user_id = parent_user_id
        # run的id
        self.run_id = run_id
        # run状态
        self.status = status
        # 用户id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.experiment_id is not None:
            result['ExperimentId'] = self.experiment_id
        if self.is_deleted is not None:
            result['IsDeleted'] = self.is_deleted
        if self.name is not None:
            result['Name'] = self.name
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.parent_user_id is not None:
            result['ParentUserId'] = self.parent_user_id
        if self.run_id is not None:
            result['RunId'] = self.run_id
        if self.status is not None:
            result['Status'] = self.status
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExperimentId') is not None:
            self.experiment_id = m.get('ExperimentId')
        if m.get('IsDeleted') is not None:
            self.is_deleted = m.get('IsDeleted')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('ParentUserId') is not None:
            self.parent_user_id = m.get('ParentUserId')
        if m.get('RunId') is not None:
            self.run_id = m.get('RunId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class ListRunsStatusResponseBody(TeaModel):
    def __init__(
        self,
        nodes: List[ListRunsStatusResponseBodyNodes] = None,
        request_id: str = None,
        runs: List[ListRunsStatusResponseBodyRuns] = None,
    ):
        self.nodes = nodes
        # Id of the request
        self.request_id = request_id
        self.runs = runs

    def validate(self):
        if self.nodes:
            for k in self.nodes:
                if k:
                    k.validate()
        if self.runs:
            for k in self.runs:
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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Runs'] = []
        if self.runs is not None:
            for k in self.runs:
                result['Runs'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.nodes = []
        if m.get('Nodes') is not None:
            for k in m.get('Nodes'):
                temp_model = ListRunsStatusResponseBodyNodes()
                self.nodes.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.runs = []
        if m.get('Runs') is not None:
            for k in m.get('Runs'):
                temp_model = ListRunsStatusResponseBodyRuns()
                self.runs.append(temp_model.from_map(k))
        return self


class ListRunsStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListRunsStatusResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListRunsStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartRunResponseBody(TeaModel):
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


class StartRunResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StartRunResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = StartRunResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TerminateRunResponseBody(TeaModel):
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


class TerminateRunResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: TerminateRunResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = TerminateRunResponseBody()
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


class UpdatePipelineResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdatePipelineResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdatePipelineResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdatePipelinePrivilegesRequest(TeaModel):
    def __init__(
        self,
        users: List[str] = None,
    ):
        self.users = users

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.users is not None:
            result['Users'] = self.users
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Users') is not None:
            self.users = m.get('Users')
        return self


class UpdatePipelinePrivilegesResponseBody(TeaModel):
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
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class UpdatePipelinePrivilegesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdatePipelinePrivilegesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdatePipelinePrivilegesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateRunRequest(TeaModel):
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


class UpdateRunResponseBody(TeaModel):
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


class UpdateRunResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateRunResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateRunResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


