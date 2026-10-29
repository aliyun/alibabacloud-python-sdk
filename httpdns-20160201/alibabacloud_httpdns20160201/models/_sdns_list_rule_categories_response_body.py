# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_httpdns20160201 import models as main_models
from darabonba.model import DaraModel

class SdnsListRuleCategoriesResponseBody(DaraModel):
    def __init__(
        self,
        list: List[main_models.SdnsListRuleCategoriesResponseBodyList] = None,
        request_id: str = None,
    ):
        # The list of all custom resolution policies for the domain name, including LINE and IP_RANGE policies, as well as enabled and disabled policies. The order of the list is not guaranteed.
        self.list = list
        # The ID of the request, which is used to troubleshoot call issues and is not the policy ID.
        self.request_id = request_id

    def validate(self):
        if self.list:
            for v1 in self.list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['List'] = []
        if self.list is not None:
            for k1 in self.list:
                result['List'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k1 in m.get('List'):
                temp_model = main_models.SdnsListRuleCategoriesResponseBodyList()
                self.list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class SdnsListRuleCategoriesResponseBodyList(DaraModel):
    def __init__(
        self,
        client_ip_ranges: List[str] = None,
        domain_name: str = None,
        id: str = None,
        match_type: str = None,
        record_line: main_models.SdnsListRuleCategoriesResponseBodyListRecordLine = None,
        region: main_models.SdnsListRuleCategoriesResponseBodyListRegion = None,
        rules: List[main_models.SdnsListRuleCategoriesResponseBodyListRules] = None,
        status: int = None,
    ):
        # The array of original CIDR blocks from the most recent successful submission for an IP_RANGE policy. The order, duplicates, and content of each string are preserved. The response is a JSON array, not a text string of an array. This field is not used for LINE policies.
        self.client_ip_ranges = client_ip_ranges
        # The domain name to which the policy is bound.
        self.domain_name = domain_name
        # The ID of the policy, which can be used to query, update, enable, disable, or delete the policy. Treat it as a string to avoid precision loss of large integers.
        self.id = id
        # The match type of the policy. Valid values: LINE: line policy. IP_RANGE: client CIDR block policy.
        self.match_type = match_type
        # The line display information for a LINE policy. This field can be empty or omitted for an IP_RANGE policy.
        self.record_line = record_line
        # The line and region display information for compatibility with existing clients. This field applies only to LINE policies and can be empty or omitted for IP_RANGE policies.
        self.region = region
        # The list of custom resolution rules included in the policy. If multiple rules have no parameter conditions, only the first rule is prioritized. Multiple return addresses should be configured in a single rule.
        self.rules = rules
        # The status of the policy. Valid values: 0: disabled. 1: enabled. After a policy is enabled, actual resolution requires waiting for configuration propagation.
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
            temp_model = main_models.SdnsListRuleCategoriesResponseBodyListRecordLine()
            self.record_line = temp_model.from_map(m.get('RecordLine'))

        if m.get('Region') is not None:
            temp_model = main_models.SdnsListRuleCategoriesResponseBodyListRegion()
            self.region = temp_model.from_map(m.get('Region'))

        self.rules = []
        if m.get('Rules') is not None:
            for k1 in m.get('Rules'):
                temp_model = main_models.SdnsListRuleCategoriesResponseBodyListRules()
                self.rules.append(temp_model.from_map(k1))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class SdnsListRuleCategoriesResponseBodyListRules(DaraModel):
    def __init__(
        self,
        arg_keys: List[str] = None,
        args: Dict[str, str] = None,
        name: str = None,
        records: List[main_models.SdnsListRuleCategoriesResponseBodyListRulesRecords] = None,
        result_mode: int = None,
        ttl: int = None,
    ):
        # The names and display order of custom parameters. This field can be empty if no custom parameters are used.
        self.arg_keys = arg_keys
        # The custom parameter matching conditions attached to the rule. If not configured, no parameter restrictions are applied.
        self.args = args
        # The name of the rule, which is used to identify the rule and cannot replace the policy ID.
        self.name = name
        # The list of configured DNS records, which can include A and AAAA records. Actual resolution returns only records of the queried type. If the list is empty or contains no records of the queried type, the system continues to fall back.
        self.records = records
        # The record return mode. Valid values: 0: returns all records of the queried type. 1: returns one record of the queried type based on weight.
        self.result_mode = result_mode
        # The cache validity period of the record, in seconds. This value must be a positive integer.
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
                temp_model = main_models.SdnsListRuleCategoriesResponseBodyListRulesRecords()
                self.records.append(temp_model.from_map(k1))

        if m.get('ResultMode') is not None:
            self.result_mode = m.get('ResultMode')

        if m.get('Ttl') is not None:
            self.ttl = m.get('Ttl')

        return self

class SdnsListRuleCategoriesResponseBodyListRulesRecords(DaraModel):
    def __init__(
        self,
        ip: str = None,
        type: int = None,
        type_label: str = None,
        weight: int = None,
    ):
        # The single destination IP address corresponding to the record. When Type is 1, it is an IPv4 address, such as 192.0.2.200. When Type is 28, it is an IPv6 address, such as 2001:db8::200. CIDR blocks, IP ranges, or domain names are not used.
        self.ip = ip
        # The DNS record type. Valid values: 1: A record. 28: AAAA record. Enter an integer instead of the string A or AAAA.
        self.type = type
        # The auxiliary display text for the record type, which is not used for matching or resolution decisions. This field can be omitted in requests.
        self.type_label = type_label
        # The relative weight of the record, which is used to select one record of the same query type only when ResultMode is 1. Set this to a positive integer from 1 to 100. The sum of the weights of all records does not need to be 100. This field is not used for selection when ResultMode is 0.
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

class SdnsListRuleCategoriesResponseBodyListRegion(DaraModel):
    def __init__(
        self,
        area: main_models.SdnsListRuleCategoriesResponseBodyListRegionArea = None,
        city: main_models.SdnsListRuleCategoriesResponseBodyListRegionCity = None,
        continent: main_models.SdnsListRuleCategoriesResponseBodyListRegionContinent = None,
        country: main_models.SdnsListRuleCategoriesResponseBodyListRegionCountry = None,
        isp: main_models.SdnsListRuleCategoriesResponseBodyListRegionIsp = None,
        province: main_models.SdnsListRuleCategoriesResponseBodyListRegionProvince = None,
    ):
        # The code and display name of the region.
        self.area = area
        # The code and display name of the city. This is a reserved field for compatibility. City-level granularity is not currently provided.
        self.city = city
        # The code and display name of the continent.
        self.continent = continent
        # The code and display name of the country or region.
        self.country = country
        # The code and display name of the ISP.
        self.isp = isp
        # The code and display name of the province.
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
            temp_model = main_models.SdnsListRuleCategoriesResponseBodyListRegionArea()
            self.area = temp_model.from_map(m.get('Area'))

        if m.get('City') is not None:
            temp_model = main_models.SdnsListRuleCategoriesResponseBodyListRegionCity()
            self.city = temp_model.from_map(m.get('City'))

        if m.get('Continent') is not None:
            temp_model = main_models.SdnsListRuleCategoriesResponseBodyListRegionContinent()
            self.continent = temp_model.from_map(m.get('Continent'))

        if m.get('Country') is not None:
            temp_model = main_models.SdnsListRuleCategoriesResponseBodyListRegionCountry()
            self.country = temp_model.from_map(m.get('Country'))

        if m.get('Isp') is not None:
            temp_model = main_models.SdnsListRuleCategoriesResponseBodyListRegionIsp()
            self.isp = temp_model.from_map(m.get('Isp'))

        if m.get('Province') is not None:
            temp_model = main_models.SdnsListRuleCategoriesResponseBodyListRegionProvince()
            self.province = temp_model.from_map(m.get('Province'))

        return self

class SdnsListRuleCategoriesResponseBodyListRegionProvince(DaraModel):
    def __init__(
        self,
        id: str = None,
        label: str = None,
    ):
        # The code of the province. The value x indicates the default item.
        self.id = id
        # The display name of the province. An empty string can be returned for the default item.
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

class SdnsListRuleCategoriesResponseBodyListRegionIsp(DaraModel):
    def __init__(
        self,
        id: str = None,
        label: str = None,
    ):
        # The code of the ISP. The value x indicates the default item.
        self.id = id
        # The display name of the ISP. An empty string can be returned for the default item.
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

class SdnsListRuleCategoriesResponseBodyListRegionCountry(DaraModel):
    def __init__(
        self,
        id: str = None,
        label: str = None,
    ):
        # The code of the country or region. The value x indicates the default item.
        self.id = id
        # The display name of the country or region. An empty string can be returned for the default item.
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

class SdnsListRuleCategoriesResponseBodyListRegionContinent(DaraModel):
    def __init__(
        self,
        id: str = None,
        label: str = None,
    ):
        # The code of the continent. The value x indicates the default item.
        self.id = id
        # The display name of the continent. An empty string can be returned for the default item.
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

class SdnsListRuleCategoriesResponseBodyListRegionCity(DaraModel):
    def __init__(
        self,
        id: str = None,
        label: str = None,
    ):
        # The code of the city. This is a reserved field for compatibility. The default value is x, which indicates that no city is specified. The example uses the JSON string literal "x", where the double quotes are not part of the actual field content.
        self.id = id
        # The display name of the city. This is a reserved field for compatibility, and an empty string is returned. The example uses the JSON literal "" to represent an empty string, where the double quotes are not part of the actual field content.
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

class SdnsListRuleCategoriesResponseBodyListRegionArea(DaraModel):
    def __init__(
        self,
        id: str = None,
        label: str = None,
    ):
        # The code of the region. The value x indicates the default item.
        self.id = id
        # The display name of the region. An empty string can be returned for the default item.
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

class SdnsListRuleCategoriesResponseBodyListRecordLine(DaraModel):
    def __init__(
        self,
        line_id: str = None,
        line_label: str = None,
        paths: List[main_models.SdnsListRuleCategoriesResponseBodyListRecordLinePaths] = None,
    ):
        # The line identifier. Valid values: internal: the Chinese mainland. overseas: outside the Chinese mainland.
        self.line_id = line_id
        # The display name of the line.
        self.line_label = line_label
        # The line selection path, which describes the line conditions at each level. This field applies only to LINE policies. IP_RANGE policies do not use line paths.
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
                temp_model = main_models.SdnsListRuleCategoriesResponseBodyListRecordLinePaths()
                self.paths.append(temp_model.from_map(k1))

        return self

class SdnsListRuleCategoriesResponseBodyListRecordLinePaths(DaraModel):
    def __init__(
        self,
        id: str = None,
        key: str = None,
        label: str = None,
        level: int = None,
    ):
        # The code of the option at this level. For example, chinanet at the isps level indicates China Telecom. Use valid options for the associated line and maintain consistent hierarchical relationships.
        self.id = id
        # The level identifier. For the Chinese mainland, valid values are isps, subRegions, and provinces. For regions outside the Chinese mainland, valid values are continents and geoRegions. This corresponds to the Level field.
        self.key = key
        # The display name of the line option. The display name of the default option can be empty.
        self.label = label
        # The sequence number of the line level. For the Chinese mainland, the values are 1 (ISP), 2 (region), and 3 (province). For regions outside the Chinese mainland, the values are 1 (continent) and 2 (geographical region).
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

