# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sophonsoar20220728 import models as main_models
from darabonba.model import DaraModel

class DescribeLatestRecordSchemaResponseBody(DaraModel):
    def __init__(
        self,
        playbook_node_schema: main_models.DescribeLatestRecordSchemaResponseBodyPlaybookNodeSchema = None,
        request_id: str = None,
    ):
        # The output structure information of the playbook.
        self.playbook_node_schema = playbook_node_schema
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.playbook_node_schema:
            self.playbook_node_schema.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.playbook_node_schema is not None:
            result['PlaybookNodeSchema'] = self.playbook_node_schema.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PlaybookNodeSchema') is not None:
            temp_model = main_models.DescribeLatestRecordSchemaResponseBodyPlaybookNodeSchema()
            self.playbook_node_schema = temp_model.from_map(m.get('PlaybookNodeSchema'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeLatestRecordSchemaResponseBodyPlaybookNodeSchema(DaraModel):
    def __init__(
        self,
        node_schema: List[main_models.DescribeLatestRecordSchemaResponseBodyPlaybookNodeSchemaNodeSchema] = None,
    ):
        # The structure information.
        self.node_schema = node_schema

    def validate(self):
        if self.node_schema:
            for v1 in self.node_schema:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['NodeSchema'] = []
        if self.node_schema is not None:
            for k1 in self.node_schema:
                result['NodeSchema'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.node_schema = []
        if m.get('NodeSchema') is not None:
            for k1 in m.get('NodeSchema'):
                temp_model = main_models.DescribeLatestRecordSchemaResponseBodyPlaybookNodeSchemaNodeSchema()
                self.node_schema.append(temp_model.from_map(k1))

        return self

class DescribeLatestRecordSchemaResponseBodyPlaybookNodeSchemaNodeSchema(DaraModel):
    def __init__(
        self,
        action_name: str = None,
        component_name: str = None,
        node_name: str = None,
        output_fields: List[str] = None,
    ):
        # The action name of the component.
        self.action_name = action_name
        # The name of the component.
        self.component_name = component_name
        # The name of the node.
        self.node_name = node_name
        # The output fields.
        self.output_fields = output_fields

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action_name is not None:
            result['ActionName'] = self.action_name

        if self.component_name is not None:
            result['ComponentName'] = self.component_name

        if self.node_name is not None:
            result['NodeName'] = self.node_name

        if self.output_fields is not None:
            result['OutputFields'] = self.output_fields

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionName') is not None:
            self.action_name = m.get('ActionName')

        if m.get('ComponentName') is not None:
            self.component_name = m.get('ComponentName')

        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')

        if m.get('OutputFields') is not None:
            self.output_fields = m.get('OutputFields')

        return self

