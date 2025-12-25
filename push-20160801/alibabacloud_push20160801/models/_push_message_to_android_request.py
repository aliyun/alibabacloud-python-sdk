# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PushMessageToAndroidRequest(DaraModel):
    def __init__(
        self,
        app_key: int = None,
        body: str = None,
        job_key: str = None,
        store_offline: bool = None,
        target: str = None,
        target_value: str = None,
        title: str = None,
    ):
        # This parameter is required.
        self.app_key = app_key
        # This parameter is required.
        self.body = body
        self.job_key = job_key
        self.store_offline = store_offline
        # This parameter is required.
        self.target = target
        # This parameter is required.
        self.target_value = target_value
        # This parameter is required.
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_key is not None:
            result['AppKey'] = self.app_key

        if self.body is not None:
            result['Body'] = self.body

        if self.job_key is not None:
            result['JobKey'] = self.job_key

        if self.store_offline is not None:
            result['StoreOffline'] = self.store_offline

        if self.target is not None:
            result['Target'] = self.target

        if self.target_value is not None:
            result['TargetValue'] = self.target_value

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')

        if m.get('Body') is not None:
            self.body = m.get('Body')

        if m.get('JobKey') is not None:
            self.job_key = m.get('JobKey')

        if m.get('StoreOffline') is not None:
            self.store_offline = m.get('StoreOffline')

        if m.get('Target') is not None:
            self.target = m.get('Target')

        if m.get('TargetValue') is not None:
            self.target_value = m.get('TargetValue')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

