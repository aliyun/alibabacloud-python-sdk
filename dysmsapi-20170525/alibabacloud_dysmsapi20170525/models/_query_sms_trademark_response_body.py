# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dysmsapi20170525 import models as main_models
from darabonba.model import DaraModel

class QuerySmsTrademarkResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: List[main_models.QuerySmsTrademarkResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

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
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        if self.code is not None:
            result['Code'] = self.code

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.QuerySmsTrademarkResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QuerySmsTrademarkResponseBodyData(DaraModel):
    def __init__(
        self,
        trademark_applicant_name: str = None,
        trademark_eff_exp_date: str = None,
        trademark_id: int = None,
        trademark_name: str = None,
        trademark_pic: str = None,
        trademark_pic_url: str = None,
        trademark_registration_number: str = None,
    ):
        # 申请人名称
        self.trademark_applicant_name = trademark_applicant_name
        # 专用权生失效日期
        self.trademark_eff_exp_date = trademark_eff_exp_date
        # 商标材料id
        self.trademark_id = trademark_id
        # 商标名称
        self.trademark_name = trademark_name
        # 商标截图Osskey（给签名传工单用）
        self.trademark_pic = trademark_pic
        # 商标截图url地址
        self.trademark_pic_url = trademark_pic_url
        # 商标注册号
        self.trademark_registration_number = trademark_registration_number

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.trademark_applicant_name is not None:
            result['TrademarkApplicantName'] = self.trademark_applicant_name

        if self.trademark_eff_exp_date is not None:
            result['TrademarkEffExpDate'] = self.trademark_eff_exp_date

        if self.trademark_id is not None:
            result['TrademarkId'] = self.trademark_id

        if self.trademark_name is not None:
            result['TrademarkName'] = self.trademark_name

        if self.trademark_pic is not None:
            result['TrademarkPic'] = self.trademark_pic

        if self.trademark_pic_url is not None:
            result['TrademarkPicUrl'] = self.trademark_pic_url

        if self.trademark_registration_number is not None:
            result['TrademarkRegistrationNumber'] = self.trademark_registration_number

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TrademarkApplicantName') is not None:
            self.trademark_applicant_name = m.get('TrademarkApplicantName')

        if m.get('TrademarkEffExpDate') is not None:
            self.trademark_eff_exp_date = m.get('TrademarkEffExpDate')

        if m.get('TrademarkId') is not None:
            self.trademark_id = m.get('TrademarkId')

        if m.get('TrademarkName') is not None:
            self.trademark_name = m.get('TrademarkName')

        if m.get('TrademarkPic') is not None:
            self.trademark_pic = m.get('TrademarkPic')

        if m.get('TrademarkPicUrl') is not None:
            self.trademark_pic_url = m.get('TrademarkPicUrl')

        if m.get('TrademarkRegistrationNumber') is not None:
            self.trademark_registration_number = m.get('TrademarkRegistrationNumber')

        return self

