# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict, Any, BinaryIO


class DetectRibFractureRequestURLList(TeaModel):
    def __init__(
        self,
        url: str = None,
    ):
        self.url = url

    def validate(self):
        self.validate_required(self.url, 'url')

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


class DetectRibFractureRequest(TeaModel):
    def __init__(
        self,
        urllist: List[DetectRibFractureRequestURLList] = None,
        data_format: str = None,
        org_name: str = None,
        org_id: str = None,
        source_type: str = None,
    ):
        self.urllist = urllist
        self.data_format = data_format
        self.org_name = org_name
        self.org_id = org_id
        self.source_type = source_type

    def validate(self):
        self.validate_required(self.urllist, 'urllist')
        if self.urllist:
            for k in self.urllist:
                if k:
                    k.validate()
        self.validate_required(self.data_format, 'data_format')
        self.validate_required(self.org_name, 'org_name')
        self.validate_required(self.org_id, 'org_id')
        self.validate_required(self.source_type, 'source_type')

    def to_map(self):
        result = dict()
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
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.urllist = []
        if m.get('URLList') is not None:
            for k in m.get('URLList'):
                temp_model = DetectRibFractureRequestURLList()
                self.urllist.append(temp_model.from_map(k))
        if m.get('DataFormat') is not None:
            self.data_format = m.get('DataFormat')
        if m.get('OrgName') is not None:
            self.org_name = m.get('OrgName')
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        return self


class DetectRibFractureResponseDataDetections(TeaModel):
    def __init__(
        self,
        fracture_id: int = None,
        fracture_confidence: float = None,
        fracture_category: str = None,
        coordinates: List[int] = None,
        coordinate_image: List[int] = None,
    ):
        self.fracture_id = fracture_id
        self.fracture_confidence = fracture_confidence
        self.fracture_category = fracture_category
        self.coordinates = coordinates
        self.coordinate_image = coordinate_image

    def validate(self):
        self.validate_required(self.fracture_id, 'fracture_id')
        self.validate_required(self.fracture_confidence, 'fracture_confidence')
        self.validate_required(self.fracture_category, 'fracture_category')
        self.validate_required(self.coordinates, 'coordinates')
        self.validate_required(self.coordinate_image, 'coordinate_image')

    def to_map(self):
        result = dict()
        if self.fracture_id is not None:
            result['FractureId'] = self.fracture_id
        if self.fracture_confidence is not None:
            result['FractureConfidence'] = self.fracture_confidence
        if self.fracture_category is not None:
            result['FractureCategory'] = self.fracture_category
        if self.coordinates is not None:
            result['Coordinates'] = self.coordinates
        if self.coordinate_image is not None:
            result['CoordinateImage'] = self.coordinate_image
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FractureId') is not None:
            self.fracture_id = m.get('FractureId')
        if m.get('FractureConfidence') is not None:
            self.fracture_confidence = m.get('FractureConfidence')
        if m.get('FractureCategory') is not None:
            self.fracture_category = m.get('FractureCategory')
        if m.get('Coordinates') is not None:
            self.coordinates = m.get('Coordinates')
        if m.get('CoordinateImage') is not None:
            self.coordinate_image = m.get('CoordinateImage')
        return self


class DetectRibFractureResponseData(TeaModel):
    def __init__(
        self,
        result_url: str = None,
        detections: List[DetectRibFractureResponseDataDetections] = None,
        spacing: List[float] = None,
        origin: List[float] = None,
    ):
        self.result_url = result_url
        self.detections = detections
        self.spacing = spacing
        self.origin = origin

    def validate(self):
        self.validate_required(self.result_url, 'result_url')
        self.validate_required(self.detections, 'detections')
        if self.detections:
            for k in self.detections:
                if k:
                    k.validate()
        self.validate_required(self.spacing, 'spacing')
        self.validate_required(self.origin, 'origin')

    def to_map(self):
        result = dict()
        if self.result_url is not None:
            result['ResultURL'] = self.result_url
        result['Detections'] = []
        if self.detections is not None:
            for k in self.detections:
                result['Detections'].append(k.to_map() if k else None)
        if self.spacing is not None:
            result['Spacing'] = self.spacing
        if self.origin is not None:
            result['Origin'] = self.origin
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResultURL') is not None:
            self.result_url = m.get('ResultURL')
        self.detections = []
        if m.get('Detections') is not None:
            for k in m.get('Detections'):
                temp_model = DetectRibFractureResponseDataDetections()
                self.detections.append(temp_model.from_map(k))
        if m.get('Spacing') is not None:
            self.spacing = m.get('Spacing')
        if m.get('Origin') is not None:
            self.origin = m.get('Origin')
        return self


class DetectRibFractureResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: DetectRibFractureResponseData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
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
            temp_model = DetectRibFractureResponseData()
            self.data = temp_model.from_map(m['Data'])
        return self


class ScreenChestCTRequestURLList(TeaModel):
    def __init__(
        self,
        url: str = None,
    ):
        self.url = url

    def validate(self):
        self.validate_required(self.url, 'url')

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


class ScreenChestCTRequest(TeaModel):
    def __init__(
        self,
        data_format: str = None,
        org_name: str = None,
        org_id: str = None,
        urllist: List[ScreenChestCTRequestURLList] = None,
    ):
        self.data_format = data_format
        self.org_name = org_name
        self.org_id = org_id
        self.urllist = urllist

    def validate(self):
        self.validate_required(self.data_format, 'data_format')
        self.validate_required(self.org_name, 'org_name')
        self.validate_required(self.org_id, 'org_id')
        self.validate_required(self.urllist, 'urllist')
        if self.urllist:
            for k in self.urllist:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.data_format is not None:
            result['DataFormat'] = self.data_format
        if self.org_name is not None:
            result['OrgName'] = self.org_name
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        result['URLList'] = []
        if self.urllist is not None:
            for k in self.urllist:
                result['URLList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataFormat') is not None:
            self.data_format = m.get('DataFormat')
        if m.get('OrgName') is not None:
            self.org_name = m.get('OrgName')
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        self.urllist = []
        if m.get('URLList') is not None:
            for k in m.get('URLList'):
                temp_model = ScreenChestCTRequestURLList()
                self.urllist.append(temp_model.from_map(k))
        return self


class ScreenChestCTResponseDataLungNoduleSeriesElements(TeaModel):
    def __init__(
        self,
        category: str = None,
        confidence: float = None,
        diameter: float = None,
        lobe: str = None,
        lung: str = None,
        x: float = None,
        z: float = None,
        y: float = None,
        image_x: float = None,
        image_y: float = None,
        image_z: float = None,
        sopinstance_uid: str = None,
        volume: float = None,
        mean_value: float = None,
    ):
        self.category = category
        self.confidence = confidence
        self.diameter = diameter
        self.lobe = lobe
        self.lung = lung
        self.x = x
        self.z = z
        self.y = y
        self.image_x = image_x
        self.image_y = image_y
        self.image_z = image_z
        self.sopinstance_uid = sopinstance_uid
        self.volume = volume
        self.mean_value = mean_value

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
        result = dict()
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Confidence') is not None:
            self.confidence = m.get('Confidence')
        if m.get('Diameter') is not None:
            self.diameter = m.get('Diameter')
        if m.get('Lobe') is not None:
            self.lobe = m.get('Lobe')
        if m.get('Lung') is not None:
            self.lung = m.get('Lung')
        if m.get('X') is not None:
            self.x = m.get('X')
        if m.get('Z') is not None:
            self.z = m.get('Z')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        if m.get('ImageX') is not None:
            self.image_x = m.get('ImageX')
        if m.get('ImageY') is not None:
            self.image_y = m.get('ImageY')
        if m.get('ImageZ') is not None:
            self.image_z = m.get('ImageZ')
        if m.get('SOPInstanceUID') is not None:
            self.sopinstance_uid = m.get('SOPInstanceUID')
        if m.get('Volume') is not None:
            self.volume = m.get('Volume')
        if m.get('MeanValue') is not None:
            self.mean_value = m.get('MeanValue')
        return self


class ScreenChestCTResponseDataLungNoduleSeries(TeaModel):
    def __init__(
        self,
        series_instance_uid: str = None,
        report: str = None,
        elements: List[ScreenChestCTResponseDataLungNoduleSeriesElements] = None,
        origin: List[float] = None,
        spacing: List[float] = None,
    ):
        self.series_instance_uid = series_instance_uid
        self.report = report
        self.elements = elements
        self.origin = origin
        self.spacing = spacing

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
        result = dict()
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SeriesInstanceUid') is not None:
            self.series_instance_uid = m.get('SeriesInstanceUid')
        if m.get('Report') is not None:
            self.report = m.get('Report')
        self.elements = []
        if m.get('Elements') is not None:
            for k in m.get('Elements'):
                temp_model = ScreenChestCTResponseDataLungNoduleSeriesElements()
                self.elements.append(temp_model.from_map(k))
        if m.get('Origin') is not None:
            self.origin = m.get('Origin')
        if m.get('Spacing') is not None:
            self.spacing = m.get('Spacing')
        return self


class ScreenChestCTResponseDataLungNodule(TeaModel):
    def __init__(
        self,
        series: List[ScreenChestCTResponseDataLungNoduleSeries] = None,
    ):
        self.series = series

    def validate(self):
        self.validate_required(self.series, 'series')
        if self.series:
            for k in self.series:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Series'] = []
        if self.series is not None:
            for k in self.series:
                result['Series'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.series = []
        if m.get('Series') is not None:
            for k in m.get('Series'):
                temp_model = ScreenChestCTResponseDataLungNoduleSeries()
                self.series.append(temp_model.from_map(k))
        return self


class ScreenChestCTResponseDataCACS(TeaModel):
    def __init__(
        self,
        score: str = None,
        result_url: str = None,
    ):
        self.score = score
        self.result_url = result_url

    def validate(self):
        self.validate_required(self.score, 'score')
        self.validate_required(self.result_url, 'result_url')

    def to_map(self):
        result = dict()
        if self.score is not None:
            result['Score'] = self.score
        if self.result_url is not None:
            result['ResultUrl'] = self.result_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('ResultUrl') is not None:
            self.result_url = m.get('ResultUrl')
        return self


class ScreenChestCTResponseDataCovid(TeaModel):
    def __init__(
        self,
        new_probability: str = None,
        normal_probability: str = None,
        other_probability: str = None,
        lesion_ratio: str = None,
        mask: str = None,
    ):
        self.new_probability = new_probability
        self.normal_probability = normal_probability
        self.other_probability = other_probability
        self.lesion_ratio = lesion_ratio
        self.mask = mask

    def validate(self):
        self.validate_required(self.new_probability, 'new_probability')
        self.validate_required(self.normal_probability, 'normal_probability')
        self.validate_required(self.other_probability, 'other_probability')
        self.validate_required(self.lesion_ratio, 'lesion_ratio')
        self.validate_required(self.mask, 'mask')

    def to_map(self):
        result = dict()
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NewProbability') is not None:
            self.new_probability = m.get('NewProbability')
        if m.get('NormalProbability') is not None:
            self.normal_probability = m.get('NormalProbability')
        if m.get('OtherProbability') is not None:
            self.other_probability = m.get('OtherProbability')
        if m.get('LesionRatio') is not None:
            self.lesion_ratio = m.get('LesionRatio')
        if m.get('Mask') is not None:
            self.mask = m.get('Mask')
        return self


class ScreenChestCTResponseData(TeaModel):
    def __init__(
        self,
        lung_nodule: ScreenChestCTResponseDataLungNodule = None,
        cacs: ScreenChestCTResponseDataCACS = None,
        covid: ScreenChestCTResponseDataCovid = None,
    ):
        self.lung_nodule = lung_nodule
        self.cacs = cacs
        self.covid = covid

    def validate(self):
        self.validate_required(self.lung_nodule, 'lung_nodule')
        if self.lung_nodule:
            self.lung_nodule.validate()
        self.validate_required(self.cacs, 'cacs')
        if self.cacs:
            self.cacs.validate()
        self.validate_required(self.covid, 'covid')
        if self.covid:
            self.covid.validate()

    def to_map(self):
        result = dict()
        if self.lung_nodule is not None:
            result['LungNodule'] = self.lung_nodule.to_map()
        if self.cacs is not None:
            result['CACS'] = self.cacs.to_map()
        if self.covid is not None:
            result['Covid'] = self.covid.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LungNodule') is not None:
            temp_model = ScreenChestCTResponseDataLungNodule()
            self.lung_nodule = temp_model.from_map(m['LungNodule'])
        if m.get('CACS') is not None:
            temp_model = ScreenChestCTResponseDataCACS()
            self.cacs = temp_model.from_map(m['CACS'])
        if m.get('Covid') is not None:
            temp_model = ScreenChestCTResponseDataCovid()
            self.covid = temp_model.from_map(m['Covid'])
        return self


class ScreenChestCTResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: ScreenChestCTResponseData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
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
            temp_model = ScreenChestCTResponseData()
            self.data = temp_model.from_map(m['Data'])
        return self


class DetectSkinDiseaseRequest(TeaModel):
    def __init__(
        self,
        url: str = None,
        org_id: str = None,
        org_name: str = None,
    ):
        self.url = url
        self.org_id = org_id
        self.org_name = org_name

    def validate(self):
        self.validate_required(self.url, 'url')
        self.validate_required(self.org_id, 'org_id')
        self.validate_required(self.org_name, 'org_name')

    def to_map(self):
        result = dict()
        if self.url is not None:
            result['Url'] = self.url
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.org_name is not None:
            result['OrgName'] = self.org_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('OrgName') is not None:
            self.org_name = m.get('OrgName')
        return self


class DetectSkinDiseaseResponseData(TeaModel):
    def __init__(
        self,
        results: Dict[str, Any] = None,
    ):
        self.results = results

    def validate(self):
        self.validate_required(self.results, 'results')

    def to_map(self):
        result = dict()
        if self.results is not None:
            result['Results'] = self.results
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Results') is not None:
            self.results = m.get('Results')
        return self


class DetectSkinDiseaseResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: DetectSkinDiseaseResponseData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
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
            temp_model = DetectSkinDiseaseResponseData()
            self.data = temp_model.from_map(m['Data'])
        return self


class DetectSkinDiseaseAdvanceRequest(TeaModel):
    def __init__(
        self,
        url_object: BinaryIO = None,
        org_id: str = None,
        org_name: str = None,
    ):
        self.url_object = url_object
        self.org_id = org_id
        self.org_name = org_name

    def validate(self):
        self.validate_required(self.url_object, 'url_object')
        self.validate_required(self.org_id, 'org_id')
        self.validate_required(self.org_name, 'org_name')

    def to_map(self):
        result = dict()
        if self.url_object is not None:
            result['UrlObject'] = self.url_object
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.org_name is not None:
            result['OrgName'] = self.org_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UrlObject') is not None:
            self.url_object = m.get('UrlObject')
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('OrgName') is not None:
            self.org_name = m.get('OrgName')
        return self


class RunMedQARequest(TeaModel):
    def __init__(
        self,
        question: str = None,
        org_id: str = None,
        org_name: str = None,
    ):
        self.question = question
        self.org_id = org_id
        self.org_name = org_name

    def validate(self):
        self.validate_required(self.question, 'question')
        self.validate_required(self.org_id, 'org_id')
        self.validate_required(self.org_name, 'org_name')

    def to_map(self):
        result = dict()
        if self.question is not None:
            result['Question'] = self.question
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.org_name is not None:
            result['OrgName'] = self.org_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Question') is not None:
            self.question = m.get('Question')
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('OrgName') is not None:
            self.org_name = m.get('OrgName')
        return self


class RunMedQAResponseData(TeaModel):
    def __init__(
        self,
        answer: str = None,
        similar_question: List[str] = None,
    ):
        self.answer = answer
        self.similar_question = similar_question

    def validate(self):
        self.validate_required(self.answer, 'answer')
        self.validate_required(self.similar_question, 'similar_question')

    def to_map(self):
        result = dict()
        if self.answer is not None:
            result['Answer'] = self.answer
        if self.similar_question is not None:
            result['SimilarQuestion'] = self.similar_question
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Answer') is not None:
            self.answer = m.get('Answer')
        if m.get('SimilarQuestion') is not None:
            self.similar_question = m.get('SimilarQuestion')
        return self


class RunMedQAResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: RunMedQAResponseData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
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
            temp_model = RunMedQAResponseData()
            self.data = temp_model.from_map(m['Data'])
        return self


class DetectKneeKeypointXRayRequest(TeaModel):
    def __init__(
        self,
        image_url: str = None,
        data_format: str = None,
        org_id: str = None,
        org_name: str = None,
        tracer_id: str = None,
    ):
        self.image_url = image_url
        self.data_format = data_format
        self.org_id = org_id
        self.org_name = org_name
        self.tracer_id = tracer_id

    def validate(self):
        self.validate_required(self.image_url, 'image_url')
        self.validate_required(self.data_format, 'data_format')
        self.validate_required(self.org_id, 'org_id')
        self.validate_required(self.org_name, 'org_name')

    def to_map(self):
        result = dict()
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        if m.get('DataFormat') is not None:
            self.data_format = m.get('DataFormat')
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('OrgName') is not None:
            self.org_name = m.get('OrgName')
        if m.get('TracerId') is not None:
            self.tracer_id = m.get('TracerId')
        return self


class DetectKneeKeypointXRayResponseDataKeyPointsTag(TeaModel):
    def __init__(
        self,
        direction: str = None,
        label: str = None,
    ):
        self.direction = direction
        self.label = label

    def validate(self):
        self.validate_required(self.direction, 'direction')
        self.validate_required(self.label, 'label')

    def to_map(self):
        result = dict()
        if self.direction is not None:
            result['Direction'] = self.direction
        if self.label is not None:
            result['Label'] = self.label
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Direction') is not None:
            self.direction = m.get('Direction')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        return self


class DetectKneeKeypointXRayResponseDataKeyPoints(TeaModel):
    def __init__(
        self,
        value: float = None,
        tag: DetectKneeKeypointXRayResponseDataKeyPointsTag = None,
        coordinates: List[int] = None,
    ):
        self.value = value
        self.tag = tag
        self.coordinates = coordinates

    def validate(self):
        self.validate_required(self.value, 'value')
        self.validate_required(self.tag, 'tag')
        if self.tag:
            self.tag.validate()
        self.validate_required(self.coordinates, 'coordinates')

    def to_map(self):
        result = dict()
        if self.value is not None:
            result['Value'] = self.value
        if self.tag is not None:
            result['Tag'] = self.tag.to_map()
        if self.coordinates is not None:
            result['Coordinates'] = self.coordinates
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('Tag') is not None:
            temp_model = DetectKneeKeypointXRayResponseDataKeyPointsTag()
            self.tag = temp_model.from_map(m['Tag'])
        if m.get('Coordinates') is not None:
            self.coordinates = m.get('Coordinates')
        return self


class DetectKneeKeypointXRayResponseData(TeaModel):
    def __init__(
        self,
        image_url: str = None,
        org_id: str = None,
        org_name: str = None,
        key_points: List[DetectKneeKeypointXRayResponseDataKeyPoints] = None,
    ):
        self.image_url = image_url
        self.org_id = org_id
        self.org_name = org_name
        self.key_points = key_points

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
        result = dict()
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('OrgName') is not None:
            self.org_name = m.get('OrgName')
        self.key_points = []
        if m.get('KeyPoints') is not None:
            for k in m.get('KeyPoints'):
                temp_model = DetectKneeKeypointXRayResponseDataKeyPoints()
                self.key_points.append(temp_model.from_map(k))
        return self


class DetectKneeKeypointXRayResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: DetectKneeKeypointXRayResponseData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
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
            temp_model = DetectKneeKeypointXRayResponseData()
            self.data = temp_model.from_map(m['Data'])
        return self


class DetectKneeKeypointXRayAdvanceRequest(TeaModel):
    def __init__(
        self,
        image_url_object: BinaryIO = None,
        data_format: str = None,
        org_id: str = None,
        org_name: str = None,
        tracer_id: str = None,
    ):
        self.image_url_object = image_url_object
        self.data_format = data_format
        self.org_id = org_id
        self.org_name = org_name
        self.tracer_id = tracer_id

    def validate(self):
        self.validate_required(self.image_url_object, 'image_url_object')
        self.validate_required(self.data_format, 'data_format')
        self.validate_required(self.org_id, 'org_id')
        self.validate_required(self.org_name, 'org_name')

    def to_map(self):
        result = dict()
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageUrlObject') is not None:
            self.image_url_object = m.get('ImageUrlObject')
        if m.get('DataFormat') is not None:
            self.data_format = m.get('DataFormat')
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('OrgName') is not None:
            self.org_name = m.get('OrgName')
        if m.get('TracerId') is not None:
            self.tracer_id = m.get('TracerId')
        return self


class ClassifyFNFRequest(TeaModel):
    def __init__(
        self,
        image_url: str = None,
        data_format: str = None,
        org_id: str = None,
        org_name: str = None,
        tracer_id: str = None,
    ):
        self.image_url = image_url
        self.data_format = data_format
        self.org_id = org_id
        self.org_name = org_name
        self.tracer_id = tracer_id

    def validate(self):
        self.validate_required(self.image_url, 'image_url')
        self.validate_required(self.data_format, 'data_format')
        self.validate_required(self.org_id, 'org_id')
        self.validate_required(self.org_name, 'org_name')

    def to_map(self):
        result = dict()
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        if m.get('DataFormat') is not None:
            self.data_format = m.get('DataFormat')
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('OrgName') is not None:
            self.org_name = m.get('OrgName')
        if m.get('TracerId') is not None:
            self.tracer_id = m.get('TracerId')
        return self


class ClassifyFNFResponseDataFracturesTag(TeaModel):
    def __init__(
        self,
        label: str = None,
    ):
        self.label = label

    def validate(self):
        self.validate_required(self.label, 'label')

    def to_map(self):
        result = dict()
        if self.label is not None:
            result['Label'] = self.label
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Label') is not None:
            self.label = m.get('Label')
        return self


class ClassifyFNFResponseDataFractures(TeaModel):
    def __init__(
        self,
        value: float = None,
        tag: ClassifyFNFResponseDataFracturesTag = None,
        boxes: List[int] = None,
    ):
        self.value = value
        self.tag = tag
        self.boxes = boxes

    def validate(self):
        self.validate_required(self.value, 'value')
        self.validate_required(self.tag, 'tag')
        if self.tag:
            self.tag.validate()
        self.validate_required(self.boxes, 'boxes')

    def to_map(self):
        result = dict()
        if self.value is not None:
            result['Value'] = self.value
        if self.tag is not None:
            result['Tag'] = self.tag.to_map()
        if self.boxes is not None:
            result['Boxes'] = self.boxes
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('Tag') is not None:
            temp_model = ClassifyFNFResponseDataFracturesTag()
            self.tag = temp_model.from_map(m['Tag'])
        if m.get('Boxes') is not None:
            self.boxes = m.get('Boxes')
        return self


class ClassifyFNFResponseData(TeaModel):
    def __init__(
        self,
        image_url: str = None,
        org_id: str = None,
        org_name: str = None,
        fractures: List[ClassifyFNFResponseDataFractures] = None,
    ):
        self.image_url = image_url
        self.org_id = org_id
        self.org_name = org_name
        self.fractures = fractures

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
        result = dict()
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('OrgName') is not None:
            self.org_name = m.get('OrgName')
        self.fractures = []
        if m.get('Fractures') is not None:
            for k in m.get('Fractures'):
                temp_model = ClassifyFNFResponseDataFractures()
                self.fractures.append(temp_model.from_map(k))
        return self


class ClassifyFNFResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: ClassifyFNFResponseData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
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
            temp_model = ClassifyFNFResponseData()
            self.data = temp_model.from_map(m['Data'])
        return self


class ClassifyFNFAdvanceRequest(TeaModel):
    def __init__(
        self,
        image_url_object: BinaryIO = None,
        data_format: str = None,
        org_id: str = None,
        org_name: str = None,
        tracer_id: str = None,
    ):
        self.image_url_object = image_url_object
        self.data_format = data_format
        self.org_id = org_id
        self.org_name = org_name
        self.tracer_id = tracer_id

    def validate(self):
        self.validate_required(self.image_url_object, 'image_url_object')
        self.validate_required(self.data_format, 'data_format')
        self.validate_required(self.org_id, 'org_id')
        self.validate_required(self.org_name, 'org_name')

    def to_map(self):
        result = dict()
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageUrlObject') is not None:
            self.image_url_object = m.get('ImageUrlObject')
        if m.get('DataFormat') is not None:
            self.data_format = m.get('DataFormat')
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('OrgName') is not None:
            self.org_name = m.get('OrgName')
        if m.get('TracerId') is not None:
            self.tracer_id = m.get('TracerId')
        return self


class RunCTRegistrationRequestReferenceList(TeaModel):
    def __init__(
        self,
        reference_url: str = None,
    ):
        self.reference_url = reference_url

    def validate(self):
        self.validate_required(self.reference_url, 'reference_url')

    def to_map(self):
        result = dict()
        if self.reference_url is not None:
            result['ReferenceURL'] = self.reference_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReferenceURL') is not None:
            self.reference_url = m.get('ReferenceURL')
        return self


class RunCTRegistrationRequestFloatingList(TeaModel):
    def __init__(
        self,
        floating_url: str = None,
    ):
        self.floating_url = floating_url

    def validate(self):
        self.validate_required(self.floating_url, 'floating_url')

    def to_map(self):
        result = dict()
        if self.floating_url is not None:
            result['FloatingURL'] = self.floating_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FloatingURL') is not None:
            self.floating_url = m.get('FloatingURL')
        return self


class RunCTRegistrationRequest(TeaModel):
    def __init__(
        self,
        reference_list: List[RunCTRegistrationRequestReferenceList] = None,
        data_format: str = None,
        org_name: str = None,
        org_id: str = None,
        data_source_type: str = None,
        floating_list: List[RunCTRegistrationRequestFloatingList] = None,
    ):
        self.reference_list = reference_list
        self.data_format = data_format
        self.org_name = org_name
        self.org_id = org_id
        self.data_source_type = data_source_type
        self.floating_list = floating_list

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
        result = dict()
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

    def from_map(self, m: dict = None):
        m = m or dict()
        self.reference_list = []
        if m.get('ReferenceList') is not None:
            for k in m.get('ReferenceList'):
                temp_model = RunCTRegistrationRequestReferenceList()
                self.reference_list.append(temp_model.from_map(k))
        if m.get('DataFormat') is not None:
            self.data_format = m.get('DataFormat')
        if m.get('OrgName') is not None:
            self.org_name = m.get('OrgName')
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('DataSourceType') is not None:
            self.data_source_type = m.get('DataSourceType')
        self.floating_list = []
        if m.get('FloatingList') is not None:
            for k in m.get('FloatingList'):
                temp_model = RunCTRegistrationRequestFloatingList()
                self.floating_list.append(temp_model.from_map(k))
        return self


class RunCTRegistrationResponseData(TeaModel):
    def __init__(
        self,
        durl: str = None,
        nurl: str = None,
    ):
        self.durl = durl
        self.nurl = nurl

    def validate(self):
        self.validate_required(self.durl, 'durl')
        self.validate_required(self.nurl, 'nurl')

    def to_map(self):
        result = dict()
        if self.durl is not None:
            result['DUrl'] = self.durl
        if self.nurl is not None:
            result['NUrl'] = self.nurl
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DUrl') is not None:
            self.durl = m.get('DUrl')
        if m.get('NUrl') is not None:
            self.nurl = m.get('NUrl')
        return self


class RunCTRegistrationResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: RunCTRegistrationResponseData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
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
            temp_model = RunCTRegistrationResponseData()
            self.data = temp_model.from_map(m['Data'])
        return self


class DetectHipKeypointXRayRequest(TeaModel):
    def __init__(
        self,
        image_url: str = None,
        data_format: str = None,
        org_id: str = None,
        org_name: str = None,
        tracer_id: str = None,
    ):
        self.image_url = image_url
        self.data_format = data_format
        self.org_id = org_id
        self.org_name = org_name
        self.tracer_id = tracer_id

    def validate(self):
        self.validate_required(self.image_url, 'image_url')
        self.validate_required(self.data_format, 'data_format')
        self.validate_required(self.org_id, 'org_id')
        self.validate_required(self.org_name, 'org_name')

    def to_map(self):
        result = dict()
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        if m.get('DataFormat') is not None:
            self.data_format = m.get('DataFormat')
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('OrgName') is not None:
            self.org_name = m.get('OrgName')
        if m.get('TracerId') is not None:
            self.tracer_id = m.get('TracerId')
        return self


class DetectHipKeypointXRayResponseDataKeyPointsTag(TeaModel):
    def __init__(
        self,
        direction: str = None,
        label: str = None,
    ):
        self.direction = direction
        self.label = label

    def validate(self):
        self.validate_required(self.direction, 'direction')
        self.validate_required(self.label, 'label')

    def to_map(self):
        result = dict()
        if self.direction is not None:
            result['Direction'] = self.direction
        if self.label is not None:
            result['Label'] = self.label
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Direction') is not None:
            self.direction = m.get('Direction')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        return self


class DetectHipKeypointXRayResponseDataKeyPoints(TeaModel):
    def __init__(
        self,
        value: float = None,
        tag: DetectHipKeypointXRayResponseDataKeyPointsTag = None,
        coordinates: List[int] = None,
    ):
        self.value = value
        self.tag = tag
        self.coordinates = coordinates

    def validate(self):
        self.validate_required(self.value, 'value')
        self.validate_required(self.tag, 'tag')
        if self.tag:
            self.tag.validate()
        self.validate_required(self.coordinates, 'coordinates')

    def to_map(self):
        result = dict()
        if self.value is not None:
            result['Value'] = self.value
        if self.tag is not None:
            result['Tag'] = self.tag.to_map()
        if self.coordinates is not None:
            result['Coordinates'] = self.coordinates
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('Tag') is not None:
            temp_model = DetectHipKeypointXRayResponseDataKeyPointsTag()
            self.tag = temp_model.from_map(m['Tag'])
        if m.get('Coordinates') is not None:
            self.coordinates = m.get('Coordinates')
        return self


class DetectHipKeypointXRayResponseData(TeaModel):
    def __init__(
        self,
        image_url: str = None,
        org_id: str = None,
        org_name: str = None,
        key_points: List[DetectHipKeypointXRayResponseDataKeyPoints] = None,
    ):
        self.image_url = image_url
        self.org_id = org_id
        self.org_name = org_name
        self.key_points = key_points

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
        result = dict()
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('OrgName') is not None:
            self.org_name = m.get('OrgName')
        self.key_points = []
        if m.get('KeyPoints') is not None:
            for k in m.get('KeyPoints'):
                temp_model = DetectHipKeypointXRayResponseDataKeyPoints()
                self.key_points.append(temp_model.from_map(k))
        return self


class DetectHipKeypointXRayResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: DetectHipKeypointXRayResponseData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
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
            temp_model = DetectHipKeypointXRayResponseData()
            self.data = temp_model.from_map(m['Data'])
        return self


class DetectHipKeypointXRayAdvanceRequest(TeaModel):
    def __init__(
        self,
        image_url_object: BinaryIO = None,
        data_format: str = None,
        org_id: str = None,
        org_name: str = None,
        tracer_id: str = None,
    ):
        self.image_url_object = image_url_object
        self.data_format = data_format
        self.org_id = org_id
        self.org_name = org_name
        self.tracer_id = tracer_id

    def validate(self):
        self.validate_required(self.image_url_object, 'image_url_object')
        self.validate_required(self.data_format, 'data_format')
        self.validate_required(self.org_id, 'org_id')
        self.validate_required(self.org_name, 'org_name')

    def to_map(self):
        result = dict()
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageUrlObject') is not None:
            self.image_url_object = m.get('ImageUrlObject')
        if m.get('DataFormat') is not None:
            self.data_format = m.get('DataFormat')
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('OrgName') is not None:
            self.org_name = m.get('OrgName')
        if m.get('TracerId') is not None:
            self.tracer_id = m.get('TracerId')
        return self


class CalcCACSRequestURLList(TeaModel):
    def __init__(
        self,
        url: str = None,
    ):
        self.url = url

    def validate(self):
        self.validate_required(self.url, 'url')

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


class CalcCACSRequest(TeaModel):
    def __init__(
        self,
        urllist: List[CalcCACSRequestURLList] = None,
        data_format: str = None,
        org_name: str = None,
        org_id: str = None,
        data_source_type: str = None,
    ):
        self.urllist = urllist
        self.data_format = data_format
        self.org_name = org_name
        self.org_id = org_id
        self.data_source_type = data_source_type

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
        result = dict()
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

    def from_map(self, m: dict = None):
        m = m or dict()
        self.urllist = []
        if m.get('URLList') is not None:
            for k in m.get('URLList'):
                temp_model = CalcCACSRequestURLList()
                self.urllist.append(temp_model.from_map(k))
        if m.get('DataFormat') is not None:
            self.data_format = m.get('DataFormat')
        if m.get('OrgName') is not None:
            self.org_name = m.get('OrgName')
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('DataSourceType') is not None:
            self.data_source_type = m.get('DataSourceType')
        return self


class CalcCACSResponseData(TeaModel):
    def __init__(
        self,
        score: str = None,
        result_url: str = None,
    ):
        self.score = score
        self.result_url = result_url

    def validate(self):
        self.validate_required(self.score, 'score')
        self.validate_required(self.result_url, 'result_url')

    def to_map(self):
        result = dict()
        if self.score is not None:
            result['Score'] = self.score
        if self.result_url is not None:
            result['ResultUrl'] = self.result_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('ResultUrl') is not None:
            self.result_url = m.get('ResultUrl')
        return self


class CalcCACSResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: CalcCACSResponseData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
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
            temp_model = CalcCACSResponseData()
            self.data = temp_model.from_map(m['Data'])
        return self


class DetectKneeXRayRequest(TeaModel):
    def __init__(
        self,
        url: str = None,
        data_format: str = None,
        org_name: str = None,
        org_id: str = None,
    ):
        self.url = url
        self.data_format = data_format
        self.org_name = org_name
        self.org_id = org_id

    def validate(self):
        self.validate_required(self.url, 'url')
        self.validate_required(self.data_format, 'data_format')
        self.validate_required(self.org_name, 'org_name')
        self.validate_required(self.org_id, 'org_id')

    def to_map(self):
        result = dict()
        if self.url is not None:
            result['Url'] = self.url
        if self.data_format is not None:
            result['DataFormat'] = self.data_format
        if self.org_name is not None:
            result['OrgName'] = self.org_name
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('DataFormat') is not None:
            self.data_format = m.get('DataFormat')
        if m.get('OrgName') is not None:
            self.org_name = m.get('OrgName')
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        return self


class DetectKneeXRayResponseDataKLDetections(TeaModel):
    def __init__(
        self,
        detections: List[float] = None,
    ):
        self.detections = detections

    def validate(self):
        self.validate_required(self.detections, 'detections')

    def to_map(self):
        result = dict()
        if self.detections is not None:
            result['Detections'] = self.detections
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Detections') is not None:
            self.detections = m.get('Detections')
        return self


class DetectKneeXRayResponseData(TeaModel):
    def __init__(
        self,
        kldetections: List[DetectKneeXRayResponseDataKLDetections] = None,
    ):
        self.kldetections = kldetections

    def validate(self):
        self.validate_required(self.kldetections, 'kldetections')
        if self.kldetections:
            for k in self.kldetections:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['KLDetections'] = []
        if self.kldetections is not None:
            for k in self.kldetections:
                result['KLDetections'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.kldetections = []
        if m.get('KLDetections') is not None:
            for k in m.get('KLDetections'):
                temp_model = DetectKneeXRayResponseDataKLDetections()
                self.kldetections.append(temp_model.from_map(k))
        return self


class DetectKneeXRayResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: DetectKneeXRayResponseData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
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
            temp_model = DetectKneeXRayResponseData()
            self.data = temp_model.from_map(m['Data'])
        return self


class DetectKneeXRayAdvanceRequest(TeaModel):
    def __init__(
        self,
        url_object: BinaryIO = None,
        data_format: str = None,
        org_name: str = None,
        org_id: str = None,
    ):
        self.url_object = url_object
        self.data_format = data_format
        self.org_name = org_name
        self.org_id = org_id

    def validate(self):
        self.validate_required(self.url_object, 'url_object')
        self.validate_required(self.data_format, 'data_format')
        self.validate_required(self.org_name, 'org_name')
        self.validate_required(self.org_id, 'org_id')

    def to_map(self):
        result = dict()
        if self.url_object is not None:
            result['UrlObject'] = self.url_object
        if self.data_format is not None:
            result['DataFormat'] = self.data_format
        if self.org_name is not None:
            result['OrgName'] = self.org_name
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UrlObject') is not None:
            self.url_object = m.get('UrlObject')
        if m.get('DataFormat') is not None:
            self.data_format = m.get('DataFormat')
        if m.get('OrgName') is not None:
            self.org_name = m.get('OrgName')
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        return self


class DetectSpineMRIRequestURLList(TeaModel):
    def __init__(
        self,
        url: str = None,
    ):
        self.url = url

    def validate(self):
        self.validate_required(self.url, 'url')

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


class DetectSpineMRIRequest(TeaModel):
    def __init__(
        self,
        urllist: List[DetectSpineMRIRequestURLList] = None,
        data_format: str = None,
        org_name: str = None,
        org_id: str = None,
    ):
        self.urllist = urllist
        self.data_format = data_format
        self.org_name = org_name
        self.org_id = org_id

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
        result = dict()
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

    def from_map(self, m: dict = None):
        m = m or dict()
        self.urllist = []
        if m.get('URLList') is not None:
            for k in m.get('URLList'):
                temp_model = DetectSpineMRIRequestURLList()
                self.urllist.append(temp_model.from_map(k))
        if m.get('DataFormat') is not None:
            self.data_format = m.get('DataFormat')
        if m.get('OrgName') is not None:
            self.org_name = m.get('OrgName')
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        return self


class DetectSpineMRIResponseDataDiscs(TeaModel):
    def __init__(
        self,
        disease: str = None,
        identification: str = None,
        location: List[float] = None,
    ):
        self.disease = disease
        self.identification = identification
        self.location = location

    def validate(self):
        self.validate_required(self.disease, 'disease')
        self.validate_required(self.identification, 'identification')
        self.validate_required(self.location, 'location')

    def to_map(self):
        result = dict()
        if self.disease is not None:
            result['Disease'] = self.disease
        if self.identification is not None:
            result['Identification'] = self.identification
        if self.location is not None:
            result['Location'] = self.location
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Disease') is not None:
            self.disease = m.get('Disease')
        if m.get('Identification') is not None:
            self.identification = m.get('Identification')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        return self


class DetectSpineMRIResponseDataVertebras(TeaModel):
    def __init__(
        self,
        disease: str = None,
        identification: str = None,
        location: List[float] = None,
    ):
        self.disease = disease
        self.identification = identification
        self.location = location

    def validate(self):
        self.validate_required(self.disease, 'disease')
        self.validate_required(self.identification, 'identification')
        self.validate_required(self.location, 'location')

    def to_map(self):
        result = dict()
        if self.disease is not None:
            result['Disease'] = self.disease
        if self.identification is not None:
            result['Identification'] = self.identification
        if self.location is not None:
            result['Location'] = self.location
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Disease') is not None:
            self.disease = m.get('Disease')
        if m.get('Identification') is not None:
            self.identification = m.get('Identification')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        return self


class DetectSpineMRIResponseData(TeaModel):
    def __init__(
        self,
        discs: List[DetectSpineMRIResponseDataDiscs] = None,
        vertebras: List[DetectSpineMRIResponseDataVertebras] = None,
    ):
        self.discs = discs
        self.vertebras = vertebras

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
        result = dict()
        result['Discs'] = []
        if self.discs is not None:
            for k in self.discs:
                result['Discs'].append(k.to_map() if k else None)
        result['Vertebras'] = []
        if self.vertebras is not None:
            for k in self.vertebras:
                result['Vertebras'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.discs = []
        if m.get('Discs') is not None:
            for k in m.get('Discs'):
                temp_model = DetectSpineMRIResponseDataDiscs()
                self.discs.append(temp_model.from_map(k))
        self.vertebras = []
        if m.get('Vertebras') is not None:
            for k in m.get('Vertebras'):
                temp_model = DetectSpineMRIResponseDataVertebras()
                self.vertebras.append(temp_model.from_map(k))
        return self


class DetectSpineMRIResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: DetectSpineMRIResponseData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
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
            temp_model = DetectSpineMRIResponseData()
            self.data = temp_model.from_map(m['Data'])
        return self


class TranslateMedRequest(TeaModel):
    def __init__(
        self,
        from_language: str = None,
        to_language: str = None,
        text: str = None,
    ):
        self.from_language = from_language
        self.to_language = to_language
        self.text = text

    def validate(self):
        self.validate_required(self.from_language, 'from_language')
        self.validate_required(self.to_language, 'to_language')
        self.validate_required(self.text, 'text')

    def to_map(self):
        result = dict()
        if self.from_language is not None:
            result['FromLanguage'] = self.from_language
        if self.to_language is not None:
            result['ToLanguage'] = self.to_language
        if self.text is not None:
            result['Text'] = self.text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FromLanguage') is not None:
            self.from_language = m.get('FromLanguage')
        if m.get('ToLanguage') is not None:
            self.to_language = m.get('ToLanguage')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        return self


class TranslateMedResponseData(TeaModel):
    def __init__(
        self,
        text: str = None,
        words: int = None,
    ):
        self.text = text
        self.words = words

    def validate(self):
        self.validate_required(self.text, 'text')
        self.validate_required(self.words, 'words')

    def to_map(self):
        result = dict()
        if self.text is not None:
            result['Text'] = self.text
        if self.words is not None:
            result['Words'] = self.words
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('Words') is not None:
            self.words = m.get('Words')
        return self


class TranslateMedResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: TranslateMedResponseData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
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
            temp_model = TranslateMedResponseData()
            self.data = temp_model.from_map(m['Data'])
        return self


class DetectLungNoduleRequestURLList(TeaModel):
    def __init__(
        self,
        url: str = None,
    ):
        self.url = url

    def validate(self):
        self.validate_required(self.url, 'url')

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


class DetectLungNoduleRequest(TeaModel):
    def __init__(
        self,
        urllist: List[DetectLungNoduleRequestURLList] = None,
        data_format: str = None,
        org_name: str = None,
        org_id: str = None,
    ):
        self.urllist = urllist
        self.data_format = data_format
        self.org_name = org_name
        self.org_id = org_id

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
        result = dict()
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

    def from_map(self, m: dict = None):
        m = m or dict()
        self.urllist = []
        if m.get('URLList') is not None:
            for k in m.get('URLList'):
                temp_model = DetectLungNoduleRequestURLList()
                self.urllist.append(temp_model.from_map(k))
        if m.get('DataFormat') is not None:
            self.data_format = m.get('DataFormat')
        if m.get('OrgName') is not None:
            self.org_name = m.get('OrgName')
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        return self


class DetectLungNoduleResponseDataSeriesElements(TeaModel):
    def __init__(
        self,
        category: str = None,
        confidence: float = None,
        diameter: float = None,
        lobe: str = None,
        lung: str = None,
        x: float = None,
        z: float = None,
        y: float = None,
        image_x: float = None,
        image_y: float = None,
        image_z: float = None,
        sopinstance_uid: str = None,
        volume: float = None,
        mean_value: float = None,
    ):
        self.category = category
        self.confidence = confidence
        self.diameter = diameter
        self.lobe = lobe
        self.lung = lung
        self.x = x
        self.z = z
        self.y = y
        self.image_x = image_x
        self.image_y = image_y
        self.image_z = image_z
        self.sopinstance_uid = sopinstance_uid
        self.volume = volume
        self.mean_value = mean_value

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
        result = dict()
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Confidence') is not None:
            self.confidence = m.get('Confidence')
        if m.get('Diameter') is not None:
            self.diameter = m.get('Diameter')
        if m.get('Lobe') is not None:
            self.lobe = m.get('Lobe')
        if m.get('Lung') is not None:
            self.lung = m.get('Lung')
        if m.get('X') is not None:
            self.x = m.get('X')
        if m.get('Z') is not None:
            self.z = m.get('Z')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        if m.get('ImageX') is not None:
            self.image_x = m.get('ImageX')
        if m.get('ImageY') is not None:
            self.image_y = m.get('ImageY')
        if m.get('ImageZ') is not None:
            self.image_z = m.get('ImageZ')
        if m.get('SOPInstanceUID') is not None:
            self.sopinstance_uid = m.get('SOPInstanceUID')
        if m.get('Volume') is not None:
            self.volume = m.get('Volume')
        if m.get('MeanValue') is not None:
            self.mean_value = m.get('MeanValue')
        return self


class DetectLungNoduleResponseDataSeries(TeaModel):
    def __init__(
        self,
        series_instance_uid: str = None,
        report: str = None,
        elements: List[DetectLungNoduleResponseDataSeriesElements] = None,
        origin: List[float] = None,
        spacing: List[float] = None,
    ):
        self.series_instance_uid = series_instance_uid
        self.report = report
        self.elements = elements
        self.origin = origin
        self.spacing = spacing

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
        result = dict()
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SeriesInstanceUid') is not None:
            self.series_instance_uid = m.get('SeriesInstanceUid')
        if m.get('Report') is not None:
            self.report = m.get('Report')
        self.elements = []
        if m.get('Elements') is not None:
            for k in m.get('Elements'):
                temp_model = DetectLungNoduleResponseDataSeriesElements()
                self.elements.append(temp_model.from_map(k))
        if m.get('Origin') is not None:
            self.origin = m.get('Origin')
        if m.get('Spacing') is not None:
            self.spacing = m.get('Spacing')
        return self


class DetectLungNoduleResponseData(TeaModel):
    def __init__(
        self,
        series: List[DetectLungNoduleResponseDataSeries] = None,
    ):
        self.series = series

    def validate(self):
        self.validate_required(self.series, 'series')
        if self.series:
            for k in self.series:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Series'] = []
        if self.series is not None:
            for k in self.series:
                result['Series'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.series = []
        if m.get('Series') is not None:
            for k in m.get('Series'):
                temp_model = DetectLungNoduleResponseDataSeries()
                self.series.append(temp_model.from_map(k))
        return self


class DetectLungNoduleResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: DetectLungNoduleResponseData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
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
            temp_model = DetectLungNoduleResponseData()
            self.data = temp_model.from_map(m['Data'])
        return self


class DetectCovid19CadRequestURLList(TeaModel):
    def __init__(
        self,
        url: str = None,
    ):
        self.url = url

    def validate(self):
        self.validate_required(self.url, 'url')

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


class DetectCovid19CadRequest(TeaModel):
    def __init__(
        self,
        urllist: List[DetectCovid19CadRequestURLList] = None,
        data_format: str = None,
        org_name: str = None,
        org_id: str = None,
    ):
        self.urllist = urllist
        self.data_format = data_format
        self.org_name = org_name
        self.org_id = org_id

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
        result = dict()
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

    def from_map(self, m: dict = None):
        m = m or dict()
        self.urllist = []
        if m.get('URLList') is not None:
            for k in m.get('URLList'):
                temp_model = DetectCovid19CadRequestURLList()
                self.urllist.append(temp_model.from_map(k))
        if m.get('DataFormat') is not None:
            self.data_format = m.get('DataFormat')
        if m.get('OrgName') is not None:
            self.org_name = m.get('OrgName')
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        return self


class DetectCovid19CadResponseData(TeaModel):
    def __init__(
        self,
        new_probability: str = None,
        normal_probability: str = None,
        other_probability: str = None,
        lesion_ratio: str = None,
        mask: str = None,
    ):
        self.new_probability = new_probability
        self.normal_probability = normal_probability
        self.other_probability = other_probability
        self.lesion_ratio = lesion_ratio
        self.mask = mask

    def validate(self):
        self.validate_required(self.new_probability, 'new_probability')
        self.validate_required(self.normal_probability, 'normal_probability')
        self.validate_required(self.other_probability, 'other_probability')
        self.validate_required(self.lesion_ratio, 'lesion_ratio')
        self.validate_required(self.mask, 'mask')

    def to_map(self):
        result = dict()
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NewProbability') is not None:
            self.new_probability = m.get('NewProbability')
        if m.get('NormalProbability') is not None:
            self.normal_probability = m.get('NormalProbability')
        if m.get('OtherProbability') is not None:
            self.other_probability = m.get('OtherProbability')
        if m.get('LesionRatio') is not None:
            self.lesion_ratio = m.get('LesionRatio')
        if m.get('Mask') is not None:
            self.mask = m.get('Mask')
        return self


class DetectCovid19CadResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: DetectCovid19CadResponseData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
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
            temp_model = DetectCovid19CadResponseData()
            self.data = temp_model.from_map(m['Data'])
        return self


class GetAsyncJobResultRequest(TeaModel):
    def __init__(
        self,
        job_id: str = None,
    ):
        self.job_id = job_id

    def validate(self):
        self.validate_required(self.job_id, 'job_id')

    def to_map(self):
        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class GetAsyncJobResultResponseData(TeaModel):
    def __init__(
        self,
        job_id: str = None,
        status: str = None,
        result: str = None,
        error_code: str = None,
        error_message: str = None,
    ):
        self.job_id = job_id
        self.status = status
        self.result = result
        self.error_code = error_code
        self.error_message = error_message

    def validate(self):
        self.validate_required(self.job_id, 'job_id')
        self.validate_required(self.status, 'status')
        self.validate_required(self.result, 'result')
        self.validate_required(self.error_code, 'error_code')
        self.validate_required(self.error_message, 'error_message')

    def to_map(self):
        result = dict()
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        return self


class GetAsyncJobResultResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: GetAsyncJobResultResponseData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
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
            temp_model = GetAsyncJobResultResponseData()
            self.data = temp_model.from_map(m['Data'])
        return self


