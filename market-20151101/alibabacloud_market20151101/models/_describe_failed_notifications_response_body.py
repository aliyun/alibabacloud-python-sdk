# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_market20151101 import models as main_models
from darabonba.model import DaraModel

class DescribeFailedNotificationsResponseBody(DaraModel):
    def __init__(
        self,
        notification_list: List[main_models.DescribeFailedNotificationsResponseBodyNotificationList] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.notification_list = notification_list
        self.page_number = page_number
        self.page_size = page_size
        # Id of the request
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.notification_list:
            for v1 in self.notification_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['NotificationList'] = []
        if self.notification_list is not None:
            for k1 in self.notification_list:
                result['NotificationList'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.notification_list = []
        if m.get('NotificationList') is not None:
            for k1 in m.get('NotificationList'):
                temp_model = main_models.DescribeFailedNotificationsResponseBodyNotificationList()
                self.notification_list.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeFailedNotificationsResponseBodyNotificationList(DaraModel):
    def __init__(
        self,
        action: str = None,
        create_time: int = None,
        message: str = None,
        notification_request_id: str = None,
    ):
        self.action = action
        self.create_time = create_time
        self.message = message
        self.notification_request_id = notification_request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['Action'] = self.action

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.message is not None:
            result['Message'] = self.message

        if self.notification_request_id is not None:
            result['NotificationRequestId'] = self.notification_request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('NotificationRequestId') is not None:
            self.notification_request_id = m.get('NotificationRequestId')

        return self

