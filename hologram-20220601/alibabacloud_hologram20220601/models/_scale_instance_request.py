# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ScaleInstanceRequest(DaraModel):
    def __init__(
        self,
        cold_storage_size: int = None,
        cpu: int = None,
        enable_serverless_computing: bool = None,
        gateway_count: int = None,
        scale_type: str = None,
        storage_size: int = None,
    ):
        # The infrequent access (IA) storage space of the instance. Unit: GB.
        # 
        # > Ignore this parameter for pay-as-you-go instances.
        self.cold_storage_size = cold_storage_size
        # The specifications of the instance. Valid values:
        # 
        # *   8-core 32GB (number of compute nodes: 1)
        # *   16-core 64GB (number of compute nodes: 1)
        # *   32-core 128GB (number of compute nodes: 2)
        # *   64-core 256GB (number of compute nodes: 4)
        # *   96-core 384GB (number of compute nodes: 6)
        # *   128-core 512GB (number of compute nodes: 8)
        # *   Others
        # 
        # > 
        # 
        # *   Set this parameter to the number of cores.
        # 
        # *   If you want to set this parameter to specifications with more than 1,024 compute units (CUs), you must submit a ticket.
        # 
        # *   This parameter is invalid for Hologres Shared Cluster instances.
        # 
        # *   The specifications of 8-core 32GB (number of compute nodes: 1) are for trial use only and cannot be used for production.
        self.cpu = cpu
        # 是否开启ServerlessComputing
        self.enable_serverless_computing = enable_serverless_computing
        # The number of gateways. Valid values: 2 to 50.
        # 
        # > This parameter is required only for virtual warehouse instances.
        self.gateway_count = gateway_count
        # The specification change type. Valid values:
        # 
        # *   UPGRADE
        # *   DOWNGRADE
        # 
        # > 
        # 
        # *   If you set this parameter to UPGRADE, the new specifications must be higher than the original specifications. You must configure at least one of the cpu, storageSize, and coldStorageSize parameters. If you leave a parameter empty, the related configuration remains unchanged.
        # 
        # *   If you set this parameter to DOWNGRADE, the new specifications must be lower than the original specifications. You must configure at least one of the cpu, storageSize, and coldStorageSize parameters. If you leave a parameter empty, the related configuration remains unchanged.
        # 
        # This parameter is required.
        self.scale_type = scale_type
        # The standard storage space of the instance. Unit: GB.
        # 
        # > Ignore this parameter for pay-as-you-go instances.
        self.storage_size = storage_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cold_storage_size is not None:
            result['coldStorageSize'] = self.cold_storage_size

        if self.cpu is not None:
            result['cpu'] = self.cpu

        if self.enable_serverless_computing is not None:
            result['enableServerlessComputing'] = self.enable_serverless_computing

        if self.gateway_count is not None:
            result['gatewayCount'] = self.gateway_count

        if self.scale_type is not None:
            result['scaleType'] = self.scale_type

        if self.storage_size is not None:
            result['storageSize'] = self.storage_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('coldStorageSize') is not None:
            self.cold_storage_size = m.get('coldStorageSize')

        if m.get('cpu') is not None:
            self.cpu = m.get('cpu')

        if m.get('enableServerlessComputing') is not None:
            self.enable_serverless_computing = m.get('enableServerlessComputing')

        if m.get('gatewayCount') is not None:
            self.gateway_count = m.get('gatewayCount')

        if m.get('scaleType') is not None:
            self.scale_type = m.get('scaleType')

        if m.get('storageSize') is not None:
            self.storage_size = m.get('storageSize')

        return self

