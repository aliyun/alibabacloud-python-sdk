# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateLoadBalancerTCPListenerRequest(DaraModel):
    def __init__(
        self,
        backend_server_port: int = None,
        bandwidth: int = None,
        connect_port: int = None,
        connect_timeout: int = None,
        established_timeout: int = None,
        health_check: str = None,
        health_check_domain: str = None,
        health_check_http_code: str = None,
        health_check_type: str = None,
        health_check_uri: str = None,
        healthy_threshold: int = None,
        interval: int = None,
        listener_port: int = None,
        listener_status: str = None,
        load_balancer_id: str = None,
        master_slave_server_group_id: str = None,
        max_connection: int = None,
        owner_account: str = None,
        owner_id: int = None,
        persistence_timeout: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        scheduler: str = None,
        tags: str = None,
        unhealthy_threshold: int = None,
        vserver_group_id: str = None,
        access_key_id: str = None,
    ):
        self.backend_server_port = backend_server_port
        self.bandwidth = bandwidth
        self.connect_port = connect_port
        self.connect_timeout = connect_timeout
        self.established_timeout = established_timeout
        self.health_check = health_check
        self.health_check_domain = health_check_domain
        self.health_check_http_code = health_check_http_code
        self.health_check_type = health_check_type
        self.health_check_uri = health_check_uri
        self.healthy_threshold = healthy_threshold
        self.interval = interval
        # This parameter is required.
        self.listener_port = listener_port
        self.listener_status = listener_status
        # This parameter is required.
        self.load_balancer_id = load_balancer_id
        self.master_slave_server_group_id = master_slave_server_group_id
        self.max_connection = max_connection
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.persistence_timeout = persistence_timeout
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.scheduler = scheduler
        self.tags = tags
        self.unhealthy_threshold = unhealthy_threshold
        self.vserver_group_id = vserver_group_id
        self.access_key_id = access_key_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backend_server_port is not None:
            result['BackendServerPort'] = self.backend_server_port

        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth

        if self.connect_port is not None:
            result['ConnectPort'] = self.connect_port

        if self.connect_timeout is not None:
            result['ConnectTimeout'] = self.connect_timeout

        if self.established_timeout is not None:
            result['EstablishedTimeout'] = self.established_timeout

        if self.health_check is not None:
            result['HealthCheck'] = self.health_check

        if self.health_check_domain is not None:
            result['HealthCheckDomain'] = self.health_check_domain

        if self.health_check_http_code is not None:
            result['HealthCheckHttpCode'] = self.health_check_http_code

        if self.health_check_type is not None:
            result['HealthCheckType'] = self.health_check_type

        if self.health_check_uri is not None:
            result['HealthCheckURI'] = self.health_check_uri

        if self.healthy_threshold is not None:
            result['HealthyThreshold'] = self.healthy_threshold

        if self.interval is not None:
            result['Interval'] = self.interval

        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port

        if self.listener_status is not None:
            result['ListenerStatus'] = self.listener_status

        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id

        if self.master_slave_server_group_id is not None:
            result['MasterSlaveServerGroupId'] = self.master_slave_server_group_id

        if self.max_connection is not None:
            result['MaxConnection'] = self.max_connection

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.persistence_timeout is not None:
            result['PersistenceTimeout'] = self.persistence_timeout

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.scheduler is not None:
            result['Scheduler'] = self.scheduler

        if self.tags is not None:
            result['Tags'] = self.tags

        if self.unhealthy_threshold is not None:
            result['UnhealthyThreshold'] = self.unhealthy_threshold

        if self.vserver_group_id is not None:
            result['VServerGroupId'] = self.vserver_group_id

        if self.access_key_id is not None:
            result['access_key_id'] = self.access_key_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackendServerPort') is not None:
            self.backend_server_port = m.get('BackendServerPort')

        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')

        if m.get('ConnectPort') is not None:
            self.connect_port = m.get('ConnectPort')

        if m.get('ConnectTimeout') is not None:
            self.connect_timeout = m.get('ConnectTimeout')

        if m.get('EstablishedTimeout') is not None:
            self.established_timeout = m.get('EstablishedTimeout')

        if m.get('HealthCheck') is not None:
            self.health_check = m.get('HealthCheck')

        if m.get('HealthCheckDomain') is not None:
            self.health_check_domain = m.get('HealthCheckDomain')

        if m.get('HealthCheckHttpCode') is not None:
            self.health_check_http_code = m.get('HealthCheckHttpCode')

        if m.get('HealthCheckType') is not None:
            self.health_check_type = m.get('HealthCheckType')

        if m.get('HealthCheckURI') is not None:
            self.health_check_uri = m.get('HealthCheckURI')

        if m.get('HealthyThreshold') is not None:
            self.healthy_threshold = m.get('HealthyThreshold')

        if m.get('Interval') is not None:
            self.interval = m.get('Interval')

        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')

        if m.get('ListenerStatus') is not None:
            self.listener_status = m.get('ListenerStatus')

        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')

        if m.get('MasterSlaveServerGroupId') is not None:
            self.master_slave_server_group_id = m.get('MasterSlaveServerGroupId')

        if m.get('MaxConnection') is not None:
            self.max_connection = m.get('MaxConnection')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PersistenceTimeout') is not None:
            self.persistence_timeout = m.get('PersistenceTimeout')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('Scheduler') is not None:
            self.scheduler = m.get('Scheduler')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        if m.get('UnhealthyThreshold') is not None:
            self.unhealthy_threshold = m.get('UnhealthyThreshold')

        if m.get('VServerGroupId') is not None:
            self.vserver_group_id = m.get('VServerGroupId')

        if m.get('access_key_id') is not None:
            self.access_key_id = m.get('access_key_id')

        return self

