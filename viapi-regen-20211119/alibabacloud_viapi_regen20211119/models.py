# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, BinaryIO, List, Any


class CreateDatasetRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        type: str = None,
        workspace_id: int = None,
    ):
        self.description = description
        self.name = name
        self.type = type
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class CreateDatasetResponseBodyData(TeaModel):
    def __init__(
        self,
        description: str = None,
        gmt_create: int = None,
        id: int = None,
        name: str = None,
    ):
        self.description = description
        self.gmt_create = gmt_create
        self.id = id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class CreateDatasetResponseBody(TeaModel):
    def __init__(
        self,
        data: CreateDatasetResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = CreateDatasetResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateDatasetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateDatasetResponseBody = None,
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
            temp_model = CreateDatasetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateLabelsetRequest(TeaModel):
    def __init__(
        self,
        dataset_id: int = None,
        description: str = None,
        name: str = None,
        object_key: str = None,
        pre_label_id: int = None,
        tag_settings: str = None,
        tag_user_list: str = None,
        type: str = None,
        user_oss_url: str = None,
    ):
        self.dataset_id = dataset_id
        self.description = description
        self.name = name
        self.object_key = object_key
        self.pre_label_id = pre_label_id
        self.tag_settings = tag_settings
        self.tag_user_list = tag_user_list
        self.type = type
        self.user_oss_url = user_oss_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_id is not None:
            result['DatasetId'] = self.dataset_id
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.object_key is not None:
            result['ObjectKey'] = self.object_key
        if self.pre_label_id is not None:
            result['PreLabelId'] = self.pre_label_id
        if self.tag_settings is not None:
            result['TagSettings'] = self.tag_settings
        if self.tag_user_list is not None:
            result['TagUserList'] = self.tag_user_list
        if self.type is not None:
            result['Type'] = self.type
        if self.user_oss_url is not None:
            result['UserOssUrl'] = self.user_oss_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetId') is not None:
            self.dataset_id = m.get('DatasetId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ObjectKey') is not None:
            self.object_key = m.get('ObjectKey')
        if m.get('PreLabelId') is not None:
            self.pre_label_id = m.get('PreLabelId')
        if m.get('TagSettings') is not None:
            self.tag_settings = m.get('TagSettings')
        if m.get('TagUserList') is not None:
            self.tag_user_list = m.get('TagUserList')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UserOssUrl') is not None:
            self.user_oss_url = m.get('UserOssUrl')
        return self


class CreateLabelsetResponseBodyData(TeaModel):
    def __init__(
        self,
        description: str = None,
        gmt_create: int = None,
        id: int = None,
        label_type: str = None,
        name: str = None,
        status: str = None,
    ):
        self.description = description
        self.gmt_create = gmt_create
        self.id = id
        self.label_type = label_type
        self.name = name
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.id is not None:
            result['Id'] = self.id
        if self.label_type is not None:
            result['LabelType'] = self.label_type
        if self.name is not None:
            result['Name'] = self.name
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LabelType') is not None:
            self.label_type = m.get('LabelType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class CreateLabelsetResponseBody(TeaModel):
    def __init__(
        self,
        data: CreateLabelsetResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = CreateLabelsetResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateLabelsetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateLabelsetResponseBody = None,
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
            temp_model = CreateLabelsetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateServiceRequest(TeaModel):
    def __init__(
        self,
        authorization_type: str = None,
        authorized_account: str = None,
        description: str = None,
        name: str = None,
        train_task_id: int = None,
    ):
        self.authorization_type = authorization_type
        self.authorized_account = authorized_account
        self.description = description
        self.name = name
        self.train_task_id = train_task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authorization_type is not None:
            result['AuthorizationType'] = self.authorization_type
        if self.authorized_account is not None:
            result['AuthorizedAccount'] = self.authorized_account
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.train_task_id is not None:
            result['TrainTaskId'] = self.train_task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthorizationType') is not None:
            self.authorization_type = m.get('AuthorizationType')
        if m.get('AuthorizedAccount') is not None:
            self.authorized_account = m.get('AuthorizedAccount')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('TrainTaskId') is not None:
            self.train_task_id = m.get('TrainTaskId')
        return self


class CreateServiceResponseBodyData(TeaModel):
    def __init__(
        self,
        authorization_type: str = None,
        authorized_account: str = None,
        gmt_create: int = None,
        id: int = None,
        service_description: str = None,
        service_name: str = None,
        status: str = None,
    ):
        self.authorization_type = authorization_type
        self.authorized_account = authorized_account
        self.gmt_create = gmt_create
        self.id = id
        self.service_description = service_description
        self.service_name = service_name
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authorization_type is not None:
            result['AuthorizationType'] = self.authorization_type
        if self.authorized_account is not None:
            result['AuthorizedAccount'] = self.authorized_account
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.id is not None:
            result['Id'] = self.id
        if self.service_description is not None:
            result['ServiceDescription'] = self.service_description
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthorizationType') is not None:
            self.authorization_type = m.get('AuthorizationType')
        if m.get('AuthorizedAccount') is not None:
            self.authorized_account = m.get('AuthorizedAccount')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ServiceDescription') is not None:
            self.service_description = m.get('ServiceDescription')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class CreateServiceResponseBody(TeaModel):
    def __init__(
        self,
        data: CreateServiceResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = CreateServiceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateServiceResponseBody = None,
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
            temp_model = CreateServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTagTaskRequest(TeaModel):
    def __init__(
        self,
        labelset_id: int = None,
    ):
        self.labelset_id = labelset_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.labelset_id is not None:
            result['LabelsetId'] = self.labelset_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LabelsetId') is not None:
            self.labelset_id = m.get('LabelsetId')
        return self


class CreateTagTaskResponseBodyData(TeaModel):
    def __init__(
        self,
        description: str = None,
        gmt_create: int = None,
        id: int = None,
        label_type: str = None,
        name: str = None,
        status: str = None,
    ):
        self.description = description
        self.gmt_create = gmt_create
        self.id = id
        self.label_type = label_type
        self.name = name
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.id is not None:
            result['Id'] = self.id
        if self.label_type is not None:
            result['LabelType'] = self.label_type
        if self.name is not None:
            result['Name'] = self.name
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LabelType') is not None:
            self.label_type = m.get('LabelType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class CreateTagTaskResponseBody(TeaModel):
    def __init__(
        self,
        data: CreateTagTaskResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = CreateTagTaskResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateTagTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateTagTaskResponseBody = None,
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
            temp_model = CreateTagTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTrainTaskRequest(TeaModel):
    def __init__(
        self,
        advanced_parameters: str = None,
        dataset_ids: str = None,
        description: str = None,
        label_ids: str = None,
        name: str = None,
        pre_train_task_id: int = None,
        train_mode: str = None,
        workspace_id: int = None,
    ):
        self.advanced_parameters = advanced_parameters
        self.dataset_ids = dataset_ids
        self.description = description
        self.label_ids = label_ids
        self.name = name
        self.pre_train_task_id = pre_train_task_id
        self.train_mode = train_mode
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.advanced_parameters is not None:
            result['AdvancedParameters'] = self.advanced_parameters
        if self.dataset_ids is not None:
            result['DatasetIds'] = self.dataset_ids
        if self.description is not None:
            result['Description'] = self.description
        if self.label_ids is not None:
            result['LabelIds'] = self.label_ids
        if self.name is not None:
            result['Name'] = self.name
        if self.pre_train_task_id is not None:
            result['PreTrainTaskId'] = self.pre_train_task_id
        if self.train_mode is not None:
            result['TrainMode'] = self.train_mode
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdvancedParameters') is not None:
            self.advanced_parameters = m.get('AdvancedParameters')
        if m.get('DatasetIds') is not None:
            self.dataset_ids = m.get('DatasetIds')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('LabelIds') is not None:
            self.label_ids = m.get('LabelIds')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PreTrainTaskId') is not None:
            self.pre_train_task_id = m.get('PreTrainTaskId')
        if m.get('TrainMode') is not None:
            self.train_mode = m.get('TrainMode')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class CreateTrainTaskResponseBodyData(TeaModel):
    def __init__(
        self,
        advanced_parameters: str = None,
        dataset_id: int = None,
        dataset_name: str = None,
        description: str = None,
        gmt_create: int = None,
        id: int = None,
        label_id: int = None,
        label_name: str = None,
        model_effect: str = None,
        model_id: int = None,
        rely_on_task_id: int = None,
        rely_on_task_name: str = None,
        task_name: str = None,
        train_mode: str = None,
        train_status: str = None,
    ):
        self.advanced_parameters = advanced_parameters
        self.dataset_id = dataset_id
        self.dataset_name = dataset_name
        self.description = description
        self.gmt_create = gmt_create
        self.id = id
        self.label_id = label_id
        self.label_name = label_name
        self.model_effect = model_effect
        self.model_id = model_id
        self.rely_on_task_id = rely_on_task_id
        self.rely_on_task_name = rely_on_task_name
        self.task_name = task_name
        self.train_mode = train_mode
        self.train_status = train_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.advanced_parameters is not None:
            result['AdvancedParameters'] = self.advanced_parameters
        if self.dataset_id is not None:
            result['DatasetId'] = self.dataset_id
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.description is not None:
            result['Description'] = self.description
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.id is not None:
            result['Id'] = self.id
        if self.label_id is not None:
            result['LabelId'] = self.label_id
        if self.label_name is not None:
            result['LabelName'] = self.label_name
        if self.model_effect is not None:
            result['ModelEffect'] = self.model_effect
        if self.model_id is not None:
            result['ModelId'] = self.model_id
        if self.rely_on_task_id is not None:
            result['RelyOnTaskId'] = self.rely_on_task_id
        if self.rely_on_task_name is not None:
            result['RelyOnTaskName'] = self.rely_on_task_name
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.train_mode is not None:
            result['TrainMode'] = self.train_mode
        if self.train_status is not None:
            result['TrainStatus'] = self.train_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdvancedParameters') is not None:
            self.advanced_parameters = m.get('AdvancedParameters')
        if m.get('DatasetId') is not None:
            self.dataset_id = m.get('DatasetId')
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LabelId') is not None:
            self.label_id = m.get('LabelId')
        if m.get('LabelName') is not None:
            self.label_name = m.get('LabelName')
        if m.get('ModelEffect') is not None:
            self.model_effect = m.get('ModelEffect')
        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')
        if m.get('RelyOnTaskId') is not None:
            self.rely_on_task_id = m.get('RelyOnTaskId')
        if m.get('RelyOnTaskName') is not None:
            self.rely_on_task_name = m.get('RelyOnTaskName')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('TrainMode') is not None:
            self.train_mode = m.get('TrainMode')
        if m.get('TrainStatus') is not None:
            self.train_status = m.get('TrainStatus')
        return self


class CreateTrainTaskResponseBody(TeaModel):
    def __init__(
        self,
        data: CreateTrainTaskResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = CreateTrainTaskResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateTrainTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateTrainTaskResponseBody = None,
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
            temp_model = CreateTrainTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateWorkspaceRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        type: str = None,
    ):
        self.description = description
        self.name = name
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreateWorkspaceResponseBodyData(TeaModel):
    def __init__(
        self,
        description: str = None,
        gmt_create: int = None,
        id: int = None,
        name: str = None,
        type: str = None,
    ):
        self.description = description
        self.gmt_create = gmt_create
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
        if self.description is not None:
            result['Description'] = self.description
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreateWorkspaceResponseBody(TeaModel):
    def __init__(
        self,
        data: CreateWorkspaceResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = CreateWorkspaceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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
            temp_model = CreateWorkspaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CustomizeClassifyImageRequest(TeaModel):
    def __init__(
        self,
        image_url: str = None,
        service_id: str = None,
    ):
        self.image_url = image_url
        self.service_id = service_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        return self


class CustomizeClassifyImageAdvanceRequest(TeaModel):
    def __init__(
        self,
        image_url_object: BinaryIO = None,
        service_id: str = None,
    ):
        self.image_url_object = image_url_object
        self.service_id = service_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_url_object is not None:
            result['ImageUrl'] = self.image_url_object
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageUrl') is not None:
            self.image_url_object = m.get('ImageUrl')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        return self


class CustomizeClassifyImageResponseBodyData(TeaModel):
    def __init__(
        self,
        category: str = None,
        score: float = None,
    ):
        self.category = category
        self.score = score

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.score is not None:
            result['Score'] = self.score
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        return self


class CustomizeClassifyImageResponseBody(TeaModel):
    def __init__(
        self,
        data: CustomizeClassifyImageResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = CustomizeClassifyImageResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CustomizeClassifyImageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CustomizeClassifyImageResponseBody = None,
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
            temp_model = CustomizeClassifyImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CustomizeDetectImageRequest(TeaModel):
    def __init__(
        self,
        image_url: str = None,
        service_id: str = None,
    ):
        self.image_url = image_url
        self.service_id = service_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        return self


class CustomizeDetectImageAdvanceRequest(TeaModel):
    def __init__(
        self,
        image_url_object: BinaryIO = None,
        service_id: str = None,
    ):
        self.image_url_object = image_url_object
        self.service_id = service_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_url_object is not None:
            result['ImageUrl'] = self.image_url_object
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageUrl') is not None:
            self.image_url_object = m.get('ImageUrl')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        return self


class CustomizeDetectImageResponseBodyDataElementsBoxes(TeaModel):
    def __init__(
        self,
        height: float = None,
        width: float = None,
        x: float = None,
        y: float = None,
    ):
        self.height = height
        self.width = width
        self.x = x
        self.y = y

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.height is not None:
            result['Height'] = self.height
        if self.width is not None:
            result['Width'] = self.width
        if self.x is not None:
            result['X'] = self.x
        if self.y is not None:
            result['Y'] = self.y
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('X') is not None:
            self.x = m.get('X')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        return self


class CustomizeDetectImageResponseBodyDataElements(TeaModel):
    def __init__(
        self,
        boxes: CustomizeDetectImageResponseBodyDataElementsBoxes = None,
        category: str = None,
        score: float = None,
    ):
        self.boxes = boxes
        self.category = category
        self.score = score

    def validate(self):
        if self.boxes:
            self.boxes.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.boxes is not None:
            result['Boxes'] = self.boxes.to_map()
        if self.category is not None:
            result['Category'] = self.category
        if self.score is not None:
            result['Score'] = self.score
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Boxes') is not None:
            temp_model = CustomizeDetectImageResponseBodyDataElementsBoxes()
            self.boxes = temp_model.from_map(m['Boxes'])
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        return self


class CustomizeDetectImageResponseBodyData(TeaModel):
    def __init__(
        self,
        elements: List[CustomizeDetectImageResponseBodyDataElements] = None,
    ):
        self.elements = elements

    def validate(self):
        if self.elements:
            for k in self.elements:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Elements'] = []
        if self.elements is not None:
            for k in self.elements:
                result['Elements'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.elements = []
        if m.get('Elements') is not None:
            for k in m.get('Elements'):
                temp_model = CustomizeDetectImageResponseBodyDataElements()
                self.elements.append(temp_model.from_map(k))
        return self


class CustomizeDetectImageResponseBody(TeaModel):
    def __init__(
        self,
        data: CustomizeDetectImageResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = CustomizeDetectImageResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CustomizeDetectImageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CustomizeDetectImageResponseBody = None,
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
            temp_model = CustomizeDetectImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CustomizeInstanceSegmentImageRequest(TeaModel):
    def __init__(
        self,
        image_url: str = None,
        service_id: str = None,
    ):
        self.image_url = image_url
        self.service_id = service_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        return self


class CustomizeInstanceSegmentImageAdvanceRequest(TeaModel):
    def __init__(
        self,
        image_url_object: BinaryIO = None,
        service_id: str = None,
    ):
        self.image_url_object = image_url_object
        self.service_id = service_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_url_object is not None:
            result['ImageUrl'] = self.image_url_object
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageUrl') is not None:
            self.image_url_object = m.get('ImageUrl')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        return self


class CustomizeInstanceSegmentImageResponseBodyDataElementsBoxes(TeaModel):
    def __init__(
        self,
        height: int = None,
        width: int = None,
        x: int = None,
        y: int = None,
    ):
        self.height = height
        self.width = width
        self.x = x
        self.y = y

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.height is not None:
            result['Height'] = self.height
        if self.width is not None:
            result['Width'] = self.width
        if self.x is not None:
            result['X'] = self.x
        if self.y is not None:
            result['Y'] = self.y
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('X') is not None:
            self.x = m.get('X')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        return self


class CustomizeInstanceSegmentImageResponseBodyDataElementsContours(TeaModel):
    def __init__(
        self,
        x: int = None,
        y: int = None,
    ):
        self.x = x
        self.y = y

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.x is not None:
            result['X'] = self.x
        if self.y is not None:
            result['Y'] = self.y
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('X') is not None:
            self.x = m.get('X')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        return self


class CustomizeInstanceSegmentImageResponseBodyDataElementsMask(TeaModel):
    def __init__(
        self,
        counts: str = None,
        sizes: List[int] = None,
    ):
        self.counts = counts
        self.sizes = sizes

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.counts is not None:
            result['Counts'] = self.counts
        if self.sizes is not None:
            result['Sizes'] = self.sizes
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Counts') is not None:
            self.counts = m.get('Counts')
        if m.get('Sizes') is not None:
            self.sizes = m.get('Sizes')
        return self


class CustomizeInstanceSegmentImageResponseBodyDataElements(TeaModel):
    def __init__(
        self,
        boxes: CustomizeInstanceSegmentImageResponseBodyDataElementsBoxes = None,
        category: str = None,
        contours: List[CustomizeInstanceSegmentImageResponseBodyDataElementsContours] = None,
        mask: CustomizeInstanceSegmentImageResponseBodyDataElementsMask = None,
        score: float = None,
    ):
        self.boxes = boxes
        self.category = category
        self.contours = contours
        self.mask = mask
        self.score = score

    def validate(self):
        if self.boxes:
            self.boxes.validate()
        if self.contours:
            for k in self.contours:
                if k:
                    k.validate()
        if self.mask:
            self.mask.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.boxes is not None:
            result['Boxes'] = self.boxes.to_map()
        if self.category is not None:
            result['Category'] = self.category
        result['Contours'] = []
        if self.contours is not None:
            for k in self.contours:
                result['Contours'].append(k.to_map() if k else None)
        if self.mask is not None:
            result['Mask'] = self.mask.to_map()
        if self.score is not None:
            result['Score'] = self.score
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Boxes') is not None:
            temp_model = CustomizeInstanceSegmentImageResponseBodyDataElementsBoxes()
            self.boxes = temp_model.from_map(m['Boxes'])
        if m.get('Category') is not None:
            self.category = m.get('Category')
        self.contours = []
        if m.get('Contours') is not None:
            for k in m.get('Contours'):
                temp_model = CustomizeInstanceSegmentImageResponseBodyDataElementsContours()
                self.contours.append(temp_model.from_map(k))
        if m.get('Mask') is not None:
            temp_model = CustomizeInstanceSegmentImageResponseBodyDataElementsMask()
            self.mask = temp_model.from_map(m['Mask'])
        if m.get('Score') is not None:
            self.score = m.get('Score')
        return self


class CustomizeInstanceSegmentImageResponseBodyData(TeaModel):
    def __init__(
        self,
        elements: List[CustomizeInstanceSegmentImageResponseBodyDataElements] = None,
    ):
        self.elements = elements

    def validate(self):
        if self.elements:
            for k in self.elements:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Elements'] = []
        if self.elements is not None:
            for k in self.elements:
                result['Elements'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.elements = []
        if m.get('Elements') is not None:
            for k in m.get('Elements'):
                temp_model = CustomizeInstanceSegmentImageResponseBodyDataElements()
                self.elements.append(temp_model.from_map(k))
        return self


class CustomizeInstanceSegmentImageResponseBody(TeaModel):
    def __init__(
        self,
        data: CustomizeInstanceSegmentImageResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = CustomizeInstanceSegmentImageResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CustomizeInstanceSegmentImageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CustomizeInstanceSegmentImageResponseBody = None,
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
            temp_model = CustomizeInstanceSegmentImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DebugServiceRequest(TeaModel):
    def __init__(
        self,
        id: int = None,
        param: str = None,
    ):
        self.id = id
        self.param = param

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.param is not None:
            result['Param'] = self.param
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Param') is not None:
            self.param = m.get('Param')
        return self


class DebugServiceResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
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


class DebugServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DebugServiceResponseBody = None,
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
            temp_model = DebugServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDataReflowDataRequest(TeaModel):
    def __init__(
        self,
        id: int = None,
        service_id: int = None,
    ):
        self.id = id
        self.service_id = service_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        return self


class DeleteDataReflowDataResponseBodyData(TeaModel):
    def __init__(
        self,
        gmt_modified: int = None,
        id: int = None,
        service_id: int = None,
        status: str = None,
    ):
        self.gmt_modified = gmt_modified
        self.id = id
        self.service_id = service_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DeleteDataReflowDataResponseBody(TeaModel):
    def __init__(
        self,
        data: DeleteDataReflowDataResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = DeleteDataReflowDataResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteDataReflowDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteDataReflowDataResponseBody = None,
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
            temp_model = DeleteDataReflowDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDatasetRequest(TeaModel):
    def __init__(
        self,
        id: int = None,
    ):
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DeleteDatasetResponseBodyData(TeaModel):
    def __init__(
        self,
        description: str = None,
        gmt_create: int = None,
        id: int = None,
        name: str = None,
    ):
        self.description = description
        self.gmt_create = gmt_create
        self.id = id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DeleteDatasetResponseBody(TeaModel):
    def __init__(
        self,
        data: DeleteDatasetResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = DeleteDatasetResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteDatasetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteDatasetResponseBody = None,
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
            temp_model = DeleteDatasetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteLabelsetRequest(TeaModel):
    def __init__(
        self,
        id: int = None,
    ):
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DeleteLabelsetResponseBodyData(TeaModel):
    def __init__(
        self,
        description: str = None,
        gmt_create: int = None,
        id: int = None,
        label_type: str = None,
        name: str = None,
        status: str = None,
    ):
        self.description = description
        self.gmt_create = gmt_create
        self.id = id
        self.label_type = label_type
        self.name = name
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.id is not None:
            result['Id'] = self.id
        if self.label_type is not None:
            result['LabelType'] = self.label_type
        if self.name is not None:
            result['Name'] = self.name
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LabelType') is not None:
            self.label_type = m.get('LabelType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DeleteLabelsetResponseBody(TeaModel):
    def __init__(
        self,
        data: DeleteLabelsetResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = DeleteLabelsetResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteLabelsetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteLabelsetResponseBody = None,
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
            temp_model = DeleteLabelsetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteLabelsetDataRequest(TeaModel):
    def __init__(
        self,
        id: int = None,
        label_id: int = None,
    ):
        self.id = id
        self.label_id = label_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.label_id is not None:
            result['LabelId'] = self.label_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LabelId') is not None:
            self.label_id = m.get('LabelId')
        return self


class DeleteLabelsetDataResponseBodyData(TeaModel):
    def __init__(
        self,
        description: str = None,
        gmt_create: int = None,
        id: int = None,
        label_type: str = None,
        name: str = None,
        status: str = None,
        total: int = None,
    ):
        self.description = description
        self.gmt_create = gmt_create
        self.id = id
        self.label_type = label_type
        self.name = name
        self.status = status
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.id is not None:
            result['Id'] = self.id
        if self.label_type is not None:
            result['LabelType'] = self.label_type
        if self.name is not None:
            result['Name'] = self.name
        if self.status is not None:
            result['Status'] = self.status
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LabelType') is not None:
            self.label_type = m.get('LabelType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class DeleteLabelsetDataResponseBody(TeaModel):
    def __init__(
        self,
        data: DeleteLabelsetDataResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = DeleteLabelsetDataResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteLabelsetDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteLabelsetDataResponseBody = None,
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
            temp_model = DeleteLabelsetDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteServiceRequest(TeaModel):
    def __init__(
        self,
        id: int = None,
    ):
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DeleteServiceResponseBodyData(TeaModel):
    def __init__(
        self,
        id: int = None,
    ):
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DeleteServiceResponseBody(TeaModel):
    def __init__(
        self,
        data: DeleteServiceResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = DeleteServiceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteServiceResponseBody = None,
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
            temp_model = DeleteServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteTrainTaskRequest(TeaModel):
    def __init__(
        self,
        id: int = None,
    ):
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DeleteTrainTaskResponseBodyData(TeaModel):
    def __init__(
        self,
        dataset_id: int = None,
        dataset_name: str = None,
        description: str = None,
        gmt_create: int = None,
        id: int = None,
        label_id: int = None,
        label_name: str = None,
        model_effect: str = None,
        model_id: int = None,
        task_name: str = None,
        train_mode: str = None,
        train_status: str = None,
    ):
        self.dataset_id = dataset_id
        self.dataset_name = dataset_name
        self.description = description
        self.gmt_create = gmt_create
        self.id = id
        self.label_id = label_id
        self.label_name = label_name
        self.model_effect = model_effect
        self.model_id = model_id
        self.task_name = task_name
        self.train_mode = train_mode
        self.train_status = train_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_id is not None:
            result['DatasetId'] = self.dataset_id
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.description is not None:
            result['Description'] = self.description
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.id is not None:
            result['Id'] = self.id
        if self.label_id is not None:
            result['LabelId'] = self.label_id
        if self.label_name is not None:
            result['LabelName'] = self.label_name
        if self.model_effect is not None:
            result['ModelEffect'] = self.model_effect
        if self.model_id is not None:
            result['ModelId'] = self.model_id
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.train_mode is not None:
            result['TrainMode'] = self.train_mode
        if self.train_status is not None:
            result['TrainStatus'] = self.train_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetId') is not None:
            self.dataset_id = m.get('DatasetId')
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LabelId') is not None:
            self.label_id = m.get('LabelId')
        if m.get('LabelName') is not None:
            self.label_name = m.get('LabelName')
        if m.get('ModelEffect') is not None:
            self.model_effect = m.get('ModelEffect')
        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('TrainMode') is not None:
            self.train_mode = m.get('TrainMode')
        if m.get('TrainStatus') is not None:
            self.train_status = m.get('TrainStatus')
        return self


class DeleteTrainTaskResponseBody(TeaModel):
    def __init__(
        self,
        data: DeleteTrainTaskResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = DeleteTrainTaskResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteTrainTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteTrainTaskResponseBody = None,
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
            temp_model = DeleteTrainTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteWorkspaceRequest(TeaModel):
    def __init__(
        self,
        id: int = None,
    ):
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DeleteWorkspaceResponseBodyData(TeaModel):
    def __init__(
        self,
        description: str = None,
        gmt_create: int = None,
        id: int = None,
        name: str = None,
        type: str = None,
    ):
        self.description = description
        self.gmt_create = gmt_create
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
        if self.description is not None:
            result['Description'] = self.description
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DeleteWorkspaceResponseBody(TeaModel):
    def __init__(
        self,
        data: DeleteWorkspaceResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = DeleteWorkspaceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
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
            temp_model = DeleteWorkspaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableDataReflowRequest(TeaModel):
    def __init__(
        self,
        service_id: int = None,
    ):
        self.service_id = service_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        return self


class DisableDataReflowResponseBodyData(TeaModel):
    def __init__(
        self,
        enable_data_reflow_flag: bool = None,
        service_id: int = None,
    ):
        self.enable_data_reflow_flag = enable_data_reflow_flag
        self.service_id = service_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_data_reflow_flag is not None:
            result['EnableDataReflowFlag'] = self.enable_data_reflow_flag
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableDataReflowFlag') is not None:
            self.enable_data_reflow_flag = m.get('EnableDataReflowFlag')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        return self


class DisableDataReflowResponseBody(TeaModel):
    def __init__(
        self,
        data: DisableDataReflowResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = DisableDataReflowResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DisableDataReflowResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DisableDataReflowResponseBody = None,
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
            temp_model = DisableDataReflowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DownloadFileNameListRequest(TeaModel):
    def __init__(
        self,
        dataset_id: int = None,
        identity: str = None,
    ):
        self.dataset_id = dataset_id
        self.identity = identity

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_id is not None:
            result['DatasetId'] = self.dataset_id
        if self.identity is not None:
            result['Identity'] = self.identity
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetId') is not None:
            self.dataset_id = m.get('DatasetId')
        if m.get('Identity') is not None:
            self.identity = m.get('Identity')
        return self


class DownloadFileNameListResponseBodyData(TeaModel):
    def __init__(
        self,
        oss_http_url: str = None,
    ):
        self.oss_http_url = oss_http_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.oss_http_url is not None:
            result['OssHttpUrl'] = self.oss_http_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OssHttpUrl') is not None:
            self.oss_http_url = m.get('OssHttpUrl')
        return self


class DownloadFileNameListResponseBody(TeaModel):
    def __init__(
        self,
        data: DownloadFileNameListResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = DownloadFileNameListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DownloadFileNameListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DownloadFileNameListResponseBody = None,
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
            temp_model = DownloadFileNameListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DownloadLabelFileRequest(TeaModel):
    def __init__(
        self,
        label_id: int = None,
    ):
        self.label_id = label_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label_id is not None:
            result['LabelId'] = self.label_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LabelId') is not None:
            self.label_id = m.get('LabelId')
        return self


class DownloadLabelFileResponseBodyData(TeaModel):
    def __init__(
        self,
        oss_http_url: str = None,
    ):
        self.oss_http_url = oss_http_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.oss_http_url is not None:
            result['OssHttpUrl'] = self.oss_http_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OssHttpUrl') is not None:
            self.oss_http_url = m.get('OssHttpUrl')
        return self


class DownloadLabelFileResponseBody(TeaModel):
    def __init__(
        self,
        data: DownloadLabelFileResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = DownloadLabelFileResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DownloadLabelFileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DownloadLabelFileResponseBody = None,
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
            temp_model = DownloadLabelFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableDataReflowRequest(TeaModel):
    def __init__(
        self,
        data_reflow_oss_path: str = None,
        data_reflow_rate: int = None,
        service_id: int = None,
    ):
        self.data_reflow_oss_path = data_reflow_oss_path
        self.data_reflow_rate = data_reflow_rate
        self.service_id = service_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_reflow_oss_path is not None:
            result['DataReflowOssPath'] = self.data_reflow_oss_path
        if self.data_reflow_rate is not None:
            result['DataReflowRate'] = self.data_reflow_rate
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataReflowOssPath') is not None:
            self.data_reflow_oss_path = m.get('DataReflowOssPath')
        if m.get('DataReflowRate') is not None:
            self.data_reflow_rate = m.get('DataReflowRate')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        return self


class EnableDataReflowResponseBodyData(TeaModel):
    def __init__(
        self,
        data_reflow_oss_path: str = None,
        data_reflow_rate: int = None,
        enable_data_reflow_flag: bool = None,
        service_id: int = None,
    ):
        self.data_reflow_oss_path = data_reflow_oss_path
        self.data_reflow_rate = data_reflow_rate
        self.enable_data_reflow_flag = enable_data_reflow_flag
        self.service_id = service_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_reflow_oss_path is not None:
            result['DataReflowOssPath'] = self.data_reflow_oss_path
        if self.data_reflow_rate is not None:
            result['DataReflowRate'] = self.data_reflow_rate
        if self.enable_data_reflow_flag is not None:
            result['EnableDataReflowFlag'] = self.enable_data_reflow_flag
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataReflowOssPath') is not None:
            self.data_reflow_oss_path = m.get('DataReflowOssPath')
        if m.get('DataReflowRate') is not None:
            self.data_reflow_rate = m.get('DataReflowRate')
        if m.get('EnableDataReflowFlag') is not None:
            self.enable_data_reflow_flag = m.get('EnableDataReflowFlag')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        return self


class EnableDataReflowResponseBody(TeaModel):
    def __init__(
        self,
        data: EnableDataReflowResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = EnableDataReflowResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class EnableDataReflowResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: EnableDataReflowResponseBody = None,
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
            temp_model = EnableDataReflowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExportDataReflowDataListRequest(TeaModel):
    def __init__(
        self,
        category: str = None,
        end_time: int = None,
        file_type: str = None,
        image_name: str = None,
        service_id: int = None,
        start_time: int = None,
    ):
        self.category = category
        self.end_time = end_time
        self.file_type = file_type
        self.image_name = image_name
        self.service_id = service_id
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.file_type is not None:
            result['FileType'] = self.file_type
        if self.image_name is not None:
            result['ImageName'] = self.image_name
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')
        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class ExportDataReflowDataListResponseBodyData(TeaModel):
    def __init__(
        self,
        oss_http_url: str = None,
    ):
        self.oss_http_url = oss_http_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.oss_http_url is not None:
            result['OssHttpUrl'] = self.oss_http_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OssHttpUrl') is not None:
            self.oss_http_url = m.get('OssHttpUrl')
        return self


class ExportDataReflowDataListResponseBody(TeaModel):
    def __init__(
        self,
        data: ExportDataReflowDataListResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = ExportDataReflowDataListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ExportDataReflowDataListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ExportDataReflowDataListResponseBody = None,
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
            temp_model = ExportDataReflowDataListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDatasetRequest(TeaModel):
    def __init__(
        self,
        id: int = None,
    ):
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class GetDatasetResponseBodyData(TeaModel):
    def __init__(
        self,
        description: str = None,
        gmt_create: int = None,
        id: int = None,
        name: str = None,
        oss_url: str = None,
        owner_type: str = None,
        total: int = None,
    ):
        self.description = description
        self.gmt_create = gmt_create
        self.id = id
        self.name = name
        self.oss_url = oss_url
        self.owner_type = owner_type
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.oss_url is not None:
            result['OssUrl'] = self.oss_url
        if self.owner_type is not None:
            result['OwnerType'] = self.owner_type
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OssUrl') is not None:
            self.oss_url = m.get('OssUrl')
        if m.get('OwnerType') is not None:
            self.owner_type = m.get('OwnerType')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class GetDatasetResponseBody(TeaModel):
    def __init__(
        self,
        data: GetDatasetResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GetDatasetResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetDatasetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDatasetResponseBody = None,
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
            temp_model = GetDatasetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDiffCountLabelsetAndDatasetRequest(TeaModel):
    def __init__(
        self,
        labelset_id: int = None,
    ):
        self.labelset_id = labelset_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.labelset_id is not None:
            result['LabelsetId'] = self.labelset_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LabelsetId') is not None:
            self.labelset_id = m.get('LabelsetId')
        return self


class GetDiffCountLabelsetAndDatasetResponseBodyData(TeaModel):
    def __init__(
        self,
        diff_count: int = None,
    ):
        self.diff_count = diff_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.diff_count is not None:
            result['DiffCount'] = self.diff_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiffCount') is not None:
            self.diff_count = m.get('DiffCount')
        return self


class GetDiffCountLabelsetAndDatasetResponseBody(TeaModel):
    def __init__(
        self,
        data: GetDiffCountLabelsetAndDatasetResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GetDiffCountLabelsetAndDatasetResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetDiffCountLabelsetAndDatasetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDiffCountLabelsetAndDatasetResponseBody = None,
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
            temp_model = GetDiffCountLabelsetAndDatasetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLabelDetailRequest(TeaModel):
    def __init__(
        self,
        id: int = None,
    ):
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class GetLabelDetailResponseBodyData(TeaModel):
    def __init__(
        self,
        label_info: str = None,
    ):
        self.label_info = label_info

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label_info is not None:
            result['LabelInfo'] = self.label_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LabelInfo') is not None:
            self.label_info = m.get('LabelInfo')
        return self


class GetLabelDetailResponseBody(TeaModel):
    def __init__(
        self,
        data: GetLabelDetailResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GetLabelDetailResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetLabelDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetLabelDetailResponseBody = None,
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
            temp_model = GetLabelDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLabelsetRequest(TeaModel):
    def __init__(
        self,
        id: int = None,
    ):
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class GetLabelsetResponseBodyData(TeaModel):
    def __init__(
        self,
        description: str = None,
        gmt_create: int = None,
        id: int = None,
        label_type: str = None,
        name: str = None,
        status: str = None,
        sub_task_package_size: str = None,
        tag_user_list: str = None,
        tags: str = None,
        total: int = None,
    ):
        self.description = description
        self.gmt_create = gmt_create
        self.id = id
        self.label_type = label_type
        self.name = name
        self.status = status
        self.sub_task_package_size = sub_task_package_size
        self.tag_user_list = tag_user_list
        self.tags = tags
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.id is not None:
            result['Id'] = self.id
        if self.label_type is not None:
            result['LabelType'] = self.label_type
        if self.name is not None:
            result['Name'] = self.name
        if self.status is not None:
            result['Status'] = self.status
        if self.sub_task_package_size is not None:
            result['SubTaskPackageSize'] = self.sub_task_package_size
        if self.tag_user_list is not None:
            result['TagUserList'] = self.tag_user_list
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LabelType') is not None:
            self.label_type = m.get('LabelType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubTaskPackageSize') is not None:
            self.sub_task_package_size = m.get('SubTaskPackageSize')
        if m.get('TagUserList') is not None:
            self.tag_user_list = m.get('TagUserList')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class GetLabelsetResponseBody(TeaModel):
    def __init__(
        self,
        data: GetLabelsetResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GetLabelsetResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetLabelsetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetLabelsetResponseBody = None,
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
            temp_model = GetLabelsetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetServiceRequest(TeaModel):
    def __init__(
        self,
        id: int = None,
    ):
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class GetServiceResponseBodyDataDataReflowInfo(TeaModel):
    def __init__(
        self,
        data_reflow_count: int = None,
        data_reflow_oss_path: str = None,
        data_reflow_rate: int = None,
        enable_data_reflow_flag: bool = None,
    ):
        self.data_reflow_count = data_reflow_count
        self.data_reflow_oss_path = data_reflow_oss_path
        self.data_reflow_rate = data_reflow_rate
        self.enable_data_reflow_flag = enable_data_reflow_flag

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_reflow_count is not None:
            result['DataReflowCount'] = self.data_reflow_count
        if self.data_reflow_oss_path is not None:
            result['DataReflowOssPath'] = self.data_reflow_oss_path
        if self.data_reflow_rate is not None:
            result['DataReflowRate'] = self.data_reflow_rate
        if self.enable_data_reflow_flag is not None:
            result['EnableDataReflowFlag'] = self.enable_data_reflow_flag
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataReflowCount') is not None:
            self.data_reflow_count = m.get('DataReflowCount')
        if m.get('DataReflowOssPath') is not None:
            self.data_reflow_oss_path = m.get('DataReflowOssPath')
        if m.get('DataReflowRate') is not None:
            self.data_reflow_rate = m.get('DataReflowRate')
        if m.get('EnableDataReflowFlag') is not None:
            self.enable_data_reflow_flag = m.get('EnableDataReflowFlag')
        return self


class GetServiceResponseBodyData(TeaModel):
    def __init__(
        self,
        data_reflow_info: GetServiceResponseBodyDataDataReflowInfo = None,
        errorcodes: str = None,
        gmt_create: int = None,
        id: int = None,
        input_example: str = None,
        input_params: str = None,
        output_example: str = None,
        output_params: str = None,
        service_description: str = None,
        service_id: str = None,
        service_name: str = None,
        status: str = None,
    ):
        self.data_reflow_info = data_reflow_info
        self.errorcodes = errorcodes
        self.gmt_create = gmt_create
        self.id = id
        self.input_example = input_example
        self.input_params = input_params
        self.output_example = output_example
        self.output_params = output_params
        self.service_description = service_description
        self.service_id = service_id
        self.service_name = service_name
        self.status = status

    def validate(self):
        if self.data_reflow_info:
            self.data_reflow_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_reflow_info is not None:
            result['DataReflowInfo'] = self.data_reflow_info.to_map()
        if self.errorcodes is not None:
            result['Errorcodes'] = self.errorcodes
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.id is not None:
            result['Id'] = self.id
        if self.input_example is not None:
            result['InputExample'] = self.input_example
        if self.input_params is not None:
            result['InputParams'] = self.input_params
        if self.output_example is not None:
            result['OutputExample'] = self.output_example
        if self.output_params is not None:
            result['OutputParams'] = self.output_params
        if self.service_description is not None:
            result['ServiceDescription'] = self.service_description
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataReflowInfo') is not None:
            temp_model = GetServiceResponseBodyDataDataReflowInfo()
            self.data_reflow_info = temp_model.from_map(m['DataReflowInfo'])
        if m.get('Errorcodes') is not None:
            self.errorcodes = m.get('Errorcodes')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InputExample') is not None:
            self.input_example = m.get('InputExample')
        if m.get('InputParams') is not None:
            self.input_params = m.get('InputParams')
        if m.get('OutputExample') is not None:
            self.output_example = m.get('OutputExample')
        if m.get('OutputParams') is not None:
            self.output_params = m.get('OutputParams')
        if m.get('ServiceDescription') is not None:
            self.service_description = m.get('ServiceDescription')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetServiceResponseBody(TeaModel):
    def __init__(
        self,
        data: GetServiceResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GetServiceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetServiceResponseBody = None,
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
            temp_model = GetServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTrainModelRequest(TeaModel):
    def __init__(
        self,
        id: int = None,
    ):
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class GetTrainModelResponseBodyData(TeaModel):
    def __init__(
        self,
        simple_evaluate: int = None,
    ):
        self.simple_evaluate = simple_evaluate

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.simple_evaluate is not None:
            result['SimpleEvaluate'] = self.simple_evaluate
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SimpleEvaluate') is not None:
            self.simple_evaluate = m.get('SimpleEvaluate')
        return self


class GetTrainModelResponseBody(TeaModel):
    def __init__(
        self,
        data: GetTrainModelResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GetTrainModelResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetTrainModelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetTrainModelResponseBody = None,
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
            temp_model = GetTrainModelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTrainTaskRequest(TeaModel):
    def __init__(
        self,
        id: int = None,
    ):
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class GetTrainTaskResponseBodyData(TeaModel):
    def __init__(
        self,
        dataset_id: int = None,
        dataset_name: str = None,
        description: str = None,
        failure_reason: str = None,
        gmt_create: int = None,
        id: int = None,
        label_id: int = None,
        label_name: str = None,
        model_effect: str = None,
        model_id: int = None,
        task_name: str = None,
        train_mode: str = None,
        train_status: str = None,
        train_use_time: int = None,
    ):
        self.dataset_id = dataset_id
        self.dataset_name = dataset_name
        self.description = description
        self.failure_reason = failure_reason
        self.gmt_create = gmt_create
        self.id = id
        self.label_id = label_id
        self.label_name = label_name
        self.model_effect = model_effect
        self.model_id = model_id
        self.task_name = task_name
        self.train_mode = train_mode
        self.train_status = train_status
        self.train_use_time = train_use_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_id is not None:
            result['DatasetId'] = self.dataset_id
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.description is not None:
            result['Description'] = self.description
        if self.failure_reason is not None:
            result['FailureReason'] = self.failure_reason
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.id is not None:
            result['Id'] = self.id
        if self.label_id is not None:
            result['LabelId'] = self.label_id
        if self.label_name is not None:
            result['LabelName'] = self.label_name
        if self.model_effect is not None:
            result['ModelEffect'] = self.model_effect
        if self.model_id is not None:
            result['ModelId'] = self.model_id
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.train_mode is not None:
            result['TrainMode'] = self.train_mode
        if self.train_status is not None:
            result['TrainStatus'] = self.train_status
        if self.train_use_time is not None:
            result['TrainUseTime'] = self.train_use_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetId') is not None:
            self.dataset_id = m.get('DatasetId')
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('FailureReason') is not None:
            self.failure_reason = m.get('FailureReason')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LabelId') is not None:
            self.label_id = m.get('LabelId')
        if m.get('LabelName') is not None:
            self.label_name = m.get('LabelName')
        if m.get('ModelEffect') is not None:
            self.model_effect = m.get('ModelEffect')
        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('TrainMode') is not None:
            self.train_mode = m.get('TrainMode')
        if m.get('TrainStatus') is not None:
            self.train_status = m.get('TrainStatus')
        if m.get('TrainUseTime') is not None:
            self.train_use_time = m.get('TrainUseTime')
        return self


class GetTrainTaskResponseBody(TeaModel):
    def __init__(
        self,
        data: GetTrainTaskResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GetTrainTaskResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetTrainTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetTrainTaskResponseBody = None,
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
            temp_model = GetTrainTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTrainTaskEstimatedTimeRequest(TeaModel):
    def __init__(
        self,
        id: int = None,
    ):
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class GetTrainTaskEstimatedTimeResponseBodyData(TeaModel):
    def __init__(
        self,
        estimated_time: str = None,
    ):
        self.estimated_time = estimated_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.estimated_time is not None:
            result['EstimatedTime'] = self.estimated_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EstimatedTime') is not None:
            self.estimated_time = m.get('EstimatedTime')
        return self


class GetTrainTaskEstimatedTimeResponseBody(TeaModel):
    def __init__(
        self,
        data: GetTrainTaskEstimatedTimeResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GetTrainTaskEstimatedTimeResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetTrainTaskEstimatedTimeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetTrainTaskEstimatedTimeResponseBody = None,
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
            temp_model = GetTrainTaskEstimatedTimeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUploadPolicyRequest(TeaModel):
    def __init__(
        self,
        file_name: str = None,
        id: int = None,
        type: str = None,
    ):
        self.file_name = file_name
        self.id = id
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.id is not None:
            result['Id'] = self.id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetUploadPolicyResponseBodyData(TeaModel):
    def __init__(
        self,
        access_id: str = None,
        bucket_name: str = None,
        endpoint: str = None,
        file_name: str = None,
        object_key: str = None,
        original_filename: str = None,
        policy: str = None,
        signature: str = None,
        signed_http_url: str = None,
    ):
        self.access_id = access_id
        self.bucket_name = bucket_name
        self.endpoint = endpoint
        self.file_name = file_name
        self.object_key = object_key
        self.original_filename = original_filename
        self.policy = policy
        self.signature = signature
        self.signed_http_url = signed_http_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_id is not None:
            result['AccessId'] = self.access_id
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.object_key is not None:
            result['ObjectKey'] = self.object_key
        if self.original_filename is not None:
            result['OriginalFilename'] = self.original_filename
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.signature is not None:
            result['Signature'] = self.signature
        if self.signed_http_url is not None:
            result['SignedHttpUrl'] = self.signed_http_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessId') is not None:
            self.access_id = m.get('AccessId')
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('ObjectKey') is not None:
            self.object_key = m.get('ObjectKey')
        if m.get('OriginalFilename') is not None:
            self.original_filename = m.get('OriginalFilename')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('Signature') is not None:
            self.signature = m.get('Signature')
        if m.get('SignedHttpUrl') is not None:
            self.signed_http_url = m.get('SignedHttpUrl')
        return self


class GetUploadPolicyResponseBody(TeaModel):
    def __init__(
        self,
        data: GetUploadPolicyResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GetUploadPolicyResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetUploadPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetUploadPolicyResponseBody = None,
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
            temp_model = GetUploadPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetWorkspaceRequest(TeaModel):
    def __init__(
        self,
        id: int = None,
    ):
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class GetWorkspaceResponseBodyData(TeaModel):
    def __init__(
        self,
        description: str = None,
        gmt_create: int = None,
        id: int = None,
        name: str = None,
        type: str = None,
    ):
        self.description = description
        self.gmt_create = gmt_create
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
        if self.description is not None:
            result['Description'] = self.description
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetWorkspaceResponseBody(TeaModel):
    def __init__(
        self,
        data: GetWorkspaceResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GetWorkspaceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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
            temp_model = GetWorkspaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDataReflowDatasRequest(TeaModel):
    def __init__(
        self,
        category: str = None,
        current_page: int = None,
        end_time: int = None,
        image_name: str = None,
        page_size: int = None,
        service_id: int = None,
        start_time: int = None,
    ):
        self.category = category
        self.current_page = current_page
        self.end_time = end_time
        self.image_name = image_name
        self.page_size = page_size
        self.service_id = service_id
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.image_name is not None:
            result['ImageName'] = self.image_name
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class ListDataReflowDatasResponseBodyData(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        elements: List[Dict[str, Any]] = None,
        page_size: int = None,
        total_count: int = None,
        total_page: int = None,
    ):
        self.current_page = current_page
        self.elements = elements
        self.page_size = page_size
        self.total_count = total_count
        self.total_page = total_page

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.elements is not None:
            result['Elements'] = self.elements
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.total_page is not None:
            result['TotalPage'] = self.total_page
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('Elements') is not None:
            self.elements = m.get('Elements')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')
        return self


class ListDataReflowDatasResponseBody(TeaModel):
    def __init__(
        self,
        data: ListDataReflowDatasResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = ListDataReflowDatasResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListDataReflowDatasResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDataReflowDatasResponseBody = None,
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
            temp_model = ListDataReflowDatasResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDatasetDatasRequest(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        dataset_id: int = None,
        identity: str = None,
        page_size: int = None,
    ):
        self.current_page = current_page
        self.dataset_id = dataset_id
        self.identity = identity
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.dataset_id is not None:
            result['DatasetId'] = self.dataset_id
        if self.identity is not None:
            result['Identity'] = self.identity
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('DatasetId') is not None:
            self.dataset_id = m.get('DatasetId')
        if m.get('Identity') is not None:
            self.identity = m.get('Identity')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListDatasetDatasResponseBodyData(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        elements: List[Dict[str, Any]] = None,
        page_size: int = None,
        total_count: int = None,
        total_page: int = None,
    ):
        self.current_page = current_page
        self.elements = elements
        self.page_size = page_size
        self.total_count = total_count
        self.total_page = total_page

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.elements is not None:
            result['Elements'] = self.elements
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.total_page is not None:
            result['TotalPage'] = self.total_page
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('Elements') is not None:
            self.elements = m.get('Elements')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')
        return self


class ListDatasetDatasResponseBody(TeaModel):
    def __init__(
        self,
        data: ListDatasetDatasResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = ListDatasetDatasResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListDatasetDatasResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDatasetDatasResponseBody = None,
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
            temp_model = ListDatasetDatasResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDatasetsRequest(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        workspace_id: int = None,
    ):
        self.current_page = current_page
        self.page_size = page_size
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class ListDatasetsResponseBodyData(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        elements: List[Dict[str, Any]] = None,
        page_size: int = None,
        total_count: int = None,
        total_page: int = None,
    ):
        self.current_page = current_page
        self.elements = elements
        self.page_size = page_size
        self.total_count = total_count
        self.total_page = total_page

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.elements is not None:
            result['Elements'] = self.elements
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.total_page is not None:
            result['TotalPage'] = self.total_page
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('Elements') is not None:
            self.elements = m.get('Elements')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')
        return self


class ListDatasetsResponseBody(TeaModel):
    def __init__(
        self,
        data: ListDatasetsResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = ListDatasetsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListDatasetsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDatasetsResponseBody = None,
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
            temp_model = ListDatasetsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListLabelsetDatasRequest(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        is_abandon: bool = None,
        label_id: int = None,
        name: str = None,
        operation: str = None,
        page_size: int = None,
        value: str = None,
    ):
        self.current_page = current_page
        self.is_abandon = is_abandon
        self.label_id = label_id
        self.name = name
        self.operation = operation
        self.page_size = page_size
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.is_abandon is not None:
            result['IsAbandon'] = self.is_abandon
        if self.label_id is not None:
            result['LabelId'] = self.label_id
        if self.name is not None:
            result['Name'] = self.name
        if self.operation is not None:
            result['Operation'] = self.operation
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('IsAbandon') is not None:
            self.is_abandon = m.get('IsAbandon')
        if m.get('LabelId') is not None:
            self.label_id = m.get('LabelId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Operation') is not None:
            self.operation = m.get('Operation')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListLabelsetDatasResponseBodyData(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        elements: List[Dict[str, Any]] = None,
        page_size: int = None,
        total_count: int = None,
        total_page: int = None,
    ):
        self.current_page = current_page
        self.elements = elements
        self.page_size = page_size
        self.total_count = total_count
        self.total_page = total_page

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.elements is not None:
            result['Elements'] = self.elements
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.total_page is not None:
            result['TotalPage'] = self.total_page
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('Elements') is not None:
            self.elements = m.get('Elements')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')
        return self


class ListLabelsetDatasResponseBody(TeaModel):
    def __init__(
        self,
        data: ListLabelsetDatasResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = ListLabelsetDatasResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListLabelsetDatasResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListLabelsetDatasResponseBody = None,
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
            temp_model = ListLabelsetDatasResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListLabelsetsRequest(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        dataset_id: int = None,
        page_size: int = None,
        status: str = None,
    ):
        self.current_page = current_page
        self.dataset_id = dataset_id
        self.page_size = page_size
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.dataset_id is not None:
            result['DatasetId'] = self.dataset_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('DatasetId') is not None:
            self.dataset_id = m.get('DatasetId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListLabelsetsResponseBodyData(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        elements: List[Dict[str, Any]] = None,
        page_size: int = None,
        total_count: int = None,
        total_page: int = None,
    ):
        self.current_page = current_page
        self.elements = elements
        self.page_size = page_size
        self.total_count = total_count
        self.total_page = total_page

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.elements is not None:
            result['Elements'] = self.elements
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.total_page is not None:
            result['TotalPage'] = self.total_page
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('Elements') is not None:
            self.elements = m.get('Elements')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')
        return self


class ListLabelsetsResponseBody(TeaModel):
    def __init__(
        self,
        data: ListLabelsetsResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = ListLabelsetsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListLabelsetsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListLabelsetsResponseBody = None,
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
            temp_model = ListLabelsetsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListServicesRequest(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        id: int = None,
        name: int = None,
        page_size: int = None,
        workspace_id: int = None,
    ):
        self.current_page = current_page
        self.id = id
        self.name = name
        self.page_size = page_size
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class ListServicesResponseBodyData(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        elements: List[Dict[str, Any]] = None,
        page_size: int = None,
        total_count: int = None,
        total_page: int = None,
    ):
        self.current_page = current_page
        self.elements = elements
        self.page_size = page_size
        self.total_count = total_count
        self.total_page = total_page

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.elements is not None:
            result['Elements'] = self.elements
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.total_page is not None:
            result['TotalPage'] = self.total_page
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('Elements') is not None:
            self.elements = m.get('Elements')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')
        return self


class ListServicesResponseBody(TeaModel):
    def __init__(
        self,
        data: ListServicesResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = ListServicesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListServicesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListServicesResponseBody = None,
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
            temp_model = ListServicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTrainTasksRequest(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        status: str = None,
        workspace_id: int = None,
    ):
        self.current_page = current_page
        self.page_size = page_size
        self.status = status
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.status is not None:
            result['Status'] = self.status
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class ListTrainTasksResponseBodyData(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        elements: List[Dict[str, Any]] = None,
        page_size: int = None,
        total_count: int = None,
        total_page: int = None,
    ):
        self.current_page = current_page
        self.elements = elements
        self.page_size = page_size
        self.total_count = total_count
        self.total_page = total_page

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.elements is not None:
            result['Elements'] = self.elements
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.total_page is not None:
            result['TotalPage'] = self.total_page
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('Elements') is not None:
            self.elements = m.get('Elements')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')
        return self


class ListTrainTasksResponseBody(TeaModel):
    def __init__(
        self,
        data: ListTrainTasksResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = ListTrainTasksResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListTrainTasksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTrainTasksResponseBody = None,
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
            temp_model = ListTrainTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListWorkspacesRequest(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        name: str = None,
        page_size: int = None,
    ):
        self.current_page = current_page
        self.name = name
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.name is not None:
            result['Name'] = self.name
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListWorkspacesResponseBodyDataElements(TeaModel):
    def __init__(
        self,
        description: str = None,
        gmt_create: int = None,
        id: int = None,
        name: str = None,
        type: str = None,
    ):
        self.description = description
        self.gmt_create = gmt_create
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
        if self.description is not None:
            result['Description'] = self.description
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListWorkspacesResponseBodyData(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        elements: List[ListWorkspacesResponseBodyDataElements] = None,
        page_size: int = None,
        total_count: int = None,
        total_page: int = None,
    ):
        self.current_page = current_page
        self.elements = elements
        self.page_size = page_size
        self.total_count = total_count
        self.total_page = total_page

    def validate(self):
        if self.elements:
            for k in self.elements:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['Elements'] = []
        if self.elements is not None:
            for k in self.elements:
                result['Elements'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.total_page is not None:
            result['TotalPage'] = self.total_page
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.elements = []
        if m.get('Elements') is not None:
            for k in m.get('Elements'):
                temp_model = ListWorkspacesResponseBodyDataElements()
                self.elements.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')
        return self


class ListWorkspacesResponseBody(TeaModel):
    def __init__(
        self,
        data: ListWorkspacesResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = ListWorkspacesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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
            temp_model = ListWorkspacesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetDatasetUserOssPathRequest(TeaModel):
    def __init__(
        self,
        dataset_id: int = None,
        user_oss_url: str = None,
    ):
        self.dataset_id = dataset_id
        self.user_oss_url = user_oss_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_id is not None:
            result['DatasetId'] = self.dataset_id
        if self.user_oss_url is not None:
            result['UserOssUrl'] = self.user_oss_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetId') is not None:
            self.dataset_id = m.get('DatasetId')
        if m.get('UserOssUrl') is not None:
            self.user_oss_url = m.get('UserOssUrl')
        return self


class SetDatasetUserOssPathResponseBodyData(TeaModel):
    def __init__(
        self,
        id: int = None,
        oss_url: str = None,
    ):
        self.id = id
        self.oss_url = oss_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.oss_url is not None:
            result['OssUrl'] = self.oss_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OssUrl') is not None:
            self.oss_url = m.get('OssUrl')
        return self


class SetDatasetUserOssPathResponseBody(TeaModel):
    def __init__(
        self,
        data: SetDatasetUserOssPathResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = SetDatasetUserOssPathResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SetDatasetUserOssPathResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SetDatasetUserOssPathResponseBody = None,
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
            temp_model = SetDatasetUserOssPathResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartServiceRequest(TeaModel):
    def __init__(
        self,
        id: int = None,
    ):
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class StartServiceResponseBodyData(TeaModel):
    def __init__(
        self,
        gmt_create: int = None,
        id: int = None,
        service_description: str = None,
        service_name: str = None,
        status: str = None,
    ):
        self.gmt_create = gmt_create
        self.id = id
        self.service_description = service_description
        self.service_name = service_name
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.id is not None:
            result['Id'] = self.id
        if self.service_description is not None:
            result['ServiceDescription'] = self.service_description
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ServiceDescription') is not None:
            self.service_description = m.get('ServiceDescription')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class StartServiceResponseBody(TeaModel):
    def __init__(
        self,
        data: StartServiceResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = StartServiceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StartServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StartServiceResponseBody = None,
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
            temp_model = StartServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartTrainTaskRequest(TeaModel):
    def __init__(
        self,
        force_start_flag: bool = None,
        id: int = None,
        rely_on_task_id: int = None,
    ):
        self.force_start_flag = force_start_flag
        self.id = id
        self.rely_on_task_id = rely_on_task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.force_start_flag is not None:
            result['ForceStartFlag'] = self.force_start_flag
        if self.id is not None:
            result['Id'] = self.id
        if self.rely_on_task_id is not None:
            result['RelyOnTaskId'] = self.rely_on_task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ForceStartFlag') is not None:
            self.force_start_flag = m.get('ForceStartFlag')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RelyOnTaskId') is not None:
            self.rely_on_task_id = m.get('RelyOnTaskId')
        return self


class StartTrainTaskResponseBodyData(TeaModel):
    def __init__(
        self,
        check_result: Dict[str, Any] = None,
        dataset_id: int = None,
        dataset_name: str = None,
        description: str = None,
        gmt_create: int = None,
        id: int = None,
        label_id: int = None,
        label_name: str = None,
        model_effect: str = None,
        model_id: int = None,
        task_name: str = None,
        train_mode: str = None,
        train_status: str = None,
    ):
        self.check_result = check_result
        self.dataset_id = dataset_id
        self.dataset_name = dataset_name
        self.description = description
        self.gmt_create = gmt_create
        self.id = id
        self.label_id = label_id
        self.label_name = label_name
        self.model_effect = model_effect
        self.model_id = model_id
        self.task_name = task_name
        self.train_mode = train_mode
        self.train_status = train_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_result is not None:
            result['CheckResult'] = self.check_result
        if self.dataset_id is not None:
            result['DatasetId'] = self.dataset_id
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.description is not None:
            result['Description'] = self.description
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.id is not None:
            result['Id'] = self.id
        if self.label_id is not None:
            result['LabelId'] = self.label_id
        if self.label_name is not None:
            result['LabelName'] = self.label_name
        if self.model_effect is not None:
            result['ModelEffect'] = self.model_effect
        if self.model_id is not None:
            result['ModelId'] = self.model_id
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.train_mode is not None:
            result['TrainMode'] = self.train_mode
        if self.train_status is not None:
            result['TrainStatus'] = self.train_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckResult') is not None:
            self.check_result = m.get('CheckResult')
        if m.get('DatasetId') is not None:
            self.dataset_id = m.get('DatasetId')
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LabelId') is not None:
            self.label_id = m.get('LabelId')
        if m.get('LabelName') is not None:
            self.label_name = m.get('LabelName')
        if m.get('ModelEffect') is not None:
            self.model_effect = m.get('ModelEffect')
        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('TrainMode') is not None:
            self.train_mode = m.get('TrainMode')
        if m.get('TrainStatus') is not None:
            self.train_status = m.get('TrainStatus')
        return self


class StartTrainTaskResponseBody(TeaModel):
    def __init__(
        self,
        data: StartTrainTaskResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = StartTrainTaskResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StartTrainTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StartTrainTaskResponseBody = None,
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
            temp_model = StartTrainTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopServiceRequest(TeaModel):
    def __init__(
        self,
        id: int = None,
    ):
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class StopServiceResponseBodyData(TeaModel):
    def __init__(
        self,
        gmt_create: int = None,
        id: int = None,
        service_description: str = None,
        service_name: str = None,
        status: str = None,
    ):
        self.gmt_create = gmt_create
        self.id = id
        self.service_description = service_description
        self.service_name = service_name
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.id is not None:
            result['Id'] = self.id
        if self.service_description is not None:
            result['ServiceDescription'] = self.service_description
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ServiceDescription') is not None:
            self.service_description = m.get('ServiceDescription')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class StopServiceResponseBody(TeaModel):
    def __init__(
        self,
        data: StopServiceResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = StopServiceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StopServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StopServiceResponseBody = None,
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
            temp_model = StopServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopTrainTaskRequest(TeaModel):
    def __init__(
        self,
        id: int = None,
    ):
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class StopTrainTaskResponseBodyData(TeaModel):
    def __init__(
        self,
        dataset_id: int = None,
        dataset_name: str = None,
        description: str = None,
        gmt_create: int = None,
        id: int = None,
        label_id: int = None,
        label_name: str = None,
        model_effect: str = None,
        model_id: int = None,
        task_name: str = None,
        train_mode: str = None,
        train_status: str = None,
    ):
        self.dataset_id = dataset_id
        self.dataset_name = dataset_name
        self.description = description
        self.gmt_create = gmt_create
        self.id = id
        self.label_id = label_id
        self.label_name = label_name
        self.model_effect = model_effect
        self.model_id = model_id
        self.task_name = task_name
        self.train_mode = train_mode
        self.train_status = train_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_id is not None:
            result['DatasetId'] = self.dataset_id
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.description is not None:
            result['Description'] = self.description
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.id is not None:
            result['Id'] = self.id
        if self.label_id is not None:
            result['LabelId'] = self.label_id
        if self.label_name is not None:
            result['LabelName'] = self.label_name
        if self.model_effect is not None:
            result['ModelEffect'] = self.model_effect
        if self.model_id is not None:
            result['ModelId'] = self.model_id
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.train_mode is not None:
            result['TrainMode'] = self.train_mode
        if self.train_status is not None:
            result['TrainStatus'] = self.train_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetId') is not None:
            self.dataset_id = m.get('DatasetId')
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LabelId') is not None:
            self.label_id = m.get('LabelId')
        if m.get('LabelName') is not None:
            self.label_name = m.get('LabelName')
        if m.get('ModelEffect') is not None:
            self.model_effect = m.get('ModelEffect')
        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('TrainMode') is not None:
            self.train_mode = m.get('TrainMode')
        if m.get('TrainStatus') is not None:
            self.train_status = m.get('TrainStatus')
        return self


class StopTrainTaskResponseBody(TeaModel):
    def __init__(
        self,
        data: StopTrainTaskResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = StopTrainTaskResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StopTrainTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StopTrainTaskResponseBody = None,
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
            temp_model = StopTrainTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDatasetRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        id: int = None,
        name: str = None,
    ):
        self.description = description
        self.id = id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class UpdateDatasetResponseBodyData(TeaModel):
    def __init__(
        self,
        description: str = None,
        gmt_create: int = None,
        id: int = None,
        name: str = None,
    ):
        self.description = description
        self.gmt_create = gmt_create
        self.id = id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class UpdateDatasetResponseBody(TeaModel):
    def __init__(
        self,
        data: UpdateDatasetResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = UpdateDatasetResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateDatasetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateDatasetResponseBody = None,
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
            temp_model = UpdateDatasetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateLabelsetRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        id: int = None,
        name: str = None,
        object_key: str = None,
        tag_user_list: str = None,
        user_oss_url: str = None,
    ):
        self.description = description
        self.id = id
        self.name = name
        self.object_key = object_key
        self.tag_user_list = tag_user_list
        self.user_oss_url = user_oss_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.object_key is not None:
            result['ObjectKey'] = self.object_key
        if self.tag_user_list is not None:
            result['TagUserList'] = self.tag_user_list
        if self.user_oss_url is not None:
            result['UserOssUrl'] = self.user_oss_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ObjectKey') is not None:
            self.object_key = m.get('ObjectKey')
        if m.get('TagUserList') is not None:
            self.tag_user_list = m.get('TagUserList')
        if m.get('UserOssUrl') is not None:
            self.user_oss_url = m.get('UserOssUrl')
        return self


class UpdateLabelsetResponseBodyData(TeaModel):
    def __init__(
        self,
        description: int = None,
        gmt_create: int = None,
        id: int = None,
        name: int = None,
    ):
        self.description = description
        self.gmt_create = gmt_create
        self.id = id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class UpdateLabelsetResponseBody(TeaModel):
    def __init__(
        self,
        data: UpdateLabelsetResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = UpdateLabelsetResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateLabelsetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateLabelsetResponseBody = None,
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
            temp_model = UpdateLabelsetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateServiceRequest(TeaModel):
    def __init__(
        self,
        authorization_type: str = None,
        authorized_account: str = None,
        description: str = None,
        id: int = None,
        name: str = None,
    ):
        self.authorization_type = authorization_type
        self.authorized_account = authorized_account
        self.description = description
        self.id = id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authorization_type is not None:
            result['AuthorizationType'] = self.authorization_type
        if self.authorized_account is not None:
            result['AuthorizedAccount'] = self.authorized_account
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthorizationType') is not None:
            self.authorization_type = m.get('AuthorizationType')
        if m.get('AuthorizedAccount') is not None:
            self.authorized_account = m.get('AuthorizedAccount')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class UpdateServiceResponseBodyData(TeaModel):
    def __init__(
        self,
        authorization_type: str = None,
        authorized_account: str = None,
        gmt_create: int = None,
        id: int = None,
        service_description: str = None,
        service_name: str = None,
    ):
        self.authorization_type = authorization_type
        self.authorized_account = authorized_account
        self.gmt_create = gmt_create
        self.id = id
        self.service_description = service_description
        self.service_name = service_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authorization_type is not None:
            result['AuthorizationType'] = self.authorization_type
        if self.authorized_account is not None:
            result['AuthorizedAccount'] = self.authorized_account
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.id is not None:
            result['Id'] = self.id
        if self.service_description is not None:
            result['ServiceDescription'] = self.service_description
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthorizationType') is not None:
            self.authorization_type = m.get('AuthorizationType')
        if m.get('AuthorizedAccount') is not None:
            self.authorized_account = m.get('AuthorizedAccount')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ServiceDescription') is not None:
            self.service_description = m.get('ServiceDescription')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        return self


class UpdateServiceResponseBody(TeaModel):
    def __init__(
        self,
        data: UpdateServiceResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = UpdateServiceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateServiceResponseBody = None,
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
            temp_model = UpdateServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateTrainTaskRequest(TeaModel):
    def __init__(
        self,
        advanced_parameters: str = None,
        dataset_ids: str = None,
        description: str = None,
        id: int = None,
        label_ids: str = None,
        name: str = None,
        pre_train_task_flag: bool = None,
        pre_train_task_id: int = None,
        train_mode: str = None,
    ):
        self.advanced_parameters = advanced_parameters
        self.dataset_ids = dataset_ids
        self.description = description
        self.id = id
        self.label_ids = label_ids
        self.name = name
        self.pre_train_task_flag = pre_train_task_flag
        self.pre_train_task_id = pre_train_task_id
        self.train_mode = train_mode

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.advanced_parameters is not None:
            result['AdvancedParameters'] = self.advanced_parameters
        if self.dataset_ids is not None:
            result['DatasetIds'] = self.dataset_ids
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.label_ids is not None:
            result['LabelIds'] = self.label_ids
        if self.name is not None:
            result['Name'] = self.name
        if self.pre_train_task_flag is not None:
            result['PreTrainTaskFlag'] = self.pre_train_task_flag
        if self.pre_train_task_id is not None:
            result['PreTrainTaskId'] = self.pre_train_task_id
        if self.train_mode is not None:
            result['TrainMode'] = self.train_mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdvancedParameters') is not None:
            self.advanced_parameters = m.get('AdvancedParameters')
        if m.get('DatasetIds') is not None:
            self.dataset_ids = m.get('DatasetIds')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LabelIds') is not None:
            self.label_ids = m.get('LabelIds')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PreTrainTaskFlag') is not None:
            self.pre_train_task_flag = m.get('PreTrainTaskFlag')
        if m.get('PreTrainTaskId') is not None:
            self.pre_train_task_id = m.get('PreTrainTaskId')
        if m.get('TrainMode') is not None:
            self.train_mode = m.get('TrainMode')
        return self


class UpdateTrainTaskResponseBodyData(TeaModel):
    def __init__(
        self,
        advanced_parameters: str = None,
        dataset_id: int = None,
        dataset_name: str = None,
        description: str = None,
        gmt_create: int = None,
        id: int = None,
        label_id: int = None,
        label_name: str = None,
        model_effect: str = None,
        model_id: int = None,
        task_name: str = None,
        train_mode: str = None,
        train_status: str = None,
    ):
        self.advanced_parameters = advanced_parameters
        self.dataset_id = dataset_id
        self.dataset_name = dataset_name
        self.description = description
        self.gmt_create = gmt_create
        self.id = id
        self.label_id = label_id
        self.label_name = label_name
        self.model_effect = model_effect
        self.model_id = model_id
        self.task_name = task_name
        self.train_mode = train_mode
        self.train_status = train_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.advanced_parameters is not None:
            result['AdvancedParameters'] = self.advanced_parameters
        if self.dataset_id is not None:
            result['DatasetId'] = self.dataset_id
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.description is not None:
            result['Description'] = self.description
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.id is not None:
            result['Id'] = self.id
        if self.label_id is not None:
            result['LabelId'] = self.label_id
        if self.label_name is not None:
            result['LabelName'] = self.label_name
        if self.model_effect is not None:
            result['ModelEffect'] = self.model_effect
        if self.model_id is not None:
            result['ModelId'] = self.model_id
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.train_mode is not None:
            result['TrainMode'] = self.train_mode
        if self.train_status is not None:
            result['TrainStatus'] = self.train_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdvancedParameters') is not None:
            self.advanced_parameters = m.get('AdvancedParameters')
        if m.get('DatasetId') is not None:
            self.dataset_id = m.get('DatasetId')
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LabelId') is not None:
            self.label_id = m.get('LabelId')
        if m.get('LabelName') is not None:
            self.label_name = m.get('LabelName')
        if m.get('ModelEffect') is not None:
            self.model_effect = m.get('ModelEffect')
        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('TrainMode') is not None:
            self.train_mode = m.get('TrainMode')
        if m.get('TrainStatus') is not None:
            self.train_status = m.get('TrainStatus')
        return self


class UpdateTrainTaskResponseBody(TeaModel):
    def __init__(
        self,
        data: UpdateTrainTaskResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = UpdateTrainTaskResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateTrainTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateTrainTaskResponseBody = None,
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
            temp_model = UpdateTrainTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateWorkspaceRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        id: int = None,
        name: str = None,
    ):
        self.description = description
        self.id = id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class UpdateWorkspaceResponseBodyData(TeaModel):
    def __init__(
        self,
        description: str = None,
        gmt_create: int = None,
        id: int = None,
        name: str = None,
        type: str = None,
    ):
        self.description = description
        self.gmt_create = gmt_create
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
        if self.description is not None:
            result['Description'] = self.description
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class UpdateWorkspaceResponseBody(TeaModel):
    def __init__(
        self,
        data: UpdateWorkspaceResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = UpdateWorkspaceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
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
            temp_model = UpdateWorkspaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


