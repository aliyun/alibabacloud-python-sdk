# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudapi20160714 import models as main_models
from darabonba.model import DaraModel

class ListPrivateDNSResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        private_dnslist: List[main_models.ListPrivateDNSResponseBodyPrivateDNSList] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The internal domain name resolutions.
        self.private_dnslist = private_dnslist
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.private_dnslist:
            for v1 in self.private_dnslist:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        result['PrivateDNSList'] = []
        if self.private_dnslist is not None:
            for k1 in self.private_dnslist:
                result['PrivateDNSList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        self.private_dnslist = []
        if m.get('PrivateDNSList') is not None:
            for k1 in m.get('PrivateDNSList'):
                temp_model = main_models.ListPrivateDNSResponseBodyPrivateDNSList()
                self.private_dnslist.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListPrivateDNSResponseBodyPrivateDNSList(DaraModel):
    def __init__(
        self,
        bind_instances: List[str] = None,
        created_time: str = None,
        intranet_domain: str = None,
        records: List[main_models.ListPrivateDNSResponseBodyPrivateDNSListRecords] = None,
        type: str = None,
    ):
        # The instances that are associated with the resolution.
        self.bind_instances = bind_instances
        # The time when the resolution was created. The time is displayed in UTC.
        self.created_time = created_time
        # The internal domain name.
        self.intranet_domain = intranet_domain
        # The resolution records.
        self.records = records
        # The internal domain name resolution type. Valid values:
        # 
        # *   VPC: resolution for VPC access authorizations. A resolution of this type can be bound only to traditional dedicated instances.
        # *   A: resolution that supports A records. A resolution of this type can be bound only to VPC integration dedicated instances.
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
        if self.bind_instances is not None:
            result['BindInstances'] = self.bind_instances

        if self.created_time is not None:
            result['CreatedTime'] = self.created_time

        if self.intranet_domain is not None:
            result['IntranetDomain'] = self.intranet_domain

        result['Records'] = []
        if self.records is not None:
            for k1 in self.records:
                result['Records'].append(k1.to_map() if k1 else None)

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BindInstances') is not None:
            self.bind_instances = m.get('BindInstances')

        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')

        if m.get('IntranetDomain') is not None:
            self.intranet_domain = m.get('IntranetDomain')

        self.records = []
        if m.get('Records') is not None:
            for k1 in m.get('Records'):
                temp_model = main_models.ListPrivateDNSResponseBodyPrivateDNSListRecords()
                self.records.append(temp_model.from_map(k1))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class ListPrivateDNSResponseBodyPrivateDNSListRecords(DaraModel):
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

