# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, Any, BinaryIO, List


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
        result['Url'] = self.url
        result['OrgId'] = self.org_id
        result['OrgName'] = self.org_name
        return result

    def from_map(self, map={}):
        self.url = map.get('Url')
        self.org_id = map.get('OrgId')
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
        result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = DetectSkinDiseaseResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class DetectSkinDiseaseResponseData(TeaModel):
    def __init__(self, results=None):
        self.results = results          # type: Dict[str, Any]

    def validate(self):
        self.validate_required(self.results, 'results')

    def to_map(self):
        result = {}
        result['Results'] = self.results
        return result

    def from_map(self, map={}):
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
        result['UrlObject'] = self.url_object
        result['OrgId'] = self.org_id
        result['OrgName'] = self.org_name
        return result

    def from_map(self, map={}):
        self.url_object = map.get('UrlObject')
        self.org_id = map.get('OrgId')
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
        result['Question'] = self.question
        result['OrgId'] = self.org_id
        result['OrgName'] = self.org_name
        return result

    def from_map(self, map={}):
        self.question = map.get('Question')
        self.org_id = map.get('OrgId')
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
        result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = RunMedQAResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
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
        result['Answer'] = self.answer
        result['SimilarQuestion'] = self.similar_question
        return result

    def from_map(self, map={}):
        self.answer = map.get('Answer')
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
        result['ImageUrl'] = self.image_url
        result['DataFormat'] = self.data_format
        result['OrgId'] = self.org_id
        result['OrgName'] = self.org_name
        result['TracerId'] = self.tracer_id
        return result

    def from_map(self, map={}):
        self.image_url = map.get('ImageUrl')
        self.data_format = map.get('DataFormat')
        self.org_id = map.get('OrgId')
        self.org_name = map.get('OrgName')
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
        result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = DetectKneeKeypointXRayResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
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
        result['Direction'] = self.direction
        result['Label'] = self.label
        return result

    def from_map(self, map={}):
        self.direction = map.get('Direction')
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
        result['Value'] = self.value
        if self.tag is not None:
            result['Tag'] = self.tag.to_map()
        else:
            result['Tag'] = None
        result['Coordinates'] = self.coordinates
        return result

    def from_map(self, map={}):
        self.value = map.get('Value')
        if map.get('Tag') is not None:
            temp_model = DetectKneeKeypointXRayResponseDataKeyPointsTag()
            self.tag = temp_model.from_map(map['Tag'])
        else:
            self.tag = None
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
        result['ImageUrl'] = self.image_url
        result['OrgId'] = self.org_id
        result['OrgName'] = self.org_name
        result['KeyPoints'] = []
        if self.key_points is not None:
            for k in self.key_points:
                result['KeyPoints'].append(k.to_map() if k else None)
        else:
            result['KeyPoints'] = None
        return result

    def from_map(self, map={}):
        self.image_url = map.get('ImageUrl')
        self.org_id = map.get('OrgId')
        self.org_name = map.get('OrgName')
        self.key_points = []
        if map.get('KeyPoints') is not None:
            for k in map.get('KeyPoints'):
                temp_model = DetectKneeKeypointXRayResponseDataKeyPoints()
                self.key_points.append(temp_model.from_map(k))
        else:
            self.key_points = None
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
        result['ImageUrlObject'] = self.image_url_object
        result['DataFormat'] = self.data_format
        result['OrgId'] = self.org_id
        result['OrgName'] = self.org_name
        result['TracerId'] = self.tracer_id
        return result

    def from_map(self, map={}):
        self.image_url_object = map.get('ImageUrlObject')
        self.data_format = map.get('DataFormat')
        self.org_id = map.get('OrgId')
        self.org_name = map.get('OrgName')
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
        result['ImageUrl'] = self.image_url
        result['DataFormat'] = self.data_format
        result['OrgId'] = self.org_id
        result['OrgName'] = self.org_name
        result['TracerId'] = self.tracer_id
        return result

    def from_map(self, map={}):
        self.image_url = map.get('ImageUrl')
        self.data_format = map.get('DataFormat')
        self.org_id = map.get('OrgId')
        self.org_name = map.get('OrgName')
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
        result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = ClassifyFNFResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class ClassifyFNFResponseDataFracturesTag(TeaModel):
    def __init__(self, label=None):
        self.label = label              # type: str

    def validate(self):
        self.validate_required(self.label, 'label')

    def to_map(self):
        result = {}
        result['Label'] = self.label
        return result

    def from_map(self, map={}):
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
        result['Value'] = self.value
        if self.tag is not None:
            result['Tag'] = self.tag.to_map()
        else:
            result['Tag'] = None
        result['Boxes'] = self.boxes
        return result

    def from_map(self, map={}):
        self.value = map.get('Value')
        if map.get('Tag') is not None:
            temp_model = ClassifyFNFResponseDataFracturesTag()
            self.tag = temp_model.from_map(map['Tag'])
        else:
            self.tag = None
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
        result['ImageUrl'] = self.image_url
        result['OrgId'] = self.org_id
        result['OrgName'] = self.org_name
        result['Fractures'] = []
        if self.fractures is not None:
            for k in self.fractures:
                result['Fractures'].append(k.to_map() if k else None)
        else:
            result['Fractures'] = None
        return result

    def from_map(self, map={}):
        self.image_url = map.get('ImageUrl')
        self.org_id = map.get('OrgId')
        self.org_name = map.get('OrgName')
        self.fractures = []
        if map.get('Fractures') is not None:
            for k in map.get('Fractures'):
                temp_model = ClassifyFNFResponseDataFractures()
                self.fractures.append(temp_model.from_map(k))
        else:
            self.fractures = None
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
        result['ImageUrlObject'] = self.image_url_object
        result['DataFormat'] = self.data_format
        result['OrgId'] = self.org_id
        result['OrgName'] = self.org_name
        result['TracerId'] = self.tracer_id
        return result

    def from_map(self, map={}):
        self.image_url_object = map.get('ImageUrlObject')
        self.data_format = map.get('DataFormat')
        self.org_id = map.get('OrgId')
        self.org_name = map.get('OrgName')
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
        else:
            result['ReferenceList'] = None
        result['DataFormat'] = self.data_format
        result['OrgName'] = self.org_name
        result['OrgId'] = self.org_id
        result['DataSourceType'] = self.data_source_type
        result['FloatingList'] = []
        if self.floating_list is not None:
            for k in self.floating_list:
                result['FloatingList'].append(k.to_map() if k else None)
        else:
            result['FloatingList'] = None
        return result

    def from_map(self, map={}):
        self.reference_list = []
        if map.get('ReferenceList') is not None:
            for k in map.get('ReferenceList'):
                temp_model = RunCTRegistrationRequestReferenceList()
                self.reference_list.append(temp_model.from_map(k))
        else:
            self.reference_list = None
        self.data_format = map.get('DataFormat')
        self.org_name = map.get('OrgName')
        self.org_id = map.get('OrgId')
        self.data_source_type = map.get('DataSourceType')
        self.floating_list = []
        if map.get('FloatingList') is not None:
            for k in map.get('FloatingList'):
                temp_model = RunCTRegistrationRequestFloatingList()
                self.floating_list.append(temp_model.from_map(k))
        else:
            self.floating_list = None
        return self


class RunCTRegistrationRequestReferenceList(TeaModel):
    def __init__(self, reference_url=None):
        self.reference_url = reference_url  # type: str

    def validate(self):
        self.validate_required(self.reference_url, 'reference_url')

    def to_map(self):
        result = {}
        result['ReferenceURL'] = self.reference_url
        return result

    def from_map(self, map={}):
        self.reference_url = map.get('ReferenceURL')
        return self


class RunCTRegistrationRequestFloatingList(TeaModel):
    def __init__(self, floating_url=None):
        self.floating_url = floating_url  # type: str

    def validate(self):
        self.validate_required(self.floating_url, 'floating_url')

    def to_map(self):
        result = {}
        result['FloatingURL'] = self.floating_url
        return result

    def from_map(self, map={}):
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
        result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = RunCTRegistrationResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
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
        result['DUrl'] = self.durl
        result['NUrl'] = self.nurl
        return result

    def from_map(self, map={}):
        self.durl = map.get('DUrl')
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
        result['ImageUrl'] = self.image_url
        result['DataFormat'] = self.data_format
        result['OrgId'] = self.org_id
        result['OrgName'] = self.org_name
        result['TracerId'] = self.tracer_id
        return result

    def from_map(self, map={}):
        self.image_url = map.get('ImageUrl')
        self.data_format = map.get('DataFormat')
        self.org_id = map.get('OrgId')
        self.org_name = map.get('OrgName')
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
        result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = DetectHipKeypointXRayResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
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
        result['Direction'] = self.direction
        result['Label'] = self.label
        return result

    def from_map(self, map={}):
        self.direction = map.get('Direction')
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
        result['Value'] = self.value
        if self.tag is not None:
            result['Tag'] = self.tag.to_map()
        else:
            result['Tag'] = None
        result['Coordinates'] = self.coordinates
        return result

    def from_map(self, map={}):
        self.value = map.get('Value')
        if map.get('Tag') is not None:
            temp_model = DetectHipKeypointXRayResponseDataKeyPointsTag()
            self.tag = temp_model.from_map(map['Tag'])
        else:
            self.tag = None
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
        result['ImageUrl'] = self.image_url
        result['OrgId'] = self.org_id
        result['OrgName'] = self.org_name
        result['KeyPoints'] = []
        if self.key_points is not None:
            for k in self.key_points:
                result['KeyPoints'].append(k.to_map() if k else None)
        else:
            result['KeyPoints'] = None
        return result

    def from_map(self, map={}):
        self.image_url = map.get('ImageUrl')
        self.org_id = map.get('OrgId')
        self.org_name = map.get('OrgName')
        self.key_points = []
        if map.get('KeyPoints') is not None:
            for k in map.get('KeyPoints'):
                temp_model = DetectHipKeypointXRayResponseDataKeyPoints()
                self.key_points.append(temp_model.from_map(k))
        else:
            self.key_points = None
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
        result['ImageUrlObject'] = self.image_url_object
        result['DataFormat'] = self.data_format
        result['OrgId'] = self.org_id
        result['OrgName'] = self.org_name
        result['TracerId'] = self.tracer_id
        return result

    def from_map(self, map={}):
        self.image_url_object = map.get('ImageUrlObject')
        self.data_format = map.get('DataFormat')
        self.org_id = map.get('OrgId')
        self.org_name = map.get('OrgName')
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
        else:
            result['URLList'] = None
        result['DataFormat'] = self.data_format
        result['OrgName'] = self.org_name
        result['OrgId'] = self.org_id
        result['DataSourceType'] = self.data_source_type
        return result

    def from_map(self, map={}):
        self.urllist = []
        if map.get('URLList') is not None:
            for k in map.get('URLList'):
                temp_model = CalcCACSRequestURLList()
                self.urllist.append(temp_model.from_map(k))
        else:
            self.urllist = None
        self.data_format = map.get('DataFormat')
        self.org_name = map.get('OrgName')
        self.org_id = map.get('OrgId')
        self.data_source_type = map.get('DataSourceType')
        return self


class CalcCACSRequestURLList(TeaModel):
    def __init__(self, url=None):
        self.url = url                  # type: str

    def validate(self):
        self.validate_required(self.url, 'url')

    def to_map(self):
        result = {}
        result['URL'] = self.url
        return result

    def from_map(self, map={}):
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
        result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = CalcCACSResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
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
        result['Score'] = self.score
        result['ResultUrl'] = self.result_url
        return result

    def from_map(self, map={}):
        self.score = map.get('Score')
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
        result['Url'] = self.url
        result['DataFormat'] = self.data_format
        result['OrgName'] = self.org_name
        result['OrgId'] = self.org_id
        return result

    def from_map(self, map={}):
        self.url = map.get('Url')
        self.data_format = map.get('DataFormat')
        self.org_name = map.get('OrgName')
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
        result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = DetectKneeXRayResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class DetectKneeXRayResponseDataKLDetections(TeaModel):
    def __init__(self, detections=None):
        self.detections = detections    # type: List[float]

    def validate(self):
        self.validate_required(self.detections, 'detections')

    def to_map(self):
        result = {}
        result['Detections'] = self.detections
        return result

    def from_map(self, map={}):
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
        else:
            result['KLDetections'] = None
        return result

    def from_map(self, map={}):
        self.kldetections = []
        if map.get('KLDetections') is not None:
            for k in map.get('KLDetections'):
                temp_model = DetectKneeXRayResponseDataKLDetections()
                self.kldetections.append(temp_model.from_map(k))
        else:
            self.kldetections = None
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
        result['UrlObject'] = self.url_object
        result['DataFormat'] = self.data_format
        result['OrgName'] = self.org_name
        result['OrgId'] = self.org_id
        return result

    def from_map(self, map={}):
        self.url_object = map.get('UrlObject')
        self.data_format = map.get('DataFormat')
        self.org_name = map.get('OrgName')
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
        else:
            result['URLList'] = None
        result['DataFormat'] = self.data_format
        result['OrgName'] = self.org_name
        result['OrgId'] = self.org_id
        return result

    def from_map(self, map={}):
        self.urllist = []
        if map.get('URLList') is not None:
            for k in map.get('URLList'):
                temp_model = DetectSpineMRIRequestURLList()
                self.urllist.append(temp_model.from_map(k))
        else:
            self.urllist = None
        self.data_format = map.get('DataFormat')
        self.org_name = map.get('OrgName')
        self.org_id = map.get('OrgId')
        return self


class DetectSpineMRIRequestURLList(TeaModel):
    def __init__(self, url=None):
        self.url = url                  # type: str

    def validate(self):
        self.validate_required(self.url, 'url')

    def to_map(self):
        result = {}
        result['URL'] = self.url
        return result

    def from_map(self, map={}):
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
        result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = DetectSpineMRIResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
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
        result['Disease'] = self.disease
        result['Identification'] = self.identification
        result['Location'] = self.location
        return result

    def from_map(self, map={}):
        self.disease = map.get('Disease')
        self.identification = map.get('Identification')
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
        result['Disease'] = self.disease
        result['Identification'] = self.identification
        result['Location'] = self.location
        return result

    def from_map(self, map={}):
        self.disease = map.get('Disease')
        self.identification = map.get('Identification')
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
        else:
            result['Discs'] = None
        result['Vertebras'] = []
        if self.vertebras is not None:
            for k in self.vertebras:
                result['Vertebras'].append(k.to_map() if k else None)
        else:
            result['Vertebras'] = None
        return result

    def from_map(self, map={}):
        self.discs = []
        if map.get('Discs') is not None:
            for k in map.get('Discs'):
                temp_model = DetectSpineMRIResponseDataDiscs()
                self.discs.append(temp_model.from_map(k))
        else:
            self.discs = None
        self.vertebras = []
        if map.get('Vertebras') is not None:
            for k in map.get('Vertebras'):
                temp_model = DetectSpineMRIResponseDataVertebras()
                self.vertebras.append(temp_model.from_map(k))
        else:
            self.vertebras = None
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
        result['FromLanguage'] = self.from_language
        result['ToLanguage'] = self.to_language
        result['Text'] = self.text
        return result

    def from_map(self, map={}):
        self.from_language = map.get('FromLanguage')
        self.to_language = map.get('ToLanguage')
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
        result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = TranslateMedResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
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
        result['Text'] = self.text
        result['Words'] = self.words
        return result

    def from_map(self, map={}):
        self.text = map.get('Text')
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
        else:
            result['URLList'] = None
        result['DataFormat'] = self.data_format
        result['OrgName'] = self.org_name
        result['OrgId'] = self.org_id
        return result

    def from_map(self, map={}):
        self.urllist = []
        if map.get('URLList') is not None:
            for k in map.get('URLList'):
                temp_model = DetectLungNoduleRequestURLList()
                self.urllist.append(temp_model.from_map(k))
        else:
            self.urllist = None
        self.data_format = map.get('DataFormat')
        self.org_name = map.get('OrgName')
        self.org_id = map.get('OrgId')
        return self


class DetectLungNoduleRequestURLList(TeaModel):
    def __init__(self, url=None):
        self.url = url                  # type: str

    def validate(self):
        self.validate_required(self.url, 'url')

    def to_map(self):
        result = {}
        result['URL'] = self.url
        return result

    def from_map(self, map={}):
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
        result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = DetectLungNoduleResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class DetectLungNoduleResponseDataSeriesElements(TeaModel):
    def __init__(self, category=None, confidence=None, diameter=None, lobe=None, lung=None, x=None, z=None, y=None,
                 image_x=None, image_y=None, image_z=None):
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

    def to_map(self):
        result = {}
        result['Category'] = self.category
        result['Confidence'] = self.confidence
        result['Diameter'] = self.diameter
        result['Lobe'] = self.lobe
        result['Lung'] = self.lung
        result['X'] = self.x
        result['Z'] = self.z
        result['Y'] = self.y
        result['ImageX'] = self.image_x
        result['ImageY'] = self.image_y
        result['ImageZ'] = self.image_z
        return result

    def from_map(self, map={}):
        self.category = map.get('Category')
        self.confidence = map.get('Confidence')
        self.diameter = map.get('Diameter')
        self.lobe = map.get('Lobe')
        self.lung = map.get('Lung')
        self.x = map.get('X')
        self.z = map.get('Z')
        self.y = map.get('Y')
        self.image_x = map.get('ImageX')
        self.image_y = map.get('ImageY')
        self.image_z = map.get('ImageZ')
        return self


class DetectLungNoduleResponseDataSeries(TeaModel):
    def __init__(self, series_instance_uid=None, elements=None, origin=None, spacing=None):
        self.series_instance_uid = series_instance_uid  # type: str
        self.elements = elements        # type: List[DetectLungNoduleResponseDataSeriesElements]
        self.origin = origin            # type: List[float]
        self.spacing = spacing          # type: List[float]

    def validate(self):
        self.validate_required(self.series_instance_uid, 'series_instance_uid')
        self.validate_required(self.elements, 'elements')
        if self.elements:
            for k in self.elements:
                if k:
                    k.validate()
        self.validate_required(self.origin, 'origin')
        self.validate_required(self.spacing, 'spacing')

    def to_map(self):
        result = {}
        result['SeriesInstanceUid'] = self.series_instance_uid
        result['Elements'] = []
        if self.elements is not None:
            for k in self.elements:
                result['Elements'].append(k.to_map() if k else None)
        else:
            result['Elements'] = None
        result['Origin'] = self.origin
        result['Spacing'] = self.spacing
        return result

    def from_map(self, map={}):
        self.series_instance_uid = map.get('SeriesInstanceUid')
        self.elements = []
        if map.get('Elements') is not None:
            for k in map.get('Elements'):
                temp_model = DetectLungNoduleResponseDataSeriesElements()
                self.elements.append(temp_model.from_map(k))
        else:
            self.elements = None
        self.origin = map.get('Origin')
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
        else:
            result['Series'] = None
        return result

    def from_map(self, map={}):
        self.series = []
        if map.get('Series') is not None:
            for k in map.get('Series'):
                temp_model = DetectLungNoduleResponseDataSeries()
                self.series.append(temp_model.from_map(k))
        else:
            self.series = None
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
        else:
            result['URLList'] = None
        result['DataFormat'] = self.data_format
        result['OrgName'] = self.org_name
        result['OrgId'] = self.org_id
        return result

    def from_map(self, map={}):
        self.urllist = []
        if map.get('URLList') is not None:
            for k in map.get('URLList'):
                temp_model = DetectCovid19CadRequestURLList()
                self.urllist.append(temp_model.from_map(k))
        else:
            self.urllist = None
        self.data_format = map.get('DataFormat')
        self.org_name = map.get('OrgName')
        self.org_id = map.get('OrgId')
        return self


class DetectCovid19CadRequestURLList(TeaModel):
    def __init__(self, url=None):
        self.url = url                  # type: str

    def validate(self):
        self.validate_required(self.url, 'url')

    def to_map(self):
        result = {}
        result['URL'] = self.url
        return result

    def from_map(self, map={}):
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
        result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = DetectCovid19CadResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
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
        result['NewProbability'] = self.new_probability
        result['NormalProbability'] = self.normal_probability
        result['OtherProbability'] = self.other_probability
        result['LesionRatio'] = self.lesion_ratio
        result['Mask'] = self.mask
        return result

    def from_map(self, map={}):
        self.new_probability = map.get('NewProbability')
        self.normal_probability = map.get('NormalProbability')
        self.other_probability = map.get('OtherProbability')
        self.lesion_ratio = map.get('LesionRatio')
        self.mask = map.get('Mask')
        return self


class GetAsyncJobResultRequest(TeaModel):
    def __init__(self, job_id=None):
        self.job_id = job_id            # type: str

    def validate(self):
        self.validate_required(self.job_id, 'job_id')

    def to_map(self):
        result = {}
        result['JobId'] = self.job_id
        return result

    def from_map(self, map={}):
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
        result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = GetAsyncJobResultResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
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
        result['JobId'] = self.job_id
        result['Status'] = self.status
        result['Result'] = self.result
        result['ErrorCode'] = self.error_code
        result['ErrorMessage'] = self.error_message
        return result

    def from_map(self, map={}):
        self.job_id = map.get('JobId')
        self.status = map.get('Status')
        self.result = map.get('Result')
        self.error_code = map.get('ErrorCode')
        self.error_message = map.get('ErrorMessage')
        return self


