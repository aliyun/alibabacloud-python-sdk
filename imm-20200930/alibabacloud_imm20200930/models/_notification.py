# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_imm20200930 import models as main_models
from darabonba.model import DaraModel

class Notification(DaraModel):
    def __init__(
        self,
        extended_message_uri: str = None,
        mns: main_models.MNS = None,
        rocket_mq: main_models.RocketMQ = None,
    ):
        # The Object Storage Service (OSS) URI of the object that stores task notifications. Task information is written to the object in the JSON format. In most cases, you can receive notifications only by using [EventBridge](https://help.aliyun.com/document_detail/161886.html), [Simple Message Queue](https://help.aliyun.com/document_detail/27412.html), or [ApsaraMQ for RocketMQ](https://help.aliyun.com/document_detail/29530.html). For tasks that have a large amount of task information, such as archive file inspection tasks and decompression tasks, you can use an OSS object to store detailed task information.
        # 
        # The OSS URI follows the oss://${Bucket}/${Object} format, where `${Bucket}` is the name of the bucket in the same region as the current project and `${Object}` is the path of the object with the extension included.
        # 
        # >  The object is not a messaging method. It serves only as a container for detailed task information. Task status information is sent as a message, whereas the object stores detailed task information.
        self.extended_message_uri = extended_message_uri
        # The SMQ notification settings.
        self.mns = mns
        # The ApsaraMQ for RocketMQ notification settings.
        self.rocket_mq = rocket_mq

    def validate(self):
        if self.mns:
            self.mns.validate()
        if self.rocket_mq:
            self.rocket_mq.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.extended_message_uri is not None:
            result['ExtendedMessageURI'] = self.extended_message_uri

        if self.mns is not None:
            result['MNS'] = self.mns.to_map()

        if self.rocket_mq is not None:
            result['RocketMQ'] = self.rocket_mq.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExtendedMessageURI') is not None:
            self.extended_message_uri = m.get('ExtendedMessageURI')

        if m.get('MNS') is not None:
            temp_model = main_models.MNS()
            self.mns = temp_model.from_map(m.get('MNS'))

        if m.get('RocketMQ') is not None:
            temp_model = main_models.RocketMQ()
            self.rocket_mq = temp_model.from_map(m.get('RocketMQ'))

        return self

