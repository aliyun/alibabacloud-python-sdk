# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_fc20230330 import models as main_models
from darabonba.model import DaraModel

class Trigger(DaraModel):
    def __init__(
        self,
        created_time: str = None,
        description: str = None,
        http_trigger: main_models.HTTPTrigger = None,
        invocation_role: str = None,
        last_modified_time: str = None,
        qualifier: str = None,
        source_arn: str = None,
        status: str = None,
        target_arn: str = None,
        trigger_config: str = None,
        trigger_id: str = None,
        trigger_name: str = None,
        trigger_type: str = None,
    ):
        # The time when the trigger was created.
        self.created_time = created_time
        # The description of the trigger.
        self.description = description
        # The information about the HTTP trigger.
        self.http_trigger = http_trigger
        # The role that is used by the event source such as OSS to invoke the function.
        self.invocation_role = invocation_role
        # The time when the trigger was last modified.
        self.last_modified_time = last_modified_time
        # The version or alias of the function.
        self.qualifier = qualifier
        # The Alibaba Cloud Resource Name (ARN) of the event source for the trigger.
        self.source_arn = source_arn
        # The status of the trigger.
        self.status = status
        # The ARN of the function.
        self.target_arn = target_arn
        # The configurations of the trigger. The configurations vary based on trigger types.
        self.trigger_config = trigger_config
        # The unique ID of the trigger.
        self.trigger_id = trigger_id
        # The name of the trigger. The name contains only letters, digits, hyphens (-), and underscores (_). The name must be 1 to 128 characters in length and cannot start with a digit or hyphen (-).
        self.trigger_name = trigger_name
        # The type of the trigger.
        self.trigger_type = trigger_type

    def validate(self):
        if self.http_trigger:
            self.http_trigger.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_time is not None:
            result['createdTime'] = self.created_time

        if self.description is not None:
            result['description'] = self.description

        if self.http_trigger is not None:
            result['httpTrigger'] = self.http_trigger.to_map()

        if self.invocation_role is not None:
            result['invocationRole'] = self.invocation_role

        if self.last_modified_time is not None:
            result['lastModifiedTime'] = self.last_modified_time

        if self.qualifier is not None:
            result['qualifier'] = self.qualifier

        if self.source_arn is not None:
            result['sourceArn'] = self.source_arn

        if self.status is not None:
            result['status'] = self.status

        if self.target_arn is not None:
            result['targetArn'] = self.target_arn

        if self.trigger_config is not None:
            result['triggerConfig'] = self.trigger_config

        if self.trigger_id is not None:
            result['triggerId'] = self.trigger_id

        if self.trigger_name is not None:
            result['triggerName'] = self.trigger_name

        if self.trigger_type is not None:
            result['triggerType'] = self.trigger_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('httpTrigger') is not None:
            temp_model = main_models.HTTPTrigger()
            self.http_trigger = temp_model.from_map(m.get('httpTrigger'))

        if m.get('invocationRole') is not None:
            self.invocation_role = m.get('invocationRole')

        if m.get('lastModifiedTime') is not None:
            self.last_modified_time = m.get('lastModifiedTime')

        if m.get('qualifier') is not None:
            self.qualifier = m.get('qualifier')

        if m.get('sourceArn') is not None:
            self.source_arn = m.get('sourceArn')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('targetArn') is not None:
            self.target_arn = m.get('targetArn')

        if m.get('triggerConfig') is not None:
            self.trigger_config = m.get('triggerConfig')

        if m.get('triggerId') is not None:
            self.trigger_id = m.get('triggerId')

        if m.get('triggerName') is not None:
            self.trigger_name = m.get('triggerName')

        if m.get('triggerType') is not None:
            self.trigger_type = m.get('triggerType')

        return self

