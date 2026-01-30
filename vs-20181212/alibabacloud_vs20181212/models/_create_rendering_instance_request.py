# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_vs20181212 import models as main_models
from darabonba.model import DaraModel

class CreateRenderingInstanceRequest(DaraModel):
    def __init__(
        self,
        attributes: main_models.CreateRenderingInstanceRequestAttributes = None,
        auto_renew: bool = None,
        client_info: main_models.CreateRenderingInstanceRequestClientInfo = None,
        instance_billing_cycle: str = None,
        instance_charge_type: str = None,
        internet_charge_type: str = None,
        internet_max_bandwidth: int = None,
        period: str = None,
        rendering_spec: str = None,
        storage_size: str = None,
    ):
        self.attributes = attributes
        self.auto_renew = auto_renew
        self.client_info = client_info
        self.instance_billing_cycle = instance_billing_cycle
        self.instance_charge_type = instance_charge_type
        self.internet_charge_type = internet_charge_type
        self.internet_max_bandwidth = internet_max_bandwidth
        self.period = period
        # This parameter is required.
        self.rendering_spec = rendering_spec
        self.storage_size = storage_size

    def validate(self):
        if self.attributes:
            self.attributes.validate()
        if self.client_info:
            self.client_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attributes is not None:
            result['Attributes'] = self.attributes.to_map()

        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew

        if self.client_info is not None:
            result['ClientInfo'] = self.client_info.to_map()

        if self.instance_billing_cycle is not None:
            result['InstanceBillingCycle'] = self.instance_billing_cycle

        if self.instance_charge_type is not None:
            result['InstanceChargeType'] = self.instance_charge_type

        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type

        if self.internet_max_bandwidth is not None:
            result['InternetMaxBandwidth'] = self.internet_max_bandwidth

        if self.period is not None:
            result['Period'] = self.period

        if self.rendering_spec is not None:
            result['RenderingSpec'] = self.rendering_spec

        if self.storage_size is not None:
            result['StorageSize'] = self.storage_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Attributes') is not None:
            temp_model = main_models.CreateRenderingInstanceRequestAttributes()
            self.attributes = temp_model.from_map(m.get('Attributes'))

        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')

        if m.get('ClientInfo') is not None:
            temp_model = main_models.CreateRenderingInstanceRequestClientInfo()
            self.client_info = temp_model.from_map(m.get('ClientInfo'))

        if m.get('InstanceBillingCycle') is not None:
            self.instance_billing_cycle = m.get('InstanceBillingCycle')

        if m.get('InstanceChargeType') is not None:
            self.instance_charge_type = m.get('InstanceChargeType')

        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')

        if m.get('InternetMaxBandwidth') is not None:
            self.internet_max_bandwidth = m.get('InternetMaxBandwidth')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('RenderingSpec') is not None:
            self.rendering_spec = m.get('RenderingSpec')

        if m.get('StorageSize') is not None:
            self.storage_size = m.get('StorageSize')

        return self

class CreateRenderingInstanceRequestClientInfo(DaraModel):
    def __init__(
        self,
        client_ip: str = None,
    ):
        self.client_ip = client_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_ip is not None:
            result['ClientIp'] = self.client_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientIp') is not None:
            self.client_ip = m.get('ClientIp')

        return self

class CreateRenderingInstanceRequestAttributes(DaraModel):
    def __init__(
        self,
        edge_media_service: str = None,
        in_access: str = None,
        out_access: str = None,
        zone: str = None,
    ):
        self.edge_media_service = edge_media_service
        self.in_access = in_access
        self.out_access = out_access
        self.zone = zone

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.edge_media_service is not None:
            result['EdgeMediaService'] = self.edge_media_service

        if self.in_access is not None:
            result['InAccess'] = self.in_access

        if self.out_access is not None:
            result['OutAccess'] = self.out_access

        if self.zone is not None:
            result['Zone'] = self.zone

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EdgeMediaService') is not None:
            self.edge_media_service = m.get('EdgeMediaService')

        if m.get('InAccess') is not None:
            self.in_access = m.get('InAccess')

        if m.get('OutAccess') is not None:
            self.out_access = m.get('OutAccess')

        if m.get('Zone') is not None:
            self.zone = m.get('Zone')

        return self

