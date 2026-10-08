# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateK8sSlbRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        cluster_id: str = None,
        disable_force_override: bool = None,
        port: str = None,
        scheduler: str = None,
        service_port_infos: str = None,
        slb_name: str = None,
        slb_protocol: str = None,
        specification: str = None,
        target_port: str = None,
        type: str = None,
    ):
        # The ID of the application. Call [ListApplication](https://help.aliyun.com/document_detail/149390.html) to get this ID.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The ID of the cluster. Call [GetK8sCluster](https://help.aliyun.com/document_detail/181437.html) to get this ID.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # Specifies whether to disable overwriting the SLB listener configuration.
        # 
        # - true: Disables overwriting.
        # 
        # - false: Allows overwriting.
        self.disable_force_override = disable_force_override
        # The frontend port. The value ranges from 1 to 65535.
        self.port = port
        # The scheduling algorithm of the SLB instance. If you do not set this parameter, rr is used. The supported algorithms are round-robin (rr) and weighted round-robin (wrr).
        # 
        # - Weighted round-robin (wrr): Backend servers with higher weights receive more requests.
        # 
        # - Round-robin (rr): Requests are distributed to backend servers in sequence.
        self.scheduler = scheduler
        # This parameter is used for scenarios that involve multiple ports or protocols other than TCP. The value must be a JSON array. For example:
        # [{"targetPort":8080,"port":82,"loadBalancerProtocol":"TCP"},{"port":81,"certId":"1362469756373809_16c185d6fa2_1914500329_-xxxxxxx","targetPort":8181,"loadBalancerProtocol":"HTTPS"}]
        # 
        # - port: Required. The frontend port. The value ranges from 1 to 65535. Each port number must be unique.
        # 
        # - targetPort: Required. The backend port. The value ranges from 1 to 65535.
        # 
        # - loadBalancerProtocol: Required. Only TCP and HTTPS are supported. For HTTP listeners, set this parameter to TCP.
        # 
        # - certId: This parameter is required for HTTPS listeners. It specifies the ID of a certificate that you can purchase in the SLB console.
        # 
        # - Note: This parameter is used to support multiple ports and must be used with the appId, clusterId, type, and slbId parameters.
        self.service_port_infos = service_port_infos
        # The name of the SLB instance.
        self.slb_name = slb_name
        # The protocol of the SLB instance. Currently, only TCP is supported.
        self.slb_protocol = slb_protocol
        # The specification of the SLB instance. The following specifications are supported:
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
        # 
        # If you do not set this parameter, the default value is slb.s1.small.
        self.specification = specification
        # The backend port, which is the service port of the application. The value ranges from 1 to 65535.
        self.target_port = target_port
        # The type of the SLB instance.
        # 
        # - Internet: An Internet-facing instance.
        # 
        # - Intranet: An internal-facing instance.
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

        if self.disable_force_override is not None:
            result['DisableForceOverride'] = self.disable_force_override

        if self.port is not None:
            result['Port'] = self.port

        if self.scheduler is not None:
            result['Scheduler'] = self.scheduler

        if self.service_port_infos is not None:
            result['ServicePortInfos'] = self.service_port_infos

        if self.slb_name is not None:
            result['SlbName'] = self.slb_name

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

        if m.get('DisableForceOverride') is not None:
            self.disable_force_override = m.get('DisableForceOverride')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('Scheduler') is not None:
            self.scheduler = m.get('Scheduler')

        if m.get('ServicePortInfos') is not None:
            self.service_port_infos = m.get('ServicePortInfos')

        if m.get('SlbName') is not None:
            self.slb_name = m.get('SlbName')

        if m.get('SlbProtocol') is not None:
            self.slb_protocol = m.get('SlbProtocol')

        if m.get('Specification') is not None:
            self.specification = m.get('Specification')

        if m.get('TargetPort') is not None:
            self.target_port = m.get('TargetPort')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

