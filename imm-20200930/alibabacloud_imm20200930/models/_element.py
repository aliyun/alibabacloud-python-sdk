# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_imm20200930 import models as main_models
from darabonba.model import DaraModel

class Element(DaraModel):
    def __init__(
        self,
        element_contents: List[main_models.ElementContent] = None,
        element_relations: List[main_models.ElementRelation] = None,
        element_type: str = None,
        object_id: str = None,
        semantic_similarity: float = None,
    ):
        # The element contents.
        self.element_contents = element_contents
        # The relationships between the current element and other elements.
        self.element_relations = element_relations
        # The element type.
        self.element_type = element_type
        # The unique ID of the element.
        self.object_id = object_id
        # The similarity between the current file and its extracted semantics.
        self.semantic_similarity = semantic_similarity

    def validate(self):
        if self.element_contents:
            for v1 in self.element_contents:
                 if v1:
                    v1.validate()
        if self.element_relations:
            for v1 in self.element_relations:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ElementContents'] = []
        if self.element_contents is not None:
            for k1 in self.element_contents:
                result['ElementContents'].append(k1.to_map() if k1 else None)

        result['ElementRelations'] = []
        if self.element_relations is not None:
            for k1 in self.element_relations:
                result['ElementRelations'].append(k1.to_map() if k1 else None)

        if self.element_type is not None:
            result['ElementType'] = self.element_type

        if self.object_id is not None:
            result['ObjectId'] = self.object_id

        if self.semantic_similarity is not None:
            result['SemanticSimilarity'] = self.semantic_similarity

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.element_contents = []
        if m.get('ElementContents') is not None:
            for k1 in m.get('ElementContents'):
                temp_model = main_models.ElementContent()
                self.element_contents.append(temp_model.from_map(k1))

        self.element_relations = []
        if m.get('ElementRelations') is not None:
            for k1 in m.get('ElementRelations'):
                temp_model = main_models.ElementRelation()
                self.element_relations.append(temp_model.from_map(k1))

        if m.get('ElementType') is not None:
            self.element_type = m.get('ElementType')

        if m.get('ObjectId') is not None:
            self.object_id = m.get('ObjectId')

        if m.get('SemanticSimilarity') is not None:
            self.semantic_similarity = m.get('SemanticSimilarity')

        return self

