# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_winnexo20260512 import models as main_models
from darabonba.model import DaraModel

class ListActiveAnnouncementsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        items: List[main_models.ListActiveAnnouncementsResponseBodyItems] = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total: int = None,
    ):
        # The business status code. A value of 200 indicates success. A failure returns a backend error code (ERR.* / InvalidParameter.*).
        self.code = code
        # The list of MCP cards.
        self.items = items
        # The description of the status code.
        self.message = message
        # The page number, starting from 1.
        self.page_number = page_number
        # The page size.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries.
        self.total = total

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        result['items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['items'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['message'] = self.message

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.total is not None:
            result['total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        self.items = []
        if m.get('items') is not None:
            for k1 in m.get('items'):
                temp_model = main_models.ListActiveAnnouncementsResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('total') is not None:
            self.total = m.get('total')

        return self

class ListActiveAnnouncementsResponseBodyItems(DaraModel):
    def __init__(
        self,
        announcement_id: int = None,
        content: str = None,
        created_by: int = None,
        display_page: str = None,
        display_type: str = None,
        effective_end: str = None,
        effective_start: str = None,
        priority: str = None,
        published_at: str = None,
        status: str = None,
        title: str = None,
    ):
        # The business ID of the notice.
        self.announcement_id = announcement_id
        # The returned content.
        self.content = content
        # The user ID of the project creator.
        self.created_by = created_by
        # The display page. Valid values: ALL, FRONTEND, BACKEND.
        self.display_page = display_page
        # The display type and group label.
        self.display_type = display_type
        # The custom effective end time.
        self.effective_end = effective_end
        # The effective start time in ISO 8601 format with time zone. If this parameter is not specified, the notice takes effect immediately.
        self.effective_start = effective_start
        # The priority of the free task.
        # 
        # - Uses the default priority of the project, as shown in the following figure. The default priority values are as follows:
        # 
        #      - **-10**: Low. This is the default value.
        # 
        #      - **0**: Normal.
        # 
        #     - **1**: Urgent.
        # 
        #      - **2**: Very urgent.
        # 
        # ![](https://img.alicdn.com/imgextra/i1/O1CN01hNuSPz25juCzgxhmW_!!6000000007563-2-tps-2682-1304.png)
        # 
        # - Custom priority defined by the user, as shown in the following figure, with an additional "Generally urgent" level.
        # 
        # The value of this parameter is subject to the actual response of the API call. A higher priority corresponds to a larger value.
        # 
        # ![](https://img.alicdn.com/imgextra/i1/O1CN01V67b3i1mkNvJiW8D1_!!6000000004992-2-tps-2128-1126.png)
        self.priority = priority
        # The publish time in ISO 8601 format.
        self.published_at = published_at
        # The task status. The value Running is returned upon submission.
        self.status = status
        # The title of the scheduled meeting.
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.announcement_id is not None:
            result['announcementId'] = self.announcement_id

        if self.content is not None:
            result['content'] = self.content

        if self.created_by is not None:
            result['createdBy'] = self.created_by

        if self.display_page is not None:
            result['displayPage'] = self.display_page

        if self.display_type is not None:
            result['displayType'] = self.display_type

        if self.effective_end is not None:
            result['effectiveEnd'] = self.effective_end

        if self.effective_start is not None:
            result['effectiveStart'] = self.effective_start

        if self.priority is not None:
            result['priority'] = self.priority

        if self.published_at is not None:
            result['publishedAt'] = self.published_at

        if self.status is not None:
            result['status'] = self.status

        if self.title is not None:
            result['title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('announcementId') is not None:
            self.announcement_id = m.get('announcementId')

        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('createdBy') is not None:
            self.created_by = m.get('createdBy')

        if m.get('displayPage') is not None:
            self.display_page = m.get('displayPage')

        if m.get('displayType') is not None:
            self.display_type = m.get('displayType')

        if m.get('effectiveEnd') is not None:
            self.effective_end = m.get('effectiveEnd')

        if m.get('effectiveStart') is not None:
            self.effective_start = m.get('effectiveStart')

        if m.get('priority') is not None:
            self.priority = m.get('priority')

        if m.get('publishedAt') is not None:
            self.published_at = m.get('publishedAt')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('title') is not None:
            self.title = m.get('title')

        return self

