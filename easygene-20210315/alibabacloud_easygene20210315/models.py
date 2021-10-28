# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class AbortRunRequest(TeaModel):
    def __init__(
        self,
        run_id: str = None,
        workspace: str = None,
    ):
        # 任务ID
        self.run_id = run_id
        # 工作空间名称
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.run_id is not None:
            result['RunId'] = self.run_id
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RunId') is not None:
            self.run_id = m.get('RunId')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
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
        submission_id: str = None,
        workspace: str = None,
    ):
        # 投递ID
        self.submission_id = submission_id
        # 工作空间名称
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.submission_id is not None:
            result['SubmissionId'] = self.submission_id
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SubmissionId') is not None:
            self.submission_id = m.get('SubmissionId')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
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


class CopyPublicEntityRequest(TeaModel):
    def __init__(
        self,
        dataset: str = None,
        entity_type: str = None,
        workspace: str = None,
    ):
        # 数据集名称
        self.dataset = dataset
        # 表格名称
        self.entity_type = entity_type
        # 要拷贝到的工作空间
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset is not None:
            result['Dataset'] = self.dataset
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Dataset') is not None:
            self.dataset = m.get('Dataset')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        return self


class CopyPublicEntityResponseBody(TeaModel):
    def __init__(
        self,
        entity_type: str = None,
        host_id: str = None,
        request_id: str = None,
        workspace: str = None,
    ):
        # 实体类型
        self.entity_type = entity_type
        # 主机ID
        self.host_id = host_id
        # 请求ID
        self.request_id = request_id
        # 工作空间
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        return self


class CopyPublicEntityResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CopyPublicEntityResponseBody = None,
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
            temp_model = CopyPublicEntityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAppRequestConfigs(TeaModel):
    def __init__(
        self,
        content: str = None,
        path: str = None,
    ):
        self.content = content
        self.path = path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.path is not None:
            result['Path'] = self.path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        return self


class CreateAppRequestDependencies(TeaModel):
    def __init__(
        self,
        content: str = None,
        path: str = None,
    ):
        # 依赖内容
        self.content = content
        # 依赖路径
        self.path = path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.path is not None:
            result['Path'] = self.path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        return self


class CreateAppRequest(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        app_type: str = None,
        client_token: str = None,
        configs: List[CreateAppRequestConfigs] = None,
        definition: str = None,
        dependencies: List[CreateAppRequestDependencies] = None,
        description: str = None,
        documentation: str = None,
        labels: str = None,
        language: str = None,
        language_version: str = None,
        path: str = None,
        revision_comment: str = None,
        workspace: str = None,
    ):
        # 应用名称
        self.app_name = app_name
        # 应用类型
        self.app_type = app_type
        # 幂等Token
        self.client_token = client_token
        # 参考输入
        self.configs = configs
        # 应用定义
        self.definition = definition
        # 依赖应用
        self.dependencies = dependencies
        # 应用描述
        self.description = description
        # 应用使用文档
        self.documentation = documentation
        # 应用标签
        self.labels = labels
        # 应用描述语言
        self.language = language
        # 应用描述语语言版本
        self.language_version = language_version
        # 主WDL路径
        self.path = path
        # 应用当前版本说明
        self.revision_comment = revision_comment
        # 工作空间名称
        self.workspace = workspace

    def validate(self):
        if self.configs:
            for k in self.configs:
                if k:
                    k.validate()
        if self.dependencies:
            for k in self.dependencies:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_type is not None:
            result['AppType'] = self.app_type
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        result['Configs'] = []
        if self.configs is not None:
            for k in self.configs:
                result['Configs'].append(k.to_map() if k else None)
        if self.definition is not None:
            result['Definition'] = self.definition
        result['Dependencies'] = []
        if self.dependencies is not None:
            for k in self.dependencies:
                result['Dependencies'].append(k.to_map() if k else None)
        if self.description is not None:
            result['Description'] = self.description
        if self.documentation is not None:
            result['Documentation'] = self.documentation
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.language is not None:
            result['Language'] = self.language
        if self.language_version is not None:
            result['LanguageVersion'] = self.language_version
        if self.path is not None:
            result['Path'] = self.path
        if self.revision_comment is not None:
            result['RevisionComment'] = self.revision_comment
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        self.configs = []
        if m.get('Configs') is not None:
            for k in m.get('Configs'):
                temp_model = CreateAppRequestConfigs()
                self.configs.append(temp_model.from_map(k))
        if m.get('Definition') is not None:
            self.definition = m.get('Definition')
        self.dependencies = []
        if m.get('Dependencies') is not None:
            for k in m.get('Dependencies'):
                temp_model = CreateAppRequestDependencies()
                self.dependencies.append(temp_model.from_map(k))
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Documentation') is not None:
            self.documentation = m.get('Documentation')
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('LanguageVersion') is not None:
            self.language_version = m.get('LanguageVersion')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('RevisionComment') is not None:
            self.revision_comment = m.get('RevisionComment')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        return self


class CreateAppShrinkRequest(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        app_type: str = None,
        client_token: str = None,
        configs_shrink: str = None,
        definition: str = None,
        dependencies_shrink: str = None,
        description: str = None,
        documentation: str = None,
        labels: str = None,
        language: str = None,
        language_version: str = None,
        path: str = None,
        revision_comment: str = None,
        workspace: str = None,
    ):
        # 应用名称
        self.app_name = app_name
        # 应用类型
        self.app_type = app_type
        # 幂等Token
        self.client_token = client_token
        # 参考输入
        self.configs_shrink = configs_shrink
        # 应用定义
        self.definition = definition
        # 依赖应用
        self.dependencies_shrink = dependencies_shrink
        # 应用描述
        self.description = description
        # 应用使用文档
        self.documentation = documentation
        # 应用标签
        self.labels = labels
        # 应用描述语言
        self.language = language
        # 应用描述语语言版本
        self.language_version = language_version
        # 主WDL路径
        self.path = path
        # 应用当前版本说明
        self.revision_comment = revision_comment
        # 工作空间名称
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_type is not None:
            result['AppType'] = self.app_type
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.configs_shrink is not None:
            result['Configs'] = self.configs_shrink
        if self.definition is not None:
            result['Definition'] = self.definition
        if self.dependencies_shrink is not None:
            result['Dependencies'] = self.dependencies_shrink
        if self.description is not None:
            result['Description'] = self.description
        if self.documentation is not None:
            result['Documentation'] = self.documentation
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.language is not None:
            result['Language'] = self.language
        if self.language_version is not None:
            result['LanguageVersion'] = self.language_version
        if self.path is not None:
            result['Path'] = self.path
        if self.revision_comment is not None:
            result['RevisionComment'] = self.revision_comment
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Configs') is not None:
            self.configs_shrink = m.get('Configs')
        if m.get('Definition') is not None:
            self.definition = m.get('Definition')
        if m.get('Dependencies') is not None:
            self.dependencies_shrink = m.get('Dependencies')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Documentation') is not None:
            self.documentation = m.get('Documentation')
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('LanguageVersion') is not None:
            self.language_version = m.get('LanguageVersion')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('RevisionComment') is not None:
            self.revision_comment = m.get('RevisionComment')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        return self


class CreateAppResponseBody(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        host_id: str = None,
        request_id: str = None,
        revision: str = None,
        workspace: str = None,
    ):
        # 应用名称
        self.app_name = app_name
        # 主机 ID
        self.host_id = host_id
        # 请求 ID
        self.request_id = request_id
        # 应用版本号
        self.revision = revision
        # 工作空间
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.revision is not None:
            result['Revision'] = self.revision
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Revision') is not None:
            self.revision = m.get('Revision')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
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
        entity_data: Dict[str, str] = None,
        entity_name: str = None,
    ):
        self.entity_data = entity_data
        # 表格元素名称
        self.entity_name = entity_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entity_data is not None:
            result['EntityData'] = self.entity_data
        if self.entity_name is not None:
            result['EntityName'] = self.entity_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EntityData') is not None:
            self.entity_data = m.get('EntityData')
        if m.get('EntityName') is not None:
            self.entity_name = m.get('EntityName')
        return self


class CreateEntityRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        entity_items: List[CreateEntityRequestEntityItems] = None,
        entity_type: str = None,
        workspace: str = None,
    ):
        # 幂等Token
        self.client_token = client_token
        self.entity_items = entity_items
        # 实体类型
        self.entity_type = entity_type
        # 工作空间
        self.workspace = workspace

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
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        result['EntityItems'] = []
        if self.entity_items is not None:
            for k in self.entity_items:
                result['EntityItems'].append(k.to_map() if k else None)
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        self.entity_items = []
        if m.get('EntityItems') is not None:
            for k in m.get('EntityItems'):
                temp_model = CreateEntityRequestEntityItems()
                self.entity_items.append(temp_model.from_map(k))
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        return self


class CreateEntityShrinkRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        entity_items_shrink: str = None,
        entity_type: str = None,
        workspace: str = None,
    ):
        # 幂等Token
        self.client_token = client_token
        self.entity_items_shrink = entity_items_shrink
        # 实体类型
        self.entity_type = entity_type
        # 工作空间
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.entity_items_shrink is not None:
            result['EntityItems'] = self.entity_items_shrink
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('EntityItems') is not None:
            self.entity_items_shrink = m.get('EntityItems')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        return self


class CreateEntityResponseBody(TeaModel):
    def __init__(
        self,
        entity_type: str = None,
        host_id: str = None,
        request_id: str = None,
        workspace: str = None,
    ):
        # 实体类型
        self.entity_type = entity_type
        # 主机ID
        self.host_id = host_id
        # 请求ID
        self.request_id = request_id
        # 工作空间
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
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


class CreateRunRequestExecuteOptions(TeaModel):
    def __init__(
        self,
        call_caching: bool = None,
        delete_intermediate_results: bool = None,
        failure_mode: str = None,
        use_relative_output_paths: bool = None,
    ):
        # 使用缓存
        self.call_caching = call_caching
        # 删除中间结果
        self.delete_intermediate_results = delete_intermediate_results
        # 失败模式
        self.failure_mode = failure_mode
        # 使用相对输出路径
        self.use_relative_output_paths = use_relative_output_paths

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
        if self.use_relative_output_paths is not None:
            result['UseRelativeOutputPaths'] = self.use_relative_output_paths
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallCaching') is not None:
            self.call_caching = m.get('CallCaching')
        if m.get('DeleteIntermediateResults') is not None:
            self.delete_intermediate_results = m.get('DeleteIntermediateResults')
        if m.get('FailureMode') is not None:
            self.failure_mode = m.get('FailureMode')
        if m.get('UseRelativeOutputPaths') is not None:
            self.use_relative_output_paths = m.get('UseRelativeOutputPaths')
        return self


class CreateRunRequest(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        app_revision: str = None,
        client_token: str = None,
        default_runtime: str = None,
        description: str = None,
        execute_directory: str = None,
        execute_options: CreateRunRequestExecuteOptions = None,
        inputs: str = None,
        labels: str = None,
        output_folder: str = None,
        run_name: str = None,
        workspace: str = None,
    ):
        # 应用名称
        self.app_name = app_name
        # 应用版本号
        self.app_revision = app_revision
        # 任务幂等token
        self.client_token = client_token
        # 默认运行时
        self.default_runtime = default_runtime
        # 任务描述
        self.description = description
        # 任务执行目录
        self.execute_directory = execute_directory
        # 任务配置
        self.execute_options = execute_options
        # 任务输入
        self.inputs = inputs
        # 任务标签
        self.labels = labels
        # 任务输出拷贝目录
        self.output_folder = output_folder
        # 任务名称
        self.run_name = run_name
        # 工作空间名字
        self.workspace = workspace

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
        if self.app_revision is not None:
            result['AppRevision'] = self.app_revision
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.default_runtime is not None:
            result['DefaultRuntime'] = self.default_runtime
        if self.description is not None:
            result['Description'] = self.description
        if self.execute_directory is not None:
            result['ExecuteDirectory'] = self.execute_directory
        if self.execute_options is not None:
            result['ExecuteOptions'] = self.execute_options.to_map()
        if self.inputs is not None:
            result['Inputs'] = self.inputs
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.output_folder is not None:
            result['OutputFolder'] = self.output_folder
        if self.run_name is not None:
            result['RunName'] = self.run_name
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppRevision') is not None:
            self.app_revision = m.get('AppRevision')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DefaultRuntime') is not None:
            self.default_runtime = m.get('DefaultRuntime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ExecuteDirectory') is not None:
            self.execute_directory = m.get('ExecuteDirectory')
        if m.get('ExecuteOptions') is not None:
            temp_model = CreateRunRequestExecuteOptions()
            self.execute_options = temp_model.from_map(m['ExecuteOptions'])
        if m.get('Inputs') is not None:
            self.inputs = m.get('Inputs')
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('OutputFolder') is not None:
            self.output_folder = m.get('OutputFolder')
        if m.get('RunName') is not None:
            self.run_name = m.get('RunName')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        return self


class CreateRunShrinkRequest(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        app_revision: str = None,
        client_token: str = None,
        default_runtime: str = None,
        description: str = None,
        execute_directory: str = None,
        execute_options_shrink: str = None,
        inputs: str = None,
        labels: str = None,
        output_folder: str = None,
        run_name: str = None,
        workspace: str = None,
    ):
        # 应用名称
        self.app_name = app_name
        # 应用版本号
        self.app_revision = app_revision
        # 任务幂等token
        self.client_token = client_token
        # 默认运行时
        self.default_runtime = default_runtime
        # 任务描述
        self.description = description
        # 任务执行目录
        self.execute_directory = execute_directory
        # 任务配置
        self.execute_options_shrink = execute_options_shrink
        # 任务输入
        self.inputs = inputs
        # 任务标签
        self.labels = labels
        # 任务输出拷贝目录
        self.output_folder = output_folder
        # 任务名称
        self.run_name = run_name
        # 工作空间名字
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_revision is not None:
            result['AppRevision'] = self.app_revision
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.default_runtime is not None:
            result['DefaultRuntime'] = self.default_runtime
        if self.description is not None:
            result['Description'] = self.description
        if self.execute_directory is not None:
            result['ExecuteDirectory'] = self.execute_directory
        if self.execute_options_shrink is not None:
            result['ExecuteOptions'] = self.execute_options_shrink
        if self.inputs is not None:
            result['Inputs'] = self.inputs
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.output_folder is not None:
            result['OutputFolder'] = self.output_folder
        if self.run_name is not None:
            result['RunName'] = self.run_name
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppRevision') is not None:
            self.app_revision = m.get('AppRevision')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DefaultRuntime') is not None:
            self.default_runtime = m.get('DefaultRuntime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ExecuteDirectory') is not None:
            self.execute_directory = m.get('ExecuteDirectory')
        if m.get('ExecuteOptions') is not None:
            self.execute_options_shrink = m.get('ExecuteOptions')
        if m.get('Inputs') is not None:
            self.inputs = m.get('Inputs')
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('OutputFolder') is not None:
            self.output_folder = m.get('OutputFolder')
        if m.get('RunName') is not None:
            self.run_name = m.get('RunName')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        return self


class CreateRunResponseBody(TeaModel):
    def __init__(
        self,
        host_id: str = None,
        request_id: str = None,
        run_id: str = None,
        workspace: str = None,
    ):
        # 主机ID
        self.host_id = host_id
        # 请求ID
        self.request_id = request_id
        # 任务ID
        self.run_id = run_id
        # 工作空间
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
        if self.run_id is not None:
            result['RunId'] = self.run_id
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RunId') is not None:
            self.run_id = m.get('RunId')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
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
        app_name: str = None,
        client_token: str = None,
        default_runtime: str = None,
        entity_names: List[str] = None,
        entity_type: str = None,
        execute_directory: str = None,
        execute_options: str = None,
        inputs: str = None,
        output_folder: str = None,
        outputs: str = None,
        revision: str = None,
        workspace: str = None,
    ):
        # 应用名称
        self.app_name = app_name
        # 任务幂等token
        self.client_token = client_token
        # 默认运行时
        self.default_runtime = default_runtime
        self.entity_names = entity_names
        # 实体类型
        self.entity_type = entity_type
        # 任务执行目录
        self.execute_directory = execute_directory
        # 任务配置
        self.execute_options = execute_options
        # 任务输入
        self.inputs = inputs
        # 任务输出拷贝目录
        self.output_folder = output_folder
        # 任务输出
        self.outputs = outputs
        # 应用版本号
        self.revision = revision
        # 工作空间名字
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.default_runtime is not None:
            result['DefaultRuntime'] = self.default_runtime
        if self.entity_names is not None:
            result['EntityNames'] = self.entity_names
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.execute_directory is not None:
            result['ExecuteDirectory'] = self.execute_directory
        if self.execute_options is not None:
            result['ExecuteOptions'] = self.execute_options
        if self.inputs is not None:
            result['Inputs'] = self.inputs
        if self.output_folder is not None:
            result['OutputFolder'] = self.output_folder
        if self.outputs is not None:
            result['Outputs'] = self.outputs
        if self.revision is not None:
            result['Revision'] = self.revision
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DefaultRuntime') is not None:
            self.default_runtime = m.get('DefaultRuntime')
        if m.get('EntityNames') is not None:
            self.entity_names = m.get('EntityNames')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('ExecuteDirectory') is not None:
            self.execute_directory = m.get('ExecuteDirectory')
        if m.get('ExecuteOptions') is not None:
            self.execute_options = m.get('ExecuteOptions')
        if m.get('Inputs') is not None:
            self.inputs = m.get('Inputs')
        if m.get('OutputFolder') is not None:
            self.output_folder = m.get('OutputFolder')
        if m.get('Outputs') is not None:
            self.outputs = m.get('Outputs')
        if m.get('Revision') is not None:
            self.revision = m.get('Revision')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        return self


class CreateSubmissionShrinkRequest(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        client_token: str = None,
        default_runtime: str = None,
        entity_names_shrink: str = None,
        entity_type: str = None,
        execute_directory: str = None,
        execute_options: str = None,
        inputs: str = None,
        output_folder: str = None,
        outputs: str = None,
        revision: str = None,
        workspace: str = None,
    ):
        # 应用名称
        self.app_name = app_name
        # 任务幂等token
        self.client_token = client_token
        # 默认运行时
        self.default_runtime = default_runtime
        self.entity_names_shrink = entity_names_shrink
        # 实体类型
        self.entity_type = entity_type
        # 任务执行目录
        self.execute_directory = execute_directory
        # 任务配置
        self.execute_options = execute_options
        # 任务输入
        self.inputs = inputs
        # 任务输出拷贝目录
        self.output_folder = output_folder
        # 任务输出
        self.outputs = outputs
        # 应用版本号
        self.revision = revision
        # 工作空间名字
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.default_runtime is not None:
            result['DefaultRuntime'] = self.default_runtime
        if self.entity_names_shrink is not None:
            result['EntityNames'] = self.entity_names_shrink
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.execute_directory is not None:
            result['ExecuteDirectory'] = self.execute_directory
        if self.execute_options is not None:
            result['ExecuteOptions'] = self.execute_options
        if self.inputs is not None:
            result['Inputs'] = self.inputs
        if self.output_folder is not None:
            result['OutputFolder'] = self.output_folder
        if self.outputs is not None:
            result['Outputs'] = self.outputs
        if self.revision is not None:
            result['Revision'] = self.revision
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DefaultRuntime') is not None:
            self.default_runtime = m.get('DefaultRuntime')
        if m.get('EntityNames') is not None:
            self.entity_names_shrink = m.get('EntityNames')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('ExecuteDirectory') is not None:
            self.execute_directory = m.get('ExecuteDirectory')
        if m.get('ExecuteOptions') is not None:
            self.execute_options = m.get('ExecuteOptions')
        if m.get('Inputs') is not None:
            self.inputs = m.get('Inputs')
        if m.get('OutputFolder') is not None:
            self.output_folder = m.get('OutputFolder')
        if m.get('Outputs') is not None:
            self.outputs = m.get('Outputs')
        if m.get('Revision') is not None:
            self.revision = m.get('Revision')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        return self


class CreateSubmissionResponseBody(TeaModel):
    def __init__(
        self,
        host_id: str = None,
        request_id: str = None,
        submission_id: str = None,
        workspace: str = None,
    ):
        # 主机ID
        self.host_id = host_id
        # 请求ID
        self.request_id = request_id
        # 投递ID
        self.submission_id = submission_id
        # 工作空间
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
        if self.submission_id is not None:
            result['SubmissionId'] = self.submission_id
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SubmissionId') is not None:
            self.submission_id = m.get('SubmissionId')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
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


class CreateTemplateRequestInputsExpression(TeaModel):
    def __init__(
        self,
        help: str = None,
        required: bool = None,
        step_order: int = None,
        task_name: str = None,
        variable_name: str = None,
        variable_type: str = None,
        variable_value: str = None,
    ):
        # 帮助信息
        self.help = help
        # 是否必填
        self.required = required
        # 步骤顺序
        self.step_order = step_order
        # 任务名称
        self.task_name = task_name
        # 变量名
        self.variable_name = variable_name
        # 变量类型
        self.variable_type = variable_type
        # 变量值
        self.variable_value = variable_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.help is not None:
            result['Help'] = self.help
        if self.required is not None:
            result['Required'] = self.required
        if self.step_order is not None:
            result['StepOrder'] = self.step_order
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.variable_name is not None:
            result['VariableName'] = self.variable_name
        if self.variable_type is not None:
            result['VariableType'] = self.variable_type
        if self.variable_value is not None:
            result['VariableValue'] = self.variable_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Help') is not None:
            self.help = m.get('Help')
        if m.get('Required') is not None:
            self.required = m.get('Required')
        if m.get('StepOrder') is not None:
            self.step_order = m.get('StepOrder')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('VariableName') is not None:
            self.variable_name = m.get('VariableName')
        if m.get('VariableType') is not None:
            self.variable_type = m.get('VariableType')
        if m.get('VariableValue') is not None:
            self.variable_value = m.get('VariableValue')
        return self


class CreateTemplateRequestOutputsExpression(TeaModel):
    def __init__(
        self,
        help: str = None,
        required: bool = None,
        step_order: int = None,
        task_name: str = None,
        variable_name: str = None,
        variable_type: str = None,
        variable_value: str = None,
    ):
        # 帮助信息
        self.help = help
        # 是否必填
        self.required = required
        # 步骤顺序
        self.step_order = step_order
        # 任务名称
        self.task_name = task_name
        # 变量名
        self.variable_name = variable_name
        # 变量类型
        self.variable_type = variable_type
        # 变量值
        self.variable_value = variable_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.help is not None:
            result['Help'] = self.help
        if self.required is not None:
            result['Required'] = self.required
        if self.step_order is not None:
            result['StepOrder'] = self.step_order
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.variable_name is not None:
            result['VariableName'] = self.variable_name
        if self.variable_type is not None:
            result['VariableType'] = self.variable_type
        if self.variable_value is not None:
            result['VariableValue'] = self.variable_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Help') is not None:
            self.help = m.get('Help')
        if m.get('Required') is not None:
            self.required = m.get('Required')
        if m.get('StepOrder') is not None:
            self.step_order = m.get('StepOrder')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('VariableName') is not None:
            self.variable_name = m.get('VariableName')
        if m.get('VariableType') is not None:
            self.variable_type = m.get('VariableType')
        if m.get('VariableValue') is not None:
            self.variable_value = m.get('VariableValue')
        return self


class CreateTemplateRequest(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        app_revision: str = None,
        client_token: str = None,
        description: str = None,
        inputs_expression: List[CreateTemplateRequestInputsExpression] = None,
        labels: str = None,
        outputs_expression: List[CreateTemplateRequestOutputsExpression] = None,
        root_entity: str = None,
        template_name: str = None,
        workspace: str = None,
    ):
        # 应用的名称
        self.app_name = app_name
        # 应用的版本
        self.app_revision = app_revision
        # 幂等Token
        self.client_token = client_token
        # 应用模板描述
        self.description = description
        # 应用的输入
        self.inputs_expression = inputs_expression
        # 应用标签
        self.labels = labels
        # 应用的输出
        self.outputs_expression = outputs_expression
        # 根实体类型
        self.root_entity = root_entity
        # 应用模板名称
        self.template_name = template_name
        # 工作空间名称
        self.workspace = workspace

    def validate(self):
        if self.inputs_expression:
            for k in self.inputs_expression:
                if k:
                    k.validate()
        if self.outputs_expression:
            for k in self.outputs_expression:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_revision is not None:
            result['AppRevision'] = self.app_revision
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        result['InputsExpression'] = []
        if self.inputs_expression is not None:
            for k in self.inputs_expression:
                result['InputsExpression'].append(k.to_map() if k else None)
        if self.labels is not None:
            result['Labels'] = self.labels
        result['OutputsExpression'] = []
        if self.outputs_expression is not None:
            for k in self.outputs_expression:
                result['OutputsExpression'].append(k.to_map() if k else None)
        if self.root_entity is not None:
            result['RootEntity'] = self.root_entity
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppRevision') is not None:
            self.app_revision = m.get('AppRevision')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        self.inputs_expression = []
        if m.get('InputsExpression') is not None:
            for k in m.get('InputsExpression'):
                temp_model = CreateTemplateRequestInputsExpression()
                self.inputs_expression.append(temp_model.from_map(k))
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        self.outputs_expression = []
        if m.get('OutputsExpression') is not None:
            for k in m.get('OutputsExpression'):
                temp_model = CreateTemplateRequestOutputsExpression()
                self.outputs_expression.append(temp_model.from_map(k))
        if m.get('RootEntity') is not None:
            self.root_entity = m.get('RootEntity')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        return self


class CreateTemplateShrinkRequest(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        app_revision: str = None,
        client_token: str = None,
        description: str = None,
        inputs_expression_shrink: str = None,
        labels: str = None,
        outputs_expression_shrink: str = None,
        root_entity: str = None,
        template_name: str = None,
        workspace: str = None,
    ):
        # 应用的名称
        self.app_name = app_name
        # 应用的版本
        self.app_revision = app_revision
        # 幂等Token
        self.client_token = client_token
        # 应用模板描述
        self.description = description
        # 应用的输入
        self.inputs_expression_shrink = inputs_expression_shrink
        # 应用标签
        self.labels = labels
        # 应用的输出
        self.outputs_expression_shrink = outputs_expression_shrink
        # 根实体类型
        self.root_entity = root_entity
        # 应用模板名称
        self.template_name = template_name
        # 工作空间名称
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_revision is not None:
            result['AppRevision'] = self.app_revision
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        if self.inputs_expression_shrink is not None:
            result['InputsExpression'] = self.inputs_expression_shrink
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.outputs_expression_shrink is not None:
            result['OutputsExpression'] = self.outputs_expression_shrink
        if self.root_entity is not None:
            result['RootEntity'] = self.root_entity
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppRevision') is not None:
            self.app_revision = m.get('AppRevision')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('InputsExpression') is not None:
            self.inputs_expression_shrink = m.get('InputsExpression')
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('OutputsExpression') is not None:
            self.outputs_expression_shrink = m.get('OutputsExpression')
        if m.get('RootEntity') is not None:
            self.root_entity = m.get('RootEntity')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        return self


class CreateTemplateResponseBody(TeaModel):
    def __init__(
        self,
        host_id: str = None,
        request_id: str = None,
        template_name: str = None,
        workspace: str = None,
    ):
        # 主机 ID
        self.host_id = host_id
        # 请求 ID
        self.request_id = request_id
        # 应用模板名称
        self.template_name = template_name
        # 工作空间名称
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
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
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
        client_token: str = None,
        description: str = None,
        job_lifecycle: int = None,
        labels: str = None,
        role: str = None,
        storage: str = None,
        workspace: str = None,
    ):
        # 幂等Token
        self.client_token = client_token
        # 工作空间描述
        self.description = description
        # 工作空间任务生命周期
        self.job_lifecycle = job_lifecycle
        # 工作空间标签
        self.labels = labels
        # 工作空间内的ram角色
        self.role = role
        # 工作空间的OSS工作路径
        self.storage = storage
        # 工作空间名称
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        if self.job_lifecycle is not None:
            result['JobLifecycle'] = self.job_lifecycle
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.role is not None:
            result['Role'] = self.role
        if self.storage is not None:
            result['Storage'] = self.storage
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('JobLifecycle') is not None:
            self.job_lifecycle = m.get('JobLifecycle')
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('Storage') is not None:
            self.storage = m.get('Storage')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
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
        app_name: str = None,
        revision: str = None,
        workspace: str = None,
    ):
        # 应用名称
        self.app_name = app_name
        # 应用版本
        self.revision = revision
        # 工作空间名称
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.revision is not None:
            result['Revision'] = self.revision
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Revision') is not None:
            self.revision = m.get('Revision')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
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
        entity_names: List[str] = None,
        entity_type: str = None,
        workspace: str = None,
    ):
        self.entity_names = entity_names
        # 实体类型
        self.entity_type = entity_type
        # 工作空间
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entity_names is not None:
            result['EntityNames'] = self.entity_names
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EntityNames') is not None:
            self.entity_names = m.get('EntityNames')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        return self


class DeleteEntityItemsShrinkRequest(TeaModel):
    def __init__(
        self,
        entity_names_shrink: str = None,
        entity_type: str = None,
        workspace: str = None,
    ):
        self.entity_names_shrink = entity_names_shrink
        # 实体类型
        self.entity_type = entity_type
        # 工作空间
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entity_names_shrink is not None:
            result['EntityNames'] = self.entity_names_shrink
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EntityNames') is not None:
            self.entity_names_shrink = m.get('EntityNames')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        return self


class DeleteEntityItemsResponseBody(TeaModel):
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
        run_id: str = None,
        workspace: str = None,
    ):
        # 任务ID
        self.run_id = run_id
        # 工作空间名称
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.run_id is not None:
            result['RunId'] = self.run_id
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RunId') is not None:
            self.run_id = m.get('RunId')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
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
        submission_id: str = None,
        workspace: str = None,
    ):
        # 投递ID
        self.submission_id = submission_id
        # 工作空间名称
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.submission_id is not None:
            result['SubmissionId'] = self.submission_id
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SubmissionId') is not None:
            self.submission_id = m.get('SubmissionId')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
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
        template_name: str = None,
        workspace: str = None,
    ):
        # 应用模板名称
        self.template_name = template_name
        # 工作空间名称
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
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
        entity_names: List[str] = None,
        entity_type: str = None,
        workspace: str = None,
    ):
        self.entity_names = entity_names
        # 实体类型
        self.entity_type = entity_type
        # 工作空间
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entity_names is not None:
            result['EntityNames'] = self.entity_names
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EntityNames') is not None:
            self.entity_names = m.get('EntityNames')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        return self


class DownloadEntityShrinkRequest(TeaModel):
    def __init__(
        self,
        entity_names_shrink: str = None,
        entity_type: str = None,
        workspace: str = None,
    ):
        self.entity_names_shrink = entity_names_shrink
        # 实体类型
        self.entity_type = entity_type
        # 工作空间
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entity_names_shrink is not None:
            result['EntityNames'] = self.entity_names_shrink
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EntityNames') is not None:
            self.entity_names_shrink = m.get('EntityNames')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        return self


class DownloadEntityResponseBody(TeaModel):
    def __init__(
        self,
        entity_csvfile: str = None,
        host_id: str = None,
        request_id: str = None,
    ):
        # 下载的表格文件URL
        self.entity_csvfile = entity_csvfile
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
        if self.entity_csvfile is not None:
            result['EntityCSVFile'] = self.entity_csvfile
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EntityCSVFile') is not None:
            self.entity_csvfile = m.get('EntityCSVFile')
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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
        app_name: str = None,
        revision: str = None,
        workspace: str = None,
    ):
        # 应用名称
        self.app_name = app_name
        # 应用版本号
        self.revision = revision
        # 工作空间名称
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.revision is not None:
            result['Revision'] = self.revision
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Revision') is not None:
            self.revision = m.get('Revision')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        return self


class GetAppResponseBodyConfigs(TeaModel):
    def __init__(
        self,
        content: str = None,
        path: str = None,
    ):
        self.content = content
        self.path = path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.path is not None:
            result['Path'] = self.path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        return self


class GetAppResponseBodyDependencies(TeaModel):
    def __init__(
        self,
        content: str = None,
        path: str = None,
    ):
        # wdl内容
        self.content = content
        # 依赖路径
        self.path = path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.path is not None:
            result['Path'] = self.path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        return self


class GetAppResponseBodyInputs(TeaModel):
    def __init__(
        self,
        help: str = None,
        required: bool = None,
        step_order: int = None,
        task_name: str = None,
        variable_name: str = None,
        variable_type: str = None,
        variable_value: str = None,
    ):
        # 帮助
        self.help = help
        # 是否必须
        self.required = required
        # 步骤顺序
        self.step_order = step_order
        # 任务名称
        self.task_name = task_name
        # 变量名称
        self.variable_name = variable_name
        # 变量类型
        self.variable_type = variable_type
        # 变量值
        self.variable_value = variable_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.help is not None:
            result['Help'] = self.help
        if self.required is not None:
            result['Required'] = self.required
        if self.step_order is not None:
            result['StepOrder'] = self.step_order
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.variable_name is not None:
            result['VariableName'] = self.variable_name
        if self.variable_type is not None:
            result['VariableType'] = self.variable_type
        if self.variable_value is not None:
            result['VariableValue'] = self.variable_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Help') is not None:
            self.help = m.get('Help')
        if m.get('Required') is not None:
            self.required = m.get('Required')
        if m.get('StepOrder') is not None:
            self.step_order = m.get('StepOrder')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('VariableName') is not None:
            self.variable_name = m.get('VariableName')
        if m.get('VariableType') is not None:
            self.variable_type = m.get('VariableType')
        if m.get('VariableValue') is not None:
            self.variable_value = m.get('VariableValue')
        return self


class GetAppResponseBodyOutputs(TeaModel):
    def __init__(
        self,
        help: str = None,
        required: bool = None,
        step_order: int = None,
        task_name: str = None,
        variable_name: str = None,
        variable_type: str = None,
        variable_value: str = None,
    ):
        # 帮助信息
        self.help = help
        # 是否必须
        self.required = required
        # 步骤编号
        self.step_order = step_order
        # 任务名称
        self.task_name = task_name
        # 参数名称
        self.variable_name = variable_name
        # 参数类型
        self.variable_type = variable_type
        # 参数值
        self.variable_value = variable_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.help is not None:
            result['Help'] = self.help
        if self.required is not None:
            result['Required'] = self.required
        if self.step_order is not None:
            result['StepOrder'] = self.step_order
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.variable_name is not None:
            result['VariableName'] = self.variable_name
        if self.variable_type is not None:
            result['VariableType'] = self.variable_type
        if self.variable_value is not None:
            result['VariableValue'] = self.variable_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Help') is not None:
            self.help = m.get('Help')
        if m.get('Required') is not None:
            self.required = m.get('Required')
        if m.get('StepOrder') is not None:
            self.step_order = m.get('StepOrder')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('VariableName') is not None:
            self.variable_name = m.get('VariableName')
        if m.get('VariableType') is not None:
            self.variable_type = m.get('VariableType')
        if m.get('VariableValue') is not None:
            self.variable_value = m.get('VariableValue')
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
        # 应用当前版本修改
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


class GetAppResponseBody(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        app_type: str = None,
        configs: List[GetAppResponseBodyConfigs] = None,
        create_time: str = None,
        definition: str = None,
        dependencies: List[GetAppResponseBodyDependencies] = None,
        description: str = None,
        documentation: str = None,
        host_id: str = None,
        inputs: List[GetAppResponseBodyInputs] = None,
        labels: Dict[str, str] = None,
        language: str = None,
        language_version: str = None,
        last_modified_time: str = None,
        outputs: List[GetAppResponseBodyOutputs] = None,
        path: str = None,
        request_id: str = None,
        revision: str = None,
        revision_comment: str = None,
        revisions: List[GetAppResponseBodyRevisions] = None,
        scope: str = None,
        source: str = None,
        url: str = None,
        workflow_name: str = None,
        workspace: str = None,
    ):
        # 应用名称
        self.app_name = app_name
        # 实体类型
        self.app_type = app_type
        # 参考输入
        self.configs = configs
        # 创建时间
        self.create_time = create_time
        # 应用定义
        self.definition = definition
        # 依赖应用
        self.dependencies = dependencies
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
        # 主WDL路径
        self.path = path
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
        # 应用来源
        self.source = source
        # 应用URL
        self.url = url
        # 工作流名称
        self.workflow_name = workflow_name
        # 工作空间名称
        self.workspace = workspace

    def validate(self):
        if self.configs:
            for k in self.configs:
                if k:
                    k.validate()
        if self.dependencies:
            for k in self.dependencies:
                if k:
                    k.validate()
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

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_type is not None:
            result['AppType'] = self.app_type
        result['Configs'] = []
        if self.configs is not None:
            for k in self.configs:
                result['Configs'].append(k.to_map() if k else None)
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.definition is not None:
            result['Definition'] = self.definition
        result['Dependencies'] = []
        if self.dependencies is not None:
            for k in self.dependencies:
                result['Dependencies'].append(k.to_map() if k else None)
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
        if self.path is not None:
            result['Path'] = self.path
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
        if self.source is not None:
            result['Source'] = self.source
        if self.url is not None:
            result['URL'] = self.url
        if self.workflow_name is not None:
            result['WorkflowName'] = self.workflow_name
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')
        self.configs = []
        if m.get('Configs') is not None:
            for k in m.get('Configs'):
                temp_model = GetAppResponseBodyConfigs()
                self.configs.append(temp_model.from_map(k))
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Definition') is not None:
            self.definition = m.get('Definition')
        self.dependencies = []
        if m.get('Dependencies') is not None:
            for k in m.get('Dependencies'):
                temp_model = GetAppResponseBodyDependencies()
                self.dependencies.append(temp_model.from_map(k))
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
        if m.get('Path') is not None:
            self.path = m.get('Path')
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
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('URL') is not None:
            self.url = m.get('URL')
        if m.get('WorkflowName') is not None:
            self.workflow_name = m.get('WorkflowName')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
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
        entity_type: str = None,
        workspace: str = None,
    ):
        # 实体类型
        self.entity_type = entity_type
        # 工作空间
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        return self


class GetEntityResponseBody(TeaModel):
    def __init__(
        self,
        attributes: List[str] = None,
        entity_type: str = None,
        host_id: str = None,
        request_id: str = None,
        total_count: int = None,
        workspace: str = None,
    ):
        # 属性列数组
        self.attributes = attributes
        # 实体类型
        self.entity_type = entity_type
        # 主机ID
        self.host_id = host_id
        # 请求ID
        self.request_id = request_id
        # 实体元素总个数
        self.total_count = total_count
        # 工作空间
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attributes is not None:
            result['Attributes'] = self.attributes
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Attributes') is not None:
            self.attributes = m.get('Attributes')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
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
        app_name: str = None,
        app_version: str = None,
        attributes: List[str] = None,
        location: str = None,
        namespace_name: str = None,
    ):
        # 应用名称
        self.app_name = app_name
        # 应用版本
        self.app_version = app_version
        # 查询字段信息：appVersions，regionIds，dag
        self.attributes = attributes
        # 应用可用区域
        self.location = location
        # 命名空间
        self.namespace_name = namespace_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_version is not None:
            result['AppVersion'] = self.app_version
        if self.attributes is not None:
            result['Attributes'] = self.attributes
        if self.location is not None:
            result['Location'] = self.location
        if self.namespace_name is not None:
            result['NamespaceName'] = self.namespace_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')
        if m.get('Attributes') is not None:
            self.attributes = m.get('Attributes')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('NamespaceName') is not None:
            self.namespace_name = m.get('NamespaceName')
        return self


class GetGlobalAppShrinkRequest(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        app_version: str = None,
        attributes_shrink: str = None,
        location: str = None,
        namespace_name: str = None,
    ):
        # 应用名称
        self.app_name = app_name
        # 应用版本
        self.app_version = app_version
        # 查询字段信息：appVersions，regionIds，dag
        self.attributes_shrink = attributes_shrink
        # 应用可用区域
        self.location = location
        # 命名空间
        self.namespace_name = namespace_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_version is not None:
            result['AppVersion'] = self.app_version
        if self.attributes_shrink is not None:
            result['Attributes'] = self.attributes_shrink
        if self.location is not None:
            result['Location'] = self.location
        if self.namespace_name is not None:
            result['NamespaceName'] = self.namespace_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')
        if m.get('Attributes') is not None:
            self.attributes_shrink = m.get('Attributes')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('NamespaceName') is not None:
            self.namespace_name = m.get('NamespaceName')
        return self


class GetGlobalAppResponseBodyAppDescriptorFiles(TeaModel):
    def __init__(
        self,
        checksum: str = None,
        content: str = None,
        file_type: str = None,
        path: str = None,
        url: str = None,
    ):
        # 应用文件内容的完整性校验码，如MD5值
        self.checksum = checksum
        # 应用文件内容
        self.content = content
        # 应用文件的类型
        self.file_type = file_type
        # 应用文件的路径，除PRIMARY_DESCRIPTOR外，其他均为相对于PRIMARY_DESCRIPTOR的相对路径
        self.path = path
        # 应用文件链接
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.checksum is not None:
            result['Checksum'] = self.checksum
        if self.content is not None:
            result['Content'] = self.content
        if self.file_type is not None:
            result['FileType'] = self.file_type
        if self.path is not None:
            result['Path'] = self.path
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Checksum') is not None:
            self.checksum = m.get('Checksum')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Url') is not None:
            self.url = m.get('Url')
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


class GetGlobalAppResponseBody(TeaModel):
    def __init__(
        self,
        app_default_version: str = None,
        app_description: str = None,
        app_descriptor_files: List[GetGlobalAppResponseBodyAppDescriptorFiles] = None,
        app_descriptor_type: str = None,
        app_fee: str = None,
        app_name: str = None,
        app_scope: str = None,
        app_type: str = None,
        app_version: str = None,
        app_versions: List[GetGlobalAppResponseBodyAppVersions] = None,
        categories: List[str] = None,
        comment: str = None,
        contact: str = None,
        dag: str = None,
        document: str = None,
        host_id: str = None,
        last_modified: str = None,
        links: List[str] = None,
        locations: List[str] = None,
        namespace_name: str = None,
        pinned: bool = None,
        request_id: str = None,
        toolkit: str = None,
    ):
        # 默认版本
        self.app_default_version = app_default_version
        # 应用描述
        self.app_description = app_description
        # 应用的描述文件内容
        self.app_descriptor_files = app_descriptor_files
        # 应用描述语言标准
        self.app_descriptor_type = app_descriptor_type
        # 应用计费说明
        self.app_fee = app_fee
        # 应用名称
        self.app_name = app_name
        # 应用权限
        self.app_scope = app_scope
        # 应用类型
        self.app_type = app_type
        # 应用版本
        self.app_version = app_version
        # 应用的所有版本列表
        self.app_versions = app_versions
        # 应用所属分类
        self.categories = categories
        # 应用的备注信息
        self.comment = comment
        # 应用联系人信息
        self.contact = contact
        # 应用的DAG信息
        self.dag = dag
        # 应用的帮助文档
        self.document = document
        # 主机ID
        self.host_id = host_id
        # 更新时间
        self.last_modified = last_modified
        # 应用主页信息
        self.links = links
        # 应用支持的区域
        self.locations = locations
        # 命名空间名称
        self.namespace_name = namespace_name
        # 应用收藏置顶标记
        self.pinned = pinned
        # 请求ID
        self.request_id = request_id
        # 应用所属工具合集
        self.toolkit = toolkit

    def validate(self):
        if self.app_descriptor_files:
            for k in self.app_descriptor_files:
                if k:
                    k.validate()
        if self.app_versions:
            for k in self.app_versions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_default_version is not None:
            result['AppDefaultVersion'] = self.app_default_version
        if self.app_description is not None:
            result['AppDescription'] = self.app_description
        result['AppDescriptorFiles'] = []
        if self.app_descriptor_files is not None:
            for k in self.app_descriptor_files:
                result['AppDescriptorFiles'].append(k.to_map() if k else None)
        if self.app_descriptor_type is not None:
            result['AppDescriptorType'] = self.app_descriptor_type
        if self.app_fee is not None:
            result['AppFee'] = self.app_fee
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_scope is not None:
            result['AppScope'] = self.app_scope
        if self.app_type is not None:
            result['AppType'] = self.app_type
        if self.app_version is not None:
            result['AppVersion'] = self.app_version
        result['AppVersions'] = []
        if self.app_versions is not None:
            for k in self.app_versions:
                result['AppVersions'].append(k.to_map() if k else None)
        if self.categories is not None:
            result['Categories'] = self.categories
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.contact is not None:
            result['Contact'] = self.contact
        if self.dag is not None:
            result['DAG'] = self.dag
        if self.document is not None:
            result['Document'] = self.document
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.last_modified is not None:
            result['LastModified'] = self.last_modified
        if self.links is not None:
            result['Links'] = self.links
        if self.locations is not None:
            result['Locations'] = self.locations
        if self.namespace_name is not None:
            result['NamespaceName'] = self.namespace_name
        if self.pinned is not None:
            result['Pinned'] = self.pinned
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.toolkit is not None:
            result['Toolkit'] = self.toolkit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppDefaultVersion') is not None:
            self.app_default_version = m.get('AppDefaultVersion')
        if m.get('AppDescription') is not None:
            self.app_description = m.get('AppDescription')
        self.app_descriptor_files = []
        if m.get('AppDescriptorFiles') is not None:
            for k in m.get('AppDescriptorFiles'):
                temp_model = GetGlobalAppResponseBodyAppDescriptorFiles()
                self.app_descriptor_files.append(temp_model.from_map(k))
        if m.get('AppDescriptorType') is not None:
            self.app_descriptor_type = m.get('AppDescriptorType')
        if m.get('AppFee') is not None:
            self.app_fee = m.get('AppFee')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppScope') is not None:
            self.app_scope = m.get('AppScope')
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')
        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')
        self.app_versions = []
        if m.get('AppVersions') is not None:
            for k in m.get('AppVersions'):
                temp_model = GetGlobalAppResponseBodyAppVersions()
                self.app_versions.append(temp_model.from_map(k))
        if m.get('Categories') is not None:
            self.categories = m.get('Categories')
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('Contact') is not None:
            self.contact = m.get('Contact')
        if m.get('DAG') is not None:
            self.dag = m.get('DAG')
        if m.get('Document') is not None:
            self.document = m.get('Document')
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('LastModified') is not None:
            self.last_modified = m.get('LastModified')
        if m.get('Links') is not None:
            self.links = m.get('Links')
        if m.get('Locations') is not None:
            self.locations = m.get('Locations')
        if m.get('NamespaceName') is not None:
            self.namespace_name = m.get('NamespaceName')
        if m.get('Pinned') is not None:
            self.pinned = m.get('Pinned')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Toolkit') is not None:
            self.toolkit = m.get('Toolkit')
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
        attributes: List[str] = None,
        dataset_name: str = None,
    ):
        # 查询的字段名:DatasetNo, DatasetDescription, About, AccessRequirements, Copyright, Tags, UpdateFrequency, Locations, LastModified, RegionIds
        self.attributes = attributes
        # 数据集名称
        self.dataset_name = dataset_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attributes is not None:
            result['Attributes'] = self.attributes
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Attributes') is not None:
            self.attributes = m.get('Attributes')
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        return self


class GetPublicDatasetShrinkRequest(TeaModel):
    def __init__(
        self,
        attributes_shrink: str = None,
        dataset_name: str = None,
    ):
        # 查询的字段名:DatasetNo, DatasetDescription, About, AccessRequirements, Copyright, Tags, UpdateFrequency, Locations, LastModified, RegionIds
        self.attributes_shrink = attributes_shrink
        # 数据集名称
        self.dataset_name = dataset_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attributes_shrink is not None:
            result['Attributes'] = self.attributes_shrink
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Attributes') is not None:
            self.attributes_shrink = m.get('Attributes')
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        return self


class GetPublicDatasetResponseBody(TeaModel):
    def __init__(
        self,
        about: str = None,
        access_requirements: str = None,
        copyright: str = None,
        dataset_description: str = None,
        dataset_name: str = None,
        host_id: str = None,
        last_modified: str = None,
        locations: List[str] = None,
        request_id: str = None,
        tags: List[str] = None,
        update_frequency: str = None,
    ):
        # 关于公共数据集
        self.about = about
        # 公共数据集访问要求
        self.access_requirements = access_requirements
        # 公共数据集版权信息
        self.copyright = copyright
        # 公共数据集描述
        self.dataset_description = dataset_description
        # 公共数据集名称
        self.dataset_name = dataset_name
        # 主机ID
        self.host_id = host_id
        # 最后更新时间
        self.last_modified = last_modified
        # 公共数据集可用区域
        self.locations = locations
        # 请求ID
        self.request_id = request_id
        # 公共数据集标签
        self.tags = tags
        # 公共数据集更新频率
        self.update_frequency = update_frequency

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.about is not None:
            result['About'] = self.about
        if self.access_requirements is not None:
            result['AccessRequirements'] = self.access_requirements
        if self.copyright is not None:
            result['Copyright'] = self.copyright
        if self.dataset_description is not None:
            result['DatasetDescription'] = self.dataset_description
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.last_modified is not None:
            result['LastModified'] = self.last_modified
        if self.locations is not None:
            result['Locations'] = self.locations
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.update_frequency is not None:
            result['UpdateFrequency'] = self.update_frequency
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('About') is not None:
            self.about = m.get('About')
        if m.get('AccessRequirements') is not None:
            self.access_requirements = m.get('AccessRequirements')
        if m.get('Copyright') is not None:
            self.copyright = m.get('Copyright')
        if m.get('DatasetDescription') is not None:
            self.dataset_description = m.get('DatasetDescription')
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('LastModified') is not None:
            self.last_modified = m.get('LastModified')
        if m.get('Locations') is not None:
            self.locations = m.get('Locations')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('UpdateFrequency') is not None:
            self.update_frequency = m.get('UpdateFrequency')
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
        location: str = None,
    ):
        # 数据集名称
        self.dataset_name = dataset_name
        # 实体类型
        self.entity_type = entity_type
        # 公共数据集所在区域
        self.location = location

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
        if self.location is not None:
            result['Location'] = self.location
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        return self


class GetPublicDatasetEntityResponseBody(TeaModel):
    def __init__(
        self,
        attributes: List[str] = None,
        dataset_name: str = None,
        entity_type: str = None,
        host_id: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # 实体属性名称列表
        self.attributes = attributes
        # 公共数据集名称
        self.dataset_name = dataset_name
        # 实体类型
        self.entity_type = entity_type
        # 主机ID
        self.host_id = host_id
        # 请求ID
        self.request_id = request_id
        # 该类型实体总数
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attributes is not None:
            result['Attributes'] = self.attributes
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Attributes') is not None:
            self.attributes = m.get('Attributes')
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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
        run_id: str = None,
        workspace: str = None,
    ):
        # 任务ID
        self.run_id = run_id
        # 工作空间名字
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.run_id is not None:
            result['RunId'] = self.run_id
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RunId') is not None:
            self.run_id = m.get('RunId')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        return self


class GetRunResponseBodyExecuteOptions(TeaModel):
    def __init__(
        self,
        call_caching: bool = None,
        delete_intermediate_results: bool = None,
        failure_mode: str = None,
        use_relative_output_paths: bool = None,
    ):
        # 是否开启CallCaching
        self.call_caching = call_caching
        # 是否删除中间文件
        self.delete_intermediate_results = delete_intermediate_results
        # 失败模式
        self.failure_mode = failure_mode
        # 相对输出路径
        self.use_relative_output_paths = use_relative_output_paths

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
        if self.use_relative_output_paths is not None:
            result['UseRelativeOutputPaths'] = self.use_relative_output_paths
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallCaching') is not None:
            self.call_caching = m.get('CallCaching')
        if m.get('DeleteIntermediateResults') is not None:
            self.delete_intermediate_results = m.get('DeleteIntermediateResults')
        if m.get('FailureMode') is not None:
            self.failure_mode = m.get('FailureMode')
        if m.get('UseRelativeOutputPaths') is not None:
            self.use_relative_output_paths = m.get('UseRelativeOutputPaths')
        return self


class GetRunResponseBody(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        app_revision: str = None,
        calls: str = None,
        create_time: str = None,
        default_runtime: str = None,
        description: str = None,
        end_time: str = None,
        entity_name: str = None,
        entity_type: str = None,
        execute_directory: str = None,
        execute_options: GetRunResponseBodyExecuteOptions = None,
        failures: str = None,
        host_id: str = None,
        inputs: str = None,
        labels: Dict[str, str] = None,
        output_folder: str = None,
        outputs: str = None,
        request_id: str = None,
        run_id: str = None,
        run_name: str = None,
        source: str = None,
        start_time: str = None,
        status: str = None,
        submission_id: str = None,
        timing: str = None,
        user: str = None,
        workspace: str = None,
    ):
        # 应用名称
        self.app_name = app_name
        # 应用版本
        self.app_revision = app_revision
        # 作业信息
        self.calls = calls
        # 提交时间
        self.create_time = create_time
        # 默认runtime值
        self.default_runtime = default_runtime
        # 任务描述
        self.description = description
        # 结束时间
        self.end_time = end_time
        # 实体对象名称
        self.entity_name = entity_name
        # 实体类型
        self.entity_type = entity_type
        # 任务执行目录
        self.execute_directory = execute_directory
        # 任务配置
        self.execute_options = execute_options
        # 错误信息
        self.failures = failures
        # 主机ID
        self.host_id = host_id
        # 任务输入
        self.inputs = inputs
        # 任务标签
        self.labels = labels
        # 输出拷贝目录
        self.output_folder = output_folder
        # 任务输出
        self.outputs = outputs
        # 请求ID
        self.request_id = request_id
        # 任务ID
        self.run_id = run_id
        # 任务名称
        self.run_name = run_name
        # 应用来源
        self.source = source
        # 开始时间
        self.start_time = start_time
        # 任务状态
        self.status = status
        # 提交ID
        self.submission_id = submission_id
        # 时序信息
        self.timing = timing
        # 用户ID
        self.user = user
        # 工作空间名字
        self.workspace = workspace

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
        if self.app_revision is not None:
            result['AppRevision'] = self.app_revision
        if self.calls is not None:
            result['Calls'] = self.calls
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.default_runtime is not None:
            result['DefaultRuntime'] = self.default_runtime
        if self.description is not None:
            result['Description'] = self.description
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.entity_name is not None:
            result['EntityName'] = self.entity_name
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.execute_directory is not None:
            result['ExecuteDirectory'] = self.execute_directory
        if self.execute_options is not None:
            result['ExecuteOptions'] = self.execute_options.to_map()
        if self.failures is not None:
            result['Failures'] = self.failures
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.inputs is not None:
            result['Inputs'] = self.inputs
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.output_folder is not None:
            result['OutputFolder'] = self.output_folder
        if self.outputs is not None:
            result['Outputs'] = self.outputs
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.run_id is not None:
            result['RunId'] = self.run_id
        if self.run_name is not None:
            result['RunName'] = self.run_name
        if self.source is not None:
            result['Source'] = self.source
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.submission_id is not None:
            result['SubmissionId'] = self.submission_id
        if self.timing is not None:
            result['Timing'] = self.timing
        if self.user is not None:
            result['User'] = self.user
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppRevision') is not None:
            self.app_revision = m.get('AppRevision')
        if m.get('Calls') is not None:
            self.calls = m.get('Calls')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DefaultRuntime') is not None:
            self.default_runtime = m.get('DefaultRuntime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('EntityName') is not None:
            self.entity_name = m.get('EntityName')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('ExecuteDirectory') is not None:
            self.execute_directory = m.get('ExecuteDirectory')
        if m.get('ExecuteOptions') is not None:
            temp_model = GetRunResponseBodyExecuteOptions()
            self.execute_options = temp_model.from_map(m['ExecuteOptions'])
        if m.get('Failures') is not None:
            self.failures = m.get('Failures')
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('Inputs') is not None:
            self.inputs = m.get('Inputs')
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('OutputFolder') is not None:
            self.output_folder = m.get('OutputFolder')
        if m.get('Outputs') is not None:
            self.outputs = m.get('Outputs')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RunId') is not None:
            self.run_id = m.get('RunId')
        if m.get('RunName') is not None:
            self.run_name = m.get('RunName')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubmissionId') is not None:
            self.submission_id = m.get('SubmissionId')
        if m.get('Timing') is not None:
            self.timing = m.get('Timing')
        if m.get('User') is not None:
            self.user = m.get('User')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
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
        submission_id: str = None,
        workspace: str = None,
    ):
        # 投递ID
        self.submission_id = submission_id
        # 工作空间
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.submission_id is not None:
            result['SubmissionId'] = self.submission_id
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SubmissionId') is not None:
            self.submission_id = m.get('SubmissionId')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        return self


class GetSubmissionResponseBodySubmissionRunStats(TeaModel):
    def __init__(
        self,
        aborted: int = None,
        aborting: int = None,
        failed: int = None,
        pending: int = None,
        running: int = None,
        submitted: int = None,
        succeeded: int = None,
    ):
        # 已取消数量
        self.aborted = aborted
        # 取消中数量
        self.aborting = aborting
        # 已失败数量
        self.failed = failed
        # 等待中数量
        self.pending = pending
        # 运行中数量
        self.running = running
        # 已提交数量
        self.submitted = submitted
        # 已成功数量
        self.succeeded = succeeded

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aborted is not None:
            result['Aborted'] = self.aborted
        if self.aborting is not None:
            result['Aborting'] = self.aborting
        if self.failed is not None:
            result['Failed'] = self.failed
        if self.pending is not None:
            result['Pending'] = self.pending
        if self.running is not None:
            result['Running'] = self.running
        if self.submitted is not None:
            result['Submitted'] = self.submitted
        if self.succeeded is not None:
            result['Succeeded'] = self.succeeded
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Aborted') is not None:
            self.aborted = m.get('Aborted')
        if m.get('Aborting') is not None:
            self.aborting = m.get('Aborting')
        if m.get('Failed') is not None:
            self.failed = m.get('Failed')
        if m.get('Pending') is not None:
            self.pending = m.get('Pending')
        if m.get('Running') is not None:
            self.running = m.get('Running')
        if m.get('Submitted') is not None:
            self.submitted = m.get('Submitted')
        if m.get('Succeeded') is not None:
            self.succeeded = m.get('Succeeded')
        return self


class GetSubmissionResponseBodySubmission(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        end_time: str = None,
        entity_type: str = None,
        run_stats: GetSubmissionResponseBodySubmissionRunStats = None,
        start_time: str = None,
        status: str = None,
        submission_id: str = None,
        workspace: str = None,
    ):
        # 提交时间
        self.create_time = create_time
        # 结束时间
        self.end_time = end_time
        # 实体类型
        self.entity_type = entity_type
        self.run_stats = run_stats
        # 开始时间
        self.start_time = start_time
        # 任务状态
        self.status = status
        # 提交ID
        self.submission_id = submission_id
        # 提交ID
        self.workspace = workspace

    def validate(self):
        if self.run_stats:
            self.run_stats.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.run_stats is not None:
            result['RunStats'] = self.run_stats.to_map()
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.submission_id is not None:
            result['SubmissionId'] = self.submission_id
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('RunStats') is not None:
            temp_model = GetSubmissionResponseBodySubmissionRunStats()
            self.run_stats = temp_model.from_map(m['RunStats'])
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubmissionId') is not None:
            self.submission_id = m.get('SubmissionId')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        return self


class GetSubmissionResponseBody(TeaModel):
    def __init__(
        self,
        host_id: str = None,
        request_id: str = None,
        submission: GetSubmissionResponseBodySubmission = None,
    ):
        # 主机ID
        self.host_id = host_id
        # 请求ID
        self.request_id = request_id
        # 投递详情
        self.submission = submission

    def validate(self):
        if self.submission:
            self.submission.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.submission is not None:
            result['Submission'] = self.submission.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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
        template_name: str = None,
        workspace: str = None,
    ):
        # 应用模板名称
        self.template_name = template_name
        # 工作空间名称
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        return self


class GetTemplateResponseBodyInputsExpression(TeaModel):
    def __init__(
        self,
        help: str = None,
        required: bool = None,
        step_order: int = None,
        task_name: str = None,
        variable_name: str = None,
        variable_type: str = None,
        variable_value: str = None,
    ):
        # 帮助信息
        self.help = help
        # 是否必须参数
        self.required = required
        # 步骤顺序
        self.step_order = step_order
        # 任务名称
        self.task_name = task_name
        # 变量名称
        self.variable_name = variable_name
        # 变量类型
        self.variable_type = variable_type
        # 变量值
        self.variable_value = variable_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.help is not None:
            result['Help'] = self.help
        if self.required is not None:
            result['Required'] = self.required
        if self.step_order is not None:
            result['StepOrder'] = self.step_order
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.variable_name is not None:
            result['VariableName'] = self.variable_name
        if self.variable_type is not None:
            result['VariableType'] = self.variable_type
        if self.variable_value is not None:
            result['VariableValue'] = self.variable_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Help') is not None:
            self.help = m.get('Help')
        if m.get('Required') is not None:
            self.required = m.get('Required')
        if m.get('StepOrder') is not None:
            self.step_order = m.get('StepOrder')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('VariableName') is not None:
            self.variable_name = m.get('VariableName')
        if m.get('VariableType') is not None:
            self.variable_type = m.get('VariableType')
        if m.get('VariableValue') is not None:
            self.variable_value = m.get('VariableValue')
        return self


class GetTemplateResponseBodyOutputsExpression(TeaModel):
    def __init__(
        self,
        help: str = None,
        required: bool = None,
        step_order: int = None,
        task_name: str = None,
        variable_name: str = None,
        variable_type: str = None,
        variable_value: str = None,
    ):
        # 帮助信息
        self.help = help
        # 是否必须参数
        self.required = required
        # 步骤顺序
        self.step_order = step_order
        # 任务名称
        self.task_name = task_name
        # 变量名称
        self.variable_name = variable_name
        # 变量类型
        self.variable_type = variable_type
        # 变量值
        self.variable_value = variable_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.help is not None:
            result['Help'] = self.help
        if self.required is not None:
            result['Required'] = self.required
        if self.step_order is not None:
            result['StepOrder'] = self.step_order
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.variable_name is not None:
            result['VariableName'] = self.variable_name
        if self.variable_type is not None:
            result['VariableType'] = self.variable_type
        if self.variable_value is not None:
            result['VariableValue'] = self.variable_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Help') is not None:
            self.help = m.get('Help')
        if m.get('Required') is not None:
            self.required = m.get('Required')
        if m.get('StepOrder') is not None:
            self.step_order = m.get('StepOrder')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('VariableName') is not None:
            self.variable_name = m.get('VariableName')
        if m.get('VariableType') is not None:
            self.variable_type = m.get('VariableType')
        if m.get('VariableValue') is not None:
            self.variable_value = m.get('VariableValue')
        return self


class GetTemplateResponseBody(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        app_revision: str = None,
        create_time: str = None,
        description: str = None,
        host_id: str = None,
        inputs_expression: List[GetTemplateResponseBodyInputsExpression] = None,
        labels: Dict[str, str] = None,
        last_modified_time: str = None,
        outputs_expression: List[GetTemplateResponseBodyOutputsExpression] = None,
        request_id: str = None,
        root_entity: str = None,
        source: str = None,
        template_name: str = None,
        workspace: str = None,
    ):
        # 应用的名称
        self.app_name = app_name
        # 应用的版本
        self.app_revision = app_revision
        # 创建时间
        self.create_time = create_time
        # 应用简要描述
        self.description = description
        # 主机ID
        self.host_id = host_id
        # 应用输入
        self.inputs_expression = inputs_expression
        # 应用标签
        self.labels = labels
        # 应用最后修改时间
        self.last_modified_time = last_modified_time
        # 应用的输出参数
        self.outputs_expression = outputs_expression
        # 请求ID
        self.request_id = request_id
        # 实体类型
        self.root_entity = root_entity
        # 应用来源
        self.source = source
        # 应用模板名称
        self.template_name = template_name
        # 工作空间名称
        self.workspace = workspace

    def validate(self):
        if self.inputs_expression:
            for k in self.inputs_expression:
                if k:
                    k.validate()
        if self.outputs_expression:
            for k in self.outputs_expression:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_revision is not None:
            result['AppRevision'] = self.app_revision
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.host_id is not None:
            result['HostId'] = self.host_id
        result['InputsExpression'] = []
        if self.inputs_expression is not None:
            for k in self.inputs_expression:
                result['InputsExpression'].append(k.to_map() if k else None)
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.last_modified_time is not None:
            result['LastModifiedTime'] = self.last_modified_time
        result['OutputsExpression'] = []
        if self.outputs_expression is not None:
            for k in self.outputs_expression:
                result['OutputsExpression'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.root_entity is not None:
            result['RootEntity'] = self.root_entity
        if self.source is not None:
            result['Source'] = self.source
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppRevision') is not None:
            self.app_revision = m.get('AppRevision')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        self.inputs_expression = []
        if m.get('InputsExpression') is not None:
            for k in m.get('InputsExpression'):
                temp_model = GetTemplateResponseBodyInputsExpression()
                self.inputs_expression.append(temp_model.from_map(k))
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('LastModifiedTime') is not None:
            self.last_modified_time = m.get('LastModifiedTime')
        self.outputs_expression = []
        if m.get('OutputsExpression') is not None:
            for k in m.get('OutputsExpression'):
                temp_model = GetTemplateResponseBodyOutputsExpression()
                self.outputs_expression.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RootEntity') is not None:
            self.root_entity = m.get('RootEntity')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
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
        # 工作空间名字
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
        bucket_name: str = None,
        create_time: str = None,
        description: str = None,
        host_id: str = None,
        job_lifecycle: int = None,
        labels: Dict[str, str] = None,
        last_modified_time: str = None,
        location: str = None,
        request_id: str = None,
        role: str = None,
        status: str = None,
        storage: str = None,
        workspace: str = None,
    ):
        # 工作空间Bucket
        self.bucket_name = bucket_name
        # 创建时间
        self.create_time = create_time
        # 工作空间简要描述
        self.description = description
        # 主机ID
        self.host_id = host_id
        # 工作空间内作业生命周期
        self.job_lifecycle = job_lifecycle
        # 工作空间标签
        self.labels = labels
        # 最后修改时间
        self.last_modified_time = last_modified_time
        # 地域ID
        self.location = location
        # 请求ID
        self.request_id = request_id
        # 工作空间内默认的RAM服务角色
        self.role = role
        # 工作空间状态
        self.status = status
        # 工作空间内OSS上的工作路径
        self.storage = storage
        # 工作空间名称
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.job_lifecycle is not None:
            result['JobLifecycle'] = self.job_lifecycle
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.last_modified_time is not None:
            result['LastModifiedTime'] = self.last_modified_time
        if self.location is not None:
            result['Location'] = self.location
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.role is not None:
            result['Role'] = self.role
        if self.status is not None:
            result['Status'] = self.status
        if self.storage is not None:
            result['Storage'] = self.storage
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('JobLifecycle') is not None:
            self.job_lifecycle = m.get('JobLifecycle')
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('LastModifiedTime') is not None:
            self.last_modified_time = m.get('LastModifiedTime')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Storage') is not None:
            self.storage = m.get('Storage')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
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


class ImportAppRequest(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        source: str = None,
        workspace: str = None,
    ):
        # 安装后应用名
        self.app_name = app_name
        # 来源
        self.source = source
        # 工作空间
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.source is not None:
            result['Source'] = self.source
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        return self


class ImportAppResponseBody(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        host_id: str = None,
        region_id: str = None,
        request_id: str = None,
        workspace: str = None,
    ):
        # 安装后应用名
        self.app_name = app_name
        # 主机 ID
        self.host_id = host_id
        # 区域名
        self.region_id = region_id
        # 请求 ID
        self.request_id = request_id
        # 工作空间
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        return self


class ImportAppResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ImportAppResponseBody = None,
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
            temp_model = ImportAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InstallGlobalAppRequest(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        installed_app_name: str = None,
        namespace_name: str = None,
        source: str = None,
        workspace: str = None,
    ):
        # 应用名称
        self.app_name = app_name
        # 安装后应用名
        self.installed_app_name = installed_app_name
        # 命名空间名称
        self.namespace_name = namespace_name
        # 来源
        self.source = source
        # 工作空间
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.installed_app_name is not None:
            result['InstalledAppName'] = self.installed_app_name
        if self.namespace_name is not None:
            result['NamespaceName'] = self.namespace_name
        if self.source is not None:
            result['Source'] = self.source
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('InstalledAppName') is not None:
            self.installed_app_name = m.get('InstalledAppName')
        if m.get('NamespaceName') is not None:
            self.namespace_name = m.get('NamespaceName')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        return self


class InstallGlobalAppResponseBody(TeaModel):
    def __init__(
        self,
        host_id: str = None,
        installed_app_name: str = None,
        region_id: str = None,
        request_id: str = None,
        workspace: str = None,
    ):
        # 主机 ID
        self.host_id = host_id
        # 安装后应用名
        self.installed_app_name = installed_app_name
        # 区域名
        self.region_id = region_id
        # 请求 ID
        self.request_id = request_id
        # 工作空间
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
        if self.installed_app_name is not None:
            result['InstalledAppName'] = self.installed_app_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('InstalledAppName') is not None:
            self.installed_app_name = m.get('InstalledAppName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
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
        app_type: str = None,
        is_reversed: bool = None,
        label_selector: str = None,
        language: str = None,
        max_results: int = None,
        next_token: str = None,
        order_by: str = None,
        scope: str = None,
        search: str = None,
        workspace: str = None,
    ):
        # 应用类型
        self.app_type = app_type
        # 是否逆序
        self.is_reversed = is_reversed
        # Label 选择器
        self.label_selector = label_selector
        # 应用描述语言
        self.language = language
        # 最大返回结果数
        self.max_results = max_results
        # Next Token
        self.next_token = next_token
        # 排序依据
        self.order_by = order_by
        # 应用范围
        self.scope = scope
        # 按照名字匹配
        self.search = search
        # 工作空间
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_type is not None:
            result['AppType'] = self.app_type
        if self.is_reversed is not None:
            result['IsReversed'] = self.is_reversed
        if self.label_selector is not None:
            result['LabelSelector'] = self.label_selector
        if self.language is not None:
            result['Language'] = self.language
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.order_by is not None:
            result['OrderBy'] = self.order_by
        if self.scope is not None:
            result['Scope'] = self.scope
        if self.search is not None:
            result['Search'] = self.search
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')
        if m.get('IsReversed') is not None:
            self.is_reversed = m.get('IsReversed')
        if m.get('LabelSelector') is not None:
            self.label_selector = m.get('LabelSelector')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')
        if m.get('Scope') is not None:
            self.scope = m.get('Scope')
        if m.get('Search') is not None:
            self.search = m.get('Search')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        return self


class ListAppsResponseBodyApps(TeaModel):
    def __init__(
        self,
        app_default_version: str = None,
        app_name: str = None,
        app_type: str = None,
        create_time: str = None,
        description: str = None,
        labels: Dict[str, str] = None,
        language: str = None,
        scope: str = None,
        source: str = None,
        workspace: str = None,
    ):
        # 默认版本
        self.app_default_version = app_default_version
        # 应用名称
        self.app_name = app_name
        # 应用类型
        self.app_type = app_type
        # 创建时间
        self.create_time = create_time
        # 应用描述
        self.description = description
        # 标签
        self.labels = labels
        # 应用描述语言
        self.language = language
        # 应用可见范围
        self.scope = scope
        # 应用来源
        self.source = source
        # 应用所在工作空间
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_default_version is not None:
            result['AppDefaultVersion'] = self.app_default_version
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_type is not None:
            result['AppType'] = self.app_type
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.language is not None:
            result['Language'] = self.language
        if self.scope is not None:
            result['Scope'] = self.scope
        if self.source is not None:
            result['Source'] = self.source
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppDefaultVersion') is not None:
            self.app_default_version = m.get('AppDefaultVersion')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('Scope') is not None:
            self.scope = m.get('Scope')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
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
        is_reversed: bool = None,
        location: str = None,
        max_results: int = None,
        next_token: str = None,
        order_by: str = None,
        search: str = None,
    ):
        # 是否反转
        self.is_reversed = is_reversed
        # 区域
        self.location = location
        # 分页数量
        self.max_results = max_results
        # 翻页Token用来标记当前开始读取的位置，置空表示从头开始
        self.next_token = next_token
        # 排序字段
        self.order_by = order_by
        # 软件名称、软件长名称中搜索的关键字
        self.search = search

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_reversed is not None:
            result['IsReversed'] = self.is_reversed
        if self.location is not None:
            result['Location'] = self.location
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.order_by is not None:
            result['OrderBy'] = self.order_by
        if self.search is not None:
            result['Search'] = self.search
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsReversed') is not None:
            self.is_reversed = m.get('IsReversed')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')
        if m.get('Search') is not None:
            self.search = m.get('Search')
        return self


class ListAuthorizedSoftwareResponseBodySoftwares(TeaModel):
    def __init__(
        self,
        help_link: str = None,
        last_modified: str = None,
        locations: List[str] = None,
        promotion: str = None,
        software_default_version: str = None,
        software_description: str = None,
        software_icon: str = None,
        software_license_fee: float = None,
        software_long_name: str = None,
        software_name: str = None,
        software_versions: List[str] = None,
    ):
        # 帮助链接
        self.help_link = help_link
        # 最后更新时间
        self.last_modified = last_modified
        # 软件可用区域
        self.locations = locations
        # 限时免费说明
        self.promotion = promotion
        # 软件默认版本
        self.software_default_version = software_default_version
        # 软件描述
        self.software_description = software_description
        # 软件图标链接
        self.software_icon = software_icon
        # 软件使用费用
        self.software_license_fee = software_license_fee
        # 软件长名称
        self.software_long_name = software_long_name
        # 软件名称
        self.software_name = software_name
        # 软件所有版本
        self.software_versions = software_versions

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.help_link is not None:
            result['HelpLink'] = self.help_link
        if self.last_modified is not None:
            result['LastModified'] = self.last_modified
        if self.locations is not None:
            result['Locations'] = self.locations
        if self.promotion is not None:
            result['Promotion'] = self.promotion
        if self.software_default_version is not None:
            result['SoftwareDefaultVersion'] = self.software_default_version
        if self.software_description is not None:
            result['SoftwareDescription'] = self.software_description
        if self.software_icon is not None:
            result['SoftwareIcon'] = self.software_icon
        if self.software_license_fee is not None:
            result['SoftwareLicenseFee'] = self.software_license_fee
        if self.software_long_name is not None:
            result['SoftwareLongName'] = self.software_long_name
        if self.software_name is not None:
            result['SoftwareName'] = self.software_name
        if self.software_versions is not None:
            result['SoftwareVersions'] = self.software_versions
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HelpLink') is not None:
            self.help_link = m.get('HelpLink')
        if m.get('LastModified') is not None:
            self.last_modified = m.get('LastModified')
        if m.get('Locations') is not None:
            self.locations = m.get('Locations')
        if m.get('Promotion') is not None:
            self.promotion = m.get('Promotion')
        if m.get('SoftwareDefaultVersion') is not None:
            self.software_default_version = m.get('SoftwareDefaultVersion')
        if m.get('SoftwareDescription') is not None:
            self.software_description = m.get('SoftwareDescription')
        if m.get('SoftwareIcon') is not None:
            self.software_icon = m.get('SoftwareIcon')
        if m.get('SoftwareLicenseFee') is not None:
            self.software_license_fee = m.get('SoftwareLicenseFee')
        if m.get('SoftwareLongName') is not None:
            self.software_long_name = m.get('SoftwareLongName')
        if m.get('SoftwareName') is not None:
            self.software_name = m.get('SoftwareName')
        if m.get('SoftwareVersions') is not None:
            self.software_versions = m.get('SoftwareVersions')
        return self


class ListAuthorizedSoftwareResponseBody(TeaModel):
    def __init__(
        self,
        host_id: str = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        softwares: List[ListAuthorizedSoftwareResponseBodySoftwares] = None,
        total_count: int = None,
    ):
        # 主机ID
        self.host_id = host_id
        # 分页数
        self.max_results = max_results
        # 翻页Token用来表示当前调用返回读取到的位置，空代表数据已经读取完毕
        self.next_token = next_token
        # 请求ID
        self.request_id = request_id
        # 软件信息
        self.softwares = softwares
        # 总记录数
        self.total_count = total_count

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
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Softwares'] = []
        if self.softwares is not None:
            for k in self.softwares:
                result['Softwares'].append(k.to_map() if k else None)
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
        self.softwares = []
        if m.get('Softwares') is not None:
            for k in m.get('Softwares'):
                temp_model = ListAuthorizedSoftwareResponseBodySoftwares()
                self.softwares.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
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
        location: str = None,
        max_results: int = None,
        next_token: str = None,
    ):
        # 区域
        self.location = location
        # 分页数量
        self.max_results = max_results
        # 翻页Token用来标记当前开始读取的位置，置空表示从头开始
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.location is not None:
            result['Location'] = self.location
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class ListContainerImagesResponseBodyContainerImages(TeaModel):
    def __init__(
        self,
        container_image_description: str = None,
        container_image_name: str = None,
        container_image_namespace: str = None,
        container_image_versions: List[str] = None,
        container_registry: str = None,
        last_modified: str = None,
        location: str = None,
    ):
        # 容器镜像描述
        self.container_image_description = container_image_description
        # 容器镜像名称
        self.container_image_name = container_image_name
        # 容器镜像名称空间名称
        self.container_image_namespace = container_image_namespace
        # 容器镜像版本
        self.container_image_versions = container_image_versions
        # 容器镜像仓库名称
        self.container_registry = container_registry
        # 最后更新时间
        self.last_modified = last_modified
        # 容器镜像所在区域
        self.location = location

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.container_image_description is not None:
            result['ContainerImageDescription'] = self.container_image_description
        if self.container_image_name is not None:
            result['ContainerImageName'] = self.container_image_name
        if self.container_image_namespace is not None:
            result['ContainerImageNamespace'] = self.container_image_namespace
        if self.container_image_versions is not None:
            result['ContainerImageVersions'] = self.container_image_versions
        if self.container_registry is not None:
            result['ContainerRegistry'] = self.container_registry
        if self.last_modified is not None:
            result['LastModified'] = self.last_modified
        if self.location is not None:
            result['Location'] = self.location
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContainerImageDescription') is not None:
            self.container_image_description = m.get('ContainerImageDescription')
        if m.get('ContainerImageName') is not None:
            self.container_image_name = m.get('ContainerImageName')
        if m.get('ContainerImageNamespace') is not None:
            self.container_image_namespace = m.get('ContainerImageNamespace')
        if m.get('ContainerImageVersions') is not None:
            self.container_image_versions = m.get('ContainerImageVersions')
        if m.get('ContainerRegistry') is not None:
            self.container_registry = m.get('ContainerRegistry')
        if m.get('LastModified') is not None:
            self.last_modified = m.get('LastModified')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        return self


class ListContainerImagesResponseBody(TeaModel):
    def __init__(
        self,
        container_images: List[ListContainerImagesResponseBodyContainerImages] = None,
        host_id: str = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # 容器镜像
        self.container_images = container_images
        # 主机ID
        self.host_id = host_id
        # 分页数
        self.max_results = max_results
        # 翻页Token用来表示当前调用返回读取到的位置，空代表数据已经读取完毕
        self.next_token = next_token
        # 主机ID
        self.request_id = request_id
        # 总记录数
        self.total_count = total_count

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
        result['ContainerImages'] = []
        if self.container_images is not None:
            for k in self.container_images:
                result['ContainerImages'].append(k.to_map() if k else None)
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
        self.container_images = []
        if m.get('ContainerImages') is not None:
            for k in m.get('ContainerImages'):
                temp_model = ListContainerImagesResponseBodyContainerImages()
                self.container_images.append(temp_model.from_map(k))
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
        is_reversed: bool = None,
        max_results: int = None,
        next_token: str = None,
        order_by: str = None,
        workspace: str = None,
    ):
        # 是否逆序
        self.is_reversed = is_reversed
        # 最大返回数量
        self.max_results = max_results
        # 起始查询位置
        self.next_token = next_token
        # 排序条件
        self.order_by = order_by
        # 工作空间
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_reversed is not None:
            result['IsReversed'] = self.is_reversed
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.order_by is not None:
            result['OrderBy'] = self.order_by
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsReversed') is not None:
            self.is_reversed = m.get('IsReversed')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
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
        entities: List[ListEntitiesResponseBodyEntities] = None,
        host_id: str = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # 实体类型数组
        self.entities = entities
        # 主机ID
        self.host_id = host_id
        # 请求的最大结果数
        self.max_results = max_results
        # 下次查询的起始Token
        self.next_token = next_token
        # 请求ID
        self.request_id = request_id
        # 返回总个数
        self.total_count = total_count

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
        result['Entities'] = []
        if self.entities is not None:
            for k in self.entities:
                result['Entities'].append(k.to_map() if k else None)
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
        self.entities = []
        if m.get('Entities') is not None:
            for k in m.get('Entities'):
                temp_model = ListEntitiesResponseBodyEntities()
                self.entities.append(temp_model.from_map(k))
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
        entity_type: str = None,
        is_reversed: bool = None,
        max_results: int = None,
        next_token: str = None,
        order_by: str = None,
        search: str = None,
        workspace: str = None,
    ):
        # 实体类型
        self.entity_type = entity_type
        # 是否逆序
        self.is_reversed = is_reversed
        # 最大返回数量
        self.max_results = max_results
        # 起始查询位置
        self.next_token = next_token
        # 排序条件
        self.order_by = order_by
        # 搜索条件
        self.search = search
        # 工作空间
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.is_reversed is not None:
            result['IsReversed'] = self.is_reversed
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.order_by is not None:
            result['OrderBy'] = self.order_by
        if self.search is not None:
            result['Search'] = self.search
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('IsReversed') is not None:
            self.is_reversed = m.get('IsReversed')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')
        if m.get('Search') is not None:
            self.search = m.get('Search')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        return self


class ListEntityItemsResponseBodyEntityItems(TeaModel):
    def __init__(
        self,
        entity_data: Dict[str, str] = None,
        entity_name: str = None,
    ):
        # 数据元素属性
        self.entity_data = entity_data
        # 表格数据元素名称
        self.entity_name = entity_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entity_data is not None:
            result['EntityData'] = self.entity_data
        if self.entity_name is not None:
            result['EntityName'] = self.entity_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EntityData') is not None:
            self.entity_data = m.get('EntityData')
        if m.get('EntityName') is not None:
            self.entity_name = m.get('EntityName')
        return self


class ListEntityItemsResponseBody(TeaModel):
    def __init__(
        self,
        entity_items: List[ListEntityItemsResponseBodyEntityItems] = None,
        host_id: str = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # 表格数据元素数组
        self.entity_items = entity_items
        # 主机ID
        self.host_id = host_id
        # 请求的最大结果数
        self.max_results = max_results
        # 下次查询的起始Token
        self.next_token = next_token
        # 请求ID
        self.request_id = request_id
        # 返回总个数
        self.total_count = total_count

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
        result['EntityItems'] = []
        if self.entity_items is not None:
            for k in self.entity_items:
                result['EntityItems'].append(k.to_map() if k else None)
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
        self.entity_items = []
        if m.get('EntityItems') is not None:
            for k in m.get('EntityItems'):
                temp_model = ListEntityItemsResponseBodyEntityItems()
                self.entity_items.append(temp_model.from_map(k))
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
        app_scope: str = None,
        category: str = None,
        is_reversed: bool = None,
        location: str = None,
        max_results: int = None,
        next_token: str = None,
        order_by: str = None,
        search: str = None,
        toolkit: str = None,
    ):
        # 可见范围
        self.app_scope = app_scope
        # 分类
        self.category = category
        # 是否倒序，默认倒序排列
        self.is_reversed = is_reversed
        # 区域Id
        self.location = location
        # 分页数
        self.max_results = max_results
        # 翻页Token用来标记当前开始读取的位置，置空表示从头开始
        self.next_token = next_token
        # 排序字段:AppName,LastModified,Used
        self.order_by = order_by
        # 模糊搜索字段：NamesapceName  AppName  Categories AppDescription
        self.search = search
        # 工具集
        self.toolkit = toolkit

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_scope is not None:
            result['AppScope'] = self.app_scope
        if self.category is not None:
            result['Category'] = self.category
        if self.is_reversed is not None:
            result['IsReversed'] = self.is_reversed
        if self.location is not None:
            result['Location'] = self.location
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.order_by is not None:
            result['OrderBy'] = self.order_by
        if self.search is not None:
            result['Search'] = self.search
        if self.toolkit is not None:
            result['Toolkit'] = self.toolkit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppScope') is not None:
            self.app_scope = m.get('AppScope')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('IsReversed') is not None:
            self.is_reversed = m.get('IsReversed')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')
        if m.get('Search') is not None:
            self.search = m.get('Search')
        if m.get('Toolkit') is not None:
            self.toolkit = m.get('Toolkit')
        return self


class ListGlobalAppsResponseBodyGlobalApps(TeaModel):
    def __init__(
        self,
        app_default_version: str = None,
        app_description: str = None,
        app_fee: str = None,
        app_name: str = None,
        app_scope: str = None,
        categories: List[str] = None,
        last_modified: str = None,
        locations: List[str] = None,
        namespace_name: str = None,
        pinned: bool = None,
        toolkit: str = None,
    ):
        # 应用默认版本
        self.app_default_version = app_default_version
        # 应用描述
        self.app_description = app_description
        # 应用计费说明
        self.app_fee = app_fee
        # 应用名称
        self.app_name = app_name
        # 应用权限
        self.app_scope = app_scope
        # 应用所属分类
        self.categories = categories
        # 更新时间
        self.last_modified = last_modified
        # 应用支持的区域ids
        self.locations = locations
        # 命名空间名称
        self.namespace_name = namespace_name
        # 应用收藏置顶标记
        self.pinned = pinned
        # 应用工具合集
        self.toolkit = toolkit

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_default_version is not None:
            result['AppDefaultVersion'] = self.app_default_version
        if self.app_description is not None:
            result['AppDescription'] = self.app_description
        if self.app_fee is not None:
            result['AppFee'] = self.app_fee
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_scope is not None:
            result['AppScope'] = self.app_scope
        if self.categories is not None:
            result['Categories'] = self.categories
        if self.last_modified is not None:
            result['LastModified'] = self.last_modified
        if self.locations is not None:
            result['Locations'] = self.locations
        if self.namespace_name is not None:
            result['NamespaceName'] = self.namespace_name
        if self.pinned is not None:
            result['Pinned'] = self.pinned
        if self.toolkit is not None:
            result['Toolkit'] = self.toolkit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppDefaultVersion') is not None:
            self.app_default_version = m.get('AppDefaultVersion')
        if m.get('AppDescription') is not None:
            self.app_description = m.get('AppDescription')
        if m.get('AppFee') is not None:
            self.app_fee = m.get('AppFee')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppScope') is not None:
            self.app_scope = m.get('AppScope')
        if m.get('Categories') is not None:
            self.categories = m.get('Categories')
        if m.get('LastModified') is not None:
            self.last_modified = m.get('LastModified')
        if m.get('Locations') is not None:
            self.locations = m.get('Locations')
        if m.get('NamespaceName') is not None:
            self.namespace_name = m.get('NamespaceName')
        if m.get('Pinned') is not None:
            self.pinned = m.get('Pinned')
        if m.get('Toolkit') is not None:
            self.toolkit = m.get('Toolkit')
        return self


class ListGlobalAppsResponseBody(TeaModel):
    def __init__(
        self,
        global_apps: List[ListGlobalAppsResponseBodyGlobalApps] = None,
        host_id: str = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # 公共应用集合
        self.global_apps = global_apps
        # 主机ID
        self.host_id = host_id
        # 分页数
        self.max_results = max_results
        # 翻页Token用来表示当前调用返回读取到的位置，空代表数据已经读取完毕
        self.next_token = next_token
        # 请求ID
        self.request_id = request_id
        # 本次请求条件下的数据总量
        self.total_count = total_count

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
        result['GlobalApps'] = []
        if self.global_apps is not None:
            for k in self.global_apps:
                result['GlobalApps'].append(k.to_map() if k else None)
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
        self.global_apps = []
        if m.get('GlobalApps') is not None:
            for k in m.get('GlobalApps'):
                temp_model = ListGlobalAppsResponseBodyGlobalApps()
                self.global_apps.append(temp_model.from_map(k))
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
        is_reversed: bool = None,
        max_results: int = None,
        next_token: str = None,
        order_by: str = None,
        search: str = None,
        tag: str = None,
    ):
        # 排序是否反转
        self.is_reversed = is_reversed
        # 分页数量
        self.max_results = max_results
        # 翻页Token用来标记当前开始读取的位置，置空表示从头开始
        self.next_token = next_token
        # 排序字段
        self.order_by = order_by
        # 名称、描述中搜索的关键字
        self.search = search
        # 公共数据集标签名
        self.tag = tag

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_reversed is not None:
            result['IsReversed'] = self.is_reversed
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.order_by is not None:
            result['OrderBy'] = self.order_by
        if self.search is not None:
            result['Search'] = self.search
        if self.tag is not None:
            result['Tag'] = self.tag
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsReversed') is not None:
            self.is_reversed = m.get('IsReversed')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')
        if m.get('Search') is not None:
            self.search = m.get('Search')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        return self


class ListPublicDatasetResponseBodyDatasets(TeaModel):
    def __init__(
        self,
        about: str = None,
        access_requirements: str = None,
        copyright: str = None,
        dataset_description: str = None,
        dataset_id: str = None,
        dataset_name: str = None,
        last_modified: str = None,
        locations: List[str] = None,
        tags: List[str] = None,
        update_frequency: str = None,
    ):
        # 关于公共数据集
        self.about = about
        # 公共数据集访问要求
        self.access_requirements = access_requirements
        # 公共数据集版权信息
        self.copyright = copyright
        # 公共数据集描述
        self.dataset_description = dataset_description
        # 公共数据集UUID
        self.dataset_id = dataset_id
        # 公共数据集名称
        self.dataset_name = dataset_name
        # 最后更新时间
        self.last_modified = last_modified
        # 公共数据集可用区域
        self.locations = locations
        # 公共数据集标签
        self.tags = tags
        # 公共数据集更新频率
        self.update_frequency = update_frequency

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.about is not None:
            result['About'] = self.about
        if self.access_requirements is not None:
            result['AccessRequirements'] = self.access_requirements
        if self.copyright is not None:
            result['Copyright'] = self.copyright
        if self.dataset_description is not None:
            result['DatasetDescription'] = self.dataset_description
        if self.dataset_id is not None:
            result['DatasetId'] = self.dataset_id
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.last_modified is not None:
            result['LastModified'] = self.last_modified
        if self.locations is not None:
            result['Locations'] = self.locations
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.update_frequency is not None:
            result['UpdateFrequency'] = self.update_frequency
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('About') is not None:
            self.about = m.get('About')
        if m.get('AccessRequirements') is not None:
            self.access_requirements = m.get('AccessRequirements')
        if m.get('Copyright') is not None:
            self.copyright = m.get('Copyright')
        if m.get('DatasetDescription') is not None:
            self.dataset_description = m.get('DatasetDescription')
        if m.get('DatasetId') is not None:
            self.dataset_id = m.get('DatasetId')
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('LastModified') is not None:
            self.last_modified = m.get('LastModified')
        if m.get('Locations') is not None:
            self.locations = m.get('Locations')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('UpdateFrequency') is not None:
            self.update_frequency = m.get('UpdateFrequency')
        return self


class ListPublicDatasetResponseBody(TeaModel):
    def __init__(
        self,
        datasets: List[ListPublicDatasetResponseBodyDatasets] = None,
        host_id: str = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # 公共数据集信息
        self.datasets = datasets
        # 主机ID
        self.host_id = host_id
        # 分页数
        self.max_results = max_results
        # 翻页Token用来表示当前调用返回读取到的位置，空代表数据已经读取完毕
        self.next_token = next_token
        # 请求ID
        self.request_id = request_id
        # 总记录数
        self.total_count = total_count

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
        result['Datasets'] = []
        if self.datasets is not None:
            for k in self.datasets:
                result['Datasets'].append(k.to_map() if k else None)
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
        self.datasets = []
        if m.get('Datasets') is not None:
            for k in m.get('Datasets'):
                temp_model = ListPublicDatasetResponseBodyDatasets()
                self.datasets.append(temp_model.from_map(k))
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
        is_reversed: bool = None,
        location: str = None,
        max_results: int = None,
        next_token: str = None,
        order_by: str = None,
    ):
        # 数据集名称
        self.dataset_name = dataset_name
        # 排序是否反转
        self.is_reversed = is_reversed
        # 公共数据集所在区域
        self.location = location
        # 分页数量
        self.max_results = max_results
        # 翻页Token用来标记当前开始读取的位置，置空表示从头开始
        self.next_token = next_token
        # 排序字段
        self.order_by = order_by

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.is_reversed is not None:
            result['IsReversed'] = self.is_reversed
        if self.location is not None:
            result['Location'] = self.location
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.order_by is not None:
            result['OrderBy'] = self.order_by
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('IsReversed') is not None:
            self.is_reversed = m.get('IsReversed')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')
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
        dataset_name: str = None,
        entities: List[ListPublicDatasetEntitiesResponseBodyEntities] = None,
        host_id: str = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # 公共数据集名称
        self.dataset_name = dataset_name
        # 该实体包含的所有类型
        self.entities = entities
        # 主机ID
        self.host_id = host_id
        # 分页数
        self.max_results = max_results
        # 翻页Token用来表示当前调用返回读取到的位置，空代表数据已经读取完毕
        self.next_token = next_token
        # 请求ID
        self.request_id = request_id
        # 总记录数
        self.total_count = total_count

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
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        result['Entities'] = []
        if self.entities is not None:
            for k in self.entities:
                result['Entities'].append(k.to_map() if k else None)
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
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        self.entities = []
        if m.get('Entities') is not None:
            for k in m.get('Entities'):
                temp_model = ListPublicDatasetEntitiesResponseBodyEntities()
                self.entities.append(temp_model.from_map(k))
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
        is_reversed: bool = None,
        location: str = None,
        max_results: int = None,
        next_token: str = None,
        order_by: str = None,
        search: str = None,
    ):
        # 数据集名称
        self.dataset_name = dataset_name
        # 实体类型
        self.entity_type = entity_type
        # 是否反转
        self.is_reversed = is_reversed
        # 公共数据集所在区域
        self.location = location
        # 分页数量
        self.max_results = max_results
        # 翻页Token用来标记当前开始读取的位置，置空表示从头开始
        self.next_token = next_token
        # 排序字段
        self.order_by = order_by
        # 实体名中搜索的关键字
        self.search = search

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
        if self.is_reversed is not None:
            result['IsReversed'] = self.is_reversed
        if self.location is not None:
            result['Location'] = self.location
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.order_by is not None:
            result['OrderBy'] = self.order_by
        if self.search is not None:
            result['Search'] = self.search
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('IsReversed') is not None:
            self.is_reversed = m.get('IsReversed')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')
        if m.get('Search') is not None:
            self.search = m.get('Search')
        return self


class ListPublicDatasetEntityItemsResponseBodyEntityItems(TeaModel):
    def __init__(
        self,
        entity_data: Dict[str, str] = None,
        entity_name: str = None,
    ):
        # 实体属性值
        self.entity_data = entity_data
        # 实体名称
        self.entity_name = entity_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entity_data is not None:
            result['EntityData'] = self.entity_data
        if self.entity_name is not None:
            result['EntityName'] = self.entity_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EntityData') is not None:
            self.entity_data = m.get('EntityData')
        if m.get('EntityName') is not None:
            self.entity_name = m.get('EntityName')
        return self


class ListPublicDatasetEntityItemsResponseBody(TeaModel):
    def __init__(
        self,
        dataset_name: str = None,
        entity_items: List[ListPublicDatasetEntityItemsResponseBodyEntityItems] = None,
        host_id: str = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # 公共数据集名称
        self.dataset_name = dataset_name
        # 该实体包含的所有对象
        self.entity_items = entity_items
        # 主机ID
        self.host_id = host_id
        # 分页数
        self.max_results = max_results
        # 翻页Token用来表示当前调用返回读取到的位置，空代表数据已经读取完毕
        self.next_token = next_token
        # 请求ID
        self.request_id = request_id
        # 总记录数
        self.total_count = total_count

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
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        result['EntityItems'] = []
        if self.entity_items is not None:
            for k in self.entity_items:
                result['EntityItems'].append(k.to_map() if k else None)
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
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        self.entity_items = []
        if m.get('EntityItems') is not None:
            for k in m.get('EntityItems'):
                temp_model = ListPublicDatasetEntityItemsResponseBodyEntityItems()
                self.entity_items.append(temp_model.from_map(k))
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
        is_reversed: bool = None,
        max_results: int = None,
        next_token: str = None,
        order_by: str = None,
        search: str = None,
    ):
        # 是否反转
        self.is_reversed = is_reversed
        # 分页数量
        self.max_results = max_results
        # 翻页Token用来标记当前开始读取的位置，置空表示从头开始
        self.next_token = next_token
        # 排序字段:TagName,LastModified
        self.order_by = order_by
        # 标签名中搜索的关键字
        self.search = search

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_reversed is not None:
            result['IsReversed'] = self.is_reversed
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.order_by is not None:
            result['OrderBy'] = self.order_by
        if self.search is not None:
            result['Search'] = self.search
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsReversed') is not None:
            self.is_reversed = m.get('IsReversed')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')
        if m.get('Search') is not None:
            self.search = m.get('Search')
        return self


class ListPublicDatasetTagsResponseBody(TeaModel):
    def __init__(
        self,
        host_id: str = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        tags: List[str] = None,
        total_count: int = None,
    ):
        # 主机ID
        self.host_id = host_id
        # 分页数
        self.max_results = max_results
        # 翻页Token用来表示当前调用返回读取到的位置，空代表数据已经读取完毕
        self.next_token = next_token
        # 请求ID
        self.request_id = request_id
        # 公共数据集标签
        self.tags = tags
        # 总记录数
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
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tags is not None:
            result['Tags'] = self.tags
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
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
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
        # 名称
        self.local_name = local_name
        # 访问Endpoint
        self.region_endpoint = region_endpoint
        # 区域ID
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
        regions: List[ListRegionsResponseBodyRegions] = None,
        request_id: str = None,
    ):
        # 主机ID
        self.host_id = host_id
        # 基因分析平台产品可用地域列表。
        self.regions = regions
        # 请求ID
        self.request_id = request_id

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
        result['Regions'] = []
        if self.regions is not None:
            for k in self.regions:
                result['Regions'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        self.regions = []
        if m.get('Regions') is not None:
            for k in m.get('Regions'):
                temp_model = ListRegionsResponseBodyRegions()
                self.regions.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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
        app_name: str = None,
        app_revision: str = None,
        entity_name: str = None,
        entity_type: str = None,
        get_total: bool = None,
        is_reversed: bool = None,
        label_selector: str = None,
        max_results: int = None,
        next_token: str = None,
        order_by: str = None,
        search: str = None,
        status: str = None,
        submission_id: str = None,
        workspace: str = None,
    ):
        # 应用名称
        self.app_name = app_name
        # 应用版本
        self.app_revision = app_revision
        # 实体名称
        self.entity_name = entity_name
        # 实体类型
        self.entity_type = entity_type
        # 是否返回所有任务条数
        self.get_total = get_total
        # 是否逆序
        self.is_reversed = is_reversed
        # 标签选择
        self.label_selector = label_selector
        # 最大返回个数
        self.max_results = max_results
        # 查询起始位置
        self.next_token = next_token
        # 排序依据
        self.order_by = order_by
        # 搜索ID
        self.search = search
        # 状态
        self.status = status
        # 提交ID
        self.submission_id = submission_id
        # 工作空间
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_revision is not None:
            result['AppRevision'] = self.app_revision
        if self.entity_name is not None:
            result['EntityName'] = self.entity_name
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.get_total is not None:
            result['GetTotal'] = self.get_total
        if self.is_reversed is not None:
            result['IsReversed'] = self.is_reversed
        if self.label_selector is not None:
            result['LabelSelector'] = self.label_selector
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.order_by is not None:
            result['OrderBy'] = self.order_by
        if self.search is not None:
            result['Search'] = self.search
        if self.status is not None:
            result['Status'] = self.status
        if self.submission_id is not None:
            result['SubmissionId'] = self.submission_id
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppRevision') is not None:
            self.app_revision = m.get('AppRevision')
        if m.get('EntityName') is not None:
            self.entity_name = m.get('EntityName')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('GetTotal') is not None:
            self.get_total = m.get('GetTotal')
        if m.get('IsReversed') is not None:
            self.is_reversed = m.get('IsReversed')
        if m.get('LabelSelector') is not None:
            self.label_selector = m.get('LabelSelector')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')
        if m.get('Search') is not None:
            self.search = m.get('Search')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubmissionId') is not None:
            self.submission_id = m.get('SubmissionId')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        return self


class ListRunsResponseBodyRunsExecuteOptions(TeaModel):
    def __init__(
        self,
        call_caching: bool = None,
        delete_intermediate_results: bool = None,
        failure_mode: str = None,
        use_relative_output_paths: bool = None,
    ):
        # 是否开启CallCaching
        self.call_caching = call_caching
        # 是否删除中间文件
        self.delete_intermediate_results = delete_intermediate_results
        # 失败模式
        self.failure_mode = failure_mode
        # 使用相对路径
        self.use_relative_output_paths = use_relative_output_paths

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
        if self.use_relative_output_paths is not None:
            result['UseRelativeOutputPaths'] = self.use_relative_output_paths
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallCaching') is not None:
            self.call_caching = m.get('CallCaching')
        if m.get('DeleteIntermediateResults') is not None:
            self.delete_intermediate_results = m.get('DeleteIntermediateResults')
        if m.get('FailureMode') is not None:
            self.failure_mode = m.get('FailureMode')
        if m.get('UseRelativeOutputPaths') is not None:
            self.use_relative_output_paths = m.get('UseRelativeOutputPaths')
        return self


class ListRunsResponseBodyRuns(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        app_revision: str = None,
        create_time: str = None,
        default_runtime: str = None,
        end_time: str = None,
        entity_name: str = None,
        entity_type: str = None,
        execute_directory: str = None,
        execute_options: ListRunsResponseBodyRunsExecuteOptions = None,
        inputs: str = None,
        labels: Dict[str, str] = None,
        region_id: str = None,
        run_id: str = None,
        run_name: str = None,
        source: str = None,
        start_time: str = None,
        status: str = None,
        submission_id: str = None,
        workspace: str = None,
    ):
        # 应用名称
        self.app_name = app_name
        # 应用版本号
        self.app_revision = app_revision
        # 提交时间
        self.create_time = create_time
        # 默认运行时
        self.default_runtime = default_runtime
        # 结束时间
        self.end_time = end_time
        # 实体名称
        self.entity_name = entity_name
        # 实体对象ID
        self.entity_type = entity_type
        # 运行目录
        self.execute_directory = execute_directory
        self.execute_options = execute_options
        # 输入参数
        self.inputs = inputs
        # 任务标签
        self.labels = labels
        # 区域
        self.region_id = region_id
        # 任务ID
        self.run_id = run_id
        # 任务名称
        self.run_name = run_name
        # 应用来源
        self.source = source
        # 开始时间
        self.start_time = start_time
        # 任务状态
        self.status = status
        # 提交ID
        self.submission_id = submission_id
        # 工作空间
        self.workspace = workspace

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
        if self.app_revision is not None:
            result['AppRevision'] = self.app_revision
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.default_runtime is not None:
            result['DefaultRuntime'] = self.default_runtime
        if self.end_time is not None:
            result['EndTime'] = self.end_time
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
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.run_id is not None:
            result['RunId'] = self.run_id
        if self.run_name is not None:
            result['RunName'] = self.run_name
        if self.source is not None:
            result['Source'] = self.source
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.submission_id is not None:
            result['SubmissionId'] = self.submission_id
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppRevision') is not None:
            self.app_revision = m.get('AppRevision')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DefaultRuntime') is not None:
            self.default_runtime = m.get('DefaultRuntime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
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
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RunId') is not None:
            self.run_id = m.get('RunId')
        if m.get('RunName') is not None:
            self.run_name = m.get('RunName')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubmissionId') is not None:
            self.submission_id = m.get('SubmissionId')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        return self


class ListRunsResponseBody(TeaModel):
    def __init__(
        self,
        host_id: str = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        runs: List[ListRunsResponseBodyRuns] = None,
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
        # 任务列表
        self.runs = runs
        # 返回个数
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
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
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
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
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


class ListSubmissionsRequest(TeaModel):
    def __init__(
        self,
        is_reversed: bool = None,
        max_results: int = None,
        next_token: str = None,
        order_by: str = None,
        search: str = None,
        status: str = None,
        workspace: str = None,
    ):
        # 逆序
        self.is_reversed = is_reversed
        # 最大返回数目
        self.max_results = max_results
        # Next Token
        self.next_token = next_token
        # 排序依据
        self.order_by = order_by
        # 搜索ID
        self.search = search
        # 状态
        self.status = status
        # 工作空间
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_reversed is not None:
            result['IsReversed'] = self.is_reversed
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.order_by is not None:
            result['OrderBy'] = self.order_by
        if self.search is not None:
            result['Search'] = self.search
        if self.status is not None:
            result['Status'] = self.status
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsReversed') is not None:
            self.is_reversed = m.get('IsReversed')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')
        if m.get('Search') is not None:
            self.search = m.get('Search')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        return self


class ListSubmissionsResponseBodySubmissionsRunStats(TeaModel):
    def __init__(
        self,
        aborted: int = None,
        aborting: int = None,
        failed: int = None,
        pending: int = None,
        running: int = None,
        submitted: int = None,
        succeeded: int = None,
    ):
        # 已取消数量
        self.aborted = aborted
        # 取消中数量
        self.aborting = aborting
        # 已失败数量
        self.failed = failed
        # 等待中数量
        self.pending = pending
        # 运行中数量
        self.running = running
        # 已提交数量
        self.submitted = submitted
        # 已成功数量
        self.succeeded = succeeded

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aborted is not None:
            result['Aborted'] = self.aborted
        if self.aborting is not None:
            result['Aborting'] = self.aborting
        if self.failed is not None:
            result['Failed'] = self.failed
        if self.pending is not None:
            result['Pending'] = self.pending
        if self.running is not None:
            result['Running'] = self.running
        if self.submitted is not None:
            result['Submitted'] = self.submitted
        if self.succeeded is not None:
            result['Succeeded'] = self.succeeded
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Aborted') is not None:
            self.aborted = m.get('Aborted')
        if m.get('Aborting') is not None:
            self.aborting = m.get('Aborting')
        if m.get('Failed') is not None:
            self.failed = m.get('Failed')
        if m.get('Pending') is not None:
            self.pending = m.get('Pending')
        if m.get('Running') is not None:
            self.running = m.get('Running')
        if m.get('Submitted') is not None:
            self.submitted = m.get('Submitted')
        if m.get('Succeeded') is not None:
            self.succeeded = m.get('Succeeded')
        return self


class ListSubmissionsResponseBodySubmissions(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        end_time: str = None,
        entity_type: str = None,
        run_stats: ListSubmissionsResponseBodySubmissionsRunStats = None,
        start_time: str = None,
        status: str = None,
        submission_id: str = None,
        workspace: str = None,
    ):
        # 提交时间
        self.create_time = create_time
        # 结束时间
        self.end_time = end_time
        # 实体类型
        self.entity_type = entity_type
        self.run_stats = run_stats
        # 开始时间
        self.start_time = start_time
        # 任务状态
        self.status = status
        # 提交ID
        self.submission_id = submission_id
        # 工作空间名字
        self.workspace = workspace

    def validate(self):
        if self.run_stats:
            self.run_stats.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.run_stats is not None:
            result['RunStats'] = self.run_stats.to_map()
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.submission_id is not None:
            result['SubmissionId'] = self.submission_id
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('RunStats') is not None:
            temp_model = ListSubmissionsResponseBodySubmissionsRunStats()
            self.run_stats = temp_model.from_map(m['RunStats'])
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubmissionId') is not None:
            self.submission_id = m.get('SubmissionId')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        return self


class ListSubmissionsResponseBody(TeaModel):
    def __init__(
        self,
        host_id: str = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        submissions: List[ListSubmissionsResponseBodySubmissions] = None,
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
        # 投递列表
        self.submissions = submissions
        # 返回个数
        self.total_count = total_count

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
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Submissions'] = []
        if self.submissions is not None:
            for k in self.submissions:
                result['Submissions'].append(k.to_map() if k else None)
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
        self.submissions = []
        if m.get('Submissions') is not None:
            for k in m.get('Submissions'):
                temp_model = ListSubmissionsResponseBodySubmissions()
                self.submissions.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
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
        is_reversed: bool = None,
        label_selector: str = None,
        max_results: int = None,
        next_token: str = None,
        order_by: str = None,
        search: str = None,
        workspace: str = None,
    ):
        # 是否逆序
        self.is_reversed = is_reversed
        # Label 选择器
        self.label_selector = label_selector
        # 最大返回结果数
        self.max_results = max_results
        # 下次查询起始位置
        self.next_token = next_token
        # 排序依据
        self.order_by = order_by
        # 查找条件
        self.search = search
        # 工作空间
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_reversed is not None:
            result['IsReversed'] = self.is_reversed
        if self.label_selector is not None:
            result['LabelSelector'] = self.label_selector
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.order_by is not None:
            result['OrderBy'] = self.order_by
        if self.search is not None:
            result['Search'] = self.search
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsReversed') is not None:
            self.is_reversed = m.get('IsReversed')
        if m.get('LabelSelector') is not None:
            self.label_selector = m.get('LabelSelector')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')
        if m.get('Search') is not None:
            self.search = m.get('Search')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        return self


class ListTemplatesResponseBodyTemplatesInputsExpression(TeaModel):
    def __init__(
        self,
        help: str = None,
        required: bool = None,
        step_order: int = None,
        task_name: str = None,
        variable_name: str = None,
        variable_type: str = None,
        variable_value: str = None,
    ):
        # 帮助信息
        self.help = help
        # 是否必须参数
        self.required = required
        # 步骤顺序
        self.step_order = step_order
        # 任务名称
        self.task_name = task_name
        # 变量名称
        self.variable_name = variable_name
        # 变量类型
        self.variable_type = variable_type
        # 变量值
        self.variable_value = variable_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.help is not None:
            result['Help'] = self.help
        if self.required is not None:
            result['Required'] = self.required
        if self.step_order is not None:
            result['StepOrder'] = self.step_order
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.variable_name is not None:
            result['VariableName'] = self.variable_name
        if self.variable_type is not None:
            result['VariableType'] = self.variable_type
        if self.variable_value is not None:
            result['VariableValue'] = self.variable_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Help') is not None:
            self.help = m.get('Help')
        if m.get('Required') is not None:
            self.required = m.get('Required')
        if m.get('StepOrder') is not None:
            self.step_order = m.get('StepOrder')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('VariableName') is not None:
            self.variable_name = m.get('VariableName')
        if m.get('VariableType') is not None:
            self.variable_type = m.get('VariableType')
        if m.get('VariableValue') is not None:
            self.variable_value = m.get('VariableValue')
        return self


class ListTemplatesResponseBodyTemplatesOutputsExpression(TeaModel):
    def __init__(
        self,
        help: str = None,
        required: bool = None,
        step_order: int = None,
        task_name: str = None,
        variable_name: str = None,
        variable_type: str = None,
        variable_value: str = None,
    ):
        # 帮助信息
        self.help = help
        # 是否必须参数
        self.required = required
        # 步骤顺序
        self.step_order = step_order
        # 任务名称
        self.task_name = task_name
        # 变量名称
        self.variable_name = variable_name
        # 变量类型
        self.variable_type = variable_type
        # 变量值
        self.variable_value = variable_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.help is not None:
            result['Help'] = self.help
        if self.required is not None:
            result['Required'] = self.required
        if self.step_order is not None:
            result['StepOrder'] = self.step_order
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.variable_name is not None:
            result['VariableName'] = self.variable_name
        if self.variable_type is not None:
            result['VariableType'] = self.variable_type
        if self.variable_value is not None:
            result['VariableValue'] = self.variable_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Help') is not None:
            self.help = m.get('Help')
        if m.get('Required') is not None:
            self.required = m.get('Required')
        if m.get('StepOrder') is not None:
            self.step_order = m.get('StepOrder')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('VariableName') is not None:
            self.variable_name = m.get('VariableName')
        if m.get('VariableType') is not None:
            self.variable_type = m.get('VariableType')
        if m.get('VariableValue') is not None:
            self.variable_value = m.get('VariableValue')
        return self


class ListTemplatesResponseBodyTemplates(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        app_revision: str = None,
        create_time: str = None,
        description: str = None,
        inputs_expression: List[ListTemplatesResponseBodyTemplatesInputsExpression] = None,
        labels: Dict[str, str] = None,
        last_modified_time: str = None,
        outputs_expression: List[ListTemplatesResponseBodyTemplatesOutputsExpression] = None,
        root_entity: str = None,
        template_name: str = None,
        workspace: str = None,
    ):
        # 应用名称
        self.app_name = app_name
        # 应用版本
        self.app_revision = app_revision
        # 创建时间
        self.create_time = create_time
        # 模板描述信息
        self.description = description
        # 应用输入
        self.inputs_expression = inputs_expression
        # 标签
        self.labels = labels
        # 最后修改时间
        self.last_modified_time = last_modified_time
        # 应用的输出参数
        self.outputs_expression = outputs_expression
        # 实体类型
        self.root_entity = root_entity
        # 应用模板名称
        self.template_name = template_name
        # 工作空间
        self.workspace = workspace

    def validate(self):
        if self.inputs_expression:
            for k in self.inputs_expression:
                if k:
                    k.validate()
        if self.outputs_expression:
            for k in self.outputs_expression:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_revision is not None:
            result['AppRevision'] = self.app_revision
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        result['InputsExpression'] = []
        if self.inputs_expression is not None:
            for k in self.inputs_expression:
                result['InputsExpression'].append(k.to_map() if k else None)
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.last_modified_time is not None:
            result['LastModifiedTime'] = self.last_modified_time
        result['OutputsExpression'] = []
        if self.outputs_expression is not None:
            for k in self.outputs_expression:
                result['OutputsExpression'].append(k.to_map() if k else None)
        if self.root_entity is not None:
            result['RootEntity'] = self.root_entity
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppRevision') is not None:
            self.app_revision = m.get('AppRevision')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        self.inputs_expression = []
        if m.get('InputsExpression') is not None:
            for k in m.get('InputsExpression'):
                temp_model = ListTemplatesResponseBodyTemplatesInputsExpression()
                self.inputs_expression.append(temp_model.from_map(k))
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('LastModifiedTime') is not None:
            self.last_modified_time = m.get('LastModifiedTime')
        self.outputs_expression = []
        if m.get('OutputsExpression') is not None:
            for k in m.get('OutputsExpression'):
                temp_model = ListTemplatesResponseBodyTemplatesOutputsExpression()
                self.outputs_expression.append(temp_model.from_map(k))
        if m.get('RootEntity') is not None:
            self.root_entity = m.get('RootEntity')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
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
        max_results: int = None,
    ):
        # 查询数量
        self.max_results = max_results

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        return self


class ListUserActiveRunsResponseBodyRunsExecuteOptions(TeaModel):
    def __init__(
        self,
        call_caching: bool = None,
        delete_intermediate_results: bool = None,
        failure_mode: str = None,
        use_relative_output_paths: bool = None,
    ):
        # 是否开启CallCaching
        self.call_caching = call_caching
        # 是否删除中间文件
        self.delete_intermediate_results = delete_intermediate_results
        # 失败模式
        self.failure_mode = failure_mode
        # 使用相对路径
        self.use_relative_output_paths = use_relative_output_paths

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
        if self.use_relative_output_paths is not None:
            result['UseRelativeOutputPaths'] = self.use_relative_output_paths
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallCaching') is not None:
            self.call_caching = m.get('CallCaching')
        if m.get('DeleteIntermediateResults') is not None:
            self.delete_intermediate_results = m.get('DeleteIntermediateResults')
        if m.get('FailureMode') is not None:
            self.failure_mode = m.get('FailureMode')
        if m.get('UseRelativeOutputPaths') is not None:
            self.use_relative_output_paths = m.get('UseRelativeOutputPaths')
        return self


class ListUserActiveRunsResponseBodyRuns(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        app_revision: str = None,
        create_time: str = None,
        default_runtime: str = None,
        end_time: str = None,
        entity_name: str = None,
        entity_type: str = None,
        execute_directory: str = None,
        execute_options: ListUserActiveRunsResponseBodyRunsExecuteOptions = None,
        inputs: str = None,
        labels: Dict[str, str] = None,
        region_id: str = None,
        run_id: str = None,
        run_name: str = None,
        source: str = None,
        start_time: str = None,
        status: str = None,
        submission_id: str = None,
        workspace: str = None,
    ):
        # 应用名称
        self.app_name = app_name
        # 应用版本号
        self.app_revision = app_revision
        # 提交时间
        self.create_time = create_time
        # 默认运行时
        self.default_runtime = default_runtime
        # 结束时间
        self.end_time = end_time
        # 实体名称
        self.entity_name = entity_name
        # 实体对象ID
        self.entity_type = entity_type
        # 运行目录
        self.execute_directory = execute_directory
        self.execute_options = execute_options
        # 输入参数
        self.inputs = inputs
        # 任务标签
        self.labels = labels
        # 区域
        self.region_id = region_id
        # 任务ID
        self.run_id = run_id
        # 任务名称
        self.run_name = run_name
        # 应用来源
        self.source = source
        # 开始时间
        self.start_time = start_time
        # 任务状态
        self.status = status
        # 提交ID
        self.submission_id = submission_id
        # 工作空间
        self.workspace = workspace

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
        if self.app_revision is not None:
            result['AppRevision'] = self.app_revision
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.default_runtime is not None:
            result['DefaultRuntime'] = self.default_runtime
        if self.end_time is not None:
            result['EndTime'] = self.end_time
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
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.run_id is not None:
            result['RunId'] = self.run_id
        if self.run_name is not None:
            result['RunName'] = self.run_name
        if self.source is not None:
            result['Source'] = self.source
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.submission_id is not None:
            result['SubmissionId'] = self.submission_id
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppRevision') is not None:
            self.app_revision = m.get('AppRevision')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DefaultRuntime') is not None:
            self.default_runtime = m.get('DefaultRuntime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
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
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RunId') is not None:
            self.run_id = m.get('RunId')
        if m.get('RunName') is not None:
            self.run_name = m.get('RunName')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubmissionId') is not None:
            self.submission_id = m.get('SubmissionId')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        return self


class ListUserActiveRunsResponseBody(TeaModel):
    def __init__(
        self,
        host_id: str = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        runs: List[ListUserActiveRunsResponseBodyRuns] = None,
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
        # 任务列表
        self.runs = runs
        # 返回个数
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
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
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
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.runs = []
        if m.get('Runs') is not None:
            for k in m.get('Runs'):
                temp_model = ListUserActiveRunsResponseBodyRuns()
                self.runs.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
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
        is_reversed: bool = None,
        label_selector: str = None,
        max_results: int = None,
        next_token: str = None,
        order_by: str = None,
        search: str = None,
    ):
        # 逆序
        self.is_reversed = is_reversed
        # Label选择器
        self.label_selector = label_selector
        # 最多返回数量
        self.max_results = max_results
        # NextToken
        self.next_token = next_token
        # 排序依据
        self.order_by = order_by
        # 搜索字段
        self.search = search

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_reversed is not None:
            result['IsReversed'] = self.is_reversed
        if self.label_selector is not None:
            result['LabelSelector'] = self.label_selector
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.order_by is not None:
            result['OrderBy'] = self.order_by
        if self.search is not None:
            result['Search'] = self.search
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsReversed') is not None:
            self.is_reversed = m.get('IsReversed')
        if m.get('LabelSelector') is not None:
            self.label_selector = m.get('LabelSelector')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')
        if m.get('Search') is not None:
            self.search = m.get('Search')
        return self


class ListWorkspacesResponseBodyWorkspaces(TeaModel):
    def __init__(
        self,
        bucket_name: str = None,
        create_time: str = None,
        description: str = None,
        job_lifecycle: int = None,
        labels: Dict[str, str] = None,
        last_modified_time: str = None,
        location: str = None,
        role: str = None,
        status: str = None,
        storage: str = None,
        workspace: str = None,
    ):
        # 工作空间Bucket名字
        self.bucket_name = bucket_name
        # 创建时间
        self.create_time = create_time
        # 工作空间描述
        self.description = description
        # 任务生命周期
        self.job_lifecycle = job_lifecycle
        # 工作空间标签
        self.labels = labels
        # 最后修改时间
        self.last_modified_time = last_modified_time
        # 地域ID
        self.location = location
        # RAM Role
        self.role = role
        # 工作空间状态
        self.status = status
        # OSS工作路径
        self.storage = storage
        # 工作空间名称
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.job_lifecycle is not None:
            result['JobLifecycle'] = self.job_lifecycle
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.last_modified_time is not None:
            result['LastModifiedTime'] = self.last_modified_time
        if self.location is not None:
            result['Location'] = self.location
        if self.role is not None:
            result['Role'] = self.role
        if self.status is not None:
            result['Status'] = self.status
        if self.storage is not None:
            result['Storage'] = self.storage
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('JobLifecycle') is not None:
            self.job_lifecycle = m.get('JobLifecycle')
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('LastModifiedTime') is not None:
            self.last_modified_time = m.get('LastModifiedTime')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Storage') is not None:
            self.storage = m.get('Storage')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        return self


class ListWorkspacesResponseBody(TeaModel):
    def __init__(
        self,
        host_id: str = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
        workspaces: List[ListWorkspacesResponseBodyWorkspaces] = None,
    ):
        # 主机ID
        self.host_id = host_id
        # 最大结果数
        self.max_results = max_results
        # 下次查询的起始Token
        self.next_token = next_token
        # 请求ID
        self.request_id = request_id
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
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
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
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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


class ResumeSubmissionRequest(TeaModel):
    def __init__(
        self,
        submission_id: str = None,
        workspace: str = None,
    ):
        # 投递ID
        self.submission_id = submission_id
        # 工作空间名称
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.submission_id is not None:
            result['SubmissionId'] = self.submission_id
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SubmissionId') is not None:
            self.submission_id = m.get('SubmissionId')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
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
        entity_data: Dict[str, str] = None,
        entity_name: str = None,
    ):
        self.entity_data = entity_data
        # 实体元素名称
        self.entity_name = entity_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entity_data is not None:
            result['EntityData'] = self.entity_data
        if self.entity_name is not None:
            result['EntityName'] = self.entity_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EntityData') is not None:
            self.entity_data = m.get('EntityData')
        if m.get('EntityName') is not None:
            self.entity_name = m.get('EntityName')
        return self


class UpdateEntityRequest(TeaModel):
    def __init__(
        self,
        entity_items: List[UpdateEntityRequestEntityItems] = None,
        entity_type: str = None,
        workspace: str = None,
    ):
        self.entity_items = entity_items
        # 实体类型
        self.entity_type = entity_type
        # 工作空间
        self.workspace = workspace

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
        result['EntityItems'] = []
        if self.entity_items is not None:
            for k in self.entity_items:
                result['EntityItems'].append(k.to_map() if k else None)
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.entity_items = []
        if m.get('EntityItems') is not None:
            for k in m.get('EntityItems'):
                temp_model = UpdateEntityRequestEntityItems()
                self.entity_items.append(temp_model.from_map(k))
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        return self


class UpdateEntityShrinkRequest(TeaModel):
    def __init__(
        self,
        entity_items_shrink: str = None,
        entity_type: str = None,
        workspace: str = None,
    ):
        self.entity_items_shrink = entity_items_shrink
        # 实体类型
        self.entity_type = entity_type
        # 工作空间
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entity_items_shrink is not None:
            result['EntityItems'] = self.entity_items_shrink
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EntityItems') is not None:
            self.entity_items_shrink = m.get('EntityItems')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        return self


class UpdateEntityResponseBody(TeaModel):
    def __init__(
        self,
        entity_type: str = None,
        host_id: str = None,
        request_id: str = None,
        workspace: str = None,
    ):
        # 实体类型
        self.entity_type = entity_type
        # 主机ID
        self.host_id = host_id
        # 请求ID
        self.request_id = request_id
        # 工作空间
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
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


class UpdateEntityItemsRequestEntityItems(TeaModel):
    def __init__(
        self,
        entity_data: Dict[str, str] = None,
        entity_name: str = None,
    ):
        self.entity_data = entity_data
        # 实体元素名称
        self.entity_name = entity_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entity_data is not None:
            result['EntityData'] = self.entity_data
        if self.entity_name is not None:
            result['EntityName'] = self.entity_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EntityData') is not None:
            self.entity_data = m.get('EntityData')
        if m.get('EntityName') is not None:
            self.entity_name = m.get('EntityName')
        return self


class UpdateEntityItemsRequest(TeaModel):
    def __init__(
        self,
        entity_items: List[UpdateEntityItemsRequestEntityItems] = None,
        entity_type: str = None,
        workspace: str = None,
    ):
        self.entity_items = entity_items
        # 实体类型
        self.entity_type = entity_type
        # 工作空间
        self.workspace = workspace

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
        result['EntityItems'] = []
        if self.entity_items is not None:
            for k in self.entity_items:
                result['EntityItems'].append(k.to_map() if k else None)
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.entity_items = []
        if m.get('EntityItems') is not None:
            for k in m.get('EntityItems'):
                temp_model = UpdateEntityItemsRequestEntityItems()
                self.entity_items.append(temp_model.from_map(k))
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        return self


class UpdateEntityItemsShrinkRequest(TeaModel):
    def __init__(
        self,
        entity_items_shrink: str = None,
        entity_type: str = None,
        workspace: str = None,
    ):
        self.entity_items_shrink = entity_items_shrink
        # 实体类型
        self.entity_type = entity_type
        # 工作空间
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entity_items_shrink is not None:
            result['EntityItems'] = self.entity_items_shrink
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EntityItems') is not None:
            self.entity_items_shrink = m.get('EntityItems')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        return self


class UpdateEntityItemsResponseBody(TeaModel):
    def __init__(
        self,
        entity_type: str = None,
        host_id: str = None,
        request_id: str = None,
        workspace: str = None,
    ):
        # 实体类型
        self.entity_type = entity_type
        # 主机ID
        self.host_id = host_id
        # 请求ID
        self.request_id = request_id
        # 工作空间
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        return self


class UpdateEntityItemsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateEntityItemsResponseBody = None,
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
            temp_model = UpdateEntityItemsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateTemplateRequestInputsExpression(TeaModel):
    def __init__(
        self,
        help: str = None,
        required: bool = None,
        step_order: int = None,
        task_name: str = None,
        variable_name: str = None,
        variable_type: str = None,
        variable_value: str = None,
    ):
        # 帮助信息
        self.help = help
        # 是否必填
        self.required = required
        # 步骤顺序
        self.step_order = step_order
        # 任务名称
        self.task_name = task_name
        # 变量名
        self.variable_name = variable_name
        # 变量类型
        self.variable_type = variable_type
        # 变量值
        self.variable_value = variable_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.help is not None:
            result['Help'] = self.help
        if self.required is not None:
            result['Required'] = self.required
        if self.step_order is not None:
            result['StepOrder'] = self.step_order
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.variable_name is not None:
            result['VariableName'] = self.variable_name
        if self.variable_type is not None:
            result['VariableType'] = self.variable_type
        if self.variable_value is not None:
            result['VariableValue'] = self.variable_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Help') is not None:
            self.help = m.get('Help')
        if m.get('Required') is not None:
            self.required = m.get('Required')
        if m.get('StepOrder') is not None:
            self.step_order = m.get('StepOrder')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('VariableName') is not None:
            self.variable_name = m.get('VariableName')
        if m.get('VariableType') is not None:
            self.variable_type = m.get('VariableType')
        if m.get('VariableValue') is not None:
            self.variable_value = m.get('VariableValue')
        return self


class UpdateTemplateRequestOutputsExpression(TeaModel):
    def __init__(
        self,
        help: str = None,
        required: bool = None,
        step_order: int = None,
        task_name: str = None,
        variable_name: str = None,
        variable_type: str = None,
        variable_value: str = None,
    ):
        # 帮助信息
        self.help = help
        # 是否必填
        self.required = required
        # 步骤顺序
        self.step_order = step_order
        # 任务名称
        self.task_name = task_name
        # 变量名
        self.variable_name = variable_name
        # 变量类型
        self.variable_type = variable_type
        # 变量值
        self.variable_value = variable_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.help is not None:
            result['Help'] = self.help
        if self.required is not None:
            result['Required'] = self.required
        if self.step_order is not None:
            result['StepOrder'] = self.step_order
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.variable_name is not None:
            result['VariableName'] = self.variable_name
        if self.variable_type is not None:
            result['VariableType'] = self.variable_type
        if self.variable_value is not None:
            result['VariableValue'] = self.variable_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Help') is not None:
            self.help = m.get('Help')
        if m.get('Required') is not None:
            self.required = m.get('Required')
        if m.get('StepOrder') is not None:
            self.step_order = m.get('StepOrder')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('VariableName') is not None:
            self.variable_name = m.get('VariableName')
        if m.get('VariableType') is not None:
            self.variable_type = m.get('VariableType')
        if m.get('VariableValue') is not None:
            self.variable_value = m.get('VariableValue')
        return self


class UpdateTemplateRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        inputs_expression: List[UpdateTemplateRequestInputsExpression] = None,
        labels: str = None,
        outputs_expression: List[UpdateTemplateRequestOutputsExpression] = None,
        root_entity: str = None,
        template_name: str = None,
        workspace: str = None,
    ):
        # 应用模板描述
        self.description = description
        # 应用的输入
        self.inputs_expression = inputs_expression
        # 应用模板标签
        self.labels = labels
        # 应用的输出
        self.outputs_expression = outputs_expression
        # 实体类型
        self.root_entity = root_entity
        # 应用模板名称
        self.template_name = template_name
        # 工作空间名称
        self.workspace = workspace

    def validate(self):
        if self.inputs_expression:
            for k in self.inputs_expression:
                if k:
                    k.validate()
        if self.outputs_expression:
            for k in self.outputs_expression:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        result['InputsExpression'] = []
        if self.inputs_expression is not None:
            for k in self.inputs_expression:
                result['InputsExpression'].append(k.to_map() if k else None)
        if self.labels is not None:
            result['Labels'] = self.labels
        result['OutputsExpression'] = []
        if self.outputs_expression is not None:
            for k in self.outputs_expression:
                result['OutputsExpression'].append(k.to_map() if k else None)
        if self.root_entity is not None:
            result['RootEntity'] = self.root_entity
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        self.inputs_expression = []
        if m.get('InputsExpression') is not None:
            for k in m.get('InputsExpression'):
                temp_model = UpdateTemplateRequestInputsExpression()
                self.inputs_expression.append(temp_model.from_map(k))
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        self.outputs_expression = []
        if m.get('OutputsExpression') is not None:
            for k in m.get('OutputsExpression'):
                temp_model = UpdateTemplateRequestOutputsExpression()
                self.outputs_expression.append(temp_model.from_map(k))
        if m.get('RootEntity') is not None:
            self.root_entity = m.get('RootEntity')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        return self


class UpdateTemplateShrinkRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        inputs_expression_shrink: str = None,
        labels: str = None,
        outputs_expression_shrink: str = None,
        root_entity: str = None,
        template_name: str = None,
        workspace: str = None,
    ):
        # 应用模板描述
        self.description = description
        # 应用的输入
        self.inputs_expression_shrink = inputs_expression_shrink
        # 应用模板标签
        self.labels = labels
        # 应用的输出
        self.outputs_expression_shrink = outputs_expression_shrink
        # 实体类型
        self.root_entity = root_entity
        # 应用模板名称
        self.template_name = template_name
        # 工作空间名称
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.inputs_expression_shrink is not None:
            result['InputsExpression'] = self.inputs_expression_shrink
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.outputs_expression_shrink is not None:
            result['OutputsExpression'] = self.outputs_expression_shrink
        if self.root_entity is not None:
            result['RootEntity'] = self.root_entity
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('InputsExpression') is not None:
            self.inputs_expression_shrink = m.get('InputsExpression')
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('OutputsExpression') is not None:
            self.outputs_expression_shrink = m.get('OutputsExpression')
        if m.get('RootEntity') is not None:
            self.root_entity = m.get('RootEntity')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
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
        description: str = None,
        job_lifecycle: int = None,
        labels: str = None,
        role: str = None,
        workspace: str = None,
    ):
        # 工作空间描述
        self.description = description
        # 工作空间内任务生命周期
        self.job_lifecycle = job_lifecycle
        # 工作空间标签
        self.labels = labels
        # 工作空间内Ram角色
        self.role = role
        # 工作空间名称
        self.workspace = workspace

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
        if self.role is not None:
            result['Role'] = self.role
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('JobLifecycle') is not None:
            self.job_lifecycle = m.get('JobLifecycle')
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
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
        entity_csvfile: str = None,
        workspace: str = None,
    ):
        # 表格文件地址
        self.entity_csvfile = entity_csvfile
        # 工作空间
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entity_csvfile is not None:
            result['EntityCSVFile'] = self.entity_csvfile
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EntityCSVFile') is not None:
            self.entity_csvfile = m.get('EntityCSVFile')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        return self


class UploadEntityResponseBody(TeaModel):
    def __init__(
        self,
        entity_type: str = None,
        host_id: str = None,
        request_id: str = None,
        workspace: str = None,
    ):
        # 表格名称
        self.entity_type = entity_type
        # 主机ID
        self.host_id = host_id
        # 请求ID
        self.request_id = request_id
        # 工作空间
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
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


