# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_arms20210422 import models as main_models
from darabonba.model import DaraModel

class SearchTraceAppByNameResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        trace_apps: List[main_models.SearchTraceAppByNameResponseBodyTraceApps] = None,
    ):
        self.request_id = request_id
        self.trace_apps = trace_apps

    def validate(self):
        if self.trace_apps:
            for v1 in self.trace_apps:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['TraceApps'] = []
        if self.trace_apps is not None:
            for k1 in self.trace_apps:
                result['TraceApps'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.trace_apps = []
        if m.get('TraceApps') is not None:
            for k1 in m.get('TraceApps'):
                temp_model = main_models.SearchTraceAppByNameResponseBodyTraceApps()
                self.trace_apps.append(temp_model.from_map(k1))

        return self

class SearchTraceAppByNameResponseBodyTraceApps(DaraModel):
    def __init__(
        self,
        app_id: int = None,
        app_name: str = None,
        create_time: int = None,
        labels: List[str] = None,
        pid: str = None,
        region_id: str = None,
        show: bool = None,
        type: str = None,
        update_time: int = None,
        user_id: str = None,
    ):
        self.app_id = app_id
        self.app_name = app_name
        self.create_time = create_time
        self.labels = labels
        self.pid = pid
        self.region_id = region_id
        self.show = show
        self.type = type
        self.update_time = update_time
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.labels is not None:
            result['Labels'] = self.labels

        if self.pid is not None:
            result['Pid'] = self.pid

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.show is not None:
            result['Show'] = self.show

        if self.type is not None:
            result['Type'] = self.type

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Labels') is not None:
            self.labels = m.get('Labels')

        if m.get('Pid') is not None:
            self.pid = m.get('Pid')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Show') is not None:
            self.show = m.get('Show')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

