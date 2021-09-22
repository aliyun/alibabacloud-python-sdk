# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict, Any


class AddImageRequestLabels(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # Key
        self.key = key
        # Value
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class AddImageRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        description: str = None,
        image_uri: str = None,
        labels: List[AddImageRequestLabels] = None,
    ):
        # 镜像名称
        self.name = name
        # 镜像描述
        self.description = description
        # 镜像地址
        self.image_uri = image_uri
        # 镜像标签，是个数组
        self.labels = labels

    def validate(self):
        if self.labels:
            for k in self.labels:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.description is not None:
            result['Description'] = self.description
        if self.image_uri is not None:
            result['ImageUri'] = self.image_uri
        result['Labels'] = []
        if self.labels is not None:
            for k in self.labels:
                result['Labels'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ImageUri') is not None:
            self.image_uri = m.get('ImageUri')
        self.labels = []
        if m.get('Labels') is not None:
            for k in m.get('Labels'):
                temp_model = AddImageRequestLabels()
                self.labels.append(temp_model.from_map(k))
        return self


class AddImageResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        image_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        # 镜像 id
        self.image_id = image_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        return self


class AddImageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddImageResponseBody = None,
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
            temp_model = AddImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddImageLabelsRequestLabels(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # Key
        self.key = key
        # Value
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class AddImageLabelsRequest(TeaModel):
    def __init__(
        self,
        labels: List[AddImageLabelsRequestLabels] = None,
    ):
        # 标签
        self.labels = labels

    def validate(self):
        if self.labels:
            for k in self.labels:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Labels'] = []
        if self.labels is not None:
            for k in self.labels:
                result['Labels'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.labels = []
        if m.get('Labels') is not None:
            for k in m.get('Labels'):
                temp_model = AddImageLabelsRequestLabels()
                self.labels.append(temp_model.from_map(k))
        return self


class AddImageLabelsResponseBody(TeaModel):
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


class AddImageLabelsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddImageLabelsResponseBody = None,
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
            temp_model = AddImageLabelsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CopyExperimentRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        description: str = None,
        source: str = None,
        folder_id: str = None,
        workspace_id: str = None,
    ):
        # 实验名称，最大长度 128，可包含中英文
        self.name = name
        # 实验描述
        self.description = description
        # 实验来源，目前 PaiStudio，data-airec（推荐白盒）
        self.source = source
        # 实验创建的目录 id
        self.folder_id = folder_id
        # 实验创建的Workspace
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
        if self.description is not None:
            result['Description'] = self.description
        if self.source is not None:
            result['Source'] = self.source
        if self.folder_id is not None:
            result['FolderId'] = self.folder_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('FolderId') is not None:
            self.folder_id = m.get('FolderId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class CopyExperimentResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        experiment_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.experiment_id = experiment_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.experiment_id is not None:
            result['ExperimentId'] = self.experiment_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ExperimentId') is not None:
            self.experiment_id = m.get('ExperimentId')
        return self


class CopyExperimentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CopyExperimentResponseBody = None,
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
            temp_model = CopyExperimentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateExperimentRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        description: str = None,
        source: str = None,
        folder_id: str = None,
        workspace_id: str = None,
        template_id: str = None,
        options: str = None,
    ):
        self.name = name
        self.description = description
        self.source = source
        self.folder_id = folder_id
        self.workspace_id = workspace_id
        self.template_id = template_id
        self.options = options

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.description is not None:
            result['Description'] = self.description
        if self.source is not None:
            result['Source'] = self.source
        if self.folder_id is not None:
            result['FolderId'] = self.folder_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.options is not None:
            result['Options'] = self.options
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('FolderId') is not None:
            self.folder_id = m.get('FolderId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('Options') is not None:
            self.options = m.get('Options')
        return self


class CreateExperimentResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        experiment_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.experiment_id = experiment_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.experiment_id is not None:
            result['ExperimentId'] = self.experiment_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ExperimentId') is not None:
            self.experiment_id = m.get('ExperimentId')
        return self


class CreateExperimentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateExperimentResponseBody = None,
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
            temp_model = CreateExperimentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateExperimentFolderRequest(TeaModel):
    def __init__(
        self,
        workspace_id: str = None,
        name: str = None,
        parent_folder_id: str = None,
        source: str = None,
    ):
        self.workspace_id = workspace_id
        self.name = name
        self.parent_folder_id = parent_folder_id
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        if self.name is not None:
            result['Name'] = self.name
        if self.parent_folder_id is not None:
            result['ParentFolderId'] = self.parent_folder_id
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ParentFolderId') is not None:
            self.parent_folder_id = m.get('ParentFolderId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class CreateExperimentFolderResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        folder_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.folder_id = folder_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.folder_id is not None:
            result['FolderId'] = self.folder_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('FolderId') is not None:
            self.folder_id = m.get('FolderId')
        return self


class CreateExperimentFolderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateExperimentFolderResponseBody = None,
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
            temp_model = CreateExperimentFolderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateJobRequest(TeaModel):
    def __init__(
        self,
        experiment_id: str = None,
        execute_type: str = None,
        node_id: str = None,
        options: str = None,
    ):
        self.experiment_id = experiment_id
        self.execute_type = execute_type
        self.node_id = node_id
        self.options = options

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.experiment_id is not None:
            result['ExperimentId'] = self.experiment_id
        if self.execute_type is not None:
            result['ExecuteType'] = self.execute_type
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.options is not None:
            result['Options'] = self.options
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExperimentId') is not None:
            self.experiment_id = m.get('ExperimentId')
        if m.get('ExecuteType') is not None:
            self.execute_type = m.get('ExecuteType')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('Options') is not None:
            self.options = m.get('Options')
        return self


class CreateJobResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        job_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.job_id = job_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class CreateJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateJobResponseBody = None,
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
            temp_model = CreateJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateServiceRequestConfig(TeaModel):
    def __init__(
        self,
        log_directory: str = None,
    ):
        self.log_directory = log_directory

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.log_directory is not None:
            result['LogDirectory'] = self.log_directory
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LogDirectory') is not None:
            self.log_directory = m.get('LogDirectory')
        return self


class CreateServiceRequest(TeaModel):
    def __init__(
        self,
        service_type: str = None,
        config: CreateServiceRequestConfig = None,
    ):
        self.service_type = service_type
        self.config = config

    def validate(self):
        if self.config:
            self.config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        if self.config is not None:
            result['Config'] = self.config.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        if m.get('Config') is not None:
            temp_model = CreateServiceRequestConfig()
            self.config = temp_model.from_map(m['Config'])
        return self


class CreateServiceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        url: str = None,
        service_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.url = url
        self.service_id = service_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.url is not None:
            result['Url'] = self.url
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        return self


class CreateServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateServiceResponseBody = None,
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
            temp_model = CreateServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteExperimentResponseBody(TeaModel):
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


class DeleteExperimentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteExperimentResponseBody = None,
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
            temp_model = DeleteExperimentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteExperimentFolderResponseBody(TeaModel):
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


class DeleteExperimentFolderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteExperimentFolderResponseBody = None,
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
            temp_model = DeleteExperimentFolderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteServiceResponseBody(TeaModel):
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


class DeleteServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteServiceResponseBody = None,
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
            temp_model = DeleteServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAlgorithmDefRequest(TeaModel):
    def __init__(
        self,
        provider: str = None,
        identifier: str = None,
        algo_version: str = None,
        signature: str = None,
    ):
        self.provider = provider
        self.identifier = identifier
        self.algo_version = algo_version
        self.signature = signature

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.provider is not None:
            result['Provider'] = self.provider
        if self.identifier is not None:
            result['Identifier'] = self.identifier
        if self.algo_version is not None:
            result['AlgoVersion'] = self.algo_version
        if self.signature is not None:
            result['Signature'] = self.signature
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Provider') is not None:
            self.provider = m.get('Provider')
        if m.get('Identifier') is not None:
            self.identifier = m.get('Identifier')
        if m.get('AlgoVersion') is not None:
            self.algo_version = m.get('AlgoVersion')
        if m.get('Signature') is not None:
            self.signature = m.get('Signature')
        return self


class GetAlgorithmDefResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        spec: Dict[str, Any] = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.spec = spec

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.spec is not None:
            result['Spec'] = self.spec
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Spec') is not None:
            self.spec = m.get('Spec')
        return self


class GetAlgorithmDefResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetAlgorithmDefResponseBody = None,
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
            temp_model = GetAlgorithmDefResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAlgorithmDefsRequest(TeaModel):
    def __init__(
        self,
        timestamp: str = None,
        latest_timestamp: str = None,
        range_start: int = None,
        range_end: int = None,
    ):
        self.timestamp = timestamp
        self.latest_timestamp = latest_timestamp
        self.range_start = range_start
        self.range_end = range_end

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.latest_timestamp is not None:
            result['LatestTimestamp'] = self.latest_timestamp
        if self.range_start is not None:
            result['RangeStart'] = self.range_start
        if self.range_end is not None:
            result['RangeEnd'] = self.range_end
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('LatestTimestamp') is not None:
            self.latest_timestamp = m.get('LatestTimestamp')
        if m.get('RangeStart') is not None:
            self.range_start = m.get('RangeStart')
        if m.get('RangeEnd') is not None:
            self.range_end = m.get('RangeEnd')
        return self


class GetAlgorithmDefsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        specs: List[Dict[str, Any]] = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.specs = specs

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.specs is not None:
            result['Specs'] = self.specs
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Specs') is not None:
            self.specs = m.get('Specs')
        return self


class GetAlgorithmDefsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetAlgorithmDefsResponseBody = None,
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
            temp_model = GetAlgorithmDefsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAlgorithmTreeRequest(TeaModel):
    def __init__(
        self,
        source: str = None,
    ):
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class GetAlgorithmTreeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        tree: List[Dict[str, Any]] = None,
        timestamp: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.tree = tree
        self.timestamp = timestamp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tree is not None:
            result['Tree'] = self.tree
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Tree') is not None:
            self.tree = m.get('Tree')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        return self


class GetAlgorithmTreeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetAlgorithmTreeResponseBody = None,
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
            temp_model = GetAlgorithmTreeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAlgoTreeRequest(TeaModel):
    def __init__(
        self,
        source: str = None,
    ):
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class GetAlgoTreeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: Dict[str, Any] = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class GetAlgoTreeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetAlgoTreeResponseBody = None,
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
            temp_model = GetAlgoTreeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetExperimentResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        experiment_id: str = None,
        name: str = None,
        description: str = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        creator: str = None,
        source: str = None,
        version: int = None,
        workspace_id: str = None,
        content: str = None,
        options: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.experiment_id = experiment_id
        self.name = name
        self.description = description
        self.gmt_create_time = gmt_create_time
        self.gmt_modified_time = gmt_modified_time
        self.creator = creator
        self.source = source
        self.version = version
        self.workspace_id = workspace_id
        self.content = content
        self.options = options

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.experiment_id is not None:
            result['ExperimentId'] = self.experiment_id
        if self.name is not None:
            result['Name'] = self.name
        if self.description is not None:
            result['Description'] = self.description
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.creator is not None:
            result['Creator'] = self.creator
        if self.source is not None:
            result['Source'] = self.source
        if self.version is not None:
            result['Version'] = self.version
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        if self.content is not None:
            result['Content'] = self.content
        if self.options is not None:
            result['Options'] = self.options
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ExperimentId') is not None:
            self.experiment_id = m.get('ExperimentId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Options') is not None:
            self.options = m.get('Options')
        return self


class GetExperimentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetExperimentResponseBody = None,
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
            temp_model = GetExperimentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetExperimentFolderChildrenRequest(TeaModel):
    def __init__(
        self,
        workspace_id: str = None,
        only_folder: bool = None,
    ):
        self.workspace_id = workspace_id
        self.only_folder = only_folder

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        if self.only_folder is not None:
            result['OnlyFolder'] = self.only_folder
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        if m.get('OnlyFolder') is not None:
            self.only_folder = m.get('OnlyFolder')
        return self


class GetExperimentFolderChildrenResponseBodyItems(TeaModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
        type: str = None,
        icon: str = None,
        empty: bool = None,
    ):
        self.id = id
        self.name = name
        self.type = type
        self.icon = icon
        self.empty = empty

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        if self.icon is not None:
            result['Icon'] = self.icon
        if self.empty is not None:
            result['Empty'] = self.empty
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Icon') is not None:
            self.icon = m.get('Icon')
        if m.get('Empty') is not None:
            self.empty = m.get('Empty')
        return self


class GetExperimentFolderChildrenResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        total_count: int = None,
        items: List[GetExperimentFolderChildrenResponseBodyItems] = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.total_count = total_count
        self.items = items

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = GetExperimentFolderChildrenResponseBodyItems()
                self.items.append(temp_model.from_map(k))
        return self


class GetExperimentFolderChildrenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetExperimentFolderChildrenResponseBody = None,
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
            temp_model = GetExperimentFolderChildrenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetExperimentMetaResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        experiment_id: str = None,
        name: str = None,
        description: str = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        creator: str = None,
        source: str = None,
        version: str = None,
        workspace_id: str = None,
        options: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.experiment_id = experiment_id
        self.name = name
        self.description = description
        self.gmt_create_time = gmt_create_time
        self.gmt_modified_time = gmt_modified_time
        self.creator = creator
        self.source = source
        self.version = version
        self.workspace_id = workspace_id
        self.options = options

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.experiment_id is not None:
            result['ExperimentId'] = self.experiment_id
        if self.name is not None:
            result['Name'] = self.name
        if self.description is not None:
            result['Description'] = self.description
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.creator is not None:
            result['Creator'] = self.creator
        if self.source is not None:
            result['Source'] = self.source
        if self.version is not None:
            result['Version'] = self.version
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        if self.options is not None:
            result['Options'] = self.options
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ExperimentId') is not None:
            self.experiment_id = m.get('ExperimentId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        if m.get('Options') is not None:
            self.options = m.get('Options')
        return self


class GetExperimentMetaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetExperimentMetaResponseBody = None,
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
            temp_model = GetExperimentMetaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetExperimentsStatisticsRequest(TeaModel):
    def __init__(
        self,
        workspace_ids: str = None,
        source: str = None,
    ):
        self.workspace_ids = workspace_ids
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.workspace_ids is not None:
            result['WorkspaceIds'] = self.workspace_ids
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('WorkspaceIds') is not None:
            self.workspace_ids = m.get('WorkspaceIds')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class GetExperimentsStatisticsResponseBodyData(TeaModel):
    def __init__(
        self,
        workspace_id: str = None,
        total_count: int = None,
        create_count: int = None,
    ):
        self.workspace_id = workspace_id
        self.total_count = total_count
        self.create_count = create_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.create_count is not None:
            result['CreateCount'] = self.create_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('CreateCount') is not None:
            self.create_count = m.get('CreateCount')
        return self


class GetExperimentsStatisticsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: List[GetExperimentsStatisticsResponseBodyData] = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetExperimentsStatisticsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        return self


class GetExperimentsStatisticsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetExperimentsStatisticsResponseBody = None,
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
            temp_model = GetExperimentsStatisticsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetExperimentStatusResponseBodyNodes(TeaModel):
    def __init__(
        self,
        node_id: str = None,
        job_id: str = None,
        run_id: str = None,
        run_node_id: str = None,
        status: str = None,
        started_at: str = None,
        finished_at: str = None,
    ):
        self.node_id = node_id
        self.job_id = job_id
        self.run_id = run_id
        self.run_node_id = run_node_id
        self.status = status
        self.started_at = started_at
        self.finished_at = finished_at

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.run_id is not None:
            result['RunId'] = self.run_id
        if self.run_node_id is not None:
            result['RunNodeId'] = self.run_node_id
        if self.status is not None:
            result['Status'] = self.status
        if self.started_at is not None:
            result['StartedAt'] = self.started_at
        if self.finished_at is not None:
            result['FinishedAt'] = self.finished_at
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('RunId') is not None:
            self.run_id = m.get('RunId')
        if m.get('RunNodeId') is not None:
            self.run_node_id = m.get('RunNodeId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StartedAt') is not None:
            self.started_at = m.get('StartedAt')
        if m.get('FinishedAt') is not None:
            self.finished_at = m.get('FinishedAt')
        return self


class GetExperimentStatusResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        status: str = None,
        nodes: List[GetExperimentStatusResponseBodyNodes] = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.status = status
        self.nodes = nodes

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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        result['Nodes'] = []
        if self.nodes is not None:
            for k in self.nodes:
                result['Nodes'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        self.nodes = []
        if m.get('Nodes') is not None:
            for k in m.get('Nodes'):
                temp_model = GetExperimentStatusResponseBodyNodes()
                self.nodes.append(temp_model.from_map(k))
        return self


class GetExperimentStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetExperimentStatusResponseBody = None,
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
            temp_model = GetExperimentStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetImageRequest(TeaModel):
    def __init__(
        self,
        verbose: bool = None,
    ):
        # 是否显示非必要信息：Labels
        self.verbose = verbose

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.verbose is not None:
            result['Verbose'] = self.verbose
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Verbose') is not None:
            self.verbose = m.get('Verbose')
        return self


class GetImageResponseBodyLabels(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # Key
        self.key = key
        # Value
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetImageResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        name: str = None,
        description: str = None,
        image_uri: str = None,
        operator_create: str = None,
        parent_operator_create: str = None,
        labels: List[GetImageResponseBodyLabels] = None,
    ):
        # Id of the request
        self.request_id = request_id
        # 创建 UTC 时间，日期格式 iso8601
        self.gmt_create_time = gmt_create_time
        # 创建 UTC 时间，日期格式 iso8601
        self.gmt_modified_time = gmt_modified_time
        # 镜像名称
        self.name = name
        # 描述
        self.description = description
        # 镜像地址，包含版本号
        self.image_uri = image_uri
        # 创建人
        self.operator_create = operator_create
        # 创建人父账户
        self.parent_operator_create = parent_operator_create
        # 镜像标签
        self.labels = labels

    def validate(self):
        if self.labels:
            for k in self.labels:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.name is not None:
            result['Name'] = self.name
        if self.description is not None:
            result['Description'] = self.description
        if self.image_uri is not None:
            result['ImageUri'] = self.image_uri
        if self.operator_create is not None:
            result['OperatorCreate'] = self.operator_create
        if self.parent_operator_create is not None:
            result['ParentOperatorCreate'] = self.parent_operator_create
        result['Labels'] = []
        if self.labels is not None:
            for k in self.labels:
                result['Labels'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ImageUri') is not None:
            self.image_uri = m.get('ImageUri')
        if m.get('OperatorCreate') is not None:
            self.operator_create = m.get('OperatorCreate')
        if m.get('ParentOperatorCreate') is not None:
            self.parent_operator_create = m.get('ParentOperatorCreate')
        self.labels = []
        if m.get('Labels') is not None:
            for k in m.get('Labels'):
                temp_model = GetImageResponseBodyLabels()
                self.labels.append(temp_model.from_map(k))
        return self


class GetImageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetImageResponseBody = None,
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
            temp_model = GetImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetJobRequest(TeaModel):
    def __init__(
        self,
        verbose: bool = None,
    ):
        self.verbose = verbose

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.verbose is not None:
            result['Verbose'] = self.verbose
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Verbose') is not None:
            self.verbose = m.get('Verbose')
        return self


class GetJobResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        experiment_id: str = None,
        workspace_id: str = None,
        job_id: str = None,
        snapshot: str = None,
        execute_type: str = None,
        node_id: str = None,
        run_info: str = None,
        run_id: str = None,
        paiflow_node_id: str = None,
        creator: str = None,
        status: str = None,
        gmt_create_time: str = None,
        arguments: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.experiment_id = experiment_id
        self.workspace_id = workspace_id
        self.job_id = job_id
        self.snapshot = snapshot
        self.execute_type = execute_type
        self.node_id = node_id
        self.run_info = run_info
        self.run_id = run_id
        self.paiflow_node_id = paiflow_node_id
        self.creator = creator
        self.status = status
        self.gmt_create_time = gmt_create_time
        self.arguments = arguments

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.experiment_id is not None:
            result['ExperimentId'] = self.experiment_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.snapshot is not None:
            result['Snapshot'] = self.snapshot
        if self.execute_type is not None:
            result['ExecuteType'] = self.execute_type
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.run_info is not None:
            result['RunInfo'] = self.run_info
        if self.run_id is not None:
            result['RunId'] = self.run_id
        if self.paiflow_node_id is not None:
            result['PaiflowNodeId'] = self.paiflow_node_id
        if self.creator is not None:
            result['Creator'] = self.creator
        if self.status is not None:
            result['Status'] = self.status
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.arguments is not None:
            result['Arguments'] = self.arguments
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ExperimentId') is not None:
            self.experiment_id = m.get('ExperimentId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Snapshot') is not None:
            self.snapshot = m.get('Snapshot')
        if m.get('ExecuteType') is not None:
            self.execute_type = m.get('ExecuteType')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('RunInfo') is not None:
            self.run_info = m.get('RunInfo')
        if m.get('RunId') is not None:
            self.run_id = m.get('RunId')
        if m.get('PaiflowNodeId') is not None:
            self.paiflow_node_id = m.get('PaiflowNodeId')
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('Arguments') is not None:
            self.arguments = m.get('Arguments')
        return self


class GetJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetJobResponseBody = None,
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
            temp_model = GetJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMCTableSchemaRequest(TeaModel):
    def __init__(
        self,
        workspace_id: str = None,
    ):
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class GetMCTableSchemaResponseBodyColumns(TeaModel):
    def __init__(
        self,
        name: str = None,
        type: str = None,
        preview: List[str] = None,
    ):
        self.name = name
        self.type = type
        self.preview = preview

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        if self.preview is not None:
            result['Preview'] = self.preview
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Preview') is not None:
            self.preview = m.get('Preview')
        return self


class GetMCTableSchemaResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        columns: List[GetMCTableSchemaResponseBodyColumns] = None,
        partition_columns: List[str] = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.columns = columns
        self.partition_columns = partition_columns

    def validate(self):
        if self.columns:
            for k in self.columns:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Columns'] = []
        if self.columns is not None:
            for k in self.columns:
                result['Columns'].append(k.to_map() if k else None)
        if self.partition_columns is not None:
            result['PartitionColumns'] = self.partition_columns
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.columns = []
        if m.get('Columns') is not None:
            for k in m.get('Columns'):
                temp_model = GetMCTableSchemaResponseBodyColumns()
                self.columns.append(temp_model.from_map(k))
        if m.get('PartitionColumns') is not None:
            self.partition_columns = m.get('PartitionColumns')
        return self


class GetMCTableSchemaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetMCTableSchemaResponseBody = None,
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
            temp_model = GetMCTableSchemaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetNodeInputSchemaRequest(TeaModel):
    def __init__(
        self,
        input_id: str = None,
        input_index: int = None,
    ):
        self.input_id = input_id
        self.input_index = input_index

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.input_id is not None:
            result['InputId'] = self.input_id
        if self.input_index is not None:
            result['InputIndex'] = self.input_index
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InputId') is not None:
            self.input_id = m.get('InputId')
        if m.get('InputIndex') is not None:
            self.input_index = m.get('InputIndex')
        return self


class GetNodeInputSchemaResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        col_names: List[str] = None,
        col_types: List[str] = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.col_names = col_names
        self.col_types = col_types

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.col_names is not None:
            result['ColNames'] = self.col_names
        if self.col_types is not None:
            result['ColTypes'] = self.col_types
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ColNames') is not None:
            self.col_names = m.get('ColNames')
        if m.get('ColTypes') is not None:
            self.col_types = m.get('ColTypes')
        return self


class GetNodeInputSchemaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetNodeInputSchemaResponseBody = None,
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
            temp_model = GetNodeInputSchemaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetNodeOutputRequest(TeaModel):
    def __init__(
        self,
        output_index: str = None,
    ):
        self.output_index = output_index

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.output_index is not None:
            result['OutputIndex'] = self.output_index
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OutputIndex') is not None:
            self.output_index = m.get('OutputIndex')
        return self


class GetNodeOutputResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        node_name: str = None,
        algo_name: str = None,
        display_name: str = None,
        type: str = None,
        value: Dict[str, Any] = None,
        location_type: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.node_name = node_name
        self.algo_name = algo_name
        self.display_name = display_name
        self.type = type
        self.value = value
        self.location_type = location_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.node_name is not None:
            result['NodeName'] = self.node_name
        if self.algo_name is not None:
            result['AlgoName'] = self.algo_name
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.type is not None:
            result['Type'] = self.type
        if self.value is not None:
            result['Value'] = self.value
        if self.location_type is not None:
            result['LocationType'] = self.location_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')
        if m.get('AlgoName') is not None:
            self.algo_name = m.get('AlgoName')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('LocationType') is not None:
            self.location_type = m.get('LocationType')
        return self


class GetNodeOutputResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetNodeOutputResponseBody = None,
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
            temp_model = GetNodeOutputResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetNodeVisualizationRequest(TeaModel):
    def __init__(
        self,
        config: str = None,
    ):
        self.config = config

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['Config'] = self.config
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')
        return self


class GetNodeVisualizationResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        visualization_type: str = None,
        content: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.visualization_type = visualization_type
        self.content = content

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.visualization_type is not None:
            result['VisualizationType'] = self.visualization_type
        if self.content is not None:
            result['Content'] = self.content
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('VisualizationType') is not None:
            self.visualization_type = m.get('VisualizationType')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        return self


class GetNodeVisualizationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetNodeVisualizationResponseBody = None,
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
            temp_model = GetNodeVisualizationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetServiceRequest(TeaModel):
    def __init__(
        self,
        service_type: str = None,
    ):
        self.service_type = service_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        return self


class GetServiceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        url: str = None,
        service_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.url = url
        self.service_id = service_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.url is not None:
            result['Url'] = self.url
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        return self


class GetServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetServiceResponseBody = None,
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
            temp_model = GetServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTemplateResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        template_id: str = None,
        name: str = None,
        image_link: str = None,
        doc_link: str = None,
        detail: str = None,
        description: str = None,
        content: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.template_id = template_id
        self.name = name
        self.image_link = image_link
        self.doc_link = doc_link
        self.detail = detail
        self.description = description
        self.content = content

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.name is not None:
            result['Name'] = self.name
        if self.image_link is not None:
            result['ImageLink'] = self.image_link
        if self.doc_link is not None:
            result['DocLink'] = self.doc_link
        if self.detail is not None:
            result['Detail'] = self.detail
        if self.description is not None:
            result['Description'] = self.description
        if self.content is not None:
            result['Content'] = self.content
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ImageLink') is not None:
            self.image_link = m.get('ImageLink')
        if m.get('DocLink') is not None:
            self.doc_link = m.get('DocLink')
        if m.get('Detail') is not None:
            self.detail = m.get('Detail')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Content') is not None:
            self.content = m.get('Content')
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


class ListAlgoDefsRequestBody(TeaModel):
    def __init__(
        self,
        provider: str = None,
        identifier: str = None,
        version: str = None,
        signature: str = None,
    ):
        self.provider = provider
        self.identifier = identifier
        self.version = version
        self.signature = signature

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.provider is not None:
            result['Provider'] = self.provider
        if self.identifier is not None:
            result['Identifier'] = self.identifier
        if self.version is not None:
            result['Version'] = self.version
        if self.signature is not None:
            result['Signature'] = self.signature
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Provider') is not None:
            self.provider = m.get('Provider')
        if m.get('Identifier') is not None:
            self.identifier = m.get('Identifier')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('Signature') is not None:
            self.signature = m.get('Signature')
        return self


class ListAlgoDefsRequest(TeaModel):
    def __init__(
        self,
        body: List[ListAlgoDefsRequestBody] = None,
    ):
        self.body = body

    def validate(self):
        if self.body:
            for k in self.body:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['body'] = []
        if self.body is not None:
            for k in self.body:
                result['body'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.body = []
        if m.get('body') is not None:
            for k in m.get('body'):
                temp_model = ListAlgoDefsRequestBody()
                self.body.append(temp_model.from_map(k))
        return self


class ListAlgoDefsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: List[Dict[str, Any]] = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class ListAlgoDefsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListAlgoDefsResponseBody = None,
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
            temp_model = ListAlgoDefsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAuthRolesRequest(TeaModel):
    def __init__(
        self,
        workspace_id: str = None,
        is_generate_token: str = None,
    ):
        self.workspace_id = workspace_id
        self.is_generate_token = is_generate_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        if self.is_generate_token is not None:
            result['IsGenerateToken'] = self.is_generate_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        if m.get('IsGenerateToken') is not None:
            self.is_generate_token = m.get('IsGenerateToken')
        return self


class ListAuthRolesResponseBodyRolesToken(TeaModel):
    def __init__(
        self,
        security_token: str = None,
        access_key_id: str = None,
        access_key_secret: str = None,
        expiration: str = None,
    ):
        self.security_token = security_token
        self.access_key_id = access_key_id
        self.access_key_secret = access_key_secret
        self.expiration = expiration

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.access_key_id is not None:
            result['AccessKeyId'] = self.access_key_id
        if self.access_key_secret is not None:
            result['AccessKeySecret'] = self.access_key_secret
        if self.expiration is not None:
            result['Expiration'] = self.expiration
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('AccessKeyId') is not None:
            self.access_key_id = m.get('AccessKeyId')
        if m.get('AccessKeySecret') is not None:
            self.access_key_secret = m.get('AccessKeySecret')
        if m.get('Expiration') is not None:
            self.expiration = m.get('Expiration')
        return self


class ListAuthRolesResponseBodyRoles(TeaModel):
    def __init__(
        self,
        role_name: str = None,
        role_arn: str = None,
        is_enabled: str = None,
        token: ListAuthRolesResponseBodyRolesToken = None,
        role_type: str = None,
    ):
        self.role_name = role_name
        self.role_arn = role_arn
        self.is_enabled = is_enabled
        self.token = token
        self.role_type = role_type

    def validate(self):
        if self.token:
            self.token.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        if self.role_arn is not None:
            result['RoleARN'] = self.role_arn
        if self.is_enabled is not None:
            result['IsEnabled'] = self.is_enabled
        if self.token is not None:
            result['Token'] = self.token.to_map()
        if self.role_type is not None:
            result['RoleType'] = self.role_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        if m.get('RoleARN') is not None:
            self.role_arn = m.get('RoleARN')
        if m.get('IsEnabled') is not None:
            self.is_enabled = m.get('IsEnabled')
        if m.get('Token') is not None:
            temp_model = ListAuthRolesResponseBodyRolesToken()
            self.token = temp_model.from_map(m['Token'])
        if m.get('RoleType') is not None:
            self.role_type = m.get('RoleType')
        return self


class ListAuthRolesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        roles: List[ListAuthRolesResponseBodyRoles] = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.roles = roles

    def validate(self):
        if self.roles:
            for k in self.roles:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Roles'] = []
        if self.roles is not None:
            for k in self.roles:
                result['Roles'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.roles = []
        if m.get('Roles') is not None:
            for k in m.get('Roles'):
                temp_model = ListAuthRolesResponseBodyRoles()
                self.roles.append(temp_model.from_map(k))
        return self


class ListAuthRolesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListAuthRolesResponseBody = None,
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
            temp_model = ListAuthRolesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListExperimentsRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        order: str = None,
        experiment_id: str = None,
        name: str = None,
        creator: str = None,
        source: str = None,
        workspace_id: str = None,
        sort_by: str = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.order = order
        self.experiment_id = experiment_id
        self.name = name
        self.creator = creator
        self.source = source
        self.workspace_id = workspace_id
        self.sort_by = sort_by

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.order is not None:
            result['Order'] = self.order
        if self.experiment_id is not None:
            result['ExperimentId'] = self.experiment_id
        if self.name is not None:
            result['Name'] = self.name
        if self.creator is not None:
            result['Creator'] = self.creator
        if self.source is not None:
            result['Source'] = self.source
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('ExperimentId') is not None:
            self.experiment_id = m.get('ExperimentId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        return self


class ListExperimentsResponseBodyExperiments(TeaModel):
    def __init__(
        self,
        experiment_id: str = None,
        name: str = None,
        description: str = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        creator: str = None,
        source: str = None,
        version: int = None,
        workspace_id: str = None,
    ):
        self.experiment_id = experiment_id
        self.name = name
        self.description = description
        self.gmt_create_time = gmt_create_time
        self.gmt_modified_time = gmt_modified_time
        self.creator = creator
        self.source = source
        self.version = version
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
        if self.description is not None:
            result['Description'] = self.description
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.creator is not None:
            result['Creator'] = self.creator
        if self.source is not None:
            result['Source'] = self.source
        if self.version is not None:
            result['Version'] = self.version
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExperimentId') is not None:
            self.experiment_id = m.get('ExperimentId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class ListExperimentsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        experiments: List[ListExperimentsResponseBodyExperiments] = None,
        total_count: int = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.experiments = experiments
        self.total_count = total_count

    def validate(self):
        if self.experiments:
            for k in self.experiments:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Experiments'] = []
        if self.experiments is not None:
            for k in self.experiments:
                result['Experiments'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.experiments = []
        if m.get('Experiments') is not None:
            for k in m.get('Experiments'):
                temp_model = ListExperimentsResponseBodyExperiments()
                self.experiments.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListExperimentsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListExperimentsResponseBody = None,
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
            temp_model = ListExperimentsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListImageLabelsRequest(TeaModel):
    def __init__(
        self,
        label_keys: str = None,
        label_filter: str = None,
        image_id: str = None,
    ):
        # 标签列表，以逗号分隔
        self.label_keys = label_keys
        # image过滤条件，获取满足条件的image的所有label
        self.label_filter = label_filter
        # 镜像id
        self.image_id = image_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label_keys is not None:
            result['LabelKeys'] = self.label_keys
        if self.label_filter is not None:
            result['LabelFilter'] = self.label_filter
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LabelKeys') is not None:
            self.label_keys = m.get('LabelKeys')
        if m.get('LabelFilter') is not None:
            self.label_filter = m.get('LabelFilter')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        return self


class ListImageLabelsResponseBodyLabels(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # 键
        self.key = key
        # 值
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListImageLabelsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        labels: List[ListImageLabelsResponseBodyLabels] = None,
        total_count: int = None,
    ):
        # Id of the request
        self.request_id = request_id
        # 镜像标签
        self.labels = labels
        # 符合过滤条件的数量
        self.total_count = total_count

    def validate(self):
        if self.labels:
            for k in self.labels:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['Labels'] = []
        if self.labels is not None:
            for k in self.labels:
                result['Labels'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.labels = []
        if m.get('Labels') is not None:
            for k in m.get('Labels'):
                temp_model = ListImageLabelsResponseBodyLabels()
                self.labels.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListImageLabelsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListImageLabelsResponseBody = None,
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
            temp_model = ListImageLabelsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListImagesRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        page_number: int = None,
        page_size: int = None,
        sort_by: str = None,
        order: str = None,
        labels: str = None,
        verbose: bool = None,
    ):
        # 镜像名称，支持模糊搜索
        self.name = name
        # 分页，从1开始，默认1
        self.page_number = page_number
        # 页大小，默认20
        self.page_size = page_size
        # 排序字段
        self.sort_by = sort_by
        # 排序方向： ASC - 升序 DESC - 降序
        self.order = order
        # 过滤值 以逗号分隔
        self.labels = labels
        # 是否显示非必要信息：Labels
        self.verbose = verbose

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.order is not None:
            result['Order'] = self.order
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.verbose is not None:
            result['Verbose'] = self.verbose
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('Verbose') is not None:
            self.verbose = m.get('Verbose')
        return self


class ListImagesResponseBodyImagesLabels(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # Key
        self.key = key
        # Value
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListImagesResponseBodyImages(TeaModel):
    def __init__(
        self,
        name: str = None,
        gmt_create_time: str = None,
        description: str = None,
        image_uri: str = None,
        labels: List[ListImagesResponseBodyImagesLabels] = None,
        image_id: str = None,
    ):
        # 镜像名称
        self.name = name
        # 创建 UTC 时间，日期格式 iso8601
        self.gmt_create_time = gmt_create_time
        # 镜像描述
        self.description = description
        # 镜像地址，包含版本号
        self.image_uri = image_uri
        # 镜像标签，是个map
        self.labels = labels
        # 镜像id
        self.image_id = image_id

    def validate(self):
        if self.labels:
            for k in self.labels:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.image_uri is not None:
            result['ImageUri'] = self.image_uri
        result['Labels'] = []
        if self.labels is not None:
            for k in self.labels:
                result['Labels'].append(k.to_map() if k else None)
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ImageUri') is not None:
            self.image_uri = m.get('ImageUri')
        self.labels = []
        if m.get('Labels') is not None:
            for k in m.get('Labels'):
                temp_model = ListImagesResponseBodyImagesLabels()
                self.labels.append(temp_model.from_map(k))
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        return self


class ListImagesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        total_count: int = None,
        images: List[ListImagesResponseBodyImages] = None,
    ):
        # Id of the request
        self.request_id = request_id
        # 总数
        self.total_count = total_count
        # 镜像列表
        self.images = images

    def validate(self):
        if self.images:
            for k in self.images:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['Images'] = []
        if self.images is not None:
            for k in self.images:
                result['Images'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.images = []
        if m.get('Images') is not None:
            for k in m.get('Images'):
                temp_model = ListImagesResponseBodyImages()
                self.images.append(temp_model.from_map(k))
        return self


class ListImagesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListImagesResponseBody = None,
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
            temp_model = ListImagesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListJobsRequest(TeaModel):
    def __init__(
        self,
        experiment_id: str = None,
        creator: str = None,
        order: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.experiment_id = experiment_id
        self.creator = creator
        self.order = order
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.experiment_id is not None:
            result['ExperimentId'] = self.experiment_id
        if self.creator is not None:
            result['Creator'] = self.creator
        if self.order is not None:
            result['Order'] = self.order
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExperimentId') is not None:
            self.experiment_id = m.get('ExperimentId')
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListJobsResponseBodyJobs(TeaModel):
    def __init__(
        self,
        experiment_id: str = None,
        workspace_id: str = None,
        job_id: str = None,
        execute_type: str = None,
        node_id: str = None,
        run_id: str = None,
        paiflow_node_id: str = None,
        creator: str = None,
        status: str = None,
        gmt_create_time: str = None,
    ):
        self.experiment_id = experiment_id
        self.workspace_id = workspace_id
        self.job_id = job_id
        self.execute_type = execute_type
        self.node_id = node_id
        self.run_id = run_id
        self.paiflow_node_id = paiflow_node_id
        self.creator = creator
        self.status = status
        self.gmt_create_time = gmt_create_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.experiment_id is not None:
            result['ExperimentId'] = self.experiment_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.execute_type is not None:
            result['ExecuteType'] = self.execute_type
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.run_id is not None:
            result['RunId'] = self.run_id
        if self.paiflow_node_id is not None:
            result['PaiflowNodeId'] = self.paiflow_node_id
        if self.creator is not None:
            result['Creator'] = self.creator
        if self.status is not None:
            result['Status'] = self.status
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExperimentId') is not None:
            self.experiment_id = m.get('ExperimentId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('ExecuteType') is not None:
            self.execute_type = m.get('ExecuteType')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('RunId') is not None:
            self.run_id = m.get('RunId')
        if m.get('PaiflowNodeId') is not None:
            self.paiflow_node_id = m.get('PaiflowNodeId')
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        return self


class ListJobsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        jobs: List[ListJobsResponseBodyJobs] = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.jobs = jobs

    def validate(self):
        if self.jobs:
            for k in self.jobs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Jobs'] = []
        if self.jobs is not None:
            for k in self.jobs:
                result['Jobs'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.jobs = []
        if m.get('Jobs') is not None:
            for k in m.get('Jobs'):
                temp_model = ListJobsResponseBodyJobs()
                self.jobs.append(temp_model.from_map(k))
        return self


class ListJobsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListJobsResponseBody = None,
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
            temp_model = ListJobsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListNodeOutputsResponseBodyOutputs(TeaModel):
    def __init__(
        self,
        display_name: str = None,
        type: str = None,
        output_id: str = None,
        output_index: str = None,
        value: Dict[str, Any] = None,
        node_name: str = None,
        algo_name: str = None,
        location_type: str = None,
    ):
        self.display_name = display_name
        self.type = type
        self.output_id = output_id
        self.output_index = output_index
        self.value = value
        self.node_name = node_name
        self.algo_name = algo_name
        self.location_type = location_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.type is not None:
            result['Type'] = self.type
        if self.output_id is not None:
            result['OutputId'] = self.output_id
        if self.output_index is not None:
            result['OutputIndex'] = self.output_index
        if self.value is not None:
            result['Value'] = self.value
        if self.node_name is not None:
            result['NodeName'] = self.node_name
        if self.algo_name is not None:
            result['AlgoName'] = self.algo_name
        if self.location_type is not None:
            result['LocationType'] = self.location_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('OutputId') is not None:
            self.output_id = m.get('OutputId')
        if m.get('OutputIndex') is not None:
            self.output_index = m.get('OutputIndex')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')
        if m.get('AlgoName') is not None:
            self.algo_name = m.get('AlgoName')
        if m.get('LocationType') is not None:
            self.location_type = m.get('LocationType')
        return self


class ListNodeOutputsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        outputs: List[ListNodeOutputsResponseBodyOutputs] = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.outputs = outputs

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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Outputs'] = []
        if self.outputs is not None:
            for k in self.outputs:
                result['Outputs'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.outputs = []
        if m.get('Outputs') is not None:
            for k in m.get('Outputs'):
                temp_model = ListNodeOutputsResponseBodyOutputs()
                self.outputs.append(temp_model.from_map(k))
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


class ListRecentExperimentsRequest(TeaModel):
    def __init__(
        self,
        order: str = None,
        source: str = None,
        type: str = None,
        workspace_id: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.order = order
        self.source = source
        self.type = type
        self.workspace_id = workspace_id
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order is not None:
            result['Order'] = self.order
        if self.source is not None:
            result['Source'] = self.source
        if self.type is not None:
            result['Type'] = self.type
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListRecentExperimentsResponseBodyExperiments(TeaModel):
    def __init__(
        self,
        experiment_id: str = None,
        name: str = None,
        description: str = None,
        recent_gmt_modified_time: str = None,
        source: str = None,
        modify_cnt: int = None,
        workspace_id: str = None,
        workspace_name: str = None,
    ):
        self.experiment_id = experiment_id
        self.name = name
        self.description = description
        self.recent_gmt_modified_time = recent_gmt_modified_time
        self.source = source
        self.modify_cnt = modify_cnt
        self.workspace_id = workspace_id
        self.workspace_name = workspace_name

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
        if self.description is not None:
            result['Description'] = self.description
        if self.recent_gmt_modified_time is not None:
            result['RecentGmtModifiedTime'] = self.recent_gmt_modified_time
        if self.source is not None:
            result['Source'] = self.source
        if self.modify_cnt is not None:
            result['ModifyCnt'] = self.modify_cnt
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        if self.workspace_name is not None:
            result['WorkspaceName'] = self.workspace_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExperimentId') is not None:
            self.experiment_id = m.get('ExperimentId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('RecentGmtModifiedTime') is not None:
            self.recent_gmt_modified_time = m.get('RecentGmtModifiedTime')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('ModifyCnt') is not None:
            self.modify_cnt = m.get('ModifyCnt')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        if m.get('WorkspaceName') is not None:
            self.workspace_name = m.get('WorkspaceName')
        return self


class ListRecentExperimentsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        experiments: List[ListRecentExperimentsResponseBodyExperiments] = None,
        total_count: int = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.experiments = experiments
        self.total_count = total_count

    def validate(self):
        if self.experiments:
            for k in self.experiments:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Experiments'] = []
        if self.experiments is not None:
            for k in self.experiments:
                result['Experiments'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.experiments = []
        if m.get('Experiments') is not None:
            for k in m.get('Experiments'):
                temp_model = ListRecentExperimentsResponseBodyExperiments()
                self.experiments.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListRecentExperimentsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListRecentExperimentsResponseBody = None,
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
            temp_model = ListRecentExperimentsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListServicesRequest(TeaModel):
    def __init__(
        self,
        workspace_id: str = None,
        service_type: str = None,
    ):
        self.workspace_id = workspace_id
        self.service_type = service_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        return self


class ListServicesResponseBodyServices(TeaModel):
    def __init__(
        self,
        url: str = None,
        service_id: str = None,
    ):
        self.url = url
        self.service_id = service_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.url is not None:
            result['Url'] = self.url
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        return self


class ListServicesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        total_count: int = None,
        services: List[ListServicesResponseBodyServices] = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.total_count = total_count
        self.services = services

    def validate(self):
        if self.services:
            for k in self.services:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['Services'] = []
        if self.services is not None:
            for k in self.services:
                result['Services'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.services = []
        if m.get('Services') is not None:
            for k in m.get('Services'):
                temp_model = ListServicesResponseBodyServices()
                self.services.append(temp_model.from_map(k))
        return self


class ListServicesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListServicesResponseBody = None,
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
            temp_model = ListServicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTemplatesRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        source: str = None,
        list: str = None,
        tag_id: str = None,
        order: str = None,
        type_id: str = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.source = source
        self.list = list
        self.tag_id = tag_id
        self.order = order
        self.type_id = type_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.source is not None:
            result['Source'] = self.source
        if self.list is not None:
            result['List'] = self.list
        if self.tag_id is not None:
            result['TagId'] = self.tag_id
        if self.order is not None:
            result['Order'] = self.order
        if self.type_id is not None:
            result['TypeId'] = self.type_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('List') is not None:
            self.list = m.get('List')
        if m.get('TagId') is not None:
            self.tag_id = m.get('TagId')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('TypeId') is not None:
            self.type_id = m.get('TypeId')
        return self


class ListTemplatesResponseBodyTemplateDataTemplate(TeaModel):
    def __init__(
        self,
        template_id: str = None,
        content: str = None,
        description: str = None,
        detail: str = None,
        doc_link: str = None,
        image_link: str = None,
        name: str = None,
    ):
        self.template_id = template_id
        self.content = content
        self.description = description
        self.detail = detail
        self.doc_link = doc_link
        self.image_link = image_link
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.content is not None:
            result['Content'] = self.content
        if self.description is not None:
            result['Description'] = self.description
        if self.detail is not None:
            result['Detail'] = self.detail
        if self.doc_link is not None:
            result['DocLink'] = self.doc_link
        if self.image_link is not None:
            result['ImageLink'] = self.image_link
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Detail') is not None:
            self.detail = m.get('Detail')
        if m.get('DocLink') is not None:
            self.doc_link = m.get('DocLink')
        if m.get('ImageLink') is not None:
            self.image_link = m.get('ImageLink')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class ListTemplatesResponseBodyTemplateDataTemplateTag(TeaModel):
    def __init__(
        self,
        name: str = None,
        tag_id: str = None,
        type_id: str = None,
    ):
        self.name = name
        self.tag_id = tag_id
        self.type_id = type_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.tag_id is not None:
            result['TagId'] = self.tag_id
        if self.type_id is not None:
            result['TypeId'] = self.type_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('TagId') is not None:
            self.tag_id = m.get('TagId')
        if m.get('TypeId') is not None:
            self.type_id = m.get('TypeId')
        return self


class ListTemplatesResponseBodyTemplateDataTemplateType(TeaModel):
    def __init__(
        self,
        type_id: str = None,
        name: str = None,
    ):
        self.type_id = type_id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type_id is not None:
            result['TypeId'] = self.type_id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TypeId') is not None:
            self.type_id = m.get('TypeId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class ListTemplatesResponseBodyTemplateData(TeaModel):
    def __init__(
        self,
        template: ListTemplatesResponseBodyTemplateDataTemplate = None,
        template_tag: ListTemplatesResponseBodyTemplateDataTemplateTag = None,
        template_type: ListTemplatesResponseBodyTemplateDataTemplateType = None,
    ):
        self.template = template
        self.template_tag = template_tag
        self.template_type = template_type

    def validate(self):
        if self.template:
            self.template.validate()
        if self.template_tag:
            self.template_tag.validate()
        if self.template_type:
            self.template_type.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.template is not None:
            result['Template'] = self.template.to_map()
        if self.template_tag is not None:
            result['TemplateTag'] = self.template_tag.to_map()
        if self.template_type is not None:
            result['TemplateType'] = self.template_type.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Template') is not None:
            temp_model = ListTemplatesResponseBodyTemplateDataTemplate()
            self.template = temp_model.from_map(m['Template'])
        if m.get('TemplateTag') is not None:
            temp_model = ListTemplatesResponseBodyTemplateDataTemplateTag()
            self.template_tag = temp_model.from_map(m['TemplateTag'])
        if m.get('TemplateType') is not None:
            temp_model = ListTemplatesResponseBodyTemplateDataTemplateType()
            self.template_type = temp_model.from_map(m['TemplateType'])
        return self


class ListTemplatesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        total_count: int = None,
        template_data: List[ListTemplatesResponseBodyTemplateData] = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.total_count = total_count
        self.template_data = template_data

    def validate(self):
        if self.template_data:
            for k in self.template_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['TemplateData'] = []
        if self.template_data is not None:
            for k in self.template_data:
                result['TemplateData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.template_data = []
        if m.get('TemplateData') is not None:
            for k in m.get('TemplateData'):
                temp_model = ListTemplatesResponseBodyTemplateData()
                self.template_data.append(temp_model.from_map(k))
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


class PreviewMCTableRequest(TeaModel):
    def __init__(
        self,
        workspace_id: str = None,
        endpoint: str = None,
    ):
        self.workspace_id = workspace_id
        self.endpoint = endpoint

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        return self


class PreviewMCTableResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        content: List[List[str]] = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.content = content

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.content is not None:
            result['Content'] = self.content
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        return self


class PreviewMCTableResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: PreviewMCTableResponseBody = None,
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
            temp_model = PreviewMCTableResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveImageResponseBody(TeaModel):
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


class RemoveImageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RemoveImageResponseBody = None,
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
            temp_model = RemoveImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveImageLabelsResponseBody(TeaModel):
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


class RemoveImageLabelsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RemoveImageLabelsResponseBody = None,
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
            temp_model = RemoveImageLabelsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchMCTablesRequest(TeaModel):
    def __init__(
        self,
        workspace_id: str = None,
        keyword: str = None,
    ):
        self.workspace_id = workspace_id
        self.keyword = keyword

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        return self


class SearchMCTablesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        tables: List[str] = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.tables = tables

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tables is not None:
            result['Tables'] = self.tables
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Tables') is not None:
            self.tables = m.get('Tables')
        return self


class SearchMCTablesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SearchMCTablesResponseBody = None,
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
            temp_model = SearchMCTablesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopExperimentResponseBody(TeaModel):
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


class StopExperimentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StopExperimentResponseBody = None,
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
            temp_model = StopExperimentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopJobResponseBody(TeaModel):
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


class StopJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StopJobResponseBody = None,
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
            temp_model = StopJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateExperimentContentRequest(TeaModel):
    def __init__(
        self,
        content: str = None,
        version: int = None,
    ):
        self.content = content
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class UpdateExperimentContentResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        version: int = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class UpdateExperimentContentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateExperimentContentResponseBody = None,
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
            temp_model = UpdateExperimentContentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateExperimentFolderRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        parent_folder_id: str = None,
    ):
        self.name = name
        self.parent_folder_id = parent_folder_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.parent_folder_id is not None:
            result['ParentFolderId'] = self.parent_folder_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ParentFolderId') is not None:
            self.parent_folder_id = m.get('ParentFolderId')
        return self


class UpdateExperimentFolderResponseBody(TeaModel):
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


class UpdateExperimentFolderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateExperimentFolderResponseBody = None,
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
            temp_model = UpdateExperimentFolderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateExperimentMetaRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        description: str = None,
        folder_id: str = None,
        options: str = None,
    ):
        self.name = name
        self.description = description
        self.folder_id = folder_id
        self.options = options

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.description is not None:
            result['Description'] = self.description
        if self.folder_id is not None:
            result['FolderId'] = self.folder_id
        if self.options is not None:
            result['Options'] = self.options
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('FolderId') is not None:
            self.folder_id = m.get('FolderId')
        if m.get('Options') is not None:
            self.options = m.get('Options')
        return self


class UpdateExperimentMetaResponseBody(TeaModel):
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


class UpdateExperimentMetaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateExperimentMetaResponseBody = None,
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
            temp_model = UpdateExperimentMetaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


