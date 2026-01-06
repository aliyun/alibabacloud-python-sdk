# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ChatBIPredictSseShrinkRequest(DaraModel):
    def __init__(
        self,
        auth_message: str = None,
        auth_type: str = None,
        db_name: str = None,
        generate_chart: bool = None,
        generate_summary: bool = None,
        instance_name: str = None,
        parameters_shrink: str = None,
        pattern_index_table_name: str = None,
        question: str = None,
        schema_index_table_name: str = None,
        select_data: bool = None,
        thinking_mode: bool = None,
    ):
        self.auth_message = auth_message
        self.auth_type = auth_type
        # This parameter is required.
        self.db_name = db_name
        self.generate_chart = generate_chart
        self.generate_summary = generate_summary
        # This parameter is required.
        self.instance_name = instance_name
        self.parameters_shrink = parameters_shrink
        self.pattern_index_table_name = pattern_index_table_name
        # This parameter is required.
        self.question = question
        self.schema_index_table_name = schema_index_table_name
        self.select_data = select_data
        self.thinking_mode = thinking_mode

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

        if self.generate_chart is not None:
            result['GenerateChart'] = self.generate_chart

        if self.generate_summary is not None:
            result['GenerateSummary'] = self.generate_summary

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.parameters_shrink is not None:
            result['Parameters'] = self.parameters_shrink

        if self.pattern_index_table_name is not None:
            result['PatternIndexTableName'] = self.pattern_index_table_name

        if self.question is not None:
            result['Question'] = self.question

        if self.schema_index_table_name is not None:
            result['SchemaIndexTableName'] = self.schema_index_table_name

        if self.select_data is not None:
            result['SelectData'] = self.select_data

        if self.thinking_mode is not None:
            result['ThinkingMode'] = self.thinking_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthMessage') is not None:
            self.auth_message = m.get('AuthMessage')

        if m.get('AuthType') is not None:
            self.auth_type = m.get('AuthType')

        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')

        if m.get('GenerateChart') is not None:
            self.generate_chart = m.get('GenerateChart')

        if m.get('GenerateSummary') is not None:
            self.generate_summary = m.get('GenerateSummary')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('Parameters') is not None:
            self.parameters_shrink = m.get('Parameters')

        if m.get('PatternIndexTableName') is not None:
            self.pattern_index_table_name = m.get('PatternIndexTableName')

        if m.get('Question') is not None:
            self.question = m.get('Question')

        if m.get('SchemaIndexTableName') is not None:
            self.schema_index_table_name = m.get('SchemaIndexTableName')

        if m.get('SelectData') is not None:
            self.select_data = m.get('SelectData')

        if m.get('ThinkingMode') is not None:
            self.thinking_mode = m.get('ThinkingMode')

        return self

