# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import BinaryIO, Dict, List


class ChangeSkyRequest(TeaModel):
    def __init__(
        self,
        image_url: str = None,
        replace_image_url: str = None,
    ):
        self.image_url = image_url
        self.replace_image_url = replace_image_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        if self.replace_image_url is not None:
            result['ReplaceImageURL'] = self.replace_image_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        if m.get('ReplaceImageURL') is not None:
            self.replace_image_url = m.get('ReplaceImageURL')
        return self


class ChangeSkyAdvanceRequest(TeaModel):
    def __init__(
        self,
        image_urlobject: BinaryIO = None,
        replace_image_url: str = None,
    ):
        self.image_urlobject = image_urlobject
        self.replace_image_url = replace_image_url

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        result = dict()
        if self.image_urlobject is not None:
            result['ImageURLObject'] = self.image_urlobject
        if self.replace_image_url is not None:
            result['ReplaceImageURL'] = self.replace_image_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURLObject') is not None:
            self.image_urlobject = m.get('ImageURLObject')
        if m.get('ReplaceImageURL') is not None:
            self.replace_image_url = m.get('ReplaceImageURL')
        return self


class ChangeSkyResponseBodyData(TeaModel):
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


class ChangeSkyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: ChangeSkyResponseBodyData = None,
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
            temp_model = ChangeSkyResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class ChangeSkyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ChangeSkyResponseBody = None,
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
            temp_model = ChangeSkyResponseBody()
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


class ParseFaceAdvanceRequest(TeaModel):
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


class RefineMaskRequest(TeaModel):
    def __init__(
        self,
        mask_image_url: str = None,
        image_url: str = None,
    ):
        self.mask_image_url = mask_image_url
        self.image_url = image_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.mask_image_url is not None:
            result['MaskImageURL'] = self.mask_image_url
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaskImageURL') is not None:
            self.mask_image_url = m.get('MaskImageURL')
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        return self


class RefineMaskAdvanceRequest(TeaModel):
    def __init__(
        self,
        image_urlobject: BinaryIO = None,
        mask_image_url: str = None,
    ):
        self.image_urlobject = image_urlobject
        self.mask_image_url = mask_image_url

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        result = dict()
        if self.image_urlobject is not None:
            result['ImageURLObject'] = self.image_urlobject
        if self.mask_image_url is not None:
            result['MaskImageURL'] = self.mask_image_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURLObject') is not None:
            self.image_urlobject = m.get('ImageURLObject')
        if m.get('MaskImageURL') is not None:
            self.mask_image_url = m.get('MaskImageURL')
        return self


class RefineMaskResponseBodyDataElements(TeaModel):
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


class RefineMaskResponseBodyData(TeaModel):
    def __init__(
        self,
        elements: List[RefineMaskResponseBodyDataElements] = None,
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
                temp_model = RefineMaskResponseBodyDataElements()
                self.elements.append(temp_model.from_map(k))
        return self


class RefineMaskResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: RefineMaskResponseBodyData = None,
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
            temp_model = RefineMaskResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class RefineMaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RefineMaskResponseBody = None,
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
            temp_model = RefineMaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SegmentAnimalRequest(TeaModel):
    def __init__(
        self,
        image_url: str = None,
        return_form: str = None,
    ):
        self.image_url = image_url
        self.return_form = return_form

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        if self.return_form is not None:
            result['ReturnForm'] = self.return_form
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        if m.get('ReturnForm') is not None:
            self.return_form = m.get('ReturnForm')
        return self


class SegmentAnimalAdvanceRequest(TeaModel):
    def __init__(
        self,
        image_urlobject: BinaryIO = None,
        return_form: str = None,
    ):
        self.image_urlobject = image_urlobject
        self.return_form = return_form

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        result = dict()
        if self.image_urlobject is not None:
            result['ImageURLObject'] = self.image_urlobject
        if self.return_form is not None:
            result['ReturnForm'] = self.return_form
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURLObject') is not None:
            self.image_urlobject = m.get('ImageURLObject')
        if m.get('ReturnForm') is not None:
            self.return_form = m.get('ReturnForm')
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
        async_: bool = None,
        return_form: str = None,
    ):
        self.image_url = image_url
        self.async_ = async_
        self.return_form = return_form

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        if self.async_ is not None:
            result['Async'] = self.async_
        if self.return_form is not None:
            result['ReturnForm'] = self.return_form
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        if m.get('Async') is not None:
            self.async_ = m.get('Async')
        if m.get('ReturnForm') is not None:
            self.return_form = m.get('ReturnForm')
        return self


class SegmentBodyAdvanceRequest(TeaModel):
    def __init__(
        self,
        image_urlobject: BinaryIO = None,
        async_: bool = None,
        return_form: str = None,
    ):
        self.image_urlobject = image_urlobject
        self.async_ = async_
        self.return_form = return_form

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        result = dict()
        if self.image_urlobject is not None:
            result['ImageURLObject'] = self.image_urlobject
        if self.async_ is not None:
            result['Async'] = self.async_
        if self.return_form is not None:
            result['ReturnForm'] = self.return_form
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURLObject') is not None:
            self.image_urlobject = m.get('ImageURLObject')
        if m.get('Async') is not None:
            self.async_ = m.get('Async')
        if m.get('ReturnForm') is not None:
            self.return_form = m.get('ReturnForm')
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
            result['ImageURL'] = self.image_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        return self


class SegmentBodyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: SegmentBodyResponseBodyData = None,
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
            temp_model = SegmentBodyResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
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


class SegmentClothAdvanceRequest(TeaModel):
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
        return_form: str = None,
    ):
        self.image_url = image_url
        self.return_form = return_form

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        if self.return_form is not None:
            result['ReturnForm'] = self.return_form
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        if m.get('ReturnForm') is not None:
            self.return_form = m.get('ReturnForm')
        return self


class SegmentCommodityAdvanceRequest(TeaModel):
    def __init__(
        self,
        image_urlobject: BinaryIO = None,
        return_form: str = None,
    ):
        self.image_urlobject = image_urlobject
        self.return_form = return_form

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        result = dict()
        if self.image_urlobject is not None:
            result['ImageURLObject'] = self.image_urlobject
        if self.return_form is not None:
            result['ReturnForm'] = self.return_form
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURLObject') is not None:
            self.image_urlobject = m.get('ImageURLObject')
        if m.get('ReturnForm') is not None:
            self.return_form = m.get('ReturnForm')
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


class SegmentCommonImageRequest(TeaModel):
    def __init__(
        self,
        image_url: str = None,
        return_form: str = None,
    ):
        self.image_url = image_url
        self.return_form = return_form

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        if self.return_form is not None:
            result['ReturnForm'] = self.return_form
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        if m.get('ReturnForm') is not None:
            self.return_form = m.get('ReturnForm')
        return self


class SegmentCommonImageAdvanceRequest(TeaModel):
    def __init__(
        self,
        image_urlobject: BinaryIO = None,
        return_form: str = None,
    ):
        self.image_urlobject = image_urlobject
        self.return_form = return_form

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        result = dict()
        if self.image_urlobject is not None:
            result['ImageURLObject'] = self.image_urlobject
        if self.return_form is not None:
            result['ReturnForm'] = self.return_form
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURLObject') is not None:
            self.image_urlobject = m.get('ImageURLObject')
        if m.get('ReturnForm') is not None:
            self.return_form = m.get('ReturnForm')
        return self


class SegmentCommonImageResponseBodyData(TeaModel):
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


class SegmentCommonImageResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: SegmentCommonImageResponseBodyData = None,
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
            temp_model = SegmentCommonImageResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class SegmentCommonImageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SegmentCommonImageResponseBody = None,
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
            temp_model = SegmentCommonImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SegmentFaceRequest(TeaModel):
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


class SegmentFaceAdvanceRequest(TeaModel):
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


class SegmentFaceResponseBodyDataElements(TeaModel):
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


class SegmentFaceResponseBodyData(TeaModel):
    def __init__(
        self,
        elements: List[SegmentFaceResponseBodyDataElements] = None,
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
                temp_model = SegmentFaceResponseBodyDataElements()
                self.elements.append(temp_model.from_map(k))
        return self


class SegmentFaceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: SegmentFaceResponseBodyData = None,
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
            temp_model = SegmentFaceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class SegmentFaceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SegmentFaceResponseBody = None,
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
            temp_model = SegmentFaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SegmentFoodRequest(TeaModel):
    def __init__(
        self,
        image_url: str = None,
        return_form: str = None,
    ):
        self.image_url = image_url
        self.return_form = return_form

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        if self.return_form is not None:
            result['ReturnForm'] = self.return_form
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        if m.get('ReturnForm') is not None:
            self.return_form = m.get('ReturnForm')
        return self


class SegmentFoodAdvanceRequest(TeaModel):
    def __init__(
        self,
        image_urlobject: BinaryIO = None,
        return_form: str = None,
    ):
        self.image_urlobject = image_urlobject
        self.return_form = return_form

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        result = dict()
        if self.image_urlobject is not None:
            result['ImageURLObject'] = self.image_urlobject
        if self.return_form is not None:
            result['ReturnForm'] = self.return_form
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURLObject') is not None:
            self.image_urlobject = m.get('ImageURLObject')
        if m.get('ReturnForm') is not None:
            self.return_form = m.get('ReturnForm')
        return self


class SegmentFoodResponseBodyData(TeaModel):
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


class SegmentFoodResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: SegmentFoodResponseBodyData = None,
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
            temp_model = SegmentFoodResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class SegmentFoodResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SegmentFoodResponseBody = None,
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
            temp_model = SegmentFoodResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SegmentFurnitureRequest(TeaModel):
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


class SegmentFurnitureAdvanceRequest(TeaModel):
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


class SegmentFurnitureResponseBodyDataElements(TeaModel):
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


class SegmentFurnitureResponseBodyData(TeaModel):
    def __init__(
        self,
        elements: List[SegmentFurnitureResponseBodyDataElements] = None,
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
                temp_model = SegmentFurnitureResponseBodyDataElements()
                self.elements.append(temp_model.from_map(k))
        return self


class SegmentFurnitureResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: SegmentFurnitureResponseBodyData = None,
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
            temp_model = SegmentFurnitureResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class SegmentFurnitureResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SegmentFurnitureResponseBody = None,
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
            temp_model = SegmentFurnitureResponseBody()
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


class SegmentHairAdvanceRequest(TeaModel):
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


class SegmentHDBodyRequest(TeaModel):
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


class SegmentHDBodyAdvanceRequest(TeaModel):
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


class SegmentHDBodyResponseBodyData(TeaModel):
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


class SegmentHDBodyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: SegmentHDBodyResponseBodyData = None,
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
            temp_model = SegmentHDBodyResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class SegmentHDBodyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SegmentHDBodyResponseBody = None,
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
            temp_model = SegmentHDBodyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SegmentHDCommonImageRequest(TeaModel):
    def __init__(
        self,
        image_url: str = None,
        async_: bool = None,
    ):
        self.image_url = image_url
        self.async_ = async_

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        if self.async_ is not None:
            result['Async'] = self.async_
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        if m.get('Async') is not None:
            self.async_ = m.get('Async')
        return self


class SegmentHDCommonImageAdvanceRequest(TeaModel):
    def __init__(
        self,
        image_url_object: BinaryIO = None,
        async_: bool = None,
    ):
        self.image_url_object = image_url_object
        self.async_ = async_

    def validate(self):
        self.validate_required(self.image_url_object, 'image_url_object')

    def to_map(self):
        result = dict()
        if self.image_url_object is not None:
            result['ImageUrlObject'] = self.image_url_object
        if self.async_ is not None:
            result['Async'] = self.async_
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageUrlObject') is not None:
            self.image_url_object = m.get('ImageUrlObject')
        if m.get('Async') is not None:
            self.async_ = m.get('Async')
        return self


class SegmentHDCommonImageResponseBodyData(TeaModel):
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


class SegmentHDCommonImageResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: SegmentHDCommonImageResponseBodyData = None,
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
            temp_model = SegmentHDCommonImageResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class SegmentHDCommonImageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SegmentHDCommonImageResponseBody = None,
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
            temp_model = SegmentHDCommonImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SegmentHDSkyRequest(TeaModel):
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


class SegmentHDSkyAdvanceRequest(TeaModel):
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


class SegmentHDSkyResponseBodyData(TeaModel):
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


class SegmentHDSkyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: SegmentHDSkyResponseBodyData = None,
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
            temp_model = SegmentHDSkyResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class SegmentHDSkyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SegmentHDSkyResponseBody = None,
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
            temp_model = SegmentHDSkyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SegmentHeadRequest(TeaModel):
    def __init__(
        self,
        image_url: str = None,
        return_form: str = None,
    ):
        self.image_url = image_url
        self.return_form = return_form

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        if self.return_form is not None:
            result['ReturnForm'] = self.return_form
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        if m.get('ReturnForm') is not None:
            self.return_form = m.get('ReturnForm')
        return self


class SegmentHeadAdvanceRequest(TeaModel):
    def __init__(
        self,
        image_urlobject: BinaryIO = None,
        return_form: str = None,
    ):
        self.image_urlobject = image_urlobject
        self.return_form = return_form

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        result = dict()
        if self.image_urlobject is not None:
            result['ImageURLObject'] = self.image_urlobject
        if self.return_form is not None:
            result['ReturnForm'] = self.return_form
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURLObject') is not None:
            self.image_urlobject = m.get('ImageURLObject')
        if m.get('ReturnForm') is not None:
            self.return_form = m.get('ReturnForm')
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


class SegmentLogoRequest(TeaModel):
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


class SegmentLogoAdvanceRequest(TeaModel):
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


class SegmentLogoResponseBodyData(TeaModel):
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


class SegmentLogoResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: SegmentLogoResponseBodyData = None,
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
            temp_model = SegmentLogoResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class SegmentLogoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SegmentLogoResponseBody = None,
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
            temp_model = SegmentLogoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SegmentSceneRequest(TeaModel):
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


class SegmentSceneAdvanceRequest(TeaModel):
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


class SegmentSceneResponseBodyData(TeaModel):
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


class SegmentSceneResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: SegmentSceneResponseBodyData = None,
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
            temp_model = SegmentSceneResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class SegmentSceneResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SegmentSceneResponseBody = None,
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
            temp_model = SegmentSceneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SegmentSkinRequest(TeaModel):
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
            result['URL'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('URL') is not None:
            self.url = m.get('URL')
        return self


class SegmentSkinAdvanceRequest(TeaModel):
    def __init__(
        self,
        urlobject: BinaryIO = None,
    ):
        self.urlobject = urlobject

    def validate(self):
        self.validate_required(self.urlobject, 'urlobject')

    def to_map(self):
        result = dict()
        if self.urlobject is not None:
            result['URLObject'] = self.urlobject
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('URLObject') is not None:
            self.urlobject = m.get('URLObject')
        return self


class SegmentSkinResponseBodyData(TeaModel):
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
            result['URL'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('URL') is not None:
            self.url = m.get('URL')
        return self


class SegmentSkinResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: SegmentSkinResponseBodyData = None,
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
            temp_model = SegmentSkinResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class SegmentSkinResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SegmentSkinResponseBody = None,
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
            temp_model = SegmentSkinResponseBody()
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


class SegmentSkyAdvanceRequest(TeaModel):
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


class SegmentVehicleAdvanceRequest(TeaModel):
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


