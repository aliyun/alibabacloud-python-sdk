# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_opensearch20171225 import models as main_models
from darabonba.model import DaraModel

class ListInterventionDictionaryEntriesResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[main_models.ListInterventionDictionaryEntriesResponseBodyResult] = None,
        total_count: int = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The information about intervention entries.
        # 
        # For more information, see [InterventionDictionaryEntry](https://help.aliyun.com/document_detail/173606.html).
        self.result = result
        # The total number of entries returned.
        self.total_count = total_count

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

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        self.result = []
        if m.get('result') is not None:
            for k1 in m.get('result'):
                temp_model = main_models.ListInterventionDictionaryEntriesResponseBodyResult()
                self.result.append(temp_model.from_map(k1))

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

class ListInterventionDictionaryEntriesResponseBodyResult(DaraModel):
    def __init__(
        self,
        cmd: str = None,
        created: int = None,
        relevance: Dict[str, Any] = None,
        status: str = None,
        tokens: List[main_models.ListInterventionDictionaryEntriesResponseBodyResultTokens] = None,
        updated: int = None,
        word: str = None,
    ):
        # The command. Valid values:
        # 
        # *   add
        # *   delete
        self.cmd = cmd
        # The timestamp when the intervention entry was created.
        self.created = created
        # The content of an intervention entry for category prediction. The field value consists of key-value pairs. The key in a key-value pair indicates the ID of the category. The value in a key-value pair indicates the relevance to the category. A value of 0 indicates irrelevant. A value of 1 indicates slightly relevant. A value of 2 indicates relevant. Example: {"2":1, "100":0}
        self.relevance = relevance
        # The status of the intervention entry. Valid value:
        # 
        # *   ACTIVE: The intervention entry takes effect.
        self.status = status
        # The content of the intervention entry for term weight analysis.
        self.tokens = tokens
        # The timestamp when the intervention entry was last updated.
        self.updated = updated
        # The intervention entry.
        self.word = word

    def validate(self):
        if self.tokens:
            for v1 in self.tokens:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cmd is not None:
            result['cmd'] = self.cmd

        if self.created is not None:
            result['created'] = self.created

        if self.relevance is not None:
            result['relevance'] = self.relevance

        if self.status is not None:
            result['status'] = self.status

        result['tokens'] = []
        if self.tokens is not None:
            for k1 in self.tokens:
                result['tokens'].append(k1.to_map() if k1 else None)

        if self.updated is not None:
            result['updated'] = self.updated

        if self.word is not None:
            result['word'] = self.word

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cmd') is not None:
            self.cmd = m.get('cmd')

        if m.get('created') is not None:
            self.created = m.get('created')

        if m.get('relevance') is not None:
            self.relevance = m.get('relevance')

        if m.get('status') is not None:
            self.status = m.get('status')

        self.tokens = []
        if m.get('tokens') is not None:
            for k1 in m.get('tokens'):
                temp_model = main_models.ListInterventionDictionaryEntriesResponseBodyResultTokens()
                self.tokens.append(temp_model.from_map(k1))

        if m.get('updated') is not None:
            self.updated = m.get('updated')

        if m.get('word') is not None:
            self.word = m.get('word')

        return self

class ListInterventionDictionaryEntriesResponseBodyResultTokens(DaraModel):
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

