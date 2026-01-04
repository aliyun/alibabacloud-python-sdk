# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyEpnInstanceRequest(DaraModel):
    def __init__(
        self,
        epninstance_id: str = None,
        epninstance_name: str = None,
        internet_max_bandwidth_out: int = None,
        networking_model: str = None,
    ):
        # The ID of the EPN instance.
        # 
        # This parameter is required.
        self.epninstance_id = epninstance_id
        # The name of the EPN instance.
        self.epninstance_name = epninstance_name
        # The maximum outbound public bandwidth. Unit: Mbit/s. Valid values: 1 Mbit/s to 100 Mbit/s.
        self.internet_max_bandwidth_out = internet_max_bandwidth_out
        # The networking mode. Valid values:
        # 
        # *   **SpeedUp**: Intelligent acceleration network (Internet).
        # *   **Connection**: Internal network.
        # *   **SpeedUpAndConnection**: Intelligent acceleration network and internal network.
        # 
        # >  The internal network supports only **Connection** and **SpeedUpAndConnection**.
        self.networking_model = networking_model

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.epninstance_id is not None:
            result['EPNInstanceId'] = self.epninstance_id

        if self.epninstance_name is not None:
            result['EPNInstanceName'] = self.epninstance_name

        if self.internet_max_bandwidth_out is not None:
            result['InternetMaxBandwidthOut'] = self.internet_max_bandwidth_out

        if self.networking_model is not None:
            result['NetworkingModel'] = self.networking_model

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EPNInstanceId') is not None:
            self.epninstance_id = m.get('EPNInstanceId')

        if m.get('EPNInstanceName') is not None:
            self.epninstance_name = m.get('EPNInstanceName')

        if m.get('InternetMaxBandwidthOut') is not None:
            self.internet_max_bandwidth_out = m.get('InternetMaxBandwidthOut')

        if m.get('NetworkingModel') is not None:
            self.networking_model = m.get('NetworkingModel')

        return self

