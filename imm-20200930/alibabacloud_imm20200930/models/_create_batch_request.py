# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_imm20200930 import models as main_models
from darabonba.model import DaraModel

class CreateBatchRequest(DaraModel):
    def __init__(
        self,
        actions: List[main_models.CreateBatchRequestActions] = None,
        input: main_models.Input = None,
        notification: main_models.CreateBatchRequestNotification = None,
        project_name: str = None,
        service_role: str = None,
        tags: Dict[str, Any] = None,
    ):
        # A list of processing templates.
        # 
        # This parameter is required.
        self.actions = actions
        # The input data source configuration.
        # 
        # This parameter is required.
        self.input = input
        # The notification recipient. Multiple middleware services are supported. For details about the message format, see Asynchronous notification message. Select one of the following methods to receive messages:
        # 
        # Activate and access EventBridge in the same region as Intelligent Media Management (IMM) to promptly receive task notifications. For more information, see IMM events.
        # Activate MNS in the same region as IMM and configure a subscription.
        self.notification = notification
        # The project name. For more information, see [Create a project](https://help.aliyun.com/document_detail/478153.html).
        # 
        # This parameter is required.
        self.project_name = project_name
        # The service role that grants IMM the permissions to access other cloud resources, such as OSS. The default value is AliyunIMMBatchTriggerRole.
        # 
        # To use a custom service role, create a service role and grant permissions to the role in the RAM console. For more information, see [Create a service role](https://help.aliyun.com/document_detail/116800.html) and [Grant permissions to a RAM role](https://help.aliyun.com/document_detail/116147.html).
        # 
        # This parameter is required.
        self.service_role = service_role
        # Custom tags used to search and filter asynchronous tasks.
        self.tags = tags

    def validate(self):
        if self.actions:
            for v1 in self.actions:
                 if v1:
                    v1.validate()
        if self.input:
            self.input.validate()
        if self.notification:
            self.notification.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Actions'] = []
        if self.actions is not None:
            for k1 in self.actions:
                result['Actions'].append(k1.to_map() if k1 else None)

        if self.input is not None:
            result['Input'] = self.input.to_map()

        if self.notification is not None:
            result['Notification'] = self.notification.to_map()

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.service_role is not None:
            result['ServiceRole'] = self.service_role

        if self.tags is not None:
            result['Tags'] = self.tags

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.actions = []
        if m.get('Actions') is not None:
            for k1 in m.get('Actions'):
                temp_model = main_models.CreateBatchRequestActions()
                self.actions.append(temp_model.from_map(k1))

        if m.get('Input') is not None:
            temp_model = main_models.Input()
            self.input = temp_model.from_map(m.get('Input'))

        if m.get('Notification') is not None:
            temp_model = main_models.CreateBatchRequestNotification()
            self.notification = temp_model.from_map(m.get('Notification'))

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('ServiceRole') is not None:
            self.service_role = m.get('ServiceRole')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        return self

class CreateBatchRequestNotification(DaraModel):
    def __init__(
        self,
        mns: main_models.MNS = None,
    ):
        # The parameters for MNS notifications.
        self.mns = mns

    def validate(self):
        if self.mns:
            self.mns.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.mns is not None:
            result['MNS'] = self.mns.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MNS') is not None:
            temp_model = main_models.MNS()
            self.mns = temp_model.from_map(m.get('MNS'))

        return self

class CreateBatchRequestActions(DaraModel):
    def __init__(
        self,
        fast_fail_policy: main_models.FastFailPolicy = None,
        name: str = None,
        parameters: List[str] = None,
    ):
        # The fast-fail policy configuration.
        self.fast_fail_policy = fast_fail_policy
        # The template name.
        # 
        # This parameter is required.
        self.name = name
        # A list of template parameters.
        self.parameters = parameters

    def validate(self):
        if self.fast_fail_policy:
            self.fast_fail_policy.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.fast_fail_policy is not None:
            result['FastFailPolicy'] = self.fast_fail_policy.to_map()

        if self.name is not None:
            result['Name'] = self.name

        if self.parameters is not None:
            result['Parameters'] = self.parameters

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FastFailPolicy') is not None:
            temp_model = main_models.FastFailPolicy()
            self.fast_fail_policy = temp_model.from_map(m.get('FastFailPolicy'))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')

        return self

