# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_das20200116 import models as main_models
from darabonba.model import DaraModel

class DescribeQueryExplainResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.DescribeQueryExplainResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        # List<ExplainedSqlDO>
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.DescribeQueryExplainResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeQueryExplainResponseBodyData(DaraModel):
    def __init__(
        self,
        argument: str = None,
        avg_row_size: str = None,
        defined_values: str = None,
        estimate_cpu: str = None,
        estimate_executions: str = None,
        estimate_io: str = None,
        estimate_rows: str = None,
        extra: str = None,
        id: str = None,
        index_list: List[str] = None,
        key: str = None,
        key_len: str = None,
        logical_op: str = None,
        logical_plan_list: List[str] = None,
        node_id: str = None,
        output_list: str = None,
        parallel: str = None,
        parent: str = None,
        physical_op: str = None,
        possible_keys: str = None,
        query_plan: str = None,
        ref: str = None,
        rows: str = None,
        select_type: str = None,
        stmt_id: str = None,
        stmt_text: str = None,
        table: str = None,
        table_list: List[str] = None,
        total_subtree_cost: str = None,
        type: str = None,
        warnings: str = None,
    ):
        self.argument = argument
        self.avg_row_size = avg_row_size
        self.defined_values = defined_values
        self.estimate_cpu = estimate_cpu
        self.estimate_executions = estimate_executions
        self.estimate_io = estimate_io
        self.estimate_rows = estimate_rows
        self.extra = extra
        self.id = id
        self.index_list = index_list
        self.key = key
        self.key_len = key_len
        self.logical_op = logical_op
        self.logical_plan_list = logical_plan_list
        self.node_id = node_id
        self.output_list = output_list
        self.parallel = parallel
        self.parent = parent
        self.physical_op = physical_op
        self.possible_keys = possible_keys
        self.query_plan = query_plan
        self.ref = ref
        self.rows = rows
        self.select_type = select_type
        self.stmt_id = stmt_id
        self.stmt_text = stmt_text
        self.table = table
        self.table_list = table_list
        self.total_subtree_cost = total_subtree_cost
        self.type = type
        self.warnings = warnings

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.argument is not None:
            result['Argument'] = self.argument

        if self.avg_row_size is not None:
            result['AvgRowSize'] = self.avg_row_size

        if self.defined_values is not None:
            result['DefinedValues'] = self.defined_values

        if self.estimate_cpu is not None:
            result['EstimateCPU'] = self.estimate_cpu

        if self.estimate_executions is not None:
            result['EstimateExecutions'] = self.estimate_executions

        if self.estimate_io is not None:
            result['EstimateIO'] = self.estimate_io

        if self.estimate_rows is not None:
            result['EstimateRows'] = self.estimate_rows

        if self.extra is not None:
            result['Extra'] = self.extra

        if self.id is not None:
            result['Id'] = self.id

        if self.index_list is not None:
            result['IndexList'] = self.index_list

        if self.key is not None:
            result['Key'] = self.key

        if self.key_len is not None:
            result['KeyLen'] = self.key_len

        if self.logical_op is not None:
            result['LogicalOp'] = self.logical_op

        if self.logical_plan_list is not None:
            result['LogicalPlanList'] = self.logical_plan_list

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.output_list is not None:
            result['OutputList'] = self.output_list

        if self.parallel is not None:
            result['Parallel'] = self.parallel

        if self.parent is not None:
            result['Parent'] = self.parent

        if self.physical_op is not None:
            result['PhysicalOp'] = self.physical_op

        if self.possible_keys is not None:
            result['PossibleKeys'] = self.possible_keys

        if self.query_plan is not None:
            result['QueryPlan'] = self.query_plan

        if self.ref is not None:
            result['Ref'] = self.ref

        if self.rows is not None:
            result['Rows'] = self.rows

        if self.select_type is not None:
            result['SelectType'] = self.select_type

        if self.stmt_id is not None:
            result['StmtId'] = self.stmt_id

        if self.stmt_text is not None:
            result['StmtText'] = self.stmt_text

        if self.table is not None:
            result['Table'] = self.table

        if self.table_list is not None:
            result['TableList'] = self.table_list

        if self.total_subtree_cost is not None:
            result['TotalSubtreeCost'] = self.total_subtree_cost

        if self.type is not None:
            result['Type'] = self.type

        if self.warnings is not None:
            result['Warnings'] = self.warnings

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Argument') is not None:
            self.argument = m.get('Argument')

        if m.get('AvgRowSize') is not None:
            self.avg_row_size = m.get('AvgRowSize')

        if m.get('DefinedValues') is not None:
            self.defined_values = m.get('DefinedValues')

        if m.get('EstimateCPU') is not None:
            self.estimate_cpu = m.get('EstimateCPU')

        if m.get('EstimateExecutions') is not None:
            self.estimate_executions = m.get('EstimateExecutions')

        if m.get('EstimateIO') is not None:
            self.estimate_io = m.get('EstimateIO')

        if m.get('EstimateRows') is not None:
            self.estimate_rows = m.get('EstimateRows')

        if m.get('Extra') is not None:
            self.extra = m.get('Extra')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('IndexList') is not None:
            self.index_list = m.get('IndexList')

        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('KeyLen') is not None:
            self.key_len = m.get('KeyLen')

        if m.get('LogicalOp') is not None:
            self.logical_op = m.get('LogicalOp')

        if m.get('LogicalPlanList') is not None:
            self.logical_plan_list = m.get('LogicalPlanList')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('OutputList') is not None:
            self.output_list = m.get('OutputList')

        if m.get('Parallel') is not None:
            self.parallel = m.get('Parallel')

        if m.get('Parent') is not None:
            self.parent = m.get('Parent')

        if m.get('PhysicalOp') is not None:
            self.physical_op = m.get('PhysicalOp')

        if m.get('PossibleKeys') is not None:
            self.possible_keys = m.get('PossibleKeys')

        if m.get('QueryPlan') is not None:
            self.query_plan = m.get('QueryPlan')

        if m.get('Ref') is not None:
            self.ref = m.get('Ref')

        if m.get('Rows') is not None:
            self.rows = m.get('Rows')

        if m.get('SelectType') is not None:
            self.select_type = m.get('SelectType')

        if m.get('StmtId') is not None:
            self.stmt_id = m.get('StmtId')

        if m.get('StmtText') is not None:
            self.stmt_text = m.get('StmtText')

        if m.get('Table') is not None:
            self.table = m.get('Table')

        if m.get('TableList') is not None:
            self.table_list = m.get('TableList')

        if m.get('TotalSubtreeCost') is not None:
            self.total_subtree_cost = m.get('TotalSubtreeCost')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Warnings') is not None:
            self.warnings = m.get('Warnings')

        return self

