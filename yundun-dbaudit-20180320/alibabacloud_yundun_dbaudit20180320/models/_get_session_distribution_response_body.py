# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_yundun_dbaudit20180320 import models as main_models
from darabonba.model import DaraModel

class GetSessionDistributionResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        time_list: List[main_models.GetSessionDistributionResponseBodyTimeList] = None,
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
                temp_model = main_models.GetSessionDistributionResponseBodyTimeList()
                self.time_list.append(temp_model.from_map(k1))

        return self

class GetSessionDistributionResponseBodyTimeList(DaraModel):
    def __init__(
        self,
        active_session_count: int = None,
        begin_date: str = None,
        end_date: str = None,
        error_session_count: int = None,
        login_session_count: int = None,
    ):
        self.active_session_count = active_session_count
        self.begin_date = begin_date
        self.end_date = end_date
        self.error_session_count = error_session_count
        self.login_session_count = login_session_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.active_session_count is not None:
            result['ActiveSessionCount'] = self.active_session_count

        if self.begin_date is not None:
            result['BeginDate'] = self.begin_date

        if self.end_date is not None:
            result['EndDate'] = self.end_date

        if self.error_session_count is not None:
            result['ErrorSessionCount'] = self.error_session_count

        if self.login_session_count is not None:
            result['LoginSessionCount'] = self.login_session_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActiveSessionCount') is not None:
            self.active_session_count = m.get('ActiveSessionCount')

        if m.get('BeginDate') is not None:
            self.begin_date = m.get('BeginDate')

        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')

        if m.get('ErrorSessionCount') is not None:
            self.error_session_count = m.get('ErrorSessionCount')

        if m.get('LoginSessionCount') is not None:
            self.login_session_count = m.get('LoginSessionCount')

        return self

