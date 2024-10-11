# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, Any, List


class CancelSparkStatementRequest(TeaModel):
    def __init__(
        self,
        job_id: str = None,
        statement_id: str = None,
    ):
        # This parameter is required.
        self.job_id = job_id
        # This parameter is required.
        self.statement_id = statement_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.statement_id is not None:
            result['StatementId'] = self.statement_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('StatementId') is not None:
            self.statement_id = m.get('StatementId')
        return self


class CancelSparkStatementResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
    ):
        self.data = data
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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CancelSparkStatementResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CancelSparkStatementResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CancelSparkStatementResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateInstanceRequest(TeaModel):
    def __init__(
        self,
        charge_type: str = None,
        component: str = None,
        instance_type: str = None,
        region_id: str = None,
    ):
        # This parameter is required.
        self.charge_type = charge_type
        # This parameter is required.
        self.component = component
        # This parameter is required.
        self.instance_type = instance_type
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.component is not None:
            result['Component'] = self.component
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('Component') is not None:
            self.component = m.get('Component')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CreateInstanceResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_info: str = None,
        request_id: str = None,
        result: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_info = error_info
        self.request_id = request_id
        self.result = result
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_info is not None:
            result['ErrorInfo'] = self.error_info
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorInfo') is not None:
            self.error_info = m.get('ErrorInfo')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateInstanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExecuteSparkStatementRequest(TeaModel):
    def __init__(
        self,
        code: str = None,
        job_id: str = None,
        kind: str = None,
    ):
        # This parameter is required.
        self.code = code
        # This parameter is required.
        self.job_id = job_id
        self.kind = kind

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.kind is not None:
            result['Kind'] = self.kind
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Kind') is not None:
            self.kind = m.get('Kind')
        return self


class ExecuteSparkStatementResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
    ):
        self.data = data
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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ExecuteSparkStatementResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ExecuteSparkStatementResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ExecuteSparkStatementResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetJobAttemptLogRequest(TeaModel):
    def __init__(
        self,
        job_attempt_id: str = None,
        job_id: str = None,
        vc_name: str = None,
    ):
        # This parameter is required.
        self.job_attempt_id = job_attempt_id
        # This parameter is required.
        self.job_id = job_id
        # This parameter is required.
        self.vc_name = vc_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_attempt_id is not None:
            result['JobAttemptId'] = self.job_attempt_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.vc_name is not None:
            result['VcName'] = self.vc_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobAttemptId') is not None:
            self.job_attempt_id = m.get('JobAttemptId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('VcName') is not None:
            self.vc_name = m.get('VcName')
        return self


class GetJobAttemptLogResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
    ):
        self.data = data
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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetJobAttemptLogResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetJobAttemptLogResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetJobAttemptLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetJobDetailRequest(TeaModel):
    def __init__(
        self,
        job_id: str = None,
        vc_name: str = None,
    ):
        # This parameter is required.
        self.job_id = job_id
        # This parameter is required.
        self.vc_name = vc_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.vc_name is not None:
            result['VcName'] = self.vc_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('VcName') is not None:
            self.vc_name = m.get('VcName')
        return self


class GetJobDetailResponseBodyJobDetail(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        create_time_value: str = None,
        detail: str = None,
        driver_resource_spec: str = None,
        executor_instances: str = None,
        executor_resource_spec: str = None,
        job_id: str = None,
        job_name: str = None,
        last_job_attempt_id: str = None,
        spark_ui: str = None,
        status: str = None,
        submit_time: str = None,
        submit_time_value: str = None,
        update_time: str = None,
        update_time_value: str = None,
        vc_name: str = None,
    ):
        self.create_time = create_time
        self.create_time_value = create_time_value
        self.detail = detail
        self.driver_resource_spec = driver_resource_spec
        self.executor_instances = executor_instances
        self.executor_resource_spec = executor_resource_spec
        self.job_id = job_id
        self.job_name = job_name
        self.last_job_attempt_id = last_job_attempt_id
        self.spark_ui = spark_ui
        self.status = status
        self.submit_time = submit_time
        self.submit_time_value = submit_time_value
        self.update_time = update_time
        self.update_time_value = update_time_value
        self.vc_name = vc_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_time_value is not None:
            result['CreateTimeValue'] = self.create_time_value
        if self.detail is not None:
            result['Detail'] = self.detail
        if self.driver_resource_spec is not None:
            result['DriverResourceSpec'] = self.driver_resource_spec
        if self.executor_instances is not None:
            result['ExecutorInstances'] = self.executor_instances
        if self.executor_resource_spec is not None:
            result['ExecutorResourceSpec'] = self.executor_resource_spec
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.job_name is not None:
            result['JobName'] = self.job_name
        if self.last_job_attempt_id is not None:
            result['LastJobAttemptId'] = self.last_job_attempt_id
        if self.spark_ui is not None:
            result['SparkUI'] = self.spark_ui
        if self.status is not None:
            result['Status'] = self.status
        if self.submit_time is not None:
            result['SubmitTime'] = self.submit_time
        if self.submit_time_value is not None:
            result['SubmitTimeValue'] = self.submit_time_value
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.update_time_value is not None:
            result['UpdateTimeValue'] = self.update_time_value
        if self.vc_name is not None:
            result['VcName'] = self.vc_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateTimeValue') is not None:
            self.create_time_value = m.get('CreateTimeValue')
        if m.get('Detail') is not None:
            self.detail = m.get('Detail')
        if m.get('DriverResourceSpec') is not None:
            self.driver_resource_spec = m.get('DriverResourceSpec')
        if m.get('ExecutorInstances') is not None:
            self.executor_instances = m.get('ExecutorInstances')
        if m.get('ExecutorResourceSpec') is not None:
            self.executor_resource_spec = m.get('ExecutorResourceSpec')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('JobName') is not None:
            self.job_name = m.get('JobName')
        if m.get('LastJobAttemptId') is not None:
            self.last_job_attempt_id = m.get('LastJobAttemptId')
        if m.get('SparkUI') is not None:
            self.spark_ui = m.get('SparkUI')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubmitTime') is not None:
            self.submit_time = m.get('SubmitTime')
        if m.get('SubmitTimeValue') is not None:
            self.submit_time_value = m.get('SubmitTimeValue')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('UpdateTimeValue') is not None:
            self.update_time_value = m.get('UpdateTimeValue')
        if m.get('VcName') is not None:
            self.vc_name = m.get('VcName')
        return self


class GetJobDetailResponseBody(TeaModel):
    def __init__(
        self,
        job_detail: GetJobDetailResponseBodyJobDetail = None,
        request_id: str = None,
    ):
        self.job_detail = job_detail
        self.request_id = request_id

    def validate(self):
        if self.job_detail:
            self.job_detail.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_detail is not None:
            result['JobDetail'] = self.job_detail.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobDetail') is not None:
            temp_model = GetJobDetailResponseBodyJobDetail()
            self.job_detail = temp_model.from_map(m['JobDetail'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetJobDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetJobDetailResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetJobDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetJobLogRequest(TeaModel):
    def __init__(
        self,
        job_id: str = None,
        vc_name: str = None,
    ):
        # This parameter is required.
        self.job_id = job_id
        # This parameter is required.
        self.vc_name = vc_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.vc_name is not None:
            result['VcName'] = self.vc_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('VcName') is not None:
            self.vc_name = m.get('VcName')
        return self


class GetJobLogResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
    ):
        self.data = data
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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetJobLogResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetJobLogResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetJobLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetJobStatusRequest(TeaModel):
    def __init__(
        self,
        job_id: str = None,
        vc_name: str = None,
    ):
        # This parameter is required.
        self.job_id = job_id
        # This parameter is required.
        self.vc_name = vc_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.vc_name is not None:
            result['VcName'] = self.vc_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('VcName') is not None:
            self.vc_name = m.get('VcName')
        return self


class GetJobStatusResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        status: str = None,
    ):
        self.request_id = request_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetJobStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetJobStatusResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetJobStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSparkSessionStateRequest(TeaModel):
    def __init__(
        self,
        job_id: str = None,
    ):
        # This parameter is required.
        self.job_id = job_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class GetSparkSessionStateResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        state: str = None,
    ):
        self.request_id = request_id
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.state is not None:
            result['State'] = self.state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('State') is not None:
            self.state = m.get('State')
        return self


class GetSparkSessionStateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetSparkSessionStateResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetSparkSessionStateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSparkStatementRequest(TeaModel):
    def __init__(
        self,
        job_id: str = None,
        statement_id: int = None,
    ):
        # This parameter is required.
        self.job_id = job_id
        # This parameter is required.
        self.statement_id = statement_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.statement_id is not None:
            result['StatementId'] = self.statement_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('StatementId') is not None:
            self.statement_id = m.get('StatementId')
        return self


class GetSparkStatementResponseBodyData(TeaModel):
    def __init__(
        self,
        code: str = None,
        completed_time: int = None,
        id: int = None,
        output: str = None,
        process: float = None,
        started_time: int = None,
        state: str = None,
    ):
        self.code = code
        self.completed_time = completed_time
        self.id = id
        self.output = output
        self.process = process
        self.started_time = started_time
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.completed_time is not None:
            result['CompletedTime'] = self.completed_time
        if self.id is not None:
            result['Id'] = self.id
        if self.output is not None:
            result['Output'] = self.output
        if self.process is not None:
            result['Process'] = self.process
        if self.started_time is not None:
            result['StartedTime'] = self.started_time
        if self.state is not None:
            result['State'] = self.state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('CompletedTime') is not None:
            self.completed_time = m.get('CompletedTime')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Output') is not None:
            self.output = m.get('Output')
        if m.get('Process') is not None:
            self.process = m.get('Process')
        if m.get('StartedTime') is not None:
            self.started_time = m.get('StartedTime')
        if m.get('State') is not None:
            self.state = m.get('State')
        return self


class GetSparkStatementResponseBody(TeaModel):
    def __init__(
        self,
        data: GetSparkStatementResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GetSparkStatementResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetSparkStatementResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetSparkStatementResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetSparkStatementResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class KillSparkJobRequest(TeaModel):
    def __init__(
        self,
        job_id: str = None,
        vc_name: str = None,
    ):
        # This parameter is required.
        self.job_id = job_id
        # This parameter is required.
        self.vc_name = vc_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.vc_name is not None:
            result['VcName'] = self.vc_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('VcName') is not None:
            self.vc_name = m.get('VcName')
        return self


class KillSparkJobResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
    ):
        self.data = data
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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class KillSparkJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: KillSparkJobResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = KillSparkJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSparkJobRequest(TeaModel):
    def __init__(
        self,
        condition: Dict[str, Any] = None,
        page_number: int = None,
        page_size: int = None,
        vc_name: str = None,
    ):
        self.condition = condition
        # This parameter is required.
        self.page_number = page_number
        # This parameter is required.
        self.page_size = page_size
        # This parameter is required.
        self.vc_name = vc_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.condition is not None:
            result['Condition'] = self.condition
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.vc_name is not None:
            result['VcName'] = self.vc_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Condition') is not None:
            self.condition = m.get('Condition')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('VcName') is not None:
            self.vc_name = m.get('VcName')
        return self


class ListSparkJobShrinkRequest(TeaModel):
    def __init__(
        self,
        condition_shrink: str = None,
        page_number: int = None,
        page_size: int = None,
        vc_name: str = None,
    ):
        self.condition_shrink = condition_shrink
        # This parameter is required.
        self.page_number = page_number
        # This parameter is required.
        self.page_size = page_size
        # This parameter is required.
        self.vc_name = vc_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.condition_shrink is not None:
            result['Condition'] = self.condition_shrink
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.vc_name is not None:
            result['VcName'] = self.vc_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Condition') is not None:
            self.condition_shrink = m.get('Condition')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('VcName') is not None:
            self.vc_name = m.get('VcName')
        return self


class ListSparkJobResponseBodyDataResultJobList(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        create_time_value: str = None,
        detail: str = None,
        driver_resource_spec: str = None,
        executor_instances: str = None,
        executor_resource_spec: str = None,
        job_id: str = None,
        job_name: str = None,
        spark_ui: str = None,
        status: str = None,
        submit_time: str = None,
        submit_time_value: str = None,
        update_time: str = None,
        update_time_value: str = None,
        vc_name: str = None,
    ):
        self.create_time = create_time
        self.create_time_value = create_time_value
        self.detail = detail
        self.driver_resource_spec = driver_resource_spec
        self.executor_instances = executor_instances
        self.executor_resource_spec = executor_resource_spec
        self.job_id = job_id
        self.job_name = job_name
        self.spark_ui = spark_ui
        self.status = status
        self.submit_time = submit_time
        self.submit_time_value = submit_time_value
        self.update_time = update_time
        self.update_time_value = update_time_value
        self.vc_name = vc_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_time_value is not None:
            result['CreateTimeValue'] = self.create_time_value
        if self.detail is not None:
            result['Detail'] = self.detail
        if self.driver_resource_spec is not None:
            result['DriverResourceSpec'] = self.driver_resource_spec
        if self.executor_instances is not None:
            result['ExecutorInstances'] = self.executor_instances
        if self.executor_resource_spec is not None:
            result['ExecutorResourceSpec'] = self.executor_resource_spec
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.job_name is not None:
            result['JobName'] = self.job_name
        if self.spark_ui is not None:
            result['SparkUI'] = self.spark_ui
        if self.status is not None:
            result['Status'] = self.status
        if self.submit_time is not None:
            result['SubmitTime'] = self.submit_time
        if self.submit_time_value is not None:
            result['SubmitTimeValue'] = self.submit_time_value
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.update_time_value is not None:
            result['UpdateTimeValue'] = self.update_time_value
        if self.vc_name is not None:
            result['VcName'] = self.vc_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateTimeValue') is not None:
            self.create_time_value = m.get('CreateTimeValue')
        if m.get('Detail') is not None:
            self.detail = m.get('Detail')
        if m.get('DriverResourceSpec') is not None:
            self.driver_resource_spec = m.get('DriverResourceSpec')
        if m.get('ExecutorInstances') is not None:
            self.executor_instances = m.get('ExecutorInstances')
        if m.get('ExecutorResourceSpec') is not None:
            self.executor_resource_spec = m.get('ExecutorResourceSpec')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('JobName') is not None:
            self.job_name = m.get('JobName')
        if m.get('SparkUI') is not None:
            self.spark_ui = m.get('SparkUI')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubmitTime') is not None:
            self.submit_time = m.get('SubmitTime')
        if m.get('SubmitTimeValue') is not None:
            self.submit_time_value = m.get('SubmitTimeValue')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('UpdateTimeValue') is not None:
            self.update_time_value = m.get('UpdateTimeValue')
        if m.get('VcName') is not None:
            self.vc_name = m.get('VcName')
        return self


class ListSparkJobResponseBodyDataResult(TeaModel):
    def __init__(
        self,
        job_list: List[ListSparkJobResponseBodyDataResultJobList] = None,
        page_number: str = None,
        page_size: str = None,
        total_count: str = None,
    ):
        self.job_list = job_list
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        if self.job_list:
            for k in self.job_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['JobList'] = []
        if self.job_list is not None:
            for k in self.job_list:
                result['JobList'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.job_list = []
        if m.get('JobList') is not None:
            for k in m.get('JobList'):
                temp_model = ListSparkJobResponseBodyDataResultJobList()
                self.job_list.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListSparkJobResponseBody(TeaModel):
    def __init__(
        self,
        data_result: ListSparkJobResponseBodyDataResult = None,
        request_id: str = None,
    ):
        self.data_result = data_result
        self.request_id = request_id

    def validate(self):
        if self.data_result:
            self.data_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_result is not None:
            result['DataResult'] = self.data_result.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataResult') is not None:
            temp_model = ListSparkJobResponseBodyDataResult()
            self.data_result = temp_model.from_map(m['DataResult'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListSparkJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListSparkJobResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListSparkJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSparkJobAttemptRequest(TeaModel):
    def __init__(
        self,
        condition: Dict[str, Any] = None,
        job_id: str = None,
        page_number: int = None,
        page_size: int = None,
        vc_name: str = None,
    ):
        self.condition = condition
        # This parameter is required.
        self.job_id = job_id
        # This parameter is required.
        self.page_number = page_number
        # This parameter is required.
        self.page_size = page_size
        # This parameter is required.
        self.vc_name = vc_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.condition is not None:
            result['Condition'] = self.condition
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.vc_name is not None:
            result['VcName'] = self.vc_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Condition') is not None:
            self.condition = m.get('Condition')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('VcName') is not None:
            self.vc_name = m.get('VcName')
        return self


class ListSparkJobAttemptShrinkRequest(TeaModel):
    def __init__(
        self,
        condition_shrink: str = None,
        job_id: str = None,
        page_number: int = None,
        page_size: int = None,
        vc_name: str = None,
    ):
        self.condition_shrink = condition_shrink
        # This parameter is required.
        self.job_id = job_id
        # This parameter is required.
        self.page_number = page_number
        # This parameter is required.
        self.page_size = page_size
        # This parameter is required.
        self.vc_name = vc_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.condition_shrink is not None:
            result['Condition'] = self.condition_shrink
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.vc_name is not None:
            result['VcName'] = self.vc_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Condition') is not None:
            self.condition_shrink = m.get('Condition')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('VcName') is not None:
            self.vc_name = m.get('VcName')
        return self


class ListSparkJobAttemptResponseBodyDataResultJobAttemptList(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        create_time_value: str = None,
        detail: str = None,
        duration_time: str = None,
        duration_time_value: str = None,
        job_attempt_id: str = None,
        job_id: str = None,
        job_name: str = None,
        spark_ui: str = None,
        status: str = None,
        terminated_time: str = None,
        terminated_time_value: str = None,
        vc_name: str = None,
    ):
        self.create_time = create_time
        self.create_time_value = create_time_value
        self.detail = detail
        self.duration_time = duration_time
        self.duration_time_value = duration_time_value
        self.job_attempt_id = job_attempt_id
        self.job_id = job_id
        self.job_name = job_name
        self.spark_ui = spark_ui
        self.status = status
        self.terminated_time = terminated_time
        self.terminated_time_value = terminated_time_value
        self.vc_name = vc_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_time_value is not None:
            result['CreateTimeValue'] = self.create_time_value
        if self.detail is not None:
            result['Detail'] = self.detail
        if self.duration_time is not None:
            result['DurationTime'] = self.duration_time
        if self.duration_time_value is not None:
            result['DurationTimeValue'] = self.duration_time_value
        if self.job_attempt_id is not None:
            result['JobAttemptId'] = self.job_attempt_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.job_name is not None:
            result['JobName'] = self.job_name
        if self.spark_ui is not None:
            result['SparkUI'] = self.spark_ui
        if self.status is not None:
            result['Status'] = self.status
        if self.terminated_time is not None:
            result['TerminatedTime'] = self.terminated_time
        if self.terminated_time_value is not None:
            result['TerminatedTimeValue'] = self.terminated_time_value
        if self.vc_name is not None:
            result['VcName'] = self.vc_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateTimeValue') is not None:
            self.create_time_value = m.get('CreateTimeValue')
        if m.get('Detail') is not None:
            self.detail = m.get('Detail')
        if m.get('DurationTime') is not None:
            self.duration_time = m.get('DurationTime')
        if m.get('DurationTimeValue') is not None:
            self.duration_time_value = m.get('DurationTimeValue')
        if m.get('JobAttemptId') is not None:
            self.job_attempt_id = m.get('JobAttemptId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('JobName') is not None:
            self.job_name = m.get('JobName')
        if m.get('SparkUI') is not None:
            self.spark_ui = m.get('SparkUI')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TerminatedTime') is not None:
            self.terminated_time = m.get('TerminatedTime')
        if m.get('TerminatedTimeValue') is not None:
            self.terminated_time_value = m.get('TerminatedTimeValue')
        if m.get('VcName') is not None:
            self.vc_name = m.get('VcName')
        return self


class ListSparkJobAttemptResponseBodyDataResult(TeaModel):
    def __init__(
        self,
        job_attempt_list: List[ListSparkJobAttemptResponseBodyDataResultJobAttemptList] = None,
        page_number: str = None,
        page_size: str = None,
        total_count: str = None,
    ):
        self.job_attempt_list = job_attempt_list
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        if self.job_attempt_list:
            for k in self.job_attempt_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['JobAttemptList'] = []
        if self.job_attempt_list is not None:
            for k in self.job_attempt_list:
                result['JobAttemptList'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.job_attempt_list = []
        if m.get('JobAttemptList') is not None:
            for k in m.get('JobAttemptList'):
                temp_model = ListSparkJobAttemptResponseBodyDataResultJobAttemptList()
                self.job_attempt_list.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListSparkJobAttemptResponseBody(TeaModel):
    def __init__(
        self,
        data_result: ListSparkJobAttemptResponseBodyDataResult = None,
        request_id: str = None,
    ):
        self.data_result = data_result
        self.request_id = request_id

    def validate(self):
        if self.data_result:
            self.data_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_result is not None:
            result['DataResult'] = self.data_result.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataResult') is not None:
            temp_model = ListSparkJobAttemptResponseBodyDataResult()
            self.data_result = temp_model.from_map(m['DataResult'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListSparkJobAttemptResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListSparkJobAttemptResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListSparkJobAttemptResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSparkStatementsRequest(TeaModel):
    def __init__(
        self,
        job_id: str = None,
    ):
        # This parameter is required.
        self.job_id = job_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class ListSparkStatementsResponseBodyStatements(TeaModel):
    def __init__(
        self,
        code: str = None,
        completed_time: int = None,
        id: int = None,
        output: str = None,
        progress: float = None,
        started_time: int = None,
        state: str = None,
    ):
        self.code = code
        self.completed_time = completed_time
        self.id = id
        self.output = output
        self.progress = progress
        self.started_time = started_time
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.completed_time is not None:
            result['CompletedTime'] = self.completed_time
        if self.id is not None:
            result['Id'] = self.id
        if self.output is not None:
            result['Output'] = self.output
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.started_time is not None:
            result['StartedTime'] = self.started_time
        if self.state is not None:
            result['State'] = self.state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('CompletedTime') is not None:
            self.completed_time = m.get('CompletedTime')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Output') is not None:
            self.output = m.get('Output')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('StartedTime') is not None:
            self.started_time = m.get('StartedTime')
        if m.get('State') is not None:
            self.state = m.get('State')
        return self


class ListSparkStatementsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        statements: List[ListSparkStatementsResponseBodyStatements] = None,
    ):
        self.request_id = request_id
        self.statements = statements

    def validate(self):
        if self.statements:
            for k in self.statements:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Statements'] = []
        if self.statements is not None:
            for k in self.statements:
                result['Statements'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.statements = []
        if m.get('Statements') is not None:
            for k in m.get('Statements'):
                temp_model = ListSparkStatementsResponseBodyStatements()
                self.statements.append(temp_model.from_map(k))
        return self


class ListSparkStatementsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListSparkStatementsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListSparkStatementsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReleaseInstanceRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        region_id: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ReleaseInstanceResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_info: str = None,
        request_id: str = None,
        result: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_info = error_info
        self.request_id = request_id
        self.result = result
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_info is not None:
            result['ErrorInfo'] = self.error_info
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorInfo') is not None:
            self.error_info = m.get('ErrorInfo')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ReleaseInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ReleaseInstanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ReleaseInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitSparkJobRequest(TeaModel):
    def __init__(
        self,
        config_json: str = None,
        vc_name: str = None,
    ):
        # This parameter is required.
        self.config_json = config_json
        # This parameter is required.
        self.vc_name = vc_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_json is not None:
            result['ConfigJson'] = self.config_json
        if self.vc_name is not None:
            result['VcName'] = self.vc_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigJson') is not None:
            self.config_json = m.get('ConfigJson')
        if m.get('VcName') is not None:
            self.vc_name = m.get('VcName')
        return self


class SubmitSparkJobResponseBody(TeaModel):
    def __init__(
        self,
        job_id: str = None,
        request_id: str = None,
    ):
        self.job_id = job_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SubmitSparkJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SubmitSparkJobResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SubmitSparkJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitSparkSQLRequest(TeaModel):
    def __init__(
        self,
        sql: str = None,
        vc_name: str = None,
    ):
        # This parameter is required.
        self.sql = sql
        # This parameter is required.
        self.vc_name = vc_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sql is not None:
            result['Sql'] = self.sql
        if self.vc_name is not None:
            result['VcName'] = self.vc_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Sql') is not None:
            self.sql = m.get('Sql')
        if m.get('VcName') is not None:
            self.vc_name = m.get('VcName')
        return self


class SubmitSparkSQLResponseBody(TeaModel):
    def __init__(
        self,
        job_id: str = None,
        request_id: str = None,
    ):
        self.job_id = job_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SubmitSparkSQLResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SubmitSparkSQLResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SubmitSparkSQLResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ValidateVirtualClusterNameRequest(TeaModel):
    def __init__(
        self,
        vc_name: str = None,
    ):
        self.vc_name = vc_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.vc_name is not None:
            result['VcName'] = self.vc_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VcName') is not None:
            self.vc_name = m.get('VcName')
        return self


class ValidateVirtualClusterNameResponseBodyData(TeaModel):
    def __init__(
        self,
        legal: str = None,
        message: str = None,
    ):
        self.legal = legal
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.legal is not None:
            result['Legal'] = self.legal
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Legal') is not None:
            self.legal = m.get('Legal')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class ValidateVirtualClusterNameResponseBody(TeaModel):
    def __init__(
        self,
        data: ValidateVirtualClusterNameResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = ValidateVirtualClusterNameResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ValidateVirtualClusterNameResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ValidateVirtualClusterNameResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ValidateVirtualClusterNameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


