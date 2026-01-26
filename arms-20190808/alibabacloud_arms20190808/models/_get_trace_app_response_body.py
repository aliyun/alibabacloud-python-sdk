# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_arms20190808 import models as main_models
from darabonba.model import DaraModel

class GetTraceAppResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        trace_app: main_models.GetTraceAppResponseBodyTraceApp = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The information about the array object.
        self.trace_app = trace_app

    def validate(self):
        if self.trace_app:
            self.trace_app.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.trace_app is not None:
            result['TraceApp'] = self.trace_app.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TraceApp') is not None:
            temp_model = main_models.GetTraceAppResponseBodyTraceApp()
            self.trace_app = temp_model.from_map(m.get('TraceApp'))

        return self

class GetTraceAppResponseBodyTraceApp(DaraModel):
    def __init__(
        self,
        app_id: int = None,
        app_name: str = None,
        cluster_id: str = None,
        create_time: int = None,
        labels: List[str] = None,
        language: str = None,
        pid: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        show: bool = None,
        source: str = None,
        tags: List[main_models.GetTraceAppResponseBodyTraceAppTags] = None,
        type: str = None,
        update_time: int = None,
        user_id: str = None,
    ):
        # The application ID.
        self.app_id = app_id
        # The name of the application.
        self.app_name = app_name
        # The ID of the cluster.
        self.cluster_id = cluster_id
        # The timestamp generated when the task was created.
        self.create_time = create_time
        # The aliases of the application.
        self.labels = labels
        # The programming language of the application.
        self.language = language
        # The process identifier (PID) of the application.
        self.pid = pid
        # The region ID.
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # Indicates whether the application is displayed in the Application Real-Time Monitoring Service (ARMS) console. Valid values:
        # 
        # *   `true`: yes
        # *   `false`: no
        self.show = show
        # The source of the application.
        self.source = source
        # A list of key-value pairs.
        self.tags = tags
        # The type of the monitoring task. Valid values:
        # 
        # *   `TRACE`: Application Monitoring
        # *   `RETCODE`: Browser Monitoring
        self.type = type
        # The timestamp generated when the task information was updated.
        self.update_time = update_time
        # The user ID.
        self.user_id = user_id

    def validate(self):
        if self.tags:
            for v1 in self.tags:
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

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.labels is not None:
            result['Labels'] = self.labels

        if self.language is not None:
            result['Language'] = self.language

        if self.pid is not None:
            result['Pid'] = self.pid

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.show is not None:
            result['Show'] = self.show

        if self.source is not None:
            result['Source'] = self.source

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

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

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Labels') is not None:
            self.labels = m.get('Labels')

        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('Pid') is not None:
            self.pid = m.get('Pid')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Show') is not None:
            self.show = m.get('Show')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.GetTraceAppResponseBodyTraceAppTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

class GetTraceAppResponseBodyTraceAppTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

