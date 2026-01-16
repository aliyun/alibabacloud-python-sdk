# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_elasticsearch20170613 import models as main_models
from darabonba.model import DaraModel

class DescribeDiagnoseReportResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: main_models.DescribeDiagnoseReportResponseBodyResult = None,
    ):
        self.request_id = request_id
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
            temp_model = main_models.DescribeDiagnoseReportResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        return self

class DescribeDiagnoseReportResponseBodyResult(DaraModel):
    def __init__(
        self,
        create_time: int = None,
        diagnose_items: List[main_models.DescribeDiagnoseReportResponseBodyResultDiagnoseItems] = None,
        health: str = None,
        instance_id: str = None,
        report_id: str = None,
        state: str = None,
        trigger: str = None,
    ):
        self.create_time = create_time
        self.diagnose_items = diagnose_items
        self.health = health
        self.instance_id = instance_id
        self.report_id = report_id
        self.state = state
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
                temp_model = main_models.DescribeDiagnoseReportResponseBodyResultDiagnoseItems()
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

class DescribeDiagnoseReportResponseBodyResultDiagnoseItems(DaraModel):
    def __init__(
        self,
        detail: main_models.DescribeDiagnoseReportResponseBodyResultDiagnoseItemsDetail = None,
        health: str = None,
        item: str = None,
    ):
        self.detail = detail
        self.health = health
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
            temp_model = main_models.DescribeDiagnoseReportResponseBodyResultDiagnoseItemsDetail()
            self.detail = temp_model.from_map(m.get('detail'))

        if m.get('health') is not None:
            self.health = m.get('health')

        if m.get('item') is not None:
            self.item = m.get('item')

        return self

class DescribeDiagnoseReportResponseBodyResultDiagnoseItemsDetail(DaraModel):
    def __init__(
        self,
        desc: str = None,
        name: str = None,
        result: str = None,
        suggest: str = None,
        type: str = None,
    ):
        self.desc = desc
        self.name = name
        self.result = result
        self.suggest = suggest
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

