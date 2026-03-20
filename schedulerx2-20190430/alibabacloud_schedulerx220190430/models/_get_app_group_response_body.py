# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_schedulerx220190430 import models as main_models
from darabonba.model import DaraModel

class GetAppGroupResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.GetAppGroupResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code that is returned.
        self.code = code
        # The information about the application group.
        self.data = data
        # The additional information that is returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # - **true**: The request was successful.
        # - **false**: The request failed.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.GetAppGroupResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetAppGroupResponseBodyData(DaraModel):
    def __init__(
        self,
        app_key: str = None,
        app_name: str = None,
        app_version: str = None,
        cur_jobs: int = None,
        description: str = None,
        enable_log: bool = None,
        group_id: str = None,
        max_jobs: int = None,
        monitor_config_json: str = None,
        monitor_contacts_json: str = None,
        namespace: str = None,
        notification_policy_name: str = None,
    ):
        # The AppKey of the application.
        self.app_key = app_key
        # The name of the application.
        self.app_name = app_name
        # The application version. 1: Basic version, 2: Professional version.
        self.app_version = app_version
        # The number of jobs that are configured for the application group.
        self.cur_jobs = cur_jobs
        # The description of the application.
        self.description = description
        self.enable_log = enable_log
        # The ID of the application.
        self.group_id = group_id
        # The maximum number of jobs that can be configured for the application group.
        self.max_jobs = max_jobs
        # The alert notification configurations.
        # 
        # >  For more information about this parameter, see the following **additional information about request parameters**.
        self.monitor_config_json = monitor_config_json
        # The alert contact configurations.
        # 
        # >  For more information about this parameter, see the following **additional information about request parameters**.
        self.monitor_contacts_json = monitor_contacts_json
        # The ID of the namespace.
        self.namespace = namespace
        self.notification_policy_name = notification_policy_name

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

        if self.app_version is not None:
            result['AppVersion'] = self.app_version

        if self.cur_jobs is not None:
            result['CurJobs'] = self.cur_jobs

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

        if self.notification_policy_name is not None:
            result['NotificationPolicyName'] = self.notification_policy_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')

        if m.get('CurJobs') is not None:
            self.cur_jobs = m.get('CurJobs')

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

        if m.get('NotificationPolicyName') is not None:
            self.notification_policy_name = m.get('NotificationPolicyName')

        return self

