# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_elasticsearch20170613 import models as main_models
from darabonba.model import DaraModel

class ListDiagnoseReportResponseBody(DaraModel):
    def __init__(
        self,
        headers: main_models.ListDiagnoseReportResponseBodyHeaders = None,
        request_id: str = None,
        result: List[main_models.ListDiagnoseReportResponseBodyResult] = None,
    ):
        # The total number of entries returned.
        self.headers = headers
        # The header of the response.
        self.request_id = request_id
        # The trigger mode of health diagnostics. Valid values:
        # 
        # *   SYSTEM: The system is automatically triggered.
        # *   INNER: internal trigger
        # *   USER: manually triggered by the user
        self.result = result

    def validate(self):
        if self.headers:
            self.headers.validate()
        if self.result:
            for v1 in self.result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.headers is not None:
            result['Headers'] = self.headers.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['Result'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Headers') is not None:
            temp_model = main_models.ListDiagnoseReportResponseBodyHeaders()
            self.headers = temp_model.from_map(m.get('Headers'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.result = []
        if m.get('Result') is not None:
            for k1 in m.get('Result'):
                temp_model = main_models.ListDiagnoseReportResponseBodyResult()
                self.result.append(temp_model.from_map(k1))

        return self

class ListDiagnoseReportResponseBodyResult(DaraModel):
    def __init__(
        self,
        create_time: int = None,
        diagnose_items: List[main_models.ListDiagnoseReportResponseBodyResultDiagnoseItems] = None,
        health: str = None,
        instance_id: str = None,
        report_id: str = None,
        state: str = None,
        trigger: str = None,
    ):
        # The ID of the report.
        self.create_time = create_time
        # The name of the item.
        self.diagnose_items = diagnose_items
        # Reports the list of diagnostic item information.
        self.health = health
        # The overall health of the cluster in the report. Supported: GREEN, YELLOW, RED, and UNKNOWN.
        self.instance_id = instance_id
        # The diagnosis status. Valid values: Supported: SUCCESS, FAILED, and RUNNING.
        self.report_id = report_id
        # The ID of the instance for diagnosis.
        self.state = state
        # The timestamp when the report was created.
        self.trigger = trigger

    def validate(self):
        if self.diagnose_items:
            for v1 in self.diagnose_items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['createTime'] = self.create_time

        result['diagnoseItems'] = []
        if self.diagnose_items is not None:
            for k1 in self.diagnose_items:
                result['diagnoseItems'].append(k1.to_map() if k1 else None)

        if self.health is not None:
            result['health'] = self.health

        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        if self.report_id is not None:
            result['reportId'] = self.report_id

        if self.state is not None:
            result['state'] = self.state

        if self.trigger is not None:
            result['trigger'] = self.trigger

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        self.diagnose_items = []
        if m.get('diagnoseItems') is not None:
            for k1 in m.get('diagnoseItems'):
                temp_model = main_models.ListDiagnoseReportResponseBodyResultDiagnoseItems()
                self.diagnose_items.append(temp_model.from_map(k1))

        if m.get('health') is not None:
            self.health = m.get('health')

        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        if m.get('reportId') is not None:
            self.report_id = m.get('reportId')

        if m.get('state') is not None:
            self.state = m.get('state')

        if m.get('trigger') is not None:
            self.trigger = m.get('trigger')

        return self

class ListDiagnoseReportResponseBodyResultDiagnoseItems(DaraModel):
    def __init__(
        self,
        detail: main_models.ListDiagnoseReportResponseBodyResultDiagnoseItemsDetail = None,
        health: str = None,
        item: str = None,
    ):
        # The type of the diagnostic result. Valid values:
        # 
        # *   TEXT: text description
        # *   CONSOLE_API: console-triggered
        # *   ES_API: API triggered
        self.detail = detail
        # The details of the diagnostic item.
        self.health = health
        # The health of the diagnostic item. Supported: GREEN, YELLOW, RED, and UNKNOWN.
        self.item = item

    def validate(self):
        if self.detail:
            self.detail.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.detail is not None:
            result['detail'] = self.detail.to_map()

        if self.health is not None:
            result['health'] = self.health

        if self.item is not None:
            result['item'] = self.item

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('detail') is not None:
            temp_model = main_models.ListDiagnoseReportResponseBodyResultDiagnoseItemsDetail()
            self.detail = temp_model.from_map(m.get('detail'))

        if m.get('health') is not None:
            self.health = m.get('health')

        if m.get('item') is not None:
            self.item = m.get('item')

        return self

class ListDiagnoseReportResponseBodyResultDiagnoseItemsDetail(DaraModel):
    def __init__(
        self,
        desc: str = None,
        name: str = None,
        result: str = None,
        suggest: str = None,
        type: str = None,
    ):
        # The diagnosis.
        self.desc = desc
        # The description of the diagnostic item.
        self.name = name
        # The suggestion for the diagnosis.
        self.result = result
        self.suggest = suggest
        # The full name of the diagnostic item.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.desc is not None:
            result['desc'] = self.desc

        if self.name is not None:
            result['name'] = self.name

        if self.result is not None:
            result['result'] = self.result

        if self.suggest is not None:
            result['suggest'] = self.suggest

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('desc') is not None:
            self.desc = m.get('desc')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('result') is not None:
            self.result = m.get('result')

        if m.get('suggest') is not None:
            self.suggest = m.get('suggest')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class ListDiagnoseReportResponseBodyHeaders(DaraModel):
    def __init__(
        self,
        x_total_count: int = None,
    ):
        # The returned results.
        self.x_total_count = x_total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.x_total_count is not None:
            result['X-Total-Count'] = self.x_total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('X-Total-Count') is not None:
            self.x_total_count = m.get('X-Total-Count')

        return self

