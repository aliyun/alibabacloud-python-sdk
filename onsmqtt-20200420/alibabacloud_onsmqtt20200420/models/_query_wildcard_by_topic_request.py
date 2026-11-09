# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryWildcardByTopicRequest(DaraModel):
    def __init__(
        self,
        first_topic: str = None,
        instance_id: str = None,
        page_no: int = None,
        page_size: int = None,
    ):
        # The parent topic.
        # 
        # This parameter is required.
        self.first_topic = first_topic
        # The ID of the ApsaraMQ for MQTT instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The page number of the results to return. Pages start from page 1.
        self.page_no = page_no
        # The maximum number of records to display per page.
        # 
        # Valid values: 1 to 100.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.first_topic is not None:
            result['FirstTopic'] = self.first_topic

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FirstTopic') is not None:
            self.first_topic = m.get('FirstTopic')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

