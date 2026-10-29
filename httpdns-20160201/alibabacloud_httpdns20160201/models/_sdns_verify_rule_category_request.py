# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, List

from alibabacloud_httpdns20160201 import models as main_models
from darabonba.model import DaraModel

class SdnsVerifyRuleCategoryRequest(DaraModel):
    def __init__(
        self,
        args: Dict[str, str] = None,
        cip: str = None,
        client_ip_ranges: List[str] = None,
        match_type: str = None,
        rules: List[main_models.SdnsVerifyRuleCategoryRequestRules] = None,
    ):
        # The parameter object used for the current validation. If no custom parameters are used, pass an empty JSON object {}. Do not pass an empty string or null.
        self.args = args
        # The simulated client IP address. This parameter is required in IP_RANGE mode. Supports a single IPv4 or IPv6 address. CIDR blocks and start-to-end ranges are not supported. This parameter is used for CIDR block matching in the current request and does not change the source of the actual DNS resolution request.
        self.cip = cip
        # The array of client CIDR blocks that must be provided in the IP_RANGE pattern. Send this parameter as a JSON form field. Do not pass this parameter in the LINE pattern. Supports single IPv4 and IPv6 addresses, CIDR blocks, and start-to-end ranges. Multiple entries have an OR relationship. For CIDR blocks, the IPv4 prefix length ranges from 0 to 32, and the IPv6 prefix length ranges from 0 to 128. Start-to-end ranges are inclusive and must belong to the same address family, with the start address not greater than the end address. Overlapping, containing, and duplicate ranges are allowed within the same policy. When the policy is saved and read back, the array sequence, duplicate items, and the original text of each string are preserved. The array can contain up to 2,000 array elements. The total number of parsed non-empty address expressions ranges from 1 to 2,000, including duplicates. Specify one expression per array element. It is compatible with line breaks within an array element. Each expression can contain up to 128 characters, including leading and trailing whitespace. The serialized UTF-8 JSON content cannot exceed 65,535 bytes. Both the quantity and byte limits apply simultaneously. To authenticate, the system only checks the ranges that you commit and does not check for conflicts with saved policies.
        self.client_ip_ranges = client_ip_ranges
        # The match type. Valid values:
        # - LINE: line mode
        # - IP_RANGE: client CIDR block mode
        # If this parameter is omitted, LINE is used. In IP_RANGE mode, you must provide both ClientIpRanges and Cip.
        self.match_type = match_type
        # The complete list of rules. This parameter is required and must contain at least one rule. If you only need to match CIDR blocks, configure a default rule without ArgKeys and Args, and configure the A/AAAA destination addresses in the Records field of this rule. This operation is used for match validation and does not save the rules.
        self.rules = rules

    def validate(self):
        if self.rules:
            for v1 in self.rules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.args is not None:
            result['Args'] = self.args

        if self.cip is not None:
            result['Cip'] = self.cip

        if self.client_ip_ranges is not None:
            result['ClientIpRanges'] = self.client_ip_ranges

        if self.match_type is not None:
            result['MatchType'] = self.match_type

        result['Rules'] = []
        if self.rules is not None:
            for k1 in self.rules:
                result['Rules'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Args') is not None:
            self.args = m.get('Args')

        if m.get('Cip') is not None:
            self.cip = m.get('Cip')

        if m.get('ClientIpRanges') is not None:
            self.client_ip_ranges = m.get('ClientIpRanges')

        if m.get('MatchType') is not None:
            self.match_type = m.get('MatchType')

        self.rules = []
        if m.get('Rules') is not None:
            for k1 in m.get('Rules'):
                temp_model = main_models.SdnsVerifyRuleCategoryRequestRules()
                self.rules.append(temp_model.from_map(k1))

        return self

class SdnsVerifyRuleCategoryRequestRules(DaraModel):
    def __init__(
        self,
        arg_keys: List[str] = None,
        args: Dict[str, str] = None,
        name: str = None,
        records: List[main_models.SdnsVerifyRuleCategoryRequestRulesRecords] = None,
        result_mode: int = None,
        ttl: int = None,
    ):
        # The optional list of custom parameter names, used to record the display order. Omit this parameter if you only match CIDR blocks. If you use Args, the names must correspond to the parameter names in Args.
        self.arg_keys = arg_keys
        # The optional custom parameter conditions. The key is the parameter name and the value is the match value. Omit this parameter if you only match CIDR blocks. You do not need to add business parameters.
        self.args = args
        # The rule name. This parameter is required and cannot be null. Use a non-empty name with business meaning. This parameter cannot replace the policy ID.
        self.name = name
        # The list of configured DNS records, which can include A and AAAA records. Actual DNS resolution returns only records of the queried type. If the list is empty or does not contain records of the queried type, the system continues to fall back. This operation returns the records configured in the rule and does not filter them by query type.
        self.records = records
        # The record return mode. Valid values:
        # - 0: Returns all records of the queried type.
        # - 1: Returns one record of the queried type based on weight.
        # Policy validation only returns the rule configuration and does not perform weight sampling.
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
                temp_model = main_models.SdnsVerifyRuleCategoryRequestRulesRecords()
                self.records.append(temp_model.from_map(k1))

        if m.get('ResultMode') is not None:
            self.result_mode = m.get('ResultMode')

        if m.get('Ttl') is not None:
            self.ttl = m.get('Ttl')

        return self

class SdnsVerifyRuleCategoryRequestRulesRecords(DaraModel):
    def __init__(
        self,
        ip: str = None,
        type: int = None,
        type_label: str = None,
        weight: int = None,
    ):
        # The single destination IP address for the record. If Type is set to 1, specify an IPv4 address, such as 192.0.2.200. If Type is set to 28, specify an IPv6 address, such as 2001:db8::200. Do not use CIDR blocks, start-to-end ranges, or domain names.
        self.ip = ip
        # The DNS record type. Valid values:
        # - 1: A record
        # - 28: AAAA record
        # Specify an integer. Do not use the strings A or AAAA.
        self.type = type
        # The auxiliary display text for the record type. This parameter does not participate in matching or resolution decisions and can be omitted in the request.
        self.type_label = type_label
        # The relative weight of the record. This parameter is used to select one record of the same query type only when ResultMode is set to 1. Set this parameter to a positive integer from 1 to 100. The sum of the weights of all records does not need to be 100. This parameter does not participate in selection when ResultMode is set to 0.
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

