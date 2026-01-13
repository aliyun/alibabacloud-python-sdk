# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateInstanceElasticVCUUpperLimitRequest(DaraModel):
    def __init__(
        self,
        elastic_vcuupper_limit: float = None,
        instance_name: str = None,
    ):
        # The upper limit for the VCUs of the instance.
        # 
        # >  Valid values of the upper limit for the VCUs of an instance: **Number of reserved VCUs+0.1 to 2000**. You can upgrade or downgrade configurations to modify the number of reserved VCUs by increments or decrements of 1. You can dynamically modify the upper limit for the VCUs of an instance by increments or decrements of 0.1
        # 
        # This parameter is required.
        self.elastic_vcuupper_limit = elastic_vcuupper_limit
        # The name of the instance.
        # 
        # This parameter is required.
        self.instance_name = instance_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.elastic_vcuupper_limit is not None:
            result['ElasticVCUUpperLimit'] = self.elastic_vcuupper_limit

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ElasticVCUUpperLimit') is not None:
            self.elastic_vcuupper_limit = m.get('ElasticVCUUpperLimit')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        return self

