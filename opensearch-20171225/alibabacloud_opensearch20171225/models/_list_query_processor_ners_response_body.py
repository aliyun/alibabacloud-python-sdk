# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_opensearch20171225 import models as main_models
from darabonba.model import DaraModel

class ListQueryProcessorNersResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[main_models.ListQueryProcessorNersResponseBodyResult] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The priority settings of entity types.
        # 
        # For more information, see [Priority settings of entity types](https://help.aliyun.com/document_detail/173616.html).
        self.result = result

    def validate(self):
        if self.result:
            for v1 in self.result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['requestId'] = self.request_id

        result['result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['result'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        self.result = []
        if m.get('result') is not None:
            for k1 in m.get('result'):
                temp_model = main_models.ListQueryProcessorNersResponseBodyResult()
                self.result.append(temp_model.from_map(k1))

        return self

class ListQueryProcessorNersResponseBodyResult(DaraModel):
    def __init__(
        self,
        label: str = None,
        order: int = None,
        priority: str = None,
        tag: str = None,
    ):
        # The name of the entity type.
        self.label = label
        # The priority of an entity type among entity types that have the same priority level. A smaller value indicates a higher priority. Default value: 0.
        self.order = order
        # The priority level of the entity type. Valid values:
        # 
        # *   HIGH
        # *   MIDDLE
        # *   LOW
        self.priority = priority
        # The internal name of the entity type.
        self.tag = tag

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.label is not None:
            result['label'] = self.label

        if self.order is not None:
            result['order'] = self.order

        if self.priority is not None:
            result['priority'] = self.priority

        if self.tag is not None:
            result['tag'] = self.tag

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('label') is not None:
            self.label = m.get('label')

        if m.get('order') is not None:
            self.order = m.get('order')

        if m.get('priority') is not None:
            self.priority = m.get('priority')

        if m.get('tag') is not None:
            self.tag = m.get('tag')

        return self

