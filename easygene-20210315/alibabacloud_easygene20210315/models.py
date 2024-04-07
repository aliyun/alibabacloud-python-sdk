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
        self.run_id = run_id
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


class AbortRunResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AbortRunResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = AbortRunResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AbortSubmissionRequest(TeaModel):
    def __init__(
        self,
        submission_id: str = None,
        workspace: str = None,
    ):
        self.submission_id = submission_id
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


class AbortSubmissionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AbortSubmissionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
        self.dataset = dataset
        self.entity_type = entity_type
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
        self.entity_type = entity_type
        self.host_id = host_id
        self.request_id = request_id
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
        status_code: int = None,
        body: CopyPublicEntityResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
        revision_tag: str = None,
        workspace: str = None,
    ):
        self.app_name = app_name
        self.app_type = app_type
        self.client_token = client_token
        self.configs = configs
        self.definition = definition
        self.dependencies = dependencies
        self.description = description
        self.documentation = documentation
        self.labels = labels
        self.language = language
        self.language_version = language_version
        self.path = path
        self.revision_comment = revision_comment
        self.revision_tag = revision_tag
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
        if self.revision_tag is not None:
            result['RevisionTag'] = self.revision_tag
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
        if m.get('RevisionTag') is not None:
            self.revision_tag = m.get('RevisionTag')
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
        revision_tag: str = None,
        workspace: str = None,
    ):
        self.app_name = app_name
        self.app_type = app_type
        self.client_token = client_token
        self.configs_shrink = configs_shrink
        self.definition = definition
        self.dependencies_shrink = dependencies_shrink
        self.description = description
        self.documentation = documentation
        self.labels = labels
        self.language = language
        self.language_version = language_version
        self.path = path
        self.revision_comment = revision_comment
        self.revision_tag = revision_tag
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
        if self.revision_tag is not None:
            result['RevisionTag'] = self.revision_tag
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
        if m.get('RevisionTag') is not None:
            self.revision_tag = m.get('RevisionTag')
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
        revision_tag: str = None,
        workspace: str = None,
    ):
        self.app_name = app_name
        self.host_id = host_id
        self.request_id = request_id
        self.revision = revision
        self.revision_tag = revision_tag
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
        if self.revision_tag is not None:
            result['RevisionTag'] = self.revision_tag
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
        if m.get('RevisionTag') is not None:
            self.revision_tag = m.get('RevisionTag')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        return self


class CreateAppResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateAppResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
        self.client_token = client_token
        self.entity_items = entity_items
        self.entity_type = entity_type
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
        self.client_token = client_token
        self.entity_items_shrink = entity_items_shrink
        self.entity_type = entity_type
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
        self.entity_type = entity_type
        self.host_id = host_id
        self.request_id = request_id
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
        status_code: int = None,
        body: CreateEntityResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
        self.call_caching = call_caching
        self.delete_intermediate_results = delete_intermediate_results
        self.failure_mode = failure_mode
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
        revision_tag: str = None,
        role: str = None,
        run_name: str = None,
        workspace: str = None,
    ):
        self.app_name = app_name
        self.app_revision = app_revision
        self.client_token = client_token
        self.default_runtime = default_runtime
        self.description = description
        self.execute_directory = execute_directory
        self.execute_options = execute_options
        self.inputs = inputs
        self.labels = labels
        self.output_folder = output_folder
        self.revision_tag = revision_tag
        self.role = role
        self.run_name = run_name
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
        if self.revision_tag is not None:
            result['RevisionTag'] = self.revision_tag
        if self.role is not None:
            result['Role'] = self.role
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
        if m.get('RevisionTag') is not None:
            self.revision_tag = m.get('RevisionTag')
        if m.get('Role') is not None:
            self.role = m.get('Role')
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
        revision_tag: str = None,
        role: str = None,
        run_name: str = None,
        workspace: str = None,
    ):
        self.app_name = app_name
        self.app_revision = app_revision
        self.client_token = client_token
        self.default_runtime = default_runtime
        self.description = description
        self.execute_directory = execute_directory
        self.execute_options_shrink = execute_options_shrink
        self.inputs = inputs
        self.labels = labels
        self.output_folder = output_folder
        self.revision_tag = revision_tag
        self.role = role
        self.run_name = run_name
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
        if self.revision_tag is not None:
            result['RevisionTag'] = self.revision_tag
        if self.role is not None:
            result['Role'] = self.role
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
        if m.get('RevisionTag') is not None:
            self.revision_tag = m.get('RevisionTag')
        if m.get('Role') is not None:
            self.role = m.get('Role')
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
        self.host_id = host_id
        self.request_id = request_id
        self.run_id = run_id
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
        status_code: int = None,
        body: CreateRunResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
        revision_tag: str = None,
        workspace: str = None,
    ):
        self.app_name = app_name
        self.client_token = client_token
        self.default_runtime = default_runtime
        self.entity_names = entity_names
        self.entity_type = entity_type
        self.execute_directory = execute_directory
        self.execute_options = execute_options
        self.inputs = inputs
        self.output_folder = output_folder
        self.outputs = outputs
        self.revision = revision
        self.revision_tag = revision_tag
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
        if self.revision_tag is not None:
            result['RevisionTag'] = self.revision_tag
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
        if m.get('RevisionTag') is not None:
            self.revision_tag = m.get('RevisionTag')
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
        revision_tag: str = None,
        workspace: str = None,
    ):
        self.app_name = app_name
        self.client_token = client_token
        self.default_runtime = default_runtime
        self.entity_names_shrink = entity_names_shrink
        self.entity_type = entity_type
        self.execute_directory = execute_directory
        self.execute_options = execute_options
        self.inputs = inputs
        self.output_folder = output_folder
        self.outputs = outputs
        self.revision = revision
        self.revision_tag = revision_tag
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
        if self.revision_tag is not None:
            result['RevisionTag'] = self.revision_tag
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
        if m.get('RevisionTag') is not None:
            self.revision_tag = m.get('RevisionTag')
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
        self.host_id = host_id
        self.request_id = request_id
        self.submission_id = submission_id
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
        status_code: int = None,
        body: CreateSubmissionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
        self.help = help
        self.required = required
        self.step_order = step_order
        self.task_name = task_name
        self.variable_name = variable_name
        self.variable_type = variable_type
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
        self.help = help
        self.required = required
        self.step_order = step_order
        self.task_name = task_name
        self.variable_name = variable_name
        self.variable_type = variable_type
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
        revision_tag: str = None,
        root_entity: str = None,
        template_name: str = None,
        workspace: str = None,
    ):
        self.app_name = app_name
        self.app_revision = app_revision
        self.client_token = client_token
        self.description = description
        self.inputs_expression = inputs_expression
        self.labels = labels
        self.outputs_expression = outputs_expression
        self.revision_tag = revision_tag
        self.root_entity = root_entity
        self.template_name = template_name
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
        if self.revision_tag is not None:
            result['RevisionTag'] = self.revision_tag
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
        if m.get('RevisionTag') is not None:
            self.revision_tag = m.get('RevisionTag')
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
        revision_tag: str = None,
        root_entity: str = None,
        template_name: str = None,
        workspace: str = None,
    ):
        self.app_name = app_name
        self.app_revision = app_revision
        self.client_token = client_token
        self.description = description
        self.inputs_expression_shrink = inputs_expression_shrink
        self.labels = labels
        self.outputs_expression_shrink = outputs_expression_shrink
        self.revision_tag = revision_tag
        self.root_entity = root_entity
        self.template_name = template_name
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
        if self.revision_tag is not None:
            result['RevisionTag'] = self.revision_tag
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
        if m.get('RevisionTag') is not None:
            self.revision_tag = m.get('RevisionTag')
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
        self.host_id = host_id
        self.request_id = request_id
        self.template_name = template_name
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
        status_code: int = None,
        body: CreateTemplateResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
        self.client_token = client_token
        self.description = description
        self.job_lifecycle = job_lifecycle
        self.labels = labels
        self.role = role
        self.storage = storage
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
        self.host_id = host_id
        self.request_id = request_id
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
        status_code: int = None,
        body: CreateWorkspaceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
        self.app_name = app_name
        self.revision = revision
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


class DeleteAppResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteAppResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DeleteAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteEntityRequest(TeaModel):
    def __init__(
        self,
        entity_type: str = None,
        workspace: str = None,
    ):
        self.entity_type = entity_type
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


class DeleteEntityResponseBody(TeaModel):
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


class DeleteEntityResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteEntityResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DeleteEntityResponseBody()
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
        self.entity_type = entity_type
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
        self.entity_type = entity_type
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
        status_code: int = None,
        body: DeleteEntityItemsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DeleteEntityItemsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteRunRequest(TeaModel):
    def __init__(
        self,
        run_id: str = None,
        workspace: str = None,
    ):
        self.run_id = run_id
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


class DeleteRunResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteRunResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DeleteRunResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSubmissionRequest(TeaModel):
    def __init__(
        self,
        submission_id: str = None,
        workspace: str = None,
    ):
        self.submission_id = submission_id
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


class DeleteSubmissionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteSubmissionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DeleteSubmissionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteTemplateRequest(TeaModel):
    def __init__(
        self,
        template_name: str = None,
        workspace: str = None,
    ):
        self.template_name = template_name
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


class DeleteTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteTemplateResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DeleteTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteWorkspaceRequest(TeaModel):
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


class DeleteWorkspaceResponseBody(TeaModel):
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


class DeleteWorkspaceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteWorkspaceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
        self.entity_type = entity_type
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
        self.entity_type = entity_type
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
        self.entity_csvfile = entity_csvfile
        self.host_id = host_id
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
        status_code: int = None,
        body: DownloadEntityResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DownloadEntityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAppRequest(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        revision: str = None,
        revision_tag: str = None,
        workspace: str = None,
    ):
        self.app_name = app_name
        self.revision = revision
        self.revision_tag = revision_tag
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
        if self.revision_tag is not None:
            result['RevisionTag'] = self.revision_tag
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Revision') is not None:
            self.revision = m.get('Revision')
        if m.get('RevisionTag') is not None:
            self.revision_tag = m.get('RevisionTag')
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
        self.help = help
        self.required = required
        self.step_order = step_order
        self.task_name = task_name
        self.variable_name = variable_name
        self.variable_type = variable_type
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
        self.help = help
        self.required = required
        self.step_order = step_order
        self.task_name = task_name
        self.variable_name = variable_name
        self.variable_type = variable_type
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
        revision_tag: str = None,
    ):
        self.create_time = create_time
        self.revision = revision
        self.revision_comment = revision_comment
        self.revision_tag = revision_tag

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
        if self.revision_tag is not None:
            result['RevisionTag'] = self.revision_tag
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Revision') is not None:
            self.revision = m.get('Revision')
        if m.get('RevisionComment') is not None:
            self.revision_comment = m.get('RevisionComment')
        if m.get('RevisionTag') is not None:
            self.revision_tag = m.get('RevisionTag')
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
        revision_tag: str = None,
        revisions: List[GetAppResponseBodyRevisions] = None,
        scope: str = None,
        source: str = None,
        url: str = None,
        workflow_name: str = None,
        workspace: str = None,
    ):
        self.app_name = app_name
        self.app_type = app_type
        self.configs = configs
        self.create_time = create_time
        self.definition = definition
        self.dependencies = dependencies
        self.description = description
        self.documentation = documentation
        self.host_id = host_id
        self.inputs = inputs
        self.labels = labels
        self.language = language
        self.language_version = language_version
        self.last_modified_time = last_modified_time
        self.outputs = outputs
        self.path = path
        self.request_id = request_id
        self.revision = revision
        self.revision_comment = revision_comment
        self.revision_tag = revision_tag
        self.revisions = revisions
        self.scope = scope
        self.source = source
        self.url = url
        self.workflow_name = workflow_name
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
        if self.revision_tag is not None:
            result['RevisionTag'] = self.revision_tag
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
        if m.get('RevisionTag') is not None:
            self.revision_tag = m.get('RevisionTag')
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
        status_code: int = None,
        body: GetAppResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = GetAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetEntityRequest(TeaModel):
    def __init__(
        self,
        entity_type: str = None,
        workspace: str = None,
    ):
        self.entity_type = entity_type
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
        self.attributes = attributes
        self.entity_type = entity_type
        self.host_id = host_id
        self.request_id = request_id
        self.total_count = total_count
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
        status_code: int = None,
        body: GetEntityResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
        self.app_name = app_name
        self.app_version = app_version
        self.attributes = attributes
        self.location = location
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
        self.app_name = app_name
        self.app_version = app_version
        self.attributes_shrink = attributes_shrink
        self.location = location
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
        self.checksum = checksum
        self.content = content
        self.file_type = file_type
        self.path = path
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
        self.app_version = app_version
        self.comment = comment
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
        self.app_default_version = app_default_version
        self.app_description = app_description
        self.app_descriptor_files = app_descriptor_files
        self.app_descriptor_type = app_descriptor_type
        self.app_fee = app_fee
        self.app_name = app_name
        self.app_scope = app_scope
        self.app_type = app_type
        self.app_version = app_version
        self.app_versions = app_versions
        self.categories = categories
        self.comment = comment
        self.contact = contact
        self.dag = dag
        self.document = document
        self.host_id = host_id
        self.last_modified = last_modified
        self.links = links
        self.locations = locations
        self.namespace_name = namespace_name
        self.pinned = pinned
        self.request_id = request_id
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
        status_code: int = None,
        body: GetGlobalAppResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = GetGlobalAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPublicDatasetRequest(TeaModel):
    def __init__(
        self,
        attributes: List[str] = None,
        dataset_name: str = None,
    ):
        self.attributes = attributes
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
        self.attributes_shrink = attributes_shrink
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
        self.about = about
        self.access_requirements = access_requirements
        self.copyright = copyright
        self.dataset_description = dataset_description
        self.dataset_name = dataset_name
        self.host_id = host_id
        self.last_modified = last_modified
        self.locations = locations
        self.request_id = request_id
        self.tags = tags
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
        status_code: int = None,
        body: GetPublicDatasetResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
        self.dataset_name = dataset_name
        self.entity_type = entity_type
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
        self.attributes = attributes
        self.dataset_name = dataset_name
        self.entity_type = entity_type
        self.host_id = host_id
        self.request_id = request_id
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
        status_code: int = None,
        body: GetPublicDatasetEntityResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = GetPublicDatasetEntityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRunRequest(TeaModel):
    def __init__(
        self,
        run_id: str = None,
        workspace: str = None,
    ):
        self.run_id = run_id
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
        self.call_caching = call_caching
        self.delete_intermediate_results = delete_intermediate_results
        self.failure_mode = failure_mode
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
        billing_instance_ids: List[str] = None,
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
        self.app_name = app_name
        self.app_revision = app_revision
        self.billing_instance_ids = billing_instance_ids
        self.calls = calls
        self.create_time = create_time
        self.default_runtime = default_runtime
        self.description = description
        self.end_time = end_time
        self.entity_name = entity_name
        self.entity_type = entity_type
        self.execute_directory = execute_directory
        self.execute_options = execute_options
        self.failures = failures
        self.host_id = host_id
        self.inputs = inputs
        self.labels = labels
        self.output_folder = output_folder
        self.outputs = outputs
        self.request_id = request_id
        self.run_id = run_id
        self.run_name = run_name
        self.source = source
        self.start_time = start_time
        self.status = status
        self.submission_id = submission_id
        self.timing = timing
        self.user = user
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
        if self.billing_instance_ids is not None:
            result['BillingInstanceIds'] = self.billing_instance_ids
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
        if m.get('BillingInstanceIds') is not None:
            self.billing_instance_ids = m.get('BillingInstanceIds')
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
        status_code: int = None,
        body: GetRunResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = GetRunResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSubmissionRequest(TeaModel):
    def __init__(
        self,
        submission_id: str = None,
        workspace: str = None,
    ):
        self.submission_id = submission_id
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
        self.aborted = aborted
        self.aborting = aborting
        self.failed = failed
        self.pending = pending
        self.running = running
        self.submitted = submitted
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
        self.create_time = create_time
        self.end_time = end_time
        self.entity_type = entity_type
        self.run_stats = run_stats
        self.start_time = start_time
        self.status = status
        self.submission_id = submission_id
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
        self.host_id = host_id
        self.request_id = request_id
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
        status_code: int = None,
        body: GetSubmissionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = GetSubmissionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTemplateRequest(TeaModel):
    def __init__(
        self,
        template_name: str = None,
        workspace: str = None,
    ):
        self.template_name = template_name
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
        self.help = help
        self.required = required
        self.step_order = step_order
        self.task_name = task_name
        self.variable_name = variable_name
        self.variable_type = variable_type
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
        self.help = help
        self.required = required
        self.step_order = step_order
        self.task_name = task_name
        self.variable_name = variable_name
        self.variable_type = variable_type
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
        revision_tag: str = None,
        root_entity: str = None,
        source: str = None,
        template_name: str = None,
        workspace: str = None,
    ):
        self.app_name = app_name
        self.app_revision = app_revision
        self.create_time = create_time
        self.description = description
        self.host_id = host_id
        self.inputs_expression = inputs_expression
        self.labels = labels
        self.last_modified_time = last_modified_time
        self.outputs_expression = outputs_expression
        self.request_id = request_id
        self.revision_tag = revision_tag
        self.root_entity = root_entity
        self.source = source
        self.template_name = template_name
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
        if self.revision_tag is not None:
            result['RevisionTag'] = self.revision_tag
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
        if m.get('RevisionTag') is not None:
            self.revision_tag = m.get('RevisionTag')
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
        status_code: int = None,
        body: GetTemplateResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
        self.bucket_name = bucket_name
        self.create_time = create_time
        self.description = description
        self.host_id = host_id
        self.job_lifecycle = job_lifecycle
        self.labels = labels
        self.last_modified_time = last_modified_time
        self.location = location
        self.request_id = request_id
        self.role = role
        self.status = status
        self.storage = storage
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
        status_code: int = None,
        body: GetWorkspaceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
        self.app_name = app_name
        self.source = source
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
        self.app_name = app_name
        self.host_id = host_id
        self.region_id = region_id
        self.request_id = request_id
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
        status_code: int = None,
        body: ImportAppResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
        self.app_name = app_name
        self.installed_app_name = installed_app_name
        self.namespace_name = namespace_name
        self.source = source
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
        self.host_id = host_id
        self.installed_app_name = installed_app_name
        self.region_id = region_id
        self.request_id = request_id
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
        status_code: int = None,
        body: InstallGlobalAppResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
        self.app_type = app_type
        self.is_reversed = is_reversed
        self.label_selector = label_selector
        self.language = language
        self.max_results = max_results
        # Next Token
        self.next_token = next_token
        self.order_by = order_by
        self.scope = scope
        self.search = search
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
        self.app_default_version = app_default_version
        self.app_name = app_name
        self.app_type = app_type
        self.create_time = create_time
        self.description = description
        self.labels = labels
        self.language = language
        self.scope = scope
        self.source = source
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
        self.apps = apps
        self.host_id = host_id
        self.max_results = max_results
        # Next Token
        self.next_token = next_token
        self.request_id = request_id
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
        status_code: int = None,
        body: ListAppsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
        self.is_reversed = is_reversed
        self.location = location
        self.max_results = max_results
        self.next_token = next_token
        self.order_by = order_by
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
        self.help_link = help_link
        self.last_modified = last_modified
        self.locations = locations
        self.promotion = promotion
        self.software_default_version = software_default_version
        self.software_description = software_description
        self.software_icon = software_icon
        self.software_license_fee = software_license_fee
        self.software_long_name = software_long_name
        self.software_name = software_name
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
        self.host_id = host_id
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id
        self.softwares = softwares
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
        status_code: int = None,
        body: ListAuthorizedSoftwareResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
        self.location = location
        self.max_results = max_results
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
        self.container_image_description = container_image_description
        self.container_image_name = container_image_name
        self.container_image_namespace = container_image_namespace
        self.container_image_versions = container_image_versions
        self.container_registry = container_registry
        self.last_modified = last_modified
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
        self.container_images = container_images
        self.host_id = host_id
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id
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
        status_code: int = None,
        body: ListContainerImagesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
        self.is_reversed = is_reversed
        self.max_results = max_results
        self.next_token = next_token
        self.order_by = order_by
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
        self.entities = entities
        self.host_id = host_id
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id
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
        status_code: int = None,
        body: ListEntitiesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
        self.entity_type = entity_type
        self.is_reversed = is_reversed
        self.max_results = max_results
        self.next_token = next_token
        self.order_by = order_by
        self.search = search
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
        self.entity_data = entity_data
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
        self.entity_items = entity_items
        self.host_id = host_id
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id
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
        status_code: int = None,
        body: ListEntityItemsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
        self.app_scope = app_scope
        self.category = category
        self.is_reversed = is_reversed
        self.location = location
        self.max_results = max_results
        self.next_token = next_token
        self.order_by = order_by
        self.search = search
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
        self.app_default_version = app_default_version
        self.app_description = app_description
        self.app_fee = app_fee
        self.app_name = app_name
        self.app_scope = app_scope
        self.categories = categories
        self.last_modified = last_modified
        self.locations = locations
        self.namespace_name = namespace_name
        self.pinned = pinned
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
        self.global_apps = global_apps
        self.host_id = host_id
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id
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
        status_code: int = None,
        body: ListGlobalAppsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
        self.is_reversed = is_reversed
        self.max_results = max_results
        self.next_token = next_token
        self.order_by = order_by
        self.search = search
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
        self.about = about
        self.access_requirements = access_requirements
        self.copyright = copyright
        self.dataset_description = dataset_description
        self.dataset_id = dataset_id
        self.dataset_name = dataset_name
        self.last_modified = last_modified
        self.locations = locations
        self.tags = tags
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
        self.datasets = datasets
        self.host_id = host_id
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id
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
        status_code: int = None,
        body: ListPublicDatasetResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
        self.dataset_name = dataset_name
        self.is_reversed = is_reversed
        self.location = location
        self.max_results = max_results
        self.next_token = next_token
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
        self.dataset_name = dataset_name
        self.entities = entities
        self.host_id = host_id
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id
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
        status_code: int = None,
        body: ListPublicDatasetEntitiesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
        self.dataset_name = dataset_name
        self.entity_type = entity_type
        self.is_reversed = is_reversed
        self.location = location
        self.max_results = max_results
        self.next_token = next_token
        self.order_by = order_by
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
        self.entity_data = entity_data
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
        self.dataset_name = dataset_name
        self.entity_items = entity_items
        self.host_id = host_id
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id
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
        status_code: int = None,
        body: ListPublicDatasetEntityItemsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
        self.is_reversed = is_reversed
        self.max_results = max_results
        self.next_token = next_token
        self.order_by = order_by
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
        self.host_id = host_id
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id
        self.tags = tags
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
        status_code: int = None,
        body: ListPublicDatasetTagsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
        regions: List[ListRegionsResponseBodyRegions] = None,
        request_id: str = None,
    ):
        self.host_id = host_id
        self.regions = regions
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
        status_code: int = None,
        body: ListRegionsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
        self.app_name = app_name
        self.app_revision = app_revision
        self.entity_name = entity_name
        self.entity_type = entity_type
        self.get_total = get_total
        self.is_reversed = is_reversed
        self.label_selector = label_selector
        self.max_results = max_results
        self.next_token = next_token
        self.order_by = order_by
        self.search = search
        self.status = status
        self.submission_id = submission_id
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
        self.call_caching = call_caching
        self.delete_intermediate_results = delete_intermediate_results
        self.failure_mode = failure_mode
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
        self.app_name = app_name
        self.app_revision = app_revision
        self.create_time = create_time
        self.default_runtime = default_runtime
        self.end_time = end_time
        self.entity_name = entity_name
        self.entity_type = entity_type
        self.execute_directory = execute_directory
        self.execute_options = execute_options
        self.inputs = inputs
        self.labels = labels
        self.region_id = region_id
        self.run_id = run_id
        self.run_name = run_name
        self.source = source
        self.start_time = start_time
        self.status = status
        self.submission_id = submission_id
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
        self.host_id = host_id
        self.max_results = max_results
        self.next_token = next_token
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
        status_code: int = None,
        body: ListRunsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
        self.is_reversed = is_reversed
        self.max_results = max_results
        # Next Token
        self.next_token = next_token
        self.order_by = order_by
        self.search = search
        self.status = status
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
        self.aborted = aborted
        self.aborting = aborting
        self.failed = failed
        self.pending = pending
        self.running = running
        self.submitted = submitted
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
        self.create_time = create_time
        self.end_time = end_time
        self.entity_type = entity_type
        self.run_stats = run_stats
        self.start_time = start_time
        self.status = status
        self.submission_id = submission_id
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
        self.host_id = host_id
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id
        self.submissions = submissions
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
        status_code: int = None,
        body: ListSubmissionsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
        self.is_reversed = is_reversed
        self.label_selector = label_selector
        self.max_results = max_results
        self.next_token = next_token
        self.order_by = order_by
        self.search = search
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
        self.help = help
        self.required = required
        self.step_order = step_order
        self.task_name = task_name
        self.variable_name = variable_name
        self.variable_type = variable_type
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
        self.help = help
        self.required = required
        self.step_order = step_order
        self.task_name = task_name
        self.variable_name = variable_name
        self.variable_type = variable_type
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
        revision_tag: str = None,
        root_entity: str = None,
        template_name: str = None,
        workspace: str = None,
    ):
        self.app_name = app_name
        self.app_revision = app_revision
        self.create_time = create_time
        self.description = description
        self.inputs_expression = inputs_expression
        self.labels = labels
        self.last_modified_time = last_modified_time
        self.outputs_expression = outputs_expression
        self.revision_tag = revision_tag
        self.root_entity = root_entity
        self.template_name = template_name
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
        if self.revision_tag is not None:
            result['RevisionTag'] = self.revision_tag
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
        if m.get('RevisionTag') is not None:
            self.revision_tag = m.get('RevisionTag')
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
        self.host_id = host_id
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id
        self.templates = templates
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
        status_code: int = None,
        body: ListTemplatesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ListTemplatesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUserActiveRunsRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
    ):
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
        self.call_caching = call_caching
        self.delete_intermediate_results = delete_intermediate_results
        self.failure_mode = failure_mode
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
        self.app_name = app_name
        self.app_revision = app_revision
        self.create_time = create_time
        self.default_runtime = default_runtime
        self.end_time = end_time
        self.entity_name = entity_name
        self.entity_type = entity_type
        self.execute_directory = execute_directory
        self.execute_options = execute_options
        self.inputs = inputs
        self.labels = labels
        self.region_id = region_id
        self.run_id = run_id
        self.run_name = run_name
        self.source = source
        self.start_time = start_time
        self.status = status
        self.submission_id = submission_id
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
        self.host_id = host_id
        self.max_results = max_results
        self.next_token = next_token
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
        status_code: int = None,
        body: ListUserActiveRunsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
        self.is_reversed = is_reversed
        self.label_selector = label_selector
        self.max_results = max_results
        # NextToken
        self.next_token = next_token
        self.order_by = order_by
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
        self.bucket_name = bucket_name
        self.create_time = create_time
        self.description = description
        self.job_lifecycle = job_lifecycle
        self.labels = labels
        self.last_modified_time = last_modified_time
        self.location = location
        # RAM Role
        self.role = role
        self.status = status
        self.storage = storage
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
        self.host_id = host_id
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id
        self.total_count = total_count
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
        status_code: int = None,
        body: ListWorkspacesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ListWorkspacesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResumeSubmissionRequest(TeaModel):
    def __init__(
        self,
        submission_id: str = None,
        workspace: str = None,
    ):
        self.submission_id = submission_id
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


class ResumeSubmissionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ResumeSubmissionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ResumeSubmissionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TagAppRequest(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        app_revision: str = None,
        revision_tag: str = None,
        workspace: str = None,
    ):
        self.app_name = app_name
        self.app_revision = app_revision
        self.revision_tag = revision_tag
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
        if self.revision_tag is not None:
            result['RevisionTag'] = self.revision_tag
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppRevision') is not None:
            self.app_revision = m.get('AppRevision')
        if m.get('RevisionTag') is not None:
            self.revision_tag = m.get('RevisionTag')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        return self


class TagAppResponseBody(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        app_revision: str = None,
        former_revision: str = None,
        former_tag: str = None,
        request_id: str = None,
        revision_tag: str = None,
        workspace: str = None,
    ):
        self.app_name = app_name
        self.app_revision = app_revision
        self.former_revision = former_revision
        self.former_tag = former_tag
        self.request_id = request_id
        self.revision_tag = revision_tag
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
        if self.former_revision is not None:
            result['FormerRevision'] = self.former_revision
        if self.former_tag is not None:
            result['FormerTag'] = self.former_tag
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.revision_tag is not None:
            result['RevisionTag'] = self.revision_tag
        if self.workspace is not None:
            result['Workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppRevision') is not None:
            self.app_revision = m.get('AppRevision')
        if m.get('FormerRevision') is not None:
            self.former_revision = m.get('FormerRevision')
        if m.get('FormerTag') is not None:
            self.former_tag = m.get('FormerTag')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RevisionTag') is not None:
            self.revision_tag = m.get('RevisionTag')
        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')
        return self


class TagAppResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: TagAppResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = TagAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateEntityRequestEntityItems(TeaModel):
    def __init__(
        self,
        entity_data: Dict[str, str] = None,
        entity_name: str = None,
    ):
        self.entity_data = entity_data
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
        self.entity_type = entity_type
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
        self.entity_type = entity_type
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
        self.entity_type = entity_type
        self.host_id = host_id
        self.request_id = request_id
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
        status_code: int = None,
        body: UpdateEntityResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
        self.entity_type = entity_type
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
        self.entity_type = entity_type
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
        self.entity_type = entity_type
        self.host_id = host_id
        self.request_id = request_id
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
        status_code: int = None,
        body: UpdateEntityItemsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
        self.help = help
        self.required = required
        self.step_order = step_order
        self.task_name = task_name
        self.variable_name = variable_name
        self.variable_type = variable_type
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
        self.help = help
        self.required = required
        self.step_order = step_order
        self.task_name = task_name
        self.variable_name = variable_name
        self.variable_type = variable_type
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
        self.description = description
        self.inputs_expression = inputs_expression
        self.labels = labels
        self.outputs_expression = outputs_expression
        self.root_entity = root_entity
        self.template_name = template_name
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
        self.description = description
        self.inputs_expression_shrink = inputs_expression_shrink
        self.labels = labels
        self.outputs_expression_shrink = outputs_expression_shrink
        self.root_entity = root_entity
        self.template_name = template_name
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


class UpdateTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateTemplateResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
        self.description = description
        self.job_lifecycle = job_lifecycle
        self.labels = labels
        self.role = role
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


class UpdateWorkspaceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateWorkspaceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = UpdateWorkspaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UploadEntityRequest(TeaModel):
    def __init__(
        self,
        entity_csvfile: str = None,
        workspace: str = None,
    ):
        self.entity_csvfile = entity_csvfile
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
        self.entity_type = entity_type
        self.host_id = host_id
        self.request_id = request_id
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
        status_code: int = None,
        body: UploadEntityResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = UploadEntityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


