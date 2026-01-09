# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aiccs20191015 import models as main_models
from darabonba.model import DaraModel

class ListChatRecordDetailResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        result_data: main_models.ListChatRecordDetailResponseBodyResultData = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.result_data = result_data
        self.success = success

    def validate(self):
        if self.result_data:
            self.result_data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result_data is not None:
            result['ResultData'] = self.result_data.to_map()

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResultData') is not None:
            temp_model = main_models.ListChatRecordDetailResponseBodyResultData()
            self.result_data = temp_model.from_map(m.get('ResultData'))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListChatRecordDetailResponseBodyResultData(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        data: List[main_models.ListChatRecordDetailResponseBodyResultDataData] = None,
        one_page_size: int = None,
        total_page: int = None,
        total_results: int = None,
    ):
        self.current_page = current_page
        self.data = data
        self.one_page_size = one_page_size
        self.total_page = total_page
        self.total_results = total_results

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
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.one_page_size is not None:
            result['OnePageSize'] = self.one_page_size

        if self.total_page is not None:
            result['TotalPage'] = self.total_page

        if self.total_results is not None:
            result['TotalResults'] = self.total_results

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListChatRecordDetailResponseBodyResultDataData()
                self.data.append(temp_model.from_map(k1))

        if m.get('OnePageSize') is not None:
            self.one_page_size = m.get('OnePageSize')

        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')

        if m.get('TotalResults') is not None:
            self.total_results = m.get('TotalResults')

        return self

class ListChatRecordDetailResponseBodyResultDataData(DaraModel):
    def __init__(
        self,
        end_time: int = None,
        message_list: List[main_models.ListChatRecordDetailResponseBodyResultDataDataMessageList] = None,
        servicer_name: str = None,
        start_time: int = None,
    ):
        self.end_time = end_time
        self.message_list = message_list
        self.servicer_name = servicer_name
        self.start_time = start_time

    def validate(self):
        if self.message_list:
            for v1 in self.message_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        result['MessageList'] = []
        if self.message_list is not None:
            for k1 in self.message_list:
                result['MessageList'].append(k1.to_map() if k1 else None)

        if self.servicer_name is not None:
            result['ServicerName'] = self.servicer_name

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        self.message_list = []
        if m.get('MessageList') is not None:
            for k1 in m.get('MessageList'):
                temp_model = main_models.ListChatRecordDetailResponseBodyResultDataDataMessageList()
                self.message_list.append(temp_model.from_map(k1))

        if m.get('ServicerName') is not None:
            self.servicer_name = m.get('ServicerName')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

class ListChatRecordDetailResponseBodyResultDataDataMessageList(DaraModel):
    def __init__(
        self,
        content: str = None,
        create_time: int = None,
        msg_type: str = None,
        sender_name: str = None,
        sender_type: int = None,
    ):
        self.content = content
        self.create_time = create_time
        self.msg_type = msg_type
        self.sender_name = sender_name
        self.sender_type = sender_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.msg_type is not None:
            result['MsgType'] = self.msg_type

        if self.sender_name is not None:
            result['SenderName'] = self.sender_name

        if self.sender_type is not None:
            result['SenderType'] = self.sender_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('MsgType') is not None:
            self.msg_type = m.get('MsgType')

        if m.get('SenderName') is not None:
            self.sender_name = m.get('SenderName')

        if m.get('SenderType') is not None:
            self.sender_type = m.get('SenderType')

        return self

