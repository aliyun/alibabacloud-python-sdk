# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetTaskResponseBody(DaraModel):
    def __init__(
        self,
        config: str = None,
        gmt_create_time: str = None,
        gmt_executed_time: str = None,
        gmt_finished_time: str = None,
        gmt_modified_time: str = None,
        object_id: str = None,
        object_type: str = None,
        project_id: str = None,
        project_name: str = None,
        request_id: str = None,
        running_config: str = None,
        status: str = None,
        type: str = None,
    ):
        self.config = config
        self.gmt_create_time = gmt_create_time
        self.gmt_executed_time = gmt_executed_time
        self.gmt_finished_time = gmt_finished_time
        self.gmt_modified_time = gmt_modified_time
        self.object_id = object_id
        self.object_type = object_type
        self.project_id = project_id
        self.project_name = project_name
        self.request_id = request_id
        self.running_config = running_config
        self.status = status
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config is not None:
            result['Config'] = self.config

        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time

        if self.gmt_executed_time is not None:
            result['GmtExecutedTime'] = self.gmt_executed_time

        if self.gmt_finished_time is not None:
            result['GmtFinishedTime'] = self.gmt_finished_time

        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time

        if self.object_id is not None:
            result['ObjectId'] = self.object_id

        if self.object_type is not None:
            result['ObjectType'] = self.object_type

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.running_config is not None:
            result['RunningConfig'] = self.running_config

        if self.status is not None:
            result['Status'] = self.status

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')

        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')

        if m.get('GmtExecutedTime') is not None:
            self.gmt_executed_time = m.get('GmtExecutedTime')

        if m.get('GmtFinishedTime') is not None:
            self.gmt_finished_time = m.get('GmtFinishedTime')

        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')

        if m.get('ObjectId') is not None:
            self.object_id = m.get('ObjectId')

        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RunningConfig') is not None:
            self.running_config = m.get('RunningConfig')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

