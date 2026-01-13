# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateCustomerModuleOutputInfoRequest(DaraModel):
    def __init__(
        self,
        customer_module_id: int = None,
        final_score_format: str = None,
        process_expression: str = None,
        test_file_url: str = None,
    ):
        # Customer model ID
        self.customer_module_id = customer_module_id
        # Number of decimal places to retain.
        self.final_score_format = final_score_format
        # Score processing logic.
        self.process_expression = process_expression
        # Test file URL.
        self.test_file_url = test_file_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.customer_module_id is not None:
            result['CustomerModuleId'] = self.customer_module_id

        if self.final_score_format is not None:
            result['FinalScoreFormat'] = self.final_score_format

        if self.process_expression is not None:
            result['ProcessExpression'] = self.process_expression

        if self.test_file_url is not None:
            result['TestFileUrl'] = self.test_file_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomerModuleId') is not None:
            self.customer_module_id = m.get('CustomerModuleId')

        if m.get('FinalScoreFormat') is not None:
            self.final_score_format = m.get('FinalScoreFormat')

        if m.get('ProcessExpression') is not None:
            self.process_expression = m.get('ProcessExpression')

        if m.get('TestFileUrl') is not None:
            self.test_file_url = m.get('TestFileUrl')

        return self

