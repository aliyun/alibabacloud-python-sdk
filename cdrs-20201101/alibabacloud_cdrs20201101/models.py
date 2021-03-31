# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List, Any


class AddCdrsMonitorRequest(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        monitor_type: str = None,
        description: str = None,
        batch_indicator: int = None,
        algorithm_vendor: str = None,
        notifier_type: str = None,
        notifier_url: str = None,
        notifier_app_secret: str = None,
        notifier_time_out: int = None,
        notifier_extend_values: str = None,
    ):
        self.corp_id = corp_id
        self.monitor_type = monitor_type
        self.description = description
        self.batch_indicator = batch_indicator
        self.algorithm_vendor = algorithm_vendor
        self.notifier_type = notifier_type
        self.notifier_url = notifier_url
        self.notifier_app_secret = notifier_app_secret
        self.notifier_time_out = notifier_time_out
        self.notifier_extend_values = notifier_extend_values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.monitor_type is not None:
            result['MonitorType'] = self.monitor_type
        if self.description is not None:
            result['Description'] = self.description
        if self.batch_indicator is not None:
            result['BatchIndicator'] = self.batch_indicator
        if self.algorithm_vendor is not None:
            result['AlgorithmVendor'] = self.algorithm_vendor
        if self.notifier_type is not None:
            result['NotifierType'] = self.notifier_type
        if self.notifier_url is not None:
            result['NotifierUrl'] = self.notifier_url
        if self.notifier_app_secret is not None:
            result['NotifierAppSecret'] = self.notifier_app_secret
        if self.notifier_time_out is not None:
            result['NotifierTimeOut'] = self.notifier_time_out
        if self.notifier_extend_values is not None:
            result['NotifierExtendValues'] = self.notifier_extend_values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('MonitorType') is not None:
            self.monitor_type = m.get('MonitorType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('BatchIndicator') is not None:
            self.batch_indicator = m.get('BatchIndicator')
        if m.get('AlgorithmVendor') is not None:
            self.algorithm_vendor = m.get('AlgorithmVendor')
        if m.get('NotifierType') is not None:
            self.notifier_type = m.get('NotifierType')
        if m.get('NotifierUrl') is not None:
            self.notifier_url = m.get('NotifierUrl')
        if m.get('NotifierAppSecret') is not None:
            self.notifier_app_secret = m.get('NotifierAppSecret')
        if m.get('NotifierTimeOut') is not None:
            self.notifier_time_out = m.get('NotifierTimeOut')
        if m.get('NotifierExtendValues') is not None:
            self.notifier_extend_values = m.get('NotifierExtendValues')
        return self


class AddCdrsMonitorResponseBodyData(TeaModel):
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


class AddCdrsMonitorResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: AddCdrsMonitorResponseBodyData = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = AddCdrsMonitorResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class AddCdrsMonitorResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddCdrsMonitorResponseBody = None,
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
            temp_model = AddCdrsMonitorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddMonitorRequest(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        monitor_type: str = None,
        description: str = None,
        batch_indicator: int = None,
        algorithm_vendor: str = None,
        notifier_type: str = None,
        notifier_url: str = None,
        notifier_app_secret: str = None,
        notifier_time_out: int = None,
        notifier_extend_values: str = None,
    ):
        self.corp_id = corp_id
        self.monitor_type = monitor_type
        self.description = description
        self.batch_indicator = batch_indicator
        self.algorithm_vendor = algorithm_vendor
        self.notifier_type = notifier_type
        self.notifier_url = notifier_url
        self.notifier_app_secret = notifier_app_secret
        self.notifier_time_out = notifier_time_out
        self.notifier_extend_values = notifier_extend_values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.monitor_type is not None:
            result['MonitorType'] = self.monitor_type
        if self.description is not None:
            result['Description'] = self.description
        if self.batch_indicator is not None:
            result['BatchIndicator'] = self.batch_indicator
        if self.algorithm_vendor is not None:
            result['AlgorithmVendor'] = self.algorithm_vendor
        if self.notifier_type is not None:
            result['NotifierType'] = self.notifier_type
        if self.notifier_url is not None:
            result['NotifierUrl'] = self.notifier_url
        if self.notifier_app_secret is not None:
            result['NotifierAppSecret'] = self.notifier_app_secret
        if self.notifier_time_out is not None:
            result['NotifierTimeOut'] = self.notifier_time_out
        if self.notifier_extend_values is not None:
            result['NotifierExtendValues'] = self.notifier_extend_values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('MonitorType') is not None:
            self.monitor_type = m.get('MonitorType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('BatchIndicator') is not None:
            self.batch_indicator = m.get('BatchIndicator')
        if m.get('AlgorithmVendor') is not None:
            self.algorithm_vendor = m.get('AlgorithmVendor')
        if m.get('NotifierType') is not None:
            self.notifier_type = m.get('NotifierType')
        if m.get('NotifierUrl') is not None:
            self.notifier_url = m.get('NotifierUrl')
        if m.get('NotifierAppSecret') is not None:
            self.notifier_app_secret = m.get('NotifierAppSecret')
        if m.get('NotifierTimeOut') is not None:
            self.notifier_time_out = m.get('NotifierTimeOut')
        if m.get('NotifierExtendValues') is not None:
            self.notifier_extend_values = m.get('NotifierExtendValues')
        return self


class AddMonitorResponseBodyData(TeaModel):
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


class AddMonitorResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: AddMonitorResponseBodyData = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = AddMonitorResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class AddMonitorResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddMonitorResponseBody = None,
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
            temp_model = AddMonitorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BindDeviceRequestDevices(TeaModel):
    def __init__(
        self,
        device_id: str = None,
        corp_id: str = None,
    ):
        self.device_id = device_id
        self.corp_id = corp_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        return self


class BindDeviceRequest(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        devices: List[BindDeviceRequestDevices] = None,
    ):
        self.corp_id = corp_id
        self.devices = devices

    def validate(self):
        if self.devices:
            for k in self.devices:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        result['Devices'] = []
        if self.devices is not None:
            for k in self.devices:
                result['Devices'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        self.devices = []
        if m.get('Devices') is not None:
            for k in m.get('Devices'):
                temp_model = BindDeviceRequestDevices()
                self.devices.append(temp_model.from_map(k))
        return self


class BindDeviceResponseBodyData(TeaModel):
    def __init__(
        self,
        device_id: str = None,
        success: bool = None,
        code: str = None,
        message: str = None,
    ):
        self.device_id = device_id
        self.success = success
        self.code = code
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.success is not None:
            result['Success'] = self.success
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class BindDeviceResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: List[BindDeviceResponseBodyData] = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = BindDeviceResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class BindDeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: BindDeviceResponseBody = None,
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
            temp_model = BindDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateProjectRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        icon: str = None,
        description: str = None,
        aggregate_scene_code: str = None,
    ):
        self.name = name
        self.icon = icon
        self.description = description
        self.aggregate_scene_code = aggregate_scene_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.icon is not None:
            result['Icon'] = self.icon
        if self.description is not None:
            result['Description'] = self.description
        if self.aggregate_scene_code is not None:
            result['AggregateSceneCode'] = self.aggregate_scene_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Icon') is not None:
            self.icon = m.get('Icon')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('AggregateSceneCode') is not None:
            self.aggregate_scene_code = m.get('AggregateSceneCode')
        return self


class CreateProjectResponseBody(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        message: str = None,
        request_id: str = None,
        code: str = None,
    ):
        self.corp_id = corp_id
        self.message = message
        self.request_id = request_id
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class CreateProjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateProjectResponseBody = None,
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
            temp_model = CreateProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetectTrajectoryRegularPatternRequest(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        id_type: str = None,
        id_value: str = None,
        predict_date: str = None,
    ):
        self.corp_id = corp_id
        self.id_type = id_type
        self.id_value = id_value
        self.predict_date = predict_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.id_value is not None:
            result['IdValue'] = self.id_value
        if self.predict_date is not None:
            result['PredictDate'] = self.predict_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('IdValue') is not None:
            self.id_value = m.get('IdValue')
        if m.get('PredictDate') is not None:
            self.predict_date = m.get('PredictDate')
        return self


class DetectTrajectoryRegularPatternResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: str = None,
        code: int = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DetectTrajectoryRegularPatternResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DetectTrajectoryRegularPatternResponseBody = None,
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
            temp_model = DetectTrajectoryRegularPatternResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCdrsMonitorListRequest(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        page_no: int = None,
        page_size: int = None,
    ):
        self.corp_id = corp_id
        self.page_no = page_no
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class GetCdrsMonitorListResponseBodyDataRecords(TeaModel):
    def __init__(
        self,
        status: str = None,
        rule_expression: str = None,
        image_match: str = None,
        monitor_type: str = None,
        create_date: str = None,
        rule_name: str = None,
        notifier_type: str = None,
        description: str = None,
        expression: str = None,
        notifier_extra: str = None,
        attributes: str = None,
        device_list: str = None,
        task_id: str = None,
        modified_date: str = None,
        algorithm_vendor: str = None,
    ):
        self.status = status
        self.rule_expression = rule_expression
        self.image_match = image_match
        self.monitor_type = monitor_type
        self.create_date = create_date
        self.rule_name = rule_name
        self.notifier_type = notifier_type
        self.description = description
        self.expression = expression
        self.notifier_extra = notifier_extra
        self.attributes = attributes
        self.device_list = device_list
        self.task_id = task_id
        self.modified_date = modified_date
        self.algorithm_vendor = algorithm_vendor

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.rule_expression is not None:
            result['RuleExpression'] = self.rule_expression
        if self.image_match is not None:
            result['ImageMatch'] = self.image_match
        if self.monitor_type is not None:
            result['MonitorType'] = self.monitor_type
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.notifier_type is not None:
            result['NotifierType'] = self.notifier_type
        if self.description is not None:
            result['Description'] = self.description
        if self.expression is not None:
            result['Expression'] = self.expression
        if self.notifier_extra is not None:
            result['NotifierExtra'] = self.notifier_extra
        if self.attributes is not None:
            result['Attributes'] = self.attributes
        if self.device_list is not None:
            result['DeviceList'] = self.device_list
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.modified_date is not None:
            result['ModifiedDate'] = self.modified_date
        if self.algorithm_vendor is not None:
            result['AlgorithmVendor'] = self.algorithm_vendor
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('RuleExpression') is not None:
            self.rule_expression = m.get('RuleExpression')
        if m.get('ImageMatch') is not None:
            self.image_match = m.get('ImageMatch')
        if m.get('MonitorType') is not None:
            self.monitor_type = m.get('MonitorType')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('NotifierType') is not None:
            self.notifier_type = m.get('NotifierType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Expression') is not None:
            self.expression = m.get('Expression')
        if m.get('NotifierExtra') is not None:
            self.notifier_extra = m.get('NotifierExtra')
        if m.get('Attributes') is not None:
            self.attributes = m.get('Attributes')
        if m.get('DeviceList') is not None:
            self.device_list = m.get('DeviceList')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('ModifiedDate') is not None:
            self.modified_date = m.get('ModifiedDate')
        if m.get('AlgorithmVendor') is not None:
            self.algorithm_vendor = m.get('AlgorithmVendor')
        return self


class GetCdrsMonitorListResponseBodyData(TeaModel):
    def __init__(
        self,
        records: List[GetCdrsMonitorListResponseBodyDataRecords] = None,
        page_no: int = None,
        total_page: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.records = records
        self.page_no = page_no
        self.total_page = total_page
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        if self.records:
            for k in self.records:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Records'] = []
        if self.records is not None:
            for k in self.records:
                result['Records'].append(k.to_map() if k else None)
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.total_page is not None:
            result['TotalPage'] = self.total_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.records = []
        if m.get('Records') is not None:
            for k in m.get('Records'):
                temp_model = GetCdrsMonitorListResponseBodyDataRecords()
                self.records.append(temp_model.from_map(k))
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class GetCdrsMonitorListResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: GetCdrsMonitorListResponseBodyData = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = GetCdrsMonitorListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class GetCdrsMonitorListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetCdrsMonitorListResponseBody = None,
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
            temp_model = GetCdrsMonitorListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCdrsMonitorResultRequest(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        task_id: str = None,
        min_record_id: str = None,
        start_time: int = None,
        end_time: int = None,
        algorithm_vendor: str = None,
    ):
        self.corp_id = corp_id
        self.task_id = task_id
        self.min_record_id = min_record_id
        self.start_time = start_time
        self.end_time = end_time
        self.algorithm_vendor = algorithm_vendor

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.min_record_id is not None:
            result['MinRecordId'] = self.min_record_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.algorithm_vendor is not None:
            result['AlgorithmVendor'] = self.algorithm_vendor
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('MinRecordId') is not None:
            self.min_record_id = m.get('MinRecordId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('AlgorithmVendor') is not None:
            self.algorithm_vendor = m.get('AlgorithmVendor')
        return self


class GetCdrsMonitorResultResponseBodyDataRecordsExtendInfo(TeaModel):
    def __init__(
        self,
        plate_no: str = None,
    ):
        self.plate_no = plate_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.plate_no is not None:
            result['PlateNo'] = self.plate_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PlateNo') is not None:
            self.plate_no = m.get('PlateNo')
        return self


class GetCdrsMonitorResultResponseBodyDataRecords(TeaModel):
    def __init__(
        self,
        pic_url: str = None,
        right_bottom_y: str = None,
        score: str = None,
        monitor_pic_url: str = None,
        right_bottom_x: str = None,
        extend_info: GetCdrsMonitorResultResponseBodyDataRecordsExtendInfo = None,
        gb_id: str = None,
        left_up_y: str = None,
        left_up_x: str = None,
        shot_time: str = None,
        task_id: str = None,
        target_pic_url: str = None,
    ):
        self.pic_url = pic_url
        self.right_bottom_y = right_bottom_y
        self.score = score
        self.monitor_pic_url = monitor_pic_url
        self.right_bottom_x = right_bottom_x
        self.extend_info = extend_info
        self.gb_id = gb_id
        self.left_up_y = left_up_y
        self.left_up_x = left_up_x
        self.shot_time = shot_time
        self.task_id = task_id
        self.target_pic_url = target_pic_url

    def validate(self):
        if self.extend_info:
            self.extend_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pic_url is not None:
            result['PicUrl'] = self.pic_url
        if self.right_bottom_y is not None:
            result['RightBottomY'] = self.right_bottom_y
        if self.score is not None:
            result['Score'] = self.score
        if self.monitor_pic_url is not None:
            result['MonitorPicUrl'] = self.monitor_pic_url
        if self.right_bottom_x is not None:
            result['RightBottomX'] = self.right_bottom_x
        if self.extend_info is not None:
            result['ExtendInfo'] = self.extend_info.to_map()
        if self.gb_id is not None:
            result['GbId'] = self.gb_id
        if self.left_up_y is not None:
            result['LeftUpY'] = self.left_up_y
        if self.left_up_x is not None:
            result['LeftUpX'] = self.left_up_x
        if self.shot_time is not None:
            result['ShotTime'] = self.shot_time
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.target_pic_url is not None:
            result['TargetPicUrl'] = self.target_pic_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PicUrl') is not None:
            self.pic_url = m.get('PicUrl')
        if m.get('RightBottomY') is not None:
            self.right_bottom_y = m.get('RightBottomY')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('MonitorPicUrl') is not None:
            self.monitor_pic_url = m.get('MonitorPicUrl')
        if m.get('RightBottomX') is not None:
            self.right_bottom_x = m.get('RightBottomX')
        if m.get('ExtendInfo') is not None:
            temp_model = GetCdrsMonitorResultResponseBodyDataRecordsExtendInfo()
            self.extend_info = temp_model.from_map(m['ExtendInfo'])
        if m.get('GbId') is not None:
            self.gb_id = m.get('GbId')
        if m.get('LeftUpY') is not None:
            self.left_up_y = m.get('LeftUpY')
        if m.get('LeftUpX') is not None:
            self.left_up_x = m.get('LeftUpX')
        if m.get('ShotTime') is not None:
            self.shot_time = m.get('ShotTime')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TargetPicUrl') is not None:
            self.target_pic_url = m.get('TargetPicUrl')
        return self


class GetCdrsMonitorResultResponseBodyData(TeaModel):
    def __init__(
        self,
        max_id: str = None,
        records: List[GetCdrsMonitorResultResponseBodyDataRecords] = None,
    ):
        self.max_id = max_id
        self.records = records

    def validate(self):
        if self.records:
            for k in self.records:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_id is not None:
            result['MaxId'] = self.max_id
        result['Records'] = []
        if self.records is not None:
            for k in self.records:
                result['Records'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxId') is not None:
            self.max_id = m.get('MaxId')
        self.records = []
        if m.get('Records') is not None:
            for k in m.get('Records'):
                temp_model = GetCdrsMonitorResultResponseBodyDataRecords()
                self.records.append(temp_model.from_map(k))
        return self


class GetCdrsMonitorResultResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: GetCdrsMonitorResultResponseBodyData = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = GetCdrsMonitorResultResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class GetCdrsMonitorResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetCdrsMonitorResultResponseBody = None,
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
            temp_model = GetCdrsMonitorResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMonitorListRequest(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.corp_id = corp_id
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class GetMonitorListResponseBodyDataRecords(TeaModel):
    def __init__(
        self,
        status: str = None,
        rule_expression: str = None,
        image_match: str = None,
        monitor_type: str = None,
        create_date: str = None,
        rule_name: str = None,
        notifier_type: str = None,
        description: str = None,
        expression: str = None,
        notifier_extra: str = None,
        attributes: str = None,
        device_list: str = None,
        task_id: str = None,
        modified_date: str = None,
        algorithm_vendor: str = None,
    ):
        self.status = status
        self.rule_expression = rule_expression
        self.image_match = image_match
        self.monitor_type = monitor_type
        self.create_date = create_date
        self.rule_name = rule_name
        self.notifier_type = notifier_type
        self.description = description
        self.expression = expression
        self.notifier_extra = notifier_extra
        self.attributes = attributes
        self.device_list = device_list
        self.task_id = task_id
        self.modified_date = modified_date
        self.algorithm_vendor = algorithm_vendor

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.rule_expression is not None:
            result['RuleExpression'] = self.rule_expression
        if self.image_match is not None:
            result['ImageMatch'] = self.image_match
        if self.monitor_type is not None:
            result['MonitorType'] = self.monitor_type
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.notifier_type is not None:
            result['NotifierType'] = self.notifier_type
        if self.description is not None:
            result['Description'] = self.description
        if self.expression is not None:
            result['Expression'] = self.expression
        if self.notifier_extra is not None:
            result['NotifierExtra'] = self.notifier_extra
        if self.attributes is not None:
            result['Attributes'] = self.attributes
        if self.device_list is not None:
            result['DeviceList'] = self.device_list
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.modified_date is not None:
            result['ModifiedDate'] = self.modified_date
        if self.algorithm_vendor is not None:
            result['AlgorithmVendor'] = self.algorithm_vendor
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('RuleExpression') is not None:
            self.rule_expression = m.get('RuleExpression')
        if m.get('ImageMatch') is not None:
            self.image_match = m.get('ImageMatch')
        if m.get('MonitorType') is not None:
            self.monitor_type = m.get('MonitorType')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('NotifierType') is not None:
            self.notifier_type = m.get('NotifierType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Expression') is not None:
            self.expression = m.get('Expression')
        if m.get('NotifierExtra') is not None:
            self.notifier_extra = m.get('NotifierExtra')
        if m.get('Attributes') is not None:
            self.attributes = m.get('Attributes')
        if m.get('DeviceList') is not None:
            self.device_list = m.get('DeviceList')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('ModifiedDate') is not None:
            self.modified_date = m.get('ModifiedDate')
        if m.get('AlgorithmVendor') is not None:
            self.algorithm_vendor = m.get('AlgorithmVendor')
        return self


class GetMonitorListResponseBodyData(TeaModel):
    def __init__(
        self,
        records: List[GetMonitorListResponseBodyDataRecords] = None,
        total_page: int = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.records = records
        self.total_page = total_page
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        if self.records:
            for k in self.records:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Records'] = []
        if self.records is not None:
            for k in self.records:
                result['Records'].append(k.to_map() if k else None)
        if self.total_page is not None:
            result['TotalPage'] = self.total_page
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.records = []
        if m.get('Records') is not None:
            for k in m.get('Records'):
                temp_model = GetMonitorListResponseBodyDataRecords()
                self.records.append(temp_model.from_map(k))
        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class GetMonitorListResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: GetMonitorListResponseBodyData = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = GetMonitorListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class GetMonitorListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetMonitorListResponseBody = None,
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
            temp_model = GetMonitorListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMonitorResultRequest(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        task_id: str = None,
        min_record_id: str = None,
        start_time: int = None,
        end_time: int = None,
        algorithm_vendor: str = None,
    ):
        self.corp_id = corp_id
        self.task_id = task_id
        self.min_record_id = min_record_id
        self.start_time = start_time
        self.end_time = end_time
        self.algorithm_vendor = algorithm_vendor

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.min_record_id is not None:
            result['MinRecordId'] = self.min_record_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.algorithm_vendor is not None:
            result['AlgorithmVendor'] = self.algorithm_vendor
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('MinRecordId') is not None:
            self.min_record_id = m.get('MinRecordId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('AlgorithmVendor') is not None:
            self.algorithm_vendor = m.get('AlgorithmVendor')
        return self


class GetMonitorResultResponseBodyDataRecordsExtendInfo(TeaModel):
    def __init__(
        self,
        plate_no: str = None,
    ):
        self.plate_no = plate_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.plate_no is not None:
            result['PlateNo'] = self.plate_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PlateNo') is not None:
            self.plate_no = m.get('PlateNo')
        return self


class GetMonitorResultResponseBodyDataRecords(TeaModel):
    def __init__(
        self,
        pic_url: str = None,
        right_bottom_y: str = None,
        score: str = None,
        monitor_pic_url: str = None,
        right_bottom_x: str = None,
        extend_info: GetMonitorResultResponseBodyDataRecordsExtendInfo = None,
        gb_id: str = None,
        left_up_y: str = None,
        left_up_x: str = None,
        shot_time: str = None,
        task_id: str = None,
        target_pic_url: str = None,
    ):
        self.pic_url = pic_url
        self.right_bottom_y = right_bottom_y
        self.score = score
        self.monitor_pic_url = monitor_pic_url
        self.right_bottom_x = right_bottom_x
        self.extend_info = extend_info
        self.gb_id = gb_id
        self.left_up_y = left_up_y
        self.left_up_x = left_up_x
        self.shot_time = shot_time
        self.task_id = task_id
        self.target_pic_url = target_pic_url

    def validate(self):
        if self.extend_info:
            self.extend_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pic_url is not None:
            result['PicUrl'] = self.pic_url
        if self.right_bottom_y is not None:
            result['RightBottomY'] = self.right_bottom_y
        if self.score is not None:
            result['Score'] = self.score
        if self.monitor_pic_url is not None:
            result['MonitorPicUrl'] = self.monitor_pic_url
        if self.right_bottom_x is not None:
            result['RightBottomX'] = self.right_bottom_x
        if self.extend_info is not None:
            result['ExtendInfo'] = self.extend_info.to_map()
        if self.gb_id is not None:
            result['GbId'] = self.gb_id
        if self.left_up_y is not None:
            result['LeftUpY'] = self.left_up_y
        if self.left_up_x is not None:
            result['LeftUpX'] = self.left_up_x
        if self.shot_time is not None:
            result['ShotTime'] = self.shot_time
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.target_pic_url is not None:
            result['TargetPicUrl'] = self.target_pic_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PicUrl') is not None:
            self.pic_url = m.get('PicUrl')
        if m.get('RightBottomY') is not None:
            self.right_bottom_y = m.get('RightBottomY')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('MonitorPicUrl') is not None:
            self.monitor_pic_url = m.get('MonitorPicUrl')
        if m.get('RightBottomX') is not None:
            self.right_bottom_x = m.get('RightBottomX')
        if m.get('ExtendInfo') is not None:
            temp_model = GetMonitorResultResponseBodyDataRecordsExtendInfo()
            self.extend_info = temp_model.from_map(m['ExtendInfo'])
        if m.get('GbId') is not None:
            self.gb_id = m.get('GbId')
        if m.get('LeftUpY') is not None:
            self.left_up_y = m.get('LeftUpY')
        if m.get('LeftUpX') is not None:
            self.left_up_x = m.get('LeftUpX')
        if m.get('ShotTime') is not None:
            self.shot_time = m.get('ShotTime')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TargetPicUrl') is not None:
            self.target_pic_url = m.get('TargetPicUrl')
        return self


class GetMonitorResultResponseBodyData(TeaModel):
    def __init__(
        self,
        max_id: str = None,
        records: List[GetMonitorResultResponseBodyDataRecords] = None,
    ):
        self.max_id = max_id
        self.records = records

    def validate(self):
        if self.records:
            for k in self.records:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_id is not None:
            result['MaxId'] = self.max_id
        result['Records'] = []
        if self.records is not None:
            for k in self.records:
                result['Records'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxId') is not None:
            self.max_id = m.get('MaxId')
        self.records = []
        if m.get('Records') is not None:
            for k in m.get('Records'):
                temp_model = GetMonitorResultResponseBodyDataRecords()
                self.records.append(temp_model.from_map(k))
        return self


class GetMonitorResultResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: GetMonitorResultResponseBodyData = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = GetMonitorResultResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class GetMonitorResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetMonitorResultResponseBody = None,
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
            temp_model = GetMonitorResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class IntersectTrajectoryRequestIdList(TeaModel):
    def __init__(
        self,
        id_value: str = None,
        id_type: str = None,
    ):
        self.id_value = id_value
        self.id_type = id_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id_value is not None:
            result['IdValue'] = self.id_value
        if self.id_type is not None:
            result['IdType'] = self.id_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IdValue') is not None:
            self.id_value = m.get('IdValue')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        return self


class IntersectTrajectoryRequest(TeaModel):
    def __init__(
        self,
        start_time: str = None,
        end_time: str = None,
        corp_id: str = None,
        delta_distance: int = None,
        delta_time: int = None,
        id_list: List[IntersectTrajectoryRequestIdList] = None,
    ):
        self.start_time = start_time
        self.end_time = end_time
        self.corp_id = corp_id
        self.delta_distance = delta_distance
        self.delta_time = delta_time
        self.id_list = id_list

    def validate(self):
        if self.id_list:
            for k in self.id_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.delta_distance is not None:
            result['DeltaDistance'] = self.delta_distance
        if self.delta_time is not None:
            result['DeltaTime'] = self.delta_time
        result['IdList'] = []
        if self.id_list is not None:
            for k in self.id_list:
                result['IdList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('DeltaDistance') is not None:
            self.delta_distance = m.get('DeltaDistance')
        if m.get('DeltaTime') is not None:
            self.delta_time = m.get('DeltaTime')
        self.id_list = []
        if m.get('IdList') is not None:
            for k in m.get('IdList'):
                temp_model = IntersectTrajectoryRequestIdList()
                self.id_list.append(temp_model.from_map(k))
        return self


class IntersectTrajectoryResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: str = None,
        code: int = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class IntersectTrajectoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: IntersectTrajectoryResponseBody = None,
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
            temp_model = IntersectTrajectoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAreaHotSpotMetricsRequest(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        person_id: str = None,
        device_id: str = None,
        start_time: str = None,
        end_time: str = None,
        page_number: str = None,
        page_size: str = None,
    ):
        self.corp_id = corp_id
        self.person_id = person_id
        self.device_id = device_id
        self.start_time = start_time
        self.end_time = end_time
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.person_id is not None:
            result['PersonId'] = self.person_id
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('PersonId') is not None:
            self.person_id = m.get('PersonId')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListAreaHotSpotMetricsResponseBodyData(TeaModel):
    def __init__(
        self,
        coordinates: str = None,
        device_id: str = None,
        times: str = None,
        interval_time: str = None,
        person_id: str = None,
    ):
        self.coordinates = coordinates
        self.device_id = device_id
        self.times = times
        self.interval_time = interval_time
        self.person_id = person_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.coordinates is not None:
            result['Coordinates'] = self.coordinates
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.times is not None:
            result['Times'] = self.times
        if self.interval_time is not None:
            result['IntervalTime'] = self.interval_time
        if self.person_id is not None:
            result['PersonId'] = self.person_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Coordinates') is not None:
            self.coordinates = m.get('Coordinates')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('Times') is not None:
            self.times = m.get('Times')
        if m.get('IntervalTime') is not None:
            self.interval_time = m.get('IntervalTime')
        if m.get('PersonId') is not None:
            self.person_id = m.get('PersonId')
        return self


class ListAreaHotSpotMetricsResponseBody(TeaModel):
    def __init__(
        self,
        total_count: str = None,
        request_id: str = None,
        message: str = None,
        page_size: str = None,
        page_number: str = None,
        data: List[ListAreaHotSpotMetricsResponseBodyData] = None,
        code: str = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.message = message
        self.page_size = page_size
        self.page_number = page_number
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListAreaHotSpotMetricsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class ListAreaHotSpotMetricsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListAreaHotSpotMetricsResponseBody = None,
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
            temp_model = ListAreaHotSpotMetricsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCityMapAoisRequest(TeaModel):
    def __init__(
        self,
        radius: int = None,
        latitude: str = None,
        longitude: str = None,
    ):
        self.radius = radius
        self.latitude = latitude
        self.longitude = longitude

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.radius is not None:
            result['Radius'] = self.radius
        if self.latitude is not None:
            result['Latitude'] = self.latitude
        if self.longitude is not None:
            result['Longitude'] = self.longitude
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Radius') is not None:
            self.radius = m.get('Radius')
        if m.get('Latitude') is not None:
            self.latitude = m.get('Latitude')
        if m.get('Longitude') is not None:
            self.longitude = m.get('Longitude')
        return self


class ListCityMapAoisResponseBodyData(TeaModel):
    def __init__(
        self,
        value: str = None,
        id: str = None,
    ):
        self.value = value
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.value is not None:
            result['Value'] = self.value
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class ListCityMapAoisResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        message: str = None,
        request_id: str = None,
        data: List[ListCityMapAoisResponseBodyData] = None,
        code: str = None,
    ):
        self.total_count = total_count
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListCityMapAoisResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class ListCityMapAoisResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListCityMapAoisResponseBody = None,
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
            temp_model = ListCityMapAoisResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCityMapCameraResultsRequest(TeaModel):
    def __init__(
        self,
        data_source_id_list: Dict[str, Any] = None,
        page_num: int = None,
        page_size: int = None,
    ):
        self.data_source_id_list = data_source_id_list
        self.page_num = page_num
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_source_id_list is not None:
            result['DataSourceIdList'] = self.data_source_id_list
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSourceIdList') is not None:
            self.data_source_id_list = m.get('DataSourceIdList')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListCityMapCameraResultsShrinkRequest(TeaModel):
    def __init__(
        self,
        data_source_id_list_shrink: str = None,
        page_num: int = None,
        page_size: int = None,
    ):
        self.data_source_id_list_shrink = data_source_id_list_shrink
        self.page_num = page_num
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_source_id_list_shrink is not None:
            result['DataSourceIdList'] = self.data_source_id_list_shrink
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSourceIdList') is not None:
            self.data_source_id_list_shrink = m.get('DataSourceIdList')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListCityMapCameraResultsResponseBodyData(TeaModel):
    def __init__(
        self,
        data_source_name: str = None,
        data_source_id: str = None,
        corp_id: str = None,
        longitude: str = None,
        latitude: str = None,
        data_source_poi: str = None,
        near_poi: str = None,
    ):
        self.data_source_name = data_source_name
        self.data_source_id = data_source_id
        self.corp_id = corp_id
        self.longitude = longitude
        self.latitude = latitude
        self.data_source_poi = data_source_poi
        self.near_poi = near_poi

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_source_name is not None:
            result['DataSourceName'] = self.data_source_name
        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.longitude is not None:
            result['Longitude'] = self.longitude
        if self.latitude is not None:
            result['Latitude'] = self.latitude
        if self.data_source_poi is not None:
            result['DataSourcePoi'] = self.data_source_poi
        if self.near_poi is not None:
            result['NearPoi'] = self.near_poi
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSourceName') is not None:
            self.data_source_name = m.get('DataSourceName')
        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('Longitude') is not None:
            self.longitude = m.get('Longitude')
        if m.get('Latitude') is not None:
            self.latitude = m.get('Latitude')
        if m.get('DataSourcePoi') is not None:
            self.data_source_poi = m.get('DataSourcePoi')
        if m.get('NearPoi') is not None:
            self.near_poi = m.get('NearPoi')
        return self


class ListCityMapCameraResultsResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        page_num: str = None,
        request_id: str = None,
        message: str = None,
        page_size: str = None,
        data: List[ListCityMapCameraResultsResponseBodyData] = None,
        code: str = None,
    ):
        self.total_count = total_count
        self.page_num = page_num
        self.request_id = request_id
        self.message = message
        self.page_size = page_size
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListCityMapCameraResultsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class ListCityMapCameraResultsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListCityMapCameraResultsResponseBody = None,
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
            temp_model = ListCityMapCameraResultsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCityMapCameraStatisticsRequest(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        start_time: str = None,
        data_source_id_list: str = None,
        page_size: int = None,
        page_number: int = None,
    ):
        self.end_time = end_time
        self.start_time = start_time
        self.data_source_id_list = data_source_id_list
        self.page_size = page_size
        self.page_number = page_number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.data_source_id_list is not None:
            result['DataSourceIdList'] = self.data_source_id_list
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('DataSourceIdList') is not None:
            self.data_source_id_list = m.get('DataSourceIdList')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        return self


class ListCityMapCameraStatisticsResponseBodyData(TeaModel):
    def __init__(
        self,
        old_value: str = None,
        data_source_name: str = None,
        data_source_id: str = None,
        statistic_time: str = None,
        adult_value: str = None,
        child_value: str = None,
        man_value: str = None,
        corp_id: str = None,
        motor_value: str = None,
        longitude: str = None,
        latitude: str = None,
        woman_value: str = None,
    ):
        self.old_value = old_value
        self.data_source_name = data_source_name
        self.data_source_id = data_source_id
        self.statistic_time = statistic_time
        self.adult_value = adult_value
        self.child_value = child_value
        self.man_value = man_value
        self.corp_id = corp_id
        self.motor_value = motor_value
        self.longitude = longitude
        self.latitude = latitude
        self.woman_value = woman_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.old_value is not None:
            result['OldValue'] = self.old_value
        if self.data_source_name is not None:
            result['DataSourceName'] = self.data_source_name
        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id
        if self.statistic_time is not None:
            result['StatisticTime'] = self.statistic_time
        if self.adult_value is not None:
            result['AdultValue'] = self.adult_value
        if self.child_value is not None:
            result['ChildValue'] = self.child_value
        if self.man_value is not None:
            result['ManValue'] = self.man_value
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.motor_value is not None:
            result['MotorValue'] = self.motor_value
        if self.longitude is not None:
            result['Longitude'] = self.longitude
        if self.latitude is not None:
            result['Latitude'] = self.latitude
        if self.woman_value is not None:
            result['WomanValue'] = self.woman_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OldValue') is not None:
            self.old_value = m.get('OldValue')
        if m.get('DataSourceName') is not None:
            self.data_source_name = m.get('DataSourceName')
        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')
        if m.get('StatisticTime') is not None:
            self.statistic_time = m.get('StatisticTime')
        if m.get('AdultValue') is not None:
            self.adult_value = m.get('AdultValue')
        if m.get('ChildValue') is not None:
            self.child_value = m.get('ChildValue')
        if m.get('ManValue') is not None:
            self.man_value = m.get('ManValue')
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('MotorValue') is not None:
            self.motor_value = m.get('MotorValue')
        if m.get('Longitude') is not None:
            self.longitude = m.get('Longitude')
        if m.get('Latitude') is not None:
            self.latitude = m.get('Latitude')
        if m.get('WomanValue') is not None:
            self.woman_value = m.get('WomanValue')
        return self


class ListCityMapCameraStatisticsResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        message: str = None,
        page_size: int = None,
        page_number: int = None,
        data: List[ListCityMapCameraStatisticsResponseBodyData] = None,
        code: str = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.message = message
        self.page_size = page_size
        self.page_number = page_number
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListCityMapCameraStatisticsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class ListCityMapCameraStatisticsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListCityMapCameraStatisticsResponseBody = None,
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
            temp_model = ListCityMapCameraStatisticsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCityMapImageDetailsRequest(TeaModel):
    def __init__(
        self,
        data_source_id: str = None,
        record_number: int = None,
        time_interval: str = None,
    ):
        self.data_source_id = data_source_id
        self.record_number = record_number
        self.time_interval = time_interval

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id
        if self.record_number is not None:
            result['RecordNumber'] = self.record_number
        if self.time_interval is not None:
            result['TimeInterval'] = self.time_interval
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')
        if m.get('RecordNumber') is not None:
            self.record_number = m.get('RecordNumber')
        if m.get('TimeInterval') is not None:
            self.time_interval = m.get('TimeInterval')
        return self


class ListCityMapImageDetailsResponseBodyData(TeaModel):
    def __init__(
        self,
        motor_target_image_storage_path: str = None,
        right_bottom_y: str = None,
        data_source_id: str = None,
        record_id: str = None,
        vehicle_color: str = None,
        source_image_storage_path: str = None,
        age_up_limit: str = None,
        coat_color: str = None,
        right_bottom_x: str = None,
        trousers_color_reliability: str = None,
        age_lower_limit: str = None,
        left_top_y: str = None,
        shot_time: str = None,
        person_target_image_storage_path: str = None,
        vehicle_class_reliability: str = None,
        gender_code_reliability: str = None,
        gender: str = None,
        trousers_color: str = None,
        age_code_reliability: str = None,
        face_target_image_storage_path: str = None,
        vehicle_class: str = None,
        vehicle_color_reliability: str = None,
        left_top_x: str = None,
        age_lower_limit_reliability: str = None,
        coat_color_reliability: str = None,
    ):
        self.motor_target_image_storage_path = motor_target_image_storage_path
        self.right_bottom_y = right_bottom_y
        self.data_source_id = data_source_id
        self.record_id = record_id
        self.vehicle_color = vehicle_color
        self.source_image_storage_path = source_image_storage_path
        self.age_up_limit = age_up_limit
        self.coat_color = coat_color
        self.right_bottom_x = right_bottom_x
        self.trousers_color_reliability = trousers_color_reliability
        self.age_lower_limit = age_lower_limit
        self.left_top_y = left_top_y
        self.shot_time = shot_time
        self.person_target_image_storage_path = person_target_image_storage_path
        self.vehicle_class_reliability = vehicle_class_reliability
        self.gender_code_reliability = gender_code_reliability
        self.gender = gender
        self.trousers_color = trousers_color
        self.age_code_reliability = age_code_reliability
        self.face_target_image_storage_path = face_target_image_storage_path
        self.vehicle_class = vehicle_class
        self.vehicle_color_reliability = vehicle_color_reliability
        self.left_top_x = left_top_x
        self.age_lower_limit_reliability = age_lower_limit_reliability
        self.coat_color_reliability = coat_color_reliability

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.motor_target_image_storage_path is not None:
            result['MotorTargetImageStoragePath'] = self.motor_target_image_storage_path
        if self.right_bottom_y is not None:
            result['RightBottomY'] = self.right_bottom_y
        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id
        if self.record_id is not None:
            result['RecordId'] = self.record_id
        if self.vehicle_color is not None:
            result['VehicleColor'] = self.vehicle_color
        if self.source_image_storage_path is not None:
            result['SourceImageStoragePath'] = self.source_image_storage_path
        if self.age_up_limit is not None:
            result['AgeUpLimit'] = self.age_up_limit
        if self.coat_color is not None:
            result['CoatColor'] = self.coat_color
        if self.right_bottom_x is not None:
            result['RightBottomX'] = self.right_bottom_x
        if self.trousers_color_reliability is not None:
            result['TrousersColorReliability'] = self.trousers_color_reliability
        if self.age_lower_limit is not None:
            result['AgeLowerLimit'] = self.age_lower_limit
        if self.left_top_y is not None:
            result['LeftTopY'] = self.left_top_y
        if self.shot_time is not None:
            result['ShotTime'] = self.shot_time
        if self.person_target_image_storage_path is not None:
            result['PersonTargetImageStoragePath'] = self.person_target_image_storage_path
        if self.vehicle_class_reliability is not None:
            result['VehicleClassReliability'] = self.vehicle_class_reliability
        if self.gender_code_reliability is not None:
            result['GenderCodeReliability'] = self.gender_code_reliability
        if self.gender is not None:
            result['Gender'] = self.gender
        if self.trousers_color is not None:
            result['TrousersColor'] = self.trousers_color
        if self.age_code_reliability is not None:
            result['AgeCodeReliability'] = self.age_code_reliability
        if self.face_target_image_storage_path is not None:
            result['FaceTargetImageStoragePath'] = self.face_target_image_storage_path
        if self.vehicle_class is not None:
            result['VehicleClass'] = self.vehicle_class
        if self.vehicle_color_reliability is not None:
            result['VehicleColorReliability'] = self.vehicle_color_reliability
        if self.left_top_x is not None:
            result['LeftTopX'] = self.left_top_x
        if self.age_lower_limit_reliability is not None:
            result['AgeLowerLimitReliability'] = self.age_lower_limit_reliability
        if self.coat_color_reliability is not None:
            result['CoatColorReliability'] = self.coat_color_reliability
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MotorTargetImageStoragePath') is not None:
            self.motor_target_image_storage_path = m.get('MotorTargetImageStoragePath')
        if m.get('RightBottomY') is not None:
            self.right_bottom_y = m.get('RightBottomY')
        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')
        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')
        if m.get('VehicleColor') is not None:
            self.vehicle_color = m.get('VehicleColor')
        if m.get('SourceImageStoragePath') is not None:
            self.source_image_storage_path = m.get('SourceImageStoragePath')
        if m.get('AgeUpLimit') is not None:
            self.age_up_limit = m.get('AgeUpLimit')
        if m.get('CoatColor') is not None:
            self.coat_color = m.get('CoatColor')
        if m.get('RightBottomX') is not None:
            self.right_bottom_x = m.get('RightBottomX')
        if m.get('TrousersColorReliability') is not None:
            self.trousers_color_reliability = m.get('TrousersColorReliability')
        if m.get('AgeLowerLimit') is not None:
            self.age_lower_limit = m.get('AgeLowerLimit')
        if m.get('LeftTopY') is not None:
            self.left_top_y = m.get('LeftTopY')
        if m.get('ShotTime') is not None:
            self.shot_time = m.get('ShotTime')
        if m.get('PersonTargetImageStoragePath') is not None:
            self.person_target_image_storage_path = m.get('PersonTargetImageStoragePath')
        if m.get('VehicleClassReliability') is not None:
            self.vehicle_class_reliability = m.get('VehicleClassReliability')
        if m.get('GenderCodeReliability') is not None:
            self.gender_code_reliability = m.get('GenderCodeReliability')
        if m.get('Gender') is not None:
            self.gender = m.get('Gender')
        if m.get('TrousersColor') is not None:
            self.trousers_color = m.get('TrousersColor')
        if m.get('AgeCodeReliability') is not None:
            self.age_code_reliability = m.get('AgeCodeReliability')
        if m.get('FaceTargetImageStoragePath') is not None:
            self.face_target_image_storage_path = m.get('FaceTargetImageStoragePath')
        if m.get('VehicleClass') is not None:
            self.vehicle_class = m.get('VehicleClass')
        if m.get('VehicleColorReliability') is not None:
            self.vehicle_color_reliability = m.get('VehicleColorReliability')
        if m.get('LeftTopX') is not None:
            self.left_top_x = m.get('LeftTopX')
        if m.get('AgeLowerLimitReliability') is not None:
            self.age_lower_limit_reliability = m.get('AgeLowerLimitReliability')
        if m.get('CoatColorReliability') is not None:
            self.coat_color_reliability = m.get('CoatColorReliability')
        return self


class ListCityMapImageDetailsResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        message: str = None,
        page_size: int = None,
        page_number: int = None,
        data: List[ListCityMapImageDetailsResponseBodyData] = None,
        code: str = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.message = message
        self.page_size = page_size
        self.page_number = page_number
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListCityMapImageDetailsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class ListCityMapImageDetailsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListCityMapImageDetailsResponseBody = None,
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
            temp_model = ListCityMapImageDetailsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCityMapPersonFlowRequest(TeaModel):
    def __init__(
        self,
        origin_data_source_id_list: Dict[str, Any] = None,
        page_number: int = None,
        page_size: int = None,
        target_data_source_id_list: Dict[str, Any] = None,
        end_time: str = None,
        start_time: str = None,
        range: str = None,
    ):
        self.origin_data_source_id_list = origin_data_source_id_list
        self.page_number = page_number
        self.page_size = page_size
        self.target_data_source_id_list = target_data_source_id_list
        self.end_time = end_time
        self.start_time = start_time
        self.range = range

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.origin_data_source_id_list is not None:
            result['OriginDataSourceIdList'] = self.origin_data_source_id_list
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.target_data_source_id_list is not None:
            result['TargetDataSourceIdList'] = self.target_data_source_id_list
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.range is not None:
            result['Range'] = self.range
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OriginDataSourceIdList') is not None:
            self.origin_data_source_id_list = m.get('OriginDataSourceIdList')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TargetDataSourceIdList') is not None:
            self.target_data_source_id_list = m.get('TargetDataSourceIdList')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Range') is not None:
            self.range = m.get('Range')
        return self


class ListCityMapPersonFlowShrinkRequest(TeaModel):
    def __init__(
        self,
        origin_data_source_id_list_shrink: str = None,
        page_number: int = None,
        page_size: int = None,
        target_data_source_id_list_shrink: str = None,
        end_time: str = None,
        start_time: str = None,
        range: str = None,
    ):
        self.origin_data_source_id_list_shrink = origin_data_source_id_list_shrink
        self.page_number = page_number
        self.page_size = page_size
        self.target_data_source_id_list_shrink = target_data_source_id_list_shrink
        self.end_time = end_time
        self.start_time = start_time
        self.range = range

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.origin_data_source_id_list_shrink is not None:
            result['OriginDataSourceIdList'] = self.origin_data_source_id_list_shrink
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.target_data_source_id_list_shrink is not None:
            result['TargetDataSourceIdList'] = self.target_data_source_id_list_shrink
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.range is not None:
            result['Range'] = self.range
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OriginDataSourceIdList') is not None:
            self.origin_data_source_id_list_shrink = m.get('OriginDataSourceIdList')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TargetDataSourceIdList') is not None:
            self.target_data_source_id_list_shrink = m.get('TargetDataSourceIdList')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Range') is not None:
            self.range = m.get('Range')
        return self


class ListCityMapPersonFlowResponseBodyData(TeaModel):
    def __init__(
        self,
        flow_number: str = None,
        origin_data_source_id: str = None,
        target_data_source_id: str = None,
        flow_direction: str = None,
    ):
        self.flow_number = flow_number
        self.origin_data_source_id = origin_data_source_id
        self.target_data_source_id = target_data_source_id
        self.flow_direction = flow_direction

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flow_number is not None:
            result['FlowNumber'] = self.flow_number
        if self.origin_data_source_id is not None:
            result['OriginDataSourceId'] = self.origin_data_source_id
        if self.target_data_source_id is not None:
            result['TargetDataSourceId'] = self.target_data_source_id
        if self.flow_direction is not None:
            result['FlowDirection'] = self.flow_direction
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FlowNumber') is not None:
            self.flow_number = m.get('FlowNumber')
        if m.get('OriginDataSourceId') is not None:
            self.origin_data_source_id = m.get('OriginDataSourceId')
        if m.get('TargetDataSourceId') is not None:
            self.target_data_source_id = m.get('TargetDataSourceId')
        if m.get('FlowDirection') is not None:
            self.flow_direction = m.get('FlowDirection')
        return self


class ListCityMapPersonFlowResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        message: str = None,
        page_size: int = None,
        page_number: int = None,
        data: List[ListCityMapPersonFlowResponseBodyData] = None,
        code: str = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.message = message
        self.page_size = page_size
        self.page_number = page_number
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListCityMapPersonFlowResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class ListCityMapPersonFlowResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListCityMapPersonFlowResponseBody = None,
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
            temp_model = ListCityMapPersonFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCityMapRangeStatisticRequest(TeaModel):
    def __init__(
        self,
        radius: int = None,
        latitude: str = None,
        longitude: str = None,
        end_time: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.radius = radius
        self.latitude = latitude
        self.longitude = longitude
        self.end_time = end_time
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.radius is not None:
            result['Radius'] = self.radius
        if self.latitude is not None:
            result['Latitude'] = self.latitude
        if self.longitude is not None:
            result['Longitude'] = self.longitude
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Radius') is not None:
            self.radius = m.get('Radius')
        if m.get('Latitude') is not None:
            self.latitude = m.get('Latitude')
        if m.get('Longitude') is not None:
            self.longitude = m.get('Longitude')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListCityMapRangeStatisticResponseBodyData(TeaModel):
    def __init__(
        self,
        adult_value: str = None,
        child_value: str = None,
        old_value: str = None,
        man_value: str = None,
        data_source_name: str = None,
        data_source_id: str = None,
        corp_id: str = None,
        motor_value: str = None,
        longitude: str = None,
        latitude: str = None,
        woman_value: str = None,
    ):
        self.adult_value = adult_value
        self.child_value = child_value
        self.old_value = old_value
        self.man_value = man_value
        self.data_source_name = data_source_name
        self.data_source_id = data_source_id
        self.corp_id = corp_id
        self.motor_value = motor_value
        self.longitude = longitude
        self.latitude = latitude
        self.woman_value = woman_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.adult_value is not None:
            result['AdultValue'] = self.adult_value
        if self.child_value is not None:
            result['ChildValue'] = self.child_value
        if self.old_value is not None:
            result['OldValue'] = self.old_value
        if self.man_value is not None:
            result['ManValue'] = self.man_value
        if self.data_source_name is not None:
            result['DataSourceName'] = self.data_source_name
        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.motor_value is not None:
            result['MotorValue'] = self.motor_value
        if self.longitude is not None:
            result['Longitude'] = self.longitude
        if self.latitude is not None:
            result['Latitude'] = self.latitude
        if self.woman_value is not None:
            result['WomanValue'] = self.woman_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdultValue') is not None:
            self.adult_value = m.get('AdultValue')
        if m.get('ChildValue') is not None:
            self.child_value = m.get('ChildValue')
        if m.get('OldValue') is not None:
            self.old_value = m.get('OldValue')
        if m.get('ManValue') is not None:
            self.man_value = m.get('ManValue')
        if m.get('DataSourceName') is not None:
            self.data_source_name = m.get('DataSourceName')
        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('MotorValue') is not None:
            self.motor_value = m.get('MotorValue')
        if m.get('Longitude') is not None:
            self.longitude = m.get('Longitude')
        if m.get('Latitude') is not None:
            self.latitude = m.get('Latitude')
        if m.get('WomanValue') is not None:
            self.woman_value = m.get('WomanValue')
        return self


class ListCityMapRangeStatisticResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        message: str = None,
        page_size: int = None,
        page_number: int = None,
        data: List[ListCityMapRangeStatisticResponseBodyData] = None,
        code: str = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.message = message
        self.page_size = page_size
        self.page_number = page_number
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListCityMapRangeStatisticResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class ListCityMapRangeStatisticResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListCityMapRangeStatisticResponseBody = None,
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
            temp_model = ListCityMapRangeStatisticResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCorpMetricsRequest(TeaModel):
    def __init__(
        self,
        corp_id: Dict[str, Any] = None,
        tag_code: str = None,
        start_time: str = None,
        end_time: str = None,
        page_number: int = None,
        page_size: int = None,
        user_group_list: Dict[str, Any] = None,
        device_group_list: Dict[str, Any] = None,
        device_id_list: Dict[str, Any] = None,
    ):
        self.corp_id = corp_id
        self.tag_code = tag_code
        self.start_time = start_time
        self.end_time = end_time
        self.page_number = page_number
        self.page_size = page_size
        self.user_group_list = user_group_list
        self.device_group_list = device_group_list
        self.device_id_list = device_id_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.tag_code is not None:
            result['TagCode'] = self.tag_code
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.user_group_list is not None:
            result['UserGroupList'] = self.user_group_list
        if self.device_group_list is not None:
            result['DeviceGroupList'] = self.device_group_list
        if self.device_id_list is not None:
            result['DeviceIdList'] = self.device_id_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('TagCode') is not None:
            self.tag_code = m.get('TagCode')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('UserGroupList') is not None:
            self.user_group_list = m.get('UserGroupList')
        if m.get('DeviceGroupList') is not None:
            self.device_group_list = m.get('DeviceGroupList')
        if m.get('DeviceIdList') is not None:
            self.device_id_list = m.get('DeviceIdList')
        return self


class ListCorpMetricsShrinkRequest(TeaModel):
    def __init__(
        self,
        corp_id_shrink: str = None,
        tag_code: str = None,
        start_time: str = None,
        end_time: str = None,
        page_number: int = None,
        page_size: int = None,
        user_group_list_shrink: str = None,
        device_group_list_shrink: str = None,
        device_id_list_shrink: str = None,
    ):
        self.corp_id_shrink = corp_id_shrink
        self.tag_code = tag_code
        self.start_time = start_time
        self.end_time = end_time
        self.page_number = page_number
        self.page_size = page_size
        self.user_group_list_shrink = user_group_list_shrink
        self.device_group_list_shrink = device_group_list_shrink
        self.device_id_list_shrink = device_id_list_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id_shrink is not None:
            result['CorpId'] = self.corp_id_shrink
        if self.tag_code is not None:
            result['TagCode'] = self.tag_code
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.user_group_list_shrink is not None:
            result['UserGroupList'] = self.user_group_list_shrink
        if self.device_group_list_shrink is not None:
            result['DeviceGroupList'] = self.device_group_list_shrink
        if self.device_id_list_shrink is not None:
            result['DeviceIdList'] = self.device_id_list_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorpId') is not None:
            self.corp_id_shrink = m.get('CorpId')
        if m.get('TagCode') is not None:
            self.tag_code = m.get('TagCode')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('UserGroupList') is not None:
            self.user_group_list_shrink = m.get('UserGroupList')
        if m.get('DeviceGroupList') is not None:
            self.device_group_list_shrink = m.get('DeviceGroupList')
        if m.get('DeviceIdList') is not None:
            self.device_id_list_shrink = m.get('DeviceIdList')
        return self


class ListCorpMetricsResponseBodyData(TeaModel):
    def __init__(
        self,
        date_id: str = None,
        device_group_id: str = None,
        device_id: str = None,
        tag_code: str = None,
        user_group_id: str = None,
        corp_id: str = None,
        tag_metrics: str = None,
        tag_value: str = None,
        person_id: str = None,
    ):
        self.date_id = date_id
        self.device_group_id = device_group_id
        self.device_id = device_id
        self.tag_code = tag_code
        self.user_group_id = user_group_id
        self.corp_id = corp_id
        self.tag_metrics = tag_metrics
        self.tag_value = tag_value
        self.person_id = person_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.date_id is not None:
            result['DateId'] = self.date_id
        if self.device_group_id is not None:
            result['DeviceGroupId'] = self.device_group_id
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.tag_code is not None:
            result['TagCode'] = self.tag_code
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.tag_metrics is not None:
            result['TagMetrics'] = self.tag_metrics
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        if self.person_id is not None:
            result['PersonId'] = self.person_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DateId') is not None:
            self.date_id = m.get('DateId')
        if m.get('DeviceGroupId') is not None:
            self.device_group_id = m.get('DeviceGroupId')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('TagCode') is not None:
            self.tag_code = m.get('TagCode')
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('TagMetrics') is not None:
            self.tag_metrics = m.get('TagMetrics')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        if m.get('PersonId') is not None:
            self.person_id = m.get('PersonId')
        return self


class ListCorpMetricsResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        message: str = None,
        page_size: int = None,
        page_number: int = None,
        data: List[ListCorpMetricsResponseBodyData] = None,
        code: str = None,
        success: str = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.message = message
        self.page_size = page_size
        self.page_number = page_number
        self.data = data
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListCorpMetricsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListCorpMetricsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListCorpMetricsResponseBody = None,
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
            temp_model = ListCorpMetricsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCorpMetricsStatisticRequest(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        tag_code: str = None,
        start_time: str = None,
        end_time: str = None,
        page_number: int = None,
        page_size: int = None,
        user_group_list: Dict[str, Any] = None,
        device_group_list: Dict[str, Any] = None,
        device_id_list: Dict[str, Any] = None,
        qualit_score: str = None,
    ):
        self.corp_id = corp_id
        self.tag_code = tag_code
        self.start_time = start_time
        self.end_time = end_time
        self.page_number = page_number
        self.page_size = page_size
        self.user_group_list = user_group_list
        self.device_group_list = device_group_list
        self.device_id_list = device_id_list
        self.qualit_score = qualit_score

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.tag_code is not None:
            result['TagCode'] = self.tag_code
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.user_group_list is not None:
            result['UserGroupList'] = self.user_group_list
        if self.device_group_list is not None:
            result['DeviceGroupList'] = self.device_group_list
        if self.device_id_list is not None:
            result['DeviceIdList'] = self.device_id_list
        if self.qualit_score is not None:
            result['QualitScore'] = self.qualit_score
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('TagCode') is not None:
            self.tag_code = m.get('TagCode')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('UserGroupList') is not None:
            self.user_group_list = m.get('UserGroupList')
        if m.get('DeviceGroupList') is not None:
            self.device_group_list = m.get('DeviceGroupList')
        if m.get('DeviceIdList') is not None:
            self.device_id_list = m.get('DeviceIdList')
        if m.get('QualitScore') is not None:
            self.qualit_score = m.get('QualitScore')
        return self


class ListCorpMetricsStatisticShrinkRequest(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        tag_code: str = None,
        start_time: str = None,
        end_time: str = None,
        page_number: int = None,
        page_size: int = None,
        user_group_list_shrink: str = None,
        device_group_list_shrink: str = None,
        device_id_list_shrink: str = None,
        qualit_score: str = None,
    ):
        self.corp_id = corp_id
        self.tag_code = tag_code
        self.start_time = start_time
        self.end_time = end_time
        self.page_number = page_number
        self.page_size = page_size
        self.user_group_list_shrink = user_group_list_shrink
        self.device_group_list_shrink = device_group_list_shrink
        self.device_id_list_shrink = device_id_list_shrink
        self.qualit_score = qualit_score

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.tag_code is not None:
            result['TagCode'] = self.tag_code
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.user_group_list_shrink is not None:
            result['UserGroupList'] = self.user_group_list_shrink
        if self.device_group_list_shrink is not None:
            result['DeviceGroupList'] = self.device_group_list_shrink
        if self.device_id_list_shrink is not None:
            result['DeviceIdList'] = self.device_id_list_shrink
        if self.qualit_score is not None:
            result['QualitScore'] = self.qualit_score
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('TagCode') is not None:
            self.tag_code = m.get('TagCode')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('UserGroupList') is not None:
            self.user_group_list_shrink = m.get('UserGroupList')
        if m.get('DeviceGroupList') is not None:
            self.device_group_list_shrink = m.get('DeviceGroupList')
        if m.get('DeviceIdList') is not None:
            self.device_id_list_shrink = m.get('DeviceIdList')
        if m.get('QualitScore') is not None:
            self.qualit_score = m.get('QualitScore')
        return self


class ListCorpMetricsStatisticResponseBodyData(TeaModel):
    def __init__(
        self,
        date_id: str = None,
        device_group_id: str = None,
        device_id: str = None,
        tag_code: str = None,
        user_group_id: str = None,
        corp_id: str = None,
        tag_metrics: str = None,
        tag_value: str = None,
        person_id: str = None,
    ):
        self.date_id = date_id
        self.device_group_id = device_group_id
        self.device_id = device_id
        self.tag_code = tag_code
        self.user_group_id = user_group_id
        self.corp_id = corp_id
        self.tag_metrics = tag_metrics
        self.tag_value = tag_value
        self.person_id = person_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.date_id is not None:
            result['DateId'] = self.date_id
        if self.device_group_id is not None:
            result['DeviceGroupId'] = self.device_group_id
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.tag_code is not None:
            result['TagCode'] = self.tag_code
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.tag_metrics is not None:
            result['TagMetrics'] = self.tag_metrics
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        if self.person_id is not None:
            result['PersonId'] = self.person_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DateId') is not None:
            self.date_id = m.get('DateId')
        if m.get('DeviceGroupId') is not None:
            self.device_group_id = m.get('DeviceGroupId')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('TagCode') is not None:
            self.tag_code = m.get('TagCode')
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('TagMetrics') is not None:
            self.tag_metrics = m.get('TagMetrics')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        if m.get('PersonId') is not None:
            self.person_id = m.get('PersonId')
        return self


class ListCorpMetricsStatisticResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        message: str = None,
        page_size: int = None,
        page_number: int = None,
        data: List[ListCorpMetricsStatisticResponseBodyData] = None,
        code: str = None,
        success: str = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.message = message
        self.page_size = page_size
        self.page_number = page_number
        self.data = data
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListCorpMetricsStatisticResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListCorpMetricsStatisticResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListCorpMetricsStatisticResponseBody = None,
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
            temp_model = ListCorpMetricsStatisticResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCorpTrackDetailRequest(TeaModel):
    def __init__(
        self,
        start_time: str = None,
        corp_id: str = None,
        page_number: str = None,
        page_size: str = None,
        end_time: str = None,
        data_source_id: Dict[str, Any] = None,
        person_id: Dict[str, Any] = None,
    ):
        self.start_time = start_time
        self.corp_id = corp_id
        self.page_number = page_number
        self.page_size = page_size
        self.end_time = end_time
        self.data_source_id = data_source_id
        self.person_id = person_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id
        if self.person_id is not None:
            result['PersonId'] = self.person_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')
        if m.get('PersonId') is not None:
            self.person_id = m.get('PersonId')
        return self


class ListCorpTrackDetailShrinkRequest(TeaModel):
    def __init__(
        self,
        start_time: str = None,
        corp_id: str = None,
        page_number: str = None,
        page_size: str = None,
        end_time: str = None,
        data_source_id_shrink: str = None,
        person_id_shrink: str = None,
    ):
        self.start_time = start_time
        self.corp_id = corp_id
        self.page_number = page_number
        self.page_size = page_size
        self.end_time = end_time
        self.data_source_id_shrink = data_source_id_shrink
        self.person_id_shrink = person_id_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.data_source_id_shrink is not None:
            result['DataSourceId'] = self.data_source_id_shrink
        if self.person_id_shrink is not None:
            result['PersonId'] = self.person_id_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('DataSourceId') is not None:
            self.data_source_id_shrink = m.get('DataSourceId')
        if m.get('PersonId') is not None:
            self.person_id_shrink = m.get('PersonId')
        return self


class ListCorpTrackDetailResponseBodyData(TeaModel):
    def __init__(
        self,
        end_target_image: str = None,
        source_url: str = None,
        device_id: str = None,
        end_source_image: str = None,
        start_source_image: str = None,
        date: str = None,
        start_target_image: str = None,
        last_time: str = None,
        start_time: str = None,
        group_id: str = None,
        target_url: str = None,
        corp_id: str = None,
        person_id: str = None,
    ):
        self.end_target_image = end_target_image
        self.source_url = source_url
        self.device_id = device_id
        self.end_source_image = end_source_image
        self.start_source_image = start_source_image
        self.date = date
        self.start_target_image = start_target_image
        self.last_time = last_time
        self.start_time = start_time
        self.group_id = group_id
        self.target_url = target_url
        self.corp_id = corp_id
        self.person_id = person_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_target_image is not None:
            result['EndTargetImage'] = self.end_target_image
        if self.source_url is not None:
            result['SourceUrl'] = self.source_url
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.end_source_image is not None:
            result['EndSourceImage'] = self.end_source_image
        if self.start_source_image is not None:
            result['StartSourceImage'] = self.start_source_image
        if self.date is not None:
            result['Date'] = self.date
        if self.start_target_image is not None:
            result['StartTargetImage'] = self.start_target_image
        if self.last_time is not None:
            result['LastTime'] = self.last_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.target_url is not None:
            result['TargetUrl'] = self.target_url
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.person_id is not None:
            result['PersonId'] = self.person_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTargetImage') is not None:
            self.end_target_image = m.get('EndTargetImage')
        if m.get('SourceUrl') is not None:
            self.source_url = m.get('SourceUrl')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('EndSourceImage') is not None:
            self.end_source_image = m.get('EndSourceImage')
        if m.get('StartSourceImage') is not None:
            self.start_source_image = m.get('StartSourceImage')
        if m.get('Date') is not None:
            self.date = m.get('Date')
        if m.get('StartTargetImage') is not None:
            self.start_target_image = m.get('StartTargetImage')
        if m.get('LastTime') is not None:
            self.last_time = m.get('LastTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('TargetUrl') is not None:
            self.target_url = m.get('TargetUrl')
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('PersonId') is not None:
            self.person_id = m.get('PersonId')
        return self


class ListCorpTrackDetailResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        message: str = None,
        page_size: int = None,
        page_number: int = None,
        data: List[ListCorpTrackDetailResponseBodyData] = None,
        code: str = None,
        success: str = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.message = message
        self.page_size = page_size
        self.page_number = page_number
        self.data = data
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListCorpTrackDetailResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListCorpTrackDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListCorpTrackDetailResponseBody = None,
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
            temp_model = ListCorpTrackDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDataStatisticsRequest(TeaModel):
    def __init__(
        self,
        back_category: str = None,
        schema: str = None,
    ):
        self.back_category = back_category
        self.schema = schema

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.back_category is not None:
            result['BackCategory'] = self.back_category
        if self.schema is not None:
            result['Schema'] = self.schema
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackCategory') is not None:
            self.back_category = m.get('BackCategory')
        if m.get('Schema') is not None:
            self.schema = m.get('Schema')
        return self


class ListDataStatisticsResponseBodyData(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        number: str = None,
    ):
        self.corp_id = corp_id
        self.number = number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.number is not None:
            result['Number'] = self.number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('Number') is not None:
            self.number = m.get('Number')
        return self


class ListDataStatisticsResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        message: str = None,
        page_size: int = None,
        page_number: int = None,
        data: List[ListDataStatisticsResponseBodyData] = None,
        code: str = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.message = message
        self.page_size = page_size
        self.page_number = page_number
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListDataStatisticsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class ListDataStatisticsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListDataStatisticsResponseBody = None,
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
            temp_model = ListDataStatisticsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDataStatisticsByDayRequest(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        start_time: str = None,
        end_time: str = None,
    ):
        self.corp_id = corp_id
        self.start_time = start_time
        self.end_time = end_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        return self


class ListDataStatisticsByDayResponseBodyData(TeaModel):
    def __init__(
        self,
        non_motor_number: int = None,
        face_number: int = None,
        motor_number: int = None,
        corp_id: str = None,
        date: str = None,
        body_number: int = None,
        total_number: int = None,
    ):
        self.non_motor_number = non_motor_number
        self.face_number = face_number
        self.motor_number = motor_number
        self.corp_id = corp_id
        self.date = date
        self.body_number = body_number
        self.total_number = total_number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.non_motor_number is not None:
            result['NonMotorNumber'] = self.non_motor_number
        if self.face_number is not None:
            result['FaceNumber'] = self.face_number
        if self.motor_number is not None:
            result['MotorNumber'] = self.motor_number
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.date is not None:
            result['Date'] = self.date
        if self.body_number is not None:
            result['BodyNumber'] = self.body_number
        if self.total_number is not None:
            result['TotalNumber'] = self.total_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NonMotorNumber') is not None:
            self.non_motor_number = m.get('NonMotorNumber')
        if m.get('FaceNumber') is not None:
            self.face_number = m.get('FaceNumber')
        if m.get('MotorNumber') is not None:
            self.motor_number = m.get('MotorNumber')
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('Date') is not None:
            self.date = m.get('Date')
        if m.get('BodyNumber') is not None:
            self.body_number = m.get('BodyNumber')
        if m.get('TotalNumber') is not None:
            self.total_number = m.get('TotalNumber')
        return self


class ListDataStatisticsByDayResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        message: str = None,
        page_size: int = None,
        page_number: int = None,
        data: List[ListDataStatisticsByDayResponseBodyData] = None,
        code: str = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.message = message
        self.page_size = page_size
        self.page_number = page_number
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListDataStatisticsByDayResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class ListDataStatisticsByDayResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListDataStatisticsByDayResponseBody = None,
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
            temp_model = ListDataStatisticsByDayResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDeviceDetailRequest(TeaModel):
    def __init__(
        self,
        data_source_id: str = None,
        page_number: int = None,
        page_size: int = None,
        corp_id: str = None,
    ):
        self.data_source_id = data_source_id
        self.page_number = page_number
        self.page_size = page_size
        self.corp_id = corp_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        return self


class ListDeviceDetailResponseBodyData(TeaModel):
    def __init__(
        self,
        data_source_name: str = None,
        data_source_id: str = None,
        corp_id: str = None,
        longitude: str = None,
        latitude: str = None,
        data_source_poi: str = None,
        near_poi: str = None,
    ):
        self.data_source_name = data_source_name
        self.data_source_id = data_source_id
        self.corp_id = corp_id
        self.longitude = longitude
        self.latitude = latitude
        self.data_source_poi = data_source_poi
        self.near_poi = near_poi

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_source_name is not None:
            result['DataSourceName'] = self.data_source_name
        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.longitude is not None:
            result['Longitude'] = self.longitude
        if self.latitude is not None:
            result['Latitude'] = self.latitude
        if self.data_source_poi is not None:
            result['DataSourcePoi'] = self.data_source_poi
        if self.near_poi is not None:
            result['NearPoi'] = self.near_poi
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSourceName') is not None:
            self.data_source_name = m.get('DataSourceName')
        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('Longitude') is not None:
            self.longitude = m.get('Longitude')
        if m.get('Latitude') is not None:
            self.latitude = m.get('Latitude')
        if m.get('DataSourcePoi') is not None:
            self.data_source_poi = m.get('DataSourcePoi')
        if m.get('NearPoi') is not None:
            self.near_poi = m.get('NearPoi')
        return self


class ListDeviceDetailResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        message: str = None,
        page_size: int = None,
        page_number: int = None,
        data: List[ListDeviceDetailResponseBodyData] = None,
        code: str = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.message = message
        self.page_size = page_size
        self.page_number = page_number
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListDeviceDetailResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class ListDeviceDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListDeviceDetailResponseBody = None,
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
            temp_model = ListDeviceDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDeviceGenderStatisticsRequest(TeaModel):
    def __init__(
        self,
        data_source_id: str = None,
        start_time: str = None,
        end_time: str = None,
        corp_id: str = None,
    ):
        self.data_source_id = data_source_id
        self.start_time = start_time
        self.end_time = end_time
        self.corp_id = corp_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        return self


class ListDeviceGenderStatisticsResponseBodyData(TeaModel):
    def __init__(
        self,
        gender: str = None,
        data_source_id: str = None,
        number: str = None,
    ):
        self.gender = gender
        self.data_source_id = data_source_id
        self.number = number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gender is not None:
            result['Gender'] = self.gender
        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id
        if self.number is not None:
            result['Number'] = self.number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Gender') is not None:
            self.gender = m.get('Gender')
        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')
        if m.get('Number') is not None:
            self.number = m.get('Number')
        return self


class ListDeviceGenderStatisticsResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        message: str = None,
        request_id: str = None,
        data: List[ListDeviceGenderStatisticsResponseBodyData] = None,
        code: str = None,
    ):
        self.total_count = total_count
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListDeviceGenderStatisticsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class ListDeviceGenderStatisticsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListDeviceGenderStatisticsResponseBody = None,
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
            temp_model = ListDeviceGenderStatisticsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDevicePersonRequest(TeaModel):
    def __init__(
        self,
        data_source_id: str = None,
        statistics_type: str = None,
        start_time: str = None,
        end_time: str = None,
        page_number: int = None,
        page_size: int = None,
        corp_id: str = None,
    ):
        self.data_source_id = data_source_id
        self.statistics_type = statistics_type
        self.start_time = start_time
        self.end_time = end_time
        self.page_number = page_number
        self.page_size = page_size
        self.corp_id = corp_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id
        if self.statistics_type is not None:
            result['StatisticsType'] = self.statistics_type
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')
        if m.get('StatisticsType') is not None:
            self.statistics_type = m.get('StatisticsType')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        return self


class ListDevicePersonResponseBodyData(TeaModel):
    def __init__(
        self,
        target_pic_url_path: str = None,
        gender: str = None,
        data_source_id: str = None,
        freq_num: str = None,
        person_id: str = None,
    ):
        self.target_pic_url_path = target_pic_url_path
        self.gender = gender
        self.data_source_id = data_source_id
        self.freq_num = freq_num
        self.person_id = person_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.target_pic_url_path is not None:
            result['TargetPicUrlPath'] = self.target_pic_url_path
        if self.gender is not None:
            result['Gender'] = self.gender
        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id
        if self.freq_num is not None:
            result['FreqNum'] = self.freq_num
        if self.person_id is not None:
            result['PersonId'] = self.person_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TargetPicUrlPath') is not None:
            self.target_pic_url_path = m.get('TargetPicUrlPath')
        if m.get('Gender') is not None:
            self.gender = m.get('Gender')
        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')
        if m.get('FreqNum') is not None:
            self.freq_num = m.get('FreqNum')
        if m.get('PersonId') is not None:
            self.person_id = m.get('PersonId')
        return self


class ListDevicePersonResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        message: str = None,
        page_size: int = None,
        page_number: int = None,
        data: List[ListDevicePersonResponseBodyData] = None,
        code: str = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.message = message
        self.page_size = page_size
        self.page_number = page_number
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListDevicePersonResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class ListDevicePersonResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListDevicePersonResponseBody = None,
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
            temp_model = ListDevicePersonResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDevicePersonStatisticsRequest(TeaModel):
    def __init__(
        self,
        data_source_id: str = None,
        statistics_type: str = None,
        start_time: str = None,
        end_time: str = None,
        corp_id: str = None,
    ):
        self.data_source_id = data_source_id
        self.statistics_type = statistics_type
        self.start_time = start_time
        self.end_time = end_time
        self.corp_id = corp_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id
        if self.statistics_type is not None:
            result['StatisticsType'] = self.statistics_type
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')
        if m.get('StatisticsType') is not None:
            self.statistics_type = m.get('StatisticsType')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        return self


class ListDevicePersonStatisticsResponseBodyData(TeaModel):
    def __init__(
        self,
        data_source_id: str = None,
        number: str = None,
        shot_time: str = None,
    ):
        self.data_source_id = data_source_id
        self.number = number
        self.shot_time = shot_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id
        if self.number is not None:
            result['Number'] = self.number
        if self.shot_time is not None:
            result['ShotTime'] = self.shot_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')
        if m.get('Number') is not None:
            self.number = m.get('Number')
        if m.get('ShotTime') is not None:
            self.shot_time = m.get('ShotTime')
        return self


class ListDevicePersonStatisticsResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        message: str = None,
        request_id: str = None,
        data: List[ListDevicePersonStatisticsResponseBodyData] = None,
        code: str = None,
    ):
        self.total_count = total_count
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListDevicePersonStatisticsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class ListDevicePersonStatisticsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListDevicePersonStatisticsResponseBody = None,
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
            temp_model = ListDevicePersonStatisticsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDeviceRelationRequest(TeaModel):
    def __init__(
        self,
        device_id: str = None,
    ):
        self.device_id = device_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        return self


class ListDeviceRelationResponseBodyData(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
    ):
        self.corp_id = corp_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        return self


class ListDeviceRelationResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: List[ListDeviceRelationResponseBodyData] = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListDeviceRelationResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class ListDeviceRelationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListDeviceRelationResponseBody = None,
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
            temp_model = ListDeviceRelationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListMapRouteDetailsRequest(TeaModel):
    def __init__(
        self,
        route_list: Dict[str, Any] = None,
    ):
        self.route_list = route_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.route_list is not None:
            result['RouteList'] = self.route_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RouteList') is not None:
            self.route_list = m.get('RouteList')
        return self


class ListMapRouteDetailsShrinkRequest(TeaModel):
    def __init__(
        self,
        route_list_shrink: str = None,
    ):
        self.route_list_shrink = route_list_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.route_list_shrink is not None:
            result['RouteList'] = self.route_list_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RouteList') is not None:
            self.route_list_shrink = m.get('RouteList')
        return self


class ListMapRouteDetailsResponseBodyData(TeaModel):
    def __init__(
        self,
        type: str = None,
        destination: str = None,
        origin: str = None,
        route: str = None,
    ):
        self.type = type
        self.destination = destination
        self.origin = origin
        self.route = route

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.destination is not None:
            result['Destination'] = self.destination
        if self.origin is not None:
            result['Origin'] = self.origin
        if self.route is not None:
            result['Route'] = self.route
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Destination') is not None:
            self.destination = m.get('Destination')
        if m.get('Origin') is not None:
            self.origin = m.get('Origin')
        if m.get('Route') is not None:
            self.route = m.get('Route')
        return self


class ListMapRouteDetailsResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        message: str = None,
        page_size: int = None,
        page_number: int = None,
        data: List[ListMapRouteDetailsResponseBodyData] = None,
        code: str = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.message = message
        self.page_size = page_size
        self.page_number = page_number
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListMapRouteDetailsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class ListMapRouteDetailsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListMapRouteDetailsResponseBody = None,
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
            temp_model = ListMapRouteDetailsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListMetricsRequest(TeaModel):
    def __init__(
        self,
        corp_id: Dict[str, Any] = None,
        tag_code: Dict[str, Any] = None,
        aggregate_type: str = None,
        start_time: str = None,
        end_time: str = None,
        page_number: str = None,
        page_size: str = None,
    ):
        self.corp_id = corp_id
        self.tag_code = tag_code
        self.aggregate_type = aggregate_type
        self.start_time = start_time
        self.end_time = end_time
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.tag_code is not None:
            result['TagCode'] = self.tag_code
        if self.aggregate_type is not None:
            result['AggregateType'] = self.aggregate_type
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('TagCode') is not None:
            self.tag_code = m.get('TagCode')
        if m.get('AggregateType') is not None:
            self.aggregate_type = m.get('AggregateType')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListMetricsShrinkRequest(TeaModel):
    def __init__(
        self,
        corp_id_shrink: str = None,
        tag_code_shrink: str = None,
        aggregate_type: str = None,
        start_time: str = None,
        end_time: str = None,
        page_number: str = None,
        page_size: str = None,
    ):
        self.corp_id_shrink = corp_id_shrink
        self.tag_code_shrink = tag_code_shrink
        self.aggregate_type = aggregate_type
        self.start_time = start_time
        self.end_time = end_time
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id_shrink is not None:
            result['CorpId'] = self.corp_id_shrink
        if self.tag_code_shrink is not None:
            result['TagCode'] = self.tag_code_shrink
        if self.aggregate_type is not None:
            result['AggregateType'] = self.aggregate_type
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorpId') is not None:
            self.corp_id_shrink = m.get('CorpId')
        if m.get('TagCode') is not None:
            self.tag_code_shrink = m.get('TagCode')
        if m.get('AggregateType') is not None:
            self.aggregate_type = m.get('AggregateType')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListMetricsResponseBodyData(TeaModel):
    def __init__(
        self,
        tag_metric: str = None,
        tag_code: str = None,
        corp_id: str = None,
        tag_value: str = None,
        date_time: str = None,
    ):
        self.tag_metric = tag_metric
        self.tag_code = tag_code
        self.corp_id = corp_id
        self.tag_value = tag_value
        self.date_time = date_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_metric is not None:
            result['TagMetric'] = self.tag_metric
        if self.tag_code is not None:
            result['TagCode'] = self.tag_code
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        if self.date_time is not None:
            result['DateTime'] = self.date_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagMetric') is not None:
            self.tag_metric = m.get('TagMetric')
        if m.get('TagCode') is not None:
            self.tag_code = m.get('TagCode')
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        if m.get('DateTime') is not None:
            self.date_time = m.get('DateTime')
        return self


class ListMetricsResponseBody(TeaModel):
    def __init__(
        self,
        total_count: str = None,
        request_id: str = None,
        message: str = None,
        page_size: str = None,
        page_number: str = None,
        data: List[ListMetricsResponseBodyData] = None,
        code: str = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.message = message
        self.page_size = page_size
        self.page_number = page_number
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListMetricsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class ListMetricsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListMetricsResponseBody = None,
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
            temp_model = ListMetricsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPersonDetailsRequest(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        person_id: str = None,
        start_time: str = None,
        end_time: str = None,
        page_number: int = None,
        page_size: int = None,
        schema: str = None,
    ):
        self.corp_id = corp_id
        self.person_id = person_id
        self.start_time = start_time
        self.end_time = end_time
        self.page_number = page_number
        self.page_size = page_size
        self.schema = schema

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.person_id is not None:
            result['PersonId'] = self.person_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.schema is not None:
            result['Schema'] = self.schema
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('PersonId') is not None:
            self.person_id = m.get('PersonId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Schema') is not None:
            self.schema = m.get('Schema')
        return self


class ListPersonDetailsResponseBodyData(TeaModel):
    def __init__(
        self,
        update_time: str = None,
        gender: str = None,
        body_target_image: str = None,
        preferred_color: str = None,
        hot_spot_address: str = None,
        age: str = None,
        person_type: str = None,
        transportation: str = None,
        profession: str = None,
        address: str = None,
        face_source_image: str = None,
        face_target_image: str = None,
        pref_out_time: str = None,
        body_source_image: str = None,
        person_id: str = None,
    ):
        self.update_time = update_time
        self.gender = gender
        self.body_target_image = body_target_image
        self.preferred_color = preferred_color
        self.hot_spot_address = hot_spot_address
        self.age = age
        self.person_type = person_type
        self.transportation = transportation
        self.profession = profession
        self.address = address
        self.face_source_image = face_source_image
        self.face_target_image = face_target_image
        self.pref_out_time = pref_out_time
        self.body_source_image = body_source_image
        self.person_id = person_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.gender is not None:
            result['Gender'] = self.gender
        if self.body_target_image is not None:
            result['BodyTargetImage'] = self.body_target_image
        if self.preferred_color is not None:
            result['PreferredColor'] = self.preferred_color
        if self.hot_spot_address is not None:
            result['HotSpotAddress'] = self.hot_spot_address
        if self.age is not None:
            result['Age'] = self.age
        if self.person_type is not None:
            result['PersonType'] = self.person_type
        if self.transportation is not None:
            result['Transportation'] = self.transportation
        if self.profession is not None:
            result['Profession'] = self.profession
        if self.address is not None:
            result['Address'] = self.address
        if self.face_source_image is not None:
            result['FaceSourceImage'] = self.face_source_image
        if self.face_target_image is not None:
            result['FaceTargetImage'] = self.face_target_image
        if self.pref_out_time is not None:
            result['PrefOutTime'] = self.pref_out_time
        if self.body_source_image is not None:
            result['BodySourceImage'] = self.body_source_image
        if self.person_id is not None:
            result['PersonId'] = self.person_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('Gender') is not None:
            self.gender = m.get('Gender')
        if m.get('BodyTargetImage') is not None:
            self.body_target_image = m.get('BodyTargetImage')
        if m.get('PreferredColor') is not None:
            self.preferred_color = m.get('PreferredColor')
        if m.get('HotSpotAddress') is not None:
            self.hot_spot_address = m.get('HotSpotAddress')
        if m.get('Age') is not None:
            self.age = m.get('Age')
        if m.get('PersonType') is not None:
            self.person_type = m.get('PersonType')
        if m.get('Transportation') is not None:
            self.transportation = m.get('Transportation')
        if m.get('Profession') is not None:
            self.profession = m.get('Profession')
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('FaceSourceImage') is not None:
            self.face_source_image = m.get('FaceSourceImage')
        if m.get('FaceTargetImage') is not None:
            self.face_target_image = m.get('FaceTargetImage')
        if m.get('PrefOutTime') is not None:
            self.pref_out_time = m.get('PrefOutTime')
        if m.get('BodySourceImage') is not None:
            self.body_source_image = m.get('BodySourceImage')
        if m.get('PersonId') is not None:
            self.person_id = m.get('PersonId')
        return self


class ListPersonDetailsResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        message: str = None,
        page_size: int = None,
        page_number: int = None,
        data: List[ListPersonDetailsResponseBodyData] = None,
        code: str = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.message = message
        self.page_size = page_size
        self.page_number = page_number
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListPersonDetailsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class ListPersonDetailsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListPersonDetailsResponseBody = None,
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
            temp_model = ListPersonDetailsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPersonResultRequest(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        age: str = None,
        gender: str = None,
        profession: str = None,
        start_time: str = None,
        end_time: str = None,
        page_number: int = None,
        page_size: int = None,
        quality_score: str = None,
    ):
        self.corp_id = corp_id
        self.age = age
        self.gender = gender
        self.profession = profession
        self.start_time = start_time
        self.end_time = end_time
        self.page_number = page_number
        self.page_size = page_size
        self.quality_score = quality_score

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.age is not None:
            result['Age'] = self.age
        if self.gender is not None:
            result['Gender'] = self.gender
        if self.profession is not None:
            result['Profession'] = self.profession
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.quality_score is not None:
            result['QualityScore'] = self.quality_score
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('Age') is not None:
            self.age = m.get('Age')
        if m.get('Gender') is not None:
            self.gender = m.get('Gender')
        if m.get('Profession') is not None:
            self.profession = m.get('Profession')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('QualityScore') is not None:
            self.quality_score = m.get('QualityScore')
        return self


class ListPersonResultResponseBodyData(TeaModel):
    def __init__(
        self,
        source_url: str = None,
        profession: str = None,
        update_time: str = None,
        gender: str = None,
        target_url: str = None,
        address: str = None,
        hot_spot_address: str = None,
        age: str = None,
        person_id: str = None,
        person_type: str = None,
        transportation: str = None,
    ):
        self.source_url = source_url
        self.profession = profession
        self.update_time = update_time
        self.gender = gender
        self.target_url = target_url
        self.address = address
        self.hot_spot_address = hot_spot_address
        self.age = age
        self.person_id = person_id
        self.person_type = person_type
        self.transportation = transportation

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_url is not None:
            result['SourceUrl'] = self.source_url
        if self.profession is not None:
            result['Profession'] = self.profession
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.gender is not None:
            result['Gender'] = self.gender
        if self.target_url is not None:
            result['TargetUrl'] = self.target_url
        if self.address is not None:
            result['Address'] = self.address
        if self.hot_spot_address is not None:
            result['HotSpotAddress'] = self.hot_spot_address
        if self.age is not None:
            result['Age'] = self.age
        if self.person_id is not None:
            result['PersonId'] = self.person_id
        if self.person_type is not None:
            result['PersonType'] = self.person_type
        if self.transportation is not None:
            result['Transportation'] = self.transportation
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceUrl') is not None:
            self.source_url = m.get('SourceUrl')
        if m.get('Profession') is not None:
            self.profession = m.get('Profession')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('Gender') is not None:
            self.gender = m.get('Gender')
        if m.get('TargetUrl') is not None:
            self.target_url = m.get('TargetUrl')
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('HotSpotAddress') is not None:
            self.hot_spot_address = m.get('HotSpotAddress')
        if m.get('Age') is not None:
            self.age = m.get('Age')
        if m.get('PersonId') is not None:
            self.person_id = m.get('PersonId')
        if m.get('PersonType') is not None:
            self.person_type = m.get('PersonType')
        if m.get('Transportation') is not None:
            self.transportation = m.get('Transportation')
        return self


class ListPersonResultResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        message: str = None,
        page_size: int = None,
        page_number: int = None,
        data: List[ListPersonResultResponseBodyData] = None,
        code: str = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.message = message
        self.page_size = page_size
        self.page_number = page_number
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListPersonResultResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class ListPersonResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListPersonResultResponseBody = None,
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
            temp_model = ListPersonResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPersonTagRequest(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        tag_code: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.corp_id = corp_id
        self.tag_code = tag_code
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.tag_code is not None:
            result['TagCode'] = self.tag_code
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('TagCode') is not None:
            self.tag_code = m.get('TagCode')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListPersonTagResponseBodyData(TeaModel):
    def __init__(
        self,
        value: str = None,
        corp_id: str = None,
        tag_value: str = None,
    ):
        self.value = value
        self.corp_id = corp_id
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.value is not None:
            result['Value'] = self.value
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        return self


class ListPersonTagResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        message: str = None,
        page_size: int = None,
        page_number: int = None,
        data: List[ListPersonTagResponseBodyData] = None,
        code: str = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.message = message
        self.page_size = page_size
        self.page_number = page_number
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListPersonTagResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class ListPersonTagResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListPersonTagResponseBody = None,
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
            temp_model = ListPersonTagResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPersonTopRequest(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        person_id: str = None,
        start_time: str = None,
        end_time: str = None,
    ):
        self.corp_id = corp_id
        self.person_id = person_id
        self.start_time = start_time
        self.end_time = end_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.person_id is not None:
            result['PersonId'] = self.person_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('PersonId') is not None:
            self.person_id = m.get('PersonId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        return self


class ListPersonTopResponseBodyData(TeaModel):
    def __init__(
        self,
        frequency: str = None,
        poi_id: str = None,
        corp_id: str = None,
        pass_hour: str = None,
        poi_name: str = None,
        person_id: str = None,
    ):
        self.frequency = frequency
        self.poi_id = poi_id
        self.corp_id = corp_id
        self.pass_hour = pass_hour
        self.poi_name = poi_name
        self.person_id = person_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.frequency is not None:
            result['Frequency'] = self.frequency
        if self.poi_id is not None:
            result['PoiId'] = self.poi_id
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.pass_hour is not None:
            result['PassHour'] = self.pass_hour
        if self.poi_name is not None:
            result['PoiName'] = self.poi_name
        if self.person_id is not None:
            result['PersonId'] = self.person_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Frequency') is not None:
            self.frequency = m.get('Frequency')
        if m.get('PoiId') is not None:
            self.poi_id = m.get('PoiId')
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('PassHour') is not None:
            self.pass_hour = m.get('PassHour')
        if m.get('PoiName') is not None:
            self.poi_name = m.get('PoiName')
        if m.get('PersonId') is not None:
            self.person_id = m.get('PersonId')
        return self


class ListPersonTopResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        message: str = None,
        page_size: int = None,
        page_number: int = None,
        data: List[ListPersonTopResponseBodyData] = None,
        code: str = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.message = message
        self.page_size = page_size
        self.page_number = page_number
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListPersonTopResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class ListPersonTopResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListPersonTopResponseBody = None,
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
            temp_model = ListPersonTopResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPersonTraceRequest(TeaModel):
    def __init__(
        self,
        start_time: str = None,
        corp_id: Dict[str, Any] = None,
        page_number: str = None,
        page_size: str = None,
        end_time: str = None,
        data_source_id: Dict[str, Any] = None,
        person_id: Dict[str, Any] = None,
    ):
        self.start_time = start_time
        self.corp_id = corp_id
        self.page_number = page_number
        self.page_size = page_size
        self.end_time = end_time
        self.data_source_id = data_source_id
        self.person_id = person_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id
        if self.person_id is not None:
            result['PersonId'] = self.person_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')
        if m.get('PersonId') is not None:
            self.person_id = m.get('PersonId')
        return self


class ListPersonTraceShrinkRequest(TeaModel):
    def __init__(
        self,
        start_time: str = None,
        corp_id_shrink: str = None,
        page_number: str = None,
        page_size: str = None,
        end_time: str = None,
        data_source_id_shrink: str = None,
        person_id_shrink: str = None,
    ):
        self.start_time = start_time
        self.corp_id_shrink = corp_id_shrink
        self.page_number = page_number
        self.page_size = page_size
        self.end_time = end_time
        self.data_source_id_shrink = data_source_id_shrink
        self.person_id_shrink = person_id_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.corp_id_shrink is not None:
            result['CorpId'] = self.corp_id_shrink
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.data_source_id_shrink is not None:
            result['DataSourceId'] = self.data_source_id_shrink
        if self.person_id_shrink is not None:
            result['PersonId'] = self.person_id_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('CorpId') is not None:
            self.corp_id_shrink = m.get('CorpId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('DataSourceId') is not None:
            self.data_source_id_shrink = m.get('DataSourceId')
        if m.get('PersonId') is not None:
            self.person_id_shrink = m.get('PersonId')
        return self


class ListPersonTraceResponseBodyData(TeaModel):
    def __init__(
        self,
        end_target_image: str = None,
        last_time: str = None,
        start_time: str = None,
        group_id: str = None,
        device_id: str = None,
        end_source_image: str = None,
        corp_id: str = None,
        start_source_image: str = None,
        date: str = None,
        person_id: str = None,
        start_target_image: str = None,
    ):
        self.end_target_image = end_target_image
        self.last_time = last_time
        self.start_time = start_time
        self.group_id = group_id
        self.device_id = device_id
        self.end_source_image = end_source_image
        self.corp_id = corp_id
        self.start_source_image = start_source_image
        self.date = date
        self.person_id = person_id
        self.start_target_image = start_target_image

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_target_image is not None:
            result['EndTargetImage'] = self.end_target_image
        if self.last_time is not None:
            result['LastTime'] = self.last_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.end_source_image is not None:
            result['EndSourceImage'] = self.end_source_image
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.start_source_image is not None:
            result['StartSourceImage'] = self.start_source_image
        if self.date is not None:
            result['Date'] = self.date
        if self.person_id is not None:
            result['PersonId'] = self.person_id
        if self.start_target_image is not None:
            result['StartTargetImage'] = self.start_target_image
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTargetImage') is not None:
            self.end_target_image = m.get('EndTargetImage')
        if m.get('LastTime') is not None:
            self.last_time = m.get('LastTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('EndSourceImage') is not None:
            self.end_source_image = m.get('EndSourceImage')
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('StartSourceImage') is not None:
            self.start_source_image = m.get('StartSourceImage')
        if m.get('Date') is not None:
            self.date = m.get('Date')
        if m.get('PersonId') is not None:
            self.person_id = m.get('PersonId')
        if m.get('StartTargetImage') is not None:
            self.start_target_image = m.get('StartTargetImage')
        return self


class ListPersonTraceResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        message: str = None,
        page_size: int = None,
        page_number: int = None,
        data: List[ListPersonTraceResponseBodyData] = None,
        code: str = None,
        success: str = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.message = message
        self.page_size = page_size
        self.page_number = page_number
        self.data = data
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListPersonTraceResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListPersonTraceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListPersonTraceResponseBody = None,
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
            temp_model = ListPersonTraceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPersonTrackRequest(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        person_id: str = None,
        start_time: str = None,
        end_time: str = None,
        page_number: int = None,
        page_size: int = None,
        image_source_type: str = None,
        aggregate_dimension: str = None,
        quality_score: str = None,
    ):
        self.corp_id = corp_id
        self.person_id = person_id
        self.start_time = start_time
        self.end_time = end_time
        self.page_number = page_number
        self.page_size = page_size
        self.image_source_type = image_source_type
        self.aggregate_dimension = aggregate_dimension
        self.quality_score = quality_score

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.person_id is not None:
            result['PersonId'] = self.person_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.image_source_type is not None:
            result['ImageSourceType'] = self.image_source_type
        if self.aggregate_dimension is not None:
            result['AggregateDimension'] = self.aggregate_dimension
        if self.quality_score is not None:
            result['QualityScore'] = self.quality_score
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('PersonId') is not None:
            self.person_id = m.get('PersonId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ImageSourceType') is not None:
            self.image_source_type = m.get('ImageSourceType')
        if m.get('AggregateDimension') is not None:
            self.aggregate_dimension = m.get('AggregateDimension')
        if m.get('QualityScore') is not None:
            self.quality_score = m.get('QualityScore')
        return self


class ListPersonTrackResponseBodyData(TeaModel):
    def __init__(
        self,
        source_url: str = None,
        right_bottom_y: str = None,
        data_source_name: str = None,
        pic_url_path: str = None,
        data_source_id: str = None,
        right_bottom_x: str = None,
        target_pic_url_path: str = None,
        left_top_y: str = None,
        target_url: str = None,
        corp_id: str = None,
        longitude: str = None,
        latitude: str = None,
        shot_time: str = None,
        person_id: str = None,
        left_top_x: str = None,
    ):
        self.source_url = source_url
        self.right_bottom_y = right_bottom_y
        self.data_source_name = data_source_name
        self.pic_url_path = pic_url_path
        self.data_source_id = data_source_id
        self.right_bottom_x = right_bottom_x
        self.target_pic_url_path = target_pic_url_path
        self.left_top_y = left_top_y
        self.target_url = target_url
        self.corp_id = corp_id
        self.longitude = longitude
        self.latitude = latitude
        self.shot_time = shot_time
        self.person_id = person_id
        self.left_top_x = left_top_x

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_url is not None:
            result['SourceUrl'] = self.source_url
        if self.right_bottom_y is not None:
            result['RightBottomY'] = self.right_bottom_y
        if self.data_source_name is not None:
            result['DataSourceName'] = self.data_source_name
        if self.pic_url_path is not None:
            result['PicUrlPath'] = self.pic_url_path
        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id
        if self.right_bottom_x is not None:
            result['RightBottomX'] = self.right_bottom_x
        if self.target_pic_url_path is not None:
            result['TargetPicUrlPath'] = self.target_pic_url_path
        if self.left_top_y is not None:
            result['LeftTopY'] = self.left_top_y
        if self.target_url is not None:
            result['TargetUrl'] = self.target_url
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.longitude is not None:
            result['Longitude'] = self.longitude
        if self.latitude is not None:
            result['Latitude'] = self.latitude
        if self.shot_time is not None:
            result['ShotTime'] = self.shot_time
        if self.person_id is not None:
            result['PersonId'] = self.person_id
        if self.left_top_x is not None:
            result['LeftTopX'] = self.left_top_x
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceUrl') is not None:
            self.source_url = m.get('SourceUrl')
        if m.get('RightBottomY') is not None:
            self.right_bottom_y = m.get('RightBottomY')
        if m.get('DataSourceName') is not None:
            self.data_source_name = m.get('DataSourceName')
        if m.get('PicUrlPath') is not None:
            self.pic_url_path = m.get('PicUrlPath')
        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')
        if m.get('RightBottomX') is not None:
            self.right_bottom_x = m.get('RightBottomX')
        if m.get('TargetPicUrlPath') is not None:
            self.target_pic_url_path = m.get('TargetPicUrlPath')
        if m.get('LeftTopY') is not None:
            self.left_top_y = m.get('LeftTopY')
        if m.get('TargetUrl') is not None:
            self.target_url = m.get('TargetUrl')
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('Longitude') is not None:
            self.longitude = m.get('Longitude')
        if m.get('Latitude') is not None:
            self.latitude = m.get('Latitude')
        if m.get('ShotTime') is not None:
            self.shot_time = m.get('ShotTime')
        if m.get('PersonId') is not None:
            self.person_id = m.get('PersonId')
        if m.get('LeftTopX') is not None:
            self.left_top_x = m.get('LeftTopX')
        return self


class ListPersonTrackResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        message: str = None,
        page_size: int = None,
        page_number: int = None,
        data: List[ListPersonTrackResponseBodyData] = None,
        code: str = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.message = message
        self.page_size = page_size
        self.page_number = page_number
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListPersonTrackResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class ListPersonTrackResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListPersonTrackResponseBody = None,
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
            temp_model = ListPersonTrackResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRangeDeviceRequest(TeaModel):
    def __init__(
        self,
        radius: int = None,
        data_source_id: str = None,
        page_number: int = None,
        page_size: int = None,
        corp_id: str = None,
    ):
        self.radius = radius
        self.data_source_id = data_source_id
        self.page_number = page_number
        self.page_size = page_size
        self.corp_id = corp_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.radius is not None:
            result['Radius'] = self.radius
        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Radius') is not None:
            self.radius = m.get('Radius')
        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        return self


class ListRangeDeviceResponseBodyData(TeaModel):
    def __init__(
        self,
        data_source_id_poi: str = None,
        distance: str = None,
        data_source_id: str = None,
        corp_id: str = None,
        longitude: str = None,
        data_source_id_name: str = None,
        latitude: str = None,
        near_poi: str = None,
    ):
        self.data_source_id_poi = data_source_id_poi
        self.distance = distance
        self.data_source_id = data_source_id
        self.corp_id = corp_id
        self.longitude = longitude
        self.data_source_id_name = data_source_id_name
        self.latitude = latitude
        self.near_poi = near_poi

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_source_id_poi is not None:
            result['DataSourceIdPoi'] = self.data_source_id_poi
        if self.distance is not None:
            result['Distance'] = self.distance
        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.longitude is not None:
            result['Longitude'] = self.longitude
        if self.data_source_id_name is not None:
            result['DataSourceIdName'] = self.data_source_id_name
        if self.latitude is not None:
            result['Latitude'] = self.latitude
        if self.near_poi is not None:
            result['NearPoi'] = self.near_poi
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSourceIdPoi') is not None:
            self.data_source_id_poi = m.get('DataSourceIdPoi')
        if m.get('Distance') is not None:
            self.distance = m.get('Distance')
        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('Longitude') is not None:
            self.longitude = m.get('Longitude')
        if m.get('DataSourceIdName') is not None:
            self.data_source_id_name = m.get('DataSourceIdName')
        if m.get('Latitude') is not None:
            self.latitude = m.get('Latitude')
        if m.get('NearPoi') is not None:
            self.near_poi = m.get('NearPoi')
        return self


class ListRangeDeviceResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        message: str = None,
        page_size: int = None,
        page_number: int = None,
        data: List[ListRangeDeviceResponseBodyData] = None,
        code: str = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.message = message
        self.page_size = page_size
        self.page_number = page_number
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListRangeDeviceResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class ListRangeDeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListRangeDeviceResponseBody = None,
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
            temp_model = ListRangeDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListStorageStatisticsRequest(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
    ):
        self.corp_id = corp_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        return self


class ListStorageStatisticsResponseBodyData(TeaModel):
    def __init__(
        self,
        used_store: str = None,
        unused_store: str = None,
        corp_id: str = None,
        number: str = None,
        total_store: str = None,
    ):
        self.used_store = used_store
        self.unused_store = unused_store
        self.corp_id = corp_id
        self.number = number
        self.total_store = total_store

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.used_store is not None:
            result['UsedStore'] = self.used_store
        if self.unused_store is not None:
            result['UnusedStore'] = self.unused_store
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.number is not None:
            result['Number'] = self.number
        if self.total_store is not None:
            result['TotalStore'] = self.total_store
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UsedStore') is not None:
            self.used_store = m.get('UsedStore')
        if m.get('UnusedStore') is not None:
            self.unused_store = m.get('UnusedStore')
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('Number') is not None:
            self.number = m.get('Number')
        if m.get('TotalStore') is not None:
            self.total_store = m.get('TotalStore')
        return self


class ListStorageStatisticsResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        message: str = None,
        request_id: str = None,
        data: List[ListStorageStatisticsResponseBodyData] = None,
        code: str = None,
    ):
        self.total_count = total_count
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListStorageStatisticsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class ListStorageStatisticsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListStorageStatisticsResponseBody = None,
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
            temp_model = ListStorageStatisticsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListStructureStatisticsRequest(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        back_category: str = None,
    ):
        self.corp_id = corp_id
        self.back_category = back_category

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.back_category is not None:
            result['BackCategory'] = self.back_category
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('BackCategory') is not None:
            self.back_category = m.get('BackCategory')
        return self


class ListStructureStatisticsResponseBodyData(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        number: str = None,
    ):
        self.corp_id = corp_id
        self.number = number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.number is not None:
            result['Number'] = self.number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('Number') is not None:
            self.number = m.get('Number')
        return self


class ListStructureStatisticsResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        message: str = None,
        page_size: int = None,
        page_number: int = None,
        data: List[ListStructureStatisticsResponseBodyData] = None,
        code: str = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.message = message
        self.page_size = page_size
        self.page_number = page_number
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListStructureStatisticsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class ListStructureStatisticsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListStructureStatisticsResponseBody = None,
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
            temp_model = ListStructureStatisticsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagMetricsRequest(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        tag_code: Dict[str, Any] = None,
        aggregate_type: str = None,
        start_time: str = None,
        end_time: str = None,
        page_number: str = None,
        page_size: str = None,
    ):
        self.corp_id = corp_id
        self.tag_code = tag_code
        self.aggregate_type = aggregate_type
        self.start_time = start_time
        self.end_time = end_time
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.tag_code is not None:
            result['TagCode'] = self.tag_code
        if self.aggregate_type is not None:
            result['AggregateType'] = self.aggregate_type
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('TagCode') is not None:
            self.tag_code = m.get('TagCode')
        if m.get('AggregateType') is not None:
            self.aggregate_type = m.get('AggregateType')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListTagMetricsShrinkRequest(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        tag_code_shrink: str = None,
        aggregate_type: str = None,
        start_time: str = None,
        end_time: str = None,
        page_number: str = None,
        page_size: str = None,
    ):
        self.corp_id = corp_id
        self.tag_code_shrink = tag_code_shrink
        self.aggregate_type = aggregate_type
        self.start_time = start_time
        self.end_time = end_time
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.tag_code_shrink is not None:
            result['TagCode'] = self.tag_code_shrink
        if self.aggregate_type is not None:
            result['AggregateType'] = self.aggregate_type
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('TagCode') is not None:
            self.tag_code_shrink = m.get('TagCode')
        if m.get('AggregateType') is not None:
            self.aggregate_type = m.get('AggregateType')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListTagMetricsResponseBodyData(TeaModel):
    def __init__(
        self,
        tag_metric: str = None,
        tag_code: str = None,
        corp_id: str = None,
        tag_value: str = None,
        date_time: str = None,
    ):
        self.tag_metric = tag_metric
        self.tag_code = tag_code
        self.corp_id = corp_id
        self.tag_value = tag_value
        self.date_time = date_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_metric is not None:
            result['TagMetric'] = self.tag_metric
        if self.tag_code is not None:
            result['TagCode'] = self.tag_code
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        if self.date_time is not None:
            result['DateTime'] = self.date_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagMetric') is not None:
            self.tag_metric = m.get('TagMetric')
        if m.get('TagCode') is not None:
            self.tag_code = m.get('TagCode')
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        if m.get('DateTime') is not None:
            self.date_time = m.get('DateTime')
        return self


class ListTagMetricsResponseBody(TeaModel):
    def __init__(
        self,
        total_count: str = None,
        request_id: str = None,
        message: str = None,
        page_size: str = None,
        page_number: str = None,
        data: List[ListTagMetricsResponseBodyData] = None,
        code: str = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.message = message
        self.page_size = page_size
        self.page_number = page_number
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListTagMetricsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class ListTagMetricsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListTagMetricsResponseBody = None,
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
            temp_model = ListTagMetricsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListVehicleDetailsRequest(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        plate_id: str = None,
        start_time: str = None,
        end_time: str = None,
        page_number: str = None,
        page_size: str = None,
    ):
        self.corp_id = corp_id
        self.plate_id = plate_id
        self.start_time = start_time
        self.end_time = end_time
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.plate_id is not None:
            result['PlateId'] = self.plate_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('PlateId') is not None:
            self.plate_id = m.get('PlateId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListVehicleDetailsResponseBodyData(TeaModel):
    def __init__(
        self,
        vehicle_application: str = None,
        source_url: str = None,
        gender: str = None,
        vehicle_color: str = None,
        vehicle_id: str = None,
        source_image_storage_path: str = None,
        person_type: str = None,
        popular_poi: str = None,
        popular_address: str = None,
        plate_id: str = None,
        target_url: str = None,
        vehicle_class: str = None,
        pref_out_time: str = None,
        person_id: str = None,
        target_image_storage_path: str = None,
    ):
        self.vehicle_application = vehicle_application
        self.source_url = source_url
        self.gender = gender
        self.vehicle_color = vehicle_color
        self.vehicle_id = vehicle_id
        self.source_image_storage_path = source_image_storage_path
        self.person_type = person_type
        self.popular_poi = popular_poi
        self.popular_address = popular_address
        self.plate_id = plate_id
        self.target_url = target_url
        self.vehicle_class = vehicle_class
        self.pref_out_time = pref_out_time
        self.person_id = person_id
        self.target_image_storage_path = target_image_storage_path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.vehicle_application is not None:
            result['VehicleApplication'] = self.vehicle_application
        if self.source_url is not None:
            result['SourceUrl'] = self.source_url
        if self.gender is not None:
            result['Gender'] = self.gender
        if self.vehicle_color is not None:
            result['VehicleColor'] = self.vehicle_color
        if self.vehicle_id is not None:
            result['VehicleId'] = self.vehicle_id
        if self.source_image_storage_path is not None:
            result['SourceImageStoragePath'] = self.source_image_storage_path
        if self.person_type is not None:
            result['PersonType'] = self.person_type
        if self.popular_poi is not None:
            result['PopularPoi'] = self.popular_poi
        if self.popular_address is not None:
            result['PopularAddress'] = self.popular_address
        if self.plate_id is not None:
            result['PlateId'] = self.plate_id
        if self.target_url is not None:
            result['TargetUrl'] = self.target_url
        if self.vehicle_class is not None:
            result['VehicleClass'] = self.vehicle_class
        if self.pref_out_time is not None:
            result['PrefOutTime'] = self.pref_out_time
        if self.person_id is not None:
            result['PersonId'] = self.person_id
        if self.target_image_storage_path is not None:
            result['TargetImageStoragePath'] = self.target_image_storage_path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VehicleApplication') is not None:
            self.vehicle_application = m.get('VehicleApplication')
        if m.get('SourceUrl') is not None:
            self.source_url = m.get('SourceUrl')
        if m.get('Gender') is not None:
            self.gender = m.get('Gender')
        if m.get('VehicleColor') is not None:
            self.vehicle_color = m.get('VehicleColor')
        if m.get('VehicleId') is not None:
            self.vehicle_id = m.get('VehicleId')
        if m.get('SourceImageStoragePath') is not None:
            self.source_image_storage_path = m.get('SourceImageStoragePath')
        if m.get('PersonType') is not None:
            self.person_type = m.get('PersonType')
        if m.get('PopularPoi') is not None:
            self.popular_poi = m.get('PopularPoi')
        if m.get('PopularAddress') is not None:
            self.popular_address = m.get('PopularAddress')
        if m.get('PlateId') is not None:
            self.plate_id = m.get('PlateId')
        if m.get('TargetUrl') is not None:
            self.target_url = m.get('TargetUrl')
        if m.get('VehicleClass') is not None:
            self.vehicle_class = m.get('VehicleClass')
        if m.get('PrefOutTime') is not None:
            self.pref_out_time = m.get('PrefOutTime')
        if m.get('PersonId') is not None:
            self.person_id = m.get('PersonId')
        if m.get('TargetImageStoragePath') is not None:
            self.target_image_storage_path = m.get('TargetImageStoragePath')
        return self


class ListVehicleDetailsResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        message: str = None,
        page_size: int = None,
        page_number: int = None,
        data: List[ListVehicleDetailsResponseBodyData] = None,
        code: str = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.message = message
        self.page_size = page_size
        self.page_number = page_number
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListVehicleDetailsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class ListVehicleDetailsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListVehicleDetailsResponseBody = None,
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
            temp_model = ListVehicleDetailsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListVehicleResultsRequest(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        vehicle_color: str = None,
        vehicle_class: str = None,
        vehicle_application: str = None,
        start_time: str = None,
        end_time: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.corp_id = corp_id
        self.vehicle_color = vehicle_color
        self.vehicle_class = vehicle_class
        self.vehicle_application = vehicle_application
        self.start_time = start_time
        self.end_time = end_time
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.vehicle_color is not None:
            result['VehicleColor'] = self.vehicle_color
        if self.vehicle_class is not None:
            result['VehicleClass'] = self.vehicle_class
        if self.vehicle_application is not None:
            result['VehicleApplication'] = self.vehicle_application
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('VehicleColor') is not None:
            self.vehicle_color = m.get('VehicleColor')
        if m.get('VehicleClass') is not None:
            self.vehicle_class = m.get('VehicleClass')
        if m.get('VehicleApplication') is not None:
            self.vehicle_application = m.get('VehicleApplication')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListVehicleResultsResponseBodyData(TeaModel):
    def __init__(
        self,
        vehicle_application: str = None,
        profession: str = None,
        update_time: str = None,
        gender: str = None,
        plate_id: str = None,
        vehicle_class: str = None,
        live_address: str = None,
        vehicle_id: str = None,
        person_id: str = None,
    ):
        self.vehicle_application = vehicle_application
        self.profession = profession
        self.update_time = update_time
        self.gender = gender
        self.plate_id = plate_id
        self.vehicle_class = vehicle_class
        self.live_address = live_address
        self.vehicle_id = vehicle_id
        self.person_id = person_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.vehicle_application is not None:
            result['VehicleApplication'] = self.vehicle_application
        if self.profession is not None:
            result['Profession'] = self.profession
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.gender is not None:
            result['Gender'] = self.gender
        if self.plate_id is not None:
            result['PlateId'] = self.plate_id
        if self.vehicle_class is not None:
            result['VehicleClass'] = self.vehicle_class
        if self.live_address is not None:
            result['LiveAddress'] = self.live_address
        if self.vehicle_id is not None:
            result['VehicleId'] = self.vehicle_id
        if self.person_id is not None:
            result['PersonId'] = self.person_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VehicleApplication') is not None:
            self.vehicle_application = m.get('VehicleApplication')
        if m.get('Profession') is not None:
            self.profession = m.get('Profession')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('Gender') is not None:
            self.gender = m.get('Gender')
        if m.get('PlateId') is not None:
            self.plate_id = m.get('PlateId')
        if m.get('VehicleClass') is not None:
            self.vehicle_class = m.get('VehicleClass')
        if m.get('LiveAddress') is not None:
            self.live_address = m.get('LiveAddress')
        if m.get('VehicleId') is not None:
            self.vehicle_id = m.get('VehicleId')
        if m.get('PersonId') is not None:
            self.person_id = m.get('PersonId')
        return self


class ListVehicleResultsResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        message: str = None,
        page_size: int = None,
        page_number: int = None,
        data: List[ListVehicleResultsResponseBodyData] = None,
        code: str = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.message = message
        self.page_size = page_size
        self.page_number = page_number
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListVehicleResultsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class ListVehicleResultsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListVehicleResultsResponseBody = None,
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
            temp_model = ListVehicleResultsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListVehicleTagDistributeRequest(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        tag_code: str = None,
        start_time: str = None,
        end_time: str = None,
    ):
        self.corp_id = corp_id
        self.tag_code = tag_code
        self.start_time = start_time
        self.end_time = end_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.tag_code is not None:
            result['TagCode'] = self.tag_code
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('TagCode') is not None:
            self.tag_code = m.get('TagCode')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        return self


class ListVehicleTagDistributeResponseBodyData(TeaModel):
    def __init__(
        self,
        value: str = None,
        corp_id: str = None,
        tag_value: str = None,
    ):
        self.value = value
        self.corp_id = corp_id
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.value is not None:
            result['Value'] = self.value
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        return self


class ListVehicleTagDistributeResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        message: str = None,
        page_size: int = None,
        page_number: int = None,
        data: List[ListVehicleTagDistributeResponseBodyData] = None,
        code: str = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.message = message
        self.page_size = page_size
        self.page_number = page_number
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListVehicleTagDistributeResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class ListVehicleTagDistributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListVehicleTagDistributeResponseBody = None,
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
            temp_model = ListVehicleTagDistributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListVehicleTopRequest(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        plate_id: str = None,
        start_time: str = None,
        end_time: str = None,
        page_size: str = None,
        page_num: str = None,
    ):
        self.corp_id = corp_id
        self.plate_id = plate_id
        self.start_time = start_time
        self.end_time = end_time
        self.page_size = page_size
        self.page_num = page_num

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.plate_id is not None:
            result['PlateId'] = self.plate_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('PlateId') is not None:
            self.plate_id = m.get('PlateId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        return self


class ListVehicleTopResponseBodyData(TeaModel):
    def __init__(
        self,
        frequency: str = None,
        poi_id: str = None,
        corp_id: str = None,
        vehicle_id: str = None,
        pass_hour: str = None,
        poi_name: str = None,
    ):
        self.frequency = frequency
        self.poi_id = poi_id
        self.corp_id = corp_id
        self.vehicle_id = vehicle_id
        self.pass_hour = pass_hour
        self.poi_name = poi_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.frequency is not None:
            result['Frequency'] = self.frequency
        if self.poi_id is not None:
            result['PoiId'] = self.poi_id
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.vehicle_id is not None:
            result['VehicleId'] = self.vehicle_id
        if self.pass_hour is not None:
            result['PassHour'] = self.pass_hour
        if self.poi_name is not None:
            result['PoiName'] = self.poi_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Frequency') is not None:
            self.frequency = m.get('Frequency')
        if m.get('PoiId') is not None:
            self.poi_id = m.get('PoiId')
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('VehicleId') is not None:
            self.vehicle_id = m.get('VehicleId')
        if m.get('PassHour') is not None:
            self.pass_hour = m.get('PassHour')
        if m.get('PoiName') is not None:
            self.poi_name = m.get('PoiName')
        return self


class ListVehicleTopResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        message: str = None,
        page_size: int = None,
        page_number: int = None,
        data: List[ListVehicleTopResponseBodyData] = None,
        code: str = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.message = message
        self.page_size = page_size
        self.page_number = page_number
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListVehicleTopResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class ListVehicleTopResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListVehicleTopResponseBody = None,
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
            temp_model = ListVehicleTopResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListVehicleTrackRequest(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        plate_id: str = None,
        start_time: str = None,
        end_time: str = None,
        page_size: int = None,
        page_number: int = None,
    ):
        self.corp_id = corp_id
        self.plate_id = plate_id
        self.start_time = start_time
        self.end_time = end_time
        self.page_size = page_size
        self.page_number = page_number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.plate_id is not None:
            result['PlateId'] = self.plate_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('PlateId') is not None:
            self.plate_id = m.get('PlateId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        return self


class ListVehicleTrackResponseBodyData(TeaModel):
    def __init__(
        self,
        source_url: str = None,
        right_bottom_y: str = None,
        data_source_name: str = None,
        pic_url_path: str = None,
        data_source_id: str = None,
        right_bottom_x: str = None,
        target_pic_url_path: str = None,
        plate_id: str = None,
        left_top_y: str = None,
        target_url: str = None,
        corp_id: str = None,
        longitude: str = None,
        latitude: str = None,
        left_top_x: str = None,
        pass_time: str = None,
    ):
        self.source_url = source_url
        self.right_bottom_y = right_bottom_y
        self.data_source_name = data_source_name
        self.pic_url_path = pic_url_path
        self.data_source_id = data_source_id
        self.right_bottom_x = right_bottom_x
        self.target_pic_url_path = target_pic_url_path
        self.plate_id = plate_id
        self.left_top_y = left_top_y
        self.target_url = target_url
        self.corp_id = corp_id
        self.longitude = longitude
        self.latitude = latitude
        self.left_top_x = left_top_x
        self.pass_time = pass_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_url is not None:
            result['SourceUrl'] = self.source_url
        if self.right_bottom_y is not None:
            result['RightBottomY'] = self.right_bottom_y
        if self.data_source_name is not None:
            result['DataSourceName'] = self.data_source_name
        if self.pic_url_path is not None:
            result['PicUrlPath'] = self.pic_url_path
        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id
        if self.right_bottom_x is not None:
            result['RightBottomX'] = self.right_bottom_x
        if self.target_pic_url_path is not None:
            result['TargetPicUrlPath'] = self.target_pic_url_path
        if self.plate_id is not None:
            result['PlateId'] = self.plate_id
        if self.left_top_y is not None:
            result['LeftTopY'] = self.left_top_y
        if self.target_url is not None:
            result['TargetUrl'] = self.target_url
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.longitude is not None:
            result['Longitude'] = self.longitude
        if self.latitude is not None:
            result['Latitude'] = self.latitude
        if self.left_top_x is not None:
            result['LeftTopX'] = self.left_top_x
        if self.pass_time is not None:
            result['PassTime'] = self.pass_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceUrl') is not None:
            self.source_url = m.get('SourceUrl')
        if m.get('RightBottomY') is not None:
            self.right_bottom_y = m.get('RightBottomY')
        if m.get('DataSourceName') is not None:
            self.data_source_name = m.get('DataSourceName')
        if m.get('PicUrlPath') is not None:
            self.pic_url_path = m.get('PicUrlPath')
        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')
        if m.get('RightBottomX') is not None:
            self.right_bottom_x = m.get('RightBottomX')
        if m.get('TargetPicUrlPath') is not None:
            self.target_pic_url_path = m.get('TargetPicUrlPath')
        if m.get('PlateId') is not None:
            self.plate_id = m.get('PlateId')
        if m.get('LeftTopY') is not None:
            self.left_top_y = m.get('LeftTopY')
        if m.get('TargetUrl') is not None:
            self.target_url = m.get('TargetUrl')
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('Longitude') is not None:
            self.longitude = m.get('Longitude')
        if m.get('Latitude') is not None:
            self.latitude = m.get('Latitude')
        if m.get('LeftTopX') is not None:
            self.left_top_x = m.get('LeftTopX')
        if m.get('PassTime') is not None:
            self.pass_time = m.get('PassTime')
        return self


class ListVehicleTrackResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        message: str = None,
        page_size: int = None,
        page_number: int = None,
        data: List[ListVehicleTrackResponseBodyData] = None,
        code: str = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.message = message
        self.page_size = page_size
        self.page_number = page_number
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListVehicleTrackResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class ListVehicleTrackResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListVehicleTrackResponseBody = None,
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
            temp_model = ListVehicleTrackResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PaginateDeviceRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        count_total_num: bool = None,
        corp_id: str = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.count_total_num = count_total_num
        self.corp_id = corp_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.count_total_num is not None:
            result['CountTotalNum'] = self.count_total_num
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CountTotalNum') is not None:
            self.count_total_num = m.get('CountTotalNum')
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        return self


class PaginateDeviceResponseBodyDataRecords(TeaModel):
    def __init__(
        self,
        device_id: str = None,
    ):
        self.device_id = device_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        return self


class PaginateDeviceResponseBodyData(TeaModel):
    def __init__(
        self,
        records: List[PaginateDeviceResponseBodyDataRecords] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.records = records
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        if self.records:
            for k in self.records:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Records'] = []
        if self.records is not None:
            for k in self.records:
                result['Records'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.records = []
        if m.get('Records') is not None:
            for k in m.get('Records'):
                temp_model = PaginateDeviceResponseBodyDataRecords()
                self.records.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class PaginateDeviceResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: PaginateDeviceResponseBodyData = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = PaginateDeviceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class PaginateDeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: PaginateDeviceResponseBody = None,
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
            temp_model = PaginateDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PaginateProjectRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        count_total_num: bool = None,
        type: str = None,
        name_like: str = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.count_total_num = count_total_num
        self.type = type
        self.name_like = name_like

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.count_total_num is not None:
            result['CountTotalNum'] = self.count_total_num
        if self.type is not None:
            result['Type'] = self.type
        if self.name_like is not None:
            result['NameLike'] = self.name_like
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CountTotalNum') is not None:
            self.count_total_num = m.get('CountTotalNum')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('NameLike') is not None:
            self.name_like = m.get('NameLike')
        return self


class PaginateProjectResponseBodyDataRecords(TeaModel):
    def __init__(
        self,
        type: str = None,
        modified_time: str = None,
        description: str = None,
        aggregate_scene_code: str = None,
        corp_id: str = None,
        user_id: str = None,
        icon: str = None,
        name: str = None,
        created_time: str = None,
    ):
        self.type = type
        self.modified_time = modified_time
        self.description = description
        self.aggregate_scene_code = aggregate_scene_code
        self.corp_id = corp_id
        self.user_id = user_id
        self.icon = icon
        self.name = name
        self.created_time = created_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.description is not None:
            result['Description'] = self.description
        if self.aggregate_scene_code is not None:
            result['AggregateSceneCode'] = self.aggregate_scene_code
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.icon is not None:
            result['Icon'] = self.icon
        if self.name is not None:
            result['Name'] = self.name
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('AggregateSceneCode') is not None:
            self.aggregate_scene_code = m.get('AggregateSceneCode')
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('Icon') is not None:
            self.icon = m.get('Icon')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        return self


class PaginateProjectResponseBodyData(TeaModel):
    def __init__(
        self,
        records: List[PaginateProjectResponseBodyDataRecords] = None,
        total_page: int = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.records = records
        self.total_page = total_page
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        if self.records:
            for k in self.records:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Records'] = []
        if self.records is not None:
            for k in self.records:
                result['Records'].append(k.to_map() if k else None)
        if self.total_page is not None:
            result['TotalPage'] = self.total_page
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.records = []
        if m.get('Records') is not None:
            for k in m.get('Records'):
                temp_model = PaginateProjectResponseBodyDataRecords()
                self.records.append(temp_model.from_map(k))
        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class PaginateProjectResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: PaginateProjectResponseBodyData = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = PaginateProjectResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class PaginateProjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: PaginateProjectResponseBody = None,
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
            temp_model = PaginateProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PredictTrajectoryDestinationRequest(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        id_type: str = None,
        id_value: str = None,
        predict_time_span: int = None,
    ):
        self.corp_id = corp_id
        self.id_type = id_type
        self.id_value = id_value
        self.predict_time_span = predict_time_span

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.id_value is not None:
            result['IdValue'] = self.id_value
        if self.predict_time_span is not None:
            result['PredictTimeSpan'] = self.predict_time_span
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('IdValue') is not None:
            self.id_value = m.get('IdValue')
        if m.get('PredictTimeSpan') is not None:
            self.predict_time_span = m.get('PredictTimeSpan')
        return self


class PredictTrajectoryDestinationResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: str = None,
        code: int = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class PredictTrajectoryDestinationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: PredictTrajectoryDestinationResponseBody = None,
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
            temp_model = PredictTrajectoryDestinationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTrajectoryByIdRequestIdList(TeaModel):
    def __init__(
        self,
        id_value: str = None,
        id_type: str = None,
    ):
        self.id_value = id_value
        self.id_type = id_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id_value is not None:
            result['IdValue'] = self.id_value
        if self.id_type is not None:
            result['IdType'] = self.id_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IdValue') is not None:
            self.id_value = m.get('IdValue')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        return self


class QueryTrajectoryByIdRequestDeviceList(TeaModel):
    def __init__(
        self,
        device_id: str = None,
    ):
        self.device_id = device_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        return self


class QueryTrajectoryByIdRequest(TeaModel):
    def __init__(
        self,
        start_time: str = None,
        end_time: str = None,
        corp_id: str = None,
        id_list: List[QueryTrajectoryByIdRequestIdList] = None,
        device_list: List[QueryTrajectoryByIdRequestDeviceList] = None,
    ):
        self.start_time = start_time
        self.end_time = end_time
        self.corp_id = corp_id
        self.id_list = id_list
        self.device_list = device_list

    def validate(self):
        if self.id_list:
            for k in self.id_list:
                if k:
                    k.validate()
        if self.device_list:
            for k in self.device_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        result['IdList'] = []
        if self.id_list is not None:
            for k in self.id_list:
                result['IdList'].append(k.to_map() if k else None)
        result['DeviceList'] = []
        if self.device_list is not None:
            for k in self.device_list:
                result['DeviceList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        self.id_list = []
        if m.get('IdList') is not None:
            for k in m.get('IdList'):
                temp_model = QueryTrajectoryByIdRequestIdList()
                self.id_list.append(temp_model.from_map(k))
        self.device_list = []
        if m.get('DeviceList') is not None:
            for k in m.get('DeviceList'):
                temp_model = QueryTrajectoryByIdRequestDeviceList()
                self.device_list.append(temp_model.from_map(k))
        return self


class QueryTrajectoryByIdResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: str = None,
        code: int = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryTrajectoryByIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryTrajectoryByIdResponseBody = None,
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
            temp_model = QueryTrajectoryByIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecallTrajectoryByCoordinateRequestPointList(TeaModel):
    def __init__(
        self,
        longitude: float = None,
        latitude: float = None,
    ):
        self.longitude = longitude
        self.latitude = latitude

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.longitude is not None:
            result['Longitude'] = self.longitude
        if self.latitude is not None:
            result['Latitude'] = self.latitude
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Longitude') is not None:
            self.longitude = m.get('Longitude')
        if m.get('Latitude') is not None:
            self.latitude = m.get('Latitude')
        return self


class RecallTrajectoryByCoordinateRequest(TeaModel):
    def __init__(
        self,
        start_time: str = None,
        end_time: str = None,
        corp_id: str = None,
        output_id_count: int = None,
        delta_distance: int = None,
        delta_time: int = None,
        point_list: List[RecallTrajectoryByCoordinateRequestPointList] = None,
        output_id_type_list: List[str] = None,
    ):
        self.start_time = start_time
        self.end_time = end_time
        self.corp_id = corp_id
        self.output_id_count = output_id_count
        self.delta_distance = delta_distance
        self.delta_time = delta_time
        self.point_list = point_list
        self.output_id_type_list = output_id_type_list

    def validate(self):
        if self.point_list:
            for k in self.point_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.output_id_count is not None:
            result['OutputIdCount'] = self.output_id_count
        if self.delta_distance is not None:
            result['DeltaDistance'] = self.delta_distance
        if self.delta_time is not None:
            result['DeltaTime'] = self.delta_time
        result['PointList'] = []
        if self.point_list is not None:
            for k in self.point_list:
                result['PointList'].append(k.to_map() if k else None)
        if self.output_id_type_list is not None:
            result['OutputIdTypeList'] = self.output_id_type_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('OutputIdCount') is not None:
            self.output_id_count = m.get('OutputIdCount')
        if m.get('DeltaDistance') is not None:
            self.delta_distance = m.get('DeltaDistance')
        if m.get('DeltaTime') is not None:
            self.delta_time = m.get('DeltaTime')
        self.point_list = []
        if m.get('PointList') is not None:
            for k in m.get('PointList'):
                temp_model = RecallTrajectoryByCoordinateRequestPointList()
                self.point_list.append(temp_model.from_map(k))
        if m.get('OutputIdTypeList') is not None:
            self.output_id_type_list = m.get('OutputIdTypeList')
        return self


class RecallTrajectoryByCoordinateResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: str = None,
        code: int = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RecallTrajectoryByCoordinateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RecallTrajectoryByCoordinateResponseBody = None,
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
            temp_model = RecallTrajectoryByCoordinateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecallTrajectoryByCoordinateTimeRequestPointList(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        start_time: str = None,
        longitude: float = None,
        latitude: float = None,
        delta_distance: float = None,
    ):
        self.end_time = end_time
        self.start_time = start_time
        self.longitude = longitude
        self.latitude = latitude
        self.delta_distance = delta_distance

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.longitude is not None:
            result['Longitude'] = self.longitude
        if self.latitude is not None:
            result['Latitude'] = self.latitude
        if self.delta_distance is not None:
            result['DeltaDistance'] = self.delta_distance
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Longitude') is not None:
            self.longitude = m.get('Longitude')
        if m.get('Latitude') is not None:
            self.latitude = m.get('Latitude')
        if m.get('DeltaDistance') is not None:
            self.delta_distance = m.get('DeltaDistance')
        return self


class RecallTrajectoryByCoordinateTimeRequest(TeaModel):
    def __init__(
        self,
        start_time: str = None,
        end_time: str = None,
        corp_id: str = None,
        output_id_count: int = None,
        point_list: List[RecallTrajectoryByCoordinateTimeRequestPointList] = None,
        output_id_type_list: List[str] = None,
    ):
        self.start_time = start_time
        self.end_time = end_time
        self.corp_id = corp_id
        self.output_id_count = output_id_count
        self.point_list = point_list
        self.output_id_type_list = output_id_type_list

    def validate(self):
        if self.point_list:
            for k in self.point_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.output_id_count is not None:
            result['OutputIdCount'] = self.output_id_count
        result['PointList'] = []
        if self.point_list is not None:
            for k in self.point_list:
                result['PointList'].append(k.to_map() if k else None)
        if self.output_id_type_list is not None:
            result['OutputIdTypeList'] = self.output_id_type_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('OutputIdCount') is not None:
            self.output_id_count = m.get('OutputIdCount')
        self.point_list = []
        if m.get('PointList') is not None:
            for k in m.get('PointList'):
                temp_model = RecallTrajectoryByCoordinateTimeRequestPointList()
                self.point_list.append(temp_model.from_map(k))
        if m.get('OutputIdTypeList') is not None:
            self.output_id_type_list = m.get('OutputIdTypeList')
        return self


class RecallTrajectoryByCoordinateTimeResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: str = None,
        code: int = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RecallTrajectoryByCoordinateTimeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RecallTrajectoryByCoordinateTimeResponseBody = None,
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
            temp_model = RecallTrajectoryByCoordinateTimeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecallTrajectoryByIdRequest(TeaModel):
    def __init__(
        self,
        start_time: str = None,
        end_time: str = None,
        corp_id: str = None,
        output_id_count: int = None,
        delta_distance: int = None,
        delta_time: int = None,
        id_type: str = None,
        id_value: str = None,
        output_id_type_list: List[str] = None,
    ):
        self.start_time = start_time
        self.end_time = end_time
        self.corp_id = corp_id
        self.output_id_count = output_id_count
        self.delta_distance = delta_distance
        self.delta_time = delta_time
        self.id_type = id_type
        self.id_value = id_value
        self.output_id_type_list = output_id_type_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.output_id_count is not None:
            result['OutputIdCount'] = self.output_id_count
        if self.delta_distance is not None:
            result['DeltaDistance'] = self.delta_distance
        if self.delta_time is not None:
            result['DeltaTime'] = self.delta_time
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.id_value is not None:
            result['IdValue'] = self.id_value
        if self.output_id_type_list is not None:
            result['OutputIdTypeList'] = self.output_id_type_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('OutputIdCount') is not None:
            self.output_id_count = m.get('OutputIdCount')
        if m.get('DeltaDistance') is not None:
            self.delta_distance = m.get('DeltaDistance')
        if m.get('DeltaTime') is not None:
            self.delta_time = m.get('DeltaTime')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('IdValue') is not None:
            self.id_value = m.get('IdValue')
        if m.get('OutputIdTypeList') is not None:
            self.output_id_type_list = m.get('OutputIdTypeList')
        return self


class RecallTrajectoryByIdResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: str = None,
        code: int = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RecallTrajectoryByIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RecallTrajectoryByIdResponseBody = None,
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
            temp_model = RecallTrajectoryByIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeImageRequest(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        vendor: str = None,
        image_content: str = None,
        image_url: str = None,
        recognize_type: str = None,
        require_crop_image: bool = None,
    ):
        self.corp_id = corp_id
        self.vendor = vendor
        self.image_content = image_content
        self.image_url = image_url
        self.recognize_type = recognize_type
        self.require_crop_image = require_crop_image

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.vendor is not None:
            result['Vendor'] = self.vendor
        if self.image_content is not None:
            result['ImageContent'] = self.image_content
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        if self.recognize_type is not None:
            result['RecognizeType'] = self.recognize_type
        if self.require_crop_image is not None:
            result['RequireCropImage'] = self.require_crop_image
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')
        if m.get('ImageContent') is not None:
            self.image_content = m.get('ImageContent')
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        if m.get('RecognizeType') is not None:
            self.recognize_type = m.get('RecognizeType')
        if m.get('RequireCropImage') is not None:
            self.require_crop_image = m.get('RequireCropImage')
        return self


class RecognizeImageResponseBodyDataBodyList(TeaModel):
    def __init__(
        self,
        crop_algorithm_code: str = None,
        right_bottom_y: int = None,
        feature: str = None,
        left_top_y: int = None,
        target_image_content: str = None,
        left_top_x: int = None,
        right_bottom_x: int = None,
    ):
        self.crop_algorithm_code = crop_algorithm_code
        self.right_bottom_y = right_bottom_y
        self.feature = feature
        self.left_top_y = left_top_y
        self.target_image_content = target_image_content
        self.left_top_x = left_top_x
        self.right_bottom_x = right_bottom_x

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.crop_algorithm_code is not None:
            result['CropAlgorithmCode'] = self.crop_algorithm_code
        if self.right_bottom_y is not None:
            result['RightBottomY'] = self.right_bottom_y
        if self.feature is not None:
            result['Feature'] = self.feature
        if self.left_top_y is not None:
            result['LeftTopY'] = self.left_top_y
        if self.target_image_content is not None:
            result['TargetImageContent'] = self.target_image_content
        if self.left_top_x is not None:
            result['LeftTopX'] = self.left_top_x
        if self.right_bottom_x is not None:
            result['RightBottomX'] = self.right_bottom_x
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CropAlgorithmCode') is not None:
            self.crop_algorithm_code = m.get('CropAlgorithmCode')
        if m.get('RightBottomY') is not None:
            self.right_bottom_y = m.get('RightBottomY')
        if m.get('Feature') is not None:
            self.feature = m.get('Feature')
        if m.get('LeftTopY') is not None:
            self.left_top_y = m.get('LeftTopY')
        if m.get('TargetImageContent') is not None:
            self.target_image_content = m.get('TargetImageContent')
        if m.get('LeftTopX') is not None:
            self.left_top_x = m.get('LeftTopX')
        if m.get('RightBottomX') is not None:
            self.right_bottom_x = m.get('RightBottomX')
        return self


class RecognizeImageResponseBodyDataFaceList(TeaModel):
    def __init__(
        self,
        crop_algorithm_code: str = None,
        feature: str = None,
        right_bottom_y: int = None,
        left_top_y: int = None,
        target_image_content: str = None,
        face_quality: float = None,
        right_bottom_x: int = None,
        left_top_x: int = None,
        face_key_point_quality: float = None,
    ):
        self.crop_algorithm_code = crop_algorithm_code
        self.feature = feature
        self.right_bottom_y = right_bottom_y
        self.left_top_y = left_top_y
        self.target_image_content = target_image_content
        self.face_quality = face_quality
        self.right_bottom_x = right_bottom_x
        self.left_top_x = left_top_x
        self.face_key_point_quality = face_key_point_quality

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.crop_algorithm_code is not None:
            result['CropAlgorithmCode'] = self.crop_algorithm_code
        if self.feature is not None:
            result['Feature'] = self.feature
        if self.right_bottom_y is not None:
            result['RightBottomY'] = self.right_bottom_y
        if self.left_top_y is not None:
            result['LeftTopY'] = self.left_top_y
        if self.target_image_content is not None:
            result['TargetImageContent'] = self.target_image_content
        if self.face_quality is not None:
            result['FaceQuality'] = self.face_quality
        if self.right_bottom_x is not None:
            result['RightBottomX'] = self.right_bottom_x
        if self.left_top_x is not None:
            result['LeftTopX'] = self.left_top_x
        if self.face_key_point_quality is not None:
            result['FaceKeyPointQuality'] = self.face_key_point_quality
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CropAlgorithmCode') is not None:
            self.crop_algorithm_code = m.get('CropAlgorithmCode')
        if m.get('Feature') is not None:
            self.feature = m.get('Feature')
        if m.get('RightBottomY') is not None:
            self.right_bottom_y = m.get('RightBottomY')
        if m.get('LeftTopY') is not None:
            self.left_top_y = m.get('LeftTopY')
        if m.get('TargetImageContent') is not None:
            self.target_image_content = m.get('TargetImageContent')
        if m.get('FaceQuality') is not None:
            self.face_quality = m.get('FaceQuality')
        if m.get('RightBottomX') is not None:
            self.right_bottom_x = m.get('RightBottomX')
        if m.get('LeftTopX') is not None:
            self.left_top_x = m.get('LeftTopX')
        if m.get('FaceKeyPointQuality') is not None:
            self.face_key_point_quality = m.get('FaceKeyPointQuality')
        return self


class RecognizeImageResponseBodyData(TeaModel):
    def __init__(
        self,
        body_list: List[RecognizeImageResponseBodyDataBodyList] = None,
        face_list: List[RecognizeImageResponseBodyDataFaceList] = None,
    ):
        self.body_list = body_list
        self.face_list = face_list

    def validate(self):
        if self.body_list:
            for k in self.body_list:
                if k:
                    k.validate()
        if self.face_list:
            for k in self.face_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['BodyList'] = []
        if self.body_list is not None:
            for k in self.body_list:
                result['BodyList'].append(k.to_map() if k else None)
        result['FaceList'] = []
        if self.face_list is not None:
            for k in self.face_list:
                result['FaceList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.body_list = []
        if m.get('BodyList') is not None:
            for k in m.get('BodyList'):
                temp_model = RecognizeImageResponseBodyDataBodyList()
                self.body_list.append(temp_model.from_map(k))
        self.face_list = []
        if m.get('FaceList') is not None:
            for k in m.get('FaceList'):
                temp_model = RecognizeImageResponseBodyDataFaceList()
                self.face_list.append(temp_model.from_map(k))
        return self


class RecognizeImageResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: RecognizeImageResponseBodyData = None,
        code: str = None,
        success: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = RecognizeImageResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RecognizeImageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RecognizeImageResponseBody = None,
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
            temp_model = RecognizeImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchAggregateObjectRequest(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        object_type: str = None,
        vendor: str = None,
        feature: str = None,
        image_content: str = None,
        image_url: str = None,
        device_list: str = None,
        attributes: str = None,
        shot_time_start: str = None,
        shot_time_end: str = None,
        page_number: int = None,
        page_size: int = None,
        require_total_count: bool = None,
    ):
        self.corp_id = corp_id
        self.object_type = object_type
        self.vendor = vendor
        self.feature = feature
        self.image_content = image_content
        self.image_url = image_url
        self.device_list = device_list
        self.attributes = attributes
        self.shot_time_start = shot_time_start
        self.shot_time_end = shot_time_end
        self.page_number = page_number
        self.page_size = page_size
        self.require_total_count = require_total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.object_type is not None:
            result['ObjectType'] = self.object_type
        if self.vendor is not None:
            result['Vendor'] = self.vendor
        if self.feature is not None:
            result['Feature'] = self.feature
        if self.image_content is not None:
            result['ImageContent'] = self.image_content
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        if self.device_list is not None:
            result['DeviceList'] = self.device_list
        if self.attributes is not None:
            result['Attributes'] = self.attributes
        if self.shot_time_start is not None:
            result['ShotTimeStart'] = self.shot_time_start
        if self.shot_time_end is not None:
            result['ShotTimeEnd'] = self.shot_time_end
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.require_total_count is not None:
            result['RequireTotalCount'] = self.require_total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')
        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')
        if m.get('Feature') is not None:
            self.feature = m.get('Feature')
        if m.get('ImageContent') is not None:
            self.image_content = m.get('ImageContent')
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        if m.get('DeviceList') is not None:
            self.device_list = m.get('DeviceList')
        if m.get('Attributes') is not None:
            self.attributes = m.get('Attributes')
        if m.get('ShotTimeStart') is not None:
            self.shot_time_start = m.get('ShotTimeStart')
        if m.get('ShotTimeEnd') is not None:
            self.shot_time_end = m.get('ShotTimeEnd')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequireTotalCount') is not None:
            self.require_total_count = m.get('RequireTotalCount')
        return self


class SearchAggregateObjectResponseBodyDataBodyList(TeaModel):
    def __init__(
        self,
        device_id: str = None,
        object_type: str = None,
        device_name: str = None,
        right_bottom_y: int = None,
        score: float = None,
        right_bottom_x: int = None,
        device_longitude: float = None,
        source_image_url: str = None,
        target_image_url: str = None,
        left_top_y: int = None,
        shot_time: str = None,
        person_id: str = None,
        left_top_x: int = None,
        device_latitude: float = None,
    ):
        self.device_id = device_id
        self.object_type = object_type
        self.device_name = device_name
        self.right_bottom_y = right_bottom_y
        self.score = score
        self.right_bottom_x = right_bottom_x
        self.device_longitude = device_longitude
        self.source_image_url = source_image_url
        self.target_image_url = target_image_url
        self.left_top_y = left_top_y
        self.shot_time = shot_time
        self.person_id = person_id
        self.left_top_x = left_top_x
        self.device_latitude = device_latitude

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_id is not None:
            result['DeviceID'] = self.device_id
        if self.object_type is not None:
            result['ObjectType'] = self.object_type
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.right_bottom_y is not None:
            result['RightBottomY'] = self.right_bottom_y
        if self.score is not None:
            result['Score'] = self.score
        if self.right_bottom_x is not None:
            result['RightBottomX'] = self.right_bottom_x
        if self.device_longitude is not None:
            result['DeviceLongitude'] = self.device_longitude
        if self.source_image_url is not None:
            result['SourceImageUrl'] = self.source_image_url
        if self.target_image_url is not None:
            result['TargetImageUrl'] = self.target_image_url
        if self.left_top_y is not None:
            result['LeftTopY'] = self.left_top_y
        if self.shot_time is not None:
            result['ShotTime'] = self.shot_time
        if self.person_id is not None:
            result['PersonId'] = self.person_id
        if self.left_top_x is not None:
            result['LeftTopX'] = self.left_top_x
        if self.device_latitude is not None:
            result['DeviceLatitude'] = self.device_latitude
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceID') is not None:
            self.device_id = m.get('DeviceID')
        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('RightBottomY') is not None:
            self.right_bottom_y = m.get('RightBottomY')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('RightBottomX') is not None:
            self.right_bottom_x = m.get('RightBottomX')
        if m.get('DeviceLongitude') is not None:
            self.device_longitude = m.get('DeviceLongitude')
        if m.get('SourceImageUrl') is not None:
            self.source_image_url = m.get('SourceImageUrl')
        if m.get('TargetImageUrl') is not None:
            self.target_image_url = m.get('TargetImageUrl')
        if m.get('LeftTopY') is not None:
            self.left_top_y = m.get('LeftTopY')
        if m.get('ShotTime') is not None:
            self.shot_time = m.get('ShotTime')
        if m.get('PersonId') is not None:
            self.person_id = m.get('PersonId')
        if m.get('LeftTopX') is not None:
            self.left_top_x = m.get('LeftTopX')
        if m.get('DeviceLatitude') is not None:
            self.device_latitude = m.get('DeviceLatitude')
        return self


class SearchAggregateObjectResponseBodyDataFaceList(TeaModel):
    def __init__(
        self,
        device_id: str = None,
        object_type: str = None,
        device_name: str = None,
        right_bottom_y: int = None,
        score: float = None,
        right_bottom_x: int = None,
        device_longitude: float = None,
        source_image_url: str = None,
        target_image_url: str = None,
        left_top_y: int = None,
        shot_time: str = None,
        person_id: str = None,
        left_top_x: int = None,
        device_latitude: float = None,
    ):
        self.device_id = device_id
        self.object_type = object_type
        self.device_name = device_name
        self.right_bottom_y = right_bottom_y
        self.score = score
        self.right_bottom_x = right_bottom_x
        self.device_longitude = device_longitude
        self.source_image_url = source_image_url
        self.target_image_url = target_image_url
        self.left_top_y = left_top_y
        self.shot_time = shot_time
        self.person_id = person_id
        self.left_top_x = left_top_x
        self.device_latitude = device_latitude

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_id is not None:
            result['DeviceID'] = self.device_id
        if self.object_type is not None:
            result['ObjectType'] = self.object_type
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.right_bottom_y is not None:
            result['RightBottomY'] = self.right_bottom_y
        if self.score is not None:
            result['Score'] = self.score
        if self.right_bottom_x is not None:
            result['RightBottomX'] = self.right_bottom_x
        if self.device_longitude is not None:
            result['DeviceLongitude'] = self.device_longitude
        if self.source_image_url is not None:
            result['SourceImageUrl'] = self.source_image_url
        if self.target_image_url is not None:
            result['TargetImageUrl'] = self.target_image_url
        if self.left_top_y is not None:
            result['LeftTopY'] = self.left_top_y
        if self.shot_time is not None:
            result['ShotTime'] = self.shot_time
        if self.person_id is not None:
            result['PersonId'] = self.person_id
        if self.left_top_x is not None:
            result['LeftTopX'] = self.left_top_x
        if self.device_latitude is not None:
            result['DeviceLatitude'] = self.device_latitude
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceID') is not None:
            self.device_id = m.get('DeviceID')
        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('RightBottomY') is not None:
            self.right_bottom_y = m.get('RightBottomY')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('RightBottomX') is not None:
            self.right_bottom_x = m.get('RightBottomX')
        if m.get('DeviceLongitude') is not None:
            self.device_longitude = m.get('DeviceLongitude')
        if m.get('SourceImageUrl') is not None:
            self.source_image_url = m.get('SourceImageUrl')
        if m.get('TargetImageUrl') is not None:
            self.target_image_url = m.get('TargetImageUrl')
        if m.get('LeftTopY') is not None:
            self.left_top_y = m.get('LeftTopY')
        if m.get('ShotTime') is not None:
            self.shot_time = m.get('ShotTime')
        if m.get('PersonId') is not None:
            self.person_id = m.get('PersonId')
        if m.get('LeftTopX') is not None:
            self.left_top_x = m.get('LeftTopX')
        if m.get('DeviceLatitude') is not None:
            self.device_latitude = m.get('DeviceLatitude')
        return self


class SearchAggregateObjectResponseBodyDataMotorList(TeaModel):
    def __init__(
        self,
        device_id: str = None,
        object_type: str = None,
        device_name: str = None,
        right_bottom_y: int = None,
        score: float = None,
        right_bottom_x: int = None,
        device_longitude: float = None,
        source_image_url: str = None,
        target_image_url: str = None,
        left_top_y: int = None,
        shot_time: str = None,
        person_id: str = None,
        left_top_x: int = None,
        device_latitude: float = None,
    ):
        self.device_id = device_id
        self.object_type = object_type
        self.device_name = device_name
        self.right_bottom_y = right_bottom_y
        self.score = score
        self.right_bottom_x = right_bottom_x
        self.device_longitude = device_longitude
        self.source_image_url = source_image_url
        self.target_image_url = target_image_url
        self.left_top_y = left_top_y
        self.shot_time = shot_time
        self.person_id = person_id
        self.left_top_x = left_top_x
        self.device_latitude = device_latitude

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_id is not None:
            result['DeviceID'] = self.device_id
        if self.object_type is not None:
            result['ObjectType'] = self.object_type
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.right_bottom_y is not None:
            result['RightBottomY'] = self.right_bottom_y
        if self.score is not None:
            result['Score'] = self.score
        if self.right_bottom_x is not None:
            result['RightBottomX'] = self.right_bottom_x
        if self.device_longitude is not None:
            result['DeviceLongitude'] = self.device_longitude
        if self.source_image_url is not None:
            result['SourceImageUrl'] = self.source_image_url
        if self.target_image_url is not None:
            result['TargetImageUrl'] = self.target_image_url
        if self.left_top_y is not None:
            result['LeftTopY'] = self.left_top_y
        if self.shot_time is not None:
            result['ShotTime'] = self.shot_time
        if self.person_id is not None:
            result['PersonId'] = self.person_id
        if self.left_top_x is not None:
            result['LeftTopX'] = self.left_top_x
        if self.device_latitude is not None:
            result['DeviceLatitude'] = self.device_latitude
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceID') is not None:
            self.device_id = m.get('DeviceID')
        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('RightBottomY') is not None:
            self.right_bottom_y = m.get('RightBottomY')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('RightBottomX') is not None:
            self.right_bottom_x = m.get('RightBottomX')
        if m.get('DeviceLongitude') is not None:
            self.device_longitude = m.get('DeviceLongitude')
        if m.get('SourceImageUrl') is not None:
            self.source_image_url = m.get('SourceImageUrl')
        if m.get('TargetImageUrl') is not None:
            self.target_image_url = m.get('TargetImageUrl')
        if m.get('LeftTopY') is not None:
            self.left_top_y = m.get('LeftTopY')
        if m.get('ShotTime') is not None:
            self.shot_time = m.get('ShotTime')
        if m.get('PersonId') is not None:
            self.person_id = m.get('PersonId')
        if m.get('LeftTopX') is not None:
            self.left_top_x = m.get('LeftTopX')
        if m.get('DeviceLatitude') is not None:
            self.device_latitude = m.get('DeviceLatitude')
        return self


class SearchAggregateObjectResponseBodyDataNonMotorList(TeaModel):
    def __init__(
        self,
        device_id: str = None,
        object_type: str = None,
        device_name: str = None,
        right_bottom_y: int = None,
        score: float = None,
        right_bottom_x: int = None,
        device_longitude: float = None,
        source_image_url: str = None,
        target_image_url: str = None,
        left_top_y: int = None,
        shot_time: str = None,
        person_id: str = None,
        left_top_x: int = None,
        device_latitude: float = None,
    ):
        self.device_id = device_id
        self.object_type = object_type
        self.device_name = device_name
        self.right_bottom_y = right_bottom_y
        self.score = score
        self.right_bottom_x = right_bottom_x
        self.device_longitude = device_longitude
        self.source_image_url = source_image_url
        self.target_image_url = target_image_url
        self.left_top_y = left_top_y
        self.shot_time = shot_time
        self.person_id = person_id
        self.left_top_x = left_top_x
        self.device_latitude = device_latitude

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_id is not None:
            result['DeviceID'] = self.device_id
        if self.object_type is not None:
            result['ObjectType'] = self.object_type
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.right_bottom_y is not None:
            result['RightBottomY'] = self.right_bottom_y
        if self.score is not None:
            result['Score'] = self.score
        if self.right_bottom_x is not None:
            result['RightBottomX'] = self.right_bottom_x
        if self.device_longitude is not None:
            result['DeviceLongitude'] = self.device_longitude
        if self.source_image_url is not None:
            result['SourceImageUrl'] = self.source_image_url
        if self.target_image_url is not None:
            result['TargetImageUrl'] = self.target_image_url
        if self.left_top_y is not None:
            result['LeftTopY'] = self.left_top_y
        if self.shot_time is not None:
            result['ShotTime'] = self.shot_time
        if self.person_id is not None:
            result['PersonId'] = self.person_id
        if self.left_top_x is not None:
            result['LeftTopX'] = self.left_top_x
        if self.device_latitude is not None:
            result['DeviceLatitude'] = self.device_latitude
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceID') is not None:
            self.device_id = m.get('DeviceID')
        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('RightBottomY') is not None:
            self.right_bottom_y = m.get('RightBottomY')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('RightBottomX') is not None:
            self.right_bottom_x = m.get('RightBottomX')
        if m.get('DeviceLongitude') is not None:
            self.device_longitude = m.get('DeviceLongitude')
        if m.get('SourceImageUrl') is not None:
            self.source_image_url = m.get('SourceImageUrl')
        if m.get('TargetImageUrl') is not None:
            self.target_image_url = m.get('TargetImageUrl')
        if m.get('LeftTopY') is not None:
            self.left_top_y = m.get('LeftTopY')
        if m.get('ShotTime') is not None:
            self.shot_time = m.get('ShotTime')
        if m.get('PersonId') is not None:
            self.person_id = m.get('PersonId')
        if m.get('LeftTopX') is not None:
            self.left_top_x = m.get('LeftTopX')
        if m.get('DeviceLatitude') is not None:
            self.device_latitude = m.get('DeviceLatitude')
        return self


class SearchAggregateObjectResponseBodyData(TeaModel):
    def __init__(
        self,
        body_list: List[SearchAggregateObjectResponseBodyDataBodyList] = None,
        face_list: List[SearchAggregateObjectResponseBodyDataFaceList] = None,
        motor_list: List[SearchAggregateObjectResponseBodyDataMotorList] = None,
        non_motor_list: List[SearchAggregateObjectResponseBodyDataNonMotorList] = None,
    ):
        self.body_list = body_list
        self.face_list = face_list
        self.motor_list = motor_list
        self.non_motor_list = non_motor_list

    def validate(self):
        if self.body_list:
            for k in self.body_list:
                if k:
                    k.validate()
        if self.face_list:
            for k in self.face_list:
                if k:
                    k.validate()
        if self.motor_list:
            for k in self.motor_list:
                if k:
                    k.validate()
        if self.non_motor_list:
            for k in self.non_motor_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['BodyList'] = []
        if self.body_list is not None:
            for k in self.body_list:
                result['BodyList'].append(k.to_map() if k else None)
        result['FaceList'] = []
        if self.face_list is not None:
            for k in self.face_list:
                result['FaceList'].append(k.to_map() if k else None)
        result['MotorList'] = []
        if self.motor_list is not None:
            for k in self.motor_list:
                result['MotorList'].append(k.to_map() if k else None)
        result['NonMotorList'] = []
        if self.non_motor_list is not None:
            for k in self.non_motor_list:
                result['NonMotorList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.body_list = []
        if m.get('BodyList') is not None:
            for k in m.get('BodyList'):
                temp_model = SearchAggregateObjectResponseBodyDataBodyList()
                self.body_list.append(temp_model.from_map(k))
        self.face_list = []
        if m.get('FaceList') is not None:
            for k in m.get('FaceList'):
                temp_model = SearchAggregateObjectResponseBodyDataFaceList()
                self.face_list.append(temp_model.from_map(k))
        self.motor_list = []
        if m.get('MotorList') is not None:
            for k in m.get('MotorList'):
                temp_model = SearchAggregateObjectResponseBodyDataMotorList()
                self.motor_list.append(temp_model.from_map(k))
        self.non_motor_list = []
        if m.get('NonMotorList') is not None:
            for k in m.get('NonMotorList'):
                temp_model = SearchAggregateObjectResponseBodyDataNonMotorList()
                self.non_motor_list.append(temp_model.from_map(k))
        return self


class SearchAggregateObjectResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        message: str = None,
        page_size: int = None,
        total: int = None,
        data: SearchAggregateObjectResponseBodyData = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.message = message
        self.page_size = page_size
        self.total = total
        self.data = data
        self.code = code
        self.success = success

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
        if self.message is not None:
            result['Message'] = self.message
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('Data') is not None:
            temp_model = SearchAggregateObjectResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SearchAggregateObjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SearchAggregateObjectResponseBody = None,
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
            temp_model = SearchAggregateObjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchObjectRequest(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        object_type: str = None,
        vendor: str = None,
        feature: str = None,
        image_content: str = None,
        image_url: str = None,
        device_list: str = None,
        attributes: str = None,
        shot_time_start: str = None,
        shot_time_end: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.corp_id = corp_id
        self.object_type = object_type
        self.vendor = vendor
        self.feature = feature
        self.image_content = image_content
        self.image_url = image_url
        self.device_list = device_list
        self.attributes = attributes
        self.shot_time_start = shot_time_start
        self.shot_time_end = shot_time_end
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.object_type is not None:
            result['ObjectType'] = self.object_type
        if self.vendor is not None:
            result['Vendor'] = self.vendor
        if self.feature is not None:
            result['Feature'] = self.feature
        if self.image_content is not None:
            result['ImageContent'] = self.image_content
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        if self.device_list is not None:
            result['DeviceList'] = self.device_list
        if self.attributes is not None:
            result['Attributes'] = self.attributes
        if self.shot_time_start is not None:
            result['ShotTimeStart'] = self.shot_time_start
        if self.shot_time_end is not None:
            result['ShotTimeEnd'] = self.shot_time_end
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')
        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')
        if m.get('Feature') is not None:
            self.feature = m.get('Feature')
        if m.get('ImageContent') is not None:
            self.image_content = m.get('ImageContent')
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        if m.get('DeviceList') is not None:
            self.device_list = m.get('DeviceList')
        if m.get('Attributes') is not None:
            self.attributes = m.get('Attributes')
        if m.get('ShotTimeStart') is not None:
            self.shot_time_start = m.get('ShotTimeStart')
        if m.get('ShotTimeEnd') is not None:
            self.shot_time_end = m.get('ShotTimeEnd')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class SearchObjectResponseBodyDataBodyList(TeaModel):
    def __init__(
        self,
        source_image_url: str = None,
        device_id: str = None,
        object_type: str = None,
        target_image_url: str = None,
        right_bottom_y: int = None,
        left_top_y: int = None,
        score: float = None,
        shot_time: str = None,
        right_bottom_x: int = None,
        left_top_x: int = None,
    ):
        self.source_image_url = source_image_url
        self.device_id = device_id
        self.object_type = object_type
        self.target_image_url = target_image_url
        self.right_bottom_y = right_bottom_y
        self.left_top_y = left_top_y
        self.score = score
        self.shot_time = shot_time
        self.right_bottom_x = right_bottom_x
        self.left_top_x = left_top_x

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_image_url is not None:
            result['SourceImageUrl'] = self.source_image_url
        if self.device_id is not None:
            result['DeviceID'] = self.device_id
        if self.object_type is not None:
            result['ObjectType'] = self.object_type
        if self.target_image_url is not None:
            result['TargetImageUrl'] = self.target_image_url
        if self.right_bottom_y is not None:
            result['RightBottomY'] = self.right_bottom_y
        if self.left_top_y is not None:
            result['LeftTopY'] = self.left_top_y
        if self.score is not None:
            result['Score'] = self.score
        if self.shot_time is not None:
            result['ShotTime'] = self.shot_time
        if self.right_bottom_x is not None:
            result['RightBottomX'] = self.right_bottom_x
        if self.left_top_x is not None:
            result['LeftTopX'] = self.left_top_x
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceImageUrl') is not None:
            self.source_image_url = m.get('SourceImageUrl')
        if m.get('DeviceID') is not None:
            self.device_id = m.get('DeviceID')
        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')
        if m.get('TargetImageUrl') is not None:
            self.target_image_url = m.get('TargetImageUrl')
        if m.get('RightBottomY') is not None:
            self.right_bottom_y = m.get('RightBottomY')
        if m.get('LeftTopY') is not None:
            self.left_top_y = m.get('LeftTopY')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('ShotTime') is not None:
            self.shot_time = m.get('ShotTime')
        if m.get('RightBottomX') is not None:
            self.right_bottom_x = m.get('RightBottomX')
        if m.get('LeftTopX') is not None:
            self.left_top_x = m.get('LeftTopX')
        return self


class SearchObjectResponseBodyDataFaceList(TeaModel):
    def __init__(
        self,
        source_image_url: str = None,
        device_id: str = None,
        object_type: str = None,
        target_image_url: str = None,
        right_bottom_y: int = None,
        left_top_y: int = None,
        score: float = None,
        shot_time: str = None,
        right_bottom_x: int = None,
        left_top_x: int = None,
    ):
        self.source_image_url = source_image_url
        self.device_id = device_id
        self.object_type = object_type
        self.target_image_url = target_image_url
        self.right_bottom_y = right_bottom_y
        self.left_top_y = left_top_y
        self.score = score
        self.shot_time = shot_time
        self.right_bottom_x = right_bottom_x
        self.left_top_x = left_top_x

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_image_url is not None:
            result['SourceImageUrl'] = self.source_image_url
        if self.device_id is not None:
            result['DeviceID'] = self.device_id
        if self.object_type is not None:
            result['ObjectType'] = self.object_type
        if self.target_image_url is not None:
            result['TargetImageUrl'] = self.target_image_url
        if self.right_bottom_y is not None:
            result['RightBottomY'] = self.right_bottom_y
        if self.left_top_y is not None:
            result['LeftTopY'] = self.left_top_y
        if self.score is not None:
            result['Score'] = self.score
        if self.shot_time is not None:
            result['ShotTime'] = self.shot_time
        if self.right_bottom_x is not None:
            result['RightBottomX'] = self.right_bottom_x
        if self.left_top_x is not None:
            result['LeftTopX'] = self.left_top_x
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceImageUrl') is not None:
            self.source_image_url = m.get('SourceImageUrl')
        if m.get('DeviceID') is not None:
            self.device_id = m.get('DeviceID')
        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')
        if m.get('TargetImageUrl') is not None:
            self.target_image_url = m.get('TargetImageUrl')
        if m.get('RightBottomY') is not None:
            self.right_bottom_y = m.get('RightBottomY')
        if m.get('LeftTopY') is not None:
            self.left_top_y = m.get('LeftTopY')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('ShotTime') is not None:
            self.shot_time = m.get('ShotTime')
        if m.get('RightBottomX') is not None:
            self.right_bottom_x = m.get('RightBottomX')
        if m.get('LeftTopX') is not None:
            self.left_top_x = m.get('LeftTopX')
        return self


class SearchObjectResponseBodyDataMotorList(TeaModel):
    def __init__(
        self,
        source_image_url: str = None,
        device_id: str = None,
        object_type: str = None,
        target_image_url: str = None,
        right_bottom_y: int = None,
        left_top_y: int = None,
        score: float = None,
        shot_time: str = None,
        right_bottom_x: int = None,
        left_top_x: int = None,
    ):
        self.source_image_url = source_image_url
        self.device_id = device_id
        self.object_type = object_type
        self.target_image_url = target_image_url
        self.right_bottom_y = right_bottom_y
        self.left_top_y = left_top_y
        self.score = score
        self.shot_time = shot_time
        self.right_bottom_x = right_bottom_x
        self.left_top_x = left_top_x

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_image_url is not None:
            result['SourceImageUrl'] = self.source_image_url
        if self.device_id is not None:
            result['DeviceID'] = self.device_id
        if self.object_type is not None:
            result['ObjectType'] = self.object_type
        if self.target_image_url is not None:
            result['TargetImageUrl'] = self.target_image_url
        if self.right_bottom_y is not None:
            result['RightBottomY'] = self.right_bottom_y
        if self.left_top_y is not None:
            result['LeftTopY'] = self.left_top_y
        if self.score is not None:
            result['Score'] = self.score
        if self.shot_time is not None:
            result['ShotTime'] = self.shot_time
        if self.right_bottom_x is not None:
            result['RightBottomX'] = self.right_bottom_x
        if self.left_top_x is not None:
            result['LeftTopX'] = self.left_top_x
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceImageUrl') is not None:
            self.source_image_url = m.get('SourceImageUrl')
        if m.get('DeviceID') is not None:
            self.device_id = m.get('DeviceID')
        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')
        if m.get('TargetImageUrl') is not None:
            self.target_image_url = m.get('TargetImageUrl')
        if m.get('RightBottomY') is not None:
            self.right_bottom_y = m.get('RightBottomY')
        if m.get('LeftTopY') is not None:
            self.left_top_y = m.get('LeftTopY')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('ShotTime') is not None:
            self.shot_time = m.get('ShotTime')
        if m.get('RightBottomX') is not None:
            self.right_bottom_x = m.get('RightBottomX')
        if m.get('LeftTopX') is not None:
            self.left_top_x = m.get('LeftTopX')
        return self


class SearchObjectResponseBodyDataNonMotorList(TeaModel):
    def __init__(
        self,
        source_image_url: str = None,
        device_id: str = None,
        object_type: str = None,
        target_image_url: str = None,
        right_bottom_y: int = None,
        left_top_y: int = None,
        score: float = None,
        shot_time: str = None,
        right_bottom_x: int = None,
        left_top_x: int = None,
    ):
        self.source_image_url = source_image_url
        self.device_id = device_id
        self.object_type = object_type
        self.target_image_url = target_image_url
        self.right_bottom_y = right_bottom_y
        self.left_top_y = left_top_y
        self.score = score
        self.shot_time = shot_time
        self.right_bottom_x = right_bottom_x
        self.left_top_x = left_top_x

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_image_url is not None:
            result['SourceImageUrl'] = self.source_image_url
        if self.device_id is not None:
            result['DeviceID'] = self.device_id
        if self.object_type is not None:
            result['ObjectType'] = self.object_type
        if self.target_image_url is not None:
            result['TargetImageUrl'] = self.target_image_url
        if self.right_bottom_y is not None:
            result['RightBottomY'] = self.right_bottom_y
        if self.left_top_y is not None:
            result['LeftTopY'] = self.left_top_y
        if self.score is not None:
            result['Score'] = self.score
        if self.shot_time is not None:
            result['ShotTime'] = self.shot_time
        if self.right_bottom_x is not None:
            result['RightBottomX'] = self.right_bottom_x
        if self.left_top_x is not None:
            result['LeftTopX'] = self.left_top_x
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceImageUrl') is not None:
            self.source_image_url = m.get('SourceImageUrl')
        if m.get('DeviceID') is not None:
            self.device_id = m.get('DeviceID')
        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')
        if m.get('TargetImageUrl') is not None:
            self.target_image_url = m.get('TargetImageUrl')
        if m.get('RightBottomY') is not None:
            self.right_bottom_y = m.get('RightBottomY')
        if m.get('LeftTopY') is not None:
            self.left_top_y = m.get('LeftTopY')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('ShotTime') is not None:
            self.shot_time = m.get('ShotTime')
        if m.get('RightBottomX') is not None:
            self.right_bottom_x = m.get('RightBottomX')
        if m.get('LeftTopX') is not None:
            self.left_top_x = m.get('LeftTopX')
        return self


class SearchObjectResponseBodyData(TeaModel):
    def __init__(
        self,
        body_list: List[SearchObjectResponseBodyDataBodyList] = None,
        face_list: List[SearchObjectResponseBodyDataFaceList] = None,
        motor_list: List[SearchObjectResponseBodyDataMotorList] = None,
        non_motor_list: List[SearchObjectResponseBodyDataNonMotorList] = None,
    ):
        self.body_list = body_list
        self.face_list = face_list
        self.motor_list = motor_list
        self.non_motor_list = non_motor_list

    def validate(self):
        if self.body_list:
            for k in self.body_list:
                if k:
                    k.validate()
        if self.face_list:
            for k in self.face_list:
                if k:
                    k.validate()
        if self.motor_list:
            for k in self.motor_list:
                if k:
                    k.validate()
        if self.non_motor_list:
            for k in self.non_motor_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['BodyList'] = []
        if self.body_list is not None:
            for k in self.body_list:
                result['BodyList'].append(k.to_map() if k else None)
        result['FaceList'] = []
        if self.face_list is not None:
            for k in self.face_list:
                result['FaceList'].append(k.to_map() if k else None)
        result['MotorList'] = []
        if self.motor_list is not None:
            for k in self.motor_list:
                result['MotorList'].append(k.to_map() if k else None)
        result['NonMotorList'] = []
        if self.non_motor_list is not None:
            for k in self.non_motor_list:
                result['NonMotorList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.body_list = []
        if m.get('BodyList') is not None:
            for k in m.get('BodyList'):
                temp_model = SearchObjectResponseBodyDataBodyList()
                self.body_list.append(temp_model.from_map(k))
        self.face_list = []
        if m.get('FaceList') is not None:
            for k in m.get('FaceList'):
                temp_model = SearchObjectResponseBodyDataFaceList()
                self.face_list.append(temp_model.from_map(k))
        self.motor_list = []
        if m.get('MotorList') is not None:
            for k in m.get('MotorList'):
                temp_model = SearchObjectResponseBodyDataMotorList()
                self.motor_list.append(temp_model.from_map(k))
        self.non_motor_list = []
        if m.get('NonMotorList') is not None:
            for k in m.get('NonMotorList'):
                temp_model = SearchObjectResponseBodyDataNonMotorList()
                self.non_motor_list.append(temp_model.from_map(k))
        return self


class SearchObjectResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        message: str = None,
        page_size: int = None,
        total: int = None,
        data: SearchObjectResponseBodyData = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.message = message
        self.page_size = page_size
        self.total = total
        self.data = data
        self.code = code
        self.success = success

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
        if self.message is not None:
            result['Message'] = self.message
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('Data') is not None:
            temp_model = SearchObjectResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SearchObjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SearchObjectResponseBody = None,
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
            temp_model = SearchObjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopCdrsMonitorRequest(TeaModel):
    def __init__(
        self,
        task_id: str = None,
        algorithm_vendor: str = None,
        corp_id: str = None,
    ):
        self.task_id = task_id
        self.algorithm_vendor = algorithm_vendor
        self.corp_id = corp_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.algorithm_vendor is not None:
            result['AlgorithmVendor'] = self.algorithm_vendor
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('AlgorithmVendor') is not None:
            self.algorithm_vendor = m.get('AlgorithmVendor')
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        return self


class StopCdrsMonitorResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: str = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class StopCdrsMonitorResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StopCdrsMonitorResponseBody = None,
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
            temp_model = StopCdrsMonitorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopMonitorRequest(TeaModel):
    def __init__(
        self,
        task_id: str = None,
        algorithm_vendor: str = None,
        corp_id: str = None,
    ):
        self.task_id = task_id
        self.algorithm_vendor = algorithm_vendor
        self.corp_id = corp_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.algorithm_vendor is not None:
            result['AlgorithmVendor'] = self.algorithm_vendor
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('AlgorithmVendor') is not None:
            self.algorithm_vendor = m.get('AlgorithmVendor')
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        return self


class StopMonitorResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: str = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class StopMonitorResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StopMonitorResponseBody = None,
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
            temp_model = StopMonitorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnbindDeviceRequest(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        device_ids: str = None,
    ):
        self.corp_id = corp_id
        self.device_ids = device_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.device_ids is not None:
            result['DeviceIds'] = self.device_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('DeviceIds') is not None:
            self.device_ids = m.get('DeviceIds')
        return self


class UnbindDeviceResponseBodyData(TeaModel):
    def __init__(
        self,
        device_id: str = None,
        success: bool = None,
        code: str = None,
        message: str = None,
    ):
        self.device_id = device_id
        self.success = success
        self.code = code
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.success is not None:
            result['Success'] = self.success
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class UnbindDeviceResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: List[UnbindDeviceResponseBodyData] = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = UnbindDeviceResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class UnbindDeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UnbindDeviceResponseBody = None,
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
            temp_model = UnbindDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateCdrsMonitorRequest(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        task_id: str = None,
        rule_name: str = None,
        device_operate_type: str = None,
        device_list: str = None,
        pic_operate_type: str = None,
        pic_list: str = None,
        attribute_operate_type: str = None,
        attribute_name: str = None,
        attribute_value_list: str = None,
        description: str = None,
        rule_expression: str = None,
        algorithm_vendor: str = None,
        notifier_type: str = None,
        notifier_url: str = None,
        notifier_app_secret: str = None,
        notifier_time_out: int = None,
        notifier_extend_values: str = None,
    ):
        self.corp_id = corp_id
        self.task_id = task_id
        self.rule_name = rule_name
        self.device_operate_type = device_operate_type
        self.device_list = device_list
        self.pic_operate_type = pic_operate_type
        self.pic_list = pic_list
        self.attribute_operate_type = attribute_operate_type
        self.attribute_name = attribute_name
        self.attribute_value_list = attribute_value_list
        self.description = description
        self.rule_expression = rule_expression
        self.algorithm_vendor = algorithm_vendor
        self.notifier_type = notifier_type
        self.notifier_url = notifier_url
        self.notifier_app_secret = notifier_app_secret
        self.notifier_time_out = notifier_time_out
        self.notifier_extend_values = notifier_extend_values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.device_operate_type is not None:
            result['DeviceOperateType'] = self.device_operate_type
        if self.device_list is not None:
            result['DeviceList'] = self.device_list
        if self.pic_operate_type is not None:
            result['PicOperateType'] = self.pic_operate_type
        if self.pic_list is not None:
            result['PicList'] = self.pic_list
        if self.attribute_operate_type is not None:
            result['AttributeOperateType'] = self.attribute_operate_type
        if self.attribute_name is not None:
            result['AttributeName'] = self.attribute_name
        if self.attribute_value_list is not None:
            result['AttributeValueList'] = self.attribute_value_list
        if self.description is not None:
            result['Description'] = self.description
        if self.rule_expression is not None:
            result['RuleExpression'] = self.rule_expression
        if self.algorithm_vendor is not None:
            result['AlgorithmVendor'] = self.algorithm_vendor
        if self.notifier_type is not None:
            result['NotifierType'] = self.notifier_type
        if self.notifier_url is not None:
            result['NotifierUrl'] = self.notifier_url
        if self.notifier_app_secret is not None:
            result['NotifierAppSecret'] = self.notifier_app_secret
        if self.notifier_time_out is not None:
            result['NotifierTimeOut'] = self.notifier_time_out
        if self.notifier_extend_values is not None:
            result['NotifierExtendValues'] = self.notifier_extend_values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('DeviceOperateType') is not None:
            self.device_operate_type = m.get('DeviceOperateType')
        if m.get('DeviceList') is not None:
            self.device_list = m.get('DeviceList')
        if m.get('PicOperateType') is not None:
            self.pic_operate_type = m.get('PicOperateType')
        if m.get('PicList') is not None:
            self.pic_list = m.get('PicList')
        if m.get('AttributeOperateType') is not None:
            self.attribute_operate_type = m.get('AttributeOperateType')
        if m.get('AttributeName') is not None:
            self.attribute_name = m.get('AttributeName')
        if m.get('AttributeValueList') is not None:
            self.attribute_value_list = m.get('AttributeValueList')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('RuleExpression') is not None:
            self.rule_expression = m.get('RuleExpression')
        if m.get('AlgorithmVendor') is not None:
            self.algorithm_vendor = m.get('AlgorithmVendor')
        if m.get('NotifierType') is not None:
            self.notifier_type = m.get('NotifierType')
        if m.get('NotifierUrl') is not None:
            self.notifier_url = m.get('NotifierUrl')
        if m.get('NotifierAppSecret') is not None:
            self.notifier_app_secret = m.get('NotifierAppSecret')
        if m.get('NotifierTimeOut') is not None:
            self.notifier_time_out = m.get('NotifierTimeOut')
        if m.get('NotifierExtendValues') is not None:
            self.notifier_extend_values = m.get('NotifierExtendValues')
        return self


class UpdateCdrsMonitorResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: str = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class UpdateCdrsMonitorResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateCdrsMonitorResponseBody = None,
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
            temp_model = UpdateCdrsMonitorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateMonitorRequest(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        task_id: str = None,
        rule_name: str = None,
        device_operate_type: str = None,
        device_list: str = None,
        pic_operate_type: str = None,
        pic_list: str = None,
        attribute_operate_type: str = None,
        attribute_name: str = None,
        attribute_value_list: str = None,
        description: str = None,
        rule_expression: str = None,
        algorithm_vendor: str = None,
        notifier_type: str = None,
        notifier_url: str = None,
        notifier_app_secret: str = None,
        notifier_time_out: int = None,
        notifier_extend_values: str = None,
        pic_extend_list: str = None,
    ):
        self.corp_id = corp_id
        self.task_id = task_id
        self.rule_name = rule_name
        self.device_operate_type = device_operate_type
        self.device_list = device_list
        self.pic_operate_type = pic_operate_type
        self.pic_list = pic_list
        self.attribute_operate_type = attribute_operate_type
        self.attribute_name = attribute_name
        self.attribute_value_list = attribute_value_list
        self.description = description
        self.rule_expression = rule_expression
        self.algorithm_vendor = algorithm_vendor
        self.notifier_type = notifier_type
        self.notifier_url = notifier_url
        self.notifier_app_secret = notifier_app_secret
        self.notifier_time_out = notifier_time_out
        self.notifier_extend_values = notifier_extend_values
        self.pic_extend_list = pic_extend_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.device_operate_type is not None:
            result['DeviceOperateType'] = self.device_operate_type
        if self.device_list is not None:
            result['DeviceList'] = self.device_list
        if self.pic_operate_type is not None:
            result['PicOperateType'] = self.pic_operate_type
        if self.pic_list is not None:
            result['PicList'] = self.pic_list
        if self.attribute_operate_type is not None:
            result['AttributeOperateType'] = self.attribute_operate_type
        if self.attribute_name is not None:
            result['AttributeName'] = self.attribute_name
        if self.attribute_value_list is not None:
            result['AttributeValueList'] = self.attribute_value_list
        if self.description is not None:
            result['Description'] = self.description
        if self.rule_expression is not None:
            result['RuleExpression'] = self.rule_expression
        if self.algorithm_vendor is not None:
            result['AlgorithmVendor'] = self.algorithm_vendor
        if self.notifier_type is not None:
            result['NotifierType'] = self.notifier_type
        if self.notifier_url is not None:
            result['NotifierUrl'] = self.notifier_url
        if self.notifier_app_secret is not None:
            result['NotifierAppSecret'] = self.notifier_app_secret
        if self.notifier_time_out is not None:
            result['NotifierTimeOut'] = self.notifier_time_out
        if self.notifier_extend_values is not None:
            result['NotifierExtendValues'] = self.notifier_extend_values
        if self.pic_extend_list is not None:
            result['PicExtendList'] = self.pic_extend_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('DeviceOperateType') is not None:
            self.device_operate_type = m.get('DeviceOperateType')
        if m.get('DeviceList') is not None:
            self.device_list = m.get('DeviceList')
        if m.get('PicOperateType') is not None:
            self.pic_operate_type = m.get('PicOperateType')
        if m.get('PicList') is not None:
            self.pic_list = m.get('PicList')
        if m.get('AttributeOperateType') is not None:
            self.attribute_operate_type = m.get('AttributeOperateType')
        if m.get('AttributeName') is not None:
            self.attribute_name = m.get('AttributeName')
        if m.get('AttributeValueList') is not None:
            self.attribute_value_list = m.get('AttributeValueList')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('RuleExpression') is not None:
            self.rule_expression = m.get('RuleExpression')
        if m.get('AlgorithmVendor') is not None:
            self.algorithm_vendor = m.get('AlgorithmVendor')
        if m.get('NotifierType') is not None:
            self.notifier_type = m.get('NotifierType')
        if m.get('NotifierUrl') is not None:
            self.notifier_url = m.get('NotifierUrl')
        if m.get('NotifierAppSecret') is not None:
            self.notifier_app_secret = m.get('NotifierAppSecret')
        if m.get('NotifierTimeOut') is not None:
            self.notifier_time_out = m.get('NotifierTimeOut')
        if m.get('NotifierExtendValues') is not None:
            self.notifier_extend_values = m.get('NotifierExtendValues')
        if m.get('PicExtendList') is not None:
            self.pic_extend_list = m.get('PicExtendList')
        return self


class UpdateMonitorResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: str = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class UpdateMonitorResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateMonitorResponseBody = None,
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
            temp_model = UpdateMonitorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateProjectRequest(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        icon: str = None,
        name: str = None,
        description: str = None,
        aggregate_scene_code: str = None,
    ):
        self.corp_id = corp_id
        self.icon = icon
        self.name = name
        self.description = description
        self.aggregate_scene_code = aggregate_scene_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.icon is not None:
            result['Icon'] = self.icon
        if self.name is not None:
            result['Name'] = self.name
        if self.description is not None:
            result['Description'] = self.description
        if self.aggregate_scene_code is not None:
            result['AggregateSceneCode'] = self.aggregate_scene_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('Icon') is not None:
            self.icon = m.get('Icon')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('AggregateSceneCode') is not None:
            self.aggregate_scene_code = m.get('AggregateSceneCode')
        return self


class UpdateProjectResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class UpdateProjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateProjectResponseBody = None,
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
            temp_model = UpdateProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ValidateTrajectoryRequest(TeaModel):
    def __init__(
        self,
        start_time: str = None,
        end_time: str = None,
        corp_id: str = None,
        id_type: str = None,
        id_value: str = None,
    ):
        self.start_time = start_time
        self.end_time = end_time
        self.corp_id = corp_id
        self.id_type = id_type
        self.id_value = id_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.id_value is not None:
            result['IdValue'] = self.id_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('IdValue') is not None:
            self.id_value = m.get('IdValue')
        return self


class ValidateTrajectoryResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: str = None,
        code: int = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ValidateTrajectoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ValidateTrajectoryResponseBody = None,
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
            temp_model = ValidateTrajectoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


