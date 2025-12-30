# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_alidns20150109 import models as main_models
from darabonba.model import DaraModel

class DescribePdnsAppKeyResponseBody(DaraModel):
    def __init__(
        self,
        app_key: main_models.DescribePdnsAppKeyResponseBodyAppKey = None,
        request_id: str = None,
    ):
        self.app_key = app_key
        self.request_id = request_id

    def validate(self):
        if self.app_key:
            self.app_key.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_key is not None:
            result['AppKey'] = self.app_key.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKey') is not None:
            temp_model = main_models.DescribePdnsAppKeyResponseBodyAppKey()
            self.app_key = temp_model.from_map(m.get('AppKey'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribePdnsAppKeyResponseBodyAppKey(DaraModel):
    def __init__(
        self,
        app_key_id: str = None,
        app_key_secret: str = None,
        create_date: str = None,
        create_timestamp: int = None,
        remark: str = None,
        state: str = None,
    ):
        self.app_key_id = app_key_id
        self.app_key_secret = app_key_secret
        self.create_date = create_date
        self.create_timestamp = create_timestamp
        self.remark = remark
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_key_id is not None:
            result['AppKeyId'] = self.app_key_id

        if self.app_key_secret is not None:
            result['AppKeySecret'] = self.app_key_secret

        if self.create_date is not None:
            result['CreateDate'] = self.create_date

        if self.create_timestamp is not None:
            result['CreateTimestamp'] = self.create_timestamp

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.state is not None:
            result['State'] = self.state

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKeyId') is not None:
            self.app_key_id = m.get('AppKeyId')

        if m.get('AppKeySecret') is not None:
            self.app_key_secret = m.get('AppKeySecret')

        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')

        if m.get('CreateTimestamp') is not None:
            self.create_timestamp = m.get('CreateTimestamp')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('State') is not None:
            self.state = m.get('State')

        return self

