# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetLoadBalancerTCPListenerAttributeRequest(DaraModel):
    def __init__(
        self,
        connect_port: int = None,
        connect_timeout: int = None,
        health_check: str = None,
        healthy_threshold: int = None,
        host_id: str = None,
        interval: int = None,
        listener_port: int = None,
        load_balancer_id: str = None,
        owner_account: str = None,
        owner_id: str = None,
        persistence_timeout: int = None,
        scheduler: str = None,
        unhealthy_threshold: int = None,
    ):
        self.connect_port = connect_port
        self.connect_timeout = connect_timeout
        self.health_check = health_check
        self.healthy_threshold = healthy_threshold
        self.host_id = host_id
        self.interval = interval
        self.listener_port = listener_port
        self.load_balancer_id = load_balancer_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.persistence_timeout = persistence_timeout
        self.scheduler = scheduler
        self.unhealthy_threshold = unhealthy_threshold

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.connect_port is not None:
            result['ConnectPort'] = self.connect_port

        if self.connect_timeout is not None:
            result['ConnectTimeout'] = self.connect_timeout

        if self.health_check is not None:
            result['HealthCheck'] = self.health_check

        if self.healthy_threshold is not None:
            result['HealthyThreshold'] = self.healthy_threshold

        if self.host_id is not None:
            result['HostId'] = self.host_id

        if self.interval is not None:
            result['Interval'] = self.interval

        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port

        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.persistence_timeout is not None:
            result['PersistenceTimeout'] = self.persistence_timeout

        if self.scheduler is not None:
            result['Scheduler'] = self.scheduler

        if self.unhealthy_threshold is not None:
            result['UnhealthyThreshold'] = self.unhealthy_threshold

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectPort') is not None:
            self.connect_port = m.get('ConnectPort')

        if m.get('ConnectTimeout') is not None:
            self.connect_timeout = m.get('ConnectTimeout')

        if m.get('HealthCheck') is not None:
            self.health_check = m.get('HealthCheck')

        if m.get('HealthyThreshold') is not None:
            self.healthy_threshold = m.get('HealthyThreshold')

        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')

        if m.get('Interval') is not None:
            self.interval = m.get('Interval')

        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')

        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PersistenceTimeout') is not None:
            self.persistence_timeout = m.get('PersistenceTimeout')

        if m.get('Scheduler') is not None:
            self.scheduler = m.get('Scheduler')

        if m.get('UnhealthyThreshold') is not None:
            self.unhealthy_threshold = m.get('UnhealthyThreshold')

        return self

