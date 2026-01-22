# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_polardbx20200202 import models as main_models
from darabonba.model import DaraModel

class DescribeSqlAuditInfoResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.DescribeSqlAuditInfoResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.DescribeSqlAuditInfoResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeSqlAuditInfoResponseBodyData(DaraModel):
    def __init__(
        self,
        is_enabled: bool = None,
        slslog_store: str = None,
        slsproject: str = None,
    ):
        self.is_enabled = is_enabled
        self.slslog_store = slslog_store
        self.slsproject = slsproject

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.is_enabled is not None:
            result['IsEnabled'] = self.is_enabled

        if self.slslog_store is not None:
            result['SLSLogStore'] = self.slslog_store

        if self.slsproject is not None:
            result['SLSProject'] = self.slsproject

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsEnabled') is not None:
            self.is_enabled = m.get('IsEnabled')

        if m.get('SLSLogStore') is not None:
            self.slslog_store = m.get('SLSLogStore')

        if m.get('SLSProject') is not None:
            self.slsproject = m.get('SLSProject')

        return self

