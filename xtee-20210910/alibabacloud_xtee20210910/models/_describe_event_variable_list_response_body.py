# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_xtee20210910 import models as main_models
from darabonba.model import DaraModel

class DescribeEventVariableListResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result_object: main_models.DescribeEventVariableListResponseBodyResultObject = None,
    ):
        # Request ID.
        self.request_id = request_id
        # Return object.
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
            temp_model = main_models.DescribeEventVariableListResponseBodyResultObject()
            self.result_object = temp_model.from_map(m.get('resultObject'))

        return self

class DescribeEventVariableListResponseBodyResultObject(DaraModel):
    def __init__(
        self,
        actions: List[main_models.DescribeEventVariableListResponseBodyResultObjectActions] = None,
        device_variables: List[main_models.DescribeEventVariableListResponseBodyResultObjectDeviceVariables] = None,
        expression_variables: List[main_models.DescribeEventVariableListResponseBodyResultObjectExpressionVariables] = None,
        favorite_variables: List[main_models.DescribeEventVariableListResponseBodyResultObjectFavoriteVariables] = None,
        middle_variables: List[main_models.DescribeEventVariableListResponseBodyResultObjectMiddleVariables] = None,
        model_variables: List[main_models.DescribeEventVariableListResponseBodyResultObjectModelVariables] = None,
        name_list: List[main_models.DescribeEventVariableListResponseBodyResultObjectNameList] = None,
        native_variable_functions: List[main_models.DescribeEventVariableListResponseBodyResultObjectNativeVariableFunctions] = None,
        native_variables: List[main_models.DescribeEventVariableListResponseBodyResultObjectNativeVariables] = None,
        query_variables: List[main_models.DescribeEventVariableListResponseBodyResultObjectQueryVariables] = None,
        self_variables: List[main_models.DescribeEventVariableListResponseBodyResultObjectSelfVariables] = None,
        sys_variables: List[main_models.DescribeEventVariableListResponseBodyResultObjectSysVariables] = None,
        third_variables: Dict[str, Any] = None,
        velocity_variables: List[main_models.DescribeEventVariableListResponseBodyResultObjectVelocityVariables] = None,
    ):
        # Action variable.
        self.actions = actions
        # Device variable.
        self.device_variables = device_variables
        # Custom variable.
        self.expression_variables = expression_variables
        # Favorite variables.
        self.favorite_variables = favorite_variables
        # Intermediate variable return object.
        self.middle_variables = middle_variables
        # An array of model variables.
        self.model_variables = model_variables
        # List of name variables.
        self.name_list = name_list
        # List of available functions for the original variable.
        self.native_variable_functions = native_variable_functions
        # List of event fields.
        self.native_variables = native_variables
        # An array of custom query variables.
        self.query_variables = query_variables
        # Custom variables (custom variables, cumulative variables, custom system variables).
        self.self_variables = self_variables
        # System variables.
        self.sys_variables = sys_variables
        # Other related variables.
        self.third_variables = third_variables
        # An array of accumulated variables.
        self.velocity_variables = velocity_variables

    def validate(self):
        if self.actions:
            for v1 in self.actions:
                 if v1:
                    v1.validate()
        if self.device_variables:
            for v1 in self.device_variables:
                 if v1:
                    v1.validate()
        if self.expression_variables:
            for v1 in self.expression_variables:
                 if v1:
                    v1.validate()
        if self.favorite_variables:
            for v1 in self.favorite_variables:
                 if v1:
                    v1.validate()
        if self.middle_variables:
            for v1 in self.middle_variables:
                 if v1:
                    v1.validate()
        if self.model_variables:
            for v1 in self.model_variables:
                 if v1:
                    v1.validate()
        if self.name_list:
            for v1 in self.name_list:
                 if v1:
                    v1.validate()
        if self.native_variable_functions:
            for v1 in self.native_variable_functions:
                 if v1:
                    v1.validate()
        if self.native_variables:
            for v1 in self.native_variables:
                 if v1:
                    v1.validate()
        if self.query_variables:
            for v1 in self.query_variables:
                 if v1:
                    v1.validate()
        if self.self_variables:
            for v1 in self.self_variables:
                 if v1:
                    v1.validate()
        if self.sys_variables:
            for v1 in self.sys_variables:
                 if v1:
                    v1.validate()
        if self.velocity_variables:
            for v1 in self.velocity_variables:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['actions'] = []
        if self.actions is not None:
            for k1 in self.actions:
                result['actions'].append(k1.to_map() if k1 else None)

        result['deviceVariables'] = []
        if self.device_variables is not None:
            for k1 in self.device_variables:
                result['deviceVariables'].append(k1.to_map() if k1 else None)

        result['expressionVariables'] = []
        if self.expression_variables is not None:
            for k1 in self.expression_variables:
                result['expressionVariables'].append(k1.to_map() if k1 else None)

        result['favoriteVariables'] = []
        if self.favorite_variables is not None:
            for k1 in self.favorite_variables:
                result['favoriteVariables'].append(k1.to_map() if k1 else None)

        result['middleVariables'] = []
        if self.middle_variables is not None:
            for k1 in self.middle_variables:
                result['middleVariables'].append(k1.to_map() if k1 else None)

        result['modelVariables'] = []
        if self.model_variables is not None:
            for k1 in self.model_variables:
                result['modelVariables'].append(k1.to_map() if k1 else None)

        result['nameList'] = []
        if self.name_list is not None:
            for k1 in self.name_list:
                result['nameList'].append(k1.to_map() if k1 else None)

        result['nativeVariableFunctions'] = []
        if self.native_variable_functions is not None:
            for k1 in self.native_variable_functions:
                result['nativeVariableFunctions'].append(k1.to_map() if k1 else None)

        result['nativeVariables'] = []
        if self.native_variables is not None:
            for k1 in self.native_variables:
                result['nativeVariables'].append(k1.to_map() if k1 else None)

        result['queryVariables'] = []
        if self.query_variables is not None:
            for k1 in self.query_variables:
                result['queryVariables'].append(k1.to_map() if k1 else None)

        result['selfVariables'] = []
        if self.self_variables is not None:
            for k1 in self.self_variables:
                result['selfVariables'].append(k1.to_map() if k1 else None)

        result['sysVariables'] = []
        if self.sys_variables is not None:
            for k1 in self.sys_variables:
                result['sysVariables'].append(k1.to_map() if k1 else None)

        if self.third_variables is not None:
            result['thirdVariables'] = self.third_variables

        result['velocityVariables'] = []
        if self.velocity_variables is not None:
            for k1 in self.velocity_variables:
                result['velocityVariables'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.actions = []
        if m.get('actions') is not None:
            for k1 in m.get('actions'):
                temp_model = main_models.DescribeEventVariableListResponseBodyResultObjectActions()
                self.actions.append(temp_model.from_map(k1))

        self.device_variables = []
        if m.get('deviceVariables') is not None:
            for k1 in m.get('deviceVariables'):
                temp_model = main_models.DescribeEventVariableListResponseBodyResultObjectDeviceVariables()
                self.device_variables.append(temp_model.from_map(k1))

        self.expression_variables = []
        if m.get('expressionVariables') is not None:
            for k1 in m.get('expressionVariables'):
                temp_model = main_models.DescribeEventVariableListResponseBodyResultObjectExpressionVariables()
                self.expression_variables.append(temp_model.from_map(k1))

        self.favorite_variables = []
        if m.get('favoriteVariables') is not None:
            for k1 in m.get('favoriteVariables'):
                temp_model = main_models.DescribeEventVariableListResponseBodyResultObjectFavoriteVariables()
                self.favorite_variables.append(temp_model.from_map(k1))

        self.middle_variables = []
        if m.get('middleVariables') is not None:
            for k1 in m.get('middleVariables'):
                temp_model = main_models.DescribeEventVariableListResponseBodyResultObjectMiddleVariables()
                self.middle_variables.append(temp_model.from_map(k1))

        self.model_variables = []
        if m.get('modelVariables') is not None:
            for k1 in m.get('modelVariables'):
                temp_model = main_models.DescribeEventVariableListResponseBodyResultObjectModelVariables()
                self.model_variables.append(temp_model.from_map(k1))

        self.name_list = []
        if m.get('nameList') is not None:
            for k1 in m.get('nameList'):
                temp_model = main_models.DescribeEventVariableListResponseBodyResultObjectNameList()
                self.name_list.append(temp_model.from_map(k1))

        self.native_variable_functions = []
        if m.get('nativeVariableFunctions') is not None:
            for k1 in m.get('nativeVariableFunctions'):
                temp_model = main_models.DescribeEventVariableListResponseBodyResultObjectNativeVariableFunctions()
                self.native_variable_functions.append(temp_model.from_map(k1))

        self.native_variables = []
        if m.get('nativeVariables') is not None:
            for k1 in m.get('nativeVariables'):
                temp_model = main_models.DescribeEventVariableListResponseBodyResultObjectNativeVariables()
                self.native_variables.append(temp_model.from_map(k1))

        self.query_variables = []
        if m.get('queryVariables') is not None:
            for k1 in m.get('queryVariables'):
                temp_model = main_models.DescribeEventVariableListResponseBodyResultObjectQueryVariables()
                self.query_variables.append(temp_model.from_map(k1))

        self.self_variables = []
        if m.get('selfVariables') is not None:
            for k1 in m.get('selfVariables'):
                temp_model = main_models.DescribeEventVariableListResponseBodyResultObjectSelfVariables()
                self.self_variables.append(temp_model.from_map(k1))

        self.sys_variables = []
        if m.get('sysVariables') is not None:
            for k1 in m.get('sysVariables'):
                temp_model = main_models.DescribeEventVariableListResponseBodyResultObjectSysVariables()
                self.sys_variables.append(temp_model.from_map(k1))

        if m.get('thirdVariables') is not None:
            self.third_variables = m.get('thirdVariables')

        self.velocity_variables = []
        if m.get('velocityVariables') is not None:
            for k1 in m.get('velocityVariables'):
                temp_model = main_models.DescribeEventVariableListResponseBodyResultObjectVelocityVariables()
                self.velocity_variables.append(temp_model.from_map(k1))

        return self

class DescribeEventVariableListResponseBodyResultObjectVelocityVariables(DaraModel):
    def __init__(
        self,
        code: str = None,
        data_display: str = None,
        define_id: str = None,
        description: str = None,
        display_type: str = None,
        expression_title: str = None,
        favorite_flag: bool = None,
        field_detail: str = None,
        field_rank: int = None,
        field_source: str = None,
        field_type: str = None,
        id: int = None,
        input_field_type: str = None,
        input_required: str = None,
        inputs: str = None,
        name: str = None,
        outlier: str = None,
        output_threshold: main_models.DescribeEventVariableListResponseBodyResultObjectVelocityVariablesOutputThreshold = None,
        parent_name: str = None,
        source_type: str = None,
        title: str = None,
        type: str = None,
        variable_velocity: main_models.DescribeEventVariableListResponseBodyResultObjectVelocityVariablesVariableVelocity = None,
        x_label: str = None,
        y_label: str = None,
    ):
        # The code of the variable.
        self.code = code
        # Data distribution display, in JSON format. This field is not returned for this type of variable.
        self.data_display = data_display
        # The definition ID of the variable. This field is not returned for this type of variable.
        self.define_id = define_id
        # The description of the variable.
        self.description = description
        # The display type and grouping label.
        self.display_type = display_type
        # The display value of the calculation expression. This field is not returned for this type of variable.
        self.expression_title = expression_title
        # The favorite flag.
        self.favorite_flag = favorite_flag
        # The detailed information of the field in the field pool. This field is not returned for this type of variable.
        self.field_detail = field_detail
        # The field rank.
        self.field_rank = field_rank
        # The source of the field. This field is not returned for this type of variable.
        self.field_source = field_source
        # The type of the field.
        self.field_type = field_type
        # The primary key ID.
        self.id = id
        # The input type of the parameter. This field is not returned for this type of variable.
        self.input_field_type = input_field_type
        # The required parameter. This field is not returned for this type of variable.
        self.input_required = input_required
        # Multiple input parameters separated by commas. This field is not returned for this type of variable.
        self.inputs = inputs
        # The name of the variable.
        self.name = name
        # The outlier value. This field is not returned for this type of variable.
        self.outlier = outlier
        # The output value threshold.
        self.output_threshold = output_threshold
        # The parent node. This field is not returned for this type of variable.
        self.parent_name = parent_name
        # The source type.
        self.source_type = source_type
        # The title of the variable.
        self.title = title
        # The type of the variable.
        self.type = type
        # The variable metric information. This field is not returned for this type of variable.
        self.variable_velocity = variable_velocity
        # The X label. This field is not returned for this type of variable.
        self.x_label = x_label
        # The Y label. This field is not returned for this type of variable.
        self.y_label = y_label

    def validate(self):
        if self.output_threshold:
            self.output_threshold.validate()
        if self.variable_velocity:
            self.variable_velocity.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.data_display is not None:
            result['dataDisplay'] = self.data_display

        if self.define_id is not None:
            result['defineId'] = self.define_id

        if self.description is not None:
            result['description'] = self.description

        if self.display_type is not None:
            result['displayType'] = self.display_type

        if self.expression_title is not None:
            result['expressionTitle'] = self.expression_title

        if self.favorite_flag is not None:
            result['favoriteFlag'] = self.favorite_flag

        if self.field_detail is not None:
            result['fieldDetail'] = self.field_detail

        if self.field_rank is not None:
            result['fieldRank'] = self.field_rank

        if self.field_source is not None:
            result['fieldSource'] = self.field_source

        if self.field_type is not None:
            result['fieldType'] = self.field_type

        if self.id is not None:
            result['id'] = self.id

        if self.input_field_type is not None:
            result['inputFieldType'] = self.input_field_type

        if self.input_required is not None:
            result['inputRequired'] = self.input_required

        if self.inputs is not None:
            result['inputs'] = self.inputs

        if self.name is not None:
            result['name'] = self.name

        if self.outlier is not None:
            result['outlier'] = self.outlier

        if self.output_threshold is not None:
            result['outputThreshold'] = self.output_threshold.to_map()

        if self.parent_name is not None:
            result['parentName'] = self.parent_name

        if self.source_type is not None:
            result['sourceType'] = self.source_type

        if self.title is not None:
            result['title'] = self.title

        if self.type is not None:
            result['type'] = self.type

        if self.variable_velocity is not None:
            result['variableVelocity'] = self.variable_velocity.to_map()

        if self.x_label is not None:
            result['xLabel'] = self.x_label

        if self.y_label is not None:
            result['yLabel'] = self.y_label

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('dataDisplay') is not None:
            self.data_display = m.get('dataDisplay')

        if m.get('defineId') is not None:
            self.define_id = m.get('defineId')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('displayType') is not None:
            self.display_type = m.get('displayType')

        if m.get('expressionTitle') is not None:
            self.expression_title = m.get('expressionTitle')

        if m.get('favoriteFlag') is not None:
            self.favorite_flag = m.get('favoriteFlag')

        if m.get('fieldDetail') is not None:
            self.field_detail = m.get('fieldDetail')

        if m.get('fieldRank') is not None:
            self.field_rank = m.get('fieldRank')

        if m.get('fieldSource') is not None:
            self.field_source = m.get('fieldSource')

        if m.get('fieldType') is not None:
            self.field_type = m.get('fieldType')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('inputFieldType') is not None:
            self.input_field_type = m.get('inputFieldType')

        if m.get('inputRequired') is not None:
            self.input_required = m.get('inputRequired')

        if m.get('inputs') is not None:
            self.inputs = m.get('inputs')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('outlier') is not None:
            self.outlier = m.get('outlier')

        if m.get('outputThreshold') is not None:
            temp_model = main_models.DescribeEventVariableListResponseBodyResultObjectVelocityVariablesOutputThreshold()
            self.output_threshold = temp_model.from_map(m.get('outputThreshold'))

        if m.get('parentName') is not None:
            self.parent_name = m.get('parentName')

        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')

        if m.get('title') is not None:
            self.title = m.get('title')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('variableVelocity') is not None:
            temp_model = main_models.DescribeEventVariableListResponseBodyResultObjectVelocityVariablesVariableVelocity()
            self.variable_velocity = temp_model.from_map(m.get('variableVelocity'))

        if m.get('xLabel') is not None:
            self.x_label = m.get('xLabel')

        if m.get('yLabel') is not None:
            self.y_label = m.get('yLabel')

        return self

class DescribeEventVariableListResponseBodyResultObjectVelocityVariablesVariableVelocity(DaraModel):
    def __init__(
        self,
        iv: str = None,
    ):
        # The IV value. This field is not returned for this type of variable.
        self.iv = iv

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.iv is not None:
            result['iv'] = self.iv

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('iv') is not None:
            self.iv = m.get('iv')

        return self

class DescribeEventVariableListResponseBodyResultObjectVelocityVariablesOutputThreshold(DaraModel):
    def __init__(
        self,
        max_value: float = None,
        min_value: float = None,
    ):
        # The maximum value.
        self.max_value = max_value
        # The minimum value.
        self.min_value = min_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_value is not None:
            result['maxValue'] = self.max_value

        if self.min_value is not None:
            result['minValue'] = self.min_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxValue') is not None:
            self.max_value = m.get('maxValue')

        if m.get('minValue') is not None:
            self.min_value = m.get('minValue')

        return self

class DescribeEventVariableListResponseBodyResultObjectSysVariables(DaraModel):
    def __init__(
        self,
        code: str = None,
        data_display: str = None,
        define_id: str = None,
        description: str = None,
        display_type: str = None,
        expression_title: str = None,
        favorite_flag: bool = None,
        field_detail: str = None,
        field_rank: int = None,
        field_source: str = None,
        field_type: str = None,
        id: int = None,
        input_field_type: str = None,
        input_required: str = None,
        inputs: str = None,
        name: str = None,
        outlier: str = None,
        output_threshold: main_models.DescribeEventVariableListResponseBodyResultObjectSysVariablesOutputThreshold = None,
        parent_name: str = None,
        source_type: str = None,
        title: str = None,
        type: str = None,
        variable_velocity: main_models.DescribeEventVariableListResponseBodyResultObjectSysVariablesVariableVelocity = None,
        x_label: str = None,
        y_label: str = None,
    ):
        # Variable code.
        self.code = code
        # Data distribution display, in JSON format. This field is not returned for this type of variable.
        self.data_display = data_display
        # ID of the bound variable definition.
        self.define_id = define_id
        # Description of the variable.
        self.description = description
        # Display type and group label.
        self.display_type = display_type
        # Calculate the expression display value. This type of variable does not return this field.
        self.expression_title = expression_title
        # Favorite identifier.
        self.favorite_flag = favorite_flag
        # Details of the field pool. This type of variable does not return this field.
        self.field_detail = field_detail
        # Field sorting.
        self.field_rank = field_rank
        # Source of the field. This type of variable does not return this field.
        self.field_source = field_source
        # Field type.
        self.field_type = field_type
        # Variable ID.
        self.id = id
        # Input type of the parameter. This field is not returned for this type of variable.
        self.input_field_type = input_field_type
        # Required parameter. This field is not returned for this type of variable.
        self.input_required = input_required
        # Variable value input.
        self.inputs = inputs
        # Variable name.
        self.name = name
        # Outlier value. This field is not returned for this type of variable.
        self.outlier = outlier
        # Output value threshold.
        self.output_threshold = output_threshold
        # Parent name.
        self.parent_name = parent_name
        # Source type.
        self.source_type = source_type
        # Title.
        self.title = title
        # Variable type.
        self.type = type
        # Variable metric information. This field is not returned for this type of variable.
        self.variable_velocity = variable_velocity
        # x label. This type of variable does not return this field.
        self.x_label = x_label
        # y label. This type of variable does not return this field.
        self.y_label = y_label

    def validate(self):
        if self.output_threshold:
            self.output_threshold.validate()
        if self.variable_velocity:
            self.variable_velocity.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.data_display is not None:
            result['dataDisplay'] = self.data_display

        if self.define_id is not None:
            result['defineId'] = self.define_id

        if self.description is not None:
            result['description'] = self.description

        if self.display_type is not None:
            result['displayType'] = self.display_type

        if self.expression_title is not None:
            result['expressionTitle'] = self.expression_title

        if self.favorite_flag is not None:
            result['favoriteFlag'] = self.favorite_flag

        if self.field_detail is not None:
            result['fieldDetail'] = self.field_detail

        if self.field_rank is not None:
            result['fieldRank'] = self.field_rank

        if self.field_source is not None:
            result['fieldSource'] = self.field_source

        if self.field_type is not None:
            result['fieldType'] = self.field_type

        if self.id is not None:
            result['id'] = self.id

        if self.input_field_type is not None:
            result['inputFieldType'] = self.input_field_type

        if self.input_required is not None:
            result['inputRequired'] = self.input_required

        if self.inputs is not None:
            result['inputs'] = self.inputs

        if self.name is not None:
            result['name'] = self.name

        if self.outlier is not None:
            result['outlier'] = self.outlier

        if self.output_threshold is not None:
            result['outputThreshold'] = self.output_threshold.to_map()

        if self.parent_name is not None:
            result['parentName'] = self.parent_name

        if self.source_type is not None:
            result['sourceType'] = self.source_type

        if self.title is not None:
            result['title'] = self.title

        if self.type is not None:
            result['type'] = self.type

        if self.variable_velocity is not None:
            result['variableVelocity'] = self.variable_velocity.to_map()

        if self.x_label is not None:
            result['xLabel'] = self.x_label

        if self.y_label is not None:
            result['yLabel'] = self.y_label

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('dataDisplay') is not None:
            self.data_display = m.get('dataDisplay')

        if m.get('defineId') is not None:
            self.define_id = m.get('defineId')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('displayType') is not None:
            self.display_type = m.get('displayType')

        if m.get('expressionTitle') is not None:
            self.expression_title = m.get('expressionTitle')

        if m.get('favoriteFlag') is not None:
            self.favorite_flag = m.get('favoriteFlag')

        if m.get('fieldDetail') is not None:
            self.field_detail = m.get('fieldDetail')

        if m.get('fieldRank') is not None:
            self.field_rank = m.get('fieldRank')

        if m.get('fieldSource') is not None:
            self.field_source = m.get('fieldSource')

        if m.get('fieldType') is not None:
            self.field_type = m.get('fieldType')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('inputFieldType') is not None:
            self.input_field_type = m.get('inputFieldType')

        if m.get('inputRequired') is not None:
            self.input_required = m.get('inputRequired')

        if m.get('inputs') is not None:
            self.inputs = m.get('inputs')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('outlier') is not None:
            self.outlier = m.get('outlier')

        if m.get('outputThreshold') is not None:
            temp_model = main_models.DescribeEventVariableListResponseBodyResultObjectSysVariablesOutputThreshold()
            self.output_threshold = temp_model.from_map(m.get('outputThreshold'))

        if m.get('parentName') is not None:
            self.parent_name = m.get('parentName')

        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')

        if m.get('title') is not None:
            self.title = m.get('title')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('variableVelocity') is not None:
            temp_model = main_models.DescribeEventVariableListResponseBodyResultObjectSysVariablesVariableVelocity()
            self.variable_velocity = temp_model.from_map(m.get('variableVelocity'))

        if m.get('xLabel') is not None:
            self.x_label = m.get('xLabel')

        if m.get('yLabel') is not None:
            self.y_label = m.get('yLabel')

        return self

class DescribeEventVariableListResponseBodyResultObjectSysVariablesVariableVelocity(DaraModel):
    def __init__(
        self,
        iv: str = None,
    ):
        # iv value. This type of variable does not return this field.
        self.iv = iv

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.iv is not None:
            result['iv'] = self.iv

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('iv') is not None:
            self.iv = m.get('iv')

        return self

class DescribeEventVariableListResponseBodyResultObjectSysVariablesOutputThreshold(DaraModel):
    def __init__(
        self,
        max_value: float = None,
        min_value: float = None,
    ):
        # Maximum value.
        self.max_value = max_value
        # Minimum value.
        self.min_value = min_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_value is not None:
            result['maxValue'] = self.max_value

        if self.min_value is not None:
            result['minValue'] = self.min_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxValue') is not None:
            self.max_value = m.get('maxValue')

        if m.get('minValue') is not None:
            self.min_value = m.get('minValue')

        return self

class DescribeEventVariableListResponseBodyResultObjectSelfVariables(DaraModel):
    def __init__(
        self,
        code: str = None,
        data_display: str = None,
        define_id: str = None,
        description: str = None,
        display_type: str = None,
        expression_title: str = None,
        favorite_flag: bool = None,
        field_detail: str = None,
        field_rank: int = None,
        field_source: str = None,
        field_type: str = None,
        id: int = None,
        input_field_type: str = None,
        input_required: str = None,
        inputs: str = None,
        name: str = None,
        outlier: str = None,
        output_threshold: main_models.DescribeEventVariableListResponseBodyResultObjectSelfVariablesOutputThreshold = None,
        parent_name: str = None,
        source_type: str = None,
        title: str = None,
        type: str = None,
        variable_velocity: main_models.DescribeEventVariableListResponseBodyResultObjectSelfVariablesVariableVelocity = None,
        x_label: str = None,
        y_label: str = None,
    ):
        # Variable code.
        self.code = code
        # Data distribution display, in JSON format. This field is not returned for this type of variable.
        self.data_display = data_display
        # Variable definition ID. Only returned for custom system variables.
        self.define_id = define_id
        # Description of the variable.
        self.description = description
        # Display type and group label.
        self.display_type = display_type
        # Expression name.
        self.expression_title = expression_title
        # Favorite identifier.
        self.favorite_flag = favorite_flag
        # Details of the field pool. This type of variable does not return this field.
        self.field_detail = field_detail
        # Field sorting.
        self.field_rank = field_rank
        # Source of the field. This type of variable does not return this field.
        self.field_source = field_source
        # Field type.
        self.field_type = field_type
        # Variable ID.
        self.id = id
        # The input type of the parameter. This field is not returned for this type of variable.
        self.input_field_type = input_field_type
        # Required parameter. This field is not returned for this type of variable.
        self.input_required = input_required
        # Input parameters. Only returned when custom system variables are defined.
        self.inputs = inputs
        # Variable name.
        self.name = name
        # Anomaly value. Returned when the variable is a custom variable (type= EXPRESSION).
        self.outlier = outlier
        # Output value threshold.
        self.output_threshold = output_threshold
        # Parent node. This field is not returned currently.
        self.parent_name = parent_name
        # Source type.
        self.source_type = source_type
        # Title.
        self.title = title
        # Variable type.
        self.type = type
        # Variable metric information. This field is not returned for this type of variable.
        self.variable_velocity = variable_velocity
        # x label. This type of variable does not return this field.
        self.x_label = x_label
        # y label. This type of variable does not return this field.
        self.y_label = y_label

    def validate(self):
        if self.output_threshold:
            self.output_threshold.validate()
        if self.variable_velocity:
            self.variable_velocity.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.data_display is not None:
            result['dataDisplay'] = self.data_display

        if self.define_id is not None:
            result['defineId'] = self.define_id

        if self.description is not None:
            result['description'] = self.description

        if self.display_type is not None:
            result['displayType'] = self.display_type

        if self.expression_title is not None:
            result['expressionTitle'] = self.expression_title

        if self.favorite_flag is not None:
            result['favoriteFlag'] = self.favorite_flag

        if self.field_detail is not None:
            result['fieldDetail'] = self.field_detail

        if self.field_rank is not None:
            result['fieldRank'] = self.field_rank

        if self.field_source is not None:
            result['fieldSource'] = self.field_source

        if self.field_type is not None:
            result['fieldType'] = self.field_type

        if self.id is not None:
            result['id'] = self.id

        if self.input_field_type is not None:
            result['inputFieldType'] = self.input_field_type

        if self.input_required is not None:
            result['inputRequired'] = self.input_required

        if self.inputs is not None:
            result['inputs'] = self.inputs

        if self.name is not None:
            result['name'] = self.name

        if self.outlier is not None:
            result['outlier'] = self.outlier

        if self.output_threshold is not None:
            result['outputThreshold'] = self.output_threshold.to_map()

        if self.parent_name is not None:
            result['parentName'] = self.parent_name

        if self.source_type is not None:
            result['sourceType'] = self.source_type

        if self.title is not None:
            result['title'] = self.title

        if self.type is not None:
            result['type'] = self.type

        if self.variable_velocity is not None:
            result['variableVelocity'] = self.variable_velocity.to_map()

        if self.x_label is not None:
            result['xLabel'] = self.x_label

        if self.y_label is not None:
            result['yLabel'] = self.y_label

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('dataDisplay') is not None:
            self.data_display = m.get('dataDisplay')

        if m.get('defineId') is not None:
            self.define_id = m.get('defineId')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('displayType') is not None:
            self.display_type = m.get('displayType')

        if m.get('expressionTitle') is not None:
            self.expression_title = m.get('expressionTitle')

        if m.get('favoriteFlag') is not None:
            self.favorite_flag = m.get('favoriteFlag')

        if m.get('fieldDetail') is not None:
            self.field_detail = m.get('fieldDetail')

        if m.get('fieldRank') is not None:
            self.field_rank = m.get('fieldRank')

        if m.get('fieldSource') is not None:
            self.field_source = m.get('fieldSource')

        if m.get('fieldType') is not None:
            self.field_type = m.get('fieldType')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('inputFieldType') is not None:
            self.input_field_type = m.get('inputFieldType')

        if m.get('inputRequired') is not None:
            self.input_required = m.get('inputRequired')

        if m.get('inputs') is not None:
            self.inputs = m.get('inputs')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('outlier') is not None:
            self.outlier = m.get('outlier')

        if m.get('outputThreshold') is not None:
            temp_model = main_models.DescribeEventVariableListResponseBodyResultObjectSelfVariablesOutputThreshold()
            self.output_threshold = temp_model.from_map(m.get('outputThreshold'))

        if m.get('parentName') is not None:
            self.parent_name = m.get('parentName')

        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')

        if m.get('title') is not None:
            self.title = m.get('title')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('variableVelocity') is not None:
            temp_model = main_models.DescribeEventVariableListResponseBodyResultObjectSelfVariablesVariableVelocity()
            self.variable_velocity = temp_model.from_map(m.get('variableVelocity'))

        if m.get('xLabel') is not None:
            self.x_label = m.get('xLabel')

        if m.get('yLabel') is not None:
            self.y_label = m.get('yLabel')

        return self

class DescribeEventVariableListResponseBodyResultObjectSelfVariablesVariableVelocity(DaraModel):
    def __init__(
        self,
        iv: str = None,
    ):
        # iv value. This type of variable does not return this field.
        self.iv = iv

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.iv is not None:
            result['iv'] = self.iv

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('iv') is not None:
            self.iv = m.get('iv')

        return self

class DescribeEventVariableListResponseBodyResultObjectSelfVariablesOutputThreshold(DaraModel):
    def __init__(
        self,
        max_value: float = None,
        min_value: float = None,
    ):
        # Maximum value.
        self.max_value = max_value
        # Minimum value.
        self.min_value = min_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_value is not None:
            result['maxValue'] = self.max_value

        if self.min_value is not None:
            result['minValue'] = self.min_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxValue') is not None:
            self.max_value = m.get('maxValue')

        if m.get('minValue') is not None:
            self.min_value = m.get('minValue')

        return self

class DescribeEventVariableListResponseBodyResultObjectQueryVariables(DaraModel):
    def __init__(
        self,
        code: str = None,
        data_display: str = None,
        define_id: str = None,
        description: str = None,
        display_type: str = None,
        expression_title: str = None,
        favorite_flag: bool = None,
        field_detail: str = None,
        field_rank: int = None,
        field_source: str = None,
        field_type: str = None,
        id: int = None,
        input_field_type: str = None,
        input_required: str = None,
        inputs: str = None,
        name: str = None,
        outlier: str = None,
        output_threshold: main_models.DescribeEventVariableListResponseBodyResultObjectQueryVariablesOutputThreshold = None,
        parent_name: str = None,
        source_type: str = None,
        title: str = None,
        type: str = None,
        variable_velocity: main_models.DescribeEventVariableListResponseBodyResultObjectQueryVariablesVariableVelocity = None,
        x_label: str = None,
        y_label: str = None,
    ):
        # The code of the query variable.
        self.code = code
        # Data distribution display, in JSON format. This field is not returned for this type of variable.
        self.data_display = data_display
        # The definition ID of the query variable. This field is not returned for this type of variable.
        self.define_id = define_id
        # The description of the query variable.
        self.description = description
        # The display type and grouping label.
        self.display_type = display_type
        # The display value of the calculation expression. This field is not returned for this type of variable.
        self.expression_title = expression_title
        # The favorite flag.
        self.favorite_flag = favorite_flag
        # The detailed information of the field in the field pool. This field is not returned for this type of variable.
        self.field_detail = field_detail
        # The field rank.
        self.field_rank = field_rank
        # The source of the field. This field is not returned for this type of variable.
        self.field_source = field_source
        # The type of the field.
        self.field_type = field_type
        # The primary key ID of the query variable.
        self.id = id
        # The input type of the parameter. This field is not returned for this type of variable.
        self.input_field_type = input_field_type
        # The required parameter. This field is not returned for this type of variable.
        self.input_required = input_required
        # Multiple input parameters separated by commas. This field is not returned for this type of variable.
        self.inputs = inputs
        # The name of the query variable.
        self.name = name
        # The outlier value.
        self.outlier = outlier
        # The output value threshold.
        self.output_threshold = output_threshold
        # The parent node. This field is not returned for this type of variable.
        self.parent_name = parent_name
        # The source type.
        self.source_type = source_type
        # The title of the query variable. The title of the query variable.
        self.title = title
        # The type of the query variable.
        self.type = type
        # The variable metric information. This field is not returned for this type of variable.
        self.variable_velocity = variable_velocity
        # The X label. This field is not returned for this type of variable.
        self.x_label = x_label
        # The Y label. This field is not returned for this type of variable.
        self.y_label = y_label

    def validate(self):
        if self.output_threshold:
            self.output_threshold.validate()
        if self.variable_velocity:
            self.variable_velocity.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.data_display is not None:
            result['dataDisplay'] = self.data_display

        if self.define_id is not None:
            result['defineId'] = self.define_id

        if self.description is not None:
            result['description'] = self.description

        if self.display_type is not None:
            result['displayType'] = self.display_type

        if self.expression_title is not None:
            result['expressionTitle'] = self.expression_title

        if self.favorite_flag is not None:
            result['favoriteFlag'] = self.favorite_flag

        if self.field_detail is not None:
            result['fieldDetail'] = self.field_detail

        if self.field_rank is not None:
            result['fieldRank'] = self.field_rank

        if self.field_source is not None:
            result['fieldSource'] = self.field_source

        if self.field_type is not None:
            result['fieldType'] = self.field_type

        if self.id is not None:
            result['id'] = self.id

        if self.input_field_type is not None:
            result['inputFieldType'] = self.input_field_type

        if self.input_required is not None:
            result['inputRequired'] = self.input_required

        if self.inputs is not None:
            result['inputs'] = self.inputs

        if self.name is not None:
            result['name'] = self.name

        if self.outlier is not None:
            result['outlier'] = self.outlier

        if self.output_threshold is not None:
            result['outputThreshold'] = self.output_threshold.to_map()

        if self.parent_name is not None:
            result['parentName'] = self.parent_name

        if self.source_type is not None:
            result['sourceType'] = self.source_type

        if self.title is not None:
            result['title'] = self.title

        if self.type is not None:
            result['type'] = self.type

        if self.variable_velocity is not None:
            result['variableVelocity'] = self.variable_velocity.to_map()

        if self.x_label is not None:
            result['xLabel'] = self.x_label

        if self.y_label is not None:
            result['yLabel'] = self.y_label

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('dataDisplay') is not None:
            self.data_display = m.get('dataDisplay')

        if m.get('defineId') is not None:
            self.define_id = m.get('defineId')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('displayType') is not None:
            self.display_type = m.get('displayType')

        if m.get('expressionTitle') is not None:
            self.expression_title = m.get('expressionTitle')

        if m.get('favoriteFlag') is not None:
            self.favorite_flag = m.get('favoriteFlag')

        if m.get('fieldDetail') is not None:
            self.field_detail = m.get('fieldDetail')

        if m.get('fieldRank') is not None:
            self.field_rank = m.get('fieldRank')

        if m.get('fieldSource') is not None:
            self.field_source = m.get('fieldSource')

        if m.get('fieldType') is not None:
            self.field_type = m.get('fieldType')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('inputFieldType') is not None:
            self.input_field_type = m.get('inputFieldType')

        if m.get('inputRequired') is not None:
            self.input_required = m.get('inputRequired')

        if m.get('inputs') is not None:
            self.inputs = m.get('inputs')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('outlier') is not None:
            self.outlier = m.get('outlier')

        if m.get('outputThreshold') is not None:
            temp_model = main_models.DescribeEventVariableListResponseBodyResultObjectQueryVariablesOutputThreshold()
            self.output_threshold = temp_model.from_map(m.get('outputThreshold'))

        if m.get('parentName') is not None:
            self.parent_name = m.get('parentName')

        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')

        if m.get('title') is not None:
            self.title = m.get('title')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('variableVelocity') is not None:
            temp_model = main_models.DescribeEventVariableListResponseBodyResultObjectQueryVariablesVariableVelocity()
            self.variable_velocity = temp_model.from_map(m.get('variableVelocity'))

        if m.get('xLabel') is not None:
            self.x_label = m.get('xLabel')

        if m.get('yLabel') is not None:
            self.y_label = m.get('yLabel')

        return self

class DescribeEventVariableListResponseBodyResultObjectQueryVariablesVariableVelocity(DaraModel):
    def __init__(
        self,
        iv: str = None,
    ):
        # The IV value. This field is not returned for this type of variable.
        self.iv = iv

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.iv is not None:
            result['iv'] = self.iv

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('iv') is not None:
            self.iv = m.get('iv')

        return self

class DescribeEventVariableListResponseBodyResultObjectQueryVariablesOutputThreshold(DaraModel):
    def __init__(
        self,
        max_value: float = None,
        min_value: float = None,
    ):
        # The maximum value.
        self.max_value = max_value
        # The minimum value.
        self.min_value = min_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_value is not None:
            result['maxValue'] = self.max_value

        if self.min_value is not None:
            result['minValue'] = self.min_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxValue') is not None:
            self.max_value = m.get('maxValue')

        if m.get('minValue') is not None:
            self.min_value = m.get('minValue')

        return self

class DescribeEventVariableListResponseBodyResultObjectNativeVariables(DaraModel):
    def __init__(
        self,
        code: str = None,
        data_display: str = None,
        define_id: str = None,
        description: str = None,
        display_type: str = None,
        expression_title: str = None,
        favorite_flag: bool = None,
        field_detail: str = None,
        field_rank: int = None,
        field_source: str = None,
        field_type: str = None,
        id: int = None,
        input_field_type: str = None,
        input_required: str = None,
        inputs: str = None,
        name: str = None,
        outlier: str = None,
        output_threshold: main_models.DescribeEventVariableListResponseBodyResultObjectNativeVariablesOutputThreshold = None,
        parent_name: str = None,
        source_type: str = None,
        title: str = None,
        type: str = None,
        variable_velocity: main_models.DescribeEventVariableListResponseBodyResultObjectNativeVariablesVariableVelocity = None,
        x_label: str = None,
        y_label: str = None,
    ):
        # variable code.
        self.code = code
        # Data distribution display, in JSON format.
        self.data_display = data_display
        # Associated variable definition ID.
        self.define_id = define_id
        # Variable description.
        self.description = description
        # Display type and group label.
        self.display_type = display_type
        # Calculate expression display value.
        self.expression_title = expression_title
        # Favorite Identifier.
        self.favorite_flag = favorite_flag
        # Field pool field details.
        self.field_detail = field_detail
        # Field Sorting.
        self.field_rank = field_rank
        # Variable source.
        self.field_source = field_source
        # Field type.
        self.field_type = field_type
        # Variable ID.
        self.id = id
        # Input field type, indicating the type of input parameters, mainly used for function categorization.
        self.input_field_type = input_field_type
        # Required parameters.
        self.input_required = input_required
        # Input of the variable. Event field is not present.
        self.inputs = inputs
        # variable name.
        self.name = name
        # outlier.
        self.outlier = outlier
        # Output score threshold.
        self.output_threshold = output_threshold
        # Parent name.
        self.parent_name = parent_name
        # Variable source type.
        self.source_type = source_type
        # Variable name.
        self.title = title
        # Variable type.
        self.type = type
        # Variable indicator information.
        self.variable_velocity = variable_velocity
        # x label.
        self.x_label = x_label
        # y label.
        self.y_label = y_label

    def validate(self):
        if self.output_threshold:
            self.output_threshold.validate()
        if self.variable_velocity:
            self.variable_velocity.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.data_display is not None:
            result['dataDisplay'] = self.data_display

        if self.define_id is not None:
            result['defineId'] = self.define_id

        if self.description is not None:
            result['description'] = self.description

        if self.display_type is not None:
            result['displayType'] = self.display_type

        if self.expression_title is not None:
            result['expressionTitle'] = self.expression_title

        if self.favorite_flag is not None:
            result['favoriteFlag'] = self.favorite_flag

        if self.field_detail is not None:
            result['fieldDetail'] = self.field_detail

        if self.field_rank is not None:
            result['fieldRank'] = self.field_rank

        if self.field_source is not None:
            result['fieldSource'] = self.field_source

        if self.field_type is not None:
            result['fieldType'] = self.field_type

        if self.id is not None:
            result['id'] = self.id

        if self.input_field_type is not None:
            result['inputFieldType'] = self.input_field_type

        if self.input_required is not None:
            result['inputRequired'] = self.input_required

        if self.inputs is not None:
            result['inputs'] = self.inputs

        if self.name is not None:
            result['name'] = self.name

        if self.outlier is not None:
            result['outlier'] = self.outlier

        if self.output_threshold is not None:
            result['outputThreshold'] = self.output_threshold.to_map()

        if self.parent_name is not None:
            result['parentName'] = self.parent_name

        if self.source_type is not None:
            result['sourceType'] = self.source_type

        if self.title is not None:
            result['title'] = self.title

        if self.type is not None:
            result['type'] = self.type

        if self.variable_velocity is not None:
            result['variableVelocity'] = self.variable_velocity.to_map()

        if self.x_label is not None:
            result['xLabel'] = self.x_label

        if self.y_label is not None:
            result['yLabel'] = self.y_label

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('dataDisplay') is not None:
            self.data_display = m.get('dataDisplay')

        if m.get('defineId') is not None:
            self.define_id = m.get('defineId')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('displayType') is not None:
            self.display_type = m.get('displayType')

        if m.get('expressionTitle') is not None:
            self.expression_title = m.get('expressionTitle')

        if m.get('favoriteFlag') is not None:
            self.favorite_flag = m.get('favoriteFlag')

        if m.get('fieldDetail') is not None:
            self.field_detail = m.get('fieldDetail')

        if m.get('fieldRank') is not None:
            self.field_rank = m.get('fieldRank')

        if m.get('fieldSource') is not None:
            self.field_source = m.get('fieldSource')

        if m.get('fieldType') is not None:
            self.field_type = m.get('fieldType')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('inputFieldType') is not None:
            self.input_field_type = m.get('inputFieldType')

        if m.get('inputRequired') is not None:
            self.input_required = m.get('inputRequired')

        if m.get('inputs') is not None:
            self.inputs = m.get('inputs')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('outlier') is not None:
            self.outlier = m.get('outlier')

        if m.get('outputThreshold') is not None:
            temp_model = main_models.DescribeEventVariableListResponseBodyResultObjectNativeVariablesOutputThreshold()
            self.output_threshold = temp_model.from_map(m.get('outputThreshold'))

        if m.get('parentName') is not None:
            self.parent_name = m.get('parentName')

        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')

        if m.get('title') is not None:
            self.title = m.get('title')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('variableVelocity') is not None:
            temp_model = main_models.DescribeEventVariableListResponseBodyResultObjectNativeVariablesVariableVelocity()
            self.variable_velocity = temp_model.from_map(m.get('variableVelocity'))

        if m.get('xLabel') is not None:
            self.x_label = m.get('xLabel')

        if m.get('yLabel') is not None:
            self.y_label = m.get('yLabel')

        return self

class DescribeEventVariableListResponseBodyResultObjectNativeVariablesVariableVelocity(DaraModel):
    def __init__(
        self,
        iv: str = None,
    ):
        # iv value.
        self.iv = iv

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.iv is not None:
            result['iv'] = self.iv

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('iv') is not None:
            self.iv = m.get('iv')

        return self

class DescribeEventVariableListResponseBodyResultObjectNativeVariablesOutputThreshold(DaraModel):
    def __init__(
        self,
        max_value: float = None,
        min_value: float = None,
    ):
        # Maximum value.
        self.max_value = max_value
        # Minimum value.
        self.min_value = min_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_value is not None:
            result['maxValue'] = self.max_value

        if self.min_value is not None:
            result['minValue'] = self.min_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxValue') is not None:
            self.max_value = m.get('maxValue')

        if m.get('minValue') is not None:
            self.min_value = m.get('minValue')

        return self

class DescribeEventVariableListResponseBodyResultObjectNativeVariableFunctions(DaraModel):
    def __init__(
        self,
        code: str = None,
        data_display: str = None,
        define_id: str = None,
        description: str = None,
        display_type: str = None,
        expression_title: str = None,
        favorite_flag: bool = None,
        field_detail: str = None,
        field_rank: int = None,
        field_source: str = None,
        field_type: str = None,
        id: int = None,
        input_field_type: str = None,
        input_required: str = None,
        inputs: str = None,
        name: str = None,
        outlier: str = None,
        output_threshold: main_models.DescribeEventVariableListResponseBodyResultObjectNativeVariableFunctionsOutputThreshold = None,
        parent_name: str = None,
        source_type: str = None,
        title: str = None,
        type: str = None,
        variable_velocity: main_models.DescribeEventVariableListResponseBodyResultObjectNativeVariableFunctionsVariableVelocity = None,
        x_label: str = None,
        y_label: str = None,
    ):
        # Variable code.
        self.code = code
        # Data distribution display in JSON format. This field is not returned for this type of variable.
        self.data_display = data_display
        # Variable definition ID. This type of variable does not return this field.
        self.define_id = define_id
        # Description information.
        self.description = description
        # Display type and group label.
        self.display_type = display_type
        # Calculate the expression display value. This field is not returned for this type of variable.
        self.expression_title = expression_title
        # Favorite identifier.
        self.favorite_flag = favorite_flag
        # Details of the field pool. This type of variable does not return this field.
        self.field_detail = field_detail
        # Field sorting.
        self.field_rank = field_rank
        # Source of the field. This type of variable does not return this field.
        self.field_source = field_source
        # Variable return type.
        self.field_type = field_type
        # Primary key ID.
        self.id = id
        # The input type of the parameter.
        self.input_field_type = input_field_type
        # Required parameter. This field is not returned for this type of variable.
        self.input_required = input_required
        # Input field. This type of variable does not return this field.
        self.inputs = inputs
        # Variable name.
        self.name = name
        # Exception value. This type of variable does not return this field.
        self.outlier = outlier
        # Output value threshold.
        self.output_threshold = output_threshold
        # Parent node. This field is not returned for this type of variable.
        self.parent_name = parent_name
        # Source type.
        self.source_type = source_type
        # Variable title.
        self.title = title
        # Variable type.
        self.type = type
        # Variable metric information. This type of variable does not return this field.
        self.variable_velocity = variable_velocity
        # x label. This type of variable does not return this field.
        self.x_label = x_label
        # y label. This type of variable does not return this field.
        self.y_label = y_label

    def validate(self):
        if self.output_threshold:
            self.output_threshold.validate()
        if self.variable_velocity:
            self.variable_velocity.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.data_display is not None:
            result['dataDisplay'] = self.data_display

        if self.define_id is not None:
            result['defineId'] = self.define_id

        if self.description is not None:
            result['description'] = self.description

        if self.display_type is not None:
            result['displayType'] = self.display_type

        if self.expression_title is not None:
            result['expressionTitle'] = self.expression_title

        if self.favorite_flag is not None:
            result['favoriteFlag'] = self.favorite_flag

        if self.field_detail is not None:
            result['fieldDetail'] = self.field_detail

        if self.field_rank is not None:
            result['fieldRank'] = self.field_rank

        if self.field_source is not None:
            result['fieldSource'] = self.field_source

        if self.field_type is not None:
            result['fieldType'] = self.field_type

        if self.id is not None:
            result['id'] = self.id

        if self.input_field_type is not None:
            result['inputFieldType'] = self.input_field_type

        if self.input_required is not None:
            result['inputRequired'] = self.input_required

        if self.inputs is not None:
            result['inputs'] = self.inputs

        if self.name is not None:
            result['name'] = self.name

        if self.outlier is not None:
            result['outlier'] = self.outlier

        if self.output_threshold is not None:
            result['outputThreshold'] = self.output_threshold.to_map()

        if self.parent_name is not None:
            result['parentName'] = self.parent_name

        if self.source_type is not None:
            result['sourceType'] = self.source_type

        if self.title is not None:
            result['title'] = self.title

        if self.type is not None:
            result['type'] = self.type

        if self.variable_velocity is not None:
            result['variableVelocity'] = self.variable_velocity.to_map()

        if self.x_label is not None:
            result['xLabel'] = self.x_label

        if self.y_label is not None:
            result['yLabel'] = self.y_label

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('dataDisplay') is not None:
            self.data_display = m.get('dataDisplay')

        if m.get('defineId') is not None:
            self.define_id = m.get('defineId')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('displayType') is not None:
            self.display_type = m.get('displayType')

        if m.get('expressionTitle') is not None:
            self.expression_title = m.get('expressionTitle')

        if m.get('favoriteFlag') is not None:
            self.favorite_flag = m.get('favoriteFlag')

        if m.get('fieldDetail') is not None:
            self.field_detail = m.get('fieldDetail')

        if m.get('fieldRank') is not None:
            self.field_rank = m.get('fieldRank')

        if m.get('fieldSource') is not None:
            self.field_source = m.get('fieldSource')

        if m.get('fieldType') is not None:
            self.field_type = m.get('fieldType')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('inputFieldType') is not None:
            self.input_field_type = m.get('inputFieldType')

        if m.get('inputRequired') is not None:
            self.input_required = m.get('inputRequired')

        if m.get('inputs') is not None:
            self.inputs = m.get('inputs')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('outlier') is not None:
            self.outlier = m.get('outlier')

        if m.get('outputThreshold') is not None:
            temp_model = main_models.DescribeEventVariableListResponseBodyResultObjectNativeVariableFunctionsOutputThreshold()
            self.output_threshold = temp_model.from_map(m.get('outputThreshold'))

        if m.get('parentName') is not None:
            self.parent_name = m.get('parentName')

        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')

        if m.get('title') is not None:
            self.title = m.get('title')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('variableVelocity') is not None:
            temp_model = main_models.DescribeEventVariableListResponseBodyResultObjectNativeVariableFunctionsVariableVelocity()
            self.variable_velocity = temp_model.from_map(m.get('variableVelocity'))

        if m.get('xLabel') is not None:
            self.x_label = m.get('xLabel')

        if m.get('yLabel') is not None:
            self.y_label = m.get('yLabel')

        return self

class DescribeEventVariableListResponseBodyResultObjectNativeVariableFunctionsVariableVelocity(DaraModel):
    def __init__(
        self,
        iv: str = None,
    ):
        # iv value. This type of variable does not return this field.
        self.iv = iv

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.iv is not None:
            result['iv'] = self.iv

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('iv') is not None:
            self.iv = m.get('iv')

        return self

class DescribeEventVariableListResponseBodyResultObjectNativeVariableFunctionsOutputThreshold(DaraModel):
    def __init__(
        self,
        max_value: float = None,
        min_value: float = None,
    ):
        # Maximum value.
        self.max_value = max_value
        # Minimum value.
        self.min_value = min_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_value is not None:
            result['maxValue'] = self.max_value

        if self.min_value is not None:
            result['minValue'] = self.min_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxValue') is not None:
            self.max_value = m.get('maxValue')

        if m.get('minValue') is not None:
            self.min_value = m.get('minValue')

        return self

class DescribeEventVariableListResponseBodyResultObjectNameList(DaraModel):
    def __init__(
        self,
        code: str = None,
        data_display: str = None,
        define_id: str = None,
        description: str = None,
        display_type: str = None,
        expression_title: str = None,
        favorite_flag: bool = None,
        field_detail: str = None,
        field_rank: int = None,
        field_source: str = None,
        field_type: str = None,
        id: int = None,
        input_field_type: str = None,
        input_required: str = None,
        inputs: str = None,
        name: str = None,
        outlier: str = None,
        output_threshold: main_models.DescribeEventVariableListResponseBodyResultObjectNameListOutputThreshold = None,
        parent_name: str = None,
        source_type: str = None,
        title: str = None,
        type: str = None,
        variable_velocity: main_models.DescribeEventVariableListResponseBodyResultObjectNameListVariableVelocity = None,
        x_label: str = None,
        y_label: str = None,
    ):
        # Variable code.
        self.code = code
        # Data distribution display in JSON format. This field is not currently returned.
        self.data_display = data_display
        # Variable definition ID. This type of variable does not return this field.
        self.define_id = define_id
        # Description information.
        self.description = description
        # Display type and group label.
        self.display_type = display_type
        # Calculate the expression display value. This type of variable does not return this field.
        self.expression_title = expression_title
        # Favorite identifier.
        self.favorite_flag = favorite_flag
        # Details of the field pool. This type of variable does not return this field.
        self.field_detail = field_detail
        # Field sorting.
        self.field_rank = field_rank
        # Source of the field. This type of variable does not return this field.
        self.field_source = field_source
        # Field type. This field is not returned for this type of variable.
        self.field_type = field_type
        # Primary key ID.
        self.id = id
        # Input type of the parameter. This field is not returned for this type of variable.
        self.input_field_type = input_field_type
        # Required parameter. This field is not returned for this type of variable.
        self.input_required = input_required
        # Input parameters. This field is not returned for this type of variable.
        self.inputs = inputs
        # Variable name.
        self.name = name
        # Outlier value. This field is not returned for this type of variable.
        self.outlier = outlier
        # Output value threshold.
        self.output_threshold = output_threshold
        # Parent node. This field is not returned currently.
        self.parent_name = parent_name
        # Source type.
        self.source_type = source_type
        # Title.
        self.title = title
        # Variable type.
        self.type = type
        # Variable metric information. This field is not returned for this type of variable.
        self.variable_velocity = variable_velocity
        # x label. This type of variable does not return this field.
        self.x_label = x_label
        # y label. This type of variable does not return this field.
        self.y_label = y_label

    def validate(self):
        if self.output_threshold:
            self.output_threshold.validate()
        if self.variable_velocity:
            self.variable_velocity.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.data_display is not None:
            result['dataDisplay'] = self.data_display

        if self.define_id is not None:
            result['defineId'] = self.define_id

        if self.description is not None:
            result['description'] = self.description

        if self.display_type is not None:
            result['displayType'] = self.display_type

        if self.expression_title is not None:
            result['expressionTitle'] = self.expression_title

        if self.favorite_flag is not None:
            result['favoriteFlag'] = self.favorite_flag

        if self.field_detail is not None:
            result['fieldDetail'] = self.field_detail

        if self.field_rank is not None:
            result['fieldRank'] = self.field_rank

        if self.field_source is not None:
            result['fieldSource'] = self.field_source

        if self.field_type is not None:
            result['fieldType'] = self.field_type

        if self.id is not None:
            result['id'] = self.id

        if self.input_field_type is not None:
            result['inputFieldType'] = self.input_field_type

        if self.input_required is not None:
            result['inputRequired'] = self.input_required

        if self.inputs is not None:
            result['inputs'] = self.inputs

        if self.name is not None:
            result['name'] = self.name

        if self.outlier is not None:
            result['outlier'] = self.outlier

        if self.output_threshold is not None:
            result['outputThreshold'] = self.output_threshold.to_map()

        if self.parent_name is not None:
            result['parentName'] = self.parent_name

        if self.source_type is not None:
            result['sourceType'] = self.source_type

        if self.title is not None:
            result['title'] = self.title

        if self.type is not None:
            result['type'] = self.type

        if self.variable_velocity is not None:
            result['variableVelocity'] = self.variable_velocity.to_map()

        if self.x_label is not None:
            result['xLabel'] = self.x_label

        if self.y_label is not None:
            result['yLabel'] = self.y_label

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('dataDisplay') is not None:
            self.data_display = m.get('dataDisplay')

        if m.get('defineId') is not None:
            self.define_id = m.get('defineId')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('displayType') is not None:
            self.display_type = m.get('displayType')

        if m.get('expressionTitle') is not None:
            self.expression_title = m.get('expressionTitle')

        if m.get('favoriteFlag') is not None:
            self.favorite_flag = m.get('favoriteFlag')

        if m.get('fieldDetail') is not None:
            self.field_detail = m.get('fieldDetail')

        if m.get('fieldRank') is not None:
            self.field_rank = m.get('fieldRank')

        if m.get('fieldSource') is not None:
            self.field_source = m.get('fieldSource')

        if m.get('fieldType') is not None:
            self.field_type = m.get('fieldType')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('inputFieldType') is not None:
            self.input_field_type = m.get('inputFieldType')

        if m.get('inputRequired') is not None:
            self.input_required = m.get('inputRequired')

        if m.get('inputs') is not None:
            self.inputs = m.get('inputs')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('outlier') is not None:
            self.outlier = m.get('outlier')

        if m.get('outputThreshold') is not None:
            temp_model = main_models.DescribeEventVariableListResponseBodyResultObjectNameListOutputThreshold()
            self.output_threshold = temp_model.from_map(m.get('outputThreshold'))

        if m.get('parentName') is not None:
            self.parent_name = m.get('parentName')

        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')

        if m.get('title') is not None:
            self.title = m.get('title')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('variableVelocity') is not None:
            temp_model = main_models.DescribeEventVariableListResponseBodyResultObjectNameListVariableVelocity()
            self.variable_velocity = temp_model.from_map(m.get('variableVelocity'))

        if m.get('xLabel') is not None:
            self.x_label = m.get('xLabel')

        if m.get('yLabel') is not None:
            self.y_label = m.get('yLabel')

        return self

class DescribeEventVariableListResponseBodyResultObjectNameListVariableVelocity(DaraModel):
    def __init__(
        self,
        iv: str = None,
    ):
        # iv value. This type of variable does not return this field.
        self.iv = iv

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.iv is not None:
            result['iv'] = self.iv

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('iv') is not None:
            self.iv = m.get('iv')

        return self

class DescribeEventVariableListResponseBodyResultObjectNameListOutputThreshold(DaraModel):
    def __init__(
        self,
        max_value: float = None,
        min_value: float = None,
    ):
        # Maximum value.
        self.max_value = max_value
        # Minimum value.
        self.min_value = min_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_value is not None:
            result['maxValue'] = self.max_value

        if self.min_value is not None:
            result['minValue'] = self.min_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxValue') is not None:
            self.max_value = m.get('maxValue')

        if m.get('minValue') is not None:
            self.min_value = m.get('minValue')

        return self

class DescribeEventVariableListResponseBodyResultObjectModelVariables(DaraModel):
    def __init__(
        self,
        code: str = None,
        data_display: str = None,
        define_id: str = None,
        description: str = None,
        display_type: str = None,
        expression_title: str = None,
        favorite_flag: bool = None,
        field_detail: str = None,
        field_rank: int = None,
        field_source: str = None,
        field_type: str = None,
        id: int = None,
        input_field_type: str = None,
        input_required: str = None,
        inputs: str = None,
        name: str = None,
        outlier: str = None,
        output_threshold: main_models.DescribeEventVariableListResponseBodyResultObjectModelVariablesOutputThreshold = None,
        parent_name: str = None,
        source_type: str = None,
        title: str = None,
        type: str = None,
        variable_velocity: main_models.DescribeEventVariableListResponseBodyResultObjectModelVariablesVariableVelocity = None,
        x_label: str = None,
        y_label: str = None,
    ):
        # The code of the model variable.
        self.code = code
        # Data distribution display, in JSON format. This field is not returned for this type of variable.
        self.data_display = data_display
        # The definition ID of the model variable. This field is not returned for this type of variable.
        self.define_id = define_id
        # The description of the model variable.
        self.description = description
        # The display type and grouping label.
        self.display_type = display_type
        # The display value of the calculation expression. This field is not returned for this type of variable.
        self.expression_title = expression_title
        # The favorite flag.
        self.favorite_flag = favorite_flag
        # The detailed information of the field in the field pool. This field is not returned for this type of variable.
        self.field_detail = field_detail
        # The field rank.
        self.field_rank = field_rank
        # The source of the field. This field is not returned for this type of variable.
        self.field_source = field_source
        # The type of the field.
        self.field_type = field_type
        # The primary key ID of the model variable.
        self.id = id
        # The input type of the parameter. This field is not returned for this type of variable.
        self.input_field_type = input_field_type
        # The required parameter. This field is not returned for this type of variable.
        self.input_required = input_required
        # Multiple input parameters separated by commas. This field is not returned for this type of variable.
        self.inputs = inputs
        # The name of the model variable.
        self.name = name
        # The outlier value. This field is not returned for this type of variable.
        self.outlier = outlier
        # The output value threshold.
        self.output_threshold = output_threshold
        # The parent node. This field is not returned for this type of variable.
        self.parent_name = parent_name
        # The source type.
        self.source_type = source_type
        # The title of the model variable.
        self.title = title
        # The type of the model variable.
        self.type = type
        # The variable metric information. This field is not returned for this type of variable.
        self.variable_velocity = variable_velocity
        # The X label. This field is not returned for this type of variable.
        self.x_label = x_label
        # The Y label. This field is not returned for this type of variable.
        self.y_label = y_label

    def validate(self):
        if self.output_threshold:
            self.output_threshold.validate()
        if self.variable_velocity:
            self.variable_velocity.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.data_display is not None:
            result['dataDisplay'] = self.data_display

        if self.define_id is not None:
            result['defineId'] = self.define_id

        if self.description is not None:
            result['description'] = self.description

        if self.display_type is not None:
            result['displayType'] = self.display_type

        if self.expression_title is not None:
            result['expressionTitle'] = self.expression_title

        if self.favorite_flag is not None:
            result['favoriteFlag'] = self.favorite_flag

        if self.field_detail is not None:
            result['fieldDetail'] = self.field_detail

        if self.field_rank is not None:
            result['fieldRank'] = self.field_rank

        if self.field_source is not None:
            result['fieldSource'] = self.field_source

        if self.field_type is not None:
            result['fieldType'] = self.field_type

        if self.id is not None:
            result['id'] = self.id

        if self.input_field_type is not None:
            result['inputFieldType'] = self.input_field_type

        if self.input_required is not None:
            result['inputRequired'] = self.input_required

        if self.inputs is not None:
            result['inputs'] = self.inputs

        if self.name is not None:
            result['name'] = self.name

        if self.outlier is not None:
            result['outlier'] = self.outlier

        if self.output_threshold is not None:
            result['outputThreshold'] = self.output_threshold.to_map()

        if self.parent_name is not None:
            result['parentName'] = self.parent_name

        if self.source_type is not None:
            result['sourceType'] = self.source_type

        if self.title is not None:
            result['title'] = self.title

        if self.type is not None:
            result['type'] = self.type

        if self.variable_velocity is not None:
            result['variableVelocity'] = self.variable_velocity.to_map()

        if self.x_label is not None:
            result['xLabel'] = self.x_label

        if self.y_label is not None:
            result['yLabel'] = self.y_label

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('dataDisplay') is not None:
            self.data_display = m.get('dataDisplay')

        if m.get('defineId') is not None:
            self.define_id = m.get('defineId')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('displayType') is not None:
            self.display_type = m.get('displayType')

        if m.get('expressionTitle') is not None:
            self.expression_title = m.get('expressionTitle')

        if m.get('favoriteFlag') is not None:
            self.favorite_flag = m.get('favoriteFlag')

        if m.get('fieldDetail') is not None:
            self.field_detail = m.get('fieldDetail')

        if m.get('fieldRank') is not None:
            self.field_rank = m.get('fieldRank')

        if m.get('fieldSource') is not None:
            self.field_source = m.get('fieldSource')

        if m.get('fieldType') is not None:
            self.field_type = m.get('fieldType')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('inputFieldType') is not None:
            self.input_field_type = m.get('inputFieldType')

        if m.get('inputRequired') is not None:
            self.input_required = m.get('inputRequired')

        if m.get('inputs') is not None:
            self.inputs = m.get('inputs')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('outlier') is not None:
            self.outlier = m.get('outlier')

        if m.get('outputThreshold') is not None:
            temp_model = main_models.DescribeEventVariableListResponseBodyResultObjectModelVariablesOutputThreshold()
            self.output_threshold = temp_model.from_map(m.get('outputThreshold'))

        if m.get('parentName') is not None:
            self.parent_name = m.get('parentName')

        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')

        if m.get('title') is not None:
            self.title = m.get('title')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('variableVelocity') is not None:
            temp_model = main_models.DescribeEventVariableListResponseBodyResultObjectModelVariablesVariableVelocity()
            self.variable_velocity = temp_model.from_map(m.get('variableVelocity'))

        if m.get('xLabel') is not None:
            self.x_label = m.get('xLabel')

        if m.get('yLabel') is not None:
            self.y_label = m.get('yLabel')

        return self

class DescribeEventVariableListResponseBodyResultObjectModelVariablesVariableVelocity(DaraModel):
    def __init__(
        self,
        iv: str = None,
    ):
        # The IV value. This field is not returned for this type of variable.
        self.iv = iv

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.iv is not None:
            result['iv'] = self.iv

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('iv') is not None:
            self.iv = m.get('iv')

        return self

class DescribeEventVariableListResponseBodyResultObjectModelVariablesOutputThreshold(DaraModel):
    def __init__(
        self,
        max_value: float = None,
        min_value: float = None,
    ):
        # The maximum value.
        self.max_value = max_value
        # The minimum value.
        self.min_value = min_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_value is not None:
            result['maxValue'] = self.max_value

        if self.min_value is not None:
            result['minValue'] = self.min_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxValue') is not None:
            self.max_value = m.get('maxValue')

        if m.get('minValue') is not None:
            self.min_value = m.get('minValue')

        return self

class DescribeEventVariableListResponseBodyResultObjectMiddleVariables(DaraModel):
    def __init__(
        self,
        code: str = None,
        data_display: str = None,
        define_id: str = None,
        description: str = None,
        display_type: str = None,
        expression_title: str = None,
        favorite_flag: bool = None,
        field_detail: str = None,
        field_rank: int = None,
        field_source: str = None,
        field_type: str = None,
        id: int = None,
        input_field_type: str = None,
        input_required: str = None,
        inputs: str = None,
        name: str = None,
        outlier: str = None,
        output_threshold: main_models.DescribeEventVariableListResponseBodyResultObjectMiddleVariablesOutputThreshold = None,
        parent_name: str = None,
        source_type: str = None,
        title: str = None,
        type: str = None,
        variable_velocity: main_models.DescribeEventVariableListResponseBodyResultObjectMiddleVariablesVariableVelocity = None,
        x_label: str = None,
        y_label: str = None,
    ):
        # Variable code.
        self.code = code
        # Data distribution display in JSON format. This field is not returned for this type of variable.
        self.data_display = data_display
        # Variable definition ID.
        self.define_id = define_id
        # Variable description.
        self.description = description
        # Display type and group label.
        self.display_type = display_type
        # Calculate the display value of the expression. This type of variable does not return this field.
        self.expression_title = expression_title
        # Favorite identifier.
        self.favorite_flag = favorite_flag
        # Details of the field pool. This type of variable does not return this field.
        self.field_detail = field_detail
        # Field sorting.
        self.field_rank = field_rank
        # Variable source.
        self.field_source = field_source
        # Field type.
        self.field_type = field_type
        # Primary key ID.
        self.id = id
        # Input field type, indicating the type of input parameters, mainly used for function classification. This type of variable does not return this field.
        self.input_field_type = input_field_type
        # Required parameter. This field is not returned for this type of variable.
        self.input_required = input_required
        # Input of the variable.
        self.inputs = inputs
        # Variable name.
        self.name = name
        # Outlier value. This field is not returned for this type of variable.
        self.outlier = outlier
        # Output value threshold.
        self.output_threshold = output_threshold
        # Parent node. This field is not returned for this type of variable.
        self.parent_name = parent_name
        # Source type.
        self.source_type = source_type
        # Title.
        self.title = title
        # Variable type.
        self.type = type
        # Variable metric information. This type of variable does not return this field.
        self.variable_velocity = variable_velocity
        # x label. This type of variable does not return this field.
        self.x_label = x_label
        # y label. This type of variable does not return this field.
        self.y_label = y_label

    def validate(self):
        if self.output_threshold:
            self.output_threshold.validate()
        if self.variable_velocity:
            self.variable_velocity.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.data_display is not None:
            result['dataDisplay'] = self.data_display

        if self.define_id is not None:
            result['defineId'] = self.define_id

        if self.description is not None:
            result['description'] = self.description

        if self.display_type is not None:
            result['displayType'] = self.display_type

        if self.expression_title is not None:
            result['expressionTitle'] = self.expression_title

        if self.favorite_flag is not None:
            result['favoriteFlag'] = self.favorite_flag

        if self.field_detail is not None:
            result['fieldDetail'] = self.field_detail

        if self.field_rank is not None:
            result['fieldRank'] = self.field_rank

        if self.field_source is not None:
            result['fieldSource'] = self.field_source

        if self.field_type is not None:
            result['fieldType'] = self.field_type

        if self.id is not None:
            result['id'] = self.id

        if self.input_field_type is not None:
            result['inputFieldType'] = self.input_field_type

        if self.input_required is not None:
            result['inputRequired'] = self.input_required

        if self.inputs is not None:
            result['inputs'] = self.inputs

        if self.name is not None:
            result['name'] = self.name

        if self.outlier is not None:
            result['outlier'] = self.outlier

        if self.output_threshold is not None:
            result['outputThreshold'] = self.output_threshold.to_map()

        if self.parent_name is not None:
            result['parentName'] = self.parent_name

        if self.source_type is not None:
            result['sourceType'] = self.source_type

        if self.title is not None:
            result['title'] = self.title

        if self.type is not None:
            result['type'] = self.type

        if self.variable_velocity is not None:
            result['variableVelocity'] = self.variable_velocity.to_map()

        if self.x_label is not None:
            result['xLabel'] = self.x_label

        if self.y_label is not None:
            result['yLabel'] = self.y_label

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('dataDisplay') is not None:
            self.data_display = m.get('dataDisplay')

        if m.get('defineId') is not None:
            self.define_id = m.get('defineId')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('displayType') is not None:
            self.display_type = m.get('displayType')

        if m.get('expressionTitle') is not None:
            self.expression_title = m.get('expressionTitle')

        if m.get('favoriteFlag') is not None:
            self.favorite_flag = m.get('favoriteFlag')

        if m.get('fieldDetail') is not None:
            self.field_detail = m.get('fieldDetail')

        if m.get('fieldRank') is not None:
            self.field_rank = m.get('fieldRank')

        if m.get('fieldSource') is not None:
            self.field_source = m.get('fieldSource')

        if m.get('fieldType') is not None:
            self.field_type = m.get('fieldType')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('inputFieldType') is not None:
            self.input_field_type = m.get('inputFieldType')

        if m.get('inputRequired') is not None:
            self.input_required = m.get('inputRequired')

        if m.get('inputs') is not None:
            self.inputs = m.get('inputs')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('outlier') is not None:
            self.outlier = m.get('outlier')

        if m.get('outputThreshold') is not None:
            temp_model = main_models.DescribeEventVariableListResponseBodyResultObjectMiddleVariablesOutputThreshold()
            self.output_threshold = temp_model.from_map(m.get('outputThreshold'))

        if m.get('parentName') is not None:
            self.parent_name = m.get('parentName')

        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')

        if m.get('title') is not None:
            self.title = m.get('title')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('variableVelocity') is not None:
            temp_model = main_models.DescribeEventVariableListResponseBodyResultObjectMiddleVariablesVariableVelocity()
            self.variable_velocity = temp_model.from_map(m.get('variableVelocity'))

        if m.get('xLabel') is not None:
            self.x_label = m.get('xLabel')

        if m.get('yLabel') is not None:
            self.y_label = m.get('yLabel')

        return self

class DescribeEventVariableListResponseBodyResultObjectMiddleVariablesVariableVelocity(DaraModel):
    def __init__(
        self,
        iv: str = None,
    ):
        # id value. This type of variable does not return this field.
        self.iv = iv

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.iv is not None:
            result['iv'] = self.iv

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('iv') is not None:
            self.iv = m.get('iv')

        return self

class DescribeEventVariableListResponseBodyResultObjectMiddleVariablesOutputThreshold(DaraModel):
    def __init__(
        self,
        max_value: float = None,
        min_value: float = None,
    ):
        # Maximum value.
        self.max_value = max_value
        # Minimum value.
        self.min_value = min_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_value is not None:
            result['maxValue'] = self.max_value

        if self.min_value is not None:
            result['minValue'] = self.min_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxValue') is not None:
            self.max_value = m.get('maxValue')

        if m.get('minValue') is not None:
            self.min_value = m.get('minValue')

        return self

class DescribeEventVariableListResponseBodyResultObjectFavoriteVariables(DaraModel):
    def __init__(
        self,
        code: str = None,
        data_display: str = None,
        define_id: str = None,
        description: str = None,
        display_type: str = None,
        expression_title: str = None,
        favorite_flag: bool = None,
        field_detail: str = None,
        field_rank: int = None,
        field_source: str = None,
        field_type: str = None,
        id: int = None,
        input_field_type: str = None,
        input_required: str = None,
        inputs: str = None,
        name: str = None,
        outlier: str = None,
        output_threshold: main_models.DescribeEventVariableListResponseBodyResultObjectFavoriteVariablesOutputThreshold = None,
        parent_name: str = None,
        source_type: str = None,
        title: str = None,
        type: str = None,
        variable_velocity: main_models.DescribeEventVariableListResponseBodyResultObjectFavoriteVariablesVariableVelocity = None,
        x_label: str = None,
        y_label: str = None,
    ):
        # Variable code.
        self.code = code
        # Data distribution display in JSON format. This field is not returned for this type of variable.
        self.data_display = data_display
        # Variable definition ID.
        self.define_id = define_id
        # Description of the variable.
        self.description = description
        # Display type and group label.
        self.display_type = display_type
        # Expression display value. This type of variable does not return this field.
        self.expression_title = expression_title
        # Favorite identifier.
        self.favorite_flag = favorite_flag
        # Details of the field pool. This type of variable does not return this field.
        self.field_detail = field_detail
        # Field sorting.
        self.field_rank = field_rank
        # Source of the field. This type of variable does not return this field.
        self.field_source = field_source
        # Field type.
        self.field_type = field_type
        # Primary key ID.
        self.id = id
        # Input type of the parameter. This field is not returned for this type of variable.
        self.input_field_type = input_field_type
        # Required parameter. This field is not returned for this type of variable.
        self.input_required = input_required
        # Input parameters should be separated by commas. Some variables may not have this field.
        self.inputs = inputs
        # Variable name.
        self.name = name
        # Anomaly value. This field is not returned for this type of variable.
        self.outlier = outlier
        # Output value threshold.
        self.output_threshold = output_threshold
        # Parent node. This field is not returned for this type of variable.
        self.parent_name = parent_name
        # Source type.
        self.source_type = source_type
        # Title.
        self.title = title
        # Variable type.
        self.type = type
        # Variable metric information. This field is not returned for this type of variable.
        self.variable_velocity = variable_velocity
        # x label. This type of variable does not return this field.
        self.x_label = x_label
        # y label. This type of variable does not return this field.
        self.y_label = y_label

    def validate(self):
        if self.output_threshold:
            self.output_threshold.validate()
        if self.variable_velocity:
            self.variable_velocity.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.data_display is not None:
            result['dataDisplay'] = self.data_display

        if self.define_id is not None:
            result['defineId'] = self.define_id

        if self.description is not None:
            result['description'] = self.description

        if self.display_type is not None:
            result['displayType'] = self.display_type

        if self.expression_title is not None:
            result['expressionTitle'] = self.expression_title

        if self.favorite_flag is not None:
            result['favoriteFlag'] = self.favorite_flag

        if self.field_detail is not None:
            result['fieldDetail'] = self.field_detail

        if self.field_rank is not None:
            result['fieldRank'] = self.field_rank

        if self.field_source is not None:
            result['fieldSource'] = self.field_source

        if self.field_type is not None:
            result['fieldType'] = self.field_type

        if self.id is not None:
            result['id'] = self.id

        if self.input_field_type is not None:
            result['inputFieldType'] = self.input_field_type

        if self.input_required is not None:
            result['inputRequired'] = self.input_required

        if self.inputs is not None:
            result['inputs'] = self.inputs

        if self.name is not None:
            result['name'] = self.name

        if self.outlier is not None:
            result['outlier'] = self.outlier

        if self.output_threshold is not None:
            result['outputThreshold'] = self.output_threshold.to_map()

        if self.parent_name is not None:
            result['parentName'] = self.parent_name

        if self.source_type is not None:
            result['sourceType'] = self.source_type

        if self.title is not None:
            result['title'] = self.title

        if self.type is not None:
            result['type'] = self.type

        if self.variable_velocity is not None:
            result['variableVelocity'] = self.variable_velocity.to_map()

        if self.x_label is not None:
            result['xLabel'] = self.x_label

        if self.y_label is not None:
            result['yLabel'] = self.y_label

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('dataDisplay') is not None:
            self.data_display = m.get('dataDisplay')

        if m.get('defineId') is not None:
            self.define_id = m.get('defineId')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('displayType') is not None:
            self.display_type = m.get('displayType')

        if m.get('expressionTitle') is not None:
            self.expression_title = m.get('expressionTitle')

        if m.get('favoriteFlag') is not None:
            self.favorite_flag = m.get('favoriteFlag')

        if m.get('fieldDetail') is not None:
            self.field_detail = m.get('fieldDetail')

        if m.get('fieldRank') is not None:
            self.field_rank = m.get('fieldRank')

        if m.get('fieldSource') is not None:
            self.field_source = m.get('fieldSource')

        if m.get('fieldType') is not None:
            self.field_type = m.get('fieldType')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('inputFieldType') is not None:
            self.input_field_type = m.get('inputFieldType')

        if m.get('inputRequired') is not None:
            self.input_required = m.get('inputRequired')

        if m.get('inputs') is not None:
            self.inputs = m.get('inputs')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('outlier') is not None:
            self.outlier = m.get('outlier')

        if m.get('outputThreshold') is not None:
            temp_model = main_models.DescribeEventVariableListResponseBodyResultObjectFavoriteVariablesOutputThreshold()
            self.output_threshold = temp_model.from_map(m.get('outputThreshold'))

        if m.get('parentName') is not None:
            self.parent_name = m.get('parentName')

        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')

        if m.get('title') is not None:
            self.title = m.get('title')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('variableVelocity') is not None:
            temp_model = main_models.DescribeEventVariableListResponseBodyResultObjectFavoriteVariablesVariableVelocity()
            self.variable_velocity = temp_model.from_map(m.get('variableVelocity'))

        if m.get('xLabel') is not None:
            self.x_label = m.get('xLabel')

        if m.get('yLabel') is not None:
            self.y_label = m.get('yLabel')

        return self

class DescribeEventVariableListResponseBodyResultObjectFavoriteVariablesVariableVelocity(DaraModel):
    def __init__(
        self,
        iv: str = None,
    ):
        # iv value. This type of variable does not return this field.
        self.iv = iv

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.iv is not None:
            result['iv'] = self.iv

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('iv') is not None:
            self.iv = m.get('iv')

        return self

class DescribeEventVariableListResponseBodyResultObjectFavoriteVariablesOutputThreshold(DaraModel):
    def __init__(
        self,
        max_value: float = None,
        min_value: float = None,
    ):
        # Maximum value.
        self.max_value = max_value
        # Minimum value.
        self.min_value = min_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_value is not None:
            result['maxValue'] = self.max_value

        if self.min_value is not None:
            result['minValue'] = self.min_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxValue') is not None:
            self.max_value = m.get('maxValue')

        if m.get('minValue') is not None:
            self.min_value = m.get('minValue')

        return self

class DescribeEventVariableListResponseBodyResultObjectExpressionVariables(DaraModel):
    def __init__(
        self,
        code: str = None,
        data_display: str = None,
        define_id: str = None,
        description: str = None,
        display_type: str = None,
        expression_title: str = None,
        favorite_flag: bool = None,
        field_detail: str = None,
        field_rank: int = None,
        field_source: str = None,
        field_type: str = None,
        id: int = None,
        input_field_type: str = None,
        input_required: str = None,
        inputs: str = None,
        name: str = None,
        outlier: str = None,
        output_threshold: main_models.DescribeEventVariableListResponseBodyResultObjectExpressionVariablesOutputThreshold = None,
        parent_name: str = None,
        source_type: str = None,
        title: str = None,
        type: str = None,
        variable_velocity: main_models.DescribeEventVariableListResponseBodyResultObjectExpressionVariablesVariableVelocity = None,
        x_label: str = None,
        y_label: str = None,
    ):
        # The code of the variable.
        self.code = code
        # Data distribution display, in JSON format. This field is not returned for this type of variable.
        self.data_display = data_display
        # The definition ID of the variable. This field is not returned for this type of variable.
        self.define_id = define_id
        # The description of the variable.
        self.description = description
        # The display type and grouping label.
        self.display_type = display_type
        # The display value of the calculation expression.
        self.expression_title = expression_title
        # The favorite flag.
        self.favorite_flag = favorite_flag
        # The detailed information of the field in the field pool. This field is not returned for this type of variable.
        self.field_detail = field_detail
        # The field rank.
        self.field_rank = field_rank
        # The source of the field. This field is not returned for this type of variable.
        self.field_source = field_source
        # The input type of the variable.
        self.field_type = field_type
        # Primary key ID.
        self.id = id
        # The input type of the parameter. This field is not returned for this type of variable.
        self.input_field_type = input_field_type
        # The required parameter. This field is not returned for this type of variable.
        self.input_required = input_required
        # Multiple input parameters separated by commas. This field is not returned for this type of variable.
        self.inputs = inputs
        # The name of the variable.
        self.name = name
        # The outlier value.
        self.outlier = outlier
        # The output value threshold.
        self.output_threshold = output_threshold
        # The parent node. This field is not returned for this type of variable.
        self.parent_name = parent_name
        # The source type.
        self.source_type = source_type
        # Title.
        self.title = title
        # The type of the variable.
        self.type = type
        # The variable metric information. This field is not returned for this type of variable.
        self.variable_velocity = variable_velocity
        # The X label. This field is not returned for this type of variable.
        self.x_label = x_label
        # The Y label. This field is not returned for this type of variable.
        self.y_label = y_label

    def validate(self):
        if self.output_threshold:
            self.output_threshold.validate()
        if self.variable_velocity:
            self.variable_velocity.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.data_display is not None:
            result['dataDisplay'] = self.data_display

        if self.define_id is not None:
            result['defineId'] = self.define_id

        if self.description is not None:
            result['description'] = self.description

        if self.display_type is not None:
            result['displayType'] = self.display_type

        if self.expression_title is not None:
            result['expressionTitle'] = self.expression_title

        if self.favorite_flag is not None:
            result['favoriteFlag'] = self.favorite_flag

        if self.field_detail is not None:
            result['fieldDetail'] = self.field_detail

        if self.field_rank is not None:
            result['fieldRank'] = self.field_rank

        if self.field_source is not None:
            result['fieldSource'] = self.field_source

        if self.field_type is not None:
            result['fieldType'] = self.field_type

        if self.id is not None:
            result['id'] = self.id

        if self.input_field_type is not None:
            result['inputFieldType'] = self.input_field_type

        if self.input_required is not None:
            result['inputRequired'] = self.input_required

        if self.inputs is not None:
            result['inputs'] = self.inputs

        if self.name is not None:
            result['name'] = self.name

        if self.outlier is not None:
            result['outlier'] = self.outlier

        if self.output_threshold is not None:
            result['outputThreshold'] = self.output_threshold.to_map()

        if self.parent_name is not None:
            result['parentName'] = self.parent_name

        if self.source_type is not None:
            result['sourceType'] = self.source_type

        if self.title is not None:
            result['title'] = self.title

        if self.type is not None:
            result['type'] = self.type

        if self.variable_velocity is not None:
            result['variableVelocity'] = self.variable_velocity.to_map()

        if self.x_label is not None:
            result['xLabel'] = self.x_label

        if self.y_label is not None:
            result['yLabel'] = self.y_label

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('dataDisplay') is not None:
            self.data_display = m.get('dataDisplay')

        if m.get('defineId') is not None:
            self.define_id = m.get('defineId')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('displayType') is not None:
            self.display_type = m.get('displayType')

        if m.get('expressionTitle') is not None:
            self.expression_title = m.get('expressionTitle')

        if m.get('favoriteFlag') is not None:
            self.favorite_flag = m.get('favoriteFlag')

        if m.get('fieldDetail') is not None:
            self.field_detail = m.get('fieldDetail')

        if m.get('fieldRank') is not None:
            self.field_rank = m.get('fieldRank')

        if m.get('fieldSource') is not None:
            self.field_source = m.get('fieldSource')

        if m.get('fieldType') is not None:
            self.field_type = m.get('fieldType')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('inputFieldType') is not None:
            self.input_field_type = m.get('inputFieldType')

        if m.get('inputRequired') is not None:
            self.input_required = m.get('inputRequired')

        if m.get('inputs') is not None:
            self.inputs = m.get('inputs')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('outlier') is not None:
            self.outlier = m.get('outlier')

        if m.get('outputThreshold') is not None:
            temp_model = main_models.DescribeEventVariableListResponseBodyResultObjectExpressionVariablesOutputThreshold()
            self.output_threshold = temp_model.from_map(m.get('outputThreshold'))

        if m.get('parentName') is not None:
            self.parent_name = m.get('parentName')

        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')

        if m.get('title') is not None:
            self.title = m.get('title')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('variableVelocity') is not None:
            temp_model = main_models.DescribeEventVariableListResponseBodyResultObjectExpressionVariablesVariableVelocity()
            self.variable_velocity = temp_model.from_map(m.get('variableVelocity'))

        if m.get('xLabel') is not None:
            self.x_label = m.get('xLabel')

        if m.get('yLabel') is not None:
            self.y_label = m.get('yLabel')

        return self

class DescribeEventVariableListResponseBodyResultObjectExpressionVariablesVariableVelocity(DaraModel):
    def __init__(
        self,
        iv: str = None,
    ):
        # The IV value. This field is not returned for this type of variable.
        self.iv = iv

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.iv is not None:
            result['iv'] = self.iv

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('iv') is not None:
            self.iv = m.get('iv')

        return self

class DescribeEventVariableListResponseBodyResultObjectExpressionVariablesOutputThreshold(DaraModel):
    def __init__(
        self,
        max_value: float = None,
        min_value: float = None,
    ):
        # The maximum value.
        self.max_value = max_value
        # The minimum value.
        self.min_value = min_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_value is not None:
            result['maxValue'] = self.max_value

        if self.min_value is not None:
            result['minValue'] = self.min_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxValue') is not None:
            self.max_value = m.get('maxValue')

        if m.get('minValue') is not None:
            self.min_value = m.get('minValue')

        return self

class DescribeEventVariableListResponseBodyResultObjectDeviceVariables(DaraModel):
    def __init__(
        self,
        code: str = None,
        data_display: str = None,
        define_id: str = None,
        description: str = None,
        display_type: str = None,
        expression_title: str = None,
        favorite_flag: bool = None,
        field_detail: str = None,
        field_rank: int = None,
        field_source: str = None,
        field_type: str = None,
        id: int = None,
        input_field_type: str = None,
        input_required: str = None,
        inputs: str = None,
        name: str = None,
        outlier: str = None,
        output_threshold: main_models.DescribeEventVariableListResponseBodyResultObjectDeviceVariablesOutputThreshold = None,
        parent_name: str = None,
        source_type: str = None,
        title: str = None,
        type: str = None,
        variable_velocity: main_models.DescribeEventVariableListResponseBodyResultObjectDeviceVariablesVariableVelocity = None,
        x_label: str = None,
        y_label: str = None,
    ):
        # Variable code.
        self.code = code
        # Data distribution display in JSON format. This field is not returned for this type of variable.
        self.data_display = data_display
        # Variable definition ID. This type of variable does not return this field.
        self.define_id = define_id
        # Description information.
        self.description = description
        # The display type and grouping label.
        self.display_type = display_type
        # The display value of the calculation expression. This field is not returned for this type of variable.
        self.expression_title = expression_title
        # The favorite flag.
        self.favorite_flag = favorite_flag
        # The detailed information of the field in the field pool. This field is not returned for this type of variable.
        self.field_detail = field_detail
        # The field rank.
        self.field_rank = field_rank
        # The source of the field. This field is not returned for this type of variable.
        self.field_source = field_source
        # Field type.
        self.field_type = field_type
        # Primary key ID.
        self.id = id
        # The input type of the parameter. This field is not returned for this type of variable.
        self.input_field_type = input_field_type
        # The required parameter. This field is not returned for this type of variable.
        self.input_required = input_required
        # Input for the variable. This field is not returned for this type of variable.
        self.inputs = inputs
        # Variable name.
        self.name = name
        # The outlier value. This field is not returned for this type of variable.
        self.outlier = outlier
        # The output value threshold.
        self.output_threshold = output_threshold
        # Parent node. This field is not returned for this type of variable.
        self.parent_name = parent_name
        # The source type.
        self.source_type = source_type
        # Title.
        self.title = title
        # Variable type.
        self.type = type
        # The variable metric information. This field is not returned for this type of variable.
        self.variable_velocity = variable_velocity
        # The X label. This field is not returned for this type of variable.
        self.x_label = x_label
        # The Y label. This field is not returned for this type of variable.
        self.y_label = y_label

    def validate(self):
        if self.output_threshold:
            self.output_threshold.validate()
        if self.variable_velocity:
            self.variable_velocity.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.data_display is not None:
            result['dataDisplay'] = self.data_display

        if self.define_id is not None:
            result['defineId'] = self.define_id

        if self.description is not None:
            result['description'] = self.description

        if self.display_type is not None:
            result['displayType'] = self.display_type

        if self.expression_title is not None:
            result['expressionTitle'] = self.expression_title

        if self.favorite_flag is not None:
            result['favoriteFlag'] = self.favorite_flag

        if self.field_detail is not None:
            result['fieldDetail'] = self.field_detail

        if self.field_rank is not None:
            result['fieldRank'] = self.field_rank

        if self.field_source is not None:
            result['fieldSource'] = self.field_source

        if self.field_type is not None:
            result['fieldType'] = self.field_type

        if self.id is not None:
            result['id'] = self.id

        if self.input_field_type is not None:
            result['inputFieldType'] = self.input_field_type

        if self.input_required is not None:
            result['inputRequired'] = self.input_required

        if self.inputs is not None:
            result['inputs'] = self.inputs

        if self.name is not None:
            result['name'] = self.name

        if self.outlier is not None:
            result['outlier'] = self.outlier

        if self.output_threshold is not None:
            result['outputThreshold'] = self.output_threshold.to_map()

        if self.parent_name is not None:
            result['parentName'] = self.parent_name

        if self.source_type is not None:
            result['sourceType'] = self.source_type

        if self.title is not None:
            result['title'] = self.title

        if self.type is not None:
            result['type'] = self.type

        if self.variable_velocity is not None:
            result['variableVelocity'] = self.variable_velocity.to_map()

        if self.x_label is not None:
            result['xLabel'] = self.x_label

        if self.y_label is not None:
            result['yLabel'] = self.y_label

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('dataDisplay') is not None:
            self.data_display = m.get('dataDisplay')

        if m.get('defineId') is not None:
            self.define_id = m.get('defineId')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('displayType') is not None:
            self.display_type = m.get('displayType')

        if m.get('expressionTitle') is not None:
            self.expression_title = m.get('expressionTitle')

        if m.get('favoriteFlag') is not None:
            self.favorite_flag = m.get('favoriteFlag')

        if m.get('fieldDetail') is not None:
            self.field_detail = m.get('fieldDetail')

        if m.get('fieldRank') is not None:
            self.field_rank = m.get('fieldRank')

        if m.get('fieldSource') is not None:
            self.field_source = m.get('fieldSource')

        if m.get('fieldType') is not None:
            self.field_type = m.get('fieldType')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('inputFieldType') is not None:
            self.input_field_type = m.get('inputFieldType')

        if m.get('inputRequired') is not None:
            self.input_required = m.get('inputRequired')

        if m.get('inputs') is not None:
            self.inputs = m.get('inputs')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('outlier') is not None:
            self.outlier = m.get('outlier')

        if m.get('outputThreshold') is not None:
            temp_model = main_models.DescribeEventVariableListResponseBodyResultObjectDeviceVariablesOutputThreshold()
            self.output_threshold = temp_model.from_map(m.get('outputThreshold'))

        if m.get('parentName') is not None:
            self.parent_name = m.get('parentName')

        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')

        if m.get('title') is not None:
            self.title = m.get('title')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('variableVelocity') is not None:
            temp_model = main_models.DescribeEventVariableListResponseBodyResultObjectDeviceVariablesVariableVelocity()
            self.variable_velocity = temp_model.from_map(m.get('variableVelocity'))

        if m.get('xLabel') is not None:
            self.x_label = m.get('xLabel')

        if m.get('yLabel') is not None:
            self.y_label = m.get('yLabel')

        return self

class DescribeEventVariableListResponseBodyResultObjectDeviceVariablesVariableVelocity(DaraModel):
    def __init__(
        self,
        iv: str = None,
    ):
        # The IV value. This field is not returned for this type of variable.
        self.iv = iv

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.iv is not None:
            result['iv'] = self.iv

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('iv') is not None:
            self.iv = m.get('iv')

        return self

class DescribeEventVariableListResponseBodyResultObjectDeviceVariablesOutputThreshold(DaraModel):
    def __init__(
        self,
        max_value: float = None,
        min_value: float = None,
    ):
        # The minimum value.
        self.max_value = max_value
        # The minimum value.
        self.min_value = min_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_value is not None:
            result['maxValue'] = self.max_value

        if self.min_value is not None:
            result['minValue'] = self.min_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxValue') is not None:
            self.max_value = m.get('maxValue')

        if m.get('minValue') is not None:
            self.min_value = m.get('minValue')

        return self

class DescribeEventVariableListResponseBodyResultObjectActions(DaraModel):
    def __init__(
        self,
        code: str = None,
        data_display: str = None,
        define_id: str = None,
        description: str = None,
        display_type: str = None,
        expression_title: str = None,
        favorite_flag: bool = None,
        field_detail: str = None,
        field_rank: int = None,
        field_source: str = None,
        field_type: str = None,
        id: int = None,
        input_field_type: str = None,
        input_required: str = None,
        inputs: str = None,
        name: str = None,
        outlier: str = None,
        output_threshold: main_models.DescribeEventVariableListResponseBodyResultObjectActionsOutputThreshold = None,
        parent_name: str = None,
        source_type: str = None,
        title: str = None,
        type: str = None,
        variable_velocity: main_models.DescribeEventVariableListResponseBodyResultObjectActionsVariableVelocity = None,
        x_label: str = None,
        y_label: str = None,
    ):
        # Variable code.
        self.code = code
        # Data distribution display in JSON format. This field is not returned for this type of variable.
        self.data_display = data_display
        # Variable definition ID. This type of variable does not return this field.
        self.define_id = define_id
        # Description information.
        self.description = description
        # Display type and group label.
        self.display_type = display_type
        # Expression display. This type of variable does not return this field.
        self.expression_title = expression_title
        # Favorite identifier.
        self.favorite_flag = favorite_flag
        # Details of the field pool. This type of variable does not return this field.
        self.field_detail = field_detail
        # Field sorting.
        self.field_rank = field_rank
        # Source of the field. This type of variable does not return this field.
        self.field_source = field_source
        # Field type. This field is not returned for this type of variable.
        self.field_type = field_type
        # Primary key ID.
        self.id = id
        # Input type of the parameter.
        self.input_field_type = input_field_type
        # Required parameter. This type of variable does not return this field.
        self.input_required = input_required
        # Input parameters. This field is not returned for this type of variable.
        self.inputs = inputs
        # Variable name.
        self.name = name
        # Anomaly value. This field is not returned for this type of variable.
        self.outlier = outlier
        # Output value threshold.
        self.output_threshold = output_threshold
        # Parent node. This field is not returned for this type of variable.
        self.parent_name = parent_name
        # Source type.
        self.source_type = source_type
        # Title.
        self.title = title
        # Variable type.
        self.type = type
        # Variable metric information. This field is not returned for this type of variable.
        self.variable_velocity = variable_velocity
        # x label. This type of variable does not return this field.
        self.x_label = x_label
        # y label. This type of variable does not return this field.
        self.y_label = y_label

    def validate(self):
        if self.output_threshold:
            self.output_threshold.validate()
        if self.variable_velocity:
            self.variable_velocity.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.data_display is not None:
            result['dataDisplay'] = self.data_display

        if self.define_id is not None:
            result['defineId'] = self.define_id

        if self.description is not None:
            result['description'] = self.description

        if self.display_type is not None:
            result['displayType'] = self.display_type

        if self.expression_title is not None:
            result['expressionTitle'] = self.expression_title

        if self.favorite_flag is not None:
            result['favoriteFlag'] = self.favorite_flag

        if self.field_detail is not None:
            result['fieldDetail'] = self.field_detail

        if self.field_rank is not None:
            result['fieldRank'] = self.field_rank

        if self.field_source is not None:
            result['fieldSource'] = self.field_source

        if self.field_type is not None:
            result['fieldType'] = self.field_type

        if self.id is not None:
            result['id'] = self.id

        if self.input_field_type is not None:
            result['inputFieldType'] = self.input_field_type

        if self.input_required is not None:
            result['inputRequired'] = self.input_required

        if self.inputs is not None:
            result['inputs'] = self.inputs

        if self.name is not None:
            result['name'] = self.name

        if self.outlier is not None:
            result['outlier'] = self.outlier

        if self.output_threshold is not None:
            result['outputThreshold'] = self.output_threshold.to_map()

        if self.parent_name is not None:
            result['parentName'] = self.parent_name

        if self.source_type is not None:
            result['sourceType'] = self.source_type

        if self.title is not None:
            result['title'] = self.title

        if self.type is not None:
            result['type'] = self.type

        if self.variable_velocity is not None:
            result['variableVelocity'] = self.variable_velocity.to_map()

        if self.x_label is not None:
            result['xLabel'] = self.x_label

        if self.y_label is not None:
            result['yLabel'] = self.y_label

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('dataDisplay') is not None:
            self.data_display = m.get('dataDisplay')

        if m.get('defineId') is not None:
            self.define_id = m.get('defineId')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('displayType') is not None:
            self.display_type = m.get('displayType')

        if m.get('expressionTitle') is not None:
            self.expression_title = m.get('expressionTitle')

        if m.get('favoriteFlag') is not None:
            self.favorite_flag = m.get('favoriteFlag')

        if m.get('fieldDetail') is not None:
            self.field_detail = m.get('fieldDetail')

        if m.get('fieldRank') is not None:
            self.field_rank = m.get('fieldRank')

        if m.get('fieldSource') is not None:
            self.field_source = m.get('fieldSource')

        if m.get('fieldType') is not None:
            self.field_type = m.get('fieldType')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('inputFieldType') is not None:
            self.input_field_type = m.get('inputFieldType')

        if m.get('inputRequired') is not None:
            self.input_required = m.get('inputRequired')

        if m.get('inputs') is not None:
            self.inputs = m.get('inputs')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('outlier') is not None:
            self.outlier = m.get('outlier')

        if m.get('outputThreshold') is not None:
            temp_model = main_models.DescribeEventVariableListResponseBodyResultObjectActionsOutputThreshold()
            self.output_threshold = temp_model.from_map(m.get('outputThreshold'))

        if m.get('parentName') is not None:
            self.parent_name = m.get('parentName')

        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')

        if m.get('title') is not None:
            self.title = m.get('title')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('variableVelocity') is not None:
            temp_model = main_models.DescribeEventVariableListResponseBodyResultObjectActionsVariableVelocity()
            self.variable_velocity = temp_model.from_map(m.get('variableVelocity'))

        if m.get('xLabel') is not None:
            self.x_label = m.get('xLabel')

        if m.get('yLabel') is not None:
            self.y_label = m.get('yLabel')

        return self

class DescribeEventVariableListResponseBodyResultObjectActionsVariableVelocity(DaraModel):
    def __init__(
        self,
        iv: str = None,
    ):
        # iv value. This type of variable does not return this field.
        self.iv = iv

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.iv is not None:
            result['iv'] = self.iv

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('iv') is not None:
            self.iv = m.get('iv')

        return self

class DescribeEventVariableListResponseBodyResultObjectActionsOutputThreshold(DaraModel):
    def __init__(
        self,
        max_value: float = None,
        min_value: float = None,
    ):
        # Maximum value.
        self.max_value = max_value
        # Minimum value.
        self.min_value = min_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_value is not None:
            result['maxValue'] = self.max_value

        if self.min_value is not None:
            result['minValue'] = self.min_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxValue') is not None:
            self.max_value = m.get('maxValue')

        if m.get('minValue') is not None:
            self.min_value = m.get('minValue')

        return self

