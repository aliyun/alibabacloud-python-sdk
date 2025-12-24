# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateGatewayRequest(DaraModel):
    def __init__(
        self,
        resource_name: str = None,
        auto_renewal: bool = None,
        charge_type: str = None,
        enable_internet: bool = None,
        enable_intranet: bool = None,
        gateway_type: str = None,
        instance_type: str = None,
        name: str = None,
        replicas: int = None,
    ):
        # The resource group ID. To obtain a resource group ID, see the ResourceId field in the response of the [ListResources](https://help.aliyun.com/document_detail/412133.html) operation.
        self.resource_name = resource_name
        # Specifies whether to enable auto-renewal. Valid values:
        # 
        # *   false (default)
        # *   true
        self.auto_renewal = auto_renewal
        # The billing method. Valid values:
        # 
        # *   PrePaid: subscription.
        # *   PostPaid: pay-as-you-go.
        self.charge_type = charge_type
        # Specifies whether to enable Internet access. Default value: false.
        # 
        # Valid values:
        # 
        # *   true
        # *   false
        self.enable_internet = enable_internet
        # Specifies whether to enable private access. Default value: true.
        # 
        # Valid values:
        # 
        # *   true
        # *   false
        self.enable_intranet = enable_intranet
        self.gateway_type = gateway_type
        # The instance type used by the private gateway. Valid values:
        # 
        # *   2c4g
        # *   4c8g
        # *   8c16g
        # *   16c32g
        self.instance_type = instance_type
        # The alias of the private gateway.
        self.name = name
        # The number of nodes in the private gateway.
        self.replicas = replicas

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name

        if self.auto_renewal is not None:
            result['AutoRenewal'] = self.auto_renewal

        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.enable_internet is not None:
            result['EnableInternet'] = self.enable_internet

        if self.enable_intranet is not None:
            result['EnableIntranet'] = self.enable_intranet

        if self.gateway_type is not None:
            result['GatewayType'] = self.gateway_type

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.name is not None:
            result['Name'] = self.name

        if self.replicas is not None:
            result['Replicas'] = self.replicas

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')

        if m.get('AutoRenewal') is not None:
            self.auto_renewal = m.get('AutoRenewal')

        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('EnableInternet') is not None:
            self.enable_internet = m.get('EnableInternet')

        if m.get('EnableIntranet') is not None:
            self.enable_intranet = m.get('EnableIntranet')

        if m.get('GatewayType') is not None:
            self.gateway_type = m.get('GatewayType')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Replicas') is not None:
            self.replicas = m.get('Replicas')

        return self

