# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteResourceInstancesRequest(DaraModel):
    def __init__(
        self,
        all_failed: bool = None,
        instance_list: str = None,
    ):
        # Specifies whether to delete all the instances that fail to be created. Valid values:
        # 
        # *   true
        # *   false
        self.all_failed = all_failed
        # The instances. Separate multiple instances with commas (,), such as `instanceId1,instanceId2`. For more information about how to query the instances, see [ListResourceInstances](https://help.aliyun.com/document_detail/412129.html).
        self.instance_list = instance_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.all_failed is not None:
            result['AllFailed'] = self.all_failed

        if self.instance_list is not None:
            result['InstanceList'] = self.instance_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllFailed') is not None:
            self.all_failed = m.get('AllFailed')

        if m.get('InstanceList') is not None:
            self.instance_list = m.get('InstanceList')

        return self

