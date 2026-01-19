# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudapi20160714 import models as main_models
from darabonba.model import DaraModel

class CreatePrivateDNSRequest(DaraModel):
    def __init__(
        self,
        intranet_domain: str = None,
        records: List[main_models.CreatePrivateDNSRequestRecords] = None,
        security_token: str = None,
        type: str = None,
    ):
        # The internal domain name.
        # 
        # This parameter is required.
        self.intranet_domain = intranet_domain
        # The resolution records. This parameter is valid only when Type is set to A.
        self.records = records
        self.security_token = security_token
        # The internal domain name resolution type. Valid values:
        # 
        # *   VPC: resolution for VPC access authorizations. A resolution of this type can be bound only to traditional dedicated instances.
        # *   A: resolution that supports A records. A resolution of this type can be bound only to VPC integration dedicated instances.
        # 
        # This parameter is required.
        self.type = type

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
        if self.intranet_domain is not None:
            result['IntranetDomain'] = self.intranet_domain

        result['Records'] = []
        if self.records is not None:
            for k1 in self.records:
                result['Records'].append(k1.to_map() if k1 else None)

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IntranetDomain') is not None:
            self.intranet_domain = m.get('IntranetDomain')

        self.records = []
        if m.get('Records') is not None:
            for k1 in m.get('Records'):
                temp_model = main_models.CreatePrivateDNSRequestRecords()
                self.records.append(temp_model.from_map(k1))

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class CreatePrivateDNSRequestRecords(DaraModel):
    def __init__(
        self,
        record: str = None,
        weight: int = None,
    ):
        # The resolution record.
        self.record = record
        # The weight of the record.
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.record is not None:
            result['Record'] = self.record

        if self.weight is not None:
            result['Weight'] = self.weight

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Record') is not None:
            self.record = m.get('Record')

        if m.get('Weight') is not None:
            self.weight = m.get('Weight')

        return self

