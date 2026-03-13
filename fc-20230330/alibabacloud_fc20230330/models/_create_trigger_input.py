# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateTriggerInput(DaraModel):
    def __init__(
        self,
        description: str = None,
        invocation_role: str = None,
        qualifier: str = None,
        source_arn: str = None,
        trigger_config: str = None,
        trigger_name: str = None,
        trigger_type: str = None,
    ):
        # The description of the trigger.
        self.description = description
        # The RAM role that is used by the event source such as Object Storage Service (OSS) to invoke the function.
        self.invocation_role = invocation_role
        # The version or alias of the function.
        self.qualifier = qualifier
        # The Alibaba Cloud Resource Name (ARN) of the trigger event source.
        self.source_arn = source_arn
        # The configurations of the trigger. The configurations vary based on the trigger type. The following items list the data structures for different types of triggers:
        # 
        # *   OSS triggers: [OSSTriggerConfig](https://help.aliyun.com/document_detail/2766465.html).
        # *   Simple Log Service trigger: [LogTriggerConfig](https://help.aliyun.com/document_detail/2618711.html).
        # *   Time triggers: [TimerTriggerConfig](https://help.aliyun.com/document_detail/2754638.html).
        # *   HTTP triggers: [HTTPTriggerConfig](https://help.aliyun.com/document_detail/2766461.html).
        # *   Tablestore triggers: Specify the **SourceArnm** parameter and leave this parameter empty.
        # *   Alibaba Cloud CDN event triggers: [CDNEventsTriggerConfig](https://help.aliyun.com/document_detail/2766462.html).
        # *   MNS topic triggers: [MnsTopicTriggerConfig](https://help.aliyun.com/document_detail/2766464.html).
        # *   EventBridge-based triggers: [EventBridgeTriggerConfig](https://help.aliyun.com/document_detail/2766447.html).
        # 
        # This parameter is required.
        self.trigger_config = trigger_config
        # The name of the trigger. The name can contain only letters, digits, hyphens (-), and underscores (_). The name must be 1 to 128 characters in length and cannot start with a digit or a hyphen (-).
        # 
        # This parameter is required.
        self.trigger_name = trigger_name
        # The type of the trigger. Valid values:
        # 
        # *   **oss**: OSS event triggers. For more information, see [Overview](https://help.aliyun.com/document_detail/2513613.html).
        # *   **log**: Simple Log Service triggers. For more information, see [Simple Log Service triggers](https://help.aliyun.com/document_detail/2513638.html).
        # *   **timer**: time triggers. For more information, see [Time triggers](https://help.aliyun.com/document_detail/2513611.html).
        # *   **http**: HTTP triggers. For more information, see [Overview](https://help.aliyun.com/document_detail/2513634.html).
        # *   **tablestore**: Tablestore triggers. For more information, see [Tablestore triggers](https://help.aliyun.com/document_detail/2513640.html).
        # *   **cdn_events**: CDN event triggers. For more information, see [Overview](https://help.aliyun.com/document_detail/2513636.html).
        # *   **mns_topic**: Message Service (MNS) topic triggers. For more information, see [MNS topic triggers](https://help.aliyun.com/document_detail/2513641.html).
        # *   **eventbridge**: EventBridge-based triggers.
        # 
        # This parameter is required.
        self.trigger_type = trigger_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['description'] = self.description

        if self.invocation_role is not None:
            result['invocationRole'] = self.invocation_role

        if self.qualifier is not None:
            result['qualifier'] = self.qualifier

        if self.source_arn is not None:
            result['sourceArn'] = self.source_arn

        if self.trigger_config is not None:
            result['triggerConfig'] = self.trigger_config

        if self.trigger_name is not None:
            result['triggerName'] = self.trigger_name

        if self.trigger_type is not None:
            result['triggerType'] = self.trigger_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('invocationRole') is not None:
            self.invocation_role = m.get('invocationRole')

        if m.get('qualifier') is not None:
            self.qualifier = m.get('qualifier')

        if m.get('sourceArn') is not None:
            self.source_arn = m.get('sourceArn')

        if m.get('triggerConfig') is not None:
            self.trigger_config = m.get('triggerConfig')

        if m.get('triggerName') is not None:
            self.trigger_name = m.get('triggerName')

        if m.get('triggerType') is not None:
            self.trigger_type = m.get('triggerType')

        return self

