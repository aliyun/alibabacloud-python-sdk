# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, BinaryIO, List


class GetAsyncJobResultRequest(TeaModel):
    def __init__(
        self,
        job_id: str = None,
        async_: str = None,
    ):
        self.job_id = job_id
        self.async_ = async_

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.async_ is not None:
            result['Async'] = self.async_
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Async') is not None:
            self.async_ = m.get('Async')
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


class DetectImageElementsAdvanceRequest(TeaModel):
    def __init__(
        self,
        url_object: BinaryIO = None,
    ):
        self.url_object = url_object

    def validate(self):
        self.validate_required(self.url_object, 'url_object')

    def to_map(self):
        result = dict()
        if self.url_object is not None:
            result['UrlObject'] = self.url_object
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UrlObject') is not None:
            self.url_object = m.get('UrlObject')
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
        request_id: str = None,
        data: DetectImageElementsResponseBodyData = None,
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
            temp_model = DetectImageElementsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
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


class RecognizeVehicleTypeRequest(TeaModel):
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


class RecognizeVehicleTypeAdvanceRequest(TeaModel):
    def __init__(
        self,
        image_urlobject: BinaryIO = None,
    ):
        self.image_urlobject = image_urlobject

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        result = dict()
        if self.image_urlobject is not None:
            result['ImageURLObject'] = self.image_urlobject
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURLObject') is not None:
            self.image_urlobject = m.get('ImageURLObject')
        return self


class RecognizeVehicleTypeResponseBodyDataElements(TeaModel):
    def __init__(
        self,
        score: float = None,
        name: str = None,
    ):
        self.score = score
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.score is not None:
            result['Score'] = self.score
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class RecognizeVehicleTypeResponseBodyData(TeaModel):
    def __init__(
        self,
        elements: List[RecognizeVehicleTypeResponseBodyDataElements] = None,
        threshold: float = None,
    ):
        self.elements = elements
        self.threshold = threshold

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
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.elements = []
        if m.get('Elements') is not None:
            for k in m.get('Elements'):
                temp_model = RecognizeVehicleTypeResponseBodyDataElements()
                self.elements.append(temp_model.from_map(k))
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        return self


class RecognizeVehicleTypeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: RecognizeVehicleTypeResponseBodyData = None,
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
            temp_model = RecognizeVehicleTypeResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class RecognizeVehicleTypeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RecognizeVehicleTypeResponseBody = None,
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
            temp_model = RecognizeVehicleTypeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeFoodRequest(TeaModel):
    def __init__(
        self,
        image_url: str = None,
    ):
        # A short description of struct
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


class RecognizeFoodAdvanceRequest(TeaModel):
    def __init__(
        self,
        image_urlobject: BinaryIO = None,
    ):
        self.image_urlobject = image_urlobject

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        result = dict()
        if self.image_urlobject is not None:
            result['ImageURLObject'] = self.image_urlobject
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURLObject') is not None:
            self.image_urlobject = m.get('ImageURLObject')
        return self


class RecognizeFoodResponseBodyDataTopFives(TeaModel):
    def __init__(
        self,
        category: str = None,
        score: float = None,
        calorie: str = None,
    ):
        self.category = category
        self.score = score
        self.calorie = calorie

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.score is not None:
            result['Score'] = self.score
        if self.calorie is not None:
            result['Calorie'] = self.calorie
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('Calorie') is not None:
            self.calorie = m.get('Calorie')
        return self


class RecognizeFoodResponseBodyData(TeaModel):
    def __init__(
        self,
        top_fives: List[RecognizeFoodResponseBodyDataTopFives] = None,
    ):
        self.top_fives = top_fives

    def validate(self):
        if self.top_fives:
            for k in self.top_fives:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['TopFives'] = []
        if self.top_fives is not None:
            for k in self.top_fives:
                result['TopFives'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.top_fives = []
        if m.get('TopFives') is not None:
            for k in m.get('TopFives'):
                temp_model = RecognizeFoodResponseBodyDataTopFives()
                self.top_fives.append(temp_model.from_map(k))
        return self


class RecognizeFoodResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: RecognizeFoodResponseBodyData = None,
    ):
        # Id of the request
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
            temp_model = RecognizeFoodResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class RecognizeFoodResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RecognizeFoodResponseBody = None,
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
            temp_model = RecognizeFoodResponseBody()
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


class RecognizeImageStyleAdvanceRequest(TeaModel):
    def __init__(
        self,
        url_object: BinaryIO = None,
    ):
        self.url_object = url_object

    def validate(self):
        self.validate_required(self.url_object, 'url_object')

    def to_map(self):
        result = dict()
        if self.url_object is not None:
            result['UrlObject'] = self.url_object
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UrlObject') is not None:
            self.url_object = m.get('UrlObject')
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
        request_id: str = None,
        data: RecognizeImageStyleResponseBodyData = None,
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
            temp_model = RecognizeImageStyleResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
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


class RecognizeSceneRequest(TeaModel):
    def __init__(
        self,
        image_type: int = None,
        image_url: str = None,
    ):
        self.image_type = image_type
        self.image_url = image_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.image_type is not None:
            result['ImageType'] = self.image_type
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageType') is not None:
            self.image_type = m.get('ImageType')
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        return self


class RecognizeSceneAdvanceRequest(TeaModel):
    def __init__(
        self,
        image_urlobject: BinaryIO = None,
        image_type: int = None,
    ):
        self.image_urlobject = image_urlobject
        self.image_type = image_type

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        result = dict()
        if self.image_urlobject is not None:
            result['ImageURLObject'] = self.image_urlobject
        if self.image_type is not None:
            result['ImageType'] = self.image_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURLObject') is not None:
            self.image_urlobject = m.get('ImageURLObject')
        if m.get('ImageType') is not None:
            self.image_type = m.get('ImageType')
        return self


class RecognizeSceneResponseBodyDataTags(TeaModel):
    def __init__(
        self,
        value: str = None,
        confidence: float = None,
    ):
        self.value = value
        self.confidence = confidence

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.value is not None:
            result['Value'] = self.value
        if self.confidence is not None:
            result['Confidence'] = self.confidence
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('Confidence') is not None:
            self.confidence = m.get('Confidence')
        return self


class RecognizeSceneResponseBodyData(TeaModel):
    def __init__(
        self,
        tags: List[RecognizeSceneResponseBodyDataTags] = None,
    ):
        self.tags = tags

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = RecognizeSceneResponseBodyDataTags()
                self.tags.append(temp_model.from_map(k))
        return self


class RecognizeSceneResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: RecognizeSceneResponseBodyData = None,
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
            temp_model = RecognizeSceneResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class RecognizeSceneResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RecognizeSceneResponseBody = None,
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
            temp_model = RecognizeSceneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ClassifyingRubbishRequest(TeaModel):
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


class ClassifyingRubbishAdvanceRequest(TeaModel):
    def __init__(
        self,
        image_urlobject: BinaryIO = None,
    ):
        self.image_urlobject = image_urlobject

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        result = dict()
        if self.image_urlobject is not None:
            result['ImageURLObject'] = self.image_urlobject
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURLObject') is not None:
            self.image_urlobject = m.get('ImageURLObject')
        return self


class ClassifyingRubbishResponseBodyDataElements(TeaModel):
    def __init__(
        self,
        category_score: float = None,
        rubbish: str = None,
        rubbish_score: float = None,
        category: str = None,
    ):
        self.category_score = category_score
        self.rubbish = rubbish
        self.rubbish_score = rubbish_score
        self.category = category

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.category_score is not None:
            result['CategoryScore'] = self.category_score
        if self.rubbish is not None:
            result['Rubbish'] = self.rubbish
        if self.rubbish_score is not None:
            result['RubbishScore'] = self.rubbish_score
        if self.category is not None:
            result['Category'] = self.category
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryScore') is not None:
            self.category_score = m.get('CategoryScore')
        if m.get('Rubbish') is not None:
            self.rubbish = m.get('Rubbish')
        if m.get('RubbishScore') is not None:
            self.rubbish_score = m.get('RubbishScore')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        return self


class ClassifyingRubbishResponseBodyData(TeaModel):
    def __init__(
        self,
        sensitive: bool = None,
        elements: List[ClassifyingRubbishResponseBodyDataElements] = None,
    ):
        self.sensitive = sensitive
        self.elements = elements

    def validate(self):
        if self.elements:
            for k in self.elements:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.sensitive is not None:
            result['Sensitive'] = self.sensitive
        result['Elements'] = []
        if self.elements is not None:
            for k in self.elements:
                result['Elements'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Sensitive') is not None:
            self.sensitive = m.get('Sensitive')
        self.elements = []
        if m.get('Elements') is not None:
            for k in m.get('Elements'):
                temp_model = ClassifyingRubbishResponseBodyDataElements()
                self.elements.append(temp_model.from_map(k))
        return self


class ClassifyingRubbishResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: ClassifyingRubbishResponseBodyData = None,
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
            temp_model = ClassifyingRubbishResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class ClassifyingRubbishResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ClassifyingRubbishResponseBody = None,
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
            temp_model = ClassifyingRubbishResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetectFruitsRequest(TeaModel):
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


class DetectFruitsAdvanceRequest(TeaModel):
    def __init__(
        self,
        image_urlobject: BinaryIO = None,
    ):
        self.image_urlobject = image_urlobject

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        result = dict()
        if self.image_urlobject is not None:
            result['ImageURLObject'] = self.image_urlobject
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURLObject') is not None:
            self.image_urlobject = m.get('ImageURLObject')
        return self


class DetectFruitsResponseBodyDataElements(TeaModel):
    def __init__(
        self,
        score: float = None,
        box: List[float] = None,
        name: str = None,
    ):
        self.score = score
        self.box = box
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.score is not None:
            result['Score'] = self.score
        if self.box is not None:
            result['Box'] = self.box
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('Box') is not None:
            self.box = m.get('Box')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DetectFruitsResponseBodyData(TeaModel):
    def __init__(
        self,
        elements: List[DetectFruitsResponseBodyDataElements] = None,
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
                temp_model = DetectFruitsResponseBodyDataElements()
                self.elements.append(temp_model.from_map(k))
        return self


class DetectFruitsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: DetectFruitsResponseBodyData = None,
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
            temp_model = DetectFruitsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class DetectFruitsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DetectFruitsResponseBody = None,
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
            temp_model = DetectFruitsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeImageColorRequest(TeaModel):
    def __init__(
        self,
        url: str = None,
        color_count: int = None,
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


class RecognizeImageColorAdvanceRequest(TeaModel):
    def __init__(
        self,
        url_object: BinaryIO = None,
        color_count: int = None,
    ):
        self.url_object = url_object
        self.color_count = color_count

    def validate(self):
        self.validate_required(self.url_object, 'url_object')

    def to_map(self):
        result = dict()
        if self.url_object is not None:
            result['UrlObject'] = self.url_object
        if self.color_count is not None:
            result['ColorCount'] = self.color_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UrlObject') is not None:
            self.url_object = m.get('UrlObject')
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
        request_id: str = None,
        data: RecognizeImageColorResponseBodyData = None,
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
            temp_model = RecognizeImageColorResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
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


class RecognizeLogoRequestTasks(TeaModel):
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


class RecognizeLogoRequest(TeaModel):
    def __init__(
        self,
        tasks: List[RecognizeLogoRequestTasks] = None,
    ):
        self.tasks = tasks

    def validate(self):
        if self.tasks:
            for k in self.tasks:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Tasks'] = []
        if self.tasks is not None:
            for k in self.tasks:
                result['Tasks'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tasks = []
        if m.get('Tasks') is not None:
            for k in m.get('Tasks'):
                temp_model = RecognizeLogoRequestTasks()
                self.tasks.append(temp_model.from_map(k))
        return self


class RecognizeLogoResponseBodyDataElementsResultsLogosData(TeaModel):
    def __init__(
        self,
        type: str = None,
        w: float = None,
        h: float = None,
        y: float = None,
        name: str = None,
        x: float = None,
    ):
        self.type = type
        self.w = w
        self.h = h
        self.y = y
        self.name = name
        self.x = x

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.w is not None:
            result['W'] = self.w
        if self.h is not None:
            result['H'] = self.h
        if self.y is not None:
            result['Y'] = self.y
        if self.name is not None:
            result['Name'] = self.name
        if self.x is not None:
            result['X'] = self.x
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('W') is not None:
            self.w = m.get('W')
        if m.get('H') is not None:
            self.h = m.get('H')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('X') is not None:
            self.x = m.get('X')
        return self


class RecognizeLogoResponseBodyDataElementsResults(TeaModel):
    def __init__(
        self,
        suggestion: str = None,
        logos_data: List[RecognizeLogoResponseBodyDataElementsResultsLogosData] = None,
        label: str = None,
        rate: float = None,
    ):
        self.suggestion = suggestion
        self.logos_data = logos_data
        self.label = label
        self.rate = rate

    def validate(self):
        if self.logos_data:
            for k in self.logos_data:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.suggestion is not None:
            result['Suggestion'] = self.suggestion
        result['LogosData'] = []
        if self.logos_data is not None:
            for k in self.logos_data:
                result['LogosData'].append(k.to_map() if k else None)
        if self.label is not None:
            result['Label'] = self.label
        if self.rate is not None:
            result['Rate'] = self.rate
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Suggestion') is not None:
            self.suggestion = m.get('Suggestion')
        self.logos_data = []
        if m.get('LogosData') is not None:
            for k in m.get('LogosData'):
                temp_model = RecognizeLogoResponseBodyDataElementsResultsLogosData()
                self.logos_data.append(temp_model.from_map(k))
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Rate') is not None:
            self.rate = m.get('Rate')
        return self


class RecognizeLogoResponseBodyDataElements(TeaModel):
    def __init__(
        self,
        image_url: str = None,
        task_id: str = None,
        results: List[RecognizeLogoResponseBodyDataElementsResults] = None,
    ):
        self.image_url = image_url
        self.task_id = task_id
        self.results = results

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        result['Results'] = []
        if self.results is not None:
            for k in self.results:
                result['Results'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        self.results = []
        if m.get('Results') is not None:
            for k in m.get('Results'):
                temp_model = RecognizeLogoResponseBodyDataElementsResults()
                self.results.append(temp_model.from_map(k))
        return self


class RecognizeLogoResponseBodyData(TeaModel):
    def __init__(
        self,
        elements: List[RecognizeLogoResponseBodyDataElements] = None,
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
                temp_model = RecognizeLogoResponseBodyDataElements()
                self.elements.append(temp_model.from_map(k))
        return self


class RecognizeLogoResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: RecognizeLogoResponseBodyData = None,
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
            temp_model = RecognizeLogoResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class RecognizeLogoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RecognizeLogoResponseBody = None,
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
            temp_model = RecognizeLogoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TaggingImageRequest(TeaModel):
    def __init__(
        self,
        image_type: int = None,
        image_url: str = None,
        async_: bool = None,
    ):
        self.image_type = image_type
        self.image_url = image_url
        self.async_ = async_

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.image_type is not None:
            result['ImageType'] = self.image_type
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        if self.async_ is not None:
            result['Async'] = self.async_
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageType') is not None:
            self.image_type = m.get('ImageType')
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        if m.get('Async') is not None:
            self.async_ = m.get('Async')
        return self


class TaggingImageAdvanceRequest(TeaModel):
    def __init__(
        self,
        image_urlobject: BinaryIO = None,
        image_type: int = None,
        async_: bool = None,
    ):
        self.image_urlobject = image_urlobject
        self.image_type = image_type
        self.async_ = async_

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        result = dict()
        if self.image_urlobject is not None:
            result['ImageURLObject'] = self.image_urlobject
        if self.image_type is not None:
            result['ImageType'] = self.image_type
        if self.async_ is not None:
            result['Async'] = self.async_
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURLObject') is not None:
            self.image_urlobject = m.get('ImageURLObject')
        if m.get('ImageType') is not None:
            self.image_type = m.get('ImageType')
        if m.get('Async') is not None:
            self.async_ = m.get('Async')
        return self


class TaggingImageResponseBodyDataTags(TeaModel):
    def __init__(
        self,
        value: str = None,
        confidence: float = None,
    ):
        self.value = value
        self.confidence = confidence

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.value is not None:
            result['Value'] = self.value
        if self.confidence is not None:
            result['Confidence'] = self.confidence
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('Confidence') is not None:
            self.confidence = m.get('Confidence')
        return self


class TaggingImageResponseBodyData(TeaModel):
    def __init__(
        self,
        tags: List[TaggingImageResponseBodyDataTags] = None,
    ):
        self.tags = tags

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = TaggingImageResponseBodyDataTags()
                self.tags.append(temp_model.from_map(k))
        return self


class TaggingImageResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: TaggingImageResponseBodyData = None,
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
            temp_model = TaggingImageResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class TaggingImageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: TaggingImageResponseBody = None,
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
            temp_model = TaggingImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EvaluateCertificateQualityRequest(TeaModel):
    def __init__(
        self,
        image_url: str = None,
        type: str = None,
    ):
        self.image_url = image_url
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class EvaluateCertificateQualityAdvanceRequest(TeaModel):
    def __init__(
        self,
        image_urlobject: BinaryIO = None,
        type: str = None,
    ):
        self.image_urlobject = image_urlobject
        self.type = type

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        result = dict()
        if self.image_urlobject is not None:
            result['ImageURLObject'] = self.image_urlobject
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURLObject') is not None:
            self.image_urlobject = m.get('ImageURLObject')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class EvaluateCertificateQualityResponseBodyDataElements(TeaModel):
    def __init__(
        self,
        value: str = None,
        pass_: str = None,
        score: str = None,
    ):
        self.value = value
        self.pass_ = pass_
        self.score = score

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.value is not None:
            result['Value'] = self.value
        if self.pass_ is not None:
            result['Pass'] = self.pass_
        if self.score is not None:
            result['Score'] = self.score
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('Pass') is not None:
            self.pass_ = m.get('Pass')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        return self


class EvaluateCertificateQualityResponseBodyData(TeaModel):
    def __init__(
        self,
        elements: List[EvaluateCertificateQualityResponseBodyDataElements] = None,
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
                temp_model = EvaluateCertificateQualityResponseBodyDataElements()
                self.elements.append(temp_model.from_map(k))
        return self


class EvaluateCertificateQualityResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: EvaluateCertificateQualityResponseBodyData = None,
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
            temp_model = EvaluateCertificateQualityResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class EvaluateCertificateQualityResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: EvaluateCertificateQualityResponseBody = None,
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
            temp_model = EvaluateCertificateQualityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


