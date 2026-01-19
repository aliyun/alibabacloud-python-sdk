# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_xtee20210910 import models as main_models
from darabonba.model import DaraModel

class DescribeVariableDetailResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result_object: main_models.DescribeVariableDetailResponseBodyResultObject = None,
    ):
        # Request ID.
        self.request_id = request_id
        # Return object
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
            temp_model = main_models.DescribeVariableDetailResponseBodyResultObject()
            self.result_object = temp_model.from_map(m.get('resultObject'))

        return self

class DescribeVariableDetailResponseBodyResultObject(DaraModel):
    def __init__(
        self,
        base_info: main_models.DescribeVariableDetailResponseBodyResultObjectBaseInfo = None,
    ):
        # Basic attributes.
        self.base_info = base_info

    def validate(self):
        if self.base_info:
            self.base_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.base_info is not None:
            result['baseInfo'] = self.base_info.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('baseInfo') is not None:
            temp_model = main_models.DescribeVariableDetailResponseBodyResultObjectBaseInfo()
            self.base_info = temp_model.from_map(m.get('baseInfo'))

        return self

class DescribeVariableDetailResponseBodyResultObjectBaseInfo(DaraModel):
    def __init__(
        self,
        allow_bind: str = None,
        charging_mode: str = None,
        charging_mode_desc: str = None,
        creator: str = None,
        data_display: str = None,
        data_threshold: str = None,
        deduction_factor: int = None,
        description: str = None,
        front_allow_bind: str = None,
        gmt_create: int = None,
        gmt_modified: int = None,
        id: int = None,
        input_required: str = None,
        inputs: str = None,
        inputs_desc: str = None,
        invoke_key: str = None,
        invoke_rt: int = None,
        invoke_success_rate: str = None,
        invoke_times: int = None,
        last_modified_operator: str = None,
        name: str = None,
        outputs: str = None,
        outputs_desc: str = None,
        scene: List[str] = None,
        scene_desc: List[str] = None,
        show_order: str = None,
        source: str = None,
        source_desc: str = None,
        status: str = None,
        support_regions: List[str] = None,
        title: str = None,
        type: str = None,
        type_desc: str = None,
        x_label: str = None,
        y_label: str = None,
    ):
        # Whether variable binding is allowed
        self.allow_bind = allow_bind
        # Charging mode
        self.charging_mode = charging_mode
        # Charging mode description
        self.charging_mode_desc = charging_mode_desc
        # Creator.
        self.creator = creator
        # Data distribution display, in JSON format
        self.data_display = data_display
        # Data valid range, left-closed and right-closed
        self.data_threshold = data_threshold
        # Deduction factor
        self.deduction_factor = deduction_factor
        # Description.
        self.description = description
        # Front-end binding allowed
        self.front_allow_bind = front_allow_bind
        # Creation time.
        self.gmt_create = gmt_create
        # Modification time.
        self.gmt_modified = gmt_modified
        # Primary key ID
        self.id = id
        # Required parameters
        #      
        #      When inputRequired=__all__, it means all parameters are required
        #      When inputRequired=__one__, it means only one input is needed
        #      Required fields are separated by commas, e.g., mobile,ip,email
        self.input_required = input_required
        # Input parameters.
        self.inputs = inputs
        # Input parameter description.
        self.inputs_desc = inputs_desc
        # Invoke key
        self.invoke_key = invoke_key
        # Invoke RT, unit: milliseconds
        self.invoke_rt = invoke_rt
        # Invocation success rate
        self.invoke_success_rate = invoke_success_rate
        # Number of invocations
        self.invoke_times = invoke_times
        # Last modifier.
        self.last_modified_operator = last_modified_operator
        # Variable name
        self.name = name
        # Output
        self.outputs = outputs
        # Output description
        self.outputs_desc = outputs_desc
        # Code of applicable scenarios
        self.scene = scene
        # Applicable scenario description
        self.scene_desc = scene_desc
        # Display order
        self.show_order = show_order
        # Source
        self.source = source
        # Source description
        self.source_desc = source_desc
        # Status.
        self.status = status
        # List of supported regions.
        self.support_regions = support_regions
        # Title.
        self.title = title
        # Type
        self.type = type
        # Category description
        self.type_desc = type_desc
        # X-axis label for data distribution display
        self.x_label = x_label
        # Data distribution display y-axis label
        self.y_label = y_label

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allow_bind is not None:
            result['allowBind'] = self.allow_bind

        if self.charging_mode is not None:
            result['chargingMode'] = self.charging_mode

        if self.charging_mode_desc is not None:
            result['chargingModeDesc'] = self.charging_mode_desc

        if self.creator is not None:
            result['creator'] = self.creator

        if self.data_display is not None:
            result['dataDisplay'] = self.data_display

        if self.data_threshold is not None:
            result['dataThreshold'] = self.data_threshold

        if self.deduction_factor is not None:
            result['deductionFactor'] = self.deduction_factor

        if self.description is not None:
            result['description'] = self.description

        if self.front_allow_bind is not None:
            result['frontAllowBind'] = self.front_allow_bind

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        if self.id is not None:
            result['id'] = self.id

        if self.input_required is not None:
            result['inputRequired'] = self.input_required

        if self.inputs is not None:
            result['inputs'] = self.inputs

        if self.inputs_desc is not None:
            result['inputsDesc'] = self.inputs_desc

        if self.invoke_key is not None:
            result['invokeKey'] = self.invoke_key

        if self.invoke_rt is not None:
            result['invokeRt'] = self.invoke_rt

        if self.invoke_success_rate is not None:
            result['invokeSuccessRate'] = self.invoke_success_rate

        if self.invoke_times is not None:
            result['invokeTimes'] = self.invoke_times

        if self.last_modified_operator is not None:
            result['lastModifiedOperator'] = self.last_modified_operator

        if self.name is not None:
            result['name'] = self.name

        if self.outputs is not None:
            result['outputs'] = self.outputs

        if self.outputs_desc is not None:
            result['outputsDesc'] = self.outputs_desc

        if self.scene is not None:
            result['scene'] = self.scene

        if self.scene_desc is not None:
            result['sceneDesc'] = self.scene_desc

        if self.show_order is not None:
            result['showOrder'] = self.show_order

        if self.source is not None:
            result['source'] = self.source

        if self.source_desc is not None:
            result['sourceDesc'] = self.source_desc

        if self.status is not None:
            result['status'] = self.status

        if self.support_regions is not None:
            result['supportRegions'] = self.support_regions

        if self.title is not None:
            result['title'] = self.title

        if self.type is not None:
            result['type'] = self.type

        if self.type_desc is not None:
            result['typeDesc'] = self.type_desc

        if self.x_label is not None:
            result['xLabel'] = self.x_label

        if self.y_label is not None:
            result['yLabel'] = self.y_label

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('allowBind') is not None:
            self.allow_bind = m.get('allowBind')

        if m.get('chargingMode') is not None:
            self.charging_mode = m.get('chargingMode')

        if m.get('chargingModeDesc') is not None:
            self.charging_mode_desc = m.get('chargingModeDesc')

        if m.get('creator') is not None:
            self.creator = m.get('creator')

        if m.get('dataDisplay') is not None:
            self.data_display = m.get('dataDisplay')

        if m.get('dataThreshold') is not None:
            self.data_threshold = m.get('dataThreshold')

        if m.get('deductionFactor') is not None:
            self.deduction_factor = m.get('deductionFactor')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('frontAllowBind') is not None:
            self.front_allow_bind = m.get('frontAllowBind')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('inputRequired') is not None:
            self.input_required = m.get('inputRequired')

        if m.get('inputs') is not None:
            self.inputs = m.get('inputs')

        if m.get('inputsDesc') is not None:
            self.inputs_desc = m.get('inputsDesc')

        if m.get('invokeKey') is not None:
            self.invoke_key = m.get('invokeKey')

        if m.get('invokeRt') is not None:
            self.invoke_rt = m.get('invokeRt')

        if m.get('invokeSuccessRate') is not None:
            self.invoke_success_rate = m.get('invokeSuccessRate')

        if m.get('invokeTimes') is not None:
            self.invoke_times = m.get('invokeTimes')

        if m.get('lastModifiedOperator') is not None:
            self.last_modified_operator = m.get('lastModifiedOperator')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('outputs') is not None:
            self.outputs = m.get('outputs')

        if m.get('outputsDesc') is not None:
            self.outputs_desc = m.get('outputsDesc')

        if m.get('scene') is not None:
            self.scene = m.get('scene')

        if m.get('sceneDesc') is not None:
            self.scene_desc = m.get('sceneDesc')

        if m.get('showOrder') is not None:
            self.show_order = m.get('showOrder')

        if m.get('source') is not None:
            self.source = m.get('source')

        if m.get('sourceDesc') is not None:
            self.source_desc = m.get('sourceDesc')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('supportRegions') is not None:
            self.support_regions = m.get('supportRegions')

        if m.get('title') is not None:
            self.title = m.get('title')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('typeDesc') is not None:
            self.type_desc = m.get('typeDesc')

        if m.get('xLabel') is not None:
            self.x_label = m.get('xLabel')

        if m.get('yLabel') is not None:
            self.y_label = m.get('yLabel')

        return self

