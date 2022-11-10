# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import BinaryIO, List, Dict, Any


class ClassifyingRubbishRequest(TeaModel):
    def __init__(
        self,
        image_url: str = None,
    ):
        self.image_url = image_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_urlobject is not None:
            result['ImageURL'] = self.image_urlobject
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_urlobject = m.get('ImageURL')
        return self


class ClassifyingRubbishResponseBodyDataElements(TeaModel):
    def __init__(
        self,
        category: str = None,
        category_score: float = None,
        rubbish: str = None,
        rubbish_score: float = None,
    ):
        self.category = category
        self.category_score = category_score
        self.rubbish = rubbish
        self.rubbish_score = rubbish_score

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.category_score is not None:
            result['CategoryScore'] = self.category_score
        if self.rubbish is not None:
            result['Rubbish'] = self.rubbish
        if self.rubbish_score is not None:
            result['RubbishScore'] = self.rubbish_score
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('CategoryScore') is not None:
            self.category_score = m.get('CategoryScore')
        if m.get('Rubbish') is not None:
            self.rubbish = m.get('Rubbish')
        if m.get('RubbishScore') is not None:
            self.rubbish_score = m.get('RubbishScore')
        return self


class ClassifyingRubbishResponseBodyData(TeaModel):
    def __init__(
        self,
        elements: List[ClassifyingRubbishResponseBodyDataElements] = None,
        sensitive: bool = None,
    ):
        self.elements = elements
        self.sensitive = sensitive

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
        if self.sensitive is not None:
            result['Sensitive'] = self.sensitive
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.elements = []
        if m.get('Elements') is not None:
            for k in m.get('Elements'):
                temp_model = ClassifyingRubbishResponseBodyDataElements()
                self.elements.append(temp_model.from_map(k))
        if m.get('Sensitive') is not None:
            self.sensitive = m.get('Sensitive')
        return self


class ClassifyingRubbishResponseBody(TeaModel):
    def __init__(
        self,
        data: ClassifyingRubbishResponseBodyData = None,
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
            temp_model = ClassifyingRubbishResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ClassifyingRubbishResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ClassifyingRubbishResponseBody = None,
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_urlobject is not None:
            result['ImageURL'] = self.image_urlobject
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_urlobject = m.get('ImageURL')
        return self


class DetectFruitsResponseBodyDataElements(TeaModel):
    def __init__(
        self,
        box: List[float] = None,
        name: str = None,
        score: float = None,
    ):
        self.box = box
        self.name = name
        self.score = score

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.box is not None:
            result['Box'] = self.box
        if self.name is not None:
            result['Name'] = self.name
        if self.score is not None:
            result['Score'] = self.score
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Box') is not None:
            self.box = m.get('Box')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Score') is not None:
            self.score = m.get('Score')
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
                temp_model = DetectFruitsResponseBodyDataElements()
                self.elements.append(temp_model.from_map(k))
        return self


class DetectFruitsResponseBody(TeaModel):
    def __init__(
        self,
        data: DetectFruitsResponseBodyData = None,
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
            temp_model = DetectFruitsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DetectFruitsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DetectFruitsResponseBody = None,
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
            temp_model = DetectFruitsResponseBody()
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.url_object is not None:
            result['Url'] = self.url_object
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url_object = m.get('Url')
        return self


class DetectImageElementsResponseBodyDataElements(TeaModel):
    def __init__(
        self,
        height: int = None,
        score: float = None,
        type: str = None,
        width: int = None,
        x: int = None,
        y: int = None,
    ):
        self.height = height
        self.score = score
        self.type = type
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
        if self.score is not None:
            result['Score'] = self.score
        if self.type is not None:
            result['Type'] = self.type
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
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('X') is not None:
            self.x = m.get('X')
        if m.get('Y') is not None:
            self.y = m.get('Y')
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
                temp_model = DetectImageElementsResponseBodyDataElements()
                self.elements.append(temp_model.from_map(k))
        return self


class DetectImageElementsResponseBody(TeaModel):
    def __init__(
        self,
        data: DetectImageElementsResponseBodyData = None,
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
            temp_model = DetectImageElementsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DetectImageElementsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DetectImageElementsResponseBody = None,
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
            temp_model = DetectImageElementsResponseBody()
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_urlobject is not None:
            result['ImageURL'] = self.image_urlobject
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_urlobject = m.get('ImageURL')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class EvaluateCertificateQualityResponseBodyDataElements(TeaModel):
    def __init__(
        self,
        pass_: str = None,
        score: str = None,
        value: str = None,
    ):
        self.pass_ = pass_
        self.score = score
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pass_ is not None:
            result['Pass'] = self.pass_
        if self.score is not None:
            result['Score'] = self.score
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Pass') is not None:
            self.pass_ = m.get('Pass')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('Value') is not None:
            self.value = m.get('Value')
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
                temp_model = EvaluateCertificateQualityResponseBodyDataElements()
                self.elements.append(temp_model.from_map(k))
        return self


class EvaluateCertificateQualityResponseBody(TeaModel):
    def __init__(
        self,
        data: EvaluateCertificateQualityResponseBodyData = None,
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
            temp_model = EvaluateCertificateQualityResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class EvaluateCertificateQualityResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: EvaluateCertificateQualityResponseBody = None,
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
            temp_model = EvaluateCertificateQualityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAsyncJobResultRequest(TeaModel):
    def __init__(
        self,
        job_id: str = None,
    ):
        self.job_id = job_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class GetAsyncJobResultResponseBodyData(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        job_id: str = None,
        result: str = None,
        status: str = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.job_id = job_id
        self.result = result
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.result is not None:
            result['Result'] = self.result
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetAsyncJobResultResponseBody(TeaModel):
    def __init__(
        self,
        data: GetAsyncJobResultResponseBodyData = None,
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
            temp_model = GetAsyncJobResultResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetAsyncJobResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAsyncJobResultResponseBody = None,
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
            temp_model = GetAsyncJobResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeFoodRequest(TeaModel):
    def __init__(
        self,
        image_url: str = None,
    ):
        self.image_url = image_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_urlobject is not None:
            result['ImageURL'] = self.image_urlobject
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_urlobject = m.get('ImageURL')
        return self


class RecognizeFoodResponseBodyDataTopFives(TeaModel):
    def __init__(
        self,
        calorie: str = None,
        category: str = None,
        score: float = None,
    ):
        self.calorie = calorie
        self.category = category
        self.score = score

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.calorie is not None:
            result['Calorie'] = self.calorie
        if self.category is not None:
            result['Category'] = self.category
        if self.score is not None:
            result['Score'] = self.score
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Calorie') is not None:
            self.calorie = m.get('Calorie')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Score') is not None:
            self.score = m.get('Score')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        data: RecognizeFoodResponseBodyData = None,
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
            temp_model = RecognizeFoodResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RecognizeFoodResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RecognizeFoodResponseBody = None,
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
            temp_model = RecognizeFoodResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeImageColorRequest(TeaModel):
    def __init__(
        self,
        color_count: int = None,
        url: str = None,
    ):
        self.color_count = color_count
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.color_count is not None:
            result['ColorCount'] = self.color_count
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ColorCount') is not None:
            self.color_count = m.get('ColorCount')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class RecognizeImageColorAdvanceRequest(TeaModel):
    def __init__(
        self,
        color_count: int = None,
        url_object: BinaryIO = None,
    ):
        self.color_count = color_count
        self.url_object = url_object

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.color_count is not None:
            result['ColorCount'] = self.color_count
        if self.url_object is not None:
            result['Url'] = self.url_object
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ColorCount') is not None:
            self.color_count = m.get('ColorCount')
        if m.get('Url') is not None:
            self.url_object = m.get('Url')
        return self


class RecognizeImageColorResponseBodyDataColorTemplateList(TeaModel):
    def __init__(
        self,
        color: str = None,
        label: str = None,
        percentage: float = None,
    ):
        self.color = color
        self.label = label
        self.percentage = percentage

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.color is not None:
            result['Color'] = self.color
        if self.label is not None:
            result['Label'] = self.label
        if self.percentage is not None:
            result['Percentage'] = self.percentage
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Color') is not None:
            self.color = m.get('Color')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Percentage') is not None:
            self.percentage = m.get('Percentage')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        data: RecognizeImageColorResponseBodyData = None,
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
            temp_model = RecognizeImageColorResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RecognizeImageColorResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RecognizeImageColorResponseBody = None,
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.url_object is not None:
            result['Url'] = self.url_object
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url_object = m.get('Url')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        data: RecognizeImageStyleResponseBodyData = None,
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
            temp_model = RecognizeImageStyleResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RecognizeImageStyleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RecognizeImageStyleResponseBody = None,
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
            temp_model = RecognizeImageStyleResponseBody()
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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


class RecognizeLogoAdvanceRequestTasks(TeaModel):
    def __init__(
        self,
        image_urlobject: BinaryIO = None,
    ):
        self.image_urlobject = image_urlobject

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_urlobject is not None:
            result['ImageURL'] = self.image_urlobject
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_urlobject = m.get('ImageURL')
        return self


class RecognizeLogoAdvanceRequest(TeaModel):
    def __init__(
        self,
        tasks: List[RecognizeLogoAdvanceRequestTasks] = None,
    ):
        self.tasks = tasks

    def validate(self):
        if self.tasks:
            for k in self.tasks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
                temp_model = RecognizeLogoAdvanceRequestTasks()
                self.tasks.append(temp_model.from_map(k))
        return self


class RecognizeLogoResponseBodyDataElementsResultsLogosData(TeaModel):
    def __init__(
        self,
        h: float = None,
        name: str = None,
        type: str = None,
        w: float = None,
        x: float = None,
        y: float = None,
    ):
        self.h = h
        self.name = name
        self.type = type
        self.w = w
        self.x = x
        self.y = y

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.h is not None:
            result['H'] = self.h
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        if self.w is not None:
            result['W'] = self.w
        if self.x is not None:
            result['X'] = self.x
        if self.y is not None:
            result['Y'] = self.y
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('H') is not None:
            self.h = m.get('H')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('W') is not None:
            self.w = m.get('W')
        if m.get('X') is not None:
            self.x = m.get('X')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        return self


class RecognizeLogoResponseBodyDataElementsResults(TeaModel):
    def __init__(
        self,
        label: str = None,
        logos_data: List[RecognizeLogoResponseBodyDataElementsResultsLogosData] = None,
        rate: float = None,
        suggestion: str = None,
    ):
        self.label = label
        self.logos_data = logos_data
        self.rate = rate
        self.suggestion = suggestion

    def validate(self):
        if self.logos_data:
            for k in self.logos_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label is not None:
            result['Label'] = self.label
        result['LogosData'] = []
        if self.logos_data is not None:
            for k in self.logos_data:
                result['LogosData'].append(k.to_map() if k else None)
        if self.rate is not None:
            result['Rate'] = self.rate
        if self.suggestion is not None:
            result['Suggestion'] = self.suggestion
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Label') is not None:
            self.label = m.get('Label')
        self.logos_data = []
        if m.get('LogosData') is not None:
            for k in m.get('LogosData'):
                temp_model = RecognizeLogoResponseBodyDataElementsResultsLogosData()
                self.logos_data.append(temp_model.from_map(k))
        if m.get('Rate') is not None:
            self.rate = m.get('Rate')
        if m.get('Suggestion') is not None:
            self.suggestion = m.get('Suggestion')
        return self


class RecognizeLogoResponseBodyDataElements(TeaModel):
    def __init__(
        self,
        image_url: str = None,
        results: List[RecognizeLogoResponseBodyDataElementsResults] = None,
        task_id: str = None,
    ):
        self.image_url = image_url
        self.results = results
        self.task_id = task_id

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        result['Results'] = []
        if self.results is not None:
            for k in self.results:
                result['Results'].append(k.to_map() if k else None)
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        self.results = []
        if m.get('Results') is not None:
            for k in m.get('Results'):
                temp_model = RecognizeLogoResponseBodyDataElementsResults()
                self.results.append(temp_model.from_map(k))
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
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
                temp_model = RecognizeLogoResponseBodyDataElements()
                self.elements.append(temp_model.from_map(k))
        return self


class RecognizeLogoResponseBody(TeaModel):
    def __init__(
        self,
        data: RecognizeLogoResponseBodyData = None,
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
            temp_model = RecognizeLogoResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RecognizeLogoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RecognizeLogoResponseBody = None,
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
            temp_model = RecognizeLogoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeSceneRequest(TeaModel):
    def __init__(
        self,
        image_url: str = None,
    ):
        self.image_url = image_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        return self


class RecognizeSceneAdvanceRequest(TeaModel):
    def __init__(
        self,
        image_urlobject: BinaryIO = None,
    ):
        self.image_urlobject = image_urlobject

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_urlobject is not None:
            result['ImageURL'] = self.image_urlobject
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_urlobject = m.get('ImageURL')
        return self


class RecognizeSceneResponseBodyDataTags(TeaModel):
    def __init__(
        self,
        confidence: float = None,
        value: str = None,
    ):
        self.confidence = confidence
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.confidence is not None:
            result['Confidence'] = self.confidence
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Confidence') is not None:
            self.confidence = m.get('Confidence')
        if m.get('Value') is not None:
            self.value = m.get('Value')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        data: RecognizeSceneResponseBodyData = None,
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
            temp_model = RecognizeSceneResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RecognizeSceneResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RecognizeSceneResponseBody = None,
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
            temp_model = RecognizeSceneResponseBody()
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_urlobject is not None:
            result['ImageURL'] = self.image_urlobject
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_urlobject = m.get('ImageURL')
        return self


class RecognizeVehicleTypeResponseBodyDataElements(TeaModel):
    def __init__(
        self,
        name: str = None,
        score: float = None,
    ):
        self.name = name
        self.score = score

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.score is not None:
            result['Score'] = self.score
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Score') is not None:
            self.score = m.get('Score')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        data: RecognizeVehicleTypeResponseBodyData = None,
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
            temp_model = RecognizeVehicleTypeResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RecognizeVehicleTypeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RecognizeVehicleTypeResponseBody = None,
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
            temp_model = RecognizeVehicleTypeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TaggingAdImageRequest(TeaModel):
    def __init__(
        self,
        image_url: str = None,
    ):
        self.image_url = image_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        return self


class TaggingAdImageAdvanceRequest(TeaModel):
    def __init__(
        self,
        image_urlobject: BinaryIO = None,
    ):
        self.image_urlobject = image_urlobject

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_urlobject is not None:
            result['ImageURL'] = self.image_urlobject
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_urlobject = m.get('ImageURL')
        return self


class TaggingAdImageResponseBodyData(TeaModel):
    def __init__(
        self,
        tag_info: Dict[str, Any] = None,
    ):
        self.tag_info = tag_info

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_info is not None:
            result['TagInfo'] = self.tag_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagInfo') is not None:
            self.tag_info = m.get('TagInfo')
        return self


class TaggingAdImageResponseBody(TeaModel):
    def __init__(
        self,
        data: TaggingAdImageResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
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
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = TaggingAdImageResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class TaggingAdImageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: TaggingAdImageResponseBody = None,
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
            temp_model = TaggingAdImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TaggingImageRequest(TeaModel):
    def __init__(
        self,
        image_url: str = None,
    ):
        self.image_url = image_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        return self


class TaggingImageAdvanceRequest(TeaModel):
    def __init__(
        self,
        image_urlobject: BinaryIO = None,
    ):
        self.image_urlobject = image_urlobject

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_urlobject is not None:
            result['ImageURL'] = self.image_urlobject
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_urlobject = m.get('ImageURL')
        return self


class TaggingImageResponseBodyDataTags(TeaModel):
    def __init__(
        self,
        confidence: float = None,
        value: str = None,
    ):
        self.confidence = confidence
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.confidence is not None:
            result['Confidence'] = self.confidence
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Confidence') is not None:
            self.confidence = m.get('Confidence')
        if m.get('Value') is not None:
            self.value = m.get('Value')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        data: TaggingImageResponseBodyData = None,
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
            temp_model = TaggingImageResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class TaggingImageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: TaggingImageResponseBody = None,
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
            temp_model = TaggingImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


