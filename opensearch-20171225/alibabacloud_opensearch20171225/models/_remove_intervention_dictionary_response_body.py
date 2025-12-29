# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_opensearch20171225 import models as main_models
from darabonba.model import DaraModel

class RemoveInterventionDictionaryResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: main_models.RemoveInterventionDictionaryResponseBodyResult = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The information about the intervention dictionary.
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.result is not None:
            result['result'] = self.result.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('result') is not None:
            temp_model = main_models.RemoveInterventionDictionaryResponseBodyResult()
            self.result = temp_model.from_map(m.get('result'))

        return self

class RemoveInterventionDictionaryResponseBodyResult(DaraModel):
    def __init__(
        self,
        analyzer: str = None,
        created: str = None,
        name: str = None,
        type: str = None,
        updated: str = None,
    ):
        # The custom analyzer.
        self.analyzer = analyzer
        # The time when the intervention dictionary was created.
        self.created = created
        # Parameter
        self.name = name
        # Type
        # 
        # *   stopword: an intervention dictionary for stop word filtering.
        # *   synonym: an intervention dictionary for synonym configuration.
        # *   correction: an intervention dictionary for spelling correction.
        # *   category_prediction: an intervention dictionary for category prediction.
        # *   ner: an intervention dictionary for named entity recognition.
        # *   term_weighting: an intervention dictionary for term weight analysis.
        self.type = type
        # The time when the the intervention dictionary was modified.
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

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('updated') is not None:
            self.updated = m.get('updated')

        return self

