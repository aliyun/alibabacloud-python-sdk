# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_httpdns20160201 import models as main_models
from darabonba.model import DaraModel

class SdnsGetRuleCategoryResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.SdnsGetRuleCategoryResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.SdnsGetRuleCategoryResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class SdnsGetRuleCategoryResponseBodyData(DaraModel):
    def __init__(
        self,
        client_ip_ranges: List[str] = None,
        domain_name: str = None,
        id: str = None,
        match_type: str = None,
        record_line: main_models.SdnsGetRuleCategoryResponseBodyDataRecordLine = None,
        region: main_models.SdnsGetRuleCategoryResponseBodyDataRegion = None,
        rules: List[main_models.SdnsGetRuleCategoryResponseBodyDataRules] = None,
        status: int = None,
    ):
        self.client_ip_ranges = client_ip_ranges
        self.domain_name = domain_name
        self.id = id
        self.match_type = match_type
        self.record_line = record_line
        self.region = region
        self.rules = rules
        self.status = status

    def validate(self):
        if self.record_line:
            self.record_line.validate()
        if self.region:
            self.region.validate()
        if self.rules:
            for v1 in self.rules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_ip_ranges is not None:
            result['ClientIpRanges'] = self.client_ip_ranges

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.id is not None:
            result['Id'] = self.id

        if self.match_type is not None:
            result['MatchType'] = self.match_type

        if self.record_line is not None:
            result['RecordLine'] = self.record_line.to_map()

        if self.region is not None:
            result['Region'] = self.region.to_map()

        result['Rules'] = []
        if self.rules is not None:
            for k1 in self.rules:
                result['Rules'].append(k1.to_map() if k1 else None)

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientIpRanges') is not None:
            self.client_ip_ranges = m.get('ClientIpRanges')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('MatchType') is not None:
            self.match_type = m.get('MatchType')

        if m.get('RecordLine') is not None:
            temp_model = main_models.SdnsGetRuleCategoryResponseBodyDataRecordLine()
            self.record_line = temp_model.from_map(m.get('RecordLine'))

        if m.get('Region') is not None:
            temp_model = main_models.SdnsGetRuleCategoryResponseBodyDataRegion()
            self.region = temp_model.from_map(m.get('Region'))

        self.rules = []
        if m.get('Rules') is not None:
            for k1 in m.get('Rules'):
                temp_model = main_models.SdnsGetRuleCategoryResponseBodyDataRules()
                self.rules.append(temp_model.from_map(k1))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class SdnsGetRuleCategoryResponseBodyDataRules(DaraModel):
    def __init__(
        self,
        arg_keys: List[str] = None,
        args: Dict[str, str] = None,
        name: str = None,
        records: List[main_models.SdnsGetRuleCategoryResponseBodyDataRulesRecords] = None,
        result_mode: int = None,
        ttl: int = None,
    ):
        self.arg_keys = arg_keys
        self.args = args
        self.name = name
        self.records = records
        self.result_mode = result_mode
        self.ttl = ttl

    def validate(self):
        if self.records:
            for v1 in self.records:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.arg_keys is not None:
            result['ArgKeys'] = self.arg_keys

        if self.args is not None:
            result['Args'] = self.args

        if self.name is not None:
            result['Name'] = self.name

        result['Records'] = []
        if self.records is not None:
            for k1 in self.records:
                result['Records'].append(k1.to_map() if k1 else None)

        if self.result_mode is not None:
            result['ResultMode'] = self.result_mode

        if self.ttl is not None:
            result['Ttl'] = self.ttl

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArgKeys') is not None:
            self.arg_keys = m.get('ArgKeys')

        if m.get('Args') is not None:
            self.args = m.get('Args')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        self.records = []
        if m.get('Records') is not None:
            for k1 in m.get('Records'):
                temp_model = main_models.SdnsGetRuleCategoryResponseBodyDataRulesRecords()
                self.records.append(temp_model.from_map(k1))

        if m.get('ResultMode') is not None:
            self.result_mode = m.get('ResultMode')

        if m.get('Ttl') is not None:
            self.ttl = m.get('Ttl')

        return self

class SdnsGetRuleCategoryResponseBodyDataRulesRecords(DaraModel):
    def __init__(
        self,
        ip: str = None,
        type: int = None,
        type_label: str = None,
        weight: int = None,
    ):
        self.ip = ip
        self.type = type
        self.type_label = type_label
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ip is not None:
            result['Ip'] = self.ip

        if self.type is not None:
            result['Type'] = self.type

        if self.type_label is not None:
            result['TypeLabel'] = self.type_label

        if self.weight is not None:
            result['Weight'] = self.weight

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('TypeLabel') is not None:
            self.type_label = m.get('TypeLabel')

        if m.get('Weight') is not None:
            self.weight = m.get('Weight')

        return self

class SdnsGetRuleCategoryResponseBodyDataRegion(DaraModel):
    def __init__(
        self,
        area: main_models.SdnsGetRuleCategoryResponseBodyDataRegionArea = None,
        city: main_models.SdnsGetRuleCategoryResponseBodyDataRegionCity = None,
        continent: main_models.SdnsGetRuleCategoryResponseBodyDataRegionContinent = None,
        country: main_models.SdnsGetRuleCategoryResponseBodyDataRegionCountry = None,
        isp: main_models.SdnsGetRuleCategoryResponseBodyDataRegionIsp = None,
        province: main_models.SdnsGetRuleCategoryResponseBodyDataRegionProvince = None,
    ):
        self.area = area
        self.city = city
        self.continent = continent
        self.country = country
        self.isp = isp
        self.province = province

    def validate(self):
        if self.area:
            self.area.validate()
        if self.city:
            self.city.validate()
        if self.continent:
            self.continent.validate()
        if self.country:
            self.country.validate()
        if self.isp:
            self.isp.validate()
        if self.province:
            self.province.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.area is not None:
            result['Area'] = self.area.to_map()

        if self.city is not None:
            result['City'] = self.city.to_map()

        if self.continent is not None:
            result['Continent'] = self.continent.to_map()

        if self.country is not None:
            result['Country'] = self.country.to_map()

        if self.isp is not None:
            result['Isp'] = self.isp.to_map()

        if self.province is not None:
            result['Province'] = self.province.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Area') is not None:
            temp_model = main_models.SdnsGetRuleCategoryResponseBodyDataRegionArea()
            self.area = temp_model.from_map(m.get('Area'))

        if m.get('City') is not None:
            temp_model = main_models.SdnsGetRuleCategoryResponseBodyDataRegionCity()
            self.city = temp_model.from_map(m.get('City'))

        if m.get('Continent') is not None:
            temp_model = main_models.SdnsGetRuleCategoryResponseBodyDataRegionContinent()
            self.continent = temp_model.from_map(m.get('Continent'))

        if m.get('Country') is not None:
            temp_model = main_models.SdnsGetRuleCategoryResponseBodyDataRegionCountry()
            self.country = temp_model.from_map(m.get('Country'))

        if m.get('Isp') is not None:
            temp_model = main_models.SdnsGetRuleCategoryResponseBodyDataRegionIsp()
            self.isp = temp_model.from_map(m.get('Isp'))

        if m.get('Province') is not None:
            temp_model = main_models.SdnsGetRuleCategoryResponseBodyDataRegionProvince()
            self.province = temp_model.from_map(m.get('Province'))

        return self

class SdnsGetRuleCategoryResponseBodyDataRegionProvince(DaraModel):
    def __init__(
        self,
        id: str = None,
        label: str = None,
    ):
        self.id = id
        self.label = label

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.label is not None:
            result['Label'] = self.label

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Label') is not None:
            self.label = m.get('Label')

        return self

class SdnsGetRuleCategoryResponseBodyDataRegionIsp(DaraModel):
    def __init__(
        self,
        id: str = None,
        label: str = None,
    ):
        self.id = id
        self.label = label

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.label is not None:
            result['Label'] = self.label

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Label') is not None:
            self.label = m.get('Label')

        return self

class SdnsGetRuleCategoryResponseBodyDataRegionCountry(DaraModel):
    def __init__(
        self,
        id: str = None,
        label: str = None,
    ):
        self.id = id
        self.label = label

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.label is not None:
            result['Label'] = self.label

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Label') is not None:
            self.label = m.get('Label')

        return self

class SdnsGetRuleCategoryResponseBodyDataRegionContinent(DaraModel):
    def __init__(
        self,
        id: str = None,
        label: str = None,
    ):
        self.id = id
        self.label = label

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.label is not None:
            result['Label'] = self.label

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Label') is not None:
            self.label = m.get('Label')

        return self

class SdnsGetRuleCategoryResponseBodyDataRegionCity(DaraModel):
    def __init__(
        self,
        id: str = None,
        label: str = None,
    ):
        self.id = id
        self.label = label

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.label is not None:
            result['Label'] = self.label

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Label') is not None:
            self.label = m.get('Label')

        return self

class SdnsGetRuleCategoryResponseBodyDataRegionArea(DaraModel):
    def __init__(
        self,
        id: str = None,
        label: str = None,
    ):
        self.id = id
        self.label = label

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.label is not None:
            result['Label'] = self.label

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Label') is not None:
            self.label = m.get('Label')

        return self

class SdnsGetRuleCategoryResponseBodyDataRecordLine(DaraModel):
    def __init__(
        self,
        line_id: str = None,
        line_label: str = None,
        paths: List[main_models.SdnsGetRuleCategoryResponseBodyDataRecordLinePaths] = None,
    ):
        self.line_id = line_id
        self.line_label = line_label
        self.paths = paths

    def validate(self):
        if self.paths:
            for v1 in self.paths:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.line_id is not None:
            result['LineId'] = self.line_id

        if self.line_label is not None:
            result['LineLabel'] = self.line_label

        result['Paths'] = []
        if self.paths is not None:
            for k1 in self.paths:
                result['Paths'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LineId') is not None:
            self.line_id = m.get('LineId')

        if m.get('LineLabel') is not None:
            self.line_label = m.get('LineLabel')

        self.paths = []
        if m.get('Paths') is not None:
            for k1 in m.get('Paths'):
                temp_model = main_models.SdnsGetRuleCategoryResponseBodyDataRecordLinePaths()
                self.paths.append(temp_model.from_map(k1))

        return self

class SdnsGetRuleCategoryResponseBodyDataRecordLinePaths(DaraModel):
    def __init__(
        self,
        id: str = None,
        key: str = None,
        label: str = None,
        level: int = None,
    ):
        self.id = id
        self.key = key
        self.label = label
        self.level = level

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.key is not None:
            result['Key'] = self.key

        if self.label is not None:
            result['Label'] = self.label

        if self.level is not None:
            result['Level'] = self.level

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Label') is not None:
            self.label = m.get('Label')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        return self

