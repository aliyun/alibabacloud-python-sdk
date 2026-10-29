# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_httpdns20160201 import models as main_models
from darabonba.model import DaraModel

class CreateSdnsRuleCategoryRequest(DaraModel):
    def __init__(
        self,
        client_ip_ranges: List[str] = None,
        domain_name: str = None,
        enable: bool = None,
        line_id: str = None,
        match_type: str = None,
        paths: List[main_models.CreateSdnsRuleCategoryRequestPaths] = None,
        rules: List[main_models.CreateSdnsRuleCategoryRequestRules] = None,
    ):
        # The array of client IP address ranges required for the IP_RANGE pattern. Send this parameter as a JSON form field. Do not specify this parameter for the LINE pattern. This parameter supports single IPv4 and IPv6 addresses, CIDR blocks, and start-end ranges. Multiple entries have an OR relationship. For CIDR blocks, the IPv4 prefix length ranges from 0 to 32, and the IPv6 prefix length ranges from 0 to 128. Start-end ranges are inclusive and must belong to the same address family, and the start address cannot be greater than the end address. Duplicates, inclusions, and overlaps are allowed within the same policy. When the policy is saved and read back, the array sequence, duplicates, and original text of each string are preserved. The array can contain up to 2,000 array elements. The total number of parsed non-empty address expressions ranges from 1 to 2,000, and duplicates are counted. We recommend that you specify one expression per array element. It is compatible with line breaks within an array element. Each expression can contain up to 128 characters, including leading and trailing spaces. The serialized UTF-8 JSON content cannot exceed 65,535 bytes. The quantity and byte limits take effect simultaneously. Overlaps are not allowed between different IP_RANGE policies for the same account, domain name, and address family. Disabled policies are also checked. Disabling a policy does not release the ranges. This limit does not compare independent configurations of LINE policies and the legacy SetIPRegionResult operation.
        self.client_ip_ranges = client_ip_ranges
        # The domain name connected to HTTPDNS for the current account. This parameter is required.
        self.domain_name = domain_name
        # Specifies whether to enable the policy upon creation. If this parameter is omitted or set to false, the policy is disabled (Status=0). If this parameter is set to true, the policy is enabled (Status=1), and you do not need to call the enable operation. This parameter applies to the LINE and IP_RANGE modes. Actual resolution still requires waiting for configuration propagation.
        self.enable = enable
        # The line identifier required for the LINE mode. Valid values:
        # - internal: the Chinese mainland.
        # - overseas: outside the Chinese mainland.
        # 
        # Do not specify this parameter for the IP_RANGE mode.
        self.line_id = line_id
        # The match type. Valid values:
        # - LINE: the line mode.
        # - IP_RANGE: the client IP address range mode.
        # 
        # If this parameter is omitted, it is processed as LINE. To create an IP address range policy, you must explicitly set this parameter to IP_RANGE and provide ClientIpRanges. You cannot provide LineId or Paths at the same time. The match type cannot be changed after creation.
        self.match_type = match_type
        # The line selection path that describes the line conditions at each level. This parameter applies only to the LINE mode. The IP_RANGE mode does not use line paths. When you create a line policy, provide valid options at each level. Use x for the default option. For the Chinese mainland, the levels include ISP, region, and province. For regions outside the Chinese mainland, the levels include continent and region.
        self.paths = paths
        # The complete list of rules. This parameter is required and must contain at least one rule. When matching only by IP address range, configure a default rule without ArgKeys and Args, and configure the A or AAAA destination addresses in the Records of this rule. When saved, the serialized UTF-8 JSON content must be less than 65,535 bytes.
        self.rules = rules

    def validate(self):
        if self.paths:
            for v1 in self.paths:
                 if v1:
                    v1.validate()
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

        if self.enable is not None:
            result['Enable'] = self.enable

        if self.line_id is not None:
            result['LineId'] = self.line_id

        if self.match_type is not None:
            result['MatchType'] = self.match_type

        result['Paths'] = []
        if self.paths is not None:
            for k1 in self.paths:
                result['Paths'].append(k1.to_map() if k1 else None)

        result['Rules'] = []
        if self.rules is not None:
            for k1 in self.rules:
                result['Rules'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientIpRanges') is not None:
            self.client_ip_ranges = m.get('ClientIpRanges')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('LineId') is not None:
            self.line_id = m.get('LineId')

        if m.get('MatchType') is not None:
            self.match_type = m.get('MatchType')

        self.paths = []
        if m.get('Paths') is not None:
            for k1 in m.get('Paths'):
                temp_model = main_models.CreateSdnsRuleCategoryRequestPaths()
                self.paths.append(temp_model.from_map(k1))

        self.rules = []
        if m.get('Rules') is not None:
            for k1 in m.get('Rules'):
                temp_model = main_models.CreateSdnsRuleCategoryRequestRules()
                self.rules.append(temp_model.from_map(k1))

        return self

class CreateSdnsRuleCategoryRequestRules(DaraModel):
    def __init__(
        self,
        arg_keys: List[str] = None,
        args: Dict[str, str] = None,
        name: str = None,
        records: List[main_models.CreateSdnsRuleCategoryRequestRulesRecords] = None,
        result_mode: int = None,
        ttl: int = None,
    ):
        # The optional list of custom parameter names used to record the display order. Omit this parameter when matching only by IP address range. If Args is used, the names must correspond to the parameter names in Args.
        self.arg_keys = arg_keys
        # The optional custom parameter conditions. The key is the parameter name, and the value is the match value. Omit this parameter when matching only by IP address range. You do not need to add business parameters.
        self.args = args
        # The rule name. This parameter is required and cannot be null. We recommend that you use a non-empty name with business meaning. This parameter cannot replace the policy Id.
        self.name = name
        # The list of configured resolution records, which can include A and AAAA records. Actual resolution returns only records of the queried type. If the list is empty or does not contain records of the queried type, the system continues to fall back.
        self.records = records
        # The record return mode. Valid values:
        # - 0: returns all records of the queried type.
        # - 1: returns one record of the queried type based on the weight.
        self.result_mode = result_mode
        # The cache validity period of the record, in seconds. This parameter must be a positive integer.
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
                temp_model = main_models.CreateSdnsRuleCategoryRequestRulesRecords()
                self.records.append(temp_model.from_map(k1))

        if m.get('ResultMode') is not None:
            self.result_mode = m.get('ResultMode')

        if m.get('Ttl') is not None:
            self.ttl = m.get('Ttl')

        return self

class CreateSdnsRuleCategoryRequestRulesRecords(DaraModel):
    def __init__(
        self,
        ip: str = None,
        type: int = None,
        type_label: str = None,
        weight: int = None,
    ):
        # The single destination IP address corresponding to the record. If Type is set to 1, the value is an IPv4 address, such as 192.0.2.200. If Type is set to 28, the value is an IPv6 address, such as 2001:db8::200. Do not use CIDR blocks, start-end ranges, or domain names.
        self.ip = ip
        # The DNS record type. Valid values:
        # - 1: A record.
        # - 28: AAAA record.
        # 
        # Specify an integer. Do not use the string A or AAAA.
        self.type = type
        # The auxiliary display text for the record type. This parameter does not participate in matching or resolution decisions and can be omitted in the request.
        self.type_label = type_label
        # The relative weight of the record. This parameter is used to select one record of the same queried type only when ResultMode is set to 1. We recommend that you set this parameter to a positive integer from 1 to 100. The sum of the weights of all records does not need to be 100. This parameter does not participate in selection when ResultMode is set to 0.
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



class CreateSdnsRuleCategoryRequestPaths(DaraModel):
    def __init__(
        self,
        id: str = None,
        key: str = None,
        level: int = None,
    ):
        # The code of the option at this level. For example, chinanet at the isps level indicates China Telecom. Use valid options for the associated line and maintain consistent hierarchical subordination.
        self.id = id
        # The level identifier. For the Chinese mainland, use isps, subRegions, and provinces. For regions outside the Chinese mainland, use continents and geoRegions. This parameter corresponds to Level.
        self.key = key
        # The sequence number of the line level. For the Chinese mainland, the values are 1 (ISP), 2 (region), and 3 (province). For regions outside the Chinese mainland, the values are 1 (continent) and 2 (region).
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

        if self.level is not None:
            result['Level'] = self.level

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        return self

