# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_yundun_dbaudit20180320 import models as main_models
from darabonba.model import DaraModel

class GetAuditCountDistributionResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        time_list: List[main_models.GetAuditCountDistributionResponseBodyTimeList] = None,
    ):
        self.request_id = request_id
        self.time_list = time_list

    def validate(self):
        if self.time_list:
            for v1 in self.time_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['TimeList'] = []
        if self.time_list is not None:
            for k1 in self.time_list:
                result['TimeList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.time_list = []
        if m.get('TimeList') is not None:
            for k1 in m.get('TimeList'):
                temp_model = main_models.GetAuditCountDistributionResponseBodyTimeList()
                self.time_list.append(temp_model.from_map(k1))

        return self

class GetAuditCountDistributionResponseBodyTimeList(DaraModel):
    def __init__(
        self,
        begin_date: str = None,
        end_date: str = None,
        risk_count: int = None,
        session_count: int = None,
        sql_count: int = None,
    ):
        self.begin_date = begin_date
        self.end_date = end_date
        self.risk_count = risk_count
        self.session_count = session_count
        self.sql_count = sql_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.begin_date is not None:
            result['BeginDate'] = self.begin_date

        if self.end_date is not None:
            result['EndDate'] = self.end_date

        if self.risk_count is not None:
            result['RiskCount'] = self.risk_count

        if self.session_count is not None:
            result['SessionCount'] = self.session_count

        if self.sql_count is not None:
            result['SqlCount'] = self.sql_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginDate') is not None:
            self.begin_date = m.get('BeginDate')

        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')

        if m.get('RiskCount') is not None:
            self.risk_count = m.get('RiskCount')

        if m.get('SessionCount') is not None:
            self.session_count = m.get('SessionCount')

        if m.get('SqlCount') is not None:
            self.sql_count = m.get('SqlCount')

        return self

