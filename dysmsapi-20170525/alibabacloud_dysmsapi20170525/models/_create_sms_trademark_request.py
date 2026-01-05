# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateSmsTrademarkRequest(DaraModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        trademark_applicant_name: str = None,
        trademark_eff_exp_date: str = None,
        trademark_name: str = None,
        trademark_pic: str = None,
        trademark_registration_number: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # 申请人名称
        # 
        # This parameter is required.
        self.trademark_applicant_name = trademark_applicant_name
        # 专用权生失效日期
        # 
        # This parameter is required.
        self.trademark_eff_exp_date = trademark_eff_exp_date
        # 商标名称
        # 
        # This parameter is required.
        self.trademark_name = trademark_name
        # 商标详情截图osskey
        # 
        # This parameter is required.
        self.trademark_pic = trademark_pic
        # 商标注册号
        # 
        # This parameter is required.
        self.trademark_registration_number = trademark_registration_number

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.trademark_applicant_name is not None:
            result['TrademarkApplicantName'] = self.trademark_applicant_name

        if self.trademark_eff_exp_date is not None:
            result['TrademarkEffExpDate'] = self.trademark_eff_exp_date

        if self.trademark_name is not None:
            result['TrademarkName'] = self.trademark_name

        if self.trademark_pic is not None:
            result['TrademarkPic'] = self.trademark_pic

        if self.trademark_registration_number is not None:
            result['TrademarkRegistrationNumber'] = self.trademark_registration_number

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('TrademarkApplicantName') is not None:
            self.trademark_applicant_name = m.get('TrademarkApplicantName')

        if m.get('TrademarkEffExpDate') is not None:
            self.trademark_eff_exp_date = m.get('TrademarkEffExpDate')

        if m.get('TrademarkName') is not None:
            self.trademark_name = m.get('TrademarkName')

        if m.get('TrademarkPic') is not None:
            self.trademark_pic = m.get('TrademarkPic')

        if m.get('TrademarkRegistrationNumber') is not None:
            self.trademark_registration_number = m.get('TrademarkRegistrationNumber')

        return self

