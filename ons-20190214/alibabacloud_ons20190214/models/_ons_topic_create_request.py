# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class OnsTopicCreateRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        message_type: int = None,
        remark: str = None,
        topic: str = None,
    ):
        # The ID of the instance in which you want to create the topic.
        self.instance_id = instance_id
        # The type of messages that you want to publish to the topic. Valid values:
        # 
        # *   **0**: normal messages
        # *   **1**: partitionally ordered messages
        # *   **2**: globally ordered messages
        # *   **4**: transactional messages
        # *   **5**: scheduled or delayed messages
        # 
        # For more information about message types, see [Message types](https://help.aliyun.com/document_detail/155952.html).
        # 
        # This parameter is required.
        self.message_type = message_type
        # The description of the topic that you want to create.
        self.remark = remark
        # The name of the topic that you want to create. The name must meet the following rules:
        # 
        # *   The name must be 3 to 64 characters in length and can contain letters, digits, hyphens (-), and underscores (_).
        # *   The topic name cannot start with CID or GID because CID and GID are reserved prefixes for group IDs.
        # *   If the ApsaraMQ for RocketMQ instance in which you want to create the topic uses a namespace, the topic name must be unique in the instance. The topic name cannot be the same as an existing topic name or a group ID in the instance. The topic name can be the same as a topic name or a group ID in another instance that uses a different namespace. For example, if Instance A and Instance B use different namespaces, a topic name in Instance A can be the same as a topic name or a group ID in Instance B.
        # *   If the instance in which you want to create the topic does not use a namespace, the topic name must be globally unique across instances and regions. The topic name cannot be the same as an existing topic name or group ID in all ApsaraMQ for RocketMQ instances that belong to your Alibaba Cloud account.
        # 
        # > To check whether an instance uses a namespace, log on to the ApsaraMQ for RocketMQ console, go to the **Instance Details** page, and then view the value of the Namespace field in the **Basic Information** section.
        # 
        # This parameter is required.
        self.topic = topic

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.message_type is not None:
            result['MessageType'] = self.message_type

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.topic is not None:
            result['Topic'] = self.topic

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('MessageType') is not None:
            self.message_type = m.get('MessageType')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('Topic') is not None:
            self.topic = m.get('Topic')

        return self

