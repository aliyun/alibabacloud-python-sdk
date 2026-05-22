# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_computenestsupplier20210521 import models as main_models
from darabonba.model import DaraModel

class ListOpsNoticesResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        ops_notices: List[main_models.ListOpsNoticesResponseBodyOpsNotices] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.ops_notices = ops_notices
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.ops_notices:
            for v1 in self.ops_notices:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        result['OpsNotices'] = []
        if self.ops_notices is not None:
            for k1 in self.ops_notices:
                result['OpsNotices'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        self.ops_notices = []
        if m.get('OpsNotices') is not None:
            for k1 in m.get('OpsNotices'):
                temp_model = main_models.ListOpsNoticesResponseBodyOpsNotices()
                self.ops_notices.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListOpsNoticesResponseBodyOpsNotices(DaraModel):
    def __init__(
        self,
        attributes: str = None,
        category: str = None,
        content: str = None,
        notice_id: str = None,
        service_id: str = None,
        service_name: str = None,
        service_versions: List[str] = None,
        severity: str = None,
        solutions: str = None,
        start_time: str = None,
        success: str = None,
        type: str = None,
    ):
        self.attributes = attributes
        self.category = category
        self.content = content
        self.notice_id = notice_id
        self.service_id = service_id
        self.service_name = service_name
        self.service_versions = service_versions
        self.severity = severity
        self.solutions = solutions
        self.start_time = start_time
        self.success = success
        self.type = type

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

        if self.service_id is not None:
            result['ServiceId'] = self.service_id

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

        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')

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

        return self

