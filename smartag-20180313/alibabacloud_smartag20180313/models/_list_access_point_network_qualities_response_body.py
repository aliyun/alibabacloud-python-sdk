# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_smartag20180313 import models as main_models
from darabonba.model import DaraModel

class ListAccessPointNetworkQualitiesResponseBody(DaraModel):
    def __init__(
        self,
        access_point_network_qualities: List[main_models.ListAccessPointNetworkQualitiesResponseBodyAccessPointNetworkQualities] = None,
        request_id: str = None,
    ):
        # The network quality of the endpoint.
        self.access_point_network_qualities = access_point_network_qualities
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.access_point_network_qualities:
            for v1 in self.access_point_network_qualities:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AccessPointNetworkQualities'] = []
        if self.access_point_network_qualities is not None:
            for k1 in self.access_point_network_qualities:
                result['AccessPointNetworkQualities'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.access_point_network_qualities = []
        if m.get('AccessPointNetworkQualities') is not None:
            for k1 in m.get('AccessPointNetworkQualities'):
                temp_model = main_models.ListAccessPointNetworkQualitiesResponseBodyAccessPointNetworkQualities()
                self.access_point_network_qualities.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListAccessPointNetworkQualitiesResponseBodyAccessPointNetworkQualities(DaraModel):
    def __init__(
        self,
        id: int = None,
        loss: str = None,
        rtt: str = None,
    ):
        # The ID of the endpoint.
        self.id = id
        # The packet loss rate.
        self.loss = loss
        # The network latency. Unit: milliseconds.
        self.rtt = rtt

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.loss is not None:
            result['Loss'] = self.loss

        if self.rtt is not None:
            result['Rtt'] = self.rtt

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Loss') is not None:
            self.loss = m.get('Loss')

        if m.get('Rtt') is not None:
            self.rtt = m.get('Rtt')

        return self

