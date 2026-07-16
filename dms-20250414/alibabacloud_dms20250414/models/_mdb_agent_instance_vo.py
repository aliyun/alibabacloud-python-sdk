# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class MdbAgentInstanceVo(DaraModel):
    def __init__(
        self,
        access_url: str = None,
        charge_type: str = None,
        engine_instance_id: str = None,
        engine_region: str = None,
        engine_type: str = None,
        gmt_create: str = None,
        instance_id: str = None,
        instance_name: str = None,
        last_active_time: str = None,
        lock_time: str = None,
        order_id: str = None,
        public_domain: str = None,
        status: int = None,
        status_desc: str = None,
        status_message: str = None,
    ):
        self.access_url = access_url
        self.charge_type = charge_type
        self.engine_instance_id = engine_instance_id
        self.engine_region = engine_region
        self.engine_type = engine_type
        self.gmt_create = gmt_create
        self.instance_id = instance_id
        self.instance_name = instance_name
        self.last_active_time = last_active_time
        self.lock_time = lock_time
        self.order_id = order_id
        self.public_domain = public_domain
        self.status = status
        self.status_desc = status_desc
        self.status_message = status_message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_url is not None:
            result['AccessUrl'] = self.access_url

        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.engine_instance_id is not None:
            result['EngineInstanceId'] = self.engine_instance_id

        if self.engine_region is not None:
            result['EngineRegion'] = self.engine_region

        if self.engine_type is not None:
            result['EngineType'] = self.engine_type

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.last_active_time is not None:
            result['LastActiveTime'] = self.last_active_time

        if self.lock_time is not None:
            result['LockTime'] = self.lock_time

        if self.order_id is not None:
            result['OrderId'] = self.order_id

        if self.public_domain is not None:
            result['PublicDomain'] = self.public_domain

        if self.status is not None:
            result['Status'] = self.status

        if self.status_desc is not None:
            result['StatusDesc'] = self.status_desc

        if self.status_message is not None:
            result['StatusMessage'] = self.status_message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessUrl') is not None:
            self.access_url = m.get('AccessUrl')

        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('EngineInstanceId') is not None:
            self.engine_instance_id = m.get('EngineInstanceId')

        if m.get('EngineRegion') is not None:
            self.engine_region = m.get('EngineRegion')

        if m.get('EngineType') is not None:
            self.engine_type = m.get('EngineType')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('LastActiveTime') is not None:
            self.last_active_time = m.get('LastActiveTime')

        if m.get('LockTime') is not None:
            self.lock_time = m.get('LockTime')

        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        if m.get('PublicDomain') is not None:
            self.public_domain = m.get('PublicDomain')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StatusDesc') is not None:
            self.status_desc = m.get('StatusDesc')

        if m.get('StatusMessage') is not None:
            self.status_message = m.get('StatusMessage')

        return self

