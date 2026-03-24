# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteCdnDeliverTaskRequest(DaraModel):
    def __init__(
        self,
        deliver_id: int = None,
    ):
        # The ID of the tracking task that you want to delete. You can call the [DescribeCdnDeliverList](https://help.aliyun.com/document_detail/270877.html) operation to query task IDs.
        # 
        # This parameter is required.
        self.deliver_id = deliver_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.deliver_id is not None:
            result['DeliverId'] = self.deliver_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeliverId') is not None:
            self.deliver_id = m.get('DeliverId')

        return self

