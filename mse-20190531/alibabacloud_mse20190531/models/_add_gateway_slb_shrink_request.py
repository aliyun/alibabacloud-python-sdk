# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddGatewaySlbShrinkRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        gateway_unique_id: str = None,
        http_port: int = None,
        https_port: int = None,
        https_vserver_group_id: str = None,
        service_weight: int = None,
        slb_id: str = None,
        type: str = None,
        vserver_group_id: str = None,
        vservice_list_shrink: str = None,
    ):
        # The language of the response. Valid values:
        # 
        # *   zh: Chinese
        # *   en: English
        self.accept_language = accept_language
        # The unique ID of the gateway.
        # 
        # This parameter is required.
        self.gateway_unique_id = gateway_unique_id
        # The HTTP port number (virtual service group).
        self.http_port = http_port
        # The HTTPS port number (virtual service group).
        self.https_port = https_port
        # The ID of the HTTPS virtual service group.
        self.https_vserver_group_id = https_vserver_group_id
        # The service weight.
        self.service_weight = service_weight
        # The ID of the SLB instance.
        # 
        # This parameter is required.
        self.slb_id = slb_id
        # The type of the service source. Valid values:
        # 
        # *   PUB_NET: Internet
        # *   PRIVATE_NET: VPC
        self.type = type
        # The ID of the HTTP virtual service group.
        self.vserver_group_id = vserver_group_id
        # The SLB monitoring information.
        self.vservice_list_shrink = vservice_list_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language

        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id

        if self.http_port is not None:
            result['HttpPort'] = self.http_port

        if self.https_port is not None:
            result['HttpsPort'] = self.https_port

        if self.https_vserver_group_id is not None:
            result['HttpsVServerGroupId'] = self.https_vserver_group_id

        if self.service_weight is not None:
            result['ServiceWeight'] = self.service_weight

        if self.slb_id is not None:
            result['SlbId'] = self.slb_id

        if self.type is not None:
            result['Type'] = self.type

        if self.vserver_group_id is not None:
            result['VServerGroupId'] = self.vserver_group_id

        if self.vservice_list_shrink is not None:
            result['VServiceList'] = self.vservice_list_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')

        if m.get('HttpPort') is not None:
            self.http_port = m.get('HttpPort')

        if m.get('HttpsPort') is not None:
            self.https_port = m.get('HttpsPort')

        if m.get('HttpsVServerGroupId') is not None:
            self.https_vserver_group_id = m.get('HttpsVServerGroupId')

        if m.get('ServiceWeight') is not None:
            self.service_weight = m.get('ServiceWeight')

        if m.get('SlbId') is not None:
            self.slb_id = m.get('SlbId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('VServerGroupId') is not None:
            self.vserver_group_id = m.get('VServerGroupId')

        if m.get('VServiceList') is not None:
            self.vservice_list_shrink = m.get('VServiceList')

        return self

