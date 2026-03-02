# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ims20190815 import models as main_models
from darabonba.model import DaraModel

class GetAccessKeyLastUsedResponseBody(DaraModel):
    def __init__(
        self,
        access_key_last_used: main_models.GetAccessKeyLastUsedResponseBodyAccessKeyLastUsed = None,
        request_id: str = None,
    ):
        self.access_key_last_used = access_key_last_used
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
        service_name: str = None,
    ):
        self.last_used_date = last_used_date
        self.service_name = service_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.last_used_date is not None:
            result['LastUsedDate'] = self.last_used_date

        if self.service_name is not None:
            result['ServiceName'] = self.service_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LastUsedDate') is not None:
            self.last_used_date = m.get('LastUsedDate')

        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')

        return self

