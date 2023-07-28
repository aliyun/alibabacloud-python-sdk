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
        self.key = key
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
        description: str = None,
        image_uri: str = None,
        labels: List[AddImageRequestLabels] = None,
        name: str = None,
    ):
        self.description = description
        self.image_uri = image_uri
        self.labels = labels
        self.name = name

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
        if self.description is not None:
            result['Description'] = self.description
        if self.image_uri is not None:
            result['ImageUri'] = self.image_uri
        result['Labels'] = []
        if self.labels is not None:
            for k in self.labels:
                result['Labels'].append(k.to_map() if k else None)
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ImageUri') is not None:
            self.image_uri = m.get('ImageUri')
        self.labels = []
        if m.get('Labels') is not None:
            for k in m.get('Labels'):
                temp_model = AddImageRequestLabels()
                self.labels.append(temp_model.from_map(k))
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class AddImageResponseBody(TeaModel):
    def __init__(
        self,
        image_id: str = None,
        request_id: str = None,
    ):
        self.image_id = image_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class AddImageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddImageResponseBody = None,
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
            temp_model = AddImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddImageLabelsRequestLabels(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
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
        status_code: int = None,
        body: AddImageLabelsResponseBody = None,
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
            temp_model = AddImageLabelsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CopyExperimentRequest(TeaModel):
    def __init__(
        self,
        accessibility: str = None,
        description: str = None,
        folder_id: str = None,
        name: str = None,
        source: str = None,
        workspace_id: str = None,
    ):
        self.accessibility = accessibility
        self.description = description
        self.folder_id = folder_id
        self.name = name
        self.source = source
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
        if self.description is not None:
            result['Description'] = self.description
        if self.folder_id is not None:
            result['FolderId'] = self.folder_id
        if self.name is not None:
            result['Name'] = self.name
        if self.source is not None:
            result['Source'] = self.source
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accessibility') is not None:
            self.accessibility = m.get('Accessibility')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('FolderId') is not None:
            self.folder_id = m.get('FolderId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class CopyExperimentResponseBody(TeaModel):
    def __init__(
        self,
        experiment_id: str = None,
        request_id: str = None,
    ):
        self.experiment_id = experiment_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.experiment_id is not None:
            result['ExperimentId'] = self.experiment_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExperimentId') is not None:
            self.experiment_id = m.get('ExperimentId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CopyExperimentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CopyExperimentResponseBody = None,
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
            temp_model = CopyExperimentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateExperimentRequest(TeaModel):
    def __init__(
        self,
        accessibility: str = None,
        description: str = None,
        folder_id: str = None,
        name: str = None,
        options: str = None,
        source: str = None,
        template_id: str = None,
        workspace_id: str = None,
    ):
        self.accessibility = accessibility
        self.description = description
        self.folder_id = folder_id
        self.name = name
        self.options = options
        self.source = source
        self.template_id = template_id
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
        if self.description is not None:
            result['Description'] = self.description
        if self.folder_id is not None:
            result['FolderId'] = self.folder_id
        if self.name is not None:
            result['Name'] = self.name
        if self.options is not None:
            result['Options'] = self.options
        if self.source is not None:
            result['Source'] = self.source
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accessibility') is not None:
            self.accessibility = m.get('Accessibility')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('FolderId') is not None:
            self.folder_id = m.get('FolderId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Options') is not None:
            self.options = m.get('Options')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class CreateExperimentResponseBody(TeaModel):
    def __init__(
        self,
        experiment_id: str = None,
        request_id: str = None,
    ):
        self.experiment_id = experiment_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.experiment_id is not None:
            result['ExperimentId'] = self.experiment_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExperimentId') is not None:
            self.experiment_id = m.get('ExperimentId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateExperimentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateExperimentResponseBody = None,
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
            temp_model = CreateExperimentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateExperimentFolderRequest(TeaModel):
    def __init__(
        self,
        accessibility: str = None,
        name: str = None,
        parent_folder_id: str = None,
        source: str = None,
        workspace_id: str = None,
    ):
        self.accessibility = accessibility
        self.name = name
        self.parent_folder_id = parent_folder_id
        self.source = source
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
        if self.name is not None:
            result['Name'] = self.name
        if self.parent_folder_id is not None:
            result['ParentFolderId'] = self.parent_folder_id
        if self.source is not None:
            result['Source'] = self.source
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accessibility') is not None:
            self.accessibility = m.get('Accessibility')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ParentFolderId') is not None:
            self.parent_folder_id = m.get('ParentFolderId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class CreateExperimentFolderResponseBody(TeaModel):
    def __init__(
        self,
        folder_id: str = None,
        request_id: str = None,
    ):
        self.folder_id = folder_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.folder_id is not None:
            result['FolderId'] = self.folder_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FolderId') is not None:
            self.folder_id = m.get('FolderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateExperimentFolderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateExperimentFolderResponseBody = None,
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
            temp_model = CreateExperimentFolderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateExperimentMigrateValidationRequest(TeaModel):
    def __init__(
        self,
        source_exp_id: int = None,
    ):
        self.source_exp_id = source_exp_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_exp_id is not None:
            result['SourceExpId'] = self.source_exp_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceExpId') is not None:
            self.source_exp_id = m.get('SourceExpId')
        return self


class CreateExperimentMigrateValidationResponseBody(TeaModel):
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


class CreateExperimentMigrateValidationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateExperimentMigrateValidationResponseBody = None,
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
            temp_model = CreateExperimentMigrateValidationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateJobRequest(TeaModel):
    def __init__(
        self,
        execute_type: str = None,
        experiment_id: str = None,
        node_id: str = None,
        options: str = None,
    ):
        self.execute_type = execute_type
        self.experiment_id = experiment_id
        self.node_id = node_id
        self.options = options

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.execute_type is not None:
            result['ExecuteType'] = self.execute_type
        if self.experiment_id is not None:
            result['ExperimentId'] = self.experiment_id
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.options is not None:
            result['Options'] = self.options
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExecuteType') is not None:
            self.execute_type = m.get('ExecuteType')
        if m.get('ExperimentId') is not None:
            self.experiment_id = m.get('ExperimentId')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('Options') is not None:
            self.options = m.get('Options')
        return self


class CreateJobResponseBody(TeaModel):
    def __init__(
        self,
        job_id: str = None,
        request_id: str = None,
    ):
        self.job_id = job_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateJobResponseBody = None,
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
            temp_model = CreateJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteExperimentResponseBody(TeaModel):
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


class DeleteExperimentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteExperimentResponseBody = None,
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
            temp_model = DeleteExperimentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteExperimentFolderResponseBody(TeaModel):
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


class DeleteExperimentFolderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteExperimentFolderResponseBody = None,
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
            temp_model = DeleteExperimentFolderResponseBody()
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
        data: Dict[str, Any] = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetAlgoTreeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAlgoTreeResponseBody = None,
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
            temp_model = GetAlgoTreeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAlgorithmDefRequest(TeaModel):
    def __init__(
        self,
        algo_version: str = None,
        identifier: str = None,
        provider: str = None,
        signature: str = None,
    ):
        self.algo_version = algo_version
        self.identifier = identifier
        self.provider = provider
        self.signature = signature

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algo_version is not None:
            result['AlgoVersion'] = self.algo_version
        if self.identifier is not None:
            result['Identifier'] = self.identifier
        if self.provider is not None:
            result['Provider'] = self.provider
        if self.signature is not None:
            result['Signature'] = self.signature
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlgoVersion') is not None:
            self.algo_version = m.get('AlgoVersion')
        if m.get('Identifier') is not None:
            self.identifier = m.get('Identifier')
        if m.get('Provider') is not None:
            self.provider = m.get('Provider')
        if m.get('Signature') is not None:
            self.signature = m.get('Signature')
        return self


class GetAlgorithmDefResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        spec: Dict[str, Any] = None,
    ):
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
        status_code: int = None,
        body: GetAlgorithmDefResponseBody = None,
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
            temp_model = GetAlgorithmDefResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAlgorithmDefsRequest(TeaModel):
    def __init__(
        self,
        latest_timestamp: str = None,
        range_end: int = None,
        range_start: int = None,
        timestamp: str = None,
    ):
        self.latest_timestamp = latest_timestamp
        self.range_end = range_end
        self.range_start = range_start
        self.timestamp = timestamp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.latest_timestamp is not None:
            result['LatestTimestamp'] = self.latest_timestamp
        if self.range_end is not None:
            result['RangeEnd'] = self.range_end
        if self.range_start is not None:
            result['RangeStart'] = self.range_start
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LatestTimestamp') is not None:
            self.latest_timestamp = m.get('LatestTimestamp')
        if m.get('RangeEnd') is not None:
            self.range_end = m.get('RangeEnd')
        if m.get('RangeStart') is not None:
            self.range_start = m.get('RangeStart')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        return self


class GetAlgorithmDefsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        specs: List[Dict[str, Any]] = None,
    ):
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
        status_code: int = None,
        body: GetAlgorithmDefsResponseBody = None,
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
            temp_model = GetAlgorithmDefsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAlgorithmTreeRequest(TeaModel):
    def __init__(
        self,
        source: str = None,
        workspace_id: str = None,
    ):
        self.source = source
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source is not None:
            result['Source'] = self.source
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class GetAlgorithmTreeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        timestamp: str = None,
        tree: List[Dict[str, Any]] = None,
    ):
        self.request_id = request_id
        self.timestamp = timestamp
        self.tree = tree

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.tree is not None:
            result['Tree'] = self.tree
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('Tree') is not None:
            self.tree = m.get('Tree')
        return self


class GetAlgorithmTreeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAlgorithmTreeResponseBody = None,
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
            temp_model = GetAlgorithmTreeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetExperimentResponseBody(TeaModel):
    def __init__(
        self,
        accessibility: str = None,
        content: str = None,
        creator: str = None,
        description: str = None,
        experiment_id: str = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        name: str = None,
        options: str = None,
        request_id: str = None,
        source: str = None,
        version: int = None,
        workspace_id: str = None,
    ):
        self.accessibility = accessibility
        self.content = content
        self.creator = creator
        self.description = description
        self.experiment_id = experiment_id
        self.gmt_create_time = gmt_create_time
        self.gmt_modified_time = gmt_modified_time
        self.name = name
        self.options = options
        self.request_id = request_id
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
        if self.accessibility is not None:
            result['Accessibility'] = self.accessibility
        if self.content is not None:
            result['Content'] = self.content
        if self.creator is not None:
            result['Creator'] = self.creator
        if self.description is not None:
            result['Description'] = self.description
        if self.experiment_id is not None:
            result['ExperimentId'] = self.experiment_id
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.name is not None:
            result['Name'] = self.name
        if self.options is not None:
            result['Options'] = self.options
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.source is not None:
            result['Source'] = self.source
        if self.version is not None:
            result['Version'] = self.version
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accessibility') is not None:
            self.accessibility = m.get('Accessibility')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ExperimentId') is not None:
            self.experiment_id = m.get('ExperimentId')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Options') is not None:
            self.options = m.get('Options')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class GetExperimentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetExperimentResponseBody = None,
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
            temp_model = GetExperimentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetExperimentFolderChildrenRequest(TeaModel):
    def __init__(
        self,
        accessibility: str = None,
        only_folder: bool = None,
        source: str = None,
        user_id: str = None,
        workspace_id: str = None,
    ):
        self.accessibility = accessibility
        self.only_folder = only_folder
        self.source = source
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
        if self.only_folder is not None:
            result['OnlyFolder'] = self.only_folder
        if self.source is not None:
            result['Source'] = self.source
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accessibility') is not None:
            self.accessibility = m.get('Accessibility')
        if m.get('OnlyFolder') is not None:
            self.only_folder = m.get('OnlyFolder')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class GetExperimentFolderChildrenResponseBodyItems(TeaModel):
    def __init__(
        self,
        empty: bool = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        icon: str = None,
        id: str = None,
        name: str = None,
        type: str = None,
    ):
        self.empty = empty
        self.gmt_create_time = gmt_create_time
        self.gmt_modified_time = gmt_modified_time
        self.icon = icon
        self.id = id
        self.name = name
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.empty is not None:
            result['Empty'] = self.empty
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.icon is not None:
            result['Icon'] = self.icon
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Empty') is not None:
            self.empty = m.get('Empty')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('Icon') is not None:
            self.icon = m.get('Icon')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetExperimentFolderChildrenResponseBody(TeaModel):
    def __init__(
        self,
        items: List[GetExperimentFolderChildrenResponseBodyItems] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.items = items
        self.request_id = request_id
        self.total_count = total_count

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
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = GetExperimentFolderChildrenResponseBodyItems()
                self.items.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class GetExperimentFolderChildrenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetExperimentFolderChildrenResponseBody = None,
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
            temp_model = GetExperimentFolderChildrenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetExperimentMetaResponseBody(TeaModel):
    def __init__(
        self,
        accessibility: str = None,
        creator: str = None,
        description: str = None,
        experiment_id: str = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        name: str = None,
        options: str = None,
        request_id: str = None,
        source: str = None,
        version: str = None,
        workspace_id: str = None,
    ):
        self.accessibility = accessibility
        self.creator = creator
        self.description = description
        self.experiment_id = experiment_id
        self.gmt_create_time = gmt_create_time
        self.gmt_modified_time = gmt_modified_time
        self.name = name
        self.options = options
        self.request_id = request_id
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
        if self.accessibility is not None:
            result['Accessibility'] = self.accessibility
        if self.creator is not None:
            result['Creator'] = self.creator
        if self.description is not None:
            result['Description'] = self.description
        if self.experiment_id is not None:
            result['ExperimentId'] = self.experiment_id
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.name is not None:
            result['Name'] = self.name
        if self.options is not None:
            result['Options'] = self.options
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.source is not None:
            result['Source'] = self.source
        if self.version is not None:
            result['Version'] = self.version
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accessibility') is not None:
            self.accessibility = m.get('Accessibility')
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ExperimentId') is not None:
            self.experiment_id = m.get('ExperimentId')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Options') is not None:
            self.options = m.get('Options')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class GetExperimentMetaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetExperimentMetaResponseBody = None,
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
            temp_model = GetExperimentMetaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetExperimentStatusResponseBodyNodes(TeaModel):
    def __init__(
        self,
        finished_at: str = None,
        job_id: str = None,
        node_id: str = None,
        run_id: str = None,
        run_node_id: str = None,
        started_at: str = None,
        status: str = None,
    ):
        self.finished_at = finished_at
        self.job_id = job_id
        self.node_id = node_id
        self.run_id = run_id
        self.run_node_id = run_node_id
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
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.run_id is not None:
            result['RunId'] = self.run_id
        if self.run_node_id is not None:
            result['RunNodeId'] = self.run_node_id
        if self.started_at is not None:
            result['StartedAt'] = self.started_at
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FinishedAt') is not None:
            self.finished_at = m.get('FinishedAt')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('RunId') is not None:
            self.run_id = m.get('RunId')
        if m.get('RunNodeId') is not None:
            self.run_node_id = m.get('RunNodeId')
        if m.get('StartedAt') is not None:
            self.started_at = m.get('StartedAt')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetExperimentStatusResponseBody(TeaModel):
    def __init__(
        self,
        nodes: List[GetExperimentStatusResponseBodyNodes] = None,
        request_id: str = None,
        status: str = None,
    ):
        self.nodes = nodes
        self.request_id = request_id
        self.status = status

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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.nodes = []
        if m.get('Nodes') is not None:
            for k in m.get('Nodes'):
                temp_model = GetExperimentStatusResponseBodyNodes()
                self.nodes.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetExperimentStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetExperimentStatusResponseBody = None,
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
            temp_model = GetExperimentStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetExperimentVisualizationMetaRequest(TeaModel):
    def __init__(
        self,
        node_ids: str = None,
    ):
        self.node_ids = node_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.node_ids is not None:
            result['NodeIds'] = self.node_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NodeIds') is not None:
            self.node_ids = m.get('NodeIds')
        return self


class GetExperimentVisualizationMetaResponseBodyVisualizationMeta(TeaModel):
    def __init__(
        self,
        meta: str = None,
        node_id: str = None,
        node_name: str = None,
    ):
        self.meta = meta
        self.node_id = node_id
        self.node_name = node_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.meta is not None:
            result['Meta'] = self.meta
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.node_name is not None:
            result['NodeName'] = self.node_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Meta') is not None:
            self.meta = m.get('Meta')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')
        return self


class GetExperimentVisualizationMetaResponseBody(TeaModel):
    def __init__(
        self,
        visualization_meta: List[GetExperimentVisualizationMetaResponseBodyVisualizationMeta] = None,
        request_id: str = None,
    ):
        self.visualization_meta = visualization_meta
        self.request_id = request_id

    def validate(self):
        if self.visualization_meta:
            for k in self.visualization_meta:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['VisualizationMeta'] = []
        if self.visualization_meta is not None:
            for k in self.visualization_meta:
                result['VisualizationMeta'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.visualization_meta = []
        if m.get('VisualizationMeta') is not None:
            for k in m.get('VisualizationMeta'):
                temp_model = GetExperimentVisualizationMetaResponseBodyVisualizationMeta()
                self.visualization_meta.append(temp_model.from_map(k))
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetExperimentVisualizationMetaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetExperimentVisualizationMetaResponseBody = None,
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
            temp_model = GetExperimentVisualizationMetaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetExperimentsStatisticsRequest(TeaModel):
    def __init__(
        self,
        source: str = None,
        workspace_ids: str = None,
    ):
        self.source = source
        self.workspace_ids = workspace_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source is not None:
            result['Source'] = self.source
        if self.workspace_ids is not None:
            result['WorkspaceIds'] = self.workspace_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('WorkspaceIds') is not None:
            self.workspace_ids = m.get('WorkspaceIds')
        return self


class GetExperimentsStatisticsResponseBodyData(TeaModel):
    def __init__(
        self,
        create_count: int = None,
        total_count: int = None,
        workspace_id: str = None,
    ):
        self.create_count = create_count
        self.total_count = total_count
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_count is not None:
            result['CreateCount'] = self.create_count
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateCount') is not None:
            self.create_count = m.get('CreateCount')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class GetExperimentsStatisticsResponseBody(TeaModel):
    def __init__(
        self,
        data: List[GetExperimentsStatisticsResponseBodyData] = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

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
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetExperimentsStatisticsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetExperimentsStatisticsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetExperimentsStatisticsResponseBody = None,
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
            temp_model = GetExperimentsStatisticsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetExperimentsUsersStatisticsRequest(TeaModel):
    def __init__(
        self,
        source: str = None,
        workspace_id: str = None,
    ):
        self.source = source
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source is not None:
            result['Source'] = self.source
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class GetExperimentsUsersStatisticsResponseBodyUsers(TeaModel):
    def __init__(
        self,
        user_id: str = None,
    ):
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class GetExperimentsUsersStatisticsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        users: List[GetExperimentsUsersStatisticsResponseBodyUsers] = None,
    ):
        self.request_id = request_id
        self.users = users

    def validate(self):
        if self.users:
            for k in self.users:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Users'] = []
        if self.users is not None:
            for k in self.users:
                result['Users'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.users = []
        if m.get('Users') is not None:
            for k in m.get('Users'):
                temp_model = GetExperimentsUsersStatisticsResponseBodyUsers()
                self.users.append(temp_model.from_map(k))
        return self


class GetExperimentsUsersStatisticsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetExperimentsUsersStatisticsResponseBody = None,
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
            temp_model = GetExperimentsUsersStatisticsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetImageRequest(TeaModel):
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


class GetImageResponseBodyLabels(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
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
        description: str = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        image_uri: str = None,
        labels: List[GetImageResponseBodyLabels] = None,
        name: str = None,
        operator_create: str = None,
        parent_operator_create: str = None,
        request_id: str = None,
    ):
        self.description = description
        self.gmt_create_time = gmt_create_time
        self.gmt_modified_time = gmt_modified_time
        self.image_uri = image_uri
        self.labels = labels
        self.name = name
        self.operator_create = operator_create
        self.parent_operator_create = parent_operator_create
        self.request_id = request_id

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
        if self.description is not None:
            result['Description'] = self.description
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.image_uri is not None:
            result['ImageUri'] = self.image_uri
        result['Labels'] = []
        if self.labels is not None:
            for k in self.labels:
                result['Labels'].append(k.to_map() if k else None)
        if self.name is not None:
            result['Name'] = self.name
        if self.operator_create is not None:
            result['OperatorCreate'] = self.operator_create
        if self.parent_operator_create is not None:
            result['ParentOperatorCreate'] = self.parent_operator_create
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('ImageUri') is not None:
            self.image_uri = m.get('ImageUri')
        self.labels = []
        if m.get('Labels') is not None:
            for k in m.get('Labels'):
                temp_model = GetImageResponseBodyLabels()
                self.labels.append(temp_model.from_map(k))
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OperatorCreate') is not None:
            self.operator_create = m.get('OperatorCreate')
        if m.get('ParentOperatorCreate') is not None:
            self.parent_operator_create = m.get('ParentOperatorCreate')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetImageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetImageResponseBody = None,
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
        arguments: str = None,
        creator: str = None,
        execute_type: str = None,
        experiment_id: str = None,
        gmt_create_time: str = None,
        job_id: str = None,
        node_id: str = None,
        paiflow_node_id: str = None,
        request_id: str = None,
        run_id: str = None,
        run_info: str = None,
        snapshot: str = None,
        status: str = None,
        workspace_id: str = None,
    ):
        self.arguments = arguments
        self.creator = creator
        self.execute_type = execute_type
        self.experiment_id = experiment_id
        self.gmt_create_time = gmt_create_time
        self.job_id = job_id
        self.node_id = node_id
        self.paiflow_node_id = paiflow_node_id
        self.request_id = request_id
        self.run_id = run_id
        self.run_info = run_info
        self.snapshot = snapshot
        self.status = status
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
        if self.creator is not None:
            result['Creator'] = self.creator
        if self.execute_type is not None:
            result['ExecuteType'] = self.execute_type
        if self.experiment_id is not None:
            result['ExperimentId'] = self.experiment_id
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.paiflow_node_id is not None:
            result['PaiflowNodeId'] = self.paiflow_node_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.run_id is not None:
            result['RunId'] = self.run_id
        if self.run_info is not None:
            result['RunInfo'] = self.run_info
        if self.snapshot is not None:
            result['Snapshot'] = self.snapshot
        if self.status is not None:
            result['Status'] = self.status
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Arguments') is not None:
            self.arguments = m.get('Arguments')
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')
        if m.get('ExecuteType') is not None:
            self.execute_type = m.get('ExecuteType')
        if m.get('ExperimentId') is not None:
            self.experiment_id = m.get('ExperimentId')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('PaiflowNodeId') is not None:
            self.paiflow_node_id = m.get('PaiflowNodeId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RunId') is not None:
            self.run_id = m.get('RunId')
        if m.get('RunInfo') is not None:
            self.run_info = m.get('RunInfo')
        if m.get('Snapshot') is not None:
            self.snapshot = m.get('Snapshot')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class GetJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetJobResponseBody = None,
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
        preview: List[str] = None,
        type: str = None,
    ):
        self.name = name
        self.preview = preview
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.preview is not None:
            result['Preview'] = self.preview
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Preview') is not None:
            self.preview = m.get('Preview')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetMCTableSchemaResponseBody(TeaModel):
    def __init__(
        self,
        columns: List[GetMCTableSchemaResponseBodyColumns] = None,
        partition_columns: List[str] = None,
        request_id: str = None,
    ):
        self.columns = columns
        self.partition_columns = partition_columns
        self.request_id = request_id

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
        result['Columns'] = []
        if self.columns is not None:
            for k in self.columns:
                result['Columns'].append(k.to_map() if k else None)
        if self.partition_columns is not None:
            result['PartitionColumns'] = self.partition_columns
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.columns = []
        if m.get('Columns') is not None:
            for k in m.get('Columns'):
                temp_model = GetMCTableSchemaResponseBodyColumns()
                self.columns.append(temp_model.from_map(k))
        if m.get('PartitionColumns') is not None:
            self.partition_columns = m.get('PartitionColumns')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetMCTableSchemaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetMCTableSchemaResponseBody = None,
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
        col_names: List[str] = None,
        col_types: List[str] = None,
        request_id: str = None,
    ):
        self.col_names = col_names
        self.col_types = col_types
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.col_names is not None:
            result['ColNames'] = self.col_names
        if self.col_types is not None:
            result['ColTypes'] = self.col_types
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ColNames') is not None:
            self.col_names = m.get('ColNames')
        if m.get('ColTypes') is not None:
            self.col_types = m.get('ColTypes')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetNodeInputSchemaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetNodeInputSchemaResponseBody = None,
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
        algo_name: str = None,
        display_name: str = None,
        location_type: str = None,
        node_name: str = None,
        request_id: str = None,
        type: str = None,
        value: Dict[str, Any] = None,
    ):
        self.algo_name = algo_name
        self.display_name = display_name
        self.location_type = location_type
        self.node_name = node_name
        self.request_id = request_id
        self.type = type
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algo_name is not None:
            result['AlgoName'] = self.algo_name
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.location_type is not None:
            result['LocationType'] = self.location_type
        if self.node_name is not None:
            result['NodeName'] = self.node_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.type is not None:
            result['Type'] = self.type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlgoName') is not None:
            self.algo_name = m.get('AlgoName')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('LocationType') is not None:
            self.location_type = m.get('LocationType')
        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetNodeOutputResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetNodeOutputResponseBody = None,
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
        content: str = None,
        request_id: str = None,
        visualization_type: str = None,
    ):
        self.content = content
        self.request_id = request_id
        self.visualization_type = visualization_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.visualization_type is not None:
            result['VisualizationType'] = self.visualization_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('VisualizationType') is not None:
            self.visualization_type = m.get('VisualizationType')
        return self


class GetNodeVisualizationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetNodeVisualizationResponseBody = None,
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
            temp_model = GetNodeVisualizationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTemplateRequest(TeaModel):
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


class GetTemplateResponseBody(TeaModel):
    def __init__(
        self,
        content: str = None,
        description: str = None,
        detail: str = None,
        doc_link: str = None,
        image_link: str = None,
        labels: List[Dict[str, Any]] = None,
        name: str = None,
        request_id: str = None,
        source_id: str = None,
        source_type: str = None,
        template_id: str = None,
        template_type: str = None,
    ):
        self.content = content
        self.description = description
        self.detail = detail
        self.doc_link = doc_link
        self.image_link = image_link
        self.labels = labels
        self.name = name
        self.request_id = request_id
        self.source_id = source_id
        self.source_type = source_type
        self.template_id = template_id
        self.template_type = template_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.name is not None:
            result['Name'] = self.name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.source_id is not None:
            result['SourceId'] = self.source_id
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
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
            temp_model = GetTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAlgoDefsRequestBody(TeaModel):
    def __init__(
        self,
        identifier: str = None,
        provider: str = None,
        signature: str = None,
        version: str = None,
    ):
        self.identifier = identifier
        self.provider = provider
        self.signature = signature
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.identifier is not None:
            result['Identifier'] = self.identifier
        if self.provider is not None:
            result['Provider'] = self.provider
        if self.signature is not None:
            result['Signature'] = self.signature
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Identifier') is not None:
            self.identifier = m.get('Identifier')
        if m.get('Provider') is not None:
            self.provider = m.get('Provider')
        if m.get('Signature') is not None:
            self.signature = m.get('Signature')
        if m.get('Version') is not None:
            self.version = m.get('Version')
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
        data: List[Dict[str, Any]] = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListAlgoDefsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAlgoDefsResponseBody = None,
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
            temp_model = ListAlgoDefsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAuthRolesRequest(TeaModel):
    def __init__(
        self,
        is_generate_token: str = None,
        workspace_id: str = None,
    ):
        self.is_generate_token = is_generate_token
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_generate_token is not None:
            result['IsGenerateToken'] = self.is_generate_token
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsGenerateToken') is not None:
            self.is_generate_token = m.get('IsGenerateToken')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class ListAuthRolesResponseBodyRolesToken(TeaModel):
    def __init__(
        self,
        access_key_id: str = None,
        access_key_secret: str = None,
        expiration: str = None,
        security_token: str = None,
    ):
        self.access_key_id = access_key_id
        self.access_key_secret = access_key_secret
        self.expiration = expiration
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key_id is not None:
            result['AccessKeyId'] = self.access_key_id
        if self.access_key_secret is not None:
            result['AccessKeySecret'] = self.access_key_secret
        if self.expiration is not None:
            result['Expiration'] = self.expiration
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessKeyId') is not None:
            self.access_key_id = m.get('AccessKeyId')
        if m.get('AccessKeySecret') is not None:
            self.access_key_secret = m.get('AccessKeySecret')
        if m.get('Expiration') is not None:
            self.expiration = m.get('Expiration')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class ListAuthRolesResponseBodyRoles(TeaModel):
    def __init__(
        self,
        is_enabled: str = None,
        role_arn: str = None,
        role_name: str = None,
        role_type: str = None,
        token: ListAuthRolesResponseBodyRolesToken = None,
    ):
        self.is_enabled = is_enabled
        self.role_arn = role_arn
        self.role_name = role_name
        self.role_type = role_type
        self.token = token

    def validate(self):
        if self.token:
            self.token.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_enabled is not None:
            result['IsEnabled'] = self.is_enabled
        if self.role_arn is not None:
            result['RoleARN'] = self.role_arn
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        if self.role_type is not None:
            result['RoleType'] = self.role_type
        if self.token is not None:
            result['Token'] = self.token.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsEnabled') is not None:
            self.is_enabled = m.get('IsEnabled')
        if m.get('RoleARN') is not None:
            self.role_arn = m.get('RoleARN')
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        if m.get('RoleType') is not None:
            self.role_type = m.get('RoleType')
        if m.get('Token') is not None:
            temp_model = ListAuthRolesResponseBodyRolesToken()
            self.token = temp_model.from_map(m['Token'])
        return self


class ListAuthRolesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        roles: List[ListAuthRolesResponseBodyRoles] = None,
    ):
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
        status_code: int = None,
        body: ListAuthRolesResponseBody = None,
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
            temp_model = ListAuthRolesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListExperimentsRequest(TeaModel):
    def __init__(
        self,
        creator: str = None,
        experiment_id: str = None,
        name: str = None,
        order: str = None,
        page_number: int = None,
        page_size: int = None,
        sort_by: str = None,
        source: str = None,
        workspace_id: str = None,
    ):
        self.creator = creator
        self.experiment_id = experiment_id
        self.name = name
        self.order = order
        self.page_number = page_number
        self.page_size = page_size
        self.sort_by = sort_by
        self.source = source
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creator is not None:
            result['Creator'] = self.creator
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
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.source is not None:
            result['Source'] = self.source
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')
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
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class ListExperimentsResponseBodyExperiments(TeaModel):
    def __init__(
        self,
        accessibility: str = None,
        creator: str = None,
        description: str = None,
        experiment_id: str = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        name: str = None,
        source: str = None,
        version: int = None,
        workspace_id: str = None,
    ):
        self.accessibility = accessibility
        self.creator = creator
        self.description = description
        self.experiment_id = experiment_id
        self.gmt_create_time = gmt_create_time
        self.gmt_modified_time = gmt_modified_time
        self.name = name
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
        if self.accessibility is not None:
            result['Accessibility'] = self.accessibility
        if self.creator is not None:
            result['Creator'] = self.creator
        if self.description is not None:
            result['Description'] = self.description
        if self.experiment_id is not None:
            result['ExperimentId'] = self.experiment_id
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.name is not None:
            result['Name'] = self.name
        if self.source is not None:
            result['Source'] = self.source
        if self.version is not None:
            result['Version'] = self.version
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accessibility') is not None:
            self.accessibility = m.get('Accessibility')
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ExperimentId') is not None:
            self.experiment_id = m.get('ExperimentId')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
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
        experiments: List[ListExperimentsResponseBodyExperiments] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.experiments = experiments
        self.request_id = request_id
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
        result['Experiments'] = []
        if self.experiments is not None:
            for k in self.experiments:
                result['Experiments'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.experiments = []
        if m.get('Experiments') is not None:
            for k in m.get('Experiments'):
                temp_model = ListExperimentsResponseBodyExperiments()
                self.experiments.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListExperimentsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListExperimentsResponseBody = None,
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
            temp_model = ListExperimentsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListImageLabelsRequest(TeaModel):
    def __init__(
        self,
        image_id: str = None,
        label_filter: str = None,
        label_keys: str = None,
    ):
        self.image_id = image_id
        self.label_filter = label_filter
        self.label_keys = label_keys

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.label_filter is not None:
            result['LabelFilter'] = self.label_filter
        if self.label_keys is not None:
            result['LabelKeys'] = self.label_keys
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('LabelFilter') is not None:
            self.label_filter = m.get('LabelFilter')
        if m.get('LabelKeys') is not None:
            self.label_keys = m.get('LabelKeys')
        return self


class ListImageLabelsResponseBodyLabels(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
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
        labels: List[ListImageLabelsResponseBodyLabels] = None,
        total_count: int = None,
        request_id: str = None,
    ):
        self.labels = labels
        self.total_count = total_count
        self.request_id = request_id

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
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.labels = []
        if m.get('Labels') is not None:
            for k in m.get('Labels'):
                temp_model = ListImageLabelsResponseBodyLabels()
                self.labels.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListImageLabelsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListImageLabelsResponseBody = None,
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
            temp_model = ListImageLabelsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListImagesRequest(TeaModel):
    def __init__(
        self,
        labels: str = None,
        name: str = None,
        order: str = None,
        page_number: int = None,
        page_size: int = None,
        sort_by: str = None,
        verbose: bool = None,
    ):
        self.labels = labels
        self.name = name
        self.order = order
        self.page_number = page_number
        self.page_size = page_size
        self.sort_by = sort_by
        self.verbose = verbose

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.labels is not None:
            result['Labels'] = self.labels
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
        if self.verbose is not None:
            result['Verbose'] = self.verbose
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
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
        if m.get('Verbose') is not None:
            self.verbose = m.get('Verbose')
        return self


class ListImagesResponseBodyImagesLabels(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
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
        description: str = None,
        gmt_create_time: str = None,
        image_id: str = None,
        image_uri: str = None,
        labels: List[ListImagesResponseBodyImagesLabels] = None,
        name: str = None,
    ):
        self.description = description
        self.gmt_create_time = gmt_create_time
        self.image_id = image_id
        self.image_uri = image_uri
        self.labels = labels
        self.name = name

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
        if self.description is not None:
            result['Description'] = self.description
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.image_uri is not None:
            result['ImageUri'] = self.image_uri
        result['Labels'] = []
        if self.labels is not None:
            for k in self.labels:
                result['Labels'].append(k.to_map() if k else None)
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('ImageUri') is not None:
            self.image_uri = m.get('ImageUri')
        self.labels = []
        if m.get('Labels') is not None:
            for k in m.get('Labels'):
                temp_model = ListImagesResponseBodyImagesLabels()
                self.labels.append(temp_model.from_map(k))
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class ListImagesResponseBody(TeaModel):
    def __init__(
        self,
        images: List[ListImagesResponseBodyImages] = None,
        total_count: int = None,
        request_id: str = None,
    ):
        self.images = images
        self.total_count = total_count
        self.request_id = request_id

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
        result['Images'] = []
        if self.images is not None:
            for k in self.images:
                result['Images'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.images = []
        if m.get('Images') is not None:
            for k in m.get('Images'):
                temp_model = ListImagesResponseBodyImages()
                self.images.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListImagesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListImagesResponseBody = None,
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
            temp_model = ListImagesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListJobsRequest(TeaModel):
    def __init__(
        self,
        creator: str = None,
        experiment_id: str = None,
        order: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.creator = creator
        self.experiment_id = experiment_id
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
        if self.creator is not None:
            result['Creator'] = self.creator
        if self.experiment_id is not None:
            result['ExperimentId'] = self.experiment_id
        if self.order is not None:
            result['Order'] = self.order
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')
        if m.get('ExperimentId') is not None:
            self.experiment_id = m.get('ExperimentId')
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
        creator: str = None,
        execute_type: str = None,
        experiment_id: str = None,
        gmt_create_time: str = None,
        job_id: str = None,
        node_id: str = None,
        paiflow_node_id: str = None,
        run_id: str = None,
        status: str = None,
        workspace_id: str = None,
    ):
        self.creator = creator
        self.execute_type = execute_type
        self.experiment_id = experiment_id
        self.gmt_create_time = gmt_create_time
        self.job_id = job_id
        self.node_id = node_id
        self.paiflow_node_id = paiflow_node_id
        self.run_id = run_id
        self.status = status
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creator is not None:
            result['Creator'] = self.creator
        if self.execute_type is not None:
            result['ExecuteType'] = self.execute_type
        if self.experiment_id is not None:
            result['ExperimentId'] = self.experiment_id
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.paiflow_node_id is not None:
            result['PaiflowNodeId'] = self.paiflow_node_id
        if self.run_id is not None:
            result['RunId'] = self.run_id
        if self.status is not None:
            result['Status'] = self.status
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')
        if m.get('ExecuteType') is not None:
            self.execute_type = m.get('ExecuteType')
        if m.get('ExperimentId') is not None:
            self.experiment_id = m.get('ExperimentId')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('PaiflowNodeId') is not None:
            self.paiflow_node_id = m.get('PaiflowNodeId')
        if m.get('RunId') is not None:
            self.run_id = m.get('RunId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class ListJobsResponseBody(TeaModel):
    def __init__(
        self,
        jobs: List[ListJobsResponseBodyJobs] = None,
        request_id: str = None,
    ):
        self.jobs = jobs
        self.request_id = request_id

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
        result['Jobs'] = []
        if self.jobs is not None:
            for k in self.jobs:
                result['Jobs'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.jobs = []
        if m.get('Jobs') is not None:
            for k in m.get('Jobs'):
                temp_model = ListJobsResponseBodyJobs()
                self.jobs.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListJobsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListJobsResponseBody = None,
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
            temp_model = ListJobsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListNodeOutputsResponseBodyOutputs(TeaModel):
    def __init__(
        self,
        algo_name: str = None,
        display_name: str = None,
        location_type: str = None,
        node_name: str = None,
        output_id: str = None,
        output_index: str = None,
        type: str = None,
        value: Dict[str, Any] = None,
    ):
        self.algo_name = algo_name
        self.display_name = display_name
        self.location_type = location_type
        self.node_name = node_name
        self.output_id = output_id
        self.output_index = output_index
        self.type = type
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algo_name is not None:
            result['AlgoName'] = self.algo_name
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.location_type is not None:
            result['LocationType'] = self.location_type
        if self.node_name is not None:
            result['NodeName'] = self.node_name
        if self.output_id is not None:
            result['OutputId'] = self.output_id
        if self.output_index is not None:
            result['OutputIndex'] = self.output_index
        if self.type is not None:
            result['Type'] = self.type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlgoName') is not None:
            self.algo_name = m.get('AlgoName')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('LocationType') is not None:
            self.location_type = m.get('LocationType')
        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')
        if m.get('OutputId') is not None:
            self.output_id = m.get('OutputId')
        if m.get('OutputIndex') is not None:
            self.output_index = m.get('OutputIndex')
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
    ):
        self.outputs = outputs
        self.request_id = request_id

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
        return self


class ListNodeOutputsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListNodeOutputsResponseBody = None,
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
            temp_model = ListNodeOutputsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRecentExperimentsRequest(TeaModel):
    def __init__(
        self,
        order: str = None,
        page_number: int = None,
        page_size: int = None,
        source: str = None,
        type: str = None,
        workspace_id: str = None,
    ):
        self.order = order
        self.page_number = page_number
        self.page_size = page_size
        self.source = source
        self.type = type
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order is not None:
            result['Order'] = self.order
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.source is not None:
            result['Source'] = self.source
        if self.type is not None:
            result['Type'] = self.type
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class ListRecentExperimentsResponseBodyExperiments(TeaModel):
    def __init__(
        self,
        description: str = None,
        experiment_id: str = None,
        modify_cnt: int = None,
        name: str = None,
        recent_gmt_modified_time: str = None,
        source: str = None,
        workspace_id: str = None,
        workspace_name: str = None,
    ):
        self.description = description
        self.experiment_id = experiment_id
        self.modify_cnt = modify_cnt
        self.name = name
        self.recent_gmt_modified_time = recent_gmt_modified_time
        self.source = source
        self.workspace_id = workspace_id
        self.workspace_name = workspace_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.experiment_id is not None:
            result['ExperimentId'] = self.experiment_id
        if self.modify_cnt is not None:
            result['ModifyCnt'] = self.modify_cnt
        if self.name is not None:
            result['Name'] = self.name
        if self.recent_gmt_modified_time is not None:
            result['RecentGmtModifiedTime'] = self.recent_gmt_modified_time
        if self.source is not None:
            result['Source'] = self.source
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        if self.workspace_name is not None:
            result['WorkspaceName'] = self.workspace_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ExperimentId') is not None:
            self.experiment_id = m.get('ExperimentId')
        if m.get('ModifyCnt') is not None:
            self.modify_cnt = m.get('ModifyCnt')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RecentGmtModifiedTime') is not None:
            self.recent_gmt_modified_time = m.get('RecentGmtModifiedTime')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        if m.get('WorkspaceName') is not None:
            self.workspace_name = m.get('WorkspaceName')
        return self


class ListRecentExperimentsResponseBody(TeaModel):
    def __init__(
        self,
        experiments: List[ListRecentExperimentsResponseBodyExperiments] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.experiments = experiments
        self.request_id = request_id
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
        result['Experiments'] = []
        if self.experiments is not None:
            for k in self.experiments:
                result['Experiments'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.experiments = []
        if m.get('Experiments') is not None:
            for k in m.get('Experiments'):
                temp_model = ListRecentExperimentsResponseBodyExperiments()
                self.experiments.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListRecentExperimentsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListRecentExperimentsResponseBody = None,
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
            temp_model = ListRecentExperimentsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTemplatesRequest(TeaModel):
    def __init__(
        self,
        label: str = None,
        list: str = None,
        name: str = None,
        order: str = None,
        page_number: int = None,
        page_size: int = None,
        sort_by: str = None,
        source: str = None,
        tag_id: str = None,
        template_type: str = None,
        type_id: str = None,
        verbose: bool = None,
        workspace_id: str = None,
    ):
        self.label = label
        self.list = list
        self.name = name
        self.order = order
        self.page_number = page_number
        self.page_size = page_size
        self.sort_by = sort_by
        self.source = source
        self.tag_id = tag_id
        self.template_type = template_type
        self.type_id = type_id
        self.verbose = verbose
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label is not None:
            result['Label'] = self.label
        if self.list is not None:
            result['List'] = self.list
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
        if self.source is not None:
            result['Source'] = self.source
        if self.tag_id is not None:
            result['TagId'] = self.tag_id
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        if self.type_id is not None:
            result['TypeId'] = self.type_id
        if self.verbose is not None:
            result['Verbose'] = self.verbose
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('List') is not None:
            self.list = m.get('List')
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
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('TagId') is not None:
            self.tag_id = m.get('TagId')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        if m.get('TypeId') is not None:
            self.type_id = m.get('TypeId')
        if m.get('Verbose') is not None:
            self.verbose = m.get('Verbose')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class ListTemplatesResponseBodyTemplateDataTemplate(TeaModel):
    def __init__(
        self,
        content: str = None,
        creator: str = None,
        description: str = None,
        detail: str = None,
        doc_link: str = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        image_link: str = None,
        labels: List[Dict[str, Any]] = None,
        name: str = None,
        template_id: str = None,
    ):
        self.content = content
        self.creator = creator
        self.description = description
        self.detail = detail
        self.doc_link = doc_link
        self.gmt_create_time = gmt_create_time
        self.gmt_modified_time = gmt_modified_time
        self.image_link = image_link
        self.labels = labels
        self.name = name
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.creator is not None:
            result['Creator'] = self.creator
        if self.description is not None:
            result['Description'] = self.description
        if self.detail is not None:
            result['Detail'] = self.detail
        if self.doc_link is not None:
            result['DocLink'] = self.doc_link
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.image_link is not None:
            result['ImageLink'] = self.image_link
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.name is not None:
            result['Name'] = self.name
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Detail') is not None:
            self.detail = m.get('Detail')
        if m.get('DocLink') is not None:
            self.doc_link = m.get('DocLink')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('ImageLink') is not None:
            self.image_link = m.get('ImageLink')
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
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
        name: str = None,
        type_id: str = None,
    ):
        self.name = name
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
        if self.type_id is not None:
            result['TypeId'] = self.type_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('TypeId') is not None:
            self.type_id = m.get('TypeId')
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
        template_data: List[ListTemplatesResponseBodyTemplateData] = None,
        total_count: int = None,
    ):
        self.request_id = request_id
        self.template_data = template_data
        self.total_count = total_count

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
        result['TemplateData'] = []
        if self.template_data is not None:
            for k in self.template_data:
                result['TemplateData'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.template_data = []
        if m.get('TemplateData') is not None:
            for k in m.get('TemplateData'):
                temp_model = ListTemplatesResponseBodyTemplateData()
                self.template_data.append(temp_model.from_map(k))
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
            temp_model = ListTemplatesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class MigrateExperimentFoldersRequest(TeaModel):
    def __init__(
        self,
        accessibility: str = None,
        is_owner: bool = None,
        workspace_id: str = None,
    ):
        self.accessibility = accessibility
        self.is_owner = is_owner
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
        if self.is_owner is not None:
            result['IsOwner'] = self.is_owner
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accessibility') is not None:
            self.accessibility = m.get('Accessibility')
        if m.get('IsOwner') is not None:
            self.is_owner = m.get('IsOwner')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class MigrateExperimentFoldersResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        folder_id_mapping: Dict[str, dict] = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.folder_id_mapping = folder_id_mapping
        self.message = message
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.folder_id_mapping is not None:
            result['FolderIdMapping'] = self.folder_id_mapping
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('FolderIdMapping') is not None:
            self.folder_id_mapping = m.get('FolderIdMapping')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class MigrateExperimentFoldersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: MigrateExperimentFoldersResponseBody = None,
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
            temp_model = MigrateExperimentFoldersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class MigrateExperimentsRequest(TeaModel):
    def __init__(
        self,
        accessibility: str = None,
        dest_folder_id: str = None,
        is_owner: bool = None,
        source_exp_id: int = None,
        update_if_exists: bool = None,
        workspace_id: str = None,
    ):
        self.accessibility = accessibility
        self.dest_folder_id = dest_folder_id
        self.is_owner = is_owner
        self.source_exp_id = source_exp_id
        self.update_if_exists = update_if_exists
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
        if self.dest_folder_id is not None:
            result['DestFolderId'] = self.dest_folder_id
        if self.is_owner is not None:
            result['IsOwner'] = self.is_owner
        if self.source_exp_id is not None:
            result['SourceExpId'] = self.source_exp_id
        if self.update_if_exists is not None:
            result['UpdateIfExists'] = self.update_if_exists
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accessibility') is not None:
            self.accessibility = m.get('Accessibility')
        if m.get('DestFolderId') is not None:
            self.dest_folder_id = m.get('DestFolderId')
        if m.get('IsOwner') is not None:
            self.is_owner = m.get('IsOwner')
        if m.get('SourceExpId') is not None:
            self.source_exp_id = m.get('SourceExpId')
        if m.get('UpdateIfExists') is not None:
            self.update_if_exists = m.get('UpdateIfExists')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class MigrateExperimentsResponseBodyData(TeaModel):
    def __init__(
        self,
        already_exists: bool = None,
        experiment_id: str = None,
        updated: bool = None,
    ):
        self.already_exists = already_exists
        self.experiment_id = experiment_id
        self.updated = updated

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.already_exists is not None:
            result['AlreadyExists'] = self.already_exists
        if self.experiment_id is not None:
            result['ExperimentId'] = self.experiment_id
        if self.updated is not None:
            result['Updated'] = self.updated
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlreadyExists') is not None:
            self.already_exists = m.get('AlreadyExists')
        if m.get('ExperimentId') is not None:
            self.experiment_id = m.get('ExperimentId')
        if m.get('Updated') is not None:
            self.updated = m.get('Updated')
        return self


class MigrateExperimentsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: MigrateExperimentsResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = MigrateExperimentsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class MigrateExperimentsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: MigrateExperimentsResponseBody = None,
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
            temp_model = MigrateExperimentsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PreviewMCTableRequest(TeaModel):
    def __init__(
        self,
        endpoint: str = None,
        limit: int = None,
        partition: str = None,
        workspace_id: str = None,
    ):
        self.endpoint = endpoint
        self.limit = limit
        self.partition = partition
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.partition is not None:
            result['Partition'] = self.partition
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('Partition') is not None:
            self.partition = m.get('Partition')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class PreviewMCTableResponseBody(TeaModel):
    def __init__(
        self,
        content: List[List[str]] = None,
        request_id: str = None,
    ):
        self.content = content
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class PreviewMCTableResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PreviewMCTableResponseBody = None,
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
            temp_model = PreviewMCTableResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PublishExperimentRequest(TeaModel):
    def __init__(
        self,
        folder_id: str = None,
    ):
        self.folder_id = folder_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.folder_id is not None:
            result['FolderId'] = self.folder_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FolderId') is not None:
            self.folder_id = m.get('FolderId')
        return self


class PublishExperimentResponseBody(TeaModel):
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


class PublishExperimentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PublishExperimentResponseBody = None,
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
            temp_model = PublishExperimentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryExperimentVisualizationDataRequestBody(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        node_id: str = None,
        start_time: str = None,
        visualization_data_ids: List[str] = None,
    ):
        self.end_time = end_time
        self.node_id = node_id
        self.start_time = start_time
        self.visualization_data_ids = visualization_data_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.visualization_data_ids is not None:
            result['VisualizationDataIds'] = self.visualization_data_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('VisualizationDataIds') is not None:
            self.visualization_data_ids = m.get('VisualizationDataIds')
        return self


class QueryExperimentVisualizationDataRequest(TeaModel):
    def __init__(
        self,
        body: List[QueryExperimentVisualizationDataRequestBody] = None,
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
                temp_model = QueryExperimentVisualizationDataRequestBody()
                self.body.append(temp_model.from_map(k))
        return self


class QueryExperimentVisualizationDataResponseBodyVisualizationData(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        data: str = None,
        data_id: str = None,
        node_id: str = None,
    ):
        self.create_time = create_time
        self.data = data
        self.data_id = data_id
        self.node_id = node_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.data is not None:
            result['Data'] = self.data
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        return self


class QueryExperimentVisualizationDataResponseBody(TeaModel):
    def __init__(
        self,
        visualization_data: List[QueryExperimentVisualizationDataResponseBodyVisualizationData] = None,
        request_id: str = None,
    ):
        self.visualization_data = visualization_data
        self.request_id = request_id

    def validate(self):
        if self.visualization_data:
            for k in self.visualization_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['VisualizationData'] = []
        if self.visualization_data is not None:
            for k in self.visualization_data:
                result['VisualizationData'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.visualization_data = []
        if m.get('VisualizationData') is not None:
            for k in m.get('VisualizationData'):
                temp_model = QueryExperimentVisualizationDataResponseBodyVisualizationData()
                self.visualization_data.append(temp_model.from_map(k))
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class QueryExperimentVisualizationDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryExperimentVisualizationDataResponseBody = None,
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
            temp_model = QueryExperimentVisualizationDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveImageResponseBody(TeaModel):
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
        status_code: int = None,
        body: RemoveImageResponseBody = None,
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
            temp_model = RemoveImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveImageLabelsResponseBody(TeaModel):
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
        status_code: int = None,
        body: RemoveImageLabelsResponseBody = None,
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
            temp_model = RemoveImageLabelsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchMCTablesRequest(TeaModel):
    def __init__(
        self,
        keyword: str = None,
        workspace_id: str = None,
    ):
        self.keyword = keyword
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class SearchMCTablesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        tables: List[str] = None,
    ):
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
        status_code: int = None,
        body: SearchMCTablesResponseBody = None,
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
            temp_model = SearchMCTablesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopExperimentResponseBody(TeaModel):
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


class StopExperimentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StopExperimentResponseBody = None,
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
            temp_model = StopExperimentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopJobResponseBody(TeaModel):
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


class StopJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StopJobResponseBody = None,
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
        status_code: int = None,
        body: UpdateExperimentContentResponseBody = None,
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
        status_code: int = None,
        body: UpdateExperimentFolderResponseBody = None,
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
            temp_model = UpdateExperimentFolderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateExperimentMetaRequest(TeaModel):
    def __init__(
        self,
        accessibility: str = None,
        description: str = None,
        folder_id: str = None,
        name: str = None,
        options: str = None,
    ):
        self.accessibility = accessibility
        self.description = description
        self.folder_id = folder_id
        self.name = name
        self.options = options

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accessibility is not None:
            result['Accessibility'] = self.accessibility
        if self.description is not None:
            result['Description'] = self.description
        if self.folder_id is not None:
            result['FolderId'] = self.folder_id
        if self.name is not None:
            result['Name'] = self.name
        if self.options is not None:
            result['Options'] = self.options
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accessibility') is not None:
            self.accessibility = m.get('Accessibility')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('FolderId') is not None:
            self.folder_id = m.get('FolderId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Options') is not None:
            self.options = m.get('Options')
        return self


class UpdateExperimentMetaResponseBody(TeaModel):
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


class UpdateExperimentMetaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateExperimentMetaResponseBody = None,
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
            temp_model = UpdateExperimentMetaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


