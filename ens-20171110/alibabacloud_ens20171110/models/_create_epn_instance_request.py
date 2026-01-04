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
        # The name of the EPN instance.
        self.epninstance_name = epninstance_name
        # The type of the EPN instance. Set the value to **EdgeToEdge**.
        # 
        # This parameter is required.
        self.epninstance_type = epninstance_type
        # The billing method for network usage. Valid values:
        # 
        # *   **BandwidthByDay**: Pay by daily peak bandwidth.
        # *   **95BandwidthByMonth**: Pay by monthly 95th percentile bandwidth.
        # *   **PayByBandwidth4thMonth**: Pay by monthly fourth peak bandwidth.
        # *   **PayByBandwidth**: Pay by fixed bandwidth.
        # 
        # You can specify only one metering method for network usage and cannot overwrite the existing metering method.
        # 
        # This parameter is required.
        self.internet_charge_type = internet_charge_type
        # The maximum outbound public bandwidth. Unit: Mbit/s. Valid values: 1 to 100.
        # 
        # This parameter is required.
        self.internet_max_bandwidth_out = internet_max_bandwidth_out
        # The networking mode. Valid values:
        # 
        # *   **SpeedUp**: intelligent acceleration network (Internet)
        # *   **Connection**: internal network
        # *   **SpeedUpAndConnection**: intelligent acceleration network and internal network
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

