# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_companyreg20200306 import models as main_models
from darabonba.model import DaraModel

class ListUserProduceOperateLogsResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.ListUserProduceOperateLogsResponseBodyData] = None,
        page_num: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_item_num: int = None,
        total_page_num: int = None,
    ):
        self.data = data
        self.page_num = page_num
        self.page_size = page_size
        self.request_id = request_id
        self.success = success
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
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total_item_num is not None:
            result['TotalItemNum'] = self.total_item_num

        if self.total_page_num is not None:
            result['TotalPageNum'] = self.total_page_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListUserProduceOperateLogsResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalItemNum') is not None:
            self.total_item_num = m.get('TotalItemNum')

        if m.get('TotalPageNum') is not None:
            self.total_page_num = m.get('TotalPageNum')

        return self

class ListUserProduceOperateLogsResponseBodyData(DaraModel):
    def __init__(
        self,
        biz_id: str = None,
        biz_status: int = None,
        biz_type: str = None,
        note: str = None,
        operate_name: str = None,
        operate_time: int = None,
        operate_user_type: str = None,
        to_biz_status: int = None,
    ):
        self.biz_id = biz_id
        self.biz_status = biz_status
        self.biz_type = biz_type
        self.note = note
        self.operate_name = operate_name
        self.operate_time = operate_time
        self.operate_user_type = operate_user_type
        self.to_biz_status = to_biz_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_id is not None:
            result['BizId'] = self.biz_id

        if self.biz_status is not None:
            result['BizStatus'] = self.biz_status

        if self.biz_type is not None:
            result['BizType'] = self.biz_type

        if self.note is not None:
            result['Note'] = self.note

        if self.operate_name is not None:
            result['OperateName'] = self.operate_name

        if self.operate_time is not None:
            result['OperateTime'] = self.operate_time

        if self.operate_user_type is not None:
            result['OperateUserType'] = self.operate_user_type

        if self.to_biz_status is not None:
            result['ToBizStatus'] = self.to_biz_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')

        if m.get('BizStatus') is not None:
            self.biz_status = m.get('BizStatus')

        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')

        if m.get('Note') is not None:
            self.note = m.get('Note')

        if m.get('OperateName') is not None:
            self.operate_name = m.get('OperateName')

        if m.get('OperateTime') is not None:
            self.operate_time = m.get('OperateTime')

        if m.get('OperateUserType') is not None:
            self.operate_user_type = m.get('OperateUserType')

        if m.get('ToBizStatus') is not None:
            self.to_biz_status = m.get('ToBizStatus')

        return self

