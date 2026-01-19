# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_xtee20210910 import models as main_models
from darabonba.model import DaraModel

class DescribeExpressionVariableVersionDetailResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result_object: main_models.DescribeExpressionVariableVersionDetailResponseBodyResultObject = None,
    ):
        # Request ID.
        self.request_id = request_id
        # Returned object.
        self.result_object = result_object

    def validate(self):
        if self.result_object:
            self.result_object.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result_object is not None:
            result['resultObject'] = self.result_object.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('resultObject') is not None:
            temp_model = main_models.DescribeExpressionVariableVersionDetailResponseBodyResultObject()
            self.result_object = temp_model.from_map(m.get('resultObject'))

        return self

class DescribeExpressionVariableVersionDetailResponseBodyResultObject(DaraModel):
    def __init__(
        self,
        create_type: str = None,
        description: str = None,
        expression: str = None,
        expression_title: str = None,
        expression_variable: str = None,
        field_rank: int = None,
        gmt_create: int = None,
        gmt_modified: int = None,
        id: int = None,
        invoke_key: str = None,
        name: str = None,
        outlier: str = None,
        outputs: str = None,
        ref_obj_id: str = None,
        ref_obj_type: str = None,
        region: str = None,
        source_type: str = None,
        status: str = None,
        title: str = None,
        type: str = None,
        user_id: int = None,
        version: int = None,
    ):
        # Creation type.
        self.create_type = create_type
        # Description information.
        self.description = description
        # Expression.
        self.expression = expression
        # Expression title.
        self.expression_title = expression_title
        # Expression variable.
        self.expression_variable = expression_variable
        # Field ranking.
        self.field_rank = field_rank
        # Creation time.
        self.gmt_create = gmt_create
        # Modification time.
        self.gmt_modified = gmt_modified
        # Custom variable primary key.
        self.id = id
        # Invoke key.
        self.invoke_key = invoke_key
        # Variable name, a uniquely generated identifier.
        self.name = name
        # Outlier.
        self.outlier = outlier
        # Variable return type.
        self.outputs = outputs
        # Variable associated event.
        self.ref_obj_id = ref_obj_id
        # Variable association type.
        self.ref_obj_type = ref_obj_type
        # Region ID.
        self.region = region
        # Source type.
        self.source_type = source_type
        # Status.
        self.status = status
        # Variable title.
        self.title = title
        # Variable type.
        self.type = type
        # User UID.
        self.user_id = user_id
        # Variable version.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_type is not None:
            result['createType'] = self.create_type

        if self.description is not None:
            result['description'] = self.description

        if self.expression is not None:
            result['expression'] = self.expression

        if self.expression_title is not None:
            result['expressionTitle'] = self.expression_title

        if self.expression_variable is not None:
            result['expressionVariable'] = self.expression_variable

        if self.field_rank is not None:
            result['fieldRank'] = self.field_rank

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        if self.id is not None:
            result['id'] = self.id

        if self.invoke_key is not None:
            result['invokeKey'] = self.invoke_key

        if self.name is not None:
            result['name'] = self.name

        if self.outlier is not None:
            result['outlier'] = self.outlier

        if self.outputs is not None:
            result['outputs'] = self.outputs

        if self.ref_obj_id is not None:
            result['refObjId'] = self.ref_obj_id

        if self.ref_obj_type is not None:
            result['refObjType'] = self.ref_obj_type

        if self.region is not None:
            result['region'] = self.region

        if self.source_type is not None:
            result['sourceType'] = self.source_type

        if self.status is not None:
            result['status'] = self.status

        if self.title is not None:
            result['title'] = self.title

        if self.type is not None:
            result['type'] = self.type

        if self.user_id is not None:
            result['userId'] = self.user_id

        if self.version is not None:
            result['version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createType') is not None:
            self.create_type = m.get('createType')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('expression') is not None:
            self.expression = m.get('expression')

        if m.get('expressionTitle') is not None:
            self.expression_title = m.get('expressionTitle')

        if m.get('expressionVariable') is not None:
            self.expression_variable = m.get('expressionVariable')

        if m.get('fieldRank') is not None:
            self.field_rank = m.get('fieldRank')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('invokeKey') is not None:
            self.invoke_key = m.get('invokeKey')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('outlier') is not None:
            self.outlier = m.get('outlier')

        if m.get('outputs') is not None:
            self.outputs = m.get('outputs')

        if m.get('refObjId') is not None:
            self.ref_obj_id = m.get('refObjId')

        if m.get('refObjType') is not None:
            self.ref_obj_type = m.get('refObjType')

        if m.get('region') is not None:
            self.region = m.get('region')

        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('title') is not None:
            self.title = m.get('title')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('userId') is not None:
            self.user_id = m.get('userId')

        if m.get('version') is not None:
            self.version = m.get('version')

        return self

