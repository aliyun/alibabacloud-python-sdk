# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import BinaryIO, List, Dict, Any


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
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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


class ClassifyFNFResponseBodyDataFracturesTag(TeaModel):
    def __init__(
        self,
        label: str = None,
    ):
        self.label = label

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label is not None:
            result['Label'] = self.label
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Label') is not None:
            self.label = m.get('Label')
        return self


class ClassifyFNFResponseBodyDataFractures(TeaModel):
    def __init__(
        self,
        value: float = None,
        boxes: List[int] = None,
        tag: ClassifyFNFResponseBodyDataFracturesTag = None,
    ):
        self.value = value
        self.boxes = boxes
        self.tag = tag

    def validate(self):
        if self.tag:
            self.tag.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.value is not None:
            result['Value'] = self.value
        if self.boxes is not None:
            result['Boxes'] = self.boxes
        if self.tag is not None:
            result['Tag'] = self.tag.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('Boxes') is not None:
            self.boxes = m.get('Boxes')
        if m.get('Tag') is not None:
            temp_model = ClassifyFNFResponseBodyDataFracturesTag()
            self.tag = temp_model.from_map(m['Tag'])
        return self


class ClassifyFNFResponseBodyData(TeaModel):
    def __init__(
        self,
        fractures: List[ClassifyFNFResponseBodyDataFractures] = None,
        image_url: str = None,
        org_id: str = None,
        org_name: str = None,
    ):
        self.fractures = fractures
        self.image_url = image_url
        self.org_id = org_id
        self.org_name = org_name

    def validate(self):
        if self.fractures:
            for k in self.fractures:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Fractures'] = []
        if self.fractures is not None:
            for k in self.fractures:
                result['Fractures'].append(k.to_map() if k else None)
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.org_name is not None:
            result['OrgName'] = self.org_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.fractures = []
        if m.get('Fractures') is not None:
            for k in m.get('Fractures'):
                temp_model = ClassifyFNFResponseBodyDataFractures()
                self.fractures.append(temp_model.from_map(k))
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('OrgName') is not None:
            self.org_name = m.get('OrgName')
        return self


class ClassifyFNFResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: ClassifyFNFResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = ClassifyFNFResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class ClassifyFNFResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ClassifyFNFResponseBody = None,
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
            temp_model = ClassifyFNFResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetectLungNoduleRequestURLList(TeaModel):
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
        data_format: str = None,
        org_name: str = None,
        org_id: str = None,
        urllist: List[DetectLungNoduleRequestURLList] = None,
        threshold: float = None,
    ):
        self.data_format = data_format
        self.org_name = org_name
        self.org_id = org_id
        self.urllist = urllist
        self.threshold = threshold

    def validate(self):
        if self.urllist:
            for k in self.urllist:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        if self.threshold is not None:
            result['Threshold'] = self.threshold
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
                temp_model = DetectLungNoduleRequestURLList()
                self.urllist.append(temp_model.from_map(k))
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        return self


class DetectLungNoduleResponseBodyDataSeriesElements(TeaModel):
    def __init__(
        self,
        z: float = None,
        lobe: str = None,
        mean_value: float = None,
        image_z: float = None,
        lung: str = None,
        confidence: float = None,
        sopinstance_uid: str = None,
        image_x: float = None,
        y: float = None,
        category: str = None,
        volume: float = None,
        image_y: float = None,
        diameter: float = None,
        x: float = None,
    ):
        self.z = z
        self.lobe = lobe
        self.mean_value = mean_value
        self.image_z = image_z
        self.lung = lung
        self.confidence = confidence
        self.sopinstance_uid = sopinstance_uid
        self.image_x = image_x
        self.y = y
        self.category = category
        self.volume = volume
        self.image_y = image_y
        self.diameter = diameter
        self.x = x

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.z is not None:
            result['Z'] = self.z
        if self.lobe is not None:
            result['Lobe'] = self.lobe
        if self.mean_value is not None:
            result['MeanValue'] = self.mean_value
        if self.image_z is not None:
            result['ImageZ'] = self.image_z
        if self.lung is not None:
            result['Lung'] = self.lung
        if self.confidence is not None:
            result['Confidence'] = self.confidence
        if self.sopinstance_uid is not None:
            result['SOPInstanceUID'] = self.sopinstance_uid
        if self.image_x is not None:
            result['ImageX'] = self.image_x
        if self.y is not None:
            result['Y'] = self.y
        if self.category is not None:
            result['Category'] = self.category
        if self.volume is not None:
            result['Volume'] = self.volume
        if self.image_y is not None:
            result['ImageY'] = self.image_y
        if self.diameter is not None:
            result['Diameter'] = self.diameter
        if self.x is not None:
            result['X'] = self.x
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Z') is not None:
            self.z = m.get('Z')
        if m.get('Lobe') is not None:
            self.lobe = m.get('Lobe')
        if m.get('MeanValue') is not None:
            self.mean_value = m.get('MeanValue')
        if m.get('ImageZ') is not None:
            self.image_z = m.get('ImageZ')
        if m.get('Lung') is not None:
            self.lung = m.get('Lung')
        if m.get('Confidence') is not None:
            self.confidence = m.get('Confidence')
        if m.get('SOPInstanceUID') is not None:
            self.sopinstance_uid = m.get('SOPInstanceUID')
        if m.get('ImageX') is not None:
            self.image_x = m.get('ImageX')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Volume') is not None:
            self.volume = m.get('Volume')
        if m.get('ImageY') is not None:
            self.image_y = m.get('ImageY')
        if m.get('Diameter') is not None:
            self.diameter = m.get('Diameter')
        if m.get('X') is not None:
            self.x = m.get('X')
        return self


class DetectLungNoduleResponseBodyDataSeries(TeaModel):
    def __init__(
        self,
        series_instance_uid: str = None,
        elements: List[DetectLungNoduleResponseBodyDataSeriesElements] = None,
        origin: List[float] = None,
        report: str = None,
        spacing: List[float] = None,
    ):
        self.series_instance_uid = series_instance_uid
        self.elements = elements
        self.origin = origin
        self.report = report
        self.spacing = spacing

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
        if self.series_instance_uid is not None:
            result['SeriesInstanceUid'] = self.series_instance_uid
        result['Elements'] = []
        if self.elements is not None:
            for k in self.elements:
                result['Elements'].append(k.to_map() if k else None)
        if self.origin is not None:
            result['Origin'] = self.origin
        if self.report is not None:
            result['Report'] = self.report
        if self.spacing is not None:
            result['Spacing'] = self.spacing
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SeriesInstanceUid') is not None:
            self.series_instance_uid = m.get('SeriesInstanceUid')
        self.elements = []
        if m.get('Elements') is not None:
            for k in m.get('Elements'):
                temp_model = DetectLungNoduleResponseBodyDataSeriesElements()
                self.elements.append(temp_model.from_map(k))
        if m.get('Origin') is not None:
            self.origin = m.get('Origin')
        if m.get('Report') is not None:
            self.report = m.get('Report')
        if m.get('Spacing') is not None:
            self.spacing = m.get('Spacing')
        return self


class DetectLungNoduleResponseBodyData(TeaModel):
    def __init__(
        self,
        series: List[DetectLungNoduleResponseBodyDataSeries] = None,
    ):
        self.series = series

    def validate(self):
        if self.series:
            for k in self.series:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
                temp_model = DetectLungNoduleResponseBodyDataSeries()
                self.series.append(temp_model.from_map(k))
        return self


class DetectLungNoduleResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: DetectLungNoduleResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = DetectLungNoduleResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class DetectLungNoduleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DetectLungNoduleResponseBody = None,
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
            temp_model = DetectLungNoduleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RunCTRegistrationRequestReferenceList(TeaModel):
    def __init__(
        self,
        reference_url: str = None,
    ):
        self.reference_url = reference_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        data_format: str = None,
        org_name: str = None,
        org_id: str = None,
        data_source_type: str = None,
        reference_list: List[RunCTRegistrationRequestReferenceList] = None,
        floating_list: List[RunCTRegistrationRequestFloatingList] = None,
    ):
        self.data_format = data_format
        self.org_name = org_name
        self.org_id = org_id
        self.data_source_type = data_source_type
        self.reference_list = reference_list
        self.floating_list = floating_list

    def validate(self):
        if self.reference_list:
            for k in self.reference_list:
                if k:
                    k.validate()
        if self.floating_list:
            for k in self.floating_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_format is not None:
            result['DataFormat'] = self.data_format
        if self.org_name is not None:
            result['OrgName'] = self.org_name
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.data_source_type is not None:
            result['DataSourceType'] = self.data_source_type
        result['ReferenceList'] = []
        if self.reference_list is not None:
            for k in self.reference_list:
                result['ReferenceList'].append(k.to_map() if k else None)
        result['FloatingList'] = []
        if self.floating_list is not None:
            for k in self.floating_list:
                result['FloatingList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataFormat') is not None:
            self.data_format = m.get('DataFormat')
        if m.get('OrgName') is not None:
            self.org_name = m.get('OrgName')
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('DataSourceType') is not None:
            self.data_source_type = m.get('DataSourceType')
        self.reference_list = []
        if m.get('ReferenceList') is not None:
            for k in m.get('ReferenceList'):
                temp_model = RunCTRegistrationRequestReferenceList()
                self.reference_list.append(temp_model.from_map(k))
        self.floating_list = []
        if m.get('FloatingList') is not None:
            for k in m.get('FloatingList'):
                temp_model = RunCTRegistrationRequestFloatingList()
                self.floating_list.append(temp_model.from_map(k))
        return self


class RunCTRegistrationResponseBodyData(TeaModel):
    def __init__(
        self,
        durl: str = None,
        nurl: str = None,
    ):
        self.durl = durl
        self.nurl = nurl

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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


class RunCTRegistrationResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: RunCTRegistrationResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = RunCTRegistrationResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class RunCTRegistrationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RunCTRegistrationResponseBody = None,
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
            temp_model = RunCTRegistrationResponseBody()
            self.body = temp_model.from_map(m['body'])
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
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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


class TranslateMedResponseBodyData(TeaModel):
    def __init__(
        self,
        words: int = None,
        text: str = None,
    ):
        self.words = words
        self.text = text

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.words is not None:
            result['Words'] = self.words
        if self.text is not None:
            result['Text'] = self.text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Words') is not None:
            self.words = m.get('Words')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        return self


class TranslateMedResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: TranslateMedResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = TranslateMedResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class TranslateMedResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: TranslateMedResponseBody = None,
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
            temp_model = TranslateMedResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetectSpineMRIRequestURLList(TeaModel):
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
        data_format: str = None,
        org_name: str = None,
        org_id: str = None,
        urllist: List[DetectSpineMRIRequestURLList] = None,
    ):
        self.data_format = data_format
        self.org_name = org_name
        self.org_id = org_id
        self.urllist = urllist

    def validate(self):
        if self.urllist:
            for k in self.urllist:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
                temp_model = DetectSpineMRIRequestURLList()
                self.urllist.append(temp_model.from_map(k))
        return self


class DetectSpineMRIResponseBodyDataDiscs(TeaModel):
    def __init__(
        self,
        identification: str = None,
        disease: str = None,
        location: List[float] = None,
    ):
        self.identification = identification
        self.disease = disease
        self.location = location

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.identification is not None:
            result['Identification'] = self.identification
        if self.disease is not None:
            result['Disease'] = self.disease
        if self.location is not None:
            result['Location'] = self.location
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Identification') is not None:
            self.identification = m.get('Identification')
        if m.get('Disease') is not None:
            self.disease = m.get('Disease')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        return self


class DetectSpineMRIResponseBodyDataVertebras(TeaModel):
    def __init__(
        self,
        identification: str = None,
        disease: str = None,
        location: List[float] = None,
    ):
        self.identification = identification
        self.disease = disease
        self.location = location

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.identification is not None:
            result['Identification'] = self.identification
        if self.disease is not None:
            result['Disease'] = self.disease
        if self.location is not None:
            result['Location'] = self.location
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Identification') is not None:
            self.identification = m.get('Identification')
        if m.get('Disease') is not None:
            self.disease = m.get('Disease')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        return self


class DetectSpineMRIResponseBodyData(TeaModel):
    def __init__(
        self,
        discs: List[DetectSpineMRIResponseBodyDataDiscs] = None,
        vertebras: List[DetectSpineMRIResponseBodyDataVertebras] = None,
    ):
        self.discs = discs
        self.vertebras = vertebras

    def validate(self):
        if self.discs:
            for k in self.discs:
                if k:
                    k.validate()
        if self.vertebras:
            for k in self.vertebras:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
                temp_model = DetectSpineMRIResponseBodyDataDiscs()
                self.discs.append(temp_model.from_map(k))
        self.vertebras = []
        if m.get('Vertebras') is not None:
            for k in m.get('Vertebras'):
                temp_model = DetectSpineMRIResponseBodyDataVertebras()
                self.vertebras.append(temp_model.from_map(k))
        return self


class DetectSpineMRIResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: DetectSpineMRIResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = DetectSpineMRIResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class DetectSpineMRIResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DetectSpineMRIResponseBody = None,
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
            temp_model = DetectSpineMRIResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CalcCACSRequestURLList(TeaModel):
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
        data_format: str = None,
        org_name: str = None,
        org_id: str = None,
        data_source_type: str = None,
        urllist: List[CalcCACSRequestURLList] = None,
    ):
        self.data_format = data_format
        self.org_name = org_name
        self.org_id = org_id
        self.data_source_type = data_source_type
        self.urllist = urllist

    def validate(self):
        if self.urllist:
            for k in self.urllist:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_format is not None:
            result['DataFormat'] = self.data_format
        if self.org_name is not None:
            result['OrgName'] = self.org_name
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.data_source_type is not None:
            result['DataSourceType'] = self.data_source_type
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
        if m.get('DataSourceType') is not None:
            self.data_source_type = m.get('DataSourceType')
        self.urllist = []
        if m.get('URLList') is not None:
            for k in m.get('URLList'):
                temp_model = CalcCACSRequestURLList()
                self.urllist.append(temp_model.from_map(k))
        return self


class CalcCACSResponseBodyData(TeaModel):
    def __init__(
        self,
        result_url: str = None,
        score: str = None,
    ):
        self.result_url = result_url
        self.score = score

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result_url is not None:
            result['ResultUrl'] = self.result_url
        if self.score is not None:
            result['Score'] = self.score
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResultUrl') is not None:
            self.result_url = m.get('ResultUrl')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        return self


class CalcCACSResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: CalcCACSResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = CalcCACSResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class CalcCACSResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CalcCACSResponseBody = None,
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
            temp_model = CalcCACSResponseBody()
            self.body = temp_model.from_map(m['body'])
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
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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


class DetectHipKeypointXRayResponseBodyDataKeyPointsTag(TeaModel):
    def __init__(
        self,
        direction: str = None,
        label: str = None,
    ):
        self.direction = direction
        self.label = label

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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


class DetectHipKeypointXRayResponseBodyDataKeyPoints(TeaModel):
    def __init__(
        self,
        value: float = None,
        coordinates: List[int] = None,
        tag: DetectHipKeypointXRayResponseBodyDataKeyPointsTag = None,
    ):
        self.value = value
        self.coordinates = coordinates
        self.tag = tag

    def validate(self):
        if self.tag:
            self.tag.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.value is not None:
            result['Value'] = self.value
        if self.coordinates is not None:
            result['Coordinates'] = self.coordinates
        if self.tag is not None:
            result['Tag'] = self.tag.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('Coordinates') is not None:
            self.coordinates = m.get('Coordinates')
        if m.get('Tag') is not None:
            temp_model = DetectHipKeypointXRayResponseBodyDataKeyPointsTag()
            self.tag = temp_model.from_map(m['Tag'])
        return self


class DetectHipKeypointXRayResponseBodyData(TeaModel):
    def __init__(
        self,
        key_points: List[DetectHipKeypointXRayResponseBodyDataKeyPoints] = None,
        image_url: str = None,
        org_id: str = None,
        org_name: str = None,
    ):
        self.key_points = key_points
        self.image_url = image_url
        self.org_id = org_id
        self.org_name = org_name

    def validate(self):
        if self.key_points:
            for k in self.key_points:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['KeyPoints'] = []
        if self.key_points is not None:
            for k in self.key_points:
                result['KeyPoints'].append(k.to_map() if k else None)
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.org_name is not None:
            result['OrgName'] = self.org_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.key_points = []
        if m.get('KeyPoints') is not None:
            for k in m.get('KeyPoints'):
                temp_model = DetectHipKeypointXRayResponseBodyDataKeyPoints()
                self.key_points.append(temp_model.from_map(k))
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('OrgName') is not None:
            self.org_name = m.get('OrgName')
        return self


class DetectHipKeypointXRayResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: DetectHipKeypointXRayResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = DetectHipKeypointXRayResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class DetectHipKeypointXRayResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DetectHipKeypointXRayResponseBody = None,
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
            temp_model = DetectHipKeypointXRayResponseBody()
            self.body = temp_model.from_map(m['body'])
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
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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


class DetectKneeKeypointXRayResponseBodyDataKeyPointsTag(TeaModel):
    def __init__(
        self,
        direction: str = None,
        label: str = None,
    ):
        self.direction = direction
        self.label = label

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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


class DetectKneeKeypointXRayResponseBodyDataKeyPoints(TeaModel):
    def __init__(
        self,
        value: float = None,
        coordinates: List[int] = None,
        tag: DetectKneeKeypointXRayResponseBodyDataKeyPointsTag = None,
    ):
        self.value = value
        self.coordinates = coordinates
        self.tag = tag

    def validate(self):
        if self.tag:
            self.tag.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.value is not None:
            result['Value'] = self.value
        if self.coordinates is not None:
            result['Coordinates'] = self.coordinates
        if self.tag is not None:
            result['Tag'] = self.tag.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('Coordinates') is not None:
            self.coordinates = m.get('Coordinates')
        if m.get('Tag') is not None:
            temp_model = DetectKneeKeypointXRayResponseBodyDataKeyPointsTag()
            self.tag = temp_model.from_map(m['Tag'])
        return self


class DetectKneeKeypointXRayResponseBodyData(TeaModel):
    def __init__(
        self,
        key_points: List[DetectKneeKeypointXRayResponseBodyDataKeyPoints] = None,
        image_url: str = None,
        org_id: str = None,
        org_name: str = None,
    ):
        self.key_points = key_points
        self.image_url = image_url
        self.org_id = org_id
        self.org_name = org_name

    def validate(self):
        if self.key_points:
            for k in self.key_points:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['KeyPoints'] = []
        if self.key_points is not None:
            for k in self.key_points:
                result['KeyPoints'].append(k.to_map() if k else None)
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.org_name is not None:
            result['OrgName'] = self.org_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.key_points = []
        if m.get('KeyPoints') is not None:
            for k in m.get('KeyPoints'):
                temp_model = DetectKneeKeypointXRayResponseBodyDataKeyPoints()
                self.key_points.append(temp_model.from_map(k))
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('OrgName') is not None:
            self.org_name = m.get('OrgName')
        return self


class DetectKneeKeypointXRayResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: DetectKneeKeypointXRayResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = DetectKneeKeypointXRayResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class DetectKneeKeypointXRayResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DetectKneeKeypointXRayResponseBody = None,
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
            temp_model = DetectKneeKeypointXRayResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RunMedQARequestAnswerImageURLList(TeaModel):
    def __init__(
        self,
        answer_image_url: str = None,
    ):
        self.answer_image_url = answer_image_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.answer_image_url is not None:
            result['AnswerImageURL'] = self.answer_image_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AnswerImageURL') is not None:
            self.answer_image_url = m.get('AnswerImageURL')
        return self


class RunMedQARequestAnswerImageDataList(TeaModel):
    def __init__(
        self,
        answer_image_data: bytes = None,
    ):
        self.answer_image_data = answer_image_data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.answer_image_data is not None:
            result['AnswerImageData'] = self.answer_image_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AnswerImageData') is not None:
            self.answer_image_data = m.get('AnswerImageData')
        return self


class RunMedQARequestAnswerTextList(TeaModel):
    def __init__(
        self,
        answer_text: str = None,
    ):
        self.answer_text = answer_text

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.answer_text is not None:
            result['AnswerText'] = self.answer_text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AnswerText') is not None:
            self.answer_text = m.get('AnswerText')
        return self


class RunMedQARequest(TeaModel):
    def __init__(
        self,
        org_id: str = None,
        org_name: str = None,
        session_id: str = None,
        department: str = None,
        question_type: str = None,
        answer_image_urllist: List[RunMedQARequestAnswerImageURLList] = None,
        answer_image_data_list: List[RunMedQARequestAnswerImageDataList] = None,
        answer_text_list: List[RunMedQARequestAnswerTextList] = None,
    ):
        self.org_id = org_id
        self.org_name = org_name
        self.session_id = session_id
        self.department = department
        self.question_type = question_type
        self.answer_image_urllist = answer_image_urllist
        self.answer_image_data_list = answer_image_data_list
        self.answer_text_list = answer_text_list

    def validate(self):
        if self.answer_image_urllist:
            for k in self.answer_image_urllist:
                if k:
                    k.validate()
        if self.answer_image_data_list:
            for k in self.answer_image_data_list:
                if k:
                    k.validate()
        if self.answer_text_list:
            for k in self.answer_text_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.org_name is not None:
            result['OrgName'] = self.org_name
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.department is not None:
            result['Department'] = self.department
        if self.question_type is not None:
            result['QuestionType'] = self.question_type
        result['AnswerImageURLList'] = []
        if self.answer_image_urllist is not None:
            for k in self.answer_image_urllist:
                result['AnswerImageURLList'].append(k.to_map() if k else None)
        result['AnswerImageDataList'] = []
        if self.answer_image_data_list is not None:
            for k in self.answer_image_data_list:
                result['AnswerImageDataList'].append(k.to_map() if k else None)
        result['AnswerTextList'] = []
        if self.answer_text_list is not None:
            for k in self.answer_text_list:
                result['AnswerTextList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('OrgName') is not None:
            self.org_name = m.get('OrgName')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('Department') is not None:
            self.department = m.get('Department')
        if m.get('QuestionType') is not None:
            self.question_type = m.get('QuestionType')
        self.answer_image_urllist = []
        if m.get('AnswerImageURLList') is not None:
            for k in m.get('AnswerImageURLList'):
                temp_model = RunMedQARequestAnswerImageURLList()
                self.answer_image_urllist.append(temp_model.from_map(k))
        self.answer_image_data_list = []
        if m.get('AnswerImageDataList') is not None:
            for k in m.get('AnswerImageDataList'):
                temp_model = RunMedQARequestAnswerImageDataList()
                self.answer_image_data_list.append(temp_model.from_map(k))
        self.answer_text_list = []
        if m.get('AnswerTextList') is not None:
            for k in m.get('AnswerTextList'):
                temp_model = RunMedQARequestAnswerTextList()
                self.answer_text_list.append(temp_model.from_map(k))
        return self


class RunMedQAResponseBodyData(TeaModel):
    def __init__(
        self,
        session_id: str = None,
        question_type: str = None,
        question: str = None,
        answer_type: str = None,
        options: List[str] = None,
        reports: Dict[str, str] = None,
    ):
        self.session_id = session_id
        self.question_type = question_type
        self.question = question
        self.answer_type = answer_type
        self.options = options
        self.reports = reports

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.question_type is not None:
            result['QuestionType'] = self.question_type
        if self.question is not None:
            result['Question'] = self.question
        if self.answer_type is not None:
            result['AnswerType'] = self.answer_type
        if self.options is not None:
            result['Options'] = self.options
        if self.reports is not None:
            result['Reports'] = self.reports
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('QuestionType') is not None:
            self.question_type = m.get('QuestionType')
        if m.get('Question') is not None:
            self.question = m.get('Question')
        if m.get('AnswerType') is not None:
            self.answer_type = m.get('AnswerType')
        if m.get('Options') is not None:
            self.options = m.get('Options')
        if m.get('Reports') is not None:
            self.reports = m.get('Reports')
        return self


class RunMedQAResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: RunMedQAResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = RunMedQAResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class RunMedQAResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RunMedQAResponseBody = None,
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
            temp_model = RunMedQAResponseBody()
            self.body = temp_model.from_map(m['body'])
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
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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


class DetectKneeXRayResponseBodyDataKLDetections(TeaModel):
    def __init__(
        self,
        detections: List[float] = None,
    ):
        self.detections = detections

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.detections is not None:
            result['Detections'] = self.detections
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Detections') is not None:
            self.detections = m.get('Detections')
        return self


class DetectKneeXRayResponseBodyData(TeaModel):
    def __init__(
        self,
        kldetections: List[DetectKneeXRayResponseBodyDataKLDetections] = None,
    ):
        self.kldetections = kldetections

    def validate(self):
        if self.kldetections:
            for k in self.kldetections:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
                temp_model = DetectKneeXRayResponseBodyDataKLDetections()
                self.kldetections.append(temp_model.from_map(k))
        return self


class DetectKneeXRayResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: DetectKneeXRayResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = DetectKneeXRayResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class DetectKneeXRayResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DetectKneeXRayResponseBody = None,
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
            temp_model = DetectKneeXRayResponseBody()
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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


class DetectRibFractureRequestURLList(TeaModel):
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
        data_format: str = None,
        org_name: str = None,
        org_id: str = None,
        source_type: str = None,
        urllist: List[DetectRibFractureRequestURLList] = None,
    ):
        self.data_format = data_format
        self.org_name = org_name
        self.org_id = org_id
        self.source_type = source_type
        self.urllist = urllist

    def validate(self):
        if self.urllist:
            for k in self.urllist:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_format is not None:
            result['DataFormat'] = self.data_format
        if self.org_name is not None:
            result['OrgName'] = self.org_name
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.source_type is not None:
            result['SourceType'] = self.source_type
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
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        self.urllist = []
        if m.get('URLList') is not None:
            for k in m.get('URLList'):
                temp_model = DetectRibFractureRequestURLList()
                self.urllist.append(temp_model.from_map(k))
        return self


class DetectRibFractureResponseBodyDataDetections(TeaModel):
    def __init__(
        self,
        coordinates: List[int] = None,
        fracture_id: int = None,
        coordinate_image: List[int] = None,
        fracture_confidence: float = None,
        fracture_category: str = None,
        fracture_location: str = None,
        fracture_segment: int = None,
    ):
        self.coordinates = coordinates
        self.fracture_id = fracture_id
        self.coordinate_image = coordinate_image
        self.fracture_confidence = fracture_confidence
        self.fracture_category = fracture_category
        self.fracture_location = fracture_location
        self.fracture_segment = fracture_segment

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.coordinates is not None:
            result['Coordinates'] = self.coordinates
        if self.fracture_id is not None:
            result['FractureId'] = self.fracture_id
        if self.coordinate_image is not None:
            result['CoordinateImage'] = self.coordinate_image
        if self.fracture_confidence is not None:
            result['FractureConfidence'] = self.fracture_confidence
        if self.fracture_category is not None:
            result['FractureCategory'] = self.fracture_category
        if self.fracture_location is not None:
            result['FractureLocation'] = self.fracture_location
        if self.fracture_segment is not None:
            result['FractureSegment'] = self.fracture_segment
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Coordinates') is not None:
            self.coordinates = m.get('Coordinates')
        if m.get('FractureId') is not None:
            self.fracture_id = m.get('FractureId')
        if m.get('CoordinateImage') is not None:
            self.coordinate_image = m.get('CoordinateImage')
        if m.get('FractureConfidence') is not None:
            self.fracture_confidence = m.get('FractureConfidence')
        if m.get('FractureCategory') is not None:
            self.fracture_category = m.get('FractureCategory')
        if m.get('FractureLocation') is not None:
            self.fracture_location = m.get('FractureLocation')
        if m.get('FractureSegment') is not None:
            self.fracture_segment = m.get('FractureSegment')
        return self


class DetectRibFractureResponseBodyData(TeaModel):
    def __init__(
        self,
        detections: List[DetectRibFractureResponseBodyDataDetections] = None,
        origin: List[float] = None,
        result_url: str = None,
        spacing: List[float] = None,
    ):
        self.detections = detections
        self.origin = origin
        self.result_url = result_url
        self.spacing = spacing

    def validate(self):
        if self.detections:
            for k in self.detections:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Detections'] = []
        if self.detections is not None:
            for k in self.detections:
                result['Detections'].append(k.to_map() if k else None)
        if self.origin is not None:
            result['Origin'] = self.origin
        if self.result_url is not None:
            result['ResultURL'] = self.result_url
        if self.spacing is not None:
            result['Spacing'] = self.spacing
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.detections = []
        if m.get('Detections') is not None:
            for k in m.get('Detections'):
                temp_model = DetectRibFractureResponseBodyDataDetections()
                self.detections.append(temp_model.from_map(k))
        if m.get('Origin') is not None:
            self.origin = m.get('Origin')
        if m.get('ResultURL') is not None:
            self.result_url = m.get('ResultURL')
        if m.get('Spacing') is not None:
            self.spacing = m.get('Spacing')
        return self


class DetectRibFractureResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: DetectRibFractureResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = DetectRibFractureResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class DetectRibFractureResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DetectRibFractureResponseBody = None,
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
            temp_model = DetectRibFractureResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetectCovid19CadRequestURLList(TeaModel):
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
        data_format: str = None,
        org_name: str = None,
        org_id: str = None,
        urllist: List[DetectCovid19CadRequestURLList] = None,
    ):
        self.data_format = data_format
        self.org_name = org_name
        self.org_id = org_id
        self.urllist = urllist

    def validate(self):
        if self.urllist:
            for k in self.urllist:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
                temp_model = DetectCovid19CadRequestURLList()
                self.urllist.append(temp_model.from_map(k))
        return self


class DetectCovid19CadResponseBodyData(TeaModel):
    def __init__(
        self,
        normal_probability: str = None,
        new_probability: str = None,
        lesion_ratio: str = None,
        other_probability: str = None,
        mask: str = None,
    ):
        self.normal_probability = normal_probability
        self.new_probability = new_probability
        self.lesion_ratio = lesion_ratio
        self.other_probability = other_probability
        self.mask = mask

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.normal_probability is not None:
            result['NormalProbability'] = self.normal_probability
        if self.new_probability is not None:
            result['NewProbability'] = self.new_probability
        if self.lesion_ratio is not None:
            result['LesionRatio'] = self.lesion_ratio
        if self.other_probability is not None:
            result['OtherProbability'] = self.other_probability
        if self.mask is not None:
            result['Mask'] = self.mask
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NormalProbability') is not None:
            self.normal_probability = m.get('NormalProbability')
        if m.get('NewProbability') is not None:
            self.new_probability = m.get('NewProbability')
        if m.get('LesionRatio') is not None:
            self.lesion_ratio = m.get('LesionRatio')
        if m.get('OtherProbability') is not None:
            self.other_probability = m.get('OtherProbability')
        if m.get('Mask') is not None:
            self.mask = m.get('Mask')
        return self


class DetectCovid19CadResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: DetectCovid19CadResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = DetectCovid19CadResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class DetectCovid19CadResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DetectCovid19CadResponseBody = None,
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
            temp_model = DetectCovid19CadResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ScreenChestCTRequestURLList(TeaModel):
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
        if self.urllist:
            for k in self.urllist:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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


class ScreenChestCTResponseBodyDataLungNoduleSeriesElements(TeaModel):
    def __init__(
        self,
        lobe: str = None,
        mean_value: float = None,
        lung: str = None,
        confidence: float = None,
        sopinstance_uid: str = None,
        category: str = None,
        volume: float = None,
        diameter: float = None,
        x: float = None,
        y: float = None,
        z: float = None,
        image_x: float = None,
        image_y: float = None,
        image_z: float = None,
    ):
        self.lobe = lobe
        self.mean_value = mean_value
        self.lung = lung
        self.confidence = confidence
        self.sopinstance_uid = sopinstance_uid
        self.category = category
        self.volume = volume
        self.diameter = diameter
        self.x = x
        self.y = y
        self.z = z
        self.image_x = image_x
        self.image_y = image_y
        self.image_z = image_z

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lobe is not None:
            result['Lobe'] = self.lobe
        if self.mean_value is not None:
            result['MeanValue'] = self.mean_value
        if self.lung is not None:
            result['Lung'] = self.lung
        if self.confidence is not None:
            result['Confidence'] = self.confidence
        if self.sopinstance_uid is not None:
            result['SOPInstanceUID'] = self.sopinstance_uid
        if self.category is not None:
            result['Category'] = self.category
        if self.volume is not None:
            result['Volume'] = self.volume
        if self.diameter is not None:
            result['Diameter'] = self.diameter
        if self.x is not None:
            result['X'] = self.x
        if self.y is not None:
            result['Y'] = self.y
        if self.z is not None:
            result['Z'] = self.z
        if self.image_x is not None:
            result['ImageX'] = self.image_x
        if self.image_y is not None:
            result['ImageY'] = self.image_y
        if self.image_z is not None:
            result['ImageZ'] = self.image_z
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lobe') is not None:
            self.lobe = m.get('Lobe')
        if m.get('MeanValue') is not None:
            self.mean_value = m.get('MeanValue')
        if m.get('Lung') is not None:
            self.lung = m.get('Lung')
        if m.get('Confidence') is not None:
            self.confidence = m.get('Confidence')
        if m.get('SOPInstanceUID') is not None:
            self.sopinstance_uid = m.get('SOPInstanceUID')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Volume') is not None:
            self.volume = m.get('Volume')
        if m.get('Diameter') is not None:
            self.diameter = m.get('Diameter')
        if m.get('X') is not None:
            self.x = m.get('X')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        if m.get('Z') is not None:
            self.z = m.get('Z')
        if m.get('ImageX') is not None:
            self.image_x = m.get('ImageX')
        if m.get('ImageY') is not None:
            self.image_y = m.get('ImageY')
        if m.get('ImageZ') is not None:
            self.image_z = m.get('ImageZ')
        return self


class ScreenChestCTResponseBodyDataLungNoduleSeries(TeaModel):
    def __init__(
        self,
        series_instance_uid: str = None,
        elements: List[ScreenChestCTResponseBodyDataLungNoduleSeriesElements] = None,
        origin: List[float] = None,
        report: str = None,
        spacing: List[float] = None,
    ):
        self.series_instance_uid = series_instance_uid
        self.elements = elements
        self.origin = origin
        self.report = report
        self.spacing = spacing

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
        if self.series_instance_uid is not None:
            result['SeriesInstanceUid'] = self.series_instance_uid
        result['Elements'] = []
        if self.elements is not None:
            for k in self.elements:
                result['Elements'].append(k.to_map() if k else None)
        if self.origin is not None:
            result['Origin'] = self.origin
        if self.report is not None:
            result['Report'] = self.report
        if self.spacing is not None:
            result['Spacing'] = self.spacing
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SeriesInstanceUid') is not None:
            self.series_instance_uid = m.get('SeriesInstanceUid')
        self.elements = []
        if m.get('Elements') is not None:
            for k in m.get('Elements'):
                temp_model = ScreenChestCTResponseBodyDataLungNoduleSeriesElements()
                self.elements.append(temp_model.from_map(k))
        if m.get('Origin') is not None:
            self.origin = m.get('Origin')
        if m.get('Report') is not None:
            self.report = m.get('Report')
        if m.get('Spacing') is not None:
            self.spacing = m.get('Spacing')
        return self


class ScreenChestCTResponseBodyDataLungNodule(TeaModel):
    def __init__(
        self,
        series: List[ScreenChestCTResponseBodyDataLungNoduleSeries] = None,
    ):
        self.series = series

    def validate(self):
        if self.series:
            for k in self.series:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
                temp_model = ScreenChestCTResponseBodyDataLungNoduleSeries()
                self.series.append(temp_model.from_map(k))
        return self


class ScreenChestCTResponseBodyDataCACS(TeaModel):
    def __init__(
        self,
        result_url: str = None,
        score: str = None,
    ):
        self.result_url = result_url
        self.score = score

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result_url is not None:
            result['ResultUrl'] = self.result_url
        if self.score is not None:
            result['Score'] = self.score
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResultUrl') is not None:
            self.result_url = m.get('ResultUrl')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        return self


class ScreenChestCTResponseBodyDataCovid(TeaModel):
    def __init__(
        self,
        normal_probability: str = None,
        new_probability: str = None,
        lesion_ratio: str = None,
        other_probability: str = None,
        mask: str = None,
    ):
        self.normal_probability = normal_probability
        self.new_probability = new_probability
        self.lesion_ratio = lesion_ratio
        self.other_probability = other_probability
        self.mask = mask

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.normal_probability is not None:
            result['NormalProbability'] = self.normal_probability
        if self.new_probability is not None:
            result['NewProbability'] = self.new_probability
        if self.lesion_ratio is not None:
            result['LesionRatio'] = self.lesion_ratio
        if self.other_probability is not None:
            result['OtherProbability'] = self.other_probability
        if self.mask is not None:
            result['Mask'] = self.mask
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NormalProbability') is not None:
            self.normal_probability = m.get('NormalProbability')
        if m.get('NewProbability') is not None:
            self.new_probability = m.get('NewProbability')
        if m.get('LesionRatio') is not None:
            self.lesion_ratio = m.get('LesionRatio')
        if m.get('OtherProbability') is not None:
            self.other_probability = m.get('OtherProbability')
        if m.get('Mask') is not None:
            self.mask = m.get('Mask')
        return self


class ScreenChestCTResponseBodyDataDetectRibFractureDetections(TeaModel):
    def __init__(
        self,
        fracture_id: int = None,
        fracture_confidence: float = None,
        fracture_category: int = None,
        coordinates: List[int] = None,
        coordinate_image: List[int] = None,
        fracture_location: str = None,
        fracture_segment: int = None,
    ):
        self.fracture_id = fracture_id
        self.fracture_confidence = fracture_confidence
        self.fracture_category = fracture_category
        self.coordinates = coordinates
        self.coordinate_image = coordinate_image
        self.fracture_location = fracture_location
        self.fracture_segment = fracture_segment

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        if self.fracture_location is not None:
            result['FractureLocation'] = self.fracture_location
        if self.fracture_segment is not None:
            result['FractureSegment'] = self.fracture_segment
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
        if m.get('FractureLocation') is not None:
            self.fracture_location = m.get('FractureLocation')
        if m.get('FractureSegment') is not None:
            self.fracture_segment = m.get('FractureSegment')
        return self


class ScreenChestCTResponseBodyDataDetectRibFracture(TeaModel):
    def __init__(
        self,
        result_url: str = None,
        spacing: List[float] = None,
        origin: List[float] = None,
        detections: List[ScreenChestCTResponseBodyDataDetectRibFractureDetections] = None,
    ):
        self.result_url = result_url
        self.spacing = spacing
        self.origin = origin
        self.detections = detections

    def validate(self):
        if self.detections:
            for k in self.detections:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result_url is not None:
            result['ResultURL'] = self.result_url
        if self.spacing is not None:
            result['Spacing'] = self.spacing
        if self.origin is not None:
            result['Origin'] = self.origin
        result['Detections'] = []
        if self.detections is not None:
            for k in self.detections:
                result['Detections'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResultURL') is not None:
            self.result_url = m.get('ResultURL')
        if m.get('Spacing') is not None:
            self.spacing = m.get('Spacing')
        if m.get('Origin') is not None:
            self.origin = m.get('Origin')
        self.detections = []
        if m.get('Detections') is not None:
            for k in m.get('Detections'):
                temp_model = ScreenChestCTResponseBodyDataDetectRibFractureDetections()
                self.detections.append(temp_model.from_map(k))
        return self


class ScreenChestCTResponseBodyData(TeaModel):
    def __init__(
        self,
        lung_nodule: ScreenChestCTResponseBodyDataLungNodule = None,
        cacs: ScreenChestCTResponseBodyDataCACS = None,
        covid: ScreenChestCTResponseBodyDataCovid = None,
        detect_rib_fracture: ScreenChestCTResponseBodyDataDetectRibFracture = None,
    ):
        self.lung_nodule = lung_nodule
        self.cacs = cacs
        self.covid = covid
        self.detect_rib_fracture = detect_rib_fracture

    def validate(self):
        if self.lung_nodule:
            self.lung_nodule.validate()
        if self.cacs:
            self.cacs.validate()
        if self.covid:
            self.covid.validate()
        if self.detect_rib_fracture:
            self.detect_rib_fracture.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lung_nodule is not None:
            result['LungNodule'] = self.lung_nodule.to_map()
        if self.cacs is not None:
            result['CACS'] = self.cacs.to_map()
        if self.covid is not None:
            result['Covid'] = self.covid.to_map()
        if self.detect_rib_fracture is not None:
            result['DetectRibFracture'] = self.detect_rib_fracture.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LungNodule') is not None:
            temp_model = ScreenChestCTResponseBodyDataLungNodule()
            self.lung_nodule = temp_model.from_map(m['LungNodule'])
        if m.get('CACS') is not None:
            temp_model = ScreenChestCTResponseBodyDataCACS()
            self.cacs = temp_model.from_map(m['CACS'])
        if m.get('Covid') is not None:
            temp_model = ScreenChestCTResponseBodyDataCovid()
            self.covid = temp_model.from_map(m['Covid'])
        if m.get('DetectRibFracture') is not None:
            temp_model = ScreenChestCTResponseBodyDataDetectRibFracture()
            self.detect_rib_fracture = temp_model.from_map(m['DetectRibFracture'])
        return self


class ScreenChestCTResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: ScreenChestCTResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = ScreenChestCTResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class ScreenChestCTResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ScreenChestCTResponseBody = None,
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
            temp_model = ScreenChestCTResponseBody()
            self.body = temp_model.from_map(m['body'])
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
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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


class DetectSkinDiseaseResponseBodyData(TeaModel):
    def __init__(
        self,
        results: Dict[str, Any] = None,
    ):
        self.results = results

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.results is not None:
            result['Results'] = self.results
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Results') is not None:
            self.results = m.get('Results')
        return self


class DetectSkinDiseaseResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: DetectSkinDiseaseResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = DetectSkinDiseaseResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class DetectSkinDiseaseResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DetectSkinDiseaseResponseBody = None,
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
            temp_model = DetectSkinDiseaseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


