# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SendDryRunSystemEventRequest(DaraModel):
    def __init__(
        self,
        event_content: str = None,
        event_name: str = None,
        group_id: str = None,
        product: str = None,
        region_id: str = None,
    ):
        # The content of the system event.
        # 
        # >  The value of this parameter is a JSON object. We recommend that you include the `product`, `resourceId`, and `regionId` fields in the JSON object.
        self.event_content = event_content
        # The name of the system event.
        # 
        # >  For more information, see [DescribeSystemEventMetaList](https://help.aliyun.com/document_detail/114972.html).
        # 
        # This parameter is required.
        self.event_name = event_name
        # The ID of the application group.
        self.group_id = group_id
        # The name of the cloud service.
        # 
        # >  For information about the Alibaba Cloud services that are supported by CloudMonitor, see [Supported cloud services and their system events](https://help.aliyun.com/document_detail/167388.html).
        # 
        # This parameter is required.
        self.product = product
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.event_content is not None:
            result['EventContent'] = self.event_content

        if self.event_name is not None:
            result['EventName'] = self.event_name

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.product is not None:
            result['Product'] = self.product

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventContent') is not None:
            self.event_content = m.get('EventContent')

        if m.get('EventName') is not None:
            self.event_name = m.get('EventName')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('Product') is not None:
            self.product = m.get('Product')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

