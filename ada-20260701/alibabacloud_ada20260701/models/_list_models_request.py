# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListModelsRequest(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        model_type: str = None,
        next_token: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # The maximum number of models to return per page. Valid values: 1 to 100. Explicitly specify this parameter.
        self.max_results = max_results
        # Set this parameter to `text` for text sessions. If you omit this parameter, all visible models are queried.
        self.model_type = model_type
        # The pagination token returned from the previous page. Omit this parameter for the first page.
        self.next_token = next_token
        # The legacy pagination parameter for compatibility. The page number starts from 1. Use MaxResults and NextToken instead. Do not mix the two sets of pagination parameters.
        self.page_number = page_number
        # The legacy pagination parameter for compatibility. The number of entries per page. Valid values: 1 to 100. Use MaxResults and NextToken instead. Do not mix the two sets of pagination parameters.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.model_type is not None:
            result['ModelType'] = self.model_type

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('ModelType') is not None:
            self.model_type = m.get('ModelType')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

