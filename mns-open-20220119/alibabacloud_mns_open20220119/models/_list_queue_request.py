# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_mns_open20220119 import models as main_models
from darabonba.model import DaraModel

class ListQueueRequest(DaraModel):
    def __init__(
        self,
        page_num: int = None,
        page_size: int = None,
        queue_name: str = None,
        queue_type: str = None,
        tag: List[main_models.ListQueueRequestTag] = None,
    ):
        # The page number of the results to return.
        # 
        # Valid values: 1 to 100000000.
        # 
        # If you set this parameter to a value less than 1, the system uses 1 by default. If you set this parameter to a value greater than 100000000, the system uses 100000000 by default.
        self.page_num = page_num
        # The number of entries to return on each page.
        # 
        # Valid values: 10 to 50.
        # 
        # If you set this parameter to a value less than 10, the system uses 10 by default. If you set this parameter to a value greater than 50, the system uses 50 by default.
        self.page_size = page_size
        # The name of the queue.
        self.queue_name = queue_name
        # The type of the queue. Valid values:
        #    * normal: standard queue
        #    * fifo: FIFO queue
        self.queue_type = queue_type
        # The list of resource tags.
        self.tag = tag

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.queue_name is not None:
            result['QueueName'] = self.queue_name

        if self.queue_type is not None:
            result['QueueType'] = self.queue_type

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')

        if m.get('QueueType') is not None:
            self.queue_type = m.get('QueueType')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.ListQueueRequestTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class ListQueueRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the tag.
        self.key = key
        # The value of the tag.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

