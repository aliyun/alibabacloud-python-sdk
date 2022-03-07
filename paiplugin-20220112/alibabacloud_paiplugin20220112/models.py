# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class CreateGroupRequest(TeaModel):
    def __init__(
        self,
        algorithm: str = None,
        column: str = None,
        filter: str = None,
        inference_job_id: str = None,
        name: str = None,
        project: str = None,
        remark: str = None,
        source: int = None,
        table: str = None,
        text: str = None,
        uri: str = None,
    ):
        # 算法
        self.algorithm = algorithm
        # 手机号列名
        self.column = column
        # ODPS过滤语句
        self.filter = filter
        # 预测任务Id
        self.inference_job_id = inference_job_id
        # 人群名称。
        self.name = name
        # ODPS项目名
        self.project = project
        # 备注
        self.remark = remark
        # 人群来源。
        # - 0: Text，每行一个手机号。
        # - 1: 文本文件，每行一个手机号。
        # - 2: 带header的csv文件，需指定手机号列名。
        # - 3: Odps，需指定手机号列名。
        # - 4: Algorithm，由算法预测生成。
        self.source = source
        # ODPS表名
        self.table = table
        # 文本
        self.text = text
        # 文件地址
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm
        if self.column is not None:
            result['Column'] = self.column
        if self.filter is not None:
            result['Filter'] = self.filter
        if self.inference_job_id is not None:
            result['InferenceJobId'] = self.inference_job_id
        if self.name is not None:
            result['Name'] = self.name
        if self.project is not None:
            result['Project'] = self.project
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.source is not None:
            result['Source'] = self.source
        if self.table is not None:
            result['Table'] = self.table
        if self.text is not None:
            result['Text'] = self.text
        if self.uri is not None:
            result['Uri'] = self.uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')
        if m.get('Column') is not None:
            self.column = m.get('Column')
        if m.get('Filter') is not None:
            self.filter = m.get('Filter')
        if m.get('InferenceJobId') is not None:
            self.inference_job_id = m.get('InferenceJobId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Table') is not None:
            self.table = m.get('Table')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('Uri') is not None:
            self.uri = m.get('Uri')
        return self


class CreateGroupResponseBodyData(TeaModel):
    def __init__(
        self,
        algorithm: str = None,
        amount: int = None,
        column: str = None,
        created_time: str = None,
        filter: str = None,
        id: str = None,
        inference_job_id: str = None,
        name: str = None,
        project: str = None,
        remark: str = None,
        source: int = None,
        status: int = None,
        table: str = None,
        text: str = None,
        updated_time: str = None,
        uri: str = None,
    ):
        # 算法
        self.algorithm = algorithm
        # 人群数量。
        self.amount = amount
        # 手机号列名
        self.column = column
        # 创建时间 (UTC+8)。
        self.created_time = created_time
        # ODPS过滤语句
        self.filter = filter
        # 人群Id。
        self.id = id
        # 预测任务Id
        self.inference_job_id = inference_job_id
        # 人群名称。
        self.name = name
        # ODPS项目名
        self.project = project
        # 备注
        self.remark = remark
        # 人群来源。
        # - 0: Text，每行一个手机号。
        # - 1: 文本文件，每行一个手机号。
        # - 2: 带header的csv文件，需指定手机号列名。
        # - 3: Odps，需指定手机号列名。
        # - 4: Algorithm，由算法预测生成。
        self.source = source
        # 人群状态。
        # - 0: 检查中。
        # - 1: 已通过。
        # - 2: 未通过。
        self.status = status
        # ODPS表名
        self.table = table
        # 文本
        self.text = text
        # 更新时间 (UTC+8)。
        self.updated_time = updated_time
        # 文件地址
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.column is not None:
            result['Column'] = self.column
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.filter is not None:
            result['Filter'] = self.filter
        if self.id is not None:
            result['Id'] = self.id
        if self.inference_job_id is not None:
            result['InferenceJobId'] = self.inference_job_id
        if self.name is not None:
            result['Name'] = self.name
        if self.project is not None:
            result['Project'] = self.project
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.source is not None:
            result['Source'] = self.source
        if self.status is not None:
            result['Status'] = self.status
        if self.table is not None:
            result['Table'] = self.table
        if self.text is not None:
            result['Text'] = self.text
        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time
        if self.uri is not None:
            result['Uri'] = self.uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('Column') is not None:
            self.column = m.get('Column')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('Filter') is not None:
            self.filter = m.get('Filter')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InferenceJobId') is not None:
            self.inference_job_id = m.get('InferenceJobId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Table') is not None:
            self.table = m.get('Table')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')
        if m.get('Uri') is not None:
            self.uri = m.get('Uri')
        return self


class CreateGroupResponseBody(TeaModel):
    def __init__(
        self,
        data: CreateGroupResponseBodyData = None,
        error_code: int = None,
        error_message: str = None,
        request_id: str = None,
    ):
        # 返回数据。
        self.data = data
        # 错误码。
        self.error_code = error_code
        # 错误信息。
        self.error_message = error_message
        # 请求ID。
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = CreateGroupResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateGroupResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = CreateGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateInferenceJobRequest(TeaModel):
    def __init__(
        self,
        algorithm: str = None,
        name: str = None,
        remark: str = None,
        training_job_id: str = None,
        user_config: str = None,
    ):
        # 关联算法。
        self.algorithm = algorithm
        # 预测任务名称。
        self.name = name
        # 备注。
        self.remark = remark
        # 关联训练任务。
        self.training_job_id = training_job_id
        # 用户配置。
        self.user_config = user_config

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm
        if self.name is not None:
            result['Name'] = self.name
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.training_job_id is not None:
            result['TrainingJobId'] = self.training_job_id
        if self.user_config is not None:
            result['UserConfig'] = self.user_config
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('TrainingJobId') is not None:
            self.training_job_id = m.get('TrainingJobId')
        if m.get('UserConfig') is not None:
            self.user_config = m.get('UserConfig')
        return self


class CreateInferenceJobResponseBodyData(TeaModel):
    def __init__(
        self,
        algorithm: str = None,
        created_time: str = None,
        group_id: str = None,
        history: str = None,
        id: str = None,
        name: str = None,
        remark: str = None,
        status: int = None,
        training_job_id: str = None,
        updated_time: str = None,
        user_config: str = None,
    ):
        # 关联算法。
        self.algorithm = algorithm
        # 创建时间 (UTC+8)。
        self.created_time = created_time
        # 关联人群Id，如果任务失败则人群无效。
        self.group_id = group_id
        # 预测任务日志。
        self.history = history
        # 预测任务Id。
        self.id = id
        # 预测任务名称。
        self.name = name
        # 备注。
        self.remark = remark
        # 预测任务状态。
        self.status = status
        # 关联训练任务。
        self.training_job_id = training_job_id
        # 更新时间 (UTC+8)。
        self.updated_time = updated_time
        # 用户配置。
        self.user_config = user_config

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.history is not None:
            result['History'] = self.history
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.status is not None:
            result['Status'] = self.status
        if self.training_job_id is not None:
            result['TrainingJobId'] = self.training_job_id
        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time
        if self.user_config is not None:
            result['UserConfig'] = self.user_config
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('History') is not None:
            self.history = m.get('History')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TrainingJobId') is not None:
            self.training_job_id = m.get('TrainingJobId')
        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')
        if m.get('UserConfig') is not None:
            self.user_config = m.get('UserConfig')
        return self


class CreateInferenceJobResponseBody(TeaModel):
    def __init__(
        self,
        data: CreateInferenceJobResponseBodyData = None,
        error_code: int = None,
        error_message: str = None,
        request_id: str = None,
    ):
        # 返回数据。
        self.data = data
        # 错误码。
        self.error_code = error_code
        # 错误信息。
        self.error_message = error_message
        # 请求ID。
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = CreateInferenceJobResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateInferenceJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateInferenceJobResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = CreateInferenceJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateScheduleRequest(TeaModel):
    def __init__(
        self,
        end_time: int = None,
        execute_time: str = None,
        group_id: str = None,
        name: str = None,
        repeat_cycle: int = None,
        repeat_cycle_unit: int = None,
        repeat_times: int = None,
        sign_name: str = None,
        signature_id: str = None,
        template_code: str = None,
        template_id: str = None,
    ):
        # 终止时间（UTC+8）。
        self.end_time = end_time
        # 执行时间 (UTC+8)，为空立即执行。
        self.execute_time = execute_time
        # 人群Id。
        self.group_id = group_id
        # 触达计划名称。
        self.name = name
        # 重复周期，按重复周期与重复周期单位执行。
        self.repeat_cycle = repeat_cycle
        # 重复周期单位，若指定执行时间，则重复周期生效。
        # - 0: 从不（默认）。
        # - 1: 小时。
        # - 2: 天。
        # - 3: 周。
        # - 4: 月。
        self.repeat_cycle_unit = repeat_cycle_unit
        # 重复次数。
        # - -1: 不设终止时间（默认）。
        # - 0: 不重复。
        # - N: 重复N次后终止。
        self.repeat_times = repeat_times
        # 签名。
        self.sign_name = sign_name
        # 签名Id，或指定签名。
        self.signature_id = signature_id
        # 模板Code。
        self.template_code = template_code
        # 模板Id，或指定模板Code。
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.execute_time is not None:
            result['ExecuteTime'] = self.execute_time
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.name is not None:
            result['Name'] = self.name
        if self.repeat_cycle is not None:
            result['RepeatCycle'] = self.repeat_cycle
        if self.repeat_cycle_unit is not None:
            result['RepeatCycleUnit'] = self.repeat_cycle_unit
        if self.repeat_times is not None:
            result['RepeatTimes'] = self.repeat_times
        if self.sign_name is not None:
            result['SignName'] = self.sign_name
        if self.signature_id is not None:
            result['SignatureId'] = self.signature_id
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('ExecuteTime') is not None:
            self.execute_time = m.get('ExecuteTime')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RepeatCycle') is not None:
            self.repeat_cycle = m.get('RepeatCycle')
        if m.get('RepeatCycleUnit') is not None:
            self.repeat_cycle_unit = m.get('RepeatCycleUnit')
        if m.get('RepeatTimes') is not None:
            self.repeat_times = m.get('RepeatTimes')
        if m.get('SignName') is not None:
            self.sign_name = m.get('SignName')
        if m.get('SignatureId') is not None:
            self.signature_id = m.get('SignatureId')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class CreateScheduleResponseBodyData(TeaModel):
    def __init__(
        self,
        created_time: str = None,
        end_time: int = None,
        execute_time: str = None,
        group_id: str = None,
        id: str = None,
        name: str = None,
        repeat_cycle: int = None,
        repeat_cycle_unit: int = None,
        repeat_times: int = None,
        sign_name: str = None,
        signature_id: str = None,
        status: int = None,
        template_code: str = None,
        template_id: str = None,
        updated_time: str = None,
    ):
        # 创建时间 (UTC+8)。
        self.created_time = created_time
        # 终止时间（UTC+8）。
        self.end_time = end_time
        # 执行时间 (UTC+8)，为空立即执行。
        self.execute_time = execute_time
        # 人群Id。
        self.group_id = group_id
        # 触达计划Id。
        self.id = id
        # 触达计划名称。
        self.name = name
        # 重复周期，按重复周期与重复周期单位执行。
        self.repeat_cycle = repeat_cycle
        # 重复周期单位，若指定执行时间，则重复周期生效。
        # - 0: 从不（默认）。
        # - 1: 小时。
        # - 2: 天。
        # - 3: 周。
        # - 4: 月。
        self.repeat_cycle_unit = repeat_cycle_unit
        # 重复次数。
        # - -1: 不设终止时间（默认）。
        # - 0: 不重复。
        # - N: 重复N次后终止。
        self.repeat_times = repeat_times
        # 签名。
        self.sign_name = sign_name
        # 签名Id，或指定签名。
        self.signature_id = signature_id
        # 状态。
        # - 0: 检查中。
        # - 1: 检查成功。
        # - 2: 检查失败。
        # - 3: 发送中。
        # - 4: 发送成功。
        # - 5: 发送失败。
        self.status = status
        # 模板Code。
        self.template_code = template_code
        # 模板Id，或指定模板Code。
        self.template_id = template_id
        # 更新时间 (UTC+8)。
        self.updated_time = updated_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.execute_time is not None:
            result['ExecuteTime'] = self.execute_time
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.repeat_cycle is not None:
            result['RepeatCycle'] = self.repeat_cycle
        if self.repeat_cycle_unit is not None:
            result['RepeatCycleUnit'] = self.repeat_cycle_unit
        if self.repeat_times is not None:
            result['RepeatTimes'] = self.repeat_times
        if self.sign_name is not None:
            result['SignName'] = self.sign_name
        if self.signature_id is not None:
            result['SignatureId'] = self.signature_id
        if self.status is not None:
            result['Status'] = self.status
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('ExecuteTime') is not None:
            self.execute_time = m.get('ExecuteTime')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RepeatCycle') is not None:
            self.repeat_cycle = m.get('RepeatCycle')
        if m.get('RepeatCycleUnit') is not None:
            self.repeat_cycle_unit = m.get('RepeatCycleUnit')
        if m.get('RepeatTimes') is not None:
            self.repeat_times = m.get('RepeatTimes')
        if m.get('SignName') is not None:
            self.sign_name = m.get('SignName')
        if m.get('SignatureId') is not None:
            self.signature_id = m.get('SignatureId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')
        return self


class CreateScheduleResponseBody(TeaModel):
    def __init__(
        self,
        data: CreateScheduleResponseBodyData = None,
        error_code: int = None,
        error_message: str = None,
        request_id: str = None,
    ):
        # 返回数据。
        self.data = data
        # 错误码。
        self.error_code = error_code
        # 错误信息。
        self.error_message = error_message
        # 请求ID。
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = CreateScheduleResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateScheduleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateScheduleResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = CreateScheduleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSignatureRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
    ):
        # 申请说明。
        self.description = description
        # 签名名称。
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class CreateSignatureResponseBodyData(TeaModel):
    def __init__(
        self,
        created_time: str = None,
        id: str = None,
        name: str = None,
        status: int = None,
        updated_time: str = None,
    ):
        # 创建时间 (UTC+8)。
        self.created_time = created_time
        # 签名Id。
        self.id = id
        # 签名名称。
        self.name = name
        # 签名审核状态。
        # - 0：审核中。
        # - 1：审核通过。
        # - 2：审核不通过。
        self.status = status
        # 更新时间 (UTC+8)。
        self.updated_time = updated_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.status is not None:
            result['Status'] = self.status
        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')
        return self


class CreateSignatureResponseBody(TeaModel):
    def __init__(
        self,
        data: CreateSignatureResponseBodyData = None,
        error_code: int = None,
        error_message: str = None,
        request_id: str = None,
    ):
        # 返回数据。
        self.data = data
        # 错误码。
        self.error_code = error_code
        # 错误信息。
        self.error_message = error_message
        # 请求ID。
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = CreateSignatureResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateSignatureResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateSignatureResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = CreateSignatureResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTemplateRequest(TeaModel):
    def __init__(
        self,
        content: str = None,
        description: str = None,
        name: str = None,
        signature: str = None,
        signature_id: str = None,
        type: int = None,
    ):
        # 模板内容，请注意控制总字数在70个字以内，超出部分按长短信收费，按67个字为单位记一条短信，必须在结尾添加”回T退订“。
        self.content = content
        # 申请说明。
        self.description = description
        # 模板名称。
        self.name = name
        # 签名名称，同时只能指定签名名称或签名Id其中之一。
        self.signature = signature
        # 签名Id，可通过ListSignatures获取审核状态为已通过的签名列表，获取签名Id。
        self.signature_id = signature_id
        # 模板类型。
        # - 0 : 验证码。
        # - 1 : 短信通知。
        # - 2 : 推广短信。
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.signature is not None:
            result['Signature'] = self.signature
        if self.signature_id is not None:
            result['SignatureId'] = self.signature_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Signature') is not None:
            self.signature = m.get('Signature')
        if m.get('SignatureId') is not None:
            self.signature_id = m.get('SignatureId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreateTemplateResponseBodyData(TeaModel):
    def __init__(
        self,
        content: str = None,
        created_time: str = None,
        description: str = None,
        id: str = None,
        name: str = None,
        reason: str = None,
        signature_id: str = None,
        status: int = None,
        template_code: str = None,
        type: int = None,
        updated_time: str = None,
    ):
        # 模板内容。
        self.content = content
        # 创建时间 (UTC+8)。
        self.created_time = created_time
        # 申请说明。
        self.description = description
        # 模板Id。
        self.id = id
        # 签名名称。
        self.name = name
        # 审核意见。
        self.reason = reason
        # 签名Id。
        self.signature_id = signature_id
        # 审核状态。
        # - 0 : 审核中。
        # - 1 : 审核通过。
        # - 2 : 审核不通过。
        self.status = status
        # 模板Code。
        self.template_code = template_code
        # 模板类型。
        # - 0 : 验证码。
        # - 1 : 短信通知。
        # - 2 : 推广短信。
        self.type = type
        # 更新时间 (UTC+8)。
        self.updated_time = updated_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.signature_id is not None:
            result['SignatureId'] = self.signature_id
        if self.status is not None:
            result['Status'] = self.status
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        if self.type is not None:
            result['Type'] = self.type
        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('SignatureId') is not None:
            self.signature_id = m.get('SignatureId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')
        return self


class CreateTemplateResponseBody(TeaModel):
    def __init__(
        self,
        data: CreateTemplateResponseBodyData = None,
        error_code: int = None,
        error_message: str = None,
        request_id: str = None,
    ):
        # 返回数据。
        self.data = data
        # 错误码。
        self.error_code = error_code
        # 错误信息。
        self.error_message = error_message
        # 请求ID。
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = CreateTemplateResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateTemplateResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = CreateTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTrainingJobRequest(TeaModel):
    def __init__(
        self,
        algorithm: str = None,
        name: str = None,
        remark: str = None,
        user_config: str = None,
    ):
        # 关联算法Id。
        self.algorithm = algorithm
        # 训练任务名称。
        self.name = name
        # 备注。
        self.remark = remark
        # 用户配置。
        self.user_config = user_config

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm
        if self.name is not None:
            result['Name'] = self.name
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.user_config is not None:
            result['UserConfig'] = self.user_config
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('UserConfig') is not None:
            self.user_config = m.get('UserConfig')
        return self


class CreateTrainingJobResponseBodyData(TeaModel):
    def __init__(
        self,
        algorithm: str = None,
        created_time: str = None,
        history: str = None,
        id: str = None,
        name: str = None,
        remark: str = None,
        status: int = None,
        updated_time: str = None,
        user_config: str = None,
    ):
        # 关联算法Id。
        self.algorithm = algorithm
        # 创建时间 (UTC+8)。
        self.created_time = created_time
        # 训练任务日志。
        self.history = history
        # 训练任务Id。
        self.id = id
        # 训练任务名称。
        self.name = name
        # 备注。
        self.remark = remark
        # 训练任务状态。
        self.status = status
        # 更新时间 (UTC+8)。
        self.updated_time = updated_time
        # 用户配置。
        self.user_config = user_config

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.history is not None:
            result['History'] = self.history
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.status is not None:
            result['Status'] = self.status
        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time
        if self.user_config is not None:
            result['UserConfig'] = self.user_config
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('History') is not None:
            self.history = m.get('History')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')
        if m.get('UserConfig') is not None:
            self.user_config = m.get('UserConfig')
        return self


class CreateTrainingJobResponseBody(TeaModel):
    def __init__(
        self,
        data: CreateTrainingJobResponseBodyData = None,
        error_code: int = None,
        error_message: str = None,
        request_id: str = None,
    ):
        # 返回数据。
        self.data = data
        # 错误码。
        self.error_code = error_code
        # 错误信息。
        self.error_message = error_message
        # 请求ID。
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = CreateTrainingJobResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateTrainingJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateTrainingJobResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = CreateTrainingJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteGroupResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        error_code: int = None,
        error_message: str = None,
        request_id: str = None,
    ):
        # 返回数据。
        self.data = data
        # 错误码。
        self.error_code = error_code
        # 错误信息。
        self.error_message = error_message
        # 请求ID。
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteGroupResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = DeleteGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteInferenceJobResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        error_code: int = None,
        error_message: str = None,
        request_id: str = None,
    ):
        # 返回数据。
        self.data = data
        # 错误码。
        self.error_code = error_code
        # 错误信息。
        self.error_message = error_message
        # 请求ID。
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteInferenceJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteInferenceJobResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = DeleteInferenceJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteScheduleResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        error_code: int = None,
        error_message: str = None,
        request_id: str = None,
    ):
        # 返回数据。
        self.data = data
        # 错误码。
        self.error_code = error_code
        # 错误信息。
        self.error_message = error_message
        # 请求ID。
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteScheduleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteScheduleResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = DeleteScheduleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSignatureResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        error_code: int = None,
        error_message: str = None,
        request_id: str = None,
    ):
        # 返回数据。
        self.data = data
        # 错误码。
        self.error_code = error_code
        # 错误信息。
        self.error_message = error_message
        # 请求ID。
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteSignatureResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteSignatureResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = DeleteSignatureResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteTemplateResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        error_code: int = None,
        error_message: str = None,
        request_id: str = None,
    ):
        # 返回数据。
        self.data = data
        # 错误码。
        self.error_code = error_code
        # 错误信息。
        self.error_message = error_message
        # 请求ID。
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteTemplateResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = DeleteTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteTrainingJobResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        error_code: int = None,
        error_message: str = None,
        request_id: str = None,
    ):
        # 返回数据。
        self.data = data
        # 错误码。
        self.error_code = error_code
        # 错误信息。
        self.error_message = error_message
        # 请求ID。
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteTrainingJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteTrainingJobResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = DeleteTrainingJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAlgorithmResponseBodyData(TeaModel):
    def __init__(
        self,
        description: str = None,
        id: str = None,
        infer_user_config_map: str = None,
        name: str = None,
        train_user_config_map: str = None,
    ):
        # 算法说明。
        self.description = description
        # 算法Id。
        self.id = id
        # 预测所需参数名与对应的参数说明。
        self.infer_user_config_map = infer_user_config_map
        # 算法名称。
        self.name = name
        # 训练所需参数名与对应的参数说明。
        self.train_user_config_map = train_user_config_map

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.infer_user_config_map is not None:
            result['InferUserConfigMap'] = self.infer_user_config_map
        if self.name is not None:
            result['Name'] = self.name
        if self.train_user_config_map is not None:
            result['TrainUserConfigMap'] = self.train_user_config_map
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InferUserConfigMap') is not None:
            self.infer_user_config_map = m.get('InferUserConfigMap')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('TrainUserConfigMap') is not None:
            self.train_user_config_map = m.get('TrainUserConfigMap')
        return self


class GetAlgorithmResponseBody(TeaModel):
    def __init__(
        self,
        data: GetAlgorithmResponseBodyData = None,
        error_code: int = None,
        error_message: str = None,
        request_id: str = None,
    ):
        # 返回数据。
        self.data = data
        # 错误码。
        self.error_code = error_code
        # 错误信息。
        self.error_message = error_message
        # 请求ID。
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GetAlgorithmResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetAlgorithmResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetAlgorithmResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = GetAlgorithmResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetGroupResponseBodyData(TeaModel):
    def __init__(
        self,
        algorithm: str = None,
        amount: int = None,
        column: str = None,
        created_time: str = None,
        filter: str = None,
        id: str = None,
        inference_job_id: str = None,
        name: str = None,
        project: str = None,
        remark: str = None,
        source: int = None,
        status: int = None,
        table: str = None,
        text: str = None,
        updated_time: str = None,
        uri: str = None,
    ):
        # 算法
        self.algorithm = algorithm
        # 人群数量。
        self.amount = amount
        # 手机号列名
        self.column = column
        # 创建时间 (UTC+8)。
        self.created_time = created_time
        # ODPS过滤语句
        self.filter = filter
        # 人群Id。
        self.id = id
        # 预测任务Id
        self.inference_job_id = inference_job_id
        # 人群名称。
        self.name = name
        # ODPS项目名
        self.project = project
        # 备注
        self.remark = remark
        # 人群来源。
        # - 0: Text，每行一个手机号。
        # - 1: 文本文件，每行一个手机号。
        # - 2: 带header的csv文件，需指定手机号列名。
        # - 3: Odps，需指定手机号列名。
        # - 4: Algorithm，由算法预测生成。
        self.source = source
        # 人群状态。
        # - 0: 检查中。
        # - 1: 已通过。
        # - 2: 未通过。
        self.status = status
        # ODPS表名
        self.table = table
        # 文本
        self.text = text
        # 更新时间 (UTC+8)。
        self.updated_time = updated_time
        # 文件地址
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.column is not None:
            result['Column'] = self.column
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.filter is not None:
            result['Filter'] = self.filter
        if self.id is not None:
            result['Id'] = self.id
        if self.inference_job_id is not None:
            result['InferenceJobId'] = self.inference_job_id
        if self.name is not None:
            result['Name'] = self.name
        if self.project is not None:
            result['Project'] = self.project
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.source is not None:
            result['Source'] = self.source
        if self.status is not None:
            result['Status'] = self.status
        if self.table is not None:
            result['Table'] = self.table
        if self.text is not None:
            result['Text'] = self.text
        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time
        if self.uri is not None:
            result['Uri'] = self.uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('Column') is not None:
            self.column = m.get('Column')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('Filter') is not None:
            self.filter = m.get('Filter')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InferenceJobId') is not None:
            self.inference_job_id = m.get('InferenceJobId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Table') is not None:
            self.table = m.get('Table')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')
        if m.get('Uri') is not None:
            self.uri = m.get('Uri')
        return self


class GetGroupResponseBody(TeaModel):
    def __init__(
        self,
        data: GetGroupResponseBodyData = None,
        error_code: int = None,
        error_message: str = None,
        request_id: str = None,
    ):
        # 返回数据。
        self.data = data
        # 错误码。
        self.error_code = error_code
        # 错误信息。
        self.error_message = error_message
        # 请求ID。
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GetGroupResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetGroupResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = GetGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetInferenceJobResponseBodyData(TeaModel):
    def __init__(
        self,
        algorithm: str = None,
        created_time: str = None,
        group_id: str = None,
        history: str = None,
        id: str = None,
        name: str = None,
        remark: str = None,
        status: int = None,
        training_job_id: str = None,
        updated_time: str = None,
        user_config: str = None,
    ):
        # 关联算法。
        self.algorithm = algorithm
        # 创建时间 (UTC+8)。
        self.created_time = created_time
        # 关联人群Id，如果任务失败则人群无效。
        self.group_id = group_id
        # 预测任务日志。
        self.history = history
        # 预测任务Id。
        self.id = id
        # 预测任务名称。
        self.name = name
        # 备注。
        self.remark = remark
        # 预测任务状态。
        self.status = status
        # 关联训练任务。
        self.training_job_id = training_job_id
        # 更新时间 (UTC+8)。
        self.updated_time = updated_time
        # 用户配置。
        self.user_config = user_config

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.history is not None:
            result['History'] = self.history
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.status is not None:
            result['Status'] = self.status
        if self.training_job_id is not None:
            result['TrainingJobId'] = self.training_job_id
        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time
        if self.user_config is not None:
            result['UserConfig'] = self.user_config
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('History') is not None:
            self.history = m.get('History')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TrainingJobId') is not None:
            self.training_job_id = m.get('TrainingJobId')
        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')
        if m.get('UserConfig') is not None:
            self.user_config = m.get('UserConfig')
        return self


class GetInferenceJobResponseBody(TeaModel):
    def __init__(
        self,
        data: GetInferenceJobResponseBodyData = None,
        error_code: int = None,
        error_message: str = None,
        request_id: str = None,
    ):
        # 返回数据。
        self.data = data
        # 错误码。
        self.error_code = error_code
        # 错误信息。
        self.error_message = error_message
        # 请求ID。
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GetInferenceJobResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetInferenceJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetInferenceJobResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = GetInferenceJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMessageConfigResponseBodyData(TeaModel):
    def __init__(
        self,
        sms_report_url: str = None,
        sms_up_url: str = None,
    ):
        # 短信发送状态回执接收服务地址。
        self.sms_report_url = sms_report_url
        # 上行短信消息接收服务地址。
        self.sms_up_url = sms_up_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sms_report_url is not None:
            result['SmsReportUrl'] = self.sms_report_url
        if self.sms_up_url is not None:
            result['SmsUpUrl'] = self.sms_up_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SmsReportUrl') is not None:
            self.sms_report_url = m.get('SmsReportUrl')
        if m.get('SmsUpUrl') is not None:
            self.sms_up_url = m.get('SmsUpUrl')
        return self


class GetMessageConfigResponseBody(TeaModel):
    def __init__(
        self,
        data: GetMessageConfigResponseBodyData = None,
        error_code: int = None,
        error_message: str = None,
        request_id: str = None,
    ):
        # 返回数据。
        self.data = data
        # 错误码。
        self.error_code = error_code
        # 错误信息。
        self.error_message = error_message
        # 请求ID。
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GetMessageConfigResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetMessageConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetMessageConfigResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = GetMessageConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetScheduleResponseBodyData(TeaModel):
    def __init__(
        self,
        created_time: str = None,
        end_time: int = None,
        execute_time: str = None,
        group_id: str = None,
        history: str = None,
        id: str = None,
        name: str = None,
        repeat_cycle: int = None,
        repeat_cycle_unit: int = None,
        repeat_times: int = None,
        sign_name: str = None,
        signature_id: str = None,
        status: int = None,
        template_code: str = None,
        template_id: str = None,
        updated_time: str = None,
    ):
        # 创建时间 (UTC+8)。
        self.created_time = created_time
        # 终止时间（UTC+8）。
        self.end_time = end_time
        # 执行时间 (UTC+8)，为空立即执行。
        self.execute_time = execute_time
        # 人群Id。
        self.group_id = group_id
        # 历史记录。
        self.history = history
        # 触达计划Id。
        self.id = id
        # 触达计划名称。
        self.name = name
        # 重复周期，按重复周期与重复周期单位执行。
        self.repeat_cycle = repeat_cycle
        # 重复周期单位，若指定执行时间，则重复周期生效。
        # - 0: 从不（默认）。
        # - 1: 小时。
        # - 2: 天。
        # - 3: 周。
        # - 4: 月。
        self.repeat_cycle_unit = repeat_cycle_unit
        # 重复次数。
        # - -1: 不设终止时间（默认）。
        # - 0: 不重复。
        # - N: 重复N次后终止。
        self.repeat_times = repeat_times
        # 签名。
        self.sign_name = sign_name
        # 签名Id，或指定签名。
        self.signature_id = signature_id
        # 状态。
        # - 0: 检查中。
        # - 1: 检查成功。
        # - 2: 检查失败。
        # - 3: 发送中。
        # - 4: 发送成功。
        # - 5: 发送失败。
        self.status = status
        # 模板Code。
        self.template_code = template_code
        # 模板Id，或指定模板Code。
        self.template_id = template_id
        # 更新时间 (UTC+8)。
        self.updated_time = updated_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.execute_time is not None:
            result['ExecuteTime'] = self.execute_time
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.history is not None:
            result['History'] = self.history
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.repeat_cycle is not None:
            result['RepeatCycle'] = self.repeat_cycle
        if self.repeat_cycle_unit is not None:
            result['RepeatCycleUnit'] = self.repeat_cycle_unit
        if self.repeat_times is not None:
            result['RepeatTimes'] = self.repeat_times
        if self.sign_name is not None:
            result['SignName'] = self.sign_name
        if self.signature_id is not None:
            result['SignatureId'] = self.signature_id
        if self.status is not None:
            result['Status'] = self.status
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('ExecuteTime') is not None:
            self.execute_time = m.get('ExecuteTime')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('History') is not None:
            self.history = m.get('History')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RepeatCycle') is not None:
            self.repeat_cycle = m.get('RepeatCycle')
        if m.get('RepeatCycleUnit') is not None:
            self.repeat_cycle_unit = m.get('RepeatCycleUnit')
        if m.get('RepeatTimes') is not None:
            self.repeat_times = m.get('RepeatTimes')
        if m.get('SignName') is not None:
            self.sign_name = m.get('SignName')
        if m.get('SignatureId') is not None:
            self.signature_id = m.get('SignatureId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')
        return self


class GetScheduleResponseBody(TeaModel):
    def __init__(
        self,
        data: GetScheduleResponseBodyData = None,
        error_code: int = None,
        error_message: str = None,
        request_id: str = None,
    ):
        # 返回数据。
        self.data = data
        # 错误码。
        self.error_code = error_code
        # 错误信息。
        self.error_message = error_message
        # 请求ID。
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GetScheduleResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetScheduleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetScheduleResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = GetScheduleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSignatureResponseBodyData(TeaModel):
    def __init__(
        self,
        created_time: str = None,
        description: str = None,
        id: str = None,
        name: str = None,
        reason: str = None,
        status: int = None,
        updated_time: str = None,
    ):
        # 创建时间 (UTC+8)。
        self.created_time = created_time
        # 申请说明。
        self.description = description
        # 签名Id。
        self.id = id
        # 签名名称。
        self.name = name
        # 审核建议。
        self.reason = reason
        # 签名审核状态。
        # - 0：审核中。
        # - 1：审核通过。
        # - 2：审核不通过。
        self.status = status
        # 更新时间 (UTC+8)。
        self.updated_time = updated_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.status is not None:
            result['Status'] = self.status
        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')
        return self


class GetSignatureResponseBody(TeaModel):
    def __init__(
        self,
        data: GetSignatureResponseBodyData = None,
        error_code: int = None,
        error_message: str = None,
        request_id: str = None,
    ):
        # 返回数据。
        self.data = data
        # 错误码。
        self.error_code = error_code
        # 错误信息。
        self.error_message = error_message
        # 请求ID。
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GetSignatureResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetSignatureResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetSignatureResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = GetSignatureResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTemplateResponseBodyData(TeaModel):
    def __init__(
        self,
        content: str = None,
        created_time: str = None,
        description: str = None,
        id: str = None,
        name: str = None,
        reason: str = None,
        signature_id: str = None,
        status: int = None,
        template_code: str = None,
        type: int = None,
        updated_time: str = None,
    ):
        # 模板内容。
        self.content = content
        # 创建时间 (UTC+8)。
        self.created_time = created_time
        # 申请说明。
        self.description = description
        # 模板Id。
        self.id = id
        # 签名名称。
        self.name = name
        # 审核意见。
        self.reason = reason
        # 签名Id。
        self.signature_id = signature_id
        # 审核状态。
        # - 0 : 审核中。
        # - 1 : 审核通过。
        # - 2 : 审核不通过。
        self.status = status
        # 模板Code。
        self.template_code = template_code
        # 模板类型。
        # - 0 : 验证码。
        # - 1 : 短信通知。
        # - 2 : 推广短信。
        self.type = type
        # 更新时间 (UTC+8)。
        self.updated_time = updated_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.signature_id is not None:
            result['SignatureId'] = self.signature_id
        if self.status is not None:
            result['Status'] = self.status
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        if self.type is not None:
            result['Type'] = self.type
        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('SignatureId') is not None:
            self.signature_id = m.get('SignatureId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')
        return self


class GetTemplateResponseBody(TeaModel):
    def __init__(
        self,
        data: GetTemplateResponseBodyData = None,
        error_code: int = None,
        error_message: str = None,
        request_id: str = None,
    ):
        # 返回数据。
        self.data = data
        # 错误码。
        self.error_code = error_code
        # 错误信息。
        self.error_message = error_message
        # 请求ID。
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GetTemplateResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetTemplateResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = GetTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTrainingJobResponseBodyData(TeaModel):
    def __init__(
        self,
        algorithm: str = None,
        created_time: str = None,
        history: str = None,
        id: str = None,
        name: str = None,
        remark: str = None,
        status: int = None,
        updated_time: str = None,
        user_config: str = None,
    ):
        # 关联算法Id。
        self.algorithm = algorithm
        # 创建时间 (UTC+8)。
        self.created_time = created_time
        # 训练任务日志。
        self.history = history
        # 训练任务Id。
        self.id = id
        # 训练任务名称。
        self.name = name
        # 备注。
        self.remark = remark
        # 训练任务状态。
        self.status = status
        # 更新时间 (UTC+8)。
        self.updated_time = updated_time
        # 用户配置。
        self.user_config = user_config

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.history is not None:
            result['History'] = self.history
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.status is not None:
            result['Status'] = self.status
        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time
        if self.user_config is not None:
            result['UserConfig'] = self.user_config
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('History') is not None:
            self.history = m.get('History')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')
        if m.get('UserConfig') is not None:
            self.user_config = m.get('UserConfig')
        return self


class GetTrainingJobResponseBody(TeaModel):
    def __init__(
        self,
        data: GetTrainingJobResponseBodyData = None,
        error_code: int = None,
        error_message: str = None,
        request_id: str = None,
    ):
        # 返回数据。
        self.data = data
        # 错误码。
        self.error_code = error_code
        # 错误信息。
        self.error_message = error_message
        # 请求ID。
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GetTrainingJobResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetTrainingJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetTrainingJobResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = GetTrainingJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUserResponseBodyData(TeaModel):
    def __init__(
        self,
        account_status: int = None,
    ):
        # 账号状态。
        # - 0 : 正常使用。
        # - 1 : 因欠费等原因暂时停用。
        # - 2 : 已释放产品。
        self.account_status = account_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_status is not None:
            result['AccountStatus'] = self.account_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountStatus') is not None:
            self.account_status = m.get('AccountStatus')
        return self


class GetUserResponseBody(TeaModel):
    def __init__(
        self,
        data: GetUserResponseBodyData = None,
        error_code: int = None,
        error_message: str = None,
        request_id: str = None,
    ):
        # 返回数据。
        self.data = data
        # 错误码。
        self.error_code = error_code
        # 错误信息。
        self.error_message = error_message
        # 请求ID。
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GetUserResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetUserResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = GetUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAlgorithmsRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # 算法Id过滤。
        self.id = id
        # 算法名称过滤。
        self.name = name
        # 分页数，从1开始，默认为1。
        self.page_number = page_number
        # 分页大小，默认为10。
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListAlgorithmsResponseBodyDataAlgorithms(TeaModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
    ):
        # 算法Id。
        self.id = id
        # 算法名称。
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class ListAlgorithmsResponseBodyData(TeaModel):
    def __init__(
        self,
        algorithms: List[ListAlgorithmsResponseBodyDataAlgorithms] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # 算法列表。
        self.algorithms = algorithms
        # 分页数，从1开始，默认为1。
        self.page_number = page_number
        # 分页大小，默认为10。
        self.page_size = page_size
        # 总算法数量。
        self.total_count = total_count

    def validate(self):
        if self.algorithms:
            for k in self.algorithms:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Algorithms'] = []
        if self.algorithms is not None:
            for k in self.algorithms:
                result['Algorithms'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.algorithms = []
        if m.get('Algorithms') is not None:
            for k in m.get('Algorithms'):
                temp_model = ListAlgorithmsResponseBodyDataAlgorithms()
                self.algorithms.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListAlgorithmsResponseBody(TeaModel):
    def __init__(
        self,
        data: ListAlgorithmsResponseBodyData = None,
        error_code: int = None,
        error_message: str = None,
        request_id: str = None,
    ):
        # 返回数据。
        self.data = data
        # 错误码。
        self.error_code = error_code
        # 错误信息。
        self.error_message = error_message
        # 请求ID。
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = ListAlgorithmsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListAlgorithmsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListAlgorithmsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = ListAlgorithmsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListGroupsRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        page_number: int = None,
        page_size: int = None,
        remark: str = None,
        source: int = None,
        status: int = None,
    ):
        # 人群名称过滤。
        self.name = name
        # 分页数，从1开始，默认为1。
        self.page_number = page_number
        # 分页大小，默认为10。
        self.page_size = page_size
        # 人群备注过滤。
        self.remark = remark
        # 来源过滤。
        self.source = source
        # 审核状态过滤。
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.source is not None:
            result['Source'] = self.source
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListGroupsResponseBodyDataGroups(TeaModel):
    def __init__(
        self,
        algorithm: str = None,
        amount: int = None,
        column: str = None,
        created_time: str = None,
        filter: str = None,
        id: str = None,
        inference_job_id: str = None,
        name: str = None,
        project: str = None,
        remark: str = None,
        source: int = None,
        status: int = None,
        table: str = None,
        text: str = None,
        updated_time: str = None,
        uri: str = None,
    ):
        # 算法
        self.algorithm = algorithm
        # 人群数量。
        self.amount = amount
        # 手机号列名
        self.column = column
        # 创建时间 (UTC+8)。
        self.created_time = created_time
        # ODPS过滤语句
        self.filter = filter
        # 人群Id。
        self.id = id
        # 预测任务Id
        self.inference_job_id = inference_job_id
        # 人群名称。
        self.name = name
        # ODPS项目名
        self.project = project
        # 备注
        self.remark = remark
        # 人群来源。
        # - 0: Text，每行一个手机号。
        # - 1: 文本文件，每行一个手机号。
        # - 2: 带header的csv文件，需指定手机号列名。
        # - 3: Odps，需指定手机号列名。
        # - 4: Algorithm，由算法预测生成。
        self.source = source
        # 人群状态。
        # - 0: 检查中。
        # - 1: 已通过。
        # - 2: 未通过。
        self.status = status
        # ODPS表名
        self.table = table
        # 文本
        self.text = text
        # 更新时间 (UTC+8)。
        self.updated_time = updated_time
        # 文件地址
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.column is not None:
            result['Column'] = self.column
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.filter is not None:
            result['Filter'] = self.filter
        if self.id is not None:
            result['Id'] = self.id
        if self.inference_job_id is not None:
            result['InferenceJobId'] = self.inference_job_id
        if self.name is not None:
            result['Name'] = self.name
        if self.project is not None:
            result['Project'] = self.project
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.source is not None:
            result['Source'] = self.source
        if self.status is not None:
            result['Status'] = self.status
        if self.table is not None:
            result['Table'] = self.table
        if self.text is not None:
            result['Text'] = self.text
        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time
        if self.uri is not None:
            result['Uri'] = self.uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('Column') is not None:
            self.column = m.get('Column')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('Filter') is not None:
            self.filter = m.get('Filter')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InferenceJobId') is not None:
            self.inference_job_id = m.get('InferenceJobId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Table') is not None:
            self.table = m.get('Table')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')
        if m.get('Uri') is not None:
            self.uri = m.get('Uri')
        return self


class ListGroupsResponseBodyData(TeaModel):
    def __init__(
        self,
        groups: List[ListGroupsResponseBodyDataGroups] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # 人群列表。
        self.groups = groups
        # 分页数，从1开始，默认为1。
        self.page_number = page_number
        # 分页大小，默认为10。
        self.page_size = page_size
        # 总人群数量。
        self.total_count = total_count

    def validate(self):
        if self.groups:
            for k in self.groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Groups'] = []
        if self.groups is not None:
            for k in self.groups:
                result['Groups'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.groups = []
        if m.get('Groups') is not None:
            for k in m.get('Groups'):
                temp_model = ListGroupsResponseBodyDataGroups()
                self.groups.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListGroupsResponseBody(TeaModel):
    def __init__(
        self,
        data: ListGroupsResponseBodyData = None,
        error_code: int = None,
        error_message: str = None,
        request_id: str = None,
    ):
        # 返回数据。
        self.data = data
        # 错误码。
        self.error_code = error_code
        # 错误信息。
        self.error_message = error_message
        # 请求ID。
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = ListGroupsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListGroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListGroupsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = ListGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInferenceJobsRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        page_number: int = None,
        page_size: int = None,
        remark: str = None,
        status: int = None,
    ):
        # 预测任务名称过滤。
        self.name = name
        # 分页数，从1开始，默认为1。
        self.page_number = page_number
        # 分页大小，默认为10。
        self.page_size = page_size
        # 预测任务备注过滤。
        self.remark = remark
        # 预测任务状态过滤。
        # - 0: 队列中。
        # - 1: 已提交。
        # - 2: 运行中。
        # - 3: 成功。
        # - 4: 失败。
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListInferenceJobsResponseBodyDataInferenceJobs(TeaModel):
    def __init__(
        self,
        algorithm: str = None,
        created_time: str = None,
        group_id: str = None,
        history: str = None,
        id: str = None,
        name: str = None,
        remark: str = None,
        status: int = None,
        training_job_id: str = None,
        updated_time: str = None,
        user_config: str = None,
    ):
        # 关联算法。
        self.algorithm = algorithm
        # 创建时间 (UTC+8)。
        self.created_time = created_time
        # 关联人群Id，如果任务失败则人群无效。
        self.group_id = group_id
        # 预测任务日志。
        self.history = history
        # 预测任务Id。
        self.id = id
        # 预测任务名称。
        self.name = name
        # 备注。
        self.remark = remark
        # 预测任务状态。
        self.status = status
        # 关联训练任务。
        self.training_job_id = training_job_id
        # 更新时间 (UTC+8)。
        self.updated_time = updated_time
        # 用户配置。
        self.user_config = user_config

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.history is not None:
            result['History'] = self.history
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.status is not None:
            result['Status'] = self.status
        if self.training_job_id is not None:
            result['TrainingJobId'] = self.training_job_id
        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time
        if self.user_config is not None:
            result['UserConfig'] = self.user_config
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('History') is not None:
            self.history = m.get('History')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TrainingJobId') is not None:
            self.training_job_id = m.get('TrainingJobId')
        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')
        if m.get('UserConfig') is not None:
            self.user_config = m.get('UserConfig')
        return self


class ListInferenceJobsResponseBodyData(TeaModel):
    def __init__(
        self,
        inference_jobs: List[ListInferenceJobsResponseBodyDataInferenceJobs] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # 预测任务列表。
        self.inference_jobs = inference_jobs
        # 分页数，从1开始，默认为1。
        self.page_number = page_number
        # 分页大小，默认为10。
        self.page_size = page_size
        # 总预测任务数量。
        self.total_count = total_count

    def validate(self):
        if self.inference_jobs:
            for k in self.inference_jobs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['InferenceJobs'] = []
        if self.inference_jobs is not None:
            for k in self.inference_jobs:
                result['InferenceJobs'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.inference_jobs = []
        if m.get('InferenceJobs') is not None:
            for k in m.get('InferenceJobs'):
                temp_model = ListInferenceJobsResponseBodyDataInferenceJobs()
                self.inference_jobs.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListInferenceJobsResponseBody(TeaModel):
    def __init__(
        self,
        data: ListInferenceJobsResponseBodyData = None,
        error_code: int = None,
        error_message: str = None,
        request_id: str = None,
    ):
        # 返回数据。
        self.data = data
        # 错误码。
        self.error_code = error_code
        # 错误信息。
        self.error_message = error_message
        # 请求ID。
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = ListInferenceJobsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListInferenceJobsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListInferenceJobsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = ListInferenceJobsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListMessageMetricsRequest(TeaModel):
    def __init__(
        self,
        end_date: str = None,
        group_id: str = None,
        page_number: int = None,
        page_size: int = None,
        schedule_id: str = None,
        signature: str = None,
        signature_id: str = None,
        start_date: str = None,
        template_code: str = None,
        template_id: str = None,
        template_type: int = None,
    ):
        # 结束日期，格式20220102。
        self.end_date = end_date
        # 关联人群Id。
        self.group_id = group_id
        # 分页数，从1开始，默认为1。
        self.page_number = page_number
        # 分页大小，默认为10。
        self.page_size = page_size
        # 关联触达计划Id。
        self.schedule_id = schedule_id
        # 签名名称。
        self.signature = signature
        # 签名Id，同时只能指定签名名称或签名Id其中之一。
        self.signature_id = signature_id
        # 开始日期，格式20220102。
        self.start_date = start_date
        # 模板号。
        self.template_code = template_code
        # 模板Id，同时只能指定模板Code或模板Id其中之一。
        self.template_id = template_id
        # 模板类型。
        # - 0 : 验证码。
        # - 1 : 短信通知。
        # - 2 : 推广短信。
        self.template_type = template_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.schedule_id is not None:
            result['ScheduleId'] = self.schedule_id
        if self.signature is not None:
            result['Signature'] = self.signature
        if self.signature_id is not None:
            result['SignatureId'] = self.signature_id
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ScheduleId') is not None:
            self.schedule_id = m.get('ScheduleId')
        if m.get('Signature') is not None:
            self.signature = m.get('Signature')
        if m.get('SignatureId') is not None:
            self.signature_id = m.get('SignatureId')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        return self


class ListMessageMetricsResponseBodyDataMetrics(TeaModel):
    def __init__(
        self,
        date: str = None,
        fail: int = None,
        pending: int = None,
        rate: float = None,
        success: int = None,
        total: int = None,
    ):
        # 发送日期。
        self.date = date
        # 发送失败。
        self.fail = fail
        # 发送中。
        self.pending = pending
        # 发送成功率。
        self.rate = rate
        # 发送成功。
        self.success = success
        # 总计短信数量。
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.date is not None:
            result['Date'] = self.date
        if self.fail is not None:
            result['Fail'] = self.fail
        if self.pending is not None:
            result['Pending'] = self.pending
        if self.rate is not None:
            result['Rate'] = self.rate
        if self.success is not None:
            result['Success'] = self.success
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Date') is not None:
            self.date = m.get('Date')
        if m.get('Fail') is not None:
            self.fail = m.get('Fail')
        if m.get('Pending') is not None:
            self.pending = m.get('Pending')
        if m.get('Rate') is not None:
            self.rate = m.get('Rate')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListMessageMetricsResponseBodyData(TeaModel):
    def __init__(
        self,
        metrics: List[ListMessageMetricsResponseBodyDataMetrics] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # 分页返回的统计数据条目列表。
        self.metrics = metrics
        # 分页数，从1开始，默认为1。
        self.page_number = page_number
        # 分页大小，默认为10。
        self.page_size = page_size
        # 总统计数据条目数量。
        self.total_count = total_count

    def validate(self):
        if self.metrics:
            for k in self.metrics:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Metrics'] = []
        if self.metrics is not None:
            for k in self.metrics:
                result['Metrics'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.metrics = []
        if m.get('Metrics') is not None:
            for k in m.get('Metrics'):
                temp_model = ListMessageMetricsResponseBodyDataMetrics()
                self.metrics.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListMessageMetricsResponseBody(TeaModel):
    def __init__(
        self,
        data: ListMessageMetricsResponseBodyData = None,
        error_code: int = None,
        error_message: str = None,
        request_id: str = None,
    ):
        # 返回数据。
        self.data = data
        # 错误码。
        self.error_code = error_code
        # 错误信息。
        self.error_message = error_message
        # 请求ID。
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = ListMessageMetricsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListMessageMetricsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListMessageMetricsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = ListMessageMetricsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListMessagesRequest(TeaModel):
    def __init__(
        self,
        datetime: str = None,
        group_id: str = None,
        message_id: str = None,
        page_number: int = None,
        page_size: int = None,
        phone_number: str = None,
        request_id: str = None,
        schedule_id: str = None,
        signature: str = None,
        signature_id: str = None,
        status: int = None,
        template_code: str = None,
        template_id: str = None,
        template_type: int = None,
    ):
        # 发送日期，格式为20220101。
        self.datetime = datetime
        # 关联人群Id过滤。
        self.group_id = group_id
        # 短信Id过滤，短信Id为SendMessage成功返回的Id。
        self.message_id = message_id
        # 分页数，从1开始，默认为1。
        self.page_number = page_number
        # 分页大小，默认为10。
        self.page_size = page_size
        # 手机号码过滤。
        self.phone_number = phone_number
        # 短信批处理Id过滤，短信批处理Id为SendMessage成功返回的RequestId。
        self.request_id = request_id
        # 关联触达计划Id过滤。
        self.schedule_id = schedule_id
        # 签名名称过滤。
        self.signature = signature
        # 签名Id过滤，同时只能指定签名名称或签名Id其中之一。
        self.signature_id = signature_id
        # 短信发送状态过滤。
        # - 0 : 发送中。
        # - 1 : 发送成功。
        # - 2 : 发送失败。
        self.status = status
        # 模板号过滤。
        self.template_code = template_code
        # 模板Id过滤，同时只能指定模板Code或模板Id其中之一。
        self.template_id = template_id
        # 模板类型过滤。
        # - 0 : 验证码。
        # - 1 : 短信通知。
        # - 2 : 推广短信。
        self.template_type = template_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.datetime is not None:
            result['Datetime'] = self.datetime
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.message_id is not None:
            result['MessageId'] = self.message_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.schedule_id is not None:
            result['ScheduleId'] = self.schedule_id
        if self.signature is not None:
            result['Signature'] = self.signature
        if self.signature_id is not None:
            result['SignatureId'] = self.signature_id
        if self.status is not None:
            result['Status'] = self.status
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Datetime') is not None:
            self.datetime = m.get('Datetime')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ScheduleId') is not None:
            self.schedule_id = m.get('ScheduleId')
        if m.get('Signature') is not None:
            self.signature = m.get('Signature')
        if m.get('SignatureId') is not None:
            self.signature_id = m.get('SignatureId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        return self


class ListMessagesResponseBodyDataMessages(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        group_id: str = None,
        id: str = None,
        out_id: str = None,
        phone_number: str = None,
        schedule_id: str = None,
        signature: str = None,
        status: int = None,
        template_code: str = None,
        template_params: str = None,
        template_type: int = None,
    ):
        # 错误码。
        self.error_code = error_code
        # 关联人群Id，未关联则为空。
        self.group_id = group_id
        # 短信序列号。
        self.id = id
        # 外部拓展字段。
        self.out_id = out_id
        # 手机号码。
        self.phone_number = phone_number
        # 关联触达计划Id，未关联则为空。
        self.schedule_id = schedule_id
        # 签名名称。
        self.signature = signature
        # 短信发送状态。
        # - 0 : 发送中。
        # - 1 : 发送成功。
        # - 2 : 发送失败。
        self.status = status
        # 模板号。
        self.template_code = template_code
        # 模板参数。
        self.template_params = template_params
        # 模板类型。
        # - 0 : 验证码。
        # - 1 : 短信通知。
        # - 2 : 推广短信。
        self.template_type = template_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.id is not None:
            result['Id'] = self.id
        if self.out_id is not None:
            result['OutId'] = self.out_id
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.schedule_id is not None:
            result['ScheduleId'] = self.schedule_id
        if self.signature is not None:
            result['Signature'] = self.signature
        if self.status is not None:
            result['Status'] = self.status
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        if self.template_params is not None:
            result['TemplateParams'] = self.template_params
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OutId') is not None:
            self.out_id = m.get('OutId')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('ScheduleId') is not None:
            self.schedule_id = m.get('ScheduleId')
        if m.get('Signature') is not None:
            self.signature = m.get('Signature')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        if m.get('TemplateParams') is not None:
            self.template_params = m.get('TemplateParams')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        return self


class ListMessagesResponseBodyData(TeaModel):
    def __init__(
        self,
        messages: List[ListMessagesResponseBodyDataMessages] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # 短信列表。
        self.messages = messages
        # 分页数，从1开始，默认为1。
        self.page_number = page_number
        # 分页大小，默认为10。
        self.page_size = page_size
        # 短信数量。
        self.total_count = total_count

    def validate(self):
        if self.messages:
            for k in self.messages:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Messages'] = []
        if self.messages is not None:
            for k in self.messages:
                result['Messages'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.messages = []
        if m.get('Messages') is not None:
            for k in m.get('Messages'):
                temp_model = ListMessagesResponseBodyDataMessages()
                self.messages.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListMessagesResponseBody(TeaModel):
    def __init__(
        self,
        data: ListMessagesResponseBodyData = None,
        error_code: int = None,
        error_message: str = None,
        request_id: str = None,
    ):
        # 返回数据。
        self.data = data
        # 错误码。
        self.error_code = error_code
        # 错误信息。
        self.error_message = error_message
        # 请求ID。
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = ListMessagesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListMessagesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListMessagesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = ListMessagesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSchedulesRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        page_number: int = None,
        page_size: int = None,
        status: int = None,
    ):
        # 触达计划名称过滤。
        self.name = name
        # 分页数，从1开始，默认为1。
        self.page_number = page_number
        # 分页大小，默认为10。
        self.page_size = page_size
        # 发送状态过滤。
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListSchedulesResponseBodyDataSchedules(TeaModel):
    def __init__(
        self,
        created_time: str = None,
        end_time: int = None,
        execute_time: str = None,
        group_id: str = None,
        id: str = None,
        name: str = None,
        repeat_cycle: int = None,
        repeat_cycle_unit: int = None,
        repeat_times: int = None,
        sign_name: str = None,
        signature_id: str = None,
        status: int = None,
        template_code: str = None,
        template_id: str = None,
        updated_time: str = None,
    ):
        # 创建时间 (UTC+8)。
        self.created_time = created_time
        # 终止时间（UTC+8）。
        self.end_time = end_time
        # 执行时间 (UTC+8)，为空立即执行。
        self.execute_time = execute_time
        # 人群Id。
        self.group_id = group_id
        # 触达计划Id。
        self.id = id
        # 触达计划名称。
        self.name = name
        # 重复周期，按重复周期与重复周期单位执行。
        self.repeat_cycle = repeat_cycle
        # 重复周期单位，若指定执行时间，则重复周期生效。
        # - 0: 从不（默认）。
        # - 1: 小时。
        # - 2: 天。
        # - 3: 周。
        # - 4: 月。
        self.repeat_cycle_unit = repeat_cycle_unit
        # 重复次数。
        # - -1: 不设终止时间（默认）。
        # - 0: 不重复。
        # - N: 重复N次后终止。
        self.repeat_times = repeat_times
        # 签名。
        self.sign_name = sign_name
        # 签名Id，或指定签名。
        self.signature_id = signature_id
        # 状态。
        # - 0: 检查中。
        # - 1: 检查成功。
        # - 2: 检查失败。
        # - 3: 发送中。
        # - 4: 发送成功。
        # - 5: 发送失败。
        self.status = status
        # 模板Code。
        self.template_code = template_code
        # 模板Id，或指定模板Code。
        self.template_id = template_id
        # 更新时间 (UTC+8)。
        self.updated_time = updated_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.execute_time is not None:
            result['ExecuteTime'] = self.execute_time
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.repeat_cycle is not None:
            result['RepeatCycle'] = self.repeat_cycle
        if self.repeat_cycle_unit is not None:
            result['RepeatCycleUnit'] = self.repeat_cycle_unit
        if self.repeat_times is not None:
            result['RepeatTimes'] = self.repeat_times
        if self.sign_name is not None:
            result['SignName'] = self.sign_name
        if self.signature_id is not None:
            result['SignatureId'] = self.signature_id
        if self.status is not None:
            result['Status'] = self.status
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('ExecuteTime') is not None:
            self.execute_time = m.get('ExecuteTime')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RepeatCycle') is not None:
            self.repeat_cycle = m.get('RepeatCycle')
        if m.get('RepeatCycleUnit') is not None:
            self.repeat_cycle_unit = m.get('RepeatCycleUnit')
        if m.get('RepeatTimes') is not None:
            self.repeat_times = m.get('RepeatTimes')
        if m.get('SignName') is not None:
            self.sign_name = m.get('SignName')
        if m.get('SignatureId') is not None:
            self.signature_id = m.get('SignatureId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')
        return self


class ListSchedulesResponseBodyData(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        schedules: List[ListSchedulesResponseBodyDataSchedules] = None,
        total_count: int = None,
    ):
        # 分页数，从1开始，默认为1。
        self.page_number = page_number
        # 分页大小，默认为10。
        self.page_size = page_size
        # 触达计划列表。
        self.schedules = schedules
        # 触达计划数量。
        self.total_count = total_count

    def validate(self):
        if self.schedules:
            for k in self.schedules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['Schedules'] = []
        if self.schedules is not None:
            for k in self.schedules:
                result['Schedules'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.schedules = []
        if m.get('Schedules') is not None:
            for k in m.get('Schedules'):
                temp_model = ListSchedulesResponseBodyDataSchedules()
                self.schedules.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListSchedulesResponseBody(TeaModel):
    def __init__(
        self,
        data: ListSchedulesResponseBodyData = None,
        error_code: int = None,
        error_message: str = None,
        request_id: str = None,
    ):
        # 返回数据。
        self.data = data
        # 错误码。
        self.error_code = error_code
        # 错误信息。
        self.error_message = error_message
        # 请求ID。
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = ListSchedulesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListSchedulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListSchedulesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = ListSchedulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSignaturesRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        page_number: int = None,
        page_size: int = None,
        status: int = None,
    ):
        # 签名名称过滤。
        self.name = name
        # 分页数，从1开始，默认为1。
        self.page_number = page_number
        # 分页大小，默认为10。
        self.page_size = page_size
        # 签名审核状态过滤。
        # - 0：审核中。
        # - 1：审核通过。
        # - 2：审核不通过。
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListSignaturesResponseBodyDataSignatures(TeaModel):
    def __init__(
        self,
        created_time: str = None,
        id: str = None,
        name: str = None,
        status: int = None,
        updated_time: str = None,
    ):
        # 创建时间 (UTC+8)。
        self.created_time = created_time
        # 签名Id。
        self.id = id
        # 签名名称。
        self.name = name
        # 签名审核状态。
        # - 0：审核中。
        # - 1：审核通过。
        # - 2：审核不通过。
        self.status = status
        # 更新时间 (UTC+8)。
        self.updated_time = updated_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.status is not None:
            result['Status'] = self.status
        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')
        return self


class ListSignaturesResponseBodyData(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        signatures: List[ListSignaturesResponseBodyDataSignatures] = None,
        total_count: int = None,
    ):
        # 分页数，从1开始，默认为1。
        self.page_number = page_number
        # 分页大小，默认为10。
        self.page_size = page_size
        # 分页返回的签名列表。
        self.signatures = signatures
        # 账号下全部签名注册记录数量。
        self.total_count = total_count

    def validate(self):
        if self.signatures:
            for k in self.signatures:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['Signatures'] = []
        if self.signatures is not None:
            for k in self.signatures:
                result['Signatures'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.signatures = []
        if m.get('Signatures') is not None:
            for k in m.get('Signatures'):
                temp_model = ListSignaturesResponseBodyDataSignatures()
                self.signatures.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListSignaturesResponseBody(TeaModel):
    def __init__(
        self,
        data: ListSignaturesResponseBodyData = None,
        error_code: int = None,
        error_message: str = None,
        request_id: str = None,
    ):
        # 返回数据。
        self.data = data
        # 错误码。
        self.error_code = error_code
        # 错误信息。
        self.error_message = error_message
        # 请求ID。
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = ListSignaturesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListSignaturesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListSignaturesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = ListSignaturesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTemplatesRequest(TeaModel):
    def __init__(
        self,
        content: str = None,
        name: str = None,
        page_number: int = None,
        page_size: int = None,
        status: int = None,
        type: int = None,
    ):
        # 模板内容过滤。
        self.content = content
        # 模板名称过滤。
        self.name = name
        # 分页数，从1开始，默认为1。
        self.page_number = page_number
        # 分页大小，默认为10。
        self.page_size = page_size
        # 审核状态过滤。
        # - 0 : 审核中。
        # - 1 : 审核通过。
        # - 2 : 审核不通过。
        self.status = status
        # 模板类型过滤。
        # - 0 : 验证码。
        # - 1 : 短信通知。
        # - 2 : 推广短信。
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.name is not None:
            result['Name'] = self.name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListTemplatesResponseBodyDataTemplates(TeaModel):
    def __init__(
        self,
        content: str = None,
        created_time: str = None,
        description: str = None,
        id: str = None,
        name: str = None,
        reason: str = None,
        signature_id: str = None,
        status: int = None,
        template_code: str = None,
        type: int = None,
        updated_time: str = None,
    ):
        # 模板内容。
        self.content = content
        # 创建时间 (UTC+8)。
        self.created_time = created_time
        # 申请说明。
        self.description = description
        # 模板Id。
        self.id = id
        # 签名名称。
        self.name = name
        # 审核意见。
        self.reason = reason
        # 签名Id。
        self.signature_id = signature_id
        # 审核状态。
        # - 0 : 审核中。
        # - 1 : 审核通过。
        # - 2 : 审核不通过。
        self.status = status
        # 模板Code。
        self.template_code = template_code
        # 模板类型。
        # - 0 : 验证码。
        # - 1 : 短信通知。
        # - 2 : 推广短信。
        self.type = type
        # 更新时间 (UTC+8)。
        self.updated_time = updated_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.signature_id is not None:
            result['SignatureId'] = self.signature_id
        if self.status is not None:
            result['Status'] = self.status
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        if self.type is not None:
            result['Type'] = self.type
        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('SignatureId') is not None:
            self.signature_id = m.get('SignatureId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')
        return self


class ListTemplatesResponseBodyData(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        templates: List[ListTemplatesResponseBodyDataTemplates] = None,
        total_count: int = None,
    ):
        # 分页数，从1开始，默认为1。
        self.page_number = page_number
        # 分页大小，默认为10。
        self.page_size = page_size
        # 分页返回的模板列表。
        self.templates = templates
        # 全部模板注册记录数量。
        self.total_count = total_count

    def validate(self):
        if self.templates:
            for k in self.templates:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['Templates'] = []
        if self.templates is not None:
            for k in self.templates:
                result['Templates'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.templates = []
        if m.get('Templates') is not None:
            for k in m.get('Templates'):
                temp_model = ListTemplatesResponseBodyDataTemplates()
                self.templates.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListTemplatesResponseBody(TeaModel):
    def __init__(
        self,
        data: ListTemplatesResponseBodyData = None,
        error_code: int = None,
        error_message: str = None,
        request_id: str = None,
    ):
        # 返回数据。
        self.data = data
        # 错误码。
        self.error_code = error_code
        # 错误信息。
        self.error_message = error_message
        # 请求ID。
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = ListTemplatesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListTemplatesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListTemplatesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = ListTemplatesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTrainingJobsRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        page_number: int = None,
        page_size: int = None,
        remark: str = None,
        status: int = None,
    ):
        # 训练任务名称过滤。
        self.name = name
        # 分页数，从1开始，默认为1。
        self.page_number = page_number
        # 分页大小，默认为10。
        self.page_size = page_size
        # 训练任务备注过滤。
        self.remark = remark
        # 训练任务状态过滤
        # - 0: 队列中。
        # - 1: 已提交。
        # - 2: 运行中。
        # - 3: 成功。
        # - 4: 失败。
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListTrainingJobsResponseBodyDataTrainingJobs(TeaModel):
    def __init__(
        self,
        algorithm: str = None,
        created_time: str = None,
        history: str = None,
        id: str = None,
        name: str = None,
        remark: str = None,
        status: int = None,
        updated_time: str = None,
        user_config: str = None,
    ):
        # 关联算法Id。
        self.algorithm = algorithm
        # 创建时间 (UTC+8)。
        self.created_time = created_time
        # 训练任务日志。
        self.history = history
        # 训练任务Id。
        self.id = id
        # 训练任务名称。
        self.name = name
        # 备注。
        self.remark = remark
        # 训练任务状态。
        self.status = status
        # 更新时间 (UTC+8)。
        self.updated_time = updated_time
        # 用户配置。
        self.user_config = user_config

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.history is not None:
            result['History'] = self.history
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.status is not None:
            result['Status'] = self.status
        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time
        if self.user_config is not None:
            result['UserConfig'] = self.user_config
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('History') is not None:
            self.history = m.get('History')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')
        if m.get('UserConfig') is not None:
            self.user_config = m.get('UserConfig')
        return self


class ListTrainingJobsResponseBodyData(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
        training_jobs: List[ListTrainingJobsResponseBodyDataTrainingJobs] = None,
    ):
        # 分页数，从1开始，默认为1。
        self.page_number = page_number
        # 分页大小，默认为10。
        self.page_size = page_size
        # 总训练任务数量。
        self.total_count = total_count
        # 训练任务列表。
        self.training_jobs = training_jobs

    def validate(self):
        if self.training_jobs:
            for k in self.training_jobs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['TrainingJobs'] = []
        if self.training_jobs is not None:
            for k in self.training_jobs:
                result['TrainingJobs'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.training_jobs = []
        if m.get('TrainingJobs') is not None:
            for k in m.get('TrainingJobs'):
                temp_model = ListTrainingJobsResponseBodyDataTrainingJobs()
                self.training_jobs.append(temp_model.from_map(k))
        return self


class ListTrainingJobsResponseBody(TeaModel):
    def __init__(
        self,
        data: ListTrainingJobsResponseBodyData = None,
        error_code: int = None,
        error_message: str = None,
        request_id: str = None,
    ):
        # 返回数据。
        self.data = data
        # 错误码。
        self.error_code = error_code
        # 错误信息。
        self.error_message = error_message
        # 请求ID。
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = ListTrainingJobsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListTrainingJobsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListTrainingJobsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = ListTrainingJobsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SendMessageRequest(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        out_ids: List[str] = None,
        phone_numbers: List[str] = None,
        schedule_id: str = None,
        sign_name: str = None,
        signature_id: str = None,
        sms_up_extend_codes: List[str] = None,
        template_code: str = None,
        template_id: str = None,
        template_params: List[str] = None,
    ):
        # 人群Id，用于关联人群。
        self.group_id = group_id
        # 外部拓展字段，示例：["1234567890"]。
        self.out_ids = out_ids
        # 手机号，每个手机号对应一个模板变量、上行拓展码和外部拓展字段，示例：["1234567890"]。
        self.phone_numbers = phone_numbers
        # 触达计划Id，用于关联触达计划。
        self.schedule_id = schedule_id
        # 签名名称。
        self.sign_name = sign_name
        # 签名Id，同时只能指定签名名称或签名Id其中之一。
        self.signature_id = signature_id
        # 短信上行拓展码，示例：["1234567890"]。
        self.sms_up_extend_codes = sms_up_extend_codes
        # 模板Code。
        self.template_code = template_code
        # 模板Id，同时只能指定模板Code或模板Id其中之一。
        self.template_id = template_id
        # 短信模板变量对应的实际值，JSON格式。支持传入多个参数，示例：[{"name":"张三","number":"15038****76"}]。
        self.template_params = template_params

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.out_ids is not None:
            result['OutIds'] = self.out_ids
        if self.phone_numbers is not None:
            result['PhoneNumbers'] = self.phone_numbers
        if self.schedule_id is not None:
            result['ScheduleId'] = self.schedule_id
        if self.sign_name is not None:
            result['SignName'] = self.sign_name
        if self.signature_id is not None:
            result['SignatureId'] = self.signature_id
        if self.sms_up_extend_codes is not None:
            result['SmsUpExtendCodes'] = self.sms_up_extend_codes
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_params is not None:
            result['TemplateParams'] = self.template_params
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('OutIds') is not None:
            self.out_ids = m.get('OutIds')
        if m.get('PhoneNumbers') is not None:
            self.phone_numbers = m.get('PhoneNumbers')
        if m.get('ScheduleId') is not None:
            self.schedule_id = m.get('ScheduleId')
        if m.get('SignName') is not None:
            self.sign_name = m.get('SignName')
        if m.get('SignatureId') is not None:
            self.signature_id = m.get('SignatureId')
        if m.get('SmsUpExtendCodes') is not None:
            self.sms_up_extend_codes = m.get('SmsUpExtendCodes')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateParams') is not None:
            self.template_params = m.get('TemplateParams')
        return self


class SendMessageResponseBodyDataMessages(TeaModel):
    def __init__(
        self,
        id: str = None,
        phone_number: str = None,
    ):
        # 短信Id，可使用ListMessages查询短信状态。
        self.id = id
        # 手机号码。
        self.phone_number = phone_number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        return self


class SendMessageResponseBodyData(TeaModel):
    def __init__(
        self,
        messages: List[SendMessageResponseBodyDataMessages] = None,
        request_id: str = None,
    ):
        # 短信结果列表，列表中手机号的顺序与输入请求手机号顺序一一对应。
        self.messages = messages
        # 短信批处理Id，可使用ListMessages查询短信状态。
        self.request_id = request_id

    def validate(self):
        if self.messages:
            for k in self.messages:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Messages'] = []
        if self.messages is not None:
            for k in self.messages:
                result['Messages'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.messages = []
        if m.get('Messages') is not None:
            for k in m.get('Messages'):
                temp_model = SendMessageResponseBodyDataMessages()
                self.messages.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SendMessageResponseBody(TeaModel):
    def __init__(
        self,
        data: SendMessageResponseBodyData = None,
        error_code: int = None,
        error_message: str = None,
        request_id: str = None,
    ):
        # 返回数据。
        self.data = data
        # 错误码。
        self.error_code = error_code
        # 错误信息。
        self.error_message = error_message
        # 请求ID。
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = SendMessageResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SendMessageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SendMessageResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = SendMessageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SmsReportRequestBody(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        err_code: str = None,
        err_msg: str = None,
        message_id: str = None,
        out_id: str = None,
        phone_number: str = None,
        report_time: str = None,
        request_id: str = None,
        send_time: str = None,
        sign_name: str = None,
        sms_size: str = None,
        success: bool = None,
        template_code: str = None,
    ):
        # 发送回执ID，即发送流水号。
        self.biz_id = biz_id
        # 状态报告编码。
        self.err_code = err_code
        # 状态报告说明。
        self.err_msg = err_msg
        # 短信Id。调用发送接口SendMessage发送短信时，返回值中的Id字段。可使用短信Id在接口ListMessages查询具体的发送状态。
        self.message_id = message_id
        # 外部拓展字段。
        self.out_id = out_id
        # 手机号码。
        self.phone_number = phone_number
        # 状态报告时间。
        self.report_time = report_time
        # 短信批处理Id。调用发送接口SendMessage发送短信时，返回值中的RequestId字段。可使用短信批处理Id在接口ListMessages查询具体的发送状态。
        self.request_id = request_id
        # 发送时间。
        self.send_time = send_time
        # 签名。
        self.sign_name = sign_name
        # 短信长度。短信长度不超过70个字，按照一条短信计费；超过70个字，即为长短信，按照67字/条拆分成多条计费。
        self.sms_size = sms_size
        # 是否接收成功。
        # - true : 接收成功。
        # - false : 接收失败。
        self.success = success
        # 模板号。
        self.template_code = template_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['biz_id'] = self.biz_id
        if self.err_code is not None:
            result['err_code'] = self.err_code
        if self.err_msg is not None:
            result['err_msg'] = self.err_msg
        if self.message_id is not None:
            result['message_id'] = self.message_id
        if self.out_id is not None:
            result['out_id'] = self.out_id
        if self.phone_number is not None:
            result['phone_number'] = self.phone_number
        if self.report_time is not None:
            result['report_time'] = self.report_time
        if self.request_id is not None:
            result['request_id'] = self.request_id
        if self.send_time is not None:
            result['send_time'] = self.send_time
        if self.sign_name is not None:
            result['sign_name'] = self.sign_name
        if self.sms_size is not None:
            result['sms_size'] = self.sms_size
        if self.success is not None:
            result['success'] = self.success
        if self.template_code is not None:
            result['template_code'] = self.template_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('biz_id') is not None:
            self.biz_id = m.get('biz_id')
        if m.get('err_code') is not None:
            self.err_code = m.get('err_code')
        if m.get('err_msg') is not None:
            self.err_msg = m.get('err_msg')
        if m.get('message_id') is not None:
            self.message_id = m.get('message_id')
        if m.get('out_id') is not None:
            self.out_id = m.get('out_id')
        if m.get('phone_number') is not None:
            self.phone_number = m.get('phone_number')
        if m.get('report_time') is not None:
            self.report_time = m.get('report_time')
        if m.get('request_id') is not None:
            self.request_id = m.get('request_id')
        if m.get('send_time') is not None:
            self.send_time = m.get('send_time')
        if m.get('sign_name') is not None:
            self.sign_name = m.get('sign_name')
        if m.get('sms_size') is not None:
            self.sms_size = m.get('sms_size')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('template_code') is not None:
            self.template_code = m.get('template_code')
        return self


class SmsReportRequest(TeaModel):
    def __init__(
        self,
        body: List[SmsReportRequestBody] = None,
    ):
        # 请求参数的主体信息。
        self.body = body

    def validate(self):
        if self.body:
            for k in self.body:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['body'] = []
        if self.body is not None:
            for k in self.body:
                result['body'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.body = []
        if m.get('body') is not None:
            for k in m.get('body'):
                temp_model = SmsReportRequestBody()
                self.body.append(temp_model.from_map(k))
        return self


class SmsReportResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        msg: str = None,
    ):
        # 应答编码。
        self.code = code
        # 描述信息。
        self.msg = msg

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class SmsReportResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SmsReportResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = SmsReportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SmsUpRequestBody(TeaModel):
    def __init__(
        self,
        content: str = None,
        dest_code: str = None,
        phone_number: str = None,
        send_time: str = None,
        sequence_id: int = None,
        sign_name: str = None,
    ):
        # 发送内容。
        self.content = content
        # 上行短信扩展号码，系统后台自动生成，不支持自定义传入。
        self.dest_code = dest_code
        # 手机号码。
        self.phone_number = phone_number
        # 发送时间。
        self.send_time = send_time
        # 序列号。
        self.sequence_id = sequence_id
        # 签名信息。
        self.sign_name = sign_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['content'] = self.content
        if self.dest_code is not None:
            result['dest_code'] = self.dest_code
        if self.phone_number is not None:
            result['phone_number'] = self.phone_number
        if self.send_time is not None:
            result['send_time'] = self.send_time
        if self.sequence_id is not None:
            result['sequence_id'] = self.sequence_id
        if self.sign_name is not None:
            result['sign_name'] = self.sign_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('dest_code') is not None:
            self.dest_code = m.get('dest_code')
        if m.get('phone_number') is not None:
            self.phone_number = m.get('phone_number')
        if m.get('send_time') is not None:
            self.send_time = m.get('send_time')
        if m.get('sequence_id') is not None:
            self.sequence_id = m.get('sequence_id')
        if m.get('sign_name') is not None:
            self.sign_name = m.get('sign_name')
        return self


class SmsUpRequest(TeaModel):
    def __init__(
        self,
        body: List[SmsUpRequestBody] = None,
    ):
        # 请求参数的主体信息。
        self.body = body

    def validate(self):
        if self.body:
            for k in self.body:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['body'] = []
        if self.body is not None:
            for k in self.body:
                result['body'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.body = []
        if m.get('body') is not None:
            for k in m.get('body'):
                temp_model = SmsUpRequestBody()
                self.body.append(temp_model.from_map(k))
        return self


class SmsUpResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        msg: str = None,
    ):
        # 应答编码。
        self.code = code
        # 描述信息。
        self.msg = msg

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class SmsUpResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SmsUpResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = SmsUpResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateReportUrlRequest(TeaModel):
    def __init__(
        self,
        url: str = None,
    ):
        # 可公开访问的地址。
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class UpdateReportUrlResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        error_code: int = None,
        error_message: str = None,
        request_id: str = None,
    ):
        # 返回数据。
        self.data = data
        # 错误码。
        self.error_code = error_code
        # 错误信息。
        self.error_message = error_message
        # 请求ID。
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateReportUrlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateReportUrlResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = UpdateReportUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateUploadUrlRequest(TeaModel):
    def __init__(
        self,
        url: str = None,
    ):
        # 可公开访问的地址。
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class UpdateUploadUrlResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        error_code: int = None,
        error_message: str = None,
        request_id: str = None,
    ):
        # 返回数据。
        self.data = data
        # 错误码。
        self.error_code = error_code
        # 错误信息。
        self.error_message = error_message
        # 请求ID。
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateUploadUrlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateUploadUrlResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = UpdateUploadUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


