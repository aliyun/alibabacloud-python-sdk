# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class AbortRunRequest(TeaModel):
    def __init__(
        self,
        workspace: str = None,
        run_id: str = None,
    ):
        # 工作空间名称
        self.workspace = workspace
        # 任务ID
        self.run_id = run_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        if self.run_id is not None:
            result['RunId'] = self.run_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        if m.get('RunId') is not None:
            self.run_id = m.get('RunId')
        return self


class AbortRunResponseBody(TeaModel):
    def __init__(
        self,
        host_id: str = None,
        request_id: str = None,
    ):
        # 主机ID
        self.host_id = host_id
        # 请求ID
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AbortRunResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AbortRunResponseBody = None,
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
            temp_model = AbortRunResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AbortSubmissionRequest(TeaModel):
    def __init__(
        self,
        workspace: str = None,
        submission_id: str = None,
    ):
        # 工作空间名称
        self.workspace = workspace
        # 投递ID
        self.submission_id = submission_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        if self.submission_id is not None:
            result['SubmissionId'] = self.submission_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        if m.get('SubmissionId') is not None:
            self.submission_id = m.get('SubmissionId')
        return self


class AbortSubmissionResponseBody(TeaModel):
    def __init__(
        self,
        host_id: str = None,
        request_id: str = None,
    ):
        # 主机ID
        self.host_id = host_id
        # 请求ID
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AbortSubmissionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AbortSubmissionResponseBody = None,
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
            temp_model = AbortSubmissionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAppRequestDependencies(TeaModel):
    def __init__(
        self,
        path: str = None,
        content: str = None,
    ):
        # 依赖路径
        self.path = path
        # 依赖内容
        self.content = content

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.path is not None:
            result['Path'] = self.path
        if self.content is not None:
            result['Content'] = self.content
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        return self


class CreateAppRequestConfigs(TeaModel):
    def __init__(
        self,
        path: str = None,
        content: str = None,
    ):
        self.path = path
        self.content = content

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.path is not None:
            result['Path'] = self.path
        if self.content is not None:
            result['Content'] = self.content
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        return self


class CreateAppRequest(TeaModel):
    def __init__(
        self,
        workspace: str = None,
        app_name: str = None,
        description: str = None,
        definition: str = None,
        language: str = None,
        language_version: str = None,
        app_type: str = None,
        documentation: str = None,
        revision_comment: str = None,
        labels: str = None,
        client_token: str = None,
        dependencies: List[CreateAppRequestDependencies] = None,
        configs: List[CreateAppRequestConfigs] = None,
        path: str = None,
    ):
        # 工作空间名称
        self.workspace = workspace
        # 应用名称
        self.app_name = app_name
        # 应用描述
        self.description = description
        # 应用定义
        self.definition = definition
        # 应用描述语言
        self.language = language
        # 应用描述语语言版本
        self.language_version = language_version
        # 应用类型
        self.app_type = app_type
        # 应用使用文档
        self.documentation = documentation
        # 应用当前版本说明
        self.revision_comment = revision_comment
        # 应用标签
        self.labels = labels
        # 幂等Token
        self.client_token = client_token
        # 依赖应用
        self.dependencies = dependencies
        # 参考输入
        self.configs = configs
        # 主WDL路径
        self.path = path

    def validate(self):
        if self.dependencies:
            for k in self.dependencies:
                if k:
                    k.validate()
        if self.configs:
            for k in self.configs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.description is not None:
            result['Description'] = self.description
        if self.definition is not None:
            result['Definition'] = self.definition
        if self.language is not None:
            result['Language'] = self.language
        if self.language_version is not None:
            result['LanguageVersion'] = self.language_version
        if self.app_type is not None:
            result['AppType'] = self.app_type
        if self.documentation is not None:
            result['Documentation'] = self.documentation
        if self.revision_comment is not None:
            result['RevisionComment'] = self.revision_comment
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        result['Dependencies'] = []
        if self.dependencies is not None:
            for k in self.dependencies:
                result['Dependencies'].append(k.to_map() if k else None)
        result['Configs'] = []
        if self.configs is not None:
            for k in self.configs:
                result['Configs'].append(k.to_map() if k else None)
        if self.path is not None:
            result['Path'] = self.path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Definition') is not None:
            self.definition = m.get('Definition')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('LanguageVersion') is not None:
            self.language_version = m.get('LanguageVersion')
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')
        if m.get('Documentation') is not None:
            self.documentation = m.get('Documentation')
        if m.get('RevisionComment') is not None:
            self.revision_comment = m.get('RevisionComment')
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        self.dependencies = []
        if m.get('Dependencies') is not None:
            for k in m.get('Dependencies'):
                temp_model = CreateAppRequestDependencies()
                self.dependencies.append(temp_model.from_map(k))
        self.configs = []
        if m.get('Configs') is not None:
            for k in m.get('Configs'):
                temp_model = CreateAppRequestConfigs()
                self.configs.append(temp_model.from_map(k))
        if m.get('Path') is not None:
            self.path = m.get('Path')
        return self


class CreateAppShrinkRequest(TeaModel):
    def __init__(
        self,
        workspace: str = None,
        app_name: str = None,
        description: str = None,
        definition: str = None,
        language: str = None,
        language_version: str = None,
        app_type: str = None,
        documentation: str = None,
        revision_comment: str = None,
        labels: str = None,
        client_token: str = None,
        dependencies_shrink: str = None,
        configs_shrink: str = None,
        path: str = None,
    ):
        # 工作空间名称
        self.workspace = workspace
        # 应用名称
        self.app_name = app_name
        # 应用描述
        self.description = description
        # 应用定义
        self.definition = definition
        # 应用描述语言
        self.language = language
        # 应用描述语语言版本
        self.language_version = language_version
        # 应用类型
        self.app_type = app_type
        # 应用使用文档
        self.documentation = documentation
        # 应用当前版本说明
        self.revision_comment = revision_comment
        # 应用标签
        self.labels = labels
        # 幂等Token
        self.client_token = client_token
        # 依赖应用
        self.dependencies_shrink = dependencies_shrink
        # 参考输入
        self.configs_shrink = configs_shrink
        # 主WDL路径
        self.path = path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.description is not None:
            result['Description'] = self.description
        if self.definition is not None:
            result['Definition'] = self.definition
        if self.language is not None:
            result['Language'] = self.language
        if self.language_version is not None:
            result['LanguageVersion'] = self.language_version
        if self.app_type is not None:
            result['AppType'] = self.app_type
        if self.documentation is not None:
            result['Documentation'] = self.documentation
        if self.revision_comment is not None:
            result['RevisionComment'] = self.revision_comment
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dependencies_shrink is not None:
            result['Dependencies'] = self.dependencies_shrink
        if self.configs_shrink is not None:
            result['Configs'] = self.configs_shrink
        if self.path is not None:
            result['Path'] = self.path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Definition') is not None:
            self.definition = m.get('Definition')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('LanguageVersion') is not None:
            self.language_version = m.get('LanguageVersion')
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')
        if m.get('Documentation') is not None:
            self.documentation = m.get('Documentation')
        if m.get('RevisionComment') is not None:
            self.revision_comment = m.get('RevisionComment')
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Dependencies') is not None:
            self.dependencies_shrink = m.get('Dependencies')
        if m.get('Configs') is not None:
            self.configs_shrink = m.get('Configs')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        return self


class CreateAppResponseBody(TeaModel):
    def __init__(
        self,
        workspace: str = None,
        app_name: str = None,
        host_id: str = None,
        request_id: str = None,
        revision: str = None,
    ):
        # 工作空间
        self.workspace = workspace
        # 应用名称
        self.app_name = app_name
        # 主机 ID
        self.host_id = host_id
        # 请求 ID
        self.request_id = request_id
        # 应用版本号
        self.revision = revision

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.revision is not None:
            result['Revision'] = self.revision
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Revision') is not None:
            self.revision = m.get('Revision')
        return self


class CreateAppResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateAppResponseBody = None,
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
            temp_model = CreateAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateEntityRequestEntityItems(TeaModel):
    def __init__(
        self,
        entity_name: str = None,
        entity_data: Dict[str, str] = None,
    ):
        self.entity_name = entity_name
        self.entity_data = entity_data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entity_name is not None:
            result['EntityName'] = self.entity_name
        if self.entity_data is not None:
            result['EntityData'] = self.entity_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EntityName') is not None:
            self.entity_name = m.get('EntityName')
        if m.get('EntityData') is not None:
            self.entity_data = m.get('EntityData')
        return self


class CreateEntityRequest(TeaModel):
    def __init__(
        self,
        workspace: str = None,
        entity_type: str = None,
        entity_items: List[CreateEntityRequestEntityItems] = None,
        client_token: str = None,
    ):
        self.workspace = workspace
        self.entity_type = entity_type
        self.entity_items = entity_items
        self.client_token = client_token

    def validate(self):
        if self.entity_items:
            for k in self.entity_items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        result['EntityItems'] = []
        if self.entity_items is not None:
            for k in self.entity_items:
                result['EntityItems'].append(k.to_map() if k else None)
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        self.entity_items = []
        if m.get('EntityItems') is not None:
            for k in m.get('EntityItems'):
                temp_model = CreateEntityRequestEntityItems()
                self.entity_items.append(temp_model.from_map(k))
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class CreateEntityShrinkRequest(TeaModel):
    def __init__(
        self,
        workspace: str = None,
        entity_type: str = None,
        entity_items_shrink: str = None,
        client_token: str = None,
    ):
        self.workspace = workspace
        self.entity_type = entity_type
        self.entity_items_shrink = entity_items_shrink
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.entity_items_shrink is not None:
            result['EntityItems'] = self.entity_items_shrink
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('EntityItems') is not None:
            self.entity_items_shrink = m.get('EntityItems')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class CreateEntityResponseBody(TeaModel):
    def __init__(
        self,
        host_id: str = None,
        request_id: str = None,
        workspace: str = None,
        entity_type: str = None,
    ):
        # 主机ID
        self.host_id = host_id
        # 请求ID
        self.request_id = request_id
        self.workspace = workspace
        self.entity_type = entity_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        return self


class CreateEntityResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateEntityResponseBody = None,
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
            temp_model = CreateEntityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRunRequest(TeaModel):
    def __init__(
        self,
        workspace: str = None,
        name: str = None,
        app_name: str = None,
        revision: str = None,
        description: str = None,
        labels: str = None,
        execute_options: str = None,
        execute_directory: str = None,
        output_folder: str = None,
        default_runtime: str = None,
        inputs: str = None,
        client_token: str = None,
    ):
        # 工作空间名字
        self.workspace = workspace
        # 任务名称
        self.name = name
        # 应用名称
        self.app_name = app_name
        # 应用版本号
        self.revision = revision
        # 任务描述
        self.description = description
        # 任务标签
        self.labels = labels
        # 任务配置
        self.execute_options = execute_options
        # 任务执行目录
        self.execute_directory = execute_directory
        # 任务输出拷贝目录
        self.output_folder = output_folder
        # 默认运行时
        self.default_runtime = default_runtime
        # 任务输入
        self.inputs = inputs
        # 任务幂等token
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        if self.name is not None:
            result['Name'] = self.name
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.revision is not None:
            result['Revision'] = self.revision
        if self.description is not None:
            result['Description'] = self.description
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.execute_options is not None:
            result['ExecuteOptions'] = self.execute_options
        if self.execute_directory is not None:
            result['ExecuteDirectory'] = self.execute_directory
        if self.output_folder is not None:
            result['OutputFolder'] = self.output_folder
        if self.default_runtime is not None:
            result['DefaultRuntime'] = self.default_runtime
        if self.inputs is not None:
            result['Inputs'] = self.inputs
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Revision') is not None:
            self.revision = m.get('Revision')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('ExecuteOptions') is not None:
            self.execute_options = m.get('ExecuteOptions')
        if m.get('ExecuteDirectory') is not None:
            self.execute_directory = m.get('ExecuteDirectory')
        if m.get('OutputFolder') is not None:
            self.output_folder = m.get('OutputFolder')
        if m.get('DefaultRuntime') is not None:
            self.default_runtime = m.get('DefaultRuntime')
        if m.get('Inputs') is not None:
            self.inputs = m.get('Inputs')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class CreateRunResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        host_id: str = None,
        workspace: str = None,
        run_id: str = None,
    ):
        # 请求ID
        self.request_id = request_id
        # 主机ID
        self.host_id = host_id
        # 工作空间
        self.workspace = workspace
        # 任务ID
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
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        if self.run_id is not None:
            result['RunId'] = self.run_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
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


class CreateSubmissionRequest(TeaModel):
    def __init__(
        self,
        workspace: str = None,
        app_name: str = None,
        revision: str = None,
        entity_type: str = None,
        entity_names: List[str] = None,
        execute_options: str = None,
        execute_directory: str = None,
        output_folder: str = None,
        default_runtime: str = None,
        inputs: str = None,
        outputs: str = None,
        client_token: str = None,
    ):
        # 工作空间名字
        self.workspace = workspace
        # 应用名称
        self.app_name = app_name
        # 应用版本号
        self.revision = revision
        # 实体类型
        self.entity_type = entity_type
        self.entity_names = entity_names
        # 任务配置
        self.execute_options = execute_options
        # 任务执行目录
        self.execute_directory = execute_directory
        # 任务输出拷贝目录
        self.output_folder = output_folder
        # 默认运行时
        self.default_runtime = default_runtime
        # 任务输入
        self.inputs = inputs
        # 任务输出
        self.outputs = outputs
        # 任务幂等token
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.revision is not None:
            result['Revision'] = self.revision
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.entity_names is not None:
            result['EntityNames'] = self.entity_names
        if self.execute_options is not None:
            result['ExecuteOptions'] = self.execute_options
        if self.execute_directory is not None:
            result['ExecuteDirectory'] = self.execute_directory
        if self.output_folder is not None:
            result['OutputFolder'] = self.output_folder
        if self.default_runtime is not None:
            result['DefaultRuntime'] = self.default_runtime
        if self.inputs is not None:
            result['Inputs'] = self.inputs
        if self.outputs is not None:
            result['Outputs'] = self.outputs
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Revision') is not None:
            self.revision = m.get('Revision')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('EntityNames') is not None:
            self.entity_names = m.get('EntityNames')
        if m.get('ExecuteOptions') is not None:
            self.execute_options = m.get('ExecuteOptions')
        if m.get('ExecuteDirectory') is not None:
            self.execute_directory = m.get('ExecuteDirectory')
        if m.get('OutputFolder') is not None:
            self.output_folder = m.get('OutputFolder')
        if m.get('DefaultRuntime') is not None:
            self.default_runtime = m.get('DefaultRuntime')
        if m.get('Inputs') is not None:
            self.inputs = m.get('Inputs')
        if m.get('Outputs') is not None:
            self.outputs = m.get('Outputs')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class CreateSubmissionShrinkRequest(TeaModel):
    def __init__(
        self,
        workspace: str = None,
        app_name: str = None,
        revision: str = None,
        entity_type: str = None,
        entity_names_shrink: str = None,
        execute_options: str = None,
        execute_directory: str = None,
        output_folder: str = None,
        default_runtime: str = None,
        inputs: str = None,
        outputs: str = None,
        client_token: str = None,
    ):
        # 工作空间名字
        self.workspace = workspace
        # 应用名称
        self.app_name = app_name
        # 应用版本号
        self.revision = revision
        # 实体类型
        self.entity_type = entity_type
        self.entity_names_shrink = entity_names_shrink
        # 任务配置
        self.execute_options = execute_options
        # 任务执行目录
        self.execute_directory = execute_directory
        # 任务输出拷贝目录
        self.output_folder = output_folder
        # 默认运行时
        self.default_runtime = default_runtime
        # 任务输入
        self.inputs = inputs
        # 任务输出
        self.outputs = outputs
        # 任务幂等token
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.revision is not None:
            result['Revision'] = self.revision
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.entity_names_shrink is not None:
            result['EntityNames'] = self.entity_names_shrink
        if self.execute_options is not None:
            result['ExecuteOptions'] = self.execute_options
        if self.execute_directory is not None:
            result['ExecuteDirectory'] = self.execute_directory
        if self.output_folder is not None:
            result['OutputFolder'] = self.output_folder
        if self.default_runtime is not None:
            result['DefaultRuntime'] = self.default_runtime
        if self.inputs is not None:
            result['Inputs'] = self.inputs
        if self.outputs is not None:
            result['Outputs'] = self.outputs
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Revision') is not None:
            self.revision = m.get('Revision')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('EntityNames') is not None:
            self.entity_names_shrink = m.get('EntityNames')
        if m.get('ExecuteOptions') is not None:
            self.execute_options = m.get('ExecuteOptions')
        if m.get('ExecuteDirectory') is not None:
            self.execute_directory = m.get('ExecuteDirectory')
        if m.get('OutputFolder') is not None:
            self.output_folder = m.get('OutputFolder')
        if m.get('DefaultRuntime') is not None:
            self.default_runtime = m.get('DefaultRuntime')
        if m.get('Inputs') is not None:
            self.inputs = m.get('Inputs')
        if m.get('Outputs') is not None:
            self.outputs = m.get('Outputs')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class CreateSubmissionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        host_id: str = None,
        workspace: str = None,
        submission_id: str = None,
    ):
        # 请求ID
        self.request_id = request_id
        # 主机ID
        self.host_id = host_id
        # 工作空间
        self.workspace = workspace
        # 投递ID
        self.submission_id = submission_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        if self.submission_id is not None:
            result['SubmissionId'] = self.submission_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        if m.get('SubmissionId') is not None:
            self.submission_id = m.get('SubmissionId')
        return self


class CreateSubmissionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateSubmissionResponseBody = None,
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
            temp_model = CreateSubmissionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTemplateRequestInputs(TeaModel):
    def __init__(
        self,
        task_name: str = None,
        variable_name: str = None,
        variable_type: str = None,
        variable_value: str = None,
        required: bool = None,
        help: str = None,
        step_order: int = None,
    ):
        # 任务名称
        self.task_name = task_name
        # 变量名
        self.variable_name = variable_name
        # 变量类型
        self.variable_type = variable_type
        # 变量值
        self.variable_value = variable_value
        # 是否必填
        self.required = required
        # 帮助信息
        self.help = help
        # 步骤顺序
        self.step_order = step_order

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.variable_name is not None:
            result['VariableName'] = self.variable_name
        if self.variable_type is not None:
            result['VariableType'] = self.variable_type
        if self.variable_value is not None:
            result['VariableValue'] = self.variable_value
        if self.required is not None:
            result['Required'] = self.required
        if self.help is not None:
            result['Help'] = self.help
        if self.step_order is not None:
            result['StepOrder'] = self.step_order
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('VariableName') is not None:
            self.variable_name = m.get('VariableName')
        if m.get('VariableType') is not None:
            self.variable_type = m.get('VariableType')
        if m.get('VariableValue') is not None:
            self.variable_value = m.get('VariableValue')
        if m.get('Required') is not None:
            self.required = m.get('Required')
        if m.get('Help') is not None:
            self.help = m.get('Help')
        if m.get('StepOrder') is not None:
            self.step_order = m.get('StepOrder')
        return self


class CreateTemplateRequestOutputs(TeaModel):
    def __init__(
        self,
        task_name: str = None,
        variable_name: str = None,
        variable_type: str = None,
        variable_value: str = None,
        required: bool = None,
        help: str = None,
        step_order: int = None,
    ):
        # 任务名称
        self.task_name = task_name
        # 变量名
        self.variable_name = variable_name
        # 变量类型
        self.variable_type = variable_type
        # 变量值
        self.variable_value = variable_value
        # 是否必填
        self.required = required
        # 帮助信息
        self.help = help
        # 步骤顺序
        self.step_order = step_order

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.variable_name is not None:
            result['VariableName'] = self.variable_name
        if self.variable_type is not None:
            result['VariableType'] = self.variable_type
        if self.variable_value is not None:
            result['VariableValue'] = self.variable_value
        if self.required is not None:
            result['Required'] = self.required
        if self.help is not None:
            result['Help'] = self.help
        if self.step_order is not None:
            result['StepOrder'] = self.step_order
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('VariableName') is not None:
            self.variable_name = m.get('VariableName')
        if m.get('VariableType') is not None:
            self.variable_type = m.get('VariableType')
        if m.get('VariableValue') is not None:
            self.variable_value = m.get('VariableValue')
        if m.get('Required') is not None:
            self.required = m.get('Required')
        if m.get('Help') is not None:
            self.help = m.get('Help')
        if m.get('StepOrder') is not None:
            self.step_order = m.get('StepOrder')
        return self


class CreateTemplateRequest(TeaModel):
    def __init__(
        self,
        workspace: str = None,
        template_name: str = None,
        description: str = None,
        app_name: str = None,
        revision: str = None,
        root_entity: str = None,
        inputs: List[CreateTemplateRequestInputs] = None,
        outputs: List[CreateTemplateRequestOutputs] = None,
        labels: str = None,
        client_token: str = None,
    ):
        # 工作空间名称
        self.workspace = workspace
        # 应用模板名称
        self.template_name = template_name
        # 应用模板描述
        self.description = description
        # 应用的名称
        self.app_name = app_name
        # 应用的版本
        self.revision = revision
        # 根实体类型
        self.root_entity = root_entity
        # 应用的输入
        self.inputs = inputs
        # 应用的输出
        self.outputs = outputs
        # 应用标签
        self.labels = labels
        # 幂等Token
        self.client_token = client_token

    def validate(self):
        if self.inputs:
            for k in self.inputs:
                if k:
                    k.validate()
        if self.outputs:
            for k in self.outputs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.description is not None:
            result['Description'] = self.description
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.revision is not None:
            result['Revision'] = self.revision
        if self.root_entity is not None:
            result['RootEntity'] = self.root_entity
        result['Inputs'] = []
        if self.inputs is not None:
            for k in self.inputs:
                result['Inputs'].append(k.to_map() if k else None)
        result['Outputs'] = []
        if self.outputs is not None:
            for k in self.outputs:
                result['Outputs'].append(k.to_map() if k else None)
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Revision') is not None:
            self.revision = m.get('Revision')
        if m.get('RootEntity') is not None:
            self.root_entity = m.get('RootEntity')
        self.inputs = []
        if m.get('Inputs') is not None:
            for k in m.get('Inputs'):
                temp_model = CreateTemplateRequestInputs()
                self.inputs.append(temp_model.from_map(k))
        self.outputs = []
        if m.get('Outputs') is not None:
            for k in m.get('Outputs'):
                temp_model = CreateTemplateRequestOutputs()
                self.outputs.append(temp_model.from_map(k))
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class CreateTemplateShrinkRequest(TeaModel):
    def __init__(
        self,
        workspace: str = None,
        template_name: str = None,
        description: str = None,
        app_name: str = None,
        revision: str = None,
        root_entity: str = None,
        inputs_shrink: str = None,
        outputs_shrink: str = None,
        labels: str = None,
        client_token: str = None,
    ):
        # 工作空间名称
        self.workspace = workspace
        # 应用模板名称
        self.template_name = template_name
        # 应用模板描述
        self.description = description
        # 应用的名称
        self.app_name = app_name
        # 应用的版本
        self.revision = revision
        # 根实体类型
        self.root_entity = root_entity
        # 应用的输入
        self.inputs_shrink = inputs_shrink
        # 应用的输出
        self.outputs_shrink = outputs_shrink
        # 应用标签
        self.labels = labels
        # 幂等Token
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.description is not None:
            result['Description'] = self.description
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.revision is not None:
            result['Revision'] = self.revision
        if self.root_entity is not None:
            result['RootEntity'] = self.root_entity
        if self.inputs_shrink is not None:
            result['Inputs'] = self.inputs_shrink
        if self.outputs_shrink is not None:
            result['Outputs'] = self.outputs_shrink
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Revision') is not None:
            self.revision = m.get('Revision')
        if m.get('RootEntity') is not None:
            self.root_entity = m.get('RootEntity')
        if m.get('Inputs') is not None:
            self.inputs_shrink = m.get('Inputs')
        if m.get('Outputs') is not None:
            self.outputs_shrink = m.get('Outputs')
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class CreateTemplateResponseBody(TeaModel):
    def __init__(
        self,
        workspace: str = None,
        template_name: str = None,
        host_id: str = None,
        request_id: str = None,
    ):
        # 工作空间名称
        self.workspace = workspace
        # 应用模板名称
        self.template_name = template_name
        # 主机 ID
        self.host_id = host_id
        # 请求 ID
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateTemplateResponseBody = None,
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
            temp_model = CreateTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateWorkspaceRequest(TeaModel):
    def __init__(
        self,
        workspace: str = None,
        description: str = None,
        client_token: str = None,
        oss_root: str = None,
        job_lifecycle: int = None,
        role: str = None,
        labels: str = None,
    ):
        # 工作空间名称
        self.workspace = workspace
        # 工作空间描述
        self.description = description
        # 幂等Token
        self.client_token = client_token
        # 工作空间的OSS工作路径
        self.oss_root = oss_root
        # 工作空间任务生命周期
        self.job_lifecycle = job_lifecycle
        # 工作空间内的ram角色
        self.role = role
        # 工作空间标签
        self.labels = labels

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        if self.description is not None:
            result['Description'] = self.description
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.oss_root is not None:
            result['OssRoot'] = self.oss_root
        if self.job_lifecycle is not None:
            result['JobLifecycle'] = self.job_lifecycle
        if self.role is not None:
            result['Role'] = self.role
        if self.labels is not None:
            result['Labels'] = self.labels
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('OssRoot') is not None:
            self.oss_root = m.get('OssRoot')
        if m.get('JobLifecycle') is not None:
            self.job_lifecycle = m.get('JobLifecycle')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        return self


class CreateWorkspaceResponseBody(TeaModel):
    def __init__(
        self,
        host_id: str = None,
        request_id: str = None,
        workspace: str = None,
    ):
        # 主机ID
        self.host_id = host_id
        # 请求ID
        self.request_id = request_id
        # 创建成功的工作空间名称
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        return self


class CreateWorkspaceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateWorkspaceResponseBody = None,
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
            temp_model = CreateWorkspaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAppRequest(TeaModel):
    def __init__(
        self,
        workspace: str = None,
        app_name: str = None,
        revision: str = None,
    ):
        # 工作空间名称
        self.workspace = workspace
        # 应用名称
        self.app_name = app_name
        # 应用版本
        self.revision = revision

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.revision is not None:
            result['Revision'] = self.revision
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Revision') is not None:
            self.revision = m.get('Revision')
        return self


class DeleteAppResponseBody(TeaModel):
    def __init__(
        self,
        host_id: str = None,
        request_id: str = None,
    ):
        # 主机ID
        self.host_id = host_id
        # 请求ID
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteAppResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteAppResponseBody = None,
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
            temp_model = DeleteAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteEntityItemsRequest(TeaModel):
    def __init__(
        self,
        workspace: str = None,
        entity_type: str = None,
        entity_names: List[str] = None,
    ):
        self.workspace = workspace
        self.entity_type = entity_type
        self.entity_names = entity_names

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.entity_names is not None:
            result['EntityNames'] = self.entity_names
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('EntityNames') is not None:
            self.entity_names = m.get('EntityNames')
        return self


class DeleteEntityItemsShrinkRequest(TeaModel):
    def __init__(
        self,
        workspace: str = None,
        entity_type: str = None,
        entity_names_shrink: str = None,
    ):
        self.workspace = workspace
        self.entity_type = entity_type
        self.entity_names_shrink = entity_names_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.entity_names_shrink is not None:
            result['EntityNames'] = self.entity_names_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('EntityNames') is not None:
            self.entity_names_shrink = m.get('EntityNames')
        return self


class DeleteEntityItemsResponseBody(TeaModel):
    def __init__(
        self,
        host_id: str = None,
        request_id: str = None,
    ):
        self.host_id = host_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteEntityItemsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteEntityItemsResponseBody = None,
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
            temp_model = DeleteEntityItemsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteRunRequest(TeaModel):
    def __init__(
        self,
        workspace: str = None,
        run_id: str = None,
    ):
        # 工作空间名称
        self.workspace = workspace
        # 任务ID
        self.run_id = run_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        if self.run_id is not None:
            result['RunId'] = self.run_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        if m.get('RunId') is not None:
            self.run_id = m.get('RunId')
        return self


class DeleteRunResponseBody(TeaModel):
    def __init__(
        self,
        host_id: str = None,
        request_id: str = None,
    ):
        # 主机ID
        self.host_id = host_id
        # 请求ID
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
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


class DeleteSubmissionRequest(TeaModel):
    def __init__(
        self,
        workspace: str = None,
        submission_id: str = None,
    ):
        # 工作空间名称
        self.workspace = workspace
        # 投递ID
        self.submission_id = submission_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        if self.submission_id is not None:
            result['SubmissionId'] = self.submission_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        if m.get('SubmissionId') is not None:
            self.submission_id = m.get('SubmissionId')
        return self


class DeleteSubmissionResponseBody(TeaModel):
    def __init__(
        self,
        host_id: str = None,
        request_id: str = None,
    ):
        # 主机ID
        self.host_id = host_id
        # 请求ID
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteSubmissionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteSubmissionResponseBody = None,
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
            temp_model = DeleteSubmissionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteTemplateRequest(TeaModel):
    def __init__(
        self,
        workspace: str = None,
        template_name: str = None,
    ):
        # 工作空间名称
        self.workspace = workspace
        # 应用名称
        self.template_name = template_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        return self


class DeleteTemplateResponseBody(TeaModel):
    def __init__(
        self,
        host_id: str = None,
        request_id: str = None,
    ):
        # 主机ID
        self.host_id = host_id
        # 请求ID
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteTemplateResponseBody = None,
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
            temp_model = DeleteTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteWorkspaceRequest(TeaModel):
    def __init__(
        self,
        workspace: str = None,
    ):
        # 工作空间名称
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        return self


class DeleteWorkspaceResponseBody(TeaModel):
    def __init__(
        self,
        host_id: str = None,
        request_id: str = None,
    ):
        # 主机ID
        self.host_id = host_id
        # 请求ID
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteWorkspaceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteWorkspaceResponseBody = None,
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
            temp_model = DeleteWorkspaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DownloadEntityRequest(TeaModel):
    def __init__(
        self,
        workspace: str = None,
        entity_type: str = None,
        entity_names: List[str] = None,
    ):
        self.workspace = workspace
        self.entity_type = entity_type
        self.entity_names = entity_names

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.entity_names is not None:
            result['EntityNames'] = self.entity_names
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('EntityNames') is not None:
            self.entity_names = m.get('EntityNames')
        return self


class DownloadEntityShrinkRequest(TeaModel):
    def __init__(
        self,
        workspace: str = None,
        entity_type: str = None,
        entity_names_shrink: str = None,
    ):
        self.workspace = workspace
        self.entity_type = entity_type
        self.entity_names_shrink = entity_names_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.entity_names_shrink is not None:
            result['EntityNames'] = self.entity_names_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('EntityNames') is not None:
            self.entity_names_shrink = m.get('EntityNames')
        return self


class DownloadEntityResponseBody(TeaModel):
    def __init__(
        self,
        host_id: str = None,
        request_id: str = None,
        entity_tsvfile: str = None,
    ):
        # 主机ID
        self.host_id = host_id
        # 请求ID
        self.request_id = request_id
        self.entity_tsvfile = entity_tsvfile

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.entity_tsvfile is not None:
            result['EntityTSVFile'] = self.entity_tsvfile
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('EntityTSVFile') is not None:
            self.entity_tsvfile = m.get('EntityTSVFile')
        return self


class DownloadEntityResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DownloadEntityResponseBody = None,
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
            temp_model = DownloadEntityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAppRequest(TeaModel):
    def __init__(
        self,
        workspace: str = None,
        app_name: str = None,
        revision: str = None,
    ):
        # 工作空间名称
        self.workspace = workspace
        # 应用名称
        self.app_name = app_name
        # 应用版本号
        self.revision = revision

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.revision is not None:
            result['Revision'] = self.revision
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Revision') is not None:
            self.revision = m.get('Revision')
        return self


class GetAppResponseBodyInputs(TeaModel):
    def __init__(
        self,
        task_name: str = None,
        variable_name: str = None,
        variable_type: str = None,
        variable_value: str = None,
        required: bool = None,
        help: str = None,
        step_order: int = None,
    ):
        self.task_name = task_name
        self.variable_name = variable_name
        self.variable_type = variable_type
        self.variable_value = variable_value
        self.required = required
        self.help = help
        self.step_order = step_order

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.variable_name is not None:
            result['VariableName'] = self.variable_name
        if self.variable_type is not None:
            result['VariableType'] = self.variable_type
        if self.variable_value is not None:
            result['VariableValue'] = self.variable_value
        if self.required is not None:
            result['Required'] = self.required
        if self.help is not None:
            result['Help'] = self.help
        if self.step_order is not None:
            result['StepOrder'] = self.step_order
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('VariableName') is not None:
            self.variable_name = m.get('VariableName')
        if m.get('VariableType') is not None:
            self.variable_type = m.get('VariableType')
        if m.get('VariableValue') is not None:
            self.variable_value = m.get('VariableValue')
        if m.get('Required') is not None:
            self.required = m.get('Required')
        if m.get('Help') is not None:
            self.help = m.get('Help')
        if m.get('StepOrder') is not None:
            self.step_order = m.get('StepOrder')
        return self


class GetAppResponseBodyOutputs(TeaModel):
    def __init__(
        self,
        task_name: str = None,
        variable_name: str = None,
        variable_type: str = None,
        variable_value: str = None,
        required: bool = None,
        help: str = None,
        step_order: int = None,
    ):
        self.task_name = task_name
        self.variable_name = variable_name
        self.variable_type = variable_type
        self.variable_value = variable_value
        self.required = required
        self.help = help
        self.step_order = step_order

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.variable_name is not None:
            result['VariableName'] = self.variable_name
        if self.variable_type is not None:
            result['VariableType'] = self.variable_type
        if self.variable_value is not None:
            result['VariableValue'] = self.variable_value
        if self.required is not None:
            result['Required'] = self.required
        if self.help is not None:
            result['Help'] = self.help
        if self.step_order is not None:
            result['StepOrder'] = self.step_order
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('VariableName') is not None:
            self.variable_name = m.get('VariableName')
        if m.get('VariableType') is not None:
            self.variable_type = m.get('VariableType')
        if m.get('VariableValue') is not None:
            self.variable_value = m.get('VariableValue')
        if m.get('Required') is not None:
            self.required = m.get('Required')
        if m.get('Help') is not None:
            self.help = m.get('Help')
        if m.get('StepOrder') is not None:
            self.step_order = m.get('StepOrder')
        return self


class GetAppResponseBodyRevisions(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        revision: str = None,
        revision_comment: str = None,
    ):
        # 创建时间
        self.create_time = create_time
        # 版本号
        self.revision = revision
        # 版本描述
        self.revision_comment = revision_comment

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.revision is not None:
            result['Revision'] = self.revision
        if self.revision_comment is not None:
            result['RevisionComment'] = self.revision_comment
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Revision') is not None:
            self.revision = m.get('Revision')
        if m.get('RevisionComment') is not None:
            self.revision_comment = m.get('RevisionComment')
        return self


class GetAppResponseBodyDependencies(TeaModel):
    def __init__(
        self,
        path: str = None,
        content: str = None,
    ):
        # 依赖路径
        self.path = path
        # wdl内容
        self.content = content

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.path is not None:
            result['Path'] = self.path
        if self.content is not None:
            result['Content'] = self.content
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        return self


class GetAppResponseBodyConfigs(TeaModel):
    def __init__(
        self,
        path: str = None,
        content: str = None,
    ):
        self.path = path
        self.content = content

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.path is not None:
            result['Path'] = self.path
        if self.content is not None:
            result['Content'] = self.content
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        return self


class GetAppResponseBody(TeaModel):
    def __init__(
        self,
        workflow_name: str = None,
        app_name: str = None,
        create_time: str = None,
        definition: str = None,
        description: str = None,
        documentation: str = None,
        host_id: str = None,
        inputs: List[GetAppResponseBodyInputs] = None,
        labels: Dict[str, str] = None,
        language: str = None,
        language_version: str = None,
        last_modified_time: str = None,
        outputs: List[GetAppResponseBodyOutputs] = None,
        request_id: str = None,
        revision: str = None,
        revision_comment: str = None,
        revisions: List[GetAppResponseBodyRevisions] = None,
        scope: str = None,
        url: str = None,
        workspace: str = None,
        source: str = None,
        namespace: str = None,
        app_orig_name: str = None,
        app_type: str = None,
        dependencies: List[GetAppResponseBodyDependencies] = None,
        configs: List[GetAppResponseBodyConfigs] = None,
        path: str = None,
    ):
        # 工作流名称
        self.workflow_name = workflow_name
        # 应用名称
        self.app_name = app_name
        # 创建时间
        self.create_time = create_time
        # 应用定义
        self.definition = definition
        # 应用简要描述
        self.description = description
        # 应用详细文档
        self.documentation = documentation
        # 主机ID
        self.host_id = host_id
        # 应用输入
        self.inputs = inputs
        # 应用标签
        self.labels = labels
        # 应用描述语言
        self.language = language
        # 应用描述语言版本
        self.language_version = language_version
        # 应用最后修改时间
        self.last_modified_time = last_modified_time
        # 应用的输出参数
        self.outputs = outputs
        # 请求ID
        self.request_id = request_id
        # 应用版本号
        self.revision = revision
        # 应用当前版本修改
        self.revision_comment = revision_comment
        # 应用的所有版本号
        self.revisions = revisions
        # 应用可见范围
        self.scope = scope
        # 应用URL
        self.url = url
        # 工作空间名称
        self.workspace = workspace
        # 应用来源
        self.source = source
        # 命名空间
        self.namespace = namespace
        # 应用原名
        self.app_orig_name = app_orig_name
        # 实体类型
        self.app_type = app_type
        # 依赖应用
        self.dependencies = dependencies
        # 参考输入
        self.configs = configs
        # 主WDL路径
        self.path = path

    def validate(self):
        if self.inputs:
            for k in self.inputs:
                if k:
                    k.validate()
        if self.outputs:
            for k in self.outputs:
                if k:
                    k.validate()
        if self.revisions:
            for k in self.revisions:
                if k:
                    k.validate()
        if self.dependencies:
            for k in self.dependencies:
                if k:
                    k.validate()
        if self.configs:
            for k in self.configs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.workflow_name is not None:
            result['WorkflowName'] = self.workflow_name
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.definition is not None:
            result['Definition'] = self.definition
        if self.description is not None:
            result['Description'] = self.description
        if self.documentation is not None:
            result['Documentation'] = self.documentation
        if self.host_id is not None:
            result['HostId'] = self.host_id
        result['Inputs'] = []
        if self.inputs is not None:
            for k in self.inputs:
                result['Inputs'].append(k.to_map() if k else None)
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.language is not None:
            result['Language'] = self.language
        if self.language_version is not None:
            result['LanguageVersion'] = self.language_version
        if self.last_modified_time is not None:
            result['LastModifiedTime'] = self.last_modified_time
        result['Outputs'] = []
        if self.outputs is not None:
            for k in self.outputs:
                result['Outputs'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.revision is not None:
            result['Revision'] = self.revision
        if self.revision_comment is not None:
            result['RevisionComment'] = self.revision_comment
        result['Revisions'] = []
        if self.revisions is not None:
            for k in self.revisions:
                result['Revisions'].append(k.to_map() if k else None)
        if self.scope is not None:
            result['Scope'] = self.scope
        if self.url is not None:
            result['URL'] = self.url
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        if self.source is not None:
            result['Source'] = self.source
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.app_orig_name is not None:
            result['AppOrigName'] = self.app_orig_name
        if self.app_type is not None:
            result['AppType'] = self.app_type
        result['Dependencies'] = []
        if self.dependencies is not None:
            for k in self.dependencies:
                result['Dependencies'].append(k.to_map() if k else None)
        result['Configs'] = []
        if self.configs is not None:
            for k in self.configs:
                result['Configs'].append(k.to_map() if k else None)
        if self.path is not None:
            result['Path'] = self.path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('WorkflowName') is not None:
            self.workflow_name = m.get('WorkflowName')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Definition') is not None:
            self.definition = m.get('Definition')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Documentation') is not None:
            self.documentation = m.get('Documentation')
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        self.inputs = []
        if m.get('Inputs') is not None:
            for k in m.get('Inputs'):
                temp_model = GetAppResponseBodyInputs()
                self.inputs.append(temp_model.from_map(k))
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('LanguageVersion') is not None:
            self.language_version = m.get('LanguageVersion')
        if m.get('LastModifiedTime') is not None:
            self.last_modified_time = m.get('LastModifiedTime')
        self.outputs = []
        if m.get('Outputs') is not None:
            for k in m.get('Outputs'):
                temp_model = GetAppResponseBodyOutputs()
                self.outputs.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Revision') is not None:
            self.revision = m.get('Revision')
        if m.get('RevisionComment') is not None:
            self.revision_comment = m.get('RevisionComment')
        self.revisions = []
        if m.get('Revisions') is not None:
            for k in m.get('Revisions'):
                temp_model = GetAppResponseBodyRevisions()
                self.revisions.append(temp_model.from_map(k))
        if m.get('Scope') is not None:
            self.scope = m.get('Scope')
        if m.get('URL') is not None:
            self.url = m.get('URL')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('AppOrigName') is not None:
            self.app_orig_name = m.get('AppOrigName')
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')
        self.dependencies = []
        if m.get('Dependencies') is not None:
            for k in m.get('Dependencies'):
                temp_model = GetAppResponseBodyDependencies()
                self.dependencies.append(temp_model.from_map(k))
        self.configs = []
        if m.get('Configs') is not None:
            for k in m.get('Configs'):
                temp_model = GetAppResponseBodyConfigs()
                self.configs.append(temp_model.from_map(k))
        if m.get('Path') is not None:
            self.path = m.get('Path')
        return self


class GetAppResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetAppResponseBody = None,
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
            temp_model = GetAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetEntityRequest(TeaModel):
    def __init__(
        self,
        workspace: str = None,
        entity_type: str = None,
    ):
        self.workspace = workspace
        self.entity_type = entity_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        return self


class GetEntityResponseBody(TeaModel):
    def __init__(
        self,
        host_id: str = None,
        request_id: str = None,
        workspace: str = None,
        entity_type: str = None,
        attributes: List[str] = None,
        total_count: int = None,
    ):
        # 主机ID
        self.host_id = host_id
        # 请求ID
        self.request_id = request_id
        self.workspace = workspace
        self.entity_type = entity_type
        self.attributes = attributes
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.attributes is not None:
            result['Attributes'] = self.attributes
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('Attributes') is not None:
            self.attributes = m.get('Attributes')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class GetEntityResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetEntityResponseBody = None,
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
            temp_model = GetEntityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetGlobalAppRequest(TeaModel):
    def __init__(
        self,
        attributes: str = None,
        namespace_name: str = None,
        app_name: str = None,
        app_version: str = None,
        region: str = None,
    ):
        # 查询字段信息
        self.attributes = attributes
        # 命名空间
        self.namespace_name = namespace_name
        # 应用名称
        self.app_name = app_name
        # 应用版本
        self.app_version = app_version
        # 应用可用区域
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attributes is not None:
            result['Attributes'] = self.attributes
        if self.namespace_name is not None:
            result['NamespaceName'] = self.namespace_name
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_version is not None:
            result['AppVersion'] = self.app_version
        if self.region is not None:
            result['Region'] = self.region
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Attributes') is not None:
            self.attributes = m.get('Attributes')
        if m.get('NamespaceName') is not None:
            self.namespace_name = m.get('NamespaceName')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        return self


class GetGlobalAppResponseBodyAppVersions(TeaModel):
    def __init__(
        self,
        app_version: str = None,
        comment: str = None,
        last_modified: str = None,
    ):
        # 应用版本
        self.app_version = app_version
        # 版本描述
        self.comment = comment
        # 更新时间
        self.last_modified = last_modified

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_version is not None:
            result['AppVersion'] = self.app_version
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.last_modified is not None:
            result['LastModified'] = self.last_modified
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('LastModified') is not None:
            self.last_modified = m.get('LastModified')
        return self


class GetGlobalAppResponseBodyAppDescriptorFiles(TeaModel):
    def __init__(
        self,
        file_type: str = None,
        path: str = None,
        content: str = None,
        url: str = None,
        checksum: str = None,
    ):
        # 应用文件的类型
        self.file_type = file_type
        # 应用文件的路径，除PRIMARY_DESCRIPTOR外，其他均为相对于PRIMARY_DESCRIPTOR的相对路径
        self.path = path
        # 应用文件内容
        self.content = content
        # 应用文件链接
        self.url = url
        # 应用文件内容的完整性校验码，如MD5值
        self.checksum = checksum

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_type is not None:
            result['FileType'] = self.file_type
        if self.path is not None:
            result['Path'] = self.path
        if self.content is not None:
            result['Content'] = self.content
        if self.url is not None:
            result['Url'] = self.url
        if self.checksum is not None:
            result['Checksum'] = self.checksum
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('Checksum') is not None:
            self.checksum = m.get('Checksum')
        return self


class GetGlobalAppResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        message: str = None,
        dynamic_code: str = None,
        last_modified: str = None,
        namespace_name: str = None,
        app_scope: str = None,
        app_name: str = None,
        region_ids: List[str] = None,
        app_version: str = None,
        app_type: str = None,
        app_fee: str = None,
        app_description: str = None,
        categories: List[str] = None,
        toolkit: str = None,
        contact: str = None,
        links: List[str] = None,
        app_versions: List[GetGlobalAppResponseBodyAppVersions] = None,
        app_default_version: str = None,
        app_descriptor_type: str = None,
        app_descriptor_files: List[GetGlobalAppResponseBodyAppDescriptorFiles] = None,
        document: str = None,
        comment: str = None,
        dag: str = None,
        dynamic_message: str = None,
        code: str = None,
        host_id: str = None,
        pinned: bool = None,
    ):
        self.request_id = request_id
        self.message = message
        self.dynamic_code = dynamic_code
        # 更新时间
        self.last_modified = last_modified
        # 命名空间名称
        self.namespace_name = namespace_name
        # 应用权限
        self.app_scope = app_scope
        # 应用名称
        self.app_name = app_name
        # 应用支持的区域
        self.region_ids = region_ids
        # 应用版本
        self.app_version = app_version
        # 应用类型
        self.app_type = app_type
        # 应用计费说明
        self.app_fee = app_fee
        # 应用描述
        self.app_description = app_description
        # 应用所属分类
        self.categories = categories
        # 应用所属工具合集
        self.toolkit = toolkit
        # 应用联系人信息
        self.contact = contact
        # 应用主页信息
        self.links = links
        # 应用的所有版本列表
        self.app_versions = app_versions
        # 默认版本
        self.app_default_version = app_default_version
        # 应用描述语言标准(WDL/CWL)
        self.app_descriptor_type = app_descriptor_type
        # 应用的描述文件内容
        self.app_descriptor_files = app_descriptor_files
        # 应用的帮助文档
        self.document = document
        # 应用的备注信息
        self.comment = comment
        # 应用的DAG信息
        self.dag = dag
        self.dynamic_message = dynamic_message
        self.code = code
        self.host_id = host_id
        # 应用收藏置顶标记
        self.pinned = pinned

    def validate(self):
        if self.app_versions:
            for k in self.app_versions:
                if k:
                    k.validate()
        if self.app_descriptor_files:
            for k in self.app_descriptor_files:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.last_modified is not None:
            result['LastModified'] = self.last_modified
        if self.namespace_name is not None:
            result['NamespaceName'] = self.namespace_name
        if self.app_scope is not None:
            result['AppScope'] = self.app_scope
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.region_ids is not None:
            result['RegionIds'] = self.region_ids
        if self.app_version is not None:
            result['AppVersion'] = self.app_version
        if self.app_type is not None:
            result['AppType'] = self.app_type
        if self.app_fee is not None:
            result['AppFee'] = self.app_fee
        if self.app_description is not None:
            result['AppDescription'] = self.app_description
        if self.categories is not None:
            result['Categories'] = self.categories
        if self.toolkit is not None:
            result['Toolkit'] = self.toolkit
        if self.contact is not None:
            result['Contact'] = self.contact
        if self.links is not None:
            result['Links'] = self.links
        result['AppVersions'] = []
        if self.app_versions is not None:
            for k in self.app_versions:
                result['AppVersions'].append(k.to_map() if k else None)
        if self.app_default_version is not None:
            result['AppDefaultVersion'] = self.app_default_version
        if self.app_descriptor_type is not None:
            result['AppDescriptorType'] = self.app_descriptor_type
        result['AppDescriptorFiles'] = []
        if self.app_descriptor_files is not None:
            for k in self.app_descriptor_files:
                result['AppDescriptorFiles'].append(k.to_map() if k else None)
        if self.document is not None:
            result['Document'] = self.document
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.dag is not None:
            result['DAG'] = self.dag
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.code is not None:
            result['Code'] = self.code
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.pinned is not None:
            result['Pinned'] = self.pinned
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('LastModified') is not None:
            self.last_modified = m.get('LastModified')
        if m.get('NamespaceName') is not None:
            self.namespace_name = m.get('NamespaceName')
        if m.get('AppScope') is not None:
            self.app_scope = m.get('AppScope')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('RegionIds') is not None:
            self.region_ids = m.get('RegionIds')
        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')
        if m.get('AppFee') is not None:
            self.app_fee = m.get('AppFee')
        if m.get('AppDescription') is not None:
            self.app_description = m.get('AppDescription')
        if m.get('Categories') is not None:
            self.categories = m.get('Categories')
        if m.get('Toolkit') is not None:
            self.toolkit = m.get('Toolkit')
        if m.get('Contact') is not None:
            self.contact = m.get('Contact')
        if m.get('Links') is not None:
            self.links = m.get('Links')
        self.app_versions = []
        if m.get('AppVersions') is not None:
            for k in m.get('AppVersions'):
                temp_model = GetGlobalAppResponseBodyAppVersions()
                self.app_versions.append(temp_model.from_map(k))
        if m.get('AppDefaultVersion') is not None:
            self.app_default_version = m.get('AppDefaultVersion')
        if m.get('AppDescriptorType') is not None:
            self.app_descriptor_type = m.get('AppDescriptorType')
        self.app_descriptor_files = []
        if m.get('AppDescriptorFiles') is not None:
            for k in m.get('AppDescriptorFiles'):
                temp_model = GetGlobalAppResponseBodyAppDescriptorFiles()
                self.app_descriptor_files.append(temp_model.from_map(k))
        if m.get('Document') is not None:
            self.document = m.get('Document')
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('DAG') is not None:
            self.dag = m.get('DAG')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('Pinned') is not None:
            self.pinned = m.get('Pinned')
        return self


class GetGlobalAppResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetGlobalAppResponseBody = None,
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
            temp_model = GetGlobalAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPublicDatasetRequest(TeaModel):
    def __init__(
        self,
        dataset_name: str = None,
        attributes: List[str] = None,
    ):
        # 数据集名称
        self.dataset_name = dataset_name
        # 查询的字段名
        self.attributes = attributes

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.attributes is not None:
            result['Attributes'] = self.attributes
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('Attributes') is not None:
            self.attributes = m.get('Attributes')
        return self


class GetPublicDatasetShrinkRequest(TeaModel):
    def __init__(
        self,
        dataset_name: str = None,
        attributes_shrink: str = None,
    ):
        # 数据集名称
        self.dataset_name = dataset_name
        # 查询的字段名
        self.attributes_shrink = attributes_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.attributes_shrink is not None:
            result['Attributes'] = self.attributes_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('Attributes') is not None:
            self.attributes_shrink = m.get('Attributes')
        return self


class GetPublicDatasetResponseBody(TeaModel):
    def __init__(
        self,
        host_id: str = None,
        request_id: str = None,
        http_code: int = None,
        code: str = None,
        message: str = None,
        success: bool = None,
        dataset_description: str = None,
        copyright: str = None,
        access_requirements: str = None,
        about: str = None,
        tags: List[str] = None,
        dataset_name: str = None,
        update_frequency: str = None,
        region_ids: List[str] = None,
        last_modified: str = None,
    ):
        # 主机ID
        self.host_id = host_id
        # 请求ID
        self.request_id = request_id
        self.http_code = http_code
        # 错误码
        self.code = code
        # 错误消息
        self.message = message
        # 是否调用成功
        self.success = success
        # 公共数据集描述
        self.dataset_description = dataset_description
        # 公共数据集版权信息
        self.copyright = copyright
        # 公共数据集访问要求
        self.access_requirements = access_requirements
        # 关于公共数据集
        self.about = about
        # 公共数据集标签
        self.tags = tags
        # 公共数据集名称
        self.dataset_name = dataset_name
        # 公共数据集更新频率
        self.update_frequency = update_frequency
        # 公共数据集可用区域
        self.region_ids = region_ids
        # 最后更新时间
        self.last_modified = last_modified

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.success is not None:
            result['Success'] = self.success
        if self.dataset_description is not None:
            result['DatasetDescription'] = self.dataset_description
        if self.copyright is not None:
            result['Copyright'] = self.copyright
        if self.access_requirements is not None:
            result['AccessRequirements'] = self.access_requirements
        if self.about is not None:
            result['About'] = self.about
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.update_frequency is not None:
            result['UpdateFrequency'] = self.update_frequency
        if self.region_ids is not None:
            result['RegionIds'] = self.region_ids
        if self.last_modified is not None:
            result['LastModified'] = self.last_modified
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('DatasetDescription') is not None:
            self.dataset_description = m.get('DatasetDescription')
        if m.get('Copyright') is not None:
            self.copyright = m.get('Copyright')
        if m.get('AccessRequirements') is not None:
            self.access_requirements = m.get('AccessRequirements')
        if m.get('About') is not None:
            self.about = m.get('About')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('UpdateFrequency') is not None:
            self.update_frequency = m.get('UpdateFrequency')
        if m.get('RegionIds') is not None:
            self.region_ids = m.get('RegionIds')
        if m.get('LastModified') is not None:
            self.last_modified = m.get('LastModified')
        return self


class GetPublicDatasetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetPublicDatasetResponseBody = None,
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
            temp_model = GetPublicDatasetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPublicDatasetEntityRequest(TeaModel):
    def __init__(
        self,
        dataset_name: str = None,
        entity_type: str = None,
    ):
        # 数据集名称
        self.dataset_name = dataset_name
        # 实体类型
        self.entity_type = entity_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        return self


class GetPublicDatasetEntityResponseBody(TeaModel):
    def __init__(
        self,
        host_id: str = None,
        request_id: str = None,
        http_code: int = None,
        code: str = None,
        message: str = None,
        dataset_name: str = None,
        entity_type: str = None,
        attributes: List[str] = None,
        total_count: int = None,
    ):
        # 主机ID
        self.host_id = host_id
        # 请求ID
        self.request_id = request_id
        self.http_code = http_code
        # 错误码
        self.code = code
        # 错误消息
        self.message = message
        # 公共数据集名称
        self.dataset_name = dataset_name
        # 实体类型
        self.entity_type = entity_type
        # 实体属性名称列表
        self.attributes = attributes
        # 该类型实体总数
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.attributes is not None:
            result['Attributes'] = self.attributes
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('Attributes') is not None:
            self.attributes = m.get('Attributes')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class GetPublicDatasetEntityResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetPublicDatasetEntityResponseBody = None,
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
            temp_model = GetPublicDatasetEntityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRunRequest(TeaModel):
    def __init__(
        self,
        workspace: str = None,
        run_id: str = None,
        attributes: str = None,
    ):
        # 工作空间名字
        self.workspace = workspace
        # 任务ID
        self.run_id = run_id
        self.attributes = attributes

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        if self.run_id is not None:
            result['RunId'] = self.run_id
        if self.attributes is not None:
            result['Attributes'] = self.attributes
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        if m.get('RunId') is not None:
            self.run_id = m.get('RunId')
        if m.get('Attributes') is not None:
            self.attributes = m.get('Attributes')
        return self


class GetRunResponseBodyExecuteOptions(TeaModel):
    def __init__(
        self,
        call_caching: bool = None,
        delete_intermediate_results: bool = None,
        failure_mode: str = None,
    ):
        self.call_caching = call_caching
        self.delete_intermediate_results = delete_intermediate_results
        self.failure_mode = failure_mode

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.call_caching is not None:
            result['CallCaching'] = self.call_caching
        if self.delete_intermediate_results is not None:
            result['DeleteIntermediateResults'] = self.delete_intermediate_results
        if self.failure_mode is not None:
            result['FailureMode'] = self.failure_mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallCaching') is not None:
            self.call_caching = m.get('CallCaching')
        if m.get('DeleteIntermediateResults') is not None:
            self.delete_intermediate_results = m.get('DeleteIntermediateResults')
        if m.get('FailureMode') is not None:
            self.failure_mode = m.get('FailureMode')
        return self


class GetRunResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        host_id: str = None,
        workspace: str = None,
        run_id: str = None,
        name: str = None,
        submission_id: str = None,
        source: str = None,
        namespace: str = None,
        app_orig_name: str = None,
        app_name: str = None,
        revision: str = None,
        entity_type: str = None,
        entity_name: str = None,
        user: str = None,
        status: str = None,
        create_time: str = None,
        start_time: str = None,
        end_time: str = None,
        execute_options: GetRunResponseBodyExecuteOptions = None,
        inputs: str = None,
        outputs: str = None,
        labels: Dict[str, str] = None,
        output_folder: str = None,
        execute_directory: str = None,
        default_runtime: str = None,
        description: str = None,
        timing: str = None,
        calls: str = None,
        failures: str = None,
    ):
        # 请求ID
        self.request_id = request_id
        # 主机ID
        self.host_id = host_id
        # 工作空间名字
        self.workspace = workspace
        # 任务ID
        self.run_id = run_id
        # 任务名称
        self.name = name
        # 提交ID
        self.submission_id = submission_id
        # 应用来源
        self.source = source
        # 命名空间
        self.namespace = namespace
        # 应用原名
        self.app_orig_name = app_orig_name
        # 应用名称
        self.app_name = app_name
        # 应用版本
        self.revision = revision
        # 实体类型
        self.entity_type = entity_type
        # 实体对象名称
        self.entity_name = entity_name
        # 用户ID
        self.user = user
        # 任务状态
        self.status = status
        # 提交时间
        self.create_time = create_time
        # 开始时间
        self.start_time = start_time
        # 结束时间
        self.end_time = end_time
        # 任务配置
        self.execute_options = execute_options
        self.inputs = inputs
        self.outputs = outputs
        # 任务标签
        self.labels = labels
        # 输出拷贝目录
        self.output_folder = output_folder
        # 任务执行目录
        self.execute_directory = execute_directory
        # 默认runtime值
        self.default_runtime = default_runtime
        # 任务描述
        self.description = description
        # 时序信息
        self.timing = timing
        self.calls = calls
        self.failures = failures

    def validate(self):
        if self.execute_options:
            self.execute_options.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        if self.run_id is not None:
            result['RunId'] = self.run_id
        if self.name is not None:
            result['Name'] = self.name
        if self.submission_id is not None:
            result['SubmissionId'] = self.submission_id
        if self.source is not None:
            result['Source'] = self.source
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.app_orig_name is not None:
            result['AppOrigName'] = self.app_orig_name
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.revision is not None:
            result['Revision'] = self.revision
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.entity_name is not None:
            result['EntityName'] = self.entity_name
        if self.user is not None:
            result['User'] = self.user
        if self.status is not None:
            result['Status'] = self.status
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.execute_options is not None:
            result['ExecuteOptions'] = self.execute_options.to_map()
        if self.inputs is not None:
            result['Inputs'] = self.inputs
        if self.outputs is not None:
            result['Outputs'] = self.outputs
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.output_folder is not None:
            result['OutputFolder'] = self.output_folder
        if self.execute_directory is not None:
            result['ExecuteDirectory'] = self.execute_directory
        if self.default_runtime is not None:
            result['DefaultRuntime'] = self.default_runtime
        if self.description is not None:
            result['Description'] = self.description
        if self.timing is not None:
            result['Timing'] = self.timing
        if self.calls is not None:
            result['Calls'] = self.calls
        if self.failures is not None:
            result['Failures'] = self.failures
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        if m.get('RunId') is not None:
            self.run_id = m.get('RunId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('SubmissionId') is not None:
            self.submission_id = m.get('SubmissionId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('AppOrigName') is not None:
            self.app_orig_name = m.get('AppOrigName')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Revision') is not None:
            self.revision = m.get('Revision')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('EntityName') is not None:
            self.entity_name = m.get('EntityName')
        if m.get('User') is not None:
            self.user = m.get('User')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('ExecuteOptions') is not None:
            temp_model = GetRunResponseBodyExecuteOptions()
            self.execute_options = temp_model.from_map(m['ExecuteOptions'])
        if m.get('Inputs') is not None:
            self.inputs = m.get('Inputs')
        if m.get('Outputs') is not None:
            self.outputs = m.get('Outputs')
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('OutputFolder') is not None:
            self.output_folder = m.get('OutputFolder')
        if m.get('ExecuteDirectory') is not None:
            self.execute_directory = m.get('ExecuteDirectory')
        if m.get('DefaultRuntime') is not None:
            self.default_runtime = m.get('DefaultRuntime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Timing') is not None:
            self.timing = m.get('Timing')
        if m.get('Calls') is not None:
            self.calls = m.get('Calls')
        if m.get('Failures') is not None:
            self.failures = m.get('Failures')
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


class GetSubmissionRequest(TeaModel):
    def __init__(
        self,
        workspace: str = None,
        submission_id: str = None,
    ):
        # 工作空间
        self.workspace = workspace
        # 投递ID
        self.submission_id = submission_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        if self.submission_id is not None:
            result['SubmissionId'] = self.submission_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        if m.get('SubmissionId') is not None:
            self.submission_id = m.get('SubmissionId')
        return self


class GetSubmissionResponseBodySubmissionRunStats(TeaModel):
    def __init__(
        self,
        submitted: int = None,
        pending: int = None,
        running: int = None,
        succeeded: int = None,
        failed: int = None,
        aborting: int = None,
        aborted: int = None,
    ):
        self.submitted = submitted
        self.pending = pending
        self.running = running
        self.succeeded = succeeded
        self.failed = failed
        self.aborting = aborting
        self.aborted = aborted

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.submitted is not None:
            result['Submitted'] = self.submitted
        if self.pending is not None:
            result['Pending'] = self.pending
        if self.running is not None:
            result['Running'] = self.running
        if self.succeeded is not None:
            result['Succeeded'] = self.succeeded
        if self.failed is not None:
            result['Failed'] = self.failed
        if self.aborting is not None:
            result['Aborting'] = self.aborting
        if self.aborted is not None:
            result['Aborted'] = self.aborted
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Submitted') is not None:
            self.submitted = m.get('Submitted')
        if m.get('Pending') is not None:
            self.pending = m.get('Pending')
        if m.get('Running') is not None:
            self.running = m.get('Running')
        if m.get('Succeeded') is not None:
            self.succeeded = m.get('Succeeded')
        if m.get('Failed') is not None:
            self.failed = m.get('Failed')
        if m.get('Aborting') is not None:
            self.aborting = m.get('Aborting')
        if m.get('Aborted') is not None:
            self.aborted = m.get('Aborted')
        return self


class GetSubmissionResponseBodySubmission(TeaModel):
    def __init__(
        self,
        workspace: str = None,
        submission_id: str = None,
        status: str = None,
        create_time: str = None,
        start_time: str = None,
        end_time: str = None,
        entity_type: str = None,
        run_stats: GetSubmissionResponseBodySubmissionRunStats = None,
    ):
        # 提交ID
        self.workspace = workspace
        # 提交ID
        self.submission_id = submission_id
        # 任务状态
        self.status = status
        # 提交时间
        self.create_time = create_time
        # 开始时间
        self.start_time = start_time
        # 结束时间
        self.end_time = end_time
        # 实体类型
        self.entity_type = entity_type
        self.run_stats = run_stats

    def validate(self):
        if self.run_stats:
            self.run_stats.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        if self.submission_id is not None:
            result['SubmissionId'] = self.submission_id
        if self.status is not None:
            result['Status'] = self.status
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.run_stats is not None:
            result['RunStats'] = self.run_stats.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        if m.get('SubmissionId') is not None:
            self.submission_id = m.get('SubmissionId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('RunStats') is not None:
            temp_model = GetSubmissionResponseBodySubmissionRunStats()
            self.run_stats = temp_model.from_map(m['RunStats'])
        return self


class GetSubmissionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        host_id: str = None,
        submission: GetSubmissionResponseBodySubmission = None,
    ):
        # 请求ID
        self.request_id = request_id
        # 主机ID
        self.host_id = host_id
        # 投递列表
        self.submission = submission

    def validate(self):
        if self.submission:
            self.submission.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.submission is not None:
            result['Submission'] = self.submission.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('Submission') is not None:
            temp_model = GetSubmissionResponseBodySubmission()
            self.submission = temp_model.from_map(m['Submission'])
        return self


class GetSubmissionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetSubmissionResponseBody = None,
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
            temp_model = GetSubmissionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTemplateRequest(TeaModel):
    def __init__(
        self,
        workspace: str = None,
        template_name: str = None,
    ):
        # 工作空间名称
        self.workspace = workspace
        # 应用模板名称
        self.template_name = template_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        return self


class GetTemplateResponseBodyInputs(TeaModel):
    def __init__(
        self,
        task_name: str = None,
        variable_name: str = None,
        variable_type: str = None,
        variable_value: str = None,
        required: bool = None,
        help: str = None,
        step_order: int = None,
    ):
        # 任务名称
        self.task_name = task_name
        # 变量名称
        self.variable_name = variable_name
        # 变量类型
        self.variable_type = variable_type
        # 变量值
        self.variable_value = variable_value
        # 是否必须参数
        self.required = required
        # 帮助信息
        self.help = help
        # 步骤顺序
        self.step_order = step_order

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.variable_name is not None:
            result['VariableName'] = self.variable_name
        if self.variable_type is not None:
            result['VariableType'] = self.variable_type
        if self.variable_value is not None:
            result['VariableValue'] = self.variable_value
        if self.required is not None:
            result['Required'] = self.required
        if self.help is not None:
            result['Help'] = self.help
        if self.step_order is not None:
            result['StepOrder'] = self.step_order
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('VariableName') is not None:
            self.variable_name = m.get('VariableName')
        if m.get('VariableType') is not None:
            self.variable_type = m.get('VariableType')
        if m.get('VariableValue') is not None:
            self.variable_value = m.get('VariableValue')
        if m.get('Required') is not None:
            self.required = m.get('Required')
        if m.get('Help') is not None:
            self.help = m.get('Help')
        if m.get('StepOrder') is not None:
            self.step_order = m.get('StepOrder')
        return self


class GetTemplateResponseBodyOutputs(TeaModel):
    def __init__(
        self,
        task_name: str = None,
        variable_name: str = None,
        variable_type: str = None,
        variable_value: str = None,
        required: bool = None,
        help: str = None,
        step_order: int = None,
    ):
        # 任务名称
        self.task_name = task_name
        # 变量名称
        self.variable_name = variable_name
        # 变量类型
        self.variable_type = variable_type
        # 变量值
        self.variable_value = variable_value
        # 是否必须参数
        self.required = required
        # 帮助信息
        self.help = help
        # 步骤顺序
        self.step_order = step_order

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.variable_name is not None:
            result['VariableName'] = self.variable_name
        if self.variable_type is not None:
            result['VariableType'] = self.variable_type
        if self.variable_value is not None:
            result['VariableValue'] = self.variable_value
        if self.required is not None:
            result['Required'] = self.required
        if self.help is not None:
            result['Help'] = self.help
        if self.step_order is not None:
            result['StepOrder'] = self.step_order
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('VariableName') is not None:
            self.variable_name = m.get('VariableName')
        if m.get('VariableType') is not None:
            self.variable_type = m.get('VariableType')
        if m.get('VariableValue') is not None:
            self.variable_value = m.get('VariableValue')
        if m.get('Required') is not None:
            self.required = m.get('Required')
        if m.get('Help') is not None:
            self.help = m.get('Help')
        if m.get('StepOrder') is not None:
            self.step_order = m.get('StepOrder')
        return self


class GetTemplateResponseBody(TeaModel):
    def __init__(
        self,
        template_name: str = None,
        create_time: str = None,
        description: str = None,
        app_name: str = None,
        revision: str = None,
        host_id: str = None,
        inputs: List[GetTemplateResponseBodyInputs] = None,
        labels: Dict[str, str] = None,
        last_modified_time: str = None,
        outputs: List[GetTemplateResponseBodyOutputs] = None,
        request_id: str = None,
        source: str = None,
        workspace: str = None,
        root_entity: str = None,
    ):
        # 应用模板名称
        self.template_name = template_name
        # 创建时间
        self.create_time = create_time
        # 应用简要描述
        self.description = description
        # 应用的名称
        self.app_name = app_name
        # 应用的版本
        self.revision = revision
        # 主机ID
        self.host_id = host_id
        # 应用输入
        self.inputs = inputs
        # 应用标签
        self.labels = labels
        # 应用最后修改时间
        self.last_modified_time = last_modified_time
        # 应用的输出参数
        self.outputs = outputs
        # 请求ID
        self.request_id = request_id
        # 应用来源
        self.source = source
        # 工作空间名称
        self.workspace = workspace
        # 实体类型
        self.root_entity = root_entity

    def validate(self):
        if self.inputs:
            for k in self.inputs:
                if k:
                    k.validate()
        if self.outputs:
            for k in self.outputs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.revision is not None:
            result['Revision'] = self.revision
        if self.host_id is not None:
            result['HostId'] = self.host_id
        result['Inputs'] = []
        if self.inputs is not None:
            for k in self.inputs:
                result['Inputs'].append(k.to_map() if k else None)
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.last_modified_time is not None:
            result['LastModifiedTime'] = self.last_modified_time
        result['Outputs'] = []
        if self.outputs is not None:
            for k in self.outputs:
                result['Outputs'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.source is not None:
            result['Source'] = self.source
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        if self.root_entity is not None:
            result['RootEntity'] = self.root_entity
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Revision') is not None:
            self.revision = m.get('Revision')
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        self.inputs = []
        if m.get('Inputs') is not None:
            for k in m.get('Inputs'):
                temp_model = GetTemplateResponseBodyInputs()
                self.inputs.append(temp_model.from_map(k))
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('LastModifiedTime') is not None:
            self.last_modified_time = m.get('LastModifiedTime')
        self.outputs = []
        if m.get('Outputs') is not None:
            for k in m.get('Outputs'):
                temp_model = GetTemplateResponseBodyOutputs()
                self.outputs.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        if m.get('RootEntity') is not None:
            self.root_entity = m.get('RootEntity')
        return self


class GetTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetTemplateResponseBody = None,
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
            temp_model = GetTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetWorkspaceRequest(TeaModel):
    def __init__(
        self,
        workspace: str = None,
    ):
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        return self


class GetWorkspaceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        description: str = None,
        host_id: str = None,
        job_lifecycle: int = None,
        labels: Dict[str, str] = None,
        oss_root: str = None,
        bucket_name: str = None,
        role: str = None,
        create_time: str = None,
        last_modified_time: str = None,
        workspace: str = None,
        status: str = None,
        region_id: str = None,
    ):
        # 请求ID
        self.request_id = request_id
        # 工作空间简要描述
        self.description = description
        # 主机ID
        self.host_id = host_id
        # 工作空间内作业生命周期
        self.job_lifecycle = job_lifecycle
        # 工作空间标签
        self.labels = labels
        # 工作空间内OSS上的工作路径
        self.oss_root = oss_root
        # 工作空间Bucket
        self.bucket_name = bucket_name
        # 工作空间内默认的RAM服务角色
        self.role = role
        # 创建时间
        self.create_time = create_time
        # 最后修改时间
        self.last_modified_time = last_modified_time
        # 工作空间名称
        self.workspace = workspace
        # 工作空间状态
        self.status = status
        # 地域ID
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.description is not None:
            result['Description'] = self.description
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.job_lifecycle is not None:
            result['JobLifecycle'] = self.job_lifecycle
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.oss_root is not None:
            result['OssRoot'] = self.oss_root
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.role is not None:
            result['Role'] = self.role
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.last_modified_time is not None:
            result['LastModifiedTime'] = self.last_modified_time
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        if self.status is not None:
            result['Status'] = self.status
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('JobLifecycle') is not None:
            self.job_lifecycle = m.get('JobLifecycle')
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('OssRoot') is not None:
            self.oss_root = m.get('OssRoot')
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('LastModifiedTime') is not None:
            self.last_modified_time = m.get('LastModifiedTime')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetWorkspaceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetWorkspaceResponseBody = None,
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
            temp_model = GetWorkspaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InstallGlobalAppRequest(TeaModel):
    def __init__(
        self,
        source: str = None,
        namespace_name: str = None,
        app_name: str = None,
        workspace: str = None,
        installed_app_name: str = None,
    ):
        # 来源
        self.source = source
        # 命名空间名称
        self.namespace_name = namespace_name
        # 应用描述
        self.app_name = app_name
        # 工作空间
        self.workspace = workspace
        # 安装后应用名
        self.installed_app_name = installed_app_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source is not None:
            result['Source'] = self.source
        if self.namespace_name is not None:
            result['NamespaceName'] = self.namespace_name
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        if self.installed_app_name is not None:
            result['InstalledAppName'] = self.installed_app_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('NamespaceName') is not None:
            self.namespace_name = m.get('NamespaceName')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        if m.get('InstalledAppName') is not None:
            self.installed_app_name = m.get('InstalledAppName')
        return self


class InstallGlobalAppResponseBody(TeaModel):
    def __init__(
        self,
        host_id: str = None,
        request_id: str = None,
        installed_app_name: str = None,
        workspace: str = None,
        region_id: str = None,
    ):
        # 主机 ID
        self.host_id = host_id
        # 请求 ID
        self.request_id = request_id
        # 安装后应用名
        self.installed_app_name = installed_app_name
        # 工作空间
        self.workspace = workspace
        # 区域名
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.installed_app_name is not None:
            result['InstalledAppName'] = self.installed_app_name
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('InstalledAppName') is not None:
            self.installed_app_name = m.get('InstalledAppName')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class InstallGlobalAppResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: InstallGlobalAppResponseBody = None,
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
            temp_model = InstallGlobalAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAppsRequest(TeaModel):
    def __init__(
        self,
        workspace: str = None,
        next_token: str = None,
        max_results: int = None,
        order_by: str = None,
        is_reversed: bool = None,
        label_selector: str = None,
        scope: str = None,
        language: str = None,
        app_type: str = None,
        name: str = None,
    ):
        # 工作空间
        self.workspace = workspace
        # Next Token
        self.next_token = next_token
        # 最大返回结果数
        self.max_results = max_results
        # 排序依据
        self.order_by = order_by
        # 是否逆序
        self.is_reversed = is_reversed
        # Label 选择器
        self.label_selector = label_selector
        # 应用范围
        self.scope = scope
        # 应用描述语言
        self.language = language
        # 应用类型
        self.app_type = app_type
        # 按照名字匹配
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.order_by is not None:
            result['OrderBy'] = self.order_by
        if self.is_reversed is not None:
            result['IsReversed'] = self.is_reversed
        if self.label_selector is not None:
            result['LabelSelector'] = self.label_selector
        if self.scope is not None:
            result['Scope'] = self.scope
        if self.language is not None:
            result['Language'] = self.language
        if self.app_type is not None:
            result['AppType'] = self.app_type
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')
        if m.get('IsReversed') is not None:
            self.is_reversed = m.get('IsReversed')
        if m.get('LabelSelector') is not None:
            self.label_selector = m.get('LabelSelector')
        if m.get('Scope') is not None:
            self.scope = m.get('Scope')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class ListAppsResponseBodyApps(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        create_time: str = None,
        description: str = None,
        app_type: str = None,
        language: str = None,
        scope: str = None,
        workspace: str = None,
        source: str = None,
        namespace: str = None,
        app_orig_name: str = None,
        app_default_version: str = None,
        labels: Dict[str, str] = None,
    ):
        # 应用名称
        self.app_name = app_name
        # 创建时间
        self.create_time = create_time
        # 应用描述
        self.description = description
        # 应用类型
        self.app_type = app_type
        # 应用描述语言
        self.language = language
        # 应用可见范围
        self.scope = scope
        # 应用所在工作空间
        self.workspace = workspace
        # 应用来源
        self.source = source
        # 命名空间
        self.namespace = namespace
        # 应用原名
        self.app_orig_name = app_orig_name
        # 默认版本
        self.app_default_version = app_default_version
        # 标签
        self.labels = labels

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.app_type is not None:
            result['AppType'] = self.app_type
        if self.language is not None:
            result['Language'] = self.language
        if self.scope is not None:
            result['Scope'] = self.scope
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        if self.source is not None:
            result['Source'] = self.source
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.app_orig_name is not None:
            result['AppOrigName'] = self.app_orig_name
        if self.app_default_version is not None:
            result['AppDefaultVersion'] = self.app_default_version
        if self.labels is not None:
            result['Labels'] = self.labels
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('Scope') is not None:
            self.scope = m.get('Scope')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('AppOrigName') is not None:
            self.app_orig_name = m.get('AppOrigName')
        if m.get('AppDefaultVersion') is not None:
            self.app_default_version = m.get('AppDefaultVersion')
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        return self


class ListAppsResponseBody(TeaModel):
    def __init__(
        self,
        apps: List[ListAppsResponseBodyApps] = None,
        host_id: str = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # 应用数组
        self.apps = apps
        # 主机ID
        self.host_id = host_id
        # 最大返回个数
        self.max_results = max_results
        # Next Token
        self.next_token = next_token
        # 请求ID
        self.request_id = request_id
        # 返回个数
        self.total_count = total_count

    def validate(self):
        if self.apps:
            for k in self.apps:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Apps'] = []
        if self.apps is not None:
            for k in self.apps:
                result['Apps'].append(k.to_map() if k else None)
        if self.host_id is not None:
            result['HostId'] = self.host_id
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
        self.apps = []
        if m.get('Apps') is not None:
            for k in m.get('Apps'):
                temp_model = ListAppsResponseBodyApps()
                self.apps.append(temp_model.from_map(k))
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListAppsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListAppsResponseBody = None,
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
            temp_model = ListAppsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAuthorizedSoftwareRequest(TeaModel):
    def __init__(
        self,
        region: str = None,
        search: str = None,
        order_by: str = None,
        is_reversed: bool = None,
        next_token: str = None,
        max_results: int = None,
    ):
        # 区域
        self.region = region
        # 软件名称、软件长名称中搜索的关键字
        self.search = search
        # 排序字段
        self.order_by = order_by
        # 是否反转
        self.is_reversed = is_reversed
        # 翻页Token
        self.next_token = next_token
        # 分页数量
        self.max_results = max_results

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region is not None:
            result['Region'] = self.region
        if self.search is not None:
            result['Search'] = self.search
        if self.order_by is not None:
            result['OrderBy'] = self.order_by
        if self.is_reversed is not None:
            result['IsReversed'] = self.is_reversed
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Search') is not None:
            self.search = m.get('Search')
        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')
        if m.get('IsReversed') is not None:
            self.is_reversed = m.get('IsReversed')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        return self


class ListAuthorizedSoftwareResponseBodySoftwares(TeaModel):
    def __init__(
        self,
        software_name: str = None,
        software_long_name: str = None,
        software_description: str = None,
        software_default_version: str = None,
        software_versions: List[str] = None,
        software_license_fee: float = None,
        region_ids: List[str] = None,
        help_link: str = None,
        software_icon: str = None,
        last_modified: str = None,
    ):
        # 软件名称
        self.software_name = software_name
        # 软件长名称
        self.software_long_name = software_long_name
        # 软件描述
        self.software_description = software_description
        # 软件默认版本
        self.software_default_version = software_default_version
        # 软件所有版本
        self.software_versions = software_versions
        # 软件使用费用
        self.software_license_fee = software_license_fee
        # 软件可用区域
        self.region_ids = region_ids
        # 帮助链接
        self.help_link = help_link
        # 软件图标链接
        self.software_icon = software_icon
        # 最后更新时间
        self.last_modified = last_modified

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.software_name is not None:
            result['SoftwareName'] = self.software_name
        if self.software_long_name is not None:
            result['SoftwareLongName'] = self.software_long_name
        if self.software_description is not None:
            result['SoftwareDescription'] = self.software_description
        if self.software_default_version is not None:
            result['SoftwareDefaultVersion'] = self.software_default_version
        if self.software_versions is not None:
            result['SoftwareVersions'] = self.software_versions
        if self.software_license_fee is not None:
            result['SoftwareLicenseFee'] = self.software_license_fee
        if self.region_ids is not None:
            result['RegionIds'] = self.region_ids
        if self.help_link is not None:
            result['HelpLink'] = self.help_link
        if self.software_icon is not None:
            result['SoftwareIcon'] = self.software_icon
        if self.last_modified is not None:
            result['LastModified'] = self.last_modified
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SoftwareName') is not None:
            self.software_name = m.get('SoftwareName')
        if m.get('SoftwareLongName') is not None:
            self.software_long_name = m.get('SoftwareLongName')
        if m.get('SoftwareDescription') is not None:
            self.software_description = m.get('SoftwareDescription')
        if m.get('SoftwareDefaultVersion') is not None:
            self.software_default_version = m.get('SoftwareDefaultVersion')
        if m.get('SoftwareVersions') is not None:
            self.software_versions = m.get('SoftwareVersions')
        if m.get('SoftwareLicenseFee') is not None:
            self.software_license_fee = m.get('SoftwareLicenseFee')
        if m.get('RegionIds') is not None:
            self.region_ids = m.get('RegionIds')
        if m.get('HelpLink') is not None:
            self.help_link = m.get('HelpLink')
        if m.get('SoftwareIcon') is not None:
            self.software_icon = m.get('SoftwareIcon')
        if m.get('LastModified') is not None:
            self.last_modified = m.get('LastModified')
        return self


class ListAuthorizedSoftwareResponseBody(TeaModel):
    def __init__(
        self,
        host_id: str = None,
        request_id: str = None,
        http_code: int = None,
        code: str = None,
        message: str = None,
        success: bool = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        next_token: str = None,
        max_results: int = None,
        total_count: int = None,
        softwares: List[ListAuthorizedSoftwareResponseBodySoftwares] = None,
    ):
        # 主机ID
        self.host_id = host_id
        # 请求ID
        self.request_id = request_id
        self.http_code = http_code
        # 错误码
        self.code = code
        # 错误消息
        self.message = message
        # 是否调用成功
        self.success = success
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        # 翻页TOKEN
        self.next_token = next_token
        # 分页数
        self.max_results = max_results
        # 总记录数
        self.total_count = total_count
        # 软件信息
        self.softwares = softwares

    def validate(self):
        if self.softwares:
            for k in self.softwares:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.success is not None:
            result['Success'] = self.success
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['Softwares'] = []
        if self.softwares is not None:
            for k in self.softwares:
                result['Softwares'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.softwares = []
        if m.get('Softwares') is not None:
            for k in m.get('Softwares'):
                temp_model = ListAuthorizedSoftwareResponseBodySoftwares()
                self.softwares.append(temp_model.from_map(k))
        return self


class ListAuthorizedSoftwareResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListAuthorizedSoftwareResponseBody = None,
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
            temp_model = ListAuthorizedSoftwareResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListContainerImagesRequest(TeaModel):
    def __init__(
        self,
        region: str = None,
        next_token: str = None,
        max_results: int = None,
    ):
        # 区域
        self.region = region
        # 翻页Token
        self.next_token = next_token
        # 分页数量
        self.max_results = max_results

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region is not None:
            result['Region'] = self.region
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        return self


class ListContainerImagesResponseBodyContainerImages(TeaModel):
    def __init__(
        self,
        container_image_namespace: str = None,
        container_image_name: str = None,
        container_image_description: str = None,
        container_image_versions: List[str] = None,
        region_id: str = None,
        container_registry: str = None,
        last_modified: str = None,
    ):
        # 容器镜像名称空间名称
        self.container_image_namespace = container_image_namespace
        # 容器镜像名称
        self.container_image_name = container_image_name
        # 容器镜像描述
        self.container_image_description = container_image_description
        # 容器镜像版本
        self.container_image_versions = container_image_versions
        # 容器镜像所在区域
        self.region_id = region_id
        # 容器镜像仓库名称
        self.container_registry = container_registry
        # 最后更新时间
        self.last_modified = last_modified

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.container_image_namespace is not None:
            result['ContainerImageNamespace'] = self.container_image_namespace
        if self.container_image_name is not None:
            result['ContainerImageName'] = self.container_image_name
        if self.container_image_description is not None:
            result['ContainerImageDescription'] = self.container_image_description
        if self.container_image_versions is not None:
            result['ContainerImageVersions'] = self.container_image_versions
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.container_registry is not None:
            result['ContainerRegistry'] = self.container_registry
        if self.last_modified is not None:
            result['LastModified'] = self.last_modified
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContainerImageNamespace') is not None:
            self.container_image_namespace = m.get('ContainerImageNamespace')
        if m.get('ContainerImageName') is not None:
            self.container_image_name = m.get('ContainerImageName')
        if m.get('ContainerImageDescription') is not None:
            self.container_image_description = m.get('ContainerImageDescription')
        if m.get('ContainerImageVersions') is not None:
            self.container_image_versions = m.get('ContainerImageVersions')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ContainerRegistry') is not None:
            self.container_registry = m.get('ContainerRegistry')
        if m.get('LastModified') is not None:
            self.last_modified = m.get('LastModified')
        return self


class ListContainerImagesResponseBody(TeaModel):
    def __init__(
        self,
        host_id: str = None,
        request_id: str = None,
        http_code: int = None,
        code: str = None,
        message: str = None,
        success: bool = None,
        next_token: str = None,
        max_results: int = None,
        total_count: int = None,
        container_images: List[ListContainerImagesResponseBodyContainerImages] = None,
    ):
        self.host_id = host_id
        self.request_id = request_id
        self.http_code = http_code
        self.code = code
        self.message = message
        self.success = success
        self.next_token = next_token
        self.max_results = max_results
        self.total_count = total_count
        # 容器镜像
        self.container_images = container_images

    def validate(self):
        if self.container_images:
            for k in self.container_images:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.success is not None:
            result['Success'] = self.success
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['ContainerImages'] = []
        if self.container_images is not None:
            for k in self.container_images:
                result['ContainerImages'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.container_images = []
        if m.get('ContainerImages') is not None:
            for k in m.get('ContainerImages'):
                temp_model = ListContainerImagesResponseBodyContainerImages()
                self.container_images.append(temp_model.from_map(k))
        return self


class ListContainerImagesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListContainerImagesResponseBody = None,
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
            temp_model = ListContainerImagesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListEntitiesRequest(TeaModel):
    def __init__(
        self,
        workspace: str = None,
        next_token: str = None,
        max_results: int = None,
        order_by: str = None,
        is_reversed: bool = None,
    ):
        self.workspace = workspace
        self.next_token = next_token
        self.max_results = max_results
        self.order_by = order_by
        self.is_reversed = is_reversed

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.order_by is not None:
            result['OrderBy'] = self.order_by
        if self.is_reversed is not None:
            result['IsReversed'] = self.is_reversed
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')
        if m.get('IsReversed') is not None:
            self.is_reversed = m.get('IsReversed')
        return self


class ListEntitiesResponseBodyEntities(TeaModel):
    def __init__(
        self,
        entity_type: str = None,
    ):
        # 实体类型
        self.entity_type = entity_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        return self


class ListEntitiesResponseBody(TeaModel):
    def __init__(
        self,
        host_id: str = None,
        request_id: str = None,
        next_token: str = None,
        max_results: int = None,
        total_count: int = None,
        entities: List[ListEntitiesResponseBodyEntities] = None,
    ):
        # 主机ID
        self.host_id = host_id
        # 请求ID
        self.request_id = request_id
        self.next_token = next_token
        self.max_results = max_results
        self.total_count = total_count
        self.entities = entities

    def validate(self):
        if self.entities:
            for k in self.entities:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['Entities'] = []
        if self.entities is not None:
            for k in self.entities:
                result['Entities'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.entities = []
        if m.get('Entities') is not None:
            for k in m.get('Entities'):
                temp_model = ListEntitiesResponseBodyEntities()
                self.entities.append(temp_model.from_map(k))
        return self


class ListEntitiesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListEntitiesResponseBody = None,
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
            temp_model = ListEntitiesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListEntityItemsRequest(TeaModel):
    def __init__(
        self,
        workspace: str = None,
        entity_type: str = None,
        search: str = None,
        order_by: str = None,
        is_reversed: bool = None,
        next_token: str = None,
        max_results: int = None,
    ):
        self.workspace = workspace
        self.entity_type = entity_type
        self.search = search
        self.order_by = order_by
        self.is_reversed = is_reversed
        self.next_token = next_token
        self.max_results = max_results

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.search is not None:
            result['Search'] = self.search
        if self.order_by is not None:
            result['OrderBy'] = self.order_by
        if self.is_reversed is not None:
            result['IsReversed'] = self.is_reversed
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('Search') is not None:
            self.search = m.get('Search')
        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')
        if m.get('IsReversed') is not None:
            self.is_reversed = m.get('IsReversed')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        return self


class ListEntityItemsResponseBodyEntityItems(TeaModel):
    def __init__(
        self,
        entity_name: str = None,
        entity_data: Dict[str, str] = None,
    ):
        self.entity_name = entity_name
        self.entity_data = entity_data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entity_name is not None:
            result['EntityName'] = self.entity_name
        if self.entity_data is not None:
            result['EntityData'] = self.entity_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EntityName') is not None:
            self.entity_name = m.get('EntityName')
        if m.get('EntityData') is not None:
            self.entity_data = m.get('EntityData')
        return self


class ListEntityItemsResponseBody(TeaModel):
    def __init__(
        self,
        host_id: str = None,
        request_id: str = None,
        max_results: int = None,
        next_token: str = None,
        total_count: int = None,
        entity_items: List[ListEntityItemsResponseBodyEntityItems] = None,
    ):
        # 主机ID
        self.host_id = host_id
        # 请求ID
        self.request_id = request_id
        # 请求的最大结果数
        self.max_results = max_results
        # 下次查询的起始Token
        self.next_token = next_token
        # 返回总个数
        self.total_count = total_count
        # 实体类型数组
        self.entity_items = entity_items

    def validate(self):
        if self.entity_items:
            for k in self.entity_items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['EntityItems'] = []
        if self.entity_items is not None:
            for k in self.entity_items:
                result['EntityItems'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.entity_items = []
        if m.get('EntityItems') is not None:
            for k in m.get('EntityItems'):
                temp_model = ListEntityItemsResponseBodyEntityItems()
                self.entity_items.append(temp_model.from_map(k))
        return self


class ListEntityItemsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListEntityItemsResponseBody = None,
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
            temp_model = ListEntityItemsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListGlobalAppsRequest(TeaModel):
    def __init__(
        self,
        search: str = None,
        order_by: str = None,
        is_reversed: bool = None,
        next_token: str = None,
        max_results: int = None,
        app_scope: str = None,
        category: str = None,
        toolkit: str = None,
        region: str = None,
    ):
        # 模糊查询字段：NamesapceName  AppName  Categories AppDescription
        self.search = search
        # 排序
        self.order_by = order_by
        # 是否倒序，默认倒序排列
        self.is_reversed = is_reversed
        # 用来标记当前开始读取的位置，置空表示从头开始。
        self.next_token = next_token
        # 一批返回的最大数据量
        self.max_results = max_results
        # 可见范围
        self.app_scope = app_scope
        # 分类
        self.category = category
        # 工具集
        self.toolkit = toolkit
        # 区域Id
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.search is not None:
            result['Search'] = self.search
        if self.order_by is not None:
            result['OrderBy'] = self.order_by
        if self.is_reversed is not None:
            result['IsReversed'] = self.is_reversed
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.app_scope is not None:
            result['AppScope'] = self.app_scope
        if self.category is not None:
            result['Category'] = self.category
        if self.toolkit is not None:
            result['Toolkit'] = self.toolkit
        if self.region is not None:
            result['Region'] = self.region
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Search') is not None:
            self.search = m.get('Search')
        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')
        if m.get('IsReversed') is not None:
            self.is_reversed = m.get('IsReversed')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('AppScope') is not None:
            self.app_scope = m.get('AppScope')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Toolkit') is not None:
            self.toolkit = m.get('Toolkit')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        return self


class ListGlobalAppsResponseBodyGlobalApps(TeaModel):
    def __init__(
        self,
        namespace_name: str = None,
        app_scope: str = None,
        app_name: str = None,
        app_description: str = None,
        toolkit: str = None,
        app_fee: str = None,
        app_default_version: str = None,
        pinned: bool = None,
        last_modified: str = None,
        region_ids: List[str] = None,
        categories: List[str] = None,
    ):
        # 命名空间名称
        self.namespace_name = namespace_name
        # 应用权限
        self.app_scope = app_scope
        # 应用名称
        self.app_name = app_name
        # 应用描述
        self.app_description = app_description
        # 应用工具合集
        self.toolkit = toolkit
        # 应用计费说明
        self.app_fee = app_fee
        # 应用默认版本
        self.app_default_version = app_default_version
        # 应用收藏置顶标记
        self.pinned = pinned
        # 更新时间
        self.last_modified = last_modified
        # 应用支持的区域ids
        self.region_ids = region_ids
        # 应用所属分类
        self.categories = categories

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.namespace_name is not None:
            result['NamespaceName'] = self.namespace_name
        if self.app_scope is not None:
            result['AppScope'] = self.app_scope
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_description is not None:
            result['AppDescription'] = self.app_description
        if self.toolkit is not None:
            result['Toolkit'] = self.toolkit
        if self.app_fee is not None:
            result['AppFee'] = self.app_fee
        if self.app_default_version is not None:
            result['AppDefaultVersion'] = self.app_default_version
        if self.pinned is not None:
            result['Pinned'] = self.pinned
        if self.last_modified is not None:
            result['LastModified'] = self.last_modified
        if self.region_ids is not None:
            result['RegionIds'] = self.region_ids
        if self.categories is not None:
            result['Categories'] = self.categories
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NamespaceName') is not None:
            self.namespace_name = m.get('NamespaceName')
        if m.get('AppScope') is not None:
            self.app_scope = m.get('AppScope')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppDescription') is not None:
            self.app_description = m.get('AppDescription')
        if m.get('Toolkit') is not None:
            self.toolkit = m.get('Toolkit')
        if m.get('AppFee') is not None:
            self.app_fee = m.get('AppFee')
        if m.get('AppDefaultVersion') is not None:
            self.app_default_version = m.get('AppDefaultVersion')
        if m.get('Pinned') is not None:
            self.pinned = m.get('Pinned')
        if m.get('LastModified') is not None:
            self.last_modified = m.get('LastModified')
        if m.get('RegionIds') is not None:
            self.region_ids = m.get('RegionIds')
        if m.get('Categories') is not None:
            self.categories = m.get('Categories')
        return self


class ListGlobalAppsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        message: str = None,
        dynamic_code: str = None,
        global_apps: List[ListGlobalAppsResponseBodyGlobalApps] = None,
        next_token: str = None,
        max_results: int = None,
        total_count: int = None,
        dynamic_message: str = None,
        code: str = None,
        success: bool = None,
        host_id: str = None,
    ):
        self.request_id = request_id
        self.message = message
        self.dynamic_code = dynamic_code
        # 公共应用集合
        self.global_apps = global_apps
        # 用来表示当前调用返回读取到的位置，空代表数据已经读取完毕
        self.next_token = next_token
        # 本次请求所返回的最大记录条数
        self.max_results = max_results
        # 本次请求条件下的数据总量
        self.total_count = total_count
        self.dynamic_message = dynamic_message
        self.code = code
        self.success = success
        self.host_id = host_id

    def validate(self):
        if self.global_apps:
            for k in self.global_apps:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        result['GlobalApps'] = []
        if self.global_apps is not None:
            for k in self.global_apps:
                result['GlobalApps'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        if self.host_id is not None:
            result['HostId'] = self.host_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        self.global_apps = []
        if m.get('GlobalApps') is not None:
            for k in m.get('GlobalApps'):
                temp_model = ListGlobalAppsResponseBodyGlobalApps()
                self.global_apps.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        return self


class ListGlobalAppsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListGlobalAppsResponseBody = None,
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
            temp_model = ListGlobalAppsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPublicDatasetRequest(TeaModel):
    def __init__(
        self,
        search: str = None,
        tag: str = None,
        order_by: str = None,
        is_reversed: bool = None,
        next_token: str = None,
        max_results: int = None,
    ):
        # 名称、描述中搜索的关键字
        self.search = search
        # 公共数据集标签名
        self.tag = tag
        # 排序字段
        self.order_by = order_by
        # 排序是否反转
        self.is_reversed = is_reversed
        # 翻页Token
        self.next_token = next_token
        # 分页数量
        self.max_results = max_results

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.search is not None:
            result['Search'] = self.search
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.order_by is not None:
            result['OrderBy'] = self.order_by
        if self.is_reversed is not None:
            result['IsReversed'] = self.is_reversed
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Search') is not None:
            self.search = m.get('Search')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')
        if m.get('IsReversed') is not None:
            self.is_reversed = m.get('IsReversed')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        return self


class ListPublicDatasetResponseBodyDatasets(TeaModel):
    def __init__(
        self,
        last_modified: str = None,
        copyright: str = None,
        access_requirements: str = None,
        about: str = None,
        tags: List[str] = None,
        dataset_name: str = None,
        dataset_description: str = None,
        update_frequency: str = None,
        region_ids: List[str] = None,
    ):
        # 最后更新时间
        self.last_modified = last_modified
        # 公共数据集版权信息
        self.copyright = copyright
        # 公共数据集访问要求
        self.access_requirements = access_requirements
        # 关于公共数据集
        self.about = about
        # 公共数据集标签
        self.tags = tags
        # 公共数据集名称
        self.dataset_name = dataset_name
        # 公共数据集描述
        self.dataset_description = dataset_description
        # 公共数据集更新频率
        self.update_frequency = update_frequency
        # 公共数据集可用区域
        self.region_ids = region_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.last_modified is not None:
            result['LastModified'] = self.last_modified
        if self.copyright is not None:
            result['Copyright'] = self.copyright
        if self.access_requirements is not None:
            result['AccessRequirements'] = self.access_requirements
        if self.about is not None:
            result['About'] = self.about
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.dataset_description is not None:
            result['DatasetDescription'] = self.dataset_description
        if self.update_frequency is not None:
            result['UpdateFrequency'] = self.update_frequency
        if self.region_ids is not None:
            result['RegionIds'] = self.region_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LastModified') is not None:
            self.last_modified = m.get('LastModified')
        if m.get('Copyright') is not None:
            self.copyright = m.get('Copyright')
        if m.get('AccessRequirements') is not None:
            self.access_requirements = m.get('AccessRequirements')
        if m.get('About') is not None:
            self.about = m.get('About')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('DatasetDescription') is not None:
            self.dataset_description = m.get('DatasetDescription')
        if m.get('UpdateFrequency') is not None:
            self.update_frequency = m.get('UpdateFrequency')
        if m.get('RegionIds') is not None:
            self.region_ids = m.get('RegionIds')
        return self


class ListPublicDatasetResponseBody(TeaModel):
    def __init__(
        self,
        host_id: str = None,
        request_id: str = None,
        http_code: int = None,
        code: str = None,
        message: str = None,
        success: bool = None,
        next_token: str = None,
        max_results: int = None,
        total_count: int = None,
        datasets: List[ListPublicDatasetResponseBodyDatasets] = None,
    ):
        # 主机ID
        self.host_id = host_id
        # 请求ID
        self.request_id = request_id
        self.http_code = http_code
        # 错误码
        self.code = code
        # 错误消息
        self.message = message
        # 是否调用成功
        self.success = success
        # 翻页Token
        self.next_token = next_token
        # 分页数
        self.max_results = max_results
        # 总记录数
        self.total_count = total_count
        # 公共数据集信息
        self.datasets = datasets

    def validate(self):
        if self.datasets:
            for k in self.datasets:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.success is not None:
            result['Success'] = self.success
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['Datasets'] = []
        if self.datasets is not None:
            for k in self.datasets:
                result['Datasets'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.datasets = []
        if m.get('Datasets') is not None:
            for k in m.get('Datasets'):
                temp_model = ListPublicDatasetResponseBodyDatasets()
                self.datasets.append(temp_model.from_map(k))
        return self


class ListPublicDatasetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListPublicDatasetResponseBody = None,
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
            temp_model = ListPublicDatasetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPublicDatasetEntitiesRequest(TeaModel):
    def __init__(
        self,
        dataset_name: str = None,
        order_by: str = None,
        is_reversed: bool = None,
        next_token: str = None,
        max_results: int = None,
    ):
        # 数据集名称
        self.dataset_name = dataset_name
        # 排序字段
        self.order_by = order_by
        # 排序是否反转
        self.is_reversed = is_reversed
        # 翻页Token
        self.next_token = next_token
        # 分页数量
        self.max_results = max_results

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.order_by is not None:
            result['OrderBy'] = self.order_by
        if self.is_reversed is not None:
            result['IsReversed'] = self.is_reversed
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')
        if m.get('IsReversed') is not None:
            self.is_reversed = m.get('IsReversed')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        return self


class ListPublicDatasetEntitiesResponseBodyEntities(TeaModel):
    def __init__(
        self,
        entity_type: str = None,
    ):
        # 实体类型
        self.entity_type = entity_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        return self


class ListPublicDatasetEntitiesResponseBody(TeaModel):
    def __init__(
        self,
        host_id: str = None,
        request_id: str = None,
        http_code: int = None,
        code: str = None,
        message: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        next_token: str = None,
        max_results: int = None,
        total_count: int = None,
        dataset_name: str = None,
        entities: List[ListPublicDatasetEntitiesResponseBodyEntities] = None,
    ):
        # 主机ID
        self.host_id = host_id
        # 请求ID
        self.request_id = request_id
        self.http_code = http_code
        # 错误码
        self.code = code
        # 错误消息
        self.message = message
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        # 翻页Token
        self.next_token = next_token
        # 分页数
        self.max_results = max_results
        # 总记录数
        self.total_count = total_count
        # 公共数据集名称
        self.dataset_name = dataset_name
        # 该实体包含的所有类型
        self.entities = entities

    def validate(self):
        if self.entities:
            for k in self.entities:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        result['Entities'] = []
        if self.entities is not None:
            for k in self.entities:
                result['Entities'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        self.entities = []
        if m.get('Entities') is not None:
            for k in m.get('Entities'):
                temp_model = ListPublicDatasetEntitiesResponseBodyEntities()
                self.entities.append(temp_model.from_map(k))
        return self


class ListPublicDatasetEntitiesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListPublicDatasetEntitiesResponseBody = None,
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
            temp_model = ListPublicDatasetEntitiesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPublicDatasetEntityItemsRequest(TeaModel):
    def __init__(
        self,
        dataset_name: str = None,
        entity_type: str = None,
        search: str = None,
        order_by: str = None,
        is_reversed: bool = None,
        next_token: str = None,
        max_results: int = None,
    ):
        # 数据集名称
        self.dataset_name = dataset_name
        # 实体类型
        self.entity_type = entity_type
        # 实体名中搜索的关键字
        self.search = search
        # 排序字段
        self.order_by = order_by
        # 是否反转
        self.is_reversed = is_reversed
        # 翻页Token
        self.next_token = next_token
        # 分页数量
        self.max_results = max_results

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.search is not None:
            result['Search'] = self.search
        if self.order_by is not None:
            result['OrderBy'] = self.order_by
        if self.is_reversed is not None:
            result['IsReversed'] = self.is_reversed
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('Search') is not None:
            self.search = m.get('Search')
        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')
        if m.get('IsReversed') is not None:
            self.is_reversed = m.get('IsReversed')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        return self


class ListPublicDatasetEntityItemsResponseBodyEntityItems(TeaModel):
    def __init__(
        self,
        entity_name: str = None,
        entity_data: Dict[str, str] = None,
    ):
        # 实体名称
        self.entity_name = entity_name
        # 实体属性值
        self.entity_data = entity_data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entity_name is not None:
            result['EntityName'] = self.entity_name
        if self.entity_data is not None:
            result['EntityData'] = self.entity_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EntityName') is not None:
            self.entity_name = m.get('EntityName')
        if m.get('EntityData') is not None:
            self.entity_data = m.get('EntityData')
        return self


class ListPublicDatasetEntityItemsResponseBody(TeaModel):
    def __init__(
        self,
        host_id: str = None,
        request_id: str = None,
        http_code: int = None,
        code: str = None,
        message: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        next_token: str = None,
        max_results: int = None,
        total_count: int = None,
        dataset_name: str = None,
        entity_items: List[ListPublicDatasetEntityItemsResponseBodyEntityItems] = None,
    ):
        # 主机ID
        self.host_id = host_id
        # 请求ID
        self.request_id = request_id
        self.http_code = http_code
        # 错误码
        self.code = code
        # 错误消息
        self.message = message
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        # 翻页Token
        self.next_token = next_token
        # 分页数
        self.max_results = max_results
        # 总记录数
        self.total_count = total_count
        # 公共数据集名称
        self.dataset_name = dataset_name
        # 该实体包含的所有对象
        self.entity_items = entity_items

    def validate(self):
        if self.entity_items:
            for k in self.entity_items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        result['EntityItems'] = []
        if self.entity_items is not None:
            for k in self.entity_items:
                result['EntityItems'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        self.entity_items = []
        if m.get('EntityItems') is not None:
            for k in m.get('EntityItems'):
                temp_model = ListPublicDatasetEntityItemsResponseBodyEntityItems()
                self.entity_items.append(temp_model.from_map(k))
        return self


class ListPublicDatasetEntityItemsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListPublicDatasetEntityItemsResponseBody = None,
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
            temp_model = ListPublicDatasetEntityItemsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPublicDatasetTagsRequest(TeaModel):
    def __init__(
        self,
        search: str = None,
        order_by: str = None,
        is_reversed: bool = None,
        next_token: str = None,
        max_results: int = None,
    ):
        # 标签名中搜索的关键字
        self.search = search
        # 排序字段
        self.order_by = order_by
        # 是否反转
        self.is_reversed = is_reversed
        # 翻页Token
        self.next_token = next_token
        # 分页数量
        self.max_results = max_results

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.search is not None:
            result['Search'] = self.search
        if self.order_by is not None:
            result['OrderBy'] = self.order_by
        if self.is_reversed is not None:
            result['IsReversed'] = self.is_reversed
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Search') is not None:
            self.search = m.get('Search')
        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')
        if m.get('IsReversed') is not None:
            self.is_reversed = m.get('IsReversed')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        return self


class ListPublicDatasetTagsResponseBody(TeaModel):
    def __init__(
        self,
        host_id: str = None,
        request_id: str = None,
        http_code: int = None,
        code: str = None,
        message: str = None,
        success: bool = None,
        next_token: str = None,
        max_results: int = None,
        total_count: int = None,
        tags: List[str] = None,
    ):
        # 主机ID
        self.host_id = host_id
        # 请求ID
        self.request_id = request_id
        self.http_code = http_code
        # 错误码
        self.code = code
        # 错误消息
        self.message = message
        # 是否调用成功
        self.success = success
        # 翻页Token
        self.next_token = next_token
        # 分页数
        self.max_results = max_results
        # 总记录数
        self.total_count = total_count
        # 公共数据集标签
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.success is not None:
            result['Success'] = self.success
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        return self


class ListPublicDatasetTagsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListPublicDatasetTagsResponseBody = None,
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
            temp_model = ListPublicDatasetTagsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRegionsResponseBodyRegions(TeaModel):
    def __init__(
        self,
        local_name: str = None,
        region_endpoint: str = None,
        region_id: str = None,
    ):
        self.local_name = local_name
        self.region_endpoint = region_endpoint
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.local_name is not None:
            result['LocalName'] = self.local_name
        if self.region_endpoint is not None:
            result['RegionEndpoint'] = self.region_endpoint
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')
        if m.get('RegionEndpoint') is not None:
            self.region_endpoint = m.get('RegionEndpoint')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListRegionsResponseBody(TeaModel):
    def __init__(
        self,
        host_id: str = None,
        request_id: str = None,
        code: str = None,
        message: str = None,
        success: bool = None,
        regions: List[ListRegionsResponseBodyRegions] = None,
    ):
        # 主机ID
        self.host_id = host_id
        # 请求ID
        self.request_id = request_id
        # 错误码
        self.code = code
        # 错误消息
        self.message = message
        # 是否调用成功
        self.success = success
        # 基因云产品上线区域
        self.regions = regions

    def validate(self):
        if self.regions:
            for k in self.regions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.success is not None:
            result['Success'] = self.success
        result['Regions'] = []
        if self.regions is not None:
            for k in self.regions:
                result['Regions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        self.regions = []
        if m.get('Regions') is not None:
            for k in m.get('Regions'):
                temp_model = ListRegionsResponseBodyRegions()
                self.regions.append(temp_model.from_map(k))
        return self


class ListRegionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListRegionsResponseBody = None,
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
            temp_model = ListRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRunsRequest(TeaModel):
    def __init__(
        self,
        workspace: str = None,
        name: str = None,
        status: str = None,
        submission_id: str = None,
        search: str = None,
        label_selector: str = None,
        app_name: str = None,
        next_token: str = None,
        max_results: int = None,
        order_by: str = None,
        is_reversed: bool = None,
        get_total: bool = None,
    ):
        # 工作空间
        self.workspace = workspace
        # 任务名字
        self.name = name
        # 状态
        self.status = status
        # 提交ID
        self.submission_id = submission_id
        # 搜索ID
        self.search = search
        # 标签选择
        self.label_selector = label_selector
        # 应用名称
        self.app_name = app_name
        self.next_token = next_token
        self.max_results = max_results
        self.order_by = order_by
        self.is_reversed = is_reversed
        self.get_total = get_total

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        if self.name is not None:
            result['Name'] = self.name
        if self.status is not None:
            result['Status'] = self.status
        if self.submission_id is not None:
            result['SubmissionId'] = self.submission_id
        if self.search is not None:
            result['Search'] = self.search
        if self.label_selector is not None:
            result['LabelSelector'] = self.label_selector
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.order_by is not None:
            result['OrderBy'] = self.order_by
        if self.is_reversed is not None:
            result['IsReversed'] = self.is_reversed
        if self.get_total is not None:
            result['GetTotal'] = self.get_total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubmissionId') is not None:
            self.submission_id = m.get('SubmissionId')
        if m.get('Search') is not None:
            self.search = m.get('Search')
        if m.get('LabelSelector') is not None:
            self.label_selector = m.get('LabelSelector')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')
        if m.get('IsReversed') is not None:
            self.is_reversed = m.get('IsReversed')
        if m.get('GetTotal') is not None:
            self.get_total = m.get('GetTotal')
        return self


class ListRunsResponseBodyRunsExecuteOptions(TeaModel):
    def __init__(
        self,
        call_caching: bool = None,
        delete_intermediate_results: bool = None,
        failure_mode: str = None,
    ):
        self.call_caching = call_caching
        self.delete_intermediate_results = delete_intermediate_results
        self.failure_mode = failure_mode

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.call_caching is not None:
            result['CallCaching'] = self.call_caching
        if self.delete_intermediate_results is not None:
            result['DeleteIntermediateResults'] = self.delete_intermediate_results
        if self.failure_mode is not None:
            result['FailureMode'] = self.failure_mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallCaching') is not None:
            self.call_caching = m.get('CallCaching')
        if m.get('DeleteIntermediateResults') is not None:
            self.delete_intermediate_results = m.get('DeleteIntermediateResults')
        if m.get('FailureMode') is not None:
            self.failure_mode = m.get('FailureMode')
        return self


class ListRunsResponseBodyRuns(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        source: str = None,
        namespace: str = None,
        app_orig_name: str = None,
        labels: Dict[str, str] = None,
        name: str = None,
        revision: str = None,
        run_id: str = None,
        status: str = None,
        create_time: str = None,
        start_time: str = None,
        end_time: str = None,
        submission_id: str = None,
        entity_name: str = None,
        entity_type: str = None,
        execute_directory: str = None,
        execute_options: ListRunsResponseBodyRunsExecuteOptions = None,
        inputs: str = None,
        default_runtime: str = None,
        workspace: str = None,
        region_id: str = None,
    ):
        # 应用名称
        self.app_name = app_name
        # 应用来源
        self.source = source
        # 应用命名空间
        self.namespace = namespace
        # 应用原名
        self.app_orig_name = app_orig_name
        # 任务标签
        self.labels = labels
        # 任务名称
        self.name = name
        # 应用版本号
        self.revision = revision
        # 任务ID
        self.run_id = run_id
        # 任务状态
        self.status = status
        # 提交时间
        self.create_time = create_time
        # 开始时间
        self.start_time = start_time
        # 结束时间
        self.end_time = end_time
        # 提交ID
        self.submission_id = submission_id
        # 实体名称
        self.entity_name = entity_name
        # 实体对象ID
        self.entity_type = entity_type
        # 运行目录
        self.execute_directory = execute_directory
        self.execute_options = execute_options
        # 输入参数
        self.inputs = inputs
        self.default_runtime = default_runtime
        self.workspace = workspace
        self.region_id = region_id

    def validate(self):
        if self.execute_options:
            self.execute_options.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.source is not None:
            result['Source'] = self.source
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.app_orig_name is not None:
            result['AppOrigName'] = self.app_orig_name
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.name is not None:
            result['Name'] = self.name
        if self.revision is not None:
            result['Revision'] = self.revision
        if self.run_id is not None:
            result['RunId'] = self.run_id
        if self.status is not None:
            result['Status'] = self.status
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.submission_id is not None:
            result['SubmissionId'] = self.submission_id
        if self.entity_name is not None:
            result['EntityName'] = self.entity_name
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.execute_directory is not None:
            result['ExecuteDirectory'] = self.execute_directory
        if self.execute_options is not None:
            result['ExecuteOptions'] = self.execute_options.to_map()
        if self.inputs is not None:
            result['Inputs'] = self.inputs
        if self.default_runtime is not None:
            result['DefaultRuntime'] = self.default_runtime
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('AppOrigName') is not None:
            self.app_orig_name = m.get('AppOrigName')
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Revision') is not None:
            self.revision = m.get('Revision')
        if m.get('RunId') is not None:
            self.run_id = m.get('RunId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('SubmissionId') is not None:
            self.submission_id = m.get('SubmissionId')
        if m.get('EntityName') is not None:
            self.entity_name = m.get('EntityName')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('ExecuteDirectory') is not None:
            self.execute_directory = m.get('ExecuteDirectory')
        if m.get('ExecuteOptions') is not None:
            temp_model = ListRunsResponseBodyRunsExecuteOptions()
            self.execute_options = temp_model.from_map(m['ExecuteOptions'])
        if m.get('Inputs') is not None:
            self.inputs = m.get('Inputs')
        if m.get('DefaultRuntime') is not None:
            self.default_runtime = m.get('DefaultRuntime')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListRunsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        host_id: str = None,
        max_results: int = None,
        next_token: str = None,
        total_count: int = None,
        runs: List[ListRunsResponseBodyRuns] = None,
    ):
        # 请求ID
        self.request_id = request_id
        # 主机ID
        self.host_id = host_id
        # 最大返回结果
        self.max_results = max_results
        # 下次查询Token
        self.next_token = next_token
        # 返回个数
        self.total_count = total_count
        # 任务列表
        self.runs = runs

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
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['Runs'] = []
        if self.runs is not None:
            for k in self.runs:
                result['Runs'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.runs = []
        if m.get('Runs') is not None:
            for k in m.get('Runs'):
                temp_model = ListRunsResponseBodyRuns()
                self.runs.append(temp_model.from_map(k))
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


class ListSubmissionsRequest(TeaModel):
    def __init__(
        self,
        workspace: str = None,
        status: str = None,
        search: str = None,
        next_token: str = None,
        max_results: int = None,
        order_by: str = None,
        is_reversed: bool = None,
    ):
        # 工作空间
        self.workspace = workspace
        # 状态
        self.status = status
        # 搜索ID
        self.search = search
        self.next_token = next_token
        self.max_results = max_results
        self.order_by = order_by
        self.is_reversed = is_reversed

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        if self.status is not None:
            result['Status'] = self.status
        if self.search is not None:
            result['Search'] = self.search
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.order_by is not None:
            result['OrderBy'] = self.order_by
        if self.is_reversed is not None:
            result['IsReversed'] = self.is_reversed
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Search') is not None:
            self.search = m.get('Search')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')
        if m.get('IsReversed') is not None:
            self.is_reversed = m.get('IsReversed')
        return self


class ListSubmissionsResponseBodySubmissionsRunStats(TeaModel):
    def __init__(
        self,
        submitted: int = None,
        pending: int = None,
        running: int = None,
        succeeded: int = None,
        failed: int = None,
        aborting: int = None,
        aborted: int = None,
    ):
        self.submitted = submitted
        self.pending = pending
        self.running = running
        self.succeeded = succeeded
        self.failed = failed
        self.aborting = aborting
        self.aborted = aborted

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.submitted is not None:
            result['Submitted'] = self.submitted
        if self.pending is not None:
            result['Pending'] = self.pending
        if self.running is not None:
            result['Running'] = self.running
        if self.succeeded is not None:
            result['Succeeded'] = self.succeeded
        if self.failed is not None:
            result['Failed'] = self.failed
        if self.aborting is not None:
            result['Aborting'] = self.aborting
        if self.aborted is not None:
            result['Aborted'] = self.aborted
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Submitted') is not None:
            self.submitted = m.get('Submitted')
        if m.get('Pending') is not None:
            self.pending = m.get('Pending')
        if m.get('Running') is not None:
            self.running = m.get('Running')
        if m.get('Succeeded') is not None:
            self.succeeded = m.get('Succeeded')
        if m.get('Failed') is not None:
            self.failed = m.get('Failed')
        if m.get('Aborting') is not None:
            self.aborting = m.get('Aborting')
        if m.get('Aborted') is not None:
            self.aborted = m.get('Aborted')
        return self


class ListSubmissionsResponseBodySubmissions(TeaModel):
    def __init__(
        self,
        workspace: str = None,
        submission_id: str = None,
        status: str = None,
        create_time: str = None,
        start_time: str = None,
        end_time: str = None,
        entity_type: str = None,
        run_stats: ListSubmissionsResponseBodySubmissionsRunStats = None,
    ):
        # 提交ID
        self.workspace = workspace
        # 提交ID
        self.submission_id = submission_id
        # 任务状态
        self.status = status
        # 提交时间
        self.create_time = create_time
        # 开始时间
        self.start_time = start_time
        # 结束时间
        self.end_time = end_time
        # 实体类型
        self.entity_type = entity_type
        self.run_stats = run_stats

    def validate(self):
        if self.run_stats:
            self.run_stats.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        if self.submission_id is not None:
            result['SubmissionId'] = self.submission_id
        if self.status is not None:
            result['Status'] = self.status
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.run_stats is not None:
            result['RunStats'] = self.run_stats.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        if m.get('SubmissionId') is not None:
            self.submission_id = m.get('SubmissionId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('RunStats') is not None:
            temp_model = ListSubmissionsResponseBodySubmissionsRunStats()
            self.run_stats = temp_model.from_map(m['RunStats'])
        return self


class ListSubmissionsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        host_id: str = None,
        max_results: int = None,
        next_token: str = None,
        total_count: int = None,
        submissions: List[ListSubmissionsResponseBodySubmissions] = None,
    ):
        # 请求ID
        self.request_id = request_id
        # 主机ID
        self.host_id = host_id
        # 最大返回结果
        self.max_results = max_results
        # 下次查询Token
        self.next_token = next_token
        # 返回个数
        self.total_count = total_count
        # 投递列表
        self.submissions = submissions

    def validate(self):
        if self.submissions:
            for k in self.submissions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['Submissions'] = []
        if self.submissions is not None:
            for k in self.submissions:
                result['Submissions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.submissions = []
        if m.get('Submissions') is not None:
            for k in m.get('Submissions'):
                temp_model = ListSubmissionsResponseBodySubmissions()
                self.submissions.append(temp_model.from_map(k))
        return self


class ListSubmissionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListSubmissionsResponseBody = None,
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
            temp_model = ListSubmissionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTemplatesRequest(TeaModel):
    def __init__(
        self,
        workspace: str = None,
        next_token: str = None,
        max_results: int = None,
        order_by: str = None,
        is_reversed: bool = None,
        label_selector: str = None,
        search: str = None,
    ):
        # 工作空间
        self.workspace = workspace
        # Next Token
        self.next_token = next_token
        # 最大返回结果数
        self.max_results = max_results
        # 排序依据
        self.order_by = order_by
        # 是否逆序
        self.is_reversed = is_reversed
        # Label 选择器
        self.label_selector = label_selector
        # 查找条件
        self.search = search

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.order_by is not None:
            result['OrderBy'] = self.order_by
        if self.is_reversed is not None:
            result['IsReversed'] = self.is_reversed
        if self.label_selector is not None:
            result['LabelSelector'] = self.label_selector
        if self.search is not None:
            result['Search'] = self.search
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')
        if m.get('IsReversed') is not None:
            self.is_reversed = m.get('IsReversed')
        if m.get('LabelSelector') is not None:
            self.label_selector = m.get('LabelSelector')
        if m.get('Search') is not None:
            self.search = m.get('Search')
        return self


class ListTemplatesResponseBodyTemplatesInputs(TeaModel):
    def __init__(
        self,
        task_name: str = None,
        variable_name: str = None,
        variable_type: str = None,
        variable_value: str = None,
        required: bool = None,
        help: str = None,
        step_order: int = None,
    ):
        # 任务名称
        self.task_name = task_name
        # 变量名称
        self.variable_name = variable_name
        # 变量类型
        self.variable_type = variable_type
        # 变量值
        self.variable_value = variable_value
        # 是否必须参数
        self.required = required
        # 帮助信息
        self.help = help
        # 步骤顺序
        self.step_order = step_order

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.variable_name is not None:
            result['VariableName'] = self.variable_name
        if self.variable_type is not None:
            result['VariableType'] = self.variable_type
        if self.variable_value is not None:
            result['VariableValue'] = self.variable_value
        if self.required is not None:
            result['Required'] = self.required
        if self.help is not None:
            result['Help'] = self.help
        if self.step_order is not None:
            result['StepOrder'] = self.step_order
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('VariableName') is not None:
            self.variable_name = m.get('VariableName')
        if m.get('VariableType') is not None:
            self.variable_type = m.get('VariableType')
        if m.get('VariableValue') is not None:
            self.variable_value = m.get('VariableValue')
        if m.get('Required') is not None:
            self.required = m.get('Required')
        if m.get('Help') is not None:
            self.help = m.get('Help')
        if m.get('StepOrder') is not None:
            self.step_order = m.get('StepOrder')
        return self


class ListTemplatesResponseBodyTemplatesOutputs(TeaModel):
    def __init__(
        self,
        task_name: str = None,
        variable_name: str = None,
        variable_type: str = None,
        variable_value: str = None,
        required: bool = None,
        help: str = None,
        step_order: int = None,
    ):
        # 任务名称
        self.task_name = task_name
        # 变量名称
        self.variable_name = variable_name
        # 变量类型
        self.variable_type = variable_type
        # 变量值
        self.variable_value = variable_value
        # 是否必须参数
        self.required = required
        # 帮助信息
        self.help = help
        # 步骤顺序
        self.step_order = step_order

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.variable_name is not None:
            result['VariableName'] = self.variable_name
        if self.variable_type is not None:
            result['VariableType'] = self.variable_type
        if self.variable_value is not None:
            result['VariableValue'] = self.variable_value
        if self.required is not None:
            result['Required'] = self.required
        if self.help is not None:
            result['Help'] = self.help
        if self.step_order is not None:
            result['StepOrder'] = self.step_order
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('VariableName') is not None:
            self.variable_name = m.get('VariableName')
        if m.get('VariableType') is not None:
            self.variable_type = m.get('VariableType')
        if m.get('VariableValue') is not None:
            self.variable_value = m.get('VariableValue')
        if m.get('Required') is not None:
            self.required = m.get('Required')
        if m.get('Help') is not None:
            self.help = m.get('Help')
        if m.get('StepOrder') is not None:
            self.step_order = m.get('StepOrder')
        return self


class ListTemplatesResponseBodyTemplates(TeaModel):
    def __init__(
        self,
        workspace: str = None,
        template_name: str = None,
        labels: Dict[str, str] = None,
        app_name: str = None,
        revision: str = None,
        root_entity: str = None,
        inputs: List[ListTemplatesResponseBodyTemplatesInputs] = None,
        outputs: List[ListTemplatesResponseBodyTemplatesOutputs] = None,
        description: str = None,
        create_time: str = None,
        last_modified_time: str = None,
    ):
        # 工作空间
        self.workspace = workspace
        # 应用模板名称
        self.template_name = template_name
        # 标签
        self.labels = labels
        # 应用名称
        self.app_name = app_name
        # 应用版本
        self.revision = revision
        # 实体类型
        self.root_entity = root_entity
        # 应用输入
        self.inputs = inputs
        # 应用的输出参数
        self.outputs = outputs
        # 模板描述信息
        self.description = description
        # 创建时间
        self.create_time = create_time
        # 最后修改时间
        self.last_modified_time = last_modified_time

    def validate(self):
        if self.inputs:
            for k in self.inputs:
                if k:
                    k.validate()
        if self.outputs:
            for k in self.outputs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.revision is not None:
            result['Revision'] = self.revision
        if self.root_entity is not None:
            result['RootEntity'] = self.root_entity
        result['Inputs'] = []
        if self.inputs is not None:
            for k in self.inputs:
                result['Inputs'].append(k.to_map() if k else None)
        result['Outputs'] = []
        if self.outputs is not None:
            for k in self.outputs:
                result['Outputs'].append(k.to_map() if k else None)
        if self.description is not None:
            result['Description'] = self.description
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.last_modified_time is not None:
            result['LastModifiedTime'] = self.last_modified_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Revision') is not None:
            self.revision = m.get('Revision')
        if m.get('RootEntity') is not None:
            self.root_entity = m.get('RootEntity')
        self.inputs = []
        if m.get('Inputs') is not None:
            for k in m.get('Inputs'):
                temp_model = ListTemplatesResponseBodyTemplatesInputs()
                self.inputs.append(temp_model.from_map(k))
        self.outputs = []
        if m.get('Outputs') is not None:
            for k in m.get('Outputs'):
                temp_model = ListTemplatesResponseBodyTemplatesOutputs()
                self.outputs.append(temp_model.from_map(k))
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('LastModifiedTime') is not None:
            self.last_modified_time = m.get('LastModifiedTime')
        return self


class ListTemplatesResponseBody(TeaModel):
    def __init__(
        self,
        host_id: str = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        templates: List[ListTemplatesResponseBodyTemplates] = None,
        total_count: int = None,
    ):
        # 主机ID
        self.host_id = host_id
        # 最大返回结果
        self.max_results = max_results
        # 下次查询Token
        self.next_token = next_token
        # 请求ID
        self.request_id = request_id
        # 应用模板列表
        self.templates = templates
        # 返回个数
        self.total_count = total_count

    def validate(self):
        if self.templates:
            for k in self.templates:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Templates'] = []
        if self.templates is not None:
            for k in self.templates:
                result['Templates'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.templates = []
        if m.get('Templates') is not None:
            for k in m.get('Templates'):
                temp_model = ListTemplatesResponseBodyTemplates()
                self.templates.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListTemplatesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListTemplatesResponseBody = None,
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
            temp_model = ListTemplatesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUserActiveRunsRequest(TeaModel):
    def __init__(
        self,
        workspace: str = None,
        name: str = None,
        status: str = None,
        submission_id: str = None,
        search: str = None,
        label_selector: str = None,
        app_name: str = None,
        next_token: str = None,
        max_results: int = None,
        order_by: str = None,
        is_reversed: bool = None,
    ):
        # 工作空间
        self.workspace = workspace
        # 任务名字
        self.name = name
        # 状态
        self.status = status
        # 提交ID
        self.submission_id = submission_id
        # 搜索ID
        self.search = search
        # 标签选择
        self.label_selector = label_selector
        # 应用名称
        self.app_name = app_name
        self.next_token = next_token
        self.max_results = max_results
        self.order_by = order_by
        self.is_reversed = is_reversed

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        if self.name is not None:
            result['Name'] = self.name
        if self.status is not None:
            result['Status'] = self.status
        if self.submission_id is not None:
            result['SubmissionId'] = self.submission_id
        if self.search is not None:
            result['Search'] = self.search
        if self.label_selector is not None:
            result['LabelSelector'] = self.label_selector
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.order_by is not None:
            result['OrderBy'] = self.order_by
        if self.is_reversed is not None:
            result['IsReversed'] = self.is_reversed
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubmissionId') is not None:
            self.submission_id = m.get('SubmissionId')
        if m.get('Search') is not None:
            self.search = m.get('Search')
        if m.get('LabelSelector') is not None:
            self.label_selector = m.get('LabelSelector')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')
        if m.get('IsReversed') is not None:
            self.is_reversed = m.get('IsReversed')
        return self


class ListUserActiveRunsResponseBodyRunsExecuteOptions(TeaModel):
    def __init__(
        self,
        call_caching: bool = None,
        delete_intermediate_results: bool = None,
        failure_mode: str = None,
    ):
        self.call_caching = call_caching
        self.delete_intermediate_results = delete_intermediate_results
        self.failure_mode = failure_mode

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.call_caching is not None:
            result['CallCaching'] = self.call_caching
        if self.delete_intermediate_results is not None:
            result['DeleteIntermediateResults'] = self.delete_intermediate_results
        if self.failure_mode is not None:
            result['FailureMode'] = self.failure_mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallCaching') is not None:
            self.call_caching = m.get('CallCaching')
        if m.get('DeleteIntermediateResults') is not None:
            self.delete_intermediate_results = m.get('DeleteIntermediateResults')
        if m.get('FailureMode') is not None:
            self.failure_mode = m.get('FailureMode')
        return self


class ListUserActiveRunsResponseBodyRuns(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        source: str = None,
        namespace: str = None,
        app_orig_name: str = None,
        labels: Dict[str, str] = None,
        name: str = None,
        revision: str = None,
        run_id: str = None,
        status: str = None,
        create_time: str = None,
        start_time: str = None,
        end_time: str = None,
        submission_id: str = None,
        entity_name: str = None,
        entity_type: str = None,
        execute_directory: str = None,
        execute_options: ListUserActiveRunsResponseBodyRunsExecuteOptions = None,
        inputs: str = None,
        default_runtime: str = None,
        workspace: str = None,
        region_id: str = None,
    ):
        # 应用名称
        self.app_name = app_name
        # 应用来源
        self.source = source
        # 应用命名空间
        self.namespace = namespace
        # 应用原名
        self.app_orig_name = app_orig_name
        # 任务标签
        self.labels = labels
        # 任务名称
        self.name = name
        # 应用版本号
        self.revision = revision
        # 任务ID
        self.run_id = run_id
        # 任务状态
        self.status = status
        # 提交时间
        self.create_time = create_time
        # 开始时间
        self.start_time = start_time
        # 结束时间
        self.end_time = end_time
        # 提交ID
        self.submission_id = submission_id
        # 实体名称
        self.entity_name = entity_name
        # 实体对象ID
        self.entity_type = entity_type
        # 运行目录
        self.execute_directory = execute_directory
        self.execute_options = execute_options
        # 输入参数
        self.inputs = inputs
        self.default_runtime = default_runtime
        self.workspace = workspace
        self.region_id = region_id

    def validate(self):
        if self.execute_options:
            self.execute_options.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.source is not None:
            result['Source'] = self.source
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.app_orig_name is not None:
            result['AppOrigName'] = self.app_orig_name
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.name is not None:
            result['Name'] = self.name
        if self.revision is not None:
            result['Revision'] = self.revision
        if self.run_id is not None:
            result['RunId'] = self.run_id
        if self.status is not None:
            result['Status'] = self.status
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.submission_id is not None:
            result['SubmissionId'] = self.submission_id
        if self.entity_name is not None:
            result['EntityName'] = self.entity_name
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.execute_directory is not None:
            result['ExecuteDirectory'] = self.execute_directory
        if self.execute_options is not None:
            result['ExecuteOptions'] = self.execute_options.to_map()
        if self.inputs is not None:
            result['Inputs'] = self.inputs
        if self.default_runtime is not None:
            result['DefaultRuntime'] = self.default_runtime
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('AppOrigName') is not None:
            self.app_orig_name = m.get('AppOrigName')
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Revision') is not None:
            self.revision = m.get('Revision')
        if m.get('RunId') is not None:
            self.run_id = m.get('RunId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('SubmissionId') is not None:
            self.submission_id = m.get('SubmissionId')
        if m.get('EntityName') is not None:
            self.entity_name = m.get('EntityName')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('ExecuteDirectory') is not None:
            self.execute_directory = m.get('ExecuteDirectory')
        if m.get('ExecuteOptions') is not None:
            temp_model = ListUserActiveRunsResponseBodyRunsExecuteOptions()
            self.execute_options = temp_model.from_map(m['ExecuteOptions'])
        if m.get('Inputs') is not None:
            self.inputs = m.get('Inputs')
        if m.get('DefaultRuntime') is not None:
            self.default_runtime = m.get('DefaultRuntime')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListUserActiveRunsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        host_id: str = None,
        max_results: int = None,
        next_token: str = None,
        total_count: int = None,
        runs: List[ListUserActiveRunsResponseBodyRuns] = None,
    ):
        # 请求ID
        self.request_id = request_id
        # 主机ID
        self.host_id = host_id
        # 最大返回结果
        self.max_results = max_results
        # 下次查询Token
        self.next_token = next_token
        # 返回个数
        self.total_count = total_count
        # 任务列表
        self.runs = runs

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
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['Runs'] = []
        if self.runs is not None:
            for k in self.runs:
                result['Runs'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.runs = []
        if m.get('Runs') is not None:
            for k in m.get('Runs'):
                temp_model = ListUserActiveRunsResponseBodyRuns()
                self.runs.append(temp_model.from_map(k))
        return self


class ListUserActiveRunsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListUserActiveRunsResponseBody = None,
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
            temp_model = ListUserActiveRunsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListWorkspacesRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        order_by: str = None,
        is_reversed: bool = None,
        next_token: str = None,
        max_results: int = None,
        label_selector: str = None,
    ):
        self.name = name
        self.order_by = order_by
        self.is_reversed = is_reversed
        self.next_token = next_token
        self.max_results = max_results
        # Label选择器
        self.label_selector = label_selector

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.order_by is not None:
            result['OrderBy'] = self.order_by
        if self.is_reversed is not None:
            result['IsReversed'] = self.is_reversed
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.label_selector is not None:
            result['LabelSelector'] = self.label_selector
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')
        if m.get('IsReversed') is not None:
            self.is_reversed = m.get('IsReversed')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('LabelSelector') is not None:
            self.label_selector = m.get('LabelSelector')
        return self


class ListWorkspacesResponseBodyWorkspaces(TeaModel):
    def __init__(
        self,
        description: str = None,
        job_lifecycle: int = None,
        labels: Dict[str, str] = None,
        oss_root: str = None,
        bucket_name: str = None,
        role: str = None,
        create_time: str = None,
        last_modified_time: str = None,
        workspace: str = None,
        status: str = None,
        region_id: str = None,
    ):
        # 工作空间描述
        self.description = description
        # 任务生命周期
        self.job_lifecycle = job_lifecycle
        # 工作空间标签
        self.labels = labels
        # OSS工作路径
        self.oss_root = oss_root
        # 工作空间Bucket名字
        self.bucket_name = bucket_name
        # RAM Role
        self.role = role
        # 创建时间
        self.create_time = create_time
        # 最后修改时间
        self.last_modified_time = last_modified_time
        # 工作空间名称
        self.workspace = workspace
        # 工作空间状态
        self.status = status
        # 地域ID
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.job_lifecycle is not None:
            result['JobLifecycle'] = self.job_lifecycle
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.oss_root is not None:
            result['OssRoot'] = self.oss_root
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.role is not None:
            result['Role'] = self.role
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.last_modified_time is not None:
            result['LastModifiedTime'] = self.last_modified_time
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        if self.status is not None:
            result['Status'] = self.status
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('JobLifecycle') is not None:
            self.job_lifecycle = m.get('JobLifecycle')
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('OssRoot') is not None:
            self.oss_root = m.get('OssRoot')
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('LastModifiedTime') is not None:
            self.last_modified_time = m.get('LastModifiedTime')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListWorkspacesResponseBody(TeaModel):
    def __init__(
        self,
        host_id: str = None,
        max_results: int = None,
        request_id: str = None,
        next_token: str = None,
        total_count: int = None,
        workspaces: List[ListWorkspacesResponseBodyWorkspaces] = None,
    ):
        # 主机ID
        self.host_id = host_id
        # 最大结果数
        self.max_results = max_results
        self.request_id = request_id
        # 下次查询的起始Token
        self.next_token = next_token
        # 返回总个数
        self.total_count = total_count
        # 工作空间数组
        self.workspaces = workspaces

    def validate(self):
        if self.workspaces:
            for k in self.workspaces:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['Workspaces'] = []
        if self.workspaces is not None:
            for k in self.workspaces:
                result['Workspaces'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.workspaces = []
        if m.get('Workspaces') is not None:
            for k in m.get('Workspaces'):
                temp_model = ListWorkspacesResponseBodyWorkspaces()
                self.workspaces.append(temp_model.from_map(k))
        return self


class ListWorkspacesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListWorkspacesResponseBody = None,
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
            temp_model = ListWorkspacesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ParseAppInputsRequestDependencies(TeaModel):
    def __init__(
        self,
        path: str = None,
        content: str = None,
    ):
        # 依赖路径
        self.path = path
        # 依赖内容
        self.content = content

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.path is not None:
            result['Path'] = self.path
        if self.content is not None:
            result['Content'] = self.content
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        return self


class ParseAppInputsRequest(TeaModel):
    def __init__(
        self,
        workspace: str = None,
        app_name: str = None,
        path: str = None,
        definition: str = None,
        dependencies: List[ParseAppInputsRequestDependencies] = None,
    ):
        # 工作空间名称
        self.workspace = workspace
        # 应用名称
        self.app_name = app_name
        # 文件路径
        self.path = path
        # 应用定义
        self.definition = definition
        # 依赖应用
        self.dependencies = dependencies

    def validate(self):
        if self.dependencies:
            for k in self.dependencies:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.path is not None:
            result['Path'] = self.path
        if self.definition is not None:
            result['Definition'] = self.definition
        result['Dependencies'] = []
        if self.dependencies is not None:
            for k in self.dependencies:
                result['Dependencies'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Definition') is not None:
            self.definition = m.get('Definition')
        self.dependencies = []
        if m.get('Dependencies') is not None:
            for k in m.get('Dependencies'):
                temp_model = ParseAppInputsRequestDependencies()
                self.dependencies.append(temp_model.from_map(k))
        return self


class ParseAppInputsShrinkRequest(TeaModel):
    def __init__(
        self,
        workspace: str = None,
        app_name: str = None,
        path: str = None,
        definition: str = None,
        dependencies_shrink: str = None,
    ):
        # 工作空间名称
        self.workspace = workspace
        # 应用名称
        self.app_name = app_name
        # 文件路径
        self.path = path
        # 应用定义
        self.definition = definition
        # 依赖应用
        self.dependencies_shrink = dependencies_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.path is not None:
            result['Path'] = self.path
        if self.definition is not None:
            result['Definition'] = self.definition
        if self.dependencies_shrink is not None:
            result['Dependencies'] = self.dependencies_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Definition') is not None:
            self.definition = m.get('Definition')
        if m.get('Dependencies') is not None:
            self.dependencies_shrink = m.get('Dependencies')
        return self


class ParseAppInputsResponseBodyInputs(TeaModel):
    def __init__(
        self,
        task_name: str = None,
        variable_name: str = None,
        variable_type: str = None,
        variable_value: str = None,
        required: bool = None,
        help: str = None,
        step_order: int = None,
    ):
        # 参数名称
        self.task_name = task_name
        self.variable_name = variable_name
        self.variable_type = variable_type
        self.variable_value = variable_value
        self.required = required
        self.help = help
        self.step_order = step_order

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.variable_name is not None:
            result['VariableName'] = self.variable_name
        if self.variable_type is not None:
            result['VariableType'] = self.variable_type
        if self.variable_value is not None:
            result['VariableValue'] = self.variable_value
        if self.required is not None:
            result['Required'] = self.required
        if self.help is not None:
            result['Help'] = self.help
        if self.step_order is not None:
            result['StepOrder'] = self.step_order
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('VariableName') is not None:
            self.variable_name = m.get('VariableName')
        if m.get('VariableType') is not None:
            self.variable_type = m.get('VariableType')
        if m.get('VariableValue') is not None:
            self.variable_value = m.get('VariableValue')
        if m.get('Required') is not None:
            self.required = m.get('Required')
        if m.get('Help') is not None:
            self.help = m.get('Help')
        if m.get('StepOrder') is not None:
            self.step_order = m.get('StepOrder')
        return self


class ParseAppInputsResponseBody(TeaModel):
    def __init__(
        self,
        host_id: str = None,
        request_id: str = None,
        inputs: List[ParseAppInputsResponseBodyInputs] = None,
    ):
        # 主机 ID
        self.host_id = host_id
        # 请求 ID
        self.request_id = request_id
        # 应用输入参数
        self.inputs = inputs

    def validate(self):
        if self.inputs:
            for k in self.inputs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Inputs'] = []
        if self.inputs is not None:
            for k in self.inputs:
                result['Inputs'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.inputs = []
        if m.get('Inputs') is not None:
            for k in m.get('Inputs'):
                temp_model = ParseAppInputsResponseBodyInputs()
                self.inputs.append(temp_model.from_map(k))
        return self


class ParseAppInputsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ParseAppInputsResponseBody = None,
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
            temp_model = ParseAppInputsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResumeSubmissionRequest(TeaModel):
    def __init__(
        self,
        workspace: str = None,
        submission_id: str = None,
    ):
        # 工作空间名称
        self.workspace = workspace
        # 投递ID
        self.submission_id = submission_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        if self.submission_id is not None:
            result['SubmissionId'] = self.submission_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        if m.get('SubmissionId') is not None:
            self.submission_id = m.get('SubmissionId')
        return self


class ResumeSubmissionResponseBody(TeaModel):
    def __init__(
        self,
        host_id: str = None,
        request_id: str = None,
    ):
        # 主机ID
        self.host_id = host_id
        # 请求ID
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ResumeSubmissionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ResumeSubmissionResponseBody = None,
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
            temp_model = ResumeSubmissionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateEntityRequestEntityItems(TeaModel):
    def __init__(
        self,
        entity_name: str = None,
        entity_data: Dict[str, str] = None,
    ):
        self.entity_name = entity_name
        self.entity_data = entity_data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entity_name is not None:
            result['EntityName'] = self.entity_name
        if self.entity_data is not None:
            result['EntityData'] = self.entity_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EntityName') is not None:
            self.entity_name = m.get('EntityName')
        if m.get('EntityData') is not None:
            self.entity_data = m.get('EntityData')
        return self


class UpdateEntityRequest(TeaModel):
    def __init__(
        self,
        workspace: str = None,
        entity_type: str = None,
        entity_items: List[UpdateEntityRequestEntityItems] = None,
    ):
        self.workspace = workspace
        self.entity_type = entity_type
        self.entity_items = entity_items

    def validate(self):
        if self.entity_items:
            for k in self.entity_items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        result['EntityItems'] = []
        if self.entity_items is not None:
            for k in self.entity_items:
                result['EntityItems'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        self.entity_items = []
        if m.get('EntityItems') is not None:
            for k in m.get('EntityItems'):
                temp_model = UpdateEntityRequestEntityItems()
                self.entity_items.append(temp_model.from_map(k))
        return self


class UpdateEntityShrinkRequest(TeaModel):
    def __init__(
        self,
        workspace: str = None,
        entity_type: str = None,
        entity_items_shrink: str = None,
    ):
        self.workspace = workspace
        self.entity_type = entity_type
        self.entity_items_shrink = entity_items_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.entity_items_shrink is not None:
            result['EntityItems'] = self.entity_items_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('EntityItems') is not None:
            self.entity_items_shrink = m.get('EntityItems')
        return self


class UpdateEntityResponseBody(TeaModel):
    def __init__(
        self,
        host_id: str = None,
        request_id: str = None,
        workspace: str = None,
        entity_type: str = None,
    ):
        # 主机ID
        self.host_id = host_id
        # 请求ID
        self.request_id = request_id
        self.workspace = workspace
        self.entity_type = entity_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        return self


class UpdateEntityResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateEntityResponseBody = None,
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
            temp_model = UpdateEntityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateTemplateRequestInputs(TeaModel):
    def __init__(
        self,
        task_name: str = None,
        variable_name: str = None,
        variable_type: str = None,
        variable_value: str = None,
        required: bool = None,
        help: str = None,
        step_order: int = None,
    ):
        # 任务名称
        self.task_name = task_name
        # 变量名
        self.variable_name = variable_name
        # 变量类型
        self.variable_type = variable_type
        # 变量值
        self.variable_value = variable_value
        # 是否必填
        self.required = required
        # 帮助信息
        self.help = help
        # 步骤顺序
        self.step_order = step_order

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.variable_name is not None:
            result['VariableName'] = self.variable_name
        if self.variable_type is not None:
            result['VariableType'] = self.variable_type
        if self.variable_value is not None:
            result['VariableValue'] = self.variable_value
        if self.required is not None:
            result['Required'] = self.required
        if self.help is not None:
            result['Help'] = self.help
        if self.step_order is not None:
            result['StepOrder'] = self.step_order
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('VariableName') is not None:
            self.variable_name = m.get('VariableName')
        if m.get('VariableType') is not None:
            self.variable_type = m.get('VariableType')
        if m.get('VariableValue') is not None:
            self.variable_value = m.get('VariableValue')
        if m.get('Required') is not None:
            self.required = m.get('Required')
        if m.get('Help') is not None:
            self.help = m.get('Help')
        if m.get('StepOrder') is not None:
            self.step_order = m.get('StepOrder')
        return self


class UpdateTemplateRequestOutputs(TeaModel):
    def __init__(
        self,
        task_name: str = None,
        variable_name: str = None,
        variable_type: str = None,
        variable_value: str = None,
        required: bool = None,
        help: str = None,
        step_order: int = None,
    ):
        # 任务名称
        self.task_name = task_name
        # 变量名
        self.variable_name = variable_name
        # 变量类型
        self.variable_type = variable_type
        # 变量值
        self.variable_value = variable_value
        # 是否必填
        self.required = required
        # 帮助信息
        self.help = help
        # 步骤顺序
        self.step_order = step_order

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.variable_name is not None:
            result['VariableName'] = self.variable_name
        if self.variable_type is not None:
            result['VariableType'] = self.variable_type
        if self.variable_value is not None:
            result['VariableValue'] = self.variable_value
        if self.required is not None:
            result['Required'] = self.required
        if self.help is not None:
            result['Help'] = self.help
        if self.step_order is not None:
            result['StepOrder'] = self.step_order
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('VariableName') is not None:
            self.variable_name = m.get('VariableName')
        if m.get('VariableType') is not None:
            self.variable_type = m.get('VariableType')
        if m.get('VariableValue') is not None:
            self.variable_value = m.get('VariableValue')
        if m.get('Required') is not None:
            self.required = m.get('Required')
        if m.get('Help') is not None:
            self.help = m.get('Help')
        if m.get('StepOrder') is not None:
            self.step_order = m.get('StepOrder')
        return self


class UpdateTemplateRequest(TeaModel):
    def __init__(
        self,
        workspace: str = None,
        template_name: str = None,
        description: str = None,
        root_entity: str = None,
        inputs: List[UpdateTemplateRequestInputs] = None,
        outputs: List[UpdateTemplateRequestOutputs] = None,
        labels: str = None,
    ):
        # 工作空间名称
        self.workspace = workspace
        # 应用模板名称
        self.template_name = template_name
        # 工作空间描述
        self.description = description
        # 实体类型
        self.root_entity = root_entity
        # 应用的输入
        self.inputs = inputs
        # 应用的输出
        self.outputs = outputs
        # 工作空间标签
        self.labels = labels

    def validate(self):
        if self.inputs:
            for k in self.inputs:
                if k:
                    k.validate()
        if self.outputs:
            for k in self.outputs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.description is not None:
            result['Description'] = self.description
        if self.root_entity is not None:
            result['RootEntity'] = self.root_entity
        result['Inputs'] = []
        if self.inputs is not None:
            for k in self.inputs:
                result['Inputs'].append(k.to_map() if k else None)
        result['Outputs'] = []
        if self.outputs is not None:
            for k in self.outputs:
                result['Outputs'].append(k.to_map() if k else None)
        if self.labels is not None:
            result['Labels'] = self.labels
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('RootEntity') is not None:
            self.root_entity = m.get('RootEntity')
        self.inputs = []
        if m.get('Inputs') is not None:
            for k in m.get('Inputs'):
                temp_model = UpdateTemplateRequestInputs()
                self.inputs.append(temp_model.from_map(k))
        self.outputs = []
        if m.get('Outputs') is not None:
            for k in m.get('Outputs'):
                temp_model = UpdateTemplateRequestOutputs()
                self.outputs.append(temp_model.from_map(k))
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        return self


class UpdateTemplateShrinkRequest(TeaModel):
    def __init__(
        self,
        workspace: str = None,
        template_name: str = None,
        description: str = None,
        root_entity: str = None,
        inputs_shrink: str = None,
        outputs_shrink: str = None,
        labels: str = None,
    ):
        # 工作空间名称
        self.workspace = workspace
        # 应用模板名称
        self.template_name = template_name
        # 工作空间描述
        self.description = description
        # 实体类型
        self.root_entity = root_entity
        # 应用的输入
        self.inputs_shrink = inputs_shrink
        # 应用的输出
        self.outputs_shrink = outputs_shrink
        # 工作空间标签
        self.labels = labels

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.description is not None:
            result['Description'] = self.description
        if self.root_entity is not None:
            result['RootEntity'] = self.root_entity
        if self.inputs_shrink is not None:
            result['Inputs'] = self.inputs_shrink
        if self.outputs_shrink is not None:
            result['Outputs'] = self.outputs_shrink
        if self.labels is not None:
            result['Labels'] = self.labels
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('RootEntity') is not None:
            self.root_entity = m.get('RootEntity')
        if m.get('Inputs') is not None:
            self.inputs_shrink = m.get('Inputs')
        if m.get('Outputs') is not None:
            self.outputs_shrink = m.get('Outputs')
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        return self


class UpdateTemplateResponseBody(TeaModel):
    def __init__(
        self,
        host_id: str = None,
        request_id: str = None,
    ):
        # 主机ID
        self.host_id = host_id
        # 请求ID
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateTemplateResponseBody = None,
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
            temp_model = UpdateTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateWorkspaceRequest(TeaModel):
    def __init__(
        self,
        workspace: str = None,
        description: str = None,
        oss_root: str = None,
        job_lifecycle: int = None,
        role: str = None,
        labels: str = None,
    ):
        # 工作空间名称
        self.workspace = workspace
        # 工作空间描述
        self.description = description
        # 工作空间OSS工作路径
        self.oss_root = oss_root
        # 工作空间内任务生命周期
        self.job_lifecycle = job_lifecycle
        # 工作空间内Ram角色
        self.role = role
        # 工作空间标签
        self.labels = labels

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        if self.description is not None:
            result['Description'] = self.description
        if self.oss_root is not None:
            result['OssRoot'] = self.oss_root
        if self.job_lifecycle is not None:
            result['JobLifecycle'] = self.job_lifecycle
        if self.role is not None:
            result['Role'] = self.role
        if self.labels is not None:
            result['Labels'] = self.labels
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('OssRoot') is not None:
            self.oss_root = m.get('OssRoot')
        if m.get('JobLifecycle') is not None:
            self.job_lifecycle = m.get('JobLifecycle')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        return self


class UpdateWorkspaceResponseBody(TeaModel):
    def __init__(
        self,
        host_id: str = None,
        request_id: str = None,
    ):
        # 主机ID
        self.host_id = host_id
        # 请求ID
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateWorkspaceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateWorkspaceResponseBody = None,
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
            temp_model = UpdateWorkspaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UploadEntityRequest(TeaModel):
    def __init__(
        self,
        workspace: str = None,
        entity_tsvfile: str = None,
    ):
        self.workspace = workspace
        self.entity_tsvfile = entity_tsvfile

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        if self.entity_tsvfile is not None:
            result['EntityTSVFile'] = self.entity_tsvfile
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        if m.get('EntityTSVFile') is not None:
            self.entity_tsvfile = m.get('EntityTSVFile')
        return self


class UploadEntityResponseBody(TeaModel):
    def __init__(
        self,
        host_id: str = None,
        request_id: str = None,
        workspace: str = None,
        entity_type: str = None,
    ):
        # 主机ID
        self.host_id = host_id
        # 请求ID
        self.request_id = request_id
        self.workspace = workspace
        self.entity_type = entity_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        return self


class UploadEntityResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UploadEntityResponseBody = None,
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
            temp_model = UploadEntityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


