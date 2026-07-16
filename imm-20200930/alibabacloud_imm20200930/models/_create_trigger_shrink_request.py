# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateTriggerShrinkRequest(DaraModel):
    def __init__(
        self,
        actions_shrink: str = None,
        input_shrink: str = None,
        notification_shrink: str = None,
        project_name: str = None,
        service_role: str = None,
        tags_shrink: str = None,
    ):
        # A list of data processing templates.
        # 
        # This parameter is required.
        self.actions_shrink = actions_shrink
        # The data source configuration.
        # 
        # This parameter is required.
        self.input_shrink = input_shrink
        # The notification recipient. Various message intermediaries are supported. For details about the message format, see Asynchronous notification message. Choose one of the following methods to receive messages:
        # 
        # Activate and connect to EventBridge in the same region as Intelligent Media Management (IMM) to receive task notifications. For more information, see IMM events. Activate Message Service (MNS) in the same region as IMM and configure a subscription.
        self.notification_shrink = notification_shrink
        # The project name. For more information, see [Create a project](https://help.aliyun.com/document_detail/478153.html).
        # 
        # This parameter is required.
        self.project_name = project_name
        # The service role that grants Intelligent Media Management (IMM) permissions to access other cloud resources, such as Object Storage Service (OSS). The default value is AliyunIMMBatchTriggerRole.
        # 
        # To use a custom service role, create a service role and grant permissions to the role in the Resource Access Management (RAM) console. For more information, see [Create a service role](https://help.aliyun.com/document_detail/116800.html) and [Grant permissions to a RAM role](https://help.aliyun.com/document_detail/116147.html).
        # 
        # This parameter is required.
        self.service_role = service_role
        # Custom tags used to search and filter asynchronous tasks.
        self.tags_shrink = tags_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.actions_shrink is not None:
            result['Actions'] = self.actions_shrink

        if self.input_shrink is not None:
            result['Input'] = self.input_shrink

        if self.notification_shrink is not None:
            result['Notification'] = self.notification_shrink

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.service_role is not None:
            result['ServiceRole'] = self.service_role

        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Actions') is not None:
            self.actions_shrink = m.get('Actions')

        if m.get('Input') is not None:
            self.input_shrink = m.get('Input')

        if m.get('Notification') is not None:
            self.notification_shrink = m.get('Notification')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('ServiceRole') is not None:
            self.service_role = m.get('ServiceRole')

        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')

        return self

