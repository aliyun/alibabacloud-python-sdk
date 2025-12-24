# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class OperateRerunJobRequest(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        cluster_id: str = None,
        data_time: str = None,
        end_date: int = None,
        job_id: int = None,
        start_date: int = None,
    ):
        # This parameter is required.
        self.app_name = app_name
        # This parameter is required.
        self.cluster_id = cluster_id
        # This parameter is required.
        self.data_time = data_time
        # This parameter is required.
        self.end_date = end_date
        # This parameter is required.
        self.job_id = job_id
        # This parameter is required.
        self.start_date = start_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.data_time is not None:
            result['DataTime'] = self.data_time

        if self.end_date is not None:
            result['EndDate'] = self.end_date

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.start_date is not None:
            result['StartDate'] = self.start_date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('DataTime') is not None:
            self.data_time = m.get('DataTime')

        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')

        return self

