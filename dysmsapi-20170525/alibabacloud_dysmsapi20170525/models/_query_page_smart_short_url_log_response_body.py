# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dysmsapi20170525 import models as main_models
from darabonba.model import DaraModel

class QueryPageSmartShortUrlLogResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        model: main_models.QueryPageSmartShortUrlLogResponseBodyModel = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.model = model
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.model:
            self.model.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.model is not None:
            result['Model'] = self.model.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Model') is not None:
            temp_model = main_models.QueryPageSmartShortUrlLogResponseBodyModel()
            self.model = temp_model.from_map(m.get('Model'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryPageSmartShortUrlLogResponseBodyModel(DaraModel):
    def __init__(
        self,
        list: List[main_models.QueryPageSmartShortUrlLogResponseBodyModelList] = None,
        page_no: int = None,
        page_size: int = None,
        total_count: int = None,
        total_page: int = None,
    ):
        self.list = list
        self.page_no = page_no
        self.page_size = page_size
        self.total_count = total_count
        self.total_page = total_page

    def validate(self):
        if self.list:
            for v1 in self.list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['List'] = []
        if self.list is not None:
            for k1 in self.list:
                result['List'].append(k1.to_map() if k1 else None)

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.total_page is not None:
            result['TotalPage'] = self.total_page

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k1 in m.get('List'):
                temp_model = main_models.QueryPageSmartShortUrlLogResponseBodyModelList()
                self.list.append(temp_model.from_map(k1))

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')

        return self

class QueryPageSmartShortUrlLogResponseBodyModelList(DaraModel):
    def __init__(
        self,
        click_state: int = None,
        click_time: int = None,
        create_time: int = None,
        phone_number: str = None,
        short_name: str = None,
        short_url: str = None,
    ):
        self.click_state = click_state
        self.click_time = click_time
        self.create_time = create_time
        self.phone_number = phone_number
        self.short_name = short_name
        self.short_url = short_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.click_state is not None:
            result['ClickState'] = self.click_state

        if self.click_time is not None:
            result['ClickTime'] = self.click_time

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number

        if self.short_name is not None:
            result['ShortName'] = self.short_name

        if self.short_url is not None:
            result['ShortUrl'] = self.short_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClickState') is not None:
            self.click_state = m.get('ClickState')

        if m.get('ClickTime') is not None:
            self.click_time = m.get('ClickTime')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')

        if m.get('ShortName') is not None:
            self.short_name = m.get('ShortName')

        if m.get('ShortUrl') is not None:
            self.short_url = m.get('ShortUrl')

        return self

