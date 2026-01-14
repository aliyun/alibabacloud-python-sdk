# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_quickbi_public20220101 import models as main_models
from darabonba.model import DaraModel

class GetMailTaskListResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: main_models.GetMailTaskListResponseBodyResult = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.result = result
        self.success = success

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result is not None:
            result['Result'] = self.result.to_map()

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Result') is not None:
            temp_model = main_models.GetMailTaskListResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetMailTaskListResponseBodyResult(DaraModel):
    def __init__(
        self,
        data: List[main_models.GetMailTaskListResponseBodyResultData] = None,
        next: int = None,
        page_num: int = None,
        page_size: int = None,
        pre: int = None,
        total_num: int = None,
        total_pages: int = None,
    ):
        self.data = data
        self.next = next
        self.page_num = page_num
        self.page_size = page_size
        self.pre = pre
        self.total_num = total_num
        self.total_pages = total_pages

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

        if self.next is not None:
            result['Next'] = self.next

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.pre is not None:
            result['Pre'] = self.pre

        if self.total_num is not None:
            result['TotalNum'] = self.total_num

        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.GetMailTaskListResponseBodyResultData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Next') is not None:
            self.next = m.get('Next')

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Pre') is not None:
            self.pre = m.get('Pre')

        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')

        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')

        return self

class GetMailTaskListResponseBodyResultData(DaraModel):
    def __init__(
        self,
        biz_owner_name: str = None,
        biz_owner_user_id: str = None,
        mail_id: str = None,
        paused: bool = None,
        subscribe_name: str = None,
    ):
        self.biz_owner_name = biz_owner_name
        self.biz_owner_user_id = biz_owner_user_id
        self.mail_id = mail_id
        self.paused = paused
        self.subscribe_name = subscribe_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_owner_name is not None:
            result['BizOwnerName'] = self.biz_owner_name

        if self.biz_owner_user_id is not None:
            result['BizOwnerUserId'] = self.biz_owner_user_id

        if self.mail_id is not None:
            result['MailId'] = self.mail_id

        if self.paused is not None:
            result['Paused'] = self.paused

        if self.subscribe_name is not None:
            result['SubscribeName'] = self.subscribe_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizOwnerName') is not None:
            self.biz_owner_name = m.get('BizOwnerName')

        if m.get('BizOwnerUserId') is not None:
            self.biz_owner_user_id = m.get('BizOwnerUserId')

        if m.get('MailId') is not None:
            self.mail_id = m.get('MailId')

        if m.get('Paused') is not None:
            self.paused = m.get('Paused')

        if m.get('SubscribeName') is not None:
            self.subscribe_name = m.get('SubscribeName')

        return self

