# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyElasticBandWidthRequest(DaraModel):
    def __init__(
        self,
        elastic_bandwidth: int = None,
        instance_id: str = None,
        source_ip: str = None,
    ):
        # This parameter is required.
        self.elastic_bandwidth = elastic_bandwidth
        # This parameter is required.
        self.instance_id = instance_id
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.elastic_bandwidth is not None:
            result['ElasticBandwidth'] = self.elastic_bandwidth

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ElasticBandwidth') is not None:
            self.elastic_bandwidth = m.get('ElasticBandwidth')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        return self

