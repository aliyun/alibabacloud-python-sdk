# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import BinaryIO, Dict, List


class AssessCompositionRequest(TeaModel):
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


class AssessCompositionAdvanceRequest(TeaModel):
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


class AssessCompositionResponseBodyData(TeaModel):
    def __init__(
        self,
        score: float = None,
    ):
        self.score = score

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        data: AssessCompositionResponseBodyData = None,
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
            temp_model = AssessCompositionResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AssessCompositionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AssessCompositionResponseBody = None,
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


class AssessExposureAdvanceRequest(TeaModel):
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


class AssessExposureResponseBodyData(TeaModel):
    def __init__(
        self,
        exposure: float = None,
    ):
        self.exposure = exposure

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        data: AssessExposureResponseBodyData = None,
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
            temp_model = AssessExposureResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AssessExposureResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AssessExposureResponseBody = None,
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


class AssessSharpnessAdvanceRequest(TeaModel):
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


class AssessSharpnessResponseBodyData(TeaModel):
    def __init__(
        self,
        sharpness: float = None,
    ):
        self.sharpness = sharpness

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        data: AssessSharpnessResponseBodyData = None,
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
            temp_model = AssessSharpnessResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AssessSharpnessResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AssessSharpnessResponseBody = None,
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
            temp_model = AssessSharpnessResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ChangeImageSizeRequest(TeaModel):
    def __init__(
        self,
        height: int = None,
        url: str = None,
        width: int = None,
    ):
        self.height = height
        self.url = url
        self.width = width

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.height is not None:
            result['Height'] = self.height
        if self.url is not None:
            result['Url'] = self.url
        if self.width is not None:
            result['Width'] = self.width
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        return self


class ChangeImageSizeAdvanceRequest(TeaModel):
    def __init__(
        self,
        height: int = None,
        url_object: BinaryIO = None,
        width: int = None,
    ):
        self.height = height
        self.url_object = url_object
        self.width = width

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.height is not None:
            result['Height'] = self.height
        if self.url_object is not None:
            result['Url'] = self.url_object
        if self.width is not None:
            result['Width'] = self.width
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Url') is not None:
            self.url_object = m.get('Url')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        return self


class ChangeImageSizeResponseBodyDataRetainLocation(TeaModel):
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


class ChangeImageSizeResponseBodyData(TeaModel):
    def __init__(
        self,
        retain_location: ChangeImageSizeResponseBodyDataRetainLocation = None,
        url: str = None,
    ):
        self.retain_location = retain_location
        self.url = url

    def validate(self):
        if self.retain_location:
            self.retain_location.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.retain_location is not None:
            result['RetainLocation'] = self.retain_location.to_map()
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RetainLocation') is not None:
            temp_model = ChangeImageSizeResponseBodyDataRetainLocation()
            self.retain_location = temp_model.from_map(m['RetainLocation'])
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class ChangeImageSizeResponseBody(TeaModel):
    def __init__(
        self,
        data: ChangeImageSizeResponseBodyData = None,
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
            temp_model = ChangeImageSizeResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ChangeImageSizeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ChangeImageSizeResponseBody = None,
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
            temp_model = ChangeImageSizeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ColorizeImageRequest(TeaModel):
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


class ColorizeImageAdvanceRequest(TeaModel):
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


class ColorizeImageResponseBodyData(TeaModel):
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


class ColorizeImageResponseBody(TeaModel):
    def __init__(
        self,
        data: ColorizeImageResponseBodyData = None,
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
            temp_model = ColorizeImageResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ColorizeImageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ColorizeImageResponseBody = None,
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
            temp_model = ColorizeImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnhanceImageColorRequest(TeaModel):
    def __init__(
        self,
        image_url: str = None,
        mode: str = None,
        output_format: str = None,
    ):
        self.image_url = image_url
        self.mode = mode
        self.output_format = output_format

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.output_format is not None:
            result['OutputFormat'] = self.output_format
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('OutputFormat') is not None:
            self.output_format = m.get('OutputFormat')
        return self


class EnhanceImageColorAdvanceRequest(TeaModel):
    def __init__(
        self,
        image_urlobject: BinaryIO = None,
        mode: str = None,
        output_format: str = None,
    ):
        self.image_urlobject = image_urlobject
        self.mode = mode
        self.output_format = output_format

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_urlobject is not None:
            result['ImageURL'] = self.image_urlobject
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.output_format is not None:
            result['OutputFormat'] = self.output_format
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_urlobject = m.get('ImageURL')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('OutputFormat') is not None:
            self.output_format = m.get('OutputFormat')
        return self


class EnhanceImageColorResponseBodyData(TeaModel):
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


class EnhanceImageColorResponseBody(TeaModel):
    def __init__(
        self,
        data: EnhanceImageColorResponseBodyData = None,
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
            temp_model = EnhanceImageColorResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class EnhanceImageColorResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: EnhanceImageColorResponseBody = None,
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
            temp_model = EnhanceImageColorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ErasePersonRequest(TeaModel):
    def __init__(
        self,
        image_url: str = None,
        user_mask: str = None,
    ):
        self.image_url = image_url
        self.user_mask = user_mask

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        if self.user_mask is not None:
            result['UserMask'] = self.user_mask
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        if m.get('UserMask') is not None:
            self.user_mask = m.get('UserMask')
        return self


class ErasePersonAdvanceRequest(TeaModel):
    def __init__(
        self,
        image_urlobject: BinaryIO = None,
        user_mask_object: BinaryIO = None,
    ):
        self.image_urlobject = image_urlobject
        self.user_mask_object = user_mask_object

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_urlobject is not None:
            result['ImageURL'] = self.image_urlobject
        if self.user_mask_object is not None:
            result['UserMask'] = self.user_mask_object
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_urlobject = m.get('ImageURL')
        if m.get('UserMask') is not None:
            self.user_mask_object = m.get('UserMask')
        return self


class ErasePersonResponseBodyData(TeaModel):
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
            result['ImageUrl'] = self.image_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        return self


class ErasePersonResponseBody(TeaModel):
    def __init__(
        self,
        data: ErasePersonResponseBodyData = None,
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
            temp_model = ErasePersonResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ErasePersonResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ErasePersonResponseBody = None,
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
            temp_model = ErasePersonResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExtendImageStyleRequest(TeaModel):
    def __init__(
        self,
        major_url: str = None,
        style_url: str = None,
    ):
        self.major_url = major_url
        self.style_url = style_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.major_url is not None:
            result['MajorUrl'] = self.major_url
        if self.style_url is not None:
            result['StyleUrl'] = self.style_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MajorUrl') is not None:
            self.major_url = m.get('MajorUrl')
        if m.get('StyleUrl') is not None:
            self.style_url = m.get('StyleUrl')
        return self


class ExtendImageStyleAdvanceRequest(TeaModel):
    def __init__(
        self,
        major_url_object: BinaryIO = None,
        style_url_object: BinaryIO = None,
    ):
        self.major_url_object = major_url_object
        self.style_url_object = style_url_object

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.major_url_object is not None:
            result['MajorUrl'] = self.major_url_object
        if self.style_url_object is not None:
            result['StyleUrl'] = self.style_url_object
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MajorUrl') is not None:
            self.major_url_object = m.get('MajorUrl')
        if m.get('StyleUrl') is not None:
            self.style_url_object = m.get('StyleUrl')
        return self


class ExtendImageStyleResponseBodyData(TeaModel):
    def __init__(
        self,
        major_url: str = None,
        url: str = None,
    ):
        self.major_url = major_url
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.major_url is not None:
            result['MajorUrl'] = self.major_url
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MajorUrl') is not None:
            self.major_url = m.get('MajorUrl')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class ExtendImageStyleResponseBody(TeaModel):
    def __init__(
        self,
        data: ExtendImageStyleResponseBodyData = None,
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
            temp_model = ExtendImageStyleResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ExtendImageStyleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ExtendImageStyleResponseBody = None,
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
            temp_model = ExtendImageStyleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GenerateCartoonizedImageRequest(TeaModel):
    def __init__(
        self,
        image_type: str = None,
        image_url: str = None,
        index: str = None,
    ):
        self.image_type = image_type
        self.image_url = image_url
        self.index = index

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_type is not None:
            result['ImageType'] = self.image_type
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        if self.index is not None:
            result['Index'] = self.index
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageType') is not None:
            self.image_type = m.get('ImageType')
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        if m.get('Index') is not None:
            self.index = m.get('Index')
        return self


class GenerateCartoonizedImageAdvanceRequest(TeaModel):
    def __init__(
        self,
        image_type: str = None,
        image_url_object: BinaryIO = None,
        index: str = None,
    ):
        self.image_type = image_type
        self.image_url_object = image_url_object
        self.index = index

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_type is not None:
            result['ImageType'] = self.image_type
        if self.image_url_object is not None:
            result['ImageUrl'] = self.image_url_object
        if self.index is not None:
            result['Index'] = self.index
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageType') is not None:
            self.image_type = m.get('ImageType')
        if m.get('ImageUrl') is not None:
            self.image_url_object = m.get('ImageUrl')
        if m.get('Index') is not None:
            self.index = m.get('Index')
        return self


class GenerateCartoonizedImageResponseBodyData(TeaModel):
    def __init__(
        self,
        result_url: str = None,
    ):
        self.result_url = result_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result_url is not None:
            result['ResultUrl'] = self.result_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResultUrl') is not None:
            self.result_url = m.get('ResultUrl')
        return self


class GenerateCartoonizedImageResponseBody(TeaModel):
    def __init__(
        self,
        data: GenerateCartoonizedImageResponseBodyData = None,
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
            temp_model = GenerateCartoonizedImageResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GenerateCartoonizedImageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GenerateCartoonizedImageResponseBody = None,
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
            temp_model = GenerateCartoonizedImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GenerateDynamicImageRequest(TeaModel):
    def __init__(
        self,
        operation: str = None,
        url: str = None,
    ):
        self.operation = operation
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.operation is not None:
            result['Operation'] = self.operation
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Operation') is not None:
            self.operation = m.get('Operation')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class GenerateDynamicImageAdvanceRequest(TeaModel):
    def __init__(
        self,
        operation: str = None,
        url_object: BinaryIO = None,
    ):
        self.operation = operation
        self.url_object = url_object

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.operation is not None:
            result['Operation'] = self.operation
        if self.url_object is not None:
            result['Url'] = self.url_object
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Operation') is not None:
            self.operation = m.get('Operation')
        if m.get('Url') is not None:
            self.url_object = m.get('Url')
        return self


class GenerateDynamicImageResponseBodyData(TeaModel):
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


class GenerateDynamicImageResponseBody(TeaModel):
    def __init__(
        self,
        data: GenerateDynamicImageResponseBodyData = None,
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
            temp_model = GenerateDynamicImageResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GenerateDynamicImageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GenerateDynamicImageResponseBody = None,
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
            temp_model = GenerateDynamicImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GenerateImageWithTextRequest(TeaModel):
    def __init__(
        self,
        number: int = None,
        resolution: str = None,
        text: str = None,
    ):
        self.number = number
        self.resolution = resolution
        self.text = text

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.number is not None:
            result['Number'] = self.number
        if self.resolution is not None:
            result['Resolution'] = self.resolution
        if self.text is not None:
            result['Text'] = self.text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Number') is not None:
            self.number = m.get('Number')
        if m.get('Resolution') is not None:
            self.resolution = m.get('Resolution')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        return self


class GenerateImageWithTextResponseBodyData(TeaModel):
    def __init__(
        self,
        image_urls: List[str] = None,
    ):
        self.image_urls = image_urls

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_urls is not None:
            result['ImageUrls'] = self.image_urls
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageUrls') is not None:
            self.image_urls = m.get('ImageUrls')
        return self


class GenerateImageWithTextResponseBody(TeaModel):
    def __init__(
        self,
        data: GenerateImageWithTextResponseBodyData = None,
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
            temp_model = GenerateImageWithTextResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GenerateImageWithTextResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GenerateImageWithTextResponseBody = None,
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
            temp_model = GenerateImageWithTextResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GenerateImageWithTextAndImageRequest(TeaModel):
    def __init__(
        self,
        aspect_ratio_mode: str = None,
        number: int = None,
        ref_image_url: str = None,
        resolution: str = None,
        similarity: float = None,
        text: str = None,
    ):
        self.aspect_ratio_mode = aspect_ratio_mode
        self.number = number
        self.ref_image_url = ref_image_url
        self.resolution = resolution
        self.similarity = similarity
        self.text = text

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aspect_ratio_mode is not None:
            result['AspectRatioMode'] = self.aspect_ratio_mode
        if self.number is not None:
            result['Number'] = self.number
        if self.ref_image_url is not None:
            result['RefImageUrl'] = self.ref_image_url
        if self.resolution is not None:
            result['Resolution'] = self.resolution
        if self.similarity is not None:
            result['Similarity'] = self.similarity
        if self.text is not None:
            result['Text'] = self.text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AspectRatioMode') is not None:
            self.aspect_ratio_mode = m.get('AspectRatioMode')
        if m.get('Number') is not None:
            self.number = m.get('Number')
        if m.get('RefImageUrl') is not None:
            self.ref_image_url = m.get('RefImageUrl')
        if m.get('Resolution') is not None:
            self.resolution = m.get('Resolution')
        if m.get('Similarity') is not None:
            self.similarity = m.get('Similarity')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        return self


class GenerateImageWithTextAndImageAdvanceRequest(TeaModel):
    def __init__(
        self,
        aspect_ratio_mode: str = None,
        number: int = None,
        ref_image_url_object: BinaryIO = None,
        resolution: str = None,
        similarity: float = None,
        text: str = None,
    ):
        self.aspect_ratio_mode = aspect_ratio_mode
        self.number = number
        self.ref_image_url_object = ref_image_url_object
        self.resolution = resolution
        self.similarity = similarity
        self.text = text

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aspect_ratio_mode is not None:
            result['AspectRatioMode'] = self.aspect_ratio_mode
        if self.number is not None:
            result['Number'] = self.number
        if self.ref_image_url_object is not None:
            result['RefImageUrl'] = self.ref_image_url_object
        if self.resolution is not None:
            result['Resolution'] = self.resolution
        if self.similarity is not None:
            result['Similarity'] = self.similarity
        if self.text is not None:
            result['Text'] = self.text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AspectRatioMode') is not None:
            self.aspect_ratio_mode = m.get('AspectRatioMode')
        if m.get('Number') is not None:
            self.number = m.get('Number')
        if m.get('RefImageUrl') is not None:
            self.ref_image_url_object = m.get('RefImageUrl')
        if m.get('Resolution') is not None:
            self.resolution = m.get('Resolution')
        if m.get('Similarity') is not None:
            self.similarity = m.get('Similarity')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        return self


class GenerateImageWithTextAndImageResponseBodyData(TeaModel):
    def __init__(
        self,
        image_urls: List[str] = None,
    ):
        self.image_urls = image_urls

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_urls is not None:
            result['ImageUrls'] = self.image_urls
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageUrls') is not None:
            self.image_urls = m.get('ImageUrls')
        return self


class GenerateImageWithTextAndImageResponseBody(TeaModel):
    def __init__(
        self,
        data: GenerateImageWithTextAndImageResponseBodyData = None,
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
            temp_model = GenerateImageWithTextAndImageResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GenerateImageWithTextAndImageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GenerateImageWithTextAndImageResponseBody = None,
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
            temp_model = GenerateImageWithTextAndImageResponseBody()
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


class ImageBlindCharacterWatermarkRequest(TeaModel):
    def __init__(
        self,
        function_type: str = None,
        origin_image_url: str = None,
        output_file_type: str = None,
        quality_factor: int = None,
        text: str = None,
        watermark_image_url: str = None,
    ):
        self.function_type = function_type
        self.origin_image_url = origin_image_url
        self.output_file_type = output_file_type
        self.quality_factor = quality_factor
        self.text = text
        self.watermark_image_url = watermark_image_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.function_type is not None:
            result['FunctionType'] = self.function_type
        if self.origin_image_url is not None:
            result['OriginImageURL'] = self.origin_image_url
        if self.output_file_type is not None:
            result['OutputFileType'] = self.output_file_type
        if self.quality_factor is not None:
            result['QualityFactor'] = self.quality_factor
        if self.text is not None:
            result['Text'] = self.text
        if self.watermark_image_url is not None:
            result['WatermarkImageURL'] = self.watermark_image_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FunctionType') is not None:
            self.function_type = m.get('FunctionType')
        if m.get('OriginImageURL') is not None:
            self.origin_image_url = m.get('OriginImageURL')
        if m.get('OutputFileType') is not None:
            self.output_file_type = m.get('OutputFileType')
        if m.get('QualityFactor') is not None:
            self.quality_factor = m.get('QualityFactor')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('WatermarkImageURL') is not None:
            self.watermark_image_url = m.get('WatermarkImageURL')
        return self


class ImageBlindCharacterWatermarkAdvanceRequest(TeaModel):
    def __init__(
        self,
        function_type: str = None,
        origin_image_urlobject: BinaryIO = None,
        output_file_type: str = None,
        quality_factor: int = None,
        text: str = None,
        watermark_image_urlobject: BinaryIO = None,
    ):
        self.function_type = function_type
        self.origin_image_urlobject = origin_image_urlobject
        self.output_file_type = output_file_type
        self.quality_factor = quality_factor
        self.text = text
        self.watermark_image_urlobject = watermark_image_urlobject

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.function_type is not None:
            result['FunctionType'] = self.function_type
        if self.origin_image_urlobject is not None:
            result['OriginImageURL'] = self.origin_image_urlobject
        if self.output_file_type is not None:
            result['OutputFileType'] = self.output_file_type
        if self.quality_factor is not None:
            result['QualityFactor'] = self.quality_factor
        if self.text is not None:
            result['Text'] = self.text
        if self.watermark_image_urlobject is not None:
            result['WatermarkImageURL'] = self.watermark_image_urlobject
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FunctionType') is not None:
            self.function_type = m.get('FunctionType')
        if m.get('OriginImageURL') is not None:
            self.origin_image_urlobject = m.get('OriginImageURL')
        if m.get('OutputFileType') is not None:
            self.output_file_type = m.get('OutputFileType')
        if m.get('QualityFactor') is not None:
            self.quality_factor = m.get('QualityFactor')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('WatermarkImageURL') is not None:
            self.watermark_image_urlobject = m.get('WatermarkImageURL')
        return self


class ImageBlindCharacterWatermarkResponseBodyData(TeaModel):
    def __init__(
        self,
        text_image_url: str = None,
        watermark_image_url: str = None,
    ):
        self.text_image_url = text_image_url
        self.watermark_image_url = watermark_image_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.text_image_url is not None:
            result['TextImageURL'] = self.text_image_url
        if self.watermark_image_url is not None:
            result['WatermarkImageURL'] = self.watermark_image_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TextImageURL') is not None:
            self.text_image_url = m.get('TextImageURL')
        if m.get('WatermarkImageURL') is not None:
            self.watermark_image_url = m.get('WatermarkImageURL')
        return self


class ImageBlindCharacterWatermarkResponseBody(TeaModel):
    def __init__(
        self,
        data: ImageBlindCharacterWatermarkResponseBodyData = None,
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
            temp_model = ImageBlindCharacterWatermarkResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ImageBlindCharacterWatermarkResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ImageBlindCharacterWatermarkResponseBody = None,
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
            temp_model = ImageBlindCharacterWatermarkResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ImageBlindPicWatermarkRequest(TeaModel):
    def __init__(
        self,
        function_type: str = None,
        logo_url: str = None,
        origin_image_url: str = None,
        output_file_type: str = None,
        quality_factor: int = None,
        watermark_image_url: str = None,
    ):
        self.function_type = function_type
        self.logo_url = logo_url
        self.origin_image_url = origin_image_url
        self.output_file_type = output_file_type
        self.quality_factor = quality_factor
        self.watermark_image_url = watermark_image_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.function_type is not None:
            result['FunctionType'] = self.function_type
        if self.logo_url is not None:
            result['LogoURL'] = self.logo_url
        if self.origin_image_url is not None:
            result['OriginImageURL'] = self.origin_image_url
        if self.output_file_type is not None:
            result['OutputFileType'] = self.output_file_type
        if self.quality_factor is not None:
            result['QualityFactor'] = self.quality_factor
        if self.watermark_image_url is not None:
            result['WatermarkImageURL'] = self.watermark_image_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FunctionType') is not None:
            self.function_type = m.get('FunctionType')
        if m.get('LogoURL') is not None:
            self.logo_url = m.get('LogoURL')
        if m.get('OriginImageURL') is not None:
            self.origin_image_url = m.get('OriginImageURL')
        if m.get('OutputFileType') is not None:
            self.output_file_type = m.get('OutputFileType')
        if m.get('QualityFactor') is not None:
            self.quality_factor = m.get('QualityFactor')
        if m.get('WatermarkImageURL') is not None:
            self.watermark_image_url = m.get('WatermarkImageURL')
        return self


class ImageBlindPicWatermarkAdvanceRequest(TeaModel):
    def __init__(
        self,
        function_type: str = None,
        logo_urlobject: BinaryIO = None,
        origin_image_urlobject: BinaryIO = None,
        output_file_type: str = None,
        quality_factor: int = None,
        watermark_image_urlobject: BinaryIO = None,
    ):
        self.function_type = function_type
        self.logo_urlobject = logo_urlobject
        self.origin_image_urlobject = origin_image_urlobject
        self.output_file_type = output_file_type
        self.quality_factor = quality_factor
        self.watermark_image_urlobject = watermark_image_urlobject

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.function_type is not None:
            result['FunctionType'] = self.function_type
        if self.logo_urlobject is not None:
            result['LogoURL'] = self.logo_urlobject
        if self.origin_image_urlobject is not None:
            result['OriginImageURL'] = self.origin_image_urlobject
        if self.output_file_type is not None:
            result['OutputFileType'] = self.output_file_type
        if self.quality_factor is not None:
            result['QualityFactor'] = self.quality_factor
        if self.watermark_image_urlobject is not None:
            result['WatermarkImageURL'] = self.watermark_image_urlobject
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FunctionType') is not None:
            self.function_type = m.get('FunctionType')
        if m.get('LogoURL') is not None:
            self.logo_urlobject = m.get('LogoURL')
        if m.get('OriginImageURL') is not None:
            self.origin_image_urlobject = m.get('OriginImageURL')
        if m.get('OutputFileType') is not None:
            self.output_file_type = m.get('OutputFileType')
        if m.get('QualityFactor') is not None:
            self.quality_factor = m.get('QualityFactor')
        if m.get('WatermarkImageURL') is not None:
            self.watermark_image_urlobject = m.get('WatermarkImageURL')
        return self


class ImageBlindPicWatermarkResponseBodyData(TeaModel):
    def __init__(
        self,
        logo_url: str = None,
        watermark_image_url: str = None,
    ):
        self.logo_url = logo_url
        self.watermark_image_url = watermark_image_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.logo_url is not None:
            result['LogoURL'] = self.logo_url
        if self.watermark_image_url is not None:
            result['WatermarkImageURL'] = self.watermark_image_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LogoURL') is not None:
            self.logo_url = m.get('LogoURL')
        if m.get('WatermarkImageURL') is not None:
            self.watermark_image_url = m.get('WatermarkImageURL')
        return self


class ImageBlindPicWatermarkResponseBody(TeaModel):
    def __init__(
        self,
        data: ImageBlindPicWatermarkResponseBodyData = None,
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
            temp_model = ImageBlindPicWatermarkResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ImageBlindPicWatermarkResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ImageBlindPicWatermarkResponseBody = None,
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
            temp_model = ImageBlindPicWatermarkResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ImitatePhotoStyleRequest(TeaModel):
    def __init__(
        self,
        image_url: str = None,
        style_url: str = None,
    ):
        self.image_url = image_url
        self.style_url = style_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        if self.style_url is not None:
            result['StyleUrl'] = self.style_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        if m.get('StyleUrl') is not None:
            self.style_url = m.get('StyleUrl')
        return self


class ImitatePhotoStyleAdvanceRequest(TeaModel):
    def __init__(
        self,
        image_urlobject: BinaryIO = None,
        style_url_object: BinaryIO = None,
    ):
        self.image_urlobject = image_urlobject
        self.style_url_object = style_url_object

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_urlobject is not None:
            result['ImageURL'] = self.image_urlobject
        if self.style_url_object is not None:
            result['StyleUrl'] = self.style_url_object
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_urlobject = m.get('ImageURL')
        if m.get('StyleUrl') is not None:
            self.style_url_object = m.get('StyleUrl')
        return self


class ImitatePhotoStyleResponseBodyData(TeaModel):
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


class ImitatePhotoStyleResponseBody(TeaModel):
    def __init__(
        self,
        data: ImitatePhotoStyleResponseBodyData = None,
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
            temp_model = ImitatePhotoStyleResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ImitatePhotoStyleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ImitatePhotoStyleResponseBody = None,
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
            temp_model = ImitatePhotoStyleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class IntelligentCompositionRequest(TeaModel):
    def __init__(
        self,
        image_url: str = None,
        num_boxes: int = None,
    ):
        self.image_url = image_url
        self.num_boxes = num_boxes

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        if self.num_boxes is not None:
            result['NumBoxes'] = self.num_boxes
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        if m.get('NumBoxes') is not None:
            self.num_boxes = m.get('NumBoxes')
        return self


class IntelligentCompositionAdvanceRequest(TeaModel):
    def __init__(
        self,
        image_urlobject: BinaryIO = None,
        num_boxes: int = None,
    ):
        self.image_urlobject = image_urlobject
        self.num_boxes = num_boxes

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_urlobject is not None:
            result['ImageURL'] = self.image_urlobject
        if self.num_boxes is not None:
            result['NumBoxes'] = self.num_boxes
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_urlobject = m.get('ImageURL')
        if m.get('NumBoxes') is not None:
            self.num_boxes = m.get('NumBoxes')
        return self


class IntelligentCompositionResponseBodyDataElements(TeaModel):
    def __init__(
        self,
        max_x: int = None,
        max_y: int = None,
        min_x: int = None,
        min_y: int = None,
        score: float = None,
    ):
        self.max_x = max_x
        self.max_y = max_y
        self.min_x = min_x
        self.min_y = min_y
        self.score = score

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_x is not None:
            result['MaxX'] = self.max_x
        if self.max_y is not None:
            result['MaxY'] = self.max_y
        if self.min_x is not None:
            result['MinX'] = self.min_x
        if self.min_y is not None:
            result['MinY'] = self.min_y
        if self.score is not None:
            result['Score'] = self.score
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxX') is not None:
            self.max_x = m.get('MaxX')
        if m.get('MaxY') is not None:
            self.max_y = m.get('MaxY')
        if m.get('MinX') is not None:
            self.min_x = m.get('MinX')
        if m.get('MinY') is not None:
            self.min_y = m.get('MinY')
        if m.get('Score') is not None:
            self.score = m.get('Score')
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
                temp_model = IntelligentCompositionResponseBodyDataElements()
                self.elements.append(temp_model.from_map(k))
        return self


class IntelligentCompositionResponseBody(TeaModel):
    def __init__(
        self,
        data: IntelligentCompositionResponseBodyData = None,
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
            temp_model = IntelligentCompositionResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class IntelligentCompositionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: IntelligentCompositionResponseBody = None,
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
            temp_model = IntelligentCompositionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class MakeSuperResolutionImageRequest(TeaModel):
    def __init__(
        self,
        mode: str = None,
        output_format: str = None,
        output_quality: int = None,
        upscale_factor: int = None,
        url: str = None,
    ):
        self.mode = mode
        self.output_format = output_format
        self.output_quality = output_quality
        self.upscale_factor = upscale_factor
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.output_format is not None:
            result['OutputFormat'] = self.output_format
        if self.output_quality is not None:
            result['OutputQuality'] = self.output_quality
        if self.upscale_factor is not None:
            result['UpscaleFactor'] = self.upscale_factor
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('OutputFormat') is not None:
            self.output_format = m.get('OutputFormat')
        if m.get('OutputQuality') is not None:
            self.output_quality = m.get('OutputQuality')
        if m.get('UpscaleFactor') is not None:
            self.upscale_factor = m.get('UpscaleFactor')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class MakeSuperResolutionImageAdvanceRequest(TeaModel):
    def __init__(
        self,
        mode: str = None,
        output_format: str = None,
        output_quality: int = None,
        upscale_factor: int = None,
        url_object: BinaryIO = None,
    ):
        self.mode = mode
        self.output_format = output_format
        self.output_quality = output_quality
        self.upscale_factor = upscale_factor
        self.url_object = url_object

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.output_format is not None:
            result['OutputFormat'] = self.output_format
        if self.output_quality is not None:
            result['OutputQuality'] = self.output_quality
        if self.upscale_factor is not None:
            result['UpscaleFactor'] = self.upscale_factor
        if self.url_object is not None:
            result['Url'] = self.url_object
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('OutputFormat') is not None:
            self.output_format = m.get('OutputFormat')
        if m.get('OutputQuality') is not None:
            self.output_quality = m.get('OutputQuality')
        if m.get('UpscaleFactor') is not None:
            self.upscale_factor = m.get('UpscaleFactor')
        if m.get('Url') is not None:
            self.url_object = m.get('Url')
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


class MakeSuperResolutionImageResponseBody(TeaModel):
    def __init__(
        self,
        data: MakeSuperResolutionImageResponseBodyData = None,
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
            temp_model = MakeSuperResolutionImageResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class MakeSuperResolutionImageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: MakeSuperResolutionImageResponseBody = None,
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
            temp_model = MakeSuperResolutionImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecolorHDImageRequestColorTemplate(TeaModel):
    def __init__(
        self,
        color: str = None,
    ):
        self.color = color

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.color is not None:
            result['Color'] = self.color
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Color') is not None:
            self.color = m.get('Color')
        return self


class RecolorHDImageRequest(TeaModel):
    def __init__(
        self,
        color_count: int = None,
        color_template: List[RecolorHDImageRequestColorTemplate] = None,
        degree: str = None,
        mode: str = None,
        ref_url: str = None,
        url: str = None,
    ):
        self.color_count = color_count
        # 1
        self.color_template = color_template
        self.degree = degree
        self.mode = mode
        self.ref_url = ref_url
        self.url = url

    def validate(self):
        if self.color_template:
            for k in self.color_template:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.color_count is not None:
            result['ColorCount'] = self.color_count
        result['ColorTemplate'] = []
        if self.color_template is not None:
            for k in self.color_template:
                result['ColorTemplate'].append(k.to_map() if k else None)
        if self.degree is not None:
            result['Degree'] = self.degree
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.ref_url is not None:
            result['RefUrl'] = self.ref_url
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ColorCount') is not None:
            self.color_count = m.get('ColorCount')
        self.color_template = []
        if m.get('ColorTemplate') is not None:
            for k in m.get('ColorTemplate'):
                temp_model = RecolorHDImageRequestColorTemplate()
                self.color_template.append(temp_model.from_map(k))
        if m.get('Degree') is not None:
            self.degree = m.get('Degree')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('RefUrl') is not None:
            self.ref_url = m.get('RefUrl')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class RecolorHDImageAdvanceRequestColorTemplate(TeaModel):
    def __init__(
        self,
        color: str = None,
    ):
        self.color = color

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.color is not None:
            result['Color'] = self.color
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Color') is not None:
            self.color = m.get('Color')
        return self


class RecolorHDImageAdvanceRequest(TeaModel):
    def __init__(
        self,
        color_count: int = None,
        color_template: List[RecolorHDImageAdvanceRequestColorTemplate] = None,
        degree: str = None,
        mode: str = None,
        ref_url_object: BinaryIO = None,
        url_object: BinaryIO = None,
    ):
        self.color_count = color_count
        # 1
        self.color_template = color_template
        self.degree = degree
        self.mode = mode
        self.ref_url_object = ref_url_object
        self.url_object = url_object

    def validate(self):
        if self.color_template:
            for k in self.color_template:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.color_count is not None:
            result['ColorCount'] = self.color_count
        result['ColorTemplate'] = []
        if self.color_template is not None:
            for k in self.color_template:
                result['ColorTemplate'].append(k.to_map() if k else None)
        if self.degree is not None:
            result['Degree'] = self.degree
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.ref_url_object is not None:
            result['RefUrl'] = self.ref_url_object
        if self.url_object is not None:
            result['Url'] = self.url_object
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ColorCount') is not None:
            self.color_count = m.get('ColorCount')
        self.color_template = []
        if m.get('ColorTemplate') is not None:
            for k in m.get('ColorTemplate'):
                temp_model = RecolorHDImageAdvanceRequestColorTemplate()
                self.color_template.append(temp_model.from_map(k))
        if m.get('Degree') is not None:
            self.degree = m.get('Degree')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('RefUrl') is not None:
            self.ref_url_object = m.get('RefUrl')
        if m.get('Url') is not None:
            self.url_object = m.get('Url')
        return self


class RecolorHDImageResponseBodyData(TeaModel):
    def __init__(
        self,
        image_list: List[str] = None,
    ):
        # 1
        self.image_list = image_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_list is not None:
            result['ImageList'] = self.image_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageList') is not None:
            self.image_list = m.get('ImageList')
        return self


class RecolorHDImageResponseBody(TeaModel):
    def __init__(
        self,
        data: RecolorHDImageResponseBodyData = None,
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
            temp_model = RecolorHDImageResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RecolorHDImageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RecolorHDImageResponseBody = None,
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
            temp_model = RecolorHDImageResponseBody()
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        color_count: int = None,
        color_template: List[RecolorImageRequestColorTemplate] = None,
        mode: str = None,
        ref_url: str = None,
        url: str = None,
    ):
        self.color_count = color_count
        # 1
        self.color_template = color_template
        self.mode = mode
        self.ref_url = ref_url
        self.url = url

    def validate(self):
        if self.color_template:
            for k in self.color_template:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.color_count is not None:
            result['ColorCount'] = self.color_count
        result['ColorTemplate'] = []
        if self.color_template is not None:
            for k in self.color_template:
                result['ColorTemplate'].append(k.to_map() if k else None)
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.ref_url is not None:
            result['RefUrl'] = self.ref_url
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ColorCount') is not None:
            self.color_count = m.get('ColorCount')
        self.color_template = []
        if m.get('ColorTemplate') is not None:
            for k in m.get('ColorTemplate'):
                temp_model = RecolorImageRequestColorTemplate()
                self.color_template.append(temp_model.from_map(k))
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('RefUrl') is not None:
            self.ref_url = m.get('RefUrl')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class RecolorImageAdvanceRequestColorTemplate(TeaModel):
    def __init__(
        self,
        color: str = None,
    ):
        self.color = color

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.color is not None:
            result['Color'] = self.color
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Color') is not None:
            self.color = m.get('Color')
        return self


class RecolorImageAdvanceRequest(TeaModel):
    def __init__(
        self,
        color_count: int = None,
        color_template: List[RecolorImageAdvanceRequestColorTemplate] = None,
        mode: str = None,
        ref_url_object: BinaryIO = None,
        url_object: BinaryIO = None,
    ):
        self.color_count = color_count
        # 1
        self.color_template = color_template
        self.mode = mode
        self.ref_url_object = ref_url_object
        self.url_object = url_object

    def validate(self):
        if self.color_template:
            for k in self.color_template:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.color_count is not None:
            result['ColorCount'] = self.color_count
        result['ColorTemplate'] = []
        if self.color_template is not None:
            for k in self.color_template:
                result['ColorTemplate'].append(k.to_map() if k else None)
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.ref_url_object is not None:
            result['RefUrl'] = self.ref_url_object
        if self.url_object is not None:
            result['Url'] = self.url_object
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ColorCount') is not None:
            self.color_count = m.get('ColorCount')
        self.color_template = []
        if m.get('ColorTemplate') is not None:
            for k in m.get('ColorTemplate'):
                temp_model = RecolorImageAdvanceRequestColorTemplate()
                self.color_template.append(temp_model.from_map(k))
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('RefUrl') is not None:
            self.ref_url_object = m.get('RefUrl')
        if m.get('Url') is not None:
            self.url_object = m.get('Url')
        return self


class RecolorImageResponseBodyData(TeaModel):
    def __init__(
        self,
        image_list: List[str] = None,
    ):
        # 1
        self.image_list = image_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        data: RecolorImageResponseBodyData = None,
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
            temp_model = RecolorImageResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RecolorImageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RecolorImageResponseBody = None,
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
            temp_model = RecolorImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveImageSubtitlesRequest(TeaModel):
    def __init__(
        self,
        bh: float = None,
        bw: float = None,
        bx: float = None,
        by: float = None,
        image_url: str = None,
    ):
        self.bh = bh
        self.bw = bw
        self.bx = bx
        self.by = by
        self.image_url = image_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bh is not None:
            result['BH'] = self.bh
        if self.bw is not None:
            result['BW'] = self.bw
        if self.bx is not None:
            result['BX'] = self.bx
        if self.by is not None:
            result['BY'] = self.by
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BH') is not None:
            self.bh = m.get('BH')
        if m.get('BW') is not None:
            self.bw = m.get('BW')
        if m.get('BX') is not None:
            self.bx = m.get('BX')
        if m.get('BY') is not None:
            self.by = m.get('BY')
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        return self


class RemoveImageSubtitlesAdvanceRequest(TeaModel):
    def __init__(
        self,
        bh: float = None,
        bw: float = None,
        bx: float = None,
        by: float = None,
        image_urlobject: BinaryIO = None,
    ):
        self.bh = bh
        self.bw = bw
        self.bx = bx
        self.by = by
        self.image_urlobject = image_urlobject

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bh is not None:
            result['BH'] = self.bh
        if self.bw is not None:
            result['BW'] = self.bw
        if self.bx is not None:
            result['BX'] = self.bx
        if self.by is not None:
            result['BY'] = self.by
        if self.image_urlobject is not None:
            result['ImageURL'] = self.image_urlobject
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BH') is not None:
            self.bh = m.get('BH')
        if m.get('BW') is not None:
            self.bw = m.get('BW')
        if m.get('BX') is not None:
            self.bx = m.get('BX')
        if m.get('BY') is not None:
            self.by = m.get('BY')
        if m.get('ImageURL') is not None:
            self.image_urlobject = m.get('ImageURL')
        return self


class RemoveImageSubtitlesResponseBodyData(TeaModel):
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


class RemoveImageSubtitlesResponseBody(TeaModel):
    def __init__(
        self,
        data: RemoveImageSubtitlesResponseBodyData = None,
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
            temp_model = RemoveImageSubtitlesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RemoveImageSubtitlesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RemoveImageSubtitlesResponseBody = None,
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
            temp_model = RemoveImageSubtitlesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveImageWatermarkRequest(TeaModel):
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


class RemoveImageWatermarkAdvanceRequest(TeaModel):
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


class RemoveImageWatermarkResponseBodyData(TeaModel):
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


class RemoveImageWatermarkResponseBody(TeaModel):
    def __init__(
        self,
        data: RemoveImageWatermarkResponseBodyData = None,
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
            temp_model = RemoveImageWatermarkResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RemoveImageWatermarkResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RemoveImageWatermarkResponseBody = None,
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
            temp_model = RemoveImageWatermarkResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


