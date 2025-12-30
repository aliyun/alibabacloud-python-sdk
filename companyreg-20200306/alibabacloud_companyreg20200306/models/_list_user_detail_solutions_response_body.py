# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_companyreg20200306 import models as main_models
from darabonba.model import DaraModel

class ListUserDetailSolutionsResponseBody(DaraModel):
    def __init__(
        self,
        current_page_num: int = None,
        data: List[main_models.ListUserDetailSolutionsResponseBodyData] = None,
        page_size: int = None,
        request_id: str = None,
        total_item_num: int = None,
        total_page_num: int = None,
    ):
        self.current_page_num = current_page_num
        self.data = data
        self.page_size = page_size
        self.request_id = request_id
        self.total_item_num = total_item_num
        self.total_page_num = total_page_num

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
        if self.current_page_num is not None:
            result['CurrentPageNum'] = self.current_page_num

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_item_num is not None:
            result['TotalItemNum'] = self.total_item_num

        if self.total_page_num is not None:
            result['TotalPageNum'] = self.total_page_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPageNum') is not None:
            self.current_page_num = m.get('CurrentPageNum')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListUserDetailSolutionsResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalItemNum') is not None:
            self.total_item_num = m.get('TotalItemNum')

        if m.get('TotalPageNum') is not None:
            self.total_page_num = m.get('TotalPageNum')

        return self

class ListUserDetailSolutionsResponseBodyData(DaraModel):
    def __init__(
        self,
        biz_id: str = None,
        biz_type: str = None,
        create_time: int = None,
        delivery_order_biz_id: str = None,
        ext_info: str = None,
        intention_assign_biz_id: str = None,
        intention_biz_id: str = None,
        partner_code: str = None,
        reason: str = None,
        status: int = None,
        update_time: int = None,
        user_id: str = None,
    ):
        self.biz_id = biz_id
        self.biz_type = biz_type
        self.create_time = create_time
        self.delivery_order_biz_id = delivery_order_biz_id
        self.ext_info = ext_info
        self.intention_assign_biz_id = intention_assign_biz_id
        self.intention_biz_id = intention_biz_id
        self.partner_code = partner_code
        self.reason = reason
        self.status = status
        self.update_time = update_time
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_id is not None:
            result['BizId'] = self.biz_id

        if self.biz_type is not None:
            result['BizType'] = self.biz_type

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.delivery_order_biz_id is not None:
            result['DeliveryOrderBizId'] = self.delivery_order_biz_id

        if self.ext_info is not None:
            result['ExtInfo'] = self.ext_info

        if self.intention_assign_biz_id is not None:
            result['IntentionAssignBizId'] = self.intention_assign_biz_id

        if self.intention_biz_id is not None:
            result['IntentionBizId'] = self.intention_biz_id

        if self.partner_code is not None:
            result['PartnerCode'] = self.partner_code

        if self.reason is not None:
            result['Reason'] = self.reason

        if self.status is not None:
            result['Status'] = self.status

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')

        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DeliveryOrderBizId') is not None:
            self.delivery_order_biz_id = m.get('DeliveryOrderBizId')

        if m.get('ExtInfo') is not None:
            self.ext_info = m.get('ExtInfo')

        if m.get('IntentionAssignBizId') is not None:
            self.intention_assign_biz_id = m.get('IntentionAssignBizId')

        if m.get('IntentionBizId') is not None:
            self.intention_biz_id = m.get('IntentionBizId')

        if m.get('PartnerCode') is not None:
            self.partner_code = m.get('PartnerCode')

        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

