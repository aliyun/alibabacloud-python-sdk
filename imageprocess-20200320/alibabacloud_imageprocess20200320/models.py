# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, BinaryIO, Dict, Any


class AnalyzeChestVesselRequestURLList(TeaModel):
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


class AnalyzeChestVesselRequest(TeaModel):
    def __init__(
        self,
        data_format: str = None,
        data_source_type: str = None,
        org_id: str = None,
        org_name: str = None,
        urllist: List[AnalyzeChestVesselRequestURLList] = None,
    ):
        self.data_format = data_format
        self.data_source_type = data_source_type
        self.org_id = org_id
        self.org_name = org_name
        # 1
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
        if self.data_source_type is not None:
            result['DataSourceType'] = self.data_source_type
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.org_name is not None:
            result['OrgName'] = self.org_name
        result['URLList'] = []
        if self.urllist is not None:
            for k in self.urllist:
                result['URLList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataFormat') is not None:
            self.data_format = m.get('DataFormat')
        if m.get('DataSourceType') is not None:
            self.data_source_type = m.get('DataSourceType')
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('OrgName') is not None:
            self.org_name = m.get('OrgName')
        self.urllist = []
        if m.get('URLList') is not None:
            for k in m.get('URLList'):
                temp_model = AnalyzeChestVesselRequestURLList()
                self.urllist.append(temp_model.from_map(k))
        return self


class AnalyzeChestVesselAdvanceRequestURLList(TeaModel):
    def __init__(
        self,
        urlobject: BinaryIO = None,
    ):
        self.urlobject = urlobject

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.urlobject is not None:
            result['URL'] = self.urlobject
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('URL') is not None:
            self.urlobject = m.get('URL')
        return self


class AnalyzeChestVesselAdvanceRequest(TeaModel):
    def __init__(
        self,
        data_format: str = None,
        data_source_type: str = None,
        org_id: str = None,
        org_name: str = None,
        urllist: List[AnalyzeChestVesselAdvanceRequestURLList] = None,
    ):
        self.data_format = data_format
        self.data_source_type = data_source_type
        self.org_id = org_id
        self.org_name = org_name
        # 1
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
        if self.data_source_type is not None:
            result['DataSourceType'] = self.data_source_type
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.org_name is not None:
            result['OrgName'] = self.org_name
        result['URLList'] = []
        if self.urllist is not None:
            for k in self.urllist:
                result['URLList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataFormat') is not None:
            self.data_format = m.get('DataFormat')
        if m.get('DataSourceType') is not None:
            self.data_source_type = m.get('DataSourceType')
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('OrgName') is not None:
            self.org_name = m.get('OrgName')
        self.urllist = []
        if m.get('URLList') is not None:
            for k in m.get('URLList'):
                temp_model = AnalyzeChestVesselAdvanceRequestURLList()
                self.urllist.append(temp_model.from_map(k))
        return self


class AnalyzeChestVesselResponseBodyDataAortaInfo(TeaModel):
    def __init__(
        self,
        area: List[float] = None,
        coordinates: List[List[float]] = None,
        label_value: int = None,
        max_area: float = None,
        max_area_index: int = None,
        max_diameter: float = None,
    ):
        # 1
        self.area = area
        self.coordinates = coordinates
        self.label_value = label_value
        self.max_area = max_area
        self.max_area_index = max_area_index
        self.max_diameter = max_diameter

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.area is not None:
            result['Area'] = self.area
        if self.coordinates is not None:
            result['Coordinates'] = self.coordinates
        if self.label_value is not None:
            result['LabelValue'] = self.label_value
        if self.max_area is not None:
            result['MaxArea'] = self.max_area
        if self.max_area_index is not None:
            result['MaxAreaIndex'] = self.max_area_index
        if self.max_diameter is not None:
            result['MaxDiameter'] = self.max_diameter
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Area') is not None:
            self.area = m.get('Area')
        if m.get('Coordinates') is not None:
            self.coordinates = m.get('Coordinates')
        if m.get('LabelValue') is not None:
            self.label_value = m.get('LabelValue')
        if m.get('MaxArea') is not None:
            self.max_area = m.get('MaxArea')
        if m.get('MaxAreaIndex') is not None:
            self.max_area_index = m.get('MaxAreaIndex')
        if m.get('MaxDiameter') is not None:
            self.max_diameter = m.get('MaxDiameter')
        return self


class AnalyzeChestVesselResponseBodyDataPulmonaryInfo(TeaModel):
    def __init__(
        self,
        area: List[float] = None,
        coordinates: List[List[float]] = None,
        label_value: int = None,
        max_area: float = None,
        max_area_index: int = None,
        max_diameter: float = None,
        nearest_aorta_area: float = None,
    ):
        # 1
        self.area = area
        self.coordinates = coordinates
        self.label_value = label_value
        self.max_area = max_area
        self.max_area_index = max_area_index
        self.max_diameter = max_diameter
        self.nearest_aorta_area = nearest_aorta_area

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.area is not None:
            result['Area'] = self.area
        if self.coordinates is not None:
            result['Coordinates'] = self.coordinates
        if self.label_value is not None:
            result['LabelValue'] = self.label_value
        if self.max_area is not None:
            result['MaxArea'] = self.max_area
        if self.max_area_index is not None:
            result['MaxAreaIndex'] = self.max_area_index
        if self.max_diameter is not None:
            result['MaxDiameter'] = self.max_diameter
        if self.nearest_aorta_area is not None:
            result['NearestAortaArea'] = self.nearest_aorta_area
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Area') is not None:
            self.area = m.get('Area')
        if m.get('Coordinates') is not None:
            self.coordinates = m.get('Coordinates')
        if m.get('LabelValue') is not None:
            self.label_value = m.get('LabelValue')
        if m.get('MaxArea') is not None:
            self.max_area = m.get('MaxArea')
        if m.get('MaxAreaIndex') is not None:
            self.max_area_index = m.get('MaxAreaIndex')
        if m.get('MaxDiameter') is not None:
            self.max_diameter = m.get('MaxDiameter')
        if m.get('NearestAortaArea') is not None:
            self.nearest_aorta_area = m.get('NearestAortaArea')
        return self


class AnalyzeChestVesselResponseBodyData(TeaModel):
    def __init__(
        self,
        aorta_info: AnalyzeChestVesselResponseBodyDataAortaInfo = None,
        pulmonary_info: AnalyzeChestVesselResponseBodyDataPulmonaryInfo = None,
        result_url: str = None,
    ):
        self.aorta_info = aorta_info
        self.pulmonary_info = pulmonary_info
        self.result_url = result_url

    def validate(self):
        if self.aorta_info:
            self.aorta_info.validate()
        if self.pulmonary_info:
            self.pulmonary_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aorta_info is not None:
            result['AortaInfo'] = self.aorta_info.to_map()
        if self.pulmonary_info is not None:
            result['PulmonaryInfo'] = self.pulmonary_info.to_map()
        if self.result_url is not None:
            result['ResultURL'] = self.result_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AortaInfo') is not None:
            temp_model = AnalyzeChestVesselResponseBodyDataAortaInfo()
            self.aorta_info = temp_model.from_map(m['AortaInfo'])
        if m.get('PulmonaryInfo') is not None:
            temp_model = AnalyzeChestVesselResponseBodyDataPulmonaryInfo()
            self.pulmonary_info = temp_model.from_map(m['PulmonaryInfo'])
        if m.get('ResultURL') is not None:
            self.result_url = m.get('ResultURL')
        return self


class AnalyzeChestVesselResponseBody(TeaModel):
    def __init__(
        self,
        data: AnalyzeChestVesselResponseBodyData = None,
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
            temp_model = AnalyzeChestVesselResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AnalyzeChestVesselResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AnalyzeChestVesselResponseBody = None,
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
            temp_model = AnalyzeChestVesselResponseBody()
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
        data_source_type: str = None,
        org_id: str = None,
        org_name: str = None,
        urllist: List[CalcCACSRequestURLList] = None,
    ):
        self.data_format = data_format
        self.data_source_type = data_source_type
        self.org_id = org_id
        self.org_name = org_name
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
        if self.data_source_type is not None:
            result['DataSourceType'] = self.data_source_type
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.org_name is not None:
            result['OrgName'] = self.org_name
        result['URLList'] = []
        if self.urllist is not None:
            for k in self.urllist:
                result['URLList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataFormat') is not None:
            self.data_format = m.get('DataFormat')
        if m.get('DataSourceType') is not None:
            self.data_source_type = m.get('DataSourceType')
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('OrgName') is not None:
            self.org_name = m.get('OrgName')
        self.urllist = []
        if m.get('URLList') is not None:
            for k in m.get('URLList'):
                temp_model = CalcCACSRequestURLList()
                self.urllist.append(temp_model.from_map(k))
        return self


class CalcCACSAdvanceRequestURLList(TeaModel):
    def __init__(
        self,
        urlobject: BinaryIO = None,
    ):
        self.urlobject = urlobject

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.urlobject is not None:
            result['URL'] = self.urlobject
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('URL') is not None:
            self.urlobject = m.get('URL')
        return self


class CalcCACSAdvanceRequest(TeaModel):
    def __init__(
        self,
        data_format: str = None,
        data_source_type: str = None,
        org_id: str = None,
        org_name: str = None,
        urllist: List[CalcCACSAdvanceRequestURLList] = None,
    ):
        self.data_format = data_format
        self.data_source_type = data_source_type
        self.org_id = org_id
        self.org_name = org_name
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
        if self.data_source_type is not None:
            result['DataSourceType'] = self.data_source_type
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.org_name is not None:
            result['OrgName'] = self.org_name
        result['URLList'] = []
        if self.urllist is not None:
            for k in self.urllist:
                result['URLList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataFormat') is not None:
            self.data_format = m.get('DataFormat')
        if m.get('DataSourceType') is not None:
            self.data_source_type = m.get('DataSourceType')
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('OrgName') is not None:
            self.org_name = m.get('OrgName')
        self.urllist = []
        if m.get('URLList') is not None:
            for k in m.get('URLList'):
                temp_model = CalcCACSAdvanceRequestURLList()
                self.urllist.append(temp_model.from_map(k))
        return self


class CalcCACSResponseBodyDataDetections(TeaModel):
    def __init__(
        self,
        calcium_center: List[int] = None,
        calcium_id: int = None,
        calcium_score: float = None,
        calcium_volume: float = None,
    ):
        self.calcium_center = calcium_center
        self.calcium_id = calcium_id
        self.calcium_score = calcium_score
        self.calcium_volume = calcium_volume

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.calcium_center is not None:
            result['CalciumCenter'] = self.calcium_center
        if self.calcium_id is not None:
            result['CalciumId'] = self.calcium_id
        if self.calcium_score is not None:
            result['CalciumScore'] = self.calcium_score
        if self.calcium_volume is not None:
            result['CalciumVolume'] = self.calcium_volume
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CalciumCenter') is not None:
            self.calcium_center = m.get('CalciumCenter')
        if m.get('CalciumId') is not None:
            self.calcium_id = m.get('CalciumId')
        if m.get('CalciumScore') is not None:
            self.calcium_score = m.get('CalciumScore')
        if m.get('CalciumVolume') is not None:
            self.calcium_volume = m.get('CalciumVolume')
        return self


class CalcCACSResponseBodyData(TeaModel):
    def __init__(
        self,
        detections: List[CalcCACSResponseBodyDataDetections] = None,
        result_url: str = None,
        score: str = None,
        volume_score: str = None,
    ):
        self.detections = detections
        self.result_url = result_url
        self.score = score
        self.volume_score = volume_score

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
        if self.result_url is not None:
            result['ResultUrl'] = self.result_url
        if self.score is not None:
            result['Score'] = self.score
        if self.volume_score is not None:
            result['VolumeScore'] = self.volume_score
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.detections = []
        if m.get('Detections') is not None:
            for k in m.get('Detections'):
                temp_model = CalcCACSResponseBodyDataDetections()
                self.detections.append(temp_model.from_map(k))
        if m.get('ResultUrl') is not None:
            self.result_url = m.get('ResultUrl')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('VolumeScore') is not None:
            self.volume_score = m.get('VolumeScore')
        return self


class CalcCACSResponseBody(TeaModel):
    def __init__(
        self,
        data: CalcCACSResponseBodyData = None,
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
            temp_model = CalcCACSResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CalcCACSResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CalcCACSResponseBody = None,
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
            temp_model = CalcCACSResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ClassifyFNFRequest(TeaModel):
    def __init__(
        self,
        data_format: str = None,
        image_url: str = None,
        org_id: str = None,
        org_name: str = None,
        tracer_id: str = None,
    ):
        self.data_format = data_format
        self.image_url = image_url
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
        if self.data_format is not None:
            result['DataFormat'] = self.data_format
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.org_name is not None:
            result['OrgName'] = self.org_name
        if self.tracer_id is not None:
            result['TracerId'] = self.tracer_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataFormat') is not None:
            self.data_format = m.get('DataFormat')
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
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
        data_format: str = None,
        image_url_object: BinaryIO = None,
        org_id: str = None,
        org_name: str = None,
        tracer_id: str = None,
    ):
        self.data_format = data_format
        self.image_url_object = image_url_object
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
        if self.data_format is not None:
            result['DataFormat'] = self.data_format
        if self.image_url_object is not None:
            result['ImageUrl'] = self.image_url_object
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.org_name is not None:
            result['OrgName'] = self.org_name
        if self.tracer_id is not None:
            result['TracerId'] = self.tracer_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataFormat') is not None:
            self.data_format = m.get('DataFormat')
        if m.get('ImageUrl') is not None:
            self.image_url_object = m.get('ImageUrl')
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
        boxes: List[int] = None,
        tag: ClassifyFNFResponseBodyDataFracturesTag = None,
        value: float = None,
    ):
        self.boxes = boxes
        self.tag = tag
        self.value = value

    def validate(self):
        if self.tag:
            self.tag.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.boxes is not None:
            result['Boxes'] = self.boxes
        if self.tag is not None:
            result['Tag'] = self.tag.to_map()
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Boxes') is not None:
            self.boxes = m.get('Boxes')
        if m.get('Tag') is not None:
            temp_model = ClassifyFNFResponseBodyDataFracturesTag()
            self.tag = temp_model.from_map(m['Tag'])
        if m.get('Value') is not None:
            self.value = m.get('Value')
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
        data: ClassifyFNFResponseBodyData = None,
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
            temp_model = ClassifyFNFResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ClassifyFNFResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ClassifyFNFResponseBody = None,
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
            temp_model = ClassifyFNFResponseBody()
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
        org_id: str = None,
        org_name: str = None,
        urllist: List[DetectCovid19CadRequestURLList] = None,
    ):
        self.data_format = data_format
        self.org_id = org_id
        self.org_name = org_name
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
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.org_name is not None:
            result['OrgName'] = self.org_name
        result['URLList'] = []
        if self.urllist is not None:
            for k in self.urllist:
                result['URLList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataFormat') is not None:
            self.data_format = m.get('DataFormat')
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('OrgName') is not None:
            self.org_name = m.get('OrgName')
        self.urllist = []
        if m.get('URLList') is not None:
            for k in m.get('URLList'):
                temp_model = DetectCovid19CadRequestURLList()
                self.urllist.append(temp_model.from_map(k))
        return self


class DetectCovid19CadAdvanceRequestURLList(TeaModel):
    def __init__(
        self,
        urlobject: BinaryIO = None,
    ):
        self.urlobject = urlobject

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.urlobject is not None:
            result['URL'] = self.urlobject
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('URL') is not None:
            self.urlobject = m.get('URL')
        return self


class DetectCovid19CadAdvanceRequest(TeaModel):
    def __init__(
        self,
        data_format: str = None,
        org_id: str = None,
        org_name: str = None,
        urllist: List[DetectCovid19CadAdvanceRequestURLList] = None,
    ):
        self.data_format = data_format
        self.org_id = org_id
        self.org_name = org_name
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
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.org_name is not None:
            result['OrgName'] = self.org_name
        result['URLList'] = []
        if self.urllist is not None:
            for k in self.urllist:
                result['URLList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataFormat') is not None:
            self.data_format = m.get('DataFormat')
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('OrgName') is not None:
            self.org_name = m.get('OrgName')
        self.urllist = []
        if m.get('URLList') is not None:
            for k in m.get('URLList'):
                temp_model = DetectCovid19CadAdvanceRequestURLList()
                self.urllist.append(temp_model.from_map(k))
        return self


class DetectCovid19CadResponseBodyData(TeaModel):
    def __init__(
        self,
        lesion_ratio: str = None,
        mask: str = None,
        new_probability: str = None,
        normal_probability: str = None,
        other_probability: str = None,
    ):
        self.lesion_ratio = lesion_ratio
        self.mask = mask
        self.new_probability = new_probability
        self.normal_probability = normal_probability
        self.other_probability = other_probability

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lesion_ratio is not None:
            result['LesionRatio'] = self.lesion_ratio
        if self.mask is not None:
            result['Mask'] = self.mask
        if self.new_probability is not None:
            result['NewProbability'] = self.new_probability
        if self.normal_probability is not None:
            result['NormalProbability'] = self.normal_probability
        if self.other_probability is not None:
            result['OtherProbability'] = self.other_probability
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LesionRatio') is not None:
            self.lesion_ratio = m.get('LesionRatio')
        if m.get('Mask') is not None:
            self.mask = m.get('Mask')
        if m.get('NewProbability') is not None:
            self.new_probability = m.get('NewProbability')
        if m.get('NormalProbability') is not None:
            self.normal_probability = m.get('NormalProbability')
        if m.get('OtherProbability') is not None:
            self.other_probability = m.get('OtherProbability')
        return self


class DetectCovid19CadResponseBody(TeaModel):
    def __init__(
        self,
        data: DetectCovid19CadResponseBodyData = None,
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
            temp_model = DetectCovid19CadResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DetectCovid19CadResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DetectCovid19CadResponseBody = None,
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
            temp_model = DetectCovid19CadResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetectHipKeypointXRayRequest(TeaModel):
    def __init__(
        self,
        data_format: str = None,
        image_url: str = None,
        org_id: str = None,
        org_name: str = None,
        tracer_id: str = None,
    ):
        self.data_format = data_format
        self.image_url = image_url
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
        if self.data_format is not None:
            result['DataFormat'] = self.data_format
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.org_name is not None:
            result['OrgName'] = self.org_name
        if self.tracer_id is not None:
            result['TracerId'] = self.tracer_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataFormat') is not None:
            self.data_format = m.get('DataFormat')
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
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
        data_format: str = None,
        image_url_object: BinaryIO = None,
        org_id: str = None,
        org_name: str = None,
        tracer_id: str = None,
    ):
        self.data_format = data_format
        self.image_url_object = image_url_object
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
        if self.data_format is not None:
            result['DataFormat'] = self.data_format
        if self.image_url_object is not None:
            result['ImageUrl'] = self.image_url_object
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.org_name is not None:
            result['OrgName'] = self.org_name
        if self.tracer_id is not None:
            result['TracerId'] = self.tracer_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataFormat') is not None:
            self.data_format = m.get('DataFormat')
        if m.get('ImageUrl') is not None:
            self.image_url_object = m.get('ImageUrl')
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
        coordinates: List[int] = None,
        tag: DetectHipKeypointXRayResponseBodyDataKeyPointsTag = None,
        value: float = None,
    ):
        self.coordinates = coordinates
        self.tag = tag
        self.value = value

    def validate(self):
        if self.tag:
            self.tag.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.coordinates is not None:
            result['Coordinates'] = self.coordinates
        if self.tag is not None:
            result['Tag'] = self.tag.to_map()
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Coordinates') is not None:
            self.coordinates = m.get('Coordinates')
        if m.get('Tag') is not None:
            temp_model = DetectHipKeypointXRayResponseBodyDataKeyPointsTag()
            self.tag = temp_model.from_map(m['Tag'])
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DetectHipKeypointXRayResponseBodyData(TeaModel):
    def __init__(
        self,
        image_url: str = None,
        key_points: List[DetectHipKeypointXRayResponseBodyDataKeyPoints] = None,
        org_id: str = None,
        org_name: str = None,
    ):
        self.image_url = image_url
        self.key_points = key_points
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
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        result['KeyPoints'] = []
        if self.key_points is not None:
            for k in self.key_points:
                result['KeyPoints'].append(k.to_map() if k else None)
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.org_name is not None:
            result['OrgName'] = self.org_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        self.key_points = []
        if m.get('KeyPoints') is not None:
            for k in m.get('KeyPoints'):
                temp_model = DetectHipKeypointXRayResponseBodyDataKeyPoints()
                self.key_points.append(temp_model.from_map(k))
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('OrgName') is not None:
            self.org_name = m.get('OrgName')
        return self


class DetectHipKeypointXRayResponseBody(TeaModel):
    def __init__(
        self,
        data: DetectHipKeypointXRayResponseBodyData = None,
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
            temp_model = DetectHipKeypointXRayResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DetectHipKeypointXRayResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DetectHipKeypointXRayResponseBody = None,
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
            temp_model = DetectHipKeypointXRayResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetectKneeKeypointXRayRequest(TeaModel):
    def __init__(
        self,
        data_format: str = None,
        image_url: str = None,
        org_id: str = None,
        org_name: str = None,
        tracer_id: str = None,
    ):
        self.data_format = data_format
        self.image_url = image_url
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
        if self.data_format is not None:
            result['DataFormat'] = self.data_format
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.org_name is not None:
            result['OrgName'] = self.org_name
        if self.tracer_id is not None:
            result['TracerId'] = self.tracer_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataFormat') is not None:
            self.data_format = m.get('DataFormat')
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
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
        data_format: str = None,
        image_url_object: BinaryIO = None,
        org_id: str = None,
        org_name: str = None,
        tracer_id: str = None,
    ):
        self.data_format = data_format
        self.image_url_object = image_url_object
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
        if self.data_format is not None:
            result['DataFormat'] = self.data_format
        if self.image_url_object is not None:
            result['ImageUrl'] = self.image_url_object
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.org_name is not None:
            result['OrgName'] = self.org_name
        if self.tracer_id is not None:
            result['TracerId'] = self.tracer_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataFormat') is not None:
            self.data_format = m.get('DataFormat')
        if m.get('ImageUrl') is not None:
            self.image_url_object = m.get('ImageUrl')
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
        coordinates: List[int] = None,
        tag: DetectKneeKeypointXRayResponseBodyDataKeyPointsTag = None,
        value: float = None,
    ):
        # 1
        self.coordinates = coordinates
        self.tag = tag
        self.value = value

    def validate(self):
        if self.tag:
            self.tag.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.coordinates is not None:
            result['Coordinates'] = self.coordinates
        if self.tag is not None:
            result['Tag'] = self.tag.to_map()
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Coordinates') is not None:
            self.coordinates = m.get('Coordinates')
        if m.get('Tag') is not None:
            temp_model = DetectKneeKeypointXRayResponseBodyDataKeyPointsTag()
            self.tag = temp_model.from_map(m['Tag'])
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DetectKneeKeypointXRayResponseBodyData(TeaModel):
    def __init__(
        self,
        image_url: str = None,
        key_points: List[DetectKneeKeypointXRayResponseBodyDataKeyPoints] = None,
        org_id: str = None,
        org_name: str = None,
    ):
        self.image_url = image_url
        self.key_points = key_points
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
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        result['KeyPoints'] = []
        if self.key_points is not None:
            for k in self.key_points:
                result['KeyPoints'].append(k.to_map() if k else None)
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.org_name is not None:
            result['OrgName'] = self.org_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        self.key_points = []
        if m.get('KeyPoints') is not None:
            for k in m.get('KeyPoints'):
                temp_model = DetectKneeKeypointXRayResponseBodyDataKeyPoints()
                self.key_points.append(temp_model.from_map(k))
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('OrgName') is not None:
            self.org_name = m.get('OrgName')
        return self


class DetectKneeKeypointXRayResponseBody(TeaModel):
    def __init__(
        self,
        data: DetectKneeKeypointXRayResponseBodyData = None,
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
            temp_model = DetectKneeKeypointXRayResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DetectKneeKeypointXRayResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DetectKneeKeypointXRayResponseBody = None,
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
            temp_model = DetectKneeKeypointXRayResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetectKneeXRayRequest(TeaModel):
    def __init__(
        self,
        data_format: str = None,
        org_id: str = None,
        org_name: str = None,
        url: str = None,
    ):
        self.data_format = data_format
        self.org_id = org_id
        self.org_name = org_name
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_format is not None:
            result['DataFormat'] = self.data_format
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.org_name is not None:
            result['OrgName'] = self.org_name
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataFormat') is not None:
            self.data_format = m.get('DataFormat')
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('OrgName') is not None:
            self.org_name = m.get('OrgName')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class DetectKneeXRayAdvanceRequest(TeaModel):
    def __init__(
        self,
        data_format: str = None,
        org_id: str = None,
        org_name: str = None,
        url_object: BinaryIO = None,
    ):
        self.data_format = data_format
        self.org_id = org_id
        self.org_name = org_name
        self.url_object = url_object

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_format is not None:
            result['DataFormat'] = self.data_format
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.org_name is not None:
            result['OrgName'] = self.org_name
        if self.url_object is not None:
            result['Url'] = self.url_object
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataFormat') is not None:
            self.data_format = m.get('DataFormat')
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('OrgName') is not None:
            self.org_name = m.get('OrgName')
        if m.get('Url') is not None:
            self.url_object = m.get('Url')
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
        data: DetectKneeXRayResponseBodyData = None,
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
            temp_model = DetectKneeXRayResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DetectKneeXRayResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DetectKneeXRayResponseBody = None,
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
            temp_model = DetectKneeXRayResponseBody()
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
        org_id: str = None,
        org_name: str = None,
        threshold: float = None,
        urllist: List[DetectLungNoduleRequestURLList] = None,
    ):
        self.data_format = data_format
        self.org_id = org_id
        self.org_name = org_name
        self.threshold = threshold
        # 1
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
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.org_name is not None:
            result['OrgName'] = self.org_name
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        result['URLList'] = []
        if self.urllist is not None:
            for k in self.urllist:
                result['URLList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataFormat') is not None:
            self.data_format = m.get('DataFormat')
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('OrgName') is not None:
            self.org_name = m.get('OrgName')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        self.urllist = []
        if m.get('URLList') is not None:
            for k in m.get('URLList'):
                temp_model = DetectLungNoduleRequestURLList()
                self.urllist.append(temp_model.from_map(k))
        return self


class DetectLungNoduleAdvanceRequestURLList(TeaModel):
    def __init__(
        self,
        urlobject: BinaryIO = None,
    ):
        self.urlobject = urlobject

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.urlobject is not None:
            result['URL'] = self.urlobject
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('URL') is not None:
            self.urlobject = m.get('URL')
        return self


class DetectLungNoduleAdvanceRequest(TeaModel):
    def __init__(
        self,
        data_format: str = None,
        org_id: str = None,
        org_name: str = None,
        threshold: float = None,
        urllist: List[DetectLungNoduleAdvanceRequestURLList] = None,
    ):
        self.data_format = data_format
        self.org_id = org_id
        self.org_name = org_name
        self.threshold = threshold
        # 1
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
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.org_name is not None:
            result['OrgName'] = self.org_name
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        result['URLList'] = []
        if self.urllist is not None:
            for k in self.urllist:
                result['URLList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataFormat') is not None:
            self.data_format = m.get('DataFormat')
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('OrgName') is not None:
            self.org_name = m.get('OrgName')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        self.urllist = []
        if m.get('URLList') is not None:
            for k in m.get('URLList'):
                temp_model = DetectLungNoduleAdvanceRequestURLList()
                self.urllist.append(temp_model.from_map(k))
        return self


class DetectLungNoduleResponseBodyDataSeriesElements(TeaModel):
    def __init__(
        self,
        category: str = None,
        confidence: float = None,
        diameter: float = None,
        image_x: float = None,
        image_y: float = None,
        image_z: float = None,
        lobe: str = None,
        lung: str = None,
        major_axis: List[float] = None,
        mean_value: float = None,
        minor_axis: List[float] = None,
        recist_sopinstance_uid: str = None,
        risk: float = None,
        sopinstance_uid: str = None,
        volume: float = None,
        x: float = None,
        y: float = None,
        z: float = None,
    ):
        self.category = category
        self.confidence = confidence
        self.diameter = diameter
        self.image_x = image_x
        self.image_y = image_y
        self.image_z = image_z
        self.lobe = lobe
        self.lung = lung
        self.major_axis = major_axis
        self.mean_value = mean_value
        self.minor_axis = minor_axis
        self.recist_sopinstance_uid = recist_sopinstance_uid
        self.risk = risk
        self.sopinstance_uid = sopinstance_uid
        self.volume = volume
        self.x = x
        self.y = y
        self.z = z

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.confidence is not None:
            result['Confidence'] = self.confidence
        if self.diameter is not None:
            result['Diameter'] = self.diameter
        if self.image_x is not None:
            result['ImageX'] = self.image_x
        if self.image_y is not None:
            result['ImageY'] = self.image_y
        if self.image_z is not None:
            result['ImageZ'] = self.image_z
        if self.lobe is not None:
            result['Lobe'] = self.lobe
        if self.lung is not None:
            result['Lung'] = self.lung
        if self.major_axis is not None:
            result['MajorAxis'] = self.major_axis
        if self.mean_value is not None:
            result['MeanValue'] = self.mean_value
        if self.minor_axis is not None:
            result['MinorAxis'] = self.minor_axis
        if self.recist_sopinstance_uid is not None:
            result['RecistSOPInstanceUID'] = self.recist_sopinstance_uid
        if self.risk is not None:
            result['Risk'] = self.risk
        if self.sopinstance_uid is not None:
            result['SOPInstanceUID'] = self.sopinstance_uid
        if self.volume is not None:
            result['Volume'] = self.volume
        if self.x is not None:
            result['X'] = self.x
        if self.y is not None:
            result['Y'] = self.y
        if self.z is not None:
            result['Z'] = self.z
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Confidence') is not None:
            self.confidence = m.get('Confidence')
        if m.get('Diameter') is not None:
            self.diameter = m.get('Diameter')
        if m.get('ImageX') is not None:
            self.image_x = m.get('ImageX')
        if m.get('ImageY') is not None:
            self.image_y = m.get('ImageY')
        if m.get('ImageZ') is not None:
            self.image_z = m.get('ImageZ')
        if m.get('Lobe') is not None:
            self.lobe = m.get('Lobe')
        if m.get('Lung') is not None:
            self.lung = m.get('Lung')
        if m.get('MajorAxis') is not None:
            self.major_axis = m.get('MajorAxis')
        if m.get('MeanValue') is not None:
            self.mean_value = m.get('MeanValue')
        if m.get('MinorAxis') is not None:
            self.minor_axis = m.get('MinorAxis')
        if m.get('RecistSOPInstanceUID') is not None:
            self.recist_sopinstance_uid = m.get('RecistSOPInstanceUID')
        if m.get('Risk') is not None:
            self.risk = m.get('Risk')
        if m.get('SOPInstanceUID') is not None:
            self.sopinstance_uid = m.get('SOPInstanceUID')
        if m.get('Volume') is not None:
            self.volume = m.get('Volume')
        if m.get('X') is not None:
            self.x = m.get('X')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        if m.get('Z') is not None:
            self.z = m.get('Z')
        return self


class DetectLungNoduleResponseBodyDataSeries(TeaModel):
    def __init__(
        self,
        elements: List[DetectLungNoduleResponseBodyDataSeriesElements] = None,
        origin: List[float] = None,
        report: str = None,
        series_instance_uid: str = None,
        spacing: List[float] = None,
    ):
        self.elements = elements
        # 1
        self.origin = origin
        self.report = report
        self.series_instance_uid = series_instance_uid
        # 1
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
        result['Elements'] = []
        if self.elements is not None:
            for k in self.elements:
                result['Elements'].append(k.to_map() if k else None)
        if self.origin is not None:
            result['Origin'] = self.origin
        if self.report is not None:
            result['Report'] = self.report
        if self.series_instance_uid is not None:
            result['SeriesInstanceUid'] = self.series_instance_uid
        if self.spacing is not None:
            result['Spacing'] = self.spacing
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.elements = []
        if m.get('Elements') is not None:
            for k in m.get('Elements'):
                temp_model = DetectLungNoduleResponseBodyDataSeriesElements()
                self.elements.append(temp_model.from_map(k))
        if m.get('Origin') is not None:
            self.origin = m.get('Origin')
        if m.get('Report') is not None:
            self.report = m.get('Report')
        if m.get('SeriesInstanceUid') is not None:
            self.series_instance_uid = m.get('SeriesInstanceUid')
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
        data: DetectLungNoduleResponseBodyData = None,
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
            temp_model = DetectLungNoduleResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DetectLungNoduleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DetectLungNoduleResponseBody = None,
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
            temp_model = DetectLungNoduleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetectLymphRequestURLList(TeaModel):
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


class DetectLymphRequest(TeaModel):
    def __init__(
        self,
        data_source_type: str = None,
        urllist: List[DetectLymphRequestURLList] = None,
    ):
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
        if self.data_source_type is not None:
            result['DataSourceType'] = self.data_source_type
        result['URLList'] = []
        if self.urllist is not None:
            for k in self.urllist:
                result['URLList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSourceType') is not None:
            self.data_source_type = m.get('DataSourceType')
        self.urllist = []
        if m.get('URLList') is not None:
            for k in m.get('URLList'):
                temp_model = DetectLymphRequestURLList()
                self.urllist.append(temp_model.from_map(k))
        return self


class DetectLymphAdvanceRequestURLList(TeaModel):
    def __init__(
        self,
        urlobject: BinaryIO = None,
    ):
        self.urlobject = urlobject

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.urlobject is not None:
            result['URL'] = self.urlobject
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('URL') is not None:
            self.urlobject = m.get('URL')
        return self


class DetectLymphAdvanceRequest(TeaModel):
    def __init__(
        self,
        data_source_type: str = None,
        urllist: List[DetectLymphAdvanceRequestURLList] = None,
    ):
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
        if self.data_source_type is not None:
            result['DataSourceType'] = self.data_source_type
        result['URLList'] = []
        if self.urllist is not None:
            for k in self.urllist:
                result['URLList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSourceType') is not None:
            self.data_source_type = m.get('DataSourceType')
        self.urllist = []
        if m.get('URLList') is not None:
            for k in m.get('URLList'):
                temp_model = DetectLymphAdvanceRequestURLList()
                self.urllist.append(temp_model.from_map(k))
        return self


class DetectLymphResponseBodyDataLesions(TeaModel):
    def __init__(
        self,
        boxes: List[float] = None,
        diametermm: List[float] = None,
        key_slice: int = None,
        recist: List[List[float]] = None,
        score: float = None,
    ):
        self.boxes = boxes
        self.diametermm = diametermm
        self.key_slice = key_slice
        self.recist = recist
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
        if self.diametermm is not None:
            result['Diametermm'] = self.diametermm
        if self.key_slice is not None:
            result['KeySlice'] = self.key_slice
        if self.recist is not None:
            result['Recist'] = self.recist
        if self.score is not None:
            result['Score'] = self.score
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Boxes') is not None:
            self.boxes = m.get('Boxes')
        if m.get('Diametermm') is not None:
            self.diametermm = m.get('Diametermm')
        if m.get('KeySlice') is not None:
            self.key_slice = m.get('KeySlice')
        if m.get('Recist') is not None:
            self.recist = m.get('Recist')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        return self


class DetectLymphResponseBodyData(TeaModel):
    def __init__(
        self,
        lesions: List[DetectLymphResponseBodyDataLesions] = None,
    ):
        self.lesions = lesions

    def validate(self):
        if self.lesions:
            for k in self.lesions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Lesions'] = []
        if self.lesions is not None:
            for k in self.lesions:
                result['Lesions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.lesions = []
        if m.get('Lesions') is not None:
            for k in m.get('Lesions'):
                temp_model = DetectLymphResponseBodyDataLesions()
                self.lesions.append(temp_model.from_map(k))
        return self


class DetectLymphResponseBody(TeaModel):
    def __init__(
        self,
        data: DetectLymphResponseBodyData = None,
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
            temp_model = DetectLymphResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DetectLymphResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DetectLymphResponseBody = None,
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
            temp_model = DetectLymphResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetectPancRequestURLList(TeaModel):
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


class DetectPancRequest(TeaModel):
    def __init__(
        self,
        data_source_type: str = None,
        urllist: List[DetectPancRequestURLList] = None,
    ):
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
        if self.data_source_type is not None:
            result['DataSourceType'] = self.data_source_type
        result['URLList'] = []
        if self.urllist is not None:
            for k in self.urllist:
                result['URLList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSourceType') is not None:
            self.data_source_type = m.get('DataSourceType')
        self.urllist = []
        if m.get('URLList') is not None:
            for k in m.get('URLList'):
                temp_model = DetectPancRequestURLList()
                self.urllist.append(temp_model.from_map(k))
        return self


class DetectPancAdvanceRequestURLList(TeaModel):
    def __init__(
        self,
        urlobject: BinaryIO = None,
    ):
        self.urlobject = urlobject

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.urlobject is not None:
            result['URL'] = self.urlobject
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('URL') is not None:
            self.urlobject = m.get('URL')
        return self


class DetectPancAdvanceRequest(TeaModel):
    def __init__(
        self,
        data_source_type: str = None,
        urllist: List[DetectPancAdvanceRequestURLList] = None,
    ):
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
        if self.data_source_type is not None:
            result['DataSourceType'] = self.data_source_type
        result['URLList'] = []
        if self.urllist is not None:
            for k in self.urllist:
                result['URLList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSourceType') is not None:
            self.data_source_type = m.get('DataSourceType')
        self.urllist = []
        if m.get('URLList') is not None:
            for k in m.get('URLList'):
                temp_model = DetectPancAdvanceRequestURLList()
                self.urllist.append(temp_model.from_map(k))
        return self


class DetectPancResponseBodyDataLesion(TeaModel):
    def __init__(
        self,
        mask: str = None,
        non_pdac_vol: str = None,
        panc_vol: str = None,
        pdac_vol: str = None,
        possibilities: List[str] = None,
    ):
        self.mask = mask
        self.non_pdac_vol = non_pdac_vol
        self.panc_vol = panc_vol
        self.pdac_vol = pdac_vol
        self.possibilities = possibilities

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mask is not None:
            result['Mask'] = self.mask
        if self.non_pdac_vol is not None:
            result['NonPdacVol'] = self.non_pdac_vol
        if self.panc_vol is not None:
            result['PancVol'] = self.panc_vol
        if self.pdac_vol is not None:
            result['PdacVol'] = self.pdac_vol
        if self.possibilities is not None:
            result['Possibilities'] = self.possibilities
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Mask') is not None:
            self.mask = m.get('Mask')
        if m.get('NonPdacVol') is not None:
            self.non_pdac_vol = m.get('NonPdacVol')
        if m.get('PancVol') is not None:
            self.panc_vol = m.get('PancVol')
        if m.get('PdacVol') is not None:
            self.pdac_vol = m.get('PdacVol')
        if m.get('Possibilities') is not None:
            self.possibilities = m.get('Possibilities')
        return self


class DetectPancResponseBodyData(TeaModel):
    def __init__(
        self,
        lesion: DetectPancResponseBodyDataLesion = None,
    ):
        self.lesion = lesion

    def validate(self):
        if self.lesion:
            self.lesion.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lesion is not None:
            result['Lesion'] = self.lesion.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lesion') is not None:
            temp_model = DetectPancResponseBodyDataLesion()
            self.lesion = temp_model.from_map(m['Lesion'])
        return self


class DetectPancResponseBody(TeaModel):
    def __init__(
        self,
        data: DetectPancResponseBodyData = None,
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
            temp_model = DetectPancResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DetectPancResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DetectPancResponseBody = None,
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
            temp_model = DetectPancResponseBody()
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
        org_id: str = None,
        org_name: str = None,
        source_type: str = None,
        urllist: List[DetectRibFractureRequestURLList] = None,
    ):
        self.data_format = data_format
        self.org_id = org_id
        self.org_name = org_name
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
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.org_name is not None:
            result['OrgName'] = self.org_name
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
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('OrgName') is not None:
            self.org_name = m.get('OrgName')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        self.urllist = []
        if m.get('URLList') is not None:
            for k in m.get('URLList'):
                temp_model = DetectRibFractureRequestURLList()
                self.urllist.append(temp_model.from_map(k))
        return self


class DetectRibFractureAdvanceRequestURLList(TeaModel):
    def __init__(
        self,
        urlobject: BinaryIO = None,
    ):
        self.urlobject = urlobject

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.urlobject is not None:
            result['URL'] = self.urlobject
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('URL') is not None:
            self.urlobject = m.get('URL')
        return self


class DetectRibFractureAdvanceRequest(TeaModel):
    def __init__(
        self,
        data_format: str = None,
        org_id: str = None,
        org_name: str = None,
        source_type: str = None,
        urllist: List[DetectRibFractureAdvanceRequestURLList] = None,
    ):
        self.data_format = data_format
        self.org_id = org_id
        self.org_name = org_name
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
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.org_name is not None:
            result['OrgName'] = self.org_name
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
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('OrgName') is not None:
            self.org_name = m.get('OrgName')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        self.urllist = []
        if m.get('URLList') is not None:
            for k in m.get('URLList'):
                temp_model = DetectRibFractureAdvanceRequestURLList()
                self.urllist.append(temp_model.from_map(k))
        return self


class DetectRibFractureResponseBodyDataDetections(TeaModel):
    def __init__(
        self,
        coordinate_image: List[int] = None,
        coordinates: List[int] = None,
        frac_sopinstance_uid: str = None,
        fracture_category: str = None,
        fracture_confidence: float = None,
        fracture_id: int = None,
        fracture_location: str = None,
        fracture_segment: int = None,
    ):
        self.coordinate_image = coordinate_image
        self.coordinates = coordinates
        self.frac_sopinstance_uid = frac_sopinstance_uid
        self.fracture_category = fracture_category
        self.fracture_confidence = fracture_confidence
        self.fracture_id = fracture_id
        self.fracture_location = fracture_location
        self.fracture_segment = fracture_segment

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.coordinate_image is not None:
            result['CoordinateImage'] = self.coordinate_image
        if self.coordinates is not None:
            result['Coordinates'] = self.coordinates
        if self.frac_sopinstance_uid is not None:
            result['FracSOPInstanceUID'] = self.frac_sopinstance_uid
        if self.fracture_category is not None:
            result['FractureCategory'] = self.fracture_category
        if self.fracture_confidence is not None:
            result['FractureConfidence'] = self.fracture_confidence
        if self.fracture_id is not None:
            result['FractureId'] = self.fracture_id
        if self.fracture_location is not None:
            result['FractureLocation'] = self.fracture_location
        if self.fracture_segment is not None:
            result['FractureSegment'] = self.fracture_segment
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CoordinateImage') is not None:
            self.coordinate_image = m.get('CoordinateImage')
        if m.get('Coordinates') is not None:
            self.coordinates = m.get('Coordinates')
        if m.get('FracSOPInstanceUID') is not None:
            self.frac_sopinstance_uid = m.get('FracSOPInstanceUID')
        if m.get('FractureCategory') is not None:
            self.fracture_category = m.get('FractureCategory')
        if m.get('FractureConfidence') is not None:
            self.fracture_confidence = m.get('FractureConfidence')
        if m.get('FractureId') is not None:
            self.fracture_id = m.get('FractureId')
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
        data: DetectRibFractureResponseBodyData = None,
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
            temp_model = DetectRibFractureResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DetectRibFractureResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DetectRibFractureResponseBody = None,
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
            temp_model = DetectRibFractureResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetectSkinDiseaseRequest(TeaModel):
    def __init__(
        self,
        org_id: str = None,
        org_name: str = None,
        url: str = None,
    ):
        self.org_id = org_id
        self.org_name = org_name
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.org_name is not None:
            result['OrgName'] = self.org_name
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('OrgName') is not None:
            self.org_name = m.get('OrgName')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class DetectSkinDiseaseAdvanceRequest(TeaModel):
    def __init__(
        self,
        org_id: str = None,
        org_name: str = None,
        url_object: BinaryIO = None,
    ):
        self.org_id = org_id
        self.org_name = org_name
        self.url_object = url_object

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.org_name is not None:
            result['OrgName'] = self.org_name
        if self.url_object is not None:
            result['Url'] = self.url_object
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('OrgName') is not None:
            self.org_name = m.get('OrgName')
        if m.get('Url') is not None:
            self.url_object = m.get('Url')
        return self


class DetectSkinDiseaseResponseBodyData(TeaModel):
    def __init__(
        self,
        body_part: str = None,
        image_quality: float = None,
        image_type: str = None,
        results: Dict[str, Any] = None,
        results_english: Dict[str, Any] = None,
    ):
        self.body_part = body_part
        self.image_quality = image_quality
        self.image_type = image_type
        self.results = results
        self.results_english = results_english

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body_part is not None:
            result['BodyPart'] = self.body_part
        if self.image_quality is not None:
            result['ImageQuality'] = self.image_quality
        if self.image_type is not None:
            result['ImageType'] = self.image_type
        if self.results is not None:
            result['Results'] = self.results
        if self.results_english is not None:
            result['ResultsEnglish'] = self.results_english
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BodyPart') is not None:
            self.body_part = m.get('BodyPart')
        if m.get('ImageQuality') is not None:
            self.image_quality = m.get('ImageQuality')
        if m.get('ImageType') is not None:
            self.image_type = m.get('ImageType')
        if m.get('Results') is not None:
            self.results = m.get('Results')
        if m.get('ResultsEnglish') is not None:
            self.results_english = m.get('ResultsEnglish')
        return self


class DetectSkinDiseaseResponseBody(TeaModel):
    def __init__(
        self,
        data: DetectSkinDiseaseResponseBodyData = None,
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
            temp_model = DetectSkinDiseaseResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DetectSkinDiseaseResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DetectSkinDiseaseResponseBody = None,
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
            temp_model = DetectSkinDiseaseResponseBody()
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
        org_id: str = None,
        org_name: str = None,
        urllist: List[DetectSpineMRIRequestURLList] = None,
    ):
        self.data_format = data_format
        self.org_id = org_id
        self.org_name = org_name
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
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.org_name is not None:
            result['OrgName'] = self.org_name
        result['URLList'] = []
        if self.urllist is not None:
            for k in self.urllist:
                result['URLList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataFormat') is not None:
            self.data_format = m.get('DataFormat')
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('OrgName') is not None:
            self.org_name = m.get('OrgName')
        self.urllist = []
        if m.get('URLList') is not None:
            for k in m.get('URLList'):
                temp_model = DetectSpineMRIRequestURLList()
                self.urllist.append(temp_model.from_map(k))
        return self


class DetectSpineMRIAdvanceRequestURLList(TeaModel):
    def __init__(
        self,
        urlobject: BinaryIO = None,
    ):
        self.urlobject = urlobject

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.urlobject is not None:
            result['URL'] = self.urlobject
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('URL') is not None:
            self.urlobject = m.get('URL')
        return self


class DetectSpineMRIAdvanceRequest(TeaModel):
    def __init__(
        self,
        data_format: str = None,
        org_id: str = None,
        org_name: str = None,
        urllist: List[DetectSpineMRIAdvanceRequestURLList] = None,
    ):
        self.data_format = data_format
        self.org_id = org_id
        self.org_name = org_name
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
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.org_name is not None:
            result['OrgName'] = self.org_name
        result['URLList'] = []
        if self.urllist is not None:
            for k in self.urllist:
                result['URLList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataFormat') is not None:
            self.data_format = m.get('DataFormat')
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('OrgName') is not None:
            self.org_name = m.get('OrgName')
        self.urllist = []
        if m.get('URLList') is not None:
            for k in m.get('URLList'):
                temp_model = DetectSpineMRIAdvanceRequestURLList()
                self.urllist.append(temp_model.from_map(k))
        return self


class DetectSpineMRIResponseBodyDataDiscs(TeaModel):
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
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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


class DetectSpineMRIResponseBodyDataVertebras(TeaModel):
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
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        data: DetectSpineMRIResponseBodyData = None,
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
            temp_model = DetectSpineMRIResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DetectSpineMRIResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DetectSpineMRIResponseBody = None,
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
            temp_model = DetectSpineMRIResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FeedbackSessionRequest(TeaModel):
    def __init__(
        self,
        feedback: str = None,
        session_id: str = None,
    ):
        self.feedback = feedback
        self.session_id = session_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.feedback is not None:
            result['Feedback'] = self.feedback
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Feedback') is not None:
            self.feedback = m.get('Feedback')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        return self


class FeedbackSessionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
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


class FeedbackSessionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: FeedbackSessionResponseBody = None,
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
            temp_model = FeedbackSessionResponseBody()
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


class RunCTRegistrationRequest(TeaModel):
    def __init__(
        self,
        data_format: str = None,
        data_source_type: str = None,
        floating_list: List[RunCTRegistrationRequestFloatingList] = None,
        org_id: str = None,
        org_name: str = None,
        reference_list: List[RunCTRegistrationRequestReferenceList] = None,
    ):
        # DICOM。
        self.data_format = data_format
        self.data_source_type = data_source_type
        self.floating_list = floating_list
        self.org_id = org_id
        self.org_name = org_name
        self.reference_list = reference_list

    def validate(self):
        if self.floating_list:
            for k in self.floating_list:
                if k:
                    k.validate()
        if self.reference_list:
            for k in self.reference_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_format is not None:
            result['DataFormat'] = self.data_format
        if self.data_source_type is not None:
            result['DataSourceType'] = self.data_source_type
        result['FloatingList'] = []
        if self.floating_list is not None:
            for k in self.floating_list:
                result['FloatingList'].append(k.to_map() if k else None)
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.org_name is not None:
            result['OrgName'] = self.org_name
        result['ReferenceList'] = []
        if self.reference_list is not None:
            for k in self.reference_list:
                result['ReferenceList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataFormat') is not None:
            self.data_format = m.get('DataFormat')
        if m.get('DataSourceType') is not None:
            self.data_source_type = m.get('DataSourceType')
        self.floating_list = []
        if m.get('FloatingList') is not None:
            for k in m.get('FloatingList'):
                temp_model = RunCTRegistrationRequestFloatingList()
                self.floating_list.append(temp_model.from_map(k))
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('OrgName') is not None:
            self.org_name = m.get('OrgName')
        self.reference_list = []
        if m.get('ReferenceList') is not None:
            for k in m.get('ReferenceList'):
                temp_model = RunCTRegistrationRequestReferenceList()
                self.reference_list.append(temp_model.from_map(k))
        return self


class RunCTRegistrationAdvanceRequestFloatingList(TeaModel):
    def __init__(
        self,
        floating_urlobject: BinaryIO = None,
    ):
        self.floating_urlobject = floating_urlobject

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.floating_urlobject is not None:
            result['FloatingURL'] = self.floating_urlobject
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FloatingURL') is not None:
            self.floating_urlobject = m.get('FloatingURL')
        return self


class RunCTRegistrationAdvanceRequestReferenceList(TeaModel):
    def __init__(
        self,
        reference_urlobject: BinaryIO = None,
    ):
        self.reference_urlobject = reference_urlobject

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.reference_urlobject is not None:
            result['ReferenceURL'] = self.reference_urlobject
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReferenceURL') is not None:
            self.reference_urlobject = m.get('ReferenceURL')
        return self


class RunCTRegistrationAdvanceRequest(TeaModel):
    def __init__(
        self,
        data_format: str = None,
        data_source_type: str = None,
        floating_list: List[RunCTRegistrationAdvanceRequestFloatingList] = None,
        org_id: str = None,
        org_name: str = None,
        reference_list: List[RunCTRegistrationAdvanceRequestReferenceList] = None,
    ):
        # DICOM。
        self.data_format = data_format
        self.data_source_type = data_source_type
        self.floating_list = floating_list
        self.org_id = org_id
        self.org_name = org_name
        self.reference_list = reference_list

    def validate(self):
        if self.floating_list:
            for k in self.floating_list:
                if k:
                    k.validate()
        if self.reference_list:
            for k in self.reference_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_format is not None:
            result['DataFormat'] = self.data_format
        if self.data_source_type is not None:
            result['DataSourceType'] = self.data_source_type
        result['FloatingList'] = []
        if self.floating_list is not None:
            for k in self.floating_list:
                result['FloatingList'].append(k.to_map() if k else None)
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.org_name is not None:
            result['OrgName'] = self.org_name
        result['ReferenceList'] = []
        if self.reference_list is not None:
            for k in self.reference_list:
                result['ReferenceList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataFormat') is not None:
            self.data_format = m.get('DataFormat')
        if m.get('DataSourceType') is not None:
            self.data_source_type = m.get('DataSourceType')
        self.floating_list = []
        if m.get('FloatingList') is not None:
            for k in m.get('FloatingList'):
                temp_model = RunCTRegistrationAdvanceRequestFloatingList()
                self.floating_list.append(temp_model.from_map(k))
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('OrgName') is not None:
            self.org_name = m.get('OrgName')
        self.reference_list = []
        if m.get('ReferenceList') is not None:
            for k in m.get('ReferenceList'):
                temp_model = RunCTRegistrationAdvanceRequestReferenceList()
                self.reference_list.append(temp_model.from_map(k))
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
        data: RunCTRegistrationResponseBodyData = None,
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
            temp_model = RunCTRegistrationResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RunCTRegistrationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RunCTRegistrationResponseBody = None,
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
            temp_model = RunCTRegistrationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RunMedQARequestAnswerImageDataList(TeaModel):
    def __init__(
        self,
        answer_image_data: str = None,
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
        answer_image_data_list: List[RunMedQARequestAnswerImageDataList] = None,
        answer_image_urllist: List[RunMedQARequestAnswerImageURLList] = None,
        answer_text_list: List[RunMedQARequestAnswerTextList] = None,
        department: str = None,
        org_id: str = None,
        org_name: str = None,
        question_type: str = None,
        session_id: str = None,
    ):
        self.answer_image_data_list = answer_image_data_list
        self.answer_image_urllist = answer_image_urllist
        self.answer_text_list = answer_text_list
        self.department = department
        self.org_id = org_id
        self.org_name = org_name
        self.question_type = question_type
        self.session_id = session_id

    def validate(self):
        if self.answer_image_data_list:
            for k in self.answer_image_data_list:
                if k:
                    k.validate()
        if self.answer_image_urllist:
            for k in self.answer_image_urllist:
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
        result['AnswerImageDataList'] = []
        if self.answer_image_data_list is not None:
            for k in self.answer_image_data_list:
                result['AnswerImageDataList'].append(k.to_map() if k else None)
        result['AnswerImageURLList'] = []
        if self.answer_image_urllist is not None:
            for k in self.answer_image_urllist:
                result['AnswerImageURLList'].append(k.to_map() if k else None)
        result['AnswerTextList'] = []
        if self.answer_text_list is not None:
            for k in self.answer_text_list:
                result['AnswerTextList'].append(k.to_map() if k else None)
        if self.department is not None:
            result['Department'] = self.department
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.org_name is not None:
            result['OrgName'] = self.org_name
        if self.question_type is not None:
            result['QuestionType'] = self.question_type
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.answer_image_data_list = []
        if m.get('AnswerImageDataList') is not None:
            for k in m.get('AnswerImageDataList'):
                temp_model = RunMedQARequestAnswerImageDataList()
                self.answer_image_data_list.append(temp_model.from_map(k))
        self.answer_image_urllist = []
        if m.get('AnswerImageURLList') is not None:
            for k in m.get('AnswerImageURLList'):
                temp_model = RunMedQARequestAnswerImageURLList()
                self.answer_image_urllist.append(temp_model.from_map(k))
        self.answer_text_list = []
        if m.get('AnswerTextList') is not None:
            for k in m.get('AnswerTextList'):
                temp_model = RunMedQARequestAnswerTextList()
                self.answer_text_list.append(temp_model.from_map(k))
        if m.get('Department') is not None:
            self.department = m.get('Department')
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('OrgName') is not None:
            self.org_name = m.get('OrgName')
        if m.get('QuestionType') is not None:
            self.question_type = m.get('QuestionType')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        return self


class RunMedQAAdvanceRequestAnswerImageDataList(TeaModel):
    def __init__(
        self,
        answer_image_data: str = None,
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


class RunMedQAAdvanceRequestAnswerImageURLList(TeaModel):
    def __init__(
        self,
        answer_image_urlobject: BinaryIO = None,
    ):
        self.answer_image_urlobject = answer_image_urlobject

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.answer_image_urlobject is not None:
            result['AnswerImageURL'] = self.answer_image_urlobject
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AnswerImageURL') is not None:
            self.answer_image_urlobject = m.get('AnswerImageURL')
        return self


class RunMedQAAdvanceRequestAnswerTextList(TeaModel):
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


class RunMedQAAdvanceRequest(TeaModel):
    def __init__(
        self,
        answer_image_data_list: List[RunMedQAAdvanceRequestAnswerImageDataList] = None,
        answer_image_urllist: List[RunMedQAAdvanceRequestAnswerImageURLList] = None,
        answer_text_list: List[RunMedQAAdvanceRequestAnswerTextList] = None,
        department: str = None,
        org_id: str = None,
        org_name: str = None,
        question_type: str = None,
        session_id: str = None,
    ):
        self.answer_image_data_list = answer_image_data_list
        self.answer_image_urllist = answer_image_urllist
        self.answer_text_list = answer_text_list
        self.department = department
        self.org_id = org_id
        self.org_name = org_name
        self.question_type = question_type
        self.session_id = session_id

    def validate(self):
        if self.answer_image_data_list:
            for k in self.answer_image_data_list:
                if k:
                    k.validate()
        if self.answer_image_urllist:
            for k in self.answer_image_urllist:
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
        result['AnswerImageDataList'] = []
        if self.answer_image_data_list is not None:
            for k in self.answer_image_data_list:
                result['AnswerImageDataList'].append(k.to_map() if k else None)
        result['AnswerImageURLList'] = []
        if self.answer_image_urllist is not None:
            for k in self.answer_image_urllist:
                result['AnswerImageURLList'].append(k.to_map() if k else None)
        result['AnswerTextList'] = []
        if self.answer_text_list is not None:
            for k in self.answer_text_list:
                result['AnswerTextList'].append(k.to_map() if k else None)
        if self.department is not None:
            result['Department'] = self.department
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.org_name is not None:
            result['OrgName'] = self.org_name
        if self.question_type is not None:
            result['QuestionType'] = self.question_type
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.answer_image_data_list = []
        if m.get('AnswerImageDataList') is not None:
            for k in m.get('AnswerImageDataList'):
                temp_model = RunMedQAAdvanceRequestAnswerImageDataList()
                self.answer_image_data_list.append(temp_model.from_map(k))
        self.answer_image_urllist = []
        if m.get('AnswerImageURLList') is not None:
            for k in m.get('AnswerImageURLList'):
                temp_model = RunMedQAAdvanceRequestAnswerImageURLList()
                self.answer_image_urllist.append(temp_model.from_map(k))
        self.answer_text_list = []
        if m.get('AnswerTextList') is not None:
            for k in m.get('AnswerTextList'):
                temp_model = RunMedQAAdvanceRequestAnswerTextList()
                self.answer_text_list.append(temp_model.from_map(k))
        if m.get('Department') is not None:
            self.department = m.get('Department')
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('OrgName') is not None:
            self.org_name = m.get('OrgName')
        if m.get('QuestionType') is not None:
            self.question_type = m.get('QuestionType')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        return self


class RunMedQAResponseBodyData(TeaModel):
    def __init__(
        self,
        answer_type: str = None,
        options: List[str] = None,
        question: str = None,
        question_type: str = None,
        reports: Dict[str, str] = None,
        session_id: str = None,
    ):
        self.answer_type = answer_type
        self.options = options
        self.question = question
        self.question_type = question_type
        self.reports = reports
        self.session_id = session_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.answer_type is not None:
            result['AnswerType'] = self.answer_type
        if self.options is not None:
            result['Options'] = self.options
        if self.question is not None:
            result['Question'] = self.question
        if self.question_type is not None:
            result['QuestionType'] = self.question_type
        if self.reports is not None:
            result['Reports'] = self.reports
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AnswerType') is not None:
            self.answer_type = m.get('AnswerType')
        if m.get('Options') is not None:
            self.options = m.get('Options')
        if m.get('Question') is not None:
            self.question = m.get('Question')
        if m.get('QuestionType') is not None:
            self.question_type = m.get('QuestionType')
        if m.get('Reports') is not None:
            self.reports = m.get('Reports')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        return self


class RunMedQAResponseBody(TeaModel):
    def __init__(
        self,
        data: RunMedQAResponseBodyData = None,
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
            temp_model = RunMedQAResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RunMedQAResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RunMedQAResponseBody = None,
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
            temp_model = RunMedQAResponseBody()
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
        mask: int = None,
        org_id: str = None,
        org_name: str = None,
        urllist: List[ScreenChestCTRequestURLList] = None,
        verbose: int = None,
    ):
        self.data_format = data_format
        self.mask = mask
        self.org_id = org_id
        self.org_name = org_name
        self.urllist = urllist
        self.verbose = verbose

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
        if self.mask is not None:
            result['Mask'] = self.mask
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.org_name is not None:
            result['OrgName'] = self.org_name
        result['URLList'] = []
        if self.urllist is not None:
            for k in self.urllist:
                result['URLList'].append(k.to_map() if k else None)
        if self.verbose is not None:
            result['Verbose'] = self.verbose
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataFormat') is not None:
            self.data_format = m.get('DataFormat')
        if m.get('Mask') is not None:
            self.mask = m.get('Mask')
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('OrgName') is not None:
            self.org_name = m.get('OrgName')
        self.urllist = []
        if m.get('URLList') is not None:
            for k in m.get('URLList'):
                temp_model = ScreenChestCTRequestURLList()
                self.urllist.append(temp_model.from_map(k))
        if m.get('Verbose') is not None:
            self.verbose = m.get('Verbose')
        return self


class ScreenChestCTAdvanceRequestURLList(TeaModel):
    def __init__(
        self,
        urlobject: BinaryIO = None,
    ):
        self.urlobject = urlobject

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.urlobject is not None:
            result['URL'] = self.urlobject
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('URL') is not None:
            self.urlobject = m.get('URL')
        return self


class ScreenChestCTAdvanceRequest(TeaModel):
    def __init__(
        self,
        data_format: str = None,
        mask: int = None,
        org_id: str = None,
        org_name: str = None,
        urllist: List[ScreenChestCTAdvanceRequestURLList] = None,
        verbose: int = None,
    ):
        self.data_format = data_format
        self.mask = mask
        self.org_id = org_id
        self.org_name = org_name
        self.urllist = urllist
        self.verbose = verbose

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
        if self.mask is not None:
            result['Mask'] = self.mask
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.org_name is not None:
            result['OrgName'] = self.org_name
        result['URLList'] = []
        if self.urllist is not None:
            for k in self.urllist:
                result['URLList'].append(k.to_map() if k else None)
        if self.verbose is not None:
            result['Verbose'] = self.verbose
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataFormat') is not None:
            self.data_format = m.get('DataFormat')
        if m.get('Mask') is not None:
            self.mask = m.get('Mask')
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('OrgName') is not None:
            self.org_name = m.get('OrgName')
        self.urllist = []
        if m.get('URLList') is not None:
            for k in m.get('URLList'):
                temp_model = ScreenChestCTAdvanceRequestURLList()
                self.urllist.append(temp_model.from_map(k))
        if m.get('Verbose') is not None:
            self.verbose = m.get('Verbose')
        return self


class ScreenChestCTResponseBodyDataAnalyzeChestVesselAortaInfo(TeaModel):
    def __init__(
        self,
        area: List[float] = None,
        coordinates: List[List[float]] = None,
        label_value: int = None,
        max_area: float = None,
        max_area_index: int = None,
        max_diameter: float = None,
    ):
        self.area = area
        self.coordinates = coordinates
        self.label_value = label_value
        self.max_area = max_area
        self.max_area_index = max_area_index
        self.max_diameter = max_diameter

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.area is not None:
            result['Area'] = self.area
        if self.coordinates is not None:
            result['Coordinates'] = self.coordinates
        if self.label_value is not None:
            result['LabelValue'] = self.label_value
        if self.max_area is not None:
            result['MaxArea'] = self.max_area
        if self.max_area_index is not None:
            result['MaxAreaIndex'] = self.max_area_index
        if self.max_diameter is not None:
            result['MaxDiameter'] = self.max_diameter
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Area') is not None:
            self.area = m.get('Area')
        if m.get('Coordinates') is not None:
            self.coordinates = m.get('Coordinates')
        if m.get('LabelValue') is not None:
            self.label_value = m.get('LabelValue')
        if m.get('MaxArea') is not None:
            self.max_area = m.get('MaxArea')
        if m.get('MaxAreaIndex') is not None:
            self.max_area_index = m.get('MaxAreaIndex')
        if m.get('MaxDiameter') is not None:
            self.max_diameter = m.get('MaxDiameter')
        return self


class ScreenChestCTResponseBodyDataAnalyzeChestVesselPulmonaryInfo(TeaModel):
    def __init__(
        self,
        area: List[float] = None,
        coordinates: List[List[float]] = None,
        label_value: int = None,
        max_area: float = None,
        max_area_index: int = None,
        max_diameter: float = None,
        nearest_aorta_area: float = None,
    ):
        self.area = area
        self.coordinates = coordinates
        self.label_value = label_value
        self.max_area = max_area
        self.max_area_index = max_area_index
        self.max_diameter = max_diameter
        self.nearest_aorta_area = nearest_aorta_area

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.area is not None:
            result['Area'] = self.area
        if self.coordinates is not None:
            result['Coordinates'] = self.coordinates
        if self.label_value is not None:
            result['LabelValue'] = self.label_value
        if self.max_area is not None:
            result['MaxArea'] = self.max_area
        if self.max_area_index is not None:
            result['MaxAreaIndex'] = self.max_area_index
        if self.max_diameter is not None:
            result['MaxDiameter'] = self.max_diameter
        if self.nearest_aorta_area is not None:
            result['NearestAortaArea'] = self.nearest_aorta_area
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Area') is not None:
            self.area = m.get('Area')
        if m.get('Coordinates') is not None:
            self.coordinates = m.get('Coordinates')
        if m.get('LabelValue') is not None:
            self.label_value = m.get('LabelValue')
        if m.get('MaxArea') is not None:
            self.max_area = m.get('MaxArea')
        if m.get('MaxAreaIndex') is not None:
            self.max_area_index = m.get('MaxAreaIndex')
        if m.get('MaxDiameter') is not None:
            self.max_diameter = m.get('MaxDiameter')
        if m.get('NearestAortaArea') is not None:
            self.nearest_aorta_area = m.get('NearestAortaArea')
        return self


class ScreenChestCTResponseBodyDataAnalyzeChestVessel(TeaModel):
    def __init__(
        self,
        aorta_info: ScreenChestCTResponseBodyDataAnalyzeChestVesselAortaInfo = None,
        pulmonary_info: ScreenChestCTResponseBodyDataAnalyzeChestVesselPulmonaryInfo = None,
        result_url: str = None,
    ):
        self.aorta_info = aorta_info
        self.pulmonary_info = pulmonary_info
        self.result_url = result_url

    def validate(self):
        if self.aorta_info:
            self.aorta_info.validate()
        if self.pulmonary_info:
            self.pulmonary_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aorta_info is not None:
            result['AortaInfo'] = self.aorta_info.to_map()
        if self.pulmonary_info is not None:
            result['PulmonaryInfo'] = self.pulmonary_info.to_map()
        if self.result_url is not None:
            result['ResultURL'] = self.result_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AortaInfo') is not None:
            temp_model = ScreenChestCTResponseBodyDataAnalyzeChestVesselAortaInfo()
            self.aorta_info = temp_model.from_map(m['AortaInfo'])
        if m.get('PulmonaryInfo') is not None:
            temp_model = ScreenChestCTResponseBodyDataAnalyzeChestVesselPulmonaryInfo()
            self.pulmonary_info = temp_model.from_map(m['PulmonaryInfo'])
        if m.get('ResultURL') is not None:
            self.result_url = m.get('ResultURL')
        return self


class ScreenChestCTResponseBodyDataCACSDetections(TeaModel):
    def __init__(
        self,
        calcium_center: List[int] = None,
        calcium_id: int = None,
        calcium_score: float = None,
        calcium_volume: float = None,
    ):
        self.calcium_center = calcium_center
        self.calcium_id = calcium_id
        self.calcium_score = calcium_score
        self.calcium_volume = calcium_volume

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.calcium_center is not None:
            result['CalciumCenter'] = self.calcium_center
        if self.calcium_id is not None:
            result['CalciumId'] = self.calcium_id
        if self.calcium_score is not None:
            result['CalciumScore'] = self.calcium_score
        if self.calcium_volume is not None:
            result['CalciumVolume'] = self.calcium_volume
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CalciumCenter') is not None:
            self.calcium_center = m.get('CalciumCenter')
        if m.get('CalciumId') is not None:
            self.calcium_id = m.get('CalciumId')
        if m.get('CalciumScore') is not None:
            self.calcium_score = m.get('CalciumScore')
        if m.get('CalciumVolume') is not None:
            self.calcium_volume = m.get('CalciumVolume')
        return self


class ScreenChestCTResponseBodyDataCACS(TeaModel):
    def __init__(
        self,
        detections: List[ScreenChestCTResponseBodyDataCACSDetections] = None,
        result_url: str = None,
        score: str = None,
        series_instance_uid: str = None,
        volume_score: str = None,
    ):
        self.detections = detections
        self.result_url = result_url
        self.score = score
        self.series_instance_uid = series_instance_uid
        self.volume_score = volume_score

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
        if self.result_url is not None:
            result['ResultUrl'] = self.result_url
        if self.score is not None:
            result['Score'] = self.score
        if self.series_instance_uid is not None:
            result['SeriesInstanceUID'] = self.series_instance_uid
        if self.volume_score is not None:
            result['VolumeScore'] = self.volume_score
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.detections = []
        if m.get('Detections') is not None:
            for k in m.get('Detections'):
                temp_model = ScreenChestCTResponseBodyDataCACSDetections()
                self.detections.append(temp_model.from_map(k))
        if m.get('ResultUrl') is not None:
            self.result_url = m.get('ResultUrl')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('SeriesInstanceUID') is not None:
            self.series_instance_uid = m.get('SeriesInstanceUID')
        if m.get('VolumeScore') is not None:
            self.volume_score = m.get('VolumeScore')
        return self


class ScreenChestCTResponseBodyDataCovid(TeaModel):
    def __init__(
        self,
        lesion_ratio: str = None,
        mask: str = None,
        new_probability: str = None,
        normal_probability: str = None,
        other_probability: str = None,
        series_instance_uid: str = None,
    ):
        self.lesion_ratio = lesion_ratio
        self.mask = mask
        self.new_probability = new_probability
        self.normal_probability = normal_probability
        self.other_probability = other_probability
        self.series_instance_uid = series_instance_uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lesion_ratio is not None:
            result['LesionRatio'] = self.lesion_ratio
        if self.mask is not None:
            result['Mask'] = self.mask
        if self.new_probability is not None:
            result['NewProbability'] = self.new_probability
        if self.normal_probability is not None:
            result['NormalProbability'] = self.normal_probability
        if self.other_probability is not None:
            result['OtherProbability'] = self.other_probability
        if self.series_instance_uid is not None:
            result['SeriesInstanceUID'] = self.series_instance_uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LesionRatio') is not None:
            self.lesion_ratio = m.get('LesionRatio')
        if m.get('Mask') is not None:
            self.mask = m.get('Mask')
        if m.get('NewProbability') is not None:
            self.new_probability = m.get('NewProbability')
        if m.get('NormalProbability') is not None:
            self.normal_probability = m.get('NormalProbability')
        if m.get('OtherProbability') is not None:
            self.other_probability = m.get('OtherProbability')
        if m.get('SeriesInstanceUID') is not None:
            self.series_instance_uid = m.get('SeriesInstanceUID')
        return self


class ScreenChestCTResponseBodyDataDetectLymphLesions(TeaModel):
    def __init__(
        self,
        boxes: List[float] = None,
        diametermm: List[float] = None,
        key_slice: int = None,
        recist: List[List[float]] = None,
        score: float = None,
    ):
        self.boxes = boxes
        self.diametermm = diametermm
        self.key_slice = key_slice
        self.recist = recist
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
        if self.diametermm is not None:
            result['Diametermm'] = self.diametermm
        if self.key_slice is not None:
            result['KeySlice'] = self.key_slice
        if self.recist is not None:
            result['Recist'] = self.recist
        if self.score is not None:
            result['Score'] = self.score
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Boxes') is not None:
            self.boxes = m.get('Boxes')
        if m.get('Diametermm') is not None:
            self.diametermm = m.get('Diametermm')
        if m.get('KeySlice') is not None:
            self.key_slice = m.get('KeySlice')
        if m.get('Recist') is not None:
            self.recist = m.get('Recist')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        return self


class ScreenChestCTResponseBodyDataDetectLymph(TeaModel):
    def __init__(
        self,
        lesions: List[ScreenChestCTResponseBodyDataDetectLymphLesions] = None,
        series_instance_uid: str = None,
    ):
        self.lesions = lesions
        self.series_instance_uid = series_instance_uid

    def validate(self):
        if self.lesions:
            for k in self.lesions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Lesions'] = []
        if self.lesions is not None:
            for k in self.lesions:
                result['Lesions'].append(k.to_map() if k else None)
        if self.series_instance_uid is not None:
            result['SeriesInstanceUID'] = self.series_instance_uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.lesions = []
        if m.get('Lesions') is not None:
            for k in m.get('Lesions'):
                temp_model = ScreenChestCTResponseBodyDataDetectLymphLesions()
                self.lesions.append(temp_model.from_map(k))
        if m.get('SeriesInstanceUID') is not None:
            self.series_instance_uid = m.get('SeriesInstanceUID')
        return self


class ScreenChestCTResponseBodyDataDetectPdacLesion(TeaModel):
    def __init__(
        self,
        mask: str = None,
        non_pdac_vol: str = None,
        panc_vol: str = None,
        pdac_vol: str = None,
        possibilities: List[str] = None,
    ):
        self.mask = mask
        self.non_pdac_vol = non_pdac_vol
        self.panc_vol = panc_vol
        self.pdac_vol = pdac_vol
        self.possibilities = possibilities

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mask is not None:
            result['Mask'] = self.mask
        if self.non_pdac_vol is not None:
            result['NonPdacVol'] = self.non_pdac_vol
        if self.panc_vol is not None:
            result['PancVol'] = self.panc_vol
        if self.pdac_vol is not None:
            result['PdacVol'] = self.pdac_vol
        if self.possibilities is not None:
            result['Possibilities'] = self.possibilities
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Mask') is not None:
            self.mask = m.get('Mask')
        if m.get('NonPdacVol') is not None:
            self.non_pdac_vol = m.get('NonPdacVol')
        if m.get('PancVol') is not None:
            self.panc_vol = m.get('PancVol')
        if m.get('PdacVol') is not None:
            self.pdac_vol = m.get('PdacVol')
        if m.get('Possibilities') is not None:
            self.possibilities = m.get('Possibilities')
        return self


class ScreenChestCTResponseBodyDataDetectPdac(TeaModel):
    def __init__(
        self,
        lesion: ScreenChestCTResponseBodyDataDetectPdacLesion = None,
        series_instance_uid: str = None,
    ):
        self.lesion = lesion
        self.series_instance_uid = series_instance_uid

    def validate(self):
        if self.lesion:
            self.lesion.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lesion is not None:
            result['Lesion'] = self.lesion.to_map()
        if self.series_instance_uid is not None:
            result['SeriesInstanceUID'] = self.series_instance_uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lesion') is not None:
            temp_model = ScreenChestCTResponseBodyDataDetectPdacLesion()
            self.lesion = temp_model.from_map(m['Lesion'])
        if m.get('SeriesInstanceUID') is not None:
            self.series_instance_uid = m.get('SeriesInstanceUID')
        return self


class ScreenChestCTResponseBodyDataDetectRibFractureDetections(TeaModel):
    def __init__(
        self,
        coordinate_image: List[int] = None,
        coordinates: List[int] = None,
        frac_sopinstance_uid: str = None,
        fracture_category: int = None,
        fracture_confidence: float = None,
        fracture_id: int = None,
        fracture_location: str = None,
        fracture_segment: int = None,
    ):
        self.coordinate_image = coordinate_image
        self.coordinates = coordinates
        self.frac_sopinstance_uid = frac_sopinstance_uid
        self.fracture_category = fracture_category
        self.fracture_confidence = fracture_confidence
        self.fracture_id = fracture_id
        self.fracture_location = fracture_location
        self.fracture_segment = fracture_segment

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.coordinate_image is not None:
            result['CoordinateImage'] = self.coordinate_image
        if self.coordinates is not None:
            result['Coordinates'] = self.coordinates
        if self.frac_sopinstance_uid is not None:
            result['FracSOPInstanceUID'] = self.frac_sopinstance_uid
        if self.fracture_category is not None:
            result['FractureCategory'] = self.fracture_category
        if self.fracture_confidence is not None:
            result['FractureConfidence'] = self.fracture_confidence
        if self.fracture_id is not None:
            result['FractureId'] = self.fracture_id
        if self.fracture_location is not None:
            result['FractureLocation'] = self.fracture_location
        if self.fracture_segment is not None:
            result['FractureSegment'] = self.fracture_segment
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CoordinateImage') is not None:
            self.coordinate_image = m.get('CoordinateImage')
        if m.get('Coordinates') is not None:
            self.coordinates = m.get('Coordinates')
        if m.get('FracSOPInstanceUID') is not None:
            self.frac_sopinstance_uid = m.get('FracSOPInstanceUID')
        if m.get('FractureCategory') is not None:
            self.fracture_category = m.get('FractureCategory')
        if m.get('FractureConfidence') is not None:
            self.fracture_confidence = m.get('FractureConfidence')
        if m.get('FractureId') is not None:
            self.fracture_id = m.get('FractureId')
        if m.get('FractureLocation') is not None:
            self.fracture_location = m.get('FractureLocation')
        if m.get('FractureSegment') is not None:
            self.fracture_segment = m.get('FractureSegment')
        return self


class ScreenChestCTResponseBodyDataDetectRibFracture(TeaModel):
    def __init__(
        self,
        detections: List[ScreenChestCTResponseBodyDataDetectRibFractureDetections] = None,
        fracture_mask_url: str = None,
        origin: List[float] = None,
        result_url: str = None,
        rib_segment_mask_url: str = None,
        series_instance_uid: str = None,
        spacing: List[float] = None,
    ):
        self.detections = detections
        self.fracture_mask_url = fracture_mask_url
        self.origin = origin
        self.result_url = result_url
        self.rib_segment_mask_url = rib_segment_mask_url
        self.series_instance_uid = series_instance_uid
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
        if self.fracture_mask_url is not None:
            result['FractureMaskURL'] = self.fracture_mask_url
        if self.origin is not None:
            result['Origin'] = self.origin
        if self.result_url is not None:
            result['ResultURL'] = self.result_url
        if self.rib_segment_mask_url is not None:
            result['RibSegmentMaskURL'] = self.rib_segment_mask_url
        if self.series_instance_uid is not None:
            result['SeriesInstanceUID'] = self.series_instance_uid
        if self.spacing is not None:
            result['Spacing'] = self.spacing
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.detections = []
        if m.get('Detections') is not None:
            for k in m.get('Detections'):
                temp_model = ScreenChestCTResponseBodyDataDetectRibFractureDetections()
                self.detections.append(temp_model.from_map(k))
        if m.get('FractureMaskURL') is not None:
            self.fracture_mask_url = m.get('FractureMaskURL')
        if m.get('Origin') is not None:
            self.origin = m.get('Origin')
        if m.get('ResultURL') is not None:
            self.result_url = m.get('ResultURL')
        if m.get('RibSegmentMaskURL') is not None:
            self.rib_segment_mask_url = m.get('RibSegmentMaskURL')
        if m.get('SeriesInstanceUID') is not None:
            self.series_instance_uid = m.get('SeriesInstanceUID')
        if m.get('Spacing') is not None:
            self.spacing = m.get('Spacing')
        return self


class ScreenChestCTResponseBodyDataLungNoduleSeriesElements(TeaModel):
    def __init__(
        self,
        category: str = None,
        confidence: float = None,
        diameter: float = None,
        image_x: float = None,
        image_y: float = None,
        image_z: float = None,
        lobe: str = None,
        lung: str = None,
        major_axis: List[float] = None,
        mean_value: float = None,
        minor_axis: List[float] = None,
        recist_sopinstance_uid: str = None,
        risk: float = None,
        sopinstance_uid: str = None,
        volume: float = None,
        x: float = None,
        y: float = None,
        z: float = None,
    ):
        self.category = category
        self.confidence = confidence
        self.diameter = diameter
        self.image_x = image_x
        self.image_y = image_y
        self.image_z = image_z
        self.lobe = lobe
        self.lung = lung
        self.major_axis = major_axis
        self.mean_value = mean_value
        self.minor_axis = minor_axis
        self.recist_sopinstance_uid = recist_sopinstance_uid
        self.risk = risk
        self.sopinstance_uid = sopinstance_uid
        self.volume = volume
        self.x = x
        self.y = y
        self.z = z

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.confidence is not None:
            result['Confidence'] = self.confidence
        if self.diameter is not None:
            result['Diameter'] = self.diameter
        if self.image_x is not None:
            result['ImageX'] = self.image_x
        if self.image_y is not None:
            result['ImageY'] = self.image_y
        if self.image_z is not None:
            result['ImageZ'] = self.image_z
        if self.lobe is not None:
            result['Lobe'] = self.lobe
        if self.lung is not None:
            result['Lung'] = self.lung
        if self.major_axis is not None:
            result['MajorAxis'] = self.major_axis
        if self.mean_value is not None:
            result['MeanValue'] = self.mean_value
        if self.minor_axis is not None:
            result['MinorAxis'] = self.minor_axis
        if self.recist_sopinstance_uid is not None:
            result['RecistSOPInstanceUID'] = self.recist_sopinstance_uid
        if self.risk is not None:
            result['Risk'] = self.risk
        if self.sopinstance_uid is not None:
            result['SOPInstanceUID'] = self.sopinstance_uid
        if self.volume is not None:
            result['Volume'] = self.volume
        if self.x is not None:
            result['X'] = self.x
        if self.y is not None:
            result['Y'] = self.y
        if self.z is not None:
            result['Z'] = self.z
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Confidence') is not None:
            self.confidence = m.get('Confidence')
        if m.get('Diameter') is not None:
            self.diameter = m.get('Diameter')
        if m.get('ImageX') is not None:
            self.image_x = m.get('ImageX')
        if m.get('ImageY') is not None:
            self.image_y = m.get('ImageY')
        if m.get('ImageZ') is not None:
            self.image_z = m.get('ImageZ')
        if m.get('Lobe') is not None:
            self.lobe = m.get('Lobe')
        if m.get('Lung') is not None:
            self.lung = m.get('Lung')
        if m.get('MajorAxis') is not None:
            self.major_axis = m.get('MajorAxis')
        if m.get('MeanValue') is not None:
            self.mean_value = m.get('MeanValue')
        if m.get('MinorAxis') is not None:
            self.minor_axis = m.get('MinorAxis')
        if m.get('RecistSOPInstanceUID') is not None:
            self.recist_sopinstance_uid = m.get('RecistSOPInstanceUID')
        if m.get('Risk') is not None:
            self.risk = m.get('Risk')
        if m.get('SOPInstanceUID') is not None:
            self.sopinstance_uid = m.get('SOPInstanceUID')
        if m.get('Volume') is not None:
            self.volume = m.get('Volume')
        if m.get('X') is not None:
            self.x = m.get('X')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        if m.get('Z') is not None:
            self.z = m.get('Z')
        return self


class ScreenChestCTResponseBodyDataLungNoduleSeries(TeaModel):
    def __init__(
        self,
        elements: List[ScreenChestCTResponseBodyDataLungNoduleSeriesElements] = None,
        origin: List[float] = None,
        report: str = None,
        series_instance_uid: str = None,
        spacing: List[float] = None,
    ):
        self.elements = elements
        self.origin = origin
        self.report = report
        self.series_instance_uid = series_instance_uid
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
        result['Elements'] = []
        if self.elements is not None:
            for k in self.elements:
                result['Elements'].append(k.to_map() if k else None)
        if self.origin is not None:
            result['Origin'] = self.origin
        if self.report is not None:
            result['Report'] = self.report
        if self.series_instance_uid is not None:
            result['SeriesInstanceUid'] = self.series_instance_uid
        if self.spacing is not None:
            result['Spacing'] = self.spacing
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.elements = []
        if m.get('Elements') is not None:
            for k in m.get('Elements'):
                temp_model = ScreenChestCTResponseBodyDataLungNoduleSeriesElements()
                self.elements.append(temp_model.from_map(k))
        if m.get('Origin') is not None:
            self.origin = m.get('Origin')
        if m.get('Report') is not None:
            self.report = m.get('Report')
        if m.get('SeriesInstanceUid') is not None:
            self.series_instance_uid = m.get('SeriesInstanceUid')
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


class ScreenChestCTResponseBodyDataScreenEcLesion(TeaModel):
    def __init__(
        self,
        benign_volume: str = None,
        ec_volume: str = None,
        eso_volume: str = None,
        mask: str = None,
        possibilities: List[str] = None,
    ):
        self.benign_volume = benign_volume
        self.ec_volume = ec_volume
        self.eso_volume = eso_volume
        self.mask = mask
        self.possibilities = possibilities

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.benign_volume is not None:
            result['BenignVolume'] = self.benign_volume
        if self.ec_volume is not None:
            result['EcVolume'] = self.ec_volume
        if self.eso_volume is not None:
            result['EsoVolume'] = self.eso_volume
        if self.mask is not None:
            result['Mask'] = self.mask
        if self.possibilities is not None:
            result['Possibilities'] = self.possibilities
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BenignVolume') is not None:
            self.benign_volume = m.get('BenignVolume')
        if m.get('EcVolume') is not None:
            self.ec_volume = m.get('EcVolume')
        if m.get('EsoVolume') is not None:
            self.eso_volume = m.get('EsoVolume')
        if m.get('Mask') is not None:
            self.mask = m.get('Mask')
        if m.get('Possibilities') is not None:
            self.possibilities = m.get('Possibilities')
        return self


class ScreenChestCTResponseBodyDataScreenEc(TeaModel):
    def __init__(
        self,
        lesion: ScreenChestCTResponseBodyDataScreenEcLesion = None,
        series_instance_uid: str = None,
    ):
        self.lesion = lesion
        self.series_instance_uid = series_instance_uid

    def validate(self):
        if self.lesion:
            self.lesion.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lesion is not None:
            result['Lesion'] = self.lesion.to_map()
        if self.series_instance_uid is not None:
            result['SeriesInstanceUid'] = self.series_instance_uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lesion') is not None:
            temp_model = ScreenChestCTResponseBodyDataScreenEcLesion()
            self.lesion = temp_model.from_map(m['Lesion'])
        if m.get('SeriesInstanceUid') is not None:
            self.series_instance_uid = m.get('SeriesInstanceUid')
        return self


class ScreenChestCTResponseBodyData(TeaModel):
    def __init__(
        self,
        analyze_chest_vessel: ScreenChestCTResponseBodyDataAnalyzeChestVessel = None,
        cacs: ScreenChestCTResponseBodyDataCACS = None,
        covid: ScreenChestCTResponseBodyDataCovid = None,
        detect_lymph: ScreenChestCTResponseBodyDataDetectLymph = None,
        detect_pdac: ScreenChestCTResponseBodyDataDetectPdac = None,
        detect_rib_fracture: ScreenChestCTResponseBodyDataDetectRibFracture = None,
        error_message: str = None,
        lung_nodule: ScreenChestCTResponseBodyDataLungNodule = None,
        nested_url_list: Dict[str, Any] = None,
        screen_ec: ScreenChestCTResponseBodyDataScreenEc = None,
        urllist: Dict[str, Any] = None,
    ):
        self.analyze_chest_vessel = analyze_chest_vessel
        self.cacs = cacs
        self.covid = covid
        self.detect_lymph = detect_lymph
        self.detect_pdac = detect_pdac
        self.detect_rib_fracture = detect_rib_fracture
        self.error_message = error_message
        self.lung_nodule = lung_nodule
        self.nested_url_list = nested_url_list
        self.screen_ec = screen_ec
        self.urllist = urllist

    def validate(self):
        if self.analyze_chest_vessel:
            self.analyze_chest_vessel.validate()
        if self.cacs:
            self.cacs.validate()
        if self.covid:
            self.covid.validate()
        if self.detect_lymph:
            self.detect_lymph.validate()
        if self.detect_pdac:
            self.detect_pdac.validate()
        if self.detect_rib_fracture:
            self.detect_rib_fracture.validate()
        if self.lung_nodule:
            self.lung_nodule.validate()
        if self.screen_ec:
            self.screen_ec.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.analyze_chest_vessel is not None:
            result['AnalyzeChestVessel'] = self.analyze_chest_vessel.to_map()
        if self.cacs is not None:
            result['CACS'] = self.cacs.to_map()
        if self.covid is not None:
            result['Covid'] = self.covid.to_map()
        if self.detect_lymph is not None:
            result['DetectLymph'] = self.detect_lymph.to_map()
        if self.detect_pdac is not None:
            result['DetectPdac'] = self.detect_pdac.to_map()
        if self.detect_rib_fracture is not None:
            result['DetectRibFracture'] = self.detect_rib_fracture.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.lung_nodule is not None:
            result['LungNodule'] = self.lung_nodule.to_map()
        if self.nested_url_list is not None:
            result['NestedUrlList'] = self.nested_url_list
        if self.screen_ec is not None:
            result['ScreenEc'] = self.screen_ec.to_map()
        if self.urllist is not None:
            result['URLList'] = self.urllist
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AnalyzeChestVessel') is not None:
            temp_model = ScreenChestCTResponseBodyDataAnalyzeChestVessel()
            self.analyze_chest_vessel = temp_model.from_map(m['AnalyzeChestVessel'])
        if m.get('CACS') is not None:
            temp_model = ScreenChestCTResponseBodyDataCACS()
            self.cacs = temp_model.from_map(m['CACS'])
        if m.get('Covid') is not None:
            temp_model = ScreenChestCTResponseBodyDataCovid()
            self.covid = temp_model.from_map(m['Covid'])
        if m.get('DetectLymph') is not None:
            temp_model = ScreenChestCTResponseBodyDataDetectLymph()
            self.detect_lymph = temp_model.from_map(m['DetectLymph'])
        if m.get('DetectPdac') is not None:
            temp_model = ScreenChestCTResponseBodyDataDetectPdac()
            self.detect_pdac = temp_model.from_map(m['DetectPdac'])
        if m.get('DetectRibFracture') is not None:
            temp_model = ScreenChestCTResponseBodyDataDetectRibFracture()
            self.detect_rib_fracture = temp_model.from_map(m['DetectRibFracture'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('LungNodule') is not None:
            temp_model = ScreenChestCTResponseBodyDataLungNodule()
            self.lung_nodule = temp_model.from_map(m['LungNodule'])
        if m.get('NestedUrlList') is not None:
            self.nested_url_list = m.get('NestedUrlList')
        if m.get('ScreenEc') is not None:
            temp_model = ScreenChestCTResponseBodyDataScreenEc()
            self.screen_ec = temp_model.from_map(m['ScreenEc'])
        if m.get('URLList') is not None:
            self.urllist = m.get('URLList')
        return self


class ScreenChestCTResponseBody(TeaModel):
    def __init__(
        self,
        data: ScreenChestCTResponseBodyData = None,
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
            temp_model = ScreenChestCTResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ScreenChestCTResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ScreenChestCTResponseBody = None,
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
            temp_model = ScreenChestCTResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ScreenECRequestURLList(TeaModel):
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


class ScreenECRequest(TeaModel):
    def __init__(
        self,
        data_source_type: str = None,
        urllist: List[ScreenECRequestURLList] = None,
    ):
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
        if self.data_source_type is not None:
            result['DataSourceType'] = self.data_source_type
        result['URLList'] = []
        if self.urllist is not None:
            for k in self.urllist:
                result['URLList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSourceType') is not None:
            self.data_source_type = m.get('DataSourceType')
        self.urllist = []
        if m.get('URLList') is not None:
            for k in m.get('URLList'):
                temp_model = ScreenECRequestURLList()
                self.urllist.append(temp_model.from_map(k))
        return self


class ScreenECResponseBodyDataLesion(TeaModel):
    def __init__(
        self,
        benign_volume: str = None,
        ec_volume: str = None,
        eso_volume: str = None,
        mask: str = None,
        possibilities: List[str] = None,
    ):
        self.benign_volume = benign_volume
        self.ec_volume = ec_volume
        self.eso_volume = eso_volume
        self.mask = mask
        self.possibilities = possibilities

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.benign_volume is not None:
            result['BenignVolume'] = self.benign_volume
        if self.ec_volume is not None:
            result['EcVolume'] = self.ec_volume
        if self.eso_volume is not None:
            result['EsoVolume'] = self.eso_volume
        if self.mask is not None:
            result['Mask'] = self.mask
        if self.possibilities is not None:
            result['Possibilities'] = self.possibilities
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BenignVolume') is not None:
            self.benign_volume = m.get('BenignVolume')
        if m.get('EcVolume') is not None:
            self.ec_volume = m.get('EcVolume')
        if m.get('EsoVolume') is not None:
            self.eso_volume = m.get('EsoVolume')
        if m.get('Mask') is not None:
            self.mask = m.get('Mask')
        if m.get('Possibilities') is not None:
            self.possibilities = m.get('Possibilities')
        return self


class ScreenECResponseBodyData(TeaModel):
    def __init__(
        self,
        lesion: ScreenECResponseBodyDataLesion = None,
    ):
        self.lesion = lesion

    def validate(self):
        if self.lesion:
            self.lesion.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lesion is not None:
            result['Lesion'] = self.lesion.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lesion') is not None:
            temp_model = ScreenECResponseBodyDataLesion()
            self.lesion = temp_model.from_map(m['Lesion'])
        return self


class ScreenECResponseBody(TeaModel):
    def __init__(
        self,
        data: ScreenECResponseBodyData = None,
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
            temp_model = ScreenECResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ScreenECResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ScreenECResponseBody = None,
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
            temp_model = ScreenECResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SegmentOARRequestURLList(TeaModel):
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


class SegmentOARRequest(TeaModel):
    def __init__(
        self,
        body_part: str = None,
        contrast: bool = None,
        data_format: str = None,
        mask_list: List[int] = None,
        org_id: str = None,
        org_name: str = None,
        urllist: List[SegmentOARRequestURLList] = None,
    ):
        self.body_part = body_part
        self.contrast = contrast
        self.data_format = data_format
        self.mask_list = mask_list
        self.org_id = org_id
        self.org_name = org_name
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
        if self.body_part is not None:
            result['BodyPart'] = self.body_part
        if self.contrast is not None:
            result['Contrast'] = self.contrast
        if self.data_format is not None:
            result['DataFormat'] = self.data_format
        if self.mask_list is not None:
            result['MaskList'] = self.mask_list
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.org_name is not None:
            result['OrgName'] = self.org_name
        result['URLList'] = []
        if self.urllist is not None:
            for k in self.urllist:
                result['URLList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BodyPart') is not None:
            self.body_part = m.get('BodyPart')
        if m.get('Contrast') is not None:
            self.contrast = m.get('Contrast')
        if m.get('DataFormat') is not None:
            self.data_format = m.get('DataFormat')
        if m.get('MaskList') is not None:
            self.mask_list = m.get('MaskList')
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('OrgName') is not None:
            self.org_name = m.get('OrgName')
        self.urllist = []
        if m.get('URLList') is not None:
            for k in m.get('URLList'):
                temp_model = SegmentOARRequestURLList()
                self.urllist.append(temp_model.from_map(k))
        return self


class SegmentOARAdvanceRequestURLList(TeaModel):
    def __init__(
        self,
        urlobject: BinaryIO = None,
    ):
        self.urlobject = urlobject

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.urlobject is not None:
            result['URL'] = self.urlobject
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('URL') is not None:
            self.urlobject = m.get('URL')
        return self


class SegmentOARAdvanceRequest(TeaModel):
    def __init__(
        self,
        body_part: str = None,
        contrast: bool = None,
        data_format: str = None,
        mask_list: List[int] = None,
        org_id: str = None,
        org_name: str = None,
        urllist: List[SegmentOARAdvanceRequestURLList] = None,
    ):
        self.body_part = body_part
        self.contrast = contrast
        self.data_format = data_format
        self.mask_list = mask_list
        self.org_id = org_id
        self.org_name = org_name
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
        if self.body_part is not None:
            result['BodyPart'] = self.body_part
        if self.contrast is not None:
            result['Contrast'] = self.contrast
        if self.data_format is not None:
            result['DataFormat'] = self.data_format
        if self.mask_list is not None:
            result['MaskList'] = self.mask_list
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.org_name is not None:
            result['OrgName'] = self.org_name
        result['URLList'] = []
        if self.urllist is not None:
            for k in self.urllist:
                result['URLList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BodyPart') is not None:
            self.body_part = m.get('BodyPart')
        if m.get('Contrast') is not None:
            self.contrast = m.get('Contrast')
        if m.get('DataFormat') is not None:
            self.data_format = m.get('DataFormat')
        if m.get('MaskList') is not None:
            self.mask_list = m.get('MaskList')
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('OrgName') is not None:
            self.org_name = m.get('OrgName')
        self.urllist = []
        if m.get('URLList') is not None:
            for k in m.get('URLList'):
                temp_model = SegmentOARAdvanceRequestURLList()
                self.urllist.append(temp_model.from_map(k))
        return self


class SegmentOARResponseBodyData(TeaModel):
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
            result['ResultURL'] = self.result_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResultURL') is not None:
            self.result_url = m.get('ResultURL')
        return self


class SegmentOARResponseBody(TeaModel):
    def __init__(
        self,
        data: SegmentOARResponseBodyData = None,
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
            temp_model = SegmentOARResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SegmentOARResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SegmentOARResponseBody = None,
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
            temp_model = SegmentOARResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TargetVolumeSegmentRequestURLList(TeaModel):
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


class TargetVolumeSegmentRequest(TeaModel):
    def __init__(
        self,
        cancer_type: str = None,
        data_format: str = None,
        org_id: str = None,
        org_name: str = None,
        target_volume_type: str = None,
        urllist: List[TargetVolumeSegmentRequestURLList] = None,
    ):
        self.cancer_type = cancer_type
        self.data_format = data_format
        self.org_id = org_id
        self.org_name = org_name
        self.target_volume_type = target_volume_type
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
        if self.cancer_type is not None:
            result['CancerType'] = self.cancer_type
        if self.data_format is not None:
            result['DataFormat'] = self.data_format
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.org_name is not None:
            result['OrgName'] = self.org_name
        if self.target_volume_type is not None:
            result['TargetVolumeType'] = self.target_volume_type
        result['URLList'] = []
        if self.urllist is not None:
            for k in self.urllist:
                result['URLList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CancerType') is not None:
            self.cancer_type = m.get('CancerType')
        if m.get('DataFormat') is not None:
            self.data_format = m.get('DataFormat')
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('OrgName') is not None:
            self.org_name = m.get('OrgName')
        if m.get('TargetVolumeType') is not None:
            self.target_volume_type = m.get('TargetVolumeType')
        self.urllist = []
        if m.get('URLList') is not None:
            for k in m.get('URLList'):
                temp_model = TargetVolumeSegmentRequestURLList()
                self.urllist.append(temp_model.from_map(k))
        return self


class TargetVolumeSegmentAdvanceRequestURLList(TeaModel):
    def __init__(
        self,
        urlobject: BinaryIO = None,
    ):
        self.urlobject = urlobject

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.urlobject is not None:
            result['URL'] = self.urlobject
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('URL') is not None:
            self.urlobject = m.get('URL')
        return self


class TargetVolumeSegmentAdvanceRequest(TeaModel):
    def __init__(
        self,
        cancer_type: str = None,
        data_format: str = None,
        org_id: str = None,
        org_name: str = None,
        target_volume_type: str = None,
        urllist: List[TargetVolumeSegmentAdvanceRequestURLList] = None,
    ):
        self.cancer_type = cancer_type
        self.data_format = data_format
        self.org_id = org_id
        self.org_name = org_name
        self.target_volume_type = target_volume_type
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
        if self.cancer_type is not None:
            result['CancerType'] = self.cancer_type
        if self.data_format is not None:
            result['DataFormat'] = self.data_format
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.org_name is not None:
            result['OrgName'] = self.org_name
        if self.target_volume_type is not None:
            result['TargetVolumeType'] = self.target_volume_type
        result['URLList'] = []
        if self.urllist is not None:
            for k in self.urllist:
                result['URLList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CancerType') is not None:
            self.cancer_type = m.get('CancerType')
        if m.get('DataFormat') is not None:
            self.data_format = m.get('DataFormat')
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('OrgName') is not None:
            self.org_name = m.get('OrgName')
        if m.get('TargetVolumeType') is not None:
            self.target_volume_type = m.get('TargetVolumeType')
        self.urllist = []
        if m.get('URLList') is not None:
            for k in m.get('URLList'):
                temp_model = TargetVolumeSegmentAdvanceRequestURLList()
                self.urllist.append(temp_model.from_map(k))
        return self


class TargetVolumeSegmentResponseBodyData(TeaModel):
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
            result['ResultURL'] = self.result_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResultURL') is not None:
            self.result_url = m.get('ResultURL')
        return self


class TargetVolumeSegmentResponseBody(TeaModel):
    def __init__(
        self,
        data: TargetVolumeSegmentResponseBodyData = None,
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
            temp_model = TargetVolumeSegmentResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class TargetVolumeSegmentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: TargetVolumeSegmentResponseBody = None,
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
            temp_model = TargetVolumeSegmentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TranslateMedRequest(TeaModel):
    def __init__(
        self,
        from_language: str = None,
        text: str = None,
        to_language: str = None,
    ):
        self.from_language = from_language
        self.text = text
        self.to_language = to_language

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.from_language is not None:
            result['FromLanguage'] = self.from_language
        if self.text is not None:
            result['Text'] = self.text
        if self.to_language is not None:
            result['ToLanguage'] = self.to_language
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FromLanguage') is not None:
            self.from_language = m.get('FromLanguage')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('ToLanguage') is not None:
            self.to_language = m.get('ToLanguage')
        return self


class TranslateMedResponseBodyData(TeaModel):
    def __init__(
        self,
        text: str = None,
        words: int = None,
    ):
        self.text = text
        self.words = words

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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


class TranslateMedResponseBody(TeaModel):
    def __init__(
        self,
        data: TranslateMedResponseBodyData = None,
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
            temp_model = TranslateMedResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class TranslateMedResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: TranslateMedResponseBody = None,
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
            temp_model = TranslateMedResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


