# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PrometheusManagedInstance(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        instance_type: str = None,
        prometheus_instance_id: str = None,
        prometheus_instance_name: str = None,
        region_id: str = None,
        status: str = None,
        workspace: str = None,
    ):
        self.create_time = create_time
        self.instance_type = instance_type
        self.prometheus_instance_id = prometheus_instance_id
        self.prometheus_instance_name = prometheus_instance_name
        self.region_id = region_id
        self.status = status
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.instance_type is not None:
            result['instanceType'] = self.instance_type

        if self.prometheus_instance_id is not None:
            result['prometheusInstanceId'] = self.prometheus_instance_id

        if self.prometheus_instance_name is not None:
            result['prometheusInstanceName'] = self.prometheus_instance_name

        if self.region_id is not None:
            result['regionId'] = self.region_id

        if self.status is not None:
            result['status'] = self.status

        if self.workspace is not None:
            result['workspace'] = self.workspace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('instanceType') is not None:
            self.instance_type = m.get('instanceType')

        if m.get('prometheusInstanceId') is not None:
            self.prometheus_instance_id = m.get('prometheusInstanceId')

        if m.get('prometheusInstanceName') is not None:
            self.prometheus_instance_name = m.get('prometheusInstanceName')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')

        return self

