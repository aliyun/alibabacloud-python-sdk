# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_openapiexplorer20241130 import models as main_models
from darabonba.model import DaraModel

class GetErrorCodeSolutionsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        solutions: List[main_models.GetErrorCodeSolutionsResponseBodySolutions] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The solutions. Not all error codes have corresponding solutions. You can submit a ticket or use OpenAPI Explorer to contact technical support if necessary.
        self.solutions = solutions

    def validate(self):
        if self.solutions:
            for v1 in self.solutions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['requestId'] = self.request_id

        result['solutions'] = []
        if self.solutions is not None:
            for k1 in self.solutions:
                result['solutions'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        self.solutions = []
        if m.get('solutions') is not None:
            for k1 in m.get('solutions'):
                temp_model = main_models.GetErrorCodeSolutionsResponseBodySolutions()
                self.solutions.append(temp_model.from_map(k1))

        return self

class GetErrorCodeSolutionsResponseBodySolutions(DaraModel):
    def __init__(
        self,
        content: str = None,
        error_code: str = None,
        error_message: str = None,
        product: str = None,
        product_name: str = None,
        solution_id: str = None,
    ):
        # The content of the solution, which is in the markdown format.
        self.content = content
        # The error code.
        self.error_code = error_code
        # The error message.
        self.error_message = error_message
        # The code of the product to which the solution belongs.
        self.product = product
        # The name of the product to which the solution belongs.
        self.product_name = product_name
        # The solution ID.
        self.solution_id = solution_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['content'] = self.content

        if self.error_code is not None:
            result['errorCode'] = self.error_code

        if self.error_message is not None:
            result['errorMessage'] = self.error_message

        if self.product is not None:
            result['product'] = self.product

        if self.product_name is not None:
            result['productName'] = self.product_name

        if self.solution_id is not None:
            result['solutionId'] = self.solution_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')

        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')

        if m.get('product') is not None:
            self.product = m.get('product')

        if m.get('productName') is not None:
            self.product_name = m.get('productName')

        if m.get('solutionId') is not None:
            self.solution_id = m.get('solutionId')

        return self

