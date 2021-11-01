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
        # 目标高度(像素)
        self.height = height
        # 目标置信度，范围为[0.0, 1.0]
        self.score = score
        # 目标类型：PERSON, VEHICLE, PET
        self.type = type
        # 目标宽度(像素)
        self.width = width
        # 左上角x坐标(像素)
        self.x = x
        # 左上角y坐标(像素)
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
        # 结果集
        self.elements = elements
        # 时间
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


class ClassifyVehicleInsuranceRequest(TeaModel):
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


class ClassifyVehicleInsuranceAdvanceRequest(TeaModel):
    def __init__(
        self,
        image_urlobject: BinaryIO = None,
    ):
        self.image_urlobject = image_urlobject

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_urlobject is not None:
            result['ImageURLObject'] = self.image_urlobject
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURLObject') is not None:
            self.image_urlobject = m.get('ImageURLObject')
        return self


class ClassifyVehicleInsuranceResponseBodyDataLabels(TeaModel):
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


class ClassifyVehicleInsuranceResponseBodyData(TeaModel):
    def __init__(
        self,
        labels: List[ClassifyVehicleInsuranceResponseBodyDataLabels] = None,
        threshold: float = None,
    ):
        self.labels = labels
        self.threshold = threshold

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
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.labels = []
        if m.get('Labels') is not None:
            for k in m.get('Labels'):
                temp_model = ClassifyVehicleInsuranceResponseBodyDataLabels()
                self.labels.append(temp_model.from_map(k))
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        return self


class ClassifyVehicleInsuranceResponseBody(TeaModel):
    def __init__(
        self,
        data: ClassifyVehicleInsuranceResponseBodyData = None,
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
            temp_model = ClassifyVehicleInsuranceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ClassifyVehicleInsuranceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ClassifyVehicleInsuranceResponseBody = None,
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
            temp_model = ClassifyVehicleInsuranceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetectIPCObjectRequest(TeaModel):
    def __init__(
        self,
        image_url: str = None,
    ):
        # 图片URL地址
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
        # Id of the request
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
        body: DetectIPCObjectResponseBody = None,
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
            temp_model = DetectIPCObjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetectKitchenAnimalsRequest(TeaModel):
    def __init__(
        self,
        image_urla: str = None,
        image_urlb: str = None,
    ):
        self.image_urla = image_urla
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
        image_urlb: str = None,
    ):
        self.image_urlaobject = image_urlaobject
        self.image_urlb = image_urlb

    def validate(self):
        self.validate_required(self.image_urlaobject, 'image_urlaobject')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_urlaobject is not None:
            result['ImageURLAObject'] = self.image_urlaobject
        if self.image_urlb is not None:
            result['ImageURLB'] = self.image_urlb
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURLAObject') is not None:
            self.image_urlaobject = m.get('ImageURLAObject')
        if m.get('ImageURLB') is not None:
            self.image_urlb = m.get('ImageURLB')
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
        # Id of the request
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
        body: DetectKitchenAnimalsResponseBody = None,
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
            temp_model = DetectKitchenAnimalsResponseBody()
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
        self.image_urlobject = image_urlobject

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_urlobject is not None:
            result['ImageURLObject'] = self.image_urlobject
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURLObject') is not None:
            self.image_urlobject = m.get('ImageURLObject')
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
            temp_model = DetectMainBodyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetectObjectRequest(TeaModel):
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


class DetectObjectAdvanceRequest(TeaModel):
    def __init__(
        self,
        image_urlobject: BinaryIO = None,
    ):
        self.image_urlobject = image_urlobject

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_urlobject is not None:
            result['ImageURLObject'] = self.image_urlobject
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURLObject') is not None:
            self.image_urlobject = m.get('ImageURLObject')
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
        body: DetectObjectResponseBody = None,
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
            temp_model = DetectObjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetectTransparentImageRequest(TeaModel):
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


class DetectTransparentImageAdvanceRequest(TeaModel):
    def __init__(
        self,
        image_urlobject: BinaryIO = None,
    ):
        self.image_urlobject = image_urlobject

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_urlobject is not None:
            result['ImageURLObject'] = self.image_urlobject
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURLObject') is not None:
            self.image_urlobject = m.get('ImageURLObject')
        return self


class DetectTransparentImageResponseBodyDataElements(TeaModel):
    def __init__(
        self,
        transparent_image: int = None,
    ):
        self.transparent_image = transparent_image

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.transparent_image is not None:
            result['TransparentImage'] = self.transparent_image
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TransparentImage') is not None:
            self.transparent_image = m.get('TransparentImage')
        return self


class DetectTransparentImageResponseBodyData(TeaModel):
    def __init__(
        self,
        elements: List[DetectTransparentImageResponseBodyDataElements] = None,
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
                temp_model = DetectTransparentImageResponseBodyDataElements()
                self.elements.append(temp_model.from_map(k))
        return self


class DetectTransparentImageResponseBody(TeaModel):
    def __init__(
        self,
        data: DetectTransparentImageResponseBodyData = None,
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
            temp_model = DetectTransparentImageResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DetectTransparentImageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DetectTransparentImageResponseBody = None,
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
            temp_model = DetectTransparentImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetectVehicleRequest(TeaModel):
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


class DetectVehicleAdvanceRequest(TeaModel):
    def __init__(
        self,
        image_urlobject: BinaryIO = None,
    ):
        self.image_urlobject = image_urlobject

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_urlobject is not None:
            result['ImageURLObject'] = self.image_urlobject
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURLObject') is not None:
            self.image_urlobject = m.get('ImageURLObject')
        return self


class DetectVehicleResponseBodyDataDetectObjectInfoList(TeaModel):
    def __init__(
        self,
        boxes: List[int] = None,
        id: int = None,
        score: float = None,
        type: str = None,
    ):
        self.boxes = boxes
        self.id = id
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
        if self.id is not None:
            result['Id'] = self.id
        if self.score is not None:
            result['Score'] = self.score
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Boxes') is not None:
            self.boxes = m.get('Boxes')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DetectVehicleResponseBodyData(TeaModel):
    def __init__(
        self,
        detect_object_info_list: List[DetectVehicleResponseBodyDataDetectObjectInfoList] = None,
        height: int = None,
        width: int = None,
    ):
        self.detect_object_info_list = detect_object_info_list
        self.height = height
        self.width = width

    def validate(self):
        if self.detect_object_info_list:
            for k in self.detect_object_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DetectObjectInfoList'] = []
        if self.detect_object_info_list is not None:
            for k in self.detect_object_info_list:
                result['DetectObjectInfoList'].append(k.to_map() if k else None)
        if self.height is not None:
            result['Height'] = self.height
        if self.width is not None:
            result['Width'] = self.width
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.detect_object_info_list = []
        if m.get('DetectObjectInfoList') is not None:
            for k in m.get('DetectObjectInfoList'):
                temp_model = DetectVehicleResponseBodyDataDetectObjectInfoList()
                self.detect_object_info_list.append(temp_model.from_map(k))
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        return self


class DetectVehicleResponseBody(TeaModel):
    def __init__(
        self,
        data: DetectVehicleResponseBodyData = None,
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
            temp_model = DetectVehicleResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DetectVehicleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DetectVehicleResponseBody = None,
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
            temp_model = DetectVehicleResponseBody()
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


class DetectVehicleICongestionRequestRoadRegionsRoadRegion(TeaModel):
    def __init__(
        self,
        point: DetectVehicleICongestionRequestRoadRegionsRoadRegionPoint = None,
    ):
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
        origin_request_id: str = None,
        pre_region_intersect_features: List[DetectVehicleICongestionRequestPreRegionIntersectFeatures] = None,
        road_regions: List[DetectVehicleICongestionRequestRoadRegions] = None,
        stream_arn: str = None,
    ):
        # A short description of struct
        self.image_url = image_url
        self.origin_request_id = origin_request_id
        self.pre_region_intersect_features = pre_region_intersect_features
        self.road_regions = road_regions
        self.stream_arn = stream_arn

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
        if self.origin_request_id is not None:
            result['OriginRequestId'] = self.origin_request_id
        result['PreRegionIntersectFeatures'] = []
        if self.pre_region_intersect_features is not None:
            for k in self.pre_region_intersect_features:
                result['PreRegionIntersectFeatures'].append(k.to_map() if k else None)
        result['RoadRegions'] = []
        if self.road_regions is not None:
            for k in self.road_regions:
                result['RoadRegions'].append(k.to_map() if k else None)
        if self.stream_arn is not None:
            result['StreamArn'] = self.stream_arn
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        if m.get('OriginRequestId') is not None:
            self.origin_request_id = m.get('OriginRequestId')
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
        if m.get('StreamArn') is not None:
            self.stream_arn = m.get('StreamArn')
        return self


class DetectVehicleICongestionShrinkRequest(TeaModel):
    def __init__(
        self,
        image_url: str = None,
        origin_request_id: str = None,
        pre_region_intersect_features_shrink: str = None,
        road_regions_shrink: str = None,
        stream_arn: str = None,
    ):
        # A short description of struct
        self.image_url = image_url
        self.origin_request_id = origin_request_id
        self.pre_region_intersect_features_shrink = pre_region_intersect_features_shrink
        self.road_regions_shrink = road_regions_shrink
        self.stream_arn = stream_arn

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        if self.origin_request_id is not None:
            result['OriginRequestId'] = self.origin_request_id
        if self.pre_region_intersect_features_shrink is not None:
            result['PreRegionIntersectFeatures'] = self.pre_region_intersect_features_shrink
        if self.road_regions_shrink is not None:
            result['RoadRegions'] = self.road_regions_shrink
        if self.stream_arn is not None:
            result['StreamArn'] = self.stream_arn
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        if m.get('OriginRequestId') is not None:
            self.origin_request_id = m.get('OriginRequestId')
        if m.get('PreRegionIntersectFeatures') is not None:
            self.pre_region_intersect_features_shrink = m.get('PreRegionIntersectFeatures')
        if m.get('RoadRegions') is not None:
            self.road_regions_shrink = m.get('RoadRegions')
        if m.get('StreamArn') is not None:
            self.stream_arn = m.get('StreamArn')
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
        score: float = None,
        type_name: str = None,
    ):
        self.boxes = boxes
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
        # Id of the request
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
        body: DetectVehicleICongestionResponseBody = None,
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
            temp_model = DetectVehicleICongestionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetectVehicleIllegalParkingRequestRoadRegionsRoadRegionPoint(TeaModel):
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


class DetectVehicleIllegalParkingRequestRoadRegionsRoadRegion(TeaModel):
    def __init__(
        self,
        point: DetectVehicleIllegalParkingRequestRoadRegionsRoadRegionPoint = None,
    ):
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
        origin_request_id: str = None,
        road_regions: List[DetectVehicleIllegalParkingRequestRoadRegions] = None,
        stream_arn: str = None,
    ):
        # A short description of struct
        self.image_url = image_url
        self.origin_request_id = origin_request_id
        self.road_regions = road_regions
        self.stream_arn = stream_arn

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
        if self.origin_request_id is not None:
            result['OriginRequestId'] = self.origin_request_id
        result['RoadRegions'] = []
        if self.road_regions is not None:
            for k in self.road_regions:
                result['RoadRegions'].append(k.to_map() if k else None)
        if self.stream_arn is not None:
            result['StreamArn'] = self.stream_arn
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        if m.get('OriginRequestId') is not None:
            self.origin_request_id = m.get('OriginRequestId')
        self.road_regions = []
        if m.get('RoadRegions') is not None:
            for k in m.get('RoadRegions'):
                temp_model = DetectVehicleIllegalParkingRequestRoadRegions()
                self.road_regions.append(temp_model.from_map(k))
        if m.get('StreamArn') is not None:
            self.stream_arn = m.get('StreamArn')
        return self


class DetectVehicleIllegalParkingShrinkRequest(TeaModel):
    def __init__(
        self,
        image_url: str = None,
        origin_request_id: str = None,
        road_regions_shrink: str = None,
        stream_arn: str = None,
    ):
        # A short description of struct
        self.image_url = image_url
        self.origin_request_id = origin_request_id
        self.road_regions_shrink = road_regions_shrink
        self.stream_arn = stream_arn

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        if self.origin_request_id is not None:
            result['OriginRequestId'] = self.origin_request_id
        if self.road_regions_shrink is not None:
            result['RoadRegions'] = self.road_regions_shrink
        if self.stream_arn is not None:
            result['StreamArn'] = self.stream_arn
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        if m.get('OriginRequestId') is not None:
            self.origin_request_id = m.get('OriginRequestId')
        if m.get('RoadRegions') is not None:
            self.road_regions_shrink = m.get('RoadRegions')
        if m.get('StreamArn') is not None:
            self.stream_arn = m.get('StreamArn')
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
        score: float = None,
        type_name: str = None,
    ):
        self.boxes = boxes
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
        # Id of the request
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
        body: DetectVehicleIllegalParkingResponseBody = None,
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
            temp_model = DetectVehicleIllegalParkingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetectVideoFrameRequest(TeaModel):
    def __init__(
        self,
        create_time: int = None,
        feature_config: str = None,
        features: List[str] = None,
        height: int = None,
        image_url: str = None,
        owner_id: int = None,
        stream_arn: str = None,
        width: int = None,
    ):
        # 图片创建时间
        self.create_time = create_time
        # AI每个功能具体配置描述，每个AI算法配置都不一样
        self.feature_config = feature_config
        # AI功能名称列表
        self.features = features
        # 图像高度
        self.height = height
        # 图片URL地址
        self.image_url = image_url
        # 自用拥有者pk
        self.owner_id = owner_id
        # 流资源唯一描述
        self.stream_arn = stream_arn
        # 图像宽度
        self.width = width

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.feature_config is not None:
            result['FeatureConfig'] = self.feature_config
        if self.features is not None:
            result['Features'] = self.features
        if self.height is not None:
            result['Height'] = self.height
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.stream_arn is not None:
            result['StreamArn'] = self.stream_arn
        if self.width is not None:
            result['Width'] = self.width
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('FeatureConfig') is not None:
            self.feature_config = m.get('FeatureConfig')
        if m.get('Features') is not None:
            self.features = m.get('Features')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('StreamArn') is not None:
            self.stream_arn = m.get('StreamArn')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        return self


class DetectVideoFrameShrinkRequest(TeaModel):
    def __init__(
        self,
        create_time: int = None,
        feature_config: str = None,
        features_shrink: str = None,
        height: int = None,
        image_url: str = None,
        owner_id: int = None,
        stream_arn: str = None,
        width: int = None,
    ):
        # 图片创建时间
        self.create_time = create_time
        # AI每个功能具体配置描述，每个AI算法配置都不一样
        self.feature_config = feature_config
        # AI功能名称列表
        self.features_shrink = features_shrink
        # 图像高度
        self.height = height
        # 图片URL地址
        self.image_url = image_url
        # 自用拥有者pk
        self.owner_id = owner_id
        # 流资源唯一描述
        self.stream_arn = stream_arn
        # 图像宽度
        self.width = width

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.feature_config is not None:
            result['FeatureConfig'] = self.feature_config
        if self.features_shrink is not None:
            result['Features'] = self.features_shrink
        if self.height is not None:
            result['Height'] = self.height
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.stream_arn is not None:
            result['StreamArn'] = self.stream_arn
        if self.width is not None:
            result['Width'] = self.width
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('FeatureConfig') is not None:
            self.feature_config = m.get('FeatureConfig')
        if m.get('Features') is not None:
            self.features_shrink = m.get('Features')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('StreamArn') is not None:
            self.stream_arn = m.get('StreamArn')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        return self


class DetectVideoFrameResponseBodyData(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
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


class DetectVideoFrameResponseBody(TeaModel):
    def __init__(
        self,
        data: DetectVideoFrameResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        # Id of the request
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
            temp_model = DetectVideoFrameResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DetectVideoFrameResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DetectVideoFrameResponseBody = None,
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
            temp_model = DetectVideoFrameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetectVideoIPCObjectRequest(TeaModel):
    def __init__(
        self,
        callback_only_has_object: bool = None,
        start_timestamp: int = None,
        video_url: str = None,
    ):
        # 是否只有检测到物体才回调
        self.callback_only_has_object = callback_only_has_object
        # 视频的开始时间戳(秒)，即UTC时间，默认为0
        self.start_timestamp = start_timestamp
        # 视频文件URL地址
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
        video_urlobject: BinaryIO = None,
        callback_only_has_object: bool = None,
        start_timestamp: int = None,
    ):
        self.video_urlobject = video_urlobject
        # 是否只有检测到物体才回调
        self.callback_only_has_object = callback_only_has_object
        # 视频的开始时间戳(秒)，即UTC时间，默认为0
        self.start_timestamp = start_timestamp

    def validate(self):
        self.validate_required(self.video_urlobject, 'video_urlobject')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.video_urlobject is not None:
            result['VideoURLObject'] = self.video_urlobject
        if self.callback_only_has_object is not None:
            result['CallbackOnlyHasObject'] = self.callback_only_has_object
        if self.start_timestamp is not None:
            result['StartTimestamp'] = self.start_timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VideoURLObject') is not None:
            self.video_urlobject = m.get('VideoURLObject')
        if m.get('CallbackOnlyHasObject') is not None:
            self.callback_only_has_object = m.get('CallbackOnlyHasObject')
        if m.get('StartTimestamp') is not None:
            self.start_timestamp = m.get('StartTimestamp')
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
        # 视频帧时间，startTimestamp+视频帧的相对时间的值，单位毫秒，如果startTimestamp为空，则是相对时间
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
        # 视频帧的集合，未检测到目标的帧不列出
        self.frames = frames
        # 视频文件的分辨率(像素)
        self.height = height
        # 输入文件信息
        self.input_file = input_file
        # 视频文件的分辨率(像素)
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
        request_id: str = None,
    ):
        self.data = data
        # JobId
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
            temp_model = DetectVideoIPCObjectResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DetectVideoIPCObjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DetectVideoIPCObjectResponseBody = None,
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
            temp_model = DetectVideoIPCObjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetectWhiteBaseImageRequest(TeaModel):
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


class DetectWhiteBaseImageAdvanceRequest(TeaModel):
    def __init__(
        self,
        image_urlobject: BinaryIO = None,
    ):
        self.image_urlobject = image_urlobject

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_urlobject is not None:
            result['ImageURLObject'] = self.image_urlobject
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURLObject') is not None:
            self.image_urlobject = m.get('ImageURLObject')
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
        body: DetectWhiteBaseImageResponseBody = None,
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
        image_url_object: BinaryIO = None,
        clothes: DetectWorkwearAdvanceRequestClothes = None,
        labels: List[str] = None,
    ):
        self.image_url_object = image_url_object
        self.clothes = clothes
        self.labels = labels

    def validate(self):
        self.validate_required(self.image_url_object, 'image_url_object')
        if self.clothes:
            self.clothes.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_url_object is not None:
            result['ImageUrlObject'] = self.image_url_object
        if self.clothes is not None:
            result['Clothes'] = self.clothes.to_map()
        if self.labels is not None:
            result['Labels'] = self.labels
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageUrlObject') is not None:
            self.image_url_object = m.get('ImageUrlObject')
        if m.get('Clothes') is not None:
            temp_model = DetectWorkwearAdvanceRequestClothes()
            self.clothes = temp_model.from_map(m['Clothes'])
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
        # Id of the request
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
        body: DetectWorkwearResponseBody = None,
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
            temp_model = DetectWorkwearResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GenerateVehicleRepairPlanRequestDamageImageList(TeaModel):
    def __init__(
        self,
        create_time_stamp: str = None,
        image_url: str = None,
    ):
        self.create_time_stamp = create_time_stamp
        self.image_url = image_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time_stamp is not None:
            result['CreateTimeStamp'] = self.create_time_stamp
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTimeStamp') is not None:
            self.create_time_stamp = m.get('CreateTimeStamp')
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        return self


class GenerateVehicleRepairPlanRequest(TeaModel):
    def __init__(
        self,
        damage_image_list: List[GenerateVehicleRepairPlanRequestDamageImageList] = None,
    ):
        self.damage_image_list = damage_image_list

    def validate(self):
        if self.damage_image_list:
            for k in self.damage_image_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DamageImageList'] = []
        if self.damage_image_list is not None:
            for k in self.damage_image_list:
                result['DamageImageList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.damage_image_list = []
        if m.get('DamageImageList') is not None:
            for k in m.get('DamageImageList'):
                temp_model = GenerateVehicleRepairPlanRequestDamageImageList()
                self.damage_image_list.append(temp_model.from_map(k))
        return self


class GenerateVehicleRepairPlanResponseBodyData(TeaModel):
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


class GenerateVehicleRepairPlanResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GenerateVehicleRepairPlanResponseBodyData = None,
        error_message: str = None,
        http_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_message = error_message
        self.http_code = http_code
        self.request_id = request_id
        self.success = success

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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GenerateVehicleRepairPlanResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GenerateVehicleRepairPlanResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GenerateVehicleRepairPlanResponseBody = None,
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
            temp_model = GenerateVehicleRepairPlanResponseBody()
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
            temp_model = GetAsyncJobResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetVehicleRepairPlanRequest(TeaModel):
    def __init__(
        self,
        car_number_image: str = None,
        task_id: str = None,
        vin_code_image: str = None,
    ):
        self.car_number_image = car_number_image
        self.task_id = task_id
        self.vin_code_image = vin_code_image

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.car_number_image is not None:
            result['CarNumberImage'] = self.car_number_image
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.vin_code_image is not None:
            result['VinCodeImage'] = self.vin_code_image
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CarNumberImage') is not None:
            self.car_number_image = m.get('CarNumberImage')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('VinCodeImage') is not None:
            self.vin_code_image = m.get('VinCodeImage')
        return self


class GetVehicleRepairPlanResponseBodyDataRepairParts(TeaModel):
    def __init__(
        self,
        garage_type: str = None,
        oe_match: bool = None,
        out_standard_parts_id: str = None,
        out_standard_parts_name: str = None,
        part_name_match: bool = None,
        parts_std_code: str = None,
        parts_std_name: str = None,
        relation_type: str = None,
        repair_fee: str = None,
        repair_type: str = None,
        repair_type_name: str = None,
    ):
        self.garage_type = garage_type
        self.oe_match = oe_match
        self.out_standard_parts_id = out_standard_parts_id
        self.out_standard_parts_name = out_standard_parts_name
        self.part_name_match = part_name_match
        self.parts_std_code = parts_std_code
        self.parts_std_name = parts_std_name
        self.relation_type = relation_type
        self.repair_fee = repair_fee
        self.repair_type = repair_type
        self.repair_type_name = repair_type_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.garage_type is not None:
            result['GarageType'] = self.garage_type
        if self.oe_match is not None:
            result['OeMatch'] = self.oe_match
        if self.out_standard_parts_id is not None:
            result['OutStandardPartsId'] = self.out_standard_parts_id
        if self.out_standard_parts_name is not None:
            result['OutStandardPartsName'] = self.out_standard_parts_name
        if self.part_name_match is not None:
            result['PartNameMatch'] = self.part_name_match
        if self.parts_std_code is not None:
            result['PartsStdCode'] = self.parts_std_code
        if self.parts_std_name is not None:
            result['PartsStdName'] = self.parts_std_name
        if self.relation_type is not None:
            result['RelationType'] = self.relation_type
        if self.repair_fee is not None:
            result['RepairFee'] = self.repair_fee
        if self.repair_type is not None:
            result['RepairType'] = self.repair_type
        if self.repair_type_name is not None:
            result['RepairTypeName'] = self.repair_type_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GarageType') is not None:
            self.garage_type = m.get('GarageType')
        if m.get('OeMatch') is not None:
            self.oe_match = m.get('OeMatch')
        if m.get('OutStandardPartsId') is not None:
            self.out_standard_parts_id = m.get('OutStandardPartsId')
        if m.get('OutStandardPartsName') is not None:
            self.out_standard_parts_name = m.get('OutStandardPartsName')
        if m.get('PartNameMatch') is not None:
            self.part_name_match = m.get('PartNameMatch')
        if m.get('PartsStdCode') is not None:
            self.parts_std_code = m.get('PartsStdCode')
        if m.get('PartsStdName') is not None:
            self.parts_std_name = m.get('PartsStdName')
        if m.get('RelationType') is not None:
            self.relation_type = m.get('RelationType')
        if m.get('RepairFee') is not None:
            self.repair_fee = m.get('RepairFee')
        if m.get('RepairType') is not None:
            self.repair_type = m.get('RepairType')
        if m.get('RepairTypeName') is not None:
            self.repair_type_name = m.get('RepairTypeName')
        return self


class GetVehicleRepairPlanResponseBodyData(TeaModel):
    def __init__(
        self,
        frame_no: str = None,
        repair_parts: List[GetVehicleRepairPlanResponseBodyDataRepairParts] = None,
    ):
        self.frame_no = frame_no
        self.repair_parts = repair_parts

    def validate(self):
        if self.repair_parts:
            for k in self.repair_parts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.frame_no is not None:
            result['FrameNo'] = self.frame_no
        result['RepairParts'] = []
        if self.repair_parts is not None:
            for k in self.repair_parts:
                result['RepairParts'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FrameNo') is not None:
            self.frame_no = m.get('FrameNo')
        self.repair_parts = []
        if m.get('RepairParts') is not None:
            for k in m.get('RepairParts'):
                temp_model = GetVehicleRepairPlanResponseBodyDataRepairParts()
                self.repair_parts.append(temp_model.from_map(k))
        return self


class GetVehicleRepairPlanResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetVehicleRepairPlanResponseBodyData = None,
        error_message: str = None,
        http_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_message = error_message
        self.http_code = http_code
        self.request_id = request_id
        self.success = success

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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetVehicleRepairPlanResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetVehicleRepairPlanResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetVehicleRepairPlanResponseBody = None,
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
            temp_model = GetVehicleRepairPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeVehicleDamageRequest(TeaModel):
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


class RecognizeVehicleDamageAdvanceRequest(TeaModel):
    def __init__(
        self,
        image_urlobject: BinaryIO = None,
    ):
        self.image_urlobject = image_urlobject

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_urlobject is not None:
            result['ImageURLObject'] = self.image_urlobject
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURLObject') is not None:
            self.image_urlobject = m.get('ImageURLObject')
        return self


class RecognizeVehicleDamageResponseBodyDataElements(TeaModel):
    def __init__(
        self,
        boxes: List[int] = None,
        score: float = None,
        scores: List[float] = None,
        type: str = None,
    ):
        self.boxes = boxes
        self.score = score
        self.scores = scores
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
        if self.scores is not None:
            result['Scores'] = self.scores
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Boxes') is not None:
            self.boxes = m.get('Boxes')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('Scores') is not None:
            self.scores = m.get('Scores')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class RecognizeVehicleDamageResponseBodyData(TeaModel):
    def __init__(
        self,
        elements: List[RecognizeVehicleDamageResponseBodyDataElements] = None,
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
                temp_model = RecognizeVehicleDamageResponseBodyDataElements()
                self.elements.append(temp_model.from_map(k))
        return self


class RecognizeVehicleDamageResponseBody(TeaModel):
    def __init__(
        self,
        data: RecognizeVehicleDamageResponseBodyData = None,
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
            temp_model = RecognizeVehicleDamageResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RecognizeVehicleDamageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RecognizeVehicleDamageResponseBody = None,
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
            temp_model = RecognizeVehicleDamageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeVehicleDashboardRequest(TeaModel):
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


class RecognizeVehicleDashboardAdvanceRequest(TeaModel):
    def __init__(
        self,
        image_urlobject: BinaryIO = None,
    ):
        self.image_urlobject = image_urlobject

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_urlobject is not None:
            result['ImageURLObject'] = self.image_urlobject
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURLObject') is not None:
            self.image_urlobject = m.get('ImageURLObject')
        return self


class RecognizeVehicleDashboardResponseBodyDataElements(TeaModel):
    def __init__(
        self,
        boxes: List[float] = None,
        class_name: str = None,
        label: str = None,
        score: float = None,
    ):
        self.boxes = boxes
        self.class_name = class_name
        self.label = label
        self.score = score

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.boxes is not None:
            result['Boxes'] = self.boxes
        if self.class_name is not None:
            result['ClassName'] = self.class_name
        if self.label is not None:
            result['Label'] = self.label
        if self.score is not None:
            result['Score'] = self.score
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Boxes') is not None:
            self.boxes = m.get('Boxes')
        if m.get('ClassName') is not None:
            self.class_name = m.get('ClassName')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        return self


class RecognizeVehicleDashboardResponseBodyData(TeaModel):
    def __init__(
        self,
        elements: List[RecognizeVehicleDashboardResponseBodyDataElements] = None,
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
                temp_model = RecognizeVehicleDashboardResponseBodyDataElements()
                self.elements.append(temp_model.from_map(k))
        return self


class RecognizeVehicleDashboardResponseBody(TeaModel):
    def __init__(
        self,
        data: RecognizeVehicleDashboardResponseBodyData = None,
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
            temp_model = RecognizeVehicleDashboardResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RecognizeVehicleDashboardResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RecognizeVehicleDashboardResponseBody = None,
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
            temp_model = RecognizeVehicleDashboardResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeVehiclePartsRequest(TeaModel):
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


class RecognizeVehiclePartsAdvanceRequest(TeaModel):
    def __init__(
        self,
        image_urlobject: BinaryIO = None,
    ):
        self.image_urlobject = image_urlobject

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_urlobject is not None:
            result['ImageURLObject'] = self.image_urlobject
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURLObject') is not None:
            self.image_urlobject = m.get('ImageURLObject')
        return self


class RecognizeVehiclePartsResponseBodyDataElements(TeaModel):
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


class RecognizeVehiclePartsResponseBodyData(TeaModel):
    def __init__(
        self,
        elements: List[RecognizeVehiclePartsResponseBodyDataElements] = None,
        origin_shapes: List[int] = None,
    ):
        self.elements = elements
        self.origin_shapes = origin_shapes

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
        if self.origin_shapes is not None:
            result['OriginShapes'] = self.origin_shapes
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.elements = []
        if m.get('Elements') is not None:
            for k in m.get('Elements'):
                temp_model = RecognizeVehiclePartsResponseBodyDataElements()
                self.elements.append(temp_model.from_map(k))
        if m.get('OriginShapes') is not None:
            self.origin_shapes = m.get('OriginShapes')
        return self


class RecognizeVehiclePartsResponseBody(TeaModel):
    def __init__(
        self,
        data: RecognizeVehiclePartsResponseBodyData = None,
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
            temp_model = RecognizeVehiclePartsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RecognizeVehiclePartsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RecognizeVehiclePartsResponseBody = None,
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
            temp_model = RecognizeVehiclePartsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


