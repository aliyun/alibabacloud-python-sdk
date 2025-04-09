# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict, Any


class ActivateLicenseRequest(TeaModel):
    def __init__(
        self,
        fingerprint: str = None,
        id: str = None,
        instance_id: str = None,
        order_id: str = None,
    ):
        self.fingerprint = fingerprint
        # ID
        self.id = id
        self.instance_id = instance_id
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fingerprint is not None:
            result['Fingerprint'] = self.fingerprint
        if self.id is not None:
            result['Id'] = self.id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Fingerprint') is not None:
            self.fingerprint = m.get('Fingerprint')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class ActivateLicenseResponseBodyDataActivateRecord(TeaModel):
    def __init__(
        self,
        activate_time: str = None,
        buy_time: str = None,
        duration: str = None,
        expire_time: str = None,
        license_code: str = None,
        order_id: str = None,
        status: str = None,
    ):
        self.activate_time = activate_time
        self.buy_time = buy_time
        self.duration = duration
        self.expire_time = expire_time
        self.license_code = license_code
        self.order_id = order_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.activate_time is not None:
            result['ActivateTime'] = self.activate_time
        if self.buy_time is not None:
            result['BuyTime'] = self.buy_time
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.license_code is not None:
            result['LicenseCode'] = self.license_code
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActivateTime') is not None:
            self.activate_time = m.get('ActivateTime')
        if m.get('BuyTime') is not None:
            self.buy_time = m.get('BuyTime')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('LicenseCode') is not None:
            self.license_code = m.get('LicenseCode')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ActivateLicenseResponseBodyData(TeaModel):
    def __init__(
        self,
        activate_record: List[ActivateLicenseResponseBodyDataActivateRecord] = None,
        activate_time: str = None,
        all_duration: str = None,
        applicable_specs: str = None,
        buy_time: str = None,
        cpu_limit: int = None,
        description: str = None,
        duration: str = None,
        effect_time: str = None,
        expire_time: str = None,
        fingerprint: str = None,
        id: str = None,
        instance_id: str = None,
        license_code: str = None,
        license_spec_name: str = None,
        memory_limit: int = None,
        status: str = None,
        un_activate_all_duration: str = None,
    ):
        self.activate_record = activate_record
        self.activate_time = activate_time
        self.all_duration = all_duration
        self.applicable_specs = applicable_specs
        self.buy_time = buy_time
        self.cpu_limit = cpu_limit
        self.description = description
        self.duration = duration
        self.effect_time = effect_time
        self.expire_time = expire_time
        self.fingerprint = fingerprint
        # Id
        self.id = id
        self.instance_id = instance_id
        self.license_code = license_code
        self.license_spec_name = license_spec_name
        self.memory_limit = memory_limit
        self.status = status
        self.un_activate_all_duration = un_activate_all_duration

    def validate(self):
        if self.activate_record:
            for k in self.activate_record:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ActivateRecord'] = []
        if self.activate_record is not None:
            for k in self.activate_record:
                result['ActivateRecord'].append(k.to_map() if k else None)
        if self.activate_time is not None:
            result['ActivateTime'] = self.activate_time
        if self.all_duration is not None:
            result['AllDuration'] = self.all_duration
        if self.applicable_specs is not None:
            result['ApplicableSpecs'] = self.applicable_specs
        if self.buy_time is not None:
            result['BuyTime'] = self.buy_time
        if self.cpu_limit is not None:
            result['CpuLimit'] = self.cpu_limit
        if self.description is not None:
            result['Description'] = self.description
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.effect_time is not None:
            result['EffectTime'] = self.effect_time
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.fingerprint is not None:
            result['Fingerprint'] = self.fingerprint
        if self.id is not None:
            result['Id'] = self.id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.license_code is not None:
            result['LicenseCode'] = self.license_code
        if self.license_spec_name is not None:
            result['LicenseSpecName'] = self.license_spec_name
        if self.memory_limit is not None:
            result['MemoryLimit'] = self.memory_limit
        if self.status is not None:
            result['Status'] = self.status
        if self.un_activate_all_duration is not None:
            result['UnActivateAllDuration'] = self.un_activate_all_duration
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.activate_record = []
        if m.get('ActivateRecord') is not None:
            for k in m.get('ActivateRecord'):
                temp_model = ActivateLicenseResponseBodyDataActivateRecord()
                self.activate_record.append(temp_model.from_map(k))
        if m.get('ActivateTime') is not None:
            self.activate_time = m.get('ActivateTime')
        if m.get('AllDuration') is not None:
            self.all_duration = m.get('AllDuration')
        if m.get('ApplicableSpecs') is not None:
            self.applicable_specs = m.get('ApplicableSpecs')
        if m.get('BuyTime') is not None:
            self.buy_time = m.get('BuyTime')
        if m.get('CpuLimit') is not None:
            self.cpu_limit = m.get('CpuLimit')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('EffectTime') is not None:
            self.effect_time = m.get('EffectTime')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('Fingerprint') is not None:
            self.fingerprint = m.get('Fingerprint')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('LicenseCode') is not None:
            self.license_code = m.get('LicenseCode')
        if m.get('LicenseSpecName') is not None:
            self.license_spec_name = m.get('LicenseSpecName')
        if m.get('MemoryLimit') is not None:
            self.memory_limit = m.get('MemoryLimit')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UnActivateAllDuration') is not None:
            self.un_activate_all_duration = m.get('UnActivateAllDuration')
        return self


class ActivateLicenseResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: ActivateLicenseResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        # Id of the request
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
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = ActivateLicenseResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ActivateLicenseResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ActivateLicenseResponseBody = None,
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
            temp_model = ActivateLicenseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AicsOpenApiInvokeRequest(TeaModel):
    def __init__(
        self,
        node_id: str = None,
        param: Dict[str, Any] = None,
        service_id: str = None,
        type: str = None,
    ):
        self.node_id = node_id
        self.param = param
        # This parameter is required.
        self.service_id = service_id
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.param is not None:
            result['Param'] = self.param
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('Param') is not None:
            self.param = m.get('Param')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class AicsOpenApiInvokeShrinkRequest(TeaModel):
    def __init__(
        self,
        node_id: str = None,
        param_shrink: str = None,
        service_id: str = None,
        type: str = None,
    ):
        self.node_id = node_id
        self.param_shrink = param_shrink
        # This parameter is required.
        self.service_id = service_id
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.param_shrink is not None:
            result['Param'] = self.param_shrink
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('Param') is not None:
            self.param_shrink = m.get('Param')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class AicsOpenApiInvokeResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: Any = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
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
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AicsOpenApiInvokeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AicsOpenApiInvokeResponseBody = None,
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
            temp_model = AicsOpenApiInvokeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateEssOptJobRequestElecPrice(TeaModel):
    def __init__(
        self,
        data_time: str = None,
        price: str = None,
    ):
        self.data_time = data_time
        self.price = price

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_time is not None:
            result['DataTime'] = self.data_time
        if self.price is not None:
            result['Price'] = self.price
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataTime') is not None:
            self.data_time = m.get('DataTime')
        if m.get('Price') is not None:
            self.price = m.get('Price')
        return self


class CreateEssOptJobRequestGenPrice(TeaModel):
    def __init__(
        self,
        data_time: str = None,
        price: str = None,
    ):
        self.data_time = data_time
        self.price = price

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_time is not None:
            result['DataTime'] = self.data_time
        if self.price is not None:
            result['Price'] = self.price
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataTime') is not None:
            self.data_time = m.get('DataTime')
        if m.get('Price') is not None:
            self.price = m.get('Price')
        return self


class CreateEssOptJobRequestLocation(TeaModel):
    def __init__(
        self,
        altitude: float = None,
        latitude: float = None,
        longitude: float = None,
    ):
        self.altitude = altitude
        self.latitude = latitude
        self.longitude = longitude

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.altitude is not None:
            result['Altitude'] = self.altitude
        if self.latitude is not None:
            result['Latitude'] = self.latitude
        if self.longitude is not None:
            result['Longitude'] = self.longitude
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Altitude') is not None:
            self.altitude = m.get('Altitude')
        if m.get('Latitude') is not None:
            self.latitude = m.get('Latitude')
        if m.get('Longitude') is not None:
            self.longitude = m.get('Longitude')
        return self


class CreateEssOptJobRequestSystemData(TeaModel):
    def __init__(
        self,
        history_data: List[Dict[str, Any]] = None,
        system_id: str = None,
        system_params: Dict[str, Any] = None,
        system_type: str = None,
    ):
        self.history_data = history_data
        self.system_id = system_id
        self.system_params = system_params
        self.system_type = system_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.history_data is not None:
            result['HistoryData'] = self.history_data
        if self.system_id is not None:
            result['SystemId'] = self.system_id
        if self.system_params is not None:
            result['SystemParams'] = self.system_params
        if self.system_type is not None:
            result['SystemType'] = self.system_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HistoryData') is not None:
            self.history_data = m.get('HistoryData')
        if m.get('SystemId') is not None:
            self.system_id = m.get('SystemId')
        if m.get('SystemParams') is not None:
            self.system_params = m.get('SystemParams')
        if m.get('SystemType') is not None:
            self.system_type = m.get('SystemType')
        return self


class CreateEssOptJobRequest(TeaModel):
    def __init__(
        self,
        duration: int = None,
        elec_price: List[CreateEssOptJobRequestElecPrice] = None,
        freq: str = None,
        gen_price: List[CreateEssOptJobRequestGenPrice] = None,
        location: CreateEssOptJobRequestLocation = None,
        model_version: str = None,
        run_date: str = None,
        system_data: List[CreateEssOptJobRequestSystemData] = None,
        time_zone: str = None,
        topo_type: str = None,
    ):
        self.duration = duration
        self.elec_price = elec_price
        self.freq = freq
        self.gen_price = gen_price
        self.location = location
        self.model_version = model_version
        self.run_date = run_date
        self.system_data = system_data
        self.time_zone = time_zone
        self.topo_type = topo_type

    def validate(self):
        if self.elec_price:
            for k in self.elec_price:
                if k:
                    k.validate()
        if self.gen_price:
            for k in self.gen_price:
                if k:
                    k.validate()
        if self.location:
            self.location.validate()
        if self.system_data:
            for k in self.system_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.duration is not None:
            result['Duration'] = self.duration
        result['ElecPrice'] = []
        if self.elec_price is not None:
            for k in self.elec_price:
                result['ElecPrice'].append(k.to_map() if k else None)
        if self.freq is not None:
            result['Freq'] = self.freq
        result['GenPrice'] = []
        if self.gen_price is not None:
            for k in self.gen_price:
                result['GenPrice'].append(k.to_map() if k else None)
        if self.location is not None:
            result['Location'] = self.location.to_map()
        if self.model_version is not None:
            result['ModelVersion'] = self.model_version
        if self.run_date is not None:
            result['RunDate'] = self.run_date
        result['SystemData'] = []
        if self.system_data is not None:
            for k in self.system_data:
                result['SystemData'].append(k.to_map() if k else None)
        if self.time_zone is not None:
            result['TimeZone'] = self.time_zone
        if self.topo_type is not None:
            result['TopoType'] = self.topo_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        self.elec_price = []
        if m.get('ElecPrice') is not None:
            for k in m.get('ElecPrice'):
                temp_model = CreateEssOptJobRequestElecPrice()
                self.elec_price.append(temp_model.from_map(k))
        if m.get('Freq') is not None:
            self.freq = m.get('Freq')
        self.gen_price = []
        if m.get('GenPrice') is not None:
            for k in m.get('GenPrice'):
                temp_model = CreateEssOptJobRequestGenPrice()
                self.gen_price.append(temp_model.from_map(k))
        if m.get('Location') is not None:
            temp_model = CreateEssOptJobRequestLocation()
            self.location = temp_model.from_map(m['Location'])
        if m.get('ModelVersion') is not None:
            self.model_version = m.get('ModelVersion')
        if m.get('RunDate') is not None:
            self.run_date = m.get('RunDate')
        self.system_data = []
        if m.get('SystemData') is not None:
            for k in m.get('SystemData'):
                temp_model = CreateEssOptJobRequestSystemData()
                self.system_data.append(temp_model.from_map(k))
        if m.get('TimeZone') is not None:
            self.time_zone = m.get('TimeZone')
        if m.get('TopoType') is not None:
            self.topo_type = m.get('TopoType')
        return self


class CreateEssOptJobShrinkRequest(TeaModel):
    def __init__(
        self,
        duration: int = None,
        elec_price_shrink: str = None,
        freq: str = None,
        gen_price_shrink: str = None,
        location_shrink: str = None,
        model_version: str = None,
        run_date: str = None,
        system_data_shrink: str = None,
        time_zone: str = None,
        topo_type: str = None,
    ):
        self.duration = duration
        self.elec_price_shrink = elec_price_shrink
        self.freq = freq
        self.gen_price_shrink = gen_price_shrink
        self.location_shrink = location_shrink
        self.model_version = model_version
        self.run_date = run_date
        self.system_data_shrink = system_data_shrink
        self.time_zone = time_zone
        self.topo_type = topo_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.elec_price_shrink is not None:
            result['ElecPrice'] = self.elec_price_shrink
        if self.freq is not None:
            result['Freq'] = self.freq
        if self.gen_price_shrink is not None:
            result['GenPrice'] = self.gen_price_shrink
        if self.location_shrink is not None:
            result['Location'] = self.location_shrink
        if self.model_version is not None:
            result['ModelVersion'] = self.model_version
        if self.run_date is not None:
            result['RunDate'] = self.run_date
        if self.system_data_shrink is not None:
            result['SystemData'] = self.system_data_shrink
        if self.time_zone is not None:
            result['TimeZone'] = self.time_zone
        if self.topo_type is not None:
            result['TopoType'] = self.topo_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('ElecPrice') is not None:
            self.elec_price_shrink = m.get('ElecPrice')
        if m.get('Freq') is not None:
            self.freq = m.get('Freq')
        if m.get('GenPrice') is not None:
            self.gen_price_shrink = m.get('GenPrice')
        if m.get('Location') is not None:
            self.location_shrink = m.get('Location')
        if m.get('ModelVersion') is not None:
            self.model_version = m.get('ModelVersion')
        if m.get('RunDate') is not None:
            self.run_date = m.get('RunDate')
        if m.get('SystemData') is not None:
            self.system_data_shrink = m.get('SystemData')
        if m.get('TimeZone') is not None:
            self.time_zone = m.get('TimeZone')
        if m.get('TopoType') is not None:
            self.topo_type = m.get('TopoType')
        return self


class CreateEssOptJobResponseBodyDataResponse(TeaModel):
    def __init__(
        self,
        debug_info: Any = None,
        job_type: str = None,
        result: Any = None,
    ):
        self.debug_info = debug_info
        self.job_type = job_type
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.debug_info is not None:
            result['DebugInfo'] = self.debug_info
        if self.job_type is not None:
            result['JobType'] = self.job_type
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DebugInfo') is not None:
            self.debug_info = m.get('DebugInfo')
        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class CreateEssOptJobResponseBodyData(TeaModel):
    def __init__(
        self,
        completed: bool = None,
        create_time: str = None,
        error: str = None,
        job_id: str = None,
        progress: int = None,
        response: CreateEssOptJobResponseBodyDataResponse = None,
        status: str = None,
    ):
        self.completed = completed
        self.create_time = create_time
        self.error = error
        self.job_id = job_id
        self.progress = progress
        self.response = response
        self.status = status

    def validate(self):
        if self.response:
            self.response.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.completed is not None:
            result['Completed'] = self.completed
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.error is not None:
            result['Error'] = self.error
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.response is not None:
            result['Response'] = self.response.to_map()
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Completed') is not None:
            self.completed = m.get('Completed')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Error') is not None:
            self.error = m.get('Error')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('Response') is not None:
            temp_model = CreateEssOptJobResponseBodyDataResponse()
            self.response = temp_model.from_map(m['Response'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class CreateEssOptJobResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: CreateEssOptJobResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        # Id of the request
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
        if self.message is not None:
            result['Message'] = self.message
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
            temp_model = CreateEssOptJobResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateEssOptJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateEssOptJobResponseBody = None,
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
            temp_model = CreateEssOptJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateLoadForecastJobRequestHistoryData(TeaModel):
    def __init__(
        self,
        run_time: str = None,
        value: float = None,
    ):
        self.run_time = run_time
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.run_time is not None:
            result['RunTime'] = self.run_time
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RunTime') is not None:
            self.run_time = m.get('RunTime')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateLoadForecastJobRequest(TeaModel):
    def __init__(
        self,
        device_type: str = None,
        duration: int = None,
        freq: str = None,
        history_data: List[CreateLoadForecastJobRequestHistoryData] = None,
        model_version: str = None,
        run_date: str = None,
        system_type: str = None,
        time_zone: str = None,
    ):
        self.device_type = device_type
        self.duration = duration
        self.freq = freq
        self.history_data = history_data
        self.model_version = model_version
        self.run_date = run_date
        self.system_type = system_type
        self.time_zone = time_zone

    def validate(self):
        if self.history_data:
            for k in self.history_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_type is not None:
            result['DeviceType'] = self.device_type
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.freq is not None:
            result['Freq'] = self.freq
        result['HistoryData'] = []
        if self.history_data is not None:
            for k in self.history_data:
                result['HistoryData'].append(k.to_map() if k else None)
        if self.model_version is not None:
            result['ModelVersion'] = self.model_version
        if self.run_date is not None:
            result['RunDate'] = self.run_date
        if self.system_type is not None:
            result['SystemType'] = self.system_type
        if self.time_zone is not None:
            result['TimeZone'] = self.time_zone
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceType') is not None:
            self.device_type = m.get('DeviceType')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Freq') is not None:
            self.freq = m.get('Freq')
        self.history_data = []
        if m.get('HistoryData') is not None:
            for k in m.get('HistoryData'):
                temp_model = CreateLoadForecastJobRequestHistoryData()
                self.history_data.append(temp_model.from_map(k))
        if m.get('ModelVersion') is not None:
            self.model_version = m.get('ModelVersion')
        if m.get('RunDate') is not None:
            self.run_date = m.get('RunDate')
        if m.get('SystemType') is not None:
            self.system_type = m.get('SystemType')
        if m.get('TimeZone') is not None:
            self.time_zone = m.get('TimeZone')
        return self


class CreateLoadForecastJobShrinkRequest(TeaModel):
    def __init__(
        self,
        device_type: str = None,
        duration: int = None,
        freq: str = None,
        history_data_shrink: str = None,
        model_version: str = None,
        run_date: str = None,
        system_type: str = None,
        time_zone: str = None,
    ):
        self.device_type = device_type
        self.duration = duration
        self.freq = freq
        self.history_data_shrink = history_data_shrink
        self.model_version = model_version
        self.run_date = run_date
        self.system_type = system_type
        self.time_zone = time_zone

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_type is not None:
            result['DeviceType'] = self.device_type
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.freq is not None:
            result['Freq'] = self.freq
        if self.history_data_shrink is not None:
            result['HistoryData'] = self.history_data_shrink
        if self.model_version is not None:
            result['ModelVersion'] = self.model_version
        if self.run_date is not None:
            result['RunDate'] = self.run_date
        if self.system_type is not None:
            result['SystemType'] = self.system_type
        if self.time_zone is not None:
            result['TimeZone'] = self.time_zone
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceType') is not None:
            self.device_type = m.get('DeviceType')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Freq') is not None:
            self.freq = m.get('Freq')
        if m.get('HistoryData') is not None:
            self.history_data_shrink = m.get('HistoryData')
        if m.get('ModelVersion') is not None:
            self.model_version = m.get('ModelVersion')
        if m.get('RunDate') is not None:
            self.run_date = m.get('RunDate')
        if m.get('SystemType') is not None:
            self.system_type = m.get('SystemType')
        if m.get('TimeZone') is not None:
            self.time_zone = m.get('TimeZone')
        return self


class CreateLoadForecastJobResponseBodyDataResponse(TeaModel):
    def __init__(
        self,
        debug_info: Any = None,
        job_type: str = None,
        result: Any = None,
    ):
        self.debug_info = debug_info
        self.job_type = job_type
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.debug_info is not None:
            result['DebugInfo'] = self.debug_info
        if self.job_type is not None:
            result['JobType'] = self.job_type
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DebugInfo') is not None:
            self.debug_info = m.get('DebugInfo')
        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class CreateLoadForecastJobResponseBodyData(TeaModel):
    def __init__(
        self,
        completed: bool = None,
        create_time: str = None,
        error: str = None,
        job_id: str = None,
        progress: int = None,
        response: CreateLoadForecastJobResponseBodyDataResponse = None,
        status: str = None,
    ):
        self.completed = completed
        self.create_time = create_time
        self.error = error
        self.job_id = job_id
        self.progress = progress
        self.response = response
        self.status = status

    def validate(self):
        if self.response:
            self.response.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.completed is not None:
            result['Completed'] = self.completed
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.error is not None:
            result['Error'] = self.error
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.response is not None:
            result['Response'] = self.response.to_map()
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Completed') is not None:
            self.completed = m.get('Completed')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Error') is not None:
            self.error = m.get('Error')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('Response') is not None:
            temp_model = CreateLoadForecastJobResponseBodyDataResponse()
            self.response = temp_model.from_map(m['Response'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class CreateLoadForecastJobResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: CreateLoadForecastJobResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        # Id of the request
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
        if self.message is not None:
            result['Message'] = self.message
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
            temp_model = CreateLoadForecastJobResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateLoadForecastJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateLoadForecastJobResponseBody = None,
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
            temp_model = CreateLoadForecastJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatePowerForecastJobRequestHistoryData(TeaModel):
    def __init__(
        self,
        run_time: str = None,
        value: float = None,
    ):
        self.run_time = run_time
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.run_time is not None:
            result['RunTime'] = self.run_time
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RunTime') is not None:
            self.run_time = m.get('RunTime')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreatePowerForecastJobRequestLocation(TeaModel):
    def __init__(
        self,
        altitude: float = None,
        latitude: float = None,
        longitude: float = None,
    ):
        self.altitude = altitude
        self.latitude = latitude
        self.longitude = longitude

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.altitude is not None:
            result['Altitude'] = self.altitude
        if self.latitude is not None:
            result['Latitude'] = self.latitude
        if self.longitude is not None:
            result['Longitude'] = self.longitude
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Altitude') is not None:
            self.altitude = m.get('Altitude')
        if m.get('Latitude') is not None:
            self.latitude = m.get('Latitude')
        if m.get('Longitude') is not None:
            self.longitude = m.get('Longitude')
        return self


class CreatePowerForecastJobRequest(TeaModel):
    def __init__(
        self,
        device_type: str = None,
        duration: int = None,
        freq: str = None,
        history_data: List[CreatePowerForecastJobRequestHistoryData] = None,
        location: CreatePowerForecastJobRequestLocation = None,
        model_version: str = None,
        run_date: str = None,
        system_type: str = None,
        time_zone: str = None,
    ):
        self.device_type = device_type
        self.duration = duration
        self.freq = freq
        self.history_data = history_data
        self.location = location
        self.model_version = model_version
        self.run_date = run_date
        self.system_type = system_type
        self.time_zone = time_zone

    def validate(self):
        if self.history_data:
            for k in self.history_data:
                if k:
                    k.validate()
        if self.location:
            self.location.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_type is not None:
            result['DeviceType'] = self.device_type
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.freq is not None:
            result['Freq'] = self.freq
        result['HistoryData'] = []
        if self.history_data is not None:
            for k in self.history_data:
                result['HistoryData'].append(k.to_map() if k else None)
        if self.location is not None:
            result['Location'] = self.location.to_map()
        if self.model_version is not None:
            result['ModelVersion'] = self.model_version
        if self.run_date is not None:
            result['RunDate'] = self.run_date
        if self.system_type is not None:
            result['SystemType'] = self.system_type
        if self.time_zone is not None:
            result['TimeZone'] = self.time_zone
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceType') is not None:
            self.device_type = m.get('DeviceType')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Freq') is not None:
            self.freq = m.get('Freq')
        self.history_data = []
        if m.get('HistoryData') is not None:
            for k in m.get('HistoryData'):
                temp_model = CreatePowerForecastJobRequestHistoryData()
                self.history_data.append(temp_model.from_map(k))
        if m.get('Location') is not None:
            temp_model = CreatePowerForecastJobRequestLocation()
            self.location = temp_model.from_map(m['Location'])
        if m.get('ModelVersion') is not None:
            self.model_version = m.get('ModelVersion')
        if m.get('RunDate') is not None:
            self.run_date = m.get('RunDate')
        if m.get('SystemType') is not None:
            self.system_type = m.get('SystemType')
        if m.get('TimeZone') is not None:
            self.time_zone = m.get('TimeZone')
        return self


class CreatePowerForecastJobShrinkRequest(TeaModel):
    def __init__(
        self,
        device_type: str = None,
        duration: int = None,
        freq: str = None,
        history_data_shrink: str = None,
        location_shrink: str = None,
        model_version: str = None,
        run_date: str = None,
        system_type: str = None,
        time_zone: str = None,
    ):
        self.device_type = device_type
        self.duration = duration
        self.freq = freq
        self.history_data_shrink = history_data_shrink
        self.location_shrink = location_shrink
        self.model_version = model_version
        self.run_date = run_date
        self.system_type = system_type
        self.time_zone = time_zone

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_type is not None:
            result['DeviceType'] = self.device_type
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.freq is not None:
            result['Freq'] = self.freq
        if self.history_data_shrink is not None:
            result['HistoryData'] = self.history_data_shrink
        if self.location_shrink is not None:
            result['Location'] = self.location_shrink
        if self.model_version is not None:
            result['ModelVersion'] = self.model_version
        if self.run_date is not None:
            result['RunDate'] = self.run_date
        if self.system_type is not None:
            result['SystemType'] = self.system_type
        if self.time_zone is not None:
            result['TimeZone'] = self.time_zone
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceType') is not None:
            self.device_type = m.get('DeviceType')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Freq') is not None:
            self.freq = m.get('Freq')
        if m.get('HistoryData') is not None:
            self.history_data_shrink = m.get('HistoryData')
        if m.get('Location') is not None:
            self.location_shrink = m.get('Location')
        if m.get('ModelVersion') is not None:
            self.model_version = m.get('ModelVersion')
        if m.get('RunDate') is not None:
            self.run_date = m.get('RunDate')
        if m.get('SystemType') is not None:
            self.system_type = m.get('SystemType')
        if m.get('TimeZone') is not None:
            self.time_zone = m.get('TimeZone')
        return self


class CreatePowerForecastJobResponseBodyDataResponse(TeaModel):
    def __init__(
        self,
        debug_info: Any = None,
        job_type: str = None,
        result: Any = None,
    ):
        self.debug_info = debug_info
        self.job_type = job_type
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.debug_info is not None:
            result['DebugInfo'] = self.debug_info
        if self.job_type is not None:
            result['JobType'] = self.job_type
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DebugInfo') is not None:
            self.debug_info = m.get('DebugInfo')
        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class CreatePowerForecastJobResponseBodyData(TeaModel):
    def __init__(
        self,
        completed: bool = None,
        create_time: str = None,
        error: str = None,
        job_id: str = None,
        progress: int = None,
        response: CreatePowerForecastJobResponseBodyDataResponse = None,
        status: str = None,
    ):
        self.completed = completed
        self.create_time = create_time
        self.error = error
        self.job_id = job_id
        self.progress = progress
        self.response = response
        self.status = status

    def validate(self):
        if self.response:
            self.response.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.completed is not None:
            result['Completed'] = self.completed
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.error is not None:
            result['Error'] = self.error
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.response is not None:
            result['Response'] = self.response.to_map()
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Completed') is not None:
            self.completed = m.get('Completed')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Error') is not None:
            self.error = m.get('Error')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('Response') is not None:
            temp_model = CreatePowerForecastJobResponseBodyDataResponse()
            self.response = temp_model.from_map(m['Response'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class CreatePowerForecastJobResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: CreatePowerForecastJobResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        # Id of the request
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
        if self.message is not None:
            result['Message'] = self.message
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
            temp_model = CreatePowerForecastJobResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreatePowerForecastJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreatePowerForecastJobResponseBody = None,
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
            temp_model = CreatePowerForecastJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAivppAlgoJobRequest(TeaModel):
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


class GetAivppAlgoJobResponseBodyDataResponse(TeaModel):
    def __init__(
        self,
        debug_info: Any = None,
        job_type: str = None,
        result: Any = None,
    ):
        self.debug_info = debug_info
        self.job_type = job_type
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.debug_info is not None:
            result['DebugInfo'] = self.debug_info
        if self.job_type is not None:
            result['JobType'] = self.job_type
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DebugInfo') is not None:
            self.debug_info = m.get('DebugInfo')
        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class GetAivppAlgoJobResponseBodyData(TeaModel):
    def __init__(
        self,
        completed: bool = None,
        create_time: str = None,
        error: str = None,
        job_id: str = None,
        progress: int = None,
        response: GetAivppAlgoJobResponseBodyDataResponse = None,
        status: str = None,
    ):
        self.completed = completed
        self.create_time = create_time
        self.error = error
        self.job_id = job_id
        self.progress = progress
        self.response = response
        self.status = status

    def validate(self):
        if self.response:
            self.response.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.completed is not None:
            result['Completed'] = self.completed
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.error is not None:
            result['Error'] = self.error
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.response is not None:
            result['Response'] = self.response.to_map()
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Completed') is not None:
            self.completed = m.get('Completed')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Error') is not None:
            self.error = m.get('Error')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('Response') is not None:
            temp_model = GetAivppAlgoJobResponseBodyDataResponse()
            self.response = temp_model.from_map(m['Response'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetAivppAlgoJobResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetAivppAlgoJobResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        # Id of the request
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
        if self.message is not None:
            result['Message'] = self.message
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
            temp_model = GetAivppAlgoJobResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetAivppAlgoJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAivppAlgoJobResponseBody = None,
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
            temp_model = GetAivppAlgoJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLicenseRequest(TeaModel):
    def __init__(
        self,
        id: int = None,
        instance_id: str = None,
    ):
        # ID
        self.id = id
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class GetLicenseResponseBodyDataActivateRecord(TeaModel):
    def __init__(
        self,
        activate_time: str = None,
        buy_time: str = None,
        duration: str = None,
        expire_time: str = None,
        license_code: str = None,
        order_id: str = None,
        status: str = None,
    ):
        self.activate_time = activate_time
        self.buy_time = buy_time
        self.duration = duration
        self.expire_time = expire_time
        self.license_code = license_code
        self.order_id = order_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.activate_time is not None:
            result['ActivateTime'] = self.activate_time
        if self.buy_time is not None:
            result['BuyTime'] = self.buy_time
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.license_code is not None:
            result['LicenseCode'] = self.license_code
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActivateTime') is not None:
            self.activate_time = m.get('ActivateTime')
        if m.get('BuyTime') is not None:
            self.buy_time = m.get('BuyTime')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('LicenseCode') is not None:
            self.license_code = m.get('LicenseCode')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetLicenseResponseBodyData(TeaModel):
    def __init__(
        self,
        activate_record: List[GetLicenseResponseBodyDataActivateRecord] = None,
        activate_time: str = None,
        adaptive_machine: str = None,
        all_duration: str = None,
        applicable_specs: str = None,
        buy_time: str = None,
        cpu_limit: int = None,
        description: str = None,
        duration: str = None,
        effect_time: str = None,
        expire_time: str = None,
        fingerprint: str = None,
        id: int = None,
        instance_id: str = None,
        license_code: str = None,
        license_spec_code: str = None,
        license_spec_name: str = None,
        license_spec_type: str = None,
        memory_limit: int = None,
        proposal: str = None,
        status: str = None,
        un_activate_all_duration: str = None,
    ):
        self.activate_record = activate_record
        # 代表资源一级ID的资源属性字段
        self.activate_time = activate_time
        self.adaptive_machine = adaptive_machine
        self.all_duration = all_duration
        self.applicable_specs = applicable_specs
        # 代表资源名称的资源属性字段
        self.buy_time = buy_time
        self.cpu_limit = cpu_limit
        self.description = description
        self.duration = duration
        self.effect_time = effect_time
        self.expire_time = expire_time
        # 代表创建时间的资源属性字段
        self.fingerprint = fingerprint
        # ID
        self.id = id
        self.instance_id = instance_id
        self.license_code = license_code
        self.license_spec_code = license_spec_code
        # 代表资源组的资源属性字段
        self.license_spec_name = license_spec_name
        self.license_spec_type = license_spec_type
        self.memory_limit = memory_limit
        self.proposal = proposal
        self.status = status
        self.un_activate_all_duration = un_activate_all_duration

    def validate(self):
        if self.activate_record:
            for k in self.activate_record:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ActivateRecord'] = []
        if self.activate_record is not None:
            for k in self.activate_record:
                result['ActivateRecord'].append(k.to_map() if k else None)
        if self.activate_time is not None:
            result['ActivateTime'] = self.activate_time
        if self.adaptive_machine is not None:
            result['AdaptiveMachine'] = self.adaptive_machine
        if self.all_duration is not None:
            result['AllDuration'] = self.all_duration
        if self.applicable_specs is not None:
            result['ApplicableSpecs'] = self.applicable_specs
        if self.buy_time is not None:
            result['BuyTime'] = self.buy_time
        if self.cpu_limit is not None:
            result['CpuLimit'] = self.cpu_limit
        if self.description is not None:
            result['Description'] = self.description
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.effect_time is not None:
            result['EffectTime'] = self.effect_time
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.fingerprint is not None:
            result['Fingerprint'] = self.fingerprint
        if self.id is not None:
            result['Id'] = self.id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.license_code is not None:
            result['LicenseCode'] = self.license_code
        if self.license_spec_code is not None:
            result['LicenseSpecCode'] = self.license_spec_code
        if self.license_spec_name is not None:
            result['LicenseSpecName'] = self.license_spec_name
        if self.license_spec_type is not None:
            result['LicenseSpecType'] = self.license_spec_type
        if self.memory_limit is not None:
            result['MemoryLimit'] = self.memory_limit
        if self.proposal is not None:
            result['Proposal'] = self.proposal
        if self.status is not None:
            result['Status'] = self.status
        if self.un_activate_all_duration is not None:
            result['UnActivateAllDuration'] = self.un_activate_all_duration
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.activate_record = []
        if m.get('ActivateRecord') is not None:
            for k in m.get('ActivateRecord'):
                temp_model = GetLicenseResponseBodyDataActivateRecord()
                self.activate_record.append(temp_model.from_map(k))
        if m.get('ActivateTime') is not None:
            self.activate_time = m.get('ActivateTime')
        if m.get('AdaptiveMachine') is not None:
            self.adaptive_machine = m.get('AdaptiveMachine')
        if m.get('AllDuration') is not None:
            self.all_duration = m.get('AllDuration')
        if m.get('ApplicableSpecs') is not None:
            self.applicable_specs = m.get('ApplicableSpecs')
        if m.get('BuyTime') is not None:
            self.buy_time = m.get('BuyTime')
        if m.get('CpuLimit') is not None:
            self.cpu_limit = m.get('CpuLimit')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('EffectTime') is not None:
            self.effect_time = m.get('EffectTime')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('Fingerprint') is not None:
            self.fingerprint = m.get('Fingerprint')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('LicenseCode') is not None:
            self.license_code = m.get('LicenseCode')
        if m.get('LicenseSpecCode') is not None:
            self.license_spec_code = m.get('LicenseSpecCode')
        if m.get('LicenseSpecName') is not None:
            self.license_spec_name = m.get('LicenseSpecName')
        if m.get('LicenseSpecType') is not None:
            self.license_spec_type = m.get('LicenseSpecType')
        if m.get('MemoryLimit') is not None:
            self.memory_limit = m.get('MemoryLimit')
        if m.get('Proposal') is not None:
            self.proposal = m.get('Proposal')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UnActivateAllDuration') is not None:
            self.un_activate_all_duration = m.get('UnActivateAllDuration')
        return self


class GetLicenseResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: GetLicenseResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
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
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetLicenseResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetLicenseResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetLicenseResponseBody = None,
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
            temp_model = GetLicenseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAivppResourcesRequest(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        max_results: int = None,
    ):
        self.current_page = current_page
        self.max_results = max_results

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        return self


class ListAivppResourcesResponseBodyData(TeaModel):
    def __init__(
        self,
        detail: str = None,
        expire_time: str = None,
        instance_id: str = None,
        instance_type: str = None,
        left_quantity: str = None,
        order_id: str = None,
        quantity: str = None,
        specification: str = None,
        start_time: str = None,
        status: str = None,
        user_id: str = None,
    ):
        self.detail = detail
        self.expire_time = expire_time
        self.instance_id = instance_id
        self.instance_type = instance_type
        self.left_quantity = left_quantity
        self.order_id = order_id
        self.quantity = quantity
        self.specification = specification
        self.start_time = start_time
        self.status = status
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.detail is not None:
            result['Detail'] = self.detail
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.left_quantity is not None:
            result['LeftQuantity'] = self.left_quantity
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.quantity is not None:
            result['Quantity'] = self.quantity
        if self.specification is not None:
            result['Specification'] = self.specification
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Detail') is not None:
            self.detail = m.get('Detail')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('LeftQuantity') is not None:
            self.left_quantity = m.get('LeftQuantity')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')
        if m.get('Specification') is not None:
            self.specification = m.get('Specification')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class ListAivppResourcesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[ListAivppResourcesResponseBodyData] = None,
        max_results: int = None,
        message: str = None,
        next_token: str = None,
        request_id: str = None,
        success: str = None,
        total_count: int = None,
    ):
        self.code = code
        self.data = data
        self.max_results = max_results
        self.message = message
        self.next_token = next_token
        # Id of the request
        self.request_id = request_id
        self.success = success
        self.total_count = total_count

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
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.message is not None:
            result['Message'] = self.message
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListAivppResourcesResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListAivppResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAivppResourcesResponseBody = None,
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
            temp_model = ListAivppResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListLicensesRequest(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        query_str: str = None,
    ):
        self.current_page = current_page
        self.page_size = page_size
        self.query_str = query_str

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.query_str is not None:
            result['QueryStr'] = self.query_str
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('QueryStr') is not None:
            self.query_str = m.get('QueryStr')
        return self


class ListLicensesResponseBodyLicenseList(TeaModel):
    def __init__(
        self,
        activate_time: str = None,
        adaptive_machine: int = None,
        all_duration: str = None,
        buy_time: str = None,
        cpu_limit: int = None,
        description: str = None,
        duration: str = None,
        effect_time: str = None,
        expire_time: str = None,
        id: str = None,
        instance_id: str = None,
        license_spec_code: str = None,
        license_spec_name: str = None,
        license_spec_type: str = None,
        memory_limit: int = None,
        status: str = None,
        un_activate_all_duration: str = None,
    ):
        self.activate_time = activate_time
        self.adaptive_machine = adaptive_machine
        self.all_duration = all_duration
        self.buy_time = buy_time
        self.cpu_limit = cpu_limit
        self.description = description
        self.duration = duration
        self.effect_time = effect_time
        self.expire_time = expire_time
        self.id = id
        self.instance_id = instance_id
        self.license_spec_code = license_spec_code
        self.license_spec_name = license_spec_name
        self.license_spec_type = license_spec_type
        self.memory_limit = memory_limit
        self.status = status
        self.un_activate_all_duration = un_activate_all_duration

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.activate_time is not None:
            result['ActivateTime'] = self.activate_time
        if self.adaptive_machine is not None:
            result['AdaptiveMachine'] = self.adaptive_machine
        if self.all_duration is not None:
            result['AllDuration'] = self.all_duration
        if self.buy_time is not None:
            result['BuyTime'] = self.buy_time
        if self.cpu_limit is not None:
            result['CpuLimit'] = self.cpu_limit
        if self.description is not None:
            result['Description'] = self.description
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.effect_time is not None:
            result['EffectTime'] = self.effect_time
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.id is not None:
            result['Id'] = self.id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.license_spec_code is not None:
            result['LicenseSpecCode'] = self.license_spec_code
        if self.license_spec_name is not None:
            result['LicenseSpecName'] = self.license_spec_name
        if self.license_spec_type is not None:
            result['LicenseSpecType'] = self.license_spec_type
        if self.memory_limit is not None:
            result['MemoryLimit'] = self.memory_limit
        if self.status is not None:
            result['Status'] = self.status
        if self.un_activate_all_duration is not None:
            result['UnActivateAllDuration'] = self.un_activate_all_duration
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActivateTime') is not None:
            self.activate_time = m.get('ActivateTime')
        if m.get('AdaptiveMachine') is not None:
            self.adaptive_machine = m.get('AdaptiveMachine')
        if m.get('AllDuration') is not None:
            self.all_duration = m.get('AllDuration')
        if m.get('BuyTime') is not None:
            self.buy_time = m.get('BuyTime')
        if m.get('CpuLimit') is not None:
            self.cpu_limit = m.get('CpuLimit')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('EffectTime') is not None:
            self.effect_time = m.get('EffectTime')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('LicenseSpecCode') is not None:
            self.license_spec_code = m.get('LicenseSpecCode')
        if m.get('LicenseSpecName') is not None:
            self.license_spec_name = m.get('LicenseSpecName')
        if m.get('LicenseSpecType') is not None:
            self.license_spec_type = m.get('LicenseSpecType')
        if m.get('MemoryLimit') is not None:
            self.memory_limit = m.get('MemoryLimit')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UnActivateAllDuration') is not None:
            self.un_activate_all_duration = m.get('UnActivateAllDuration')
        return self


class ListLicensesResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        current_page: int = None,
        http_status_code: int = None,
        license_list: List[ListLicensesResponseBodyLicenseList] = None,
        message: str = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
        total_page: str = None,
        total_page_count: str = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.current_page = current_page
        self.http_status_code = http_status_code
        self.license_list = license_list
        self.message = message
        self.page_size = page_size
        self.request_id = request_id
        self.success = success
        self.total_count = total_count
        self.total_page = total_page
        self.total_page_count = total_page_count

    def validate(self):
        if self.license_list:
            for k in self.license_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        result['LicenseList'] = []
        if self.license_list is not None:
            for k in self.license_list:
                result['LicenseList'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.total_page is not None:
            result['TotalPage'] = self.total_page
        if self.total_page_count is not None:
            result['TotalPageCount'] = self.total_page_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        self.license_list = []
        if m.get('LicenseList') is not None:
            for k in m.get('LicenseList'):
                temp_model = ListLicensesResponseBodyLicenseList()
                self.license_list.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')
        if m.get('TotalPageCount') is not None:
            self.total_page_count = m.get('TotalPageCount')
        return self


class ListLicensesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListLicensesResponseBody = None,
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
            temp_model = ListLicensesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUserResourcesRequest(TeaModel):
    def __init__(
        self,
        commodity_code: str = None,
    ):
        self.commodity_code = commodity_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        return self


class ListUserResourcesResponseBodyData(TeaModel):
    def __init__(
        self,
        charge_type: str = None,
        commodity_code: str = None,
        end_date: str = None,
        instance_id: str = None,
        region: str = None,
        start_date: str = None,
        status: str = None,
        status_msg: str = None,
    ):
        self.charge_type = charge_type
        self.commodity_code = commodity_code
        self.end_date = end_date
        self.instance_id = instance_id
        self.region = region
        self.start_date = start_date
        self.status = status
        self.status_msg = status_msg

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.charge_type is not None:
            result['chargeType'] = self.charge_type
        if self.commodity_code is not None:
            result['commodityCode'] = self.commodity_code
        if self.end_date is not None:
            result['endDate'] = self.end_date
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.region is not None:
            result['region'] = self.region
        if self.start_date is not None:
            result['startDate'] = self.start_date
        if self.status is not None:
            result['status'] = self.status
        if self.status_msg is not None:
            result['statusMsg'] = self.status_msg
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('chargeType') is not None:
            self.charge_type = m.get('chargeType')
        if m.get('commodityCode') is not None:
            self.commodity_code = m.get('commodityCode')
        if m.get('endDate') is not None:
            self.end_date = m.get('endDate')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('startDate') is not None:
            self.start_date = m.get('startDate')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('statusMsg') is not None:
            self.status_msg = m.get('statusMsg')
        return self


class ListUserResourcesResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: List[ListUserResourcesResponseBodyData] = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        # Id of the request
        self.request_id = request_id
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
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListUserResourcesResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListUserResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListUserResourcesResponseBody = None,
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
            temp_model = ListUserResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateLicenseDescriptionRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        instance_id: str = None,
    ):
        self.description = description
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class UpdateLicenseDescriptionResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateLicenseDescriptionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateLicenseDescriptionResponseBody = None,
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
            temp_model = UpdateLicenseDescriptionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


