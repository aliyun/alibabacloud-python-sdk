# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict


class OrderStepRestriction(TeaModel):
    def __init__(
        self,
        label: str = None,
        value: str = None,
    ):
        # 步骤标题
        self.label = label
        # 步骤名
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.label is not None:
            result['Label'] = self.label
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class OrderStep(TeaModel):
    def __init__(
        self,
        display_method: str = None,
        gmt_create: str = None,
        gmt_modify: str = None,
        job_kwargs: str = None,
        job_message: str = None,
        job_return_status: str = None,
        job_return_values: str = None,
        job_system: str = None,
        order_id: str = None,
        order_step_id: str = None,
        real_next_step: str = None,
        restriction: List[OrderStepRestriction] = None,
        step_name: str = None,
        step_status: str = None,
        step_title: str = None,
        step_type: str = None,
    ):
        # 步骤展示方式
        self.display_method = display_method
        # 创建时间
        self.gmt_create = gmt_create
        # 修改时间
        self.gmt_modify = gmt_modify
        # 步骤任务参数
        self.job_kwargs = job_kwargs
        # 步骤标题
        self.job_message = job_message
        # 步骤标题
        self.job_return_status = job_return_status
        # 步骤任务返回
        self.job_return_values = job_return_values
        # 步骤任务系统
        self.job_system = job_system
        # 工单id
        self.order_id = order_id
        # 工单步骤id
        self.order_step_id = order_step_id
        # 下一步步骤名
        self.real_next_step = real_next_step
        # 下一步步骤可选列表
        self.restriction = restriction
        # 步骤名
        self.step_name = step_name
        # 步骤状态
        self.step_status = step_status
        # 步骤标题
        self.step_title = step_title
        # 步骤类型
        self.step_type = step_type

    def validate(self):
        if self.restriction:
            for k in self.restriction:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.display_method is not None:
            result['DisplayMethod'] = self.display_method
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modify is not None:
            result['GmtModify'] = self.gmt_modify
        if self.job_kwargs is not None:
            result['JobKwargs'] = self.job_kwargs
        if self.job_message is not None:
            result['JobMessage'] = self.job_message
        if self.job_return_status is not None:
            result['JobReturnStatus'] = self.job_return_status
        if self.job_return_values is not None:
            result['JobReturnValues'] = self.job_return_values
        if self.job_system is not None:
            result['JobSystem'] = self.job_system
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.order_step_id is not None:
            result['OrderStepId'] = self.order_step_id
        if self.real_next_step is not None:
            result['RealNextStep'] = self.real_next_step
        result['Restriction'] = []
        if self.restriction is not None:
            for k in self.restriction:
                result['Restriction'].append(k.to_map() if k else None)
        if self.step_name is not None:
            result['StepName'] = self.step_name
        if self.step_status is not None:
            result['StepStatus'] = self.step_status
        if self.step_title is not None:
            result['StepTitle'] = self.step_title
        if self.step_type is not None:
            result['StepType'] = self.step_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayMethod') is not None:
            self.display_method = m.get('DisplayMethod')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModify') is not None:
            self.gmt_modify = m.get('GmtModify')
        if m.get('JobKwargs') is not None:
            self.job_kwargs = m.get('JobKwargs')
        if m.get('JobMessage') is not None:
            self.job_message = m.get('JobMessage')
        if m.get('JobReturnStatus') is not None:
            self.job_return_status = m.get('JobReturnStatus')
        if m.get('JobReturnValues') is not None:
            self.job_return_values = m.get('JobReturnValues')
        if m.get('JobSystem') is not None:
            self.job_system = m.get('JobSystem')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('OrderStepId') is not None:
            self.order_step_id = m.get('OrderStepId')
        if m.get('RealNextStep') is not None:
            self.real_next_step = m.get('RealNextStep')
        self.restriction = []
        if m.get('Restriction') is not None:
            for k in m.get('Restriction'):
                temp_model = OrderStepRestriction()
                self.restriction.append(temp_model.from_map(k))
        if m.get('StepName') is not None:
            self.step_name = m.get('StepName')
        if m.get('StepStatus') is not None:
            self.step_status = m.get('StepStatus')
        if m.get('StepTitle') is not None:
            self.step_title = m.get('StepTitle')
        if m.get('StepType') is not None:
            self.step_type = m.get('StepType')
        return self


class DeviceFormProperty(TeaModel):
    def __init__(
        self,
        content: str = None,
        keyword: str = None,
        placeholder: bool = None,
        required: bool = None,
        search_supported: bool = None,
        sequence: int = None,
        table_visible: bool = None,
        uniqueness: bool = None,
        value_reference: str = None,
        value_source: str = None,
        value_type: str = None,
    ):
        # 属性描述
        self.content = content
        # 属性关键词
        self.keyword = keyword
        # 前端界面控件占位符文字
        self.placeholder = placeholder
        # 属性是否必填
        self.required = required
        # 属性是否作为界面查询条件
        self.search_supported = search_supported
        # 属性展示的次序
        self.sequence = sequence
        # 前端界面是否展示为表格列
        self.table_visible = table_visible
        # 属性是否需要唯一检查
        self.uniqueness = uniqueness
        # 属性值来源具体的方式
        self.value_reference = value_reference
        # 属性值来源类型：枚举、接口等
        self.value_source = value_source
        # 属性类型，JSON或者分隔符
        self.value_type = value_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.placeholder is not None:
            result['Placeholder'] = self.placeholder
        if self.required is not None:
            result['Required'] = self.required
        if self.search_supported is not None:
            result['SearchSupported'] = self.search_supported
        if self.sequence is not None:
            result['Sequence'] = self.sequence
        if self.table_visible is not None:
            result['TableVisible'] = self.table_visible
        if self.uniqueness is not None:
            result['Uniqueness'] = self.uniqueness
        if self.value_reference is not None:
            result['ValueReference'] = self.value_reference
        if self.value_source is not None:
            result['ValueSource'] = self.value_source
        if self.value_type is not None:
            result['ValueType'] = self.value_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('Placeholder') is not None:
            self.placeholder = m.get('Placeholder')
        if m.get('Required') is not None:
            self.required = m.get('Required')
        if m.get('SearchSupported') is not None:
            self.search_supported = m.get('SearchSupported')
        if m.get('Sequence') is not None:
            self.sequence = m.get('Sequence')
        if m.get('TableVisible') is not None:
            self.table_visible = m.get('TableVisible')
        if m.get('Uniqueness') is not None:
            self.uniqueness = m.get('Uniqueness')
        if m.get('ValueReference') is not None:
            self.value_reference = m.get('ValueReference')
        if m.get('ValueSource') is not None:
            self.value_source = m.get('ValueSource')
        if m.get('ValueType') is not None:
            self.value_type = m.get('ValueType')
        return self


class DeviceForm(TeaModel):
    def __init__(
        self,
        account_config: str = None,
        config_compare: str = None,
        form_id: str = None,
        form_name: str = None,
        properties_list: List[DeviceFormProperty] = None,
    ):
        # 是否需要配置账号信息
        self.account_config = account_config
        # 是否需要展示配置备份
        self.config_compare = config_compare
        # 设备形态ID
        self.form_id = form_id
        # 设备形态名称
        self.form_name = form_name
        # 设备形态属性列表
        self.properties_list = properties_list

    def validate(self):
        if self.properties_list:
            for k in self.properties_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.account_config is not None:
            result['AccountConfig'] = self.account_config
        if self.config_compare is not None:
            result['ConfigCompare'] = self.config_compare
        if self.form_id is not None:
            result['FormId'] = self.form_id
        if self.form_name is not None:
            result['FormName'] = self.form_name
        result['PropertiesList'] = []
        if self.properties_list is not None:
            for k in self.properties_list:
                result['PropertiesList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountConfig') is not None:
            self.account_config = m.get('AccountConfig')
        if m.get('ConfigCompare') is not None:
            self.config_compare = m.get('ConfigCompare')
        if m.get('FormId') is not None:
            self.form_id = m.get('FormId')
        if m.get('FormName') is not None:
            self.form_name = m.get('FormName')
        self.properties_list = []
        if m.get('PropertiesList') is not None:
            for k in m.get('PropertiesList'):
                temp_model = DeviceFormProperty()
                self.properties_list.append(temp_model.from_map(k))
        return self


class Task(TeaModel):
    def __init__(
        self,
        category: str = None,
        gmt_create: str = None,
        gmt_modify: str = None,
        params: str = None,
        response_code: str = None,
        result: str = None,
        status: str = None,
        task_id: str = None,
        template_id: str = None,
        template_name: str = None,
    ):
        # 模板类别
        self.category = category
        # 创建时间
        self.gmt_create = gmt_create
        # 修改时间
        self.gmt_modify = gmt_modify
        # 任务参数
        self.params = params
        # 任务错误码
        self.response_code = response_code
        # 任务返回
        self.result = result
        # 任务状态
        self.status = status
        # 任务id
        self.task_id = task_id
        # 模板id
        self.template_id = template_id
        # 模板名称
        self.template_name = template_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modify is not None:
            result['GmtModify'] = self.gmt_modify
        if self.params is not None:
            result['Params'] = self.params
        if self.response_code is not None:
            result['ResponseCode'] = self.response_code
        if self.result is not None:
            result['Result'] = self.result
        if self.status is not None:
            result['Status'] = self.status
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModify') is not None:
            self.gmt_modify = m.get('GmtModify')
        if m.get('Params') is not None:
            self.params = m.get('Params')
        if m.get('ResponseCode') is not None:
            self.response_code = m.get('ResponseCode')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        return self


class SchemeInput(TeaModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        sample: str = None,
        type: str = None,
    ):
        # 参数说明
        self.description = description
        # 参数名称
        self.name = name
        # 参数示例
        self.sample = sample
        # 参数类型
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.sample is not None:
            result['Sample'] = self.sample
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Sample') is not None:
            self.sample = m.get('Sample')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class SchemeOutput(TeaModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        sample: str = None,
        type: str = None,
    ):
        # 参数说明
        self.description = description
        # 参数名称
        self.name = name
        # 参数示例
        self.sample = sample
        # 参数类型
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.sample is not None:
            result['Sample'] = self.sample
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Sample') is not None:
            self.sample = m.get('Sample')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class Scheme(TeaModel):
    def __init__(
        self,
        category: str = None,
        content: str = None,
        description: str = None,
        gmt_create: str = None,
        gmt_modify: str = None,
        input: List[SchemeInput] = None,
        output: List[SchemeOutput] = None,
        scheme_id: str = None,
        scheme_name: str = None,
        status: str = None,
        view: str = None,
    ):
        # 方案类型
        self.category = category
        # 方案内容
        self.content = content
        # 方案说明
        self.description = description
        # 创建时间
        self.gmt_create = gmt_create
        # 修改时间
        self.gmt_modify = gmt_modify
        # 方案入参
        self.input = input
        # 方案出参
        self.output = output
        # 方案id
        self.scheme_id = scheme_id
        # 方案名称
        self.scheme_name = scheme_name
        # 方案状态
        self.status = status
        # 方案展示
        self.view = view

    def validate(self):
        if self.input:
            for k in self.input:
                if k:
                    k.validate()
        if self.output:
            for k in self.output:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.content is not None:
            result['Content'] = self.content
        if self.description is not None:
            result['Description'] = self.description
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modify is not None:
            result['GmtModify'] = self.gmt_modify
        result['Input'] = []
        if self.input is not None:
            for k in self.input:
                result['Input'].append(k.to_map() if k else None)
        result['Output'] = []
        if self.output is not None:
            for k in self.output:
                result['Output'].append(k.to_map() if k else None)
        if self.scheme_id is not None:
            result['SchemeId'] = self.scheme_id
        if self.scheme_name is not None:
            result['SchemeName'] = self.scheme_name
        if self.status is not None:
            result['Status'] = self.status
        if self.view is not None:
            result['View'] = self.view
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModify') is not None:
            self.gmt_modify = m.get('GmtModify')
        self.input = []
        if m.get('Input') is not None:
            for k in m.get('Input'):
                temp_model = SchemeInput()
                self.input.append(temp_model.from_map(k))
        self.output = []
        if m.get('Output') is not None:
            for k in m.get('Output'):
                temp_model = SchemeOutput()
                self.output.append(temp_model.from_map(k))
        if m.get('SchemeId') is not None:
            self.scheme_id = m.get('SchemeId')
        if m.get('SchemeName') is not None:
            self.scheme_name = m.get('SchemeName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('View') is not None:
            self.view = m.get('View')
        return self


class AggregateData(TeaModel):
    def __init__(
        self,
        gmt_create: str = None,
        gmt_modified: str = None,
        data_item: str = None,
        device_id_list: List[str] = None,
        aggregate_mode_list: List[str] = None,
        aggregate_data_name: str = None,
        aggregate_data_description: str = None,
        is_all_device: int = None,
        monitor_item_id: str = None,
        aggregate_data_id: str = None,
    ):
        # 创建时间
        self.gmt_create = gmt_create
        # 修改时间
        self.gmt_modified = gmt_modified
        # 数据项
        self.data_item = data_item
        # 聚合设备ID列表
        self.device_id_list = device_id_list
        # 聚合方式列表
        self.aggregate_mode_list = aggregate_mode_list
        # 聚合数据名称
        self.aggregate_data_name = aggregate_data_name
        # 描述
        self.aggregate_data_description = aggregate_data_description
        # 是否聚合全部设备
        self.is_all_device = is_all_device
        # 监控项ID
        self.monitor_item_id = monitor_item_id
        # 聚合数据ID
        self.aggregate_data_id = aggregate_data_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.data_item is not None:
            result['DataItem'] = self.data_item
        if self.device_id_list is not None:
            result['DeviceIdList'] = self.device_id_list
        if self.aggregate_mode_list is not None:
            result['AggregateModeList'] = self.aggregate_mode_list
        if self.aggregate_data_name is not None:
            result['AggregateDataName'] = self.aggregate_data_name
        if self.aggregate_data_description is not None:
            result['AggregateDataDescription'] = self.aggregate_data_description
        if self.is_all_device is not None:
            result['IsAllDevice'] = self.is_all_device
        if self.monitor_item_id is not None:
            result['MonitorItemId'] = self.monitor_item_id
        if self.aggregate_data_id is not None:
            result['AggregateDataId'] = self.aggregate_data_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('DataItem') is not None:
            self.data_item = m.get('DataItem')
        if m.get('DeviceIdList') is not None:
            self.device_id_list = m.get('DeviceIdList')
        if m.get('AggregateModeList') is not None:
            self.aggregate_mode_list = m.get('AggregateModeList')
        if m.get('AggregateDataName') is not None:
            self.aggregate_data_name = m.get('AggregateDataName')
        if m.get('AggregateDataDescription') is not None:
            self.aggregate_data_description = m.get('AggregateDataDescription')
        if m.get('IsAllDevice') is not None:
            self.is_all_device = m.get('IsAllDevice')
        if m.get('MonitorItemId') is not None:
            self.monitor_item_id = m.get('MonitorItemId')
        if m.get('AggregateDataId') is not None:
            self.aggregate_data_id = m.get('AggregateDataId')
        return self


class Port(TeaModel):
    def __init__(
        self,
        device_id: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        port_collection_id: str = None,
        port_name: str = None,
    ):
        # 设备ID
        self.device_id = device_id
        # 创建时间
        self.gmt_create = gmt_create
        # 修改时间
        self.gmt_modified = gmt_modified
        # 端口集ID
        self.port_collection_id = port_collection_id
        # 端口名称
        self.port_name = port_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.port_collection_id is not None:
            result['PortCollectionId'] = self.port_collection_id
        if self.port_name is not None:
            result['PortName'] = self.port_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('PortCollectionId') is not None:
            self.port_collection_id = m.get('PortCollectionId')
        if m.get('PortName') is not None:
            self.port_name = m.get('PortName')
        return self


class TaskLog(TeaModel):
    def __init__(
        self,
        func_name: str = None,
        gmt_create: str = None,
        level: str = None,
        line_no: int = None,
        log_id: str = None,
        message: str = None,
        task_id: str = None,
    ):
        # 函数名
        self.func_name = func_name
        # 记录时间
        self.gmt_create = gmt_create
        # 日志等级
        self.level = level
        # 行数
        self.line_no = line_no
        # 日志id
        self.log_id = log_id
        # 日志信息
        self.message = message
        # 任务id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.func_name is not None:
            result['FuncName'] = self.func_name
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.level is not None:
            result['Level'] = self.level
        if self.line_no is not None:
            result['LineNo'] = self.line_no
        if self.log_id is not None:
            result['LogId'] = self.log_id
        if self.message is not None:
            result['Message'] = self.message
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FuncName') is not None:
            self.func_name = m.get('FuncName')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('LineNo') is not None:
            self.line_no = m.get('LineNo')
        if m.get('LogId') is not None:
            self.log_id = m.get('LogId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class NotificationGroup(TeaModel):
    def __init__(
        self,
        gmt_create: str = None,
        gmt_modified: str = None,
        notification_group_description: str = None,
        notification_group_id: str = None,
        notification_group_name: str = None,
        notification_group_type: str = None,
        webhook: str = None,
    ):
        # 创建时间
        self.gmt_create = gmt_create
        # 修改时间
        self.gmt_modified = gmt_modified
        # 描述
        self.notification_group_description = notification_group_description
        # 通知组ID
        self.notification_group_id = notification_group_id
        # 通知组名称
        self.notification_group_name = notification_group_name
        # 通知组类型
        self.notification_group_type = notification_group_type
        # 钉钉群webhook
        self.webhook = webhook

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.notification_group_description is not None:
            result['NotificationGroupDescription'] = self.notification_group_description
        if self.notification_group_id is not None:
            result['NotificationGroupId'] = self.notification_group_id
        if self.notification_group_name is not None:
            result['NotificationGroupName'] = self.notification_group_name
        if self.notification_group_type is not None:
            result['NotificationGroupType'] = self.notification_group_type
        if self.webhook is not None:
            result['Webhook'] = self.webhook
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('NotificationGroupDescription') is not None:
            self.notification_group_description = m.get('NotificationGroupDescription')
        if m.get('NotificationGroupId') is not None:
            self.notification_group_id = m.get('NotificationGroupId')
        if m.get('NotificationGroupName') is not None:
            self.notification_group_name = m.get('NotificationGroupName')
        if m.get('NotificationGroupType') is not None:
            self.notification_group_type = m.get('NotificationGroupType')
        if m.get('Webhook') is not None:
            self.webhook = m.get('Webhook')
        return self


class TemplateInput(TeaModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        sample: str = None,
        type: str = None,
    ):
        # 参数说明
        self.description = description
        # 参数名称
        self.name = name
        # 参数示例
        self.sample = sample
        # 参数类型
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.sample is not None:
            result['Sample'] = self.sample
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Sample') is not None:
            self.sample = m.get('Sample')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class TemplateOutput(TeaModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        sample: str = None,
        type: str = None,
    ):
        # 参数说明
        self.description = description
        # 参数名称
        self.name = name
        # 参数示例
        self.sample = sample
        # 参数类型
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.sample is not None:
            result['Sample'] = self.sample
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Sample') is not None:
            self.sample = m.get('Sample')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class Template(TeaModel):
    def __init__(
        self,
        category: str = None,
        comment: str = None,
        gmt_create: str = None,
        gmt_modify: str = None,
        input: List[TemplateInput] = None,
        output: List[TemplateOutput] = None,
        template_name: str = None,
        template_type: str = None,
    ):
        # 模板类型
        self.category = category
        # 模板说明
        self.comment = comment
        # 创建时间
        self.gmt_create = gmt_create
        # 修改时间
        self.gmt_modify = gmt_modify
        # 模板入参
        self.input = input
        # 模板出参
        self.output = output
        # 模板名称
        self.template_name = template_name
        # 模板类型
        self.template_type = template_type

    def validate(self):
        if self.input:
            for k in self.input:
                if k:
                    k.validate()
        if self.output:
            for k in self.output:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modify is not None:
            result['GmtModify'] = self.gmt_modify
        result['Input'] = []
        if self.input is not None:
            for k in self.input:
                result['Input'].append(k.to_map() if k else None)
        result['Output'] = []
        if self.output is not None:
            for k in self.output:
                result['Output'].append(k.to_map() if k else None)
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModify') is not None:
            self.gmt_modify = m.get('GmtModify')
        self.input = []
        if m.get('Input') is not None:
            for k in m.get('Input'):
                temp_model = TemplateInput()
                self.input.append(temp_model.from_map(k))
        self.output = []
        if m.get('Output') is not None:
            for k in m.get('Output'):
                temp_model = TemplateOutput()
                self.output.append(temp_model.from_map(k))
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        return self


class DedicatedLine(TeaModel):
    def __init__(
        self,
        bandwidth: int = None,
        device_id: str = None,
        device_port: str = None,
        isp: str = None,
        line_gateway: str = None,
        line_id: str = None,
        line_ip: str = None,
        line_role: str = None,
    ):
        # 宽带（Mbps）
        self.bandwidth = bandwidth
        # 关联设备ID
        self.device_id = device_id
        # 关联设备端口
        self.device_port = device_port
        # 运营商
        self.isp = isp
        # 专线网关
        self.line_gateway = line_gateway
        # 物理空间专线ID
        self.line_id = line_id
        # 专线IP
        self.line_ip = line_ip
        # 专线角色
        self.line_role = line_role

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.device_port is not None:
            result['DevicePort'] = self.device_port
        if self.isp is not None:
            result['Isp'] = self.isp
        if self.line_gateway is not None:
            result['LineGateway'] = self.line_gateway
        if self.line_id is not None:
            result['LineId'] = self.line_id
        if self.line_ip is not None:
            result['LineIp'] = self.line_ip
        if self.line_role is not None:
            result['LineRole'] = self.line_role
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('DevicePort') is not None:
            self.device_port = m.get('DevicePort')
        if m.get('Isp') is not None:
            self.isp = m.get('Isp')
        if m.get('LineGateway') is not None:
            self.line_gateway = m.get('LineGateway')
        if m.get('LineId') is not None:
            self.line_id = m.get('LineId')
        if m.get('LineIp') is not None:
            self.line_ip = m.get('LineIp')
        if m.get('LineRole') is not None:
            self.line_role = m.get('LineRole')
        return self


class InspectionTaskInspectionAlarmRules(TeaModel):
    def __init__(
        self,
        expression: str = None,
        operator: str = None,
        value: str = None,
        actual_value: str = None,
        level: str = None,
    ):
        # 告警表达式
        self.expression = expression
        # 告警操作符
        self.operator = operator
        # 告警值
        self.value = value
        # 告警实际值
        self.actual_value = actual_value
        # 告警级别
        self.level = level

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.expression is not None:
            result['Expression'] = self.expression
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.value is not None:
            result['Value'] = self.value
        if self.actual_value is not None:
            result['ActualValue'] = self.actual_value
        if self.level is not None:
            result['Level'] = self.level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Expression') is not None:
            self.expression = m.get('Expression')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('ActualValue') is not None:
            self.actual_value = m.get('ActualValue')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        return self


class InspectionTask(TeaModel):
    def __init__(
        self,
        template_id: str = None,
        item_name: str = None,
        item_id: str = None,
        space: str = None,
        hostname: str = None,
        ip: str = None,
        vendor: str = None,
        model: str = None,
        role: str = None,
        task_status: str = None,
        device_id: str = None,
        error_code: str = None,
        inspection_result: str = None,
        execution_begin_time: str = None,
        execution_end_time: str = None,
        inspection_alarm_rules: List[InspectionTaskInspectionAlarmRules] = None,
    ):
        # 巡检模板ID
        self.template_id = template_id
        # 巡检项名字
        self.item_name = item_name
        # 巡检项ID
        self.item_id = item_id
        # 物理空间
        self.space = space
        # 主机名
        self.hostname = hostname
        # 设备IP
        self.ip = ip
        # 厂商
        self.vendor = vendor
        # 型号
        self.model = model
        # 角色
        self.role = role
        # 任务状态
        self.task_status = task_status
        # 设备ID
        self.device_id = device_id
        # 错误码
        self.error_code = error_code
        # 执行结果
        self.inspection_result = inspection_result
        # 执行开始时间
        self.execution_begin_time = execution_begin_time
        # 执行结束时间
        self.execution_end_time = execution_end_time
        # 告警规则
        self.inspection_alarm_rules = inspection_alarm_rules

    def validate(self):
        if self.inspection_alarm_rules:
            for k in self.inspection_alarm_rules:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.item_name is not None:
            result['ItemName'] = self.item_name
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.space is not None:
            result['Space'] = self.space
        if self.hostname is not None:
            result['Hostname'] = self.hostname
        if self.ip is not None:
            result['IP'] = self.ip
        if self.vendor is not None:
            result['Vendor'] = self.vendor
        if self.model is not None:
            result['Model'] = self.model
        if self.role is not None:
            result['Role'] = self.role
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.inspection_result is not None:
            result['InspectionResult'] = self.inspection_result
        if self.execution_begin_time is not None:
            result['ExecutionBeginTime'] = self.execution_begin_time
        if self.execution_end_time is not None:
            result['ExecutionEndTime'] = self.execution_end_time
        result['InspectionAlarmRules'] = []
        if self.inspection_alarm_rules is not None:
            for k in self.inspection_alarm_rules:
                result['InspectionAlarmRules'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('ItemName') is not None:
            self.item_name = m.get('ItemName')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('Space') is not None:
            self.space = m.get('Space')
        if m.get('Hostname') is not None:
            self.hostname = m.get('Hostname')
        if m.get('IP') is not None:
            self.ip = m.get('IP')
        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('InspectionResult') is not None:
            self.inspection_result = m.get('InspectionResult')
        if m.get('ExecutionBeginTime') is not None:
            self.execution_begin_time = m.get('ExecutionBeginTime')
        if m.get('ExecutionEndTime') is not None:
            self.execution_end_time = m.get('ExecutionEndTime')
        self.inspection_alarm_rules = []
        if m.get('InspectionAlarmRules') is not None:
            for k in m.get('InspectionAlarmRules'):
                temp_model = InspectionTaskInspectionAlarmRules()
                self.inspection_alarm_rules.append(temp_model.from_map(k))
        return self


class CliTask(TeaModel):
    def __init__(
        self,
        agent_ip: str = None,
        cli_task_id: str = None,
        command: str = None,
        device_id: str = None,
        gmt_create: str = None,
        gmt_modify: str = None,
        output: str = None,
        protocol: str = None,
        response_code: str = None,
        result: str = None,
        session_id: str = None,
        status: str = None,
        timeout: int = None,
    ):
        # agent IP
        self.agent_ip = agent_ip
        # cli任务id
        self.cli_task_id = cli_task_id
        # cli命令
        self.command = command
        # 设备id
        self.device_id = device_id
        # 创建时间
        self.gmt_create = gmt_create
        # 修改时间
        self.gmt_modify = gmt_modify
        # 设备回显
        self.output = output
        # 协议
        self.protocol = protocol
        # 任务错误码
        self.response_code = response_code
        # 任务结果
        self.result = result
        # 会话id
        self.session_id = session_id
        # cli任务状态
        self.status = status
        # 超时参数
        self.timeout = timeout

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.agent_ip is not None:
            result['AgentIp'] = self.agent_ip
        if self.cli_task_id is not None:
            result['CliTaskId'] = self.cli_task_id
        if self.command is not None:
            result['Command'] = self.command
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modify is not None:
            result['GmtModify'] = self.gmt_modify
        if self.output is not None:
            result['Output'] = self.output
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.response_code is not None:
            result['ResponseCode'] = self.response_code
        if self.result is not None:
            result['Result'] = self.result
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.status is not None:
            result['Status'] = self.status
        if self.timeout is not None:
            result['Timeout'] = self.timeout
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentIp') is not None:
            self.agent_ip = m.get('AgentIp')
        if m.get('CliTaskId') is not None:
            self.cli_task_id = m.get('CliTaskId')
        if m.get('Command') is not None:
            self.command = m.get('Command')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModify') is not None:
            self.gmt_modify = m.get('GmtModify')
        if m.get('Output') is not None:
            self.output = m.get('Output')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('ResponseCode') is not None:
            self.response_code = m.get('ResponseCode')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')
        return self


class Order(TeaModel):
    def __init__(
        self,
        gmt_create: str = None,
        gmt_modify: str = None,
        order_id: str = None,
        output: str = None,
        params: str = None,
        scheme_id: str = None,
        scheme_name: str = None,
        status: str = None,
        title: str = None,
    ):
        # 创建时间
        self.gmt_create = gmt_create
        # 修改时间
        self.gmt_modify = gmt_modify
        # 工单id
        self.order_id = order_id
        # 工单返回
        self.output = output
        # 工单参数
        self.params = params
        # 方案id
        self.scheme_id = scheme_id
        # 方案名
        self.scheme_name = scheme_name
        # 任务状态
        self.status = status
        # 工单标题
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modify is not None:
            result['GmtModify'] = self.gmt_modify
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.output is not None:
            result['Output'] = self.output
        if self.params is not None:
            result['Params'] = self.params
        if self.scheme_id is not None:
            result['SchemeId'] = self.scheme_id
        if self.scheme_name is not None:
            result['SchemeName'] = self.scheme_name
        if self.status is not None:
            result['Status'] = self.status
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModify') is not None:
            self.gmt_modify = m.get('GmtModify')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('Output') is not None:
            self.output = m.get('Output')
        if m.get('Params') is not None:
            self.params = m.get('Params')
        if m.get('SchemeId') is not None:
            self.scheme_id = m.get('SchemeId')
        if m.get('SchemeName') is not None:
            self.scheme_name = m.get('SchemeName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class ScriptInput(TeaModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        sample: str = None,
        type: str = None,
    ):
        # 参数说明
        self.description = description
        # 参数名称
        self.name = name
        # 参数示例
        self.sample = sample
        # 参数类型
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.sample is not None:
            result['Sample'] = self.sample
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Sample') is not None:
            self.sample = m.get('Sample')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ScriptOutput(TeaModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        sample: str = None,
        type: str = None,
    ):
        # 参数说明
        self.description = description
        # 参数名称
        self.name = name
        # 参数示例
        self.sample = sample
        # 参数类型
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.sample is not None:
            result['Sample'] = self.sample
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Sample') is not None:
            self.sample = m.get('Sample')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ScriptRule(TeaModel):
    def __init__(
        self,
        arch: str = None,
        domain: str = None,
        model: str = None,
        os: str = None,
        role: str = None,
        rule_id: str = None,
        script_id: str = None,
        vendor: str = None,
    ):
        # 设备架构
        self.arch = arch
        # 设备安全域
        self.domain = domain
        # 设备型号
        self.model = model
        # 设备OS版本
        self.os = os
        # 设备角色
        self.role = role
        # 规则id
        self.rule_id = rule_id
        # 脚本id
        self.script_id = script_id
        # 设备厂商
        self.vendor = vendor

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.arch is not None:
            result['Arch'] = self.arch
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.model is not None:
            result['Model'] = self.model
        if self.os is not None:
            result['Os'] = self.os
        if self.role is not None:
            result['Role'] = self.role
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.script_id is not None:
            result['ScriptId'] = self.script_id
        if self.vendor is not None:
            result['Vendor'] = self.vendor
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Arch') is not None:
            self.arch = m.get('Arch')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('Os') is not None:
            self.os = m.get('Os')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')
        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')
        return self


class Script(TeaModel):
    def __init__(
        self,
        content: str = None,
        gmt_create: str = None,
        gmt_modify: str = None,
        input: List[ScriptInput] = None,
        output: List[ScriptOutput] = None,
        rules: List[ScriptRule] = None,
        script_id: str = None,
        template_id: str = None,
        version_id: str = None,
    ):
        # 脚本代码
        self.content = content
        # 创建时间
        self.gmt_create = gmt_create
        # 修改时间
        self.gmt_modify = gmt_modify
        # 模板入参
        self.input = input
        # 模板出参
        self.output = output
        # 规则列表
        self.rules = rules
        # 脚本id
        self.script_id = script_id
        # 模板id
        self.template_id = template_id
        # 版本id
        self.version_id = version_id

    def validate(self):
        if self.input:
            for k in self.input:
                if k:
                    k.validate()
        if self.output:
            for k in self.output:
                if k:
                    k.validate()
        if self.rules:
            for k in self.rules:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modify is not None:
            result['GmtModify'] = self.gmt_modify
        result['Input'] = []
        if self.input is not None:
            for k in self.input:
                result['Input'].append(k.to_map() if k else None)
        result['Output'] = []
        if self.output is not None:
            for k in self.output:
                result['Output'].append(k.to_map() if k else None)
        result['Rules'] = []
        if self.rules is not None:
            for k in self.rules:
                result['Rules'].append(k.to_map() if k else None)
        if self.script_id is not None:
            result['ScriptId'] = self.script_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModify') is not None:
            self.gmt_modify = m.get('GmtModify')
        self.input = []
        if m.get('Input') is not None:
            for k in m.get('Input'):
                temp_model = ScriptInput()
                self.input.append(temp_model.from_map(k))
        self.output = []
        if m.get('Output') is not None:
            for k in m.get('Output'):
                temp_model = ScriptOutput()
                self.output.append(temp_model.from_map(k))
        self.rules = []
        if m.get('Rules') is not None:
            for k in m.get('Rules'):
                temp_model = ScriptRule()
                self.rules.append(temp_model.from_map(k))
        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        return self


class Agent(TeaModel):
    def __init__(
        self,
        agent_id: str = None,
        agent_name: str = None,
        agent_version: str = None,
        cpu_usage: str = None,
        disk_usage: str = None,
        gmt_modify: str = None,
        ip: str = None,
        kernel_version: str = None,
        memory_usage: str = None,
        security_domain: str = None,
        status: str = None,
    ):
        # 探针Id
        self.agent_id = agent_id
        # 探针名称
        self.agent_name = agent_name
        # 探针版本
        self.agent_version = agent_version
        # cpu使用率
        self.cpu_usage = cpu_usage
        # 磁盘利用率
        self.disk_usage = disk_usage
        # 更新时间
        self.gmt_modify = gmt_modify
        # 探针IP
        self.ip = ip
        # 系统版本
        self.kernel_version = kernel_version
        # 内存使用率
        self.memory_usage = memory_usage
        # 安全域
        self.security_domain = security_domain
        # 探针状态
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.agent_id is not None:
            result['AgentId'] = self.agent_id
        if self.agent_name is not None:
            result['AgentName'] = self.agent_name
        if self.agent_version is not None:
            result['AgentVersion'] = self.agent_version
        if self.cpu_usage is not None:
            result['CpuUsage'] = self.cpu_usage
        if self.disk_usage is not None:
            result['DiskUsage'] = self.disk_usage
        if self.gmt_modify is not None:
            result['GmtModify'] = self.gmt_modify
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.kernel_version is not None:
            result['KernelVersion'] = self.kernel_version
        if self.memory_usage is not None:
            result['MemoryUsage'] = self.memory_usage
        if self.security_domain is not None:
            result['SecurityDomain'] = self.security_domain
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')
        if m.get('AgentName') is not None:
            self.agent_name = m.get('AgentName')
        if m.get('AgentVersion') is not None:
            self.agent_version = m.get('AgentVersion')
        if m.get('CpuUsage') is not None:
            self.cpu_usage = m.get('CpuUsage')
        if m.get('DiskUsage') is not None:
            self.disk_usage = m.get('DiskUsage')
        if m.get('GmtModify') is not None:
            self.gmt_modify = m.get('GmtModify')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('KernelVersion') is not None:
            self.kernel_version = m.get('KernelVersion')
        if m.get('MemoryUsage') is not None:
            self.memory_usage = m.get('MemoryUsage')
        if m.get('SecurityDomain') is not None:
            self.security_domain = m.get('SecurityDomain')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class MonitorItem(TeaModel):
    def __init__(
        self,
        analysis_code: str = None,
        collection_type: str = None,
        config: str = None,
        monitor_item_description: str = None,
        enable: int = None,
        exec_interval: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        monitor_item_name: str = None,
        security_domain: str = None,
        monitor_item_id: str = None,
    ):
        # 解析代码
        self.analysis_code = analysis_code
        # 采集类型
        self.collection_type = collection_type
        # 采集配置
        self.config = config
        # 描述
        self.monitor_item_description = monitor_item_description
        # 是否启用
        self.enable = enable
        # 采集间隔
        self.exec_interval = exec_interval
        # 创建时间
        self.gmt_create = gmt_create
        # 更新时间
        self.gmt_modified = gmt_modified
        # 监控项名称
        self.monitor_item_name = monitor_item_name
        # 安全域
        self.security_domain = security_domain
        # 监控项ID
        self.monitor_item_id = monitor_item_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.analysis_code is not None:
            result['AnalysisCode'] = self.analysis_code
        if self.collection_type is not None:
            result['CollectionType'] = self.collection_type
        if self.config is not None:
            result['Config'] = self.config
        if self.monitor_item_description is not None:
            result['MonitorItemDescription'] = self.monitor_item_description
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.exec_interval is not None:
            result['ExecInterval'] = self.exec_interval
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.monitor_item_name is not None:
            result['MonitorItemName'] = self.monitor_item_name
        if self.security_domain is not None:
            result['SecurityDomain'] = self.security_domain
        if self.monitor_item_id is not None:
            result['MonitorItemId'] = self.monitor_item_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AnalysisCode') is not None:
            self.analysis_code = m.get('AnalysisCode')
        if m.get('CollectionType') is not None:
            self.collection_type = m.get('CollectionType')
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('MonitorItemDescription') is not None:
            self.monitor_item_description = m.get('MonitorItemDescription')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('ExecInterval') is not None:
            self.exec_interval = m.get('ExecInterval')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('MonitorItemName') is not None:
            self.monitor_item_name = m.get('MonitorItemName')
        if m.get('SecurityDomain') is not None:
            self.security_domain = m.get('SecurityDomain')
        if m.get('MonitorItemId') is not None:
            self.monitor_item_id = m.get('MonitorItemId')
        return self


class Device(TeaModel):
    def __init__(
        self,
        account_type: str = None,
        account_version: str = None,
        auth_pass_phrase: str = None,
        auth_protocol: str = None,
        community: str = None,
        device_form: str = None,
        device_id: str = None,
        device_ip: str = None,
        device_mac: str = None,
        device_sn: str = None,
        hostname: str = None,
        model: str = None,
        privacy_pass_phrase: str = None,
        privacy_protocol: str = None,
        security_domain: str = None,
        security_level: str = None,
        space: str = None,
        ssh_account: str = None,
        ssh_password: str = None,
        status: str = None,
        telnet_account: str = None,
        telnet_password: str = None,
        user_name: str = None,
        vendor: str = None,
    ):
        # 账号类型
        self.account_type = account_type
        # snmp版本号
        self.account_version = account_version
        # Auth PassPhrase
        self.auth_pass_phrase = auth_pass_phrase
        # Auth Protocol
        self.auth_protocol = auth_protocol
        # community
        self.community = community
        # 设备形态
        self.device_form = device_form
        # 设备ID
        self.device_id = device_id
        # 设备IP
        self.device_ip = device_ip
        # 设备MAC地址
        self.device_mac = device_mac
        # 设备SN
        self.device_sn = device_sn
        # 主机名
        self.hostname = hostname
        # 设备型号
        self.model = model
        # Privacy PassPhrase
        self.privacy_pass_phrase = privacy_pass_phrase
        # Privacy Protocol
        self.privacy_protocol = privacy_protocol
        # 设备安全域
        self.security_domain = security_domain
        # 安全等级
        self.security_level = security_level
        # 设备所属物理空间
        self.space = space
        # SSH登录账号
        self.ssh_account = ssh_account
        # SSH登录密码
        self.ssh_password = ssh_password
        # 设备状态
        self.status = status
        # TELNET登录账号
        self.telnet_account = telnet_account
        # TELNET登录密码
        self.telnet_password = telnet_password
        # 用户名
        self.user_name = user_name
        # 设备厂商
        self.vendor = vendor

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.account_type is not None:
            result['AccountType'] = self.account_type
        if self.account_version is not None:
            result['AccountVersion'] = self.account_version
        if self.auth_pass_phrase is not None:
            result['AuthPassPhrase'] = self.auth_pass_phrase
        if self.auth_protocol is not None:
            result['AuthProtocol'] = self.auth_protocol
        if self.community is not None:
            result['Community'] = self.community
        if self.device_form is not None:
            result['DeviceForm'] = self.device_form
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.device_ip is not None:
            result['DeviceIp'] = self.device_ip
        if self.device_mac is not None:
            result['DeviceMac'] = self.device_mac
        if self.device_sn is not None:
            result['DeviceSn'] = self.device_sn
        if self.hostname is not None:
            result['Hostname'] = self.hostname
        if self.model is not None:
            result['Model'] = self.model
        if self.privacy_pass_phrase is not None:
            result['PrivacyPassPhrase'] = self.privacy_pass_phrase
        if self.privacy_protocol is not None:
            result['PrivacyProtocol'] = self.privacy_protocol
        if self.security_domain is not None:
            result['SecurityDomain'] = self.security_domain
        if self.security_level is not None:
            result['SecurityLevel'] = self.security_level
        if self.space is not None:
            result['Space'] = self.space
        if self.ssh_account is not None:
            result['SshAccount'] = self.ssh_account
        if self.ssh_password is not None:
            result['SshPassword'] = self.ssh_password
        if self.status is not None:
            result['Status'] = self.status
        if self.telnet_account is not None:
            result['TelnetAccount'] = self.telnet_account
        if self.telnet_password is not None:
            result['TelnetPassword'] = self.telnet_password
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.vendor is not None:
            result['Vendor'] = self.vendor
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')
        if m.get('AccountVersion') is not None:
            self.account_version = m.get('AccountVersion')
        if m.get('AuthPassPhrase') is not None:
            self.auth_pass_phrase = m.get('AuthPassPhrase')
        if m.get('AuthProtocol') is not None:
            self.auth_protocol = m.get('AuthProtocol')
        if m.get('Community') is not None:
            self.community = m.get('Community')
        if m.get('DeviceForm') is not None:
            self.device_form = m.get('DeviceForm')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('DeviceIp') is not None:
            self.device_ip = m.get('DeviceIp')
        if m.get('DeviceMac') is not None:
            self.device_mac = m.get('DeviceMac')
        if m.get('DeviceSn') is not None:
            self.device_sn = m.get('DeviceSn')
        if m.get('Hostname') is not None:
            self.hostname = m.get('Hostname')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('PrivacyPassPhrase') is not None:
            self.privacy_pass_phrase = m.get('PrivacyPassPhrase')
        if m.get('PrivacyProtocol') is not None:
            self.privacy_protocol = m.get('PrivacyProtocol')
        if m.get('SecurityDomain') is not None:
            self.security_domain = m.get('SecurityDomain')
        if m.get('SecurityLevel') is not None:
            self.security_level = m.get('SecurityLevel')
        if m.get('Space') is not None:
            self.space = m.get('Space')
        if m.get('SshAccount') is not None:
            self.ssh_account = m.get('SshAccount')
        if m.get('SshPassword') is not None:
            self.ssh_password = m.get('SshPassword')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TelnetAccount') is not None:
            self.telnet_account = m.get('TelnetAccount')
        if m.get('TelnetPassword') is not None:
            self.telnet_password = m.get('TelnetPassword')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')
        return self


class TimePeriod(TeaModel):
    def __init__(
        self,
        gmt_create: str = None,
        gmt_modified: str = None,
        time_period_description: str = None,
        time_period_name: str = None,
        time_period_id: str = None,
        cron_expression: str = None,
        source: str = None,
    ):
        # 创建时间
        self.gmt_create = gmt_create
        # 修改时间
        self.gmt_modified = gmt_modified
        # 描述
        self.time_period_description = time_period_description
        # 时间段名称
        self.time_period_name = time_period_name
        # 时间段ID
        self.time_period_id = time_period_id
        # Cron表达式
        self.cron_expression = cron_expression
        # 来源
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.time_period_description is not None:
            result['TimePeriodDescription'] = self.time_period_description
        if self.time_period_name is not None:
            result['TimePeriodName'] = self.time_period_name
        if self.time_period_id is not None:
            result['TimePeriodId'] = self.time_period_id
        if self.cron_expression is not None:
            result['CronExpression'] = self.cron_expression
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('TimePeriodDescription') is not None:
            self.time_period_description = m.get('TimePeriodDescription')
        if m.get('TimePeriodName') is not None:
            self.time_period_name = m.get('TimePeriodName')
        if m.get('TimePeriodId') is not None:
            self.time_period_id = m.get('TimePeriodId')
        if m.get('CronExpression') is not None:
            self.cron_expression = m.get('CronExpression')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class PhysicalSpace(TeaModel):
    def __init__(
        self,
        address: str = None,
        city: str = None,
        country: str = None,
        province: str = None,
        space_id: str = None,
        space_name: str = None,
    ):
        # 具体所在地址
        self.address = address
        # 所属城市
        self.city = city
        # 所属国家
        self.country = country
        # 所属省份
        self.province = province
        # 物理空间ID
        self.space_id = space_id
        # 物理空间名称
        self.space_name = space_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.city is not None:
            result['City'] = self.city
        if self.country is not None:
            result['Country'] = self.country
        if self.province is not None:
            result['Province'] = self.province
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        if self.space_name is not None:
            result['SpaceName'] = self.space_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        if m.get('SpaceName') is not None:
            self.space_name = m.get('SpaceName')
        return self


class AtomicStepInput(TeaModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        sample: str = None,
        type: str = None,
    ):
        # 参数说明
        self.description = description
        # 参数名称
        self.name = name
        # 参数示例
        self.sample = sample
        # 参数类型
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.sample is not None:
            result['Sample'] = self.sample
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Sample') is not None:
            self.sample = m.get('Sample')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class AtomicStepOutput(TeaModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        sample: str = None,
        type: str = None,
    ):
        # 参数说明
        self.description = description
        # 参数名称
        self.name = name
        # 参数示例
        self.sample = sample
        # 参数类型
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.sample is not None:
            result['Sample'] = self.sample
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Sample') is not None:
            self.sample = m.get('Sample')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class AtomicStep(TeaModel):
    def __init__(
        self,
        description: str = None,
        input: List[AtomicStepInput] = None,
        output: List[AtomicStepOutput] = None,
        step_id: str = None,
        step_name: str = None,
        step_type: str = None,
    ):
        # 步骤说明
        self.description = description
        # 步骤入参
        self.input = input
        # 步骤出参
        self.output = output
        # 步骤id
        self.step_id = step_id
        # 步骤名称
        self.step_name = step_name
        # 步骤类型
        self.step_type = step_type

    def validate(self):
        if self.input:
            for k in self.input:
                if k:
                    k.validate()
        if self.output:
            for k in self.output:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        result['Input'] = []
        if self.input is not None:
            for k in self.input:
                result['Input'].append(k.to_map() if k else None)
        result['Output'] = []
        if self.output is not None:
            for k in self.output:
                result['Output'].append(k.to_map() if k else None)
        if self.step_id is not None:
            result['StepId'] = self.step_id
        if self.step_name is not None:
            result['StepName'] = self.step_name
        if self.step_type is not None:
            result['StepType'] = self.step_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        self.input = []
        if m.get('Input') is not None:
            for k in m.get('Input'):
                temp_model = AtomicStepInput()
                self.input.append(temp_model.from_map(k))
        self.output = []
        if m.get('Output') is not None:
            for k in m.get('Output'):
                temp_model = AtomicStepOutput()
                self.output.append(temp_model.from_map(k))
        if m.get('StepId') is not None:
            self.step_id = m.get('StepId')
        if m.get('StepName') is not None:
            self.step_name = m.get('StepName')
        if m.get('StepType') is not None:
            self.step_type = m.get('StepType')
        return self


class InspectionItem(TeaModel):
    def __init__(
        self,
        item_id: str = None,
        item_name: str = None,
        item_description: str = None,
        inspection_crontab: str = None,
    ):
        # 巡检项ID
        self.item_id = item_id
        # 巡检项名字
        self.item_name = item_name
        # 巡检项描述
        self.item_description = item_description
        # 巡检定时表达式
        self.inspection_crontab = inspection_crontab

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.item_name is not None:
            result['ItemName'] = self.item_name
        if self.item_description is not None:
            result['ItemDescription'] = self.item_description
        if self.inspection_crontab is not None:
            result['InspectionCrontab'] = self.inspection_crontab
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('ItemName') is not None:
            self.item_name = m.get('ItemName')
        if m.get('ItemDescription') is not None:
            self.item_description = m.get('ItemDescription')
        if m.get('InspectionCrontab') is not None:
            self.inspection_crontab = m.get('InspectionCrontab')
        return self


class InspectionScriptInspectionAlarmRules(TeaModel):
    def __init__(
        self,
        alarm_expression: str = None,
        alarm_operator: str = None,
        alarm_value: str = None,
        alarm_level: str = None,
    ):
        # 告警表达式
        self.alarm_expression = alarm_expression
        # 告警符号
        self.alarm_operator = alarm_operator
        # 告警值
        self.alarm_value = alarm_value
        # 告警级别
        self.alarm_level = alarm_level

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.alarm_expression is not None:
            result['AlarmExpression'] = self.alarm_expression
        if self.alarm_operator is not None:
            result['AlarmOperator'] = self.alarm_operator
        if self.alarm_value is not None:
            result['AlarmValue'] = self.alarm_value
        if self.alarm_level is not None:
            result['AlarmLevel'] = self.alarm_level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmExpression') is not None:
            self.alarm_expression = m.get('AlarmExpression')
        if m.get('AlarmOperator') is not None:
            self.alarm_operator = m.get('AlarmOperator')
        if m.get('AlarmValue') is not None:
            self.alarm_value = m.get('AlarmValue')
        if m.get('AlarmLevel') is not None:
            self.alarm_level = m.get('AlarmLevel')
        return self


class InspectionScript(TeaModel):
    def __init__(
        self,
        script_id: str = None,
        item_id: str = None,
        item_name: str = None,
        item_description: str = None,
        inspection_crontab: str = None,
        vendor: str = None,
        model: str = None,
        role: str = None,
        script_status: str = None,
        script: str = None,
        inspection_alarm_rules: List[InspectionScriptInspectionAlarmRules] = None,
    ):
        # 巡检模板ID
        self.script_id = script_id
        # 巡检项ID
        self.item_id = item_id
        # 巡检项名字
        self.item_name = item_name
        # 巡检项描述
        self.item_description = item_description
        # 巡检项定时表达式
        self.inspection_crontab = inspection_crontab
        # 厂商
        self.vendor = vendor
        # 型号
        self.model = model
        # 角色
        self.role = role
        # 模板状态
        self.script_status = script_status
        # 模板执行内容
        self.script = script
        # 巡检告警规则
        self.inspection_alarm_rules = inspection_alarm_rules

    def validate(self):
        if self.inspection_alarm_rules:
            for k in self.inspection_alarm_rules:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.script_id is not None:
            result['ScriptId'] = self.script_id
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.item_name is not None:
            result['ItemName'] = self.item_name
        if self.item_description is not None:
            result['ItemDescription'] = self.item_description
        if self.inspection_crontab is not None:
            result['InspectionCrontab'] = self.inspection_crontab
        if self.vendor is not None:
            result['Vendor'] = self.vendor
        if self.model is not None:
            result['Model'] = self.model
        if self.role is not None:
            result['Role'] = self.role
        if self.script_status is not None:
            result['ScriptStatus'] = self.script_status
        if self.script is not None:
            result['Script'] = self.script
        result['InspectionAlarmRules'] = []
        if self.inspection_alarm_rules is not None:
            for k in self.inspection_alarm_rules:
                result['InspectionAlarmRules'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('ItemName') is not None:
            self.item_name = m.get('ItemName')
        if m.get('ItemDescription') is not None:
            self.item_description = m.get('ItemDescription')
        if m.get('InspectionCrontab') is not None:
            self.inspection_crontab = m.get('InspectionCrontab')
        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('ScriptStatus') is not None:
            self.script_status = m.get('ScriptStatus')
        if m.get('Script') is not None:
            self.script = m.get('Script')
        self.inspection_alarm_rules = []
        if m.get('InspectionAlarmRules') is not None:
            for k in m.get('InspectionAlarmRules'):
                temp_model = InspectionScriptInspectionAlarmRules()
                self.inspection_alarm_rules.append(temp_model.from_map(k))
        return self


class SubscriptionItem(TeaModel):
    def __init__(
        self,
        alarm_status: str = None,
        notification_mode: str = None,
        suppression_strategy: str = None,
        notification_group_id: str = None,
        subscription_type: str = None,
        trigger_times: int = None,
        monitor_item_id: str = None,
        language: str = None,
        recovery_notice: int = None,
        subscription_item_id: str = None,
    ):
        # 告警状态
        self.alarm_status = alarm_status
        # 通知方式
        self.notification_mode = notification_mode
        # 抑制策略
        self.suppression_strategy = suppression_strategy
        # 通知组ID
        self.notification_group_id = notification_group_id
        # 订阅类型
        self.subscription_type = subscription_type
        # 连续触发次数
        self.trigger_times = trigger_times
        # 监控项ID
        self.monitor_item_id = monitor_item_id
        # 发送通知的语言
        self.language = language
        # 是否发送通知
        self.recovery_notice = recovery_notice
        # 订阅项ID
        self.subscription_item_id = subscription_item_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.alarm_status is not None:
            result['AlarmStatus'] = self.alarm_status
        if self.notification_mode is not None:
            result['NotificationMode'] = self.notification_mode
        if self.suppression_strategy is not None:
            result['SuppressionStrategy'] = self.suppression_strategy
        if self.notification_group_id is not None:
            result['NotificationGroupId'] = self.notification_group_id
        if self.subscription_type is not None:
            result['SubscriptionType'] = self.subscription_type
        if self.trigger_times is not None:
            result['TriggerTimes'] = self.trigger_times
        if self.monitor_item_id is not None:
            result['MonitorItemId'] = self.monitor_item_id
        if self.language is not None:
            result['Language'] = self.language
        if self.recovery_notice is not None:
            result['RecoveryNotice'] = self.recovery_notice
        if self.subscription_item_id is not None:
            result['SubscriptionItemId'] = self.subscription_item_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmStatus') is not None:
            self.alarm_status = m.get('AlarmStatus')
        if m.get('NotificationMode') is not None:
            self.notification_mode = m.get('NotificationMode')
        if m.get('SuppressionStrategy') is not None:
            self.suppression_strategy = m.get('SuppressionStrategy')
        if m.get('NotificationGroupId') is not None:
            self.notification_group_id = m.get('NotificationGroupId')
        if m.get('SubscriptionType') is not None:
            self.subscription_type = m.get('SubscriptionType')
        if m.get('TriggerTimes') is not None:
            self.trigger_times = m.get('TriggerTimes')
        if m.get('MonitorItemId') is not None:
            self.monitor_item_id = m.get('MonitorItemId')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('RecoveryNotice') is not None:
            self.recovery_notice = m.get('RecoveryNotice')
        if m.get('SubscriptionItemId') is not None:
            self.subscription_item_id = m.get('SubscriptionItemId')
        return self


class DataViewChart(TeaModel):
    def __init__(
        self,
        gmt_create: str = None,
        gmt_modified: str = None,
        data_view_id: str = None,
        chart_type: str = None,
        data_view_source: str = None,
        grid: str = None,
    ):
        # 创建时间
        self.gmt_create = gmt_create
        # 修改时间
        self.gmt_modified = gmt_modified
        # 数据视图ID
        self.data_view_id = data_view_id
        # 图表类型
        self.chart_type = chart_type
        # 数据源类型
        self.data_view_source = data_view_source
        # 布局配置
        self.grid = grid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.data_view_id is not None:
            result['DataViewId'] = self.data_view_id
        if self.chart_type is not None:
            result['ChartType'] = self.chart_type
        if self.data_view_source is not None:
            result['DataViewSource'] = self.data_view_source
        if self.grid is not None:
            result['Grid'] = self.grid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('DataViewId') is not None:
            self.data_view_id = m.get('DataViewId')
        if m.get('ChartType') is not None:
            self.chart_type = m.get('ChartType')
        if m.get('DataViewSource') is not None:
            self.data_view_source = m.get('DataViewSource')
        if m.get('Grid') is not None:
            self.grid = m.get('Grid')
        return self


class DataView(TeaModel):
    def __init__(
        self,
        gmt_create: str = None,
        gmt_modified: str = None,
        data_view_name: str = None,
        data_view_description: str = None,
        data_view_id: str = None,
        data_view_chart_list: List[DataViewChart] = None,
    ):
        # 创建时间
        self.gmt_create = gmt_create
        # 修改时间
        self.gmt_modified = gmt_modified
        # 数据视图名称
        self.data_view_name = data_view_name
        # 描述
        self.data_view_description = data_view_description
        # 聚合数据
        self.data_view_id = data_view_id
        # 图表列表
        self.data_view_chart_list = data_view_chart_list

    def validate(self):
        if self.data_view_chart_list:
            for k in self.data_view_chart_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.data_view_name is not None:
            result['DataViewName'] = self.data_view_name
        if self.data_view_description is not None:
            result['DataViewDescription'] = self.data_view_description
        if self.data_view_id is not None:
            result['DataViewId'] = self.data_view_id
        result['DataViewChartList'] = []
        if self.data_view_chart_list is not None:
            for k in self.data_view_chart_list:
                result['DataViewChartList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('DataViewName') is not None:
            self.data_view_name = m.get('DataViewName')
        if m.get('DataViewDescription') is not None:
            self.data_view_description = m.get('DataViewDescription')
        if m.get('DataViewId') is not None:
            self.data_view_id = m.get('DataViewId')
        self.data_view_chart_list = []
        if m.get('DataViewChartList') is not None:
            for k in m.get('DataViewChartList'):
                temp_model = DataViewChart()
                self.data_view_chart_list.append(temp_model.from_map(k))
        return self


class DeviceProperty(TeaModel):
    def __init__(
        self,
        content: str = None,
        device_form: str = None,
        format: str = None,
        name_cn: str = None,
        name_en: str = None,
        property_id: str = None,
    ):
        # 属性值
        self.content = content
        # 设备形态
        self.device_form = device_form
        # 属性格式，包括JSON和SPLITTER（分隔符）
        self.format = format
        # 属性展示名称
        self.name_cn = name_cn
        # 属性英文主键
        self.name_en = name_en
        # 设备属性ID
        self.property_id = property_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.device_form is not None:
            result['DeviceForm'] = self.device_form
        if self.format is not None:
            result['Format'] = self.format
        if self.name_cn is not None:
            result['NameCn'] = self.name_cn
        if self.name_en is not None:
            result['NameEn'] = self.name_en
        if self.property_id is not None:
            result['PropertyId'] = self.property_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('DeviceForm') is not None:
            self.device_form = m.get('DeviceForm')
        if m.get('Format') is not None:
            self.format = m.get('Format')
        if m.get('NameCn') is not None:
            self.name_cn = m.get('NameCn')
        if m.get('NameEn') is not None:
            self.name_en = m.get('NameEn')
        if m.get('PropertyId') is not None:
            self.property_id = m.get('PropertyId')
        return self


class AgentsTask(TeaModel):
    def __init__(
        self,
        action_type: str = None,
        agent_type: str = None,
        gmt_create: str = None,
        gmt_modify: str = None,
        params: str = None,
        status: str = None,
        agents_task_id: str = None,
    ):
        # 操作类型
        self.action_type = action_type
        # 探针类型
        self.agent_type = agent_type
        # 创建时间
        self.gmt_create = gmt_create
        # 更新时间
        self.gmt_modify = gmt_modify
        # 任务参数
        self.params = params
        # 任务状态
        self.status = status
        # 任务ID
        self.agents_task_id = agents_task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.action_type is not None:
            result['ActionType'] = self.action_type
        if self.agent_type is not None:
            result['AgentType'] = self.agent_type
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modify is not None:
            result['GmtModify'] = self.gmt_modify
        if self.params is not None:
            result['Params'] = self.params
        if self.status is not None:
            result['Status'] = self.status
        if self.agents_task_id is not None:
            result['AgentsTaskId'] = self.agents_task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionType') is not None:
            self.action_type = m.get('ActionType')
        if m.get('AgentType') is not None:
            self.agent_type = m.get('AgentType')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModify') is not None:
            self.gmt_modify = m.get('GmtModify')
        if m.get('Params') is not None:
            self.params = m.get('Params')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('AgentsTaskId') is not None:
            self.agents_task_id = m.get('AgentsTaskId')
        return self


class DeviceTask(TeaModel):
    def __init__(
        self,
        device_id: str = None,
        device_ip: str = None,
        device_name: str = None,
        device_task_id: str = None,
        gmt_create: str = None,
        gmt_modify: str = None,
        output: str = None,
        params: str = None,
        response_code: str = None,
        result: str = None,
        script_id: str = None,
        script_version: str = None,
        status: str = None,
        template_id: str = None,
        template_name: str = None,
    ):
        # 设备id
        self.device_id = device_id
        # 设备ip
        self.device_ip = device_ip
        # 设备名
        self.device_name = device_name
        # 设备任务id
        self.device_task_id = device_task_id
        # 创建时间
        self.gmt_create = gmt_create
        # 修改时间
        self.gmt_modify = gmt_modify
        # 设备任务回显
        self.output = output
        # 设备任务参数
        self.params = params
        # 设备任务错误码
        self.response_code = response_code
        # 设备任务返回
        self.result = result
        # 脚本id
        self.script_id = script_id
        # 版本id
        self.script_version = script_version
        # 设备任务状态
        self.status = status
        # 模板id
        self.template_id = template_id
        # 模板名称
        self.template_name = template_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.device_ip is not None:
            result['DeviceIp'] = self.device_ip
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.device_task_id is not None:
            result['DeviceTaskId'] = self.device_task_id
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modify is not None:
            result['GmtModify'] = self.gmt_modify
        if self.output is not None:
            result['Output'] = self.output
        if self.params is not None:
            result['Params'] = self.params
        if self.response_code is not None:
            result['ResponseCode'] = self.response_code
        if self.result is not None:
            result['Result'] = self.result
        if self.script_id is not None:
            result['ScriptId'] = self.script_id
        if self.script_version is not None:
            result['ScriptVersion'] = self.script_version
        if self.status is not None:
            result['Status'] = self.status
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('DeviceIp') is not None:
            self.device_ip = m.get('DeviceIp')
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('DeviceTaskId') is not None:
            self.device_task_id = m.get('DeviceTaskId')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModify') is not None:
            self.gmt_modify = m.get('GmtModify')
        if m.get('Output') is not None:
            self.output = m.get('Output')
        if m.get('Params') is not None:
            self.params = m.get('Params')
        if m.get('ResponseCode') is not None:
            self.response_code = m.get('ResponseCode')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')
        if m.get('ScriptVersion') is not None:
            self.script_version = m.get('ScriptVersion')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        return self


class PortCollection(TeaModel):
    def __init__(
        self,
        gmt_create: str = None,
        gmt_modified: str = None,
        port_collection_description: str = None,
        port_collection_id: str = None,
        port_collection_name: str = None,
        port_list: List[Port] = None,
    ):
        # 创建时间
        self.gmt_create = gmt_create
        # 修改时间
        self.gmt_modified = gmt_modified
        # 描述
        self.port_collection_description = port_collection_description
        # 端口集ID
        self.port_collection_id = port_collection_id
        # 端口集名称
        self.port_collection_name = port_collection_name
        # 端口列表
        self.port_list = port_list

    def validate(self):
        if self.port_list:
            for k in self.port_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.port_collection_description is not None:
            result['PortCollectionDescription'] = self.port_collection_description
        if self.port_collection_id is not None:
            result['PortCollectionId'] = self.port_collection_id
        if self.port_collection_name is not None:
            result['PortCollectionName'] = self.port_collection_name
        result['PortList'] = []
        if self.port_list is not None:
            for k in self.port_list:
                result['PortList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('PortCollectionDescription') is not None:
            self.port_collection_description = m.get('PortCollectionDescription')
        if m.get('PortCollectionId') is not None:
            self.port_collection_id = m.get('PortCollectionId')
        if m.get('PortCollectionName') is not None:
            self.port_collection_name = m.get('PortCollectionName')
        self.port_list = []
        if m.get('PortList') is not None:
            for k in m.get('PortList'):
                temp_model = Port()
                self.port_list.append(temp_model.from_map(k))
        return self


class ScriptHistoryInput(TeaModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        sample: str = None,
        type: str = None,
    ):
        # 参数说明
        self.description = description
        # 参数名称
        self.name = name
        # 参数示例
        self.sample = sample
        # 参数类型
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.sample is not None:
            result['Sample'] = self.sample
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Sample') is not None:
            self.sample = m.get('Sample')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ScriptHistoryOutput(TeaModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        sample: str = None,
        type: str = None,
    ):
        # 参数说明
        self.description = description
        # 参数名称
        self.name = name
        # 参数示例
        self.sample = sample
        # 参数类型
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.sample is not None:
            result['Sample'] = self.sample
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Sample') is not None:
            self.sample = m.get('Sample')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ScriptHistory(TeaModel):
    def __init__(
        self,
        comment: str = None,
        content: str = None,
        gmt_create: str = None,
        gmt_modify: str = None,
        input: List[ScriptHistoryInput] = None,
        output: List[ScriptHistoryOutput] = None,
        script_id: str = None,
        version_id: str = None,
    ):
        # 版本说明
        self.comment = comment
        # 脚本代码
        self.content = content
        # 创建时间
        self.gmt_create = gmt_create
        # 修改时间
        self.gmt_modify = gmt_modify
        # 模板入参
        self.input = input
        # 模板出参
        self.output = output
        # 脚本id
        self.script_id = script_id
        # 版本id
        self.version_id = version_id

    def validate(self):
        if self.input:
            for k in self.input:
                if k:
                    k.validate()
        if self.output:
            for k in self.output:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.content is not None:
            result['Content'] = self.content
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modify is not None:
            result['GmtModify'] = self.gmt_modify
        result['Input'] = []
        if self.input is not None:
            for k in self.input:
                result['Input'].append(k.to_map() if k else None)
        result['Output'] = []
        if self.output is not None:
            for k in self.output:
                result['Output'].append(k.to_map() if k else None)
        if self.script_id is not None:
            result['ScriptId'] = self.script_id
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModify') is not None:
            self.gmt_modify = m.get('GmtModify')
        self.input = []
        if m.get('Input') is not None:
            for k in m.get('Input'):
                temp_model = ScriptHistoryInput()
                self.input.append(temp_model.from_map(k))
        self.output = []
        if m.get('Output') is not None:
            for k in m.get('Output'):
                temp_model = ScriptHistoryOutput()
                self.output.append(temp_model.from_map(k))
        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        return self


class GetDeviceConfigRequest(TeaModel):
    def __init__(
        self,
        device_id: str = None,
        date: str = None,
    ):
        # 实例 ID。
        self.device_id = device_id
        # 查询日期，格式 yyyy-MM-dd
        self.date = date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.date is not None:
            result['Date'] = self.date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('Date') is not None:
            self.date = m.get('Date')
        return self


class GetDeviceConfigResponseBody(TeaModel):
    def __init__(
        self,
        device_config: str = None,
        request_id: str = None,
    ):
        # 设备配置内容
        self.device_config = device_config
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.device_config is not None:
            result['DeviceConfig'] = self.device_config
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceConfig') is not None:
            self.device_config = m.get('DeviceConfig')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetDeviceConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetDeviceConfigResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetDeviceConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDeviceRequest(TeaModel):
    def __init__(
        self,
        device_id: str = None,
    ):
        # 实例 ID。
        self.device_id = device_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        return self


class DeleteDeviceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteDeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteDeviceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDedicatedLineRequest(TeaModel):
    def __init__(
        self,
        dedicated_line_id: str = None,
    ):
        # 实例 ID。
        self.dedicated_line_id = dedicated_line_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.dedicated_line_id is not None:
            result['DedicatedLineId'] = self.dedicated_line_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DedicatedLineId') is not None:
            self.dedicated_line_id = m.get('DedicatedLineId')
        return self


class GetDedicatedLineResponseBodyDedicatedLine(TeaModel):
    def __init__(
        self,
        dedicated_line_id: str = None,
        isp: str = None,
        bandwidth: int = None,
        dedicated_line_ip: str = None,
        dedicated_line_gateway: str = None,
        dedicated_line_role: str = None,
        device_id: str = None,
        device_port: str = None,
        device_name: str = None,
    ):
        # 专线ID
        self.dedicated_line_id = dedicated_line_id
        # 运营商
        self.isp = isp
        # 宽带（Mbps）
        self.bandwidth = bandwidth
        # 专线IP
        self.dedicated_line_ip = dedicated_line_ip
        # 专线网关
        self.dedicated_line_gateway = dedicated_line_gateway
        # 专线角色
        self.dedicated_line_role = dedicated_line_role
        # 关联设备ID
        self.device_id = device_id
        # 关联设备端口名称
        self.device_port = device_port
        # 关联设备名称
        self.device_name = device_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.dedicated_line_id is not None:
            result['DedicatedLineId'] = self.dedicated_line_id
        if self.isp is not None:
            result['Isp'] = self.isp
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.dedicated_line_ip is not None:
            result['DedicatedLineIp'] = self.dedicated_line_ip
        if self.dedicated_line_gateway is not None:
            result['DedicatedLineGateway'] = self.dedicated_line_gateway
        if self.dedicated_line_role is not None:
            result['DedicatedLineRole'] = self.dedicated_line_role
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.device_port is not None:
            result['DevicePort'] = self.device_port
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DedicatedLineId') is not None:
            self.dedicated_line_id = m.get('DedicatedLineId')
        if m.get('Isp') is not None:
            self.isp = m.get('Isp')
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('DedicatedLineIp') is not None:
            self.dedicated_line_ip = m.get('DedicatedLineIp')
        if m.get('DedicatedLineGateway') is not None:
            self.dedicated_line_gateway = m.get('DedicatedLineGateway')
        if m.get('DedicatedLineRole') is not None:
            self.dedicated_line_role = m.get('DedicatedLineRole')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('DevicePort') is not None:
            self.device_port = m.get('DevicePort')
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        return self


class GetDedicatedLineResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        dedicated_line: GetDedicatedLineResponseBodyDedicatedLine = None,
    ):
        # Id of the request
        self.request_id = request_id
        # 物理空间专线详情
        self.dedicated_line = dedicated_line

    def validate(self):
        if self.dedicated_line:
            self.dedicated_line.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.dedicated_line is not None:
            result['DedicatedLine'] = self.dedicated_line.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DedicatedLine') is not None:
            temp_model = GetDedicatedLineResponseBodyDedicatedLine()
            self.dedicated_line = temp_model.from_map(m['DedicatedLine'])
        return self


class GetDedicatedLineResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetDedicatedLineResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetDedicatedLineResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDedicatedLineRequest(TeaModel):
    def __init__(
        self,
        dedicated_line_id: str = None,
    ):
        # 实例 ID。
        self.dedicated_line_id = dedicated_line_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.dedicated_line_id is not None:
            result['DedicatedLineId'] = self.dedicated_line_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DedicatedLineId') is not None:
            self.dedicated_line_id = m.get('DedicatedLineId')
        return self


class DeleteDedicatedLineResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteDedicatedLineResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteDedicatedLineResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteDedicatedLineResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDeviceValuesRequest(TeaModel):
    def __init__(
        self,
        device_form_id: str = None,
        device_form_name: str = None,
        attribute_keyword: str = None,
        attribute_group: str = None,
    ):
        # 设备形态ID
        self.device_form_id = device_form_id
        # 设备形态名称
        self.device_form_name = device_form_name
        # 查询属性主键
        self.attribute_keyword = attribute_keyword
        # 查询属性对应JSON中主键
        self.attribute_group = attribute_group

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.device_form_id is not None:
            result['DeviceFormId'] = self.device_form_id
        if self.device_form_name is not None:
            result['DeviceFormName'] = self.device_form_name
        if self.attribute_keyword is not None:
            result['AttributeKeyword'] = self.attribute_keyword
        if self.attribute_group is not None:
            result['AttributeGroup'] = self.attribute_group
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceFormId') is not None:
            self.device_form_id = m.get('DeviceFormId')
        if m.get('DeviceFormName') is not None:
            self.device_form_name = m.get('DeviceFormName')
        if m.get('AttributeKeyword') is not None:
            self.attribute_keyword = m.get('AttributeKeyword')
        if m.get('AttributeGroup') is not None:
            self.attribute_group = m.get('AttributeGroup')
        return self


class ListDeviceValuesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        device_values: List[str] = None,
    ):
        # Id of the request
        self.request_id = request_id
        # 数组，返回示例目录。
        self.device_values = device_values

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.device_values is not None:
            result['DeviceValues'] = self.device_values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DeviceValues') is not None:
            self.device_values = m.get('DeviceValues')
        return self


class ListDeviceValuesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListDeviceValuesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListDeviceValuesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableNotificationRequestList(TeaModel):
    def __init__(
        self,
        type: str = None,
        monitor_item_id: str = None,
        device_id: str = None,
        aggregate_data_id: str = None,
        dedicated_line_id: str = None,
    ):
        # 类型
        self.type = type
        # 监控项ID
        self.monitor_item_id = monitor_item_id
        # 设备ID
        self.device_id = device_id
        # 聚合数据ID
        self.aggregate_data_id = aggregate_data_id
        # 专线ID
        self.dedicated_line_id = dedicated_line_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.monitor_item_id is not None:
            result['MonitorItemId'] = self.monitor_item_id
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.aggregate_data_id is not None:
            result['AggregateDataId'] = self.aggregate_data_id
        if self.dedicated_line_id is not None:
            result['DedicatedLineId'] = self.dedicated_line_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('MonitorItemId') is not None:
            self.monitor_item_id = m.get('MonitorItemId')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('AggregateDataId') is not None:
            self.aggregate_data_id = m.get('AggregateDataId')
        if m.get('DedicatedLineId') is not None:
            self.dedicated_line_id = m.get('DedicatedLineId')
        return self


class EnableNotificationRequest(TeaModel):
    def __init__(
        self,
        list: List[EnableNotificationRequestList] = None,
    ):
        # 通知对象
        self.list = list

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = EnableNotificationRequestList()
                self.list.append(temp_model.from_map(k))
        return self


class EnableNotificationResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # request id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class EnableNotificationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: EnableNotificationResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = EnableNotificationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDevicePropertyRequest(TeaModel):
    def __init__(
        self,
        device_property_id: str = None,
        property_format: str = None,
        property_content: str = None,
        property_name: str = None,
    ):
        # 实例 ID。
        self.device_property_id = device_property_id
        # 属性格式
        self.property_format = property_format
        # 属性内容
        self.property_content = property_content
        # 属性名称
        self.property_name = property_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.device_property_id is not None:
            result['DevicePropertyId'] = self.device_property_id
        if self.property_format is not None:
            result['PropertyFormat'] = self.property_format
        if self.property_content is not None:
            result['PropertyContent'] = self.property_content
        if self.property_name is not None:
            result['PropertyName'] = self.property_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DevicePropertyId') is not None:
            self.device_property_id = m.get('DevicePropertyId')
        if m.get('PropertyFormat') is not None:
            self.property_format = m.get('PropertyFormat')
        if m.get('PropertyContent') is not None:
            self.property_content = m.get('PropertyContent')
        if m.get('PropertyName') is not None:
            self.property_name = m.get('PropertyName')
        return self


class UpdateDevicePropertyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateDevicePropertyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateDevicePropertyResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateDevicePropertyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListNotificationHistoriesRequest(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        max_results: int = None,
        monitor_item_id: str = None,
        device_id: str = None,
        type: str = None,
        dedicated_line_id: str = None,
        aggregate_data_id: str = None,
    ):
        # 标记当前开始读取的位置，置空表示从头开始
        self.next_token = next_token
        # 本次读取的最大数据记录数量
        self.max_results = max_results
        # 监控项ID
        self.monitor_item_id = monitor_item_id
        # 设备ID
        self.device_id = device_id
        # 类型
        self.type = type
        # 专线ID
        self.dedicated_line_id = dedicated_line_id
        # 聚合数据ID
        self.aggregate_data_id = aggregate_data_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.monitor_item_id is not None:
            result['MonitorItemId'] = self.monitor_item_id
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.type is not None:
            result['Type'] = self.type
        if self.dedicated_line_id is not None:
            result['DedicatedLineId'] = self.dedicated_line_id
        if self.aggregate_data_id is not None:
            result['AggregateDataId'] = self.aggregate_data_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('MonitorItemId') is not None:
            self.monitor_item_id = m.get('MonitorItemId')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('DedicatedLineId') is not None:
            self.dedicated_line_id = m.get('DedicatedLineId')
        if m.get('AggregateDataId') is not None:
            self.aggregate_data_id = m.get('AggregateDataId')
        return self


class ListNotificationHistoriesResponseBodyNotificationHistories(TeaModel):
    def __init__(
        self,
        time: str = None,
        notification_mode: str = None,
        status: str = None,
        output: str = None,
        message: str = None,
        device_id: str = None,
        monitor_item_id: str = None,
        notification_group_id: str = None,
        notification_group_name: str = None,
        dedicated_line_id: str = None,
        aggregate_data_id: str = None,
    ):
        # 发送时间
        self.time = time
        # 发送方式
        self.notification_mode = notification_mode
        # 发送状态
        self.status = status
        # 输出内容
        self.output = output
        # 发送内容
        self.message = message
        # 设备ID
        self.device_id = device_id
        # 监控项ID
        self.monitor_item_id = monitor_item_id
        # 通知组ID
        self.notification_group_id = notification_group_id
        # 通知组名称
        self.notification_group_name = notification_group_name
        # 专线ID
        self.dedicated_line_id = dedicated_line_id
        # 聚合数据ID
        self.aggregate_data_id = aggregate_data_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.time is not None:
            result['Time'] = self.time
        if self.notification_mode is not None:
            result['NotificationMode'] = self.notification_mode
        if self.status is not None:
            result['Status'] = self.status
        if self.output is not None:
            result['Output'] = self.output
        if self.message is not None:
            result['Message'] = self.message
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.monitor_item_id is not None:
            result['MonitorItemId'] = self.monitor_item_id
        if self.notification_group_id is not None:
            result['NotificationGroupId'] = self.notification_group_id
        if self.notification_group_name is not None:
            result['NotificationGroupName'] = self.notification_group_name
        if self.dedicated_line_id is not None:
            result['DedicatedLineId'] = self.dedicated_line_id
        if self.aggregate_data_id is not None:
            result['AggregateDataId'] = self.aggregate_data_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Time') is not None:
            self.time = m.get('Time')
        if m.get('NotificationMode') is not None:
            self.notification_mode = m.get('NotificationMode')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Output') is not None:
            self.output = m.get('Output')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('MonitorItemId') is not None:
            self.monitor_item_id = m.get('MonitorItemId')
        if m.get('NotificationGroupId') is not None:
            self.notification_group_id = m.get('NotificationGroupId')
        if m.get('NotificationGroupName') is not None:
            self.notification_group_name = m.get('NotificationGroupName')
        if m.get('DedicatedLineId') is not None:
            self.dedicated_line_id = m.get('DedicatedLineId')
        if m.get('AggregateDataId') is not None:
            self.aggregate_data_id = m.get('AggregateDataId')
        return self


class ListNotificationHistoriesResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        next_token: str = None,
        max_results: int = None,
        notification_histories: List[ListNotificationHistoriesResponseBodyNotificationHistories] = None,
    ):
        # TotalCount本次请求条件下的数据总量，此参数为可选参数，默认可不返回
        self.total_count = total_count
        # request Id
        self.request_id = request_id
        # 表示当前调用返回读取到的位置，空代表数据已经读取完毕
        self.next_token = next_token
        # MaxResults本次请求所返回的最大记录条数
        self.max_results = max_results
        # 数据列表
        self.notification_histories = notification_histories

    def validate(self):
        if self.notification_histories:
            for k in self.notification_histories:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        result['NotificationHistories'] = []
        if self.notification_histories is not None:
            for k in self.notification_histories:
                result['NotificationHistories'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        self.notification_histories = []
        if m.get('NotificationHistories') is not None:
            for k in m.get('NotificationHistories'):
                temp_model = ListNotificationHistoriesResponseBodyNotificationHistories()
                self.notification_histories.append(temp_model.from_map(k))
        return self


class ListNotificationHistoriesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListNotificationHistoriesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListNotificationHistoriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDevicePropertyRequest(TeaModel):
    def __init__(
        self,
        device_property_id: str = None,
    ):
        # 实例 ID。
        self.device_property_id = device_property_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.device_property_id is not None:
            result['DevicePropertyId'] = self.device_property_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DevicePropertyId') is not None:
            self.device_property_id = m.get('DevicePropertyId')
        return self


class DeleteDevicePropertyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteDevicePropertyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteDevicePropertyResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteDevicePropertyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDevicePropertiesRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        device_form_id: str = None,
    ):
        # 返回结果的最大个数。
        self.max_results = max_results
        # 当总结果个数大于MaxResults时，用于翻页的token。
        self.next_token = next_token
        # 设备形态ID
        self.device_form_id = device_form_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.device_form_id is not None:
            result['DeviceFormId'] = self.device_form_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('DeviceFormId') is not None:
            self.device_form_id = m.get('DeviceFormId')
        return self


class ListDevicePropertiesResponseBodyDeviceProperties(TeaModel):
    def __init__(
        self,
        device_property_id: str = None,
        device_form_id: str = None,
        device_form_name: str = None,
        property_name: str = None,
        property_key: str = None,
        property_format: str = None,
        property_content: str = None,
        built_in: bool = None,
    ):
        # 设备属性ID
        self.device_property_id = device_property_id
        # 设备形态ID
        self.device_form_id = device_form_id
        # 设备形态名称
        self.device_form_name = device_form_name
        # 属性名称
        self.property_name = property_name
        # 属性主键
        self.property_key = property_key
        # 属性格式
        self.property_format = property_format
        # 属性内容
        self.property_content = property_content
        # 是否内置属性
        self.built_in = built_in

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.device_property_id is not None:
            result['DevicePropertyId'] = self.device_property_id
        if self.device_form_id is not None:
            result['DeviceFormId'] = self.device_form_id
        if self.device_form_name is not None:
            result['DeviceFormName'] = self.device_form_name
        if self.property_name is not None:
            result['PropertyName'] = self.property_name
        if self.property_key is not None:
            result['PropertyKey'] = self.property_key
        if self.property_format is not None:
            result['PropertyFormat'] = self.property_format
        if self.property_content is not None:
            result['PropertyContent'] = self.property_content
        if self.built_in is not None:
            result['BuiltIn'] = self.built_in
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DevicePropertyId') is not None:
            self.device_property_id = m.get('DevicePropertyId')
        if m.get('DeviceFormId') is not None:
            self.device_form_id = m.get('DeviceFormId')
        if m.get('DeviceFormName') is not None:
            self.device_form_name = m.get('DeviceFormName')
        if m.get('PropertyName') is not None:
            self.property_name = m.get('PropertyName')
        if m.get('PropertyKey') is not None:
            self.property_key = m.get('PropertyKey')
        if m.get('PropertyFormat') is not None:
            self.property_format = m.get('PropertyFormat')
        if m.get('PropertyContent') is not None:
            self.property_content = m.get('PropertyContent')
        if m.get('BuiltIn') is not None:
            self.built_in = m.get('BuiltIn')
        return self


class ListDevicePropertiesResponseBody(TeaModel):
    def __init__(
        self,
        device_properties: List[ListDevicePropertiesResponseBodyDeviceProperties] = None,
        next_token: int = None,
        request_id: str = None,
        total_count: int = None,
        max_results: int = None,
    ):
        # 数组，返回示例目录。
        self.device_properties = device_properties
        # 当总结果个数大于MaxResults时，用于翻页的token。
        self.next_token = next_token
        # Id of the request
        self.request_id = request_id
        # 总记录数。
        self.total_count = total_count
        # 每页数量。
        self.max_results = max_results

    def validate(self):
        if self.device_properties:
            for k in self.device_properties:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['DeviceProperties'] = []
        if self.device_properties is not None:
            for k in self.device_properties:
                result['DeviceProperties'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.device_properties = []
        if m.get('DeviceProperties') is not None:
            for k in m.get('DeviceProperties'):
                temp_model = ListDevicePropertiesResponseBodyDeviceProperties()
                self.device_properties.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        return self


class ListDevicePropertiesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListDevicePropertiesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListDevicePropertiesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInspectionTasksRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        item_id: str = None,
        host_name: str = None,
        ip: str = None,
        task_status: str = None,
    ):
        # 返回结果的最大个数。
        self.max_results = max_results
        # 当总结果个数大于MaxResults时，用于翻页的token。
        self.next_token = next_token
        # 巡检项ID
        self.item_id = item_id
        # 主机名
        self.host_name = host_name
        # 设备IP
        self.ip = ip
        # 巡检状态
        self.task_status = task_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        return self


class ListInspectionTasksResponseBodyInspectionTasksInspectionAlarmRules(TeaModel):
    def __init__(
        self,
        alarm_expression: str = None,
        alarm_operator: str = None,
        alarm_value: str = None,
        actual_value: str = None,
        alarm_level: str = None,
    ):
        # 告警符号
        self.alarm_expression = alarm_expression
        # 告警变量
        self.alarm_operator = alarm_operator
        # 告警值
        self.alarm_value = alarm_value
        # 告警实际值
        self.actual_value = actual_value
        # 告警级别
        self.alarm_level = alarm_level

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.alarm_expression is not None:
            result['AlarmExpression'] = self.alarm_expression
        if self.alarm_operator is not None:
            result['AlarmOperator'] = self.alarm_operator
        if self.alarm_value is not None:
            result['AlarmValue'] = self.alarm_value
        if self.actual_value is not None:
            result['ActualValue'] = self.actual_value
        if self.alarm_level is not None:
            result['AlarmLevel'] = self.alarm_level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmExpression') is not None:
            self.alarm_expression = m.get('AlarmExpression')
        if m.get('AlarmOperator') is not None:
            self.alarm_operator = m.get('AlarmOperator')
        if m.get('AlarmValue') is not None:
            self.alarm_value = m.get('AlarmValue')
        if m.get('ActualValue') is not None:
            self.actual_value = m.get('ActualValue')
        if m.get('AlarmLevel') is not None:
            self.alarm_level = m.get('AlarmLevel')
        return self


class ListInspectionTasksResponseBodyInspectionTasks(TeaModel):
    def __init__(
        self,
        device_id: str = None,
        item_id: str = None,
        execution_end_time: str = None,
        execution_begin_time: str = None,
        item_name: str = None,
        script_id: str = None,
        space: str = None,
        inspection_result: str = None,
        inspection_alarm_rules: List[ListInspectionTasksResponseBodyInspectionTasksInspectionAlarmRules] = None,
        ip: str = None,
        host_name: str = None,
        vendor: str = None,
        task_status: str = None,
        model: List[str] = None,
        error_code: str = None,
        inspection_message: str = None,
        task_id: str = None,
    ):
        # 设备ID
        self.device_id = device_id
        # 巡检项ID
        self.item_id = item_id
        # 巡检结束时间
        self.execution_end_time = execution_end_time
        # 巡检开始时间
        self.execution_begin_time = execution_begin_time
        # 巡检项名字
        self.item_name = item_name
        # 模板ID
        self.script_id = script_id
        # 物理空间
        self.space = space
        # 巡检结果
        self.inspection_result = inspection_result
        # 告警规则
        self.inspection_alarm_rules = inspection_alarm_rules
        # IP地址
        self.ip = ip
        # 主机名
        self.host_name = host_name
        # 厂商
        self.vendor = vendor
        # 任务状态
        self.task_status = task_status
        # 型号
        self.model = model
        # 错误码
        self.error_code = error_code
        # 巡检信息
        self.inspection_message = inspection_message
        # 任务ID
        self.task_id = task_id

    def validate(self):
        if self.inspection_alarm_rules:
            for k in self.inspection_alarm_rules:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.execution_end_time is not None:
            result['ExecutionEndTime'] = self.execution_end_time
        if self.execution_begin_time is not None:
            result['ExecutionBeginTime'] = self.execution_begin_time
        if self.item_name is not None:
            result['ItemName'] = self.item_name
        if self.script_id is not None:
            result['ScriptId'] = self.script_id
        if self.space is not None:
            result['Space'] = self.space
        if self.inspection_result is not None:
            result['InspectionResult'] = self.inspection_result
        result['InspectionAlarmRules'] = []
        if self.inspection_alarm_rules is not None:
            for k in self.inspection_alarm_rules:
                result['InspectionAlarmRules'].append(k.to_map() if k else None)
        if self.ip is not None:
            result['IP'] = self.ip
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.vendor is not None:
            result['Vendor'] = self.vendor
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.model is not None:
            result['Model'] = self.model
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.inspection_message is not None:
            result['InspectionMessage'] = self.inspection_message
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('ExecutionEndTime') is not None:
            self.execution_end_time = m.get('ExecutionEndTime')
        if m.get('ExecutionBeginTime') is not None:
            self.execution_begin_time = m.get('ExecutionBeginTime')
        if m.get('ItemName') is not None:
            self.item_name = m.get('ItemName')
        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')
        if m.get('Space') is not None:
            self.space = m.get('Space')
        if m.get('InspectionResult') is not None:
            self.inspection_result = m.get('InspectionResult')
        self.inspection_alarm_rules = []
        if m.get('InspectionAlarmRules') is not None:
            for k in m.get('InspectionAlarmRules'):
                temp_model = ListInspectionTasksResponseBodyInspectionTasksInspectionAlarmRules()
                self.inspection_alarm_rules.append(temp_model.from_map(k))
        if m.get('IP') is not None:
            self.ip = m.get('IP')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('InspectionMessage') is not None:
            self.inspection_message = m.get('InspectionMessage')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class ListInspectionTasksResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        next_token: int = None,
        inspection_tasks: List[ListInspectionTasksResponseBodyInspectionTasks] = None,
    ):
        # 总记录数。
        self.total_count = total_count
        # 请求ID
        self.request_id = request_id
        # 当总结果个数大于MaxResults时，用于翻页的token。
        self.next_token = next_token
        # 数组，返回示例目录。
        self.inspection_tasks = inspection_tasks

    def validate(self):
        if self.inspection_tasks:
            for k in self.inspection_tasks:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        result['InspectionTasks'] = []
        if self.inspection_tasks is not None:
            for k in self.inspection_tasks:
                result['InspectionTasks'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.inspection_tasks = []
        if m.get('InspectionTasks') is not None:
            for k in m.get('InspectionTasks'):
                temp_model = ListInspectionTasksResponseBodyInspectionTasks()
                self.inspection_tasks.append(temp_model.from_map(k))
        return self


class ListInspectionTasksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListInspectionTasksResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListInspectionTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDevicePropertyRequest(TeaModel):
    def __init__(
        self,
        device_property_id: str = None,
        property_key: str = None,
        device_form_id: str = None,
    ):
        # 实例 ID。
        self.device_property_id = device_property_id
        # 属性主键
        self.property_key = property_key
        # 设备形态ID
        self.device_form_id = device_form_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.device_property_id is not None:
            result['DevicePropertyId'] = self.device_property_id
        if self.property_key is not None:
            result['PropertyKey'] = self.property_key
        if self.device_form_id is not None:
            result['DeviceFormId'] = self.device_form_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DevicePropertyId') is not None:
            self.device_property_id = m.get('DevicePropertyId')
        if m.get('PropertyKey') is not None:
            self.property_key = m.get('PropertyKey')
        if m.get('DeviceFormId') is not None:
            self.device_form_id = m.get('DeviceFormId')
        return self


class GetDevicePropertyResponseBodyDeviceProperty(TeaModel):
    def __init__(
        self,
        device_property_id: str = None,
        device_form_id: str = None,
        device_form_name: str = None,
        property_name: str = None,
        property_key: str = None,
        property_format: str = None,
        property_content: str = None,
        built_in: bool = None,
    ):
        # 设备属性ID
        self.device_property_id = device_property_id
        # 设备形态ID
        self.device_form_id = device_form_id
        # 设备形态名称
        self.device_form_name = device_form_name
        # 属性名称
        self.property_name = property_name
        # 属性主键
        self.property_key = property_key
        # 属性格式
        self.property_format = property_format
        # 属性内容
        self.property_content = property_content
        # 是否内置属性
        self.built_in = built_in

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.device_property_id is not None:
            result['DevicePropertyId'] = self.device_property_id
        if self.device_form_id is not None:
            result['DeviceFormId'] = self.device_form_id
        if self.device_form_name is not None:
            result['DeviceFormName'] = self.device_form_name
        if self.property_name is not None:
            result['PropertyName'] = self.property_name
        if self.property_key is not None:
            result['PropertyKey'] = self.property_key
        if self.property_format is not None:
            result['PropertyFormat'] = self.property_format
        if self.property_content is not None:
            result['PropertyContent'] = self.property_content
        if self.built_in is not None:
            result['BuiltIn'] = self.built_in
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DevicePropertyId') is not None:
            self.device_property_id = m.get('DevicePropertyId')
        if m.get('DeviceFormId') is not None:
            self.device_form_id = m.get('DeviceFormId')
        if m.get('DeviceFormName') is not None:
            self.device_form_name = m.get('DeviceFormName')
        if m.get('PropertyName') is not None:
            self.property_name = m.get('PropertyName')
        if m.get('PropertyKey') is not None:
            self.property_key = m.get('PropertyKey')
        if m.get('PropertyFormat') is not None:
            self.property_format = m.get('PropertyFormat')
        if m.get('PropertyContent') is not None:
            self.property_content = m.get('PropertyContent')
        if m.get('BuiltIn') is not None:
            self.built_in = m.get('BuiltIn')
        return self


class GetDevicePropertyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        device_property: GetDevicePropertyResponseBodyDeviceProperty = None,
    ):
        # Id of the request
        self.request_id = request_id
        # 设备属性详情
        self.device_property = device_property

    def validate(self):
        if self.device_property:
            self.device_property.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.device_property is not None:
            result['DeviceProperty'] = self.device_property.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DeviceProperty') is not None:
            temp_model = GetDevicePropertyResponseBodyDeviceProperty()
            self.device_property = temp_model.from_map(m['DeviceProperty'])
        return self


class GetDevicePropertyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetDevicePropertyResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetDevicePropertyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDedicatedLinesRequest(TeaModel):
    def __init__(
        self,
        physical_space_id: str = None,
    ):
        # 物理空间ID
        self.physical_space_id = physical_space_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.physical_space_id is not None:
            result['PhysicalSpaceId'] = self.physical_space_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PhysicalSpaceId') is not None:
            self.physical_space_id = m.get('PhysicalSpaceId')
        return self


class ListDedicatedLinesResponseBodyDedicatedLines(TeaModel):
    def __init__(
        self,
        dedicated_line_id: str = None,
        isp: str = None,
        bandwidth: int = None,
        dedicated_line_ip: str = None,
        dedicated_line_gateway: str = None,
        dedicated_line_role: str = None,
        device_id: str = None,
        device_port: str = None,
        device_name: str = None,
    ):
        # 物理空间专线ID
        self.dedicated_line_id = dedicated_line_id
        # 运营商
        self.isp = isp
        # 宽带（Mbps）
        self.bandwidth = bandwidth
        # 专线IP
        self.dedicated_line_ip = dedicated_line_ip
        # 专线网关
        self.dedicated_line_gateway = dedicated_line_gateway
        # 专线角色
        self.dedicated_line_role = dedicated_line_role
        # 关联设备ID
        self.device_id = device_id
        # 关联设备端口
        self.device_port = device_port
        # 关联设备名称
        self.device_name = device_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.dedicated_line_id is not None:
            result['DedicatedLineId'] = self.dedicated_line_id
        if self.isp is not None:
            result['Isp'] = self.isp
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.dedicated_line_ip is not None:
            result['DedicatedLineIp'] = self.dedicated_line_ip
        if self.dedicated_line_gateway is not None:
            result['DedicatedLineGateway'] = self.dedicated_line_gateway
        if self.dedicated_line_role is not None:
            result['DedicatedLineRole'] = self.dedicated_line_role
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.device_port is not None:
            result['DevicePort'] = self.device_port
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DedicatedLineId') is not None:
            self.dedicated_line_id = m.get('DedicatedLineId')
        if m.get('Isp') is not None:
            self.isp = m.get('Isp')
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('DedicatedLineIp') is not None:
            self.dedicated_line_ip = m.get('DedicatedLineIp')
        if m.get('DedicatedLineGateway') is not None:
            self.dedicated_line_gateway = m.get('DedicatedLineGateway')
        if m.get('DedicatedLineRole') is not None:
            self.dedicated_line_role = m.get('DedicatedLineRole')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('DevicePort') is not None:
            self.device_port = m.get('DevicePort')
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        return self


class ListDedicatedLinesResponseBody(TeaModel):
    def __init__(
        self,
        dedicated_lines: List[ListDedicatedLinesResponseBodyDedicatedLines] = None,
        request_id: str = None,
    ):
        # 数组，返回示例目录。
        self.dedicated_lines = dedicated_lines
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.dedicated_lines:
            for k in self.dedicated_lines:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['DedicatedLines'] = []
        if self.dedicated_lines is not None:
            for k in self.dedicated_lines:
                result['DedicatedLines'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dedicated_lines = []
        if m.get('DedicatedLines') is not None:
            for k in m.get('DedicatedLines'):
                temp_model = ListDedicatedLinesResponseBodyDedicatedLines()
                self.dedicated_lines.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListDedicatedLinesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListDedicatedLinesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListDedicatedLinesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDeviceFormsRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
    ):
        # 返回结果的最大个数。
        self.max_results = max_results
        # 当总结果个数大于MaxResults时，用于翻页的token。
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class ListDeviceFormsResponseBodyDeviceFormsAttributeList(TeaModel):
    def __init__(
        self,
        attribute_key: str = None,
        attribute_name: str = None,
        attribute_requirement: bool = None,
        attribute_uniqueness: bool = None,
        attribute_format: str = None,
        attribute_type: str = None,
        attribute_reference: str = None,
        attribute_table_display: bool = None,
        attribute_placeholder: str = None,
        attribute_query: bool = None,
        attribute_fuzzy_query: bool = None,
        attribute_built_in: bool = None,
    ):
        # 设备形态属性主键
        self.attribute_key = attribute_key
        # 设备形态属性名称
        self.attribute_name = attribute_name
        # 设备形态属性是否必填
        self.attribute_requirement = attribute_requirement
        # 设备形态属性是否唯一
        self.attribute_uniqueness = attribute_uniqueness
        # 设备形态属性值格式
        self.attribute_format = attribute_format
        # 设备形态属性值类型
        self.attribute_type = attribute_type
        # 设备形态属性关联对象
        self.attribute_reference = attribute_reference
        # 设备形态属性是否表格可见
        self.attribute_table_display = attribute_table_display
        # 前端查询控件占位符
        self.attribute_placeholder = attribute_placeholder
        # 前端是否展示对应的查询控件
        self.attribute_query = attribute_query
        # 前端查询控件是否支持模糊搜索
        self.attribute_fuzzy_query = attribute_fuzzy_query
        # 设备形态属性是否内置
        self.attribute_built_in = attribute_built_in

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.attribute_key is not None:
            result['AttributeKey'] = self.attribute_key
        if self.attribute_name is not None:
            result['AttributeName'] = self.attribute_name
        if self.attribute_requirement is not None:
            result['AttributeRequirement'] = self.attribute_requirement
        if self.attribute_uniqueness is not None:
            result['AttributeUniqueness'] = self.attribute_uniqueness
        if self.attribute_format is not None:
            result['AttributeFormat'] = self.attribute_format
        if self.attribute_type is not None:
            result['AttributeType'] = self.attribute_type
        if self.attribute_reference is not None:
            result['AttributeReference'] = self.attribute_reference
        if self.attribute_table_display is not None:
            result['AttributeTableDisplay'] = self.attribute_table_display
        if self.attribute_placeholder is not None:
            result['AttributePlaceholder'] = self.attribute_placeholder
        if self.attribute_query is not None:
            result['AttributeQuery'] = self.attribute_query
        if self.attribute_fuzzy_query is not None:
            result['AttributeFuzzyQuery'] = self.attribute_fuzzy_query
        if self.attribute_built_in is not None:
            result['AttributeBuiltIn'] = self.attribute_built_in
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttributeKey') is not None:
            self.attribute_key = m.get('AttributeKey')
        if m.get('AttributeName') is not None:
            self.attribute_name = m.get('AttributeName')
        if m.get('AttributeRequirement') is not None:
            self.attribute_requirement = m.get('AttributeRequirement')
        if m.get('AttributeUniqueness') is not None:
            self.attribute_uniqueness = m.get('AttributeUniqueness')
        if m.get('AttributeFormat') is not None:
            self.attribute_format = m.get('AttributeFormat')
        if m.get('AttributeType') is not None:
            self.attribute_type = m.get('AttributeType')
        if m.get('AttributeReference') is not None:
            self.attribute_reference = m.get('AttributeReference')
        if m.get('AttributeTableDisplay') is not None:
            self.attribute_table_display = m.get('AttributeTableDisplay')
        if m.get('AttributePlaceholder') is not None:
            self.attribute_placeholder = m.get('AttributePlaceholder')
        if m.get('AttributeQuery') is not None:
            self.attribute_query = m.get('AttributeQuery')
        if m.get('AttributeFuzzyQuery') is not None:
            self.attribute_fuzzy_query = m.get('AttributeFuzzyQuery')
        if m.get('AttributeBuiltIn') is not None:
            self.attribute_built_in = m.get('AttributeBuiltIn')
        return self


class ListDeviceFormsResponseBodyDeviceForms(TeaModel):
    def __init__(
        self,
        config_compare: bool = None,
        attribute_list: List[ListDeviceFormsResponseBodyDeviceFormsAttributeList] = None,
        account_config: bool = None,
        detail_display: bool = None,
        form_built_in: bool = None,
        unique_key: str = None,
        device_form_id: str = None,
        device_form_name: str = None,
    ):
        # 是否支持配置生成
        self.config_compare = config_compare
        # 设备形态属性列表
        self.attribute_list = attribute_list
        # 是否需要账号配置
        self.account_config = account_config
        # 是否展示详情
        self.detail_display = detail_display
        # 设备形态是否内置
        self.form_built_in = form_built_in
        # 设备形态主键
        self.unique_key = unique_key
        # 设备形态ID
        self.device_form_id = device_form_id
        # 设备形态名称
        self.device_form_name = device_form_name

    def validate(self):
        if self.attribute_list:
            for k in self.attribute_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.config_compare is not None:
            result['ConfigCompare'] = self.config_compare
        result['AttributeList'] = []
        if self.attribute_list is not None:
            for k in self.attribute_list:
                result['AttributeList'].append(k.to_map() if k else None)
        if self.account_config is not None:
            result['AccountConfig'] = self.account_config
        if self.detail_display is not None:
            result['DetailDisplay'] = self.detail_display
        if self.form_built_in is not None:
            result['FormBuiltIn'] = self.form_built_in
        if self.unique_key is not None:
            result['UniqueKey'] = self.unique_key
        if self.device_form_id is not None:
            result['DeviceFormId'] = self.device_form_id
        if self.device_form_name is not None:
            result['DeviceFormName'] = self.device_form_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigCompare') is not None:
            self.config_compare = m.get('ConfigCompare')
        self.attribute_list = []
        if m.get('AttributeList') is not None:
            for k in m.get('AttributeList'):
                temp_model = ListDeviceFormsResponseBodyDeviceFormsAttributeList()
                self.attribute_list.append(temp_model.from_map(k))
        if m.get('AccountConfig') is not None:
            self.account_config = m.get('AccountConfig')
        if m.get('DetailDisplay') is not None:
            self.detail_display = m.get('DetailDisplay')
        if m.get('FormBuiltIn') is not None:
            self.form_built_in = m.get('FormBuiltIn')
        if m.get('UniqueKey') is not None:
            self.unique_key = m.get('UniqueKey')
        if m.get('DeviceFormId') is not None:
            self.device_form_id = m.get('DeviceFormId')
        if m.get('DeviceFormName') is not None:
            self.device_form_name = m.get('DeviceFormName')
        return self


class ListDeviceFormsResponseBody(TeaModel):
    def __init__(
        self,
        device_forms: List[ListDeviceFormsResponseBodyDeviceForms] = None,
        total_count: int = None,
        request_id: str = None,
        next_token: int = None,
        max_results: int = None,
    ):
        # 数组，返回示例目录。
        self.device_forms = device_forms
        # 总记录数。
        self.total_count = total_count
        # Id of the request
        self.request_id = request_id
        # 当总结果个数大于MaxResults时，用于翻页的token。
        self.next_token = next_token
        # 每页数量。
        self.max_results = max_results

    def validate(self):
        if self.device_forms:
            for k in self.device_forms:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['DeviceForms'] = []
        if self.device_forms is not None:
            for k in self.device_forms:
                result['DeviceForms'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.device_forms = []
        if m.get('DeviceForms') is not None:
            for k in m.get('DeviceForms'):
                temp_model = ListDeviceFormsResponseBodyDeviceForms()
                self.device_forms.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        return self


class ListDeviceFormsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListDeviceFormsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListDeviceFormsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRealtimeTaskRequest(TeaModel):
    def __init__(
        self,
        task_id: str = None,
    ):
        # 实时任务ID
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class GetRealtimeTaskResponseBodyInspectionTask(TeaModel):
    def __init__(
        self,
        task_status: str = None,
        inspection_result: str = None,
        error_code: str = None,
        inspection_message: str = None,
    ):
        # 巡检状态
        self.task_status = task_status
        # 巡检输出
        self.inspection_result = inspection_result
        # 巡检错误码
        self.error_code = error_code
        # 巡检错误信息
        self.inspection_message = inspection_message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.inspection_result is not None:
            result['InspectionResult'] = self.inspection_result
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.inspection_message is not None:
            result['InspectionMessage'] = self.inspection_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('InspectionResult') is not None:
            self.inspection_result = m.get('InspectionResult')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('InspectionMessage') is not None:
            self.inspection_message = m.get('InspectionMessage')
        return self


class GetRealtimeTaskResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        inspection_task: GetRealtimeTaskResponseBodyInspectionTask = None,
    ):
        # 请求ID
        self.request_id = request_id
        # 请求任务结果
        self.inspection_task = inspection_task

    def validate(self):
        if self.inspection_task:
            self.inspection_task.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.inspection_task is not None:
            result['InspectionTask'] = self.inspection_task.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('InspectionTask') is not None:
            temp_model = GetRealtimeTaskResponseBodyInspectionTask()
            self.inspection_task = temp_model.from_map(m['InspectionTask'])
        return self


class GetRealtimeTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetRealtimeTaskResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetRealtimeTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAlarmStatusHistoriesRequest(TeaModel):
    def __init__(
        self,
        start: int = None,
        end: int = None,
        device_id: str = None,
        monitor_item_id: str = None,
        type: str = None,
        aggregate_data_id: str = None,
        dedicated_line_id: str = None,
    ):
        # 开始时间秒级时间戳
        self.start = start
        # 结束时间秒级时间戳
        self.end = end
        # 设备ID
        self.device_id = device_id
        # 监控项ID
        self.monitor_item_id = monitor_item_id
        # 类型
        self.type = type
        # 聚合数据ID
        self.aggregate_data_id = aggregate_data_id
        # 专线ID
        self.dedicated_line_id = dedicated_line_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.start is not None:
            result['Start'] = self.start
        if self.end is not None:
            result['End'] = self.end
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.monitor_item_id is not None:
            result['MonitorItemId'] = self.monitor_item_id
        if self.type is not None:
            result['Type'] = self.type
        if self.aggregate_data_id is not None:
            result['AggregateDataId'] = self.aggregate_data_id
        if self.dedicated_line_id is not None:
            result['DedicatedLineId'] = self.dedicated_line_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Start') is not None:
            self.start = m.get('Start')
        if m.get('End') is not None:
            self.end = m.get('End')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('MonitorItemId') is not None:
            self.monitor_item_id = m.get('MonitorItemId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('AggregateDataId') is not None:
            self.aggregate_data_id = m.get('AggregateDataId')
        if m.get('DedicatedLineId') is not None:
            self.dedicated_line_id = m.get('DedicatedLineId')
        return self


class ListAlarmStatusHistoriesResponseBodyAlarmStatusHistories(TeaModel):
    def __init__(
        self,
        timestamp: int = None,
        value: str = None,
    ):
        # 时间戳
        self.timestamp = timestamp
        # 数值
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListAlarmStatusHistoriesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        alarm_status_histories: List[ListAlarmStatusHistoriesResponseBodyAlarmStatusHistories] = None,
    ):
        # request id
        self.request_id = request_id
        # 数据列表
        self.alarm_status_histories = alarm_status_histories

    def validate(self):
        if self.alarm_status_histories:
            for k in self.alarm_status_histories:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['AlarmStatusHistories'] = []
        if self.alarm_status_histories is not None:
            for k in self.alarm_status_histories:
                result['AlarmStatusHistories'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.alarm_status_histories = []
        if m.get('AlarmStatusHistories') is not None:
            for k in m.get('AlarmStatusHistories'):
                temp_model = ListAlarmStatusHistoriesResponseBodyAlarmStatusHistories()
                self.alarm_status_histories.append(temp_model.from_map(k))
        return self


class ListAlarmStatusHistoriesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListAlarmStatusHistoriesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListAlarmStatusHistoriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDeviceFormRequest(TeaModel):
    def __init__(
        self,
        device_form_name: str = None,
        config_compare: bool = None,
        account_config: bool = None,
        detail_display: bool = None,
        unique_key: str = None,
        client_token: str = None,
    ):
        # 设备形态名称
        self.device_form_name = device_form_name
        # 是否支持配置生成
        self.config_compare = config_compare
        # 是否需要账号配置
        self.account_config = account_config
        # 是否展示设备详情
        self.detail_display = detail_display
        # 设备形态的主键
        self.unique_key = unique_key
        # 幂等校验 token
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.device_form_name is not None:
            result['DeviceFormName'] = self.device_form_name
        if self.config_compare is not None:
            result['ConfigCompare'] = self.config_compare
        if self.account_config is not None:
            result['AccountConfig'] = self.account_config
        if self.detail_display is not None:
            result['DetailDisplay'] = self.detail_display
        if self.unique_key is not None:
            result['UniqueKey'] = self.unique_key
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceFormName') is not None:
            self.device_form_name = m.get('DeviceFormName')
        if m.get('ConfigCompare') is not None:
            self.config_compare = m.get('ConfigCompare')
        if m.get('AccountConfig') is not None:
            self.account_config = m.get('AccountConfig')
        if m.get('DetailDisplay') is not None:
            self.detail_display = m.get('DetailDisplay')
        if m.get('UniqueKey') is not None:
            self.unique_key = m.get('UniqueKey')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class CreateDeviceFormResponseBody(TeaModel):
    def __init__(
        self,
        device_form_id: str = None,
        request_id: str = None,
    ):
        # 资源实例ID，如ECS实例的创建接口CreateInstance应返回InstanceId。
        self.device_form_id = device_form_id
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.device_form_id is not None:
            result['DeviceFormId'] = self.device_form_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceFormId') is not None:
            self.device_form_id = m.get('DeviceFormId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateDeviceFormResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateDeviceFormResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateDeviceFormResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPhysicalSpacesRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        physical_space_ids: List[str] = None,
        physical_space_name: str = None,
    ):
        # 返回结果的最大个数。
        self.max_results = max_results
        # 当总结果个数大于MaxResults时，用于翻页的token。
        self.next_token = next_token
        # 物理空间ID
        self.physical_space_ids = physical_space_ids
        # 物理空间名称，支持模糊搜索。
        self.physical_space_name = physical_space_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.physical_space_ids is not None:
            result['PhysicalSpaceIds'] = self.physical_space_ids
        if self.physical_space_name is not None:
            result['PhysicalSpaceName'] = self.physical_space_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('PhysicalSpaceIds') is not None:
            self.physical_space_ids = m.get('PhysicalSpaceIds')
        if m.get('PhysicalSpaceName') is not None:
            self.physical_space_name = m.get('PhysicalSpaceName')
        return self


class ListPhysicalSpacesResponseBodyPhysicalSpaces(TeaModel):
    def __init__(
        self,
        physical_space_id: str = None,
        physical_space_name: str = None,
        country: str = None,
        province: str = None,
        city: str = None,
        address: str = None,
    ):
        # 物理空间ID
        self.physical_space_id = physical_space_id
        # 物理空间名称
        self.physical_space_name = physical_space_name
        # 所属国家
        self.country = country
        # 所属省份
        self.province = province
        # 所属城市
        self.city = city
        # 具体地址
        self.address = address

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.physical_space_id is not None:
            result['PhysicalSpaceId'] = self.physical_space_id
        if self.physical_space_name is not None:
            result['PhysicalSpaceName'] = self.physical_space_name
        if self.country is not None:
            result['Country'] = self.country
        if self.province is not None:
            result['Province'] = self.province
        if self.city is not None:
            result['City'] = self.city
        if self.address is not None:
            result['Address'] = self.address
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PhysicalSpaceId') is not None:
            self.physical_space_id = m.get('PhysicalSpaceId')
        if m.get('PhysicalSpaceName') is not None:
            self.physical_space_name = m.get('PhysicalSpaceName')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('Address') is not None:
            self.address = m.get('Address')
        return self


class ListPhysicalSpacesResponseBody(TeaModel):
    def __init__(
        self,
        next_token: int = None,
        physical_spaces: List[ListPhysicalSpacesResponseBodyPhysicalSpaces] = None,
        request_id: str = None,
        total_count: int = None,
        max_results: int = None,
    ):
        # 当总结果个数大于MaxResults时，用于翻页的token。
        self.next_token = next_token
        # 数组，返回示例目录。
        self.physical_spaces = physical_spaces
        # Id of the request
        self.request_id = request_id
        # 总记录数。
        self.total_count = total_count
        # 每页数量。
        self.max_results = max_results

    def validate(self):
        if self.physical_spaces:
            for k in self.physical_spaces:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        result['PhysicalSpaces'] = []
        if self.physical_spaces is not None:
            for k in self.physical_spaces:
                result['PhysicalSpaces'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.physical_spaces = []
        if m.get('PhysicalSpaces') is not None:
            for k in m.get('PhysicalSpaces'):
                temp_model = ListPhysicalSpacesResponseBodyPhysicalSpaces()
                self.physical_spaces.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        return self


class ListPhysicalSpacesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListPhysicalSpacesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListPhysicalSpacesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListMonitorDataRequest(TeaModel):
    def __init__(
        self,
        start: int = None,
        end: int = None,
        data_type: str = None,
        data_item: str = None,
        monitor_item_id: str = None,
        device_id: str = None,
        key: str = None,
        aggregate_data_id: str = None,
        port_collection_id: str = None,
        dedicated_line_id: str = None,
    ):
        # 开始时间
        self.start = start
        # 结束时间
        self.end = end
        # 数据类型
        self.data_type = data_type
        # 数据项
        self.data_item = data_item
        # 监控项ID
        self.monitor_item_id = monitor_item_id
        # 设备ID
        self.device_id = device_id
        # key
        self.key = key
        # 聚合数据ID
        self.aggregate_data_id = aggregate_data_id
        # 端口集ID
        self.port_collection_id = port_collection_id
        # 专线ID
        self.dedicated_line_id = dedicated_line_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.start is not None:
            result['Start'] = self.start
        if self.end is not None:
            result['End'] = self.end
        if self.data_type is not None:
            result['DataType'] = self.data_type
        if self.data_item is not None:
            result['DataItem'] = self.data_item
        if self.monitor_item_id is not None:
            result['MonitorItemId'] = self.monitor_item_id
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.key is not None:
            result['Key'] = self.key
        if self.aggregate_data_id is not None:
            result['AggregateDataId'] = self.aggregate_data_id
        if self.port_collection_id is not None:
            result['PortCollectionId'] = self.port_collection_id
        if self.dedicated_line_id is not None:
            result['DedicatedLineId'] = self.dedicated_line_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Start') is not None:
            self.start = m.get('Start')
        if m.get('End') is not None:
            self.end = m.get('End')
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        if m.get('DataItem') is not None:
            self.data_item = m.get('DataItem')
        if m.get('MonitorItemId') is not None:
            self.monitor_item_id = m.get('MonitorItemId')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('AggregateDataId') is not None:
            self.aggregate_data_id = m.get('AggregateDataId')
        if m.get('PortCollectionId') is not None:
            self.port_collection_id = m.get('PortCollectionId')
        if m.get('DedicatedLineId') is not None:
            self.dedicated_line_id = m.get('DedicatedLineId')
        return self


class ListMonitorDataResponseBodyMonitorData(TeaModel):
    def __init__(
        self,
        timestamp: int = None,
        value: str = None,
        data_item: str = None,
        key: str = None,
    ):
        # 时间戳
        self.timestamp = timestamp
        # 数值
        self.value = value
        # 数据项
        self.data_item = data_item
        # key
        self.key = key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.value is not None:
            result['Value'] = self.value
        if self.data_item is not None:
            result['DataItem'] = self.data_item
        if self.key is not None:
            result['Key'] = self.key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('DataItem') is not None:
            self.data_item = m.get('DataItem')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        return self


class ListMonitorDataResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        monitor_data: List[ListMonitorDataResponseBodyMonitorData] = None,
    ):
        # Request Id
        self.request_id = request_id
        # 数据列表
        self.monitor_data = monitor_data

    def validate(self):
        if self.monitor_data:
            for k in self.monitor_data:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['MonitorData'] = []
        if self.monitor_data is not None:
            for k in self.monitor_data:
                result['MonitorData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.monitor_data = []
        if m.get('MonitorData') is not None:
            for k in m.get('MonitorData'):
                temp_model = ListMonitorDataResponseBodyMonitorData()
                self.monitor_data.append(temp_model.from_map(k))
        return self


class ListMonitorDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListMonitorDataResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListMonitorDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRealtimeTaskRequest(TeaModel):
    def __init__(
        self,
        device_id: str = None,
        script: str = None,
    ):
        # 设备ID
        self.device_id = device_id
        # 模板执行脚本
        self.script = script

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.script is not None:
            result['Script'] = self.script
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('Script') is not None:
            self.script = m.get('Script')
        return self


class CreateRealtimeTaskResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task_id: str = None,
    ):
        # 请求ID
        self.request_id = request_id
        # 实时任务ID
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CreateRealtimeTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateRealtimeTaskResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateRealtimeTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDeviceFormRequest(TeaModel):
    def __init__(
        self,
        device_form_id: str = None,
    ):
        # 实例 ID。
        self.device_form_id = device_form_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.device_form_id is not None:
            result['DeviceFormId'] = self.device_form_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceFormId') is not None:
            self.device_form_id = m.get('DeviceFormId')
        return self


class GetDeviceFormResponseBodyDeviceFormAttributeList(TeaModel):
    def __init__(
        self,
        attribute_key: str = None,
        attribute_name: str = None,
        attribute_requirement: bool = None,
        attribute_uniqueness: bool = None,
        attribute_format: str = None,
        attribute_type: str = None,
        attribute_reference: str = None,
        attribute_table_display: bool = None,
        attribute_placeholder: str = None,
        attribute_query: bool = None,
        attribute_fuzzy_query: bool = None,
        attribute_built_in: bool = None,
    ):
        # 设备形态属性主键
        self.attribute_key = attribute_key
        # 设备形态属性名称
        self.attribute_name = attribute_name
        # 设备形态属性是否必填
        self.attribute_requirement = attribute_requirement
        # 设备形态属性是否唯一
        self.attribute_uniqueness = attribute_uniqueness
        # 设备形态属性值格式
        self.attribute_format = attribute_format
        # 设备形态属性值类型
        self.attribute_type = attribute_type
        # 设备形态属性关联对象
        self.attribute_reference = attribute_reference
        # 设备形态属性是否表格可见
        self.attribute_table_display = attribute_table_display
        # 前端查询控件占位符
        self.attribute_placeholder = attribute_placeholder
        # 前端是否展示对应的查询控件
        self.attribute_query = attribute_query
        # 前端查询控件是否支持模糊搜索
        self.attribute_fuzzy_query = attribute_fuzzy_query
        # 设备形态属性是否内置
        self.attribute_built_in = attribute_built_in

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.attribute_key is not None:
            result['AttributeKey'] = self.attribute_key
        if self.attribute_name is not None:
            result['AttributeName'] = self.attribute_name
        if self.attribute_requirement is not None:
            result['AttributeRequirement'] = self.attribute_requirement
        if self.attribute_uniqueness is not None:
            result['AttributeUniqueness'] = self.attribute_uniqueness
        if self.attribute_format is not None:
            result['AttributeFormat'] = self.attribute_format
        if self.attribute_type is not None:
            result['AttributeType'] = self.attribute_type
        if self.attribute_reference is not None:
            result['AttributeReference'] = self.attribute_reference
        if self.attribute_table_display is not None:
            result['AttributeTableDisplay'] = self.attribute_table_display
        if self.attribute_placeholder is not None:
            result['AttributePlaceholder'] = self.attribute_placeholder
        if self.attribute_query is not None:
            result['AttributeQuery'] = self.attribute_query
        if self.attribute_fuzzy_query is not None:
            result['AttributeFuzzyQuery'] = self.attribute_fuzzy_query
        if self.attribute_built_in is not None:
            result['AttributeBuiltIn'] = self.attribute_built_in
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttributeKey') is not None:
            self.attribute_key = m.get('AttributeKey')
        if m.get('AttributeName') is not None:
            self.attribute_name = m.get('AttributeName')
        if m.get('AttributeRequirement') is not None:
            self.attribute_requirement = m.get('AttributeRequirement')
        if m.get('AttributeUniqueness') is not None:
            self.attribute_uniqueness = m.get('AttributeUniqueness')
        if m.get('AttributeFormat') is not None:
            self.attribute_format = m.get('AttributeFormat')
        if m.get('AttributeType') is not None:
            self.attribute_type = m.get('AttributeType')
        if m.get('AttributeReference') is not None:
            self.attribute_reference = m.get('AttributeReference')
        if m.get('AttributeTableDisplay') is not None:
            self.attribute_table_display = m.get('AttributeTableDisplay')
        if m.get('AttributePlaceholder') is not None:
            self.attribute_placeholder = m.get('AttributePlaceholder')
        if m.get('AttributeQuery') is not None:
            self.attribute_query = m.get('AttributeQuery')
        if m.get('AttributeFuzzyQuery') is not None:
            self.attribute_fuzzy_query = m.get('AttributeFuzzyQuery')
        if m.get('AttributeBuiltIn') is not None:
            self.attribute_built_in = m.get('AttributeBuiltIn')
        return self


class GetDeviceFormResponseBodyDeviceForm(TeaModel):
    def __init__(
        self,
        config_compare: bool = None,
        attribute_list: List[GetDeviceFormResponseBodyDeviceFormAttributeList] = None,
        device_form_id: str = None,
        device_form_name: str = None,
        form_built_in: bool = None,
        account_config: bool = None,
        detail_display: bool = None,
        unique_key: str = None,
    ):
        # 是否支持配置生成
        self.config_compare = config_compare
        # 设备形态属性列表
        self.attribute_list = attribute_list
        # 设备形态ID
        self.device_form_id = device_form_id
        # 设备形态名称
        self.device_form_name = device_form_name
        # 设备形态是否内置
        self.form_built_in = form_built_in
        # 是否需要账号配置
        self.account_config = account_config
        # 是否展示设备详情
        self.detail_display = detail_display
        # 设备形态主键
        self.unique_key = unique_key

    def validate(self):
        if self.attribute_list:
            for k in self.attribute_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.config_compare is not None:
            result['ConfigCompare'] = self.config_compare
        result['AttributeList'] = []
        if self.attribute_list is not None:
            for k in self.attribute_list:
                result['AttributeList'].append(k.to_map() if k else None)
        if self.device_form_id is not None:
            result['DeviceFormId'] = self.device_form_id
        if self.device_form_name is not None:
            result['DeviceFormName'] = self.device_form_name
        if self.form_built_in is not None:
            result['FormBuiltIn'] = self.form_built_in
        if self.account_config is not None:
            result['AccountConfig'] = self.account_config
        if self.detail_display is not None:
            result['DetailDisplay'] = self.detail_display
        if self.unique_key is not None:
            result['UniqueKey'] = self.unique_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigCompare') is not None:
            self.config_compare = m.get('ConfigCompare')
        self.attribute_list = []
        if m.get('AttributeList') is not None:
            for k in m.get('AttributeList'):
                temp_model = GetDeviceFormResponseBodyDeviceFormAttributeList()
                self.attribute_list.append(temp_model.from_map(k))
        if m.get('DeviceFormId') is not None:
            self.device_form_id = m.get('DeviceFormId')
        if m.get('DeviceFormName') is not None:
            self.device_form_name = m.get('DeviceFormName')
        if m.get('FormBuiltIn') is not None:
            self.form_built_in = m.get('FormBuiltIn')
        if m.get('AccountConfig') is not None:
            self.account_config = m.get('AccountConfig')
        if m.get('DetailDisplay') is not None:
            self.detail_display = m.get('DetailDisplay')
        if m.get('UniqueKey') is not None:
            self.unique_key = m.get('UniqueKey')
        return self


class GetDeviceFormResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        device_form: GetDeviceFormResponseBodyDeviceForm = None,
    ):
        # Id of the request
        self.request_id = request_id
        # 设备详情
        self.device_form = device_form

    def validate(self):
        if self.device_form:
            self.device_form.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.device_form is not None:
            result['DeviceForm'] = self.device_form.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DeviceForm') is not None:
            temp_model = GetDeviceFormResponseBodyDeviceForm()
            self.device_form = temp_model.from_map(m['DeviceForm'])
        return self


class GetDeviceFormResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetDeviceFormResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetDeviceFormResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDeviceRequest(TeaModel):
    def __init__(
        self,
        device_form_id: str = None,
        physical_space_id: str = None,
        host_name: str = None,
        ip: str = None,
        sn: str = None,
        mac: str = None,
        vendor: str = None,
        model: str = None,
        service_status: str = None,
        security_domain: str = None,
        login_type: str = None,
        login_username: str = None,
        login_password: str = None,
        snmp_account_version: str = None,
        snmp_community: str = None,
        snmp_account_type: str = None,
        snmp_security_level: str = None,
        snmp_username: str = None,
        snmp_auth_passphrase: str = None,
        snmp_auth_protocol: str = None,
        snmp_privacy_passphase: str = None,
        snmp_privacy_protocol: str = None,
        ext_attributes: str = None,
        client_token: str = None,
    ):
        # 设备形态ID
        self.device_form_id = device_form_id
        # 物理空间ID
        self.physical_space_id = physical_space_id
        # 主机名
        self.host_name = host_name
        # 设备IP
        self.ip = ip
        # 设备SN
        self.sn = sn
        # 设备MAC地址
        self.mac = mac
        # 设备厂商
        self.vendor = vendor
        # 设备型号
        self.model = model
        # 设备状态
        self.service_status = service_status
        # 设备安全域
        self.security_domain = security_domain
        # 登录类型
        self.login_type = login_type
        # 登录账号
        self.login_username = login_username
        # 登录密码
        self.login_password = login_password
        # SNMP 版本号
        self.snmp_account_version = snmp_account_version
        # SNMP Community
        self.snmp_community = snmp_community
        # SNMP 账号类型
        self.snmp_account_type = snmp_account_type
        # SNMP 安全级别
        self.snmp_security_level = snmp_security_level
        # SNMP 用户名
        self.snmp_username = snmp_username
        # SNMP Auth PassPhrase
        self.snmp_auth_passphrase = snmp_auth_passphrase
        # SNMP Auth Protocol
        self.snmp_auth_protocol = snmp_auth_protocol
        # SNMP Privacy Passphase
        self.snmp_privacy_passphase = snmp_privacy_passphase
        # SNMP Privacy Protocol
        self.snmp_privacy_protocol = snmp_privacy_protocol
        # 设备额外属性
        self.ext_attributes = ext_attributes
        # 幂等校验 token
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.device_form_id is not None:
            result['DeviceFormId'] = self.device_form_id
        if self.physical_space_id is not None:
            result['PhysicalSpaceId'] = self.physical_space_id
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.sn is not None:
            result['Sn'] = self.sn
        if self.mac is not None:
            result['Mac'] = self.mac
        if self.vendor is not None:
            result['Vendor'] = self.vendor
        if self.model is not None:
            result['Model'] = self.model
        if self.service_status is not None:
            result['ServiceStatus'] = self.service_status
        if self.security_domain is not None:
            result['SecurityDomain'] = self.security_domain
        if self.login_type is not None:
            result['LoginType'] = self.login_type
        if self.login_username is not None:
            result['LoginUsername'] = self.login_username
        if self.login_password is not None:
            result['LoginPassword'] = self.login_password
        if self.snmp_account_version is not None:
            result['SnmpAccountVersion'] = self.snmp_account_version
        if self.snmp_community is not None:
            result['SnmpCommunity'] = self.snmp_community
        if self.snmp_account_type is not None:
            result['SnmpAccountType'] = self.snmp_account_type
        if self.snmp_security_level is not None:
            result['SnmpSecurityLevel'] = self.snmp_security_level
        if self.snmp_username is not None:
            result['SnmpUsername'] = self.snmp_username
        if self.snmp_auth_passphrase is not None:
            result['SnmpAuthPassphrase'] = self.snmp_auth_passphrase
        if self.snmp_auth_protocol is not None:
            result['SnmpAuthProtocol'] = self.snmp_auth_protocol
        if self.snmp_privacy_passphase is not None:
            result['SnmpPrivacyPassphase'] = self.snmp_privacy_passphase
        if self.snmp_privacy_protocol is not None:
            result['SnmpPrivacyProtocol'] = self.snmp_privacy_protocol
        if self.ext_attributes is not None:
            result['ExtAttributes'] = self.ext_attributes
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceFormId') is not None:
            self.device_form_id = m.get('DeviceFormId')
        if m.get('PhysicalSpaceId') is not None:
            self.physical_space_id = m.get('PhysicalSpaceId')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Sn') is not None:
            self.sn = m.get('Sn')
        if m.get('Mac') is not None:
            self.mac = m.get('Mac')
        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('ServiceStatus') is not None:
            self.service_status = m.get('ServiceStatus')
        if m.get('SecurityDomain') is not None:
            self.security_domain = m.get('SecurityDomain')
        if m.get('LoginType') is not None:
            self.login_type = m.get('LoginType')
        if m.get('LoginUsername') is not None:
            self.login_username = m.get('LoginUsername')
        if m.get('LoginPassword') is not None:
            self.login_password = m.get('LoginPassword')
        if m.get('SnmpAccountVersion') is not None:
            self.snmp_account_version = m.get('SnmpAccountVersion')
        if m.get('SnmpCommunity') is not None:
            self.snmp_community = m.get('SnmpCommunity')
        if m.get('SnmpAccountType') is not None:
            self.snmp_account_type = m.get('SnmpAccountType')
        if m.get('SnmpSecurityLevel') is not None:
            self.snmp_security_level = m.get('SnmpSecurityLevel')
        if m.get('SnmpUsername') is not None:
            self.snmp_username = m.get('SnmpUsername')
        if m.get('SnmpAuthPassphrase') is not None:
            self.snmp_auth_passphrase = m.get('SnmpAuthPassphrase')
        if m.get('SnmpAuthProtocol') is not None:
            self.snmp_auth_protocol = m.get('SnmpAuthProtocol')
        if m.get('SnmpPrivacyPassphase') is not None:
            self.snmp_privacy_passphase = m.get('SnmpPrivacyPassphase')
        if m.get('SnmpPrivacyProtocol') is not None:
            self.snmp_privacy_protocol = m.get('SnmpPrivacyProtocol')
        if m.get('ExtAttributes') is not None:
            self.ext_attributes = m.get('ExtAttributes')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class CreateDeviceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        device_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        # 资源实例ID，如ECS实例的创建接口CreateInstance应返回InstanceId。
        self.device_id = device_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        return self


class CreateDeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateDeviceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDedicatedLineRequest(TeaModel):
    def __init__(
        self,
        dedicated_line_id: str = None,
        isp: str = None,
        bandwidth: int = None,
        dedicated_line_ip: str = None,
        dedicated_line_gateway: str = None,
        dedicated_line_role: str = None,
        device_id: str = None,
        device_port: str = None,
    ):
        # 实例 ID。
        self.dedicated_line_id = dedicated_line_id
        # 运营商
        self.isp = isp
        # 宽带（Mbps）
        self.bandwidth = bandwidth
        # 专线IP
        self.dedicated_line_ip = dedicated_line_ip
        # 专线网关
        self.dedicated_line_gateway = dedicated_line_gateway
        # 专线角色
        self.dedicated_line_role = dedicated_line_role
        # 关联设备ID
        self.device_id = device_id
        # 关联设备端口名称
        self.device_port = device_port

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.dedicated_line_id is not None:
            result['DedicatedLineId'] = self.dedicated_line_id
        if self.isp is not None:
            result['Isp'] = self.isp
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.dedicated_line_ip is not None:
            result['DedicatedLineIp'] = self.dedicated_line_ip
        if self.dedicated_line_gateway is not None:
            result['DedicatedLineGateway'] = self.dedicated_line_gateway
        if self.dedicated_line_role is not None:
            result['DedicatedLineRole'] = self.dedicated_line_role
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.device_port is not None:
            result['DevicePort'] = self.device_port
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DedicatedLineId') is not None:
            self.dedicated_line_id = m.get('DedicatedLineId')
        if m.get('Isp') is not None:
            self.isp = m.get('Isp')
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('DedicatedLineIp') is not None:
            self.dedicated_line_ip = m.get('DedicatedLineIp')
        if m.get('DedicatedLineGateway') is not None:
            self.dedicated_line_gateway = m.get('DedicatedLineGateway')
        if m.get('DedicatedLineRole') is not None:
            self.dedicated_line_role = m.get('DedicatedLineRole')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('DevicePort') is not None:
            self.device_port = m.get('DevicePort')
        return self


class UpdateDedicatedLineResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateDedicatedLineResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateDedicatedLineResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateDedicatedLineResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteInspectionTaskRequest(TeaModel):
    def __init__(
        self,
        task_id: str = None,
    ):
        # 周期性任务的ID
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DeleteInspectionTaskResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # 请求ID
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteInspectionTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteInspectionTaskResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteInspectionTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdatePhysicalSpaceRequest(TeaModel):
    def __init__(
        self,
        physical_space_id: str = None,
        physical_space_name: str = None,
        country: str = None,
        province: str = None,
        city: str = None,
        address: str = None,
    ):
        # 实例 ID。
        self.physical_space_id = physical_space_id
        # 物理空间名称
        self.physical_space_name = physical_space_name
        # 所属国家
        self.country = country
        # 所属省份
        self.province = province
        # 所属城市
        self.city = city
        # 具体地址
        self.address = address

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.physical_space_id is not None:
            result['PhysicalSpaceId'] = self.physical_space_id
        if self.physical_space_name is not None:
            result['PhysicalSpaceName'] = self.physical_space_name
        if self.country is not None:
            result['Country'] = self.country
        if self.province is not None:
            result['Province'] = self.province
        if self.city is not None:
            result['City'] = self.city
        if self.address is not None:
            result['Address'] = self.address
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PhysicalSpaceId') is not None:
            self.physical_space_id = m.get('PhysicalSpaceId')
        if m.get('PhysicalSpaceName') is not None:
            self.physical_space_name = m.get('PhysicalSpaceName')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('Address') is not None:
            self.address = m.get('Address')
        return self


class UpdatePhysicalSpaceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdatePhysicalSpaceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdatePhysicalSpaceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdatePhysicalSpaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAlarmStatusRequest(TeaModel):
    def __init__(
        self,
        device_id: str = None,
        monitor_item_id: str = None,
        type: str = None,
        aggregate_data_id: str = None,
        dedicated_line_id: str = None,
    ):
        # 设备ID
        self.device_id = device_id
        # 监控项ID
        self.monitor_item_id = monitor_item_id
        # 数据类型
        self.type = type
        # 聚合数据ID
        self.aggregate_data_id = aggregate_data_id
        # 专线ID
        self.dedicated_line_id = dedicated_line_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.monitor_item_id is not None:
            result['MonitorItemId'] = self.monitor_item_id
        if self.type is not None:
            result['Type'] = self.type
        if self.aggregate_data_id is not None:
            result['AggregateDataId'] = self.aggregate_data_id
        if self.dedicated_line_id is not None:
            result['DedicatedLineId'] = self.dedicated_line_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('MonitorItemId') is not None:
            self.monitor_item_id = m.get('MonitorItemId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('AggregateDataId') is not None:
            self.aggregate_data_id = m.get('AggregateDataId')
        if m.get('DedicatedLineId') is not None:
            self.dedicated_line_id = m.get('DedicatedLineId')
        return self


class GetAlarmStatusResponseBodyAlarmStatusResourceDevice(TeaModel):
    def __init__(
        self,
        host_name: str = None,
        ip: str = None,
        vendor: str = None,
        model: str = None,
        status: str = None,
        sn: str = None,
        space: str = None,
        device_id: str = None,
        security_domain: str = None,
        device_form: str = None,
    ):
        # 设备名
        self.host_name = host_name
        # IP
        self.ip = ip
        # 厂商
        self.vendor = vendor
        # 型号
        self.model = model
        # 状态
        self.status = status
        # sn
        self.sn = sn
        # 物理空间
        self.space = space
        # 设备ID
        self.device_id = device_id
        # 安全域
        self.security_domain = security_domain
        # 设备形态
        self.device_form = device_form

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.vendor is not None:
            result['Vendor'] = self.vendor
        if self.model is not None:
            result['Model'] = self.model
        if self.status is not None:
            result['Status'] = self.status
        if self.sn is not None:
            result['Sn'] = self.sn
        if self.space is not None:
            result['Space'] = self.space
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.security_domain is not None:
            result['SecurityDomain'] = self.security_domain
        if self.device_form is not None:
            result['DeviceForm'] = self.device_form
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Sn') is not None:
            self.sn = m.get('Sn')
        if m.get('Space') is not None:
            self.space = m.get('Space')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('SecurityDomain') is not None:
            self.security_domain = m.get('SecurityDomain')
        if m.get('DeviceForm') is not None:
            self.device_form = m.get('DeviceForm')
        return self


class GetAlarmStatusResponseBodyAlarmStatusMonitorItem(TeaModel):
    def __init__(
        self,
        monitor_item_name: str = None,
        monitor_item_description: str = None,
        security_domain: str = None,
        collection_type: str = None,
        exec_interval: str = None,
        monitor_item_id: str = None,
        device_form: str = None,
        effective: int = None,
    ):
        # 监控项名称
        self.monitor_item_name = monitor_item_name
        # 描述
        self.monitor_item_description = monitor_item_description
        # 安全域
        self.security_domain = security_domain
        # 采集类型
        self.collection_type = collection_type
        # 执行间隔
        self.exec_interval = exec_interval
        # 监控项ID
        self.monitor_item_id = monitor_item_id
        # 设备形态
        self.device_form = device_form
        # 是否启用
        self.effective = effective

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.monitor_item_name is not None:
            result['MonitorItemName'] = self.monitor_item_name
        if self.monitor_item_description is not None:
            result['MonitorItemDescription'] = self.monitor_item_description
        if self.security_domain is not None:
            result['SecurityDomain'] = self.security_domain
        if self.collection_type is not None:
            result['CollectionType'] = self.collection_type
        if self.exec_interval is not None:
            result['ExecInterval'] = self.exec_interval
        if self.monitor_item_id is not None:
            result['MonitorItemId'] = self.monitor_item_id
        if self.device_form is not None:
            result['DeviceForm'] = self.device_form
        if self.effective is not None:
            result['Effective'] = self.effective
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MonitorItemName') is not None:
            self.monitor_item_name = m.get('MonitorItemName')
        if m.get('MonitorItemDescription') is not None:
            self.monitor_item_description = m.get('MonitorItemDescription')
        if m.get('SecurityDomain') is not None:
            self.security_domain = m.get('SecurityDomain')
        if m.get('CollectionType') is not None:
            self.collection_type = m.get('CollectionType')
        if m.get('ExecInterval') is not None:
            self.exec_interval = m.get('ExecInterval')
        if m.get('MonitorItemId') is not None:
            self.monitor_item_id = m.get('MonitorItemId')
        if m.get('DeviceForm') is not None:
            self.device_form = m.get('DeviceForm')
        if m.get('Effective') is not None:
            self.effective = m.get('Effective')
        return self


class GetAlarmStatusResponseBodyAlarmStatusNotificationSwitch(TeaModel):
    def __init__(
        self,
        reason: str = None,
        expiry_time: str = None,
    ):
        # 关闭原因
        self.reason = reason
        # 关闭到期时间
        self.expiry_time = expiry_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.expiry_time is not None:
            result['ExpiryTime'] = self.expiry_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('ExpiryTime') is not None:
            self.expiry_time = m.get('ExpiryTime')
        return self


class GetAlarmStatusResponseBodyAlarmStatusAggregateData(TeaModel):
    def __init__(
        self,
        aggregate_mode: str = None,
        aggregate_data_description: str = None,
        data_item: str = None,
        aggregate_data_name: str = None,
        device_id: str = None,
        is_all_device: int = None,
        aggregate_data_id: str = None,
        monitor_item_id: str = None,
    ):
        # 聚合方式
        self.aggregate_mode = aggregate_mode
        # 描述
        self.aggregate_data_description = aggregate_data_description
        # 数据项
        self.data_item = data_item
        # 聚合数据名称
        self.aggregate_data_name = aggregate_data_name
        # 设备ID
        self.device_id = device_id
        # 是否聚合全部设备
        self.is_all_device = is_all_device
        # 聚合数据ID
        self.aggregate_data_id = aggregate_data_id
        # 监控项ID
        self.monitor_item_id = monitor_item_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.aggregate_mode is not None:
            result['AggregateMode'] = self.aggregate_mode
        if self.aggregate_data_description is not None:
            result['AggregateDataDescription'] = self.aggregate_data_description
        if self.data_item is not None:
            result['DataItem'] = self.data_item
        if self.aggregate_data_name is not None:
            result['AggregateDataName'] = self.aggregate_data_name
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.is_all_device is not None:
            result['IsAllDevice'] = self.is_all_device
        if self.aggregate_data_id is not None:
            result['AggregateDataId'] = self.aggregate_data_id
        if self.monitor_item_id is not None:
            result['MonitorItemId'] = self.monitor_item_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AggregateMode') is not None:
            self.aggregate_mode = m.get('AggregateMode')
        if m.get('AggregateDataDescription') is not None:
            self.aggregate_data_description = m.get('AggregateDataDescription')
        if m.get('DataItem') is not None:
            self.data_item = m.get('DataItem')
        if m.get('AggregateDataName') is not None:
            self.aggregate_data_name = m.get('AggregateDataName')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('IsAllDevice') is not None:
            self.is_all_device = m.get('IsAllDevice')
        if m.get('AggregateDataId') is not None:
            self.aggregate_data_id = m.get('AggregateDataId')
        if m.get('MonitorItemId') is not None:
            self.monitor_item_id = m.get('MonitorItemId')
        return self


class GetAlarmStatusResponseBodyAlarmStatusDedicatedLine(TeaModel):
    def __init__(
        self,
        dedicated_line_name: str = None,
        space: str = None,
        port_name: str = None,
        device_id: str = None,
        bandwidth: str = None,
        ip: str = None,
    ):
        # 专线名称
        self.dedicated_line_name = dedicated_line_name
        # 物理空间
        self.space = space
        # 端口名
        self.port_name = port_name
        # 设备ID
        self.device_id = device_id
        # 带宽
        self.bandwidth = bandwidth
        # IP
        self.ip = ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.dedicated_line_name is not None:
            result['DedicatedLineName'] = self.dedicated_line_name
        if self.space is not None:
            result['Space'] = self.space
        if self.port_name is not None:
            result['PortName'] = self.port_name
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.ip is not None:
            result['Ip'] = self.ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DedicatedLineName') is not None:
            self.dedicated_line_name = m.get('DedicatedLineName')
        if m.get('Space') is not None:
            self.space = m.get('Space')
        if m.get('PortName') is not None:
            self.port_name = m.get('PortName')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        return self


class GetAlarmStatusResponseBodyAlarmStatus(TeaModel):
    def __init__(
        self,
        device_id: str = None,
        monitor_item_id: str = None,
        collection_time: str = None,
        receive_time: str = None,
        alarm_rule: str = None,
        alarm_status: str = None,
        result: str = None,
        abnormal_data_item: str = None,
        unique_key: str = None,
        response_code: str = None,
        resource_device: GetAlarmStatusResponseBodyAlarmStatusResourceDevice = None,
        monitor_item: GetAlarmStatusResponseBodyAlarmStatusMonitorItem = None,
        first_abnormal_time: str = None,
        notification_switch: GetAlarmStatusResponseBodyAlarmStatusNotificationSwitch = None,
        aggregate_data_id: str = None,
        dedicated_line_id: str = None,
        aggregate_data: GetAlarmStatusResponseBodyAlarmStatusAggregateData = None,
        dedicated_line: GetAlarmStatusResponseBodyAlarmStatusDedicatedLine = None,
    ):
        # 设备ID
        self.device_id = device_id
        # 监控项ID
        self.monitor_item_id = monitor_item_id
        # 采集时间
        self.collection_time = collection_time
        # 接收时间
        self.receive_time = receive_time
        # 命中告警规则
        self.alarm_rule = alarm_rule
        # 告警状态
        self.alarm_status = alarm_status
        # 采集结果
        self.result = result
        # 异常数据项
        self.abnormal_data_item = abnormal_data_item
        # 索引
        self.unique_key = unique_key
        # 采集状态码
        self.response_code = response_code
        # 设备
        self.resource_device = resource_device
        # 监控项
        self.monitor_item = monitor_item
        # 首次异常时间
        self.first_abnormal_time = first_abnormal_time
        # 告警开关
        self.notification_switch = notification_switch
        # 聚合数据ID
        self.aggregate_data_id = aggregate_data_id
        # 专线ID
        self.dedicated_line_id = dedicated_line_id
        # 聚合数据详情
        self.aggregate_data = aggregate_data
        # 专线详情
        self.dedicated_line = dedicated_line

    def validate(self):
        if self.resource_device:
            self.resource_device.validate()
        if self.monitor_item:
            self.monitor_item.validate()
        if self.notification_switch:
            self.notification_switch.validate()
        if self.aggregate_data:
            self.aggregate_data.validate()
        if self.dedicated_line:
            self.dedicated_line.validate()

    def to_map(self):
        result = dict()
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.monitor_item_id is not None:
            result['MonitorItemId'] = self.monitor_item_id
        if self.collection_time is not None:
            result['CollectionTime'] = self.collection_time
        if self.receive_time is not None:
            result['ReceiveTime'] = self.receive_time
        if self.alarm_rule is not None:
            result['AlarmRule'] = self.alarm_rule
        if self.alarm_status is not None:
            result['AlarmStatus'] = self.alarm_status
        if self.result is not None:
            result['Result'] = self.result
        if self.abnormal_data_item is not None:
            result['AbnormalDataItem'] = self.abnormal_data_item
        if self.unique_key is not None:
            result['UniqueKey'] = self.unique_key
        if self.response_code is not None:
            result['ResponseCode'] = self.response_code
        if self.resource_device is not None:
            result['ResourceDevice'] = self.resource_device.to_map()
        if self.monitor_item is not None:
            result['MonitorItem'] = self.monitor_item.to_map()
        if self.first_abnormal_time is not None:
            result['FirstAbnormalTime'] = self.first_abnormal_time
        if self.notification_switch is not None:
            result['NotificationSwitch'] = self.notification_switch.to_map()
        if self.aggregate_data_id is not None:
            result['AggregateDataId'] = self.aggregate_data_id
        if self.dedicated_line_id is not None:
            result['DedicatedLineId'] = self.dedicated_line_id
        if self.aggregate_data is not None:
            result['AggregateData'] = self.aggregate_data.to_map()
        if self.dedicated_line is not None:
            result['DedicatedLine'] = self.dedicated_line.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('MonitorItemId') is not None:
            self.monitor_item_id = m.get('MonitorItemId')
        if m.get('CollectionTime') is not None:
            self.collection_time = m.get('CollectionTime')
        if m.get('ReceiveTime') is not None:
            self.receive_time = m.get('ReceiveTime')
        if m.get('AlarmRule') is not None:
            self.alarm_rule = m.get('AlarmRule')
        if m.get('AlarmStatus') is not None:
            self.alarm_status = m.get('AlarmStatus')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('AbnormalDataItem') is not None:
            self.abnormal_data_item = m.get('AbnormalDataItem')
        if m.get('UniqueKey') is not None:
            self.unique_key = m.get('UniqueKey')
        if m.get('ResponseCode') is not None:
            self.response_code = m.get('ResponseCode')
        if m.get('ResourceDevice') is not None:
            temp_model = GetAlarmStatusResponseBodyAlarmStatusResourceDevice()
            self.resource_device = temp_model.from_map(m['ResourceDevice'])
        if m.get('MonitorItem') is not None:
            temp_model = GetAlarmStatusResponseBodyAlarmStatusMonitorItem()
            self.monitor_item = temp_model.from_map(m['MonitorItem'])
        if m.get('FirstAbnormalTime') is not None:
            self.first_abnormal_time = m.get('FirstAbnormalTime')
        if m.get('NotificationSwitch') is not None:
            temp_model = GetAlarmStatusResponseBodyAlarmStatusNotificationSwitch()
            self.notification_switch = temp_model.from_map(m['NotificationSwitch'])
        if m.get('AggregateDataId') is not None:
            self.aggregate_data_id = m.get('AggregateDataId')
        if m.get('DedicatedLineId') is not None:
            self.dedicated_line_id = m.get('DedicatedLineId')
        if m.get('AggregateData') is not None:
            temp_model = GetAlarmStatusResponseBodyAlarmStatusAggregateData()
            self.aggregate_data = temp_model.from_map(m['AggregateData'])
        if m.get('DedicatedLine') is not None:
            temp_model = GetAlarmStatusResponseBodyAlarmStatusDedicatedLine()
            self.dedicated_line = temp_model.from_map(m['DedicatedLine'])
        return self


class GetAlarmStatusResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        alarm_status: GetAlarmStatusResponseBodyAlarmStatus = None,
    ):
        # request Id
        self.request_id = request_id
        # 告警状态
        self.alarm_status = alarm_status

    def validate(self):
        if self.alarm_status:
            self.alarm_status.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.alarm_status is not None:
            result['AlarmStatus'] = self.alarm_status.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('AlarmStatus') is not None:
            temp_model = GetAlarmStatusResponseBodyAlarmStatus()
            self.alarm_status = temp_model.from_map(m['AlarmStatus'])
        return self


class GetAlarmStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetAlarmStatusResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetAlarmStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTasksHistoriesRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        item_id: str = None,
        device_id: str = None,
    ):
        # 返回结果的最大个数。
        self.max_results = max_results
        # 当总结果个数大于MaxResults时，用于翻页的token。
        self.next_token = next_token
        # 巡检项ID
        self.item_id = item_id
        # 设备ID
        self.device_id = device_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        return self


class ListTasksHistoriesResponseBodyInspectionTasksInspectionAlarmRules(TeaModel):
    def __init__(
        self,
        alarm_expression: str = None,
        alarm_operator: str = None,
        alarm_value: str = None,
        actual_value: str = None,
        alarm_level: str = None,
    ):
        # 告警表达式
        self.alarm_expression = alarm_expression
        # 告警操作符
        self.alarm_operator = alarm_operator
        # 告警值
        self.alarm_value = alarm_value
        # 告警实际值
        self.actual_value = actual_value
        # 告警级别
        self.alarm_level = alarm_level

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.alarm_expression is not None:
            result['AlarmExpression'] = self.alarm_expression
        if self.alarm_operator is not None:
            result['AlarmOperator'] = self.alarm_operator
        if self.alarm_value is not None:
            result['AlarmValue'] = self.alarm_value
        if self.actual_value is not None:
            result['ActualValue'] = self.actual_value
        if self.alarm_level is not None:
            result['AlarmLevel'] = self.alarm_level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmExpression') is not None:
            self.alarm_expression = m.get('AlarmExpression')
        if m.get('AlarmOperator') is not None:
            self.alarm_operator = m.get('AlarmOperator')
        if m.get('AlarmValue') is not None:
            self.alarm_value = m.get('AlarmValue')
        if m.get('ActualValue') is not None:
            self.actual_value = m.get('ActualValue')
        if m.get('AlarmLevel') is not None:
            self.alarm_level = m.get('AlarmLevel')
        return self


class ListTasksHistoriesResponseBodyInspectionTasks(TeaModel):
    def __init__(
        self,
        execution_end_time: str = None,
        execution_begin_time: str = None,
        inspection_result: str = None,
        inspection_alarm_rules: List[ListTasksHistoriesResponseBodyInspectionTasksInspectionAlarmRules] = None,
        task_id: str = None,
    ):
        # 巡检结束时间
        self.execution_end_time = execution_end_time
        # 巡检开始时间
        self.execution_begin_time = execution_begin_time
        # 巡检结果
        self.inspection_result = inspection_result
        # 告警规则
        self.inspection_alarm_rules = inspection_alarm_rules
        # 任务ID
        self.task_id = task_id

    def validate(self):
        if self.inspection_alarm_rules:
            for k in self.inspection_alarm_rules:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.execution_end_time is not None:
            result['ExecutionEndTime'] = self.execution_end_time
        if self.execution_begin_time is not None:
            result['ExecutionBeginTime'] = self.execution_begin_time
        if self.inspection_result is not None:
            result['InspectionResult'] = self.inspection_result
        result['InspectionAlarmRules'] = []
        if self.inspection_alarm_rules is not None:
            for k in self.inspection_alarm_rules:
                result['InspectionAlarmRules'].append(k.to_map() if k else None)
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExecutionEndTime') is not None:
            self.execution_end_time = m.get('ExecutionEndTime')
        if m.get('ExecutionBeginTime') is not None:
            self.execution_begin_time = m.get('ExecutionBeginTime')
        if m.get('InspectionResult') is not None:
            self.inspection_result = m.get('InspectionResult')
        self.inspection_alarm_rules = []
        if m.get('InspectionAlarmRules') is not None:
            for k in m.get('InspectionAlarmRules'):
                temp_model = ListTasksHistoriesResponseBodyInspectionTasksInspectionAlarmRules()
                self.inspection_alarm_rules.append(temp_model.from_map(k))
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class ListTasksHistoriesResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        next_token: int = None,
        inspection_tasks: List[ListTasksHistoriesResponseBodyInspectionTasks] = None,
    ):
        # 总记录数。
        self.total_count = total_count
        # 请求ID
        self.request_id = request_id
        # 当总结果个数大于MaxResults时，用于翻页的token。
        self.next_token = next_token
        # 数组，返回示例目录。
        self.inspection_tasks = inspection_tasks

    def validate(self):
        if self.inspection_tasks:
            for k in self.inspection_tasks:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        result['InspectionTasks'] = []
        if self.inspection_tasks is not None:
            for k in self.inspection_tasks:
                result['InspectionTasks'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.inspection_tasks = []
        if m.get('InspectionTasks') is not None:
            for k in m.get('InspectionTasks'):
                temp_model = ListTasksHistoriesResponseBodyInspectionTasks()
                self.inspection_tasks.append(temp_model.from_map(k))
        return self


class ListTasksHistoriesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListTasksHistoriesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListTasksHistoriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDevicePropertyRequest(TeaModel):
    def __init__(
        self,
        device_form_id: str = None,
        property_name: str = None,
        property_key: str = None,
        property_format: str = None,
        property_content: str = None,
        client_token: str = None,
    ):
        # 设备形态ID
        self.device_form_id = device_form_id
        # 属性名称
        self.property_name = property_name
        # 属性主键
        self.property_key = property_key
        # 属性格式
        self.property_format = property_format
        # 属性内容
        self.property_content = property_content
        # 幂等校验 token
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.device_form_id is not None:
            result['DeviceFormId'] = self.device_form_id
        if self.property_name is not None:
            result['PropertyName'] = self.property_name
        if self.property_key is not None:
            result['PropertyKey'] = self.property_key
        if self.property_format is not None:
            result['PropertyFormat'] = self.property_format
        if self.property_content is not None:
            result['PropertyContent'] = self.property_content
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceFormId') is not None:
            self.device_form_id = m.get('DeviceFormId')
        if m.get('PropertyName') is not None:
            self.property_name = m.get('PropertyName')
        if m.get('PropertyKey') is not None:
            self.property_key = m.get('PropertyKey')
        if m.get('PropertyFormat') is not None:
            self.property_format = m.get('PropertyFormat')
        if m.get('PropertyContent') is not None:
            self.property_content = m.get('PropertyContent')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class CreateDevicePropertyResponseBody(TeaModel):
    def __init__(
        self,
        device_property_id: str = None,
        request_id: str = None,
    ):
        # 资源实例ID，如ECS实例的创建接口CreateInstance应返回InstanceId。
        self.device_property_id = device_property_id
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.device_property_id is not None:
            result['DevicePropertyId'] = self.device_property_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DevicePropertyId') is not None:
            self.device_property_id = m.get('DevicePropertyId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateDevicePropertyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateDevicePropertyResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateDevicePropertyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RetryTasksRequestRetryTasks(TeaModel):
    def __init__(
        self,
        device_id: str = None,
        script_id: str = None,
    ):
        # 设备ID
        self.device_id = device_id
        # 脚本ID
        self.script_id = script_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.script_id is not None:
            result['ScriptId'] = self.script_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')
        return self


class RetryTasksRequest(TeaModel):
    def __init__(
        self,
        retry_tasks: List[RetryTasksRequestRetryTasks] = None,
    ):
        # 重执行任务的数组
        self.retry_tasks = retry_tasks

    def validate(self):
        if self.retry_tasks:
            for k in self.retry_tasks:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['RetryTasks'] = []
        if self.retry_tasks is not None:
            for k in self.retry_tasks:
                result['RetryTasks'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.retry_tasks = []
        if m.get('RetryTasks') is not None:
            for k in m.get('RetryTasks'):
                temp_model = RetryTasksRequestRetryTasks()
                self.retry_tasks.append(temp_model.from_map(k))
        return self


class RetryTasksShrinkRequest(TeaModel):
    def __init__(
        self,
        retry_tasks_shrink: str = None,
    ):
        # 重执行任务的数组
        self.retry_tasks_shrink = retry_tasks_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.retry_tasks_shrink is not None:
            result['RetryTasks'] = self.retry_tasks_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RetryTasks') is not None:
            self.retry_tasks_shrink = m.get('RetryTasks')
        return self


class RetryTasksResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # 请求ID
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RetryTasksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RetryTasksResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RetryTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTimePeriodRequest(TeaModel):
    def __init__(
        self,
        time_period_name: str = None,
        time_period_description: str = None,
        expression: str = None,
        client_token: str = None,
    ):
        # 时间段名称
        self.time_period_name = time_period_name
        # 描述
        self.time_period_description = time_period_description
        # cron表达式
        self.expression = expression
        # 幂等参数
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.time_period_name is not None:
            result['TimePeriodName'] = self.time_period_name
        if self.time_period_description is not None:
            result['TimePeriodDescription'] = self.time_period_description
        if self.expression is not None:
            result['Expression'] = self.expression
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TimePeriodName') is not None:
            self.time_period_name = m.get('TimePeriodName')
        if m.get('TimePeriodDescription') is not None:
            self.time_period_description = m.get('TimePeriodDescription')
        if m.get('Expression') is not None:
            self.expression = m.get('Expression')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class CreateTimePeriodResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        time_period_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        # 时间段ID
        self.time_period_id = time_period_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.time_period_id is not None:
            result['TimePeriodId'] = self.time_period_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TimePeriodId') is not None:
            self.time_period_id = m.get('TimePeriodId')
        return self


class CreateTimePeriodResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateTimePeriodResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateTimePeriodResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDeviceFormRequest(TeaModel):
    def __init__(
        self,
        device_form_id: str = None,
    ):
        # 实例 ID。
        self.device_form_id = device_form_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.device_form_id is not None:
            result['DeviceFormId'] = self.device_form_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceFormId') is not None:
            self.device_form_id = m.get('DeviceFormId')
        return self


class DeleteDeviceFormResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteDeviceFormResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteDeviceFormResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteDeviceFormResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDevicesRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        device_form_id: str = None,
        device_form_name: str = None,
        physical_space_id: str = None,
        host_name: List[str] = None,
        ip: List[str] = None,
        sn: List[str] = None,
        mac: List[str] = None,
        vendor: List[str] = None,
        model: List[str] = None,
        service_status: List[str] = None,
        ext_attributes: str = None,
    ):
        # 返回结果的最大个数。
        self.max_results = max_results
        # 当总结果个数大于MaxResults时，用于翻页的token。
        self.next_token = next_token
        # 设备形态ID
        self.device_form_id = device_form_id
        # 设备形态名称
        self.device_form_name = device_form_name
        # 物理空间ID
        self.physical_space_id = physical_space_id
        # 设备主机名
        self.host_name = host_name
        # 设备IP
        self.ip = ip
        # 设备SN
        self.sn = sn
        # 设备MAC
        self.mac = mac
        # 设备厂商
        self.vendor = vendor
        # 设备型号
        self.model = model
        # 设备服务状态
        self.service_status = service_status
        # 设备额外属性
        self.ext_attributes = ext_attributes

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.device_form_id is not None:
            result['DeviceFormId'] = self.device_form_id
        if self.device_form_name is not None:
            result['DeviceFormName'] = self.device_form_name
        if self.physical_space_id is not None:
            result['PhysicalSpaceId'] = self.physical_space_id
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.sn is not None:
            result['Sn'] = self.sn
        if self.mac is not None:
            result['Mac'] = self.mac
        if self.vendor is not None:
            result['Vendor'] = self.vendor
        if self.model is not None:
            result['Model'] = self.model
        if self.service_status is not None:
            result['ServiceStatus'] = self.service_status
        if self.ext_attributes is not None:
            result['ExtAttributes'] = self.ext_attributes
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('DeviceFormId') is not None:
            self.device_form_id = m.get('DeviceFormId')
        if m.get('DeviceFormName') is not None:
            self.device_form_name = m.get('DeviceFormName')
        if m.get('PhysicalSpaceId') is not None:
            self.physical_space_id = m.get('PhysicalSpaceId')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Sn') is not None:
            self.sn = m.get('Sn')
        if m.get('Mac') is not None:
            self.mac = m.get('Mac')
        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('ServiceStatus') is not None:
            self.service_status = m.get('ServiceStatus')
        if m.get('ExtAttributes') is not None:
            self.ext_attributes = m.get('ExtAttributes')
        return self


class ListDevicesResponseBodyDevices(TeaModel):
    def __init__(
        self,
        device_id: str = None,
        device_form_name: str = None,
        device_form_id: str = None,
        physical_space_id: str = None,
        physical_space_name: str = None,
        host_name: str = None,
        ip: str = None,
        sn: str = None,
        mac: str = None,
        vendor: str = None,
        model: str = None,
        security_domain: str = None,
        service_status: str = None,
        login_type: str = None,
        login_username: str = None,
        login_password: str = None,
        snmp_account_version: str = None,
        snmp_community: str = None,
        snmp_account_type: str = None,
        snmp_security_level: str = None,
        snmp_username: str = None,
        snmp_auth_pass_phrase: str = None,
        snmp_auth_protocol: str = None,
        snmp_privacy_passphase: str = None,
        snmp_privacy_protocol: str = None,
        ext_attributes: str = None,
    ):
        # 设备ID
        self.device_id = device_id
        # 设备形态名称
        self.device_form_name = device_form_name
        # 设备形态ID
        self.device_form_id = device_form_id
        # 物理空间ID
        self.physical_space_id = physical_space_id
        # 物理空间名称
        self.physical_space_name = physical_space_name
        # 主机名
        self.host_name = host_name
        # 设备IP
        self.ip = ip
        # 设备SN
        self.sn = sn
        # 设备MAC地址
        self.mac = mac
        # 设备厂商
        self.vendor = vendor
        # 设备型号
        self.model = model
        # 设备安全域
        self.security_domain = security_domain
        # 设备状态
        self.service_status = service_status
        # 登录类型
        self.login_type = login_type
        # 登录账号
        self.login_username = login_username
        # 登录密码
        self.login_password = login_password
        # SNMP版本号
        self.snmp_account_version = snmp_account_version
        # SNMP Community
        self.snmp_community = snmp_community
        # SNMP 账号类型
        self.snmp_account_type = snmp_account_type
        # SNMP 安全级别
        self.snmp_security_level = snmp_security_level
        # SNMP 用户名
        self.snmp_username = snmp_username
        # SNMP Auth PassPhrase
        self.snmp_auth_pass_phrase = snmp_auth_pass_phrase
        # SNMP Auth Protocol
        self.snmp_auth_protocol = snmp_auth_protocol
        # SNMP Privacy Passphase
        self.snmp_privacy_passphase = snmp_privacy_passphase
        # SNMP Privacy Protocol
        self.snmp_privacy_protocol = snmp_privacy_protocol
        # 设备额外属性
        self.ext_attributes = ext_attributes

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.device_form_name is not None:
            result['DeviceFormName'] = self.device_form_name
        if self.device_form_id is not None:
            result['DeviceFormId'] = self.device_form_id
        if self.physical_space_id is not None:
            result['PhysicalSpaceId'] = self.physical_space_id
        if self.physical_space_name is not None:
            result['PhysicalSpaceName'] = self.physical_space_name
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.sn is not None:
            result['Sn'] = self.sn
        if self.mac is not None:
            result['Mac'] = self.mac
        if self.vendor is not None:
            result['Vendor'] = self.vendor
        if self.model is not None:
            result['Model'] = self.model
        if self.security_domain is not None:
            result['SecurityDomain'] = self.security_domain
        if self.service_status is not None:
            result['ServiceStatus'] = self.service_status
        if self.login_type is not None:
            result['LoginType'] = self.login_type
        if self.login_username is not None:
            result['LoginUsername'] = self.login_username
        if self.login_password is not None:
            result['LoginPassword'] = self.login_password
        if self.snmp_account_version is not None:
            result['SnmpAccountVersion'] = self.snmp_account_version
        if self.snmp_community is not None:
            result['SnmpCommunity'] = self.snmp_community
        if self.snmp_account_type is not None:
            result['SnmpAccountType'] = self.snmp_account_type
        if self.snmp_security_level is not None:
            result['SnmpSecurityLevel'] = self.snmp_security_level
        if self.snmp_username is not None:
            result['SnmpUsername'] = self.snmp_username
        if self.snmp_auth_pass_phrase is not None:
            result['SnmpAuthPassPhrase'] = self.snmp_auth_pass_phrase
        if self.snmp_auth_protocol is not None:
            result['SnmpAuthProtocol'] = self.snmp_auth_protocol
        if self.snmp_privacy_passphase is not None:
            result['SnmpPrivacyPassphase'] = self.snmp_privacy_passphase
        if self.snmp_privacy_protocol is not None:
            result['SnmpPrivacyProtocol'] = self.snmp_privacy_protocol
        if self.ext_attributes is not None:
            result['ExtAttributes'] = self.ext_attributes
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('DeviceFormName') is not None:
            self.device_form_name = m.get('DeviceFormName')
        if m.get('DeviceFormId') is not None:
            self.device_form_id = m.get('DeviceFormId')
        if m.get('PhysicalSpaceId') is not None:
            self.physical_space_id = m.get('PhysicalSpaceId')
        if m.get('PhysicalSpaceName') is not None:
            self.physical_space_name = m.get('PhysicalSpaceName')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Sn') is not None:
            self.sn = m.get('Sn')
        if m.get('Mac') is not None:
            self.mac = m.get('Mac')
        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('SecurityDomain') is not None:
            self.security_domain = m.get('SecurityDomain')
        if m.get('ServiceStatus') is not None:
            self.service_status = m.get('ServiceStatus')
        if m.get('LoginType') is not None:
            self.login_type = m.get('LoginType')
        if m.get('LoginUsername') is not None:
            self.login_username = m.get('LoginUsername')
        if m.get('LoginPassword') is not None:
            self.login_password = m.get('LoginPassword')
        if m.get('SnmpAccountVersion') is not None:
            self.snmp_account_version = m.get('SnmpAccountVersion')
        if m.get('SnmpCommunity') is not None:
            self.snmp_community = m.get('SnmpCommunity')
        if m.get('SnmpAccountType') is not None:
            self.snmp_account_type = m.get('SnmpAccountType')
        if m.get('SnmpSecurityLevel') is not None:
            self.snmp_security_level = m.get('SnmpSecurityLevel')
        if m.get('SnmpUsername') is not None:
            self.snmp_username = m.get('SnmpUsername')
        if m.get('SnmpAuthPassPhrase') is not None:
            self.snmp_auth_pass_phrase = m.get('SnmpAuthPassPhrase')
        if m.get('SnmpAuthProtocol') is not None:
            self.snmp_auth_protocol = m.get('SnmpAuthProtocol')
        if m.get('SnmpPrivacyPassphase') is not None:
            self.snmp_privacy_passphase = m.get('SnmpPrivacyPassphase')
        if m.get('SnmpPrivacyProtocol') is not None:
            self.snmp_privacy_protocol = m.get('SnmpPrivacyProtocol')
        if m.get('ExtAttributes') is not None:
            self.ext_attributes = m.get('ExtAttributes')
        return self


class ListDevicesResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        next_token: int = None,
        devices: List[ListDevicesResponseBodyDevices] = None,
        max_results: int = None,
    ):
        # 总记录数。
        self.total_count = total_count
        # Id of the request
        self.request_id = request_id
        # 当总结果个数大于MaxResults时，用于翻页的token。
        self.next_token = next_token
        # 数组，返回示例目录。
        self.devices = devices
        # 每页数量。
        self.max_results = max_results

    def validate(self):
        if self.devices:
            for k in self.devices:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        result['Devices'] = []
        if self.devices is not None:
            for k in self.devices:
                result['Devices'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.devices = []
        if m.get('Devices') is not None:
            for k in m.get('Devices'):
                temp_model = ListDevicesResponseBodyDevices()
                self.devices.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        return self


class ListDevicesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListDevicesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListDevicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDeviceFormRequestAttributeList(TeaModel):
    def __init__(
        self,
        attribute_key: str = None,
        attribute_name: str = None,
        attribute_requirement: bool = None,
        attribute_uniqueness: bool = None,
        attribute_format: str = None,
        attribute_type: str = None,
        attribute_reference: str = None,
        attribute_table_display: bool = None,
        attribute_placeholder: str = None,
        attribute_query: str = None,
        attribute_fuzzy_query: str = None,
    ):
        # 设备形态属性主键
        self.attribute_key = attribute_key
        # 设备形态属性名称
        self.attribute_name = attribute_name
        # 设备形态属性是否必填
        self.attribute_requirement = attribute_requirement
        # 设备形态属性是否唯一
        self.attribute_uniqueness = attribute_uniqueness
        # 设备形态属性值格式
        self.attribute_format = attribute_format
        # 设备形态属性值类型
        self.attribute_type = attribute_type
        # 设备形态属性关联对象
        self.attribute_reference = attribute_reference
        # 设备形态属性是否表格可见
        self.attribute_table_display = attribute_table_display
        # 前端查询控件占位符
        self.attribute_placeholder = attribute_placeholder
        # 前端展示搜索控件
        self.attribute_query = attribute_query
        # 查询支持模糊搜索
        self.attribute_fuzzy_query = attribute_fuzzy_query

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.attribute_key is not None:
            result['AttributeKey'] = self.attribute_key
        if self.attribute_name is not None:
            result['AttributeName'] = self.attribute_name
        if self.attribute_requirement is not None:
            result['AttributeRequirement'] = self.attribute_requirement
        if self.attribute_uniqueness is not None:
            result['AttributeUniqueness'] = self.attribute_uniqueness
        if self.attribute_format is not None:
            result['AttributeFormat'] = self.attribute_format
        if self.attribute_type is not None:
            result['AttributeType'] = self.attribute_type
        if self.attribute_reference is not None:
            result['AttributeReference'] = self.attribute_reference
        if self.attribute_table_display is not None:
            result['AttributeTableDisplay'] = self.attribute_table_display
        if self.attribute_placeholder is not None:
            result['AttributePlaceholder'] = self.attribute_placeholder
        if self.attribute_query is not None:
            result['AttributeQuery'] = self.attribute_query
        if self.attribute_fuzzy_query is not None:
            result['AttributeFuzzyQuery'] = self.attribute_fuzzy_query
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttributeKey') is not None:
            self.attribute_key = m.get('AttributeKey')
        if m.get('AttributeName') is not None:
            self.attribute_name = m.get('AttributeName')
        if m.get('AttributeRequirement') is not None:
            self.attribute_requirement = m.get('AttributeRequirement')
        if m.get('AttributeUniqueness') is not None:
            self.attribute_uniqueness = m.get('AttributeUniqueness')
        if m.get('AttributeFormat') is not None:
            self.attribute_format = m.get('AttributeFormat')
        if m.get('AttributeType') is not None:
            self.attribute_type = m.get('AttributeType')
        if m.get('AttributeReference') is not None:
            self.attribute_reference = m.get('AttributeReference')
        if m.get('AttributeTableDisplay') is not None:
            self.attribute_table_display = m.get('AttributeTableDisplay')
        if m.get('AttributePlaceholder') is not None:
            self.attribute_placeholder = m.get('AttributePlaceholder')
        if m.get('AttributeQuery') is not None:
            self.attribute_query = m.get('AttributeQuery')
        if m.get('AttributeFuzzyQuery') is not None:
            self.attribute_fuzzy_query = m.get('AttributeFuzzyQuery')
        return self


class UpdateDeviceFormRequest(TeaModel):
    def __init__(
        self,
        device_form_id: str = None,
        config_compare: bool = None,
        account_config: bool = None,
        attribute_list: List[UpdateDeviceFormRequestAttributeList] = None,
        detail_display: bool = None,
    ):
        # 设备形态ID
        self.device_form_id = device_form_id
        # 是否支持配置生成
        self.config_compare = config_compare
        # 是否需要账号配置
        self.account_config = account_config
        # 设备形态属性列表
        self.attribute_list = attribute_list
        # 是否展示设备详情
        self.detail_display = detail_display

    def validate(self):
        if self.attribute_list:
            for k in self.attribute_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.device_form_id is not None:
            result['DeviceFormId'] = self.device_form_id
        if self.config_compare is not None:
            result['ConfigCompare'] = self.config_compare
        if self.account_config is not None:
            result['AccountConfig'] = self.account_config
        result['AttributeList'] = []
        if self.attribute_list is not None:
            for k in self.attribute_list:
                result['AttributeList'].append(k.to_map() if k else None)
        if self.detail_display is not None:
            result['DetailDisplay'] = self.detail_display
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceFormId') is not None:
            self.device_form_id = m.get('DeviceFormId')
        if m.get('ConfigCompare') is not None:
            self.config_compare = m.get('ConfigCompare')
        if m.get('AccountConfig') is not None:
            self.account_config = m.get('AccountConfig')
        self.attribute_list = []
        if m.get('AttributeList') is not None:
            for k in m.get('AttributeList'):
                temp_model = UpdateDeviceFormRequestAttributeList()
                self.attribute_list.append(temp_model.from_map(k))
        if m.get('DetailDisplay') is not None:
            self.detail_display = m.get('DetailDisplay')
        return self


class UpdateDeviceFormShrinkRequest(TeaModel):
    def __init__(
        self,
        device_form_id: str = None,
        config_compare: bool = None,
        account_config: bool = None,
        attribute_list_shrink: str = None,
        detail_display: bool = None,
    ):
        # 设备形态ID
        self.device_form_id = device_form_id
        # 是否支持配置生成
        self.config_compare = config_compare
        # 是否需要账号配置
        self.account_config = account_config
        # 设备形态属性列表
        self.attribute_list_shrink = attribute_list_shrink
        # 是否展示设备详情
        self.detail_display = detail_display

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.device_form_id is not None:
            result['DeviceFormId'] = self.device_form_id
        if self.config_compare is not None:
            result['ConfigCompare'] = self.config_compare
        if self.account_config is not None:
            result['AccountConfig'] = self.account_config
        if self.attribute_list_shrink is not None:
            result['AttributeList'] = self.attribute_list_shrink
        if self.detail_display is not None:
            result['DetailDisplay'] = self.detail_display
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceFormId') is not None:
            self.device_form_id = m.get('DeviceFormId')
        if m.get('ConfigCompare') is not None:
            self.config_compare = m.get('ConfigCompare')
        if m.get('AccountConfig') is not None:
            self.account_config = m.get('AccountConfig')
        if m.get('AttributeList') is not None:
            self.attribute_list_shrink = m.get('AttributeList')
        if m.get('DetailDisplay') is not None:
            self.detail_display = m.get('DetailDisplay')
        return self


class UpdateDeviceFormResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateDeviceFormResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateDeviceFormResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateDeviceFormResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDeviceRequest(TeaModel):
    def __init__(
        self,
        device_id: str = None,
        physical_space_id: str = None,
        host_name: str = None,
        ip: str = None,
        sn: str = None,
        mac: str = None,
        vendor: str = None,
        model: str = None,
        service_status: str = None,
        security_domain: str = None,
        login_type: str = None,
        login_username: str = None,
        login_password: str = None,
        snmp_account_version: str = None,
        snmp_community: str = None,
        snmp_account_type: str = None,
        snmp_security_level: str = None,
        snmp_username: str = None,
        snmp_auth_passphrase: str = None,
        snmp_auth_protocol: str = None,
        snmp_privacy_passphase: str = None,
        snmp_privacy_protocol: str = None,
        ext_attributes: str = None,
    ):
        # 设备ID
        self.device_id = device_id
        # 物理空间
        self.physical_space_id = physical_space_id
        # 主机名
        self.host_name = host_name
        # 设备IP
        self.ip = ip
        # 设备SN
        self.sn = sn
        # 设备MAC地址
        self.mac = mac
        # 设备厂商
        self.vendor = vendor
        # 设备型号
        self.model = model
        # 设备状态
        self.service_status = service_status
        # 设备安全域
        self.security_domain = security_domain
        # 登录类型
        self.login_type = login_type
        # 登录账号
        self.login_username = login_username
        # 登录密码
        self.login_password = login_password
        # SNMP 版本号
        self.snmp_account_version = snmp_account_version
        # SNMP Community
        self.snmp_community = snmp_community
        # SNMP 账号类型
        self.snmp_account_type = snmp_account_type
        # SNMP 安全级别
        self.snmp_security_level = snmp_security_level
        # SNMP 用户名
        self.snmp_username = snmp_username
        # SNMP Auth PassPhrase
        self.snmp_auth_passphrase = snmp_auth_passphrase
        # Auth Protocol
        self.snmp_auth_protocol = snmp_auth_protocol
        # Privacy Passphase
        self.snmp_privacy_passphase = snmp_privacy_passphase
        # Privacy Protocol
        self.snmp_privacy_protocol = snmp_privacy_protocol
        # 设备额外属性
        self.ext_attributes = ext_attributes

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.physical_space_id is not None:
            result['PhysicalSpaceId'] = self.physical_space_id
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.sn is not None:
            result['Sn'] = self.sn
        if self.mac is not None:
            result['Mac'] = self.mac
        if self.vendor is not None:
            result['Vendor'] = self.vendor
        if self.model is not None:
            result['Model'] = self.model
        if self.service_status is not None:
            result['ServiceStatus'] = self.service_status
        if self.security_domain is not None:
            result['SecurityDomain'] = self.security_domain
        if self.login_type is not None:
            result['LoginType'] = self.login_type
        if self.login_username is not None:
            result['LoginUsername'] = self.login_username
        if self.login_password is not None:
            result['LoginPassword'] = self.login_password
        if self.snmp_account_version is not None:
            result['SnmpAccountVersion'] = self.snmp_account_version
        if self.snmp_community is not None:
            result['SnmpCommunity'] = self.snmp_community
        if self.snmp_account_type is not None:
            result['SnmpAccountType'] = self.snmp_account_type
        if self.snmp_security_level is not None:
            result['SnmpSecurityLevel'] = self.snmp_security_level
        if self.snmp_username is not None:
            result['SnmpUsername'] = self.snmp_username
        if self.snmp_auth_passphrase is not None:
            result['SnmpAuthPassphrase'] = self.snmp_auth_passphrase
        if self.snmp_auth_protocol is not None:
            result['SnmpAuthProtocol'] = self.snmp_auth_protocol
        if self.snmp_privacy_passphase is not None:
            result['SnmpPrivacyPassphase'] = self.snmp_privacy_passphase
        if self.snmp_privacy_protocol is not None:
            result['SnmpPrivacyProtocol'] = self.snmp_privacy_protocol
        if self.ext_attributes is not None:
            result['ExtAttributes'] = self.ext_attributes
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('PhysicalSpaceId') is not None:
            self.physical_space_id = m.get('PhysicalSpaceId')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Sn') is not None:
            self.sn = m.get('Sn')
        if m.get('Mac') is not None:
            self.mac = m.get('Mac')
        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('ServiceStatus') is not None:
            self.service_status = m.get('ServiceStatus')
        if m.get('SecurityDomain') is not None:
            self.security_domain = m.get('SecurityDomain')
        if m.get('LoginType') is not None:
            self.login_type = m.get('LoginType')
        if m.get('LoginUsername') is not None:
            self.login_username = m.get('LoginUsername')
        if m.get('LoginPassword') is not None:
            self.login_password = m.get('LoginPassword')
        if m.get('SnmpAccountVersion') is not None:
            self.snmp_account_version = m.get('SnmpAccountVersion')
        if m.get('SnmpCommunity') is not None:
            self.snmp_community = m.get('SnmpCommunity')
        if m.get('SnmpAccountType') is not None:
            self.snmp_account_type = m.get('SnmpAccountType')
        if m.get('SnmpSecurityLevel') is not None:
            self.snmp_security_level = m.get('SnmpSecurityLevel')
        if m.get('SnmpUsername') is not None:
            self.snmp_username = m.get('SnmpUsername')
        if m.get('SnmpAuthPassphrase') is not None:
            self.snmp_auth_passphrase = m.get('SnmpAuthPassphrase')
        if m.get('SnmpAuthProtocol') is not None:
            self.snmp_auth_protocol = m.get('SnmpAuthProtocol')
        if m.get('SnmpPrivacyPassphase') is not None:
            self.snmp_privacy_passphase = m.get('SnmpPrivacyPassphase')
        if m.get('SnmpPrivacyProtocol') is not None:
            self.snmp_privacy_protocol = m.get('SnmpPrivacyProtocol')
        if m.get('ExtAttributes') is not None:
            self.ext_attributes = m.get('ExtAttributes')
        return self


class UpdateDeviceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateDeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateDeviceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateMonitorItemRequestAlarmRuleList(TeaModel):
    def __init__(
        self,
        alarm_status: str = None,
        variable: str = None,
        expression: str = None,
        value: str = None,
    ):
        # 告警状态
        self.alarm_status = alarm_status
        # 指标名
        self.variable = variable
        # 表达式
        self.expression = expression
        # 比较值
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.alarm_status is not None:
            result['AlarmStatus'] = self.alarm_status
        if self.variable is not None:
            result['Variable'] = self.variable
        if self.expression is not None:
            result['Expression'] = self.expression
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmStatus') is not None:
            self.alarm_status = m.get('AlarmStatus')
        if m.get('Variable') is not None:
            self.variable = m.get('Variable')
        if m.get('Expression') is not None:
            self.expression = m.get('Expression')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateMonitorItemRequest(TeaModel):
    def __init__(
        self,
        monitor_item_name: str = None,
        monitor_item_description: str = None,
        data_item: str = None,
        security_domain: str = None,
        analysis_code: str = None,
        collection_type: str = None,
        effective: int = None,
        config: str = None,
        exec_interval: int = None,
        device_form: str = None,
        alarm_rule_list: List[CreateMonitorItemRequestAlarmRuleList] = None,
        type: str = None,
        client_token: str = None,
    ):
        # 监控项名称
        self.monitor_item_name = monitor_item_name
        # 监控项描述
        self.monitor_item_description = monitor_item_description
        # 数据项
        self.data_item = data_item
        # 安全域
        self.security_domain = security_domain
        # 解析代码
        self.analysis_code = analysis_code
        # 采集类型
        self.collection_type = collection_type
        # 是否启用
        self.effective = effective
        # 监控项参数配置
        self.config = config
        # 执行间隔(s)
        self.exec_interval = exec_interval
        # 设备形态
        self.device_form = device_form
        # 告警规则列表
        self.alarm_rule_list = alarm_rule_list
        # 类型
        self.type = type
        # 幂等参数
        self.client_token = client_token

    def validate(self):
        if self.alarm_rule_list:
            for k in self.alarm_rule_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.monitor_item_name is not None:
            result['MonitorItemName'] = self.monitor_item_name
        if self.monitor_item_description is not None:
            result['MonitorItemDescription'] = self.monitor_item_description
        if self.data_item is not None:
            result['DataItem'] = self.data_item
        if self.security_domain is not None:
            result['SecurityDomain'] = self.security_domain
        if self.analysis_code is not None:
            result['AnalysisCode'] = self.analysis_code
        if self.collection_type is not None:
            result['CollectionType'] = self.collection_type
        if self.effective is not None:
            result['Effective'] = self.effective
        if self.config is not None:
            result['Config'] = self.config
        if self.exec_interval is not None:
            result['ExecInterval'] = self.exec_interval
        if self.device_form is not None:
            result['DeviceForm'] = self.device_form
        result['AlarmRuleList'] = []
        if self.alarm_rule_list is not None:
            for k in self.alarm_rule_list:
                result['AlarmRuleList'].append(k.to_map() if k else None)
        if self.type is not None:
            result['Type'] = self.type
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MonitorItemName') is not None:
            self.monitor_item_name = m.get('MonitorItemName')
        if m.get('MonitorItemDescription') is not None:
            self.monitor_item_description = m.get('MonitorItemDescription')
        if m.get('DataItem') is not None:
            self.data_item = m.get('DataItem')
        if m.get('SecurityDomain') is not None:
            self.security_domain = m.get('SecurityDomain')
        if m.get('AnalysisCode') is not None:
            self.analysis_code = m.get('AnalysisCode')
        if m.get('CollectionType') is not None:
            self.collection_type = m.get('CollectionType')
        if m.get('Effective') is not None:
            self.effective = m.get('Effective')
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('ExecInterval') is not None:
            self.exec_interval = m.get('ExecInterval')
        if m.get('DeviceForm') is not None:
            self.device_form = m.get('DeviceForm')
        self.alarm_rule_list = []
        if m.get('AlarmRuleList') is not None:
            for k in m.get('AlarmRuleList'):
                temp_model = CreateMonitorItemRequestAlarmRuleList()
                self.alarm_rule_list.append(temp_model.from_map(k))
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class CreateMonitorItemResponseBody(TeaModel):
    def __init__(
        self,
        monitor_item_id: str = None,
        request_id: str = None,
    ):
        # 监控项ID
        self.monitor_item_id = monitor_item_id
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.monitor_item_id is not None:
            result['MonitorItemId'] = self.monitor_item_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MonitorItemId') is not None:
            self.monitor_item_id = m.get('MonitorItemId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateMonitorItemResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateMonitorItemResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateMonitorItemResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatePhysicalSpaceRequest(TeaModel):
    def __init__(
        self,
        physical_space_name: str = None,
        country: str = None,
        province: str = None,
        city: str = None,
        address: str = None,
        client_token: str = None,
    ):
        # 物理空间名称
        self.physical_space_name = physical_space_name
        # 所属国家
        self.country = country
        # 所属省份
        self.province = province
        # 所属城市
        self.city = city
        # 具体地址
        self.address = address
        # 幂等校验 token
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.physical_space_name is not None:
            result['PhysicalSpaceName'] = self.physical_space_name
        if self.country is not None:
            result['Country'] = self.country
        if self.province is not None:
            result['Province'] = self.province
        if self.city is not None:
            result['City'] = self.city
        if self.address is not None:
            result['Address'] = self.address
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PhysicalSpaceName') is not None:
            self.physical_space_name = m.get('PhysicalSpaceName')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class CreatePhysicalSpaceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        physical_space_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        # 物理空间ID
        self.physical_space_id = physical_space_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.physical_space_id is not None:
            result['PhysicalSpaceId'] = self.physical_space_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PhysicalSpaceId') is not None:
            self.physical_space_id = m.get('PhysicalSpaceId')
        return self


class CreatePhysicalSpaceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreatePhysicalSpaceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreatePhysicalSpaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDeviceRequest(TeaModel):
    def __init__(
        self,
        device_id: str = None,
    ):
        # 实例 ID。
        self.device_id = device_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        return self


class GetDeviceResponseBodyDevice(TeaModel):
    def __init__(
        self,
        device_id: str = None,
        device_form_id: str = None,
        device_form_name: str = None,
        physical_space_id: str = None,
        physical_space_name: str = None,
        host_name: str = None,
        ip: str = None,
        sn: str = None,
        mac: str = None,
        vendor: str = None,
        model: str = None,
        security_domain: str = None,
        service_status: str = None,
        login_type: str = None,
        login_username: str = None,
        login_password: str = None,
        snmp_account_version: str = None,
        snmp_community: str = None,
        snmp_account_type: str = None,
        snmp_security_level: str = None,
        snmp_username: str = None,
        snmp_auth_passphrase: str = None,
        snmp_auth_protocol: str = None,
        snmp_privacy_passphase: str = None,
        snmp_privacy_protocol: str = None,
        ext_attributes: str = None,
    ):
        # 设备ID
        self.device_id = device_id
        # 设备形态ID
        self.device_form_id = device_form_id
        # 设备形态名称
        self.device_form_name = device_form_name
        # 物理空间ID
        self.physical_space_id = physical_space_id
        # 物理空间名称
        self.physical_space_name = physical_space_name
        # 主机名
        self.host_name = host_name
        # 设备IP
        self.ip = ip
        # 设备SN
        self.sn = sn
        # 设备MAC地址
        self.mac = mac
        # 设备厂商
        self.vendor = vendor
        # 设备型号
        self.model = model
        # 设备安全域
        self.security_domain = security_domain
        # 设备状态
        self.service_status = service_status
        # 登录类型
        self.login_type = login_type
        # 登录账号
        self.login_username = login_username
        # 登录密码
        self.login_password = login_password
        # SNMP版本号
        self.snmp_account_version = snmp_account_version
        # SNMP Community
        self.snmp_community = snmp_community
        # SNMP 账号类型
        self.snmp_account_type = snmp_account_type
        # SNMP 安全级别
        self.snmp_security_level = snmp_security_level
        # SNMP 用户名
        self.snmp_username = snmp_username
        # SNMP Auth PassPhrase
        self.snmp_auth_passphrase = snmp_auth_passphrase
        # SNMP Auth Protocol
        self.snmp_auth_protocol = snmp_auth_protocol
        # SNMP Privacy Passphase
        self.snmp_privacy_passphase = snmp_privacy_passphase
        # SNMP Privacy Protocol
        self.snmp_privacy_protocol = snmp_privacy_protocol
        # 设备额外属性
        self.ext_attributes = ext_attributes

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.device_form_id is not None:
            result['DeviceFormId'] = self.device_form_id
        if self.device_form_name is not None:
            result['DeviceFormName'] = self.device_form_name
        if self.physical_space_id is not None:
            result['PhysicalSpaceId'] = self.physical_space_id
        if self.physical_space_name is not None:
            result['PhysicalSpaceName'] = self.physical_space_name
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.sn is not None:
            result['Sn'] = self.sn
        if self.mac is not None:
            result['Mac'] = self.mac
        if self.vendor is not None:
            result['Vendor'] = self.vendor
        if self.model is not None:
            result['Model'] = self.model
        if self.security_domain is not None:
            result['SecurityDomain'] = self.security_domain
        if self.service_status is not None:
            result['ServiceStatus'] = self.service_status
        if self.login_type is not None:
            result['LoginType'] = self.login_type
        if self.login_username is not None:
            result['LoginUsername'] = self.login_username
        if self.login_password is not None:
            result['LoginPassword'] = self.login_password
        if self.snmp_account_version is not None:
            result['SnmpAccountVersion'] = self.snmp_account_version
        if self.snmp_community is not None:
            result['SnmpCommunity'] = self.snmp_community
        if self.snmp_account_type is not None:
            result['SnmpAccountType'] = self.snmp_account_type
        if self.snmp_security_level is not None:
            result['SnmpSecurityLevel'] = self.snmp_security_level
        if self.snmp_username is not None:
            result['SnmpUsername'] = self.snmp_username
        if self.snmp_auth_passphrase is not None:
            result['SnmpAuthPassphrase'] = self.snmp_auth_passphrase
        if self.snmp_auth_protocol is not None:
            result['SnmpAuthProtocol'] = self.snmp_auth_protocol
        if self.snmp_privacy_passphase is not None:
            result['SnmpPrivacyPassphase'] = self.snmp_privacy_passphase
        if self.snmp_privacy_protocol is not None:
            result['SnmpPrivacyProtocol'] = self.snmp_privacy_protocol
        if self.ext_attributes is not None:
            result['ExtAttributes'] = self.ext_attributes
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('DeviceFormId') is not None:
            self.device_form_id = m.get('DeviceFormId')
        if m.get('DeviceFormName') is not None:
            self.device_form_name = m.get('DeviceFormName')
        if m.get('PhysicalSpaceId') is not None:
            self.physical_space_id = m.get('PhysicalSpaceId')
        if m.get('PhysicalSpaceName') is not None:
            self.physical_space_name = m.get('PhysicalSpaceName')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Sn') is not None:
            self.sn = m.get('Sn')
        if m.get('Mac') is not None:
            self.mac = m.get('Mac')
        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('SecurityDomain') is not None:
            self.security_domain = m.get('SecurityDomain')
        if m.get('ServiceStatus') is not None:
            self.service_status = m.get('ServiceStatus')
        if m.get('LoginType') is not None:
            self.login_type = m.get('LoginType')
        if m.get('LoginUsername') is not None:
            self.login_username = m.get('LoginUsername')
        if m.get('LoginPassword') is not None:
            self.login_password = m.get('LoginPassword')
        if m.get('SnmpAccountVersion') is not None:
            self.snmp_account_version = m.get('SnmpAccountVersion')
        if m.get('SnmpCommunity') is not None:
            self.snmp_community = m.get('SnmpCommunity')
        if m.get('SnmpAccountType') is not None:
            self.snmp_account_type = m.get('SnmpAccountType')
        if m.get('SnmpSecurityLevel') is not None:
            self.snmp_security_level = m.get('SnmpSecurityLevel')
        if m.get('SnmpUsername') is not None:
            self.snmp_username = m.get('SnmpUsername')
        if m.get('SnmpAuthPassphrase') is not None:
            self.snmp_auth_passphrase = m.get('SnmpAuthPassphrase')
        if m.get('SnmpAuthProtocol') is not None:
            self.snmp_auth_protocol = m.get('SnmpAuthProtocol')
        if m.get('SnmpPrivacyPassphase') is not None:
            self.snmp_privacy_passphase = m.get('SnmpPrivacyPassphase')
        if m.get('SnmpPrivacyProtocol') is not None:
            self.snmp_privacy_protocol = m.get('SnmpPrivacyProtocol')
        if m.get('ExtAttributes') is not None:
            self.ext_attributes = m.get('ExtAttributes')
        return self


class GetDeviceResponseBody(TeaModel):
    def __init__(
        self,
        device: GetDeviceResponseBodyDevice = None,
        request_id: str = None,
    ):
        # 设备详情
        self.device = device
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.device:
            self.device.validate()

    def to_map(self):
        result = dict()
        if self.device is not None:
            result['Device'] = self.device.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Device') is not None:
            temp_model = GetDeviceResponseBodyDevice()
            self.device = temp_model.from_map(m['Device'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetDeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetDeviceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDevicesRequest(TeaModel):
    def __init__(
        self,
        device_ids: List[str] = None,
        login_type: str = None,
        login_username: str = None,
        login_password: str = None,
        snmp_account_version: str = None,
        snmp_community: str = None,
        snmp_account_type: str = None,
        snmp_security_level: str = None,
        snmp_user_name: str = None,
        snmp_auth_passphrase: str = None,
        snmp_auth_protocol: str = None,
        snmp_privacy_passphase: str = None,
        snmp_privacy_protocol: str = None,
    ):
        # 设备ID
        self.device_ids = device_ids
        # 登录类型
        self.login_type = login_type
        # 登录账号
        self.login_username = login_username
        # 登录密码
        self.login_password = login_password
        # SNMP 版本号
        self.snmp_account_version = snmp_account_version
        # SNMP Community
        self.snmp_community = snmp_community
        # SNMP 账号类型
        self.snmp_account_type = snmp_account_type
        # SNMP 安全级别
        self.snmp_security_level = snmp_security_level
        # SNMP 用户名
        self.snmp_user_name = snmp_user_name
        # SNMP Auth PassPhrase
        self.snmp_auth_passphrase = snmp_auth_passphrase
        # SNMP Auth Protocol
        self.snmp_auth_protocol = snmp_auth_protocol
        # SNMP Privacy Passphase
        self.snmp_privacy_passphase = snmp_privacy_passphase
        # SNMP Privacy Protocol
        self.snmp_privacy_protocol = snmp_privacy_protocol

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.device_ids is not None:
            result['DeviceIds'] = self.device_ids
        if self.login_type is not None:
            result['LoginType'] = self.login_type
        if self.login_username is not None:
            result['LoginUsername'] = self.login_username
        if self.login_password is not None:
            result['LoginPassword'] = self.login_password
        if self.snmp_account_version is not None:
            result['SnmpAccountVersion'] = self.snmp_account_version
        if self.snmp_community is not None:
            result['SnmpCommunity'] = self.snmp_community
        if self.snmp_account_type is not None:
            result['SnmpAccountType'] = self.snmp_account_type
        if self.snmp_security_level is not None:
            result['SnmpSecurityLevel'] = self.snmp_security_level
        if self.snmp_user_name is not None:
            result['SnmpUserName'] = self.snmp_user_name
        if self.snmp_auth_passphrase is not None:
            result['SnmpAuthPassphrase'] = self.snmp_auth_passphrase
        if self.snmp_auth_protocol is not None:
            result['SnmpAuthProtocol'] = self.snmp_auth_protocol
        if self.snmp_privacy_passphase is not None:
            result['SnmpPrivacyPassphase'] = self.snmp_privacy_passphase
        if self.snmp_privacy_protocol is not None:
            result['SnmpPrivacyProtocol'] = self.snmp_privacy_protocol
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceIds') is not None:
            self.device_ids = m.get('DeviceIds')
        if m.get('LoginType') is not None:
            self.login_type = m.get('LoginType')
        if m.get('LoginUsername') is not None:
            self.login_username = m.get('LoginUsername')
        if m.get('LoginPassword') is not None:
            self.login_password = m.get('LoginPassword')
        if m.get('SnmpAccountVersion') is not None:
            self.snmp_account_version = m.get('SnmpAccountVersion')
        if m.get('SnmpCommunity') is not None:
            self.snmp_community = m.get('SnmpCommunity')
        if m.get('SnmpAccountType') is not None:
            self.snmp_account_type = m.get('SnmpAccountType')
        if m.get('SnmpSecurityLevel') is not None:
            self.snmp_security_level = m.get('SnmpSecurityLevel')
        if m.get('SnmpUserName') is not None:
            self.snmp_user_name = m.get('SnmpUserName')
        if m.get('SnmpAuthPassphrase') is not None:
            self.snmp_auth_passphrase = m.get('SnmpAuthPassphrase')
        if m.get('SnmpAuthProtocol') is not None:
            self.snmp_auth_protocol = m.get('SnmpAuthProtocol')
        if m.get('SnmpPrivacyPassphase') is not None:
            self.snmp_privacy_passphase = m.get('SnmpPrivacyPassphase')
        if m.get('SnmpPrivacyProtocol') is not None:
            self.snmp_privacy_protocol = m.get('SnmpPrivacyProtocol')
        return self


class UpdateDevicesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateDevicesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateDevicesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateDevicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableNotificationRequestList(TeaModel):
    def __init__(
        self,
        device_id: str = None,
        monitor_item_id: str = None,
        aggregate_data_id: str = None,
        type: str = None,
        dedicated_line_id: str = None,
    ):
        # 设备ID
        self.device_id = device_id
        # 监控项ID
        self.monitor_item_id = monitor_item_id
        # 聚合数据ID
        self.aggregate_data_id = aggregate_data_id
        # 类型
        self.type = type
        # 专线ID
        self.dedicated_line_id = dedicated_line_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.monitor_item_id is not None:
            result['MonitorItemId'] = self.monitor_item_id
        if self.aggregate_data_id is not None:
            result['AggregateDataId'] = self.aggregate_data_id
        if self.type is not None:
            result['Type'] = self.type
        if self.dedicated_line_id is not None:
            result['DedicatedLineId'] = self.dedicated_line_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('MonitorItemId') is not None:
            self.monitor_item_id = m.get('MonitorItemId')
        if m.get('AggregateDataId') is not None:
            self.aggregate_data_id = m.get('AggregateDataId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('DedicatedLineId') is not None:
            self.dedicated_line_id = m.get('DedicatedLineId')
        return self


class DisableNotificationRequest(TeaModel):
    def __init__(
        self,
        expiry_time: str = None,
        reason: str = None,
        list: List[DisableNotificationRequestList] = None,
    ):
        # 到期时间
        self.expiry_time = expiry_time
        # 关闭原因
        self.reason = reason
        # 关闭通知的对象
        self.list = list

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.expiry_time is not None:
            result['ExpiryTime'] = self.expiry_time
        if self.reason is not None:
            result['Reason'] = self.reason
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExpiryTime') is not None:
            self.expiry_time = m.get('ExpiryTime')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = DisableNotificationRequestList()
                self.list.append(temp_model.from_map(k))
        return self


class DisableNotificationResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # request id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DisableNotificationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DisableNotificationResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DisableNotificationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDeviceConfigDiffRequest(TeaModel):
    def __init__(
        self,
        device_id: str = None,
        start_date: str = None,
        end_date: str = None,
    ):
        # 实例 ID。
        self.device_id = device_id
        # 查询日期1，格式 yyyy-MM-dd
        self.start_date = start_date
        # 查询日期2，格式 yyyy-MM-dd
        self.end_date = end_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        return self


class GetDeviceConfigDiffResponseBodyDeviceConfigDiff(TeaModel):
    def __init__(
        self,
        extract_diff: str = None,
        total_diff: str = None,
    ):
        # 差异提取
        self.extract_diff = extract_diff
        # 全量比对
        self.total_diff = total_diff

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.extract_diff is not None:
            result['ExtractDiff'] = self.extract_diff
        if self.total_diff is not None:
            result['TotalDiff'] = self.total_diff
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExtractDiff') is not None:
            self.extract_diff = m.get('ExtractDiff')
        if m.get('TotalDiff') is not None:
            self.total_diff = m.get('TotalDiff')
        return self


class GetDeviceConfigDiffResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        device_config_diff: GetDeviceConfigDiffResponseBodyDeviceConfigDiff = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.device_config_diff = device_config_diff

    def validate(self):
        if self.device_config_diff:
            self.device_config_diff.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.device_config_diff is not None:
            result['DeviceConfigDiff'] = self.device_config_diff.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DeviceConfigDiff') is not None:
            temp_model = GetDeviceConfigDiffResponseBodyDeviceConfigDiff()
            self.device_config_diff = temp_model.from_map(m['DeviceConfigDiff'])
        return self


class GetDeviceConfigDiffResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetDeviceConfigDiffResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetDeviceConfigDiffResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetInspectionTaskRequest(TeaModel):
    def __init__(
        self,
        task_id: str = None,
    ):
        # 巡检项ID
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class GetInspectionTaskResponseBodyInspectionAlarmRules(TeaModel):
    def __init__(
        self,
        expression: str = None,
        operator: str = None,
        value: str = None,
        actual_value: str = None,
        level: str = None,
    ):
        # 告警符号
        self.expression = expression
        # 告警操作符
        self.operator = operator
        # 告警值
        self.value = value
        # 告警实际值
        self.actual_value = actual_value
        # 告警级别
        self.level = level

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.expression is not None:
            result['Expression'] = self.expression
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.value is not None:
            result['Value'] = self.value
        if self.actual_value is not None:
            result['ActualValue'] = self.actual_value
        if self.level is not None:
            result['Level'] = self.level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Expression') is not None:
            self.expression = m.get('Expression')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('ActualValue') is not None:
            self.actual_value = m.get('ActualValue')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        return self


class GetInspectionTaskResponseBody(TeaModel):
    def __init__(
        self,
        space: str = None,
        request_id: str = None,
        device_id: str = None,
        inspection_result: str = None,
        inspection_alarm_rules: List[GetInspectionTaskResponseBodyInspectionAlarmRules] = None,
        ip: str = None,
        host_name: str = None,
        vendor: str = None,
        task_status: str = None,
        item_id: str = None,
        execution_end_time: str = None,
        execution_begin_time: str = None,
        model: List[str] = None,
        item_name: str = None,
        error_code: str = None,
        script_id: str = None,
        task_id: str = None,
    ):
        # 物理空间
        self.space = space
        # 请求ID
        self.request_id = request_id
        # 设备ID
        self.device_id = device_id
        # 巡检结果
        self.inspection_result = inspection_result
        # 告警规则
        self.inspection_alarm_rules = inspection_alarm_rules
        # IP地址
        self.ip = ip
        # 主机名
        self.host_name = host_name
        # 厂商
        self.vendor = vendor
        # 任务状态
        self.task_status = task_status
        # 巡检项ID
        self.item_id = item_id
        # 巡检结束时间
        self.execution_end_time = execution_end_time
        # 巡检开始时间
        self.execution_begin_time = execution_begin_time
        # 型号
        self.model = model
        # 巡检项名字
        self.item_name = item_name
        # 错误码
        self.error_code = error_code
        # 模板ID
        self.script_id = script_id
        # 任务ID
        self.task_id = task_id

    def validate(self):
        if self.inspection_alarm_rules:
            for k in self.inspection_alarm_rules:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.space is not None:
            result['Space'] = self.space
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.inspection_result is not None:
            result['InspectionResult'] = self.inspection_result
        result['InspectionAlarmRules'] = []
        if self.inspection_alarm_rules is not None:
            for k in self.inspection_alarm_rules:
                result['InspectionAlarmRules'].append(k.to_map() if k else None)
        if self.ip is not None:
            result['IP'] = self.ip
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.vendor is not None:
            result['Vendor'] = self.vendor
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.execution_end_time is not None:
            result['ExecutionEndTime'] = self.execution_end_time
        if self.execution_begin_time is not None:
            result['ExecutionBeginTime'] = self.execution_begin_time
        if self.model is not None:
            result['Model'] = self.model
        if self.item_name is not None:
            result['ItemName'] = self.item_name
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.script_id is not None:
            result['ScriptId'] = self.script_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Space') is not None:
            self.space = m.get('Space')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('InspectionResult') is not None:
            self.inspection_result = m.get('InspectionResult')
        self.inspection_alarm_rules = []
        if m.get('InspectionAlarmRules') is not None:
            for k in m.get('InspectionAlarmRules'):
                temp_model = GetInspectionTaskResponseBodyInspectionAlarmRules()
                self.inspection_alarm_rules.append(temp_model.from_map(k))
        if m.get('IP') is not None:
            self.ip = m.get('IP')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('ExecutionEndTime') is not None:
            self.execution_end_time = m.get('ExecutionEndTime')
        if m.get('ExecutionBeginTime') is not None:
            self.execution_begin_time = m.get('ExecutionBeginTime')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('ItemName') is not None:
            self.item_name = m.get('ItemName')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class GetInspectionTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetInspectionTaskResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetInspectionTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAlarmStatusRequest(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        max_results: int = None,
        space: str = None,
        device_form: str = None,
        status: str = None,
        device_id: str = None,
        monitor_item_id: str = None,
        type: str = None,
    ):
        # 标记当前开始读取的位置，置空表示从头开始
        self.next_token = next_token
        # 本次读取的最大数据记录数量
        self.max_results = max_results
        # 物理空间
        self.space = space
        # 设备形态
        self.device_form = device_form
        # 告警状态
        self.status = status
        # 设备ID
        self.device_id = device_id
        # 监控项ID
        self.monitor_item_id = monitor_item_id
        # 数据类型
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.space is not None:
            result['Space'] = self.space
        if self.device_form is not None:
            result['DeviceForm'] = self.device_form
        if self.status is not None:
            result['Status'] = self.status
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.monitor_item_id is not None:
            result['MonitorItemId'] = self.monitor_item_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('Space') is not None:
            self.space = m.get('Space')
        if m.get('DeviceForm') is not None:
            self.device_form = m.get('DeviceForm')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('MonitorItemId') is not None:
            self.monitor_item_id = m.get('MonitorItemId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListAlarmStatusResponseBodyAlarmStatusResourceDevice(TeaModel):
    def __init__(
        self,
        host_name: str = None,
    ):
        # 设备名
        self.host_name = host_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.host_name is not None:
            result['HostName'] = self.host_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        return self


class ListAlarmStatusResponseBodyAlarmStatusMonitorItem(TeaModel):
    def __init__(
        self,
        monitor_item_name: str = None,
    ):
        # 监控项名称
        self.monitor_item_name = monitor_item_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.monitor_item_name is not None:
            result['MonitorItemName'] = self.monitor_item_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MonitorItemName') is not None:
            self.monitor_item_name = m.get('MonitorItemName')
        return self


class ListAlarmStatusResponseBodyAlarmStatusNotificationSwitch(TeaModel):
    def __init__(
        self,
        reason: str = None,
        expiry_time: str = None,
    ):
        # 关闭原因
        self.reason = reason
        # 关闭到期时间
        self.expiry_time = expiry_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.expiry_time is not None:
            result['ExpiryTime'] = self.expiry_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('ExpiryTime') is not None:
            self.expiry_time = m.get('ExpiryTime')
        return self


class ListAlarmStatusResponseBodyAlarmStatusAggregateData(TeaModel):
    def __init__(
        self,
        aggregate_data_name: str = None,
        data_item: str = None,
    ):
        # 聚合数据名称
        self.aggregate_data_name = aggregate_data_name
        # 数据项
        self.data_item = data_item

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.aggregate_data_name is not None:
            result['AggregateDataName'] = self.aggregate_data_name
        if self.data_item is not None:
            result['DataItem'] = self.data_item
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AggregateDataName') is not None:
            self.aggregate_data_name = m.get('AggregateDataName')
        if m.get('DataItem') is not None:
            self.data_item = m.get('DataItem')
        return self


class ListAlarmStatusResponseBodyAlarmStatusDedicatedLine(TeaModel):
    def __init__(
        self,
        dedicated_line_name: str = None,
    ):
        # 专线名称
        self.dedicated_line_name = dedicated_line_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.dedicated_line_name is not None:
            result['DedicatedLineName'] = self.dedicated_line_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DedicatedLineName') is not None:
            self.dedicated_line_name = m.get('DedicatedLineName')
        return self


class ListAlarmStatusResponseBodyAlarmStatus(TeaModel):
    def __init__(
        self,
        device_id: str = None,
        monitor_item_id: str = None,
        collection_time: str = None,
        receive_time: str = None,
        alarm_rule: str = None,
        alarm_status: str = None,
        result: str = None,
        abnormal_data_item: str = None,
        unique_key: str = None,
        response_code: str = None,
        resource_device: ListAlarmStatusResponseBodyAlarmStatusResourceDevice = None,
        monitor_item: ListAlarmStatusResponseBodyAlarmStatusMonitorItem = None,
        first_abnormal_time: str = None,
        notification_switch: ListAlarmStatusResponseBodyAlarmStatusNotificationSwitch = None,
        aggregate_data_id: str = None,
        aggregate_data: ListAlarmStatusResponseBodyAlarmStatusAggregateData = None,
        dedicated_line_id: str = None,
        dedicated_line: ListAlarmStatusResponseBodyAlarmStatusDedicatedLine = None,
    ):
        # 设备ID
        self.device_id = device_id
        # 监控项ID
        self.monitor_item_id = monitor_item_id
        # 检测时间
        self.collection_time = collection_time
        # 接收时间
        self.receive_time = receive_time
        # 命中告警规则
        self.alarm_rule = alarm_rule
        # 告警状态
        self.alarm_status = alarm_status
        # 采集结果
        self.result = result
        # 异常数据项
        self.abnormal_data_item = abnormal_data_item
        # 索引
        self.unique_key = unique_key
        # 采集状态码
        self.response_code = response_code
        # 设备
        self.resource_device = resource_device
        # 监控项
        self.monitor_item = monitor_item
        # 首次异常时间
        self.first_abnormal_time = first_abnormal_time
        # 告警开关配置
        self.notification_switch = notification_switch
        # 聚合数据ID
        self.aggregate_data_id = aggregate_data_id
        # 聚合数据
        self.aggregate_data = aggregate_data
        # 专线ID
        self.dedicated_line_id = dedicated_line_id
        # 专线
        self.dedicated_line = dedicated_line

    def validate(self):
        if self.resource_device:
            self.resource_device.validate()
        if self.monitor_item:
            self.monitor_item.validate()
        if self.notification_switch:
            self.notification_switch.validate()
        if self.aggregate_data:
            self.aggregate_data.validate()
        if self.dedicated_line:
            self.dedicated_line.validate()

    def to_map(self):
        result = dict()
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.monitor_item_id is not None:
            result['MonitorItemId'] = self.monitor_item_id
        if self.collection_time is not None:
            result['CollectionTime'] = self.collection_time
        if self.receive_time is not None:
            result['ReceiveTime'] = self.receive_time
        if self.alarm_rule is not None:
            result['AlarmRule'] = self.alarm_rule
        if self.alarm_status is not None:
            result['AlarmStatus'] = self.alarm_status
        if self.result is not None:
            result['Result'] = self.result
        if self.abnormal_data_item is not None:
            result['AbnormalDataItem'] = self.abnormal_data_item
        if self.unique_key is not None:
            result['UniqueKey'] = self.unique_key
        if self.response_code is not None:
            result['ResponseCode'] = self.response_code
        if self.resource_device is not None:
            result['ResourceDevice'] = self.resource_device.to_map()
        if self.monitor_item is not None:
            result['MonitorItem'] = self.monitor_item.to_map()
        if self.first_abnormal_time is not None:
            result['FirstAbnormalTime'] = self.first_abnormal_time
        if self.notification_switch is not None:
            result['NotificationSwitch'] = self.notification_switch.to_map()
        if self.aggregate_data_id is not None:
            result['AggregateDataId'] = self.aggregate_data_id
        if self.aggregate_data is not None:
            result['AggregateData'] = self.aggregate_data.to_map()
        if self.dedicated_line_id is not None:
            result['DedicatedLineId'] = self.dedicated_line_id
        if self.dedicated_line is not None:
            result['DedicatedLine'] = self.dedicated_line.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('MonitorItemId') is not None:
            self.monitor_item_id = m.get('MonitorItemId')
        if m.get('CollectionTime') is not None:
            self.collection_time = m.get('CollectionTime')
        if m.get('ReceiveTime') is not None:
            self.receive_time = m.get('ReceiveTime')
        if m.get('AlarmRule') is not None:
            self.alarm_rule = m.get('AlarmRule')
        if m.get('AlarmStatus') is not None:
            self.alarm_status = m.get('AlarmStatus')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('AbnormalDataItem') is not None:
            self.abnormal_data_item = m.get('AbnormalDataItem')
        if m.get('UniqueKey') is not None:
            self.unique_key = m.get('UniqueKey')
        if m.get('ResponseCode') is not None:
            self.response_code = m.get('ResponseCode')
        if m.get('ResourceDevice') is not None:
            temp_model = ListAlarmStatusResponseBodyAlarmStatusResourceDevice()
            self.resource_device = temp_model.from_map(m['ResourceDevice'])
        if m.get('MonitorItem') is not None:
            temp_model = ListAlarmStatusResponseBodyAlarmStatusMonitorItem()
            self.monitor_item = temp_model.from_map(m['MonitorItem'])
        if m.get('FirstAbnormalTime') is not None:
            self.first_abnormal_time = m.get('FirstAbnormalTime')
        if m.get('NotificationSwitch') is not None:
            temp_model = ListAlarmStatusResponseBodyAlarmStatusNotificationSwitch()
            self.notification_switch = temp_model.from_map(m['NotificationSwitch'])
        if m.get('AggregateDataId') is not None:
            self.aggregate_data_id = m.get('AggregateDataId')
        if m.get('AggregateData') is not None:
            temp_model = ListAlarmStatusResponseBodyAlarmStatusAggregateData()
            self.aggregate_data = temp_model.from_map(m['AggregateData'])
        if m.get('DedicatedLineId') is not None:
            self.dedicated_line_id = m.get('DedicatedLineId')
        if m.get('DedicatedLine') is not None:
            temp_model = ListAlarmStatusResponseBodyAlarmStatusDedicatedLine()
            self.dedicated_line = temp_model.from_map(m['DedicatedLine'])
        return self


class ListAlarmStatusResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        next_token: str = None,
        max_results: int = None,
        alarm_status: List[ListAlarmStatusResponseBodyAlarmStatus] = None,
    ):
        # TotalCount本次请求条件下的数据总量，此参数为可选参数，默认可不返回
        self.total_count = total_count
        # Id of the request
        self.request_id = request_id
        # 表示当前调用返回读取到的位置，空代表数据已经读取完毕
        self.next_token = next_token
        # MaxResults本次请求所返回的最大记录条数
        self.max_results = max_results
        # 告警状态列表
        self.alarm_status = alarm_status

    def validate(self):
        if self.alarm_status:
            for k in self.alarm_status:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        result['AlarmStatus'] = []
        if self.alarm_status is not None:
            for k in self.alarm_status:
                result['AlarmStatus'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        self.alarm_status = []
        if m.get('AlarmStatus') is not None:
            for k in m.get('AlarmStatus'):
                temp_model = ListAlarmStatusResponseBodyAlarmStatus()
                self.alarm_status.append(temp_model.from_map(k))
        return self


class ListAlarmStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListAlarmStatusResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListAlarmStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPhysicalSpaceRequest(TeaModel):
    def __init__(
        self,
        physical_space_id: str = None,
    ):
        # 实例 ID。
        self.physical_space_id = physical_space_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.physical_space_id is not None:
            result['PhysicalSpaceId'] = self.physical_space_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PhysicalSpaceId') is not None:
            self.physical_space_id = m.get('PhysicalSpaceId')
        return self


class GetPhysicalSpaceResponseBodyPhysicalSpace(TeaModel):
    def __init__(
        self,
        physical_space_id: str = None,
        physical_space_name: str = None,
        country: str = None,
        province: str = None,
        city: str = None,
        address: str = None,
    ):
        # 物理空间ID
        self.physical_space_id = physical_space_id
        # 物理空间名称
        self.physical_space_name = physical_space_name
        # 所属国家
        self.country = country
        # 所属省份
        self.province = province
        # 所属城市
        self.city = city
        # 具体地址
        self.address = address

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.physical_space_id is not None:
            result['PhysicalSpaceId'] = self.physical_space_id
        if self.physical_space_name is not None:
            result['PhysicalSpaceName'] = self.physical_space_name
        if self.country is not None:
            result['Country'] = self.country
        if self.province is not None:
            result['Province'] = self.province
        if self.city is not None:
            result['City'] = self.city
        if self.address is not None:
            result['Address'] = self.address
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PhysicalSpaceId') is not None:
            self.physical_space_id = m.get('PhysicalSpaceId')
        if m.get('PhysicalSpaceName') is not None:
            self.physical_space_name = m.get('PhysicalSpaceName')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('Address') is not None:
            self.address = m.get('Address')
        return self


class GetPhysicalSpaceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        physical_space: GetPhysicalSpaceResponseBodyPhysicalSpace = None,
    ):
        # Id of the request
        self.request_id = request_id
        # 物理空间详情
        self.physical_space = physical_space

    def validate(self):
        if self.physical_space:
            self.physical_space.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.physical_space is not None:
            result['PhysicalSpace'] = self.physical_space.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PhysicalSpace') is not None:
            temp_model = GetPhysicalSpaceResponseBodyPhysicalSpace()
            self.physical_space = temp_model.from_map(m['PhysicalSpace'])
        return self


class GetPhysicalSpaceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetPhysicalSpaceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetPhysicalSpaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeletePhysicalSpaceRequest(TeaModel):
    def __init__(
        self,
        physical_space_id: str = None,
    ):
        # 实例 ID。
        self.physical_space_id = physical_space_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.physical_space_id is not None:
            result['PhysicalSpaceId'] = self.physical_space_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PhysicalSpaceId') is not None:
            self.physical_space_id = m.get('PhysicalSpaceId')
        return self


class DeletePhysicalSpaceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeletePhysicalSpaceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeletePhysicalSpaceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeletePhysicalSpaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDedicatedLineRequest(TeaModel):
    def __init__(
        self,
        physical_space_id: str = None,
        isp: str = None,
        bandwidth: int = None,
        dedicated_line_ip: str = None,
        dedicated_line_gateway: str = None,
        dedicated_line_role: str = None,
        device_id: str = None,
        device_port: str = None,
        client_token: str = None,
    ):
        # 物理空间ID
        self.physical_space_id = physical_space_id
        # 运营商
        self.isp = isp
        # 宽带（Mbps）
        self.bandwidth = bandwidth
        # 专线IP
        self.dedicated_line_ip = dedicated_line_ip
        # 专线网关
        self.dedicated_line_gateway = dedicated_line_gateway
        # 专线角色
        self.dedicated_line_role = dedicated_line_role
        # 关联设备ID
        self.device_id = device_id
        # 关联设备端口名称
        self.device_port = device_port
        # 幂等校验 token
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.physical_space_id is not None:
            result['PhysicalSpaceId'] = self.physical_space_id
        if self.isp is not None:
            result['Isp'] = self.isp
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.dedicated_line_ip is not None:
            result['DedicatedLineIp'] = self.dedicated_line_ip
        if self.dedicated_line_gateway is not None:
            result['DedicatedLineGateway'] = self.dedicated_line_gateway
        if self.dedicated_line_role is not None:
            result['DedicatedLineRole'] = self.dedicated_line_role
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.device_port is not None:
            result['DevicePort'] = self.device_port
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PhysicalSpaceId') is not None:
            self.physical_space_id = m.get('PhysicalSpaceId')
        if m.get('Isp') is not None:
            self.isp = m.get('Isp')
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('DedicatedLineIp') is not None:
            self.dedicated_line_ip = m.get('DedicatedLineIp')
        if m.get('DedicatedLineGateway') is not None:
            self.dedicated_line_gateway = m.get('DedicatedLineGateway')
        if m.get('DedicatedLineRole') is not None:
            self.dedicated_line_role = m.get('DedicatedLineRole')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('DevicePort') is not None:
            self.device_port = m.get('DevicePort')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class CreateDedicatedLineResponseBody(TeaModel):
    def __init__(
        self,
        dedicated_line_id: str = None,
        request_id: str = None,
    ):
        # 资源实例ID，如ECS实例的创建接口CreateInstance应返回InstanceId。
        self.dedicated_line_id = dedicated_line_id
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.dedicated_line_id is not None:
            result['DedicatedLineId'] = self.dedicated_line_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DedicatedLineId') is not None:
            self.dedicated_line_id = m.get('DedicatedLineId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateDedicatedLineResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateDedicatedLineResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateDedicatedLineResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


