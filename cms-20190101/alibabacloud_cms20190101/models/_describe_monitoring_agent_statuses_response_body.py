# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20190101 import models as main_models
from darabonba.model import DaraModel

class DescribeMonitoringAgentStatusesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        node_status_list: main_models.DescribeMonitoringAgentStatusesResponseBodyNodeStatusList = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code.
        # 
        # > The status code 200 indicates that the request was successful.
        self.code = code
        # The error message.
        self.message = message
        # The host status information.
        self.node_status_list = node_status_list
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success

    def validate(self):
        if self.node_status_list:
            self.node_status_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.node_status_list is not None:
            result['NodeStatusList'] = self.node_status_list.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('NodeStatusList') is not None:
            temp_model = main_models.DescribeMonitoringAgentStatusesResponseBodyNodeStatusList()
            self.node_status_list = temp_model.from_map(m.get('NodeStatusList'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeMonitoringAgentStatusesResponseBodyNodeStatusList(DaraModel):
    def __init__(
        self,
        node_status: List[main_models.DescribeMonitoringAgentStatusesResponseBodyNodeStatusListNodeStatus] = None,
    ):
        self.node_status = node_status

    def validate(self):
        if self.node_status:
            for v1 in self.node_status:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['NodeStatus'] = []
        if self.node_status is not None:
            for k1 in self.node_status:
                result['NodeStatus'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.node_status = []
        if m.get('NodeStatus') is not None:
            for k1 in m.get('NodeStatus'):
                temp_model = main_models.DescribeMonitoringAgentStatusesResponseBodyNodeStatusListNodeStatus()
                self.node_status.append(temp_model.from_map(k1))

        return self

class DescribeMonitoringAgentStatusesResponseBodyNodeStatusListNodeStatus(DaraModel):
    def __init__(
        self,
        agent_install_error_code: str = None,
        auto_install: bool = None,
        instance_id: str = None,
        loong_collector_status: str = None,
        loong_collector_version: str = None,
        os_monitor_config: str = None,
        os_monitor_error_code: str = None,
        os_monitor_error_detail: str = None,
        os_monitor_status: str = None,
        os_monitor_version: str = None,
        status: str = None,
    ):
        # The error code returned when the CloudMonitor agent is installed. Valid values:
        # 
        # *   Common.Timeout: The installation timed out.
        # *   Common.SLR: The service-linked role for CloudMonitor is unauthorized.
        # *   Common.OS: The operating system is not supported.
        # *   Assist.Invalid: Cloud Assistant is not running.
        # *   Assist.Invoke: An error occurred when the installation program is started.
        # *   Assist.Execute: An error occurred when the installation program is running.
        self.agent_install_error_code = agent_install_error_code
        # Indicates whether the CloudMonitor agent is automatically installed. Valid values:
        # 
        # *   true: The CloudMonitor agent is automatically installed.
        # *   false: The CloudMonitor agent is not automatically installed.
        self.auto_install = auto_install
        # The instance ID.
        self.instance_id = instance_id
        self.loong_collector_status = loong_collector_status
        self.loong_collector_version = loong_collector_version
        # Indicates whether the SysAK monitoring feature is enabled.`` Valid values:
        # 
        # *   `true`: The SysAK monitoring feature is enabled.
        # *   `false`: the SysAK monitoring feature is disabled.
        self.os_monitor_config = os_monitor_config
        # The error status of SysOM. Valid values:
        # 
        # *   `install_fail`: SysOM fails to be installed or an unknown error occurs.
        # *   `install_assist_invalid`: SysOM fails to be installed because the status of Cloud Assistant is invalid.
        # *   `install_assist_command_fail`: SysOM fails to be installed because the installation command fails to run.
        # *   `uninstall_fail`: SysOM fails to be uninstalled or an unknown error occurs.
        # *   `uninstall_assist_invalid`: SysOM fails to be uninstalled because the status of Cloud Assistant is invalid.
        # *   `uninstall_assist_command_fail`: SysOM fails to be uninstalled because the uninstallation command fails to run.
        self.os_monitor_error_code = os_monitor_error_code
        # The details of the execution error. Valid values:
        # 
        # *   `Command.ErrorCode.Fail.Downlaod.REGIN_ID`: Failed to obtain the region ID.
        # *   `Command.ErrorCode.Fail.Downlaod.SYSAK`: Failed to download the .rpm package of System Analyse Kit (SysAK).
        # *   `Command.ErrorCode.Fail.Downlaod.CMON_FILE`: Failed to download the CMON file.
        # *   `Command.ErrorCode.Fail.Downlaod.BTF`: Failed to start SysAK because the BTF file is not found.
        # *   `Command.ErrorCode.Fail.Start.SYSAK`: Failed to start SysAK due to an unknown error.
        self.os_monitor_error_detail = os_monitor_error_detail
        # The status of SysOM. Valid values:
        # 
        # *   installing: SysOM is being installed.
        # *   running: SysOM is running.
        # *   stopped: SysOM is stopped.
        # *   uninstalling: SysOM is being uninstalled.
        self.os_monitor_status = os_monitor_status
        # The SysOM version.
        self.os_monitor_version = os_monitor_version
        # The status of the CloudMonitor agent. Valid values:
        # 
        # *   running: The CloudMonitor agent is running.
        # *   stopped: The CloudMonitor agent is stopped.
        # *   installing: The CloudMonitor agent is being installed.
        # *   install_faild: The CloudMonitor agent fails to be installed.
        # *   abnormal: The CloudMonitor agent is not properly installed.
        # *   not_installed: The CloudMonitor agent is not installed.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_install_error_code is not None:
            result['AgentInstallErrorCode'] = self.agent_install_error_code

        if self.auto_install is not None:
            result['AutoInstall'] = self.auto_install

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.loong_collector_status is not None:
            result['LoongCollectorStatus'] = self.loong_collector_status

        if self.loong_collector_version is not None:
            result['LoongCollectorVersion'] = self.loong_collector_version

        if self.os_monitor_config is not None:
            result['OsMonitorConfig'] = self.os_monitor_config

        if self.os_monitor_error_code is not None:
            result['OsMonitorErrorCode'] = self.os_monitor_error_code

        if self.os_monitor_error_detail is not None:
            result['OsMonitorErrorDetail'] = self.os_monitor_error_detail

        if self.os_monitor_status is not None:
            result['OsMonitorStatus'] = self.os_monitor_status

        if self.os_monitor_version is not None:
            result['OsMonitorVersion'] = self.os_monitor_version

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentInstallErrorCode') is not None:
            self.agent_install_error_code = m.get('AgentInstallErrorCode')

        if m.get('AutoInstall') is not None:
            self.auto_install = m.get('AutoInstall')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('LoongCollectorStatus') is not None:
            self.loong_collector_status = m.get('LoongCollectorStatus')

        if m.get('LoongCollectorVersion') is not None:
            self.loong_collector_version = m.get('LoongCollectorVersion')

        if m.get('OsMonitorConfig') is not None:
            self.os_monitor_config = m.get('OsMonitorConfig')

        if m.get('OsMonitorErrorCode') is not None:
            self.os_monitor_error_code = m.get('OsMonitorErrorCode')

        if m.get('OsMonitorErrorDetail') is not None:
            self.os_monitor_error_detail = m.get('OsMonitorErrorDetail')

        if m.get('OsMonitorStatus') is not None:
            self.os_monitor_status = m.get('OsMonitorStatus')

        if m.get('OsMonitorVersion') is not None:
            self.os_monitor_version = m.get('OsMonitorVersion')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

