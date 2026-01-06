# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class Statement(DaraModel):
    def __init__(
        self,
        aliyun_uid: int = None,
        code: str = None,
        code_state: str = None,
        code_type: str = None,
        end_time: int = None,
        error: str = None,
        have_rows: bool = None,
        output: str = None,
        resource_group: str = None,
        session_id: int = None,
        start_time: int = None,
        statement_id: int = None,
        total_count: int = None,
    ):
        self.aliyun_uid = aliyun_uid
        self.code = code
        self.code_state = code_state
        self.code_type = code_type
        self.end_time = end_time
        self.error = error
        self.have_rows = have_rows
        self.output = output
        self.resource_group = resource_group
        self.session_id = session_id
        self.start_time = start_time
        self.statement_id = statement_id
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aliyun_uid is not None:
            result['AliyunUid'] = self.aliyun_uid

        if self.code is not None:
            result['Code'] = self.code

        if self.code_state is not None:
            result['CodeState'] = self.code_state

        if self.code_type is not None:
            result['CodeType'] = self.code_type

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.error is not None:
            result['Error'] = self.error

        if self.have_rows is not None:
            result['HaveRows'] = self.have_rows

        if self.output is not None:
            result['Output'] = self.output

        if self.resource_group is not None:
            result['ResourceGroup'] = self.resource_group

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.statement_id is not None:
            result['StatementId'] = self.statement_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliyunUid') is not None:
            self.aliyun_uid = m.get('AliyunUid')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('CodeState') is not None:
            self.code_state = m.get('CodeState')

        if m.get('CodeType') is not None:
            self.code_type = m.get('CodeType')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Error') is not None:
            self.error = m.get('Error')

        if m.get('HaveRows') is not None:
            self.have_rows = m.get('HaveRows')

        if m.get('Output') is not None:
            self.output = m.get('Output')

        if m.get('ResourceGroup') is not None:
            self.resource_group = m.get('ResourceGroup')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('StatementId') is not None:
            self.statement_id = m.get('StatementId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

