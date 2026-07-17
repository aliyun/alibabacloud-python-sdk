# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class ListBotInstancesResponseBody(DaraModel):
    def __init__(
        self,
        instance_info: List[main_models.ListBotInstancesResponseBodyInstanceInfo] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
        total_page: int = None,
    ):
        # The instances that match the specified conditions under the current account.
        self.instance_info = instance_info
        # The current page number, which is the same as the PageNumber request parameter.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries.
        self.total_count = total_count
        # The total number of pages.
        self.total_page = total_page

    def validate(self):
        if self.instance_info:
            for v1 in self.instance_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['InstanceInfo'] = []
        if self.instance_info is not None:
            for k1 in self.instance_info:
                result['InstanceInfo'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.total_page is not None:
            result['TotalPage'] = self.total_page

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance_info = []
        if m.get('InstanceInfo') is not None:
            for k1 in m.get('InstanceInfo'):
                temp_model = main_models.ListBotInstancesResponseBodyInstanceInfo()
                self.instance_info.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')

        return self

class ListBotInstancesResponseBodyInstanceInfo(DaraModel):
    def __init__(
        self,
        bot_instance_level: str = None,
        create_time: str = None,
        instance_id: str = None,
        reserve_release_time: str = None,
        site_instance_id: str = None,
        status: str = None,
    ):
        # The Bot protection instance level. If this parameter is empty, the plan does not include a Bot protection instance. If a value is returned, the plan includes a Bot protection instance. Valid values:
        # 
        # - enterprise_bot: web edition.
        # 
        # - enterprise_bot_with_app: app edition.
        self.bot_instance_level = bot_instance_level
        # The time when the instance was purchased. The time is in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.create_time = create_time
        # The instance ID.
        self.instance_id = instance_id
        # The scheduled release time. The time is in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.reserve_release_time = reserve_release_time
        # The ID of the associated site plan instance.
        self.site_instance_id = site_instance_id
        # The instance status. Valid values:
        # - **online**: The instance is running normally.
        # - **offline**: The instance has expired but has not exceeded the retention period and is unavailable.
        # - **disable**: The instance has been released.
        # - **overdue**: The instance has been stopped due to an overdue payment.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bot_instance_level is not None:
            result['BotInstanceLevel'] = self.bot_instance_level

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.reserve_release_time is not None:
            result['ReserveReleaseTime'] = self.reserve_release_time

        if self.site_instance_id is not None:
            result['SiteInstanceId'] = self.site_instance_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BotInstanceLevel') is not None:
            self.bot_instance_level = m.get('BotInstanceLevel')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('ReserveReleaseTime') is not None:
            self.reserve_release_time = m.get('ReserveReleaseTime')

        if m.get('SiteInstanceId') is not None:
            self.site_instance_id = m.get('SiteInstanceId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

