# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ResizeColdStorageSizeRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        cold_storage_size: int = None,
    ):
        # The ID of the HBase instance. You can call the [DescribeInstances](https://help.aliyun.com/document_detail/144595.html) operation to obtain the instance ID.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The cold storage capacity after the change. Unit: GB. Valid values: **800** to **1000000**.
        # 
        # This parameter is required.
        self.cold_storage_size = cold_storage_size

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('ColdStorageSize') is not None:
            self.cold_storage_size = m.get('ColdStorageSize')

        return self

