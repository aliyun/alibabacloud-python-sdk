# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryReleaseMetricRequest(DaraModel):
    def __init__(
        self,
        change_order_id: str = None,
        create_time: int = None,
        metric_type: str = None,
        pid: str = None,
        proxy_user_id: str = None,
        release_end_time: int = None,
        release_start_time: int = None,
        service: str = None,
    ):
        # The ID of the change order.
        # 
        # This parameter is required.
        self.change_order_id = change_order_id
        # The time when the change order was created.
        self.create_time = create_time
        # The type of the metric that you want to query.
        self.metric_type = metric_type
        # The ID of the Enterprise Distributed Application Service (EDAS) or Kubernetes application.
        # 
        # This parameter is required.
        self.pid = pid
        # This parameter is not in use.
        self.proxy_user_id = proxy_user_id
        # The end time of the version release.
        # 
        # This parameter is required.
        self.release_end_time = release_end_time
        # The start time of the version release.
        # 
        # This parameter is required.
        self.release_start_time = release_start_time
        # The service that you want to query.
        self.service = service

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.change_order_id is not None:
            result['ChangeOrderId'] = self.change_order_id

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.metric_type is not None:
            result['MetricType'] = self.metric_type

        if self.pid is not None:
            result['Pid'] = self.pid

        if self.proxy_user_id is not None:
            result['ProxyUserId'] = self.proxy_user_id

        if self.release_end_time is not None:
            result['ReleaseEndTime'] = self.release_end_time

        if self.release_start_time is not None:
            result['ReleaseStartTime'] = self.release_start_time

        if self.service is not None:
            result['Service'] = self.service

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChangeOrderId') is not None:
            self.change_order_id = m.get('ChangeOrderId')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('MetricType') is not None:
            self.metric_type = m.get('MetricType')

        if m.get('Pid') is not None:
            self.pid = m.get('Pid')

        if m.get('ProxyUserId') is not None:
            self.proxy_user_id = m.get('ProxyUserId')

        if m.get('ReleaseEndTime') is not None:
            self.release_end_time = m.get('ReleaseEndTime')

        if m.get('ReleaseStartTime') is not None:
            self.release_start_time = m.get('ReleaseStartTime')

        if m.get('Service') is not None:
            self.service = m.get('Service')

        return self

