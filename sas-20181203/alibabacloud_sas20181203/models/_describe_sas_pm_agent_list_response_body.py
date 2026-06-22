# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeSasPmAgentListResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        sas_pm_agent_list: List[main_models.DescribeSasPmAgentListResponseBodySasPmAgentList] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The query result list.
        self.sas_pm_agent_list = sas_pm_agent_list

    def validate(self):
        if self.sas_pm_agent_list:
            for v1 in self.sas_pm_agent_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['SasPmAgentList'] = []
        if self.sas_pm_agent_list is not None:
            for k1 in self.sas_pm_agent_list:
                result['SasPmAgentList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.sas_pm_agent_list = []
        if m.get('SasPmAgentList') is not None:
            for k1 in m.get('SasPmAgentList'):
                temp_model = main_models.DescribeSasPmAgentListResponseBodySasPmAgentList()
                self.sas_pm_agent_list.append(temp_model.from_map(k1))

        return self

class DescribeSasPmAgentListResponseBodySasPmAgentList(DaraModel):
    def __init__(
        self,
        aliyun_assist_id: str = None,
        aliyun_monitor_id: str = None,
        assist_install_result: int = None,
        assist_install_status: int = None,
        monitor_install_result: int = None,
        monitor_install_status: int = None,
        uuid: str = None,
    ):
        # The globally unique ID of Cloud Assistant.
        self.aliyun_assist_id = aliyun_assist_id
        # The globally unique ID of CloudMonitor.
        self.aliyun_monitor_id = aliyun_monitor_id
        # The installation execution result of Cloud Assistant. Valid values:
        # - **0**: SUCCESS
        # - **1**: MISSING_PARAM
        # - **2**: UNKNOWN_SYSTEM
        # - **3**: DOWNLOAD_FAILED
        # - **4**: INSTALL_FAILED.
        self.assist_install_result = assist_install_result
        # The installation status of Cloud Assistant. Valid values:
        # - **0**: Installing.
        # - **1**: Installed.
        # - **2**: Installation failed.
        # - **3**: Installation timed out.
        self.assist_install_status = assist_install_status
        # The installation execution result of CloudMonitor. Valid values:
        # - **0**: Failed.
        # - **1**: Succeeded.
        self.monitor_install_result = monitor_install_result
        # The installation status of CloudMonitor. Valid values:
        # - **0**: Failed.
        # - **1**: Succeeded.
        self.monitor_install_status = monitor_install_status
        # The UUID of the server.
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aliyun_assist_id is not None:
            result['AliyunAssistId'] = self.aliyun_assist_id

        if self.aliyun_monitor_id is not None:
            result['AliyunMonitorId'] = self.aliyun_monitor_id

        if self.assist_install_result is not None:
            result['AssistInstallResult'] = self.assist_install_result

        if self.assist_install_status is not None:
            result['AssistInstallStatus'] = self.assist_install_status

        if self.monitor_install_result is not None:
            result['MonitorInstallResult'] = self.monitor_install_result

        if self.monitor_install_status is not None:
            result['MonitorInstallStatus'] = self.monitor_install_status

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliyunAssistId') is not None:
            self.aliyun_assist_id = m.get('AliyunAssistId')

        if m.get('AliyunMonitorId') is not None:
            self.aliyun_monitor_id = m.get('AliyunMonitorId')

        if m.get('AssistInstallResult') is not None:
            self.assist_install_result = m.get('AssistInstallResult')

        if m.get('AssistInstallStatus') is not None:
            self.assist_install_status = m.get('AssistInstallStatus')

        if m.get('MonitorInstallResult') is not None:
            self.monitor_install_result = m.get('MonitorInstallResult')

        if m.get('MonitorInstallStatus') is not None:
            self.monitor_install_status = m.get('MonitorInstallStatus')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

