# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_imm20200930 import models as main_models
from darabonba.model import DaraModel

class SimpleQuery(DaraModel):
    def __init__(
        self,
        field: str = None,
        operation: str = None,
        sub_queries: List[main_models.SimpleQuery] = None,
        value: str = None,
    ):
        # This parameter is required. The field name. For a list of the supported fields, see [Supported fields and operators](https://help.aliyun.com/document_detail/252856.html).
        self.field = field
        # This parameter is required. The operator.
        # 
        # Enumerated values:
        # 
        # *   exist: exists query.
        # *   not: logical NOT.
        # *   or: logical OR.
        # *   prefix: prefix query.
        # *   and: logical AND.
        # *   It: less than.
        # *   match-phrase: string match query.
        # *   gte: greater than or equal to.
        # *   eq: equal to.
        # *   lte: less than or equal to.
        # *   gt: greater than.
        # *   nested: You can perform logical condition queries within the same object when the data type of a field is ARRAY.
        self.operation = operation
        # The subquery structure.
        # 
        # You can configure Subquery conditions only if you set the Operation parameter to and, or, not, or nested.
        # 
        # If you set the Operation parameter to and, or, or not, all query conditions specified by the SubQueries parameter must comply with the logical relationship of the parent query condition.
        # 
        # If you set the Operation parameter to nested, the parent field of a subquery must be of the ARRAY type, such as Labels. The operator of a subquery condition must be one or more of the following operators: and, or, and not. The field of the subquery must be a sub-field of the parent field.
        # 
        # For information about how to call the SimpleQuery operation, see [SimpleQuery](https://help.aliyun.com/document_detail/478175.html).
        self.sub_queries = sub_queries
        # The field value. If you set the Operation parameter to and, or, not, or nested, this parameter is invalid.
        self.value = value

    def validate(self):
        if self.sub_queries:
            for v1 in self.sub_queries:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.field is not None:
            result['Field'] = self.field

        if self.operation is not None:
            result['Operation'] = self.operation

        result['SubQueries'] = []
        if self.sub_queries is not None:
            for k1 in self.sub_queries:
                result['SubQueries'].append(k1.to_map() if k1 else None)

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Field') is not None:
            self.field = m.get('Field')

        if m.get('Operation') is not None:
            self.operation = m.get('Operation')

        self.sub_queries = []
        if m.get('SubQueries') is not None:
            for k1 in m.get('SubQueries'):
                temp_model = main_models.SimpleQuery()
                self.sub_queries.append(temp_model.from_map(k1))

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

