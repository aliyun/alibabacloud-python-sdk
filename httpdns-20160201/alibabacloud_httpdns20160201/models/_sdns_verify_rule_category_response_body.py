# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_httpdns20160201 import models as main_models
from darabonba.model import DaraModel

class SdnsVerifyRuleCategoryResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.SdnsVerifyRuleCategoryResponseBodyData = None,
        request_id: str = None,
    ):
        # The configuration of the matched rule. If no rules are matched, this field is empty or omitted. This field does not represent the final response of the actual resolution chain.
        self.data = data
        # The ID of the request, used to troubleshoot call issues. This field is not the policy ID.
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
            temp_model = main_models.SdnsVerifyRuleCategoryResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class SdnsVerifyRuleCategoryResponseBodyData(DaraModel):
    def __init__(
        self,
        arg_keys: List[str] = None,
        args: Dict[str, str] = None,
        name: str = None,
        records: List[main_models.SdnsVerifyRuleCategoryResponseBodyDataRecords] = None,
        result_mode: int = None,
        ttl: int = None,
    ):
        # The custom parameter names and their display order. This field can be empty if no custom parameters are used.
        self.arg_keys = arg_keys
        # The custom parameter match conditions attached to the rule. If not configured, no parameter restrictions are attached.
        self.args = args
        # The rule name, used to identify the rule. This field cannot replace the policy ID.
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
                temp_model = main_models.SdnsVerifyRuleCategoryResponseBodyDataRecords()
                self.records.append(temp_model.from_map(k1))

        if m.get('ResultMode') is not None:
            self.result_mode = m.get('ResultMode')

        if m.get('Ttl') is not None:
            self.ttl = m.get('Ttl')

        return self

class SdnsVerifyRuleCategoryResponseBodyDataRecords(DaraModel):
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

