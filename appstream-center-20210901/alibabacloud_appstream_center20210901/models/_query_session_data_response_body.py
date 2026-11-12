# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_appstream_center20210901 import models as main_models
from darabonba.model import DaraModel

class QuerySessionDataResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        index_data: List[main_models.QuerySessionDataResponseBodyIndexData] = None,
        message: str = None,
        request_id: str = None,
    ):
        # The return code. It is empty when the request is successful and data is found. NO_DATA is returned when the query result is empty. A corresponding error code is returned when the request fails. For example, InvalidParameter.DateFormat is returned when the format of the statistical parameter is invalid.
        self.code = code
        # The list of session trend data, sorted in ascending order by hour and minute. An empty array is returned when there is no session data on the specified date, and the return code is NO_DATA.
        self.index_data = index_data
        # The return message. It is empty when the request is successful. A corresponding error description is returned when the request fails.
        self.message = message
        # The ID of the request, used to locate call records and troubleshoot issues. The example is a partially desensitized value.
        self.request_id = request_id

    def validate(self):
        if self.index_data:
            for v1 in self.index_data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        result['IndexData'] = []
        if self.index_data is not None:
            for k1 in self.index_data:
                result['IndexData'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.index_data = []
        if m.get('IndexData') is not None:
            for k1 in m.get('IndexData'):
                temp_model = main_models.QuerySessionDataResponseBodyIndexData()
                self.index_data.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class QuerySessionDataResponseBodyIndexData(DaraModel):
    def __init__(
        self,
        hh: str = None,
        mi: str = None,
        session_cnt_mi: int = None,
        stat_date: str = None,
    ):
        # The hour to which the session data belongs, with a value range of 00 to 23 (full hours).
        self.hh = hh
        # The minute to which the session data belongs, aggregated in 10-minute intervals, with a value range of 00 to 50 (namely 00, 10, 20, 30, 40, and 50).
        self.mi = mi
        # The total number of sessions within the hour and minute interval (10-minute granularity).
        self.session_cnt_mi = session_cnt_mi
        # The statistical date to which the session data belongs, in the yyyyMMdd format, consistent with the request parameter StatDate.
        self.stat_date = stat_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.hh is not None:
            result['Hh'] = self.hh

        if self.mi is not None:
            result['Mi'] = self.mi

        if self.session_cnt_mi is not None:
            result['SessionCntMi'] = self.session_cnt_mi

        if self.stat_date is not None:
            result['StatDate'] = self.stat_date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Hh') is not None:
            self.hh = m.get('Hh')

        if m.get('Mi') is not None:
            self.mi = m.get('Mi')

        if m.get('SessionCntMi') is not None:
            self.session_cnt_mi = m.get('SessionCntMi')

        if m.get('StatDate') is not None:
            self.stat_date = m.get('StatDate')

        return self

