# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeBasicStartRequest(DaraModel):
    def __init__(
        self,
        app_key: str = None,
        end_ds: str = None,
        reg_id: str = None,
        service: str = None,
        start_ds: str = None,
    ):
        # Application appkey.
        self.app_key = app_key
        # End time, accurate to milliseconds (ms).
        self.end_ds = end_ds
        # Region code
        self.reg_id = reg_id
        # Service to call
        self.service = service
        # Start time, accurate to milliseconds (ms).
        self.start_ds = start_ds

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_key is not None:
            result['appKey'] = self.app_key

        if self.end_ds is not None:
            result['endDs'] = self.end_ds

        if self.reg_id is not None:
            result['regId'] = self.reg_id

        if self.service is not None:
            result['service'] = self.service

        if self.start_ds is not None:
            result['startDs'] = self.start_ds

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appKey') is not None:
            self.app_key = m.get('appKey')

        if m.get('endDs') is not None:
            self.end_ds = m.get('endDs')

        if m.get('regId') is not None:
            self.reg_id = m.get('regId')

        if m.get('service') is not None:
            self.service = m.get('service')

        if m.get('startDs') is not None:
            self.start_ds = m.get('startDs')

        return self

