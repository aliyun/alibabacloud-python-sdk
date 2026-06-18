# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetRecordUrlRequest(DaraModel):
    def __init__(
        self,
        acid: str = None,
        instance_id: str = None,
        record_type: str = None,
    ):
        # The session ID.
        # 
        # This parameter is required.
        self.acid = acid
        # The Artificial Intelligence Cloud Call Service (AICCS) instance ID. You can obtain it in the [Artificial Intelligence Cloud Call Service console](https://aiccs.console.aliyun.com/overview) > Instance Management.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The call type. Valid values:
        # 
        # - **DUP_CALL**: Incoming and outgoing calls.
        # - **IVR_CALL**: IVR outbound call.
        # - **SMART_CALL**: Intelligent outbound call.
        # 
        # This parameter is required.
        self.record_type = record_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acid is not None:
            result['Acid'] = self.acid

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.record_type is not None:
            result['RecordType'] = self.record_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Acid') is not None:
            self.acid = m.get('Acid')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RecordType') is not None:
            self.record_type = m.get('RecordType')

        return self

