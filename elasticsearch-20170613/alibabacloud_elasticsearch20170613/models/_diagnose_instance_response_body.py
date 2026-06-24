# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_elasticsearch20170613 import models as main_models
from darabonba.model import DaraModel

class DiagnoseInstanceResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: main_models.DiagnoseInstanceResponseBodyResult = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The returned result.
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
        diagnosis_mode: str = None,
        instance_id: str = None,
        items: List[main_models.DiagnoseInstanceResponseBodyResultItems] = None,
        report_id: str = None,
        state: str = None,
    ):
        # The timestamp when the diagnostic report was generated.
        self.create_time = create_time
        self.diagnosis_mode = diagnosis_mode
        # The instance ID of the diagnosed instance.
        self.instance_id = instance_id
        self.items = items
        # The report ID.
        self.report_id = report_id
        # The diagnostic status. Valid values: SUCCESS, FAILED, and RUNNING.
        self.state = state

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.diagnosis_mode is not None:
            result['diagnosisMode'] = self.diagnosis_mode

        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        result['items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['items'].append(k1.to_map() if k1 else None)

        if self.report_id is not None:
            result['reportId'] = self.report_id

        if self.state is not None:
            result['state'] = self.state

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('diagnosisMode') is not None:
            self.diagnosis_mode = m.get('diagnosisMode')

        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        self.items = []
        if m.get('items') is not None:
            for k1 in m.get('items'):
                temp_model = main_models.DiagnoseInstanceResponseBodyResultItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('reportId') is not None:
            self.report_id = m.get('reportId')

        if m.get('state') is not None:
            self.state = m.get('state')

        return self

class DiagnoseInstanceResponseBodyResultItems(DaraModel):
    def __init__(
        self,
        desc: str = None,
        detail: Dict[str, Any] = None,
        item: str = None,
        name: str = None,
        state: str = None,
        suggest: str = None,
    ):
        self.desc = desc
        self.detail = detail
        self.item = item
        self.name = name
        self.state = state
        self.suggest = suggest

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.desc is not None:
            result['desc'] = self.desc

        if self.detail is not None:
            result['detail'] = self.detail

        if self.item is not None:
            result['item'] = self.item

        if self.name is not None:
            result['name'] = self.name

        if self.state is not None:
            result['state'] = self.state

        if self.suggest is not None:
            result['suggest'] = self.suggest

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('desc') is not None:
            self.desc = m.get('desc')

        if m.get('detail') is not None:
            self.detail = m.get('detail')

        if m.get('item') is not None:
            self.item = m.get('item')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('state') is not None:
            self.state = m.get('state')

        if m.get('suggest') is not None:
            self.suggest = m.get('suggest')

        return self

