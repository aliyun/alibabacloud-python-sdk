# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class ListMessageGroupResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: main_models.ListMessageGroupResponseBodyResult = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The returned result.
        self.result = result

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Result') is not None:
            temp_model = main_models.ListMessageGroupResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        return self

class ListMessageGroupResponseBodyResult(DaraModel):
    def __init__(
        self,
        group_list: List[main_models.ListMessageGroupResponseBodyResultGroupList] = None,
        has_more: bool = None,
        total: int = None,
    ):
        # The list of message groups.
        self.group_list = group_list
        # Indicates whether the current page is followed by another page. Valid values:
        # 
        # *   true: The current page is followed by another page.
        # *   false: The current page is not followed by another page.
        self.has_more = has_more
        # The total number of message groups.
        self.total = total

    def validate(self):
        if self.group_list:
            for v1 in self.group_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['GroupList'] = []
        if self.group_list is not None:
            for k1 in self.group_list:
                result['GroupList'].append(k1.to_map() if k1 else None)

        if self.has_more is not None:
            result['HasMore'] = self.has_more

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.group_list = []
        if m.get('GroupList') is not None:
            for k1 in m.get('GroupList'):
                temp_model = main_models.ListMessageGroupResponseBodyResultGroupList()
                self.group_list.append(temp_model.from_map(k1))

        if m.get('HasMore') is not None:
            self.has_more = m.get('HasMore')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class ListMessageGroupResponseBodyResultGroupList(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        create_time: int = None,
        creator_id: str = None,
        extension: Dict[str, str] = None,
        group_id: str = None,
        status: int = None,
    ):
        # The ID of the interactive messaging application.
        self.app_id = app_id
        # The time when the message group was created. The time is displayed in UTC.
        self.create_time = create_time
        # The ID of the creator.
        self.creator_id = creator_id
        # The extended field.
        self.extension = extension
        # The ID of the message group.
        self.group_id = group_id
        # The status of the message group. The default value is **1**, which indicates that the status of the message group is normal.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.creator_id is not None:
            result['CreatorId'] = self.creator_id

        if self.extension is not None:
            result['Extension'] = self.extension

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')

        if m.get('Extension') is not None:
            self.extension = m.get('Extension')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

