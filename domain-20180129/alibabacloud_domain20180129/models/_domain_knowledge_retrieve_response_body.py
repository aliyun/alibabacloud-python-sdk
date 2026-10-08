# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_domain20180129 import models as main_models
from darabonba.model import DaraModel

class DomainKnowledgeRetrieveResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.DomainKnowledgeRetrieveResponseBodyData] = None,
        request_id: str = None,
    ):
        # La liste des résultats récupérés.
        self.data = data
        # L\\"identifiant de la requête.
        self.request_id = request_id

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.DomainKnowledgeRetrieveResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DomainKnowledgeRetrieveResponseBodyData(DaraModel):
    def __init__(
        self,
        score: float = None,
        source: str = None,
        text: str = None,
    ):
        # Le score du texte récupéré ; plus le score est élevé, plus le résultat est pertinent.
        self.score = score
        # La source des résultats récupérés.
        self.source = source
        # Le texte récupéré.
        self.text = text

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.score is not None:
            result['Score'] = self.score

        if self.source is not None:
            result['Source'] = self.source

        if self.text is not None:
            result['Text'] = self.text

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Score') is not None:
            self.score = m.get('Score')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('Text') is not None:
            self.text = m.get('Text')

        return self

