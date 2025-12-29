# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_opensearch20171225 import models as main_models
from darabonba.model import DaraModel

class ListInterventionDictionariesResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[main_models.ListInterventionDictionariesResponseBodyResult] = None,
        total_count: int = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The information about each intervention dictionary.
        # 
        # For more information, see [InterventionDictionary](https://help.aliyun.com/document_detail/173608.html).
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
                temp_model = main_models.ListInterventionDictionariesResponseBodyResult()
                self.result.append(temp_model.from_map(k1))

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

class ListInterventionDictionariesResponseBodyResult(DaraModel):
    def __init__(
        self,
        analyzer: str = None,
        created: int = None,
        id: int = None,
        name: str = None,
        type: str = None,
        updated: int = None,
    ):
        # The custom analyzer.
        self.analyzer = analyzer
        # The time when the intervention dictionary was created.
        self.created = created
        # The ID of the intervention dictionary.
        self.id = id
        # The name of the intervention dictionary.
        self.name = name
        # The type of the intervention dictionary. Valid values:
        # 
        # *   stopword: an intervention dictionary for stop word filtering
        # *   synonym: an intervention dictionary for synonym configuration
        # *   correction: an intervention dictionary for spelling correction
        # *   category_prediction: an intervention dictionary for category prediction
        # *   ner: an intervention dictionary for named entity recognition (NER)
        # *   term_weighting: an intervention dictionary for term weight analysis
        self.type = type
        # The time when the intervention dictionary was last updated.
        self.updated = updated

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.analyzer is not None:
            result['analyzer'] = self.analyzer

        if self.created is not None:
            result['created'] = self.created

        if self.id is not None:
            result['id'] = self.id

        if self.name is not None:
            result['name'] = self.name

        if self.type is not None:
            result['type'] = self.type

        if self.updated is not None:
            result['updated'] = self.updated

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('analyzer') is not None:
            self.analyzer = m.get('analyzer')

        if m.get('created') is not None:
            self.created = m.get('created')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('updated') is not None:
            self.updated = m.get('updated')

        return self

