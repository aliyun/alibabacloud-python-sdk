# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetLoadBalancerHTTPListenerAttributeRequest(DaraModel):
    def __init__(
        self,
        cookie: str = None,
        cookie_timeout: int = None,
        domain: str = None,
        health_check: str = None,
        health_check_timeout: int = None,
        healthy_threshold: int = None,
        host_id: str = None,
        interval: int = None,
        listener_port: int = None,
        load_balancer_id: str = None,
        owner_account: str = None,
        owner_id: str = None,
        scheduler: str = None,
        sticky_session: str = None,
        sticky_session_type: str = None,
        uri: str = None,
        unhealthy_threshold: int = None,
        xforwarded_for: str = None,
    ):
        self.cookie = cookie
        self.cookie_timeout = cookie_timeout
        self.domain = domain
        self.health_check = health_check
        self.health_check_timeout = health_check_timeout
        self.healthy_threshold = healthy_threshold
        self.host_id = host_id
        self.interval = interval
        self.listener_port = listener_port
        self.load_balancer_id = load_balancer_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.scheduler = scheduler
        self.sticky_session = sticky_session
        self.sticky_session_type = sticky_session_type
        self.uri = uri
        self.unhealthy_threshold = unhealthy_threshold
        self.xforwarded_for = xforwarded_for

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cookie is not None:
            result['Cookie'] = self.cookie

        if self.cookie_timeout is not None:
            result['CookieTimeout'] = self.cookie_timeout

        if self.domain is not None:
            result['Domain'] = self.domain

        if self.health_check is not None:
            result['HealthCheck'] = self.health_check

        if self.health_check_timeout is not None:
            result['HealthCheckTimeout'] = self.health_check_timeout

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

        if self.scheduler is not None:
            result['Scheduler'] = self.scheduler

        if self.sticky_session is not None:
            result['StickySession'] = self.sticky_session

        if self.sticky_session_type is not None:
            result['StickySessionType'] = self.sticky_session_type

        if self.uri is not None:
            result['URI'] = self.uri

        if self.unhealthy_threshold is not None:
            result['UnhealthyThreshold'] = self.unhealthy_threshold

        if self.xforwarded_for is not None:
            result['XForwardedFor'] = self.xforwarded_for

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cookie') is not None:
            self.cookie = m.get('Cookie')

        if m.get('CookieTimeout') is not None:
            self.cookie_timeout = m.get('CookieTimeout')

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('HealthCheck') is not None:
            self.health_check = m.get('HealthCheck')

        if m.get('HealthCheckTimeout') is not None:
            self.health_check_timeout = m.get('HealthCheckTimeout')

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

        if m.get('Scheduler') is not None:
            self.scheduler = m.get('Scheduler')

        if m.get('StickySession') is not None:
            self.sticky_session = m.get('StickySession')

        if m.get('StickySessionType') is not None:
            self.sticky_session_type = m.get('StickySessionType')

        if m.get('URI') is not None:
            self.uri = m.get('URI')

        if m.get('UnhealthyThreshold') is not None:
            self.unhealthy_threshold = m.get('UnhealthyThreshold')

        if m.get('XForwardedFor') is not None:
            self.xforwarded_for = m.get('XForwardedFor')

        return self

