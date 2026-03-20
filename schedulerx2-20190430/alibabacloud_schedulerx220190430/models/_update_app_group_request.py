# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateAppGroupRequest(DaraModel):
    def __init__(
        self,
        app_version: int = None,
        description: str = None,
        enable_log: bool = None,
        group_id: str = None,
        max_concurrency: int = None,
        monitor_config_json: str = None,
        monitor_contacts_json: str = None,
        namespace: str = None,
        notification_policy_name: str = None,
        region_id: str = None,
    ):
        # The application version. 1: Basic version, 2: Professional version.
        self.app_version = app_version
        # The description of the application.
        self.description = description
        self.enable_log = enable_log
        # The ID of the application. You can obtain the application ID on the **Application Management** page in the SchedulerX console.
        # 
        # This parameter is required.
        self.group_id = group_id
        # The maximum number of concurrent instances. Default value: 1. A value of 1 specifies that if the last triggered instance is running, the next instance is not triggered even if the scheduled point in time for running the next instance is reached.
        self.max_concurrency = max_concurrency
        # The configuration of the alert. The value is a JSON string. For more information about this parameter, see **Additional information about request parameters**.
        self.monitor_config_json = monitor_config_json
        # The configuration of alert contacts. The value is a JSON string.
        self.monitor_contacts_json = monitor_contacts_json
        # The ID of the namespace. You can obtain the ID of the namespace on the Namespace page in the SchedulerX console.
        # 
        # This parameter is required.
        self.namespace = namespace
        self.notification_policy_name = notification_policy_name
        # The ID of the region.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_version is not None:
            result['AppVersion'] = self.app_version

        if self.description is not None:
            result['Description'] = self.description

        if self.enable_log is not None:
            result['EnableLog'] = self.enable_log

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.max_concurrency is not None:
            result['MaxConcurrency'] = self.max_concurrency

        if self.monitor_config_json is not None:
            result['MonitorConfigJson'] = self.monitor_config_json

        if self.monitor_contacts_json is not None:
            result['MonitorContactsJson'] = self.monitor_contacts_json

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.notification_policy_name is not None:
            result['NotificationPolicyName'] = self.notification_policy_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EnableLog') is not None:
            self.enable_log = m.get('EnableLog')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('MaxConcurrency') is not None:
            self.max_concurrency = m.get('MaxConcurrency')

        if m.get('MonitorConfigJson') is not None:
            self.monitor_config_json = m.get('MonitorConfigJson')

        if m.get('MonitorContactsJson') is not None:
            self.monitor_contacts_json = m.get('MonitorContactsJson')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('NotificationPolicyName') is not None:
            self.notification_policy_name = m.get('NotificationPolicyName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

