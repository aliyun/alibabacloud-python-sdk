# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyElasticBizBandWidthRequest(DaraModel):
    def __init__(
        self,
        elastic_biz_bandwidth: int = None,
        instance_id: str = None,
        mode: str = None,
    ):
        # This parameter is required.
        self.elastic_biz_bandwidth = elastic_biz_bandwidth
        # This parameter is required.
        self.instance_id = instance_id
        self.mode = mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.elastic_biz_bandwidth is not None:
            result['ElasticBizBandwidth'] = self.elastic_biz_bandwidth

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.mode is not None:
            result['Mode'] = self.mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ElasticBizBandwidth') is not None:
            self.elastic_biz_bandwidth = m.get('ElasticBizBandwidth')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        return self

