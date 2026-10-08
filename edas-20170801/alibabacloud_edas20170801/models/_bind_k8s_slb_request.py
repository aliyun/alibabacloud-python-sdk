# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class BindK8sSlbRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        cluster_id: str = None,
        port: str = None,
        scheduler: str = None,
        service_port_infos: str = None,
        slb_id: str = None,
        slb_protocol: str = None,
        specification: str = None,
        target_port: str = None,
        type: str = None,
    ):
        # The ID of the application.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The ID of the cluster.
        self.cluster_id = cluster_id
        # The frontend port. The value must be an integer from 1 to 65,535.
        self.port = port
        # The scheduling algorithm. If you do not specify this parameter, \\`rr\\` is used. Valid values:
        # 
        # - wrr: weighted round-robin. Backend servers with higher weights receive more requests.
        # 
        # - rr: round-robin. Requests are distributed to backend servers in sequence.
        self.scheduler = scheduler
        # The information about the service ports. Use this parameter to configure multiple listeners or use protocols other than TCP.
        # This parameter must be a JSON array. Example:
        # [{"targetPort":8080,"port":82,"loadBalancerProtocol":"TCP"},{"port":81,"certId":"1362469756373809_16c185d6fa2_1914500329_-xxxxxxx","targetPort":8181,"loadBalancerProtocol":"HTTPS"}]
        # 
        # - port: Required. The frontend port. The value must be an integer from 1 to 65,535. Each port number must be unique.
        # 
        # - targetPort: Required. The backend port. The value must be an integer from 1 to 65,535.
        # 
        # - loadBalancerProtocol: Required. The frontend protocol. Valid values: TCP and HTTPS. For HTTP, use TCP.
        # 
        # - certId: Required if you use the HTTPS protocol. You can purchase a certificate in the SLB console.
        # 
        # > This parameter is used to configure multiple listeners. You must use it with the appId, clusterId, type, and slbId parameters.
        self.service_port_infos = service_port_infos
        # The ID of the SLB instance. If you do not specify this parameter, EDAS automatically purchases a new SLB instance.
        self.slb_id = slb_id
        # The frontend protocol for the SLB instance. Valid values: TCP, HTTP, and HTTPS.
        self.slb_protocol = slb_protocol
        # The specification of the SLB instance.
        # 
        # - slb.s1.small
        # 
        # - slb.s2.small
        # 
        # - slb.s2.medium
        # 
        # - slb.s3.small
        # 
        # - slb.s3.medium
        # 
        # - slb.s3.large
        self.specification = specification
        # The backend port. This port is also the service port of the application. The value must be an integer from 1 to 65,535.
        self.target_port = target_port
        # The type of the SLB instance.
        # 
        # - internet: an internet-facing SLB instance.
        # 
        # - intranet: an internal-facing SLB instance.
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.port is not None:
            result['Port'] = self.port

        if self.scheduler is not None:
            result['Scheduler'] = self.scheduler

        if self.service_port_infos is not None:
            result['ServicePortInfos'] = self.service_port_infos

        if self.slb_id is not None:
            result['SlbId'] = self.slb_id

        if self.slb_protocol is not None:
            result['SlbProtocol'] = self.slb_protocol

        if self.specification is not None:
            result['Specification'] = self.specification

        if self.target_port is not None:
            result['TargetPort'] = self.target_port

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('Scheduler') is not None:
            self.scheduler = m.get('Scheduler')

        if m.get('ServicePortInfos') is not None:
            self.service_port_infos = m.get('ServicePortInfos')

        if m.get('SlbId') is not None:
            self.slb_id = m.get('SlbId')

        if m.get('SlbProtocol') is not None:
            self.slb_protocol = m.get('SlbProtocol')

        if m.get('Specification') is not None:
            self.specification = m.get('Specification')

        if m.get('TargetPort') is not None:
            self.target_port = m.get('TargetPort')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

