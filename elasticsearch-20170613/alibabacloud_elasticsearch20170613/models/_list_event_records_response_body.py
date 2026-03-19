# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_elasticsearch20170613 import models as main_models
from darabonba.model import DaraModel

class ListEventRecordsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: main_models.ListEventRecordsResponseBodyResult = None,
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
            temp_model = main_models.ListEventRecordsResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        return self

class ListEventRecordsResponseBodyResult(DaraModel):
    def __init__(
        self,
        result: List[main_models.ListEventRecordsResponseBodyResultResult] = None,
        total: str = None,
    ):
        self.result = result
        self.total = total

    def validate(self):
        if self.result:
            for v1 in self.result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['result'].append(k1.to_map() if k1 else None)

        if self.total is not None:
            result['total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.result = []
        if m.get('result') is not None:
            for k1 in m.get('result'):
                temp_model = main_models.ListEventRecordsResponseBodyResultResult()
                self.result.append(temp_model.from_map(k1))

        if m.get('total') is not None:
            self.total = m.get('total')

        return self

class ListEventRecordsResponseBodyResultResult(DaraModel):
    def __init__(
        self,
        auto_alarm: bool = None,
        display_name: str = None,
        dry_run: bool = None,
        level: str = None,
        must_ops: bool = None,
        product: str = None,
        schedule_execute_time: str = None,
        schedule_finish_time: str = None,
        show_content: main_models.ListEventRecordsResponseBodyResultResultShowContent = None,
        source: str = None,
        status: str = None,
        type: str = None,
    ):
        self.auto_alarm = auto_alarm
        self.display_name = display_name
        self.dry_run = dry_run
        self.level = level
        self.must_ops = must_ops
        self.product = product
        self.schedule_execute_time = schedule_execute_time
        self.schedule_finish_time = schedule_finish_time
        self.show_content = show_content
        self.source = source
        self.status = status
        self.type = type

    def validate(self):
        if self.show_content:
            self.show_content.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_alarm is not None:
            result['autoAlarm'] = self.auto_alarm

        if self.display_name is not None:
            result['displayName'] = self.display_name

        if self.dry_run is not None:
            result['dryRun'] = self.dry_run

        if self.level is not None:
            result['level'] = self.level

        if self.must_ops is not None:
            result['mustOps'] = self.must_ops

        if self.product is not None:
            result['product'] = self.product

        if self.schedule_execute_time is not None:
            result['scheduleExecuteTime'] = self.schedule_execute_time

        if self.schedule_finish_time is not None:
            result['scheduleFinishTime'] = self.schedule_finish_time

        if self.show_content is not None:
            result['showContent'] = self.show_content.to_map()

        if self.source is not None:
            result['source'] = self.source

        if self.status is not None:
            result['status'] = self.status

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('autoAlarm') is not None:
            self.auto_alarm = m.get('autoAlarm')

        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')

        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')

        if m.get('level') is not None:
            self.level = m.get('level')

        if m.get('mustOps') is not None:
            self.must_ops = m.get('mustOps')

        if m.get('product') is not None:
            self.product = m.get('product')

        if m.get('scheduleExecuteTime') is not None:
            self.schedule_execute_time = m.get('scheduleExecuteTime')

        if m.get('scheduleFinishTime') is not None:
            self.schedule_finish_time = m.get('scheduleFinishTime')

        if m.get('showContent') is not None:
            temp_model = main_models.ListEventRecordsResponseBodyResultResultShowContent()
            self.show_content = temp_model.from_map(m.get('showContent'))

        if m.get('source') is not None:
            self.source = m.get('source')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class ListEventRecordsResponseBodyResultResultShowContent(DaraModel):
    def __init__(
        self,
        action_suggest: main_models.ListEventRecordsResponseBodyResultResultShowContentActionSuggest = None,
        desc: str = None,
        event_status: str = None,
        event_time: str = None,
        execute_finish_time: str = None,
        execute_start_time: str = None,
        instance_id: str = None,
        ops_change_id: str = None,
    ):
        self.action_suggest = action_suggest
        self.desc = desc
        self.event_status = event_status
        self.event_time = event_time
        self.execute_finish_time = execute_finish_time
        self.execute_start_time = execute_start_time
        self.instance_id = instance_id
        self.ops_change_id = ops_change_id

    def validate(self):
        if self.action_suggest:
            self.action_suggest.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action_suggest is not None:
            result['actionSuggest'] = self.action_suggest.to_map()

        if self.desc is not None:
            result['desc'] = self.desc

        if self.event_status is not None:
            result['eventStatus'] = self.event_status

        if self.event_time is not None:
            result['eventTime'] = self.event_time

        if self.execute_finish_time is not None:
            result['executeFinishTime'] = self.execute_finish_time

        if self.execute_start_time is not None:
            result['executeStartTime'] = self.execute_start_time

        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        if self.ops_change_id is not None:
            result['opsChangeId'] = self.ops_change_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('actionSuggest') is not None:
            temp_model = main_models.ListEventRecordsResponseBodyResultResultShowContentActionSuggest()
            self.action_suggest = temp_model.from_map(m.get('actionSuggest'))

        if m.get('desc') is not None:
            self.desc = m.get('desc')

        if m.get('eventStatus') is not None:
            self.event_status = m.get('eventStatus')

        if m.get('eventTime') is not None:
            self.event_time = m.get('eventTime')

        if m.get('executeFinishTime') is not None:
            self.execute_finish_time = m.get('executeFinishTime')

        if m.get('executeStartTime') is not None:
            self.execute_start_time = m.get('executeStartTime')

        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        if m.get('opsChangeId') is not None:
            self.ops_change_id = m.get('opsChangeId')

        return self

class ListEventRecordsResponseBodyResultResultShowContentActionSuggest(DaraModel):
    def __init__(
        self,
        suggest_actions: List[str] = None,
        suggest_text: str = None,
        suggest_type: str = None,
    ):
        self.suggest_actions = suggest_actions
        self.suggest_text = suggest_text
        self.suggest_type = suggest_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.suggest_actions is not None:
            result['suggestActions'] = self.suggest_actions

        if self.suggest_text is not None:
            result['suggestText'] = self.suggest_text

        if self.suggest_type is not None:
            result['suggestType'] = self.suggest_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('suggestActions') is not None:
            self.suggest_actions = m.get('suggestActions')

        if m.get('suggestText') is not None:
            self.suggest_text = m.get('suggestText')

        if m.get('suggestType') is not None:
            self.suggest_type = m.get('suggestType')

        return self

