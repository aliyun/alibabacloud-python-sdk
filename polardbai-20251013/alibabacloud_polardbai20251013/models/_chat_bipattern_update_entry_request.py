# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ChatBIPatternUpdateEntryRequest(DaraModel):
    def __init__(
        self,
        auth_message: str = None,
        auth_type: str = None,
        db_name: str = None,
        id: int = None,
        instance_name: str = None,
        pattern_description: str = None,
        pattern_params: str = None,
        pattern_question: str = None,
        pattern_sql: str = None,
        table_name: str = None,
    ):
        self.auth_message = auth_message
        self.auth_type = auth_type
        # This parameter is required.
        self.db_name = db_name
        self.id = id
        # This parameter is required.
        self.instance_name = instance_name
        # This parameter is required.
        self.pattern_description = pattern_description
        # This parameter is required.
        self.pattern_params = pattern_params
        # This parameter is required.
        self.pattern_question = pattern_question
        # This parameter is required.
        self.pattern_sql = pattern_sql
        # This parameter is required.
        self.table_name = table_name

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

        if self.id is not None:
            result['Id'] = self.id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.pattern_description is not None:
            result['PatternDescription'] = self.pattern_description

        if self.pattern_params is not None:
            result['PatternParams'] = self.pattern_params

        if self.pattern_question is not None:
            result['PatternQuestion'] = self.pattern_question

        if self.pattern_sql is not None:
            result['PatternSql'] = self.pattern_sql

        if self.table_name is not None:
            result['TableName'] = self.table_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthMessage') is not None:
            self.auth_message = m.get('AuthMessage')

        if m.get('AuthType') is not None:
            self.auth_type = m.get('AuthType')

        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('PatternDescription') is not None:
            self.pattern_description = m.get('PatternDescription')

        if m.get('PatternParams') is not None:
            self.pattern_params = m.get('PatternParams')

        if m.get('PatternQuestion') is not None:
            self.pattern_question = m.get('PatternQuestion')

        if m.get('PatternSql') is not None:
            self.pattern_sql = m.get('PatternSql')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        return self

