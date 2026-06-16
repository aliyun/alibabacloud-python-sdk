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
        # The request ID.
        self.request_id = request_id
        # The returned object.
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
        # The basic properties.
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
        # Specifies whether variable binding is allowed. Valid values:
        # - **DISABLE**: unavailable
        # - **ALL**: all
        # - **ENABLE**: available
        # - **PART_ENABLE**: partially available.
        self.allow_bind = allow_bind
        # The billing mode. Valid values:
        # - **PAY_PER_VIEW**: paid
        # - **FREE**: free.
        self.charging_mode = charging_mode
        # The billing mode description.
        self.charging_mode_desc = charging_mode_desc
        # The creator.
        self.creator = creator
        # The data distribution display in JSON format.
        self.data_display = data_display
        # The valid data range, inclusive on both ends.
        self.data_threshold = data_threshold
        # The deduction coefficient.
        self.deduction_factor = deduction_factor
        # The description.
        self.description = description
        # Specifies whether front-end binding is allowed. Valid values:
        # - **DISABLE**: not allowed
        # - **ENABLE**: allowed.
        self.front_allow_bind = front_allow_bind
        # The creation time.
        self.gmt_create = gmt_create
        # The modification time.
        self.gmt_modified = gmt_modified
        # The primary key ID.
        self.id = id
        # The required parameters.
        #      
        # When inputRequired is set to __all__, all parameters are required.
        # When inputRequired is set to __one__, only one input parameter is required.
        # Required fields are separated by commas, such as mobile,ip,email.
        self.input_required = input_required
        # The input parameters.
        self.inputs = inputs
        # The input parameter description.
        self.inputs_desc = inputs_desc
        # The invocation key.
        self.invoke_key = invoke_key
        # The invocation response time, in milliseconds.
        self.invoke_rt = invoke_rt
        # The invocation success rate.
        self.invoke_success_rate = invoke_success_rate
        # The number of invocations.
        self.invoke_times = invoke_times
        # The last modifier.
        self.last_modified_operator = last_modified_operator
        # The variable name.
        self.name = name
        # The outputs.
        self.outputs = outputs
        # The output description.
        self.outputs_desc = outputs_desc
        # The applicable scenario code.
        self.scene = scene
        # The applicable scenario description.
        self.scene_desc = scene_desc
        # The display order.
        self.show_order = show_order
        # The source.
        self.source = source
        # The source description.
        self.source_desc = source_desc
        # The status.
        self.status = status
        # The list of supported regions.
        self.support_regions = support_regions
        # The title.
        self.title = title
        # The type.
        self.type = type
        # The category description.
        self.type_desc = type_desc
        # The X-axis label for the data distribution chart.
        self.x_label = x_label
        # The Y-axis label for the data distribution chart.
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

