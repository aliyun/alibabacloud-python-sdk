# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sddp20260120 import models as main_models
from darabonba.model import DaraModel

class GetDataMaskingAccountCountResponseBody(DaraModel):
    def __init__(
        self,
        account_count: main_models.GetDataMaskingAccountCountResponseBodyAccountCount = None,
        request_id: str = None,
    ):
        self.account_count = account_count
        self.request_id = request_id

    def validate(self):
        if self.account_count:
            self.account_count.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_count is not None:
            result['AccountCount'] = self.account_count.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountCount') is not None:
            temp_model = main_models.GetDataMaskingAccountCountResponseBodyAccountCount()
            self.account_count = temp_model.from_map(m.get('AccountCount'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetDataMaskingAccountCountResponseBodyAccountCount(DaraModel):
    def __init__(
        self,
        full_access_count: int = None,
        none_access_count: int = None,
        restricted_access_count: int = None,
        total_count: int = None,
    ):
        self.full_access_count = full_access_count
        self.none_access_count = none_access_count
        self.restricted_access_count = restricted_access_count
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.full_access_count is not None:
            result['FullAccessCount'] = self.full_access_count

        if self.none_access_count is not None:
            result['NoneAccessCount'] = self.none_access_count

        if self.restricted_access_count is not None:
            result['RestrictedAccessCount'] = self.restricted_access_count

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FullAccessCount') is not None:
            self.full_access_count = m.get('FullAccessCount')

        if m.get('NoneAccessCount') is not None:
            self.none_access_count = m.get('NoneAccessCount')

        if m.get('RestrictedAccessCount') is not None:
            self.restricted_access_count = m.get('RestrictedAccessCount')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

