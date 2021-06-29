# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class CreateFaceGroupRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        name: str = None,
    ):
        self.owner_id = owner_id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class CreateFaceGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        group_id: str = None,
    ):
        self.request_id = request_id
        self.group_id = group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        return self


class CreateFaceGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateFaceGroupResponseBody = None,
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
            temp_model = CreateFaceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFilePredictRequest(TeaModel):
    def __init__(
        self,
        algorithm_code: str = None,
        resource_url: str = None,
        push_config: str = None,
        decrypt_config: str = None,
        client_token: str = None,
        output_oss: str = None,
        output_region: str = None,
    ):
        self.algorithm_code = algorithm_code
        self.resource_url = resource_url
        self.push_config = push_config
        self.decrypt_config = decrypt_config
        self.client_token = client_token
        self.output_oss = output_oss
        self.output_region = output_region

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm_code is not None:
            result['AlgorithmCode'] = self.algorithm_code
        if self.resource_url is not None:
            result['ResourceUrl'] = self.resource_url
        if self.push_config is not None:
            result['PushConfig'] = self.push_config
        if self.decrypt_config is not None:
            result['DecryptConfig'] = self.decrypt_config
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.output_oss is not None:
            result['OutputOss'] = self.output_oss
        if self.output_region is not None:
            result['OutputRegion'] = self.output_region
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlgorithmCode') is not None:
            self.algorithm_code = m.get('AlgorithmCode')
        if m.get('ResourceUrl') is not None:
            self.resource_url = m.get('ResourceUrl')
        if m.get('PushConfig') is not None:
            self.push_config = m.get('PushConfig')
        if m.get('DecryptConfig') is not None:
            self.decrypt_config = m.get('DecryptConfig')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('OutputOss') is not None:
            self.output_oss = m.get('OutputOss')
        if m.get('OutputRegion') is not None:
            self.output_region = m.get('OutputRegion')
        return self


class CreateFilePredictResponseBodyData(TeaModel):
    def __init__(
        self,
        task_id: str = None,
    ):
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CreateFilePredictResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: CreateFilePredictResponseBodyData = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = CreateFilePredictResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class CreateFilePredictResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateFilePredictResponseBody = None,
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
            temp_model = CreateFilePredictResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateStreamPredictRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        client_token: str = None,
        stream_type: str = None,
        stream_id: str = None,
        predict_template_id: str = None,
        model_ids: str = None,
        probability_thresholds: str = None,
        detect_intervals: str = None,
        output: str = None,
        notify: str = None,
        auto_start: str = None,
        face_group_id: str = None,
        model_user_data: str = None,
    ):
        self.owner_id = owner_id
        self.client_token = client_token
        self.stream_type = stream_type
        self.stream_id = stream_id
        self.predict_template_id = predict_template_id
        self.model_ids = model_ids
        self.probability_thresholds = probability_thresholds
        self.detect_intervals = detect_intervals
        self.output = output
        self.notify = notify
        self.auto_start = auto_start
        self.face_group_id = face_group_id
        self.model_user_data = model_user_data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.stream_type is not None:
            result['StreamType'] = self.stream_type
        if self.stream_id is not None:
            result['StreamId'] = self.stream_id
        if self.predict_template_id is not None:
            result['PredictTemplateId'] = self.predict_template_id
        if self.model_ids is not None:
            result['ModelIds'] = self.model_ids
        if self.probability_thresholds is not None:
            result['ProbabilityThresholds'] = self.probability_thresholds
        if self.detect_intervals is not None:
            result['DetectIntervals'] = self.detect_intervals
        if self.output is not None:
            result['Output'] = self.output
        if self.notify is not None:
            result['Notify'] = self.notify
        if self.auto_start is not None:
            result['AutoStart'] = self.auto_start
        if self.face_group_id is not None:
            result['FaceGroupId'] = self.face_group_id
        if self.model_user_data is not None:
            result['ModelUserData'] = self.model_user_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('StreamType') is not None:
            self.stream_type = m.get('StreamType')
        if m.get('StreamId') is not None:
            self.stream_id = m.get('StreamId')
        if m.get('PredictTemplateId') is not None:
            self.predict_template_id = m.get('PredictTemplateId')
        if m.get('ModelIds') is not None:
            self.model_ids = m.get('ModelIds')
        if m.get('ProbabilityThresholds') is not None:
            self.probability_thresholds = m.get('ProbabilityThresholds')
        if m.get('DetectIntervals') is not None:
            self.detect_intervals = m.get('DetectIntervals')
        if m.get('Output') is not None:
            self.output = m.get('Output')
        if m.get('Notify') is not None:
            self.notify = m.get('Notify')
        if m.get('AutoStart') is not None:
            self.auto_start = m.get('AutoStart')
        if m.get('FaceGroupId') is not None:
            self.face_group_id = m.get('FaceGroupId')
        if m.get('ModelUserData') is not None:
            self.model_user_data = m.get('ModelUserData')
        return self


class CreateStreamPredictResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        predict_id: str = None,
    ):
        self.request_id = request_id
        self.predict_id = predict_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.predict_id is not None:
            result['PredictId'] = self.predict_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PredictId') is not None:
            self.predict_id = m.get('PredictId')
        return self


class CreateStreamPredictResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateStreamPredictResponseBody = None,
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
            temp_model = CreateStreamPredictResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteFaceGroupRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        group_id: str = None,
    ):
        self.owner_id = owner_id
        self.group_id = group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        return self


class DeleteFaceGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        group_id: str = None,
    ):
        self.request_id = request_id
        self.group_id = group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        return self


class DeleteFaceGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteFaceGroupResponseBody = None,
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
            temp_model = DeleteFaceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteFilePredictRequest(TeaModel):
    def __init__(
        self,
        task_id: str = None,
    ):
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DeleteFilePredictResponseBodyData(TeaModel):
    def __init__(
        self,
        task_id: str = None,
    ):
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DeleteFilePredictResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: DeleteFilePredictResponseBodyData = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = DeleteFilePredictResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class DeleteFilePredictResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteFilePredictResponseBody = None,
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
            temp_model = DeleteFilePredictResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteStreamPredictRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        predict_id: str = None,
    ):
        self.owner_id = owner_id
        self.predict_id = predict_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.predict_id is not None:
            result['PredictId'] = self.predict_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PredictId') is not None:
            self.predict_id = m.get('PredictId')
        return self


class DeleteStreamPredictResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        predict_id: str = None,
    ):
        self.request_id = request_id
        self.predict_id = predict_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.predict_id is not None:
            result['PredictId'] = self.predict_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PredictId') is not None:
            self.predict_id = m.get('PredictId')
        return self


class DeleteStreamPredictResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteStreamPredictResponseBody = None,
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
            temp_model = DeleteStreamPredictResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFaceGroupsRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        next_page_token: str = None,
        current_page: int = None,
        page_size: int = None,
    ):
        self.owner_id = owner_id
        self.next_page_token = next_page_token
        self.current_page = current_page
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.next_page_token is not None:
            result['NextPageToken'] = self.next_page_token
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('NextPageToken') is not None:
            self.next_page_token = m.get('NextPageToken')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeFaceGroupsResponseBodyGroups(TeaModel):
    def __init__(
        self,
        creation_time: str = None,
        group_id: str = None,
        name: str = None,
    ):
        self.creation_time = creation_time
        self.group_id = group_id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DescribeFaceGroupsResponseBody(TeaModel):
    def __init__(
        self,
        total_num: int = None,
        page_size: int = None,
        request_id: str = None,
        current_page: int = None,
        next_page_token: str = None,
        groups: List[DescribeFaceGroupsResponseBodyGroups] = None,
    ):
        self.total_num = total_num
        self.page_size = page_size
        self.request_id = request_id
        self.current_page = current_page
        self.next_page_token = next_page_token
        self.groups = groups

    def validate(self):
        if self.groups:
            for k in self.groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.next_page_token is not None:
            result['NextPageToken'] = self.next_page_token
        result['Groups'] = []
        if self.groups is not None:
            for k in self.groups:
                result['Groups'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('NextPageToken') is not None:
            self.next_page_token = m.get('NextPageToken')
        self.groups = []
        if m.get('Groups') is not None:
            for k in m.get('Groups'):
                temp_model = DescribeFaceGroupsResponseBodyGroups()
                self.groups.append(temp_model.from_map(k))
        return self


class DescribeFaceGroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeFaceGroupsResponseBody = None,
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
            temp_model = DescribeFaceGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeStreamPredictResultRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        predict_id: str = None,
        model_id: str = None,
        start_time: str = None,
        end_time: str = None,
        probability_threshold: str = None,
        next_page_token: str = None,
        current_page: int = None,
        page_size: int = None,
    ):
        self.owner_id = owner_id
        self.predict_id = predict_id
        self.model_id = model_id
        self.start_time = start_time
        self.end_time = end_time
        self.probability_threshold = probability_threshold
        self.next_page_token = next_page_token
        self.current_page = current_page
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.predict_id is not None:
            result['PredictId'] = self.predict_id
        if self.model_id is not None:
            result['ModelId'] = self.model_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.probability_threshold is not None:
            result['ProbabilityThreshold'] = self.probability_threshold
        if self.next_page_token is not None:
            result['NextPageToken'] = self.next_page_token
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PredictId') is not None:
            self.predict_id = m.get('PredictId')
        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('ProbabilityThreshold') is not None:
            self.probability_threshold = m.get('ProbabilityThreshold')
        if m.get('NextPageToken') is not None:
            self.next_page_token = m.get('NextPageToken')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeStreamPredictResultResponseBodyStreamPredictDatas(TeaModel):
    def __init__(
        self,
        status: str = None,
        predict_result: str = None,
        predict_id: str = None,
        predict_time: str = None,
        data_url: str = None,
        timestamp: int = None,
        model_id: str = None,
    ):
        self.status = status
        self.predict_result = predict_result
        self.predict_id = predict_id
        self.predict_time = predict_time
        self.data_url = data_url
        self.timestamp = timestamp
        self.model_id = model_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.predict_result is not None:
            result['PredictResult'] = self.predict_result
        if self.predict_id is not None:
            result['PredictId'] = self.predict_id
        if self.predict_time is not None:
            result['PredictTime'] = self.predict_time
        if self.data_url is not None:
            result['DataUrl'] = self.data_url
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.model_id is not None:
            result['ModelId'] = self.model_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('PredictResult') is not None:
            self.predict_result = m.get('PredictResult')
        if m.get('PredictId') is not None:
            self.predict_id = m.get('PredictId')
        if m.get('PredictTime') is not None:
            self.predict_time = m.get('PredictTime')
        if m.get('DataUrl') is not None:
            self.data_url = m.get('DataUrl')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')
        return self


class DescribeStreamPredictResultResponseBody(TeaModel):
    def __init__(
        self,
        stream_predict_datas: List[DescribeStreamPredictResultResponseBodyStreamPredictDatas] = None,
        total_num: int = None,
        page_size: int = None,
        request_id: str = None,
        current_page: int = None,
        next_page_token: str = None,
    ):
        self.stream_predict_datas = stream_predict_datas
        self.total_num = total_num
        self.page_size = page_size
        self.request_id = request_id
        self.current_page = current_page
        self.next_page_token = next_page_token

    def validate(self):
        if self.stream_predict_datas:
            for k in self.stream_predict_datas:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['StreamPredictDatas'] = []
        if self.stream_predict_datas is not None:
            for k in self.stream_predict_datas:
                result['StreamPredictDatas'].append(k.to_map() if k else None)
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.next_page_token is not None:
            result['NextPageToken'] = self.next_page_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.stream_predict_datas = []
        if m.get('StreamPredictDatas') is not None:
            for k in m.get('StreamPredictDatas'):
                temp_model = DescribeStreamPredictResultResponseBodyStreamPredictDatas()
                self.stream_predict_datas.append(temp_model.from_map(k))
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('NextPageToken') is not None:
            self.next_page_token = m.get('NextPageToken')
        return self


class DescribeStreamPredictResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeStreamPredictResultResponseBody = None,
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
            temp_model = DescribeStreamPredictResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeStreamPredictsRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        predict_ids: str = None,
        model_id: str = None,
        next_page_token: str = None,
        current_page: int = None,
        page_size: int = None,
    ):
        self.owner_id = owner_id
        self.predict_ids = predict_ids
        self.model_id = model_id
        self.next_page_token = next_page_token
        self.current_page = current_page
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.predict_ids is not None:
            result['PredictIds'] = self.predict_ids
        if self.model_id is not None:
            result['ModelId'] = self.model_id
        if self.next_page_token is not None:
            result['NextPageToken'] = self.next_page_token
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PredictIds') is not None:
            self.predict_ids = m.get('PredictIds')
        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')
        if m.get('NextPageToken') is not None:
            self.next_page_token = m.get('NextPageToken')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeStreamPredictsResponseBodyStreamPredicts(TeaModel):
    def __init__(
        self,
        creation_time: str = None,
        status: str = None,
        notify: str = None,
        predict_id: str = None,
        model_user_data: str = None,
        output: str = None,
        predict_template_id: str = None,
        stream_id: str = None,
        auto_start: str = None,
        probability_thresholds: str = None,
        detect_intervals: str = None,
        stream_type: str = None,
        user_data: str = None,
        model_ids: str = None,
        face_group_id: str = None,
    ):
        self.creation_time = creation_time
        self.status = status
        self.notify = notify
        self.predict_id = predict_id
        self.model_user_data = model_user_data
        self.output = output
        self.predict_template_id = predict_template_id
        self.stream_id = stream_id
        self.auto_start = auto_start
        self.probability_thresholds = probability_thresholds
        self.detect_intervals = detect_intervals
        self.stream_type = stream_type
        self.user_data = user_data
        self.model_ids = model_ids
        self.face_group_id = face_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.status is not None:
            result['Status'] = self.status
        if self.notify is not None:
            result['Notify'] = self.notify
        if self.predict_id is not None:
            result['PredictId'] = self.predict_id
        if self.model_user_data is not None:
            result['ModelUserData'] = self.model_user_data
        if self.output is not None:
            result['Output'] = self.output
        if self.predict_template_id is not None:
            result['PredictTemplateId'] = self.predict_template_id
        if self.stream_id is not None:
            result['StreamId'] = self.stream_id
        if self.auto_start is not None:
            result['AutoStart'] = self.auto_start
        if self.probability_thresholds is not None:
            result['ProbabilityThresholds'] = self.probability_thresholds
        if self.detect_intervals is not None:
            result['DetectIntervals'] = self.detect_intervals
        if self.stream_type is not None:
            result['StreamType'] = self.stream_type
        if self.user_data is not None:
            result['UserData'] = self.user_data
        if self.model_ids is not None:
            result['ModelIds'] = self.model_ids
        if self.face_group_id is not None:
            result['FaceGroupId'] = self.face_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Notify') is not None:
            self.notify = m.get('Notify')
        if m.get('PredictId') is not None:
            self.predict_id = m.get('PredictId')
        if m.get('ModelUserData') is not None:
            self.model_user_data = m.get('ModelUserData')
        if m.get('Output') is not None:
            self.output = m.get('Output')
        if m.get('PredictTemplateId') is not None:
            self.predict_template_id = m.get('PredictTemplateId')
        if m.get('StreamId') is not None:
            self.stream_id = m.get('StreamId')
        if m.get('AutoStart') is not None:
            self.auto_start = m.get('AutoStart')
        if m.get('ProbabilityThresholds') is not None:
            self.probability_thresholds = m.get('ProbabilityThresholds')
        if m.get('DetectIntervals') is not None:
            self.detect_intervals = m.get('DetectIntervals')
        if m.get('StreamType') is not None:
            self.stream_type = m.get('StreamType')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        if m.get('ModelIds') is not None:
            self.model_ids = m.get('ModelIds')
        if m.get('FaceGroupId') is not None:
            self.face_group_id = m.get('FaceGroupId')
        return self


class DescribeStreamPredictsResponseBody(TeaModel):
    def __init__(
        self,
        total_num: int = None,
        page_size: int = None,
        request_id: str = None,
        current_page: int = None,
        next_page_token: str = None,
        stream_predicts: List[DescribeStreamPredictsResponseBodyStreamPredicts] = None,
    ):
        self.total_num = total_num
        self.page_size = page_size
        self.request_id = request_id
        self.current_page = current_page
        self.next_page_token = next_page_token
        self.stream_predicts = stream_predicts

    def validate(self):
        if self.stream_predicts:
            for k in self.stream_predicts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.next_page_token is not None:
            result['NextPageToken'] = self.next_page_token
        result['StreamPredicts'] = []
        if self.stream_predicts is not None:
            for k in self.stream_predicts:
                result['StreamPredicts'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('NextPageToken') is not None:
            self.next_page_token = m.get('NextPageToken')
        self.stream_predicts = []
        if m.get('StreamPredicts') is not None:
            for k in m.get('StreamPredicts'):
                temp_model = DescribeStreamPredictsResponseBodyStreamPredicts()
                self.stream_predicts.append(temp_model.from_map(k))
        return self


class DescribeStreamPredictsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeStreamPredictsResponseBody = None,
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
            temp_model = DescribeStreamPredictsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAlgorithmDetailRequest(TeaModel):
    def __init__(
        self,
        algorithm_code: str = None,
    ):
        self.algorithm_code = algorithm_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm_code is not None:
            result['AlgorithmCode'] = self.algorithm_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlgorithmCode') is not None:
            self.algorithm_code = m.get('AlgorithmCode')
        return self


class GetAlgorithmDetailResponseBodyData(TeaModel):
    def __init__(
        self,
        algorithm_name: str = None,
        deploy_region: str = None,
        current_month_count: int = None,
        algorithm_code: str = None,
        api_doc_url: str = None,
        current_month_success_count: int = None,
    ):
        self.algorithm_name = algorithm_name
        self.deploy_region = deploy_region
        self.current_month_count = current_month_count
        self.algorithm_code = algorithm_code
        self.api_doc_url = api_doc_url
        self.current_month_success_count = current_month_success_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm_name is not None:
            result['AlgorithmName'] = self.algorithm_name
        if self.deploy_region is not None:
            result['DeployRegion'] = self.deploy_region
        if self.current_month_count is not None:
            result['CurrentMonthCount'] = self.current_month_count
        if self.algorithm_code is not None:
            result['AlgorithmCode'] = self.algorithm_code
        if self.api_doc_url is not None:
            result['ApiDocUrl'] = self.api_doc_url
        if self.current_month_success_count is not None:
            result['CurrentMonthSuccessCount'] = self.current_month_success_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlgorithmName') is not None:
            self.algorithm_name = m.get('AlgorithmName')
        if m.get('DeployRegion') is not None:
            self.deploy_region = m.get('DeployRegion')
        if m.get('CurrentMonthCount') is not None:
            self.current_month_count = m.get('CurrentMonthCount')
        if m.get('AlgorithmCode') is not None:
            self.algorithm_code = m.get('AlgorithmCode')
        if m.get('ApiDocUrl') is not None:
            self.api_doc_url = m.get('ApiDocUrl')
        if m.get('CurrentMonthSuccessCount') is not None:
            self.current_month_success_count = m.get('CurrentMonthSuccessCount')
        return self


class GetAlgorithmDetailResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: GetAlgorithmDetailResponseBodyData = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = GetAlgorithmDetailResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetAlgorithmDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetAlgorithmDetailResponseBody = None,
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
            temp_model = GetAlgorithmDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAlgorithmHistogramsRequest(TeaModel):
    def __init__(
        self,
        algorithm_code: str = None,
        start_date: str = None,
        end_date: str = None,
        aggregate_type: str = None,
    ):
        self.algorithm_code = algorithm_code
        self.start_date = start_date
        self.end_date = end_date
        self.aggregate_type = aggregate_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm_code is not None:
            result['AlgorithmCode'] = self.algorithm_code
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.aggregate_type is not None:
            result['AggregateType'] = self.aggregate_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlgorithmCode') is not None:
            self.algorithm_code = m.get('AlgorithmCode')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('AggregateType') is not None:
            self.aggregate_type = m.get('AggregateType')
        return self


class GetAlgorithmHistogramsResponseBodyDataHistograms(TeaModel):
    def __init__(
        self,
        time: str = None,
        failure_count: int = None,
        success_count: int = None,
    ):
        self.time = time
        self.failure_count = failure_count
        self.success_count = success_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.time is not None:
            result['Time'] = self.time
        if self.failure_count is not None:
            result['FailureCount'] = self.failure_count
        if self.success_count is not None:
            result['SuccessCount'] = self.success_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Time') is not None:
            self.time = m.get('Time')
        if m.get('FailureCount') is not None:
            self.failure_count = m.get('FailureCount')
        if m.get('SuccessCount') is not None:
            self.success_count = m.get('SuccessCount')
        return self


class GetAlgorithmHistogramsResponseBodyData(TeaModel):
    def __init__(
        self,
        failure_count: int = None,
        success_count: int = None,
        histograms: List[GetAlgorithmHistogramsResponseBodyDataHistograms] = None,
    ):
        self.failure_count = failure_count
        self.success_count = success_count
        self.histograms = histograms

    def validate(self):
        if self.histograms:
            for k in self.histograms:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.failure_count is not None:
            result['FailureCount'] = self.failure_count
        if self.success_count is not None:
            result['SuccessCount'] = self.success_count
        result['Histograms'] = []
        if self.histograms is not None:
            for k in self.histograms:
                result['Histograms'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FailureCount') is not None:
            self.failure_count = m.get('FailureCount')
        if m.get('SuccessCount') is not None:
            self.success_count = m.get('SuccessCount')
        self.histograms = []
        if m.get('Histograms') is not None:
            for k in m.get('Histograms'):
                temp_model = GetAlgorithmHistogramsResponseBodyDataHistograms()
                self.histograms.append(temp_model.from_map(k))
        return self


class GetAlgorithmHistogramsResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: GetAlgorithmHistogramsResponseBodyData = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = GetAlgorithmHistogramsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetAlgorithmHistogramsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetAlgorithmHistogramsResponseBody = None,
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
            temp_model = GetAlgorithmHistogramsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ImagePredictRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        model_id: str = None,
        data_url: str = None,
    ):
        self.owner_id = owner_id
        self.model_id = model_id
        self.data_url = data_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.model_id is not None:
            result['ModelId'] = self.model_id
        if self.data_url is not None:
            result['DataUrl'] = self.data_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')
        if m.get('DataUrl') is not None:
            self.data_url = m.get('DataUrl')
        return self


class ImagePredictResponseBodyImagePredict(TeaModel):
    def __init__(
        self,
        status: str = None,
        predict_result: str = None,
        predict_id: str = None,
        predict_time: str = None,
        data_url: str = None,
        code: str = None,
        message: str = None,
        model_id: str = None,
    ):
        self.status = status
        self.predict_result = predict_result
        self.predict_id = predict_id
        self.predict_time = predict_time
        self.data_url = data_url
        self.code = code
        self.message = message
        self.model_id = model_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.predict_result is not None:
            result['PredictResult'] = self.predict_result
        if self.predict_id is not None:
            result['PredictId'] = self.predict_id
        if self.predict_time is not None:
            result['PredictTime'] = self.predict_time
        if self.data_url is not None:
            result['DataUrl'] = self.data_url
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.model_id is not None:
            result['ModelId'] = self.model_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('PredictResult') is not None:
            self.predict_result = m.get('PredictResult')
        if m.get('PredictId') is not None:
            self.predict_id = m.get('PredictId')
        if m.get('PredictTime') is not None:
            self.predict_time = m.get('PredictTime')
        if m.get('DataUrl') is not None:
            self.data_url = m.get('DataUrl')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')
        return self


class ImagePredictResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        image_predict: ImagePredictResponseBodyImagePredict = None,
    ):
        self.request_id = request_id
        self.image_predict = image_predict

    def validate(self):
        if self.image_predict:
            self.image_predict.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.image_predict is not None:
            result['ImagePredict'] = self.image_predict.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ImagePredict') is not None:
            temp_model = ImagePredictResponseBodyImagePredict()
            self.image_predict = temp_model.from_map(m['ImagePredict'])
        return self


class ImagePredictResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ImagePredictResponseBody = None,
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
            temp_model = ImagePredictResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListMyAlgorithmRequest(TeaModel):
    def __init__(
        self,
        algorithm_name: str = None,
        page_size: int = None,
        page_number: int = None,
    ):
        self.algorithm_name = algorithm_name
        self.page_size = page_size
        self.page_number = page_number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm_name is not None:
            result['AlgorithmName'] = self.algorithm_name
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlgorithmName') is not None:
            self.algorithm_name = m.get('AlgorithmName')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        return self


class ListMyAlgorithmResponseBodyDataAlgorithmList(TeaModel):
    def __init__(
        self,
        algorithm_name: str = None,
        deploy_region: str = None,
        current_month_count: int = None,
        algorithm_code: str = None,
        api_doc_url: str = None,
        yesterday_count: int = None,
        algorithm_order: int = None,
    ):
        self.algorithm_name = algorithm_name
        self.deploy_region = deploy_region
        self.current_month_count = current_month_count
        self.algorithm_code = algorithm_code
        self.api_doc_url = api_doc_url
        self.yesterday_count = yesterday_count
        self.algorithm_order = algorithm_order

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm_name is not None:
            result['AlgorithmName'] = self.algorithm_name
        if self.deploy_region is not None:
            result['DeployRegion'] = self.deploy_region
        if self.current_month_count is not None:
            result['CurrentMonthCount'] = self.current_month_count
        if self.algorithm_code is not None:
            result['AlgorithmCode'] = self.algorithm_code
        if self.api_doc_url is not None:
            result['ApiDocUrl'] = self.api_doc_url
        if self.yesterday_count is not None:
            result['YesterdayCount'] = self.yesterday_count
        if self.algorithm_order is not None:
            result['AlgorithmOrder'] = self.algorithm_order
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlgorithmName') is not None:
            self.algorithm_name = m.get('AlgorithmName')
        if m.get('DeployRegion') is not None:
            self.deploy_region = m.get('DeployRegion')
        if m.get('CurrentMonthCount') is not None:
            self.current_month_count = m.get('CurrentMonthCount')
        if m.get('AlgorithmCode') is not None:
            self.algorithm_code = m.get('AlgorithmCode')
        if m.get('ApiDocUrl') is not None:
            self.api_doc_url = m.get('ApiDocUrl')
        if m.get('YesterdayCount') is not None:
            self.yesterday_count = m.get('YesterdayCount')
        if m.get('AlgorithmOrder') is not None:
            self.algorithm_order = m.get('AlgorithmOrder')
        return self


class ListMyAlgorithmResponseBodyData(TeaModel):
    def __init__(
        self,
        algorithm_list: List[ListMyAlgorithmResponseBodyDataAlgorithmList] = None,
        page_size: int = None,
        page_number: int = None,
        total_count: int = None,
    ):
        self.algorithm_list = algorithm_list
        self.page_size = page_size
        self.page_number = page_number
        self.total_count = total_count

    def validate(self):
        if self.algorithm_list:
            for k in self.algorithm_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AlgorithmList'] = []
        if self.algorithm_list is not None:
            for k in self.algorithm_list:
                result['AlgorithmList'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.algorithm_list = []
        if m.get('AlgorithmList') is not None:
            for k in m.get('AlgorithmList'):
                temp_model = ListMyAlgorithmResponseBodyDataAlgorithmList()
                self.algorithm_list.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListMyAlgorithmResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: ListMyAlgorithmResponseBodyData = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = ListMyAlgorithmResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListMyAlgorithmResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListMyAlgorithmResponseBody = None,
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
            temp_model = ListMyAlgorithmResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PredictPictureRequest(TeaModel):
    def __init__(
        self,
        algorithm_code: str = None,
        oss_path: str = None,
        resource_url: str = None,
        customer_data: str = None,
        image_url: str = None,
    ):
        self.algorithm_code = algorithm_code
        self.oss_path = oss_path
        self.resource_url = resource_url
        self.customer_data = customer_data
        self.image_url = image_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm_code is not None:
            result['AlgorithmCode'] = self.algorithm_code
        if self.oss_path is not None:
            result['OssPath'] = self.oss_path
        if self.resource_url is not None:
            result['ResourceUrl'] = self.resource_url
        if self.customer_data is not None:
            result['CustomerData'] = self.customer_data
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlgorithmCode') is not None:
            self.algorithm_code = m.get('AlgorithmCode')
        if m.get('OssPath') is not None:
            self.oss_path = m.get('OssPath')
        if m.get('ResourceUrl') is not None:
            self.resource_url = m.get('ResourceUrl')
        if m.get('CustomerData') is not None:
            self.customer_data = m.get('CustomerData')
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        return self


class PredictPictureResponseBodyData(TeaModel):
    def __init__(
        self,
        predict_result: str = None,
    ):
        self.predict_result = predict_result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.predict_result is not None:
            result['PredictResult'] = self.predict_result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PredictResult') is not None:
            self.predict_result = m.get('PredictResult')
        return self


class PredictPictureResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: PredictPictureResponseBodyData = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = PredictPictureResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class PredictPictureResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: PredictPictureResponseBody = None,
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
            temp_model = PredictPictureResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RegisterFaceRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        group_id: str = None,
        data_type: str = None,
        content: str = None,
    ):
        self.owner_id = owner_id
        self.group_id = group_id
        self.data_type = data_type
        self.content = content

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.data_type is not None:
            result['DataType'] = self.data_type
        if self.content is not None:
            result['Content'] = self.content
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        return self


class RegisterFaceResponseBodyFacesRect(TeaModel):
    def __init__(
        self,
        top: int = None,
        width: int = None,
        height: int = None,
        left: int = None,
    ):
        self.top = top
        self.width = width
        self.height = height
        self.left = left

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.top is not None:
            result['Top'] = self.top
        if self.width is not None:
            result['Width'] = self.width
        if self.height is not None:
            result['Height'] = self.height
        if self.left is not None:
            result['Left'] = self.left
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Top') is not None:
            self.top = m.get('Top')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Left') is not None:
            self.left = m.get('Left')
        return self


class RegisterFaceResponseBodyFaces(TeaModel):
    def __init__(
        self,
        face_token: str = None,
        rect: RegisterFaceResponseBodyFacesRect = None,
    ):
        self.face_token = face_token
        self.rect = rect

    def validate(self):
        if self.rect:
            self.rect.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.face_token is not None:
            result['FaceToken'] = self.face_token
        if self.rect is not None:
            result['Rect'] = self.rect.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FaceToken') is not None:
            self.face_token = m.get('FaceToken')
        if m.get('Rect') is not None:
            temp_model = RegisterFaceResponseBodyFacesRect()
            self.rect = temp_model.from_map(m['Rect'])
        return self


class RegisterFaceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        faces: List[RegisterFaceResponseBodyFaces] = None,
        group_id: str = None,
    ):
        self.request_id = request_id
        self.faces = faces
        self.group_id = group_id

    def validate(self):
        if self.faces:
            for k in self.faces:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Faces'] = []
        if self.faces is not None:
            for k in self.faces:
                result['Faces'].append(k.to_map() if k else None)
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.faces = []
        if m.get('Faces') is not None:
            for k in m.get('Faces'):
                temp_model = RegisterFaceResponseBodyFaces()
                self.faces.append(temp_model.from_map(k))
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        return self


class RegisterFaceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RegisterFaceResponseBody = None,
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
            temp_model = RegisterFaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchFaceRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        group_id: str = None,
        probability_threshold: float = None,
        count: int = None,
        data_type: str = None,
        content: str = None,
    ):
        self.owner_id = owner_id
        self.group_id = group_id
        self.probability_threshold = probability_threshold
        self.count = count
        self.data_type = data_type
        self.content = content

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.probability_threshold is not None:
            result['ProbabilityThreshold'] = self.probability_threshold
        if self.count is not None:
            result['Count'] = self.count
        if self.data_type is not None:
            result['DataType'] = self.data_type
        if self.content is not None:
            result['Content'] = self.content
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('ProbabilityThreshold') is not None:
            self.probability_threshold = m.get('ProbabilityThreshold')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        return self


class SearchFaceResponseBodyRect(TeaModel):
    def __init__(
        self,
        top: int = None,
        width: int = None,
        height: int = None,
        left: int = None,
    ):
        self.top = top
        self.width = width
        self.height = height
        self.left = left

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.top is not None:
            result['Top'] = self.top
        if self.width is not None:
            result['Width'] = self.width
        if self.height is not None:
            result['Height'] = self.height
        if self.left is not None:
            result['Left'] = self.left
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Top') is not None:
            self.top = m.get('Top')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Left') is not None:
            self.left = m.get('Left')
        return self


class SearchFaceResponseBodyFaceResults(TeaModel):
    def __init__(
        self,
        face_token: str = None,
        probability: float = None,
    ):
        self.face_token = face_token
        self.probability = probability

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.face_token is not None:
            result['FaceToken'] = self.face_token
        if self.probability is not None:
            result['Probability'] = self.probability
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FaceToken') is not None:
            self.face_token = m.get('FaceToken')
        if m.get('Probability') is not None:
            self.probability = m.get('Probability')
        return self


class SearchFaceResponseBody(TeaModel):
    def __init__(
        self,
        rect: SearchFaceResponseBodyRect = None,
        request_id: str = None,
        face_results: List[SearchFaceResponseBodyFaceResults] = None,
        group_id: str = None,
    ):
        self.rect = rect
        self.request_id = request_id
        self.face_results = face_results
        self.group_id = group_id

    def validate(self):
        if self.rect:
            self.rect.validate()
        if self.face_results:
            for k in self.face_results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rect is not None:
            result['Rect'] = self.rect.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['FaceResults'] = []
        if self.face_results is not None:
            for k in self.face_results:
                result['FaceResults'].append(k.to_map() if k else None)
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Rect') is not None:
            temp_model = SearchFaceResponseBodyRect()
            self.rect = temp_model.from_map(m['Rect'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.face_results = []
        if m.get('FaceResults') is not None:
            for k in m.get('FaceResults'):
                temp_model = SearchFaceResponseBodyFaceResults()
                self.face_results.append(temp_model.from_map(k))
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        return self


class SearchFaceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SearchFaceResponseBody = None,
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
            temp_model = SearchFaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartStreamPredictRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        predict_id: str = None,
    ):
        self.owner_id = owner_id
        self.predict_id = predict_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.predict_id is not None:
            result['PredictId'] = self.predict_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PredictId') is not None:
            self.predict_id = m.get('PredictId')
        return self


class StartStreamPredictResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        predict_id: str = None,
    ):
        self.request_id = request_id
        self.predict_id = predict_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.predict_id is not None:
            result['PredictId'] = self.predict_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PredictId') is not None:
            self.predict_id = m.get('PredictId')
        return self


class StartStreamPredictResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StartStreamPredictResponseBody = None,
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
            temp_model = StartStreamPredictResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopStreamPredictRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        predict_id: str = None,
    ):
        self.owner_id = owner_id
        self.predict_id = predict_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.predict_id is not None:
            result['PredictId'] = self.predict_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PredictId') is not None:
            self.predict_id = m.get('PredictId')
        return self


class StopStreamPredictResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        predict_id: str = None,
    ):
        self.request_id = request_id
        self.predict_id = predict_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.predict_id is not None:
            result['PredictId'] = self.predict_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PredictId') is not None:
            self.predict_id = m.get('PredictId')
        return self


class StopStreamPredictResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StopStreamPredictResponseBody = None,
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
            temp_model = StopStreamPredictResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnregisterFaceRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        group_id: str = None,
        face_token: str = None,
    ):
        self.owner_id = owner_id
        self.group_id = group_id
        self.face_token = face_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.face_token is not None:
            result['FaceToken'] = self.face_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('FaceToken') is not None:
            self.face_token = m.get('FaceToken')
        return self


class UnregisterFaceResponseBody(TeaModel):
    def __init__(
        self,
        face_token: str = None,
        request_id: str = None,
        group_id: str = None,
    ):
        self.face_token = face_token
        self.request_id = request_id
        self.group_id = group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.face_token is not None:
            result['FaceToken'] = self.face_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FaceToken') is not None:
            self.face_token = m.get('FaceToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        return self


class UnregisterFaceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UnregisterFaceResponseBody = None,
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
            temp_model = UnregisterFaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


