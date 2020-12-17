# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
try:
    from typing import BinaryIO, List
except ImportError:
    pass


class SegmentHDSkyRequest(TeaModel):
    def __init__(self, image_url=None):
        self.image_url = image_url      # type: str

    def validate(self):
        self.validate_required(self.image_url, 'image_url')

    def to_map(self):
        result = {}
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        return result

    def from_map(self, map={}):
        if map.get('ImageURL') is not None:
            self.image_url = map.get('ImageURL')
        return self


class SegmentHDSkyResponse(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id    # type: str
        self.data = data                # type: SegmentHDSkyResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = SegmentHDSkyResponseData()
            self.data = temp_model.from_map(map['Data'])
        return self


class SegmentHDSkyResponseData(TeaModel):
    def __init__(self, image_url=None):
        self.image_url = image_url      # type: str

    def validate(self):
        self.validate_required(self.image_url, 'image_url')

    def to_map(self):
        result = {}
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        return result

    def from_map(self, map={}):
        if map.get('ImageURL') is not None:
            self.image_url = map.get('ImageURL')
        return self


class SegmentHDSkyAdvanceRequest(TeaModel):
    def __init__(self, image_urlobject=None):
        self.image_urlobject = image_urlobject  # type: BinaryIO

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        result = {}
        if self.image_urlobject is not None:
            result['ImageURLObject'] = self.image_urlobject
        return result

    def from_map(self, map={}):
        if map.get('ImageURLObject') is not None:
            self.image_urlobject = map.get('ImageURLObject')
        return self


class SegmentHDCommonImageRequest(TeaModel):
    def __init__(self, image_url=None):
        self.image_url = image_url      # type: str

    def validate(self):
        self.validate_required(self.image_url, 'image_url')

    def to_map(self):
        result = {}
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        return result

    def from_map(self, map={}):
        if map.get('ImageUrl') is not None:
            self.image_url = map.get('ImageUrl')
        return self


class SegmentHDCommonImageResponse(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id    # type: str
        self.data = data                # type: SegmentHDCommonImageResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = SegmentHDCommonImageResponseData()
            self.data = temp_model.from_map(map['Data'])
        return self


class SegmentHDCommonImageResponseData(TeaModel):
    def __init__(self, image_url=None):
        self.image_url = image_url      # type: str

    def validate(self):
        self.validate_required(self.image_url, 'image_url')

    def to_map(self):
        result = {}
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        return result

    def from_map(self, map={}):
        if map.get('ImageUrl') is not None:
            self.image_url = map.get('ImageUrl')
        return self


class SegmentHDCommonImageAdvanceRequest(TeaModel):
    def __init__(self, image_url_object=None):
        self.image_url_object = image_url_object  # type: BinaryIO

    def validate(self):
        self.validate_required(self.image_url_object, 'image_url_object')

    def to_map(self):
        result = {}
        if self.image_url_object is not None:
            result['ImageUrlObject'] = self.image_url_object
        return result

    def from_map(self, map={}):
        if map.get('ImageUrlObject') is not None:
            self.image_url_object = map.get('ImageUrlObject')
        return self


class SegmentSkinRequest(TeaModel):
    def __init__(self, url=None):
        self.url = url                  # type: str

    def validate(self):
        self.validate_required(self.url, 'url')

    def to_map(self):
        result = {}
        if self.url is not None:
            result['URL'] = self.url
        return result

    def from_map(self, map={}):
        if map.get('URL') is not None:
            self.url = map.get('URL')
        return self


class SegmentSkinResponse(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id    # type: str
        self.data = data                # type: SegmentSkinResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = SegmentSkinResponseData()
            self.data = temp_model.from_map(map['Data'])
        return self


class SegmentSkinResponseData(TeaModel):
    def __init__(self, url=None):
        self.url = url                  # type: str

    def validate(self):
        self.validate_required(self.url, 'url')

    def to_map(self):
        result = {}
        if self.url is not None:
            result['URL'] = self.url
        return result

    def from_map(self, map={}):
        if map.get('URL') is not None:
            self.url = map.get('URL')
        return self


class SegmentSkinAdvanceRequest(TeaModel):
    def __init__(self, urlobject=None):
        self.urlobject = urlobject      # type: BinaryIO

    def validate(self):
        self.validate_required(self.urlobject, 'urlobject')

    def to_map(self):
        result = {}
        if self.urlobject is not None:
            result['URLObject'] = self.urlobject
        return result

    def from_map(self, map={}):
        if map.get('URLObject') is not None:
            self.urlobject = map.get('URLObject')
        return self


class ChangeSkyRequest(TeaModel):
    def __init__(self, image_url=None, replace_image_url=None):
        self.image_url = image_url      # type: str
        self.replace_image_url = replace_image_url  # type: str

    def validate(self):
        self.validate_required(self.image_url, 'image_url')
        self.validate_required(self.replace_image_url, 'replace_image_url')

    def to_map(self):
        result = {}
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        if self.replace_image_url is not None:
            result['ReplaceImageURL'] = self.replace_image_url
        return result

    def from_map(self, map={}):
        if map.get('ImageURL') is not None:
            self.image_url = map.get('ImageURL')
        if map.get('ReplaceImageURL') is not None:
            self.replace_image_url = map.get('ReplaceImageURL')
        return self


class ChangeSkyResponse(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id    # type: str
        self.data = data                # type: ChangeSkyResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = ChangeSkyResponseData()
            self.data = temp_model.from_map(map['Data'])
        return self


class ChangeSkyResponseData(TeaModel):
    def __init__(self, image_url=None):
        self.image_url = image_url      # type: str

    def validate(self):
        self.validate_required(self.image_url, 'image_url')

    def to_map(self):
        result = {}
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        return result

    def from_map(self, map={}):
        if map.get('ImageURL') is not None:
            self.image_url = map.get('ImageURL')
        return self


class ChangeSkyAdvanceRequest(TeaModel):
    def __init__(self, image_urlobject=None, replace_image_url=None):
        self.image_urlobject = image_urlobject  # type: BinaryIO
        self.replace_image_url = replace_image_url  # type: str

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')
        self.validate_required(self.replace_image_url, 'replace_image_url')

    def to_map(self):
        result = {}
        if self.image_urlobject is not None:
            result['ImageURLObject'] = self.image_urlobject
        if self.replace_image_url is not None:
            result['ReplaceImageURL'] = self.replace_image_url
        return result

    def from_map(self, map={}):
        if map.get('ImageURLObject') is not None:
            self.image_urlobject = map.get('ImageURLObject')
        if map.get('ReplaceImageURL') is not None:
            self.replace_image_url = map.get('ReplaceImageURL')
        return self


class SegmentLogoRequest(TeaModel):
    def __init__(self, image_url=None):
        self.image_url = image_url      # type: str

    def validate(self):
        self.validate_required(self.image_url, 'image_url')

    def to_map(self):
        result = {}
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        return result

    def from_map(self, map={}):
        if map.get('ImageURL') is not None:
            self.image_url = map.get('ImageURL')
        return self


class SegmentLogoResponse(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id    # type: str
        self.data = data                # type: SegmentLogoResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = SegmentLogoResponseData()
            self.data = temp_model.from_map(map['Data'])
        return self


class SegmentLogoResponseData(TeaModel):
    def __init__(self, image_url=None):
        self.image_url = image_url      # type: str

    def validate(self):
        self.validate_required(self.image_url, 'image_url')

    def to_map(self):
        result = {}
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        return result

    def from_map(self, map={}):
        if map.get('ImageURL') is not None:
            self.image_url = map.get('ImageURL')
        return self


class SegmentLogoAdvanceRequest(TeaModel):
    def __init__(self, image_urlobject=None):
        self.image_urlobject = image_urlobject  # type: BinaryIO

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        result = {}
        if self.image_urlobject is not None:
            result['ImageURLObject'] = self.image_urlobject
        return result

    def from_map(self, map={}):
        if map.get('ImageURLObject') is not None:
            self.image_urlobject = map.get('ImageURLObject')
        return self


class SegmentSceneRequest(TeaModel):
    def __init__(self, image_url=None):
        self.image_url = image_url      # type: str

    def validate(self):
        self.validate_required(self.image_url, 'image_url')

    def to_map(self):
        result = {}
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        return result

    def from_map(self, map={}):
        if map.get('ImageURL') is not None:
            self.image_url = map.get('ImageURL')
        return self


class SegmentSceneResponse(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id    # type: str
        self.data = data                # type: SegmentSceneResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = SegmentSceneResponseData()
            self.data = temp_model.from_map(map['Data'])
        return self


class SegmentSceneResponseData(TeaModel):
    def __init__(self, image_url=None):
        self.image_url = image_url      # type: str

    def validate(self):
        self.validate_required(self.image_url, 'image_url')

    def to_map(self):
        result = {}
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        return result

    def from_map(self, map={}):
        if map.get('ImageURL') is not None:
            self.image_url = map.get('ImageURL')
        return self


class SegmentSceneAdvanceRequest(TeaModel):
    def __init__(self, image_urlobject=None):
        self.image_urlobject = image_urlobject  # type: BinaryIO

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        result = {}
        if self.image_urlobject is not None:
            result['ImageURLObject'] = self.image_urlobject
        return result

    def from_map(self, map={}):
        if map.get('ImageURLObject') is not None:
            self.image_urlobject = map.get('ImageURLObject')
        return self


class SegmentFoodRequest(TeaModel):
    def __init__(self, image_url=None, return_form=None):
        self.image_url = image_url      # type: str
        self.return_form = return_form  # type: str

    def validate(self):
        self.validate_required(self.image_url, 'image_url')

    def to_map(self):
        result = {}
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        if self.return_form is not None:
            result['ReturnForm'] = self.return_form
        return result

    def from_map(self, map={}):
        if map.get('ImageURL') is not None:
            self.image_url = map.get('ImageURL')
        if map.get('ReturnForm') is not None:
            self.return_form = map.get('ReturnForm')
        return self


class SegmentFoodResponse(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id    # type: str
        self.data = data                # type: SegmentFoodResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = SegmentFoodResponseData()
            self.data = temp_model.from_map(map['Data'])
        return self


class SegmentFoodResponseData(TeaModel):
    def __init__(self, image_url=None):
        self.image_url = image_url      # type: str

    def validate(self):
        self.validate_required(self.image_url, 'image_url')

    def to_map(self):
        result = {}
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        return result

    def from_map(self, map={}):
        if map.get('ImageURL') is not None:
            self.image_url = map.get('ImageURL')
        return self


class SegmentFoodAdvanceRequest(TeaModel):
    def __init__(self, image_urlobject=None, return_form=None):
        self.image_urlobject = image_urlobject  # type: BinaryIO
        self.return_form = return_form  # type: str

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        result = {}
        if self.image_urlobject is not None:
            result['ImageURLObject'] = self.image_urlobject
        if self.return_form is not None:
            result['ReturnForm'] = self.return_form
        return result

    def from_map(self, map={}):
        if map.get('ImageURLObject') is not None:
            self.image_urlobject = map.get('ImageURLObject')
        if map.get('ReturnForm') is not None:
            self.return_form = map.get('ReturnForm')
        return self


class SegmentClothRequest(TeaModel):
    def __init__(self, image_url=None):
        self.image_url = image_url      # type: str

    def validate(self):
        self.validate_required(self.image_url, 'image_url')

    def to_map(self):
        result = {}
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        return result

    def from_map(self, map={}):
        if map.get('ImageURL') is not None:
            self.image_url = map.get('ImageURL')
        return self


class SegmentClothResponse(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id    # type: str
        self.data = data                # type: SegmentClothResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = SegmentClothResponseData()
            self.data = temp_model.from_map(map['Data'])
        return self


class SegmentClothResponseDataElements(TeaModel):
    def __init__(self, image_url=None):
        self.image_url = image_url      # type: str

    def validate(self):
        self.validate_required(self.image_url, 'image_url')

    def to_map(self):
        result = {}
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        return result

    def from_map(self, map={}):
        if map.get('ImageURL') is not None:
            self.image_url = map.get('ImageURL')
        return self


class SegmentClothResponseData(TeaModel):
    def __init__(self, elements=None):
        self.elements = elements        # type: List[SegmentClothResponseDataElements]

    def validate(self):
        self.validate_required(self.elements, 'elements')
        if self.elements:
            for k in self.elements:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Elements'] = []
        if self.elements is not None:
            for k in self.elements:
                result['Elements'].append(k.to_map() if k else None)
        return result

    def from_map(self, map={}):
        self.elements = []
        if map.get('Elements') is not None:
            for k in map.get('Elements'):
                temp_model = SegmentClothResponseDataElements()
                self.elements.append(temp_model.from_map(k))
        return self


class SegmentClothAdvanceRequest(TeaModel):
    def __init__(self, image_urlobject=None):
        self.image_urlobject = image_urlobject  # type: BinaryIO

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        result = {}
        if self.image_urlobject is not None:
            result['ImageURLObject'] = self.image_urlobject
        return result

    def from_map(self, map={}):
        if map.get('ImageURLObject') is not None:
            self.image_urlobject = map.get('ImageURLObject')
        return self


class SegmentAnimalRequest(TeaModel):
    def __init__(self, image_url=None):
        self.image_url = image_url      # type: str

    def validate(self):
        self.validate_required(self.image_url, 'image_url')

    def to_map(self):
        result = {}
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        return result

    def from_map(self, map={}):
        if map.get('ImageURL') is not None:
            self.image_url = map.get('ImageURL')
        return self


class SegmentAnimalResponse(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id    # type: str
        self.data = data                # type: SegmentAnimalResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = SegmentAnimalResponseData()
            self.data = temp_model.from_map(map['Data'])
        return self


class SegmentAnimalResponseData(TeaModel):
    def __init__(self, image_url=None):
        self.image_url = image_url      # type: str

    def validate(self):
        self.validate_required(self.image_url, 'image_url')

    def to_map(self):
        result = {}
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        return result

    def from_map(self, map={}):
        if map.get('ImageURL') is not None:
            self.image_url = map.get('ImageURL')
        return self


class SegmentAnimalAdvanceRequest(TeaModel):
    def __init__(self, image_urlobject=None):
        self.image_urlobject = image_urlobject  # type: BinaryIO

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        result = {}
        if self.image_urlobject is not None:
            result['ImageURLObject'] = self.image_urlobject
        return result

    def from_map(self, map={}):
        if map.get('ImageURLObject') is not None:
            self.image_urlobject = map.get('ImageURLObject')
        return self


class SegmentHDBodyRequest(TeaModel):
    def __init__(self, image_url=None):
        self.image_url = image_url      # type: str

    def validate(self):
        self.validate_required(self.image_url, 'image_url')

    def to_map(self):
        result = {}
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        return result

    def from_map(self, map={}):
        if map.get('ImageURL') is not None:
            self.image_url = map.get('ImageURL')
        return self


class SegmentHDBodyResponse(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id    # type: str
        self.data = data                # type: SegmentHDBodyResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = SegmentHDBodyResponseData()
            self.data = temp_model.from_map(map['Data'])
        return self


class SegmentHDBodyResponseData(TeaModel):
    def __init__(self, image_url=None):
        self.image_url = image_url      # type: str

    def validate(self):
        self.validate_required(self.image_url, 'image_url')

    def to_map(self):
        result = {}
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        return result

    def from_map(self, map={}):
        if map.get('ImageURL') is not None:
            self.image_url = map.get('ImageURL')
        return self


class SegmentHDBodyAdvanceRequest(TeaModel):
    def __init__(self, image_urlobject=None):
        self.image_urlobject = image_urlobject  # type: BinaryIO

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        result = {}
        if self.image_urlobject is not None:
            result['ImageURLObject'] = self.image_urlobject
        return result

    def from_map(self, map={}):
        if map.get('ImageURLObject') is not None:
            self.image_urlobject = map.get('ImageURLObject')
        return self


class SegmentSkyRequest(TeaModel):
    def __init__(self, image_url=None):
        self.image_url = image_url      # type: str

    def validate(self):
        self.validate_required(self.image_url, 'image_url')

    def to_map(self):
        result = {}
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        return result

    def from_map(self, map={}):
        if map.get('ImageURL') is not None:
            self.image_url = map.get('ImageURL')
        return self


class SegmentSkyResponse(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id    # type: str
        self.data = data                # type: SegmentSkyResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = SegmentSkyResponseData()
            self.data = temp_model.from_map(map['Data'])
        return self


class SegmentSkyResponseData(TeaModel):
    def __init__(self, image_url=None):
        self.image_url = image_url      # type: str

    def validate(self):
        self.validate_required(self.image_url, 'image_url')

    def to_map(self):
        result = {}
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        return result

    def from_map(self, map={}):
        if map.get('ImageURL') is not None:
            self.image_url = map.get('ImageURL')
        return self


class SegmentSkyAdvanceRequest(TeaModel):
    def __init__(self, image_urlobject=None):
        self.image_urlobject = image_urlobject  # type: BinaryIO

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        result = {}
        if self.image_urlobject is not None:
            result['ImageURLObject'] = self.image_urlobject
        return result

    def from_map(self, map={}):
        if map.get('ImageURLObject') is not None:
            self.image_urlobject = map.get('ImageURLObject')
        return self


class GetAsyncJobResultRequest(TeaModel):
    def __init__(self, job_id=None):
        self.job_id = job_id            # type: str

    def validate(self):
        self.validate_required(self.job_id, 'job_id')

    def to_map(self):
        result = {}
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, map={}):
        if map.get('JobId') is not None:
            self.job_id = map.get('JobId')
        return self


class GetAsyncJobResultResponse(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id    # type: str
        self.data = data                # type: GetAsyncJobResultResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = GetAsyncJobResultResponseData()
            self.data = temp_model.from_map(map['Data'])
        return self


class GetAsyncJobResultResponseData(TeaModel):
    def __init__(self, error_code=None, error_message=None, job_id=None, result=None, status=None):
        self.error_code = error_code    # type: str
        self.error_message = error_message  # type: str
        self.job_id = job_id            # type: str
        self.result = result            # type: str
        self.status = status            # type: str

    def validate(self):
        self.validate_required(self.error_code, 'error_code')
        self.validate_required(self.error_message, 'error_message')
        self.validate_required(self.job_id, 'job_id')
        self.validate_required(self.result, 'result')
        self.validate_required(self.status, 'status')

    def to_map(self):
        result = {}
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

    def from_map(self, map={}):
        if map.get('ErrorCode') is not None:
            self.error_code = map.get('ErrorCode')
        if map.get('ErrorMessage') is not None:
            self.error_message = map.get('ErrorMessage')
        if map.get('JobId') is not None:
            self.job_id = map.get('JobId')
        if map.get('Result') is not None:
            self.result = map.get('Result')
        if map.get('Status') is not None:
            self.status = map.get('Status')
        return self


class SegmentFurnitureRequest(TeaModel):
    def __init__(self, image_url=None):
        self.image_url = image_url      # type: str

    def validate(self):
        self.validate_required(self.image_url, 'image_url')

    def to_map(self):
        result = {}
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        return result

    def from_map(self, map={}):
        if map.get('ImageURL') is not None:
            self.image_url = map.get('ImageURL')
        return self


class SegmentFurnitureResponse(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id    # type: str
        self.data = data                # type: SegmentFurnitureResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = SegmentFurnitureResponseData()
            self.data = temp_model.from_map(map['Data'])
        return self


class SegmentFurnitureResponseDataElements(TeaModel):
    def __init__(self, image_url=None):
        self.image_url = image_url      # type: str

    def validate(self):
        self.validate_required(self.image_url, 'image_url')

    def to_map(self):
        result = {}
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        return result

    def from_map(self, map={}):
        if map.get('ImageURL') is not None:
            self.image_url = map.get('ImageURL')
        return self


class SegmentFurnitureResponseData(TeaModel):
    def __init__(self, elements=None):
        self.elements = elements        # type: List[SegmentFurnitureResponseDataElements]

    def validate(self):
        self.validate_required(self.elements, 'elements')
        if self.elements:
            for k in self.elements:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Elements'] = []
        if self.elements is not None:
            for k in self.elements:
                result['Elements'].append(k.to_map() if k else None)
        return result

    def from_map(self, map={}):
        self.elements = []
        if map.get('Elements') is not None:
            for k in map.get('Elements'):
                temp_model = SegmentFurnitureResponseDataElements()
                self.elements.append(temp_model.from_map(k))
        return self


class SegmentFurnitureAdvanceRequest(TeaModel):
    def __init__(self, image_urlobject=None):
        self.image_urlobject = image_urlobject  # type: BinaryIO

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        result = {}
        if self.image_urlobject is not None:
            result['ImageURLObject'] = self.image_urlobject
        return result

    def from_map(self, map={}):
        if map.get('ImageURLObject') is not None:
            self.image_urlobject = map.get('ImageURLObject')
        return self


class RefineMaskRequest(TeaModel):
    def __init__(self, mask_image_url=None, image_url=None):
        self.mask_image_url = mask_image_url  # type: str
        self.image_url = image_url      # type: str

    def validate(self):
        self.validate_required(self.mask_image_url, 'mask_image_url')
        self.validate_required(self.image_url, 'image_url')

    def to_map(self):
        result = {}
        if self.mask_image_url is not None:
            result['MaskImageURL'] = self.mask_image_url
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        return result

    def from_map(self, map={}):
        if map.get('MaskImageURL') is not None:
            self.mask_image_url = map.get('MaskImageURL')
        if map.get('ImageURL') is not None:
            self.image_url = map.get('ImageURL')
        return self


class RefineMaskResponse(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id    # type: str
        self.data = data                # type: RefineMaskResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = RefineMaskResponseData()
            self.data = temp_model.from_map(map['Data'])
        return self


class RefineMaskResponseDataElements(TeaModel):
    def __init__(self, image_url=None):
        self.image_url = image_url      # type: str

    def validate(self):
        self.validate_required(self.image_url, 'image_url')

    def to_map(self):
        result = {}
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        return result

    def from_map(self, map={}):
        if map.get('ImageURL') is not None:
            self.image_url = map.get('ImageURL')
        return self


class RefineMaskResponseData(TeaModel):
    def __init__(self, elements=None):
        self.elements = elements        # type: List[RefineMaskResponseDataElements]

    def validate(self):
        self.validate_required(self.elements, 'elements')
        if self.elements:
            for k in self.elements:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Elements'] = []
        if self.elements is not None:
            for k in self.elements:
                result['Elements'].append(k.to_map() if k else None)
        return result

    def from_map(self, map={}):
        self.elements = []
        if map.get('Elements') is not None:
            for k in map.get('Elements'):
                temp_model = RefineMaskResponseDataElements()
                self.elements.append(temp_model.from_map(k))
        return self


class RefineMaskAdvanceRequest(TeaModel):
    def __init__(self, image_urlobject=None, mask_image_url=None):
        self.image_urlobject = image_urlobject  # type: BinaryIO
        self.mask_image_url = mask_image_url  # type: str

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')
        self.validate_required(self.mask_image_url, 'mask_image_url')

    def to_map(self):
        result = {}
        if self.image_urlobject is not None:
            result['ImageURLObject'] = self.image_urlobject
        if self.mask_image_url is not None:
            result['MaskImageURL'] = self.mask_image_url
        return result

    def from_map(self, map={}):
        if map.get('ImageURLObject') is not None:
            self.image_urlobject = map.get('ImageURLObject')
        if map.get('MaskImageURL') is not None:
            self.mask_image_url = map.get('MaskImageURL')
        return self


class ParseFaceRequest(TeaModel):
    def __init__(self, image_url=None):
        self.image_url = image_url      # type: str

    def validate(self):
        self.validate_required(self.image_url, 'image_url')

    def to_map(self):
        result = {}
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        return result

    def from_map(self, map={}):
        if map.get('ImageURL') is not None:
            self.image_url = map.get('ImageURL')
        return self


class ParseFaceResponse(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id    # type: str
        self.data = data                # type: ParseFaceResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = ParseFaceResponseData()
            self.data = temp_model.from_map(map['Data'])
        return self


class ParseFaceResponseDataElements(TeaModel):
    def __init__(self, name=None, image_url=None):
        self.name = name                # type: str
        self.image_url = image_url      # type: str

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.image_url, 'image_url')

    def to_map(self):
        result = {}
        if self.name is not None:
            result['Name'] = self.name
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        return result

    def from_map(self, map={}):
        if map.get('Name') is not None:
            self.name = map.get('Name')
        if map.get('ImageURL') is not None:
            self.image_url = map.get('ImageURL')
        return self


class ParseFaceResponseData(TeaModel):
    def __init__(self, origin_image_url=None, elements=None):
        self.origin_image_url = origin_image_url  # type: str
        self.elements = elements        # type: List[ParseFaceResponseDataElements]

    def validate(self):
        self.validate_required(self.origin_image_url, 'origin_image_url')
        self.validate_required(self.elements, 'elements')
        if self.elements:
            for k in self.elements:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        if self.origin_image_url is not None:
            result['OriginImageURL'] = self.origin_image_url
        result['Elements'] = []
        if self.elements is not None:
            for k in self.elements:
                result['Elements'].append(k.to_map() if k else None)
        return result

    def from_map(self, map={}):
        if map.get('OriginImageURL') is not None:
            self.origin_image_url = map.get('OriginImageURL')
        self.elements = []
        if map.get('Elements') is not None:
            for k in map.get('Elements'):
                temp_model = ParseFaceResponseDataElements()
                self.elements.append(temp_model.from_map(k))
        return self


class ParseFaceAdvanceRequest(TeaModel):
    def __init__(self, image_urlobject=None):
        self.image_urlobject = image_urlobject  # type: BinaryIO

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        result = {}
        if self.image_urlobject is not None:
            result['ImageURLObject'] = self.image_urlobject
        return result

    def from_map(self, map={}):
        if map.get('ImageURLObject') is not None:
            self.image_urlobject = map.get('ImageURLObject')
        return self


class SegmentVehicleRequest(TeaModel):
    def __init__(self, image_url=None):
        self.image_url = image_url      # type: str

    def validate(self):
        self.validate_required(self.image_url, 'image_url')

    def to_map(self):
        result = {}
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        return result

    def from_map(self, map={}):
        if map.get('ImageURL') is not None:
            self.image_url = map.get('ImageURL')
        return self


class SegmentVehicleResponse(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id    # type: str
        self.data = data                # type: SegmentVehicleResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = SegmentVehicleResponseData()
            self.data = temp_model.from_map(map['Data'])
        return self


class SegmentVehicleResponseDataElements(TeaModel):
    def __init__(self, origin_image_url=None, image_url=None):
        self.origin_image_url = origin_image_url  # type: str
        self.image_url = image_url      # type: str

    def validate(self):
        self.validate_required(self.origin_image_url, 'origin_image_url')
        self.validate_required(self.image_url, 'image_url')

    def to_map(self):
        result = {}
        if self.origin_image_url is not None:
            result['OriginImageURL'] = self.origin_image_url
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        return result

    def from_map(self, map={}):
        if map.get('OriginImageURL') is not None:
            self.origin_image_url = map.get('OriginImageURL')
        if map.get('ImageURL') is not None:
            self.image_url = map.get('ImageURL')
        return self


class SegmentVehicleResponseData(TeaModel):
    def __init__(self, elements=None):
        self.elements = elements        # type: List[SegmentVehicleResponseDataElements]

    def validate(self):
        self.validate_required(self.elements, 'elements')
        if self.elements:
            for k in self.elements:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Elements'] = []
        if self.elements is not None:
            for k in self.elements:
                result['Elements'].append(k.to_map() if k else None)
        return result

    def from_map(self, map={}):
        self.elements = []
        if map.get('Elements') is not None:
            for k in map.get('Elements'):
                temp_model = SegmentVehicleResponseDataElements()
                self.elements.append(temp_model.from_map(k))
        return self


class SegmentVehicleAdvanceRequest(TeaModel):
    def __init__(self, image_urlobject=None):
        self.image_urlobject = image_urlobject  # type: BinaryIO

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        result = {}
        if self.image_urlobject is not None:
            result['ImageURLObject'] = self.image_urlobject
        return result

    def from_map(self, map={}):
        if map.get('ImageURLObject') is not None:
            self.image_urlobject = map.get('ImageURLObject')
        return self


class SegmentHairRequest(TeaModel):
    def __init__(self, image_url=None):
        self.image_url = image_url      # type: str

    def validate(self):
        self.validate_required(self.image_url, 'image_url')

    def to_map(self):
        result = {}
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        return result

    def from_map(self, map={}):
        if map.get('ImageURL') is not None:
            self.image_url = map.get('ImageURL')
        return self


class SegmentHairResponse(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id    # type: str
        self.data = data                # type: SegmentHairResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = SegmentHairResponseData()
            self.data = temp_model.from_map(map['Data'])
        return self


class SegmentHairResponseDataElements(TeaModel):
    def __init__(self, image_url=None, x=None, y=None, width=None, height=None):
        self.image_url = image_url      # type: str
        self.x = x                      # type: int
        self.y = y                      # type: int
        self.width = width              # type: int
        self.height = height            # type: int

    def validate(self):
        self.validate_required(self.image_url, 'image_url')
        self.validate_required(self.x, 'x')
        self.validate_required(self.y, 'y')
        self.validate_required(self.width, 'width')
        self.validate_required(self.height, 'height')

    def to_map(self):
        result = {}
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        if self.x is not None:
            result['X'] = self.x
        if self.y is not None:
            result['Y'] = self.y
        if self.width is not None:
            result['Width'] = self.width
        if self.height is not None:
            result['Height'] = self.height
        return result

    def from_map(self, map={}):
        if map.get('ImageURL') is not None:
            self.image_url = map.get('ImageURL')
        if map.get('X') is not None:
            self.x = map.get('X')
        if map.get('Y') is not None:
            self.y = map.get('Y')
        if map.get('Width') is not None:
            self.width = map.get('Width')
        if map.get('Height') is not None:
            self.height = map.get('Height')
        return self


class SegmentHairResponseData(TeaModel):
    def __init__(self, elements=None):
        self.elements = elements        # type: List[SegmentHairResponseDataElements]

    def validate(self):
        self.validate_required(self.elements, 'elements')
        if self.elements:
            for k in self.elements:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Elements'] = []
        if self.elements is not None:
            for k in self.elements:
                result['Elements'].append(k.to_map() if k else None)
        return result

    def from_map(self, map={}):
        self.elements = []
        if map.get('Elements') is not None:
            for k in map.get('Elements'):
                temp_model = SegmentHairResponseDataElements()
                self.elements.append(temp_model.from_map(k))
        return self


class SegmentHairAdvanceRequest(TeaModel):
    def __init__(self, image_urlobject=None):
        self.image_urlobject = image_urlobject  # type: BinaryIO

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        result = {}
        if self.image_urlobject is not None:
            result['ImageURLObject'] = self.image_urlobject
        return result

    def from_map(self, map={}):
        if map.get('ImageURLObject') is not None:
            self.image_urlobject = map.get('ImageURLObject')
        return self


class SegmentFaceRequest(TeaModel):
    def __init__(self, image_url=None):
        self.image_url = image_url      # type: str

    def validate(self):
        self.validate_required(self.image_url, 'image_url')

    def to_map(self):
        result = {}
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        return result

    def from_map(self, map={}):
        if map.get('ImageURL') is not None:
            self.image_url = map.get('ImageURL')
        return self


class SegmentFaceResponse(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id    # type: str
        self.data = data                # type: SegmentFaceResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = SegmentFaceResponseData()
            self.data = temp_model.from_map(map['Data'])
        return self


class SegmentFaceResponseDataElements(TeaModel):
    def __init__(self, image_url=None, x=None, y=None, width=None, height=None):
        self.image_url = image_url      # type: str
        self.x = x                      # type: int
        self.y = y                      # type: int
        self.width = width              # type: int
        self.height = height            # type: int

    def validate(self):
        self.validate_required(self.image_url, 'image_url')
        self.validate_required(self.x, 'x')
        self.validate_required(self.y, 'y')
        self.validate_required(self.width, 'width')
        self.validate_required(self.height, 'height')

    def to_map(self):
        result = {}
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        if self.x is not None:
            result['X'] = self.x
        if self.y is not None:
            result['Y'] = self.y
        if self.width is not None:
            result['Width'] = self.width
        if self.height is not None:
            result['Height'] = self.height
        return result

    def from_map(self, map={}):
        if map.get('ImageURL') is not None:
            self.image_url = map.get('ImageURL')
        if map.get('X') is not None:
            self.x = map.get('X')
        if map.get('Y') is not None:
            self.y = map.get('Y')
        if map.get('Width') is not None:
            self.width = map.get('Width')
        if map.get('Height') is not None:
            self.height = map.get('Height')
        return self


class SegmentFaceResponseData(TeaModel):
    def __init__(self, elements=None):
        self.elements = elements        # type: List[SegmentFaceResponseDataElements]

    def validate(self):
        self.validate_required(self.elements, 'elements')
        if self.elements:
            for k in self.elements:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Elements'] = []
        if self.elements is not None:
            for k in self.elements:
                result['Elements'].append(k.to_map() if k else None)
        return result

    def from_map(self, map={}):
        self.elements = []
        if map.get('Elements') is not None:
            for k in map.get('Elements'):
                temp_model = SegmentFaceResponseDataElements()
                self.elements.append(temp_model.from_map(k))
        return self


class SegmentFaceAdvanceRequest(TeaModel):
    def __init__(self, image_urlobject=None):
        self.image_urlobject = image_urlobject  # type: BinaryIO

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        result = {}
        if self.image_urlobject is not None:
            result['ImageURLObject'] = self.image_urlobject
        return result

    def from_map(self, map={}):
        if map.get('ImageURLObject') is not None:
            self.image_urlobject = map.get('ImageURLObject')
        return self


class SegmentHeadRequest(TeaModel):
    def __init__(self, image_url=None, return_form=None):
        self.image_url = image_url      # type: str
        self.return_form = return_form  # type: str

    def validate(self):
        self.validate_required(self.image_url, 'image_url')

    def to_map(self):
        result = {}
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        if self.return_form is not None:
            result['ReturnForm'] = self.return_form
        return result

    def from_map(self, map={}):
        if map.get('ImageURL') is not None:
            self.image_url = map.get('ImageURL')
        if map.get('ReturnForm') is not None:
            self.return_form = map.get('ReturnForm')
        return self


class SegmentHeadResponse(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id    # type: str
        self.data = data                # type: SegmentHeadResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = SegmentHeadResponseData()
            self.data = temp_model.from_map(map['Data'])
        return self


class SegmentHeadResponseDataElements(TeaModel):
    def __init__(self, x=None, y=None, image_url=None, height=None, width=None):
        self.x = x                      # type: int
        self.y = y                      # type: int
        self.image_url = image_url      # type: str
        self.height = height            # type: int
        self.width = width              # type: int

    def validate(self):
        self.validate_required(self.x, 'x')
        self.validate_required(self.y, 'y')
        self.validate_required(self.image_url, 'image_url')
        self.validate_required(self.height, 'height')
        self.validate_required(self.width, 'width')

    def to_map(self):
        result = {}
        if self.x is not None:
            result['X'] = self.x
        if self.y is not None:
            result['Y'] = self.y
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        if self.height is not None:
            result['Height'] = self.height
        if self.width is not None:
            result['Width'] = self.width
        return result

    def from_map(self, map={}):
        if map.get('X') is not None:
            self.x = map.get('X')
        if map.get('Y') is not None:
            self.y = map.get('Y')
        if map.get('ImageURL') is not None:
            self.image_url = map.get('ImageURL')
        if map.get('Height') is not None:
            self.height = map.get('Height')
        if map.get('Width') is not None:
            self.width = map.get('Width')
        return self


class SegmentHeadResponseData(TeaModel):
    def __init__(self, elements=None):
        self.elements = elements        # type: List[SegmentHeadResponseDataElements]

    def validate(self):
        self.validate_required(self.elements, 'elements')
        if self.elements:
            for k in self.elements:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Elements'] = []
        if self.elements is not None:
            for k in self.elements:
                result['Elements'].append(k.to_map() if k else None)
        return result

    def from_map(self, map={}):
        self.elements = []
        if map.get('Elements') is not None:
            for k in map.get('Elements'):
                temp_model = SegmentHeadResponseDataElements()
                self.elements.append(temp_model.from_map(k))
        return self


class SegmentHeadAdvanceRequest(TeaModel):
    def __init__(self, image_urlobject=None, return_form=None):
        self.image_urlobject = image_urlobject  # type: BinaryIO
        self.return_form = return_form  # type: str

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        result = {}
        if self.image_urlobject is not None:
            result['ImageURLObject'] = self.image_urlobject
        if self.return_form is not None:
            result['ReturnForm'] = self.return_form
        return result

    def from_map(self, map={}):
        if map.get('ImageURLObject') is not None:
            self.image_urlobject = map.get('ImageURLObject')
        if map.get('ReturnForm') is not None:
            self.return_form = map.get('ReturnForm')
        return self


class SegmentCommodityRequest(TeaModel):
    def __init__(self, image_url=None, return_form=None):
        self.image_url = image_url      # type: str
        self.return_form = return_form  # type: str

    def validate(self):
        self.validate_required(self.image_url, 'image_url')

    def to_map(self):
        result = {}
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        if self.return_form is not None:
            result['ReturnForm'] = self.return_form
        return result

    def from_map(self, map={}):
        if map.get('ImageURL') is not None:
            self.image_url = map.get('ImageURL')
        if map.get('ReturnForm') is not None:
            self.return_form = map.get('ReturnForm')
        return self


class SegmentCommodityResponse(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id    # type: str
        self.data = data                # type: SegmentCommodityResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = SegmentCommodityResponseData()
            self.data = temp_model.from_map(map['Data'])
        return self


class SegmentCommodityResponseData(TeaModel):
    def __init__(self, image_url=None):
        self.image_url = image_url      # type: str

    def validate(self):
        self.validate_required(self.image_url, 'image_url')

    def to_map(self):
        result = {}
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        return result

    def from_map(self, map={}):
        if map.get('ImageURL') is not None:
            self.image_url = map.get('ImageURL')
        return self


class SegmentCommodityAdvanceRequest(TeaModel):
    def __init__(self, image_urlobject=None, return_form=None):
        self.image_urlobject = image_urlobject  # type: BinaryIO
        self.return_form = return_form  # type: str

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        result = {}
        if self.image_urlobject is not None:
            result['ImageURLObject'] = self.image_urlobject
        if self.return_form is not None:
            result['ReturnForm'] = self.return_form
        return result

    def from_map(self, map={}):
        if map.get('ImageURLObject') is not None:
            self.image_urlobject = map.get('ImageURLObject')
        if map.get('ReturnForm') is not None:
            self.return_form = map.get('ReturnForm')
        return self


class SegmentBodyRequest(TeaModel):
    def __init__(self, image_url=None, async_=None, return_form=None):
        self.image_url = image_url      # type: str
        self.async_ = async_            # type: bool
        self.return_form = return_form  # type: str

    def validate(self):
        self.validate_required(self.image_url, 'image_url')

    def to_map(self):
        result = {}
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        if self.async_ is not None:
            result['Async'] = self.async_
        if self.return_form is not None:
            result['ReturnForm'] = self.return_form
        return result

    def from_map(self, map={}):
        if map.get('ImageURL') is not None:
            self.image_url = map.get('ImageURL')
        if map.get('Async') is not None:
            self.async_ = map.get('Async')
        if map.get('ReturnForm') is not None:
            self.return_form = map.get('ReturnForm')
        return self


class SegmentBodyResponse(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id    # type: str
        self.data = data                # type: SegmentBodyResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = SegmentBodyResponseData()
            self.data = temp_model.from_map(map['Data'])
        return self


class SegmentBodyResponseData(TeaModel):
    def __init__(self, image_url=None):
        self.image_url = image_url      # type: str

    def validate(self):
        self.validate_required(self.image_url, 'image_url')

    def to_map(self):
        result = {}
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        return result

    def from_map(self, map={}):
        if map.get('ImageURL') is not None:
            self.image_url = map.get('ImageURL')
        return self


class SegmentBodyAdvanceRequest(TeaModel):
    def __init__(self, image_urlobject=None, async_=None, return_form=None):
        self.image_urlobject = image_urlobject  # type: BinaryIO
        self.async_ = async_            # type: bool
        self.return_form = return_form  # type: str

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        result = {}
        if self.image_urlobject is not None:
            result['ImageURLObject'] = self.image_urlobject
        if self.async_ is not None:
            result['Async'] = self.async_
        if self.return_form is not None:
            result['ReturnForm'] = self.return_form
        return result

    def from_map(self, map={}):
        if map.get('ImageURLObject') is not None:
            self.image_urlobject = map.get('ImageURLObject')
        if map.get('Async') is not None:
            self.async_ = map.get('Async')
        if map.get('ReturnForm') is not None:
            self.return_form = map.get('ReturnForm')
        return self


class SegmentCommonImageRequest(TeaModel):
    def __init__(self, image_url=None):
        self.image_url = image_url      # type: str

    def validate(self):
        self.validate_required(self.image_url, 'image_url')

    def to_map(self):
        result = {}
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        return result

    def from_map(self, map={}):
        if map.get('ImageURL') is not None:
            self.image_url = map.get('ImageURL')
        return self


class SegmentCommonImageResponse(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id    # type: str
        self.data = data                # type: SegmentCommonImageResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = SegmentCommonImageResponseData()
            self.data = temp_model.from_map(map['Data'])
        return self


class SegmentCommonImageResponseData(TeaModel):
    def __init__(self, image_url=None):
        self.image_url = image_url      # type: str

    def validate(self):
        self.validate_required(self.image_url, 'image_url')

    def to_map(self):
        result = {}
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        return result

    def from_map(self, map={}):
        if map.get('ImageURL') is not None:
            self.image_url = map.get('ImageURL')
        return self


class SegmentCommonImageAdvanceRequest(TeaModel):
    def __init__(self, image_urlobject=None):
        self.image_urlobject = image_urlobject  # type: BinaryIO

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        result = {}
        if self.image_urlobject is not None:
            result['ImageURLObject'] = self.image_urlobject
        return result

    def from_map(self, map={}):
        if map.get('ImageURLObject') is not None:
            self.image_urlobject = map.get('ImageURLObject')
        return self
