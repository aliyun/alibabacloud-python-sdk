# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dm20151123 import models as main_models
from darabonba.model import DaraModel

class QueryDomainByParamResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
        data: main_models.QueryDomainByParamResponseBodyData = None,
    ):
        # Current page number
        self.page_number = page_number
        # Page size
        self.page_size = page_size
        # Request ID
        self.request_id = request_id
        # Total count
        self.total_count = total_count
        # List of domains
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.data is not None:
            result['data'] = self.data.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('data') is not None:
            temp_model = main_models.QueryDomainByParamResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        return self

class QueryDomainByParamResponseBodyData(DaraModel):
    def __init__(
        self,
        domain: List[main_models.QueryDomainByParamResponseBodyDataDomain] = None,
    ):
        self.domain = domain

    def validate(self):
        if self.domain:
            for v1 in self.domain:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['domain'] = []
        if self.domain is not None:
            for k1 in self.domain:
                result['domain'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.domain = []
        if m.get('domain') is not None:
            for k1 in m.get('domain'):
                temp_model = main_models.QueryDomainByParamResponseBodyDataDomain()
                self.domain.append(temp_model.from_map(k1))

        return self

class QueryDomainByParamResponseBodyDataDomain(DaraModel):
    def __init__(
        self,
        cname_auth_status: str = None,
        confirm_status: str = None,
        create_time: str = None,
        domain_id: str = None,
        domain_name: str = None,
        domain_record: str = None,
        domain_status: str = None,
        icp_status: str = None,
        mx_auth_status: str = None,
        spf_auth_status: str = None,
        utc_create_time: int = None,
    ):
        # Track verification
        self.cname_auth_status = cname_auth_status
        # CName verification status, success: 0; failure: 1
        self.confirm_status = confirm_status
        # Creation time
        self.create_time = create_time
        # Domain ID
        self.domain_id = domain_id
        # Domain name
        self.domain_name = domain_name
        # Domain record
        self.domain_record = domain_record
        # Domain status.
        # 
        # - 0: Available, verified
        # - 1: Unavailable, verification failed
        self.domain_status = domain_status
        # ICP filing status.
        # 
        # - 1 indicates filed
        # - 0 indicates not filed
        self.icp_status = icp_status
        # MX authentication status, success: 0, failure: 1.
        self.mx_auth_status = mx_auth_status
        # SPF authentication status, success: 0, failure: 1.
        self.spf_auth_status = spf_auth_status
        # Creation time in UTC format.
        self.utc_create_time = utc_create_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cname_auth_status is not None:
            result['CnameAuthStatus'] = self.cname_auth_status

        if self.confirm_status is not None:
            result['ConfirmStatus'] = self.confirm_status

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.domain_id is not None:
            result['DomainId'] = self.domain_id

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.domain_record is not None:
            result['DomainRecord'] = self.domain_record

        if self.domain_status is not None:
            result['DomainStatus'] = self.domain_status

        if self.icp_status is not None:
            result['IcpStatus'] = self.icp_status

        if self.mx_auth_status is not None:
            result['MxAuthStatus'] = self.mx_auth_status

        if self.spf_auth_status is not None:
            result['SpfAuthStatus'] = self.spf_auth_status

        if self.utc_create_time is not None:
            result['UtcCreateTime'] = self.utc_create_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CnameAuthStatus') is not None:
            self.cname_auth_status = m.get('CnameAuthStatus')

        if m.get('ConfirmStatus') is not None:
            self.confirm_status = m.get('ConfirmStatus')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DomainId') is not None:
            self.domain_id = m.get('DomainId')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('DomainRecord') is not None:
            self.domain_record = m.get('DomainRecord')

        if m.get('DomainStatus') is not None:
            self.domain_status = m.get('DomainStatus')

        if m.get('IcpStatus') is not None:
            self.icp_status = m.get('IcpStatus')

        if m.get('MxAuthStatus') is not None:
            self.mx_auth_status = m.get('MxAuthStatus')

        if m.get('SpfAuthStatus') is not None:
            self.spf_auth_status = m.get('SpfAuthStatus')

        if m.get('UtcCreateTime') is not None:
            self.utc_create_time = m.get('UtcCreateTime')

        return self

