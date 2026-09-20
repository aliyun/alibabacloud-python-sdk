# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeColdStorageResponseBody(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        cold_storage_size: str = None,
        cold_storage_type: str = None,
        cold_storage_use_amount: str = None,
        cold_storage_use_percent: str = None,
        open_status: str = None,
        pay_type: str = None,
        request_id: str = None,
    ):
        # The instance ID.
        self.cluster_id = cluster_id
        # The total storage capacity of cold storage, in GB.
        # 
        # > This parameter is returned only when **OpenStatus** is **open**.
        self.cold_storage_size = cold_storage_size
        # The cold storage type. For newly created BDS instances, the cold storage type is **BdsColdStorage**. This parameter is not returned for other instances by default.
        self.cold_storage_type = cold_storage_type
        # The amount of cold storage space used, in GB.
        # 
        # > This parameter is returned only when **OpenStatus** is **open**.
        self.cold_storage_use_amount = cold_storage_use_amount
        # The usage of the cold storage space, in percentage (%).
        # 
        # > This parameter is returned only when **OpenStatus** is **open**.
        self.cold_storage_use_percent = cold_storage_use_percent
        # The enabling status of cold storage. Valid values:
        # - **open**: Cold storage is enabled.
        # - **close**: Cold storage is not enabled.
        self.open_status = open_status
        # The billing method of the instance. Valid values:
        # - **PREPAY**: subscription.
        # - **POSTPAY**: pay-as-you-go.
        self.pay_type = pay_type
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.cold_storage_size is not None:
            result['ColdStorageSize'] = self.cold_storage_size

        if self.cold_storage_type is not None:
            result['ColdStorageType'] = self.cold_storage_type

        if self.cold_storage_use_amount is not None:
            result['ColdStorageUseAmount'] = self.cold_storage_use_amount

        if self.cold_storage_use_percent is not None:
            result['ColdStorageUsePercent'] = self.cold_storage_use_percent

        if self.open_status is not None:
            result['OpenStatus'] = self.open_status

        if self.pay_type is not None:
            result['PayType'] = self.pay_type

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('ColdStorageSize') is not None:
            self.cold_storage_size = m.get('ColdStorageSize')

        if m.get('ColdStorageType') is not None:
            self.cold_storage_type = m.get('ColdStorageType')

        if m.get('ColdStorageUseAmount') is not None:
            self.cold_storage_use_amount = m.get('ColdStorageUseAmount')

        if m.get('ColdStorageUsePercent') is not None:
            self.cold_storage_use_percent = m.get('ColdStorageUsePercent')

        if m.get('OpenStatus') is not None:
            self.open_status = m.get('OpenStatus')

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

