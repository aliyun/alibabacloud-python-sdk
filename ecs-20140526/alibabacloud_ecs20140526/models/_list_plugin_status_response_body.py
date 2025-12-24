# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class ListPluginStatusResponseBody(DaraModel):
    def __init__(
        self,
        instance_plugin_status_set: main_models.ListPluginStatusResponseBodyInstancePluginStatusSet = None,
        next_token: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The states of Cloud Assistant plug-ins on the instances.
        self.instance_plugin_status_set = instance_plugin_status_set
        # The returned value of NextToken is a pagination token, which can be used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.instance_plugin_status_set:
            self.instance_plugin_status_set.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_plugin_status_set is not None:
            result['InstancePluginStatusSet'] = self.instance_plugin_status_set.to_map()

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstancePluginStatusSet') is not None:
            temp_model = main_models.ListPluginStatusResponseBodyInstancePluginStatusSet()
            self.instance_plugin_status_set = temp_model.from_map(m.get('InstancePluginStatusSet'))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListPluginStatusResponseBodyInstancePluginStatusSet(DaraModel):
    def __init__(
        self,
        instance_plugin_status: List[main_models.ListPluginStatusResponseBodyInstancePluginStatusSetInstancePluginStatus] = None,
    ):
        self.instance_plugin_status = instance_plugin_status

    def validate(self):
        if self.instance_plugin_status:
            for v1 in self.instance_plugin_status:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['InstancePluginStatus'] = []
        if self.instance_plugin_status is not None:
            for k1 in self.instance_plugin_status:
                result['InstancePluginStatus'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance_plugin_status = []
        if m.get('InstancePluginStatus') is not None:
            for k1 in m.get('InstancePluginStatus'):
                temp_model = main_models.ListPluginStatusResponseBodyInstancePluginStatusSetInstancePluginStatus()
                self.instance_plugin_status.append(temp_model.from_map(k1))

        return self

class ListPluginStatusResponseBodyInstancePluginStatusSetInstancePluginStatus(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        plugin_status_set: main_models.ListPluginStatusResponseBodyInstancePluginStatusSetInstancePluginStatusPluginStatusSet = None,
    ):
        # The ID of the instance.
        self.instance_id = instance_id
        # The queried Cloud Assistant plug-ins.
        self.plugin_status_set = plugin_status_set

    def validate(self):
        if self.plugin_status_set:
            self.plugin_status_set.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.plugin_status_set is not None:
            result['PluginStatusSet'] = self.plugin_status_set.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PluginStatusSet') is not None:
            temp_model = main_models.ListPluginStatusResponseBodyInstancePluginStatusSetInstancePluginStatusPluginStatusSet()
            self.plugin_status_set = temp_model.from_map(m.get('PluginStatusSet'))

        return self

class ListPluginStatusResponseBodyInstancePluginStatusSetInstancePluginStatusPluginStatusSet(DaraModel):
    def __init__(
        self,
        plugin_status: List[main_models.ListPluginStatusResponseBodyInstancePluginStatusSetInstancePluginStatusPluginStatusSetPluginStatus] = None,
    ):
        self.plugin_status = plugin_status

    def validate(self):
        if self.plugin_status:
            for v1 in self.plugin_status:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['PluginStatus'] = []
        if self.plugin_status is not None:
            for k1 in self.plugin_status:
                result['PluginStatus'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.plugin_status = []
        if m.get('PluginStatus') is not None:
            for k1 in m.get('PluginStatus'):
                temp_model = main_models.ListPluginStatusResponseBodyInstancePluginStatusSetInstancePluginStatusPluginStatusSetPluginStatus()
                self.plugin_status.append(temp_model.from_map(k1))

        return self

class ListPluginStatusResponseBodyInstancePluginStatusSetInstancePluginStatusPluginStatusSetPluginStatus(DaraModel):
    def __init__(
        self,
        first_heartbeat_time: str = None,
        last_heartbeat_time: str = None,
        plugin_name: str = None,
        plugin_status: str = None,
        plugin_version: str = None,
    ):
        # The first time when Cloud Assistant reported the state of the plug-in.
        self.first_heartbeat_time = first_heartbeat_time
        # The last time when Cloud Assistant reported the state of the plug-in.
        self.last_heartbeat_time = last_heartbeat_time
        # The name of the plug-in.
        self.plugin_name = plugin_name
        # The state of the Cloud Assistant plug-in. Valid values:
        # 
        # *   NotInstalled: The plug-in is not installed.
        # *   Installed: The one-time plug-in is installed.
        # *   Running: The long-running plug-in is running.
        # *   Stopped: The long-running plug-in is not running.
        # *   Crashed: The plug-in is abnormal.
        # *   Removed: The plug-in is uninstalled.
        # *   Unknown: The state of the plug-in is unknown.
        self.plugin_status = plugin_status
        # The version of the plug-in.
        self.plugin_version = plugin_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.first_heartbeat_time is not None:
            result['FirstHeartbeatTime'] = self.first_heartbeat_time

        if self.last_heartbeat_time is not None:
            result['LastHeartbeatTime'] = self.last_heartbeat_time

        if self.plugin_name is not None:
            result['PluginName'] = self.plugin_name

        if self.plugin_status is not None:
            result['PluginStatus'] = self.plugin_status

        if self.plugin_version is not None:
            result['PluginVersion'] = self.plugin_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FirstHeartbeatTime') is not None:
            self.first_heartbeat_time = m.get('FirstHeartbeatTime')

        if m.get('LastHeartbeatTime') is not None:
            self.last_heartbeat_time = m.get('LastHeartbeatTime')

        if m.get('PluginName') is not None:
            self.plugin_name = m.get('PluginName')

        if m.get('PluginStatus') is not None:
            self.plugin_status = m.get('PluginStatus')

        if m.get('PluginVersion') is not None:
            self.plugin_version = m.get('PluginVersion')

        return self

