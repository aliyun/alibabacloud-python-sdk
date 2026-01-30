# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vs20181212 import models as main_models
from darabonba.model import DaraModel

class ListFilePushStatusesResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        push_statuses: List[main_models.ListFilePushStatusesResponseBodyPushStatuses] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.push_statuses = push_statuses
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.push_statuses:
            for v1 in self.push_statuses:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        result['PushStatuses'] = []
        if self.push_statuses is not None:
            for k1 in self.push_statuses:
                result['PushStatuses'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        self.push_statuses = []
        if m.get('PushStatuses') is not None:
            for k1 in m.get('PushStatuses'):
                temp_model = main_models.ListFilePushStatusesResponseBodyPushStatuses()
                self.push_statuses.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListFilePushStatusesResponseBodyPushStatuses(DaraModel):
    def __init__(
        self,
        file_id: str = None,
        file_name: str = None,
        push_time: str = None,
        rendering_instance_id: str = None,
        status: str = None,
        status_description: str = None,
        update_time: str = None,
    ):
        self.file_id = file_id
        self.file_name = file_name
        self.push_time = push_time
        self.rendering_instance_id = rendering_instance_id
        self.status = status
        self.status_description = status_description
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_id is not None:
            result['FileId'] = self.file_id

        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.push_time is not None:
            result['PushTime'] = self.push_time

        if self.rendering_instance_id is not None:
            result['RenderingInstanceId'] = self.rendering_instance_id

        if self.status is not None:
            result['Status'] = self.status

        if self.status_description is not None:
            result['StatusDescription'] = self.status_description

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('PushTime') is not None:
            self.push_time = m.get('PushTime')

        if m.get('RenderingInstanceId') is not None:
            self.rendering_instance_id = m.get('RenderingInstanceId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StatusDescription') is not None:
            self.status_description = m.get('StatusDescription')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

