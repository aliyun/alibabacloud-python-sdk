# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ChatBIConfigUpdateEntryRequest(DaraModel):
    def __init__(
        self,
        auth_message: str = None,
        auth_type: str = None,
        db_name: str = None,
        formula_function: str = None,
        id: int = None,
        instance_name: str = None,
        is_functional: int = None,
        query_function: str = None,
        sql_condition: str = None,
        sql_function: str = None,
        text_condition: str = None,
    ):
        self.auth_message = auth_message
        self.auth_type = auth_type
        # This parameter is required.
        self.db_name = db_name
        # This parameter is required.
        self.formula_function = formula_function
        self.id = id
        # This parameter is required.
        self.instance_name = instance_name
        self.is_functional = is_functional
        # This parameter is required.
        self.query_function = query_function
        # This parameter is required.
        self.sql_condition = sql_condition
        # This parameter is required.
        self.sql_function = sql_function
        # This parameter is required.
        self.text_condition = text_condition

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_message is not None:
            result['AuthMessage'] = self.auth_message

        if self.auth_type is not None:
            result['AuthType'] = self.auth_type

        if self.db_name is not None:
            result['DbName'] = self.db_name

        if self.formula_function is not None:
            result['FormulaFunction'] = self.formula_function

        if self.id is not None:
            result['Id'] = self.id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.is_functional is not None:
            result['IsFunctional'] = self.is_functional

        if self.query_function is not None:
            result['QueryFunction'] = self.query_function

        if self.sql_condition is not None:
            result['SqlCondition'] = self.sql_condition

        if self.sql_function is not None:
            result['SqlFunction'] = self.sql_function

        if self.text_condition is not None:
            result['TextCondition'] = self.text_condition

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthMessage') is not None:
            self.auth_message = m.get('AuthMessage')

        if m.get('AuthType') is not None:
            self.auth_type = m.get('AuthType')

        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')

        if m.get('FormulaFunction') is not None:
            self.formula_function = m.get('FormulaFunction')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('IsFunctional') is not None:
            self.is_functional = m.get('IsFunctional')

        if m.get('QueryFunction') is not None:
            self.query_function = m.get('QueryFunction')

        if m.get('SqlCondition') is not None:
            self.sql_condition = m.get('SqlCondition')

        if m.get('SqlFunction') is not None:
            self.sql_function = m.get('SqlFunction')

        if m.get('TextCondition') is not None:
            self.text_condition = m.get('TextCondition')

        return self

