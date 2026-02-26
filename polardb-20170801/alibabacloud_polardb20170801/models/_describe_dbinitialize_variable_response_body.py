# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribeDBInitializeVariableResponseBody(DaraModel):
    def __init__(
        self,
        dbtype: str = None,
        dbversion: str = None,
        request_id: str = None,
        variables: main_models.DescribeDBInitializeVariableResponseBodyVariables = None,
    ):
        # The database type. Valid values:
        # 
        # *   Oracle
        # *   PostgreSQL
        # *   MySQL
        self.dbtype = dbtype
        # The version of the database engine.
        self.dbversion = dbversion
        # The ID of the request.
        self.request_id = request_id
        self.variables = variables

    def validate(self):
        if self.variables:
            self.variables.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbtype is not None:
            result['DBType'] = self.dbtype

        if self.dbversion is not None:
            result['DBVersion'] = self.dbversion

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.variables is not None:
            result['Variables'] = self.variables.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBType') is not None:
            self.dbtype = m.get('DBType')

        if m.get('DBVersion') is not None:
            self.dbversion = m.get('DBVersion')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Variables') is not None:
            temp_model = main_models.DescribeDBInitializeVariableResponseBodyVariables()
            self.variables = temp_model.from_map(m.get('Variables'))

        return self

class DescribeDBInitializeVariableResponseBodyVariables(DaraModel):
    def __init__(
        self,
        variable: List[main_models.DescribeDBInitializeVariableResponseBodyVariablesVariable] = None,
    ):
        self.variable = variable

    def validate(self):
        if self.variable:
            for v1 in self.variable:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Variable'] = []
        if self.variable is not None:
            for k1 in self.variable:
                result['Variable'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.variable = []
        if m.get('Variable') is not None:
            for k1 in m.get('Variable'):
                temp_model = main_models.DescribeDBInitializeVariableResponseBodyVariablesVariable()
                self.variable.append(temp_model.from_map(k1))

        return self

class DescribeDBInitializeVariableResponseBodyVariablesVariable(DaraModel):
    def __init__(
        self,
        charset: str = None,
        collate: str = None,
        ctype: str = None,
    ):
        self.charset = charset
        self.collate = collate
        self.ctype = ctype

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.charset is not None:
            result['Charset'] = self.charset

        if self.collate is not None:
            result['Collate'] = self.collate

        if self.ctype is not None:
            result['Ctype'] = self.ctype

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Charset') is not None:
            self.charset = m.get('Charset')

        if m.get('Collate') is not None:
            self.collate = m.get('Collate')

        if m.get('Ctype') is not None:
            self.ctype = m.get('Ctype')

        return self

