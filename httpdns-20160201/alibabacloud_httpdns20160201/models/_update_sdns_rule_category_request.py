# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_httpdns20160201 import models as main_models
from darabonba.model import DaraModel

class UpdateSdnsRuleCategoryRequest(DaraModel):
    def __init__(
        self,
        client_ip_ranges: str = None,
        id: str = None,
        rules: List[main_models.UpdateSdnsRuleCategoryRequestRules] = None,
    ):
        # The JSON text string of the IP address range array. This parameter is used only to update IP_RANGE policies. If this parameter is omitted, the original IP address ranges are retained. If this parameter is provided, the original IP address ranges are replaced as a whole. You cannot pass an empty string, an empty array [], null, or a non-string array. Single IP addresses, CIDR blocks, and start-end ranges of IPv4 and IPv6 are supported. Multiple entries have an OR relationship. For CIDR blocks, the IPv4 prefix length ranges from 0 to 32, and the IPv6 prefix length ranges from 0 to 128. Start-end ranges are inclusive and must belong to the same address family, and the start address must not be greater than the end address. Overlapping, containing, and duplicate ranges are allowed within the same policy. When the policy is saved and read back, the array order, duplicate items, and the original text of each string are retained. An array can contain up to 2,000 array elements. The total number of parsed non-empty address expressions ranges from 1 to 2,000, and duplicate items are counted. We recommend that you specify one expression per element. It is compatible with line breaks within an element. Each expression can contain up to 128 characters, including leading and trailing whitespace. The serialized UTF-8 JSON sequence cannot exceed 65,535 bytes. The quantity and byte limits take effect at the same time. Overlapping is not allowed among different IP_RANGE policies of the same account, the same domain name, and the same address family. Disabled policies are also checked. Disabling a policy does not release its IP address ranges. This limit does not compare LINE policies and the independent configurations of the legacy SetIPRegionResult operation. The new ranges do not conflict with the old ranges of the same policy during an update. Send this parameter as a single form field, and do not add quotes to the JSON text again.
        self.client_ip_ranges = client_ip_ranges
        # The ID of the policy for the current account. This parameter is required. You can obtain the ID from the Id field in the response of CreateSdnsRuleCategory or from the list returned by SdnsListRuleCategories. Use a decimal string to avoid precision loss for large integers.
        self.id = id
        # The complete list of rules. This parameter is required and must contain at least one rule. If you match only by IP address range, you can configure a default rule without ArgKeys and Args, and configure the A or AAAA destination addresses in the Records field of the rule. The update replaces the original rule list as a whole. Old rules that are not included in the new list are removed. When the rules are saved, the serialized UTF-8 JSON content must be less than 65,535 bytes.
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
        if self.client_ip_ranges is not None:
            result['ClientIpRanges'] = self.client_ip_ranges

        if self.id is not None:
            result['Id'] = self.id

        result['Rules'] = []
        if self.rules is not None:
            for k1 in self.rules:
                result['Rules'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientIpRanges') is not None:
            self.client_ip_ranges = m.get('ClientIpRanges')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        self.rules = []
        if m.get('Rules') is not None:
            for k1 in m.get('Rules'):
                temp_model = main_models.UpdateSdnsRuleCategoryRequestRules()
                self.rules.append(temp_model.from_map(k1))

        return self

class UpdateSdnsRuleCategoryRequestRules(DaraModel):
    def __init__(
        self,
        arg_keys: List[str] = None,
        args: Dict[str, str] = None,
        name: str = None,
        records: List[main_models.UpdateSdnsRuleCategoryRequestRulesRecords] = None,
        result_mode: int = None,
        ttl: int = None,
    ):
        # The optional list of custom parameter names, which is used to record the display order. Omit this parameter if you match only by IP address range. If you use Args, the names must correspond to the parameter names in Args.
        self.arg_keys = arg_keys
        # The optional custom parameter conditions. The key is the parameter name, and the value is the match value. Omit this parameter if you match only by IP address range. You do not need to add business parameters.
        self.args = args
        # The name of the rule. This parameter is required and cannot be null. We recommend that you use a non-empty name that has business meaning. The name cannot replace the policy ID.
        self.name = name
        # The list of configured DNS records. The list can include A and AAAA records. Actual DNS resolution returns only the records of the queried type. If the list is empty or does not contain records of the queried type, the system continues to fall back.
        self.records = records
        # The record return mode. Valid values:
        # - 0: Returns all records of the queried type.
        # - 1: Returns one record of the queried type based on the weight.
        self.result_mode = result_mode
        # The cache validity period of the record, in seconds. The value must be a positive integer.
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
                temp_model = main_models.UpdateSdnsRuleCategoryRequestRulesRecords()
                self.records.append(temp_model.from_map(k1))

        if m.get('ResultMode') is not None:
            self.result_mode = m.get('ResultMode')

        if m.get('Ttl') is not None:
            self.ttl = m.get('Ttl')

        return self

class UpdateSdnsRuleCategoryRequestRulesRecords(DaraModel):
    def __init__(
        self,
        ip: str = None,
        type: int = None,
        type_label: str = None,
        weight: int = None,
    ):
        # The single destination IP address corresponding to the record. When Type is set to 1, the IP address is an IPv4 address, such as 192.0.2.200. When Type is set to 28, the IP address is an IPv6 address, such as 2001:db8::200. Do not use CIDR blocks, start-end ranges, or domain names.
        self.ip = ip
        # The DNS record type. Valid values:
        # - 1: A record.
        # - 28: AAAA record.
        # Specify an integer. Do not use the string A or AAAA.
        self.type = type
        # The auxiliary display text for the record type. This text is not used for matching or DNS resolution decisions. You can omit this parameter in the request.
        self.type_label = type_label
        # The relative weight of the record. This parameter is used to select one record of the same queried type only when ResultMode is set to 1. We recommend that you set this parameter to a positive integer from 1 to 100. The sum of the weights of all records does not need to be 100. This parameter is not used for selection when ResultMode is set to 0.
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

