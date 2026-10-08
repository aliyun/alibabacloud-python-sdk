# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class BindEcsSlbRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        deploy_group_id: str = None,
        listener_health_check_url: str = None,
        listener_port: int = None,
        listener_protocol: str = None,
        slb_id: str = None,
        vforwarding_url_rule: str = None,
        vserver_group_id: str = None,
        vserver_group_name: str = None,
    ):
        # The ID of the application. You can query the application ID by calling the ListApplication operation. For more information, see [ListApplication](https://help.aliyun.com/document_detail/149390.html).
        # 
        # This parameter is required.
        self.app_id = app_id
        # The ID of the instance group whose application you want to bind. You can call the ListDeployGroup operation to query the group ID. For more information, see [ListDeployGroup](https://help.aliyun.com/document_detail/62077.html).
        self.deploy_group_id = deploy_group_id
        # The health check URL.
        self.listener_health_check_url = listener_health_check_url
        # The listener port for the SLB instance.
        # 
        # This parameter is required.
        self.listener_port = listener_port
        # The listener protocol for the SLB instance.
        # 
        # This parameter is required.
        self.listener_protocol = listener_protocol
        # The ID of the SLB instance.
        # 
        # This parameter is required.
        self.slb_id = slb_id
        # The forwarding rule of the SLB listener.
        self.vforwarding_url_rule = vforwarding_url_rule
        # The ID of the vServer group for the SLB instance.
        self.vserver_group_id = vserver_group_id
        # The name of the vServer group.
        self.vserver_group_name = vserver_group_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.deploy_group_id is not None:
            result['DeployGroupId'] = self.deploy_group_id

        if self.listener_health_check_url is not None:
            result['ListenerHealthCheckUrl'] = self.listener_health_check_url

        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port

        if self.listener_protocol is not None:
            result['ListenerProtocol'] = self.listener_protocol

        if self.slb_id is not None:
            result['SlbId'] = self.slb_id

        if self.vforwarding_url_rule is not None:
            result['VForwardingUrlRule'] = self.vforwarding_url_rule

        if self.vserver_group_id is not None:
            result['VServerGroupId'] = self.vserver_group_id

        if self.vserver_group_name is not None:
            result['VServerGroupName'] = self.vserver_group_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('DeployGroupId') is not None:
            self.deploy_group_id = m.get('DeployGroupId')

        if m.get('ListenerHealthCheckUrl') is not None:
            self.listener_health_check_url = m.get('ListenerHealthCheckUrl')

        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')

        if m.get('ListenerProtocol') is not None:
            self.listener_protocol = m.get('ListenerProtocol')

        if m.get('SlbId') is not None:
            self.slb_id = m.get('SlbId')

        if m.get('VForwardingUrlRule') is not None:
            self.vforwarding_url_rule = m.get('VForwardingUrlRule')

        if m.get('VServerGroupId') is not None:
            self.vserver_group_id = m.get('VServerGroupId')

        if m.get('VServerGroupName') is not None:
            self.vserver_group_name = m.get('VServerGroupName')

        return self

