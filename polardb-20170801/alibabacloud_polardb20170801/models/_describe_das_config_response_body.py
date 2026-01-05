# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDasConfigResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        storage_auto_scale: str = None,
        storage_upper_bound: int = None,
    ):
        # The request ID.
        self.request_id = request_id
        # Specifies whether to enable automatic storage scaling for the Standard Edition cluster. Valid values:
        # 
        # *   Enable
        # *   Disable
        self.storage_auto_scale = storage_auto_scale
        # The maximum storage capacity that is allowed for storage automatic scaling of the Standard Edition cluster. Unit: GB.
        # 
        # >  This parameter is valid only when the StorageAutoScale parameter is set to Enable.
        self.storage_upper_bound = storage_upper_bound

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.storage_auto_scale is not None:
            result['StorageAutoScale'] = self.storage_auto_scale

        if self.storage_upper_bound is not None:
            result['StorageUpperBound'] = self.storage_upper_bound

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StorageAutoScale') is not None:
            self.storage_auto_scale = m.get('StorageAutoScale')

        if m.get('StorageUpperBound') is not None:
            self.storage_upper_bound = m.get('StorageUpperBound')

        return self

