# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict


class NlpAddressNormalizationRequest(TeaModel):
    def __init__(
        self,
        city_std_manual: str = None,
        city_str: str = None,
        client_token: str = None,
        district_std_manual: str = None,
        instance_id: str = None,
        province_std_manual: str = None,
        province_str: str = None,
        query_str: str = None,
    ):
        self.city_std_manual = city_std_manual
        self.city_str = city_str
        self.client_token = client_token
        self.district_std_manual = district_std_manual
        self.instance_id = instance_id
        self.province_std_manual = province_std_manual
        self.province_str = province_str
        self.query_str = query_str

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.city_std_manual is not None:
            result['CityStdManual'] = self.city_std_manual
        if self.city_str is not None:
            result['CityStr'] = self.city_str
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.district_std_manual is not None:
            result['DistrictStdManual'] = self.district_std_manual
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.province_std_manual is not None:
            result['ProvinceStdManual'] = self.province_std_manual
        if self.province_str is not None:
            result['ProvinceStr'] = self.province_str
        if self.query_str is not None:
            result['QueryStr'] = self.query_str
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CityStdManual') is not None:
            self.city_std_manual = m.get('CityStdManual')
        if m.get('CityStr') is not None:
            self.city_str = m.get('CityStr')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DistrictStdManual') is not None:
            self.district_std_manual = m.get('DistrictStdManual')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ProvinceStdManual') is not None:
            self.province_std_manual = m.get('ProvinceStdManual')
        if m.get('ProvinceStr') is not None:
            self.province_str = m.get('ProvinceStr')
        if m.get('QueryStr') is not None:
            self.query_str = m.get('QueryStr')
        return self


class NlpAddressNormalizationResponseBodyData(TeaModel):
    def __init__(
        self,
        city_std: str = None,
        district_std: str = None,
        province_std: str = None,
        results: List[str] = None,
        status_es: str = None,
    ):
        self.city_std = city_std
        self.district_std = district_std
        self.province_std = province_std
        self.results = results
        self.status_es = status_es

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.city_std is not None:
            result['CityStd'] = self.city_std
        if self.district_std is not None:
            result['DistrictStd'] = self.district_std
        if self.province_std is not None:
            result['ProvinceStd'] = self.province_std
        if self.results is not None:
            result['Results'] = self.results
        if self.status_es is not None:
            result['StatusEs'] = self.status_es
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CityStd') is not None:
            self.city_std = m.get('CityStd')
        if m.get('DistrictStd') is not None:
            self.district_std = m.get('DistrictStd')
        if m.get('ProvinceStd') is not None:
            self.province_std = m.get('ProvinceStd')
        if m.get('Results') is not None:
            self.results = m.get('Results')
        if m.get('StatusEs') is not None:
            self.status_es = m.get('StatusEs')
        return self


class NlpAddressNormalizationResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: NlpAddressNormalizationResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        result: str = None,
        success: bool = None,
        timestamp: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.result = result
        self.success = success
        self.timestamp = timestamp

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
        if self.result is not None:
            result['Result'] = self.result
        if self.success is not None:
            result['Success'] = self.success
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = NlpAddressNormalizationResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        return self


class NlpAddressNormalizationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: NlpAddressNormalizationResponseBody = None,
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
            temp_model = NlpAddressNormalizationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


