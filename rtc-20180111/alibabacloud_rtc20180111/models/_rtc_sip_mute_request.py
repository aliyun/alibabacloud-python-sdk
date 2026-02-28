# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rtc20180111 import models as main_models
from darabonba.model import DaraModel

class RtcSipMuteRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        channel_id: str = None,
        operations: List[main_models.RtcSipMuteRequestOperations] = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        # This parameter is required.
        self.channel_id = channel_id
        # This parameter is required.
        self.operations = operations

    def validate(self):
        if self.operations:
            for v1 in self.operations:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id

        result['Operations'] = []
        if self.operations is not None:
            for k1 in self.operations:
                result['Operations'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')

        self.operations = []
        if m.get('Operations') is not None:
            for k1 in m.get('Operations'):
                temp_model = main_models.RtcSipMuteRequestOperations()
                self.operations.append(temp_model.from_map(k1))

        return self

class RtcSipMuteRequestOperations(DaraModel):
    def __init__(
        self,
        ids: List[str] = None,
        op: str = None,
        operation_id: str = None,
        path: str = None,
        value: main_models.RtcSipMuteRequestOperationsValue = None,
    ):
        # This parameter is required.
        self.ids = ids
        # This parameter is required.
        self.op = op
        # This parameter is required.
        self.operation_id = operation_id
        # This parameter is required.
        self.path = path
        # This parameter is required.
        self.value = value

    def validate(self):
        if self.value:
            self.value.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ids is not None:
            result['Ids'] = self.ids

        if self.op is not None:
            result['Op'] = self.op

        if self.operation_id is not None:
            result['OperationId'] = self.operation_id

        if self.path is not None:
            result['Path'] = self.path

        if self.value is not None:
            result['Value'] = self.value.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ids') is not None:
            self.ids = m.get('Ids')

        if m.get('Op') is not None:
            self.op = m.get('Op')

        if m.get('OperationId') is not None:
            self.operation_id = m.get('OperationId')

        if m.get('Path') is not None:
            self.path = m.get('Path')

        if m.get('Value') is not None:
            temp_model = main_models.RtcSipMuteRequestOperationsValue()
            self.value = temp_model.from_map(m.get('Value'))

        return self

class RtcSipMuteRequestOperationsValue(DaraModel):
    def __init__(
        self,
        status: str = None,
    ):
        # This parameter is required.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

