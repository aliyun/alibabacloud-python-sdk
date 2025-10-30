# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_gpdb20160503 import models as main_models
from darabonba.model import DaraModel

class DescribeDataReDistributeInfoResponseBody(DaraModel):
    def __init__(
        self,
        data_re_distribute_info: main_models.DescribeDataReDistributeInfoResponseBodyDataReDistributeInfo = None,
        request_id: str = None,
    ):
        # The data redistribution information.
        self.data_re_distribute_info = data_re_distribute_info
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data_re_distribute_info:
            self.data_re_distribute_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_re_distribute_info is not None:
            result['DataReDistributeInfo'] = self.data_re_distribute_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataReDistributeInfo') is not None:
            temp_model = main_models.DescribeDataReDistributeInfoResponseBodyDataReDistributeInfo()
            self.data_re_distribute_info = temp_model.from_map(m.get('DataReDistributeInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeDataReDistributeInfoResponseBodyDataReDistributeInfo(DaraModel):
    def __init__(
        self,
        message: str = None,
        progress: int = None,
        remain_time: str = None,
        start_time: str = None,
        status: str = None,
        type: str = None,
    ):
        # The execution information. If an error occurs, the error message is returned.
        self.message = message
        # The progress of data redistribution. Unit: %.
        self.progress = progress
        # The estimated remaining time for data redistribution.
        self.remain_time = remain_time
        # This parameter is not supported.
        self.start_time = start_time
        # The status of data redistribution.
        self.status = status
        # The execution type. The value **immediate** is returned, indicating immediate execution.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.message is not None:
            result['Message'] = self.message

        if self.progress is not None:
            result['Progress'] = self.progress

        if self.remain_time is not None:
            result['RemainTime'] = self.remain_time

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Progress') is not None:
            self.progress = m.get('Progress')

        if m.get('RemainTime') is not None:
            self.remain_time = m.get('RemainTime')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

