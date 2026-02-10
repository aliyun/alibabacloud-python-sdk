# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeDingTalkResponseBody(DaraModel):
    def __init__(
        self,
        action_list: List[main_models.DescribeDingTalkResponseBodyActionList] = None,
        page_info: main_models.DescribeDingTalkResponseBodyPageInfo = None,
        request_id: str = None,
    ):
        # An array that consists of details of notifications.
        self.action_list = action_list
        # The pagination information.
        self.page_info = page_info
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.action_list:
            for v1 in self.action_list:
                 if v1:
                    v1.validate()
        if self.page_info:
            self.page_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ActionList'] = []
        if self.action_list is not None:
            for k1 in self.action_list:
                result['ActionList'].append(k1.to_map() if k1 else None)

        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.action_list = []
        if m.get('ActionList') is not None:
            for k1 in m.get('ActionList'):
                temp_model = main_models.DescribeDingTalkResponseBodyActionList()
                self.action_list.append(temp_model.from_map(k1))

        if m.get('PageInfo') is not None:
            temp_model = main_models.DescribeDingTalkResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m.get('PageInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeDingTalkResponseBodyPageInfo(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The page number of the returned page.
        self.current_page = current_page
        # The number of entries returned per page.
        self.page_size = page_size
        # The total number of messages.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeDingTalkResponseBodyActionList(DaraModel):
    def __init__(
        self,
        action_name: str = None,
        ali_uid: int = None,
        config_list: str = None,
        ding_talk_lang: str = None,
        gmt_create: int = None,
        gmt_modified: int = None,
        group_id_list: str = None,
        id: int = None,
        interval_time: int = None,
        status: int = None,
        url: str = None,
    ):
        # The name of the notification.
        self.action_name = action_name
        # The UID of the user.
        self.ali_uid = ali_uid
        # The list of notification settings.
        self.config_list = config_list
        # The language of the content within notifications. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        self.ding_talk_lang = ding_talk_lang
        # The creation time. unit:millisecond.
        self.gmt_create = gmt_create
        # The modification time.
        self.gmt_modified = gmt_modified
        # The group IDs.
        self.group_id_list = group_id_list
        # The ID of the notification.
        self.id = id
        # The interval at which the notifications are sent.unit:minute.
        self.interval_time = interval_time
        # The status of the notification. Valid values:
        # 
        # *   **0**: disabled
        # *   **1**: enabled
        self.status = status
        # The parameters of the notification.
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action_name is not None:
            result['ActionName'] = self.action_name

        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid

        if self.config_list is not None:
            result['ConfigList'] = self.config_list

        if self.ding_talk_lang is not None:
            result['DingTalkLang'] = self.ding_talk_lang

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.group_id_list is not None:
            result['GroupIdList'] = self.group_id_list

        if self.id is not None:
            result['Id'] = self.id

        if self.interval_time is not None:
            result['IntervalTime'] = self.interval_time

        if self.status is not None:
            result['Status'] = self.status

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionName') is not None:
            self.action_name = m.get('ActionName')

        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')

        if m.get('ConfigList') is not None:
            self.config_list = m.get('ConfigList')

        if m.get('DingTalkLang') is not None:
            self.ding_talk_lang = m.get('DingTalkLang')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('GroupIdList') is not None:
            self.group_id_list = m.get('GroupIdList')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('IntervalTime') is not None:
            self.interval_time = m.get('IntervalTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

