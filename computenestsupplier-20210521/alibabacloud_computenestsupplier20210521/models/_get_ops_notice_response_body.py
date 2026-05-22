# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class GetOpsNoticeResponseBody(DaraModel):
    def __init__(
        self,
        attributes: str = None,
        category: str = None,
        content: str = None,
        notice_id: str = None,
        request_id: str = None,
        service_id: str = None,
        service_instance_count: str = None,
        service_name: str = None,
        service_versions: List[str] = None,
        severity: str = None,
        solutions: str = None,
        start_time: str = None,
        success: str = None,
        type: str = None,
        user_count: str = None,
    ):
        self.attributes = attributes
        self.category = category
        self.content = content
        self.notice_id = notice_id
        self.request_id = request_id
        self.service_id = service_id
        self.service_instance_count = service_instance_count
        self.service_name = service_name
        self.service_versions = service_versions
        self.severity = severity
        self.solutions = solutions
        self.start_time = start_time
        self.success = success
        self.type = type
        self.user_count = user_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attributes is not None:
            result['Attributes'] = self.attributes

        if self.category is not None:
            result['Category'] = self.category

        if self.content is not None:
            result['Content'] = self.content

        if self.notice_id is not None:
            result['NoticeId'] = self.notice_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.service_id is not None:
            result['ServiceId'] = self.service_id

        if self.service_instance_count is not None:
            result['ServiceInstanceCount'] = self.service_instance_count

        if self.service_name is not None:
            result['ServiceName'] = self.service_name

        if self.service_versions is not None:
            result['ServiceVersions'] = self.service_versions

        if self.severity is not None:
            result['Severity'] = self.severity

        if self.solutions is not None:
            result['Solutions'] = self.solutions

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.success is not None:
            result['Success'] = self.success

        if self.type is not None:
            result['Type'] = self.type

        if self.user_count is not None:
            result['UserCount'] = self.user_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Attributes') is not None:
            self.attributes = m.get('Attributes')

        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('NoticeId') is not None:
            self.notice_id = m.get('NoticeId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')

        if m.get('ServiceInstanceCount') is not None:
            self.service_instance_count = m.get('ServiceInstanceCount')

        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')

        if m.get('ServiceVersions') is not None:
            self.service_versions = m.get('ServiceVersions')

        if m.get('Severity') is not None:
            self.severity = m.get('Severity')

        if m.get('Solutions') is not None:
            self.solutions = m.get('Solutions')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('UserCount') is not None:
            self.user_count = m.get('UserCount')

        return self

