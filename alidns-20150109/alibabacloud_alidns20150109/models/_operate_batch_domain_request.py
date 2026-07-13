# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alidns20150109 import models as main_models
from darabonba.model import DaraModel

class OperateBatchDomainRequest(DaraModel):
    def __init__(
        self,
        domain_record_info: List[main_models.OperateBatchDomainRequestDomainRecordInfo] = None,
        lang: str = None,
        type: str = None,
    ):
        # The data for the batch operation.
        # 
        # This parameter is required.
        self.domain_record_info = domain_record_info
        # The response language. Valid values:
        # 
        # - zh: Chinese
        # 
        # - en: English
        # 
        # Default value: zh
        self.lang = lang
        # The batch operation type. Valid values:
        # 
        # - **DOMAIN_ADD**: adds domain names in batches.
        # 
        # - **DOMAIN_DEL**: deletes domain names in batches.
        # 
        # - **RR_ADD**: adds DNS records in batches.
        # 
        # - **RR_DEL**: deletes DNS records in batches. This operation deletes DNS records that match the conditions specified by `Rr`, `Value`, or both. If you do not specify `Rr` and `Value`, all DNS records for the specified domain name are deleted.
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        if self.domain_record_info:
            for v1 in self.domain_record_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DomainRecordInfo'] = []
        if self.domain_record_info is not None:
            for k1 in self.domain_record_info:
                result['DomainRecordInfo'].append(k1.to_map() if k1 else None)

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.domain_record_info = []
        if m.get('DomainRecordInfo') is not None:
            for k1 in m.get('DomainRecordInfo'):
                temp_model = main_models.OperateBatchDomainRequestDomainRecordInfo()
                self.domain_record_info.append(temp_model.from_map(k1))

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class OperateBatchDomainRequestDomainRecordInfo(DaraModel):
    def __init__(
        self,
        domain: str = None,
        line: str = None,
        new_rr: str = None,
        new_type: str = None,
        new_value: str = None,
        priority: int = None,
        rr: str = None,
        ttl: int = None,
        type: str = None,
        value: str = None,
    ):
        # The domain name.
        # 
        # > A single request can contain up to 200 entries. Exceeding this limit may cause the request to fail due to the HTTP request header size limit.
        # 
        # This parameter is required.
        self.domain = domain
        # The resolution line. Default value: default.
        self.line = line
        # The new host record. This parameter is used only for modification operations and is for internal use only.
        self.new_rr = new_rr
        # The new record type. This parameter is used only for modification operations and is for internal use only.
        self.new_type = new_type
        # The new record value. This parameter is used only for modification operations and is for internal use only.
        self.new_value = new_value
        # The MX priority.
        # 
        # This parameter is required if the record type is MX. Default value: 10.
        self.priority = priority
        # The host record.
        # 
        # > This parameter is required when `Type` is **RR_ADD** or **RR_DEL**.
        self.rr = rr
        # The TTL, in seconds. Default value: ***600***.
        self.ttl = ttl
        # The record type. Examples: A, AAAA, TXT, MX, and CNAME.
        # 
        # > This parameter is required when `Type` is **RR_ADD** or **RR_DEL**.
        self.type = type
        # The record value.
        # 
        # > This parameter is required when `Type` is **RR_ADD** or **RR_DEL**.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain is not None:
            result['Domain'] = self.domain

        if self.line is not None:
            result['Line'] = self.line

        if self.new_rr is not None:
            result['NewRr'] = self.new_rr

        if self.new_type is not None:
            result['NewType'] = self.new_type

        if self.new_value is not None:
            result['NewValue'] = self.new_value

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.rr is not None:
            result['Rr'] = self.rr

        if self.ttl is not None:
            result['Ttl'] = self.ttl

        if self.type is not None:
            result['Type'] = self.type

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('Line') is not None:
            self.line = m.get('Line')

        if m.get('NewRr') is not None:
            self.new_rr = m.get('NewRr')

        if m.get('NewType') is not None:
            self.new_type = m.get('NewType')

        if m.get('NewValue') is not None:
            self.new_value = m.get('NewValue')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('Rr') is not None:
            self.rr = m.get('Rr')

        if m.get('Ttl') is not None:
            self.ttl = m.get('Ttl')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

