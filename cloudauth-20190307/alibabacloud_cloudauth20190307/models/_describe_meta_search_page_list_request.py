# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeMetaSearchPageListRequest(DaraModel):
    def __init__(
        self,
        api: str = None,
        bank_card: str = None,
        biz_code: str = None,
        current_page: int = None,
        end_date: int = None,
        identify_num: str = None,
        isp_name: str = None,
        mobile: str = None,
        page_size: int = None,
        req_id: str = None,
        start_date: int = None,
        sub_code: str = None,
        user_name: str = None,
        vehicle_num: str = None,
    ):
        # This parameter is required.
        self.api = api
        self.bank_card = bank_card
        self.biz_code = biz_code
        # This parameter is required.
        self.current_page = current_page
        # This parameter is required.
        self.end_date = end_date
        self.identify_num = identify_num
        self.isp_name = isp_name
        self.mobile = mobile
        # This parameter is required.
        self.page_size = page_size
        self.req_id = req_id
        # This parameter is required.
        self.start_date = start_date
        self.sub_code = sub_code
        self.user_name = user_name
        self.vehicle_num = vehicle_num

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api is not None:
            result['Api'] = self.api

        if self.bank_card is not None:
            result['BankCard'] = self.bank_card

        if self.biz_code is not None:
            result['BizCode'] = self.biz_code

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.end_date is not None:
            result['EndDate'] = self.end_date

        if self.identify_num is not None:
            result['IdentifyNum'] = self.identify_num

        if self.isp_name is not None:
            result['IspName'] = self.isp_name

        if self.mobile is not None:
            result['Mobile'] = self.mobile

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.req_id is not None:
            result['ReqId'] = self.req_id

        if self.start_date is not None:
            result['StartDate'] = self.start_date

        if self.sub_code is not None:
            result['SubCode'] = self.sub_code

        if self.user_name is not None:
            result['UserName'] = self.user_name

        if self.vehicle_num is not None:
            result['VehicleNum'] = self.vehicle_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Api') is not None:
            self.api = m.get('Api')

        if m.get('BankCard') is not None:
            self.bank_card = m.get('BankCard')

        if m.get('BizCode') is not None:
            self.biz_code = m.get('BizCode')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')

        if m.get('IdentifyNum') is not None:
            self.identify_num = m.get('IdentifyNum')

        if m.get('IspName') is not None:
            self.isp_name = m.get('IspName')

        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ReqId') is not None:
            self.req_id = m.get('ReqId')

        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')

        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        if m.get('VehicleNum') is not None:
            self.vehicle_num = m.get('VehicleNum')

        return self

