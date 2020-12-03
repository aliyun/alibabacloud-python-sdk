# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
try:
    from typing import Dict, Any, BinaryIO, List
except ImportError:
    pass


class DetectSkinDiseaseRequest(TeaModel):
    def __init__(self, url=None, org_id=None, org_name=None):
        self.url = url                  # type: str
        self.org_id = org_id            # type: str
        self.org_name = org_name        # type: str

    def validate(self):
        self.validate_required(self.url, 'url')
        self.validate_required(self.org_id, 'org_id')
        self.validate_required(self.org_name, 'org_name')

    def to_map(self):
        result = {}
        if self.url is not None:
            result['Url'] = self.url
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.org_name is not None:
            result['OrgName'] = self.org_name
        return result

    def from_map(self, map={}):
        if map.get('Url') is not None:
            self.url = map.get('Url')
        if map.get('OrgId') is not None:
            self.org_id = map.get('OrgId')
        if map.get('OrgName') is not None:
            self.org_name = map.get('OrgName')
        return self


class DetectSkinDiseaseResponse(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id    # type: str
        self.data = data                # type: DetectSkinDiseaseResponseData

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
            temp_model = DetectSkinDiseaseResponseData()
            self.data = temp_model.from_map(map['Data'])
        return self


class DetectSkinDiseaseResponseData(TeaModel):
    def __init__(self, results=None):
        self.results = results          # type: Dict[str, Any]

    def validate(self):
        self.validate_required(self.results, 'results')

    def to_map(self):
        result = {}
        if self.results is not None:
            result['Results'] = self.results
        return result

    def from_map(self, map={}):
        if map.get('Results') is not None:
            self.results = map.get('Results')
        return self


class DetectSkinDiseaseAdvanceRequest(TeaModel):
    def __init__(self, url_object=None, org_id=None, org_name=None):
        self.url_object = url_object    # type: BinaryIO
        self.org_id = org_id            # type: str
        self.org_name = org_name        # type: str

    def validate(self):
        self.validate_required(self.url_object, 'url_object')
        self.validate_required(self.org_id, 'org_id')
        self.validate_required(self.org_name, 'org_name')

    def to_map(self):
        result = {}
        if self.url_object is not None:
            result['UrlObject'] = self.url_object
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.org_name is not None:
            result['OrgName'] = self.org_name
        return result

    def from_map(self, map={}):
        if map.get('UrlObject') is not None:
            self.url_object = map.get('UrlObject')
        if map.get('OrgId') is not None:
            self.org_id = map.get('OrgId')
        if map.get('OrgName') is not None:
            self.org_name = map.get('OrgName')
        return self


class RunMedQARequest(TeaModel):
    def __init__(self, question=None, org_id=None, org_name=None):
        self.question = question        # type: str
        self.org_id = org_id            # type: str
        self.org_name = org_name        # type: str

    def validate(self):
        self.validate_required(self.question, 'question')
        self.validate_required(self.org_id, 'org_id')
        self.validate_required(self.org_name, 'org_name')

    def to_map(self):
        result = {}
        if self.question is not None:
            result['Question'] = self.question
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.org_name is not None:
            result['OrgName'] = self.org_name
        return result

    def from_map(self, map={}):
        if map.get('Question') is not None:
            self.question = map.get('Question')
        if map.get('OrgId') is not None:
            self.org_id = map.get('OrgId')
        if map.get('OrgName') is not None:
            self.org_name = map.get('OrgName')
        return self


class RunMedQAResponse(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id    # type: str
        self.data = data                # type: RunMedQAResponseData

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
            temp_model = RunMedQAResponseData()
            self.data = temp_model.from_map(map['Data'])
        return self


class RunMedQAResponseData(TeaModel):
    def __init__(self, answer=None, similar_question=None):
        self.answer = answer            # type: str
        self.similar_question = similar_question  # type: List[str]

    def validate(self):
        self.validate_required(self.answer, 'answer')
        self.validate_required(self.similar_question, 'similar_question')

    def to_map(self):
        result = {}
        if self.answer is not None:
            result['Answer'] = self.answer
        if self.similar_question is not None:
            result['SimilarQuestion'] = self.similar_question
        return result

    def from_map(self, map={}):
        if map.get('Answer') is not None:
            self.answer = map.get('Answer')
        if map.get('SimilarQuestion') is not None:
            self.similar_question = map.get('SimilarQuestion')
        return self


class DetectKneeKeypointXRayRequest(TeaModel):
    def __init__(self, image_url=None, data_format=None, org_id=None, org_name=None, tracer_id=None):
        self.image_url = image_url      # type: str
        self.data_format = data_format  # type: str
        self.org_id = org_id            # type: str
        self.org_name = org_name        # type: str
        self.tracer_id = tracer_id      # type: str

    def validate(self):
        self.validate_required(self.image_url, 'image_url')
        self.validate_required(self.data_format, 'data_format')
        self.validate_required(self.org_id, 'org_id')
        self.validate_required(self.org_name, 'org_name')

    def to_map(self):
        result = {}
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        if self.data_format is not None:
            result['DataFormat'] = self.data_format
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.org_name is not None:
            result['OrgName'] = self.org_name
        if self.tracer_id is not None:
            result['TracerId'] = self.tracer_id
        return result

    def from_map(self, map={}):
        if map.get('ImageUrl') is not None:
            self.image_url = map.get('ImageUrl')
        if map.get('DataFormat') is not None:
            self.data_format = map.get('DataFormat')
        if map.get('OrgId') is not None:
            self.org_id = map.get('OrgId')
        if map.get('OrgName') is not None:
            self.org_name = map.get('OrgName')
        if map.get('TracerId') is not None:
            self.tracer_id = map.get('TracerId')
        return self


class DetectKneeKeypointXRayResponse(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id    # type: str
        self.data = data                # type: DetectKneeKeypointXRayResponseData

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
            temp_model = DetectKneeKeypointXRayResponseData()
            self.data = temp_model.from_map(map['Data'])
        return self


class DetectKneeKeypointXRayResponseDataKeyPointsTag(TeaModel):
    def __init__(self, direction=None, label=None):
        self.direction = direction      # type: str
        self.label = label              # type: str

    def validate(self):
        self.validate_required(self.direction, 'direction')
        self.validate_required(self.label, 'label')

    def to_map(self):
        result = {}
        if self.direction is not None:
            result['Direction'] = self.direction
        if self.label is not None:
            result['Label'] = self.label
        return result

    def from_map(self, map={}):
        if map.get('Direction') is not None:
            self.direction = map.get('Direction')
        if map.get('Label') is not None:
            self.label = map.get('Label')
        return self


class DetectKneeKeypointXRayResponseDataKeyPoints(TeaModel):
    def __init__(self, value=None, tag=None, coordinates=None):
        self.value = value              # type: float
        self.tag = tag                  # type: DetectKneeKeypointXRayResponseDataKeyPointsTag
        self.coordinates = coordinates  # type: List[int]

    def validate(self):
        self.validate_required(self.value, 'value')
        self.validate_required(self.tag, 'tag')
        if self.tag:
            self.tag.validate()
        self.validate_required(self.coordinates, 'coordinates')

    def to_map(self):
        result = {}
        if self.value is not None:
            result['Value'] = self.value
        if self.tag is not None:
            result['Tag'] = self.tag.to_map()
        if self.coordinates is not None:
            result['Coordinates'] = self.coordinates
        return result

    def from_map(self, map={}):
        if map.get('Value') is not None:
            self.value = map.get('Value')
        if map.get('Tag') is not None:
            temp_model = DetectKneeKeypointXRayResponseDataKeyPointsTag()
            self.tag = temp_model.from_map(map['Tag'])
        if map.get('Coordinates') is not None:
            self.coordinates = map.get('Coordinates')
        return self


class DetectKneeKeypointXRayResponseData(TeaModel):
    def __init__(self, image_url=None, org_id=None, org_name=None, key_points=None):
        self.image_url = image_url      # type: str
        self.org_id = org_id            # type: str
        self.org_name = org_name        # type: str
        self.key_points = key_points    # type: List[DetectKneeKeypointXRayResponseDataKeyPoints]

    def validate(self):
        self.validate_required(self.image_url, 'image_url')
        self.validate_required(self.org_id, 'org_id')
        self.validate_required(self.org_name, 'org_name')
        self.validate_required(self.key_points, 'key_points')
        if self.key_points:
            for k in self.key_points:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.org_name is not None:
            result['OrgName'] = self.org_name
        result['KeyPoints'] = []
        if self.key_points is not None:
            for k in self.key_points:
                result['KeyPoints'].append(k.to_map() if k else None)
        return result

    def from_map(self, map={}):
        if map.get('ImageUrl') is not None:
            self.image_url = map.get('ImageUrl')
        if map.get('OrgId') is not None:
            self.org_id = map.get('OrgId')
        if map.get('OrgName') is not None:
            self.org_name = map.get('OrgName')
        self.key_points = []
        if map.get('KeyPoints') is not None:
            for k in map.get('KeyPoints'):
                temp_model = DetectKneeKeypointXRayResponseDataKeyPoints()
                self.key_points.append(temp_model.from_map(k))
        return self


class DetectKneeKeypointXRayAdvanceRequest(TeaModel):
    def __init__(self, image_url_object=None, data_format=None, org_id=None, org_name=None, tracer_id=None):
        self.image_url_object = image_url_object  # type: BinaryIO
        self.data_format = data_format  # type: str
        self.org_id = org_id            # type: str
        self.org_name = org_name        # type: str
        self.tracer_id = tracer_id      # type: str

    def validate(self):
        self.validate_required(self.image_url_object, 'image_url_object')
        self.validate_required(self.data_format, 'data_format')
        self.validate_required(self.org_id, 'org_id')
        self.validate_required(self.org_name, 'org_name')

    def to_map(self):
        result = {}
        if self.image_url_object is not None:
            result['ImageUrlObject'] = self.image_url_object
        if self.data_format is not None:
            result['DataFormat'] = self.data_format
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.org_name is not None:
            result['OrgName'] = self.org_name
        if self.tracer_id is not None:
            result['TracerId'] = self.tracer_id
        return result

    def from_map(self, map={}):
        if map.get('ImageUrlObject') is not None:
            self.image_url_object = map.get('ImageUrlObject')
        if map.get('DataFormat') is not None:
            self.data_format = map.get('DataFormat')
        if map.get('OrgId') is not None:
            self.org_id = map.get('OrgId')
        if map.get('OrgName') is not None:
            self.org_name = map.get('OrgName')
        if map.get('TracerId') is not None:
            self.tracer_id = map.get('TracerId')
        return self


class ClassifyFNFRequest(TeaModel):
    def __init__(self, image_url=None, data_format=None, org_id=None, org_name=None, tracer_id=None):
        self.image_url = image_url      # type: str
        self.data_format = data_format  # type: str
        self.org_id = org_id            # type: str
        self.org_name = org_name        # type: str
        self.tracer_id = tracer_id      # type: str

    def validate(self):
        self.validate_required(self.image_url, 'image_url')
        self.validate_required(self.data_format, 'data_format')
        self.validate_required(self.org_id, 'org_id')
        self.validate_required(self.org_name, 'org_name')

    def to_map(self):
        result = {}
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        if self.data_format is not None:
            result['DataFormat'] = self.data_format
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.org_name is not None:
            result['OrgName'] = self.org_name
        if self.tracer_id is not None:
            result['TracerId'] = self.tracer_id
        return result

    def from_map(self, map={}):
        if map.get('ImageUrl') is not None:
            self.image_url = map.get('ImageUrl')
        if map.get('DataFormat') is not None:
            self.data_format = map.get('DataFormat')
        if map.get('OrgId') is not None:
            self.org_id = map.get('OrgId')
        if map.get('OrgName') is not None:
            self.org_name = map.get('OrgName')
        if map.get('TracerId') is not None:
            self.tracer_id = map.get('TracerId')
        return self


class ClassifyFNFResponse(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id    # type: str
        self.data = data                # type: ClassifyFNFResponseData

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
            temp_model = ClassifyFNFResponseData()
            self.data = temp_model.from_map(map['Data'])
        return self


class ClassifyFNFResponseDataFracturesTag(TeaModel):
    def __init__(self, label=None):
        self.label = label              # type: str

    def validate(self):
        self.validate_required(self.label, 'label')

    def to_map(self):
        result = {}
        if self.label is not None:
            result['Label'] = self.label
        return result

    def from_map(self, map={}):
        if map.get('Label') is not None:
            self.label = map.get('Label')
        return self


class ClassifyFNFResponseDataFractures(TeaModel):
    def __init__(self, value=None, tag=None, boxes=None):
        self.value = value              # type: float
        self.tag = tag                  # type: ClassifyFNFResponseDataFracturesTag
        self.boxes = boxes              # type: List[int]

    def validate(self):
        self.validate_required(self.value, 'value')
        self.validate_required(self.tag, 'tag')
        if self.tag:
            self.tag.validate()
        self.validate_required(self.boxes, 'boxes')

    def to_map(self):
        result = {}
        if self.value is not None:
            result['Value'] = self.value
        if self.tag is not None:
            result['Tag'] = self.tag.to_map()
        if self.boxes is not None:
            result['Boxes'] = self.boxes
        return result

    def from_map(self, map={}):
        if map.get('Value') is not None:
            self.value = map.get('Value')
        if map.get('Tag') is not None:
            temp_model = ClassifyFNFResponseDataFracturesTag()
            self.tag = temp_model.from_map(map['Tag'])
        if map.get('Boxes') is not None:
            self.boxes = map.get('Boxes')
        return self


class ClassifyFNFResponseData(TeaModel):
    def __init__(self, image_url=None, org_id=None, org_name=None, fractures=None):
        self.image_url = image_url      # type: str
        self.org_id = org_id            # type: str
        self.org_name = org_name        # type: str
        self.fractures = fractures      # type: List[ClassifyFNFResponseDataFractures]

    def validate(self):
        self.validate_required(self.image_url, 'image_url')
        self.validate_required(self.org_id, 'org_id')
        self.validate_required(self.org_name, 'org_name')
        self.validate_required(self.fractures, 'fractures')
        if self.fractures:
            for k in self.fractures:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.org_name is not None:
            result['OrgName'] = self.org_name
        result['Fractures'] = []
        if self.fractures is not None:
            for k in self.fractures:
                result['Fractures'].append(k.to_map() if k else None)
        return result

    def from_map(self, map={}):
        if map.get('ImageUrl') is not None:
            self.image_url = map.get('ImageUrl')
        if map.get('OrgId') is not None:
            self.org_id = map.get('OrgId')
        if map.get('OrgName') is not None:
            self.org_name = map.get('OrgName')
        self.fractures = []
        if map.get('Fractures') is not None:
            for k in map.get('Fractures'):
                temp_model = ClassifyFNFResponseDataFractures()
                self.fractures.append(temp_model.from_map(k))
        return self


class ClassifyFNFAdvanceRequest(TeaModel):
    def __init__(self, image_url_object=None, data_format=None, org_id=None, org_name=None, tracer_id=None):
        self.image_url_object = image_url_object  # type: BinaryIO
        self.data_format = data_format  # type: str
        self.org_id = org_id            # type: str
        self.org_name = org_name        # type: str
        self.tracer_id = tracer_id      # type: str

    def validate(self):
        self.validate_required(self.image_url_object, 'image_url_object')
        self.validate_required(self.data_format, 'data_format')
        self.validate_required(self.org_id, 'org_id')
        self.validate_required(self.org_name, 'org_name')

    def to_map(self):
        result = {}
        if self.image_url_object is not None:
            result['ImageUrlObject'] = self.image_url_object
        if self.data_format is not None:
            result['DataFormat'] = self.data_format
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.org_name is not None:
            result['OrgName'] = self.org_name
        if self.tracer_id is not None:
            result['TracerId'] = self.tracer_id
        return result

    def from_map(self, map={}):
        if map.get('ImageUrlObject') is not None:
            self.image_url_object = map.get('ImageUrlObject')
        if map.get('DataFormat') is not None:
            self.data_format = map.get('DataFormat')
        if map.get('OrgId') is not None:
            self.org_id = map.get('OrgId')
        if map.get('OrgName') is not None:
            self.org_name = map.get('OrgName')
        if map.get('TracerId') is not None:
            self.tracer_id = map.get('TracerId')
        return self


class RunCTRegistrationRequest(TeaModel):
    def __init__(self, reference_list=None, data_format=None, org_name=None, org_id=None, data_source_type=None,
                 floating_list=None):
        self.reference_list = reference_list  # type: List[RunCTRegistrationRequestReferenceList]
        self.data_format = data_format  # type: str
        self.org_name = org_name        # type: str
        self.org_id = org_id            # type: str
        self.data_source_type = data_source_type  # type: str
        self.floating_list = floating_list  # type: List[RunCTRegistrationRequestFloatingList]

    def validate(self):
        self.validate_required(self.reference_list, 'reference_list')
        if self.reference_list:
            for k in self.reference_list:
                if k:
                    k.validate()
        self.validate_required(self.data_format, 'data_format')
        self.validate_required(self.org_name, 'org_name')
        self.validate_required(self.org_id, 'org_id')
        self.validate_required(self.data_source_type, 'data_source_type')
        self.validate_required(self.floating_list, 'floating_list')
        if self.floating_list:
            for k in self.floating_list:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['ReferenceList'] = []
        if self.reference_list is not None:
            for k in self.reference_list:
                result['ReferenceList'].append(k.to_map() if k else None)
        if self.data_format is not None:
            result['DataFormat'] = self.data_format
        if self.org_name is not None:
            result['OrgName'] = self.org_name
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.data_source_type is not None:
            result['DataSourceType'] = self.data_source_type
        result['FloatingList'] = []
        if self.floating_list is not None:
            for k in self.floating_list:
                result['FloatingList'].append(k.to_map() if k else None)
        return result

    def from_map(self, map={}):
        self.reference_list = []
        if map.get('ReferenceList') is not None:
            for k in map.get('ReferenceList'):
                temp_model = RunCTRegistrationRequestReferenceList()
                self.reference_list.append(temp_model.from_map(k))
        if map.get('DataFormat') is not None:
            self.data_format = map.get('DataFormat')
        if map.get('OrgName') is not None:
            self.org_name = map.get('OrgName')
        if map.get('OrgId') is not None:
            self.org_id = map.get('OrgId')
        if map.get('DataSourceType') is not None:
            self.data_source_type = map.get('DataSourceType')
        self.floating_list = []
        if map.get('FloatingList') is not None:
            for k in map.get('FloatingList'):
                temp_model = RunCTRegistrationRequestFloatingList()
                self.floating_list.append(temp_model.from_map(k))
        return self


class RunCTRegistrationRequestReferenceList(TeaModel):
    def __init__(self, reference_url=None):
        self.reference_url = reference_url  # type: str

    def validate(self):
        self.validate_required(self.reference_url, 'reference_url')

    def to_map(self):
        result = {}
        if self.reference_url is not None:
            result['ReferenceURL'] = self.reference_url
        return result

    def from_map(self, map={}):
        if map.get('ReferenceURL') is not None:
            self.reference_url = map.get('ReferenceURL')
        return self


class RunCTRegistrationRequestFloatingList(TeaModel):
    def __init__(self, floating_url=None):
        self.floating_url = floating_url  # type: str

    def validate(self):
        self.validate_required(self.floating_url, 'floating_url')

    def to_map(self):
        result = {}
        if self.floating_url is not None:
            result['FloatingURL'] = self.floating_url
        return result

    def from_map(self, map={}):
        if map.get('FloatingURL') is not None:
            self.floating_url = map.get('FloatingURL')
        return self


class RunCTRegistrationResponse(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id    # type: str
        self.data = data                # type: RunCTRegistrationResponseData

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
            temp_model = RunCTRegistrationResponseData()
            self.data = temp_model.from_map(map['Data'])
        return self


class RunCTRegistrationResponseData(TeaModel):
    def __init__(self, durl=None, nurl=None):
        self.durl = durl                # type: str
        self.nurl = nurl                # type: str

    def validate(self):
        self.validate_required(self.durl, 'durl')
        self.validate_required(self.nurl, 'nurl')

    def to_map(self):
        result = {}
        if self.durl is not None:
            result['DUrl'] = self.durl
        if self.nurl is not None:
            result['NUrl'] = self.nurl
        return result

    def from_map(self, map={}):
        if map.get('DUrl') is not None:
            self.durl = map.get('DUrl')
        if map.get('NUrl') is not None:
            self.nurl = map.get('NUrl')
        return self


class DetectHipKeypointXRayRequest(TeaModel):
    def __init__(self, image_url=None, data_format=None, org_id=None, org_name=None, tracer_id=None):
        self.image_url = image_url      # type: str
        self.data_format = data_format  # type: str
        self.org_id = org_id            # type: str
        self.org_name = org_name        # type: str
        self.tracer_id = tracer_id      # type: str

    def validate(self):
        self.validate_required(self.image_url, 'image_url')
        self.validate_required(self.data_format, 'data_format')
        self.validate_required(self.org_id, 'org_id')
        self.validate_required(self.org_name, 'org_name')

    def to_map(self):
        result = {}
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        if self.data_format is not None:
            result['DataFormat'] = self.data_format
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.org_name is not None:
            result['OrgName'] = self.org_name
        if self.tracer_id is not None:
            result['TracerId'] = self.tracer_id
        return result

    def from_map(self, map={}):
        if map.get('ImageUrl') is not None:
            self.image_url = map.get('ImageUrl')
        if map.get('DataFormat') is not None:
            self.data_format = map.get('DataFormat')
        if map.get('OrgId') is not None:
            self.org_id = map.get('OrgId')
        if map.get('OrgName') is not None:
            self.org_name = map.get('OrgName')
        if map.get('TracerId') is not None:
            self.tracer_id = map.get('TracerId')
        return self


class DetectHipKeypointXRayResponse(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id    # type: str
        self.data = data                # type: DetectHipKeypointXRayResponseData

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
            temp_model = DetectHipKeypointXRayResponseData()
            self.data = temp_model.from_map(map['Data'])
        return self


class DetectHipKeypointXRayResponseDataKeyPointsTag(TeaModel):
    def __init__(self, direction=None, label=None):
        self.direction = direction      # type: str
        self.label = label              # type: str

    def validate(self):
        self.validate_required(self.direction, 'direction')
        self.validate_required(self.label, 'label')

    def to_map(self):
        result = {}
        if self.direction is not None:
            result['Direction'] = self.direction
        if self.label is not None:
            result['Label'] = self.label
        return result

    def from_map(self, map={}):
        if map.get('Direction') is not None:
            self.direction = map.get('Direction')
        if map.get('Label') is not None:
            self.label = map.get('Label')
        return self


class DetectHipKeypointXRayResponseDataKeyPoints(TeaModel):
    def __init__(self, value=None, tag=None, coordinates=None):
        self.value = value              # type: float
        self.tag = tag                  # type: DetectHipKeypointXRayResponseDataKeyPointsTag
        self.coordinates = coordinates  # type: List[int]

    def validate(self):
        self.validate_required(self.value, 'value')
        self.validate_required(self.tag, 'tag')
        if self.tag:
            self.tag.validate()
        self.validate_required(self.coordinates, 'coordinates')

    def to_map(self):
        result = {}
        if self.value is not None:
            result['Value'] = self.value
        if self.tag is not None:
            result['Tag'] = self.tag.to_map()
        if self.coordinates is not None:
            result['Coordinates'] = self.coordinates
        return result

    def from_map(self, map={}):
        if map.get('Value') is not None:
            self.value = map.get('Value')
        if map.get('Tag') is not None:
            temp_model = DetectHipKeypointXRayResponseDataKeyPointsTag()
            self.tag = temp_model.from_map(map['Tag'])
        if map.get('Coordinates') is not None:
            self.coordinates = map.get('Coordinates')
        return self


class DetectHipKeypointXRayResponseData(TeaModel):
    def __init__(self, image_url=None, org_id=None, org_name=None, key_points=None):
        self.image_url = image_url      # type: str
        self.org_id = org_id            # type: str
        self.org_name = org_name        # type: str
        self.key_points = key_points    # type: List[DetectHipKeypointXRayResponseDataKeyPoints]

    def validate(self):
        self.validate_required(self.image_url, 'image_url')
        self.validate_required(self.org_id, 'org_id')
        self.validate_required(self.org_name, 'org_name')
        self.validate_required(self.key_points, 'key_points')
        if self.key_points:
            for k in self.key_points:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.org_name is not None:
            result['OrgName'] = self.org_name
        result['KeyPoints'] = []
        if self.key_points is not None:
            for k in self.key_points:
                result['KeyPoints'].append(k.to_map() if k else None)
        return result

    def from_map(self, map={}):
        if map.get('ImageUrl') is not None:
            self.image_url = map.get('ImageUrl')
        if map.get('OrgId') is not None:
            self.org_id = map.get('OrgId')
        if map.get('OrgName') is not None:
            self.org_name = map.get('OrgName')
        self.key_points = []
        if map.get('KeyPoints') is not None:
            for k in map.get('KeyPoints'):
                temp_model = DetectHipKeypointXRayResponseDataKeyPoints()
                self.key_points.append(temp_model.from_map(k))
        return self


class DetectHipKeypointXRayAdvanceRequest(TeaModel):
    def __init__(self, image_url_object=None, data_format=None, org_id=None, org_name=None, tracer_id=None):
        self.image_url_object = image_url_object  # type: BinaryIO
        self.data_format = data_format  # type: str
        self.org_id = org_id            # type: str
        self.org_name = org_name        # type: str
        self.tracer_id = tracer_id      # type: str

    def validate(self):
        self.validate_required(self.image_url_object, 'image_url_object')
        self.validate_required(self.data_format, 'data_format')
        self.validate_required(self.org_id, 'org_id')
        self.validate_required(self.org_name, 'org_name')

    def to_map(self):
        result = {}
        if self.image_url_object is not None:
            result['ImageUrlObject'] = self.image_url_object
        if self.data_format is not None:
            result['DataFormat'] = self.data_format
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.org_name is not None:
            result['OrgName'] = self.org_name
        if self.tracer_id is not None:
            result['TracerId'] = self.tracer_id
        return result

    def from_map(self, map={}):
        if map.get('ImageUrlObject') is not None:
            self.image_url_object = map.get('ImageUrlObject')
        if map.get('DataFormat') is not None:
            self.data_format = map.get('DataFormat')
        if map.get('OrgId') is not None:
            self.org_id = map.get('OrgId')
        if map.get('OrgName') is not None:
            self.org_name = map.get('OrgName')
        if map.get('TracerId') is not None:
            self.tracer_id = map.get('TracerId')
        return self


class CalcCACSRequest(TeaModel):
    def __init__(self, urllist=None, data_format=None, org_name=None, org_id=None, data_source_type=None):
        self.urllist = urllist          # type: List[CalcCACSRequestURLList]
        self.data_format = data_format  # type: str
        self.org_name = org_name        # type: str
        self.org_id = org_id            # type: str
        self.data_source_type = data_source_type  # type: str

    def validate(self):
        self.validate_required(self.urllist, 'urllist')
        if self.urllist:
            for k in self.urllist:
                if k:
                    k.validate()
        self.validate_required(self.data_format, 'data_format')
        self.validate_required(self.org_name, 'org_name')
        self.validate_required(self.org_id, 'org_id')
        self.validate_required(self.data_source_type, 'data_source_type')

    def to_map(self):
        result = {}
        result['URLList'] = []
        if self.urllist is not None:
            for k in self.urllist:
                result['URLList'].append(k.to_map() if k else None)
        if self.data_format is not None:
            result['DataFormat'] = self.data_format
        if self.org_name is not None:
            result['OrgName'] = self.org_name
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.data_source_type is not None:
            result['DataSourceType'] = self.data_source_type
        return result

    def from_map(self, map={}):
        self.urllist = []
        if map.get('URLList') is not None:
            for k in map.get('URLList'):
                temp_model = CalcCACSRequestURLList()
                self.urllist.append(temp_model.from_map(k))
        if map.get('DataFormat') is not None:
            self.data_format = map.get('DataFormat')
        if map.get('OrgName') is not None:
            self.org_name = map.get('OrgName')
        if map.get('OrgId') is not None:
            self.org_id = map.get('OrgId')
        if map.get('DataSourceType') is not None:
            self.data_source_type = map.get('DataSourceType')
        return self


class CalcCACSRequestURLList(TeaModel):
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


class CalcCACSResponse(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id    # type: str
        self.data = data                # type: CalcCACSResponseData

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
            temp_model = CalcCACSResponseData()
            self.data = temp_model.from_map(map['Data'])
        return self


class CalcCACSResponseData(TeaModel):
    def __init__(self, score=None, result_url=None):
        self.score = score              # type: str
        self.result_url = result_url    # type: str

    def validate(self):
        self.validate_required(self.score, 'score')
        self.validate_required(self.result_url, 'result_url')

    def to_map(self):
        result = {}
        if self.score is not None:
            result['Score'] = self.score
        if self.result_url is not None:
            result['ResultUrl'] = self.result_url
        return result

    def from_map(self, map={}):
        if map.get('Score') is not None:
            self.score = map.get('Score')
        if map.get('ResultUrl') is not None:
            self.result_url = map.get('ResultUrl')
        return self


class DetectKneeXRayRequest(TeaModel):
    def __init__(self, url=None, data_format=None, org_name=None, org_id=None):
        self.url = url                  # type: str
        self.data_format = data_format  # type: str
        self.org_name = org_name        # type: str
        self.org_id = org_id            # type: str

    def validate(self):
        self.validate_required(self.url, 'url')
        self.validate_required(self.data_format, 'data_format')
        self.validate_required(self.org_name, 'org_name')
        self.validate_required(self.org_id, 'org_id')

    def to_map(self):
        result = {}
        if self.url is not None:
            result['Url'] = self.url
        if self.data_format is not None:
            result['DataFormat'] = self.data_format
        if self.org_name is not None:
            result['OrgName'] = self.org_name
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        return result

    def from_map(self, map={}):
        if map.get('Url') is not None:
            self.url = map.get('Url')
        if map.get('DataFormat') is not None:
            self.data_format = map.get('DataFormat')
        if map.get('OrgName') is not None:
            self.org_name = map.get('OrgName')
        if map.get('OrgId') is not None:
            self.org_id = map.get('OrgId')
        return self


class DetectKneeXRayResponse(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id    # type: str
        self.data = data                # type: DetectKneeXRayResponseData

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
            temp_model = DetectKneeXRayResponseData()
            self.data = temp_model.from_map(map['Data'])
        return self


class DetectKneeXRayResponseDataKLDetections(TeaModel):
    def __init__(self, detections=None):
        self.detections = detections    # type: List[float]

    def validate(self):
        self.validate_required(self.detections, 'detections')

    def to_map(self):
        result = {}
        if self.detections is not None:
            result['Detections'] = self.detections
        return result

    def from_map(self, map={}):
        if map.get('Detections') is not None:
            self.detections = map.get('Detections')
        return self


class DetectKneeXRayResponseData(TeaModel):
    def __init__(self, kldetections=None):
        self.kldetections = kldetections  # type: List[DetectKneeXRayResponseDataKLDetections]

    def validate(self):
        self.validate_required(self.kldetections, 'kldetections')
        if self.kldetections:
            for k in self.kldetections:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['KLDetections'] = []
        if self.kldetections is not None:
            for k in self.kldetections:
                result['KLDetections'].append(k.to_map() if k else None)
        return result

    def from_map(self, map={}):
        self.kldetections = []
        if map.get('KLDetections') is not None:
            for k in map.get('KLDetections'):
                temp_model = DetectKneeXRayResponseDataKLDetections()
                self.kldetections.append(temp_model.from_map(k))
        return self


class DetectKneeXRayAdvanceRequest(TeaModel):
    def __init__(self, url_object=None, data_format=None, org_name=None, org_id=None):
        self.url_object = url_object    # type: BinaryIO
        self.data_format = data_format  # type: str
        self.org_name = org_name        # type: str
        self.org_id = org_id            # type: str

    def validate(self):
        self.validate_required(self.url_object, 'url_object')
        self.validate_required(self.data_format, 'data_format')
        self.validate_required(self.org_name, 'org_name')
        self.validate_required(self.org_id, 'org_id')

    def to_map(self):
        result = {}
        if self.url_object is not None:
            result['UrlObject'] = self.url_object
        if self.data_format is not None:
            result['DataFormat'] = self.data_format
        if self.org_name is not None:
            result['OrgName'] = self.org_name
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        return result

    def from_map(self, map={}):
        if map.get('UrlObject') is not None:
            self.url_object = map.get('UrlObject')
        if map.get('DataFormat') is not None:
            self.data_format = map.get('DataFormat')
        if map.get('OrgName') is not None:
            self.org_name = map.get('OrgName')
        if map.get('OrgId') is not None:
            self.org_id = map.get('OrgId')
        return self


class DetectSpineMRIRequest(TeaModel):
    def __init__(self, urllist=None, data_format=None, org_name=None, org_id=None):
        self.urllist = urllist          # type: List[DetectSpineMRIRequestURLList]
        self.data_format = data_format  # type: str
        self.org_name = org_name        # type: str
        self.org_id = org_id            # type: str

    def validate(self):
        self.validate_required(self.urllist, 'urllist')
        if self.urllist:
            for k in self.urllist:
                if k:
                    k.validate()
        self.validate_required(self.data_format, 'data_format')
        self.validate_required(self.org_name, 'org_name')
        self.validate_required(self.org_id, 'org_id')

    def to_map(self):
        result = {}
        result['URLList'] = []
        if self.urllist is not None:
            for k in self.urllist:
                result['URLList'].append(k.to_map() if k else None)
        if self.data_format is not None:
            result['DataFormat'] = self.data_format
        if self.org_name is not None:
            result['OrgName'] = self.org_name
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        return result

    def from_map(self, map={}):
        self.urllist = []
        if map.get('URLList') is not None:
            for k in map.get('URLList'):
                temp_model = DetectSpineMRIRequestURLList()
                self.urllist.append(temp_model.from_map(k))
        if map.get('DataFormat') is not None:
            self.data_format = map.get('DataFormat')
        if map.get('OrgName') is not None:
            self.org_name = map.get('OrgName')
        if map.get('OrgId') is not None:
            self.org_id = map.get('OrgId')
        return self


class DetectSpineMRIRequestURLList(TeaModel):
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


class DetectSpineMRIResponse(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id    # type: str
        self.data = data                # type: DetectSpineMRIResponseData

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
            temp_model = DetectSpineMRIResponseData()
            self.data = temp_model.from_map(map['Data'])
        return self


class DetectSpineMRIResponseDataDiscs(TeaModel):
    def __init__(self, disease=None, identification=None, location=None):
        self.disease = disease          # type: str
        self.identification = identification  # type: str
        self.location = location        # type: List[float]

    def validate(self):
        self.validate_required(self.disease, 'disease')
        self.validate_required(self.identification, 'identification')
        self.validate_required(self.location, 'location')

    def to_map(self):
        result = {}
        if self.disease is not None:
            result['Disease'] = self.disease
        if self.identification is not None:
            result['Identification'] = self.identification
        if self.location is not None:
            result['Location'] = self.location
        return result

    def from_map(self, map={}):
        if map.get('Disease') is not None:
            self.disease = map.get('Disease')
        if map.get('Identification') is not None:
            self.identification = map.get('Identification')
        if map.get('Location') is not None:
            self.location = map.get('Location')
        return self


class DetectSpineMRIResponseDataVertebras(TeaModel):
    def __init__(self, disease=None, identification=None, location=None):
        self.disease = disease          # type: str
        self.identification = identification  # type: str
        self.location = location        # type: List[float]

    def validate(self):
        self.validate_required(self.disease, 'disease')
        self.validate_required(self.identification, 'identification')
        self.validate_required(self.location, 'location')

    def to_map(self):
        result = {}
        if self.disease is not None:
            result['Disease'] = self.disease
        if self.identification is not None:
            result['Identification'] = self.identification
        if self.location is not None:
            result['Location'] = self.location
        return result

    def from_map(self, map={}):
        if map.get('Disease') is not None:
            self.disease = map.get('Disease')
        if map.get('Identification') is not None:
            self.identification = map.get('Identification')
        if map.get('Location') is not None:
            self.location = map.get('Location')
        return self


class DetectSpineMRIResponseData(TeaModel):
    def __init__(self, discs=None, vertebras=None):
        self.discs = discs              # type: List[DetectSpineMRIResponseDataDiscs]
        self.vertebras = vertebras      # type: List[DetectSpineMRIResponseDataVertebras]

    def validate(self):
        self.validate_required(self.discs, 'discs')
        if self.discs:
            for k in self.discs:
                if k:
                    k.validate()
        self.validate_required(self.vertebras, 'vertebras')
        if self.vertebras:
            for k in self.vertebras:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Discs'] = []
        if self.discs is not None:
            for k in self.discs:
                result['Discs'].append(k.to_map() if k else None)
        result['Vertebras'] = []
        if self.vertebras is not None:
            for k in self.vertebras:
                result['Vertebras'].append(k.to_map() if k else None)
        return result

    def from_map(self, map={}):
        self.discs = []
        if map.get('Discs') is not None:
            for k in map.get('Discs'):
                temp_model = DetectSpineMRIResponseDataDiscs()
                self.discs.append(temp_model.from_map(k))
        self.vertebras = []
        if map.get('Vertebras') is not None:
            for k in map.get('Vertebras'):
                temp_model = DetectSpineMRIResponseDataVertebras()
                self.vertebras.append(temp_model.from_map(k))
        return self


class TranslateMedRequest(TeaModel):
    def __init__(self, from_language=None, to_language=None, text=None):
        self.from_language = from_language  # type: str
        self.to_language = to_language  # type: str
        self.text = text                # type: str

    def validate(self):
        self.validate_required(self.from_language, 'from_language')
        self.validate_required(self.to_language, 'to_language')
        self.validate_required(self.text, 'text')

    def to_map(self):
        result = {}
        if self.from_language is not None:
            result['FromLanguage'] = self.from_language
        if self.to_language is not None:
            result['ToLanguage'] = self.to_language
        if self.text is not None:
            result['Text'] = self.text
        return result

    def from_map(self, map={}):
        if map.get('FromLanguage') is not None:
            self.from_language = map.get('FromLanguage')
        if map.get('ToLanguage') is not None:
            self.to_language = map.get('ToLanguage')
        if map.get('Text') is not None:
            self.text = map.get('Text')
        return self


class TranslateMedResponse(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id    # type: str
        self.data = data                # type: TranslateMedResponseData

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
            temp_model = TranslateMedResponseData()
            self.data = temp_model.from_map(map['Data'])
        return self


class TranslateMedResponseData(TeaModel):
    def __init__(self, text=None, words=None):
        self.text = text                # type: str
        self.words = words              # type: int

    def validate(self):
        self.validate_required(self.text, 'text')
        self.validate_required(self.words, 'words')

    def to_map(self):
        result = {}
        if self.text is not None:
            result['Text'] = self.text
        if self.words is not None:
            result['Words'] = self.words
        return result

    def from_map(self, map={}):
        if map.get('Text') is not None:
            self.text = map.get('Text')
        if map.get('Words') is not None:
            self.words = map.get('Words')
        return self


class DetectLungNoduleRequest(TeaModel):
    def __init__(self, urllist=None, data_format=None, org_name=None, org_id=None):
        self.urllist = urllist          # type: List[DetectLungNoduleRequestURLList]
        self.data_format = data_format  # type: str
        self.org_name = org_name        # type: str
        self.org_id = org_id            # type: str

    def validate(self):
        self.validate_required(self.urllist, 'urllist')
        if self.urllist:
            for k in self.urllist:
                if k:
                    k.validate()
        self.validate_required(self.data_format, 'data_format')
        self.validate_required(self.org_name, 'org_name')
        self.validate_required(self.org_id, 'org_id')

    def to_map(self):
        result = {}
        result['URLList'] = []
        if self.urllist is not None:
            for k in self.urllist:
                result['URLList'].append(k.to_map() if k else None)
        if self.data_format is not None:
            result['DataFormat'] = self.data_format
        if self.org_name is not None:
            result['OrgName'] = self.org_name
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        return result

    def from_map(self, map={}):
        self.urllist = []
        if map.get('URLList') is not None:
            for k in map.get('URLList'):
                temp_model = DetectLungNoduleRequestURLList()
                self.urllist.append(temp_model.from_map(k))
        if map.get('DataFormat') is not None:
            self.data_format = map.get('DataFormat')
        if map.get('OrgName') is not None:
            self.org_name = map.get('OrgName')
        if map.get('OrgId') is not None:
            self.org_id = map.get('OrgId')
        return self


class DetectLungNoduleRequestURLList(TeaModel):
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


class DetectLungNoduleResponse(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id    # type: str
        self.data = data                # type: DetectLungNoduleResponseData

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
            temp_model = DetectLungNoduleResponseData()
            self.data = temp_model.from_map(map['Data'])
        return self


class DetectLungNoduleResponseDataSeriesElements(TeaModel):
    def __init__(self, category=None, confidence=None, diameter=None, lobe=None, lung=None, x=None, z=None, y=None,
                 image_x=None, image_y=None, image_z=None, sopinstance_uid=None, volume=None, mean_value=None):
        self.category = category        # type: str
        self.confidence = confidence    # type: float
        self.diameter = diameter        # type: float
        self.lobe = lobe                # type: str
        self.lung = lung                # type: str
        self.x = x                      # type: float
        self.z = z                      # type: float
        self.y = y                      # type: float
        self.image_x = image_x          # type: float
        self.image_y = image_y          # type: float
        self.image_z = image_z          # type: float
        self.sopinstance_uid = sopinstance_uid  # type: str
        self.volume = volume            # type: float
        self.mean_value = mean_value    # type: float

    def validate(self):
        self.validate_required(self.category, 'category')
        self.validate_required(self.confidence, 'confidence')
        self.validate_required(self.diameter, 'diameter')
        self.validate_required(self.lobe, 'lobe')
        self.validate_required(self.lung, 'lung')
        self.validate_required(self.x, 'x')
        self.validate_required(self.z, 'z')
        self.validate_required(self.y, 'y')
        self.validate_required(self.image_x, 'image_x')
        self.validate_required(self.image_y, 'image_y')
        self.validate_required(self.image_z, 'image_z')
        self.validate_required(self.sopinstance_uid, 'sopinstance_uid')
        self.validate_required(self.volume, 'volume')
        self.validate_required(self.mean_value, 'mean_value')

    def to_map(self):
        result = {}
        if self.category is not None:
            result['Category'] = self.category
        if self.confidence is not None:
            result['Confidence'] = self.confidence
        if self.diameter is not None:
            result['Diameter'] = self.diameter
        if self.lobe is not None:
            result['Lobe'] = self.lobe
        if self.lung is not None:
            result['Lung'] = self.lung
        if self.x is not None:
            result['X'] = self.x
        if self.z is not None:
            result['Z'] = self.z
        if self.y is not None:
            result['Y'] = self.y
        if self.image_x is not None:
            result['ImageX'] = self.image_x
        if self.image_y is not None:
            result['ImageY'] = self.image_y
        if self.image_z is not None:
            result['ImageZ'] = self.image_z
        if self.sopinstance_uid is not None:
            result['SOPInstanceUID'] = self.sopinstance_uid
        if self.volume is not None:
            result['Volume'] = self.volume
        if self.mean_value is not None:
            result['MeanValue'] = self.mean_value
        return result

    def from_map(self, map={}):
        if map.get('Category') is not None:
            self.category = map.get('Category')
        if map.get('Confidence') is not None:
            self.confidence = map.get('Confidence')
        if map.get('Diameter') is not None:
            self.diameter = map.get('Diameter')
        if map.get('Lobe') is not None:
            self.lobe = map.get('Lobe')
        if map.get('Lung') is not None:
            self.lung = map.get('Lung')
        if map.get('X') is not None:
            self.x = map.get('X')
        if map.get('Z') is not None:
            self.z = map.get('Z')
        if map.get('Y') is not None:
            self.y = map.get('Y')
        if map.get('ImageX') is not None:
            self.image_x = map.get('ImageX')
        if map.get('ImageY') is not None:
            self.image_y = map.get('ImageY')
        if map.get('ImageZ') is not None:
            self.image_z = map.get('ImageZ')
        if map.get('SOPInstanceUID') is not None:
            self.sopinstance_uid = map.get('SOPInstanceUID')
        if map.get('Volume') is not None:
            self.volume = map.get('Volume')
        if map.get('MeanValue') is not None:
            self.mean_value = map.get('MeanValue')
        return self


class DetectLungNoduleResponseDataSeries(TeaModel):
    def __init__(self, series_instance_uid=None, report=None, elements=None, origin=None, spacing=None):
        self.series_instance_uid = series_instance_uid  # type: str
        self.report = report            # type: str
        self.elements = elements        # type: List[DetectLungNoduleResponseDataSeriesElements]
        self.origin = origin            # type: List[float]
        self.spacing = spacing          # type: List[float]

    def validate(self):
        self.validate_required(self.series_instance_uid, 'series_instance_uid')
        self.validate_required(self.report, 'report')
        self.validate_required(self.elements, 'elements')
        if self.elements:
            for k in self.elements:
                if k:
                    k.validate()
        self.validate_required(self.origin, 'origin')
        self.validate_required(self.spacing, 'spacing')

    def to_map(self):
        result = {}
        if self.series_instance_uid is not None:
            result['SeriesInstanceUid'] = self.series_instance_uid
        if self.report is not None:
            result['Report'] = self.report
        result['Elements'] = []
        if self.elements is not None:
            for k in self.elements:
                result['Elements'].append(k.to_map() if k else None)
        if self.origin is not None:
            result['Origin'] = self.origin
        if self.spacing is not None:
            result['Spacing'] = self.spacing
        return result

    def from_map(self, map={}):
        if map.get('SeriesInstanceUid') is not None:
            self.series_instance_uid = map.get('SeriesInstanceUid')
        if map.get('Report') is not None:
            self.report = map.get('Report')
        self.elements = []
        if map.get('Elements') is not None:
            for k in map.get('Elements'):
                temp_model = DetectLungNoduleResponseDataSeriesElements()
                self.elements.append(temp_model.from_map(k))
        if map.get('Origin') is not None:
            self.origin = map.get('Origin')
        if map.get('Spacing') is not None:
            self.spacing = map.get('Spacing')
        return self


class DetectLungNoduleResponseData(TeaModel):
    def __init__(self, series=None):
        self.series = series            # type: List[DetectLungNoduleResponseDataSeries]

    def validate(self):
        self.validate_required(self.series, 'series')
        if self.series:
            for k in self.series:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Series'] = []
        if self.series is not None:
            for k in self.series:
                result['Series'].append(k.to_map() if k else None)
        return result

    def from_map(self, map={}):
        self.series = []
        if map.get('Series') is not None:
            for k in map.get('Series'):
                temp_model = DetectLungNoduleResponseDataSeries()
                self.series.append(temp_model.from_map(k))
        return self


class DetectCovid19CadRequest(TeaModel):
    def __init__(self, urllist=None, data_format=None, org_name=None, org_id=None):
        self.urllist = urllist          # type: List[DetectCovid19CadRequestURLList]
        self.data_format = data_format  # type: str
        self.org_name = org_name        # type: str
        self.org_id = org_id            # type: str

    def validate(self):
        self.validate_required(self.urllist, 'urllist')
        if self.urllist:
            for k in self.urllist:
                if k:
                    k.validate()
        self.validate_required(self.data_format, 'data_format')
        self.validate_required(self.org_name, 'org_name')
        self.validate_required(self.org_id, 'org_id')

    def to_map(self):
        result = {}
        result['URLList'] = []
        if self.urllist is not None:
            for k in self.urllist:
                result['URLList'].append(k.to_map() if k else None)
        if self.data_format is not None:
            result['DataFormat'] = self.data_format
        if self.org_name is not None:
            result['OrgName'] = self.org_name
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        return result

    def from_map(self, map={}):
        self.urllist = []
        if map.get('URLList') is not None:
            for k in map.get('URLList'):
                temp_model = DetectCovid19CadRequestURLList()
                self.urllist.append(temp_model.from_map(k))
        if map.get('DataFormat') is not None:
            self.data_format = map.get('DataFormat')
        if map.get('OrgName') is not None:
            self.org_name = map.get('OrgName')
        if map.get('OrgId') is not None:
            self.org_id = map.get('OrgId')
        return self


class DetectCovid19CadRequestURLList(TeaModel):
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


class DetectCovid19CadResponse(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id    # type: str
        self.data = data                # type: DetectCovid19CadResponseData

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
            temp_model = DetectCovid19CadResponseData()
            self.data = temp_model.from_map(map['Data'])
        return self


class DetectCovid19CadResponseData(TeaModel):
    def __init__(self, new_probability=None, normal_probability=None, other_probability=None, lesion_ratio=None,
                 mask=None):
        self.new_probability = new_probability  # type: str
        self.normal_probability = normal_probability  # type: str
        self.other_probability = other_probability  # type: str
        self.lesion_ratio = lesion_ratio  # type: str
        self.mask = mask                # type: str

    def validate(self):
        self.validate_required(self.new_probability, 'new_probability')
        self.validate_required(self.normal_probability, 'normal_probability')
        self.validate_required(self.other_probability, 'other_probability')
        self.validate_required(self.lesion_ratio, 'lesion_ratio')
        self.validate_required(self.mask, 'mask')

    def to_map(self):
        result = {}
        if self.new_probability is not None:
            result['NewProbability'] = self.new_probability
        if self.normal_probability is not None:
            result['NormalProbability'] = self.normal_probability
        if self.other_probability is not None:
            result['OtherProbability'] = self.other_probability
        if self.lesion_ratio is not None:
            result['LesionRatio'] = self.lesion_ratio
        if self.mask is not None:
            result['Mask'] = self.mask
        return result

    def from_map(self, map={}):
        if map.get('NewProbability') is not None:
            self.new_probability = map.get('NewProbability')
        if map.get('NormalProbability') is not None:
            self.normal_probability = map.get('NormalProbability')
        if map.get('OtherProbability') is not None:
            self.other_probability = map.get('OtherProbability')
        if map.get('LesionRatio') is not None:
            self.lesion_ratio = map.get('LesionRatio')
        if map.get('Mask') is not None:
            self.mask = map.get('Mask')
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
    def __init__(self, job_id=None, status=None, result=None, error_code=None, error_message=None):
        self.job_id = job_id            # type: str
        self.status = status            # type: str
        self.result = result            # type: str
        self.error_code = error_code    # type: str
        self.error_message = error_message  # type: str

    def validate(self):
        self.validate_required(self.job_id, 'job_id')
        self.validate_required(self.status, 'status')
        self.validate_required(self.result, 'result')
        self.validate_required(self.error_code, 'error_code')
        self.validate_required(self.error_message, 'error_message')

    def to_map(self):
        result = {}
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.status is not None:
            result['Status'] = self.status
        if self.result is not None:
            result['Result'] = self.result
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        return result

    def from_map(self, map={}):
        if map.get('JobId') is not None:
            self.job_id = map.get('JobId')
        if map.get('Status') is not None:
            self.status = map.get('Status')
        if map.get('Result') is not None:
            self.result = map.get('Result')
        if map.get('ErrorCode') is not None:
            self.error_code = map.get('ErrorCode')
        if map.get('ErrorMessage') is not None:
            self.error_message = map.get('ErrorMessage')
        return self


