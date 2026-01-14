# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryClusterInfoRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        acl_switch: bool = None,
        cluster_id: str = None,
        instance_id: str = None,
        order_id: str = None,
        region_id: str = None,
        request_pars: str = None,
    ):
        # The language of the response. Valid values:
        # 
        # *   zh: Chinese
        # *   en: English
        self.accept_language = accept_language
        # Specifies whether to query the configuration of a public IP address whitelist.
        self.acl_switch = acl_switch
        # The ID of the instance.
        self.cluster_id = cluster_id
        # The ID of the instance.
        self.instance_id = instance_id
        # The ID of the order.
        self.order_id = order_id
        # The ID of the region.
        self.region_id = region_id
        # The extended request parameters in the JSON format.
        self.request_pars = request_pars

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language

        if self.acl_switch is not None:
            result['AclSwitch'] = self.acl_switch

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.order_id is not None:
            result['OrderId'] = self.order_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.request_pars is not None:
            result['RequestPars'] = self.request_pars

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('AclSwitch') is not None:
            self.acl_switch = m.get('AclSwitch')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RequestPars') is not None:
            self.request_pars = m.get('RequestPars')

        return self

