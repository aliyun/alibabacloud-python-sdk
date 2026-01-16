# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_elasticsearch20170613 import models as main_models
from darabonba.model import DaraModel

class DiagnoseInstanceResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: main_models.DiagnoseInstanceResponseBodyResult = None,
    ):
        # The ID of the report.
        self.request_id = request_id
        # The diagnosis status. Valid values: Supported: SUCCESS, FAILED, and RUNNING.
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result is not None:
            result['Result'] = self.result.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Result') is not None:
            temp_model = main_models.DiagnoseInstanceResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        return self

class DiagnoseInstanceResponseBodyResult(DaraModel):
    def __init__(
        self,
        create_time: int = None,
        instance_id: str = None,
        report_id: str = None,
        state: str = None,
    ):
        # The ID of the diagnostic instance.
        self.create_time = create_time
        self.instance_id = instance_id
        self.report_id = report_id
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        if self.report_id is not None:
            result['reportId'] = self.report_id

        if self.state is not None:
            result['state'] = self.state

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        if m.get('reportId') is not None:
            self.report_id = m.get('reportId')

        if m.get('state') is not None:
            self.state = m.get('state')

        return self

