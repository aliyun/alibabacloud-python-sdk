# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateAppGroupRequest(DaraModel):
    def __init__(
        self,
        app_key: str = None,
        app_name: str = None,
        app_type: int = None,
        app_version: int = None,
        description: str = None,
        enable_log: bool = None,
        group_id: str = None,
        max_jobs: int = None,
        monitor_config_json: str = None,
        monitor_contacts_json: str = None,
        namespace: str = None,
        namespace_name: str = None,
        namespace_source: str = None,
        notification_policy_name: str = None,
        region_id: str = None,
        schedule_busy_workers: bool = None,
    ):
        # The AppKey for the application.
        self.app_key = app_key
        # The name of the application.
        # 
        # This parameter is required.
        self.app_name = app_name
        # The type of application. Valid values:
        # 
        # *   `TRACE`: Application Monitoring
        # *   `EBPF`: Application Monitoring eBPF Edition
        self.app_type = app_type
        # The application version. 1: Basic version, 2: Professional version.
        self.app_version = app_version
        # The description of the application.
        self.description = description
        # Specifies whether to enable logging. Valid values:
        # 
        # *   `true`: enabled
        # *   `false`: disabled
        self.enable_log = enable_log
        # The application ID. You can obtain the application ID on the Application Management page in the SchedulerX console.
        # 
        # This parameter is required.
        self.group_id = group_id
        # The maximum number of jobs.
        self.max_jobs = max_jobs
        # The configuration of the alert. The value is a JSON string. For more information about this parameter, see **Additional information about request parameters**.
        self.monitor_config_json = monitor_config_json
        # The configuration of alert contacts. The value is a JSON string.
        self.monitor_contacts_json = monitor_contacts_json
        # The namespace ID. You can obtain the namespace ID on the Namespace page in the SchedulerX console.
        # 
        # This parameter is required.
        self.namespace = namespace
        # The name of the namespace.
        self.namespace_name = namespace_name
        # This parameter is not supported. You do not need to specify this parameter.
        self.namespace_source = namespace_source
        self.notification_policy_name = notification_policy_name
        # The region ID.
        self.region_id = region_id
        # Specifies whether to schedule a busy worker.
        self.schedule_busy_workers = schedule_busy_workers

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_key is not None:
            result['AppKey'] = self.app_key

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.app_type is not None:
            result['AppType'] = self.app_type

        if self.app_version is not None:
            result['AppVersion'] = self.app_version

        if self.description is not None:
            result['Description'] = self.description

        if self.enable_log is not None:
            result['EnableLog'] = self.enable_log

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.max_jobs is not None:
            result['MaxJobs'] = self.max_jobs

        if self.monitor_config_json is not None:
            result['MonitorConfigJson'] = self.monitor_config_json

        if self.monitor_contacts_json is not None:
            result['MonitorContactsJson'] = self.monitor_contacts_json

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.namespace_name is not None:
            result['NamespaceName'] = self.namespace_name

        if self.namespace_source is not None:
            result['NamespaceSource'] = self.namespace_source

        if self.notification_policy_name is not None:
            result['NotificationPolicyName'] = self.notification_policy_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.schedule_busy_workers is not None:
            result['ScheduleBusyWorkers'] = self.schedule_busy_workers

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')

        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EnableLog') is not None:
            self.enable_log = m.get('EnableLog')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('MaxJobs') is not None:
            self.max_jobs = m.get('MaxJobs')

        if m.get('MonitorConfigJson') is not None:
            self.monitor_config_json = m.get('MonitorConfigJson')

        if m.get('MonitorContactsJson') is not None:
            self.monitor_contacts_json = m.get('MonitorContactsJson')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('NamespaceName') is not None:
            self.namespace_name = m.get('NamespaceName')

        if m.get('NamespaceSource') is not None:
            self.namespace_source = m.get('NamespaceSource')

        if m.get('NotificationPolicyName') is not None:
            self.notification_policy_name = m.get('NotificationPolicyName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ScheduleBusyWorkers') is not None:
            self.schedule_busy_workers = m.get('ScheduleBusyWorkers')

        return self

