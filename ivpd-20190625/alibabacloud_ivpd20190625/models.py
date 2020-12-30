# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List, Any, BinaryIO


class AssessCompositionRequest(TeaModel):
    def __init__(
        self,
        image_url: str = None,
    ):
        self.image_url = image_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        return self


class AssessCompositionResponseBodyData(TeaModel):
    def __init__(
        self,
        score: float = None,
    ):
        self.score = score

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.score is not None:
            result['Score'] = self.score
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Score') is not None:
            self.score = m.get('Score')
        return self


class AssessCompositionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: AssessCompositionResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = AssessCompositionResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class AssessCompositionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AssessCompositionResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = AssessCompositionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AssessExposureRequest(TeaModel):
    def __init__(
        self,
        image_url: str = None,
    ):
        self.image_url = image_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        return self


class AssessExposureResponseBodyData(TeaModel):
    def __init__(
        self,
        exposure: float = None,
    ):
        self.exposure = exposure

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.exposure is not None:
            result['Exposure'] = self.exposure
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Exposure') is not None:
            self.exposure = m.get('Exposure')
        return self


class AssessExposureResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: AssessExposureResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = AssessExposureResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class AssessExposureResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AssessExposureResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = AssessExposureResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AssessSharpnessRequest(TeaModel):
    def __init__(
        self,
        image_url: str = None,
    ):
        self.image_url = image_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        return self


class AssessSharpnessResponseBodyData(TeaModel):
    def __init__(
        self,
        sharpness: float = None,
    ):
        self.sharpness = sharpness

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.sharpness is not None:
            result['Sharpness'] = self.sharpness
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Sharpness') is not None:
            self.sharpness = m.get('Sharpness')
        return self


class AssessSharpnessResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: AssessSharpnessResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = AssessSharpnessResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class AssessSharpnessResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AssessSharpnessResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = AssessSharpnessResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ChangeImageSizeRequest(TeaModel):
    def __init__(
        self,
        width: int = None,
        height: int = None,
        url: str = None,
    ):
        self.width = width
        self.height = height
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.width is not None:
            result['Width'] = self.width
        if self.height is not None:
            result['Height'] = self.height
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class ChangeImageSizeResponseBodyData(TeaModel):
    def __init__(
        self,
        url: str = None,
    ):
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class ChangeImageSizeResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: ChangeImageSizeResponseBodyData = None,
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
            temp_model = ChangeImageSizeResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class ChangeImageSizeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ChangeImageSizeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = ChangeImageSizeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSegmentBodyJobRequestDataList(TeaModel):
    def __init__(
        self,
        image_url: str = None,
        data_id: str = None,
    ):
        self.image_url = image_url
        self.data_id = data_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        if self.data_id is not None:
            result['DataId'] = self.data_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        return self


class CreateSegmentBodyJobRequest(TeaModel):
    def __init__(
        self,
        async_: bool = None,
        job_id: str = None,
        time_to_live: int = None,
        data_list: List[CreateSegmentBodyJobRequestDataList] = None,
    ):
        self.async_ = async_
        self.job_id = job_id
        self.time_to_live = time_to_live
        self.data_list = data_list

    def validate(self):
        if self.data_list:
            for k in self.data_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.async_ is not None:
            result['Async'] = self.async_
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.time_to_live is not None:
            result['TimeToLive'] = self.time_to_live
        result['DataList'] = []
        if self.data_list is not None:
            for k in self.data_list:
                result['DataList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Async') is not None:
            self.async_ = m.get('Async')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('TimeToLive') is not None:
            self.time_to_live = m.get('TimeToLive')
        self.data_list = []
        if m.get('DataList') is not None:
            for k in m.get('DataList'):
                temp_model = CreateSegmentBodyJobRequestDataList()
                self.data_list.append(temp_model.from_map(k))
        return self


class CreateSegmentBodyJobResponseBodyDataResultListResultData(TeaModel):
    def __init__(
        self,
        image_url: str = None,
    ):
        self.image_url = image_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        return self


class CreateSegmentBodyJobResponseBodyDataResultList(TeaModel):
    def __init__(
        self,
        result_data: CreateSegmentBodyJobResponseBodyDataResultListResultData = None,
        success: bool = None,
        code: str = None,
        message: str = None,
        data_id: str = None,
    ):
        self.result_data = result_data
        self.success = success
        self.code = code
        self.message = message
        self.data_id = data_id

    def validate(self):
        if self.result_data:
            self.result_data.validate()

    def to_map(self):
        result = dict()
        if self.result_data is not None:
            result['ResultData'] = self.result_data.to_map()
        if self.success is not None:
            result['Success'] = self.success
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.data_id is not None:
            result['DataId'] = self.data_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResultData') is not None:
            temp_model = CreateSegmentBodyJobResponseBodyDataResultListResultData()
            self.result_data = temp_model.from_map(m['ResultData'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        return self


class CreateSegmentBodyJobResponseBodyData(TeaModel):
    def __init__(
        self,
        status: str = None,
        result_list: List[CreateSegmentBodyJobResponseBodyDataResultList] = None,
        batch_size: int = None,
        total_used_time: int = None,
        progress: int = None,
        completed: bool = None,
        job_id: str = None,
    ):
        self.status = status
        self.result_list = result_list
        self.batch_size = batch_size
        self.total_used_time = total_used_time
        self.progress = progress
        self.completed = completed
        self.job_id = job_id

    def validate(self):
        if self.result_list:
            for k in self.result_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        result['ResultList'] = []
        if self.result_list is not None:
            for k in self.result_list:
                result['ResultList'].append(k.to_map() if k else None)
        if self.batch_size is not None:
            result['BatchSize'] = self.batch_size
        if self.total_used_time is not None:
            result['TotalUsedTime'] = self.total_used_time
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.completed is not None:
            result['Completed'] = self.completed
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        self.result_list = []
        if m.get('ResultList') is not None:
            for k in m.get('ResultList'):
                temp_model = CreateSegmentBodyJobResponseBodyDataResultList()
                self.result_list.append(temp_model.from_map(k))
        if m.get('BatchSize') is not None:
            self.batch_size = m.get('BatchSize')
        if m.get('TotalUsedTime') is not None:
            self.total_used_time = m.get('TotalUsedTime')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('Completed') is not None:
            self.completed = m.get('Completed')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class CreateSegmentBodyJobResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: CreateSegmentBodyJobResponseBodyData = None,
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
            temp_model = CreateSegmentBodyJobResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class CreateSegmentBodyJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateSegmentBodyJobResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = CreateSegmentBodyJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetectImageElementsRequest(TeaModel):
    def __init__(
        self,
        url: str = None,
    ):
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class DetectImageElementsResponseBodyDataElements(TeaModel):
    def __init__(
        self,
        type: str = None,
        width: int = None,
        height: int = None,
        y: int = None,
        score: float = None,
        x: int = None,
    ):
        self.type = type
        self.width = width
        self.height = height
        self.y = y
        self.score = score
        self.x = x

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.width is not None:
            result['Width'] = self.width
        if self.height is not None:
            result['Height'] = self.height
        if self.y is not None:
            result['Y'] = self.y
        if self.score is not None:
            result['Score'] = self.score
        if self.x is not None:
            result['X'] = self.x
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('X') is not None:
            self.x = m.get('X')
        return self


class DetectImageElementsResponseBodyData(TeaModel):
    def __init__(
        self,
        elements: List[DetectImageElementsResponseBodyDataElements] = None,
    ):
        self.elements = elements

    def validate(self):
        if self.elements:
            for k in self.elements:
                if k:
                    k.validate()

    def to_map(self):
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
                temp_model = DetectImageElementsResponseBodyDataElements()
                self.elements.append(temp_model.from_map(k))
        return self


class DetectImageElementsResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: DetectImageElementsResponseBodyData = None,
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
            temp_model = DetectImageElementsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class DetectImageElementsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DetectImageElementsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = DetectImageElementsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetectMainBodyRequest(TeaModel):
    def __init__(
        self,
        image_url: str = None,
    ):
        self.image_url = image_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        return self


class DetectMainBodyResponseBodyDataLocation(TeaModel):
    def __init__(
        self,
        width: int = None,
        height: int = None,
        y: int = None,
        x: int = None,
    ):
        self.width = width
        self.height = height
        self.y = y
        self.x = x

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.width is not None:
            result['Width'] = self.width
        if self.height is not None:
            result['Height'] = self.height
        if self.y is not None:
            result['Y'] = self.y
        if self.x is not None:
            result['X'] = self.x
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        if m.get('X') is not None:
            self.x = m.get('X')
        return self


class DetectMainBodyResponseBodyData(TeaModel):
    def __init__(
        self,
        location: DetectMainBodyResponseBodyDataLocation = None,
    ):
        self.location = location

    def validate(self):
        if self.location:
            self.location.validate()

    def to_map(self):
        result = dict()
        if self.location is not None:
            result['Location'] = self.location.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Location') is not None:
            temp_model = DetectMainBodyResponseBodyDataLocation()
            self.location = temp_model.from_map(m['Location'])
        return self


class DetectMainBodyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: DetectMainBodyResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = DetectMainBodyResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class DetectMainBodyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DetectMainBodyResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = DetectMainBodyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnhanceFaceRequest(TeaModel):
    def __init__(
        self,
        image_url: str = None,
    ):
        self.image_url = image_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        return self


class EnhanceFaceResponseBodyData(TeaModel):
    def __init__(
        self,
        image_url: str = None,
    ):
        self.image_url = image_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        return self


class EnhanceFaceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: EnhanceFaceResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = EnhanceFaceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class EnhanceFaceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: EnhanceFaceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = EnhanceFaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EraseLogoInVideoRequestBoxes(TeaModel):
    def __init__(
        self,
        w: float = None,
        h: float = None,
        y: float = None,
        x: float = None,
    ):
        self.w = w
        self.h = h
        self.y = y
        self.x = x

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.w is not None:
            result['W'] = self.w
        if self.h is not None:
            result['H'] = self.h
        if self.y is not None:
            result['Y'] = self.y
        if self.x is not None:
            result['X'] = self.x
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('W') is not None:
            self.w = m.get('W')
        if m.get('H') is not None:
            self.h = m.get('H')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        if m.get('X') is not None:
            self.x = m.get('X')
        return self


class EraseLogoInVideoRequest(TeaModel):
    def __init__(
        self,
        video_url: str = None,
        async_: bool = None,
        job_id: str = None,
        boxes: List[EraseLogoInVideoRequestBoxes] = None,
    ):
        self.video_url = video_url
        self.async_ = async_
        self.job_id = job_id
        self.boxes = boxes

    def validate(self):
        if self.boxes:
            for k in self.boxes:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.video_url is not None:
            result['VideoUrl'] = self.video_url
        if self.async_ is not None:
            result['Async'] = self.async_
        if self.job_id is not None:
            result['JobId'] = self.job_id
        result['Boxes'] = []
        if self.boxes is not None:
            for k in self.boxes:
                result['Boxes'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VideoUrl') is not None:
            self.video_url = m.get('VideoUrl')
        if m.get('Async') is not None:
            self.async_ = m.get('Async')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        self.boxes = []
        if m.get('Boxes') is not None:
            for k in m.get('Boxes'):
                temp_model = EraseLogoInVideoRequestBoxes()
                self.boxes.append(temp_model.from_map(k))
        return self


class EraseLogoInVideoResponseBodyData(TeaModel):
    def __init__(
        self,
        job_id: str = None,
        video_url: str = None,
    ):
        self.job_id = job_id
        self.video_url = video_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.video_url is not None:
            result['VideoUrl'] = self.video_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('VideoUrl') is not None:
            self.video_url = m.get('VideoUrl')
        return self


class EraseLogoInVideoResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: EraseLogoInVideoResponseBodyData = None,
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
            temp_model = EraseLogoInVideoResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class EraseLogoInVideoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: EraseLogoInVideoResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = EraseLogoInVideoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExtendImageStyleRequest(TeaModel):
    def __init__(
        self,
        style_url: str = None,
        major_url: str = None,
    ):
        self.style_url = style_url
        self.major_url = major_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.style_url is not None:
            result['StyleUrl'] = self.style_url
        if self.major_url is not None:
            result['MajorUrl'] = self.major_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StyleUrl') is not None:
            self.style_url = m.get('StyleUrl')
        if m.get('MajorUrl') is not None:
            self.major_url = m.get('MajorUrl')
        return self


class ExtendImageStyleResponseBodyData(TeaModel):
    def __init__(
        self,
        url: str = None,
        major_url: str = None,
    ):
        self.url = url
        self.major_url = major_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.url is not None:
            result['Url'] = self.url
        if self.major_url is not None:
            result['MajorUrl'] = self.major_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('MajorUrl') is not None:
            self.major_url = m.get('MajorUrl')
        return self


class ExtendImageStyleResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: ExtendImageStyleResponseBodyData = None,
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
            temp_model = ExtendImageStyleResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class ExtendImageStyleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ExtendImageStyleResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = ExtendImageStyleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAsyncJobResultRequest(TeaModel):
    def __init__(
        self,
        async_: bool = None,
        job_id: str = None,
    ):
        self.async_ = async_
        self.job_id = job_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.async_ is not None:
            result['Async'] = self.async_
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Async') is not None:
            self.async_ = m.get('Async')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class GetAsyncJobResultResponseBodyData(TeaModel):
    def __init__(
        self,
        status: str = None,
        error_message: str = None,
        result: str = None,
        error_code: str = None,
        job_id: str = None,
    ):
        self.status = status
        self.error_message = error_message
        self.result = result
        self.error_code = error_code
        self.job_id = job_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.result is not None:
            result['Result'] = self.result
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class GetAsyncJobResultResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: GetAsyncJobResultResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = GetAsyncJobResultResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class GetAsyncJobResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetAsyncJobResultResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = GetAsyncJobResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAsyncResultRequest(TeaModel):
    def __init__(
        self,
        job_id: str = None,
    ):
        self.job_id = job_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class GetAsyncResultResponseBodyData(TeaModel):
    def __init__(
        self,
        status: str = None,
        total_used_time: int = None,
        progress: float = None,
        batch_size: str = None,
        result: Dict[str, Any] = None,
        completed: bool = None,
        code: str = None,
        finish: bool = None,
        message: str = None,
    ):
        self.status = status
        self.total_used_time = total_used_time
        self.progress = progress
        self.batch_size = batch_size
        self.result = result
        self.completed = completed
        self.code = code
        self.finish = finish
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.total_used_time is not None:
            result['TotalUsedTime'] = self.total_used_time
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.batch_size is not None:
            result['BatchSize'] = self.batch_size
        if self.result is not None:
            result['Result'] = self.result
        if self.completed is not None:
            result['Completed'] = self.completed
        if self.code is not None:
            result['Code'] = self.code
        if self.finish is not None:
            result['Finish'] = self.finish
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TotalUsedTime') is not None:
            self.total_used_time = m.get('TotalUsedTime')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('BatchSize') is not None:
            self.batch_size = m.get('BatchSize')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Completed') is not None:
            self.completed = m.get('Completed')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Finish') is not None:
            self.finish = m.get('Finish')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class GetAsyncResultResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: GetAsyncResultResponseBodyData = None,
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
            temp_model = GetAsyncResultResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class GetAsyncResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetAsyncResultResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = GetAsyncResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetJobResultRequest(TeaModel):
    def __init__(
        self,
        job_id: str = None,
    ):
        self.job_id = job_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class GetJobResultResponseBodyData(TeaModel):
    def __init__(
        self,
        status: str = None,
        result_list: List[Dict[str, Any]] = None,
        total_used_time: int = None,
        batch_size: str = None,
        progress: float = None,
        completed: bool = None,
        finish: bool = None,
        message: str = None,
    ):
        self.status = status
        self.result_list = result_list
        self.total_used_time = total_used_time
        self.batch_size = batch_size
        self.progress = progress
        self.completed = completed
        self.finish = finish
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.result_list is not None:
            result['ResultList'] = self.result_list
        if self.total_used_time is not None:
            result['TotalUsedTime'] = self.total_used_time
        if self.batch_size is not None:
            result['BatchSize'] = self.batch_size
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.completed is not None:
            result['Completed'] = self.completed
        if self.finish is not None:
            result['Finish'] = self.finish
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ResultList') is not None:
            self.result_list = m.get('ResultList')
        if m.get('TotalUsedTime') is not None:
            self.total_used_time = m.get('TotalUsedTime')
        if m.get('BatchSize') is not None:
            self.batch_size = m.get('BatchSize')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('Completed') is not None:
            self.completed = m.get('Completed')
        if m.get('Finish') is not None:
            self.finish = m.get('Finish')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class GetJobResultResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: GetJobResultResponseBodyData = None,
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
            temp_model = GetJobResultResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class GetJobResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetJobResultResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = GetJobResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetJobStatusRequest(TeaModel):
    def __init__(
        self,
        job_id: str = None,
    ):
        self.job_id = job_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class GetJobStatusResponseBodyData(TeaModel):
    def __init__(
        self,
        status: str = None,
        total_used_time: int = None,
        batch_size: str = None,
        progress: float = None,
        time_to_live: int = None,
        completed: bool = None,
        finish: bool = None,
        message: str = None,
    ):
        self.status = status
        self.total_used_time = total_used_time
        self.batch_size = batch_size
        self.progress = progress
        self.time_to_live = time_to_live
        self.completed = completed
        self.finish = finish
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.total_used_time is not None:
            result['TotalUsedTime'] = self.total_used_time
        if self.batch_size is not None:
            result['BatchSize'] = self.batch_size
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.time_to_live is not None:
            result['TimeToLive'] = self.time_to_live
        if self.completed is not None:
            result['Completed'] = self.completed
        if self.finish is not None:
            result['Finish'] = self.finish
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TotalUsedTime') is not None:
            self.total_used_time = m.get('TotalUsedTime')
        if m.get('BatchSize') is not None:
            self.batch_size = m.get('BatchSize')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('TimeToLive') is not None:
            self.time_to_live = m.get('TimeToLive')
        if m.get('Completed') is not None:
            self.completed = m.get('Completed')
        if m.get('Finish') is not None:
            self.finish = m.get('Finish')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class GetJobStatusResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: GetJobStatusResponseBodyData = None,
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
            temp_model = GetJobStatusResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class GetJobStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetJobStatusResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = GetJobStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRenderResultRequest(TeaModel):
    def __init__(
        self,
        job_id: str = None,
    ):
        self.job_id = job_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class GetRenderResultResponseBodyDataResultData(TeaModel):
    def __init__(
        self,
        image_url: str = None,
    ):
        self.image_url = image_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        return self


class GetRenderResultResponseBodyData(TeaModel):
    def __init__(
        self,
        result_data: GetRenderResultResponseBodyDataResultData = None,
        progress: float = None,
        completed: bool = None,
        code: str = None,
        message: str = None,
    ):
        self.result_data = result_data
        self.progress = progress
        self.completed = completed
        self.code = code
        self.message = message

    def validate(self):
        if self.result_data:
            self.result_data.validate()

    def to_map(self):
        result = dict()
        if self.result_data is not None:
            result['ResultData'] = self.result_data.to_map()
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.completed is not None:
            result['Completed'] = self.completed
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResultData') is not None:
            temp_model = GetRenderResultResponseBodyDataResultData()
            self.result_data = temp_model.from_map(m['ResultData'])
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('Completed') is not None:
            self.completed = m.get('Completed')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class GetRenderResultResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: GetRenderResultResponseBodyData = None,
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
            temp_model = GetRenderResultResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class GetRenderResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetRenderResultResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = GetRenderResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUserBucketConfigResponseBodyData(TeaModel):
    def __init__(
        self,
        region_name: str = None,
        region: str = None,
        bucket: str = None,
    ):
        self.region_name = region_name
        self.region = region
        self.bucket = bucket

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_name is not None:
            result['RegionName'] = self.region_name
        if self.region is not None:
            result['Region'] = self.region
        if self.bucket is not None:
            result['Bucket'] = self.bucket
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionName') is not None:
            self.region_name = m.get('RegionName')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')
        return self


class GetUserBucketConfigResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: List[GetUserBucketConfigResponseBodyData] = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetUserBucketConfigResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class GetUserBucketConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetUserBucketConfigResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = GetUserBucketConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class HighlightGameVideoRequest(TeaModel):
    def __init__(
        self,
        video_url: str = None,
        async_: bool = None,
    ):
        self.video_url = video_url
        self.async_ = async_

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.video_url is not None:
            result['VideoUrl'] = self.video_url
        if self.async_ is not None:
            result['Async'] = self.async_
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VideoUrl') is not None:
            self.video_url = m.get('VideoUrl')
        if m.get('Async') is not None:
            self.async_ = m.get('Async')
        return self


class HighlightGameVideoAdvanceRequest(TeaModel):
    def __init__(
        self,
        video_url_object: BinaryIO = None,
        async_: bool = None,
    ):
        self.video_url_object = video_url_object
        self.async_ = async_

    def validate(self):
        self.validate_required(self.video_url_object, 'video_url_object')

    def to_map(self):
        result = dict()
        if self.video_url_object is not None:
            result['VideoUrlObject'] = self.video_url_object
        if self.async_ is not None:
            result['Async'] = self.async_
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VideoUrlObject') is not None:
            self.video_url_object = m.get('VideoUrlObject')
        if m.get('Async') is not None:
            self.async_ = m.get('Async')
        return self


class HighlightGameVideoResponseBodyDataHighlightList(TeaModel):
    def __init__(
        self,
        start: float = None,
        end: float = None,
    ):
        self.start = start
        self.end = end

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.start is not None:
            result['Start'] = self.start
        if self.end is not None:
            result['End'] = self.end
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Start') is not None:
            self.start = m.get('Start')
        if m.get('End') is not None:
            self.end = m.get('End')
        return self


class HighlightGameVideoResponseBodyDataGameList(TeaModel):
    def __init__(
        self,
        game_info: Dict[str, Any] = None,
        start: float = None,
        end: float = None,
        id: str = None,
    ):
        self.game_info = game_info
        self.start = start
        self.end = end
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.game_info is not None:
            result['GameInfo'] = self.game_info
        if self.start is not None:
            result['Start'] = self.start
        if self.end is not None:
            result['End'] = self.end
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GameInfo') is not None:
            self.game_info = m.get('GameInfo')
        if m.get('Start') is not None:
            self.start = m.get('Start')
        if m.get('End') is not None:
            self.end = m.get('End')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class HighlightGameVideoResponseBodyData(TeaModel):
    def __init__(
        self,
        highlight_list: List[HighlightGameVideoResponseBodyDataHighlightList] = None,
        game_list: List[HighlightGameVideoResponseBodyDataGameList] = None,
    ):
        self.highlight_list = highlight_list
        self.game_list = game_list

    def validate(self):
        if self.highlight_list:
            for k in self.highlight_list:
                if k:
                    k.validate()
        if self.game_list:
            for k in self.game_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['HighlightList'] = []
        if self.highlight_list is not None:
            for k in self.highlight_list:
                result['HighlightList'].append(k.to_map() if k else None)
        result['GameList'] = []
        if self.game_list is not None:
            for k in self.game_list:
                result['GameList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.highlight_list = []
        if m.get('HighlightList') is not None:
            for k in m.get('HighlightList'):
                temp_model = HighlightGameVideoResponseBodyDataHighlightList()
                self.highlight_list.append(temp_model.from_map(k))
        self.game_list = []
        if m.get('GameList') is not None:
            for k in m.get('GameList'):
                temp_model = HighlightGameVideoResponseBodyDataGameList()
                self.game_list.append(temp_model.from_map(k))
        return self


class HighlightGameVideoResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: HighlightGameVideoResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = HighlightGameVideoResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class HighlightGameVideoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: HighlightGameVideoResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = HighlightGameVideoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class IntelligentCompositionRequest(TeaModel):
    def __init__(
        self,
        num_boxes: int = None,
        image_url: str = None,
    ):
        self.num_boxes = num_boxes
        self.image_url = image_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.num_boxes is not None:
            result['NumBoxes'] = self.num_boxes
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NumBoxes') is not None:
            self.num_boxes = m.get('NumBoxes')
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        return self


class IntelligentCompositionResponseBodyDataElements(TeaModel):
    def __init__(
        self,
        min_x: int = None,
        score: float = None,
        max_y: int = None,
        max_x: int = None,
        min_y: int = None,
    ):
        self.min_x = min_x
        self.score = score
        self.max_y = max_y
        self.max_x = max_x
        self.min_y = min_y

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.min_x is not None:
            result['MinX'] = self.min_x
        if self.score is not None:
            result['Score'] = self.score
        if self.max_y is not None:
            result['MaxY'] = self.max_y
        if self.max_x is not None:
            result['MaxX'] = self.max_x
        if self.min_y is not None:
            result['MinY'] = self.min_y
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MinX') is not None:
            self.min_x = m.get('MinX')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('MaxY') is not None:
            self.max_y = m.get('MaxY')
        if m.get('MaxX') is not None:
            self.max_x = m.get('MaxX')
        if m.get('MinY') is not None:
            self.min_y = m.get('MinY')
        return self


class IntelligentCompositionResponseBodyData(TeaModel):
    def __init__(
        self,
        elements: List[IntelligentCompositionResponseBodyDataElements] = None,
    ):
        self.elements = elements

    def validate(self):
        if self.elements:
            for k in self.elements:
                if k:
                    k.validate()

    def to_map(self):
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
                temp_model = IntelligentCompositionResponseBodyDataElements()
                self.elements.append(temp_model.from_map(k))
        return self


class IntelligentCompositionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: IntelligentCompositionResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = IntelligentCompositionResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class IntelligentCompositionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: IntelligentCompositionResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = IntelligentCompositionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPackageDesignModelTypesResponseBodyDataModelTypeListElements(TeaModel):
    def __init__(
        self,
        side_name: str = None,
    ):
        self.side_name = side_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.side_name is not None:
            result['SideName'] = self.side_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SideName') is not None:
            self.side_name = m.get('SideName')
        return self


class ListPackageDesignModelTypesResponseBodyDataModelTypeList(TeaModel):
    def __init__(
        self,
        elements: List[ListPackageDesignModelTypesResponseBodyDataModelTypeListElements] = None,
        model_type: str = None,
    ):
        self.elements = elements
        self.model_type = model_type

    def validate(self):
        if self.elements:
            for k in self.elements:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Elements'] = []
        if self.elements is not None:
            for k in self.elements:
                result['Elements'].append(k.to_map() if k else None)
        if self.model_type is not None:
            result['ModelType'] = self.model_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.elements = []
        if m.get('Elements') is not None:
            for k in m.get('Elements'):
                temp_model = ListPackageDesignModelTypesResponseBodyDataModelTypeListElements()
                self.elements.append(temp_model.from_map(k))
        if m.get('ModelType') is not None:
            self.model_type = m.get('ModelType')
        return self


class ListPackageDesignModelTypesResponseBodyData(TeaModel):
    def __init__(
        self,
        model_type_list: List[ListPackageDesignModelTypesResponseBodyDataModelTypeList] = None,
    ):
        self.model_type_list = model_type_list

    def validate(self):
        if self.model_type_list:
            for k in self.model_type_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['ModelTypeList'] = []
        if self.model_type_list is not None:
            for k in self.model_type_list:
                result['ModelTypeList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.model_type_list = []
        if m.get('ModelTypeList') is not None:
            for k in m.get('ModelTypeList'):
                temp_model = ListPackageDesignModelTypesResponseBodyDataModelTypeList()
                self.model_type_list.append(temp_model.from_map(k))
        return self


class ListPackageDesignModelTypesResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: ListPackageDesignModelTypesResponseBodyData = None,
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
            temp_model = ListPackageDesignModelTypesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class ListPackageDesignModelTypesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListPackageDesignModelTypesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = ListPackageDesignModelTypesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUserBucketsRequestData(TeaModel):
    def __init__(
        self,
        region_id: str = None,
    ):
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListUserBucketsRequest(TeaModel):
    def __init__(
        self,
        data: List[ListUserBucketsRequestData] = None,
    ):
        self.data = data

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListUserBucketsRequestData()
                self.data.append(temp_model.from_map(k))
        return self


class ListUserBucketsResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: List[str] = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
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
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class ListUserBucketsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListUserBucketsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = ListUserBucketsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class MakeSuperResolutionImageRequest(TeaModel):
    def __init__(
        self,
        url: str = None,
    ):
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class MakeSuperResolutionImageResponseBodyData(TeaModel):
    def __init__(
        self,
        url: str = None,
    ):
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class MakeSuperResolutionImageResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: MakeSuperResolutionImageResponseBodyData = None,
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
            temp_model = MakeSuperResolutionImageResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class MakeSuperResolutionImageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: MakeSuperResolutionImageResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = MakeSuperResolutionImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ParseFaceRequest(TeaModel):
    def __init__(
        self,
        image_url: str = None,
    ):
        self.image_url = image_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        return self


class ParseFaceResponseBodyDataElements(TeaModel):
    def __init__(
        self,
        image_url: str = None,
        name: str = None,
    ):
        self.image_url = image_url
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class ParseFaceResponseBodyData(TeaModel):
    def __init__(
        self,
        elements: List[ParseFaceResponseBodyDataElements] = None,
        origin_image_url: str = None,
    ):
        self.elements = elements
        self.origin_image_url = origin_image_url

    def validate(self):
        if self.elements:
            for k in self.elements:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Elements'] = []
        if self.elements is not None:
            for k in self.elements:
                result['Elements'].append(k.to_map() if k else None)
        if self.origin_image_url is not None:
            result['OriginImageURL'] = self.origin_image_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.elements = []
        if m.get('Elements') is not None:
            for k in m.get('Elements'):
                temp_model = ParseFaceResponseBodyDataElements()
                self.elements.append(temp_model.from_map(k))
        if m.get('OriginImageURL') is not None:
            self.origin_image_url = m.get('OriginImageURL')
        return self


class ParseFaceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: ParseFaceResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = ParseFaceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class ParseFaceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ParseFaceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = ParseFaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PreviewModelForPackageDesignRequestElementList(TeaModel):
    def __init__(
        self,
        image_url: str = None,
        side_name: str = None,
    ):
        self.image_url = image_url
        self.side_name = side_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        if self.side_name is not None:
            result['SideName'] = self.side_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        if m.get('SideName') is not None:
            self.side_name = m.get('SideName')
        return self


class PreviewModelForPackageDesignRequest(TeaModel):
    def __init__(
        self,
        data_id: str = None,
        model_type: str = None,
        material_type: str = None,
        material_name: str = None,
        category: str = None,
        element_list: List[PreviewModelForPackageDesignRequestElementList] = None,
    ):
        self.data_id = data_id
        self.model_type = model_type
        self.material_type = material_type
        self.material_name = material_name
        self.category = category
        self.element_list = element_list

    def validate(self):
        if self.element_list:
            for k in self.element_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.model_type is not None:
            result['ModelType'] = self.model_type
        if self.material_type is not None:
            result['MaterialType'] = self.material_type
        if self.material_name is not None:
            result['MaterialName'] = self.material_name
        if self.category is not None:
            result['Category'] = self.category
        result['ElementList'] = []
        if self.element_list is not None:
            for k in self.element_list:
                result['ElementList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('ModelType') is not None:
            self.model_type = m.get('ModelType')
        if m.get('MaterialType') is not None:
            self.material_type = m.get('MaterialType')
        if m.get('MaterialName') is not None:
            self.material_name = m.get('MaterialName')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        self.element_list = []
        if m.get('ElementList') is not None:
            for k in m.get('ElementList'):
                temp_model = PreviewModelForPackageDesignRequestElementList()
                self.element_list.append(temp_model.from_map(k))
        return self


class PreviewModelForPackageDesignResponseBodyData(TeaModel):
    def __init__(
        self,
        preview_url: str = None,
    ):
        self.preview_url = preview_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.preview_url is not None:
            result['PreviewUrl'] = self.preview_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PreviewUrl') is not None:
            self.preview_url = m.get('PreviewUrl')
        return self


class PreviewModelForPackageDesignResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: PreviewModelForPackageDesignResponseBodyData = None,
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
            temp_model = PreviewModelForPackageDesignResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class PreviewModelForPackageDesignResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: PreviewModelForPackageDesignResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = PreviewModelForPackageDesignResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeImageColorRequest(TeaModel):
    def __init__(
        self,
        url: str = None,
        color_count: str = None,
    ):
        self.url = url
        self.color_count = color_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.url is not None:
            result['Url'] = self.url
        if self.color_count is not None:
            result['ColorCount'] = self.color_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('ColorCount') is not None:
            self.color_count = m.get('ColorCount')
        return self


class RecognizeImageColorResponseBodyDataColorTemplateList(TeaModel):
    def __init__(
        self,
        color: str = None,
        percentage: float = None,
        label: str = None,
    ):
        self.color = color
        self.percentage = percentage
        self.label = label

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.color is not None:
            result['Color'] = self.color
        if self.percentage is not None:
            result['Percentage'] = self.percentage
        if self.label is not None:
            result['Label'] = self.label
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Color') is not None:
            self.color = m.get('Color')
        if m.get('Percentage') is not None:
            self.percentage = m.get('Percentage')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        return self


class RecognizeImageColorResponseBodyData(TeaModel):
    def __init__(
        self,
        color_template_list: List[RecognizeImageColorResponseBodyDataColorTemplateList] = None,
    ):
        self.color_template_list = color_template_list

    def validate(self):
        if self.color_template_list:
            for k in self.color_template_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['ColorTemplateList'] = []
        if self.color_template_list is not None:
            for k in self.color_template_list:
                result['ColorTemplateList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.color_template_list = []
        if m.get('ColorTemplateList') is not None:
            for k in m.get('ColorTemplateList'):
                temp_model = RecognizeImageColorResponseBodyDataColorTemplateList()
                self.color_template_list.append(temp_model.from_map(k))
        return self


class RecognizeImageColorResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: RecognizeImageColorResponseBodyData = None,
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
            temp_model = RecognizeImageColorResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class RecognizeImageColorResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RecognizeImageColorResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = RecognizeImageColorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeImageStyleRequest(TeaModel):
    def __init__(
        self,
        url: str = None,
    ):
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class RecognizeImageStyleResponseBodyData(TeaModel):
    def __init__(
        self,
        styles: List[str] = None,
    ):
        self.styles = styles

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.styles is not None:
            result['Styles'] = self.styles
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Styles') is not None:
            self.styles = m.get('Styles')
        return self


class RecognizeImageStyleResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: RecognizeImageStyleResponseBodyData = None,
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
            temp_model = RecognizeImageStyleResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class RecognizeImageStyleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RecognizeImageStyleResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = RecognizeImageStyleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecolorImageRequestColorTemplate(TeaModel):
    def __init__(
        self,
        color: str = None,
    ):
        self.color = color

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.color is not None:
            result['Color'] = self.color
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Color') is not None:
            self.color = m.get('Color')
        return self


class RecolorImageRequest(TeaModel):
    def __init__(
        self,
        url: str = None,
        mode: str = None,
        ref_url: str = None,
        color_count: int = None,
        color_template: List[RecolorImageRequestColorTemplate] = None,
    ):
        self.url = url
        self.mode = mode
        self.ref_url = ref_url
        self.color_count = color_count
        self.color_template = color_template

    def validate(self):
        if self.color_template:
            for k in self.color_template:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.url is not None:
            result['Url'] = self.url
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.ref_url is not None:
            result['RefUrl'] = self.ref_url
        if self.color_count is not None:
            result['ColorCount'] = self.color_count
        result['ColorTemplate'] = []
        if self.color_template is not None:
            for k in self.color_template:
                result['ColorTemplate'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('RefUrl') is not None:
            self.ref_url = m.get('RefUrl')
        if m.get('ColorCount') is not None:
            self.color_count = m.get('ColorCount')
        self.color_template = []
        if m.get('ColorTemplate') is not None:
            for k in m.get('ColorTemplate'):
                temp_model = RecolorImageRequestColorTemplate()
                self.color_template.append(temp_model.from_map(k))
        return self


class RecolorImageResponseBodyData(TeaModel):
    def __init__(
        self,
        image_list: List[str] = None,
    ):
        self.image_list = image_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.image_list is not None:
            result['ImageList'] = self.image_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageList') is not None:
            self.image_list = m.get('ImageList')
        return self


class RecolorImageResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: RecolorImageResponseBodyData = None,
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
            temp_model = RecolorImageResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class RecolorImageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RecolorImageResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = RecolorImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RenderImageForPackageDesignRequestElementList(TeaModel):
    def __init__(
        self,
        image_url: str = None,
        side_name: str = None,
    ):
        self.image_url = image_url
        self.side_name = side_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        if self.side_name is not None:
            result['SideName'] = self.side_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        if m.get('SideName') is not None:
            self.side_name = m.get('SideName')
        return self


class RenderImageForPackageDesignRequest(TeaModel):
    def __init__(
        self,
        job_id: str = None,
        model_type: str = None,
        material_type: str = None,
        material_name: str = None,
        category: str = None,
        target_width: int = None,
        target_height: int = None,
        display_type: str = None,
        element_list: List[RenderImageForPackageDesignRequestElementList] = None,
    ):
        self.job_id = job_id
        self.model_type = model_type
        self.material_type = material_type
        self.material_name = material_name
        self.category = category
        self.target_width = target_width
        self.target_height = target_height
        self.display_type = display_type
        self.element_list = element_list

    def validate(self):
        if self.element_list:
            for k in self.element_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.model_type is not None:
            result['ModelType'] = self.model_type
        if self.material_type is not None:
            result['MaterialType'] = self.material_type
        if self.material_name is not None:
            result['MaterialName'] = self.material_name
        if self.category is not None:
            result['Category'] = self.category
        if self.target_width is not None:
            result['TargetWidth'] = self.target_width
        if self.target_height is not None:
            result['TargetHeight'] = self.target_height
        if self.display_type is not None:
            result['DisplayType'] = self.display_type
        result['ElementList'] = []
        if self.element_list is not None:
            for k in self.element_list:
                result['ElementList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('ModelType') is not None:
            self.model_type = m.get('ModelType')
        if m.get('MaterialType') is not None:
            self.material_type = m.get('MaterialType')
        if m.get('MaterialName') is not None:
            self.material_name = m.get('MaterialName')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('TargetWidth') is not None:
            self.target_width = m.get('TargetWidth')
        if m.get('TargetHeight') is not None:
            self.target_height = m.get('TargetHeight')
        if m.get('DisplayType') is not None:
            self.display_type = m.get('DisplayType')
        self.element_list = []
        if m.get('ElementList') is not None:
            for k in m.get('ElementList'):
                temp_model = RenderImageForPackageDesignRequestElementList()
                self.element_list.append(temp_model.from_map(k))
        return self


class RenderImageForPackageDesignResponseBodyData(TeaModel):
    def __init__(
        self,
        job_id: str = None,
    ):
        self.job_id = job_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class RenderImageForPackageDesignResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: RenderImageForPackageDesignResponseBodyData = None,
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
            temp_model = RenderImageForPackageDesignResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class RenderImageForPackageDesignResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RenderImageForPackageDesignResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = RenderImageForPackageDesignResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SegmentAnimalRequest(TeaModel):
    def __init__(
        self,
        image_url: str = None,
    ):
        self.image_url = image_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        return self


class SegmentAnimalResponseBodyData(TeaModel):
    def __init__(
        self,
        image_url: str = None,
    ):
        self.image_url = image_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        return self


class SegmentAnimalResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: SegmentAnimalResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = SegmentAnimalResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class SegmentAnimalResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SegmentAnimalResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = SegmentAnimalResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SegmentBodyRequest(TeaModel):
    def __init__(
        self,
        image_url: str = None,
    ):
        self.image_url = image_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        return self


class SegmentBodyResponseBodyData(TeaModel):
    def __init__(
        self,
        image_url: str = None,
    ):
        self.image_url = image_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        return self


class SegmentBodyResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: SegmentBodyResponseBodyData = None,
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
            temp_model = SegmentBodyResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class SegmentBodyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SegmentBodyResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = SegmentBodyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SegmentClothRequest(TeaModel):
    def __init__(
        self,
        image_url: str = None,
    ):
        self.image_url = image_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        return self


class SegmentClothResponseBodyDataElements(TeaModel):
    def __init__(
        self,
        image_url: str = None,
    ):
        self.image_url = image_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        return self


class SegmentClothResponseBodyData(TeaModel):
    def __init__(
        self,
        elements: List[SegmentClothResponseBodyDataElements] = None,
    ):
        self.elements = elements

    def validate(self):
        if self.elements:
            for k in self.elements:
                if k:
                    k.validate()

    def to_map(self):
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
                temp_model = SegmentClothResponseBodyDataElements()
                self.elements.append(temp_model.from_map(k))
        return self


class SegmentClothResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: SegmentClothResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = SegmentClothResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class SegmentClothResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SegmentClothResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = SegmentClothResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SegmentCommodityRequest(TeaModel):
    def __init__(
        self,
        image_url: str = None,
    ):
        self.image_url = image_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        return self


class SegmentCommodityResponseBodyData(TeaModel):
    def __init__(
        self,
        image_url: str = None,
    ):
        self.image_url = image_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        return self


class SegmentCommodityResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: SegmentCommodityResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = SegmentCommodityResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class SegmentCommodityResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SegmentCommodityResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = SegmentCommodityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SegmentHairRequest(TeaModel):
    def __init__(
        self,
        image_url: str = None,
    ):
        self.image_url = image_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        return self


class SegmentHairResponseBodyDataElements(TeaModel):
    def __init__(
        self,
        image_url: str = None,
        width: int = None,
        height: int = None,
        y: int = None,
        x: int = None,
    ):
        self.image_url = image_url
        self.width = width
        self.height = height
        self.y = y
        self.x = x

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        if self.width is not None:
            result['Width'] = self.width
        if self.height is not None:
            result['Height'] = self.height
        if self.y is not None:
            result['Y'] = self.y
        if self.x is not None:
            result['X'] = self.x
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        if m.get('X') is not None:
            self.x = m.get('X')
        return self


class SegmentHairResponseBodyData(TeaModel):
    def __init__(
        self,
        elements: List[SegmentHairResponseBodyDataElements] = None,
    ):
        self.elements = elements

    def validate(self):
        if self.elements:
            for k in self.elements:
                if k:
                    k.validate()

    def to_map(self):
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
                temp_model = SegmentHairResponseBodyDataElements()
                self.elements.append(temp_model.from_map(k))
        return self


class SegmentHairResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: SegmentHairResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = SegmentHairResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class SegmentHairResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SegmentHairResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = SegmentHairResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SegmentHeadRequest(TeaModel):
    def __init__(
        self,
        image_url: str = None,
    ):
        self.image_url = image_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        return self


class SegmentHeadResponseBodyDataElements(TeaModel):
    def __init__(
        self,
        image_url: str = None,
        width: int = None,
        height: int = None,
        y: int = None,
        x: int = None,
    ):
        self.image_url = image_url
        self.width = width
        self.height = height
        self.y = y
        self.x = x

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        if self.width is not None:
            result['Width'] = self.width
        if self.height is not None:
            result['Height'] = self.height
        if self.y is not None:
            result['Y'] = self.y
        if self.x is not None:
            result['X'] = self.x
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        if m.get('X') is not None:
            self.x = m.get('X')
        return self


class SegmentHeadResponseBodyData(TeaModel):
    def __init__(
        self,
        elements: List[SegmentHeadResponseBodyDataElements] = None,
    ):
        self.elements = elements

    def validate(self):
        if self.elements:
            for k in self.elements:
                if k:
                    k.validate()

    def to_map(self):
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
                temp_model = SegmentHeadResponseBodyDataElements()
                self.elements.append(temp_model.from_map(k))
        return self


class SegmentHeadResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: SegmentHeadResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = SegmentHeadResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class SegmentHeadResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SegmentHeadResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = SegmentHeadResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SegmentImageRequest(TeaModel):
    def __init__(
        self,
        url: str = None,
    ):
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class SegmentImageResponseBodyData(TeaModel):
    def __init__(
        self,
        url: str = None,
    ):
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class SegmentImageResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: SegmentImageResponseBodyData = None,
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
            temp_model = SegmentImageResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class SegmentImageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SegmentImageResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = SegmentImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SegmentSkyRequest(TeaModel):
    def __init__(
        self,
        image_url: str = None,
    ):
        self.image_url = image_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        return self


class SegmentSkyResponseBodyData(TeaModel):
    def __init__(
        self,
        image_url: str = None,
    ):
        self.image_url = image_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        return self


class SegmentSkyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: SegmentSkyResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = SegmentSkyResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class SegmentSkyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SegmentSkyResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = SegmentSkyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SegmentVehicleRequest(TeaModel):
    def __init__(
        self,
        image_url: str = None,
    ):
        self.image_url = image_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        return self


class SegmentVehicleResponseBodyDataElements(TeaModel):
    def __init__(
        self,
        image_url: str = None,
        origin_image_url: str = None,
    ):
        self.image_url = image_url
        self.origin_image_url = origin_image_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        if self.origin_image_url is not None:
            result['OriginImageURL'] = self.origin_image_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        if m.get('OriginImageURL') is not None:
            self.origin_image_url = m.get('OriginImageURL')
        return self


class SegmentVehicleResponseBodyData(TeaModel):
    def __init__(
        self,
        elements: List[SegmentVehicleResponseBodyDataElements] = None,
    ):
        self.elements = elements

    def validate(self):
        if self.elements:
            for k in self.elements:
                if k:
                    k.validate()

    def to_map(self):
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
                temp_model = SegmentVehicleResponseBodyDataElements()
                self.elements.append(temp_model.from_map(k))
        return self


class SegmentVehicleResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: SegmentVehicleResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = SegmentVehicleResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class SegmentVehicleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SegmentVehicleResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = SegmentVehicleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateUserBucketConfigRequestData(TeaModel):
    def __init__(
        self,
        region: str = None,
        bucket: str = None,
    ):
        self.region = region
        self.bucket = bucket

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region is not None:
            result['Region'] = self.region
        if self.bucket is not None:
            result['Bucket'] = self.bucket
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')
        return self


class UpdateUserBucketConfigRequest(TeaModel):
    def __init__(
        self,
        data: List[UpdateUserBucketConfigRequestData] = None,
    ):
        self.data = data

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = UpdateUserBucketConfigRequestData()
                self.data.append(temp_model.from_map(k))
        return self


class UpdateUserBucketConfigResponseBodyData(TeaModel):
    def __init__(
        self,
        region_name: str = None,
        region: str = None,
        bucket: str = None,
    ):
        self.region_name = region_name
        self.region = region
        self.bucket = bucket

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_name is not None:
            result['RegionName'] = self.region_name
        if self.region is not None:
            result['Region'] = self.region
        if self.bucket is not None:
            result['Bucket'] = self.bucket
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionName') is not None:
            self.region_name = m.get('RegionName')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')
        return self


class UpdateUserBucketConfigResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: List[UpdateUserBucketConfigResponseBodyData] = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = UpdateUserBucketConfigResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class UpdateUserBucketConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateUserBucketConfigResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = UpdateUserBucketConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


