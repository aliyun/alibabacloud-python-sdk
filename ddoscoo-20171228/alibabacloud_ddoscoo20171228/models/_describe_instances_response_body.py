# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ddoscoo20171228 import models as main_models
from darabonba.model import DaraModel

class DescribeInstancesResponseBody(DaraModel):
    def __init__(
        self,
        instances: List[main_models.DescribeInstancesResponseBodyInstances] = None,
        request_id: str = None,
        total: int = None,
    ):
        self.instances = instances
        self.request_id = request_id
        self.total = total

    def validate(self):
        if self.instances:
            for v1 in self.instances:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Instances'] = []
        if self.instances is not None:
            for k1 in self.instances:
                result['Instances'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instances = []
        if m.get('Instances') is not None:
            for k1 in m.get('Instances'):
                temp_model = main_models.DescribeInstancesResponseBodyInstances()
                self.instances.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class DescribeInstancesResponseBodyInstances(DaraModel):
    def __init__(
        self,
        debt_status: int = None,
        edition: int = None,
        enabled: int = None,
        expire_time: int = None,
        gmt_create: int = None,
        instance_id: str = None,
        remark: str = None,
        status: int = None,
    ):
        self.debt_status = debt_status
        self.edition = edition
        self.enabled = enabled
        self.expire_time = expire_time
        self.gmt_create = gmt_create
        self.instance_id = instance_id
        self.remark = remark
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.debt_status is not None:
            result['DebtStatus'] = self.debt_status

        if self.edition is not None:
            result['Edition'] = self.edition

        if self.enabled is not None:
            result['Enabled'] = self.enabled

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DebtStatus') is not None:
            self.debt_status = m.get('DebtStatus')

        if m.get('Edition') is not None:
            self.edition = m.get('Edition')

        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

