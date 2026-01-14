# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetKubernetesSourceRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        gateway_unique_id: str = None,
        is_all: bool = None,
        vpc_id: str = None,
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
        # Specifies whether to obtain the information about all Kubernetes clusters. If you set the value to false, only the information about unassociated clusters is obtained.
        self.is_all = is_all
        # The ID of the virtual private cloud (VPC).
        self.vpc_id = vpc_id

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

        if self.is_all is not None:
            result['IsAll'] = self.is_all

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')

        if m.get('IsAll') is not None:
            self.is_all = m.get('IsAll')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

