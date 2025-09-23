# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, BinaryIO, Dict


class DetectObjectElement(TeaModel):
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


class DetectObjectFrame(TeaModel):
    def __init__(
        self,
        elements: List[DetectObjectElement] = None,
        time: int = None,
    ):
        self.elements = elements
        self.time = time

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
        if self.time is not None:
            result['Time'] = self.time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.elements = []
        if m.get('Elements') is not None:
            for k in m.get('Elements'):
                temp_model = DetectObjectElement()
                self.elements.append(temp_model.from_map(k))
        if m.get('Time') is not None:
            self.time = m.get('Time')
        return self


class DetectIPCObjectRequest(TeaModel):
    def __init__(
        self,
        image_url: str = None,
    ):
        # This parameter is required.
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


class DetectIPCObjectAdvanceRequest(TeaModel):
    def __init__(
        self,
        image_urlobject: BinaryIO = None,
    ):
        # This parameter is required.
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


class DetectIPCObjectResponseBodyDataElements(TeaModel):
    def __init__(
        self,
        box: List[int] = None,
        score: float = None,
        target_rate: float = None,
        type: str = None,
    ):
        self.box = box
        self.score = score
        self.target_rate = target_rate
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.box is not None:
            result['Box'] = self.box
        if self.score is not None:
            result['Score'] = self.score
        if self.target_rate is not None:
            result['TargetRate'] = self.target_rate
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Box') is not None:
            self.box = m.get('Box')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('TargetRate') is not None:
            self.target_rate = m.get('TargetRate')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DetectIPCObjectResponseBodyData(TeaModel):
    def __init__(
        self,
        elements: List[DetectIPCObjectResponseBodyDataElements] = None,
        height: int = None,
        width: int = None,
    ):
        self.elements = elements
        self.height = height
        self.width = width

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
        if self.height is not None:
            result['Height'] = self.height
        if self.width is not None:
            result['Width'] = self.width
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.elements = []
        if m.get('Elements') is not None:
            for k in m.get('Elements'):
                temp_model = DetectIPCObjectResponseBodyDataElements()
                self.elements.append(temp_model.from_map(k))
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        return self


class DetectIPCObjectResponseBody(TeaModel):
    def __init__(
        self,
        data: DetectIPCObjectResponseBodyData = None,
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
            temp_model = DetectIPCObjectResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DetectIPCObjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DetectIPCObjectResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DetectIPCObjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetectKitchenAnimalsRequest(TeaModel):
    def __init__(
        self,
        image_urla: str = None,
        image_urlb: str = None,
    ):
        # This parameter is required.
        self.image_urla = image_urla
        # This parameter is required.
        self.image_urlb = image_urlb

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_urla is not None:
            result['ImageURLA'] = self.image_urla
        if self.image_urlb is not None:
            result['ImageURLB'] = self.image_urlb
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURLA') is not None:
            self.image_urla = m.get('ImageURLA')
        if m.get('ImageURLB') is not None:
            self.image_urlb = m.get('ImageURLB')
        return self


class DetectKitchenAnimalsAdvanceRequest(TeaModel):
    def __init__(
        self,
        image_urlaobject: BinaryIO = None,
        image_urlbobject: BinaryIO = None,
    ):
        # This parameter is required.
        self.image_urlaobject = image_urlaobject
        # This parameter is required.
        self.image_urlbobject = image_urlbobject

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_urlaobject is not None:
            result['ImageURLA'] = self.image_urlaobject
        if self.image_urlbobject is not None:
            result['ImageURLB'] = self.image_urlbobject
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURLA') is not None:
            self.image_urlaobject = m.get('ImageURLA')
        if m.get('ImageURLB') is not None:
            self.image_urlbobject = m.get('ImageURLB')
        return self


class DetectKitchenAnimalsResponseBodyDataElementsRectangles(TeaModel):
    def __init__(
        self,
        height: int = None,
        left: int = None,
        top: int = None,
        width: int = None,
    ):
        self.height = height
        self.left = left
        self.top = top
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
        if self.left is not None:
            result['Left'] = self.left
        if self.top is not None:
            result['Top'] = self.top
        if self.width is not None:
            result['Width'] = self.width
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Left') is not None:
            self.left = m.get('Left')
        if m.get('Top') is not None:
            self.top = m.get('Top')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        return self


class DetectKitchenAnimalsResponseBodyDataElements(TeaModel):
    def __init__(
        self,
        rectangles: DetectKitchenAnimalsResponseBodyDataElementsRectangles = None,
        score: float = None,
        type: str = None,
    ):
        self.rectangles = rectangles
        self.score = score
        self.type = type

    def validate(self):
        if self.rectangles:
            self.rectangles.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rectangles is not None:
            result['Rectangles'] = self.rectangles.to_map()
        if self.score is not None:
            result['Score'] = self.score
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Rectangles') is not None:
            temp_model = DetectKitchenAnimalsResponseBodyDataElementsRectangles()
            self.rectangles = temp_model.from_map(m['Rectangles'])
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DetectKitchenAnimalsResponseBodyData(TeaModel):
    def __init__(
        self,
        elements: List[DetectKitchenAnimalsResponseBodyDataElements] = None,
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
                temp_model = DetectKitchenAnimalsResponseBodyDataElements()
                self.elements.append(temp_model.from_map(k))
        return self


class DetectKitchenAnimalsResponseBody(TeaModel):
    def __init__(
        self,
        data: DetectKitchenAnimalsResponseBodyData = None,
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
            temp_model = DetectKitchenAnimalsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DetectKitchenAnimalsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DetectKitchenAnimalsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DetectKitchenAnimalsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetectMainBodyRequest(TeaModel):
    def __init__(
        self,
        image_url: str = None,
    ):
        # This parameter is required.
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


class DetectMainBodyAdvanceRequest(TeaModel):
    def __init__(
        self,
        image_urlobject: BinaryIO = None,
    ):
        # This parameter is required.
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


class DetectMainBodyResponseBodyDataLocation(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        data: DetectMainBodyResponseBodyData = None,
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
            temp_model = DetectMainBodyResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DetectMainBodyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DetectMainBodyResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DetectMainBodyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetectObjectRequest(TeaModel):
    def __init__(
        self,
        image_url: str = None,
    ):
        # This parameter is required.
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


class DetectObjectAdvanceRequest(TeaModel):
    def __init__(
        self,
        image_urlobject: BinaryIO = None,
    ):
        # This parameter is required.
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


class DetectObjectResponseBodyDataElements(TeaModel):
    def __init__(
        self,
        boxes: List[int] = None,
        score: float = None,
        type: str = None,
    ):
        self.boxes = boxes
        self.score = score
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.boxes is not None:
            result['Boxes'] = self.boxes
        if self.score is not None:
            result['Score'] = self.score
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Boxes') is not None:
            self.boxes = m.get('Boxes')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DetectObjectResponseBodyData(TeaModel):
    def __init__(
        self,
        elements: List[DetectObjectResponseBodyDataElements] = None,
        height: int = None,
        width: int = None,
    ):
        self.elements = elements
        self.height = height
        self.width = width

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
        if self.height is not None:
            result['Height'] = self.height
        if self.width is not None:
            result['Width'] = self.width
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.elements = []
        if m.get('Elements') is not None:
            for k in m.get('Elements'):
                temp_model = DetectObjectResponseBodyDataElements()
                self.elements.append(temp_model.from_map(k))
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        return self


class DetectObjectResponseBody(TeaModel):
    def __init__(
        self,
        data: DetectObjectResponseBodyData = None,
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
            temp_model = DetectObjectResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DetectObjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DetectObjectResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DetectObjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetectVehicleICongestionRequestPreRegionIntersectFeatures(TeaModel):
    def __init__(
        self,
        features: List[str] = None,
    ):
        self.features = features

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.features is not None:
            result['Features'] = self.features
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Features') is not None:
            self.features = m.get('Features')
        return self


class DetectVehicleICongestionRequestRoadRegionsRoadRegionPoint(TeaModel):
    def __init__(
        self,
        x: int = None,
        y: int = None,
    ):
        # This parameter is required.
        self.x = x
        # This parameter is required.
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


class DetectVehicleICongestionRequestRoadRegionsRoadRegion(TeaModel):
    def __init__(
        self,
        point: DetectVehicleICongestionRequestRoadRegionsRoadRegionPoint = None,
    ):
        # This parameter is required.
        self.point = point

    def validate(self):
        if self.point:
            self.point.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.point is not None:
            result['Point'] = self.point.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Point') is not None:
            temp_model = DetectVehicleICongestionRequestRoadRegionsRoadRegionPoint()
            self.point = temp_model.from_map(m['Point'])
        return self


class DetectVehicleICongestionRequestRoadRegions(TeaModel):
    def __init__(
        self,
        road_region: List[DetectVehicleICongestionRequestRoadRegionsRoadRegion] = None,
    ):
        # This parameter is required.
        self.road_region = road_region

    def validate(self):
        if self.road_region:
            for k in self.road_region:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RoadRegion'] = []
        if self.road_region is not None:
            for k in self.road_region:
                result['RoadRegion'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.road_region = []
        if m.get('RoadRegion') is not None:
            for k in m.get('RoadRegion'):
                temp_model = DetectVehicleICongestionRequestRoadRegionsRoadRegion()
                self.road_region.append(temp_model.from_map(k))
        return self


class DetectVehicleICongestionRequest(TeaModel):
    def __init__(
        self,
        image_url: str = None,
        pre_region_intersect_features: List[DetectVehicleICongestionRequestPreRegionIntersectFeatures] = None,
        road_regions: List[DetectVehicleICongestionRequestRoadRegions] = None,
    ):
        # This parameter is required.
        self.image_url = image_url
        self.pre_region_intersect_features = pre_region_intersect_features
        # This parameter is required.
        self.road_regions = road_regions

    def validate(self):
        if self.pre_region_intersect_features:
            for k in self.pre_region_intersect_features:
                if k:
                    k.validate()
        if self.road_regions:
            for k in self.road_regions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        result['PreRegionIntersectFeatures'] = []
        if self.pre_region_intersect_features is not None:
            for k in self.pre_region_intersect_features:
                result['PreRegionIntersectFeatures'].append(k.to_map() if k else None)
        result['RoadRegions'] = []
        if self.road_regions is not None:
            for k in self.road_regions:
                result['RoadRegions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        self.pre_region_intersect_features = []
        if m.get('PreRegionIntersectFeatures') is not None:
            for k in m.get('PreRegionIntersectFeatures'):
                temp_model = DetectVehicleICongestionRequestPreRegionIntersectFeatures()
                self.pre_region_intersect_features.append(temp_model.from_map(k))
        self.road_regions = []
        if m.get('RoadRegions') is not None:
            for k in m.get('RoadRegions'):
                temp_model = DetectVehicleICongestionRequestRoadRegions()
                self.road_regions.append(temp_model.from_map(k))
        return self


class DetectVehicleICongestionAdvanceRequestPreRegionIntersectFeatures(TeaModel):
    def __init__(
        self,
        features: List[str] = None,
    ):
        self.features = features

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.features is not None:
            result['Features'] = self.features
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Features') is not None:
            self.features = m.get('Features')
        return self


class DetectVehicleICongestionAdvanceRequestRoadRegionsRoadRegionPoint(TeaModel):
    def __init__(
        self,
        x: int = None,
        y: int = None,
    ):
        # This parameter is required.
        self.x = x
        # This parameter is required.
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


class DetectVehicleICongestionAdvanceRequestRoadRegionsRoadRegion(TeaModel):
    def __init__(
        self,
        point: DetectVehicleICongestionAdvanceRequestRoadRegionsRoadRegionPoint = None,
    ):
        # This parameter is required.
        self.point = point

    def validate(self):
        if self.point:
            self.point.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.point is not None:
            result['Point'] = self.point.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Point') is not None:
            temp_model = DetectVehicleICongestionAdvanceRequestRoadRegionsRoadRegionPoint()
            self.point = temp_model.from_map(m['Point'])
        return self


class DetectVehicleICongestionAdvanceRequestRoadRegions(TeaModel):
    def __init__(
        self,
        road_region: List[DetectVehicleICongestionAdvanceRequestRoadRegionsRoadRegion] = None,
    ):
        # This parameter is required.
        self.road_region = road_region

    def validate(self):
        if self.road_region:
            for k in self.road_region:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RoadRegion'] = []
        if self.road_region is not None:
            for k in self.road_region:
                result['RoadRegion'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.road_region = []
        if m.get('RoadRegion') is not None:
            for k in m.get('RoadRegion'):
                temp_model = DetectVehicleICongestionAdvanceRequestRoadRegionsRoadRegion()
                self.road_region.append(temp_model.from_map(k))
        return self


class DetectVehicleICongestionAdvanceRequest(TeaModel):
    def __init__(
        self,
        image_urlobject: BinaryIO = None,
        pre_region_intersect_features: List[DetectVehicleICongestionAdvanceRequestPreRegionIntersectFeatures] = None,
        road_regions: List[DetectVehicleICongestionAdvanceRequestRoadRegions] = None,
    ):
        # This parameter is required.
        self.image_urlobject = image_urlobject
        self.pre_region_intersect_features = pre_region_intersect_features
        # This parameter is required.
        self.road_regions = road_regions

    def validate(self):
        if self.pre_region_intersect_features:
            for k in self.pre_region_intersect_features:
                if k:
                    k.validate()
        if self.road_regions:
            for k in self.road_regions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_urlobject is not None:
            result['ImageURL'] = self.image_urlobject
        result['PreRegionIntersectFeatures'] = []
        if self.pre_region_intersect_features is not None:
            for k in self.pre_region_intersect_features:
                result['PreRegionIntersectFeatures'].append(k.to_map() if k else None)
        result['RoadRegions'] = []
        if self.road_regions is not None:
            for k in self.road_regions:
                result['RoadRegions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_urlobject = m.get('ImageURL')
        self.pre_region_intersect_features = []
        if m.get('PreRegionIntersectFeatures') is not None:
            for k in m.get('PreRegionIntersectFeatures'):
                temp_model = DetectVehicleICongestionAdvanceRequestPreRegionIntersectFeatures()
                self.pre_region_intersect_features.append(temp_model.from_map(k))
        self.road_regions = []
        if m.get('RoadRegions') is not None:
            for k in m.get('RoadRegions'):
                temp_model = DetectVehicleICongestionAdvanceRequestRoadRegions()
                self.road_regions.append(temp_model.from_map(k))
        return self


class DetectVehicleICongestionShrinkRequest(TeaModel):
    def __init__(
        self,
        image_url: str = None,
        pre_region_intersect_features_shrink: str = None,
        road_regions_shrink: str = None,
    ):
        # This parameter is required.
        self.image_url = image_url
        self.pre_region_intersect_features_shrink = pre_region_intersect_features_shrink
        # This parameter is required.
        self.road_regions_shrink = road_regions_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        if self.pre_region_intersect_features_shrink is not None:
            result['PreRegionIntersectFeatures'] = self.pre_region_intersect_features_shrink
        if self.road_regions_shrink is not None:
            result['RoadRegions'] = self.road_regions_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        if m.get('PreRegionIntersectFeatures') is not None:
            self.pre_region_intersect_features_shrink = m.get('PreRegionIntersectFeatures')
        if m.get('RoadRegions') is not None:
            self.road_regions_shrink = m.get('RoadRegions')
        return self


class DetectVehicleICongestionResponseBodyDataElementsBoxes(TeaModel):
    def __init__(
        self,
        bottom: int = None,
        left: int = None,
        right: int = None,
        top: int = None,
    ):
        self.bottom = bottom
        self.left = left
        self.right = right
        self.top = top

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bottom is not None:
            result['Bottom'] = self.bottom
        if self.left is not None:
            result['Left'] = self.left
        if self.right is not None:
            result['Right'] = self.right
        if self.top is not None:
            result['Top'] = self.top
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bottom') is not None:
            self.bottom = m.get('Bottom')
        if m.get('Left') is not None:
            self.left = m.get('Left')
        if m.get('Right') is not None:
            self.right = m.get('Right')
        if m.get('Top') is not None:
            self.top = m.get('Top')
        return self


class DetectVehicleICongestionResponseBodyDataElements(TeaModel):
    def __init__(
        self,
        boxes: List[DetectVehicleICongestionResponseBodyDataElementsBoxes] = None,
        id: int = None,
        score: float = None,
        type_name: str = None,
    ):
        self.boxes = boxes
        self.id = id
        self.score = score
        self.type_name = type_name

    def validate(self):
        if self.boxes:
            for k in self.boxes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Boxes'] = []
        if self.boxes is not None:
            for k in self.boxes:
                result['Boxes'].append(k.to_map() if k else None)
        if self.id is not None:
            result['Id'] = self.id
        if self.score is not None:
            result['Score'] = self.score
        if self.type_name is not None:
            result['TypeName'] = self.type_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.boxes = []
        if m.get('Boxes') is not None:
            for k in m.get('Boxes'):
                temp_model = DetectVehicleICongestionResponseBodyDataElementsBoxes()
                self.boxes.append(temp_model.from_map(k))
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('TypeName') is not None:
            self.type_name = m.get('TypeName')
        return self


class DetectVehicleICongestionResponseBodyDataRegionIntersectFeatures(TeaModel):
    def __init__(
        self,
        features: List[str] = None,
    ):
        self.features = features

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.features is not None:
            result['Features'] = self.features
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Features') is not None:
            self.features = m.get('Features')
        return self


class DetectVehicleICongestionResponseBodyDataRegionIntersectMatched(TeaModel):
    def __init__(
        self,
        ids: List[int] = None,
    ):
        self.ids = ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ids is not None:
            result['Ids'] = self.ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ids') is not None:
            self.ids = m.get('Ids')
        return self


class DetectVehicleICongestionResponseBodyDataRegionIntersects(TeaModel):
    def __init__(
        self,
        ids: List[int] = None,
    ):
        self.ids = ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ids is not None:
            result['Ids'] = self.ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ids') is not None:
            self.ids = m.get('Ids')
        return self


class DetectVehicleICongestionResponseBodyData(TeaModel):
    def __init__(
        self,
        elements: List[DetectVehicleICongestionResponseBodyDataElements] = None,
        region_intersect_features: List[DetectVehicleICongestionResponseBodyDataRegionIntersectFeatures] = None,
        region_intersect_matched: List[DetectVehicleICongestionResponseBodyDataRegionIntersectMatched] = None,
        region_intersects: List[DetectVehicleICongestionResponseBodyDataRegionIntersects] = None,
    ):
        self.elements = elements
        self.region_intersect_features = region_intersect_features
        self.region_intersect_matched = region_intersect_matched
        self.region_intersects = region_intersects

    def validate(self):
        if self.elements:
            for k in self.elements:
                if k:
                    k.validate()
        if self.region_intersect_features:
            for k in self.region_intersect_features:
                if k:
                    k.validate()
        if self.region_intersect_matched:
            for k in self.region_intersect_matched:
                if k:
                    k.validate()
        if self.region_intersects:
            for k in self.region_intersects:
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
        result['RegionIntersectFeatures'] = []
        if self.region_intersect_features is not None:
            for k in self.region_intersect_features:
                result['RegionIntersectFeatures'].append(k.to_map() if k else None)
        result['RegionIntersectMatched'] = []
        if self.region_intersect_matched is not None:
            for k in self.region_intersect_matched:
                result['RegionIntersectMatched'].append(k.to_map() if k else None)
        result['RegionIntersects'] = []
        if self.region_intersects is not None:
            for k in self.region_intersects:
                result['RegionIntersects'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.elements = []
        if m.get('Elements') is not None:
            for k in m.get('Elements'):
                temp_model = DetectVehicleICongestionResponseBodyDataElements()
                self.elements.append(temp_model.from_map(k))
        self.region_intersect_features = []
        if m.get('RegionIntersectFeatures') is not None:
            for k in m.get('RegionIntersectFeatures'):
                temp_model = DetectVehicleICongestionResponseBodyDataRegionIntersectFeatures()
                self.region_intersect_features.append(temp_model.from_map(k))
        self.region_intersect_matched = []
        if m.get('RegionIntersectMatched') is not None:
            for k in m.get('RegionIntersectMatched'):
                temp_model = DetectVehicleICongestionResponseBodyDataRegionIntersectMatched()
                self.region_intersect_matched.append(temp_model.from_map(k))
        self.region_intersects = []
        if m.get('RegionIntersects') is not None:
            for k in m.get('RegionIntersects'):
                temp_model = DetectVehicleICongestionResponseBodyDataRegionIntersects()
                self.region_intersects.append(temp_model.from_map(k))
        return self


class DetectVehicleICongestionResponseBody(TeaModel):
    def __init__(
        self,
        data: DetectVehicleICongestionResponseBodyData = None,
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
            temp_model = DetectVehicleICongestionResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DetectVehicleICongestionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DetectVehicleICongestionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DetectVehicleICongestionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetectVehicleIllegalParkingRequestRoadRegionsRoadRegionPoint(TeaModel):
    def __init__(
        self,
        x: int = None,
        y: int = None,
    ):
        # This parameter is required.
        self.x = x
        # This parameter is required.
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


class DetectVehicleIllegalParkingRequestRoadRegionsRoadRegion(TeaModel):
    def __init__(
        self,
        point: DetectVehicleIllegalParkingRequestRoadRegionsRoadRegionPoint = None,
    ):
        # This parameter is required.
        self.point = point

    def validate(self):
        if self.point:
            self.point.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.point is not None:
            result['Point'] = self.point.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Point') is not None:
            temp_model = DetectVehicleIllegalParkingRequestRoadRegionsRoadRegionPoint()
            self.point = temp_model.from_map(m['Point'])
        return self


class DetectVehicleIllegalParkingRequestRoadRegions(TeaModel):
    def __init__(
        self,
        road_region: List[DetectVehicleIllegalParkingRequestRoadRegionsRoadRegion] = None,
    ):
        # This parameter is required.
        self.road_region = road_region

    def validate(self):
        if self.road_region:
            for k in self.road_region:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RoadRegion'] = []
        if self.road_region is not None:
            for k in self.road_region:
                result['RoadRegion'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.road_region = []
        if m.get('RoadRegion') is not None:
            for k in m.get('RoadRegion'):
                temp_model = DetectVehicleIllegalParkingRequestRoadRegionsRoadRegion()
                self.road_region.append(temp_model.from_map(k))
        return self


class DetectVehicleIllegalParkingRequest(TeaModel):
    def __init__(
        self,
        image_url: str = None,
        road_regions: List[DetectVehicleIllegalParkingRequestRoadRegions] = None,
    ):
        # This parameter is required.
        self.image_url = image_url
        # This parameter is required.
        self.road_regions = road_regions

    def validate(self):
        if self.road_regions:
            for k in self.road_regions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        result['RoadRegions'] = []
        if self.road_regions is not None:
            for k in self.road_regions:
                result['RoadRegions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        self.road_regions = []
        if m.get('RoadRegions') is not None:
            for k in m.get('RoadRegions'):
                temp_model = DetectVehicleIllegalParkingRequestRoadRegions()
                self.road_regions.append(temp_model.from_map(k))
        return self


class DetectVehicleIllegalParkingAdvanceRequestRoadRegionsRoadRegionPoint(TeaModel):
    def __init__(
        self,
        x: int = None,
        y: int = None,
    ):
        # This parameter is required.
        self.x = x
        # This parameter is required.
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


class DetectVehicleIllegalParkingAdvanceRequestRoadRegionsRoadRegion(TeaModel):
    def __init__(
        self,
        point: DetectVehicleIllegalParkingAdvanceRequestRoadRegionsRoadRegionPoint = None,
    ):
        # This parameter is required.
        self.point = point

    def validate(self):
        if self.point:
            self.point.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.point is not None:
            result['Point'] = self.point.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Point') is not None:
            temp_model = DetectVehicleIllegalParkingAdvanceRequestRoadRegionsRoadRegionPoint()
            self.point = temp_model.from_map(m['Point'])
        return self


class DetectVehicleIllegalParkingAdvanceRequestRoadRegions(TeaModel):
    def __init__(
        self,
        road_region: List[DetectVehicleIllegalParkingAdvanceRequestRoadRegionsRoadRegion] = None,
    ):
        # This parameter is required.
        self.road_region = road_region

    def validate(self):
        if self.road_region:
            for k in self.road_region:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RoadRegion'] = []
        if self.road_region is not None:
            for k in self.road_region:
                result['RoadRegion'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.road_region = []
        if m.get('RoadRegion') is not None:
            for k in m.get('RoadRegion'):
                temp_model = DetectVehicleIllegalParkingAdvanceRequestRoadRegionsRoadRegion()
                self.road_region.append(temp_model.from_map(k))
        return self


class DetectVehicleIllegalParkingAdvanceRequest(TeaModel):
    def __init__(
        self,
        image_urlobject: BinaryIO = None,
        road_regions: List[DetectVehicleIllegalParkingAdvanceRequestRoadRegions] = None,
    ):
        # This parameter is required.
        self.image_urlobject = image_urlobject
        # This parameter is required.
        self.road_regions = road_regions

    def validate(self):
        if self.road_regions:
            for k in self.road_regions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_urlobject is not None:
            result['ImageURL'] = self.image_urlobject
        result['RoadRegions'] = []
        if self.road_regions is not None:
            for k in self.road_regions:
                result['RoadRegions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_urlobject = m.get('ImageURL')
        self.road_regions = []
        if m.get('RoadRegions') is not None:
            for k in m.get('RoadRegions'):
                temp_model = DetectVehicleIllegalParkingAdvanceRequestRoadRegions()
                self.road_regions.append(temp_model.from_map(k))
        return self


class DetectVehicleIllegalParkingShrinkRequest(TeaModel):
    def __init__(
        self,
        image_url: str = None,
        road_regions_shrink: str = None,
    ):
        # This parameter is required.
        self.image_url = image_url
        # This parameter is required.
        self.road_regions_shrink = road_regions_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        if self.road_regions_shrink is not None:
            result['RoadRegions'] = self.road_regions_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        if m.get('RoadRegions') is not None:
            self.road_regions_shrink = m.get('RoadRegions')
        return self


class DetectVehicleIllegalParkingResponseBodyDataElementsBoxes(TeaModel):
    def __init__(
        self,
        bottom: int = None,
        left: int = None,
        right: int = None,
        top: int = None,
    ):
        self.bottom = bottom
        self.left = left
        self.right = right
        self.top = top

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bottom is not None:
            result['Bottom'] = self.bottom
        if self.left is not None:
            result['Left'] = self.left
        if self.right is not None:
            result['Right'] = self.right
        if self.top is not None:
            result['Top'] = self.top
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bottom') is not None:
            self.bottom = m.get('Bottom')
        if m.get('Left') is not None:
            self.left = m.get('Left')
        if m.get('Right') is not None:
            self.right = m.get('Right')
        if m.get('Top') is not None:
            self.top = m.get('Top')
        return self


class DetectVehicleIllegalParkingResponseBodyDataElements(TeaModel):
    def __init__(
        self,
        boxes: List[DetectVehicleIllegalParkingResponseBodyDataElementsBoxes] = None,
        id: int = None,
        score: float = None,
        type_name: str = None,
    ):
        self.boxes = boxes
        self.id = id
        self.score = score
        self.type_name = type_name

    def validate(self):
        if self.boxes:
            for k in self.boxes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Boxes'] = []
        if self.boxes is not None:
            for k in self.boxes:
                result['Boxes'].append(k.to_map() if k else None)
        if self.id is not None:
            result['Id'] = self.id
        if self.score is not None:
            result['Score'] = self.score
        if self.type_name is not None:
            result['TypeName'] = self.type_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.boxes = []
        if m.get('Boxes') is not None:
            for k in m.get('Boxes'):
                temp_model = DetectVehicleIllegalParkingResponseBodyDataElementsBoxes()
                self.boxes.append(temp_model.from_map(k))
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('TypeName') is not None:
            self.type_name = m.get('TypeName')
        return self


class DetectVehicleIllegalParkingResponseBodyDataRegionIntersects(TeaModel):
    def __init__(
        self,
        ids: List[int] = None,
    ):
        self.ids = ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ids is not None:
            result['Ids'] = self.ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ids') is not None:
            self.ids = m.get('Ids')
        return self


class DetectVehicleIllegalParkingResponseBodyData(TeaModel):
    def __init__(
        self,
        elements: List[DetectVehicleIllegalParkingResponseBodyDataElements] = None,
        region_intersects: List[DetectVehicleIllegalParkingResponseBodyDataRegionIntersects] = None,
    ):
        self.elements = elements
        self.region_intersects = region_intersects

    def validate(self):
        if self.elements:
            for k in self.elements:
                if k:
                    k.validate()
        if self.region_intersects:
            for k in self.region_intersects:
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
        result['RegionIntersects'] = []
        if self.region_intersects is not None:
            for k in self.region_intersects:
                result['RegionIntersects'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.elements = []
        if m.get('Elements') is not None:
            for k in m.get('Elements'):
                temp_model = DetectVehicleIllegalParkingResponseBodyDataElements()
                self.elements.append(temp_model.from_map(k))
        self.region_intersects = []
        if m.get('RegionIntersects') is not None:
            for k in m.get('RegionIntersects'):
                temp_model = DetectVehicleIllegalParkingResponseBodyDataRegionIntersects()
                self.region_intersects.append(temp_model.from_map(k))
        return self


class DetectVehicleIllegalParkingResponseBody(TeaModel):
    def __init__(
        self,
        data: DetectVehicleIllegalParkingResponseBodyData = None,
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
            temp_model = DetectVehicleIllegalParkingResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DetectVehicleIllegalParkingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DetectVehicleIllegalParkingResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DetectVehicleIllegalParkingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetectVideoIPCObjectRequest(TeaModel):
    def __init__(
        self,
        callback_only_has_object: bool = None,
        start_timestamp: int = None,
        video_url: str = None,
    ):
        self.callback_only_has_object = callback_only_has_object
        self.start_timestamp = start_timestamp
        # This parameter is required.
        self.video_url = video_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.callback_only_has_object is not None:
            result['CallbackOnlyHasObject'] = self.callback_only_has_object
        if self.start_timestamp is not None:
            result['StartTimestamp'] = self.start_timestamp
        if self.video_url is not None:
            result['VideoURL'] = self.video_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallbackOnlyHasObject') is not None:
            self.callback_only_has_object = m.get('CallbackOnlyHasObject')
        if m.get('StartTimestamp') is not None:
            self.start_timestamp = m.get('StartTimestamp')
        if m.get('VideoURL') is not None:
            self.video_url = m.get('VideoURL')
        return self


class DetectVideoIPCObjectAdvanceRequest(TeaModel):
    def __init__(
        self,
        callback_only_has_object: bool = None,
        start_timestamp: int = None,
        video_urlobject: BinaryIO = None,
    ):
        self.callback_only_has_object = callback_only_has_object
        self.start_timestamp = start_timestamp
        # This parameter is required.
        self.video_urlobject = video_urlobject

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.callback_only_has_object is not None:
            result['CallbackOnlyHasObject'] = self.callback_only_has_object
        if self.start_timestamp is not None:
            result['StartTimestamp'] = self.start_timestamp
        if self.video_urlobject is not None:
            result['VideoURL'] = self.video_urlobject
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallbackOnlyHasObject') is not None:
            self.callback_only_has_object = m.get('CallbackOnlyHasObject')
        if m.get('StartTimestamp') is not None:
            self.start_timestamp = m.get('StartTimestamp')
        if m.get('VideoURL') is not None:
            self.video_urlobject = m.get('VideoURL')
        return self


class DetectVideoIPCObjectResponseBodyDataFramesElements(TeaModel):
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


class DetectVideoIPCObjectResponseBodyDataFrames(TeaModel):
    def __init__(
        self,
        elements: List[DetectVideoIPCObjectResponseBodyDataFramesElements] = None,
        time: int = None,
    ):
        self.elements = elements
        self.time = time

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
        if self.time is not None:
            result['Time'] = self.time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.elements = []
        if m.get('Elements') is not None:
            for k in m.get('Elements'):
                temp_model = DetectVideoIPCObjectResponseBodyDataFramesElements()
                self.elements.append(temp_model.from_map(k))
        if m.get('Time') is not None:
            self.time = m.get('Time')
        return self


class DetectVideoIPCObjectResponseBodyData(TeaModel):
    def __init__(
        self,
        frames: List[DetectVideoIPCObjectResponseBodyDataFrames] = None,
        height: int = None,
        input_file: str = None,
        width: int = None,
    ):
        self.frames = frames
        self.height = height
        self.input_file = input_file
        self.width = width

    def validate(self):
        if self.frames:
            for k in self.frames:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Frames'] = []
        if self.frames is not None:
            for k in self.frames:
                result['Frames'].append(k.to_map() if k else None)
        if self.height is not None:
            result['Height'] = self.height
        if self.input_file is not None:
            result['InputFile'] = self.input_file
        if self.width is not None:
            result['Width'] = self.width
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.frames = []
        if m.get('Frames') is not None:
            for k in m.get('Frames'):
                temp_model = DetectVideoIPCObjectResponseBodyDataFrames()
                self.frames.append(temp_model.from_map(k))
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('InputFile') is not None:
            self.input_file = m.get('InputFile')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        return self


class DetectVideoIPCObjectResponseBody(TeaModel):
    def __init__(
        self,
        data: DetectVideoIPCObjectResponseBodyData = None,
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
            temp_model = DetectVideoIPCObjectResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DetectVideoIPCObjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DetectVideoIPCObjectResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DetectVideoIPCObjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetectWhiteBaseImageRequest(TeaModel):
    def __init__(
        self,
        image_url: str = None,
    ):
        # This parameter is required.
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


class DetectWhiteBaseImageAdvanceRequest(TeaModel):
    def __init__(
        self,
        image_urlobject: BinaryIO = None,
    ):
        # This parameter is required.
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


class DetectWhiteBaseImageResponseBodyDataElements(TeaModel):
    def __init__(
        self,
        white_base: int = None,
    ):
        self.white_base = white_base

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.white_base is not None:
            result['WhiteBase'] = self.white_base
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('WhiteBase') is not None:
            self.white_base = m.get('WhiteBase')
        return self


class DetectWhiteBaseImageResponseBodyData(TeaModel):
    def __init__(
        self,
        elements: List[DetectWhiteBaseImageResponseBodyDataElements] = None,
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
                temp_model = DetectWhiteBaseImageResponseBodyDataElements()
                self.elements.append(temp_model.from_map(k))
        return self


class DetectWhiteBaseImageResponseBody(TeaModel):
    def __init__(
        self,
        data: DetectWhiteBaseImageResponseBodyData = None,
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
            temp_model = DetectWhiteBaseImageResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DetectWhiteBaseImageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DetectWhiteBaseImageResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DetectWhiteBaseImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetectWorkwearRequestClothes(TeaModel):
    def __init__(
        self,
        max_num: int = None,
        threshold: float = None,
    ):
        self.max_num = max_num
        self.threshold = threshold

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_num is not None:
            result['MaxNum'] = self.max_num
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxNum') is not None:
            self.max_num = m.get('MaxNum')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        return self


class DetectWorkwearRequest(TeaModel):
    def __init__(
        self,
        clothes: DetectWorkwearRequestClothes = None,
        image_url: str = None,
        labels: List[str] = None,
    ):
        self.clothes = clothes
        self.image_url = image_url
        # 1
        self.labels = labels

    def validate(self):
        if self.clothes:
            self.clothes.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.clothes is not None:
            result['Clothes'] = self.clothes.to_map()
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        if self.labels is not None:
            result['Labels'] = self.labels
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Clothes') is not None:
            temp_model = DetectWorkwearRequestClothes()
            self.clothes = temp_model.from_map(m['Clothes'])
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        return self


class DetectWorkwearAdvanceRequestClothes(TeaModel):
    def __init__(
        self,
        max_num: int = None,
        threshold: float = None,
    ):
        self.max_num = max_num
        self.threshold = threshold

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_num is not None:
            result['MaxNum'] = self.max_num
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxNum') is not None:
            self.max_num = m.get('MaxNum')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        return self


class DetectWorkwearAdvanceRequest(TeaModel):
    def __init__(
        self,
        clothes: DetectWorkwearAdvanceRequestClothes = None,
        image_url_object: BinaryIO = None,
        labels: List[str] = None,
    ):
        self.clothes = clothes
        self.image_url_object = image_url_object
        # 1
        self.labels = labels

    def validate(self):
        if self.clothes:
            self.clothes.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.clothes is not None:
            result['Clothes'] = self.clothes.to_map()
        if self.image_url_object is not None:
            result['ImageUrl'] = self.image_url_object
        if self.labels is not None:
            result['Labels'] = self.labels
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Clothes') is not None:
            temp_model = DetectWorkwearAdvanceRequestClothes()
            self.clothes = temp_model.from_map(m['Clothes'])
        if m.get('ImageUrl') is not None:
            self.image_url_object = m.get('ImageUrl')
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        return self


class DetectWorkwearShrinkRequest(TeaModel):
    def __init__(
        self,
        clothes_shrink: str = None,
        image_url: str = None,
        labels: List[str] = None,
    ):
        self.clothes_shrink = clothes_shrink
        self.image_url = image_url
        # 1
        self.labels = labels

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.clothes_shrink is not None:
            result['Clothes'] = self.clothes_shrink
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        if self.labels is not None:
            result['Labels'] = self.labels
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Clothes') is not None:
            self.clothes_shrink = m.get('Clothes')
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        return self


class DetectWorkwearResponseBodyDataElementsPropertyProbability(TeaModel):
    def __init__(
        self,
        no: float = None,
        threshold: int = None,
        unknown: float = None,
        yes: float = None,
    ):
        self.no = no
        self.threshold = threshold
        self.unknown = unknown
        self.yes = yes

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.no is not None:
            result['No'] = self.no
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        if self.unknown is not None:
            result['Unknown'] = self.unknown
        if self.yes is not None:
            result['Yes'] = self.yes
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('No') is not None:
            self.no = m.get('No')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        if m.get('Unknown') is not None:
            self.unknown = m.get('Unknown')
        if m.get('Yes') is not None:
            self.yes = m.get('Yes')
        return self


class DetectWorkwearResponseBodyDataElementsProperty(TeaModel):
    def __init__(
        self,
        label: str = None,
        probability: DetectWorkwearResponseBodyDataElementsPropertyProbability = None,
    ):
        self.label = label
        self.probability = probability

    def validate(self):
        if self.probability:
            self.probability.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label is not None:
            result['Label'] = self.label
        if self.probability is not None:
            result['Probability'] = self.probability.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Probability') is not None:
            temp_model = DetectWorkwearResponseBodyDataElementsPropertyProbability()
            self.probability = temp_model.from_map(m['Probability'])
        return self


class DetectWorkwearResponseBodyDataElementsRectangles(TeaModel):
    def __init__(
        self,
        height: int = None,
        left: int = None,
        top: int = None,
        width: int = None,
    ):
        self.height = height
        self.left = left
        self.top = top
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
        if self.left is not None:
            result['Left'] = self.left
        if self.top is not None:
            result['Top'] = self.top
        if self.width is not None:
            result['Width'] = self.width
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Left') is not None:
            self.left = m.get('Left')
        if m.get('Top') is not None:
            self.top = m.get('Top')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        return self


class DetectWorkwearResponseBodyDataElements(TeaModel):
    def __init__(
        self,
        property: List[DetectWorkwearResponseBodyDataElementsProperty] = None,
        rectangles: DetectWorkwearResponseBodyDataElementsRectangles = None,
        score: float = None,
        type: str = None,
    ):
        self.property = property
        self.rectangles = rectangles
        self.score = score
        self.type = type

    def validate(self):
        if self.property:
            for k in self.property:
                if k:
                    k.validate()
        if self.rectangles:
            self.rectangles.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Property'] = []
        if self.property is not None:
            for k in self.property:
                result['Property'].append(k.to_map() if k else None)
        if self.rectangles is not None:
            result['Rectangles'] = self.rectangles.to_map()
        if self.score is not None:
            result['Score'] = self.score
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.property = []
        if m.get('Property') is not None:
            for k in m.get('Property'):
                temp_model = DetectWorkwearResponseBodyDataElementsProperty()
                self.property.append(temp_model.from_map(k))
        if m.get('Rectangles') is not None:
            temp_model = DetectWorkwearResponseBodyDataElementsRectangles()
            self.rectangles = temp_model.from_map(m['Rectangles'])
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DetectWorkwearResponseBodyData(TeaModel):
    def __init__(
        self,
        elements: List[DetectWorkwearResponseBodyDataElements] = None,
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
                temp_model = DetectWorkwearResponseBodyDataElements()
                self.elements.append(temp_model.from_map(k))
        return self


class DetectWorkwearResponseBody(TeaModel):
    def __init__(
        self,
        data: DetectWorkwearResponseBodyData = None,
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
            temp_model = DetectWorkwearResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DetectWorkwearResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DetectWorkwearResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DetectWorkwearResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAsyncJobResultRequest(TeaModel):
    def __init__(
        self,
        job_id: str = None,
    ):
        # This parameter is required.
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


