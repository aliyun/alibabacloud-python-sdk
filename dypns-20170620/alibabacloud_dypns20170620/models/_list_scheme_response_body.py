# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dypns20170620 import models as main_models
from darabonba.model import DaraModel

class ListSchemeResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.ListSchemeResponseBodyData] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.code = code
        self.data = data
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListSchemeResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListSchemeResponseBodyData(DaraModel):
    def __init__(
        self,
        apply_time: int = None,
        audit_desc: str = None,
        business_type_list: List[int] = None,
        company_name: str = None,
        scheme_id: int = None,
        scheme_name: str = None,
        scheme_type: int = None,
        status: int = None,
    ):
        self.apply_time = apply_time
        self.audit_desc = audit_desc
        self.business_type_list = business_type_list
        self.company_name = company_name
        self.scheme_id = scheme_id
        self.scheme_name = scheme_name
        self.scheme_type = scheme_type
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.apply_time is not None:
            result['ApplyTime'] = self.apply_time

        if self.audit_desc is not None:
            result['AuditDesc'] = self.audit_desc

        if self.business_type_list is not None:
            result['BusinessTypeList'] = self.business_type_list

        if self.company_name is not None:
            result['CompanyName'] = self.company_name

        if self.scheme_id is not None:
            result['SchemeId'] = self.scheme_id

        if self.scheme_name is not None:
            result['SchemeName'] = self.scheme_name

        if self.scheme_type is not None:
            result['SchemeType'] = self.scheme_type

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplyTime') is not None:
            self.apply_time = m.get('ApplyTime')

        if m.get('AuditDesc') is not None:
            self.audit_desc = m.get('AuditDesc')

        if m.get('BusinessTypeList') is not None:
            self.business_type_list = m.get('BusinessTypeList')

        if m.get('CompanyName') is not None:
            self.company_name = m.get('CompanyName')

        if m.get('SchemeId') is not None:
            self.scheme_id = m.get('SchemeId')

        if m.get('SchemeName') is not None:
            self.scheme_name = m.get('SchemeName')

        if m.get('SchemeType') is not None:
            self.scheme_type = m.get('SchemeType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

