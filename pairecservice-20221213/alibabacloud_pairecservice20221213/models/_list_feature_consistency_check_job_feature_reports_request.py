# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListFeatureConsistencyCheckJobFeatureReportsRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        log_item_id: str = None,
        log_request_id: str = None,
        log_user_id: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.log_item_id = log_item_id
        # This parameter is required.
        self.log_request_id = log_request_id
        # This parameter is required.
        self.log_user_id = log_user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.log_item_id is not None:
            result['LogItemId'] = self.log_item_id

        if self.log_request_id is not None:
            result['LogRequestId'] = self.log_request_id

        if self.log_user_id is not None:
            result['LogUserId'] = self.log_user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('LogItemId') is not None:
            self.log_item_id = m.get('LogItemId')

        if m.get('LogRequestId') is not None:
            self.log_request_id = m.get('LogRequestId')

        if m.get('LogUserId') is not None:
            self.log_user_id = m.get('LogUserId')

        return self

