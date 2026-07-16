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
        # The product API. Valid values:
        # - **ID_CARD_2_META**: ID card two-element verification
        # - **ID_PERIOD**: ID card validity period verification
        # - **MOBILE_ONLINE_LENGTH**: mobile number online duration
        # - **MOBILE_ONLINE_STATUS**: mobile number online status
        # - **MOBILE_3_META_SIMPLE**: mobile number three-element verification (simple edition)
        # - **MOBILE_3_META**: mobile number three-element verification (detailed edition)
        # - **MOBILE_2_META**: mobile number two-element verification
        # - **BANK_CARD_N_META**: bank card verification (detailed edition)
        # - **MOBILE_DETECT**: phone number detection 
        # - **VEHICLE_N_META**: vehicle element verification (enhanced edition)
        # - **VEHICLE_PENTA_INFO**: vehicle five-element information recognition
        # - **VEHICLE_LICENSE_INFO**: vehicle information recognition
        # - **VEHICLE_INSURE_DATE**: vehicle insurance date query
        # - **VEHICLE_CHECK**: vehicle element verification.
        # 
        # This parameter is required.
        self.api = api
        # The bank card number.
        self.bank_card = bank_card
        # The verification status. Valid values:
        # - **1**: Verification passed.
        # - **2**: Verification failed.
        # - **3**: No record found.
        self.biz_code = biz_code
        # The current page number.
        # 
        # This parameter is required.
        self.current_page = current_page
        # The end time of the query. The value is a UNIX timestamp in milliseconds.
        # 
        # This parameter is required.
        self.end_date = end_date
        # The ID card number.
        self.identify_num = identify_num
        # The name of the telecommunications service provider. Valid values:
        # - **CMCC**: China Mobile
        # - **CUCC**: China Unicom
        # - **CTCC**: China Telecom.
        self.isp_name = isp_name
        # The mobile phone number.
        self.mobile = mobile
        # The number of entries per page.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The request ID.
        self.req_id = req_id
        # The start time of the query. The value is a UNIX timestamp in milliseconds.
        # 
        # This parameter is required.
        self.start_date = start_date
        # The result code. For more information, see [official documentation](https://www.alibabacloud.com/help/en/id-verification/information-verification/).
        self.sub_code = sub_code
        # The name.
        self.user_name = user_name
        # The license plate number.
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

