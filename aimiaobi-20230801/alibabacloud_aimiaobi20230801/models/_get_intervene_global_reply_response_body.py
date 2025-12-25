# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aimiaobi20230801 import models as main_models
from darabonba.model import DaraModel

class GetInterveneGlobalReplyResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetInterveneGlobalReplyResponseBodyData = None,
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
            temp_model = main_models.GetInterveneGlobalReplyResponseBodyData()
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

class GetInterveneGlobalReplyResponseBodyData(DaraModel):
    def __init__(
        self,
        code: int = None,
        reply_messag_list: List[main_models.GetInterveneGlobalReplyResponseBodyDataReplyMessagList] = None,
    ):
        self.code = code
        self.reply_messag_list = reply_messag_list

    def validate(self):
        if self.reply_messag_list:
            for v1 in self.reply_messag_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        result['ReplyMessagList'] = []
        if self.reply_messag_list is not None:
            for k1 in self.reply_messag_list:
                result['ReplyMessagList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.reply_messag_list = []
        if m.get('ReplyMessagList') is not None:
            for k1 in m.get('ReplyMessagList'):
                temp_model = main_models.GetInterveneGlobalReplyResponseBodyDataReplyMessagList()
                self.reply_messag_list.append(temp_model.from_map(k1))

        return self

class GetInterveneGlobalReplyResponseBodyDataReplyMessagList(DaraModel):
    def __init__(
        self,
        message: str = None,
        reply_type: str = None,
    ):
        self.message = message
        self.reply_type = reply_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.message is not None:
            result['Message'] = self.message

        if self.reply_type is not None:
            result['ReplyType'] = self.reply_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('ReplyType') is not None:
            self.reply_type = m.get('ReplyType')

        return self

