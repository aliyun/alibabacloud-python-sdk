# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, Any, List


class AddStreamGroupHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        trans_to_alink: str = None,
    ):
        self.common_headers = common_headers
        self.trans_to_alink = trans_to_alink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.trans_to_alink is not None:
            result['TransToAlink'] = self.trans_to_alink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('TransToAlink') is not None:
            self.trans_to_alink = m.get('TransToAlink')
        return self


class AddStreamGroupRequest(TeaModel):
    def __init__(
        self,
        algo_type_enum: str = None,
        alink_job_user: str = None,
        stream_id: int = None,
        stream_task_id: int = None,
        task_id: str = None,
        user_number: str = None,
    ):
        self.algo_type_enum = algo_type_enum
        self.alink_job_user = alink_job_user
        self.stream_id = stream_id
        self.stream_task_id = stream_task_id
        self.task_id = task_id
        self.user_number = user_number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algo_type_enum is not None:
            result['AlgoTypeEnum'] = self.algo_type_enum
        if self.alink_job_user is not None:
            result['AlinkJobUser'] = self.alink_job_user
        if self.stream_id is not None:
            result['StreamId'] = self.stream_id
        if self.stream_task_id is not None:
            result['StreamTaskId'] = self.stream_task_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.user_number is not None:
            result['UserNumber'] = self.user_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlgoTypeEnum') is not None:
            self.algo_type_enum = m.get('AlgoTypeEnum')
        if m.get('AlinkJobUser') is not None:
            self.alink_job_user = m.get('AlinkJobUser')
        if m.get('StreamId') is not None:
            self.stream_id = m.get('StreamId')
        if m.get('StreamTaskId') is not None:
            self.stream_task_id = m.get('StreamTaskId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('UserNumber') is not None:
            self.user_number = m.get('UserNumber')
        return self


class AddStreamGroupResponseBody(TeaModel):
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


class AddStreamGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddStreamGroupResponseBody = None,
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
            temp_model = AddStreamGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExportExperimentRequest(TeaModel):
    def __init__(
        self,
        experiment_id: int = None,
    ):
        self.experiment_id = experiment_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.experiment_id is not None:
            result['ExperimentId'] = self.experiment_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExperimentId') is not None:
            self.experiment_id = m.get('ExperimentId')
        return self


class ExportExperimentResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        # 实验内容
        self.data = data
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
        if self.data is not None:
            result['Data'] = self.data
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
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ExportExperimentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ExportExperimentResponseBody = None,
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
            temp_model = ExportExperimentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExportExperimentTreeRequest(TeaModel):
    def __init__(
        self,
        project_id: int = None,
    ):
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class ExportExperimentTreeResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: Dict[str, Any] = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        # 实验树
        self.data = data
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
        if self.data is not None:
            result['Data'] = self.data
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
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ExportExperimentTreeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ExportExperimentTreeResponseBody = None,
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
            temp_model = ExportExperimentTreeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExportExperimentTreeByProjectOwnerRequest(TeaModel):
    def __init__(
        self,
        project_id: int = None,
        tree_owner_id: str = None,
    ):
        self.project_id = project_id
        self.tree_owner_id = tree_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.tree_owner_id is not None:
            result['TreeOwnerId'] = self.tree_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('TreeOwnerId') is not None:
            self.tree_owner_id = m.get('TreeOwnerId')
        return self


class ExportExperimentTreeByProjectOwnerResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: Dict[str, Any] = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        # 实验树
        self.data = data
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
        if self.data is not None:
            result['Data'] = self.data
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
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ExportExperimentTreeByProjectOwnerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ExportExperimentTreeByProjectOwnerResponseBody = None,
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
            temp_model = ExportExperimentTreeByProjectOwnerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAlinkAlgoInfoRequest(TeaModel):
    def __init__(
        self,
        algo_name: str = None,
        user_number: str = None,
    ):
        self.algo_name = algo_name
        self.user_number = user_number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algo_name is not None:
            result['AlgoName'] = self.algo_name
        if self.user_number is not None:
            result['UserNumber'] = self.user_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlgoName') is not None:
            self.algo_name = m.get('AlgoName')
        if m.get('UserNumber') is not None:
            self.user_number = m.get('UserNumber')
        return self


class GetAlinkAlgoInfoResponseBodyData(TeaModel):
    def __init__(
        self,
        alink_url: str = None,
        need_trans: bool = None,
        public_key_str: str = None,
    ):
        self.alink_url = alink_url
        self.need_trans = need_trans
        self.public_key_str = public_key_str

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alink_url is not None:
            result['AlinkUrl'] = self.alink_url
        if self.need_trans is not None:
            result['NeedTrans'] = self.need_trans
        if self.public_key_str is not None:
            result['PublicKeyStr'] = self.public_key_str
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlinkUrl') is not None:
            self.alink_url = m.get('AlinkUrl')
        if m.get('NeedTrans') is not None:
            self.need_trans = m.get('NeedTrans')
        if m.get('PublicKeyStr') is not None:
            self.public_key_str = m.get('PublicKeyStr')
        return self


class GetAlinkAlgoInfoResponseBody(TeaModel):
    def __init__(
        self,
        data: GetAlinkAlgoInfoResponseBodyData = None,
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
            temp_model = GetAlinkAlgoInfoResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetAlinkAlgoInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetAlinkAlgoInfoResponseBody = None,
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
            temp_model = GetAlinkAlgoInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAlinkAlgoPublicKeyResponseBodyData(TeaModel):
    def __init__(
        self,
        alink_url: str = None,
        public_key_str: str = None,
    ):
        self.alink_url = alink_url
        self.public_key_str = public_key_str

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alink_url is not None:
            result['AlinkUrl'] = self.alink_url
        if self.public_key_str is not None:
            result['PublicKeyStr'] = self.public_key_str
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlinkUrl') is not None:
            self.alink_url = m.get('AlinkUrl')
        if m.get('PublicKeyStr') is not None:
            self.public_key_str = m.get('PublicKeyStr')
        return self


class GetAlinkAlgoPublicKeyResponseBody(TeaModel):
    def __init__(
        self,
        data: GetAlinkAlgoPublicKeyResponseBodyData = None,
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
            temp_model = GetAlinkAlgoPublicKeyResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetAlinkAlgoPublicKeyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetAlinkAlgoPublicKeyResponseBody = None,
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
            temp_model = GetAlinkAlgoPublicKeyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetProjectInfoRequest(TeaModel):
    def __init__(
        self,
        project_id: int = None,
    ):
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class GetProjectInfoResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: Dict[str, Any] = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        # project info
        self.data = data
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
        if self.data is not None:
            result['Data'] = self.data
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
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetProjectInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetProjectInfoResponseBody = None,
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
            temp_model = GetProjectInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUsedProjectsResponseBodyData(TeaModel):
    def __init__(
        self,
        project_desc: str = None,
        project_id: int = None,
        project_identifier: str = None,
        project_name: str = None,
        tenant_id: int = None,
    ):
        self.project_desc = project_desc
        self.project_id = project_id
        self.project_identifier = project_identifier
        self.project_name = project_name
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_desc is not None:
            result['ProjectDesc'] = self.project_desc
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.project_identifier is not None:
            result['ProjectIdentifier'] = self.project_identifier
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectDesc') is not None:
            self.project_desc = m.get('ProjectDesc')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ProjectIdentifier') is not None:
            self.project_identifier = m.get('ProjectIdentifier')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class ListUsedProjectsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[ListUsedProjectsResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        # project列表
        self.data = data
        self.message = message
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
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListUsedProjectsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListUsedProjectsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListUsedProjectsResponseBody = None,
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
            temp_model = ListUsedProjectsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUsedProjectsByOwnerResponseBodyData(TeaModel):
    def __init__(
        self,
        project_desc: str = None,
        project_id: int = None,
        project_identifier: str = None,
        project_name: str = None,
        tenant_id: int = None,
    ):
        self.project_desc = project_desc
        self.project_id = project_id
        self.project_identifier = project_identifier
        self.project_name = project_name
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_desc is not None:
            result['ProjectDesc'] = self.project_desc
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.project_identifier is not None:
            result['ProjectIdentifier'] = self.project_identifier
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectDesc') is not None:
            self.project_desc = m.get('ProjectDesc')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ProjectIdentifier') is not None:
            self.project_identifier = m.get('ProjectIdentifier')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class ListUsedProjectsByOwnerResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[ListUsedProjectsByOwnerResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        # project列表
        self.data = data
        self.message = message
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
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListUsedProjectsByOwnerResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListUsedProjectsByOwnerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListUsedProjectsByOwnerResponseBody = None,
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
            temp_model = ListUsedProjectsByOwnerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveAutomlJobIdRequest(TeaModel):
    def __init__(
        self,
        instance_id: int = None,
        job_id: int = None,
        task_id: int = None,
    ):
        self.instance_id = instance_id
        self.job_id = job_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class SaveAutomlJobIdResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
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
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SaveAutomlJobIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SaveAutomlJobIdResponseBody = None,
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
            temp_model = SaveAutomlJobIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveAutomlModelRequest(TeaModel):
    def __init__(
        self,
        auc: str = None,
        execution_record_id: int = None,
        experiment_id: int = None,
        f_1score: str = None,
        id: int = None,
        indicator: str = None,
        indicator_data: str = None,
        instance_id: int = None,
        is_migrate: int = None,
        iterations: int = None,
        model_index: int = None,
        model_name: str = None,
        model_param: str = None,
        precision_score: str = None,
        recall: str = None,
        roc: str = None,
        status: int = None,
        task_id: int = None,
    ):
        self.auc = auc
        self.execution_record_id = execution_record_id
        self.experiment_id = experiment_id
        self.f_1score = f_1score
        self.id = id
        self.indicator = indicator
        self.indicator_data = indicator_data
        self.instance_id = instance_id
        self.is_migrate = is_migrate
        self.iterations = iterations
        self.model_index = model_index
        self.model_name = model_name
        self.model_param = model_param
        self.precision_score = precision_score
        self.recall = recall
        self.roc = roc
        self.status = status
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auc is not None:
            result['Auc'] = self.auc
        if self.execution_record_id is not None:
            result['ExecutionRecordId'] = self.execution_record_id
        if self.experiment_id is not None:
            result['ExperimentId'] = self.experiment_id
        if self.f_1score is not None:
            result['F1score'] = self.f_1score
        if self.id is not None:
            result['Id'] = self.id
        if self.indicator is not None:
            result['Indicator'] = self.indicator
        if self.indicator_data is not None:
            result['IndicatorData'] = self.indicator_data
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.is_migrate is not None:
            result['IsMigrate'] = self.is_migrate
        if self.iterations is not None:
            result['Iterations'] = self.iterations
        if self.model_index is not None:
            result['ModelIndex'] = self.model_index
        if self.model_name is not None:
            result['ModelName'] = self.model_name
        if self.model_param is not None:
            result['ModelParam'] = self.model_param
        if self.precision_score is not None:
            result['PrecisionScore'] = self.precision_score
        if self.recall is not None:
            result['Recall'] = self.recall
        if self.roc is not None:
            result['Roc'] = self.roc
        if self.status is not None:
            result['Status'] = self.status
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Auc') is not None:
            self.auc = m.get('Auc')
        if m.get('ExecutionRecordId') is not None:
            self.execution_record_id = m.get('ExecutionRecordId')
        if m.get('ExperimentId') is not None:
            self.experiment_id = m.get('ExperimentId')
        if m.get('F1score') is not None:
            self.f_1score = m.get('F1score')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Indicator') is not None:
            self.indicator = m.get('Indicator')
        if m.get('IndicatorData') is not None:
            self.indicator_data = m.get('IndicatorData')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('IsMigrate') is not None:
            self.is_migrate = m.get('IsMigrate')
        if m.get('Iterations') is not None:
            self.iterations = m.get('Iterations')
        if m.get('ModelIndex') is not None:
            self.model_index = m.get('ModelIndex')
        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')
        if m.get('ModelParam') is not None:
            self.model_param = m.get('ModelParam')
        if m.get('PrecisionScore') is not None:
            self.precision_score = m.get('PrecisionScore')
        if m.get('Recall') is not None:
            self.recall = m.get('Recall')
        if m.get('Roc') is not None:
            self.roc = m.get('Roc')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class SaveAutomlModelResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
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
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SaveAutomlModelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SaveAutomlModelResponseBody = None,
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
            temp_model = SaveAutomlModelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveOdpsInstanceRequest(TeaModel):
    def __init__(
        self,
        gmt_create: str = None,
        node_instance_id: int = None,
        odps_instance_id: str = None,
        odps_instance_status: int = None,
        task_id: str = None,
    ):
        self.gmt_create = gmt_create
        self.node_instance_id = node_instance_id
        self.odps_instance_id = odps_instance_id
        self.odps_instance_status = odps_instance_status
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.node_instance_id is not None:
            result['NodeInstanceId'] = self.node_instance_id
        if self.odps_instance_id is not None:
            result['OdpsInstanceId'] = self.odps_instance_id
        if self.odps_instance_status is not None:
            result['OdpsInstanceStatus'] = self.odps_instance_status
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('NodeInstanceId') is not None:
            self.node_instance_id = m.get('NodeInstanceId')
        if m.get('OdpsInstanceId') is not None:
            self.odps_instance_id = m.get('OdpsInstanceId')
        if m.get('OdpsInstanceStatus') is not None:
            self.odps_instance_status = m.get('OdpsInstanceStatus')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class SaveOdpsInstanceResponseBody(TeaModel):
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


class SaveOdpsInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SaveOdpsInstanceResponseBody = None,
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
            temp_model = SaveOdpsInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


