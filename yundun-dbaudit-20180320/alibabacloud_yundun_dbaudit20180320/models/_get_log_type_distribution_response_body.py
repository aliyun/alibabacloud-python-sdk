# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_yundun_dbaudit20180320 import models as main_models
from darabonba.model import DaraModel

class GetLogTypeDistributionResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        time_list: List[main_models.GetLogTypeDistributionResponseBodyTimeList] = None,
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
                temp_model = main_models.GetLogTypeDistributionResponseBodyTimeList()
                self.time_list.append(temp_model.from_map(k1))

        return self

class GetLogTypeDistributionResponseBodyTimeList(DaraModel):
    def __init__(
        self,
        begin_date: str = None,
        delete_sql_count: int = None,
        end_date: str = None,
        exec_cost_us: str = None,
        insert_sql_count: int = None,
        other_sql_count: int = None,
        select_sql_count: int = None,
        sql_count: int = None,
        update_sql_count: int = None,
    ):
        self.begin_date = begin_date
        self.delete_sql_count = delete_sql_count
        self.end_date = end_date
        self.exec_cost_us = exec_cost_us
        self.insert_sql_count = insert_sql_count
        self.other_sql_count = other_sql_count
        self.select_sql_count = select_sql_count
        self.sql_count = sql_count
        self.update_sql_count = update_sql_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.begin_date is not None:
            result['BeginDate'] = self.begin_date

        if self.delete_sql_count is not None:
            result['DeleteSqlCount'] = self.delete_sql_count

        if self.end_date is not None:
            result['EndDate'] = self.end_date

        if self.exec_cost_us is not None:
            result['ExecCostUS'] = self.exec_cost_us

        if self.insert_sql_count is not None:
            result['InsertSqlCount'] = self.insert_sql_count

        if self.other_sql_count is not None:
            result['OtherSqlCount'] = self.other_sql_count

        if self.select_sql_count is not None:
            result['SelectSqlCount'] = self.select_sql_count

        if self.sql_count is not None:
            result['SqlCount'] = self.sql_count

        if self.update_sql_count is not None:
            result['UpdateSqlCount'] = self.update_sql_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginDate') is not None:
            self.begin_date = m.get('BeginDate')

        if m.get('DeleteSqlCount') is not None:
            self.delete_sql_count = m.get('DeleteSqlCount')

        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')

        if m.get('ExecCostUS') is not None:
            self.exec_cost_us = m.get('ExecCostUS')

        if m.get('InsertSqlCount') is not None:
            self.insert_sql_count = m.get('InsertSqlCount')

        if m.get('OtherSqlCount') is not None:
            self.other_sql_count = m.get('OtherSqlCount')

        if m.get('SelectSqlCount') is not None:
            self.select_sql_count = m.get('SelectSqlCount')

        if m.get('SqlCount') is not None:
            self.sql_count = m.get('SqlCount')

        if m.get('UpdateSqlCount') is not None:
            self.update_sql_count = m.get('UpdateSqlCount')

        return self

