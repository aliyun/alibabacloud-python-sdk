# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetMonoRecordingRequest(DaraModel):
    def __init__(
        self,
        contact_id: str = None,
        expire_seconds: int = None,
        instance_id: str = None,
    ):
        # This parameter is required.
        self.contact_id = contact_id
        self.expire_seconds = expire_seconds
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.contact_id is not None:
            result['ContactId'] = self.contact_id

        if self.expire_seconds is not None:
            result['ExpireSeconds'] = self.expire_seconds

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactId') is not None:
            self.contact_id = m.get('ContactId')

        if m.get('ExpireSeconds') is not None:
            self.expire_seconds = m.get('ExpireSeconds')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

