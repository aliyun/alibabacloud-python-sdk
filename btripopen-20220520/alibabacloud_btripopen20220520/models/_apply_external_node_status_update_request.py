# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class ApplyExternalNodeStatusUpdateRequest(DaraModel):
    def __init__(
        self,
        node_id: str = None,
        operation_records: List[main_models.ApplyExternalNodeStatusUpdateRequestOperationRecords] = None,
        process_action_result: str = None,
    ):
        # This parameter is required.
        self.node_id = node_id
        self.operation_records = operation_records
        # This parameter is required.
        self.process_action_result = process_action_result

    def validate(self):
        if self.operation_records:
            for v1 in self.operation_records:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.node_id is not None:
            result['node_id'] = self.node_id

        result['operation_records'] = []
        if self.operation_records is not None:
            for k1 in self.operation_records:
                result['operation_records'].append(k1.to_map() if k1 else None)

        if self.process_action_result is not None:
            result['process_action_result'] = self.process_action_result

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('node_id') is not None:
            self.node_id = m.get('node_id')

        self.operation_records = []
        if m.get('operation_records') is not None:
            for k1 in m.get('operation_records'):
                temp_model = main_models.ApplyExternalNodeStatusUpdateRequestOperationRecords()
                self.operation_records.append(temp_model.from_map(k1))

        if m.get('process_action_result') is not None:
            self.process_action_result = m.get('process_action_result')

        return self

class ApplyExternalNodeStatusUpdateRequestOperationRecords(DaraModel):
    def __init__(
        self,
        comment: str = None,
        operate_time: str = None,
        operator_name: str = None,
        result: str = None,
        type: str = None,
    ):
        self.comment = comment
        self.operate_time = operate_time
        self.operator_name = operator_name
        self.result = result
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comment is not None:
            result['comment'] = self.comment

        if self.operate_time is not None:
            result['operate_time'] = self.operate_time

        if self.operator_name is not None:
            result['operator_name'] = self.operator_name

        if self.result is not None:
            result['result'] = self.result

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('comment') is not None:
            self.comment = m.get('comment')

        if m.get('operate_time') is not None:
            self.operate_time = m.get('operate_time')

        if m.get('operator_name') is not None:
            self.operator_name = m.get('operator_name')

        if m.get('result') is not None:
            self.result = m.get('result')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

