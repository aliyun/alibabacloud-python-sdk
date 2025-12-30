# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_polardbai20251013 import models as main_models
from darabonba.model import DaraModel

class ChatBIPredictSseRequest(DaraModel):
    def __init__(
        self,
        db_name: str = None,
        generate_chart: bool = None,
        generate_summary: bool = None,
        instance_name: str = None,
        parameters: main_models.ChatBIPredictSseRequestParameters = None,
        pattern_index_table_name: str = None,
        question: str = None,
        schema_index_table_name: str = None,
        select_data: bool = None,
    ):
        # This parameter is required.
        self.db_name = db_name
        self.generate_chart = generate_chart
        self.generate_summary = generate_summary
        # This parameter is required.
        self.instance_name = instance_name
        self.parameters = parameters
        self.pattern_index_table_name = pattern_index_table_name
        # This parameter is required.
        self.question = question
        self.schema_index_table_name = schema_index_table_name
        self.select_data = select_data

    def validate(self):
        if self.parameters:
            self.parameters.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.db_name is not None:
            result['DbName'] = self.db_name

        if self.generate_chart is not None:
            result['GenerateChart'] = self.generate_chart

        if self.generate_summary is not None:
            result['GenerateSummary'] = self.generate_summary

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.parameters is not None:
            result['Parameters'] = self.parameters.to_map()

        if self.pattern_index_table_name is not None:
            result['PatternIndexTableName'] = self.pattern_index_table_name

        if self.question is not None:
            result['Question'] = self.question

        if self.schema_index_table_name is not None:
            result['SchemaIndexTableName'] = self.schema_index_table_name

        if self.select_data is not None:
            result['SelectData'] = self.select_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')

        if m.get('GenerateChart') is not None:
            self.generate_chart = m.get('GenerateChart')

        if m.get('GenerateSummary') is not None:
            self.generate_summary = m.get('GenerateSummary')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('Parameters') is not None:
            temp_model = main_models.ChatBIPredictSseRequestParameters()
            self.parameters = temp_model.from_map(m.get('Parameters'))

        if m.get('PatternIndexTableName') is not None:
            self.pattern_index_table_name = m.get('PatternIndexTableName')

        if m.get('Question') is not None:
            self.question = m.get('Question')

        if m.get('SchemaIndexTableName') is not None:
            self.schema_index_table_name = m.get('SchemaIndexTableName')

        if m.get('SelectData') is not None:
            self.select_data = m.get('SelectData')

        return self



class ChatBIPredictSseRequestParameters(DaraModel):
    def __init__(
        self,
        pattern_index_threshold: float = None,
        pattern_index_top: int = None,
        result_type: str = None,
    ):
        self.pattern_index_threshold = pattern_index_threshold
        self.pattern_index_top = pattern_index_top
        self.result_type = result_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.pattern_index_threshold is not None:
            result['PatternIndexThreshold'] = self.pattern_index_threshold

        if self.pattern_index_top is not None:
            result['PatternIndexTop'] = self.pattern_index_top

        if self.result_type is not None:
            result['ResultType'] = self.result_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PatternIndexThreshold') is not None:
            self.pattern_index_threshold = m.get('PatternIndexThreshold')

        if m.get('PatternIndexTop') is not None:
            self.pattern_index_top = m.get('PatternIndexTop')

        if m.get('ResultType') is not None:
            self.result_type = m.get('ResultType')

        return self

