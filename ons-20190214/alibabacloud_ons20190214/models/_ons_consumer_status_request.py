# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class OnsConsumerStatusRequest(DaraModel):
    def __init__(
        self,
        detail: bool = None,
        group_id: str = None,
        instance_id: str = None,
        need_jstack: bool = None,
    ):
        # Specifies whether to query the details of the consumer group. Valid values:
        # 
        # *   **true**: The details of the consumer group are queried. You can obtain details from the **ConsumerConnectionInfoList** and **DetailInTopicList** response parameters.
        # *   **false**: The details of the consumer group are not queried. The values of the **ConsumerConnectionInfoList** and **DetailInTopicList** response parameters are empty. This value is the default value of the Detail parameter.
        self.detail = detail
        # The ID of the consumer group whose details you want to query.
        # 
        # This parameter is required.
        self.group_id = group_id
        # The ID of the instance to which the consumer group belongs.
        self.instance_id = instance_id
        # Specifies whether to query the information about thread stack traces. Valid values:
        # 
        # *   **true**: The information about thread stack traces is queried. You can obtain the information from the **Jstack** response parameter.
        # 
        # > If you want to obtain the information about thread stack traces, make sure that the **Detail** parameter in the request is set to **true**.
        # 
        # *   **false**: The information about thread stack traces is not queried. The value of the **Jstack** response parameter is empty. This value is the default value of the NeedJstack parameter.
        self.need_jstack = need_jstack

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.detail is not None:
            result['Detail'] = self.detail

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.need_jstack is not None:
            result['NeedJstack'] = self.need_jstack

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Detail') is not None:
            self.detail = m.get('Detail')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('NeedJstack') is not None:
            self.need_jstack = m.get('NeedJstack')

        return self

