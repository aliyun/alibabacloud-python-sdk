# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_green20220926 import models as main_models
from darabonba.model import DaraModel

class ListAiAppByPageResponseBody(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        items: List[main_models.ListAiAppByPageResponseBodyItems] = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The current page number.
        self.current_page = current_page
        # The data on the current page.
        self.items = items
        # The number of entries per page.
        self.page_size = page_size
        # The ID assigned by the backend to uniquely identify the request. You can use this ID to troubleshoot issues.
        self.request_id = request_id
        # The total number of entries.
        self.total_count = total_count

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
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.ListAiAppByPageResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListAiAppByPageResponseBodyItems(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        app_name: str = None,
        app_status: str = None,
        channel: str = None,
        last_trace_time: str = None,
        risk_events: List[main_models.ListAiAppByPageResponseBodyItemsRiskEvents] = None,
        risk_level: str = None,
        trace_status: str = None,
        uid: str = None,
        warning_count: int = None,
    ):
        # appId。
        self.app_id = app_id
        # The application name.
        self.app_name = app_name
        # The application status.
        self.app_status = app_status
        # The channel.
        self.channel = channel
        # The last active time. Format: YYYY-MM-DD HH:mm:ss.
        self.last_trace_time = last_trace_time
        # The risk events.
        self.risk_events = risk_events
        # The risk level.
        self.risk_level = risk_level
        # The Tracing Analysis status.
        self.trace_status = trace_status
        # UID。
        self.uid = uid
        # The number of alerts.
        self.warning_count = warning_count

    def validate(self):
        if self.risk_events:
            for v1 in self.risk_events:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.app_status is not None:
            result['AppStatus'] = self.app_status

        if self.channel is not None:
            result['Channel'] = self.channel

        if self.last_trace_time is not None:
            result['LastTraceTime'] = self.last_trace_time

        result['RiskEvents'] = []
        if self.risk_events is not None:
            for k1 in self.risk_events:
                result['RiskEvents'].append(k1.to_map() if k1 else None)

        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level

        if self.trace_status is not None:
            result['TraceStatus'] = self.trace_status

        if self.uid is not None:
            result['Uid'] = self.uid

        if self.warning_count is not None:
            result['WarningCount'] = self.warning_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('AppStatus') is not None:
            self.app_status = m.get('AppStatus')

        if m.get('Channel') is not None:
            self.channel = m.get('Channel')

        if m.get('LastTraceTime') is not None:
            self.last_trace_time = m.get('LastTraceTime')

        self.risk_events = []
        if m.get('RiskEvents') is not None:
            for k1 in m.get('RiskEvents'):
                temp_model = main_models.ListAiAppByPageResponseBodyItemsRiskEvents()
                self.risk_events.append(temp_model.from_map(k1))

        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')

        if m.get('TraceStatus') is not None:
            self.trace_status = m.get('TraceStatus')

        if m.get('Uid') is not None:
            self.uid = m.get('Uid')

        if m.get('WarningCount') is not None:
            self.warning_count = m.get('WarningCount')

        return self

class ListAiAppByPageResponseBodyItemsRiskEvents(DaraModel):
    def __init__(
        self,
        event_code: str = None,
        event_count: int = None,
        event_descs: List[str] = None,
        event_ids: List[str] = None,
        event_name: str = None,
        event_status: str = None,
        labels: List[main_models.ListAiAppByPageResponseBodyItemsRiskEventsLabels] = None,
    ):
        # The risk event code.
        self.event_code = event_code
        # The number of events.
        self.event_count = event_count
        # The event descriptions.
        self.event_descs = event_descs
        # The list of risk event IDs.
        self.event_ids = event_ids
        # The risk event name.
        self.event_name = event_name
        # The event status. Valid values:
        # - **unhandled**: Unhandled.
        # - **resolved**: Resolved.
        self.event_status = event_status
        # The list of label items.
        self.labels = labels

    def validate(self):
        if self.labels:
            for v1 in self.labels:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.event_code is not None:
            result['EventCode'] = self.event_code

        if self.event_count is not None:
            result['EventCount'] = self.event_count

        if self.event_descs is not None:
            result['EventDescs'] = self.event_descs

        if self.event_ids is not None:
            result['EventIds'] = self.event_ids

        if self.event_name is not None:
            result['EventName'] = self.event_name

        if self.event_status is not None:
            result['EventStatus'] = self.event_status

        result['Labels'] = []
        if self.labels is not None:
            for k1 in self.labels:
                result['Labels'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventCode') is not None:
            self.event_code = m.get('EventCode')

        if m.get('EventCount') is not None:
            self.event_count = m.get('EventCount')

        if m.get('EventDescs') is not None:
            self.event_descs = m.get('EventDescs')

        if m.get('EventIds') is not None:
            self.event_ids = m.get('EventIds')

        if m.get('EventName') is not None:
            self.event_name = m.get('EventName')

        if m.get('EventStatus') is not None:
            self.event_status = m.get('EventStatus')

        self.labels = []
        if m.get('Labels') is not None:
            for k1 in m.get('Labels'):
                temp_model = main_models.ListAiAppByPageResponseBodyItemsRiskEventsLabels()
                self.labels.append(temp_model.from_map(k1))

        return self

class ListAiAppByPageResponseBodyItemsRiskEventsLabels(DaraModel):
    def __init__(
        self,
        label: str = None,
        label_desc: str = None,
        type: str = None,
    ):
        # The label name.
        self.label = label
        # The label description.
        self.label_desc = label_desc
        # The type.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.label is not None:
            result['Label'] = self.label

        if self.label_desc is not None:
            result['LabelDesc'] = self.label_desc

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Label') is not None:
            self.label = m.get('Label')

        if m.get('LabelDesc') is not None:
            self.label_desc = m.get('LabelDesc')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

