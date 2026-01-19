# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateExpressionVariableRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        description: str = None,
        event_code: str = None,
        expression: str = None,
        expression_title: str = None,
        expression_variable: str = None,
        outlier: str = None,
        outputs: str = None,
        reg_id: str = None,
        title: str = None,
    ):
        # Sets the language type for requests and received messages, with a default value of **zh**. Values:
        # - **zh**: Chinese
        # - **en**: English
        self.lang = lang
        # Description.
        self.description = description
        # Event code
        # 
        # This parameter is required.
        self.event_code = event_code
        # Calculation expression
        # 
        # This parameter is required.
        self.expression = expression
        # Display value of calculation expression
        # 
        # This parameter is required.
        self.expression_title = expression_title
        # Calculation expression variable
        self.expression_variable = expression_variable
        # Outlier
        # 
        # This parameter is required.
        self.outlier = outlier
        # Variable return type
        # 
        # This parameter is required.
        self.outputs = outputs
        # Region code
        # 
        # This parameter is required.
        self.reg_id = reg_id
        # Title.
        # 
        # This parameter is required.
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lang is not None:
            result['Lang'] = self.lang

        if self.description is not None:
            result['description'] = self.description

        if self.event_code is not None:
            result['eventCode'] = self.event_code

        if self.expression is not None:
            result['expression'] = self.expression

        if self.expression_title is not None:
            result['expressionTitle'] = self.expression_title

        if self.expression_variable is not None:
            result['expressionVariable'] = self.expression_variable

        if self.outlier is not None:
            result['outlier'] = self.outlier

        if self.outputs is not None:
            result['outputs'] = self.outputs

        if self.reg_id is not None:
            result['regId'] = self.reg_id

        if self.title is not None:
            result['title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('eventCode') is not None:
            self.event_code = m.get('eventCode')

        if m.get('expression') is not None:
            self.expression = m.get('expression')

        if m.get('expressionTitle') is not None:
            self.expression_title = m.get('expressionTitle')

        if m.get('expressionVariable') is not None:
            self.expression_variable = m.get('expressionVariable')

        if m.get('outlier') is not None:
            self.outlier = m.get('outlier')

        if m.get('outputs') is not None:
            self.outputs = m.get('outputs')

        if m.get('regId') is not None:
            self.reg_id = m.get('regId')

        if m.get('title') is not None:
            self.title = m.get('title')

        return self

