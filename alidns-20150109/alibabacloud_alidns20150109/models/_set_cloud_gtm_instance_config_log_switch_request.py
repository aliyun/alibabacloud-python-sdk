# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetCloudGtmInstanceConfigLogSwitchRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        config_id: str = None,
        instance_id: str = None,
        status: str = None,
    ):
        self.client_token = client_token
        # This parameter is required.
        self.config_id = config_id
        self.instance_id = instance_id
        # This parameter is required.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.config_id is not None:
            result['ConfigId'] = self.config_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

