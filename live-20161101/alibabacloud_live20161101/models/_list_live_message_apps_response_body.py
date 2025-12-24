# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class ListLiveMessageAppsResponseBody(DaraModel):
    def __init__(
        self,
        app_list: List[main_models.ListLiveMessageAppsResponseBodyAppList] = None,
        has_more: bool = None,
        next_page_token: int = None,
        request_id: str = None,
    ):
        # The interactive messaging applications.
        self.app_list = app_list
        # Indicates whether the current page is followed by a page.
        self.has_more = has_more
        # The starting page number for the next query. This parameter is returned only if the value of HasMore is true.
        self.next_page_token = next_page_token
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.app_list:
            for v1 in self.app_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AppList'] = []
        if self.app_list is not None:
            for k1 in self.app_list:
                result['AppList'].append(k1.to_map() if k1 else None)

        if self.has_more is not None:
            result['HasMore'] = self.has_more

        if self.next_page_token is not None:
            result['NextPageToken'] = self.next_page_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.app_list = []
        if m.get('AppList') is not None:
            for k1 in m.get('AppList'):
                temp_model = main_models.ListLiveMessageAppsResponseBodyAppList()
                self.app_list.append(temp_model.from_map(k1))

        if m.get('HasMore') is not None:
            self.has_more = m.get('HasMore')

        if m.get('NextPageToken') is not None:
            self.next_page_token = m.get('NextPageToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListLiveMessageAppsResponseBodyAppList(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        app_key: str = None,
        app_name: str = None,
        app_sign: str = None,
        create_time: int = None,
        data_center: str = None,
        disable: str = None,
        modify_time: int = None,
        msg_life_cycle: int = None,
    ):
        # The ID of the interactive messaging application queried.
        self.app_id = app_id
        # The AppKey of the interactive messaging application. It is used to authorize operations related to the application ID.
        self.app_key = app_key
        # The name of the application.
        self.app_name = app_name
        # The signature of the interactive messaging application. It is required by the interactive messaging SDK.
        self.app_sign = app_sign
        # The time when the application was created. The value is a UNIX timestamp. Unit: seconds.
        self.create_time = create_time
        # The live center.
        self.data_center = data_center
        # Indicates whether the interactive messaging application is disabled.
        self.disable = disable
        # The time when the application was last modified. The value is a UNIX timestamp. Unit: seconds.
        self.modify_time = modify_time
        # The retention period of group messages in the application. Valid values:
        # 
        # *   0 (default): 30 days
        # *   1: 90 days
        # *   2: 180 days
        self.msg_life_cycle = msg_life_cycle

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.app_key is not None:
            result['AppKey'] = self.app_key

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.app_sign is not None:
            result['AppSign'] = self.app_sign

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.data_center is not None:
            result['DataCenter'] = self.data_center

        if self.disable is not None:
            result['Disable'] = self.disable

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.msg_life_cycle is not None:
            result['MsgLifeCycle'] = self.msg_life_cycle

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('AppSign') is not None:
            self.app_sign = m.get('AppSign')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DataCenter') is not None:
            self.data_center = m.get('DataCenter')

        if m.get('Disable') is not None:
            self.disable = m.get('Disable')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('MsgLifeCycle') is not None:
            self.msg_life_cycle = m.get('MsgLifeCycle')

        return self

