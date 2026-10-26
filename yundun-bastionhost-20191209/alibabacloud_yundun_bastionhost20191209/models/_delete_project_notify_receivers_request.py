# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteProjectNotifyReceiversRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        receiver_ids: str = None,
        region_id: str = None,
    ):
        # The instance ID of the Bastionhost instance.
        # 
        # > You can call the [DescribeInstances](https://help.aliyun.com/document_detail/153281.html) operation to retrieve this parameter.
        self.instance_id = instance_id
        # The IDs of the notification recipients to delete.
        # > You can call the GetProject operation to retrieve this parameter.
        # 
        # This parameter is required.
        self.receiver_ids = receiver_ids
        # The region ID of the Bastionhost instance.
        # > For the mappings between region IDs and region names, see [Regions and zones](https://help.aliyun.com/document_detail/40654.html).
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.receiver_ids is not None:
            result['ReceiverIds'] = self.receiver_ids

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('ReceiverIds') is not None:
            self.receiver_ids = m.get('ReceiverIds')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

