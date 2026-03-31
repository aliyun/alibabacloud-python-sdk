# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ram20150501 import models as main_models
from darabonba.model import DaraModel

class GetAccessKeyLastUsedResponseBody(DaraModel):
    def __init__(
        self,
        access_key_last_used: main_models.GetAccessKeyLastUsedResponseBodyAccessKeyLastUsed = None,
        request_id: str = None,
    ):
        # The details of the time when the AccessKey pair was used for the last time.
        self.access_key_last_used = access_key_last_used
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.access_key_last_used:
            self.access_key_last_used.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_key_last_used is not None:
            result['AccessKeyLastUsed'] = self.access_key_last_used.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessKeyLastUsed') is not None:
            temp_model = main_models.GetAccessKeyLastUsedResponseBodyAccessKeyLastUsed()
            self.access_key_last_used = temp_model.from_map(m.get('AccessKeyLastUsed'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetAccessKeyLastUsedResponseBodyAccessKeyLastUsed(DaraModel):
    def __init__(
        self,
        last_used_date: str = None,
    ):
        # The time when the AccessKey pair was used for the last time.
        self.last_used_date = last_used_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.last_used_date is not None:
            result['LastUsedDate'] = self.last_used_date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LastUsedDate') is not None:
            self.last_used_date = m.get('LastUsedDate')

        return self

