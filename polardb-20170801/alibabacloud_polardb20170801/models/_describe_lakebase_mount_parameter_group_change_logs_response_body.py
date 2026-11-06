# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribeLakebaseMountParameterGroupChangeLogsResponseBody(DaraModel):
    def __init__(
        self,
        change_logs: List[main_models.DescribeLakebaseMountParameterGroupChangeLogsResponseBodyChangeLogs] = None,
        request_id: str = None,
    ):
        # The change records, sorted in descending order by CreateTime. An empty array is returned if no data is found.
        self.change_logs = change_logs
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.change_logs:
            for v1 in self.change_logs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ChangeLogs'] = []
        if self.change_logs is not None:
            for k1 in self.change_logs:
                result['ChangeLogs'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.change_logs = []
        if m.get('ChangeLogs') is not None:
            for k1 in m.get('ChangeLogs'):
                temp_model = main_models.DescribeLakebaseMountParameterGroupChangeLogsResponseBodyChangeLogs()
                self.change_logs.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeLakebaseMountParameterGroupChangeLogsResponseBodyChangeLogs(DaraModel):
    def __init__(
        self,
        change_type: str = None,
        create_time: str = None,
        creator: str = None,
        is_apply: str = None,
        modify_time: str = None,
        new_value: str = None,
        old_value: str = None,
        parameter_name: str = None,
    ):
        # The change type. Valid values: create, modify, and delete.
        self.change_type = change_type
        # The creation time (UTC).
        self.create_time = create_time
        # The ID of the user who performed the operation.
        self.creator = creator
        # Indicates whether the change has been applied. Valid values: 0 (no) and 1 (yes).
        self.is_apply = is_apply
        # The modification time (UTC).
        self.modify_time = modify_time
        # The new value after the change. This parameter is empty for delete operations.
        self.new_value = new_value
        # The old value before the change. This parameter is empty for create operations.
        self.old_value = old_value
        # The parameter name.
        self.parameter_name = parameter_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.change_type is not None:
            result['ChangeType'] = self.change_type

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.creator is not None:
            result['Creator'] = self.creator

        if self.is_apply is not None:
            result['IsApply'] = self.is_apply

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.new_value is not None:
            result['NewValue'] = self.new_value

        if self.old_value is not None:
            result['OldValue'] = self.old_value

        if self.parameter_name is not None:
            result['ParameterName'] = self.parameter_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChangeType') is not None:
            self.change_type = m.get('ChangeType')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Creator') is not None:
            self.creator = m.get('Creator')

        if m.get('IsApply') is not None:
            self.is_apply = m.get('IsApply')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('NewValue') is not None:
            self.new_value = m.get('NewValue')

        if m.get('OldValue') is not None:
            self.old_value = m.get('OldValue')

        if m.get('ParameterName') is not None:
            self.parameter_name = m.get('ParameterName')

        return self

