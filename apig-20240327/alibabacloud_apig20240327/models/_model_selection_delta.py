# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ModelSelectionDelta(DaraModel):
    def __init__(
        self,
        add_model_card_ids: List[str] = None,
        remove_model_card_ids: List[str] = None,
    ):
        # The actual source model IDs to add to the unique ModelAPI. Already selected IDs must not be added again.
        self.add_model_card_ids = add_model_card_ids
        # The actual source model IDs to remove from the unique ModelAPI. This operation does not delete models in the source. You cannot clear the API or remove backup models that are still referenced by other entry points.
        self.remove_model_card_ids = remove_model_card_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.add_model_card_ids is not None:
            result['addModelCardIds'] = self.add_model_card_ids

        if self.remove_model_card_ids is not None:
            result['removeModelCardIds'] = self.remove_model_card_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('addModelCardIds') is not None:
            self.add_model_card_ids = m.get('addModelCardIds')

        if m.get('removeModelCardIds') is not None:
            self.remove_model_card_ids = m.get('removeModelCardIds')

        return self

