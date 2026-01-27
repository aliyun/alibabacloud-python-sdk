# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeImportTaskResponseBody(DaraModel):
    def __init__(
        self,
        account: str = None,
        db_version: str = None,
        detail: str = None,
        request_id: str = None,
        source_category: str = None,
        source_ip: str = None,
        source_port: str = None,
        status: str = None,
        target_instance_name: str = None,
        task_id: int = None,
        task_name: str = None,
        task_type: str = None,
    ):
        self.account = account
        self.db_version = db_version
        self.detail = detail
        self.request_id = request_id
        self.source_category = source_category
        self.source_ip = source_ip
        self.source_port = source_port
        self.status = status
        self.target_instance_name = target_instance_name
        self.task_id = task_id
        self.task_name = task_name
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account is not None:
            result['Account'] = self.account

        if self.db_version is not None:
            result['DbVersion'] = self.db_version

        if self.detail is not None:
            result['Detail'] = self.detail

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.source_category is not None:
            result['SourceCategory'] = self.source_category

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        if self.source_port is not None:
            result['SourcePort'] = self.source_port

        if self.status is not None:
            result['Status'] = self.status

        if self.target_instance_name is not None:
            result['TargetInstanceName'] = self.target_instance_name

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Account') is not None:
            self.account = m.get('Account')

        if m.get('DbVersion') is not None:
            self.db_version = m.get('DbVersion')

        if m.get('Detail') is not None:
            self.detail = m.get('Detail')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SourceCategory') is not None:
            self.source_category = m.get('SourceCategory')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        if m.get('SourcePort') is not None:
            self.source_port = m.get('SourcePort')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TargetInstanceName') is not None:
            self.target_instance_name = m.get('TargetInstanceName')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        return self

