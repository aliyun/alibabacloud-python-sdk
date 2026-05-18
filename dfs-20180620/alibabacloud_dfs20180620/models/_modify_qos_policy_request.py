# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyQosPolicyRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        federation_id: str = None,
        file_system_id: str = None,
        input_region_id: str = None,
        max_ioband_width: int = None,
        max_iops: int = None,
        max_meta_qps: int = None,
        qos_policy_id: str = None,
    ):
        self.description = description
        self.federation_id = federation_id
        self.file_system_id = file_system_id
        # This parameter is required.
        self.input_region_id = input_region_id
        self.max_ioband_width = max_ioband_width
        self.max_iops = max_iops
        self.max_meta_qps = max_meta_qps
        # This parameter is required.
        self.qos_policy_id = qos_policy_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.federation_id is not None:
            result['FederationId'] = self.federation_id

        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id

        if self.input_region_id is not None:
            result['InputRegionId'] = self.input_region_id

        if self.max_ioband_width is not None:
            result['MaxIOBandWidth'] = self.max_ioband_width

        if self.max_iops is not None:
            result['MaxIOps'] = self.max_iops

        if self.max_meta_qps is not None:
            result['MaxMetaQps'] = self.max_meta_qps

        if self.qos_policy_id is not None:
            result['QosPolicyId'] = self.qos_policy_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('FederationId') is not None:
            self.federation_id = m.get('FederationId')

        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')

        if m.get('InputRegionId') is not None:
            self.input_region_id = m.get('InputRegionId')

        if m.get('MaxIOBandWidth') is not None:
            self.max_ioband_width = m.get('MaxIOBandWidth')

        if m.get('MaxIOps') is not None:
            self.max_iops = m.get('MaxIOps')

        if m.get('MaxMetaQps') is not None:
            self.max_meta_qps = m.get('MaxMetaQps')

        if m.get('QosPolicyId') is not None:
            self.qos_policy_id = m.get('QosPolicyId')

        return self

