# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
try:
    from typing import BinaryIO, List
except ImportError:
    pass


class CountCrowdRequest(TeaModel):
    def __init__(self, image_url=None, is_show=None):
        self.image_url = image_url      # type: str
        self.is_show = is_show          # type: bool

    def validate(self):
        self.validate_required(self.image_url, 'image_url')

    def to_map(self):
        result = {}
        result['ImageURL'] = self.image_url
        result['IsShow'] = self.is_show
        return result

    def from_map(self, map={}):
        self.image_url = map.get('ImageURL')
        self.is_show = map.get('IsShow')
        return self


class CountCrowdResponse(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id    # type: str
        self.data = data                # type: CountCrowdResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = CountCrowdResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class CountCrowdResponseData(TeaModel):
    def __init__(self, people_number=None, hot_map=None):
        self.people_number = people_number  # type: int
        self.hot_map = hot_map          # type: str

    def validate(self):
        self.validate_required(self.people_number, 'people_number')
        self.validate_required(self.hot_map, 'hot_map')

    def to_map(self):
        result = {}
        result['PeopleNumber'] = self.people_number
        result['HotMap'] = self.hot_map
        return result

    def from_map(self, map={}):
        self.people_number = map.get('PeopleNumber')
        self.hot_map = map.get('HotMap')
        return self


class CountCrowdAdvanceRequest(TeaModel):
    def __init__(self, image_urlobject=None, is_show=None):
        self.image_urlobject = image_urlobject  # type: BinaryIO
        self.is_show = is_show          # type: bool

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        result = {}
        result['ImageURLObject'] = self.image_urlobject
        result['IsShow'] = self.is_show
        return result

    def from_map(self, map={}):
        self.image_urlobject = map.get('ImageURLObject')
        self.is_show = map.get('IsShow')
        return self


class GenerateHumanAnimeStyleRequest(TeaModel):
    def __init__(self, image_url=None):
        self.image_url = image_url      # type: str

    def validate(self):
        self.validate_required(self.image_url, 'image_url')

    def to_map(self):
        result = {}
        result['ImageURL'] = self.image_url
        return result

    def from_map(self, map={}):
        self.image_url = map.get('ImageURL')
        return self


class GenerateHumanAnimeStyleResponse(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id    # type: str
        self.data = data                # type: GenerateHumanAnimeStyleResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = GenerateHumanAnimeStyleResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class GenerateHumanAnimeStyleResponseData(TeaModel):
    def __init__(self, image_url=None):
        self.image_url = image_url      # type: str

    def validate(self):
        self.validate_required(self.image_url, 'image_url')

    def to_map(self):
        result = {}
        result['ImageURL'] = self.image_url
        return result

    def from_map(self, map={}):
        self.image_url = map.get('ImageURL')
        return self


class GenerateHumanAnimeStyleAdvanceRequest(TeaModel):
    def __init__(self, image_urlobject=None):
        self.image_urlobject = image_urlobject  # type: BinaryIO

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        result = {}
        result['ImageURLObject'] = self.image_urlobject
        return result

    def from_map(self, map={}):
        self.image_urlobject = map.get('ImageURLObject')
        return self


class PedestrianDetectAttributeRequest(TeaModel):
    def __init__(self, image_url=None):
        self.image_url = image_url      # type: str

    def validate(self):
        self.validate_required(self.image_url, 'image_url')

    def to_map(self):
        result = {}
        result['ImageURL'] = self.image_url
        return result

    def from_map(self, map={}):
        self.image_url = map.get('ImageURL')
        return self


class PedestrianDetectAttributeResponse(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id    # type: str
        self.data = data                # type: PedestrianDetectAttributeResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = PedestrianDetectAttributeResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class PedestrianDetectAttributeResponseDataAttributesAge(TeaModel):
    def __init__(self, name=None, score=None):
        self.name = name                # type: str
        self.score = score              # type: float

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.score, 'score')

    def to_map(self):
        result = {}
        result['Name'] = self.name
        result['Score'] = self.score
        return result

    def from_map(self, map={}):
        self.name = map.get('Name')
        self.score = map.get('Score')
        return self


class PedestrianDetectAttributeResponseDataAttributesBackpack(TeaModel):
    def __init__(self, name=None, score=None):
        self.name = name                # type: str
        self.score = score              # type: float

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.score, 'score')

    def to_map(self):
        result = {}
        result['Name'] = self.name
        result['Score'] = self.score
        return result

    def from_map(self, map={}):
        self.name = map.get('Name')
        self.score = map.get('Score')
        return self


class PedestrianDetectAttributeResponseDataAttributesGender(TeaModel):
    def __init__(self, name=None, score=None):
        self.name = name                # type: str
        self.score = score              # type: float

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.score, 'score')

    def to_map(self):
        result = {}
        result['Name'] = self.name
        result['Score'] = self.score
        return result

    def from_map(self, map={}):
        self.name = map.get('Name')
        self.score = map.get('Score')
        return self


class PedestrianDetectAttributeResponseDataAttributesGlasses(TeaModel):
    def __init__(self, name=None, score=None):
        self.name = name                # type: str
        self.score = score              # type: float

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.score, 'score')

    def to_map(self):
        result = {}
        result['Name'] = self.name
        result['Score'] = self.score
        return result

    def from_map(self, map={}):
        self.name = map.get('Name')
        self.score = map.get('Score')
        return self


class PedestrianDetectAttributeResponseDataAttributesHandbag(TeaModel):
    def __init__(self, name=None, score=None):
        self.name = name                # type: str
        self.score = score              # type: float

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.score, 'score')

    def to_map(self):
        result = {}
        result['Name'] = self.name
        result['Score'] = self.score
        return result

    def from_map(self, map={}):
        self.name = map.get('Name')
        self.score = map.get('Score')
        return self


class PedestrianDetectAttributeResponseDataAttributesHat(TeaModel):
    def __init__(self, name=None, score=None):
        self.name = name                # type: str
        self.score = score              # type: float

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.score, 'score')

    def to_map(self):
        result = {}
        result['Name'] = self.name
        result['Score'] = self.score
        return result

    def from_map(self, map={}):
        self.name = map.get('Name')
        self.score = map.get('Score')
        return self


class PedestrianDetectAttributeResponseDataAttributesLowerColor(TeaModel):
    def __init__(self, name=None, score=None):
        self.name = name                # type: str
        self.score = score              # type: float

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.score, 'score')

    def to_map(self):
        result = {}
        result['Name'] = self.name
        result['Score'] = self.score
        return result

    def from_map(self, map={}):
        self.name = map.get('Name')
        self.score = map.get('Score')
        return self


class PedestrianDetectAttributeResponseDataAttributesLowerWear(TeaModel):
    def __init__(self, name=None, score=None):
        self.name = name                # type: str
        self.score = score              # type: float

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.score, 'score')

    def to_map(self):
        result = {}
        result['Name'] = self.name
        result['Score'] = self.score
        return result

    def from_map(self, map={}):
        self.name = map.get('Name')
        self.score = map.get('Score')
        return self


class PedestrianDetectAttributeResponseDataAttributesOrient(TeaModel):
    def __init__(self, name=None, score=None):
        self.name = name                # type: str
        self.score = score              # type: float

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.score, 'score')

    def to_map(self):
        result = {}
        result['Name'] = self.name
        result['Score'] = self.score
        return result

    def from_map(self, map={}):
        self.name = map.get('Name')
        self.score = map.get('Score')
        return self


class PedestrianDetectAttributeResponseDataAttributesShoulderBag(TeaModel):
    def __init__(self, name=None, score=None):
        self.name = name                # type: str
        self.score = score              # type: float

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.score, 'score')

    def to_map(self):
        result = {}
        result['Name'] = self.name
        result['Score'] = self.score
        return result

    def from_map(self, map={}):
        self.name = map.get('Name')
        self.score = map.get('Score')
        return self


class PedestrianDetectAttributeResponseDataAttributesUpperColor(TeaModel):
    def __init__(self, name=None, score=None):
        self.name = name                # type: str
        self.score = score              # type: float

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.score, 'score')

    def to_map(self):
        result = {}
        result['Name'] = self.name
        result['Score'] = self.score
        return result

    def from_map(self, map={}):
        self.name = map.get('Name')
        self.score = map.get('Score')
        return self


class PedestrianDetectAttributeResponseDataAttributesUpperWear(TeaModel):
    def __init__(self, name=None, score=None):
        self.name = name                # type: str
        self.score = score              # type: float

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.score, 'score')

    def to_map(self):
        result = {}
        result['Name'] = self.name
        result['Score'] = self.score
        return result

    def from_map(self, map={}):
        self.name = map.get('Name')
        self.score = map.get('Score')
        return self


class PedestrianDetectAttributeResponseDataAttributes(TeaModel):
    def __init__(self, age=None, backpack=None, gender=None, glasses=None, handbag=None, hat=None, lower_color=None,
                 lower_wear=None, orient=None, shoulder_bag=None, upper_color=None, upper_wear=None):
        self.age = age                  # type: PedestrianDetectAttributeResponseDataAttributesAge
        self.backpack = backpack        # type: PedestrianDetectAttributeResponseDataAttributesBackpack
        self.gender = gender            # type: PedestrianDetectAttributeResponseDataAttributesGender
        self.glasses = glasses          # type: PedestrianDetectAttributeResponseDataAttributesGlasses
        self.handbag = handbag          # type: PedestrianDetectAttributeResponseDataAttributesHandbag
        self.hat = hat                  # type: PedestrianDetectAttributeResponseDataAttributesHat
        self.lower_color = lower_color  # type: PedestrianDetectAttributeResponseDataAttributesLowerColor
        self.lower_wear = lower_wear    # type: PedestrianDetectAttributeResponseDataAttributesLowerWear
        self.orient = orient            # type: PedestrianDetectAttributeResponseDataAttributesOrient
        self.shoulder_bag = shoulder_bag  # type: PedestrianDetectAttributeResponseDataAttributesShoulderBag
        self.upper_color = upper_color  # type: PedestrianDetectAttributeResponseDataAttributesUpperColor
        self.upper_wear = upper_wear    # type: PedestrianDetectAttributeResponseDataAttributesUpperWear

    def validate(self):
        self.validate_required(self.age, 'age')
        if self.age:
            self.age.validate()
        self.validate_required(self.backpack, 'backpack')
        if self.backpack:
            self.backpack.validate()
        self.validate_required(self.gender, 'gender')
        if self.gender:
            self.gender.validate()
        self.validate_required(self.glasses, 'glasses')
        if self.glasses:
            self.glasses.validate()
        self.validate_required(self.handbag, 'handbag')
        if self.handbag:
            self.handbag.validate()
        self.validate_required(self.hat, 'hat')
        if self.hat:
            self.hat.validate()
        self.validate_required(self.lower_color, 'lower_color')
        if self.lower_color:
            self.lower_color.validate()
        self.validate_required(self.lower_wear, 'lower_wear')
        if self.lower_wear:
            self.lower_wear.validate()
        self.validate_required(self.orient, 'orient')
        if self.orient:
            self.orient.validate()
        self.validate_required(self.shoulder_bag, 'shoulder_bag')
        if self.shoulder_bag:
            self.shoulder_bag.validate()
        self.validate_required(self.upper_color, 'upper_color')
        if self.upper_color:
            self.upper_color.validate()
        self.validate_required(self.upper_wear, 'upper_wear')
        if self.upper_wear:
            self.upper_wear.validate()

    def to_map(self):
        result = {}
        if self.age is not None:
            result['Age'] = self.age.to_map()
        else:
            result['Age'] = None
        if self.backpack is not None:
            result['Backpack'] = self.backpack.to_map()
        else:
            result['Backpack'] = None
        if self.gender is not None:
            result['Gender'] = self.gender.to_map()
        else:
            result['Gender'] = None
        if self.glasses is not None:
            result['Glasses'] = self.glasses.to_map()
        else:
            result['Glasses'] = None
        if self.handbag is not None:
            result['Handbag'] = self.handbag.to_map()
        else:
            result['Handbag'] = None
        if self.hat is not None:
            result['Hat'] = self.hat.to_map()
        else:
            result['Hat'] = None
        if self.lower_color is not None:
            result['LowerColor'] = self.lower_color.to_map()
        else:
            result['LowerColor'] = None
        if self.lower_wear is not None:
            result['LowerWear'] = self.lower_wear.to_map()
        else:
            result['LowerWear'] = None
        if self.orient is not None:
            result['Orient'] = self.orient.to_map()
        else:
            result['Orient'] = None
        if self.shoulder_bag is not None:
            result['ShoulderBag'] = self.shoulder_bag.to_map()
        else:
            result['ShoulderBag'] = None
        if self.upper_color is not None:
            result['UpperColor'] = self.upper_color.to_map()
        else:
            result['UpperColor'] = None
        if self.upper_wear is not None:
            result['UpperWear'] = self.upper_wear.to_map()
        else:
            result['UpperWear'] = None
        return result

    def from_map(self, map={}):
        if map.get('Age') is not None:
            temp_model = PedestrianDetectAttributeResponseDataAttributesAge()
            self.age = temp_model.from_map(map['Age'])
        else:
            self.age = None
        if map.get('Backpack') is not None:
            temp_model = PedestrianDetectAttributeResponseDataAttributesBackpack()
            self.backpack = temp_model.from_map(map['Backpack'])
        else:
            self.backpack = None
        if map.get('Gender') is not None:
            temp_model = PedestrianDetectAttributeResponseDataAttributesGender()
            self.gender = temp_model.from_map(map['Gender'])
        else:
            self.gender = None
        if map.get('Glasses') is not None:
            temp_model = PedestrianDetectAttributeResponseDataAttributesGlasses()
            self.glasses = temp_model.from_map(map['Glasses'])
        else:
            self.glasses = None
        if map.get('Handbag') is not None:
            temp_model = PedestrianDetectAttributeResponseDataAttributesHandbag()
            self.handbag = temp_model.from_map(map['Handbag'])
        else:
            self.handbag = None
        if map.get('Hat') is not None:
            temp_model = PedestrianDetectAttributeResponseDataAttributesHat()
            self.hat = temp_model.from_map(map['Hat'])
        else:
            self.hat = None
        if map.get('LowerColor') is not None:
            temp_model = PedestrianDetectAttributeResponseDataAttributesLowerColor()
            self.lower_color = temp_model.from_map(map['LowerColor'])
        else:
            self.lower_color = None
        if map.get('LowerWear') is not None:
            temp_model = PedestrianDetectAttributeResponseDataAttributesLowerWear()
            self.lower_wear = temp_model.from_map(map['LowerWear'])
        else:
            self.lower_wear = None
        if map.get('Orient') is not None:
            temp_model = PedestrianDetectAttributeResponseDataAttributesOrient()
            self.orient = temp_model.from_map(map['Orient'])
        else:
            self.orient = None
        if map.get('ShoulderBag') is not None:
            temp_model = PedestrianDetectAttributeResponseDataAttributesShoulderBag()
            self.shoulder_bag = temp_model.from_map(map['ShoulderBag'])
        else:
            self.shoulder_bag = None
        if map.get('UpperColor') is not None:
            temp_model = PedestrianDetectAttributeResponseDataAttributesUpperColor()
            self.upper_color = temp_model.from_map(map['UpperColor'])
        else:
            self.upper_color = None
        if map.get('UpperWear') is not None:
            temp_model = PedestrianDetectAttributeResponseDataAttributesUpperWear()
            self.upper_wear = temp_model.from_map(map['UpperWear'])
        else:
            self.upper_wear = None
        return self


class PedestrianDetectAttributeResponseDataBoxes(TeaModel):
    def __init__(self, score=None, top_left_x=None, top_left_y=None, bottom_right_x=None, bottom_right_y=None):
        self.score = score              # type: float
        self.top_left_x = top_left_x    # type: float
        self.top_left_y = top_left_y    # type: float
        self.bottom_right_x = bottom_right_x  # type: float
        self.bottom_right_y = bottom_right_y  # type: float

    def validate(self):
        self.validate_required(self.score, 'score')
        self.validate_required(self.top_left_x, 'top_left_x')
        self.validate_required(self.top_left_y, 'top_left_y')
        self.validate_required(self.bottom_right_x, 'bottom_right_x')
        self.validate_required(self.bottom_right_y, 'bottom_right_y')

    def to_map(self):
        result = {}
        result['Score'] = self.score
        result['TopLeftX'] = self.top_left_x
        result['TopLeftY'] = self.top_left_y
        result['BottomRightX'] = self.bottom_right_x
        result['BottomRightY'] = self.bottom_right_y
        return result

    def from_map(self, map={}):
        self.score = map.get('Score')
        self.top_left_x = map.get('TopLeftX')
        self.top_left_y = map.get('TopLeftY')
        self.bottom_right_x = map.get('BottomRightX')
        self.bottom_right_y = map.get('BottomRightY')
        return self


class PedestrianDetectAttributeResponseData(TeaModel):
    def __init__(self, person_number=None, attributes=None, boxes=None):
        self.person_number = person_number  # type: int
        self.attributes = attributes    # type: List[PedestrianDetectAttributeResponseDataAttributes]
        self.boxes = boxes              # type: List[PedestrianDetectAttributeResponseDataBoxes]

    def validate(self):
        self.validate_required(self.person_number, 'person_number')
        self.validate_required(self.attributes, 'attributes')
        if self.attributes:
            for k in self.attributes:
                if k:
                    k.validate()
        self.validate_required(self.boxes, 'boxes')
        if self.boxes:
            for k in self.boxes:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['PersonNumber'] = self.person_number
        result['Attributes'] = []
        if self.attributes is not None:
            for k in self.attributes:
                result['Attributes'].append(k.to_map() if k else None)
        else:
            result['Attributes'] = None
        result['Boxes'] = []
        if self.boxes is not None:
            for k in self.boxes:
                result['Boxes'].append(k.to_map() if k else None)
        else:
            result['Boxes'] = None
        return result

    def from_map(self, map={}):
        self.person_number = map.get('PersonNumber')
        self.attributes = []
        if map.get('Attributes') is not None:
            for k in map.get('Attributes'):
                temp_model = PedestrianDetectAttributeResponseDataAttributes()
                self.attributes.append(temp_model.from_map(k))
        else:
            self.attributes = None
        self.boxes = []
        if map.get('Boxes') is not None:
            for k in map.get('Boxes'):
                temp_model = PedestrianDetectAttributeResponseDataBoxes()
                self.boxes.append(temp_model.from_map(k))
        else:
            self.boxes = None
        return self


class PedestrianDetectAttributeAdvanceRequest(TeaModel):
    def __init__(self, image_urlobject=None):
        self.image_urlobject = image_urlobject  # type: BinaryIO

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        result = {}
        result['ImageURLObject'] = self.image_urlobject
        return result

    def from_map(self, map={}):
        self.image_urlobject = map.get('ImageURLObject')
        return self


class DetectChefCapRequest(TeaModel):
    def __init__(self, image_url=None):
        self.image_url = image_url      # type: str

    def validate(self):
        self.validate_required(self.image_url, 'image_url')

    def to_map(self):
        result = {}
        result['ImageURL'] = self.image_url
        return result

    def from_map(self, map={}):
        self.image_url = map.get('ImageURL')
        return self


class DetectChefCapResponse(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id    # type: str
        self.data = data                # type: DetectChefCapResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = DetectChefCapResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class DetectChefCapResponseDataElements(TeaModel):
    def __init__(self, category=None, confidence=None, box=None):
        self.category = category        # type: str
        self.confidence = confidence    # type: float
        self.box = box                  # type: List[float]

    def validate(self):
        self.validate_required(self.category, 'category')
        self.validate_required(self.confidence, 'confidence')
        self.validate_required(self.box, 'box')

    def to_map(self):
        result = {}
        result['Category'] = self.category
        result['Confidence'] = self.confidence
        result['Box'] = self.box
        return result

    def from_map(self, map={}):
        self.category = map.get('Category')
        self.confidence = map.get('Confidence')
        self.box = map.get('Box')
        return self


class DetectChefCapResponseData(TeaModel):
    def __init__(self, elements=None):
        self.elements = elements        # type: List[DetectChefCapResponseDataElements]

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
        else:
            result['Elements'] = None
        return result

    def from_map(self, map={}):
        self.elements = []
        if map.get('Elements') is not None:
            for k in map.get('Elements'):
                temp_model = DetectChefCapResponseDataElements()
                self.elements.append(temp_model.from_map(k))
        else:
            self.elements = None
        return self


class DetectChefCapAdvanceRequest(TeaModel):
    def __init__(self, image_urlobject=None):
        self.image_urlobject = image_urlobject  # type: BinaryIO

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        result = {}
        result['ImageURLObject'] = self.image_urlobject
        return result

    def from_map(self, map={}):
        self.image_urlobject = map.get('ImageURLObject')
        return self


class ExtractPedestrianFeatureAttrRequest(TeaModel):
    def __init__(self, image_url=None, mode=None):
        self.image_url = image_url      # type: str
        self.mode = mode                # type: str

    def validate(self):
        self.validate_required(self.image_url, 'image_url')

    def to_map(self):
        result = {}
        result['ImageURL'] = self.image_url
        result['Mode'] = self.mode
        return result

    def from_map(self, map={}):
        self.image_url = map.get('ImageURL')
        self.mode = map.get('Mode')
        return self


class ExtractPedestrianFeatureAttrResponse(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id    # type: str
        self.data = data                # type: ExtractPedestrianFeatureAttrResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = ExtractPedestrianFeatureAttrResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class ExtractPedestrianFeatureAttrResponseData(TeaModel):
    def __init__(self, obj_type=None, obj_type_score=None, feature=None, quality_score=None, upper_color=None,
                 upper_color_score=None, upper_type=None, upper_type_score=None, lower_color=None, lower_color_score=None,
                 lower_type=None, lower_type_score=None, gender=None, gender_score=None, hair=None, hair_score=None, age=None,
                 age_score=None):
        self.obj_type = obj_type        # type: str
        self.obj_type_score = obj_type_score  # type: float
        self.feature = feature          # type: str
        self.quality_score = quality_score  # type: float
        self.upper_color = upper_color  # type: str
        self.upper_color_score = upper_color_score  # type: float
        self.upper_type = upper_type    # type: str
        self.upper_type_score = upper_type_score  # type: float
        self.lower_color = lower_color  # type: str
        self.lower_color_score = lower_color_score  # type: float
        self.lower_type = lower_type    # type: str
        self.lower_type_score = lower_type_score  # type: float
        self.gender = gender            # type: str
        self.gender_score = gender_score  # type: float
        self.hair = hair                # type: str
        self.hair_score = hair_score    # type: float
        self.age = age                  # type: str
        self.age_score = age_score      # type: float

    def validate(self):
        self.validate_required(self.obj_type, 'obj_type')
        self.validate_required(self.obj_type_score, 'obj_type_score')
        self.validate_required(self.feature, 'feature')
        self.validate_required(self.quality_score, 'quality_score')
        self.validate_required(self.upper_color, 'upper_color')
        self.validate_required(self.upper_color_score, 'upper_color_score')
        self.validate_required(self.upper_type, 'upper_type')
        self.validate_required(self.upper_type_score, 'upper_type_score')
        self.validate_required(self.lower_color, 'lower_color')
        self.validate_required(self.lower_color_score, 'lower_color_score')
        self.validate_required(self.lower_type, 'lower_type')
        self.validate_required(self.lower_type_score, 'lower_type_score')
        self.validate_required(self.gender, 'gender')
        self.validate_required(self.gender_score, 'gender_score')
        self.validate_required(self.hair, 'hair')
        self.validate_required(self.hair_score, 'hair_score')
        self.validate_required(self.age, 'age')
        self.validate_required(self.age_score, 'age_score')

    def to_map(self):
        result = {}
        result['ObjType'] = self.obj_type
        result['ObjTypeScore'] = self.obj_type_score
        result['Feature'] = self.feature
        result['QualityScore'] = self.quality_score
        result['UpperColor'] = self.upper_color
        result['UpperColorScore'] = self.upper_color_score
        result['UpperType'] = self.upper_type
        result['UpperTypeScore'] = self.upper_type_score
        result['LowerColor'] = self.lower_color
        result['LowerColorScore'] = self.lower_color_score
        result['LowerType'] = self.lower_type
        result['LowerTypeScore'] = self.lower_type_score
        result['Gender'] = self.gender
        result['GenderScore'] = self.gender_score
        result['Hair'] = self.hair
        result['HairScore'] = self.hair_score
        result['Age'] = self.age
        result['AgeScore'] = self.age_score
        return result

    def from_map(self, map={}):
        self.obj_type = map.get('ObjType')
        self.obj_type_score = map.get('ObjTypeScore')
        self.feature = map.get('Feature')
        self.quality_score = map.get('QualityScore')
        self.upper_color = map.get('UpperColor')
        self.upper_color_score = map.get('UpperColorScore')
        self.upper_type = map.get('UpperType')
        self.upper_type_score = map.get('UpperTypeScore')
        self.lower_color = map.get('LowerColor')
        self.lower_color_score = map.get('LowerColorScore')
        self.lower_type = map.get('LowerType')
        self.lower_type_score = map.get('LowerTypeScore')
        self.gender = map.get('Gender')
        self.gender_score = map.get('GenderScore')
        self.hair = map.get('Hair')
        self.hair_score = map.get('HairScore')
        self.age = map.get('Age')
        self.age_score = map.get('AgeScore')
        return self


class ExtractPedestrianFeatureAttrAdvanceRequest(TeaModel):
    def __init__(self, image_urlobject=None, mode=None):
        self.image_urlobject = image_urlobject  # type: BinaryIO
        self.mode = mode                # type: str

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        result = {}
        result['ImageURLObject'] = self.image_urlobject
        result['Mode'] = self.mode
        return result

    def from_map(self, map={}):
        self.image_urlobject = map.get('ImageURLObject')
        self.mode = map.get('Mode')
        return self


class DetectIPCPedestrianRequest(TeaModel):
    def __init__(self, image_data=None, width=None, height=None):
        self.image_data = image_data    # type: str
        self.width = width              # type: int
        self.height = height            # type: int

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['ImageData'] = self.image_data
        result['Width'] = self.width
        result['Height'] = self.height
        return result

    def from_map(self, map={}):
        self.image_data = map.get('ImageData')
        self.width = map.get('Width')
        self.height = map.get('Height')
        return self


class DetectIPCPedestrianResponse(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id    # type: str
        self.data = data                # type: DetectIPCPedestrianResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = DetectIPCPedestrianResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class DetectIPCPedestrianResponseDataImageInfoListElements(TeaModel):
    def __init__(self, score=None, boxes=None):
        self.score = score              # type: float
        self.boxes = boxes              # type: List[int]

    def validate(self):
        self.validate_required(self.score, 'score')
        self.validate_required(self.boxes, 'boxes')

    def to_map(self):
        result = {}
        result['Score'] = self.score
        result['Boxes'] = self.boxes
        return result

    def from_map(self, map={}):
        self.score = map.get('Score')
        self.boxes = map.get('Boxes')
        return self


class DetectIPCPedestrianResponseDataImageInfoList(TeaModel):
    def __init__(self, error_code=None, error_message=None, data_id=None, elements=None):
        self.error_code = error_code    # type: str
        self.error_message = error_message  # type: str
        self.data_id = data_id          # type: str
        self.elements = elements        # type: List[DetectIPCPedestrianResponseDataImageInfoListElements]

    def validate(self):
        self.validate_required(self.error_code, 'error_code')
        self.validate_required(self.error_message, 'error_message')
        self.validate_required(self.data_id, 'data_id')
        self.validate_required(self.elements, 'elements')
        if self.elements:
            for k in self.elements:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['ErrorCode'] = self.error_code
        result['ErrorMessage'] = self.error_message
        result['DataId'] = self.data_id
        result['Elements'] = []
        if self.elements is not None:
            for k in self.elements:
                result['Elements'].append(k.to_map() if k else None)
        else:
            result['Elements'] = None
        return result

    def from_map(self, map={}):
        self.error_code = map.get('ErrorCode')
        self.error_message = map.get('ErrorMessage')
        self.data_id = map.get('DataId')
        self.elements = []
        if map.get('Elements') is not None:
            for k in map.get('Elements'):
                temp_model = DetectIPCPedestrianResponseDataImageInfoListElements()
                self.elements.append(temp_model.from_map(k))
        else:
            self.elements = None
        return self


class DetectIPCPedestrianResponseData(TeaModel):
    def __init__(self, image_info_list=None):
        self.image_info_list = image_info_list  # type: List[DetectIPCPedestrianResponseDataImageInfoList]

    def validate(self):
        self.validate_required(self.image_info_list, 'image_info_list')
        if self.image_info_list:
            for k in self.image_info_list:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['ImageInfoList'] = []
        if self.image_info_list is not None:
            for k in self.image_info_list:
                result['ImageInfoList'].append(k.to_map() if k else None)
        else:
            result['ImageInfoList'] = None
        return result

    def from_map(self, map={}):
        self.image_info_list = []
        if map.get('ImageInfoList') is not None:
            for k in map.get('ImageInfoList'):
                temp_model = DetectIPCPedestrianResponseDataImageInfoList()
                self.image_info_list.append(temp_model.from_map(k))
        else:
            self.image_info_list = None
        return self


class BlurFaceRequest(TeaModel):
    def __init__(self, image_url=None):
        self.image_url = image_url      # type: str

    def validate(self):
        self.validate_required(self.image_url, 'image_url')

    def to_map(self):
        result = {}
        result['ImageURL'] = self.image_url
        return result

    def from_map(self, map={}):
        self.image_url = map.get('ImageURL')
        return self


class BlurFaceResponse(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id    # type: str
        self.data = data                # type: BlurFaceResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = BlurFaceResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class BlurFaceResponseData(TeaModel):
    def __init__(self, image_url=None):
        self.image_url = image_url      # type: str

    def validate(self):
        self.validate_required(self.image_url, 'image_url')

    def to_map(self):
        result = {}
        result['ImageURL'] = self.image_url
        return result

    def from_map(self, map={}):
        self.image_url = map.get('ImageURL')
        return self


class BlurFaceAdvanceRequest(TeaModel):
    def __init__(self, image_urlobject=None):
        self.image_urlobject = image_urlobject  # type: BinaryIO

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        result = {}
        result['ImageURLObject'] = self.image_urlobject
        return result

    def from_map(self, map={}):
        self.image_urlobject = map.get('ImageURLObject')
        return self


class ExtractPedestrianFeatureAttributeRequest(TeaModel):
    def __init__(self, mode=None, image_url=None, url_list=None):
        self.mode = mode                # type: str
        self.image_url = image_url      # type: str
        self.url_list = url_list        # type: List[ExtractPedestrianFeatureAttributeRequestUrlList]

    def validate(self):
        if self.url_list:
            for k in self.url_list:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Mode'] = self.mode
        result['ImageURL'] = self.image_url
        result['UrlList'] = []
        if self.url_list is not None:
            for k in self.url_list:
                result['UrlList'].append(k.to_map() if k else None)
        else:
            result['UrlList'] = None
        return result

    def from_map(self, map={}):
        self.mode = map.get('Mode')
        self.image_url = map.get('ImageURL')
        self.url_list = []
        if map.get('UrlList') is not None:
            for k in map.get('UrlList'):
                temp_model = ExtractPedestrianFeatureAttributeRequestUrlList()
                self.url_list.append(temp_model.from_map(k))
        else:
            self.url_list = None
        return self


class ExtractPedestrianFeatureAttributeRequestUrlList(TeaModel):
    def __init__(self, url=None):
        self.url = url                  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['Url'] = self.url
        return result

    def from_map(self, map={}):
        self.url = map.get('Url')
        return self


class ExtractPedestrianFeatureAttributeResponse(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id    # type: str
        self.data = data                # type: ExtractPedestrianFeatureAttributeResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = ExtractPedestrianFeatureAttributeResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class ExtractPedestrianFeatureAttributeResponseDataElements(TeaModel):
    def __init__(self, obj_type=None, obj_type_score=None, feature=None, quality_score=None, upper_color=None,
                 upper_color_score=None, upper_type=None, upper_type_score=None, lower_color=None, lower_color_score=None,
                 lower_type=None, lower_type_score=None, gender=None, gender_score=None, hair=None, hair_score=None, age=None,
                 age_score=None):
        self.obj_type = obj_type        # type: str
        self.obj_type_score = obj_type_score  # type: float
        self.feature = feature          # type: str
        self.quality_score = quality_score  # type: float
        self.upper_color = upper_color  # type: str
        self.upper_color_score = upper_color_score  # type: float
        self.upper_type = upper_type    # type: str
        self.upper_type_score = upper_type_score  # type: float
        self.lower_color = lower_color  # type: str
        self.lower_color_score = lower_color_score  # type: float
        self.lower_type = lower_type    # type: str
        self.lower_type_score = lower_type_score  # type: float
        self.gender = gender            # type: str
        self.gender_score = gender_score  # type: float
        self.hair = hair                # type: str
        self.hair_score = hair_score    # type: float
        self.age = age                  # type: str
        self.age_score = age_score      # type: float

    def validate(self):
        self.validate_required(self.obj_type, 'obj_type')
        self.validate_required(self.obj_type_score, 'obj_type_score')
        self.validate_required(self.feature, 'feature')
        self.validate_required(self.quality_score, 'quality_score')
        self.validate_required(self.upper_color, 'upper_color')
        self.validate_required(self.upper_color_score, 'upper_color_score')
        self.validate_required(self.upper_type, 'upper_type')
        self.validate_required(self.upper_type_score, 'upper_type_score')
        self.validate_required(self.lower_color, 'lower_color')
        self.validate_required(self.lower_color_score, 'lower_color_score')
        self.validate_required(self.lower_type, 'lower_type')
        self.validate_required(self.lower_type_score, 'lower_type_score')
        self.validate_required(self.gender, 'gender')
        self.validate_required(self.gender_score, 'gender_score')
        self.validate_required(self.hair, 'hair')
        self.validate_required(self.hair_score, 'hair_score')
        self.validate_required(self.age, 'age')
        self.validate_required(self.age_score, 'age_score')

    def to_map(self):
        result = {}
        result['ObjType'] = self.obj_type
        result['ObjTypeScore'] = self.obj_type_score
        result['Feature'] = self.feature
        result['QualityScore'] = self.quality_score
        result['UpperColor'] = self.upper_color
        result['UpperColorScore'] = self.upper_color_score
        result['UpperType'] = self.upper_type
        result['UpperTypeScore'] = self.upper_type_score
        result['LowerColor'] = self.lower_color
        result['LowerColorScore'] = self.lower_color_score
        result['LowerType'] = self.lower_type
        result['LowerTypeScore'] = self.lower_type_score
        result['Gender'] = self.gender
        result['GenderScore'] = self.gender_score
        result['Hair'] = self.hair
        result['HairScore'] = self.hair_score
        result['Age'] = self.age
        result['AgeScore'] = self.age_score
        return result

    def from_map(self, map={}):
        self.obj_type = map.get('ObjType')
        self.obj_type_score = map.get('ObjTypeScore')
        self.feature = map.get('Feature')
        self.quality_score = map.get('QualityScore')
        self.upper_color = map.get('UpperColor')
        self.upper_color_score = map.get('UpperColorScore')
        self.upper_type = map.get('UpperType')
        self.upper_type_score = map.get('UpperTypeScore')
        self.lower_color = map.get('LowerColor')
        self.lower_color_score = map.get('LowerColorScore')
        self.lower_type = map.get('LowerType')
        self.lower_type_score = map.get('LowerTypeScore')
        self.gender = map.get('Gender')
        self.gender_score = map.get('GenderScore')
        self.hair = map.get('Hair')
        self.hair_score = map.get('HairScore')
        self.age = map.get('Age')
        self.age_score = map.get('AgeScore')
        return self


class ExtractPedestrianFeatureAttributeResponseData(TeaModel):
    def __init__(self, obj_type=None, obj_type_score=None, feature=None, quality_score=None, upper_color=None,
                 upper_color_score=None, upper_type=None, upper_type_score=None, lower_color=None, lower_color_score=None,
                 lower_type=None, lower_type_score=None, gender=None, gender_score=None, hair=None, hair_score=None, age=None,
                 age_score=None, elements=None):
        self.obj_type = obj_type        # type: str
        self.obj_type_score = obj_type_score  # type: float
        self.feature = feature          # type: str
        self.quality_score = quality_score  # type: float
        self.upper_color = upper_color  # type: str
        self.upper_color_score = upper_color_score  # type: float
        self.upper_type = upper_type    # type: str
        self.upper_type_score = upper_type_score  # type: float
        self.lower_color = lower_color  # type: str
        self.lower_color_score = lower_color_score  # type: float
        self.lower_type = lower_type    # type: str
        self.lower_type_score = lower_type_score  # type: float
        self.gender = gender            # type: str
        self.gender_score = gender_score  # type: float
        self.hair = hair                # type: str
        self.hair_score = hair_score    # type: float
        self.age = age                  # type: str
        self.age_score = age_score      # type: float
        self.elements = elements        # type: List[ExtractPedestrianFeatureAttributeResponseDataElements]

    def validate(self):
        self.validate_required(self.obj_type, 'obj_type')
        self.validate_required(self.obj_type_score, 'obj_type_score')
        self.validate_required(self.feature, 'feature')
        self.validate_required(self.quality_score, 'quality_score')
        self.validate_required(self.upper_color, 'upper_color')
        self.validate_required(self.upper_color_score, 'upper_color_score')
        self.validate_required(self.upper_type, 'upper_type')
        self.validate_required(self.upper_type_score, 'upper_type_score')
        self.validate_required(self.lower_color, 'lower_color')
        self.validate_required(self.lower_color_score, 'lower_color_score')
        self.validate_required(self.lower_type, 'lower_type')
        self.validate_required(self.lower_type_score, 'lower_type_score')
        self.validate_required(self.gender, 'gender')
        self.validate_required(self.gender_score, 'gender_score')
        self.validate_required(self.hair, 'hair')
        self.validate_required(self.hair_score, 'hair_score')
        self.validate_required(self.age, 'age')
        self.validate_required(self.age_score, 'age_score')
        self.validate_required(self.elements, 'elements')
        if self.elements:
            for k in self.elements:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['ObjType'] = self.obj_type
        result['ObjTypeScore'] = self.obj_type_score
        result['Feature'] = self.feature
        result['QualityScore'] = self.quality_score
        result['UpperColor'] = self.upper_color
        result['UpperColorScore'] = self.upper_color_score
        result['UpperType'] = self.upper_type
        result['UpperTypeScore'] = self.upper_type_score
        result['LowerColor'] = self.lower_color
        result['LowerColorScore'] = self.lower_color_score
        result['LowerType'] = self.lower_type
        result['LowerTypeScore'] = self.lower_type_score
        result['Gender'] = self.gender
        result['GenderScore'] = self.gender_score
        result['Hair'] = self.hair
        result['HairScore'] = self.hair_score
        result['Age'] = self.age
        result['AgeScore'] = self.age_score
        result['Elements'] = []
        if self.elements is not None:
            for k in self.elements:
                result['Elements'].append(k.to_map() if k else None)
        else:
            result['Elements'] = None
        return result

    def from_map(self, map={}):
        self.obj_type = map.get('ObjType')
        self.obj_type_score = map.get('ObjTypeScore')
        self.feature = map.get('Feature')
        self.quality_score = map.get('QualityScore')
        self.upper_color = map.get('UpperColor')
        self.upper_color_score = map.get('UpperColorScore')
        self.upper_type = map.get('UpperType')
        self.upper_type_score = map.get('UpperTypeScore')
        self.lower_color = map.get('LowerColor')
        self.lower_color_score = map.get('LowerColorScore')
        self.lower_type = map.get('LowerType')
        self.lower_type_score = map.get('LowerTypeScore')
        self.gender = map.get('Gender')
        self.gender_score = map.get('GenderScore')
        self.hair = map.get('Hair')
        self.hair_score = map.get('HairScore')
        self.age = map.get('Age')
        self.age_score = map.get('AgeScore')
        self.elements = []
        if map.get('Elements') is not None:
            for k in map.get('Elements'):
                temp_model = ExtractPedestrianFeatureAttributeResponseDataElements()
                self.elements.append(temp_model.from_map(k))
        else:
            self.elements = None
        return self


class DetectCelebrityRequest(TeaModel):
    def __init__(self, image_url=None):
        self.image_url = image_url      # type: str

    def validate(self):
        self.validate_required(self.image_url, 'image_url')

    def to_map(self):
        result = {}
        result['ImageURL'] = self.image_url
        return result

    def from_map(self, map={}):
        self.image_url = map.get('ImageURL')
        return self


class DetectCelebrityResponse(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id    # type: str
        self.data = data                # type: DetectCelebrityResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = DetectCelebrityResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class DetectCelebrityResponseDataFaceRecognizeResults(TeaModel):
    def __init__(self, name=None, face_boxes=None):
        self.name = name                # type: str
        self.face_boxes = face_boxes    # type: List[float]

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.face_boxes, 'face_boxes')

    def to_map(self):
        result = {}
        result['Name'] = self.name
        result['FaceBoxes'] = self.face_boxes
        return result

    def from_map(self, map={}):
        self.name = map.get('Name')
        self.face_boxes = map.get('FaceBoxes')
        return self


class DetectCelebrityResponseData(TeaModel):
    def __init__(self, width=None, height=None, face_recognize_results=None):
        self.width = width              # type: int
        self.height = height            # type: int
        self.face_recognize_results = face_recognize_results  # type: List[DetectCelebrityResponseDataFaceRecognizeResults]

    def validate(self):
        self.validate_required(self.width, 'width')
        self.validate_required(self.height, 'height')
        self.validate_required(self.face_recognize_results, 'face_recognize_results')
        if self.face_recognize_results:
            for k in self.face_recognize_results:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Width'] = self.width
        result['Height'] = self.height
        result['FaceRecognizeResults'] = []
        if self.face_recognize_results is not None:
            for k in self.face_recognize_results:
                result['FaceRecognizeResults'].append(k.to_map() if k else None)
        else:
            result['FaceRecognizeResults'] = None
        return result

    def from_map(self, map={}):
        self.width = map.get('Width')
        self.height = map.get('Height')
        self.face_recognize_results = []
        if map.get('FaceRecognizeResults') is not None:
            for k in map.get('FaceRecognizeResults'):
                temp_model = DetectCelebrityResponseDataFaceRecognizeResults()
                self.face_recognize_results.append(temp_model.from_map(k))
        else:
            self.face_recognize_results = None
        return self


class DetectCelebrityAdvanceRequest(TeaModel):
    def __init__(self, image_urlobject=None):
        self.image_urlobject = image_urlobject  # type: BinaryIO

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        result = {}
        result['ImageURLObject'] = self.image_urlobject
        return result

    def from_map(self, map={}):
        self.image_urlobject = map.get('ImageURLObject')
        return self


class VerifyFaceMaskRequest(TeaModel):
    def __init__(self, image_url=None, ref_url=None):
        self.image_url = image_url      # type: str
        self.ref_url = ref_url          # type: str

    def validate(self):
        self.validate_required(self.image_url, 'image_url')
        self.validate_required(self.ref_url, 'ref_url')

    def to_map(self):
        result = {}
        result['ImageURL'] = self.image_url
        result['RefUrl'] = self.ref_url
        return result

    def from_map(self, map={}):
        self.image_url = map.get('ImageURL')
        self.ref_url = map.get('RefUrl')
        return self


class VerifyFaceMaskResponse(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id    # type: str
        self.data = data                # type: VerifyFaceMaskResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = VerifyFaceMaskResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class VerifyFaceMaskResponseData(TeaModel):
    def __init__(self, confidence=None, mask=None, mask_ref=None, rectangle=None, rectangle_ref=None,
                 thresholds=None):
        self.confidence = confidence    # type: float
        self.mask = mask                # type: int
        self.mask_ref = mask_ref        # type: int
        self.rectangle = rectangle      # type: List[int]
        self.rectangle_ref = rectangle_ref  # type: List[int]
        self.thresholds = thresholds    # type: List[float]

    def validate(self):
        self.validate_required(self.confidence, 'confidence')
        self.validate_required(self.mask, 'mask')
        self.validate_required(self.mask_ref, 'mask_ref')
        self.validate_required(self.rectangle, 'rectangle')
        self.validate_required(self.rectangle_ref, 'rectangle_ref')
        self.validate_required(self.thresholds, 'thresholds')

    def to_map(self):
        result = {}
        result['Confidence'] = self.confidence
        result['Mask'] = self.mask
        result['MaskRef'] = self.mask_ref
        result['Rectangle'] = self.rectangle
        result['RectangleRef'] = self.rectangle_ref
        result['Thresholds'] = self.thresholds
        return result

    def from_map(self, map={}):
        self.confidence = map.get('Confidence')
        self.mask = map.get('Mask')
        self.mask_ref = map.get('MaskRef')
        self.rectangle = map.get('Rectangle')
        self.rectangle_ref = map.get('RectangleRef')
        self.thresholds = map.get('Thresholds')
        return self


class VerifyFaceMaskAdvanceRequest(TeaModel):
    def __init__(self, image_urlobject=None, ref_url=None):
        self.image_urlobject = image_urlobject  # type: BinaryIO
        self.ref_url = ref_url          # type: str

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')
        self.validate_required(self.ref_url, 'ref_url')

    def to_map(self):
        result = {}
        result['ImageURLObject'] = self.image_urlobject
        result['RefUrl'] = self.ref_url
        return result

    def from_map(self, map={}):
        self.image_urlobject = map.get('ImageURLObject')
        self.ref_url = map.get('RefUrl')
        return self


class RecognizeActionRequest(TeaModel):
    def __init__(self, urllist=None, type=None, video_url=None):
        self.urllist = urllist          # type: List[RecognizeActionRequestURLList]
        self.type = type                # type: int
        self.video_url = video_url      # type: str

    def validate(self):
        if self.urllist:
            for k in self.urllist:
                if k:
                    k.validate()
        self.validate_required(self.type, 'type')

    def to_map(self):
        result = {}
        result['URLList'] = []
        if self.urllist is not None:
            for k in self.urllist:
                result['URLList'].append(k.to_map() if k else None)
        else:
            result['URLList'] = None
        result['Type'] = self.type
        result['VideoUrl'] = self.video_url
        return result

    def from_map(self, map={}):
        self.urllist = []
        if map.get('URLList') is not None:
            for k in map.get('URLList'):
                temp_model = RecognizeActionRequestURLList()
                self.urllist.append(temp_model.from_map(k))
        else:
            self.urllist = None
        self.type = map.get('Type')
        self.video_url = map.get('VideoUrl')
        return self


class RecognizeActionRequestURLList(TeaModel):
    def __init__(self, url=None):
        self.url = url                  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['URL'] = self.url
        return result

    def from_map(self, map={}):
        self.url = map.get('URL')
        return self


class RecognizeActionResponse(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id    # type: str
        self.data = data                # type: RecognizeActionResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = RecognizeActionResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class RecognizeActionResponseDataElementsBoxes(TeaModel):
    def __init__(self, box=None):
        self.box = box                  # type: List[int]

    def validate(self):
        self.validate_required(self.box, 'box')

    def to_map(self):
        result = {}
        result['Box'] = self.box
        return result

    def from_map(self, map={}):
        self.box = map.get('Box')
        return self


class RecognizeActionResponseDataElements(TeaModel):
    def __init__(self, timestamp=None, boxes=None, scores=None, labels=None):
        self.timestamp = timestamp      # type: int
        self.boxes = boxes              # type: List[RecognizeActionResponseDataElementsBoxes]
        self.scores = scores            # type: List[float]
        self.labels = labels            # type: List[str]

    def validate(self):
        self.validate_required(self.timestamp, 'timestamp')
        self.validate_required(self.boxes, 'boxes')
        if self.boxes:
            for k in self.boxes:
                if k:
                    k.validate()
        self.validate_required(self.scores, 'scores')
        self.validate_required(self.labels, 'labels')

    def to_map(self):
        result = {}
        result['Timestamp'] = self.timestamp
        result['Boxes'] = []
        if self.boxes is not None:
            for k in self.boxes:
                result['Boxes'].append(k.to_map() if k else None)
        else:
            result['Boxes'] = None
        result['Scores'] = self.scores
        result['Labels'] = self.labels
        return result

    def from_map(self, map={}):
        self.timestamp = map.get('Timestamp')
        self.boxes = []
        if map.get('Boxes') is not None:
            for k in map.get('Boxes'):
                temp_model = RecognizeActionResponseDataElementsBoxes()
                self.boxes.append(temp_model.from_map(k))
        else:
            self.boxes = None
        self.scores = map.get('Scores')
        self.labels = map.get('Labels')
        return self


class RecognizeActionResponseData(TeaModel):
    def __init__(self, elements=None):
        self.elements = elements        # type: List[RecognizeActionResponseDataElements]

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
        else:
            result['Elements'] = None
        return result

    def from_map(self, map={}):
        self.elements = []
        if map.get('Elements') is not None:
            for k in map.get('Elements'):
                temp_model = RecognizeActionResponseDataElements()
                self.elements.append(temp_model.from_map(k))
        else:
            self.elements = None
        return self


class DetectVideoLivingFaceRequest(TeaModel):
    def __init__(self, video_url=None):
        self.video_url = video_url      # type: str

    def validate(self):
        self.validate_required(self.video_url, 'video_url')

    def to_map(self):
        result = {}
        result['VideoUrl'] = self.video_url
        return result

    def from_map(self, map={}):
        self.video_url = map.get('VideoUrl')
        return self


class DetectVideoLivingFaceResponse(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id    # type: str
        self.data = data                # type: DetectVideoLivingFaceResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = DetectVideoLivingFaceResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class DetectVideoLivingFaceResponseDataElements(TeaModel):
    def __init__(self, live_confidence=None, face_confidence=None, rect=None):
        self.live_confidence = live_confidence  # type: float
        self.face_confidence = face_confidence  # type: float
        self.rect = rect                # type: List[int]

    def validate(self):
        self.validate_required(self.live_confidence, 'live_confidence')
        self.validate_required(self.face_confidence, 'face_confidence')
        self.validate_required(self.rect, 'rect')

    def to_map(self):
        result = {}
        result['LiveConfidence'] = self.live_confidence
        result['FaceConfidence'] = self.face_confidence
        result['Rect'] = self.rect
        return result

    def from_map(self, map={}):
        self.live_confidence = map.get('LiveConfidence')
        self.face_confidence = map.get('FaceConfidence')
        self.rect = map.get('Rect')
        return self


class DetectVideoLivingFaceResponseData(TeaModel):
    def __init__(self, elements=None):
        self.elements = elements        # type: List[DetectVideoLivingFaceResponseDataElements]

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
        else:
            result['Elements'] = None
        return result

    def from_map(self, map={}):
        self.elements = []
        if map.get('Elements') is not None:
            for k in map.get('Elements'):
                temp_model = DetectVideoLivingFaceResponseDataElements()
                self.elements.append(temp_model.from_map(k))
        else:
            self.elements = None
        return self


class DetectVideoLivingFaceAdvanceRequest(TeaModel):
    def __init__(self, video_url_object=None):
        self.video_url_object = video_url_object  # type: BinaryIO

    def validate(self):
        self.validate_required(self.video_url_object, 'video_url_object')

    def to_map(self):
        result = {}
        result['VideoUrlObject'] = self.video_url_object
        return result

    def from_map(self, map={}):
        self.video_url_object = map.get('VideoUrlObject')
        return self


class SwapFacialFeaturesRequest(TeaModel):
    def __init__(self, source_image_url=None, edit_part=None, target_image_url=None):
        self.source_image_url = source_image_url  # type: str
        self.edit_part = edit_part      # type: str
        self.target_image_url = target_image_url  # type: str

    def validate(self):
        self.validate_required(self.source_image_url, 'source_image_url')
        self.validate_required(self.edit_part, 'edit_part')
        self.validate_required(self.target_image_url, 'target_image_url')

    def to_map(self):
        result = {}
        result['SourceImageURL'] = self.source_image_url
        result['EditPart'] = self.edit_part
        result['TargetImageURL'] = self.target_image_url
        return result

    def from_map(self, map={}):
        self.source_image_url = map.get('SourceImageURL')
        self.edit_part = map.get('EditPart')
        self.target_image_url = map.get('TargetImageURL')
        return self


class SwapFacialFeaturesResponse(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id    # type: str
        self.data = data                # type: SwapFacialFeaturesResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = SwapFacialFeaturesResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class SwapFacialFeaturesResponseData(TeaModel):
    def __init__(self, image_url=None):
        self.image_url = image_url      # type: str

    def validate(self):
        self.validate_required(self.image_url, 'image_url')

    def to_map(self):
        result = {}
        result['ImageURL'] = self.image_url
        return result

    def from_map(self, map={}):
        self.image_url = map.get('ImageURL')
        return self


class SwapFacialFeaturesAdvanceRequest(TeaModel):
    def __init__(self, source_image_urlobject=None, edit_part=None, target_image_url=None):
        self.source_image_urlobject = source_image_urlobject  # type: BinaryIO
        self.edit_part = edit_part      # type: str
        self.target_image_url = target_image_url  # type: str

    def validate(self):
        self.validate_required(self.source_image_urlobject, 'source_image_urlobject')
        self.validate_required(self.edit_part, 'edit_part')
        self.validate_required(self.target_image_url, 'target_image_url')

    def to_map(self):
        result = {}
        result['SourceImageURLObject'] = self.source_image_urlobject
        result['EditPart'] = self.edit_part
        result['TargetImageURL'] = self.target_image_url
        return result

    def from_map(self, map={}):
        self.source_image_urlobject = map.get('SourceImageURLObject')
        self.edit_part = map.get('EditPart')
        self.target_image_url = map.get('TargetImageURL')
        return self


class AddFaceEntityRequest(TeaModel):
    def __init__(self, db_name=None, entity_id=None, labels=None):
        self.db_name = db_name          # type: str
        self.entity_id = entity_id      # type: str
        self.labels = labels            # type: str

    def validate(self):
        self.validate_required(self.db_name, 'db_name')
        self.validate_required(self.entity_id, 'entity_id')

    def to_map(self):
        result = {}
        result['DbName'] = self.db_name
        result['EntityId'] = self.entity_id
        result['Labels'] = self.labels
        return result

    def from_map(self, map={}):
        self.db_name = map.get('DbName')
        self.entity_id = map.get('EntityId')
        self.labels = map.get('Labels')
        return self


class AddFaceEntityResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DeleteFaceEntityRequest(TeaModel):
    def __init__(self, db_name=None, entity_id=None):
        self.db_name = db_name          # type: str
        self.entity_id = entity_id      # type: str

    def validate(self):
        self.validate_required(self.db_name, 'db_name')
        self.validate_required(self.entity_id, 'entity_id')

    def to_map(self):
        result = {}
        result['DbName'] = self.db_name
        result['EntityId'] = self.entity_id
        return result

    def from_map(self, map={}):
        self.db_name = map.get('DbName')
        self.entity_id = map.get('EntityId')
        return self


class DeleteFaceEntityResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class ListFaceEntitiesRequest(TeaModel):
    def __init__(self, db_name=None, offset=None, limit=None, token=None, labels=None, entity_id_prefix=None,
                 order=None):
        self.db_name = db_name          # type: str
        self.offset = offset            # type: int
        self.limit = limit              # type: int
        self.token = token              # type: str
        self.labels = labels            # type: str
        self.entity_id_prefix = entity_id_prefix  # type: str
        self.order = order              # type: str

    def validate(self):
        self.validate_required(self.db_name, 'db_name')

    def to_map(self):
        result = {}
        result['DbName'] = self.db_name
        result['Offset'] = self.offset
        result['Limit'] = self.limit
        result['Token'] = self.token
        result['Labels'] = self.labels
        result['EntityIdPrefix'] = self.entity_id_prefix
        result['Order'] = self.order
        return result

    def from_map(self, map={}):
        self.db_name = map.get('DbName')
        self.offset = map.get('Offset')
        self.limit = map.get('Limit')
        self.token = map.get('Token')
        self.labels = map.get('Labels')
        self.entity_id_prefix = map.get('EntityIdPrefix')
        self.order = map.get('Order')
        return self


class ListFaceEntitiesResponse(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id    # type: str
        self.data = data                # type: ListFaceEntitiesResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = ListFaceEntitiesResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class ListFaceEntitiesResponseDataEntities(TeaModel):
    def __init__(self, db_name=None, entity_id=None, face_count=None, labels=None, created_at=None, updated_at=None):
        self.db_name = db_name          # type: str
        self.entity_id = entity_id      # type: str
        self.face_count = face_count    # type: int
        self.labels = labels            # type: str
        self.created_at = created_at    # type: int
        self.updated_at = updated_at    # type: int

    def validate(self):
        self.validate_required(self.db_name, 'db_name')
        self.validate_required(self.entity_id, 'entity_id')
        self.validate_required(self.face_count, 'face_count')
        self.validate_required(self.labels, 'labels')
        self.validate_required(self.created_at, 'created_at')
        self.validate_required(self.updated_at, 'updated_at')

    def to_map(self):
        result = {}
        result['DbName'] = self.db_name
        result['EntityId'] = self.entity_id
        result['FaceCount'] = self.face_count
        result['Labels'] = self.labels
        result['CreatedAt'] = self.created_at
        result['UpdatedAt'] = self.updated_at
        return result

    def from_map(self, map={}):
        self.db_name = map.get('DbName')
        self.entity_id = map.get('EntityId')
        self.face_count = map.get('FaceCount')
        self.labels = map.get('Labels')
        self.created_at = map.get('CreatedAt')
        self.updated_at = map.get('UpdatedAt')
        return self


class ListFaceEntitiesResponseData(TeaModel):
    def __init__(self, token=None, total_count=None, entities=None):
        self.token = token              # type: str
        self.total_count = total_count  # type: int
        self.entities = entities        # type: List[ListFaceEntitiesResponseDataEntities]

    def validate(self):
        self.validate_required(self.token, 'token')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.entities, 'entities')
        if self.entities:
            for k in self.entities:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Token'] = self.token
        result['TotalCount'] = self.total_count
        result['Entities'] = []
        if self.entities is not None:
            for k in self.entities:
                result['Entities'].append(k.to_map() if k else None)
        else:
            result['Entities'] = None
        return result

    def from_map(self, map={}):
        self.token = map.get('Token')
        self.total_count = map.get('TotalCount')
        self.entities = []
        if map.get('Entities') is not None:
            for k in map.get('Entities'):
                temp_model = ListFaceEntitiesResponseDataEntities()
                self.entities.append(temp_model.from_map(k))
        else:
            self.entities = None
        return self


class GetFaceEntityRequest(TeaModel):
    def __init__(self, db_name=None, entity_id=None):
        self.db_name = db_name          # type: str
        self.entity_id = entity_id      # type: str

    def validate(self):
        self.validate_required(self.db_name, 'db_name')
        self.validate_required(self.entity_id, 'entity_id')

    def to_map(self):
        result = {}
        result['DbName'] = self.db_name
        result['EntityId'] = self.entity_id
        return result

    def from_map(self, map={}):
        self.db_name = map.get('DbName')
        self.entity_id = map.get('EntityId')
        return self


class GetFaceEntityResponse(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id    # type: str
        self.data = data                # type: GetFaceEntityResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = GetFaceEntityResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class GetFaceEntityResponseDataFaces(TeaModel):
    def __init__(self, face_id=None):
        self.face_id = face_id          # type: str

    def validate(self):
        self.validate_required(self.face_id, 'face_id')

    def to_map(self):
        result = {}
        result['FaceId'] = self.face_id
        return result

    def from_map(self, map={}):
        self.face_id = map.get('FaceId')
        return self


class GetFaceEntityResponseData(TeaModel):
    def __init__(self, db_name=None, entity_id=None, labels=None, faces=None):
        self.db_name = db_name          # type: str
        self.entity_id = entity_id      # type: str
        self.labels = labels            # type: str
        self.faces = faces              # type: List[GetFaceEntityResponseDataFaces]

    def validate(self):
        self.validate_required(self.db_name, 'db_name')
        self.validate_required(self.entity_id, 'entity_id')
        self.validate_required(self.labels, 'labels')
        self.validate_required(self.faces, 'faces')
        if self.faces:
            for k in self.faces:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['DbName'] = self.db_name
        result['EntityId'] = self.entity_id
        result['Labels'] = self.labels
        result['Faces'] = []
        if self.faces is not None:
            for k in self.faces:
                result['Faces'].append(k.to_map() if k else None)
        else:
            result['Faces'] = None
        return result

    def from_map(self, map={}):
        self.db_name = map.get('DbName')
        self.entity_id = map.get('EntityId')
        self.labels = map.get('Labels')
        self.faces = []
        if map.get('Faces') is not None:
            for k in map.get('Faces'):
                temp_model = GetFaceEntityResponseDataFaces()
                self.faces.append(temp_model.from_map(k))
        else:
            self.faces = None
        return self


class UpdateFaceEntityRequest(TeaModel):
    def __init__(self, db_name=None, entity_id=None, labels=None):
        self.db_name = db_name          # type: str
        self.entity_id = entity_id      # type: str
        self.labels = labels            # type: str

    def validate(self):
        self.validate_required(self.db_name, 'db_name')
        self.validate_required(self.entity_id, 'entity_id')

    def to_map(self):
        result = {}
        result['DbName'] = self.db_name
        result['EntityId'] = self.entity_id
        result['Labels'] = self.labels
        return result

    def from_map(self, map={}):
        self.db_name = map.get('DbName')
        self.entity_id = map.get('EntityId')
        self.labels = map.get('Labels')
        return self


class UpdateFaceEntityResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class FaceMakeupRequest(TeaModel):
    def __init__(self, image_url=None, makeup_type=None, resource_type=None, strength=None):
        self.image_url = image_url      # type: str
        self.makeup_type = makeup_type  # type: str
        self.resource_type = resource_type  # type: str
        self.strength = strength        # type: float

    def validate(self):
        self.validate_required(self.image_url, 'image_url')
        self.validate_required(self.makeup_type, 'makeup_type')
        self.validate_required(self.resource_type, 'resource_type')
        self.validate_required(self.strength, 'strength')

    def to_map(self):
        result = {}
        result['ImageURL'] = self.image_url
        result['MakeupType'] = self.makeup_type
        result['ResourceType'] = self.resource_type
        result['Strength'] = self.strength
        return result

    def from_map(self, map={}):
        self.image_url = map.get('ImageURL')
        self.makeup_type = map.get('MakeupType')
        self.resource_type = map.get('ResourceType')
        self.strength = map.get('Strength')
        return self


class FaceMakeupResponse(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id    # type: str
        self.data = data                # type: FaceMakeupResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = FaceMakeupResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class FaceMakeupResponseData(TeaModel):
    def __init__(self, image_url=None):
        self.image_url = image_url      # type: str

    def validate(self):
        self.validate_required(self.image_url, 'image_url')

    def to_map(self):
        result = {}
        result['ImageURL'] = self.image_url
        return result

    def from_map(self, map={}):
        self.image_url = map.get('ImageURL')
        return self


class FaceMakeupAdvanceRequest(TeaModel):
    def __init__(self, image_urlobject=None, makeup_type=None, resource_type=None, strength=None):
        self.image_urlobject = image_urlobject  # type: BinaryIO
        self.makeup_type = makeup_type  # type: str
        self.resource_type = resource_type  # type: str
        self.strength = strength        # type: float

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')
        self.validate_required(self.makeup_type, 'makeup_type')
        self.validate_required(self.resource_type, 'resource_type')
        self.validate_required(self.strength, 'strength')

    def to_map(self):
        result = {}
        result['ImageURLObject'] = self.image_urlobject
        result['MakeupType'] = self.makeup_type
        result['ResourceType'] = self.resource_type
        result['Strength'] = self.strength
        return result

    def from_map(self, map={}):
        self.image_urlobject = map.get('ImageURLObject')
        self.makeup_type = map.get('MakeupType')
        self.resource_type = map.get('ResourceType')
        self.strength = map.get('Strength')
        return self


class HandPostureRequest(TeaModel):
    def __init__(self, image_url=None):
        self.image_url = image_url      # type: str

    def validate(self):
        self.validate_required(self.image_url, 'image_url')

    def to_map(self):
        result = {}
        result['ImageURL'] = self.image_url
        return result

    def from_map(self, map={}):
        self.image_url = map.get('ImageURL')
        return self


class HandPostureResponse(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id    # type: str
        self.data = data                # type: HandPostureResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = HandPostureResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class HandPostureResponseDataOutputsResultsBoxPositions(TeaModel):
    def __init__(self, points=None):
        self.points = points            # type: List[float]

    def validate(self):
        self.validate_required(self.points, 'points')

    def to_map(self):
        result = {}
        result['Points'] = self.points
        return result

    def from_map(self, map={}):
        self.points = map.get('Points')
        return self


class HandPostureResponseDataOutputsResultsBox(TeaModel):
    def __init__(self, confident=None, positions=None):
        self.confident = confident      # type: float
        self.positions = positions      # type: List[HandPostureResponseDataOutputsResultsBoxPositions]

    def validate(self):
        self.validate_required(self.confident, 'confident')
        self.validate_required(self.positions, 'positions')
        if self.positions:
            for k in self.positions:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Confident'] = self.confident
        result['Positions'] = []
        if self.positions is not None:
            for k in self.positions:
                result['Positions'].append(k.to_map() if k else None)
        else:
            result['Positions'] = None
        return result

    def from_map(self, map={}):
        self.confident = map.get('Confident')
        self.positions = []
        if map.get('Positions') is not None:
            for k in map.get('Positions'):
                temp_model = HandPostureResponseDataOutputsResultsBoxPositions()
                self.positions.append(temp_model.from_map(k))
        else:
            self.positions = None
        return self


class HandPostureResponseDataOutputsResultsHandsKeyPointsPositions(TeaModel):
    def __init__(self, points=None):
        self.points = points            # type: List[float]

    def validate(self):
        self.validate_required(self.points, 'points')

    def to_map(self):
        result = {}
        result['Points'] = self.points
        return result

    def from_map(self, map={}):
        self.points = map.get('Points')
        return self


class HandPostureResponseDataOutputsResultsHandsKeyPoints(TeaModel):
    def __init__(self, label=None, positions=None):
        self.label = label              # type: str
        self.positions = positions      # type: List[HandPostureResponseDataOutputsResultsHandsKeyPointsPositions]

    def validate(self):
        self.validate_required(self.label, 'label')
        self.validate_required(self.positions, 'positions')
        if self.positions:
            for k in self.positions:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Label'] = self.label
        result['Positions'] = []
        if self.positions is not None:
            for k in self.positions:
                result['Positions'].append(k.to_map() if k else None)
        else:
            result['Positions'] = None
        return result

    def from_map(self, map={}):
        self.label = map.get('Label')
        self.positions = []
        if map.get('Positions') is not None:
            for k in map.get('Positions'):
                temp_model = HandPostureResponseDataOutputsResultsHandsKeyPointsPositions()
                self.positions.append(temp_model.from_map(k))
        else:
            self.positions = None
        return self


class HandPostureResponseDataOutputsResultsHands(TeaModel):
    def __init__(self, confident=None, key_points=None):
        self.confident = confident      # type: float
        self.key_points = key_points    # type: List[HandPostureResponseDataOutputsResultsHandsKeyPoints]

    def validate(self):
        self.validate_required(self.confident, 'confident')
        self.validate_required(self.key_points, 'key_points')
        if self.key_points:
            for k in self.key_points:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Confident'] = self.confident
        result['KeyPoints'] = []
        if self.key_points is not None:
            for k in self.key_points:
                result['KeyPoints'].append(k.to_map() if k else None)
        else:
            result['KeyPoints'] = None
        return result

    def from_map(self, map={}):
        self.confident = map.get('Confident')
        self.key_points = []
        if map.get('KeyPoints') is not None:
            for k in map.get('KeyPoints'):
                temp_model = HandPostureResponseDataOutputsResultsHandsKeyPoints()
                self.key_points.append(temp_model.from_map(k))
        else:
            self.key_points = None
        return self


class HandPostureResponseDataOutputsResults(TeaModel):
    def __init__(self, box=None, hands=None):
        self.box = box                  # type: HandPostureResponseDataOutputsResultsBox
        self.hands = hands              # type: HandPostureResponseDataOutputsResultsHands

    def validate(self):
        self.validate_required(self.box, 'box')
        if self.box:
            self.box.validate()
        self.validate_required(self.hands, 'hands')
        if self.hands:
            self.hands.validate()

    def to_map(self):
        result = {}
        if self.box is not None:
            result['Box'] = self.box.to_map()
        else:
            result['Box'] = None
        if self.hands is not None:
            result['Hands'] = self.hands.to_map()
        else:
            result['Hands'] = None
        return result

    def from_map(self, map={}):
        if map.get('Box') is not None:
            temp_model = HandPostureResponseDataOutputsResultsBox()
            self.box = temp_model.from_map(map['Box'])
        else:
            self.box = None
        if map.get('Hands') is not None:
            temp_model = HandPostureResponseDataOutputsResultsHands()
            self.hands = temp_model.from_map(map['Hands'])
        else:
            self.hands = None
        return self


class HandPostureResponseDataOutputs(TeaModel):
    def __init__(self, hand_count=None, results=None):
        self.hand_count = hand_count    # type: int
        self.results = results          # type: List[HandPostureResponseDataOutputsResults]

    def validate(self):
        self.validate_required(self.hand_count, 'hand_count')
        self.validate_required(self.results, 'results')
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['HandCount'] = self.hand_count
        result['Results'] = []
        if self.results is not None:
            for k in self.results:
                result['Results'].append(k.to_map() if k else None)
        else:
            result['Results'] = None
        return result

    def from_map(self, map={}):
        self.hand_count = map.get('HandCount')
        self.results = []
        if map.get('Results') is not None:
            for k in map.get('Results'):
                temp_model = HandPostureResponseDataOutputsResults()
                self.results.append(temp_model.from_map(k))
        else:
            self.results = None
        return self


class HandPostureResponseDataMetaObject(TeaModel):
    def __init__(self, height=None, width=None):
        self.height = height            # type: int
        self.width = width              # type: int

    def validate(self):
        self.validate_required(self.height, 'height')
        self.validate_required(self.width, 'width')

    def to_map(self):
        result = {}
        result['Height'] = self.height
        result['Width'] = self.width
        return result

    def from_map(self, map={}):
        self.height = map.get('Height')
        self.width = map.get('Width')
        return self


class HandPostureResponseData(TeaModel):
    def __init__(self, outputs=None, meta_object=None):
        self.outputs = outputs          # type: List[HandPostureResponseDataOutputs]
        self.meta_object = meta_object  # type: HandPostureResponseDataMetaObject

    def validate(self):
        self.validate_required(self.outputs, 'outputs')
        if self.outputs:
            for k in self.outputs:
                if k:
                    k.validate()
        self.validate_required(self.meta_object, 'meta_object')
        if self.meta_object:
            self.meta_object.validate()

    def to_map(self):
        result = {}
        result['Outputs'] = []
        if self.outputs is not None:
            for k in self.outputs:
                result['Outputs'].append(k.to_map() if k else None)
        else:
            result['Outputs'] = None
        if self.meta_object is not None:
            result['MetaObject'] = self.meta_object.to_map()
        else:
            result['MetaObject'] = None
        return result

    def from_map(self, map={}):
        self.outputs = []
        if map.get('Outputs') is not None:
            for k in map.get('Outputs'):
                temp_model = HandPostureResponseDataOutputs()
                self.outputs.append(temp_model.from_map(k))
        else:
            self.outputs = None
        if map.get('MetaObject') is not None:
            temp_model = HandPostureResponseDataMetaObject()
            self.meta_object = temp_model.from_map(map['MetaObject'])
        else:
            self.meta_object = None
        return self


class HandPostureAdvanceRequest(TeaModel):
    def __init__(self, image_urlobject=None):
        self.image_urlobject = image_urlobject  # type: BinaryIO

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        result = {}
        result['ImageURLObject'] = self.image_urlobject
        return result

    def from_map(self, map={}):
        self.image_urlobject = map.get('ImageURLObject')
        return self


class BodyPostureRequest(TeaModel):
    def __init__(self, image_url=None):
        self.image_url = image_url      # type: str

    def validate(self):
        self.validate_required(self.image_url, 'image_url')

    def to_map(self):
        result = {}
        result['ImageURL'] = self.image_url
        return result

    def from_map(self, map={}):
        self.image_url = map.get('ImageURL')
        return self


class BodyPostureResponse(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id    # type: str
        self.data = data                # type: BodyPostureResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = BodyPostureResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class BodyPostureResponseDataOutputsResultsBodiesPositions(TeaModel):
    def __init__(self, points=None):
        self.points = points            # type: List[float]

    def validate(self):
        self.validate_required(self.points, 'points')

    def to_map(self):
        result = {}
        result['Points'] = self.points
        return result

    def from_map(self, map={}):
        self.points = map.get('Points')
        return self


class BodyPostureResponseDataOutputsResultsBodies(TeaModel):
    def __init__(self, confident=None, label=None, positions=None):
        self.confident = confident      # type: float
        self.label = label              # type: str
        self.positions = positions      # type: List[BodyPostureResponseDataOutputsResultsBodiesPositions]

    def validate(self):
        self.validate_required(self.confident, 'confident')
        self.validate_required(self.label, 'label')
        self.validate_required(self.positions, 'positions')
        if self.positions:
            for k in self.positions:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Confident'] = self.confident
        result['Label'] = self.label
        result['Positions'] = []
        if self.positions is not None:
            for k in self.positions:
                result['Positions'].append(k.to_map() if k else None)
        else:
            result['Positions'] = None
        return result

    def from_map(self, map={}):
        self.confident = map.get('Confident')
        self.label = map.get('Label')
        self.positions = []
        if map.get('Positions') is not None:
            for k in map.get('Positions'):
                temp_model = BodyPostureResponseDataOutputsResultsBodiesPositions()
                self.positions.append(temp_model.from_map(k))
        else:
            self.positions = None
        return self


class BodyPostureResponseDataOutputsResults(TeaModel):
    def __init__(self, bodies=None):
        self.bodies = bodies            # type: List[BodyPostureResponseDataOutputsResultsBodies]

    def validate(self):
        self.validate_required(self.bodies, 'bodies')
        if self.bodies:
            for k in self.bodies:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Bodies'] = []
        if self.bodies is not None:
            for k in self.bodies:
                result['Bodies'].append(k.to_map() if k else None)
        else:
            result['Bodies'] = None
        return result

    def from_map(self, map={}):
        self.bodies = []
        if map.get('Bodies') is not None:
            for k in map.get('Bodies'):
                temp_model = BodyPostureResponseDataOutputsResultsBodies()
                self.bodies.append(temp_model.from_map(k))
        else:
            self.bodies = None
        return self


class BodyPostureResponseDataOutputs(TeaModel):
    def __init__(self, human_count=None, results=None):
        self.human_count = human_count  # type: int
        self.results = results          # type: List[BodyPostureResponseDataOutputsResults]

    def validate(self):
        self.validate_required(self.human_count, 'human_count')
        self.validate_required(self.results, 'results')
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['HumanCount'] = self.human_count
        result['Results'] = []
        if self.results is not None:
            for k in self.results:
                result['Results'].append(k.to_map() if k else None)
        else:
            result['Results'] = None
        return result

    def from_map(self, map={}):
        self.human_count = map.get('HumanCount')
        self.results = []
        if map.get('Results') is not None:
            for k in map.get('Results'):
                temp_model = BodyPostureResponseDataOutputsResults()
                self.results.append(temp_model.from_map(k))
        else:
            self.results = None
        return self


class BodyPostureResponseDataMetaObject(TeaModel):
    def __init__(self, height=None, width=None):
        self.height = height            # type: int
        self.width = width              # type: int

    def validate(self):
        self.validate_required(self.height, 'height')
        self.validate_required(self.width, 'width')

    def to_map(self):
        result = {}
        result['Height'] = self.height
        result['Width'] = self.width
        return result

    def from_map(self, map={}):
        self.height = map.get('Height')
        self.width = map.get('Width')
        return self


class BodyPostureResponseData(TeaModel):
    def __init__(self, outputs=None, meta_object=None):
        self.outputs = outputs          # type: List[BodyPostureResponseDataOutputs]
        self.meta_object = meta_object  # type: BodyPostureResponseDataMetaObject

    def validate(self):
        self.validate_required(self.outputs, 'outputs')
        if self.outputs:
            for k in self.outputs:
                if k:
                    k.validate()
        self.validate_required(self.meta_object, 'meta_object')
        if self.meta_object:
            self.meta_object.validate()

    def to_map(self):
        result = {}
        result['Outputs'] = []
        if self.outputs is not None:
            for k in self.outputs:
                result['Outputs'].append(k.to_map() if k else None)
        else:
            result['Outputs'] = None
        if self.meta_object is not None:
            result['MetaObject'] = self.meta_object.to_map()
        else:
            result['MetaObject'] = None
        return result

    def from_map(self, map={}):
        self.outputs = []
        if map.get('Outputs') is not None:
            for k in map.get('Outputs'):
                temp_model = BodyPostureResponseDataOutputs()
                self.outputs.append(temp_model.from_map(k))
        else:
            self.outputs = None
        if map.get('MetaObject') is not None:
            temp_model = BodyPostureResponseDataMetaObject()
            self.meta_object = temp_model.from_map(map['MetaObject'])
        else:
            self.meta_object = None
        return self


class BodyPostureAdvanceRequest(TeaModel):
    def __init__(self, image_urlobject=None):
        self.image_urlobject = image_urlobject  # type: BinaryIO

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        result = {}
        result['ImageURLObject'] = self.image_urlobject
        return result

    def from_map(self, map={}):
        self.image_urlobject = map.get('ImageURLObject')
        return self


class DetectPedestrianRequest(TeaModel):
    def __init__(self, image_url=None):
        self.image_url = image_url      # type: str

    def validate(self):
        self.validate_required(self.image_url, 'image_url')

    def to_map(self):
        result = {}
        result['ImageURL'] = self.image_url
        return result

    def from_map(self, map={}):
        self.image_url = map.get('ImageURL')
        return self


class DetectPedestrianResponse(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id    # type: str
        self.data = data                # type: DetectPedestrianResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = DetectPedestrianResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class DetectPedestrianResponseDataElements(TeaModel):
    def __init__(self, score=None, type=None, boxes=None):
        self.score = score              # type: float
        self.type = type                # type: str
        self.boxes = boxes              # type: List[int]

    def validate(self):
        self.validate_required(self.score, 'score')
        self.validate_required(self.type, 'type')
        self.validate_required(self.boxes, 'boxes')

    def to_map(self):
        result = {}
        result['Score'] = self.score
        result['Type'] = self.type
        result['Boxes'] = self.boxes
        return result

    def from_map(self, map={}):
        self.score = map.get('Score')
        self.type = map.get('Type')
        self.boxes = map.get('Boxes')
        return self


class DetectPedestrianResponseData(TeaModel):
    def __init__(self, height=None, width=None, elements=None):
        self.height = height            # type: int
        self.width = width              # type: int
        self.elements = elements        # type: List[DetectPedestrianResponseDataElements]

    def validate(self):
        self.validate_required(self.height, 'height')
        self.validate_required(self.width, 'width')
        self.validate_required(self.elements, 'elements')
        if self.elements:
            for k in self.elements:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Height'] = self.height
        result['Width'] = self.width
        result['Elements'] = []
        if self.elements is not None:
            for k in self.elements:
                result['Elements'].append(k.to_map() if k else None)
        else:
            result['Elements'] = None
        return result

    def from_map(self, map={}):
        self.height = map.get('Height')
        self.width = map.get('Width')
        self.elements = []
        if map.get('Elements') is not None:
            for k in map.get('Elements'):
                temp_model = DetectPedestrianResponseDataElements()
                self.elements.append(temp_model.from_map(k))
        else:
            self.elements = None
        return self


class DetectPedestrianAdvanceRequest(TeaModel):
    def __init__(self, image_urlobject=None):
        self.image_urlobject = image_urlobject  # type: BinaryIO

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        result = {}
        result['ImageURLObject'] = self.image_urlobject
        return result

    def from_map(self, map={}):
        self.image_urlobject = map.get('ImageURLObject')
        return self


class FaceBeautyRequest(TeaModel):
    def __init__(self, image_url=None, sharp=None, smooth=None, white=None):
        self.image_url = image_url      # type: str
        self.sharp = sharp              # type: float
        self.smooth = smooth            # type: float
        self.white = white              # type: float

    def validate(self):
        self.validate_required(self.image_url, 'image_url')
        self.validate_required(self.sharp, 'sharp')
        self.validate_required(self.smooth, 'smooth')
        self.validate_required(self.white, 'white')

    def to_map(self):
        result = {}
        result['ImageURL'] = self.image_url
        result['Sharp'] = self.sharp
        result['Smooth'] = self.smooth
        result['White'] = self.white
        return result

    def from_map(self, map={}):
        self.image_url = map.get('ImageURL')
        self.sharp = map.get('Sharp')
        self.smooth = map.get('Smooth')
        self.white = map.get('White')
        return self


class FaceBeautyResponse(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id    # type: str
        self.data = data                # type: FaceBeautyResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = FaceBeautyResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class FaceBeautyResponseData(TeaModel):
    def __init__(self, image_url=None):
        self.image_url = image_url      # type: str

    def validate(self):
        self.validate_required(self.image_url, 'image_url')

    def to_map(self):
        result = {}
        result['ImageURL'] = self.image_url
        return result

    def from_map(self, map={}):
        self.image_url = map.get('ImageURL')
        return self


class FaceBeautyAdvanceRequest(TeaModel):
    def __init__(self, image_urlobject=None, sharp=None, smooth=None, white=None):
        self.image_urlobject = image_urlobject  # type: BinaryIO
        self.sharp = sharp              # type: float
        self.smooth = smooth            # type: float
        self.white = white              # type: float

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')
        self.validate_required(self.sharp, 'sharp')
        self.validate_required(self.smooth, 'smooth')
        self.validate_required(self.white, 'white')

    def to_map(self):
        result = {}
        result['ImageURLObject'] = self.image_urlobject
        result['Sharp'] = self.sharp
        result['Smooth'] = self.smooth
        result['White'] = self.white
        return result

    def from_map(self, map={}):
        self.image_urlobject = map.get('ImageURLObject')
        self.sharp = map.get('Sharp')
        self.smooth = map.get('Smooth')
        self.white = map.get('White')
        return self


class FaceFilterRequest(TeaModel):
    def __init__(self, image_url=None, resource_type=None, strength=None):
        self.image_url = image_url      # type: str
        self.resource_type = resource_type  # type: str
        self.strength = strength        # type: float

    def validate(self):
        self.validate_required(self.image_url, 'image_url')
        self.validate_required(self.resource_type, 'resource_type')
        self.validate_required(self.strength, 'strength')

    def to_map(self):
        result = {}
        result['ImageURL'] = self.image_url
        result['ResourceType'] = self.resource_type
        result['Strength'] = self.strength
        return result

    def from_map(self, map={}):
        self.image_url = map.get('ImageURL')
        self.resource_type = map.get('ResourceType')
        self.strength = map.get('Strength')
        return self


class FaceFilterResponse(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id    # type: str
        self.data = data                # type: FaceFilterResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = FaceFilterResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class FaceFilterResponseData(TeaModel):
    def __init__(self, image_url=None):
        self.image_url = image_url      # type: str

    def validate(self):
        self.validate_required(self.image_url, 'image_url')

    def to_map(self):
        result = {}
        result['ImageURL'] = self.image_url
        return result

    def from_map(self, map={}):
        self.image_url = map.get('ImageURL')
        return self


class FaceFilterAdvanceRequest(TeaModel):
    def __init__(self, image_urlobject=None, resource_type=None, strength=None):
        self.image_urlobject = image_urlobject  # type: BinaryIO
        self.resource_type = resource_type  # type: str
        self.strength = strength        # type: float

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')
        self.validate_required(self.resource_type, 'resource_type')
        self.validate_required(self.strength, 'strength')

    def to_map(self):
        result = {}
        result['ImageURLObject'] = self.image_urlobject
        result['ResourceType'] = self.resource_type
        result['Strength'] = self.strength
        return result

    def from_map(self, map={}):
        self.image_urlobject = map.get('ImageURLObject')
        self.resource_type = map.get('ResourceType')
        self.strength = map.get('Strength')
        return self


class EnhanceFaceRequest(TeaModel):
    def __init__(self, image_url=None):
        self.image_url = image_url      # type: str

    def validate(self):
        self.validate_required(self.image_url, 'image_url')

    def to_map(self):
        result = {}
        result['ImageURL'] = self.image_url
        return result

    def from_map(self, map={}):
        self.image_url = map.get('ImageURL')
        return self


class EnhanceFaceResponse(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id    # type: str
        self.data = data                # type: EnhanceFaceResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = EnhanceFaceResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class EnhanceFaceResponseData(TeaModel):
    def __init__(self, image_url=None):
        self.image_url = image_url      # type: str

    def validate(self):
        self.validate_required(self.image_url, 'image_url')

    def to_map(self):
        result = {}
        result['ImageURL'] = self.image_url
        return result

    def from_map(self, map={}):
        self.image_url = map.get('ImageURL')
        return self


class EnhanceFaceAdvanceRequest(TeaModel):
    def __init__(self, image_urlobject=None):
        self.image_urlobject = image_urlobject  # type: BinaryIO

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        result = {}
        result['ImageURLObject'] = self.image_urlobject
        return result

    def from_map(self, map={}):
        self.image_urlobject = map.get('ImageURLObject')
        return self


class FaceTidyupRequest(TeaModel):
    def __init__(self, image_url=None, shape_type=None, strength=None):
        self.image_url = image_url      # type: str
        self.shape_type = shape_type    # type: int
        self.strength = strength        # type: float

    def validate(self):
        self.validate_required(self.image_url, 'image_url')
        self.validate_required(self.shape_type, 'shape_type')
        self.validate_required(self.strength, 'strength')

    def to_map(self):
        result = {}
        result['ImageURL'] = self.image_url
        result['ShapeType'] = self.shape_type
        result['Strength'] = self.strength
        return result

    def from_map(self, map={}):
        self.image_url = map.get('ImageURL')
        self.shape_type = map.get('ShapeType')
        self.strength = map.get('Strength')
        return self


class FaceTidyupResponse(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id    # type: str
        self.data = data                # type: FaceTidyupResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = FaceTidyupResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class FaceTidyupResponseData(TeaModel):
    def __init__(self, image_url=None):
        self.image_url = image_url      # type: str

    def validate(self):
        self.validate_required(self.image_url, 'image_url')

    def to_map(self):
        result = {}
        result['ImageURL'] = self.image_url
        return result

    def from_map(self, map={}):
        self.image_url = map.get('ImageURL')
        return self


class FaceTidyupAdvanceRequest(TeaModel):
    def __init__(self, image_urlobject=None, shape_type=None, strength=None):
        self.image_urlobject = image_urlobject  # type: BinaryIO
        self.shape_type = shape_type    # type: int
        self.strength = strength        # type: float

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')
        self.validate_required(self.shape_type, 'shape_type')
        self.validate_required(self.strength, 'strength')

    def to_map(self):
        result = {}
        result['ImageURLObject'] = self.image_urlobject
        result['ShapeType'] = self.shape_type
        result['Strength'] = self.strength
        return result

    def from_map(self, map={}):
        self.image_urlobject = map.get('ImageURLObject')
        self.shape_type = map.get('ShapeType')
        self.strength = map.get('Strength')
        return self


class SearchFaceRequest(TeaModel):
    def __init__(self, db_name=None, image_url=None, limit=None):
        self.db_name = db_name          # type: str
        self.image_url = image_url      # type: str
        self.limit = limit              # type: int

    def validate(self):
        self.validate_required(self.db_name, 'db_name')
        self.validate_required(self.image_url, 'image_url')
        self.validate_required(self.limit, 'limit')

    def to_map(self):
        result = {}
        result['DbName'] = self.db_name
        result['ImageUrl'] = self.image_url
        result['Limit'] = self.limit
        return result

    def from_map(self, map={}):
        self.db_name = map.get('DbName')
        self.image_url = map.get('ImageUrl')
        self.limit = map.get('Limit')
        return self


class SearchFaceResponse(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id    # type: str
        self.data = data                # type: SearchFaceResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = SearchFaceResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class SearchFaceResponseDataMatchListFaceItems(TeaModel):
    def __init__(self, face_id=None, score=None, extra_data=None, entity_id=None):
        self.face_id = face_id          # type: str
        self.score = score              # type: float
        self.extra_data = extra_data    # type: str
        self.entity_id = entity_id      # type: str

    def validate(self):
        self.validate_required(self.face_id, 'face_id')
        self.validate_required(self.score, 'score')
        self.validate_required(self.extra_data, 'extra_data')
        self.validate_required(self.entity_id, 'entity_id')

    def to_map(self):
        result = {}
        result['FaceId'] = self.face_id
        result['Score'] = self.score
        result['ExtraData'] = self.extra_data
        result['EntityId'] = self.entity_id
        return result

    def from_map(self, map={}):
        self.face_id = map.get('FaceId')
        self.score = map.get('Score')
        self.extra_data = map.get('ExtraData')
        self.entity_id = map.get('EntityId')
        return self


class SearchFaceResponseDataMatchListLocation(TeaModel):
    def __init__(self, x=None, y=None, width=None, height=None):
        self.x = x                      # type: int
        self.y = y                      # type: int
        self.width = width              # type: int
        self.height = height            # type: int

    def validate(self):
        self.validate_required(self.x, 'x')
        self.validate_required(self.y, 'y')
        self.validate_required(self.width, 'width')
        self.validate_required(self.height, 'height')

    def to_map(self):
        result = {}
        result['X'] = self.x
        result['Y'] = self.y
        result['Width'] = self.width
        result['Height'] = self.height
        return result

    def from_map(self, map={}):
        self.x = map.get('X')
        self.y = map.get('Y')
        self.width = map.get('Width')
        self.height = map.get('Height')
        return self


class SearchFaceResponseDataMatchList(TeaModel):
    def __init__(self, face_items=None, location=None):
        self.face_items = face_items    # type: List[SearchFaceResponseDataMatchListFaceItems]
        self.location = location        # type: SearchFaceResponseDataMatchListLocation

    def validate(self):
        self.validate_required(self.face_items, 'face_items')
        if self.face_items:
            for k in self.face_items:
                if k:
                    k.validate()
        self.validate_required(self.location, 'location')
        if self.location:
            self.location.validate()

    def to_map(self):
        result = {}
        result['FaceItems'] = []
        if self.face_items is not None:
            for k in self.face_items:
                result['FaceItems'].append(k.to_map() if k else None)
        else:
            result['FaceItems'] = None
        if self.location is not None:
            result['Location'] = self.location.to_map()
        else:
            result['Location'] = None
        return result

    def from_map(self, map={}):
        self.face_items = []
        if map.get('FaceItems') is not None:
            for k in map.get('FaceItems'):
                temp_model = SearchFaceResponseDataMatchListFaceItems()
                self.face_items.append(temp_model.from_map(k))
        else:
            self.face_items = None
        if map.get('Location') is not None:
            temp_model = SearchFaceResponseDataMatchListLocation()
            self.location = temp_model.from_map(map['Location'])
        else:
            self.location = None
        return self


class SearchFaceResponseData(TeaModel):
    def __init__(self, match_list=None):
        self.match_list = match_list    # type: List[SearchFaceResponseDataMatchList]

    def validate(self):
        self.validate_required(self.match_list, 'match_list')
        if self.match_list:
            for k in self.match_list:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['MatchList'] = []
        if self.match_list is not None:
            for k in self.match_list:
                result['MatchList'].append(k.to_map() if k else None)
        else:
            result['MatchList'] = None
        return result

    def from_map(self, map={}):
        self.match_list = []
        if map.get('MatchList') is not None:
            for k in map.get('MatchList'):
                temp_model = SearchFaceResponseDataMatchList()
                self.match_list.append(temp_model.from_map(k))
        else:
            self.match_list = None
        return self


class SearchFaceAdvanceRequest(TeaModel):
    def __init__(self, image_url_object=None, db_name=None, limit=None):
        self.image_url_object = image_url_object  # type: BinaryIO
        self.db_name = db_name          # type: str
        self.limit = limit              # type: int

    def validate(self):
        self.validate_required(self.image_url_object, 'image_url_object')
        self.validate_required(self.db_name, 'db_name')
        self.validate_required(self.limit, 'limit')

    def to_map(self):
        result = {}
        result['ImageUrlObject'] = self.image_url_object
        result['DbName'] = self.db_name
        result['Limit'] = self.limit
        return result

    def from_map(self, map={}):
        self.image_url_object = map.get('ImageUrlObject')
        self.db_name = map.get('DbName')
        self.limit = map.get('Limit')
        return self


class ListFaceDbsRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        result = {}
        return result

    def from_map(self, map={}):
        return self


class ListFaceDbsResponse(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id    # type: str
        self.data = data                # type: ListFaceDbsResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = ListFaceDbsResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class ListFaceDbsResponseDataDbList(TeaModel):
    def __init__(self, name=None):
        self.name = name                # type: str

    def validate(self):
        self.validate_required(self.name, 'name')

    def to_map(self):
        result = {}
        result['Name'] = self.name
        return result

    def from_map(self, map={}):
        self.name = map.get('Name')
        return self


class ListFaceDbsResponseData(TeaModel):
    def __init__(self, db_list=None):
        self.db_list = db_list          # type: List[ListFaceDbsResponseDataDbList]

    def validate(self):
        self.validate_required(self.db_list, 'db_list')
        if self.db_list:
            for k in self.db_list:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['DbList'] = []
        if self.db_list is not None:
            for k in self.db_list:
                result['DbList'].append(k.to_map() if k else None)
        else:
            result['DbList'] = None
        return result

    def from_map(self, map={}):
        self.db_list = []
        if map.get('DbList') is not None:
            for k in map.get('DbList'):
                temp_model = ListFaceDbsResponseDataDbList()
                self.db_list.append(temp_model.from_map(k))
        else:
            self.db_list = None
        return self


class CreateFaceDbRequest(TeaModel):
    def __init__(self, name=None):
        self.name = name                # type: str

    def validate(self):
        self.validate_required(self.name, 'name')

    def to_map(self):
        result = {}
        result['Name'] = self.name
        return result

    def from_map(self, map={}):
        self.name = map.get('Name')
        return self


class CreateFaceDbResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DeleteFaceRequest(TeaModel):
    def __init__(self, db_name=None, face_id=None):
        self.db_name = db_name          # type: str
        self.face_id = face_id          # type: str

    def validate(self):
        self.validate_required(self.db_name, 'db_name')
        self.validate_required(self.face_id, 'face_id')

    def to_map(self):
        result = {}
        result['DbName'] = self.db_name
        result['FaceId'] = self.face_id
        return result

    def from_map(self, map={}):
        self.db_name = map.get('DbName')
        self.face_id = map.get('FaceId')
        return self


class DeleteFaceResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DeleteFaceDbRequest(TeaModel):
    def __init__(self, name=None):
        self.name = name                # type: str

    def validate(self):
        self.validate_required(self.name, 'name')

    def to_map(self):
        result = {}
        result['Name'] = self.name
        return result

    def from_map(self, map={}):
        self.name = map.get('Name')
        return self


class DeleteFaceDbResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class AddFaceRequest(TeaModel):
    def __init__(self, db_name=None, image_url=None, entity_id=None, extra_data=None):
        self.db_name = db_name          # type: str
        self.image_url = image_url      # type: str
        self.entity_id = entity_id      # type: str
        self.extra_data = extra_data    # type: str

    def validate(self):
        self.validate_required(self.db_name, 'db_name')
        self.validate_required(self.image_url, 'image_url')
        self.validate_required(self.entity_id, 'entity_id')

    def to_map(self):
        result = {}
        result['DbName'] = self.db_name
        result['ImageUrl'] = self.image_url
        result['EntityId'] = self.entity_id
        result['ExtraData'] = self.extra_data
        return result

    def from_map(self, map={}):
        self.db_name = map.get('DbName')
        self.image_url = map.get('ImageUrl')
        self.entity_id = map.get('EntityId')
        self.extra_data = map.get('ExtraData')
        return self


class AddFaceResponse(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id    # type: str
        self.data = data                # type: AddFaceResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = AddFaceResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class AddFaceResponseData(TeaModel):
    def __init__(self, face_id=None):
        self.face_id = face_id          # type: str

    def validate(self):
        self.validate_required(self.face_id, 'face_id')

    def to_map(self):
        result = {}
        result['FaceId'] = self.face_id
        return result

    def from_map(self, map={}):
        self.face_id = map.get('FaceId')
        return self


class AddFaceAdvanceRequest(TeaModel):
    def __init__(self, image_url_object=None, db_name=None, entity_id=None, extra_data=None):
        self.image_url_object = image_url_object  # type: BinaryIO
        self.db_name = db_name          # type: str
        self.entity_id = entity_id      # type: str
        self.extra_data = extra_data    # type: str

    def validate(self):
        self.validate_required(self.image_url_object, 'image_url_object')
        self.validate_required(self.db_name, 'db_name')
        self.validate_required(self.entity_id, 'entity_id')

    def to_map(self):
        result = {}
        result['ImageUrlObject'] = self.image_url_object
        result['DbName'] = self.db_name
        result['EntityId'] = self.entity_id
        result['ExtraData'] = self.extra_data
        return result

    def from_map(self, map={}):
        self.image_url_object = map.get('ImageUrlObject')
        self.db_name = map.get('DbName')
        self.entity_id = map.get('EntityId')
        self.extra_data = map.get('ExtraData')
        return self


class RecognizeExpressionRequest(TeaModel):
    def __init__(self, image_url=None):
        self.image_url = image_url      # type: str

    def validate(self):
        self.validate_required(self.image_url, 'image_url')

    def to_map(self):
        result = {}
        result['ImageURL'] = self.image_url
        return result

    def from_map(self, map={}):
        self.image_url = map.get('ImageURL')
        return self


class RecognizeExpressionResponse(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id    # type: str
        self.data = data                # type: RecognizeExpressionResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = RecognizeExpressionResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class RecognizeExpressionResponseDataElementsFaceRectangle(TeaModel):
    def __init__(self, height=None, left=None, top=None, width=None):
        self.height = height            # type: int
        self.left = left                # type: int
        self.top = top                  # type: int
        self.width = width              # type: int

    def validate(self):
        self.validate_required(self.height, 'height')
        self.validate_required(self.left, 'left')
        self.validate_required(self.top, 'top')
        self.validate_required(self.width, 'width')

    def to_map(self):
        result = {}
        result['Height'] = self.height
        result['Left'] = self.left
        result['Top'] = self.top
        result['Width'] = self.width
        return result

    def from_map(self, map={}):
        self.height = map.get('Height')
        self.left = map.get('Left')
        self.top = map.get('Top')
        self.width = map.get('Width')
        return self


class RecognizeExpressionResponseDataElements(TeaModel):
    def __init__(self, expression=None, face_probability=None, face_rectangle=None):
        self.expression = expression    # type: str
        self.face_probability = face_probability  # type: float
        self.face_rectangle = face_rectangle  # type: RecognizeExpressionResponseDataElementsFaceRectangle

    def validate(self):
        self.validate_required(self.expression, 'expression')
        self.validate_required(self.face_probability, 'face_probability')
        self.validate_required(self.face_rectangle, 'face_rectangle')
        if self.face_rectangle:
            self.face_rectangle.validate()

    def to_map(self):
        result = {}
        result['Expression'] = self.expression
        result['FaceProbability'] = self.face_probability
        if self.face_rectangle is not None:
            result['FaceRectangle'] = self.face_rectangle.to_map()
        else:
            result['FaceRectangle'] = None
        return result

    def from_map(self, map={}):
        self.expression = map.get('Expression')
        self.face_probability = map.get('FaceProbability')
        if map.get('FaceRectangle') is not None:
            temp_model = RecognizeExpressionResponseDataElementsFaceRectangle()
            self.face_rectangle = temp_model.from_map(map['FaceRectangle'])
        else:
            self.face_rectangle = None
        return self


class RecognizeExpressionResponseData(TeaModel):
    def __init__(self, elements=None):
        self.elements = elements        # type: List[RecognizeExpressionResponseDataElements]

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
        else:
            result['Elements'] = None
        return result

    def from_map(self, map={}):
        self.elements = []
        if map.get('Elements') is not None:
            for k in map.get('Elements'):
                temp_model = RecognizeExpressionResponseDataElements()
                self.elements.append(temp_model.from_map(k))
        else:
            self.elements = None
        return self


class RecognizeExpressionAdvanceRequest(TeaModel):
    def __init__(self, image_urlobject=None):
        self.image_urlobject = image_urlobject  # type: BinaryIO

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        result = {}
        result['ImageURLObject'] = self.image_urlobject
        return result

    def from_map(self, map={}):
        self.image_urlobject = map.get('ImageURLObject')
        return self


class RecognizePublicFaceRequest(TeaModel):
    def __init__(self, task=None):
        self.task = task                # type: List[RecognizePublicFaceRequestTask]

    def validate(self):
        self.validate_required(self.task, 'task')
        if self.task:
            for k in self.task:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Task'] = []
        if self.task is not None:
            for k in self.task:
                result['Task'].append(k.to_map() if k else None)
        else:
            result['Task'] = None
        return result

    def from_map(self, map={}):
        self.task = []
        if map.get('Task') is not None:
            for k in map.get('Task'):
                temp_model = RecognizePublicFaceRequestTask()
                self.task.append(temp_model.from_map(k))
        else:
            self.task = None
        return self


class RecognizePublicFaceRequestTask(TeaModel):
    def __init__(self, image_url=None):
        self.image_url = image_url      # type: str

    def validate(self):
        self.validate_required(self.image_url, 'image_url')

    def to_map(self):
        result = {}
        result['ImageURL'] = self.image_url
        return result

    def from_map(self, map={}):
        self.image_url = map.get('ImageURL')
        return self


class RecognizePublicFaceResponse(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id    # type: str
        self.data = data                # type: RecognizePublicFaceResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = RecognizePublicFaceResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class RecognizePublicFaceResponseDataElementsResultsSubResultsFaces(TeaModel):
    def __init__(self, id=None, name=None, rate=None):
        self.id = id                    # type: str
        self.name = name                # type: str
        self.rate = rate                # type: float

    def validate(self):
        self.validate_required(self.id, 'id')
        self.validate_required(self.name, 'name')
        self.validate_required(self.rate, 'rate')

    def to_map(self):
        result = {}
        result['Id'] = self.id
        result['Name'] = self.name
        result['Rate'] = self.rate
        return result

    def from_map(self, map={}):
        self.id = map.get('Id')
        self.name = map.get('Name')
        self.rate = map.get('Rate')
        return self


class RecognizePublicFaceResponseDataElementsResultsSubResults(TeaModel):
    def __init__(self, h=None, w=None, x=None, y=None, faces=None):
        self.h = h                      # type: float
        self.w = w                      # type: float
        self.x = x                      # type: float
        self.y = y                      # type: float
        self.faces = faces              # type: List[RecognizePublicFaceResponseDataElementsResultsSubResultsFaces]

    def validate(self):
        self.validate_required(self.h, 'h')
        self.validate_required(self.w, 'w')
        self.validate_required(self.x, 'x')
        self.validate_required(self.y, 'y')
        self.validate_required(self.faces, 'faces')
        if self.faces:
            for k in self.faces:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['H'] = self.h
        result['W'] = self.w
        result['X'] = self.x
        result['Y'] = self.y
        result['Faces'] = []
        if self.faces is not None:
            for k in self.faces:
                result['Faces'].append(k.to_map() if k else None)
        else:
            result['Faces'] = None
        return result

    def from_map(self, map={}):
        self.h = map.get('H')
        self.w = map.get('W')
        self.x = map.get('X')
        self.y = map.get('Y')
        self.faces = []
        if map.get('Faces') is not None:
            for k in map.get('Faces'):
                temp_model = RecognizePublicFaceResponseDataElementsResultsSubResultsFaces()
                self.faces.append(temp_model.from_map(k))
        else:
            self.faces = None
        return self


class RecognizePublicFaceResponseDataElementsResults(TeaModel):
    def __init__(self, label=None, suggestion=None, rate=None, sub_results=None):
        self.label = label              # type: str
        self.suggestion = suggestion    # type: str
        self.rate = rate                # type: float
        self.sub_results = sub_results  # type: List[RecognizePublicFaceResponseDataElementsResultsSubResults]

    def validate(self):
        self.validate_required(self.label, 'label')
        self.validate_required(self.suggestion, 'suggestion')
        self.validate_required(self.rate, 'rate')
        self.validate_required(self.sub_results, 'sub_results')
        if self.sub_results:
            for k in self.sub_results:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Label'] = self.label
        result['Suggestion'] = self.suggestion
        result['Rate'] = self.rate
        result['SubResults'] = []
        if self.sub_results is not None:
            for k in self.sub_results:
                result['SubResults'].append(k.to_map() if k else None)
        else:
            result['SubResults'] = None
        return result

    def from_map(self, map={}):
        self.label = map.get('Label')
        self.suggestion = map.get('Suggestion')
        self.rate = map.get('Rate')
        self.sub_results = []
        if map.get('SubResults') is not None:
            for k in map.get('SubResults'):
                temp_model = RecognizePublicFaceResponseDataElementsResultsSubResults()
                self.sub_results.append(temp_model.from_map(k))
        else:
            self.sub_results = None
        return self


class RecognizePublicFaceResponseDataElements(TeaModel):
    def __init__(self, task_id=None, image_url=None, results=None):
        self.task_id = task_id          # type: str
        self.image_url = image_url      # type: str
        self.results = results          # type: List[RecognizePublicFaceResponseDataElementsResults]

    def validate(self):
        self.validate_required(self.task_id, 'task_id')
        self.validate_required(self.image_url, 'image_url')
        self.validate_required(self.results, 'results')
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['TaskId'] = self.task_id
        result['ImageURL'] = self.image_url
        result['Results'] = []
        if self.results is not None:
            for k in self.results:
                result['Results'].append(k.to_map() if k else None)
        else:
            result['Results'] = None
        return result

    def from_map(self, map={}):
        self.task_id = map.get('TaskId')
        self.image_url = map.get('ImageURL')
        self.results = []
        if map.get('Results') is not None:
            for k in map.get('Results'):
                temp_model = RecognizePublicFaceResponseDataElementsResults()
                self.results.append(temp_model.from_map(k))
        else:
            self.results = None
        return self


class RecognizePublicFaceResponseData(TeaModel):
    def __init__(self, elements=None):
        self.elements = elements        # type: List[RecognizePublicFaceResponseDataElements]

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
        else:
            result['Elements'] = None
        return result

    def from_map(self, map={}):
        self.elements = []
        if map.get('Elements') is not None:
            for k in map.get('Elements'):
                temp_model = RecognizePublicFaceResponseDataElements()
                self.elements.append(temp_model.from_map(k))
        else:
            self.elements = None
        return self


class DetectLivingFaceRequest(TeaModel):
    def __init__(self, tasks=None):
        self.tasks = tasks              # type: List[DetectLivingFaceRequestTasks]

    def validate(self):
        self.validate_required(self.tasks, 'tasks')
        if self.tasks:
            for k in self.tasks:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Tasks'] = []
        if self.tasks is not None:
            for k in self.tasks:
                result['Tasks'].append(k.to_map() if k else None)
        else:
            result['Tasks'] = None
        return result

    def from_map(self, map={}):
        self.tasks = []
        if map.get('Tasks') is not None:
            for k in map.get('Tasks'):
                temp_model = DetectLivingFaceRequestTasks()
                self.tasks.append(temp_model.from_map(k))
        else:
            self.tasks = None
        return self


class DetectLivingFaceRequestTasks(TeaModel):
    def __init__(self, image_url=None):
        self.image_url = image_url      # type: str

    def validate(self):
        self.validate_required(self.image_url, 'image_url')

    def to_map(self):
        result = {}
        result['ImageURL'] = self.image_url
        return result

    def from_map(self, map={}):
        self.image_url = map.get('ImageURL')
        return self


class DetectLivingFaceResponse(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id    # type: str
        self.data = data                # type: DetectLivingFaceResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = DetectLivingFaceResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class DetectLivingFaceResponseDataElementsResultsFrames(TeaModel):
    def __init__(self, rate=None, url=None):
        self.rate = rate                # type: float
        self.url = url                  # type: str

    def validate(self):
        self.validate_required(self.rate, 'rate')
        self.validate_required(self.url, 'url')

    def to_map(self):
        result = {}
        result['Rate'] = self.rate
        result['Url'] = self.url
        return result

    def from_map(self, map={}):
        self.rate = map.get('Rate')
        self.url = map.get('Url')
        return self


class DetectLivingFaceResponseDataElementsResults(TeaModel):
    def __init__(self, label=None, suggestion=None, rate=None, frames=None):
        self.label = label              # type: str
        self.suggestion = suggestion    # type: str
        self.rate = rate                # type: float
        self.frames = frames            # type: List[DetectLivingFaceResponseDataElementsResultsFrames]

    def validate(self):
        self.validate_required(self.label, 'label')
        self.validate_required(self.suggestion, 'suggestion')
        self.validate_required(self.rate, 'rate')
        self.validate_required(self.frames, 'frames')
        if self.frames:
            for k in self.frames:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Label'] = self.label
        result['Suggestion'] = self.suggestion
        result['Rate'] = self.rate
        result['Frames'] = []
        if self.frames is not None:
            for k in self.frames:
                result['Frames'].append(k.to_map() if k else None)
        else:
            result['Frames'] = None
        return result

    def from_map(self, map={}):
        self.label = map.get('Label')
        self.suggestion = map.get('Suggestion')
        self.rate = map.get('Rate')
        self.frames = []
        if map.get('Frames') is not None:
            for k in map.get('Frames'):
                temp_model = DetectLivingFaceResponseDataElementsResultsFrames()
                self.frames.append(temp_model.from_map(k))
        else:
            self.frames = None
        return self


class DetectLivingFaceResponseDataElements(TeaModel):
    def __init__(self, task_id=None, image_url=None, results=None):
        self.task_id = task_id          # type: str
        self.image_url = image_url      # type: str
        self.results = results          # type: List[DetectLivingFaceResponseDataElementsResults]

    def validate(self):
        self.validate_required(self.task_id, 'task_id')
        self.validate_required(self.image_url, 'image_url')
        self.validate_required(self.results, 'results')
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['TaskId'] = self.task_id
        result['ImageURL'] = self.image_url
        result['Results'] = []
        if self.results is not None:
            for k in self.results:
                result['Results'].append(k.to_map() if k else None)
        else:
            result['Results'] = None
        return result

    def from_map(self, map={}):
        self.task_id = map.get('TaskId')
        self.image_url = map.get('ImageURL')
        self.results = []
        if map.get('Results') is not None:
            for k in map.get('Results'):
                temp_model = DetectLivingFaceResponseDataElementsResults()
                self.results.append(temp_model.from_map(k))
        else:
            self.results = None
        return self


class DetectLivingFaceResponseData(TeaModel):
    def __init__(self, elements=None):
        self.elements = elements        # type: List[DetectLivingFaceResponseDataElements]

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
        else:
            result['Elements'] = None
        return result

    def from_map(self, map={}):
        self.elements = []
        if map.get('Elements') is not None:
            for k in map.get('Elements'):
                temp_model = DetectLivingFaceResponseDataElements()
                self.elements.append(temp_model.from_map(k))
        else:
            self.elements = None
        return self


class DetectBodyCountRequest(TeaModel):
    def __init__(self, image_url=None):
        self.image_url = image_url      # type: str

    def validate(self):
        self.validate_required(self.image_url, 'image_url')

    def to_map(self):
        result = {}
        result['ImageURL'] = self.image_url
        return result

    def from_map(self, map={}):
        self.image_url = map.get('ImageURL')
        return self


class DetectBodyCountResponse(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id    # type: str
        self.data = data                # type: DetectBodyCountResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = DetectBodyCountResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class DetectBodyCountResponseData(TeaModel):
    def __init__(self, person_number=None):
        self.person_number = person_number  # type: int

    def validate(self):
        self.validate_required(self.person_number, 'person_number')

    def to_map(self):
        result = {}
        result['PersonNumber'] = self.person_number
        return result

    def from_map(self, map={}):
        self.person_number = map.get('PersonNumber')
        return self


class DetectBodyCountAdvanceRequest(TeaModel):
    def __init__(self, image_urlobject=None):
        self.image_urlobject = image_urlobject  # type: BinaryIO

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        result = {}
        result['ImageURLObject'] = self.image_urlobject
        return result

    def from_map(self, map={}):
        self.image_urlobject = map.get('ImageURLObject')
        return self


class DetectMaskRequest(TeaModel):
    def __init__(self, image_url=None):
        self.image_url = image_url      # type: str

    def validate(self):
        self.validate_required(self.image_url, 'image_url')

    def to_map(self):
        result = {}
        result['ImageURL'] = self.image_url
        return result

    def from_map(self, map={}):
        self.image_url = map.get('ImageURL')
        return self


class DetectMaskResponse(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id    # type: str
        self.data = data                # type: DetectMaskResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = DetectMaskResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class DetectMaskResponseData(TeaModel):
    def __init__(self, mask=None, face_probability=None):
        self.mask = mask                # type: int
        self.face_probability = face_probability  # type: float

    def validate(self):
        self.validate_required(self.mask, 'mask')
        self.validate_required(self.face_probability, 'face_probability')

    def to_map(self):
        result = {}
        result['Mask'] = self.mask
        result['FaceProbability'] = self.face_probability
        return result

    def from_map(self, map={}):
        self.mask = map.get('Mask')
        self.face_probability = map.get('FaceProbability')
        return self


class DetectMaskAdvanceRequest(TeaModel):
    def __init__(self, image_urlobject=None):
        self.image_urlobject = image_urlobject  # type: BinaryIO

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        result = {}
        result['ImageURLObject'] = self.image_urlobject
        return result

    def from_map(self, map={}):
        self.image_urlobject = map.get('ImageURLObject')
        return self


class RecognizeFaceRequest(TeaModel):
    def __init__(self, image_url=None):
        self.image_url = image_url      # type: str

    def validate(self):
        self.validate_required(self.image_url, 'image_url')

    def to_map(self):
        result = {}
        result['ImageURL'] = self.image_url
        return result

    def from_map(self, map={}):
        self.image_url = map.get('ImageURL')
        return self


class RecognizeFaceResponse(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id    # type: str
        self.data = data                # type: RecognizeFaceResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = RecognizeFaceResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class RecognizeFaceResponseData(TeaModel):
    def __init__(self, face_count=None, landmark_count=None, dense_feature_length=None, face_rectangles=None,
                 face_probability_list=None, pose_list=None, landmarks=None, pupils=None, gender_list=None, age_list=None,
                 expressions=None, glasses=None, dense_features=None):
        self.face_count = face_count    # type: int
        self.landmark_count = landmark_count  # type: int
        self.dense_feature_length = dense_feature_length  # type: int
        self.face_rectangles = face_rectangles  # type: List[int]
        self.face_probability_list = face_probability_list  # type: List[float]
        self.pose_list = pose_list      # type: List[float]
        self.landmarks = landmarks      # type: List[float]
        self.pupils = pupils            # type: List[float]
        self.gender_list = gender_list  # type: List[int]
        self.age_list = age_list        # type: List[int]
        self.expressions = expressions  # type: List[int]
        self.glasses = glasses          # type: List[int]
        self.dense_features = dense_features  # type: List[str]

    def validate(self):
        self.validate_required(self.face_count, 'face_count')
        self.validate_required(self.landmark_count, 'landmark_count')
        self.validate_required(self.dense_feature_length, 'dense_feature_length')
        self.validate_required(self.face_rectangles, 'face_rectangles')
        self.validate_required(self.face_probability_list, 'face_probability_list')
        self.validate_required(self.pose_list, 'pose_list')
        self.validate_required(self.landmarks, 'landmarks')
        self.validate_required(self.pupils, 'pupils')
        self.validate_required(self.gender_list, 'gender_list')
        self.validate_required(self.age_list, 'age_list')
        self.validate_required(self.expressions, 'expressions')
        self.validate_required(self.glasses, 'glasses')
        self.validate_required(self.dense_features, 'dense_features')

    def to_map(self):
        result = {}
        result['FaceCount'] = self.face_count
        result['LandmarkCount'] = self.landmark_count
        result['DenseFeatureLength'] = self.dense_feature_length
        result['FaceRectangles'] = self.face_rectangles
        result['FaceProbabilityList'] = self.face_probability_list
        result['PoseList'] = self.pose_list
        result['Landmarks'] = self.landmarks
        result['Pupils'] = self.pupils
        result['GenderList'] = self.gender_list
        result['AgeList'] = self.age_list
        result['Expressions'] = self.expressions
        result['Glasses'] = self.glasses
        result['DenseFeatures'] = self.dense_features
        return result

    def from_map(self, map={}):
        self.face_count = map.get('FaceCount')
        self.landmark_count = map.get('LandmarkCount')
        self.dense_feature_length = map.get('DenseFeatureLength')
        self.face_rectangles = map.get('FaceRectangles')
        self.face_probability_list = map.get('FaceProbabilityList')
        self.pose_list = map.get('PoseList')
        self.landmarks = map.get('Landmarks')
        self.pupils = map.get('Pupils')
        self.gender_list = map.get('GenderList')
        self.age_list = map.get('AgeList')
        self.expressions = map.get('Expressions')
        self.glasses = map.get('Glasses')
        self.dense_features = map.get('DenseFeatures')
        return self


class RecognizeFaceAdvanceRequest(TeaModel):
    def __init__(self, image_urlobject=None):
        self.image_urlobject = image_urlobject  # type: BinaryIO

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        result = {}
        result['ImageURLObject'] = self.image_urlobject
        return result

    def from_map(self, map={}):
        self.image_urlobject = map.get('ImageURLObject')
        return self


class CompareFaceRequest(TeaModel):
    def __init__(self, image_urla=None, image_urlb=None):
        self.image_urla = image_urla    # type: str
        self.image_urlb = image_urlb    # type: str

    def validate(self):
        self.validate_required(self.image_urla, 'image_urla')
        self.validate_required(self.image_urlb, 'image_urlb')

    def to_map(self):
        result = {}
        result['ImageURLA'] = self.image_urla
        result['ImageURLB'] = self.image_urlb
        return result

    def from_map(self, map={}):
        self.image_urla = map.get('ImageURLA')
        self.image_urlb = map.get('ImageURLB')
        return self


class CompareFaceResponse(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id    # type: str
        self.data = data                # type: CompareFaceResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = CompareFaceResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class CompareFaceResponseData(TeaModel):
    def __init__(self, confidence=None, thresholds=None, rect_alist=None, rect_blist=None):
        self.confidence = confidence    # type: float
        self.thresholds = thresholds    # type: List[float]
        self.rect_alist = rect_alist    # type: List[int]
        self.rect_blist = rect_blist    # type: List[int]

    def validate(self):
        self.validate_required(self.confidence, 'confidence')
        self.validate_required(self.thresholds, 'thresholds')
        self.validate_required(self.rect_alist, 'rect_alist')
        self.validate_required(self.rect_blist, 'rect_blist')

    def to_map(self):
        result = {}
        result['Confidence'] = self.confidence
        result['Thresholds'] = self.thresholds
        result['RectAList'] = self.rect_alist
        result['RectBList'] = self.rect_blist
        return result

    def from_map(self, map={}):
        self.confidence = map.get('Confidence')
        self.thresholds = map.get('Thresholds')
        self.rect_alist = map.get('RectAList')
        self.rect_blist = map.get('RectBList')
        return self


class DetectFaceRequest(TeaModel):
    def __init__(self, image_url=None):
        self.image_url = image_url      # type: str

    def validate(self):
        self.validate_required(self.image_url, 'image_url')

    def to_map(self):
        result = {}
        result['ImageURL'] = self.image_url
        return result

    def from_map(self, map={}):
        self.image_url = map.get('ImageURL')
        return self


class DetectFaceResponse(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id    # type: str
        self.data = data                # type: DetectFaceResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = DetectFaceResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class DetectFaceResponseData(TeaModel):
    def __init__(self, face_count=None, landmark_count=None, face_rectangles=None, face_probability_list=None,
                 pose_list=None, landmarks=None, pupils=None):
        self.face_count = face_count    # type: int
        self.landmark_count = landmark_count  # type: int
        self.face_rectangles = face_rectangles  # type: List[int]
        self.face_probability_list = face_probability_list  # type: List[float]
        self.pose_list = pose_list      # type: List[float]
        self.landmarks = landmarks      # type: List[float]
        self.pupils = pupils            # type: List[float]

    def validate(self):
        self.validate_required(self.face_count, 'face_count')
        self.validate_required(self.landmark_count, 'landmark_count')
        self.validate_required(self.face_rectangles, 'face_rectangles')
        self.validate_required(self.face_probability_list, 'face_probability_list')
        self.validate_required(self.pose_list, 'pose_list')
        self.validate_required(self.landmarks, 'landmarks')
        self.validate_required(self.pupils, 'pupils')

    def to_map(self):
        result = {}
        result['FaceCount'] = self.face_count
        result['LandmarkCount'] = self.landmark_count
        result['FaceRectangles'] = self.face_rectangles
        result['FaceProbabilityList'] = self.face_probability_list
        result['PoseList'] = self.pose_list
        result['Landmarks'] = self.landmarks
        result['Pupils'] = self.pupils
        return result

    def from_map(self, map={}):
        self.face_count = map.get('FaceCount')
        self.landmark_count = map.get('LandmarkCount')
        self.face_rectangles = map.get('FaceRectangles')
        self.face_probability_list = map.get('FaceProbabilityList')
        self.pose_list = map.get('PoseList')
        self.landmarks = map.get('Landmarks')
        self.pupils = map.get('Pupils')
        return self


class DetectFaceAdvanceRequest(TeaModel):
    def __init__(self, image_urlobject=None):
        self.image_urlobject = image_urlobject  # type: BinaryIO

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        result = {}
        result['ImageURLObject'] = self.image_urlobject
        return result

    def from_map(self, map={}):
        self.image_urlobject = map.get('ImageURLObject')
        return self
