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
        # The account name.
        self.account = account
        # The Milvus version number.
        self.db_version = db_version
        # The detailed information about the task.
        self.detail = detail
        # The request ID.
        self.request_id = request_id
        # The category of the source instance.
        # 
        # - **ECS**: Alibaba Cloud ECS.
        # - **other**: Other.
        self.source_category = source_category
        # The source IP address.
        self.source_ip = source_ip
        # The source MySQL port.
        self.source_port = source_port
        # The task status.
        self.status = status
        # The name of the destination disaster recovery instance for the switchover.
        self.target_instance_name = target_instance_name
        # The task ID.
        self.task_id = task_id
        # The task name.
        self.task_name = task_name
        # The task type. This parameter is used to query tasks of specific types. Separate multiple task types with commas (,). A maximum of 30 task types are supported. If this parameter is left empty, tasks of all types are queried.
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

