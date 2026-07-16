# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_elasticsearch20170613 import models as main_models
from darabonba.model import DaraModel

class ListDiagnoseReportResponseBody(DaraModel):
    def __init__(
        self,
        headers: main_models.ListDiagnoseReportResponseBodyHeaders = None,
        request_id: str = None,
        result: List[main_models.ListDiagnoseReportResponseBodyResult] = None,
    ):
        # The response headers.
        self.headers = headers
        # The request ID.
        self.request_id = request_id
        # The returned results.
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
        diagnosis_mode: str = None,
        health: str = None,
        instance_id: str = None,
        items: List[main_models.ListDiagnoseReportResponseBodyResultItems] = None,
        report_id: str = None,
        state: str = None,
        trigger: str = None,
    ):
        # The timestamp when the report was created.
        self.create_time = create_time
        # The list of diagnostic items in the report.
        self.diagnose_items = diagnose_items
        self.diagnosis_mode = diagnosis_mode
        # The overall health status of the cluster in the report. Valid values: GREEN, YELLOW, RED, and UNKNOWN.
        self.health = health
        # The instance ID of the diagnosed instance.
        self.instance_id = instance_id
        self.items = items
        # The report ID.
        self.report_id = report_id
        # The diagnostic status. Valid values: SUCCESS, FAILED, and RUNNING.
        self.state = state
        # The trigger method of the health diagnostics. Valid values:
        # 
        # - SYSTEM: automatically triggered by the system
        # - INNER: internally triggered
        # - USER: manually triggered by the user.
        self.trigger = trigger

    def validate(self):
        if self.diagnose_items:
            for v1 in self.diagnose_items:
                 if v1:
                    v1.validate()
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

        result['diagnoseItems'] = []
        if self.diagnose_items is not None:
            for k1 in self.diagnose_items:
                result['diagnoseItems'].append(k1.to_map() if k1 else None)

        if self.diagnosis_mode is not None:
            result['diagnosisMode'] = self.diagnosis_mode

        if self.health is not None:
            result['health'] = self.health

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

        if m.get('diagnosisMode') is not None:
            self.diagnosis_mode = m.get('diagnosisMode')

        if m.get('health') is not None:
            self.health = m.get('health')

        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        self.items = []
        if m.get('items') is not None:
            for k1 in m.get('items'):
                temp_model = main_models.ListDiagnoseReportResponseBodyResultItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('reportId') is not None:
            self.report_id = m.get('reportId')

        if m.get('state') is not None:
            self.state = m.get('state')

        if m.get('trigger') is not None:
            self.trigger = m.get('trigger')

        return self

class ListDiagnoseReportResponseBodyResultItems(DaraModel):
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

class ListDiagnoseReportResponseBodyResultDiagnoseItems(DaraModel):
    def __init__(
        self,
        detail: main_models.ListDiagnoseReportResponseBodyResultDiagnoseItemsDetail = None,
        health: str = None,
        item: str = None,
    ):
        # The details of the diagnostic item.
        self.detail = detail
        # The health status of the diagnostic item. Valid values: GREEN, YELLOW, RED, and UNKNOWN.
        self.health = health
        # The name of the diagnostic item.
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
        # The description of the diagnostic item.
        self.desc = desc
        # The full name of the diagnostic item.
        self.name = name
        # The diagnostic result.
        self.result = result
        # The diagnostic suggestion.
        self.suggest = suggest
        # The type of the diagnostic result. Valid values:
        # 
        # - TEXT: text description
        # - CONSOLE_API: console-triggered
        # - ES_API: API-triggered.
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
        # The total number of records returned.
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

