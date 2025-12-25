# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_aimiaobi20230801 import models as main_models
from darabonba.model import DaraModel

class ListInterveneCntResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ListInterveneCntResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.ListInterveneCntResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListInterveneCntResponseBodyData(DaraModel):
    def __init__(
        self,
        cnt_list: List[Any] = None,
        code: int = None,
        page_cnt: int = None,
        page_index: int = None,
        page_size: int = None,
    ):
        self.cnt_list = cnt_list
        self.code = code
        self.page_cnt = page_cnt
        self.page_index = page_index
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cnt_list is not None:
            result['CntList'] = self.cnt_list

        if self.code is not None:
            result['Code'] = self.code

        if self.page_cnt is not None:
            result['PageCnt'] = self.page_cnt

        if self.page_index is not None:
            result['PageIndex'] = self.page_index

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CntList') is not None:
            self.cnt_list = m.get('CntList')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('PageCnt') is not None:
            self.page_cnt = m.get('PageCnt')

        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

