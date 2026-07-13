# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateCloudGtmInstanceConfigResponseBody(DaraModel):
    def __init__(
        self,
        config_id: bool = None,
        instance_id: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The ID of the domain name instance configuration. A GTM instance can have both an A record and an AAAA record for the same access domain name. In this case, the GTM instance has two domain name instance configurations. The ConfigId uniquely identifies each configuration.
        self.config_id = config_id
        # The ID of the instance.
        self.instance_id = instance_id
        # The unique request ID.
        self.request_id = request_id
        # Indicates whether the operation was successful:
        # 
        # - true: The operation was successful.
        # 
        # - false: The operation failed.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_id is not None:
            result['ConfigId'] = self.config_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

