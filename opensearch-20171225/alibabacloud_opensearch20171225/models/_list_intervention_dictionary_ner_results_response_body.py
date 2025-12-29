# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_opensearch20171225 import models as main_models
from darabonba.model import DaraModel

class ListInterventionDictionaryNerResultsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[main_models.ListInterventionDictionaryNerResultsResponseBodyResult] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The NER result.
        # 
        # For more information, see [InterventionDictionaryEntry](https://help.aliyun.com/document_detail/173606.html).
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
                temp_model = main_models.ListInterventionDictionaryNerResultsResponseBodyResult()
                self.result.append(temp_model.from_map(k1))

        return self

class ListInterventionDictionaryNerResultsResponseBodyResult(DaraModel):
    def __init__(
        self,
        order: int = None,
        tag: str = None,
        tag_label: str = None,
        token: str = None,
    ):
        # The sequence number.
        self.order = order
        # The internal name of the identified entity type. Valid values:
        # 
        # *   brand
        # *   category
        # *   material
        # *   element
        # *   style
        # *   color
        # *   function
        # *   scenario
        # *   people
        # *   season
        # *   model
        # *   region
        # *   name
        # *   adjective
        # *   category-modifier
        # *   size
        # *   quality
        # *   suit
        # *   new-release
        # *   series
        # *   marketing
        # *   entertainment
        # *   organization
        # *   movie
        # *   game
        # *   number
        # *   unit
        # *   common
        # *   new-word
        # *   proper-noun
        # *   symbol
        # *   prefix
        # *   suffix
        # *   gift
        # *   negative
        # *   agent
        self.tag = tag
        # The description of the internal name of the identified entity type.
        self.tag_label = tag_label
        # The entity.
        self.token = token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.order is not None:
            result['order'] = self.order

        if self.tag is not None:
            result['tag'] = self.tag

        if self.tag_label is not None:
            result['tagLabel'] = self.tag_label

        if self.token is not None:
            result['token'] = self.token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('order') is not None:
            self.order = m.get('order')

        if m.get('tag') is not None:
            self.tag = m.get('tag')

        if m.get('tagLabel') is not None:
            self.tag_label = m.get('tagLabel')

        if m.get('token') is not None:
            self.token = m.get('token')

        return self

