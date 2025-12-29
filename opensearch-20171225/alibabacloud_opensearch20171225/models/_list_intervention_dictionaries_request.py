# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListInterventionDictionariesRequest(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        types: str = None,
    ):
        # The number of the page to return. Default value: 1.
        self.page_number = page_number
        # The number of entries to return on each page. Default value: 10.
        self.page_size = page_size
        # The type of the intervention dictionary. Valid values:
        # 
        # *   stopword: an intervention dictionary for stop word filtering
        # *   synonym: an intervention dictionary for synonym configuration
        # *   correction: an intervention dictionary for spelling correction
        # *   category_prediction: an intervention dictionary for category prediction
        # *   ner: an intervention dictionary for named entity recognition (NER)
        # *   term_weighting: an intervention dictionary for term weight analysis
        self.types = types

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.types is not None:
            result['types'] = self.types

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('types') is not None:
            self.types = m.get('types')

        return self

