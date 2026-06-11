# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agency20250227 import models as main_models
from darabonba.model import DaraModel

class GetSubPartnerListResponseBody(DaraModel):
    def __init__(
        self,
        message: str = None,
        page_no: str = None,
        page_size: str = None,
        request_id: str = None,
        sub_partner_list: List[main_models.GetSubPartnerListResponseBodySubPartnerList] = None,
        success: bool = None,
        total: int = None,
    ):
        # Message
        self.message = message
        # Current page number
        self.page_no = page_no
        # Number of second-tier distributors returned per page, up to 100
        # 
        # This parameter is required.
        self.page_size = page_size
        # Request ID
        self.request_id = request_id
        # List of second-tier distributors
        self.sub_partner_list = sub_partner_list
        # Indicates whether the invocation succeeded.
        self.success = success
        # Total amount of data under the current request conditions
        self.total = total

    def validate(self):
        if self.sub_partner_list:
            for v1 in self.sub_partner_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.message is not None:
            result['Message'] = self.message

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['SubPartnerList'] = []
        if self.sub_partner_list is not None:
            for k1 in self.sub_partner_list:
                result['SubPartnerList'].append(k1.to_map() if k1 else None)

        if self.success is not None:
            result['Success'] = self.success

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.sub_partner_list = []
        if m.get('SubPartnerList') is not None:
            for k1 in m.get('SubPartnerList'):
                temp_model = main_models.GetSubPartnerListResponseBodySubPartnerList()
                self.sub_partner_list.append(temp_model.from_map(k1))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class GetSubPartnerListResponseBodySubPartnerList(DaraModel):
    def __init__(
        self,
        address: str = None,
        agreement_status: str = None,
        agreement_status_desc: str = None,
        city: str = None,
        company_name: str = None,
        contact: str = None,
        district: str = None,
        join_time: str = None,
        master_account: str = None,
        master_uid: str = None,
        pid: str = None,
        province: str = None,
    ):
        # Detailed address of registration
        self.address = address
        # Contract status encoding
        self.agreement_status = agreement_status
        # Agreement status description
        self.agreement_status_desc = agreement_status_desc
        # City of registration
        self.city = city
        # Name of the second-tier distributor
        self.company_name = company_name
        # Contact name
        self.contact = contact
        # District or county of registration
        self.district = district
        # Initial onboarding time
        self.join_time = join_time
        # Master account name of the secondary distributor
        self.master_account = master_account
        # UID of the Master account of the second-tier distributor
        self.master_uid = master_uid
        # PID of the secondary distributor
        self.pid = pid
        # Province of registration
        self.province = province

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address is not None:
            result['Address'] = self.address

        if self.agreement_status is not None:
            result['AgreementStatus'] = self.agreement_status

        if self.agreement_status_desc is not None:
            result['AgreementStatusDesc'] = self.agreement_status_desc

        if self.city is not None:
            result['City'] = self.city

        if self.company_name is not None:
            result['CompanyName'] = self.company_name

        if self.contact is not None:
            result['Contact'] = self.contact

        if self.district is not None:
            result['District'] = self.district

        if self.join_time is not None:
            result['JoinTime'] = self.join_time

        if self.master_account is not None:
            result['MasterAccount'] = self.master_account

        if self.master_uid is not None:
            result['MasterUid'] = self.master_uid

        if self.pid is not None:
            result['Pid'] = self.pid

        if self.province is not None:
            result['Province'] = self.province

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')

        if m.get('AgreementStatus') is not None:
            self.agreement_status = m.get('AgreementStatus')

        if m.get('AgreementStatusDesc') is not None:
            self.agreement_status_desc = m.get('AgreementStatusDesc')

        if m.get('City') is not None:
            self.city = m.get('City')

        if m.get('CompanyName') is not None:
            self.company_name = m.get('CompanyName')

        if m.get('Contact') is not None:
            self.contact = m.get('Contact')

        if m.get('District') is not None:
            self.district = m.get('District')

        if m.get('JoinTime') is not None:
            self.join_time = m.get('JoinTime')

        if m.get('MasterAccount') is not None:
            self.master_account = m.get('MasterAccount')

        if m.get('MasterUid') is not None:
            self.master_uid = m.get('MasterUid')

        if m.get('Pid') is not None:
            self.pid = m.get('Pid')

        if m.get('Province') is not None:
            self.province = m.get('Province')

        return self

