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
        # The templates.
        # 
        # This parameter is required.
        self.actions_shrink = actions_shrink
        # The data source configurations.
        # 
        # This parameter is required.
        self.input_shrink = input_shrink
        # The notification settings. The operation supports multiple messaging middleware options. For more information about notification messages, see Asynchronous message examples. You can use one of the following methods to receive notification messages:
        # 
        # In the region in which the IMM project is located, use EventBridge to receive task notifications. For more information, see IMM events. In the region in which the IMM project is located, configure a Simple Message Queue (SMQ) subscription to receive task notifications.
        self.notification_shrink = notification_shrink
        # The name of the project.[](~~478153~~)
        # 
        # This parameter is required.
        self.project_name = project_name
        # The service role. IMM assumes the service role so that it can access resources in other cloud services, such as OSS. Default value: AliyunIMMBatchTriggerRole.
        # 
        # You can also create a custom service role in the RAM console and grant the required permissions to the role based on your business requirements. For more information, see [Create a regular service role](https://help.aliyun.com/document_detail/116800.html) and [Grant permissions to a role](https://help.aliyun.com/document_detail/116147.html).
        # 
        # This parameter is required.
        self.service_role = service_role
        # The custom tags. You can search for or filter asynchronous tasks by custom tag.
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

