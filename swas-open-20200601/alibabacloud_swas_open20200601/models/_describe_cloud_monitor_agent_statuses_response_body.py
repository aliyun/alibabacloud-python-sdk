# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_swas_open20200601 import models as main_models
from darabonba.model import DaraModel

class DescribeCloudMonitorAgentStatusesResponseBody(DaraModel):
    def __init__(
        self,
        instance_status_list: List[main_models.DescribeCloudMonitorAgentStatusesResponseBodyInstanceStatusList] = None,
        request_id: str = None,
    ):
        # Indicates whether the Cloud Monitor agent was automatically installed on the simple application server.
        self.instance_status_list = instance_status_list
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.instance_status_list:
            for v1 in self.instance_status_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['InstanceStatusList'] = []
        if self.instance_status_list is not None:
            for k1 in self.instance_status_list:
                result['InstanceStatusList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance_status_list = []
        if m.get('InstanceStatusList') is not None:
            for k1 in m.get('InstanceStatusList'):
                temp_model = main_models.DescribeCloudMonitorAgentStatusesResponseBodyInstanceStatusList()
                self.instance_status_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeCloudMonitorAgentStatusesResponseBodyInstanceStatusList(DaraModel):
    def __init__(
        self,
        auto_install: bool = None,
        instance_id: str = None,
        status: str = None,
    ):
        # Indicates whether the Cloud Monitor agent was automatically installed on the simple application server. Valid values:
        # 
        # - true
        # 
        # - false
        self.auto_install = auto_install
        # The ID of the simple application server.
        self.instance_id = instance_id
        # The running status of the Cloud Monitoring plug-in. Possible values are:
        # 
        # - running: Cloud Monitoring plug-in running.
        # 
        # - stopped: Cloud Monitoring plug-in stopped.
        # 
        # - installing: Cloud Monitoring plug-in installing.
        # 
        # - install_faild: Cloud Monitoring plug-in installation failed.
        # 
        # - abnormal: Cloud Monitoring plug-in installation abnormal.
        # 
        # - not_installed: Cloud Monitoring plug-in not installed.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_install is not None:
            result['AutoInstall'] = self.auto_install

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoInstall') is not None:
            self.auto_install = m.get('AutoInstall')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

