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
        # Use an Object Storage Service (OSS) file to receive task notifications. If you provide the URI of this file, detailed task execution information is written to the file in a JSON structure. Normally, you receive notifications through [EventBridge](https://help.aliyun.com/document_detail/161886.html), [MNS](https://help.aliyun.com/document_detail/27412.html), or [RocketMQ](https://help.aliyun.com/document_detail/29530.html). However, some tasks generate large amounts of information, such as archive previews or decompression tasks. For these tasks, provide this file to get the complete execution results.
        # 
        # The OSS URI format is oss\\://${Bucket}/${Object}. `${Bucket}` is the name of an OSS bucket in the same region as the current project. `${Object}` is the full path of the file, including the file name extension.
        # 
        # >Notice: 
        # 
        # This file is not a notification method. It only serves as a medium to receive detailed task execution information. Task status is sent through standard message notifications. This file contains only the detailed execution information.
        self.extended_message_uri = extended_message_uri
        # The MNS notification parameter object.
        self.mns = mns
        # The RocketMQ notification parameter object.
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

