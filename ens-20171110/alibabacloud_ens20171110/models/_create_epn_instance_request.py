# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateEpnInstanceRequest(DaraModel):
    def __init__(
        self,
        epninstance_name: str = None,
        epninstance_type: str = None,
        internet_charge_type: str = None,
        internet_max_bandwidth_out: int = None,
        networking_model: str = None,
    ):
        # The name of the Edge-to-Edge network instance.
        self.epninstance_name = epninstance_name
        # The type of the Edge-to-Edge communication instance. Valid value: **EdgeToEdge**.
        # 
        # This parameter is required.
        self.epninstance_type = epninstance_type
        # The network billing type. Valid values:
        # 
        # - **BandwidthByDay**: Daily peak bandwidth.
        # - **95BandwidthByMonth**: Monthly 95th percentile peak bandwidth.
        # - **PayByBandwidth4thMonth**: Monthly fourth peak bandwidth.
        # - **PayByBandwidth**: Bandwidth with defined specifications.
        # 
        # Only one of the Billable methods is supported. If a billing method already exists, the new value is invalid by default, and the existing one prevails.
        # 
        # This parameter is required.
        self.internet_charge_type = internet_charge_type
        # The maximum outbound bandwidth to the Internet. Unit: Mbit/s. Valid values: 1 to 100.
        # 
        # This parameter is required.
        self.internet_max_bandwidth_out = internet_max_bandwidth_out
        # The networking mode. Valid values:
        # - **SpeedUp**: Intelligent acceleration (Internet).
        # - **Connection**: Internal network connectivity (internal network mode).
        # - **SpeedUpAndConnection**: Intelligent acceleration and internal network connectivity (internal network mode).
        # 
        # This parameter is required.
        self.networking_model = networking_model

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.epninstance_name is not None:
            result['EPNInstanceName'] = self.epninstance_name

        if self.epninstance_type is not None:
            result['EPNInstanceType'] = self.epninstance_type

        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type

        if self.internet_max_bandwidth_out is not None:
            result['InternetMaxBandwidthOut'] = self.internet_max_bandwidth_out

        if self.networking_model is not None:
            result['NetworkingModel'] = self.networking_model

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EPNInstanceName') is not None:
            self.epninstance_name = m.get('EPNInstanceName')

        if m.get('EPNInstanceType') is not None:
            self.epninstance_type = m.get('EPNInstanceType')

        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')

        if m.get('InternetMaxBandwidthOut') is not None:
            self.internet_max_bandwidth_out = m.get('InternetMaxBandwidthOut')

        if m.get('NetworkingModel') is not None:
            self.networking_model = m.get('NetworkingModel')

        return self

