# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sophonsoar20220728 import models as main_models
from darabonba.model import DaraModel

class DescribeProcessStatisticsResponseBody(DaraModel):
    def __init__(
        self,
        metrics: main_models.DescribeProcessStatisticsResponseBodyMetrics = None,
        request_id: str = None,
    ):
        # The data returned.
        self.metrics = metrics
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.metrics:
            self.metrics.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.metrics is not None:
            result['Metrics'] = self.metrics.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Metrics') is not None:
            temp_model = main_models.DescribeProcessStatisticsResponseBodyMetrics()
            self.metrics = temp_model.from_map(m.get('Metrics'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeProcessStatisticsResponseBodyMetrics(DaraModel):
    def __init__(
        self,
        ban_file_num: int = None,
        ban_ip_num: int = None,
        ban_process_num: int = None,
        task_num: int = None,
    ):
        # The number of blocked files.
        self.ban_file_num = ban_file_num
        # The number of blocked IP addresses.
        self.ban_ip_num = ban_ip_num
        # The number of blocked processes.
        self.ban_process_num = ban_process_num
        # The number of handling tasks.
        self.task_num = task_num

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ban_file_num is not None:
            result['BanFileNum'] = self.ban_file_num

        if self.ban_ip_num is not None:
            result['BanIpNum'] = self.ban_ip_num

        if self.ban_process_num is not None:
            result['BanProcessNum'] = self.ban_process_num

        if self.task_num is not None:
            result['TaskNum'] = self.task_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BanFileNum') is not None:
            self.ban_file_num = m.get('BanFileNum')

        if m.get('BanIpNum') is not None:
            self.ban_ip_num = m.get('BanIpNum')

        if m.get('BanProcessNum') is not None:
            self.ban_process_num = m.get('BanProcessNum')

        if m.get('TaskNum') is not None:
            self.task_num = m.get('TaskNum')

        return self

