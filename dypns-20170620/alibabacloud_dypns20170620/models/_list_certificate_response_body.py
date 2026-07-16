# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dypns20170620 import models as main_models
from darabonba.model import DaraModel

class ListCertificateResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.ListCertificateResponseBodyData] = None,
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
                temp_model = main_models.ListCertificateResponseBodyData()
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

class ListCertificateResponseBodyData(DaraModel):
    def __init__(
        self,
        authorization_time: int = None,
        blockchain_no: str = None,
        business_type_list: List[int] = None,
        cancel_time: int = None,
        company_name: str = None,
        end_date: str = None,
        phone_no: str = None,
        scheme_type: int = None,
        start_date: str = None,
        status: int = None,
    ):
        self.authorization_time = authorization_time
        self.blockchain_no = blockchain_no
        self.business_type_list = business_type_list
        self.cancel_time = cancel_time
        self.company_name = company_name
        self.end_date = end_date
        self.phone_no = phone_no
        self.scheme_type = scheme_type
        self.start_date = start_date
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.authorization_time is not None:
            result['AuthorizationTime'] = self.authorization_time

        if self.blockchain_no is not None:
            result['BlockchainNo'] = self.blockchain_no

        if self.business_type_list is not None:
            result['BusinessTypeList'] = self.business_type_list

        if self.cancel_time is not None:
            result['CancelTime'] = self.cancel_time

        if self.company_name is not None:
            result['CompanyName'] = self.company_name

        if self.end_date is not None:
            result['EndDate'] = self.end_date

        if self.phone_no is not None:
            result['PhoneNo'] = self.phone_no

        if self.scheme_type is not None:
            result['SchemeType'] = self.scheme_type

        if self.start_date is not None:
            result['StartDate'] = self.start_date

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthorizationTime') is not None:
            self.authorization_time = m.get('AuthorizationTime')

        if m.get('BlockchainNo') is not None:
            self.blockchain_no = m.get('BlockchainNo')

        if m.get('BusinessTypeList') is not None:
            self.business_type_list = m.get('BusinessTypeList')

        if m.get('CancelTime') is not None:
            self.cancel_time = m.get('CancelTime')

        if m.get('CompanyName') is not None:
            self.company_name = m.get('CompanyName')

        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')

        if m.get('PhoneNo') is not None:
            self.phone_no = m.get('PhoneNo')

        if m.get('SchemeType') is not None:
            self.scheme_type = m.get('SchemeType')

        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

