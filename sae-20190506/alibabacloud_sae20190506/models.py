# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List, Any


class AbortAndRollbackChangeOrderRequest(TeaModel):
    def __init__(
        self,
        change_order_id: str = None,
    ):
        self.change_order_id = change_order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.change_order_id is not None:
            result['ChangeOrderId'] = self.change_order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChangeOrderId') is not None:
            self.change_order_id = m.get('ChangeOrderId')
        return self


class AbortAndRollbackChangeOrderResponseBodyData(TeaModel):
    def __init__(
        self,
        change_order_id: str = None,
    ):
        self.change_order_id = change_order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.change_order_id is not None:
            result['ChangeOrderId'] = self.change_order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChangeOrderId') is not None:
            self.change_order_id = m.get('ChangeOrderId')
        return self


class AbortAndRollbackChangeOrderResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: AbortAndRollbackChangeOrderResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = AbortAndRollbackChangeOrderResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class AbortAndRollbackChangeOrderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AbortAndRollbackChangeOrderResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = AbortAndRollbackChangeOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AbortChangeOrderRequest(TeaModel):
    def __init__(
        self,
        change_order_id: str = None,
    ):
        self.change_order_id = change_order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.change_order_id is not None:
            result['ChangeOrderId'] = self.change_order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChangeOrderId') is not None:
            self.change_order_id = m.get('ChangeOrderId')
        return self


class AbortChangeOrderResponseBodyData(TeaModel):
    def __init__(
        self,
        change_order_id: str = None,
    ):
        self.change_order_id = change_order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.change_order_id is not None:
            result['ChangeOrderId'] = self.change_order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChangeOrderId') is not None:
            self.change_order_id = m.get('ChangeOrderId')
        return self


class AbortChangeOrderResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: AbortChangeOrderResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = AbortChangeOrderResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class AbortChangeOrderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AbortChangeOrderResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = AbortChangeOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchStartApplicationsRequest(TeaModel):
    def __init__(
        self,
        app_ids: str = None,
        namespace_id: str = None,
    ):
        self.app_ids = app_ids
        self.namespace_id = namespace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_ids is not None:
            result['AppIds'] = self.app_ids
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppIds') is not None:
            self.app_ids = m.get('AppIds')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        return self


class BatchStartApplicationsResponseBodyData(TeaModel):
    def __init__(
        self,
        change_order_id: str = None,
    ):
        self.change_order_id = change_order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.change_order_id is not None:
            result['ChangeOrderId'] = self.change_order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChangeOrderId') is not None:
            self.change_order_id = m.get('ChangeOrderId')
        return self


class BatchStartApplicationsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: BatchStartApplicationsResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = BatchStartApplicationsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class BatchStartApplicationsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BatchStartApplicationsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = BatchStartApplicationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchStopApplicationsRequest(TeaModel):
    def __init__(
        self,
        app_ids: str = None,
        namespace_id: str = None,
    ):
        self.app_ids = app_ids
        self.namespace_id = namespace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_ids is not None:
            result['AppIds'] = self.app_ids
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppIds') is not None:
            self.app_ids = m.get('AppIds')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        return self


class BatchStopApplicationsResponseBodyData(TeaModel):
    def __init__(
        self,
        change_order_id: str = None,
    ):
        self.change_order_id = change_order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.change_order_id is not None:
            result['ChangeOrderId'] = self.change_order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChangeOrderId') is not None:
            self.change_order_id = m.get('ChangeOrderId')
        return self


class BatchStopApplicationsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: BatchStopApplicationsResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = BatchStopApplicationsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class BatchStopApplicationsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BatchStopApplicationsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = BatchStopApplicationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BindSlbRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        internet: str = None,
        internet_slb_id: str = None,
        intranet: str = None,
        intranet_slb_id: str = None,
    ):
        self.app_id = app_id
        self.internet = internet
        self.internet_slb_id = internet_slb_id
        self.intranet = intranet
        self.intranet_slb_id = intranet_slb_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.internet is not None:
            result['Internet'] = self.internet
        if self.internet_slb_id is not None:
            result['InternetSlbId'] = self.internet_slb_id
        if self.intranet is not None:
            result['Intranet'] = self.intranet
        if self.intranet_slb_id is not None:
            result['IntranetSlbId'] = self.intranet_slb_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Internet') is not None:
            self.internet = m.get('Internet')
        if m.get('InternetSlbId') is not None:
            self.internet_slb_id = m.get('InternetSlbId')
        if m.get('Intranet') is not None:
            self.intranet = m.get('Intranet')
        if m.get('IntranetSlbId') is not None:
            self.intranet_slb_id = m.get('IntranetSlbId')
        return self


class BindSlbResponseBodyData(TeaModel):
    def __init__(
        self,
        change_order_id: str = None,
    ):
        self.change_order_id = change_order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.change_order_id is not None:
            result['ChangeOrderId'] = self.change_order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChangeOrderId') is not None:
            self.change_order_id = m.get('ChangeOrderId')
        return self


class BindSlbResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: BindSlbResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = BindSlbResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class BindSlbResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BindSlbResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = BindSlbResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConfirmPipelineBatchRequest(TeaModel):
    def __init__(
        self,
        confirm: bool = None,
        pipeline_id: str = None,
    ):
        self.confirm = confirm
        self.pipeline_id = pipeline_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.confirm is not None:
            result['Confirm'] = self.confirm
        if self.pipeline_id is not None:
            result['PipelineId'] = self.pipeline_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Confirm') is not None:
            self.confirm = m.get('Confirm')
        if m.get('PipelineId') is not None:
            self.pipeline_id = m.get('PipelineId')
        return self


class ConfirmPipelineBatchResponseBodyData(TeaModel):
    def __init__(
        self,
        pipeline_id: str = None,
    ):
        self.pipeline_id = pipeline_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pipeline_id is not None:
            result['PipelineId'] = self.pipeline_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PipelineId') is not None:
            self.pipeline_id = m.get('PipelineId')
        return self


class ConfirmPipelineBatchResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ConfirmPipelineBatchResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = ConfirmPipelineBatchResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class ConfirmPipelineBatchResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ConfirmPipelineBatchResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = ConfirmPipelineBatchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateApplicationRequest(TeaModel):
    def __init__(
        self,
        acr_assume_role_arn: str = None,
        acr_instance_id: str = None,
        app_description: str = None,
        app_name: str = None,
        associate_eip: bool = None,
        auto_config: bool = None,
        command: str = None,
        command_args: str = None,
        config_map_mount_desc: str = None,
        cpu: int = None,
        custom_host_alias: str = None,
        deploy: bool = None,
        edas_container_version: str = None,
        envs: str = None,
        image_pull_secrets: str = None,
        image_url: str = None,
        jar_start_args: str = None,
        jar_start_options: str = None,
        jdk: str = None,
        kafka_configs: str = None,
        liveness: str = None,
        memory: int = None,
        micro_registration: str = None,
        mount_desc: str = None,
        mount_host: str = None,
        namespace_id: str = None,
        nas_configs: str = None,
        nas_id: str = None,
        oss_ak_id: str = None,
        oss_ak_secret: str = None,
        oss_mount_descs: str = None,
        package_type: str = None,
        package_url: str = None,
        package_version: str = None,
        php_arms_config_location: str = None,
        php_config: str = None,
        php_config_location: str = None,
        post_start: str = None,
        pre_stop: str = None,
        programming_language: str = None,
        pvtz_discovery_svc: str = None,
        python: str = None,
        python_modules: str = None,
        readiness: str = None,
        replicas: int = None,
        security_group_id: str = None,
        sls_configs: str = None,
        termination_grace_period_seconds: int = None,
        timezone: str = None,
        tomcat_config: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
        war_start_options: str = None,
        web_container: str = None,
    ):
        self.acr_assume_role_arn = acr_assume_role_arn
        self.acr_instance_id = acr_instance_id
        self.app_description = app_description
        self.app_name = app_name
        self.associate_eip = associate_eip
        self.auto_config = auto_config
        self.command = command
        self.command_args = command_args
        self.config_map_mount_desc = config_map_mount_desc
        self.cpu = cpu
        self.custom_host_alias = custom_host_alias
        self.deploy = deploy
        self.edas_container_version = edas_container_version
        self.envs = envs
        self.image_pull_secrets = image_pull_secrets
        self.image_url = image_url
        self.jar_start_args = jar_start_args
        self.jar_start_options = jar_start_options
        self.jdk = jdk
        self.kafka_configs = kafka_configs
        self.liveness = liveness
        self.memory = memory
        self.micro_registration = micro_registration
        self.mount_desc = mount_desc
        self.mount_host = mount_host
        self.namespace_id = namespace_id
        self.nas_configs = nas_configs
        self.nas_id = nas_id
        self.oss_ak_id = oss_ak_id
        self.oss_ak_secret = oss_ak_secret
        self.oss_mount_descs = oss_mount_descs
        self.package_type = package_type
        self.package_url = package_url
        self.package_version = package_version
        self.php_arms_config_location = php_arms_config_location
        self.php_config = php_config
        self.php_config_location = php_config_location
        self.post_start = post_start
        self.pre_stop = pre_stop
        self.programming_language = programming_language
        self.pvtz_discovery_svc = pvtz_discovery_svc
        self.python = python
        self.python_modules = python_modules
        self.readiness = readiness
        self.replicas = replicas
        self.security_group_id = security_group_id
        self.sls_configs = sls_configs
        self.termination_grace_period_seconds = termination_grace_period_seconds
        self.timezone = timezone
        self.tomcat_config = tomcat_config
        self.v_switch_id = v_switch_id
        self.vpc_id = vpc_id
        self.war_start_options = war_start_options
        self.web_container = web_container

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acr_assume_role_arn is not None:
            result['AcrAssumeRoleArn'] = self.acr_assume_role_arn
        if self.acr_instance_id is not None:
            result['AcrInstanceId'] = self.acr_instance_id
        if self.app_description is not None:
            result['AppDescription'] = self.app_description
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.associate_eip is not None:
            result['AssociateEip'] = self.associate_eip
        if self.auto_config is not None:
            result['AutoConfig'] = self.auto_config
        if self.command is not None:
            result['Command'] = self.command
        if self.command_args is not None:
            result['CommandArgs'] = self.command_args
        if self.config_map_mount_desc is not None:
            result['ConfigMapMountDesc'] = self.config_map_mount_desc
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.custom_host_alias is not None:
            result['CustomHostAlias'] = self.custom_host_alias
        if self.deploy is not None:
            result['Deploy'] = self.deploy
        if self.edas_container_version is not None:
            result['EdasContainerVersion'] = self.edas_container_version
        if self.envs is not None:
            result['Envs'] = self.envs
        if self.image_pull_secrets is not None:
            result['ImagePullSecrets'] = self.image_pull_secrets
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        if self.jar_start_args is not None:
            result['JarStartArgs'] = self.jar_start_args
        if self.jar_start_options is not None:
            result['JarStartOptions'] = self.jar_start_options
        if self.jdk is not None:
            result['Jdk'] = self.jdk
        if self.kafka_configs is not None:
            result['KafkaConfigs'] = self.kafka_configs
        if self.liveness is not None:
            result['Liveness'] = self.liveness
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.micro_registration is not None:
            result['MicroRegistration'] = self.micro_registration
        if self.mount_desc is not None:
            result['MountDesc'] = self.mount_desc
        if self.mount_host is not None:
            result['MountHost'] = self.mount_host
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.nas_configs is not None:
            result['NasConfigs'] = self.nas_configs
        if self.nas_id is not None:
            result['NasId'] = self.nas_id
        if self.oss_ak_id is not None:
            result['OssAkId'] = self.oss_ak_id
        if self.oss_ak_secret is not None:
            result['OssAkSecret'] = self.oss_ak_secret
        if self.oss_mount_descs is not None:
            result['OssMountDescs'] = self.oss_mount_descs
        if self.package_type is not None:
            result['PackageType'] = self.package_type
        if self.package_url is not None:
            result['PackageUrl'] = self.package_url
        if self.package_version is not None:
            result['PackageVersion'] = self.package_version
        if self.php_arms_config_location is not None:
            result['PhpArmsConfigLocation'] = self.php_arms_config_location
        if self.php_config is not None:
            result['PhpConfig'] = self.php_config
        if self.php_config_location is not None:
            result['PhpConfigLocation'] = self.php_config_location
        if self.post_start is not None:
            result['PostStart'] = self.post_start
        if self.pre_stop is not None:
            result['PreStop'] = self.pre_stop
        if self.programming_language is not None:
            result['ProgrammingLanguage'] = self.programming_language
        if self.pvtz_discovery_svc is not None:
            result['PvtzDiscoverySvc'] = self.pvtz_discovery_svc
        if self.python is not None:
            result['Python'] = self.python
        if self.python_modules is not None:
            result['PythonModules'] = self.python_modules
        if self.readiness is not None:
            result['Readiness'] = self.readiness
        if self.replicas is not None:
            result['Replicas'] = self.replicas
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.sls_configs is not None:
            result['SlsConfigs'] = self.sls_configs
        if self.termination_grace_period_seconds is not None:
            result['TerminationGracePeriodSeconds'] = self.termination_grace_period_seconds
        if self.timezone is not None:
            result['Timezone'] = self.timezone
        if self.tomcat_config is not None:
            result['TomcatConfig'] = self.tomcat_config
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.war_start_options is not None:
            result['WarStartOptions'] = self.war_start_options
        if self.web_container is not None:
            result['WebContainer'] = self.web_container
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcrAssumeRoleArn') is not None:
            self.acr_assume_role_arn = m.get('AcrAssumeRoleArn')
        if m.get('AcrInstanceId') is not None:
            self.acr_instance_id = m.get('AcrInstanceId')
        if m.get('AppDescription') is not None:
            self.app_description = m.get('AppDescription')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AssociateEip') is not None:
            self.associate_eip = m.get('AssociateEip')
        if m.get('AutoConfig') is not None:
            self.auto_config = m.get('AutoConfig')
        if m.get('Command') is not None:
            self.command = m.get('Command')
        if m.get('CommandArgs') is not None:
            self.command_args = m.get('CommandArgs')
        if m.get('ConfigMapMountDesc') is not None:
            self.config_map_mount_desc = m.get('ConfigMapMountDesc')
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('CustomHostAlias') is not None:
            self.custom_host_alias = m.get('CustomHostAlias')
        if m.get('Deploy') is not None:
            self.deploy = m.get('Deploy')
        if m.get('EdasContainerVersion') is not None:
            self.edas_container_version = m.get('EdasContainerVersion')
        if m.get('Envs') is not None:
            self.envs = m.get('Envs')
        if m.get('ImagePullSecrets') is not None:
            self.image_pull_secrets = m.get('ImagePullSecrets')
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        if m.get('JarStartArgs') is not None:
            self.jar_start_args = m.get('JarStartArgs')
        if m.get('JarStartOptions') is not None:
            self.jar_start_options = m.get('JarStartOptions')
        if m.get('Jdk') is not None:
            self.jdk = m.get('Jdk')
        if m.get('KafkaConfigs') is not None:
            self.kafka_configs = m.get('KafkaConfigs')
        if m.get('Liveness') is not None:
            self.liveness = m.get('Liveness')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('MicroRegistration') is not None:
            self.micro_registration = m.get('MicroRegistration')
        if m.get('MountDesc') is not None:
            self.mount_desc = m.get('MountDesc')
        if m.get('MountHost') is not None:
            self.mount_host = m.get('MountHost')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('NasConfigs') is not None:
            self.nas_configs = m.get('NasConfigs')
        if m.get('NasId') is not None:
            self.nas_id = m.get('NasId')
        if m.get('OssAkId') is not None:
            self.oss_ak_id = m.get('OssAkId')
        if m.get('OssAkSecret') is not None:
            self.oss_ak_secret = m.get('OssAkSecret')
        if m.get('OssMountDescs') is not None:
            self.oss_mount_descs = m.get('OssMountDescs')
        if m.get('PackageType') is not None:
            self.package_type = m.get('PackageType')
        if m.get('PackageUrl') is not None:
            self.package_url = m.get('PackageUrl')
        if m.get('PackageVersion') is not None:
            self.package_version = m.get('PackageVersion')
        if m.get('PhpArmsConfigLocation') is not None:
            self.php_arms_config_location = m.get('PhpArmsConfigLocation')
        if m.get('PhpConfig') is not None:
            self.php_config = m.get('PhpConfig')
        if m.get('PhpConfigLocation') is not None:
            self.php_config_location = m.get('PhpConfigLocation')
        if m.get('PostStart') is not None:
            self.post_start = m.get('PostStart')
        if m.get('PreStop') is not None:
            self.pre_stop = m.get('PreStop')
        if m.get('ProgrammingLanguage') is not None:
            self.programming_language = m.get('ProgrammingLanguage')
        if m.get('PvtzDiscoverySvc') is not None:
            self.pvtz_discovery_svc = m.get('PvtzDiscoverySvc')
        if m.get('Python') is not None:
            self.python = m.get('Python')
        if m.get('PythonModules') is not None:
            self.python_modules = m.get('PythonModules')
        if m.get('Readiness') is not None:
            self.readiness = m.get('Readiness')
        if m.get('Replicas') is not None:
            self.replicas = m.get('Replicas')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('SlsConfigs') is not None:
            self.sls_configs = m.get('SlsConfigs')
        if m.get('TerminationGracePeriodSeconds') is not None:
            self.termination_grace_period_seconds = m.get('TerminationGracePeriodSeconds')
        if m.get('Timezone') is not None:
            self.timezone = m.get('Timezone')
        if m.get('TomcatConfig') is not None:
            self.tomcat_config = m.get('TomcatConfig')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('WarStartOptions') is not None:
            self.war_start_options = m.get('WarStartOptions')
        if m.get('WebContainer') is not None:
            self.web_container = m.get('WebContainer')
        return self


class CreateApplicationResponseBodyData(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        change_order_id: str = None,
    ):
        self.app_id = app_id
        self.change_order_id = change_order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.change_order_id is not None:
            result['ChangeOrderId'] = self.change_order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ChangeOrderId') is not None:
            self.change_order_id = m.get('ChangeOrderId')
        return self


class CreateApplicationResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: CreateApplicationResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = CreateApplicationResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class CreateApplicationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateApplicationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = CreateApplicationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateApplicationScalingRuleRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        min_ready_instance_ratio: int = None,
        min_ready_instances: int = None,
        scaling_rule_enable: bool = None,
        scaling_rule_metric: str = None,
        scaling_rule_name: str = None,
        scaling_rule_timer: str = None,
        scaling_rule_type: str = None,
    ):
        self.app_id = app_id
        self.min_ready_instance_ratio = min_ready_instance_ratio
        self.min_ready_instances = min_ready_instances
        self.scaling_rule_enable = scaling_rule_enable
        self.scaling_rule_metric = scaling_rule_metric
        self.scaling_rule_name = scaling_rule_name
        self.scaling_rule_timer = scaling_rule_timer
        self.scaling_rule_type = scaling_rule_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.min_ready_instance_ratio is not None:
            result['MinReadyInstanceRatio'] = self.min_ready_instance_ratio
        if self.min_ready_instances is not None:
            result['MinReadyInstances'] = self.min_ready_instances
        if self.scaling_rule_enable is not None:
            result['ScalingRuleEnable'] = self.scaling_rule_enable
        if self.scaling_rule_metric is not None:
            result['ScalingRuleMetric'] = self.scaling_rule_metric
        if self.scaling_rule_name is not None:
            result['ScalingRuleName'] = self.scaling_rule_name
        if self.scaling_rule_timer is not None:
            result['ScalingRuleTimer'] = self.scaling_rule_timer
        if self.scaling_rule_type is not None:
            result['ScalingRuleType'] = self.scaling_rule_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('MinReadyInstanceRatio') is not None:
            self.min_ready_instance_ratio = m.get('MinReadyInstanceRatio')
        if m.get('MinReadyInstances') is not None:
            self.min_ready_instances = m.get('MinReadyInstances')
        if m.get('ScalingRuleEnable') is not None:
            self.scaling_rule_enable = m.get('ScalingRuleEnable')
        if m.get('ScalingRuleMetric') is not None:
            self.scaling_rule_metric = m.get('ScalingRuleMetric')
        if m.get('ScalingRuleName') is not None:
            self.scaling_rule_name = m.get('ScalingRuleName')
        if m.get('ScalingRuleTimer') is not None:
            self.scaling_rule_timer = m.get('ScalingRuleTimer')
        if m.get('ScalingRuleType') is not None:
            self.scaling_rule_type = m.get('ScalingRuleType')
        return self


class CreateApplicationScalingRuleResponseBodyDataMetricMetrics(TeaModel):
    def __init__(
        self,
        metric_target_average_utilization: int = None,
        metric_type: str = None,
    ):
        self.metric_target_average_utilization = metric_target_average_utilization
        self.metric_type = metric_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.metric_target_average_utilization is not None:
            result['MetricTargetAverageUtilization'] = self.metric_target_average_utilization
        if self.metric_type is not None:
            result['MetricType'] = self.metric_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MetricTargetAverageUtilization') is not None:
            self.metric_target_average_utilization = m.get('MetricTargetAverageUtilization')
        if m.get('MetricType') is not None:
            self.metric_type = m.get('MetricType')
        return self


class CreateApplicationScalingRuleResponseBodyDataMetric(TeaModel):
    def __init__(
        self,
        max_replicas: int = None,
        metrics: List[CreateApplicationScalingRuleResponseBodyDataMetricMetrics] = None,
        min_replicas: int = None,
    ):
        self.max_replicas = max_replicas
        self.metrics = metrics
        self.min_replicas = min_replicas

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
        if self.max_replicas is not None:
            result['MaxReplicas'] = self.max_replicas
        result['Metrics'] = []
        if self.metrics is not None:
            for k in self.metrics:
                result['Metrics'].append(k.to_map() if k else None)
        if self.min_replicas is not None:
            result['MinReplicas'] = self.min_replicas
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxReplicas') is not None:
            self.max_replicas = m.get('MaxReplicas')
        self.metrics = []
        if m.get('Metrics') is not None:
            for k in m.get('Metrics'):
                temp_model = CreateApplicationScalingRuleResponseBodyDataMetricMetrics()
                self.metrics.append(temp_model.from_map(k))
        if m.get('MinReplicas') is not None:
            self.min_replicas = m.get('MinReplicas')
        return self


class CreateApplicationScalingRuleResponseBodyDataTimerSchedules(TeaModel):
    def __init__(
        self,
        at_time: str = None,
        target_replicas: int = None,
    ):
        self.at_time = at_time
        self.target_replicas = target_replicas

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.at_time is not None:
            result['AtTime'] = self.at_time
        if self.target_replicas is not None:
            result['TargetReplicas'] = self.target_replicas
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AtTime') is not None:
            self.at_time = m.get('AtTime')
        if m.get('TargetReplicas') is not None:
            self.target_replicas = m.get('TargetReplicas')
        return self


class CreateApplicationScalingRuleResponseBodyDataTimer(TeaModel):
    def __init__(
        self,
        begin_date: str = None,
        end_date: str = None,
        period: str = None,
        schedules: List[CreateApplicationScalingRuleResponseBodyDataTimerSchedules] = None,
    ):
        self.begin_date = begin_date
        self.end_date = end_date
        self.period = period
        self.schedules = schedules

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
        if self.begin_date is not None:
            result['BeginDate'] = self.begin_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.period is not None:
            result['Period'] = self.period
        result['Schedules'] = []
        if self.schedules is not None:
            for k in self.schedules:
                result['Schedules'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginDate') is not None:
            self.begin_date = m.get('BeginDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        self.schedules = []
        if m.get('Schedules') is not None:
            for k in m.get('Schedules'):
                temp_model = CreateApplicationScalingRuleResponseBodyDataTimerSchedules()
                self.schedules.append(temp_model.from_map(k))
        return self


class CreateApplicationScalingRuleResponseBodyData(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        create_time: int = None,
        last_disable_time: int = None,
        metric: CreateApplicationScalingRuleResponseBodyDataMetric = None,
        scale_rule_enabled: bool = None,
        scale_rule_name: str = None,
        scale_rule_type: str = None,
        timer: CreateApplicationScalingRuleResponseBodyDataTimer = None,
        update_time: int = None,
    ):
        self.app_id = app_id
        self.create_time = create_time
        self.last_disable_time = last_disable_time
        self.metric = metric
        self.scale_rule_enabled = scale_rule_enabled
        self.scale_rule_name = scale_rule_name
        self.scale_rule_type = scale_rule_type
        self.timer = timer
        self.update_time = update_time

    def validate(self):
        if self.metric:
            self.metric.validate()
        if self.timer:
            self.timer.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.last_disable_time is not None:
            result['LastDisableTime'] = self.last_disable_time
        if self.metric is not None:
            result['Metric'] = self.metric.to_map()
        if self.scale_rule_enabled is not None:
            result['ScaleRuleEnabled'] = self.scale_rule_enabled
        if self.scale_rule_name is not None:
            result['ScaleRuleName'] = self.scale_rule_name
        if self.scale_rule_type is not None:
            result['ScaleRuleType'] = self.scale_rule_type
        if self.timer is not None:
            result['Timer'] = self.timer.to_map()
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('LastDisableTime') is not None:
            self.last_disable_time = m.get('LastDisableTime')
        if m.get('Metric') is not None:
            temp_model = CreateApplicationScalingRuleResponseBodyDataMetric()
            self.metric = temp_model.from_map(m['Metric'])
        if m.get('ScaleRuleEnabled') is not None:
            self.scale_rule_enabled = m.get('ScaleRuleEnabled')
        if m.get('ScaleRuleName') is not None:
            self.scale_rule_name = m.get('ScaleRuleName')
        if m.get('ScaleRuleType') is not None:
            self.scale_rule_type = m.get('ScaleRuleType')
        if m.get('Timer') is not None:
            temp_model = CreateApplicationScalingRuleResponseBodyDataTimer()
            self.timer = temp_model.from_map(m['Timer'])
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class CreateApplicationScalingRuleResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: CreateApplicationScalingRuleResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = CreateApplicationScalingRuleResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class CreateApplicationScalingRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateApplicationScalingRuleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = CreateApplicationScalingRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateConfigMapRequest(TeaModel):
    def __init__(
        self,
        data: str = None,
        description: str = None,
        name: str = None,
        namespace_id: str = None,
    ):
        self.data = data
        self.description = description
        self.name = name
        self.namespace_id = namespace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        return self


class CreateConfigMapResponseBodyData(TeaModel):
    def __init__(
        self,
        config_map_id: int = None,
    ):
        self.config_map_id = config_map_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_map_id is not None:
            result['ConfigMapId'] = self.config_map_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigMapId') is not None:
            self.config_map_id = m.get('ConfigMapId')
        return self


class CreateConfigMapResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: CreateConfigMapResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = CreateConfigMapResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class CreateConfigMapResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateConfigMapResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = CreateConfigMapResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateGreyTagRouteRequest(TeaModel):
    def __init__(
        self,
        alb_rules: str = None,
        app_id: str = None,
        description: str = None,
        dubbo_rules: str = None,
        name: str = None,
        sc_rules: str = None,
    ):
        self.alb_rules = alb_rules
        self.app_id = app_id
        self.description = description
        self.dubbo_rules = dubbo_rules
        self.name = name
        self.sc_rules = sc_rules

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alb_rules is not None:
            result['AlbRules'] = self.alb_rules
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.description is not None:
            result['Description'] = self.description
        if self.dubbo_rules is not None:
            result['DubboRules'] = self.dubbo_rules
        if self.name is not None:
            result['Name'] = self.name
        if self.sc_rules is not None:
            result['ScRules'] = self.sc_rules
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlbRules') is not None:
            self.alb_rules = m.get('AlbRules')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DubboRules') is not None:
            self.dubbo_rules = m.get('DubboRules')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ScRules') is not None:
            self.sc_rules = m.get('ScRules')
        return self


class CreateGreyTagRouteResponseBodyData(TeaModel):
    def __init__(
        self,
        grey_tag_route_id: int = None,
    ):
        self.grey_tag_route_id = grey_tag_route_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.grey_tag_route_id is not None:
            result['GreyTagRouteId'] = self.grey_tag_route_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GreyTagRouteId') is not None:
            self.grey_tag_route_id = m.get('GreyTagRouteId')
        return self


class CreateGreyTagRouteResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: CreateGreyTagRouteResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = CreateGreyTagRouteResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class CreateGreyTagRouteResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateGreyTagRouteResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = CreateGreyTagRouteResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateIngressRequest(TeaModel):
    def __init__(
        self,
        cert_id: str = None,
        cert_ids: str = None,
        default_rule: str = None,
        description: str = None,
        listener_port: int = None,
        listener_protocol: str = None,
        load_balance_type: str = None,
        namespace_id: str = None,
        rules: str = None,
        slb_id: str = None,
    ):
        self.cert_id = cert_id
        self.cert_ids = cert_ids
        self.default_rule = default_rule
        self.description = description
        self.listener_port = listener_port
        self.listener_protocol = listener_protocol
        self.load_balance_type = load_balance_type
        self.namespace_id = namespace_id
        self.rules = rules
        self.slb_id = slb_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_id is not None:
            result['CertId'] = self.cert_id
        if self.cert_ids is not None:
            result['CertIds'] = self.cert_ids
        if self.default_rule is not None:
            result['DefaultRule'] = self.default_rule
        if self.description is not None:
            result['Description'] = self.description
        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port
        if self.listener_protocol is not None:
            result['ListenerProtocol'] = self.listener_protocol
        if self.load_balance_type is not None:
            result['LoadBalanceType'] = self.load_balance_type
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.rules is not None:
            result['Rules'] = self.rules
        if self.slb_id is not None:
            result['SlbId'] = self.slb_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertId') is not None:
            self.cert_id = m.get('CertId')
        if m.get('CertIds') is not None:
            self.cert_ids = m.get('CertIds')
        if m.get('DefaultRule') is not None:
            self.default_rule = m.get('DefaultRule')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')
        if m.get('ListenerProtocol') is not None:
            self.listener_protocol = m.get('ListenerProtocol')
        if m.get('LoadBalanceType') is not None:
            self.load_balance_type = m.get('LoadBalanceType')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('Rules') is not None:
            self.rules = m.get('Rules')
        if m.get('SlbId') is not None:
            self.slb_id = m.get('SlbId')
        return self


class CreateIngressResponseBodyData(TeaModel):
    def __init__(
        self,
        ingress_id: int = None,
    ):
        self.ingress_id = ingress_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ingress_id is not None:
            result['IngressId'] = self.ingress_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IngressId') is not None:
            self.ingress_id = m.get('IngressId')
        return self


class CreateIngressResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: CreateIngressResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = CreateIngressResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class CreateIngressResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateIngressResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = CreateIngressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateJobRequest(TeaModel):
    def __init__(
        self,
        acr_assume_role_arn: str = None,
        acr_instance_id: str = None,
        app_description: str = None,
        app_name: str = None,
        auto_config: bool = None,
        backoff_limit: int = None,
        command: str = None,
        command_args: str = None,
        concurrency_policy: str = None,
        config_map_mount_desc: str = None,
        cpu: int = None,
        custom_host_alias: str = None,
        edas_container_version: str = None,
        enable_image_accl: bool = None,
        envs: str = None,
        image_pull_secrets: str = None,
        image_url: str = None,
        jar_start_args: str = None,
        jar_start_options: str = None,
        jdk: str = None,
        memory: int = None,
        mount_desc: str = None,
        mount_host: str = None,
        namespace_id: str = None,
        nas_id: str = None,
        oss_ak_id: str = None,
        oss_ak_secret: str = None,
        oss_mount_descs: str = None,
        package_type: str = None,
        package_url: str = None,
        package_version: str = None,
        php_config: str = None,
        php_config_location: str = None,
        post_start: str = None,
        pre_stop: str = None,
        programming_language: str = None,
        python: str = None,
        python_modules: str = None,
        ref_app_id: str = None,
        replicas: int = None,
        security_group_id: str = None,
        slice: bool = None,
        slice_envs: str = None,
        sls_configs: str = None,
        termination_grace_period_seconds: int = None,
        timeout: int = None,
        timezone: str = None,
        tomcat_config: str = None,
        trigger_config: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
        war_start_options: str = None,
        web_container: str = None,
        workload: str = None,
    ):
        self.acr_assume_role_arn = acr_assume_role_arn
        self.acr_instance_id = acr_instance_id
        self.app_description = app_description
        self.app_name = app_name
        self.auto_config = auto_config
        self.backoff_limit = backoff_limit
        self.command = command
        self.command_args = command_args
        self.concurrency_policy = concurrency_policy
        self.config_map_mount_desc = config_map_mount_desc
        self.cpu = cpu
        self.custom_host_alias = custom_host_alias
        self.edas_container_version = edas_container_version
        self.enable_image_accl = enable_image_accl
        self.envs = envs
        self.image_pull_secrets = image_pull_secrets
        self.image_url = image_url
        self.jar_start_args = jar_start_args
        self.jar_start_options = jar_start_options
        self.jdk = jdk
        self.memory = memory
        self.mount_desc = mount_desc
        self.mount_host = mount_host
        self.namespace_id = namespace_id
        self.nas_id = nas_id
        self.oss_ak_id = oss_ak_id
        self.oss_ak_secret = oss_ak_secret
        self.oss_mount_descs = oss_mount_descs
        self.package_type = package_type
        self.package_url = package_url
        self.package_version = package_version
        self.php_config = php_config
        self.php_config_location = php_config_location
        self.post_start = post_start
        self.pre_stop = pre_stop
        self.programming_language = programming_language
        self.python = python
        self.python_modules = python_modules
        self.ref_app_id = ref_app_id
        self.replicas = replicas
        self.security_group_id = security_group_id
        self.slice = slice
        self.slice_envs = slice_envs
        self.sls_configs = sls_configs
        self.termination_grace_period_seconds = termination_grace_period_seconds
        self.timeout = timeout
        self.timezone = timezone
        self.tomcat_config = tomcat_config
        self.trigger_config = trigger_config
        self.v_switch_id = v_switch_id
        self.vpc_id = vpc_id
        self.war_start_options = war_start_options
        self.web_container = web_container
        self.workload = workload

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acr_assume_role_arn is not None:
            result['AcrAssumeRoleArn'] = self.acr_assume_role_arn
        if self.acr_instance_id is not None:
            result['AcrInstanceId'] = self.acr_instance_id
        if self.app_description is not None:
            result['AppDescription'] = self.app_description
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.auto_config is not None:
            result['AutoConfig'] = self.auto_config
        if self.backoff_limit is not None:
            result['BackoffLimit'] = self.backoff_limit
        if self.command is not None:
            result['Command'] = self.command
        if self.command_args is not None:
            result['CommandArgs'] = self.command_args
        if self.concurrency_policy is not None:
            result['ConcurrencyPolicy'] = self.concurrency_policy
        if self.config_map_mount_desc is not None:
            result['ConfigMapMountDesc'] = self.config_map_mount_desc
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.custom_host_alias is not None:
            result['CustomHostAlias'] = self.custom_host_alias
        if self.edas_container_version is not None:
            result['EdasContainerVersion'] = self.edas_container_version
        if self.enable_image_accl is not None:
            result['EnableImageAccl'] = self.enable_image_accl
        if self.envs is not None:
            result['Envs'] = self.envs
        if self.image_pull_secrets is not None:
            result['ImagePullSecrets'] = self.image_pull_secrets
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        if self.jar_start_args is not None:
            result['JarStartArgs'] = self.jar_start_args
        if self.jar_start_options is not None:
            result['JarStartOptions'] = self.jar_start_options
        if self.jdk is not None:
            result['Jdk'] = self.jdk
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.mount_desc is not None:
            result['MountDesc'] = self.mount_desc
        if self.mount_host is not None:
            result['MountHost'] = self.mount_host
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.nas_id is not None:
            result['NasId'] = self.nas_id
        if self.oss_ak_id is not None:
            result['OssAkId'] = self.oss_ak_id
        if self.oss_ak_secret is not None:
            result['OssAkSecret'] = self.oss_ak_secret
        if self.oss_mount_descs is not None:
            result['OssMountDescs'] = self.oss_mount_descs
        if self.package_type is not None:
            result['PackageType'] = self.package_type
        if self.package_url is not None:
            result['PackageUrl'] = self.package_url
        if self.package_version is not None:
            result['PackageVersion'] = self.package_version
        if self.php_config is not None:
            result['PhpConfig'] = self.php_config
        if self.php_config_location is not None:
            result['PhpConfigLocation'] = self.php_config_location
        if self.post_start is not None:
            result['PostStart'] = self.post_start
        if self.pre_stop is not None:
            result['PreStop'] = self.pre_stop
        if self.programming_language is not None:
            result['ProgrammingLanguage'] = self.programming_language
        if self.python is not None:
            result['Python'] = self.python
        if self.python_modules is not None:
            result['PythonModules'] = self.python_modules
        if self.ref_app_id is not None:
            result['RefAppId'] = self.ref_app_id
        if self.replicas is not None:
            result['Replicas'] = self.replicas
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.slice is not None:
            result['Slice'] = self.slice
        if self.slice_envs is not None:
            result['SliceEnvs'] = self.slice_envs
        if self.sls_configs is not None:
            result['SlsConfigs'] = self.sls_configs
        if self.termination_grace_period_seconds is not None:
            result['TerminationGracePeriodSeconds'] = self.termination_grace_period_seconds
        if self.timeout is not None:
            result['Timeout'] = self.timeout
        if self.timezone is not None:
            result['Timezone'] = self.timezone
        if self.tomcat_config is not None:
            result['TomcatConfig'] = self.tomcat_config
        if self.trigger_config is not None:
            result['TriggerConfig'] = self.trigger_config
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.war_start_options is not None:
            result['WarStartOptions'] = self.war_start_options
        if self.web_container is not None:
            result['WebContainer'] = self.web_container
        if self.workload is not None:
            result['Workload'] = self.workload
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcrAssumeRoleArn') is not None:
            self.acr_assume_role_arn = m.get('AcrAssumeRoleArn')
        if m.get('AcrInstanceId') is not None:
            self.acr_instance_id = m.get('AcrInstanceId')
        if m.get('AppDescription') is not None:
            self.app_description = m.get('AppDescription')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AutoConfig') is not None:
            self.auto_config = m.get('AutoConfig')
        if m.get('BackoffLimit') is not None:
            self.backoff_limit = m.get('BackoffLimit')
        if m.get('Command') is not None:
            self.command = m.get('Command')
        if m.get('CommandArgs') is not None:
            self.command_args = m.get('CommandArgs')
        if m.get('ConcurrencyPolicy') is not None:
            self.concurrency_policy = m.get('ConcurrencyPolicy')
        if m.get('ConfigMapMountDesc') is not None:
            self.config_map_mount_desc = m.get('ConfigMapMountDesc')
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('CustomHostAlias') is not None:
            self.custom_host_alias = m.get('CustomHostAlias')
        if m.get('EdasContainerVersion') is not None:
            self.edas_container_version = m.get('EdasContainerVersion')
        if m.get('EnableImageAccl') is not None:
            self.enable_image_accl = m.get('EnableImageAccl')
        if m.get('Envs') is not None:
            self.envs = m.get('Envs')
        if m.get('ImagePullSecrets') is not None:
            self.image_pull_secrets = m.get('ImagePullSecrets')
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        if m.get('JarStartArgs') is not None:
            self.jar_start_args = m.get('JarStartArgs')
        if m.get('JarStartOptions') is not None:
            self.jar_start_options = m.get('JarStartOptions')
        if m.get('Jdk') is not None:
            self.jdk = m.get('Jdk')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('MountDesc') is not None:
            self.mount_desc = m.get('MountDesc')
        if m.get('MountHost') is not None:
            self.mount_host = m.get('MountHost')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('NasId') is not None:
            self.nas_id = m.get('NasId')
        if m.get('OssAkId') is not None:
            self.oss_ak_id = m.get('OssAkId')
        if m.get('OssAkSecret') is not None:
            self.oss_ak_secret = m.get('OssAkSecret')
        if m.get('OssMountDescs') is not None:
            self.oss_mount_descs = m.get('OssMountDescs')
        if m.get('PackageType') is not None:
            self.package_type = m.get('PackageType')
        if m.get('PackageUrl') is not None:
            self.package_url = m.get('PackageUrl')
        if m.get('PackageVersion') is not None:
            self.package_version = m.get('PackageVersion')
        if m.get('PhpConfig') is not None:
            self.php_config = m.get('PhpConfig')
        if m.get('PhpConfigLocation') is not None:
            self.php_config_location = m.get('PhpConfigLocation')
        if m.get('PostStart') is not None:
            self.post_start = m.get('PostStart')
        if m.get('PreStop') is not None:
            self.pre_stop = m.get('PreStop')
        if m.get('ProgrammingLanguage') is not None:
            self.programming_language = m.get('ProgrammingLanguage')
        if m.get('Python') is not None:
            self.python = m.get('Python')
        if m.get('PythonModules') is not None:
            self.python_modules = m.get('PythonModules')
        if m.get('RefAppId') is not None:
            self.ref_app_id = m.get('RefAppId')
        if m.get('Replicas') is not None:
            self.replicas = m.get('Replicas')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('Slice') is not None:
            self.slice = m.get('Slice')
        if m.get('SliceEnvs') is not None:
            self.slice_envs = m.get('SliceEnvs')
        if m.get('SlsConfigs') is not None:
            self.sls_configs = m.get('SlsConfigs')
        if m.get('TerminationGracePeriodSeconds') is not None:
            self.termination_grace_period_seconds = m.get('TerminationGracePeriodSeconds')
        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')
        if m.get('Timezone') is not None:
            self.timezone = m.get('Timezone')
        if m.get('TomcatConfig') is not None:
            self.tomcat_config = m.get('TomcatConfig')
        if m.get('TriggerConfig') is not None:
            self.trigger_config = m.get('TriggerConfig')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('WarStartOptions') is not None:
            self.war_start_options = m.get('WarStartOptions')
        if m.get('WebContainer') is not None:
            self.web_container = m.get('WebContainer')
        if m.get('Workload') is not None:
            self.workload = m.get('Workload')
        return self


class CreateJobResponseBodyData(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        change_order_id: str = None,
    ):
        self.app_id = app_id
        self.change_order_id = change_order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.change_order_id is not None:
            result['ChangeOrderId'] = self.change_order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ChangeOrderId') is not None:
            self.change_order_id = m.get('ChangeOrderId')
        return self


class CreateJobResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: CreateJobResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = CreateJobResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class CreateJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateJobResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = CreateJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateNamespaceRequest(TeaModel):
    def __init__(
        self,
        name_space_short_id: str = None,
        namespace_description: str = None,
        namespace_id: str = None,
        namespace_name: str = None,
    ):
        self.name_space_short_id = name_space_short_id
        self.namespace_description = namespace_description
        self.namespace_id = namespace_id
        self.namespace_name = namespace_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name_space_short_id is not None:
            result['NameSpaceShortId'] = self.name_space_short_id
        if self.namespace_description is not None:
            result['NamespaceDescription'] = self.namespace_description
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.namespace_name is not None:
            result['NamespaceName'] = self.namespace_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NameSpaceShortId') is not None:
            self.name_space_short_id = m.get('NameSpaceShortId')
        if m.get('NamespaceDescription') is not None:
            self.namespace_description = m.get('NamespaceDescription')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('NamespaceName') is not None:
            self.namespace_name = m.get('NamespaceName')
        return self


class CreateNamespaceResponseBodyData(TeaModel):
    def __init__(
        self,
        name_space_short_id: str = None,
        namespace_description: str = None,
        namespace_id: str = None,
        namespace_name: str = None,
        region_id: str = None,
    ):
        self.name_space_short_id = name_space_short_id
        self.namespace_description = namespace_description
        self.namespace_id = namespace_id
        self.namespace_name = namespace_name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name_space_short_id is not None:
            result['NameSpaceShortId'] = self.name_space_short_id
        if self.namespace_description is not None:
            result['NamespaceDescription'] = self.namespace_description
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.namespace_name is not None:
            result['NamespaceName'] = self.namespace_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NameSpaceShortId') is not None:
            self.name_space_short_id = m.get('NameSpaceShortId')
        if m.get('NamespaceDescription') is not None:
            self.namespace_description = m.get('NamespaceDescription')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('NamespaceName') is not None:
            self.namespace_name = m.get('NamespaceName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CreateNamespaceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: CreateNamespaceResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = CreateNamespaceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class CreateNamespaceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateNamespaceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = CreateNamespaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSecretRequest(TeaModel):
    def __init__(
        self,
        namespace_id: str = None,
        secret_data: str = None,
        secret_name: str = None,
        secret_type: str = None,
    ):
        self.namespace_id = namespace_id
        self.secret_data = secret_data
        self.secret_name = secret_name
        self.secret_type = secret_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.secret_data is not None:
            result['SecretData'] = self.secret_data
        if self.secret_name is not None:
            result['SecretName'] = self.secret_name
        if self.secret_type is not None:
            result['SecretType'] = self.secret_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('SecretData') is not None:
            self.secret_data = m.get('SecretData')
        if m.get('SecretName') is not None:
            self.secret_name = m.get('SecretName')
        if m.get('SecretType') is not None:
            self.secret_type = m.get('SecretType')
        return self


class CreateSecretResponseBodyData(TeaModel):
    def __init__(
        self,
        secret_id: int = None,
    ):
        self.secret_id = secret_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.secret_id is not None:
            result['SecretId'] = self.secret_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecretId') is not None:
            self.secret_id = m.get('SecretId')
        return self


class CreateSecretResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: CreateSecretResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = CreateSecretResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class CreateSecretResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateSecretResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = CreateSecretResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteApplicationRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
    ):
        self.app_id = app_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        return self


class DeleteApplicationResponseBodyData(TeaModel):
    def __init__(
        self,
        change_order_id: str = None,
    ):
        self.change_order_id = change_order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.change_order_id is not None:
            result['ChangeOrderId'] = self.change_order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChangeOrderId') is not None:
            self.change_order_id = m.get('ChangeOrderId')
        return self


class DeleteApplicationResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: DeleteApplicationResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = DeleteApplicationResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class DeleteApplicationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteApplicationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DeleteApplicationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteApplicationScalingRuleRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        scaling_rule_name: str = None,
    ):
        self.app_id = app_id
        self.scaling_rule_name = scaling_rule_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.scaling_rule_name is not None:
            result['ScalingRuleName'] = self.scaling_rule_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ScalingRuleName') is not None:
            self.scaling_rule_name = m.get('ScalingRuleName')
        return self


class DeleteApplicationScalingRuleResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class DeleteApplicationScalingRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteApplicationScalingRuleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DeleteApplicationScalingRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteConfigMapRequest(TeaModel):
    def __init__(
        self,
        config_map_id: int = None,
    ):
        self.config_map_id = config_map_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_map_id is not None:
            result['ConfigMapId'] = self.config_map_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigMapId') is not None:
            self.config_map_id = m.get('ConfigMapId')
        return self


class DeleteConfigMapResponseBodyData(TeaModel):
    def __init__(
        self,
        config_map_id: int = None,
    ):
        self.config_map_id = config_map_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_map_id is not None:
            result['ConfigMapId'] = self.config_map_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigMapId') is not None:
            self.config_map_id = m.get('ConfigMapId')
        return self


class DeleteConfigMapResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: DeleteConfigMapResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = DeleteConfigMapResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class DeleteConfigMapResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteConfigMapResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DeleteConfigMapResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteGreyTagRouteRequest(TeaModel):
    def __init__(
        self,
        grey_tag_route_id: int = None,
    ):
        self.grey_tag_route_id = grey_tag_route_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.grey_tag_route_id is not None:
            result['GreyTagRouteId'] = self.grey_tag_route_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GreyTagRouteId') is not None:
            self.grey_tag_route_id = m.get('GreyTagRouteId')
        return self


class DeleteGreyTagRouteResponseBodyData(TeaModel):
    def __init__(
        self,
        grey_tag_route_id: int = None,
    ):
        self.grey_tag_route_id = grey_tag_route_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.grey_tag_route_id is not None:
            result['GreyTagRouteId'] = self.grey_tag_route_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GreyTagRouteId') is not None:
            self.grey_tag_route_id = m.get('GreyTagRouteId')
        return self


class DeleteGreyTagRouteResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: DeleteGreyTagRouteResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = DeleteGreyTagRouteResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class DeleteGreyTagRouteResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteGreyTagRouteResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DeleteGreyTagRouteResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteHistoryJobRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        job_id: str = None,
    ):
        self.app_id = app_id
        self.job_id = job_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class DeleteHistoryJobResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class DeleteHistoryJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteHistoryJobResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DeleteHistoryJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteIngressRequest(TeaModel):
    def __init__(
        self,
        ingress_id: int = None,
    ):
        self.ingress_id = ingress_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ingress_id is not None:
            result['IngressId'] = self.ingress_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IngressId') is not None:
            self.ingress_id = m.get('IngressId')
        return self


class DeleteIngressResponseBodyData(TeaModel):
    def __init__(
        self,
        ingress_id: int = None,
    ):
        self.ingress_id = ingress_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ingress_id is not None:
            result['IngressId'] = self.ingress_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IngressId') is not None:
            self.ingress_id = m.get('IngressId')
        return self


class DeleteIngressResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: DeleteIngressResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = DeleteIngressResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class DeleteIngressResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteIngressResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DeleteIngressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteJobRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
    ):
        self.app_id = app_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        return self


class DeleteJobResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class DeleteJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteJobResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DeleteJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteNamespaceRequest(TeaModel):
    def __init__(
        self,
        name_space_short_id: str = None,
        namespace_id: str = None,
    ):
        self.name_space_short_id = name_space_short_id
        self.namespace_id = namespace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name_space_short_id is not None:
            result['NameSpaceShortId'] = self.name_space_short_id
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NameSpaceShortId') is not None:
            self.name_space_short_id = m.get('NameSpaceShortId')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        return self


class DeleteNamespaceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class DeleteNamespaceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteNamespaceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DeleteNamespaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSecretRequest(TeaModel):
    def __init__(
        self,
        namespace_id: str = None,
        secret_id: int = None,
    ):
        self.namespace_id = namespace_id
        self.secret_id = secret_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.secret_id is not None:
            result['SecretId'] = self.secret_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('SecretId') is not None:
            self.secret_id = m.get('SecretId')
        return self


class DeleteSecretResponseBodyData(TeaModel):
    def __init__(
        self,
        secret_id: int = None,
    ):
        self.secret_id = secret_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.secret_id is not None:
            result['SecretId'] = self.secret_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecretId') is not None:
            self.secret_id = m.get('SecretId')
        return self


class DeleteSecretResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: DeleteSecretResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = DeleteSecretResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class DeleteSecretResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteSecretResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DeleteSecretResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeployApplicationRequest(TeaModel):
    def __init__(
        self,
        acr_assume_role_arn: str = None,
        acr_instance_id: str = None,
        app_id: str = None,
        associate_eip: bool = None,
        auto_enable_application_scaling_rule: bool = None,
        batch_wait_time: int = None,
        change_order_desc: str = None,
        command: str = None,
        command_args: str = None,
        config_map_mount_desc: str = None,
        custom_host_alias: str = None,
        deploy: str = None,
        edas_container_version: str = None,
        enable_ahas: str = None,
        enable_grey_tag_route: bool = None,
        envs: str = None,
        image_pull_secrets: str = None,
        image_url: str = None,
        jar_start_args: str = None,
        jar_start_options: str = None,
        jdk: str = None,
        kafka_configs: str = None,
        liveness: str = None,
        micro_registration: str = None,
        min_ready_instance_ratio: int = None,
        min_ready_instances: int = None,
        mount_desc: str = None,
        mount_host: str = None,
        nas_configs: str = None,
        nas_id: str = None,
        oss_ak_id: str = None,
        oss_ak_secret: str = None,
        oss_mount_descs: str = None,
        package_type: str = None,
        package_url: str = None,
        package_version: str = None,
        php_arms_config_location: str = None,
        php_config: str = None,
        php_config_location: str = None,
        post_start: str = None,
        pre_stop: str = None,
        pvtz_discovery_svc: str = None,
        python: str = None,
        python_modules: str = None,
        readiness: str = None,
        sls_configs: str = None,
        termination_grace_period_seconds: int = None,
        timezone: str = None,
        tomcat_config: str = None,
        update_strategy: str = None,
        war_start_options: str = None,
        web_container: str = None,
    ):
        self.acr_assume_role_arn = acr_assume_role_arn
        self.acr_instance_id = acr_instance_id
        self.app_id = app_id
        self.associate_eip = associate_eip
        self.auto_enable_application_scaling_rule = auto_enable_application_scaling_rule
        self.batch_wait_time = batch_wait_time
        self.change_order_desc = change_order_desc
        self.command = command
        self.command_args = command_args
        self.config_map_mount_desc = config_map_mount_desc
        self.custom_host_alias = custom_host_alias
        self.deploy = deploy
        self.edas_container_version = edas_container_version
        self.enable_ahas = enable_ahas
        self.enable_grey_tag_route = enable_grey_tag_route
        self.envs = envs
        self.image_pull_secrets = image_pull_secrets
        self.image_url = image_url
        self.jar_start_args = jar_start_args
        self.jar_start_options = jar_start_options
        self.jdk = jdk
        self.kafka_configs = kafka_configs
        self.liveness = liveness
        self.micro_registration = micro_registration
        self.min_ready_instance_ratio = min_ready_instance_ratio
        self.min_ready_instances = min_ready_instances
        self.mount_desc = mount_desc
        self.mount_host = mount_host
        self.nas_configs = nas_configs
        self.nas_id = nas_id
        self.oss_ak_id = oss_ak_id
        self.oss_ak_secret = oss_ak_secret
        self.oss_mount_descs = oss_mount_descs
        self.package_type = package_type
        self.package_url = package_url
        self.package_version = package_version
        self.php_arms_config_location = php_arms_config_location
        self.php_config = php_config
        self.php_config_location = php_config_location
        self.post_start = post_start
        self.pre_stop = pre_stop
        self.pvtz_discovery_svc = pvtz_discovery_svc
        self.python = python
        self.python_modules = python_modules
        self.readiness = readiness
        self.sls_configs = sls_configs
        self.termination_grace_period_seconds = termination_grace_period_seconds
        self.timezone = timezone
        self.tomcat_config = tomcat_config
        self.update_strategy = update_strategy
        self.war_start_options = war_start_options
        self.web_container = web_container

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acr_assume_role_arn is not None:
            result['AcrAssumeRoleArn'] = self.acr_assume_role_arn
        if self.acr_instance_id is not None:
            result['AcrInstanceId'] = self.acr_instance_id
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.associate_eip is not None:
            result['AssociateEip'] = self.associate_eip
        if self.auto_enable_application_scaling_rule is not None:
            result['AutoEnableApplicationScalingRule'] = self.auto_enable_application_scaling_rule
        if self.batch_wait_time is not None:
            result['BatchWaitTime'] = self.batch_wait_time
        if self.change_order_desc is not None:
            result['ChangeOrderDesc'] = self.change_order_desc
        if self.command is not None:
            result['Command'] = self.command
        if self.command_args is not None:
            result['CommandArgs'] = self.command_args
        if self.config_map_mount_desc is not None:
            result['ConfigMapMountDesc'] = self.config_map_mount_desc
        if self.custom_host_alias is not None:
            result['CustomHostAlias'] = self.custom_host_alias
        if self.deploy is not None:
            result['Deploy'] = self.deploy
        if self.edas_container_version is not None:
            result['EdasContainerVersion'] = self.edas_container_version
        if self.enable_ahas is not None:
            result['EnableAhas'] = self.enable_ahas
        if self.enable_grey_tag_route is not None:
            result['EnableGreyTagRoute'] = self.enable_grey_tag_route
        if self.envs is not None:
            result['Envs'] = self.envs
        if self.image_pull_secrets is not None:
            result['ImagePullSecrets'] = self.image_pull_secrets
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        if self.jar_start_args is not None:
            result['JarStartArgs'] = self.jar_start_args
        if self.jar_start_options is not None:
            result['JarStartOptions'] = self.jar_start_options
        if self.jdk is not None:
            result['Jdk'] = self.jdk
        if self.kafka_configs is not None:
            result['KafkaConfigs'] = self.kafka_configs
        if self.liveness is not None:
            result['Liveness'] = self.liveness
        if self.micro_registration is not None:
            result['MicroRegistration'] = self.micro_registration
        if self.min_ready_instance_ratio is not None:
            result['MinReadyInstanceRatio'] = self.min_ready_instance_ratio
        if self.min_ready_instances is not None:
            result['MinReadyInstances'] = self.min_ready_instances
        if self.mount_desc is not None:
            result['MountDesc'] = self.mount_desc
        if self.mount_host is not None:
            result['MountHost'] = self.mount_host
        if self.nas_configs is not None:
            result['NasConfigs'] = self.nas_configs
        if self.nas_id is not None:
            result['NasId'] = self.nas_id
        if self.oss_ak_id is not None:
            result['OssAkId'] = self.oss_ak_id
        if self.oss_ak_secret is not None:
            result['OssAkSecret'] = self.oss_ak_secret
        if self.oss_mount_descs is not None:
            result['OssMountDescs'] = self.oss_mount_descs
        if self.package_type is not None:
            result['PackageType'] = self.package_type
        if self.package_url is not None:
            result['PackageUrl'] = self.package_url
        if self.package_version is not None:
            result['PackageVersion'] = self.package_version
        if self.php_arms_config_location is not None:
            result['PhpArmsConfigLocation'] = self.php_arms_config_location
        if self.php_config is not None:
            result['PhpConfig'] = self.php_config
        if self.php_config_location is not None:
            result['PhpConfigLocation'] = self.php_config_location
        if self.post_start is not None:
            result['PostStart'] = self.post_start
        if self.pre_stop is not None:
            result['PreStop'] = self.pre_stop
        if self.pvtz_discovery_svc is not None:
            result['PvtzDiscoverySvc'] = self.pvtz_discovery_svc
        if self.python is not None:
            result['Python'] = self.python
        if self.python_modules is not None:
            result['PythonModules'] = self.python_modules
        if self.readiness is not None:
            result['Readiness'] = self.readiness
        if self.sls_configs is not None:
            result['SlsConfigs'] = self.sls_configs
        if self.termination_grace_period_seconds is not None:
            result['TerminationGracePeriodSeconds'] = self.termination_grace_period_seconds
        if self.timezone is not None:
            result['Timezone'] = self.timezone
        if self.tomcat_config is not None:
            result['TomcatConfig'] = self.tomcat_config
        if self.update_strategy is not None:
            result['UpdateStrategy'] = self.update_strategy
        if self.war_start_options is not None:
            result['WarStartOptions'] = self.war_start_options
        if self.web_container is not None:
            result['WebContainer'] = self.web_container
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcrAssumeRoleArn') is not None:
            self.acr_assume_role_arn = m.get('AcrAssumeRoleArn')
        if m.get('AcrInstanceId') is not None:
            self.acr_instance_id = m.get('AcrInstanceId')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AssociateEip') is not None:
            self.associate_eip = m.get('AssociateEip')
        if m.get('AutoEnableApplicationScalingRule') is not None:
            self.auto_enable_application_scaling_rule = m.get('AutoEnableApplicationScalingRule')
        if m.get('BatchWaitTime') is not None:
            self.batch_wait_time = m.get('BatchWaitTime')
        if m.get('ChangeOrderDesc') is not None:
            self.change_order_desc = m.get('ChangeOrderDesc')
        if m.get('Command') is not None:
            self.command = m.get('Command')
        if m.get('CommandArgs') is not None:
            self.command_args = m.get('CommandArgs')
        if m.get('ConfigMapMountDesc') is not None:
            self.config_map_mount_desc = m.get('ConfigMapMountDesc')
        if m.get('CustomHostAlias') is not None:
            self.custom_host_alias = m.get('CustomHostAlias')
        if m.get('Deploy') is not None:
            self.deploy = m.get('Deploy')
        if m.get('EdasContainerVersion') is not None:
            self.edas_container_version = m.get('EdasContainerVersion')
        if m.get('EnableAhas') is not None:
            self.enable_ahas = m.get('EnableAhas')
        if m.get('EnableGreyTagRoute') is not None:
            self.enable_grey_tag_route = m.get('EnableGreyTagRoute')
        if m.get('Envs') is not None:
            self.envs = m.get('Envs')
        if m.get('ImagePullSecrets') is not None:
            self.image_pull_secrets = m.get('ImagePullSecrets')
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        if m.get('JarStartArgs') is not None:
            self.jar_start_args = m.get('JarStartArgs')
        if m.get('JarStartOptions') is not None:
            self.jar_start_options = m.get('JarStartOptions')
        if m.get('Jdk') is not None:
            self.jdk = m.get('Jdk')
        if m.get('KafkaConfigs') is not None:
            self.kafka_configs = m.get('KafkaConfigs')
        if m.get('Liveness') is not None:
            self.liveness = m.get('Liveness')
        if m.get('MicroRegistration') is not None:
            self.micro_registration = m.get('MicroRegistration')
        if m.get('MinReadyInstanceRatio') is not None:
            self.min_ready_instance_ratio = m.get('MinReadyInstanceRatio')
        if m.get('MinReadyInstances') is not None:
            self.min_ready_instances = m.get('MinReadyInstances')
        if m.get('MountDesc') is not None:
            self.mount_desc = m.get('MountDesc')
        if m.get('MountHost') is not None:
            self.mount_host = m.get('MountHost')
        if m.get('NasConfigs') is not None:
            self.nas_configs = m.get('NasConfigs')
        if m.get('NasId') is not None:
            self.nas_id = m.get('NasId')
        if m.get('OssAkId') is not None:
            self.oss_ak_id = m.get('OssAkId')
        if m.get('OssAkSecret') is not None:
            self.oss_ak_secret = m.get('OssAkSecret')
        if m.get('OssMountDescs') is not None:
            self.oss_mount_descs = m.get('OssMountDescs')
        if m.get('PackageType') is not None:
            self.package_type = m.get('PackageType')
        if m.get('PackageUrl') is not None:
            self.package_url = m.get('PackageUrl')
        if m.get('PackageVersion') is not None:
            self.package_version = m.get('PackageVersion')
        if m.get('PhpArmsConfigLocation') is not None:
            self.php_arms_config_location = m.get('PhpArmsConfigLocation')
        if m.get('PhpConfig') is not None:
            self.php_config = m.get('PhpConfig')
        if m.get('PhpConfigLocation') is not None:
            self.php_config_location = m.get('PhpConfigLocation')
        if m.get('PostStart') is not None:
            self.post_start = m.get('PostStart')
        if m.get('PreStop') is not None:
            self.pre_stop = m.get('PreStop')
        if m.get('PvtzDiscoverySvc') is not None:
            self.pvtz_discovery_svc = m.get('PvtzDiscoverySvc')
        if m.get('Python') is not None:
            self.python = m.get('Python')
        if m.get('PythonModules') is not None:
            self.python_modules = m.get('PythonModules')
        if m.get('Readiness') is not None:
            self.readiness = m.get('Readiness')
        if m.get('SlsConfigs') is not None:
            self.sls_configs = m.get('SlsConfigs')
        if m.get('TerminationGracePeriodSeconds') is not None:
            self.termination_grace_period_seconds = m.get('TerminationGracePeriodSeconds')
        if m.get('Timezone') is not None:
            self.timezone = m.get('Timezone')
        if m.get('TomcatConfig') is not None:
            self.tomcat_config = m.get('TomcatConfig')
        if m.get('UpdateStrategy') is not None:
            self.update_strategy = m.get('UpdateStrategy')
        if m.get('WarStartOptions') is not None:
            self.war_start_options = m.get('WarStartOptions')
        if m.get('WebContainer') is not None:
            self.web_container = m.get('WebContainer')
        return self


class DeployApplicationResponseBodyData(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        change_order_id: str = None,
        is_need_approval: bool = None,
    ):
        self.app_id = app_id
        self.change_order_id = change_order_id
        self.is_need_approval = is_need_approval

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.change_order_id is not None:
            result['ChangeOrderId'] = self.change_order_id
        if self.is_need_approval is not None:
            result['IsNeedApproval'] = self.is_need_approval
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ChangeOrderId') is not None:
            self.change_order_id = m.get('ChangeOrderId')
        if m.get('IsNeedApproval') is not None:
            self.is_need_approval = m.get('IsNeedApproval')
        return self


class DeployApplicationResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: DeployApplicationResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = DeployApplicationResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class DeployApplicationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeployApplicationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DeployApplicationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAppServiceDetailRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        service_group: str = None,
        service_name: str = None,
        service_type: str = None,
        service_version: str = None,
    ):
        self.app_id = app_id
        self.service_group = service_group
        self.service_name = service_name
        self.service_type = service_type
        self.service_version = service_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.service_group is not None:
            result['ServiceGroup'] = self.service_group
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        if self.service_version is not None:
            result['ServiceVersion'] = self.service_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ServiceGroup') is not None:
            self.service_group = m.get('ServiceGroup')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        if m.get('ServiceVersion') is not None:
            self.service_version = m.get('ServiceVersion')
        return self


class DescribeAppServiceDetailResponseBodyDataMethodsParameterDefinitions(TeaModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        type: str = None,
    ):
        self.description = description
        self.name = name
        self.type = type

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
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeAppServiceDetailResponseBodyDataMethods(TeaModel):
    def __init__(
        self,
        method_controller: str = None,
        name: str = None,
        name_detail: str = None,
        parameter_definitions: List[DescribeAppServiceDetailResponseBodyDataMethodsParameterDefinitions] = None,
        parameter_details: List[str] = None,
        parameter_types: List[str] = None,
        paths: List[str] = None,
        request_methods: List[str] = None,
        return_details: str = None,
        return_type: str = None,
    ):
        self.method_controller = method_controller
        self.name = name
        self.name_detail = name_detail
        self.parameter_definitions = parameter_definitions
        self.parameter_details = parameter_details
        self.parameter_types = parameter_types
        self.paths = paths
        self.request_methods = request_methods
        self.return_details = return_details
        self.return_type = return_type

    def validate(self):
        if self.parameter_definitions:
            for k in self.parameter_definitions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.method_controller is not None:
            result['MethodController'] = self.method_controller
        if self.name is not None:
            result['Name'] = self.name
        if self.name_detail is not None:
            result['NameDetail'] = self.name_detail
        result['ParameterDefinitions'] = []
        if self.parameter_definitions is not None:
            for k in self.parameter_definitions:
                result['ParameterDefinitions'].append(k.to_map() if k else None)
        if self.parameter_details is not None:
            result['ParameterDetails'] = self.parameter_details
        if self.parameter_types is not None:
            result['ParameterTypes'] = self.parameter_types
        if self.paths is not None:
            result['Paths'] = self.paths
        if self.request_methods is not None:
            result['RequestMethods'] = self.request_methods
        if self.return_details is not None:
            result['ReturnDetails'] = self.return_details
        if self.return_type is not None:
            result['ReturnType'] = self.return_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MethodController') is not None:
            self.method_controller = m.get('MethodController')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NameDetail') is not None:
            self.name_detail = m.get('NameDetail')
        self.parameter_definitions = []
        if m.get('ParameterDefinitions') is not None:
            for k in m.get('ParameterDefinitions'):
                temp_model = DescribeAppServiceDetailResponseBodyDataMethodsParameterDefinitions()
                self.parameter_definitions.append(temp_model.from_map(k))
        if m.get('ParameterDetails') is not None:
            self.parameter_details = m.get('ParameterDetails')
        if m.get('ParameterTypes') is not None:
            self.parameter_types = m.get('ParameterTypes')
        if m.get('Paths') is not None:
            self.paths = m.get('Paths')
        if m.get('RequestMethods') is not None:
            self.request_methods = m.get('RequestMethods')
        if m.get('ReturnDetails') is not None:
            self.return_details = m.get('ReturnDetails')
        if m.get('ReturnType') is not None:
            self.return_type = m.get('ReturnType')
        return self


class DescribeAppServiceDetailResponseBodyData(TeaModel):
    def __init__(
        self,
        dubbo_application_name: str = None,
        edas_app_name: str = None,
        group: str = None,
        metadata: Dict[str, Any] = None,
        methods: List[DescribeAppServiceDetailResponseBodyDataMethods] = None,
        service_name: str = None,
        service_type: str = None,
        spring_application_name: str = None,
        version: str = None,
    ):
        self.dubbo_application_name = dubbo_application_name
        self.edas_app_name = edas_app_name
        self.group = group
        self.metadata = metadata
        self.methods = methods
        self.service_name = service_name
        self.service_type = service_type
        self.spring_application_name = spring_application_name
        self.version = version

    def validate(self):
        if self.methods:
            for k in self.methods:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dubbo_application_name is not None:
            result['DubboApplicationName'] = self.dubbo_application_name
        if self.edas_app_name is not None:
            result['EdasAppName'] = self.edas_app_name
        if self.group is not None:
            result['Group'] = self.group
        if self.metadata is not None:
            result['Metadata'] = self.metadata
        result['Methods'] = []
        if self.methods is not None:
            for k in self.methods:
                result['Methods'].append(k.to_map() if k else None)
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        if self.spring_application_name is not None:
            result['SpringApplicationName'] = self.spring_application_name
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DubboApplicationName') is not None:
            self.dubbo_application_name = m.get('DubboApplicationName')
        if m.get('EdasAppName') is not None:
            self.edas_app_name = m.get('EdasAppName')
        if m.get('Group') is not None:
            self.group = m.get('Group')
        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')
        self.methods = []
        if m.get('Methods') is not None:
            for k in m.get('Methods'):
                temp_model = DescribeAppServiceDetailResponseBodyDataMethods()
                self.methods.append(temp_model.from_map(k))
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        if m.get('SpringApplicationName') is not None:
            self.spring_application_name = m.get('SpringApplicationName')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class DescribeAppServiceDetailResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: DescribeAppServiceDetailResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = DescribeAppServiceDetailResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class DescribeAppServiceDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAppServiceDetailResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DescribeAppServiceDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeApplicationConfigRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        version_id: str = None,
    ):
        self.app_id = app_id
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        return self


class DescribeApplicationConfigResponseBodyDataConfigMapMountDesc(TeaModel):
    def __init__(
        self,
        config_map_id: int = None,
        config_map_name: str = None,
        key: str = None,
        mount_path: str = None,
    ):
        # ConfigMap ID。
        self.config_map_id = config_map_id
        self.config_map_name = config_map_name
        self.key = key
        self.mount_path = mount_path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_map_id is not None:
            result['ConfigMapId'] = self.config_map_id
        if self.config_map_name is not None:
            result['ConfigMapName'] = self.config_map_name
        if self.key is not None:
            result['Key'] = self.key
        if self.mount_path is not None:
            result['MountPath'] = self.mount_path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigMapId') is not None:
            self.config_map_id = m.get('ConfigMapId')
        if m.get('ConfigMapName') is not None:
            self.config_map_name = m.get('ConfigMapName')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('MountPath') is not None:
            self.mount_path = m.get('MountPath')
        return self


class DescribeApplicationConfigResponseBodyDataMountDesc(TeaModel):
    def __init__(
        self,
        mount_path: str = None,
        nas_path: str = None,
    ):
        self.mount_path = mount_path
        self.nas_path = nas_path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mount_path is not None:
            result['MountPath'] = self.mount_path
        if self.nas_path is not None:
            result['NasPath'] = self.nas_path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MountPath') is not None:
            self.mount_path = m.get('MountPath')
        if m.get('NasPath') is not None:
            self.nas_path = m.get('NasPath')
        return self


class DescribeApplicationConfigResponseBodyDataOssMountDescs(TeaModel):
    def __init__(
        self,
        bucket_name: str = None,
        bucket_path: str = None,
        mount_path: str = None,
        read_only: bool = None,
    ):
        self.bucket_name = bucket_name
        self.bucket_path = bucket_path
        self.mount_path = mount_path
        self.read_only = read_only

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket_name is not None:
            result['bucketName'] = self.bucket_name
        if self.bucket_path is not None:
            result['bucketPath'] = self.bucket_path
        if self.mount_path is not None:
            result['mountPath'] = self.mount_path
        if self.read_only is not None:
            result['readOnly'] = self.read_only
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bucketName') is not None:
            self.bucket_name = m.get('bucketName')
        if m.get('bucketPath') is not None:
            self.bucket_path = m.get('bucketPath')
        if m.get('mountPath') is not None:
            self.mount_path = m.get('mountPath')
        if m.get('readOnly') is not None:
            self.read_only = m.get('readOnly')
        return self


class DescribeApplicationConfigResponseBodyDataTags(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeApplicationConfigResponseBodyData(TeaModel):
    def __init__(
        self,
        acr_assume_role_arn: str = None,
        acr_instance_id: str = None,
        app_description: str = None,
        app_id: str = None,
        app_name: str = None,
        associate_eip: bool = None,
        batch_wait_time: int = None,
        command: str = None,
        command_args: str = None,
        config_map_mount_desc: List[DescribeApplicationConfigResponseBodyDataConfigMapMountDesc] = None,
        cpu: int = None,
        custom_host_alias: str = None,
        edas_container_version: str = None,
        enable_ahas: str = None,
        enable_grey_tag_route: bool = None,
        envs: str = None,
        image_pull_secrets: str = None,
        image_url: str = None,
        jar_start_args: str = None,
        jar_start_options: str = None,
        jdk: str = None,
        kafka_configs: str = None,
        liveness: str = None,
        memory: int = None,
        micro_registration: str = None,
        min_ready_instance_ratio: int = None,
        min_ready_instances: int = None,
        mount_desc: List[DescribeApplicationConfigResponseBodyDataMountDesc] = None,
        mount_host: str = None,
        mse_application_id: str = None,
        namespace_id: str = None,
        nas_configs: str = None,
        nas_id: str = None,
        oss_ak_id: str = None,
        oss_ak_secret: str = None,
        oss_mount_descs: List[DescribeApplicationConfigResponseBodyDataOssMountDescs] = None,
        package_type: str = None,
        package_url: str = None,
        package_version: str = None,
        php_arms_config_location: str = None,
        php_config: str = None,
        php_config_location: str = None,
        post_start: str = None,
        pre_stop: str = None,
        programming_language: str = None,
        pvtz_discovery: str = None,
        python: str = None,
        python_modules: str = None,
        readiness: str = None,
        region_id: str = None,
        replicas: int = None,
        security_group_id: str = None,
        sls_configs: str = None,
        tags: List[DescribeApplicationConfigResponseBodyDataTags] = None,
        termination_grace_period_seconds: int = None,
        timezone: str = None,
        tomcat_config: str = None,
        update_strategy: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
        war_start_options: str = None,
        web_container: str = None,
    ):
        self.acr_assume_role_arn = acr_assume_role_arn
        self.acr_instance_id = acr_instance_id
        self.app_description = app_description
        self.app_id = app_id
        self.app_name = app_name
        self.associate_eip = associate_eip
        self.batch_wait_time = batch_wait_time
        self.command = command
        self.command_args = command_args
        self.config_map_mount_desc = config_map_mount_desc
        self.cpu = cpu
        self.custom_host_alias = custom_host_alias
        self.edas_container_version = edas_container_version
        self.enable_ahas = enable_ahas
        self.enable_grey_tag_route = enable_grey_tag_route
        self.envs = envs
        self.image_pull_secrets = image_pull_secrets
        self.image_url = image_url
        self.jar_start_args = jar_start_args
        self.jar_start_options = jar_start_options
        self.jdk = jdk
        self.kafka_configs = kafka_configs
        self.liveness = liveness
        self.memory = memory
        self.micro_registration = micro_registration
        self.min_ready_instance_ratio = min_ready_instance_ratio
        self.min_ready_instances = min_ready_instances
        self.mount_desc = mount_desc
        self.mount_host = mount_host
        self.mse_application_id = mse_application_id
        self.namespace_id = namespace_id
        self.nas_configs = nas_configs
        # NAS ID。
        self.nas_id = nas_id
        self.oss_ak_id = oss_ak_id
        self.oss_ak_secret = oss_ak_secret
        self.oss_mount_descs = oss_mount_descs
        self.package_type = package_type
        self.package_url = package_url
        self.package_version = package_version
        self.php_arms_config_location = php_arms_config_location
        self.php_config = php_config
        self.php_config_location = php_config_location
        self.post_start = post_start
        self.pre_stop = pre_stop
        self.programming_language = programming_language
        self.pvtz_discovery = pvtz_discovery
        self.python = python
        self.python_modules = python_modules
        self.readiness = readiness
        self.region_id = region_id
        self.replicas = replicas
        self.security_group_id = security_group_id
        self.sls_configs = sls_configs
        self.tags = tags
        self.termination_grace_period_seconds = termination_grace_period_seconds
        self.timezone = timezone
        self.tomcat_config = tomcat_config
        self.update_strategy = update_strategy
        # vSwitch ID。
        self.v_switch_id = v_switch_id
        # VPC ID。
        self.vpc_id = vpc_id
        self.war_start_options = war_start_options
        self.web_container = web_container

    def validate(self):
        if self.config_map_mount_desc:
            for k in self.config_map_mount_desc:
                if k:
                    k.validate()
        if self.mount_desc:
            for k in self.mount_desc:
                if k:
                    k.validate()
        if self.oss_mount_descs:
            for k in self.oss_mount_descs:
                if k:
                    k.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acr_assume_role_arn is not None:
            result['AcrAssumeRoleArn'] = self.acr_assume_role_arn
        if self.acr_instance_id is not None:
            result['AcrInstanceId'] = self.acr_instance_id
        if self.app_description is not None:
            result['AppDescription'] = self.app_description
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.associate_eip is not None:
            result['AssociateEip'] = self.associate_eip
        if self.batch_wait_time is not None:
            result['BatchWaitTime'] = self.batch_wait_time
        if self.command is not None:
            result['Command'] = self.command
        if self.command_args is not None:
            result['CommandArgs'] = self.command_args
        result['ConfigMapMountDesc'] = []
        if self.config_map_mount_desc is not None:
            for k in self.config_map_mount_desc:
                result['ConfigMapMountDesc'].append(k.to_map() if k else None)
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.custom_host_alias is not None:
            result['CustomHostAlias'] = self.custom_host_alias
        if self.edas_container_version is not None:
            result['EdasContainerVersion'] = self.edas_container_version
        if self.enable_ahas is not None:
            result['EnableAhas'] = self.enable_ahas
        if self.enable_grey_tag_route is not None:
            result['EnableGreyTagRoute'] = self.enable_grey_tag_route
        if self.envs is not None:
            result['Envs'] = self.envs
        if self.image_pull_secrets is not None:
            result['ImagePullSecrets'] = self.image_pull_secrets
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        if self.jar_start_args is not None:
            result['JarStartArgs'] = self.jar_start_args
        if self.jar_start_options is not None:
            result['JarStartOptions'] = self.jar_start_options
        if self.jdk is not None:
            result['Jdk'] = self.jdk
        if self.kafka_configs is not None:
            result['KafkaConfigs'] = self.kafka_configs
        if self.liveness is not None:
            result['Liveness'] = self.liveness
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.micro_registration is not None:
            result['MicroRegistration'] = self.micro_registration
        if self.min_ready_instance_ratio is not None:
            result['MinReadyInstanceRatio'] = self.min_ready_instance_ratio
        if self.min_ready_instances is not None:
            result['MinReadyInstances'] = self.min_ready_instances
        result['MountDesc'] = []
        if self.mount_desc is not None:
            for k in self.mount_desc:
                result['MountDesc'].append(k.to_map() if k else None)
        if self.mount_host is not None:
            result['MountHost'] = self.mount_host
        if self.mse_application_id is not None:
            result['MseApplicationId'] = self.mse_application_id
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.nas_configs is not None:
            result['NasConfigs'] = self.nas_configs
        if self.nas_id is not None:
            result['NasId'] = self.nas_id
        if self.oss_ak_id is not None:
            result['OssAkId'] = self.oss_ak_id
        if self.oss_ak_secret is not None:
            result['OssAkSecret'] = self.oss_ak_secret
        result['OssMountDescs'] = []
        if self.oss_mount_descs is not None:
            for k in self.oss_mount_descs:
                result['OssMountDescs'].append(k.to_map() if k else None)
        if self.package_type is not None:
            result['PackageType'] = self.package_type
        if self.package_url is not None:
            result['PackageUrl'] = self.package_url
        if self.package_version is not None:
            result['PackageVersion'] = self.package_version
        if self.php_arms_config_location is not None:
            result['PhpArmsConfigLocation'] = self.php_arms_config_location
        if self.php_config is not None:
            result['PhpConfig'] = self.php_config
        if self.php_config_location is not None:
            result['PhpConfigLocation'] = self.php_config_location
        if self.post_start is not None:
            result['PostStart'] = self.post_start
        if self.pre_stop is not None:
            result['PreStop'] = self.pre_stop
        if self.programming_language is not None:
            result['ProgrammingLanguage'] = self.programming_language
        if self.pvtz_discovery is not None:
            result['PvtzDiscovery'] = self.pvtz_discovery
        if self.python is not None:
            result['Python'] = self.python
        if self.python_modules is not None:
            result['PythonModules'] = self.python_modules
        if self.readiness is not None:
            result['Readiness'] = self.readiness
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.replicas is not None:
            result['Replicas'] = self.replicas
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.sls_configs is not None:
            result['SlsConfigs'] = self.sls_configs
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.termination_grace_period_seconds is not None:
            result['TerminationGracePeriodSeconds'] = self.termination_grace_period_seconds
        if self.timezone is not None:
            result['Timezone'] = self.timezone
        if self.tomcat_config is not None:
            result['TomcatConfig'] = self.tomcat_config
        if self.update_strategy is not None:
            result['UpdateStrategy'] = self.update_strategy
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.war_start_options is not None:
            result['WarStartOptions'] = self.war_start_options
        if self.web_container is not None:
            result['WebContainer'] = self.web_container
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcrAssumeRoleArn') is not None:
            self.acr_assume_role_arn = m.get('AcrAssumeRoleArn')
        if m.get('AcrInstanceId') is not None:
            self.acr_instance_id = m.get('AcrInstanceId')
        if m.get('AppDescription') is not None:
            self.app_description = m.get('AppDescription')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AssociateEip') is not None:
            self.associate_eip = m.get('AssociateEip')
        if m.get('BatchWaitTime') is not None:
            self.batch_wait_time = m.get('BatchWaitTime')
        if m.get('Command') is not None:
            self.command = m.get('Command')
        if m.get('CommandArgs') is not None:
            self.command_args = m.get('CommandArgs')
        self.config_map_mount_desc = []
        if m.get('ConfigMapMountDesc') is not None:
            for k in m.get('ConfigMapMountDesc'):
                temp_model = DescribeApplicationConfigResponseBodyDataConfigMapMountDesc()
                self.config_map_mount_desc.append(temp_model.from_map(k))
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('CustomHostAlias') is not None:
            self.custom_host_alias = m.get('CustomHostAlias')
        if m.get('EdasContainerVersion') is not None:
            self.edas_container_version = m.get('EdasContainerVersion')
        if m.get('EnableAhas') is not None:
            self.enable_ahas = m.get('EnableAhas')
        if m.get('EnableGreyTagRoute') is not None:
            self.enable_grey_tag_route = m.get('EnableGreyTagRoute')
        if m.get('Envs') is not None:
            self.envs = m.get('Envs')
        if m.get('ImagePullSecrets') is not None:
            self.image_pull_secrets = m.get('ImagePullSecrets')
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        if m.get('JarStartArgs') is not None:
            self.jar_start_args = m.get('JarStartArgs')
        if m.get('JarStartOptions') is not None:
            self.jar_start_options = m.get('JarStartOptions')
        if m.get('Jdk') is not None:
            self.jdk = m.get('Jdk')
        if m.get('KafkaConfigs') is not None:
            self.kafka_configs = m.get('KafkaConfigs')
        if m.get('Liveness') is not None:
            self.liveness = m.get('Liveness')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('MicroRegistration') is not None:
            self.micro_registration = m.get('MicroRegistration')
        if m.get('MinReadyInstanceRatio') is not None:
            self.min_ready_instance_ratio = m.get('MinReadyInstanceRatio')
        if m.get('MinReadyInstances') is not None:
            self.min_ready_instances = m.get('MinReadyInstances')
        self.mount_desc = []
        if m.get('MountDesc') is not None:
            for k in m.get('MountDesc'):
                temp_model = DescribeApplicationConfigResponseBodyDataMountDesc()
                self.mount_desc.append(temp_model.from_map(k))
        if m.get('MountHost') is not None:
            self.mount_host = m.get('MountHost')
        if m.get('MseApplicationId') is not None:
            self.mse_application_id = m.get('MseApplicationId')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('NasConfigs') is not None:
            self.nas_configs = m.get('NasConfigs')
        if m.get('NasId') is not None:
            self.nas_id = m.get('NasId')
        if m.get('OssAkId') is not None:
            self.oss_ak_id = m.get('OssAkId')
        if m.get('OssAkSecret') is not None:
            self.oss_ak_secret = m.get('OssAkSecret')
        self.oss_mount_descs = []
        if m.get('OssMountDescs') is not None:
            for k in m.get('OssMountDescs'):
                temp_model = DescribeApplicationConfigResponseBodyDataOssMountDescs()
                self.oss_mount_descs.append(temp_model.from_map(k))
        if m.get('PackageType') is not None:
            self.package_type = m.get('PackageType')
        if m.get('PackageUrl') is not None:
            self.package_url = m.get('PackageUrl')
        if m.get('PackageVersion') is not None:
            self.package_version = m.get('PackageVersion')
        if m.get('PhpArmsConfigLocation') is not None:
            self.php_arms_config_location = m.get('PhpArmsConfigLocation')
        if m.get('PhpConfig') is not None:
            self.php_config = m.get('PhpConfig')
        if m.get('PhpConfigLocation') is not None:
            self.php_config_location = m.get('PhpConfigLocation')
        if m.get('PostStart') is not None:
            self.post_start = m.get('PostStart')
        if m.get('PreStop') is not None:
            self.pre_stop = m.get('PreStop')
        if m.get('ProgrammingLanguage') is not None:
            self.programming_language = m.get('ProgrammingLanguage')
        if m.get('PvtzDiscovery') is not None:
            self.pvtz_discovery = m.get('PvtzDiscovery')
        if m.get('Python') is not None:
            self.python = m.get('Python')
        if m.get('PythonModules') is not None:
            self.python_modules = m.get('PythonModules')
        if m.get('Readiness') is not None:
            self.readiness = m.get('Readiness')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Replicas') is not None:
            self.replicas = m.get('Replicas')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('SlsConfigs') is not None:
            self.sls_configs = m.get('SlsConfigs')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = DescribeApplicationConfigResponseBodyDataTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('TerminationGracePeriodSeconds') is not None:
            self.termination_grace_period_seconds = m.get('TerminationGracePeriodSeconds')
        if m.get('Timezone') is not None:
            self.timezone = m.get('Timezone')
        if m.get('TomcatConfig') is not None:
            self.tomcat_config = m.get('TomcatConfig')
        if m.get('UpdateStrategy') is not None:
            self.update_strategy = m.get('UpdateStrategy')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('WarStartOptions') is not None:
            self.war_start_options = m.get('WarStartOptions')
        if m.get('WebContainer') is not None:
            self.web_container = m.get('WebContainer')
        return self


class DescribeApplicationConfigResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: DescribeApplicationConfigResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = DescribeApplicationConfigResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class DescribeApplicationConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeApplicationConfigResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DescribeApplicationConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeApplicationGroupsRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        current_page: int = None,
        page_size: int = None,
    ):
        self.app_id = app_id
        self.current_page = current_page
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeApplicationGroupsResponseBodyData(TeaModel):
    def __init__(
        self,
        edas_container_version: str = None,
        group_id: str = None,
        group_name: str = None,
        group_type: int = None,
        image_url: str = None,
        jdk: str = None,
        package_type: str = None,
        package_url: str = None,
        package_version: str = None,
        replicas: int = None,
        running_instances: int = None,
        web_container: str = None,
    ):
        self.edas_container_version = edas_container_version
        self.group_id = group_id
        self.group_name = group_name
        self.group_type = group_type
        self.image_url = image_url
        self.jdk = jdk
        self.package_type = package_type
        self.package_url = package_url
        self.package_version = package_version
        self.replicas = replicas
        self.running_instances = running_instances
        self.web_container = web_container

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.edas_container_version is not None:
            result['EdasContainerVersion'] = self.edas_container_version
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.group_type is not None:
            result['GroupType'] = self.group_type
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        if self.jdk is not None:
            result['Jdk'] = self.jdk
        if self.package_type is not None:
            result['PackageType'] = self.package_type
        if self.package_url is not None:
            result['PackageUrl'] = self.package_url
        if self.package_version is not None:
            result['PackageVersion'] = self.package_version
        if self.replicas is not None:
            result['Replicas'] = self.replicas
        if self.running_instances is not None:
            result['RunningInstances'] = self.running_instances
        if self.web_container is not None:
            result['WebContainer'] = self.web_container
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EdasContainerVersion') is not None:
            self.edas_container_version = m.get('EdasContainerVersion')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('GroupType') is not None:
            self.group_type = m.get('GroupType')
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        if m.get('Jdk') is not None:
            self.jdk = m.get('Jdk')
        if m.get('PackageType') is not None:
            self.package_type = m.get('PackageType')
        if m.get('PackageUrl') is not None:
            self.package_url = m.get('PackageUrl')
        if m.get('PackageVersion') is not None:
            self.package_version = m.get('PackageVersion')
        if m.get('Replicas') is not None:
            self.replicas = m.get('Replicas')
        if m.get('RunningInstances') is not None:
            self.running_instances = m.get('RunningInstances')
        if m.get('WebContainer') is not None:
            self.web_container = m.get('WebContainer')
        return self


class DescribeApplicationGroupsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[DescribeApplicationGroupsResponseBodyData] = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = DescribeApplicationGroupsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class DescribeApplicationGroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeApplicationGroupsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DescribeApplicationGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeApplicationImageRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        image_url: str = None,
    ):
        self.app_id = app_id
        self.image_url = image_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        return self


class DescribeApplicationImageResponseBodyData(TeaModel):
    def __init__(
        self,
        cr_url: str = None,
        logo: str = None,
        region_id: str = None,
        repo_name: str = None,
        repo_namespace: str = None,
        repo_origin_type: str = None,
        repo_tag: str = None,
        repo_type: str = None,
    ):
        self.cr_url = cr_url
        self.logo = logo
        self.region_id = region_id
        self.repo_name = repo_name
        self.repo_namespace = repo_namespace
        self.repo_origin_type = repo_origin_type
        self.repo_tag = repo_tag
        self.repo_type = repo_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cr_url is not None:
            result['CrUrl'] = self.cr_url
        if self.logo is not None:
            result['Logo'] = self.logo
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.repo_name is not None:
            result['RepoName'] = self.repo_name
        if self.repo_namespace is not None:
            result['RepoNamespace'] = self.repo_namespace
        if self.repo_origin_type is not None:
            result['RepoOriginType'] = self.repo_origin_type
        if self.repo_tag is not None:
            result['RepoTag'] = self.repo_tag
        if self.repo_type is not None:
            result['RepoType'] = self.repo_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CrUrl') is not None:
            self.cr_url = m.get('CrUrl')
        if m.get('Logo') is not None:
            self.logo = m.get('Logo')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')
        if m.get('RepoNamespace') is not None:
            self.repo_namespace = m.get('RepoNamespace')
        if m.get('RepoOriginType') is not None:
            self.repo_origin_type = m.get('RepoOriginType')
        if m.get('RepoTag') is not None:
            self.repo_tag = m.get('RepoTag')
        if m.get('RepoType') is not None:
            self.repo_type = m.get('RepoType')
        return self


class DescribeApplicationImageResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: DescribeApplicationImageResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = DescribeApplicationImageResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class DescribeApplicationImageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeApplicationImageResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DescribeApplicationImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeApplicationInstancesRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        current_page: int = None,
        group_id: str = None,
        page_size: int = None,
        reverse: bool = None,
    ):
        self.app_id = app_id
        self.current_page = current_page
        self.group_id = group_id
        self.page_size = page_size
        self.reverse = reverse

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.reverse is not None:
            result['Reverse'] = self.reverse
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Reverse') is not None:
            self.reverse = m.get('Reverse')
        return self


class DescribeApplicationInstancesResponseBodyDataInstances(TeaModel):
    def __init__(
        self,
        create_time_stamp: int = None,
        debug_status: bool = None,
        eip: str = None,
        finish_time_stamp: int = None,
        group_id: str = None,
        image_url: str = None,
        instance_container_ip: str = None,
        instance_container_restarts: int = None,
        instance_container_status: str = None,
        instance_health_status: str = None,
        instance_id: str = None,
        package_version: str = None,
        v_switch_id: str = None,
    ):
        self.create_time_stamp = create_time_stamp
        self.debug_status = debug_status
        self.eip = eip
        self.finish_time_stamp = finish_time_stamp
        self.group_id = group_id
        self.image_url = image_url
        self.instance_container_ip = instance_container_ip
        self.instance_container_restarts = instance_container_restarts
        self.instance_container_status = instance_container_status
        self.instance_health_status = instance_health_status
        self.instance_id = instance_id
        self.package_version = package_version
        self.v_switch_id = v_switch_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time_stamp is not None:
            result['CreateTimeStamp'] = self.create_time_stamp
        if self.debug_status is not None:
            result['DebugStatus'] = self.debug_status
        if self.eip is not None:
            result['Eip'] = self.eip
        if self.finish_time_stamp is not None:
            result['FinishTimeStamp'] = self.finish_time_stamp
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        if self.instance_container_ip is not None:
            result['InstanceContainerIp'] = self.instance_container_ip
        if self.instance_container_restarts is not None:
            result['InstanceContainerRestarts'] = self.instance_container_restarts
        if self.instance_container_status is not None:
            result['InstanceContainerStatus'] = self.instance_container_status
        if self.instance_health_status is not None:
            result['InstanceHealthStatus'] = self.instance_health_status
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.package_version is not None:
            result['PackageVersion'] = self.package_version
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTimeStamp') is not None:
            self.create_time_stamp = m.get('CreateTimeStamp')
        if m.get('DebugStatus') is not None:
            self.debug_status = m.get('DebugStatus')
        if m.get('Eip') is not None:
            self.eip = m.get('Eip')
        if m.get('FinishTimeStamp') is not None:
            self.finish_time_stamp = m.get('FinishTimeStamp')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        if m.get('InstanceContainerIp') is not None:
            self.instance_container_ip = m.get('InstanceContainerIp')
        if m.get('InstanceContainerRestarts') is not None:
            self.instance_container_restarts = m.get('InstanceContainerRestarts')
        if m.get('InstanceContainerStatus') is not None:
            self.instance_container_status = m.get('InstanceContainerStatus')
        if m.get('InstanceHealthStatus') is not None:
            self.instance_health_status = m.get('InstanceHealthStatus')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PackageVersion') is not None:
            self.package_version = m.get('PackageVersion')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        return self


class DescribeApplicationInstancesResponseBodyData(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        instances: List[DescribeApplicationInstancesResponseBodyDataInstances] = None,
        page_size: int = None,
        total_size: int = None,
    ):
        self.current_page = current_page
        self.instances = instances
        self.page_size = page_size
        self.total_size = total_size

    def validate(self):
        if self.instances:
            for k in self.instances:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['Instances'] = []
        if self.instances is not None:
            for k in self.instances:
                result['Instances'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_size is not None:
            result['TotalSize'] = self.total_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.instances = []
        if m.get('Instances') is not None:
            for k in m.get('Instances'):
                temp_model = DescribeApplicationInstancesResponseBodyDataInstances()
                self.instances.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalSize') is not None:
            self.total_size = m.get('TotalSize')
        return self


class DescribeApplicationInstancesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: DescribeApplicationInstancesResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = DescribeApplicationInstancesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class DescribeApplicationInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeApplicationInstancesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DescribeApplicationInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeApplicationScalingRuleRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        scaling_rule_name: str = None,
    ):
        self.app_id = app_id
        self.scaling_rule_name = scaling_rule_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.scaling_rule_name is not None:
            result['ScalingRuleName'] = self.scaling_rule_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ScalingRuleName') is not None:
            self.scaling_rule_name = m.get('ScalingRuleName')
        return self


class DescribeApplicationScalingRuleResponseBodyDataMetricMetrics(TeaModel):
    def __init__(
        self,
        metric_target_average_utilization: int = None,
        metric_type: str = None,
    ):
        self.metric_target_average_utilization = metric_target_average_utilization
        self.metric_type = metric_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.metric_target_average_utilization is not None:
            result['MetricTargetAverageUtilization'] = self.metric_target_average_utilization
        if self.metric_type is not None:
            result['MetricType'] = self.metric_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MetricTargetAverageUtilization') is not None:
            self.metric_target_average_utilization = m.get('MetricTargetAverageUtilization')
        if m.get('MetricType') is not None:
            self.metric_type = m.get('MetricType')
        return self


class DescribeApplicationScalingRuleResponseBodyDataMetricMetricsStatusCurrentMetrics(TeaModel):
    def __init__(
        self,
        current_value: int = None,
        name: str = None,
        type: str = None,
    ):
        self.current_value = current_value
        self.name = name
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_value is not None:
            result['CurrentValue'] = self.current_value
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentValue') is not None:
            self.current_value = m.get('CurrentValue')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeApplicationScalingRuleResponseBodyDataMetricMetricsStatusNextScaleMetrics(TeaModel):
    def __init__(
        self,
        name: str = None,
        next_scale_in_average_utilization: int = None,
        next_scale_out_average_utilization: int = None,
    ):
        self.name = name
        self.next_scale_in_average_utilization = next_scale_in_average_utilization
        self.next_scale_out_average_utilization = next_scale_out_average_utilization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.next_scale_in_average_utilization is not None:
            result['NextScaleInAverageUtilization'] = self.next_scale_in_average_utilization
        if self.next_scale_out_average_utilization is not None:
            result['NextScaleOutAverageUtilization'] = self.next_scale_out_average_utilization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NextScaleInAverageUtilization') is not None:
            self.next_scale_in_average_utilization = m.get('NextScaleInAverageUtilization')
        if m.get('NextScaleOutAverageUtilization') is not None:
            self.next_scale_out_average_utilization = m.get('NextScaleOutAverageUtilization')
        return self


class DescribeApplicationScalingRuleResponseBodyDataMetricMetricsStatus(TeaModel):
    def __init__(
        self,
        current_metrics: List[DescribeApplicationScalingRuleResponseBodyDataMetricMetricsStatusCurrentMetrics] = None,
        current_replicas: int = None,
        desired_replicas: int = None,
        last_scale_time: str = None,
        next_scale_metrics: List[DescribeApplicationScalingRuleResponseBodyDataMetricMetricsStatusNextScaleMetrics] = None,
        next_scale_time_period: int = None,
    ):
        self.current_metrics = current_metrics
        self.current_replicas = current_replicas
        self.desired_replicas = desired_replicas
        self.last_scale_time = last_scale_time
        self.next_scale_metrics = next_scale_metrics
        self.next_scale_time_period = next_scale_time_period

    def validate(self):
        if self.current_metrics:
            for k in self.current_metrics:
                if k:
                    k.validate()
        if self.next_scale_metrics:
            for k in self.next_scale_metrics:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CurrentMetrics'] = []
        if self.current_metrics is not None:
            for k in self.current_metrics:
                result['CurrentMetrics'].append(k.to_map() if k else None)
        if self.current_replicas is not None:
            result['CurrentReplicas'] = self.current_replicas
        if self.desired_replicas is not None:
            result['DesiredReplicas'] = self.desired_replicas
        if self.last_scale_time is not None:
            result['LastScaleTime'] = self.last_scale_time
        result['NextScaleMetrics'] = []
        if self.next_scale_metrics is not None:
            for k in self.next_scale_metrics:
                result['NextScaleMetrics'].append(k.to_map() if k else None)
        if self.next_scale_time_period is not None:
            result['NextScaleTimePeriod'] = self.next_scale_time_period
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.current_metrics = []
        if m.get('CurrentMetrics') is not None:
            for k in m.get('CurrentMetrics'):
                temp_model = DescribeApplicationScalingRuleResponseBodyDataMetricMetricsStatusCurrentMetrics()
                self.current_metrics.append(temp_model.from_map(k))
        if m.get('CurrentReplicas') is not None:
            self.current_replicas = m.get('CurrentReplicas')
        if m.get('DesiredReplicas') is not None:
            self.desired_replicas = m.get('DesiredReplicas')
        if m.get('LastScaleTime') is not None:
            self.last_scale_time = m.get('LastScaleTime')
        self.next_scale_metrics = []
        if m.get('NextScaleMetrics') is not None:
            for k in m.get('NextScaleMetrics'):
                temp_model = DescribeApplicationScalingRuleResponseBodyDataMetricMetricsStatusNextScaleMetrics()
                self.next_scale_metrics.append(temp_model.from_map(k))
        if m.get('NextScaleTimePeriod') is not None:
            self.next_scale_time_period = m.get('NextScaleTimePeriod')
        return self


class DescribeApplicationScalingRuleResponseBodyDataMetricScaleDownRules(TeaModel):
    def __init__(
        self,
        disabled: bool = None,
        stabilization_window_seconds: int = None,
        step: int = None,
    ):
        self.disabled = disabled
        self.stabilization_window_seconds = stabilization_window_seconds
        self.step = step

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.disabled is not None:
            result['Disabled'] = self.disabled
        if self.stabilization_window_seconds is not None:
            result['StabilizationWindowSeconds'] = self.stabilization_window_seconds
        if self.step is not None:
            result['Step'] = self.step
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Disabled') is not None:
            self.disabled = m.get('Disabled')
        if m.get('StabilizationWindowSeconds') is not None:
            self.stabilization_window_seconds = m.get('StabilizationWindowSeconds')
        if m.get('Step') is not None:
            self.step = m.get('Step')
        return self


class DescribeApplicationScalingRuleResponseBodyDataMetricScaleUpRules(TeaModel):
    def __init__(
        self,
        disabled: bool = None,
        stabilization_window_seconds: int = None,
        step: int = None,
    ):
        self.disabled = disabled
        self.stabilization_window_seconds = stabilization_window_seconds
        self.step = step

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.disabled is not None:
            result['Disabled'] = self.disabled
        if self.stabilization_window_seconds is not None:
            result['StabilizationWindowSeconds'] = self.stabilization_window_seconds
        if self.step is not None:
            result['Step'] = self.step
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Disabled') is not None:
            self.disabled = m.get('Disabled')
        if m.get('StabilizationWindowSeconds') is not None:
            self.stabilization_window_seconds = m.get('StabilizationWindowSeconds')
        if m.get('Step') is not None:
            self.step = m.get('Step')
        return self


class DescribeApplicationScalingRuleResponseBodyDataMetric(TeaModel):
    def __init__(
        self,
        max_replicas: int = None,
        metrics: List[DescribeApplicationScalingRuleResponseBodyDataMetricMetrics] = None,
        metrics_status: DescribeApplicationScalingRuleResponseBodyDataMetricMetricsStatus = None,
        min_replicas: int = None,
        scale_down_rules: DescribeApplicationScalingRuleResponseBodyDataMetricScaleDownRules = None,
        scale_up_rules: DescribeApplicationScalingRuleResponseBodyDataMetricScaleUpRules = None,
    ):
        self.max_replicas = max_replicas
        self.metrics = metrics
        self.metrics_status = metrics_status
        self.min_replicas = min_replicas
        self.scale_down_rules = scale_down_rules
        self.scale_up_rules = scale_up_rules

    def validate(self):
        if self.metrics:
            for k in self.metrics:
                if k:
                    k.validate()
        if self.metrics_status:
            self.metrics_status.validate()
        if self.scale_down_rules:
            self.scale_down_rules.validate()
        if self.scale_up_rules:
            self.scale_up_rules.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_replicas is not None:
            result['MaxReplicas'] = self.max_replicas
        result['Metrics'] = []
        if self.metrics is not None:
            for k in self.metrics:
                result['Metrics'].append(k.to_map() if k else None)
        if self.metrics_status is not None:
            result['MetricsStatus'] = self.metrics_status.to_map()
        if self.min_replicas is not None:
            result['MinReplicas'] = self.min_replicas
        if self.scale_down_rules is not None:
            result['ScaleDownRules'] = self.scale_down_rules.to_map()
        if self.scale_up_rules is not None:
            result['ScaleUpRules'] = self.scale_up_rules.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxReplicas') is not None:
            self.max_replicas = m.get('MaxReplicas')
        self.metrics = []
        if m.get('Metrics') is not None:
            for k in m.get('Metrics'):
                temp_model = DescribeApplicationScalingRuleResponseBodyDataMetricMetrics()
                self.metrics.append(temp_model.from_map(k))
        if m.get('MetricsStatus') is not None:
            temp_model = DescribeApplicationScalingRuleResponseBodyDataMetricMetricsStatus()
            self.metrics_status = temp_model.from_map(m['MetricsStatus'])
        if m.get('MinReplicas') is not None:
            self.min_replicas = m.get('MinReplicas')
        if m.get('ScaleDownRules') is not None:
            temp_model = DescribeApplicationScalingRuleResponseBodyDataMetricScaleDownRules()
            self.scale_down_rules = temp_model.from_map(m['ScaleDownRules'])
        if m.get('ScaleUpRules') is not None:
            temp_model = DescribeApplicationScalingRuleResponseBodyDataMetricScaleUpRules()
            self.scale_up_rules = temp_model.from_map(m['ScaleUpRules'])
        return self


class DescribeApplicationScalingRuleResponseBodyDataTimerSchedules(TeaModel):
    def __init__(
        self,
        at_time: str = None,
        target_replicas: int = None,
    ):
        self.at_time = at_time
        self.target_replicas = target_replicas

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.at_time is not None:
            result['AtTime'] = self.at_time
        if self.target_replicas is not None:
            result['TargetReplicas'] = self.target_replicas
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AtTime') is not None:
            self.at_time = m.get('AtTime')
        if m.get('TargetReplicas') is not None:
            self.target_replicas = m.get('TargetReplicas')
        return self


class DescribeApplicationScalingRuleResponseBodyDataTimer(TeaModel):
    def __init__(
        self,
        begin_date: str = None,
        end_date: str = None,
        period: str = None,
        schedules: List[DescribeApplicationScalingRuleResponseBodyDataTimerSchedules] = None,
    ):
        self.begin_date = begin_date
        self.end_date = end_date
        self.period = period
        self.schedules = schedules

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
        if self.begin_date is not None:
            result['BeginDate'] = self.begin_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.period is not None:
            result['Period'] = self.period
        result['Schedules'] = []
        if self.schedules is not None:
            for k in self.schedules:
                result['Schedules'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginDate') is not None:
            self.begin_date = m.get('BeginDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        self.schedules = []
        if m.get('Schedules') is not None:
            for k in m.get('Schedules'):
                temp_model = DescribeApplicationScalingRuleResponseBodyDataTimerSchedules()
                self.schedules.append(temp_model.from_map(k))
        return self


class DescribeApplicationScalingRuleResponseBodyData(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        create_time: int = None,
        last_disable_time: int = None,
        metric: DescribeApplicationScalingRuleResponseBodyDataMetric = None,
        scale_rule_enabled: bool = None,
        scale_rule_name: str = None,
        scale_rule_type: str = None,
        timer: DescribeApplicationScalingRuleResponseBodyDataTimer = None,
        update_time: int = None,
    ):
        self.app_id = app_id
        self.create_time = create_time
        self.last_disable_time = last_disable_time
        self.metric = metric
        self.scale_rule_enabled = scale_rule_enabled
        self.scale_rule_name = scale_rule_name
        self.scale_rule_type = scale_rule_type
        self.timer = timer
        self.update_time = update_time

    def validate(self):
        if self.metric:
            self.metric.validate()
        if self.timer:
            self.timer.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.last_disable_time is not None:
            result['LastDisableTime'] = self.last_disable_time
        if self.metric is not None:
            result['Metric'] = self.metric.to_map()
        if self.scale_rule_enabled is not None:
            result['ScaleRuleEnabled'] = self.scale_rule_enabled
        if self.scale_rule_name is not None:
            result['ScaleRuleName'] = self.scale_rule_name
        if self.scale_rule_type is not None:
            result['ScaleRuleType'] = self.scale_rule_type
        if self.timer is not None:
            result['Timer'] = self.timer.to_map()
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('LastDisableTime') is not None:
            self.last_disable_time = m.get('LastDisableTime')
        if m.get('Metric') is not None:
            temp_model = DescribeApplicationScalingRuleResponseBodyDataMetric()
            self.metric = temp_model.from_map(m['Metric'])
        if m.get('ScaleRuleEnabled') is not None:
            self.scale_rule_enabled = m.get('ScaleRuleEnabled')
        if m.get('ScaleRuleName') is not None:
            self.scale_rule_name = m.get('ScaleRuleName')
        if m.get('ScaleRuleType') is not None:
            self.scale_rule_type = m.get('ScaleRuleType')
        if m.get('Timer') is not None:
            temp_model = DescribeApplicationScalingRuleResponseBodyDataTimer()
            self.timer = temp_model.from_map(m['Timer'])
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class DescribeApplicationScalingRuleResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: DescribeApplicationScalingRuleResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = DescribeApplicationScalingRuleResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class DescribeApplicationScalingRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeApplicationScalingRuleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DescribeApplicationScalingRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeApplicationScalingRulesRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
    ):
        self.app_id = app_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        return self


class DescribeApplicationScalingRulesResponseBodyDataApplicationScalingRulesMetricMetrics(TeaModel):
    def __init__(
        self,
        metric_target_average_utilization: int = None,
        metric_type: str = None,
    ):
        self.metric_target_average_utilization = metric_target_average_utilization
        self.metric_type = metric_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.metric_target_average_utilization is not None:
            result['MetricTargetAverageUtilization'] = self.metric_target_average_utilization
        if self.metric_type is not None:
            result['MetricType'] = self.metric_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MetricTargetAverageUtilization') is not None:
            self.metric_target_average_utilization = m.get('MetricTargetAverageUtilization')
        if m.get('MetricType') is not None:
            self.metric_type = m.get('MetricType')
        return self


class DescribeApplicationScalingRulesResponseBodyDataApplicationScalingRulesMetricMetricsStatusCurrentMetrics(TeaModel):
    def __init__(
        self,
        current_value: int = None,
        name: str = None,
        type: str = None,
    ):
        self.current_value = current_value
        self.name = name
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_value is not None:
            result['CurrentValue'] = self.current_value
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentValue') is not None:
            self.current_value = m.get('CurrentValue')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeApplicationScalingRulesResponseBodyDataApplicationScalingRulesMetricMetricsStatusNextScaleMetrics(TeaModel):
    def __init__(
        self,
        name: str = None,
        next_scale_in_average_utilization: int = None,
        next_scale_out_average_utilization: int = None,
    ):
        self.name = name
        self.next_scale_in_average_utilization = next_scale_in_average_utilization
        self.next_scale_out_average_utilization = next_scale_out_average_utilization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.next_scale_in_average_utilization is not None:
            result['NextScaleInAverageUtilization'] = self.next_scale_in_average_utilization
        if self.next_scale_out_average_utilization is not None:
            result['NextScaleOutAverageUtilization'] = self.next_scale_out_average_utilization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NextScaleInAverageUtilization') is not None:
            self.next_scale_in_average_utilization = m.get('NextScaleInAverageUtilization')
        if m.get('NextScaleOutAverageUtilization') is not None:
            self.next_scale_out_average_utilization = m.get('NextScaleOutAverageUtilization')
        return self


class DescribeApplicationScalingRulesResponseBodyDataApplicationScalingRulesMetricMetricsStatus(TeaModel):
    def __init__(
        self,
        current_metrics: List[DescribeApplicationScalingRulesResponseBodyDataApplicationScalingRulesMetricMetricsStatusCurrentMetrics] = None,
        current_replicas: int = None,
        desired_replicas: int = None,
        last_scale_time: str = None,
        max_replicas: int = None,
        min_replicas: int = None,
        next_scale_metrics: List[DescribeApplicationScalingRulesResponseBodyDataApplicationScalingRulesMetricMetricsStatusNextScaleMetrics] = None,
        next_scale_time_period: int = None,
    ):
        self.current_metrics = current_metrics
        self.current_replicas = current_replicas
        self.desired_replicas = desired_replicas
        self.last_scale_time = last_scale_time
        self.max_replicas = max_replicas
        self.min_replicas = min_replicas
        self.next_scale_metrics = next_scale_metrics
        self.next_scale_time_period = next_scale_time_period

    def validate(self):
        if self.current_metrics:
            for k in self.current_metrics:
                if k:
                    k.validate()
        if self.next_scale_metrics:
            for k in self.next_scale_metrics:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CurrentMetrics'] = []
        if self.current_metrics is not None:
            for k in self.current_metrics:
                result['CurrentMetrics'].append(k.to_map() if k else None)
        if self.current_replicas is not None:
            result['CurrentReplicas'] = self.current_replicas
        if self.desired_replicas is not None:
            result['DesiredReplicas'] = self.desired_replicas
        if self.last_scale_time is not None:
            result['LastScaleTime'] = self.last_scale_time
        if self.max_replicas is not None:
            result['MaxReplicas'] = self.max_replicas
        if self.min_replicas is not None:
            result['MinReplicas'] = self.min_replicas
        result['NextScaleMetrics'] = []
        if self.next_scale_metrics is not None:
            for k in self.next_scale_metrics:
                result['NextScaleMetrics'].append(k.to_map() if k else None)
        if self.next_scale_time_period is not None:
            result['NextScaleTimePeriod'] = self.next_scale_time_period
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.current_metrics = []
        if m.get('CurrentMetrics') is not None:
            for k in m.get('CurrentMetrics'):
                temp_model = DescribeApplicationScalingRulesResponseBodyDataApplicationScalingRulesMetricMetricsStatusCurrentMetrics()
                self.current_metrics.append(temp_model.from_map(k))
        if m.get('CurrentReplicas') is not None:
            self.current_replicas = m.get('CurrentReplicas')
        if m.get('DesiredReplicas') is not None:
            self.desired_replicas = m.get('DesiredReplicas')
        if m.get('LastScaleTime') is not None:
            self.last_scale_time = m.get('LastScaleTime')
        if m.get('MaxReplicas') is not None:
            self.max_replicas = m.get('MaxReplicas')
        if m.get('MinReplicas') is not None:
            self.min_replicas = m.get('MinReplicas')
        self.next_scale_metrics = []
        if m.get('NextScaleMetrics') is not None:
            for k in m.get('NextScaleMetrics'):
                temp_model = DescribeApplicationScalingRulesResponseBodyDataApplicationScalingRulesMetricMetricsStatusNextScaleMetrics()
                self.next_scale_metrics.append(temp_model.from_map(k))
        if m.get('NextScaleTimePeriod') is not None:
            self.next_scale_time_period = m.get('NextScaleTimePeriod')
        return self


class DescribeApplicationScalingRulesResponseBodyDataApplicationScalingRulesMetricScaleDownRules(TeaModel):
    def __init__(
        self,
        disabled: bool = None,
        stabilization_window_seconds: int = None,
        step: int = None,
    ):
        self.disabled = disabled
        self.stabilization_window_seconds = stabilization_window_seconds
        self.step = step

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.disabled is not None:
            result['Disabled'] = self.disabled
        if self.stabilization_window_seconds is not None:
            result['StabilizationWindowSeconds'] = self.stabilization_window_seconds
        if self.step is not None:
            result['Step'] = self.step
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Disabled') is not None:
            self.disabled = m.get('Disabled')
        if m.get('StabilizationWindowSeconds') is not None:
            self.stabilization_window_seconds = m.get('StabilizationWindowSeconds')
        if m.get('Step') is not None:
            self.step = m.get('Step')
        return self


class DescribeApplicationScalingRulesResponseBodyDataApplicationScalingRulesMetricScaleUpRules(TeaModel):
    def __init__(
        self,
        disabled: bool = None,
        stabilization_window_seconds: int = None,
        step: int = None,
    ):
        self.disabled = disabled
        self.stabilization_window_seconds = stabilization_window_seconds
        self.step = step

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.disabled is not None:
            result['Disabled'] = self.disabled
        if self.stabilization_window_seconds is not None:
            result['StabilizationWindowSeconds'] = self.stabilization_window_seconds
        if self.step is not None:
            result['Step'] = self.step
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Disabled') is not None:
            self.disabled = m.get('Disabled')
        if m.get('StabilizationWindowSeconds') is not None:
            self.stabilization_window_seconds = m.get('StabilizationWindowSeconds')
        if m.get('Step') is not None:
            self.step = m.get('Step')
        return self


class DescribeApplicationScalingRulesResponseBodyDataApplicationScalingRulesMetric(TeaModel):
    def __init__(
        self,
        max_replicas: int = None,
        metrics: List[DescribeApplicationScalingRulesResponseBodyDataApplicationScalingRulesMetricMetrics] = None,
        metrics_status: DescribeApplicationScalingRulesResponseBodyDataApplicationScalingRulesMetricMetricsStatus = None,
        min_replicas: int = None,
        scale_down_rules: DescribeApplicationScalingRulesResponseBodyDataApplicationScalingRulesMetricScaleDownRules = None,
        scale_up_rules: DescribeApplicationScalingRulesResponseBodyDataApplicationScalingRulesMetricScaleUpRules = None,
    ):
        self.max_replicas = max_replicas
        self.metrics = metrics
        self.metrics_status = metrics_status
        self.min_replicas = min_replicas
        self.scale_down_rules = scale_down_rules
        self.scale_up_rules = scale_up_rules

    def validate(self):
        if self.metrics:
            for k in self.metrics:
                if k:
                    k.validate()
        if self.metrics_status:
            self.metrics_status.validate()
        if self.scale_down_rules:
            self.scale_down_rules.validate()
        if self.scale_up_rules:
            self.scale_up_rules.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_replicas is not None:
            result['MaxReplicas'] = self.max_replicas
        result['Metrics'] = []
        if self.metrics is not None:
            for k in self.metrics:
                result['Metrics'].append(k.to_map() if k else None)
        if self.metrics_status is not None:
            result['MetricsStatus'] = self.metrics_status.to_map()
        if self.min_replicas is not None:
            result['MinReplicas'] = self.min_replicas
        if self.scale_down_rules is not None:
            result['ScaleDownRules'] = self.scale_down_rules.to_map()
        if self.scale_up_rules is not None:
            result['ScaleUpRules'] = self.scale_up_rules.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxReplicas') is not None:
            self.max_replicas = m.get('MaxReplicas')
        self.metrics = []
        if m.get('Metrics') is not None:
            for k in m.get('Metrics'):
                temp_model = DescribeApplicationScalingRulesResponseBodyDataApplicationScalingRulesMetricMetrics()
                self.metrics.append(temp_model.from_map(k))
        if m.get('MetricsStatus') is not None:
            temp_model = DescribeApplicationScalingRulesResponseBodyDataApplicationScalingRulesMetricMetricsStatus()
            self.metrics_status = temp_model.from_map(m['MetricsStatus'])
        if m.get('MinReplicas') is not None:
            self.min_replicas = m.get('MinReplicas')
        if m.get('ScaleDownRules') is not None:
            temp_model = DescribeApplicationScalingRulesResponseBodyDataApplicationScalingRulesMetricScaleDownRules()
            self.scale_down_rules = temp_model.from_map(m['ScaleDownRules'])
        if m.get('ScaleUpRules') is not None:
            temp_model = DescribeApplicationScalingRulesResponseBodyDataApplicationScalingRulesMetricScaleUpRules()
            self.scale_up_rules = temp_model.from_map(m['ScaleUpRules'])
        return self


class DescribeApplicationScalingRulesResponseBodyDataApplicationScalingRulesTimerSchedules(TeaModel):
    def __init__(
        self,
        at_time: str = None,
        max_replicas: int = None,
        min_replicas: int = None,
        target_replicas: int = None,
    ):
        self.at_time = at_time
        self.max_replicas = max_replicas
        self.min_replicas = min_replicas
        self.target_replicas = target_replicas

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.at_time is not None:
            result['AtTime'] = self.at_time
        if self.max_replicas is not None:
            result['MaxReplicas'] = self.max_replicas
        if self.min_replicas is not None:
            result['MinReplicas'] = self.min_replicas
        if self.target_replicas is not None:
            result['TargetReplicas'] = self.target_replicas
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AtTime') is not None:
            self.at_time = m.get('AtTime')
        if m.get('MaxReplicas') is not None:
            self.max_replicas = m.get('MaxReplicas')
        if m.get('MinReplicas') is not None:
            self.min_replicas = m.get('MinReplicas')
        if m.get('TargetReplicas') is not None:
            self.target_replicas = m.get('TargetReplicas')
        return self


class DescribeApplicationScalingRulesResponseBodyDataApplicationScalingRulesTimer(TeaModel):
    def __init__(
        self,
        begin_date: str = None,
        end_date: str = None,
        period: str = None,
        schedules: List[DescribeApplicationScalingRulesResponseBodyDataApplicationScalingRulesTimerSchedules] = None,
    ):
        self.begin_date = begin_date
        self.end_date = end_date
        self.period = period
        self.schedules = schedules

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
        if self.begin_date is not None:
            result['BeginDate'] = self.begin_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.period is not None:
            result['Period'] = self.period
        result['Schedules'] = []
        if self.schedules is not None:
            for k in self.schedules:
                result['Schedules'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginDate') is not None:
            self.begin_date = m.get('BeginDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        self.schedules = []
        if m.get('Schedules') is not None:
            for k in m.get('Schedules'):
                temp_model = DescribeApplicationScalingRulesResponseBodyDataApplicationScalingRulesTimerSchedules()
                self.schedules.append(temp_model.from_map(k))
        return self


class DescribeApplicationScalingRulesResponseBodyDataApplicationScalingRules(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        create_time: int = None,
        last_disable_time: int = None,
        metric: DescribeApplicationScalingRulesResponseBodyDataApplicationScalingRulesMetric = None,
        scale_rule_enabled: bool = None,
        scale_rule_name: str = None,
        scale_rule_type: str = None,
        timer: DescribeApplicationScalingRulesResponseBodyDataApplicationScalingRulesTimer = None,
        update_time: int = None,
    ):
        self.app_id = app_id
        self.create_time = create_time
        self.last_disable_time = last_disable_time
        self.metric = metric
        self.scale_rule_enabled = scale_rule_enabled
        self.scale_rule_name = scale_rule_name
        self.scale_rule_type = scale_rule_type
        self.timer = timer
        self.update_time = update_time

    def validate(self):
        if self.metric:
            self.metric.validate()
        if self.timer:
            self.timer.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.last_disable_time is not None:
            result['LastDisableTime'] = self.last_disable_time
        if self.metric is not None:
            result['Metric'] = self.metric.to_map()
        if self.scale_rule_enabled is not None:
            result['ScaleRuleEnabled'] = self.scale_rule_enabled
        if self.scale_rule_name is not None:
            result['ScaleRuleName'] = self.scale_rule_name
        if self.scale_rule_type is not None:
            result['ScaleRuleType'] = self.scale_rule_type
        if self.timer is not None:
            result['Timer'] = self.timer.to_map()
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('LastDisableTime') is not None:
            self.last_disable_time = m.get('LastDisableTime')
        if m.get('Metric') is not None:
            temp_model = DescribeApplicationScalingRulesResponseBodyDataApplicationScalingRulesMetric()
            self.metric = temp_model.from_map(m['Metric'])
        if m.get('ScaleRuleEnabled') is not None:
            self.scale_rule_enabled = m.get('ScaleRuleEnabled')
        if m.get('ScaleRuleName') is not None:
            self.scale_rule_name = m.get('ScaleRuleName')
        if m.get('ScaleRuleType') is not None:
            self.scale_rule_type = m.get('ScaleRuleType')
        if m.get('Timer') is not None:
            temp_model = DescribeApplicationScalingRulesResponseBodyDataApplicationScalingRulesTimer()
            self.timer = temp_model.from_map(m['Timer'])
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class DescribeApplicationScalingRulesResponseBodyData(TeaModel):
    def __init__(
        self,
        application_scaling_rules: List[DescribeApplicationScalingRulesResponseBodyDataApplicationScalingRules] = None,
        current_page: int = None,
        page_size: int = None,
        total_size: int = None,
    ):
        self.application_scaling_rules = application_scaling_rules
        self.current_page = current_page
        self.page_size = page_size
        self.total_size = total_size

    def validate(self):
        if self.application_scaling_rules:
            for k in self.application_scaling_rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ApplicationScalingRules'] = []
        if self.application_scaling_rules is not None:
            for k in self.application_scaling_rules:
                result['ApplicationScalingRules'].append(k.to_map() if k else None)
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_size is not None:
            result['TotalSize'] = self.total_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.application_scaling_rules = []
        if m.get('ApplicationScalingRules') is not None:
            for k in m.get('ApplicationScalingRules'):
                temp_model = DescribeApplicationScalingRulesResponseBodyDataApplicationScalingRules()
                self.application_scaling_rules.append(temp_model.from_map(k))
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalSize') is not None:
            self.total_size = m.get('TotalSize')
        return self


class DescribeApplicationScalingRulesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: DescribeApplicationScalingRulesResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = DescribeApplicationScalingRulesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class DescribeApplicationScalingRulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeApplicationScalingRulesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DescribeApplicationScalingRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeApplicationSlbsRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
    ):
        self.app_id = app_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        return self


class DescribeApplicationSlbsResponseBodyDataInternet(TeaModel):
    def __init__(
        self,
        https_cert_id: str = None,
        port: int = None,
        protocol: str = None,
        target_port: int = None,
    ):
        self.https_cert_id = https_cert_id
        self.port = port
        self.protocol = protocol
        self.target_port = target_port

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.https_cert_id is not None:
            result['HttpsCertId'] = self.https_cert_id
        if self.port is not None:
            result['Port'] = self.port
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.target_port is not None:
            result['TargetPort'] = self.target_port
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HttpsCertId') is not None:
            self.https_cert_id = m.get('HttpsCertId')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('TargetPort') is not None:
            self.target_port = m.get('TargetPort')
        return self


class DescribeApplicationSlbsResponseBodyDataIntranet(TeaModel):
    def __init__(
        self,
        https_cert_id: str = None,
        port: int = None,
        protocol: str = None,
        target_port: int = None,
    ):
        self.https_cert_id = https_cert_id
        self.port = port
        self.protocol = protocol
        self.target_port = target_port

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.https_cert_id is not None:
            result['HttpsCertId'] = self.https_cert_id
        if self.port is not None:
            result['Port'] = self.port
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.target_port is not None:
            result['TargetPort'] = self.target_port
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HttpsCertId') is not None:
            self.https_cert_id = m.get('HttpsCertId')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('TargetPort') is not None:
            self.target_port = m.get('TargetPort')
        return self


class DescribeApplicationSlbsResponseBodyData(TeaModel):
    def __init__(
        self,
        internet: List[DescribeApplicationSlbsResponseBodyDataInternet] = None,
        internet_ip: str = None,
        internet_slb_expired: bool = None,
        internet_slb_id: str = None,
        intranet: List[DescribeApplicationSlbsResponseBodyDataIntranet] = None,
        intranet_ip: str = None,
        intranet_slb_expired: bool = None,
        intranet_slb_id: str = None,
    ):
        self.internet = internet
        self.internet_ip = internet_ip
        self.internet_slb_expired = internet_slb_expired
        self.internet_slb_id = internet_slb_id
        self.intranet = intranet
        self.intranet_ip = intranet_ip
        self.intranet_slb_expired = intranet_slb_expired
        self.intranet_slb_id = intranet_slb_id

    def validate(self):
        if self.internet:
            for k in self.internet:
                if k:
                    k.validate()
        if self.intranet:
            for k in self.intranet:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Internet'] = []
        if self.internet is not None:
            for k in self.internet:
                result['Internet'].append(k.to_map() if k else None)
        if self.internet_ip is not None:
            result['InternetIp'] = self.internet_ip
        if self.internet_slb_expired is not None:
            result['InternetSlbExpired'] = self.internet_slb_expired
        if self.internet_slb_id is not None:
            result['InternetSlbId'] = self.internet_slb_id
        result['Intranet'] = []
        if self.intranet is not None:
            for k in self.intranet:
                result['Intranet'].append(k.to_map() if k else None)
        if self.intranet_ip is not None:
            result['IntranetIp'] = self.intranet_ip
        if self.intranet_slb_expired is not None:
            result['IntranetSlbExpired'] = self.intranet_slb_expired
        if self.intranet_slb_id is not None:
            result['IntranetSlbId'] = self.intranet_slb_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.internet = []
        if m.get('Internet') is not None:
            for k in m.get('Internet'):
                temp_model = DescribeApplicationSlbsResponseBodyDataInternet()
                self.internet.append(temp_model.from_map(k))
        if m.get('InternetIp') is not None:
            self.internet_ip = m.get('InternetIp')
        if m.get('InternetSlbExpired') is not None:
            self.internet_slb_expired = m.get('InternetSlbExpired')
        if m.get('InternetSlbId') is not None:
            self.internet_slb_id = m.get('InternetSlbId')
        self.intranet = []
        if m.get('Intranet') is not None:
            for k in m.get('Intranet'):
                temp_model = DescribeApplicationSlbsResponseBodyDataIntranet()
                self.intranet.append(temp_model.from_map(k))
        if m.get('IntranetIp') is not None:
            self.intranet_ip = m.get('IntranetIp')
        if m.get('IntranetSlbExpired') is not None:
            self.intranet_slb_expired = m.get('IntranetSlbExpired')
        if m.get('IntranetSlbId') is not None:
            self.intranet_slb_id = m.get('IntranetSlbId')
        return self


class DescribeApplicationSlbsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: DescribeApplicationSlbsResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = DescribeApplicationSlbsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class DescribeApplicationSlbsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeApplicationSlbsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DescribeApplicationSlbsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeApplicationStatusRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
    ):
        self.app_id = app_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        return self


class DescribeApplicationStatusResponseBodyData(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        arms_advanced_enabled: str = None,
        arms_apm_info: str = None,
        create_time: str = None,
        current_status: str = None,
        enable_agent: bool = None,
        file_size_limit: int = None,
        last_change_order_id: str = None,
        last_change_order_running: bool = None,
        last_change_order_status: str = None,
        running_instances: int = None,
        sub_status: str = None,
    ):
        self.app_id = app_id
        self.arms_advanced_enabled = arms_advanced_enabled
        self.arms_apm_info = arms_apm_info
        self.create_time = create_time
        self.current_status = current_status
        self.enable_agent = enable_agent
        self.file_size_limit = file_size_limit
        self.last_change_order_id = last_change_order_id
        self.last_change_order_running = last_change_order_running
        self.last_change_order_status = last_change_order_status
        self.running_instances = running_instances
        self.sub_status = sub_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.arms_advanced_enabled is not None:
            result['ArmsAdvancedEnabled'] = self.arms_advanced_enabled
        if self.arms_apm_info is not None:
            result['ArmsApmInfo'] = self.arms_apm_info
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.current_status is not None:
            result['CurrentStatus'] = self.current_status
        if self.enable_agent is not None:
            result['EnableAgent'] = self.enable_agent
        if self.file_size_limit is not None:
            result['FileSizeLimit'] = self.file_size_limit
        if self.last_change_order_id is not None:
            result['LastChangeOrderId'] = self.last_change_order_id
        if self.last_change_order_running is not None:
            result['LastChangeOrderRunning'] = self.last_change_order_running
        if self.last_change_order_status is not None:
            result['LastChangeOrderStatus'] = self.last_change_order_status
        if self.running_instances is not None:
            result['RunningInstances'] = self.running_instances
        if self.sub_status is not None:
            result['SubStatus'] = self.sub_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ArmsAdvancedEnabled') is not None:
            self.arms_advanced_enabled = m.get('ArmsAdvancedEnabled')
        if m.get('ArmsApmInfo') is not None:
            self.arms_apm_info = m.get('ArmsApmInfo')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CurrentStatus') is not None:
            self.current_status = m.get('CurrentStatus')
        if m.get('EnableAgent') is not None:
            self.enable_agent = m.get('EnableAgent')
        if m.get('FileSizeLimit') is not None:
            self.file_size_limit = m.get('FileSizeLimit')
        if m.get('LastChangeOrderId') is not None:
            self.last_change_order_id = m.get('LastChangeOrderId')
        if m.get('LastChangeOrderRunning') is not None:
            self.last_change_order_running = m.get('LastChangeOrderRunning')
        if m.get('LastChangeOrderStatus') is not None:
            self.last_change_order_status = m.get('LastChangeOrderStatus')
        if m.get('RunningInstances') is not None:
            self.running_instances = m.get('RunningInstances')
        if m.get('SubStatus') is not None:
            self.sub_status = m.get('SubStatus')
        return self


class DescribeApplicationStatusResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: DescribeApplicationStatusResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = DescribeApplicationStatusResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class DescribeApplicationStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeApplicationStatusResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DescribeApplicationStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeChangeOrderRequest(TeaModel):
    def __init__(
        self,
        change_order_id: str = None,
    ):
        self.change_order_id = change_order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.change_order_id is not None:
            result['ChangeOrderId'] = self.change_order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChangeOrderId') is not None:
            self.change_order_id = m.get('ChangeOrderId')
        return self


class DescribeChangeOrderResponseBodyDataPipelines(TeaModel):
    def __init__(
        self,
        batch_type: int = None,
        parallel_count: int = None,
        pipeline_id: str = None,
        pipeline_name: str = None,
        start_time: int = None,
        status: int = None,
        update_time: int = None,
    ):
        self.batch_type = batch_type
        self.parallel_count = parallel_count
        self.pipeline_id = pipeline_id
        self.pipeline_name = pipeline_name
        self.start_time = start_time
        self.status = status
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.batch_type is not None:
            result['BatchType'] = self.batch_type
        if self.parallel_count is not None:
            result['ParallelCount'] = self.parallel_count
        if self.pipeline_id is not None:
            result['PipelineId'] = self.pipeline_id
        if self.pipeline_name is not None:
            result['PipelineName'] = self.pipeline_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BatchType') is not None:
            self.batch_type = m.get('BatchType')
        if m.get('ParallelCount') is not None:
            self.parallel_count = m.get('ParallelCount')
        if m.get('PipelineId') is not None:
            self.pipeline_id = m.get('PipelineId')
        if m.get('PipelineName') is not None:
            self.pipeline_name = m.get('PipelineName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class DescribeChangeOrderResponseBodyData(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        app_name: str = None,
        approval_id: str = None,
        auto: bool = None,
        batch_count: int = None,
        batch_type: str = None,
        batch_wait_time: int = None,
        change_order_id: str = None,
        co_type: str = None,
        co_type_code: str = None,
        create_time: str = None,
        current_pipeline_id: str = None,
        description: str = None,
        error_message: str = None,
        pipelines: List[DescribeChangeOrderResponseBodyDataPipelines] = None,
        status: int = None,
        sub_status: int = None,
        support_rollback: bool = None,
    ):
        self.app_id = app_id
        self.app_name = app_name
        self.approval_id = approval_id
        self.auto = auto
        self.batch_count = batch_count
        self.batch_type = batch_type
        self.batch_wait_time = batch_wait_time
        self.change_order_id = change_order_id
        self.co_type = co_type
        self.co_type_code = co_type_code
        self.create_time = create_time
        self.current_pipeline_id = current_pipeline_id
        self.description = description
        self.error_message = error_message
        self.pipelines = pipelines
        self.status = status
        self.sub_status = sub_status
        self.support_rollback = support_rollback

    def validate(self):
        if self.pipelines:
            for k in self.pipelines:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.approval_id is not None:
            result['ApprovalId'] = self.approval_id
        if self.auto is not None:
            result['Auto'] = self.auto
        if self.batch_count is not None:
            result['BatchCount'] = self.batch_count
        if self.batch_type is not None:
            result['BatchType'] = self.batch_type
        if self.batch_wait_time is not None:
            result['BatchWaitTime'] = self.batch_wait_time
        if self.change_order_id is not None:
            result['ChangeOrderId'] = self.change_order_id
        if self.co_type is not None:
            result['CoType'] = self.co_type
        if self.co_type_code is not None:
            result['CoTypeCode'] = self.co_type_code
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.current_pipeline_id is not None:
            result['CurrentPipelineId'] = self.current_pipeline_id
        if self.description is not None:
            result['Description'] = self.description
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        result['Pipelines'] = []
        if self.pipelines is not None:
            for k in self.pipelines:
                result['Pipelines'].append(k.to_map() if k else None)
        if self.status is not None:
            result['Status'] = self.status
        if self.sub_status is not None:
            result['SubStatus'] = self.sub_status
        if self.support_rollback is not None:
            result['SupportRollback'] = self.support_rollback
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('ApprovalId') is not None:
            self.approval_id = m.get('ApprovalId')
        if m.get('Auto') is not None:
            self.auto = m.get('Auto')
        if m.get('BatchCount') is not None:
            self.batch_count = m.get('BatchCount')
        if m.get('BatchType') is not None:
            self.batch_type = m.get('BatchType')
        if m.get('BatchWaitTime') is not None:
            self.batch_wait_time = m.get('BatchWaitTime')
        if m.get('ChangeOrderId') is not None:
            self.change_order_id = m.get('ChangeOrderId')
        if m.get('CoType') is not None:
            self.co_type = m.get('CoType')
        if m.get('CoTypeCode') is not None:
            self.co_type_code = m.get('CoTypeCode')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CurrentPipelineId') is not None:
            self.current_pipeline_id = m.get('CurrentPipelineId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        self.pipelines = []
        if m.get('Pipelines') is not None:
            for k in m.get('Pipelines'):
                temp_model = DescribeChangeOrderResponseBodyDataPipelines()
                self.pipelines.append(temp_model.from_map(k))
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubStatus') is not None:
            self.sub_status = m.get('SubStatus')
        if m.get('SupportRollback') is not None:
            self.support_rollback = m.get('SupportRollback')
        return self


class DescribeChangeOrderResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: DescribeChangeOrderResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = DescribeChangeOrderResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class DescribeChangeOrderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeChangeOrderResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DescribeChangeOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeComponentsRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        type: str = None,
    ):
        self.app_id = app_id
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeComponentsResponseBodyData(TeaModel):
    def __init__(
        self,
        component_description: str = None,
        component_key: str = None,
        expired: bool = None,
        type: str = None,
    ):
        self.component_description = component_description
        self.component_key = component_key
        self.expired = expired
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.component_description is not None:
            result['ComponentDescription'] = self.component_description
        if self.component_key is not None:
            result['ComponentKey'] = self.component_key
        if self.expired is not None:
            result['Expired'] = self.expired
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComponentDescription') is not None:
            self.component_description = m.get('ComponentDescription')
        if m.get('ComponentKey') is not None:
            self.component_key = m.get('ComponentKey')
        if m.get('Expired') is not None:
            self.expired = m.get('Expired')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeComponentsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[DescribeComponentsResponseBodyData] = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = DescribeComponentsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class DescribeComponentsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeComponentsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DescribeComponentsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeConfigMapRequest(TeaModel):
    def __init__(
        self,
        config_map_id: int = None,
    ):
        self.config_map_id = config_map_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_map_id is not None:
            result['ConfigMapId'] = self.config_map_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigMapId') is not None:
            self.config_map_id = m.get('ConfigMapId')
        return self


class DescribeConfigMapResponseBodyDataRelateApps(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        app_name: str = None,
    ):
        self.app_id = app_id
        self.app_name = app_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        return self


class DescribeConfigMapResponseBodyData(TeaModel):
    def __init__(
        self,
        config_map_id: int = None,
        create_time: int = None,
        data: Dict[str, Any] = None,
        description: str = None,
        name: str = None,
        namespace_id: str = None,
        relate_apps: List[DescribeConfigMapResponseBodyDataRelateApps] = None,
        update_time: int = None,
    ):
        self.config_map_id = config_map_id
        self.create_time = create_time
        self.data = data
        self.description = description
        self.name = name
        self.namespace_id = namespace_id
        self.relate_apps = relate_apps
        self.update_time = update_time

    def validate(self):
        if self.relate_apps:
            for k in self.relate_apps:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_map_id is not None:
            result['ConfigMapId'] = self.config_map_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.data is not None:
            result['Data'] = self.data
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        result['RelateApps'] = []
        if self.relate_apps is not None:
            for k in self.relate_apps:
                result['RelateApps'].append(k.to_map() if k else None)
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigMapId') is not None:
            self.config_map_id = m.get('ConfigMapId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        self.relate_apps = []
        if m.get('RelateApps') is not None:
            for k in m.get('RelateApps'):
                temp_model = DescribeConfigMapResponseBodyDataRelateApps()
                self.relate_apps.append(temp_model.from_map(k))
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class DescribeConfigMapResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: DescribeConfigMapResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = DescribeConfigMapResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class DescribeConfigMapResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeConfigMapResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DescribeConfigMapResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeConfigurationPriceRequest(TeaModel):
    def __init__(
        self,
        cpu: int = None,
        memory: int = None,
        workload: str = None,
    ):
        self.cpu = cpu
        self.memory = memory
        self.workload = workload

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.workload is not None:
            result['Workload'] = self.workload
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('Workload') is not None:
            self.workload = m.get('Workload')
        return self


class DescribeConfigurationPriceResponseBodyDataBagUsage(TeaModel):
    def __init__(
        self,
        cpu: float = None,
        mem: float = None,
    ):
        self.cpu = cpu
        self.mem = mem

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.mem is not None:
            result['Mem'] = self.mem
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('Mem') is not None:
            self.mem = m.get('Mem')
        return self


class DescribeConfigurationPriceResponseBodyDataOrder(TeaModel):
    def __init__(
        self,
        discount_amount: float = None,
        original_amount: float = None,
        rule_ids: List[str] = None,
        trade_amount: float = None,
    ):
        self.discount_amount = discount_amount
        self.original_amount = original_amount
        self.rule_ids = rule_ids
        self.trade_amount = trade_amount

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.discount_amount is not None:
            result['DiscountAmount'] = self.discount_amount
        if self.original_amount is not None:
            result['OriginalAmount'] = self.original_amount
        if self.rule_ids is not None:
            result['RuleIds'] = self.rule_ids
        if self.trade_amount is not None:
            result['TradeAmount'] = self.trade_amount
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiscountAmount') is not None:
            self.discount_amount = m.get('DiscountAmount')
        if m.get('OriginalAmount') is not None:
            self.original_amount = m.get('OriginalAmount')
        if m.get('RuleIds') is not None:
            self.rule_ids = m.get('RuleIds')
        if m.get('TradeAmount') is not None:
            self.trade_amount = m.get('TradeAmount')
        return self


class DescribeConfigurationPriceResponseBodyDataRules(TeaModel):
    def __init__(
        self,
        name: str = None,
        rule_desc_id: int = None,
    ):
        self.name = name
        self.rule_desc_id = rule_desc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.rule_desc_id is not None:
            result['RuleDescId'] = self.rule_desc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RuleDescId') is not None:
            self.rule_desc_id = m.get('RuleDescId')
        return self


class DescribeConfigurationPriceResponseBodyData(TeaModel):
    def __init__(
        self,
        bag_usage: DescribeConfigurationPriceResponseBodyDataBagUsage = None,
        order: DescribeConfigurationPriceResponseBodyDataOrder = None,
        rules: List[DescribeConfigurationPriceResponseBodyDataRules] = None,
    ):
        self.bag_usage = bag_usage
        self.order = order
        self.rules = rules

    def validate(self):
        if self.bag_usage:
            self.bag_usage.validate()
        if self.order:
            self.order.validate()
        if self.rules:
            for k in self.rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bag_usage is not None:
            result['BagUsage'] = self.bag_usage.to_map()
        if self.order is not None:
            result['Order'] = self.order.to_map()
        result['Rules'] = []
        if self.rules is not None:
            for k in self.rules:
                result['Rules'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BagUsage') is not None:
            temp_model = DescribeConfigurationPriceResponseBodyDataBagUsage()
            self.bag_usage = temp_model.from_map(m['BagUsage'])
        if m.get('Order') is not None:
            temp_model = DescribeConfigurationPriceResponseBodyDataOrder()
            self.order = temp_model.from_map(m['Order'])
        self.rules = []
        if m.get('Rules') is not None:
            for k in m.get('Rules'):
                temp_model = DescribeConfigurationPriceResponseBodyDataRules()
                self.rules.append(temp_model.from_map(k))
        return self


class DescribeConfigurationPriceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: DescribeConfigurationPriceResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = DescribeConfigurationPriceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class DescribeConfigurationPriceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeConfigurationPriceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DescribeConfigurationPriceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeEdasContainersResponseBodyData(TeaModel):
    def __init__(
        self,
        disabled: bool = None,
        edas_container_version: str = None,
    ):
        self.disabled = disabled
        self.edas_container_version = edas_container_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.disabled is not None:
            result['Disabled'] = self.disabled
        if self.edas_container_version is not None:
            result['EdasContainerVersion'] = self.edas_container_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Disabled') is not None:
            self.disabled = m.get('Disabled')
        if m.get('EdasContainerVersion') is not None:
            self.edas_container_version = m.get('EdasContainerVersion')
        return self


class DescribeEdasContainersResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[DescribeEdasContainersResponseBodyData] = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = DescribeEdasContainersResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class DescribeEdasContainersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeEdasContainersResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DescribeEdasContainersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeGreyTagRouteRequest(TeaModel):
    def __init__(
        self,
        grey_tag_route_id: int = None,
    ):
        self.grey_tag_route_id = grey_tag_route_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.grey_tag_route_id is not None:
            result['GreyTagRouteId'] = self.grey_tag_route_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GreyTagRouteId') is not None:
            self.grey_tag_route_id = m.get('GreyTagRouteId')
        return self


class DescribeGreyTagRouteResponseBodyDataAlbRulesItems(TeaModel):
    def __init__(
        self,
        cond: str = None,
        expr: str = None,
        index: int = None,
        name: str = None,
        operator: str = None,
        type: str = None,
        value: str = None,
    ):
        self.cond = cond
        self.expr = expr
        self.index = index
        self.name = name
        self.operator = operator
        self.type = type
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cond is not None:
            result['cond'] = self.cond
        if self.expr is not None:
            result['expr'] = self.expr
        if self.index is not None:
            result['index'] = self.index
        if self.name is not None:
            result['name'] = self.name
        if self.operator is not None:
            result['operator'] = self.operator
        if self.type is not None:
            result['type'] = self.type
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cond') is not None:
            self.cond = m.get('cond')
        if m.get('expr') is not None:
            self.expr = m.get('expr')
        if m.get('index') is not None:
            self.index = m.get('index')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('operator') is not None:
            self.operator = m.get('operator')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class DescribeGreyTagRouteResponseBodyDataAlbRules(TeaModel):
    def __init__(
        self,
        condition: str = None,
        ingress_id: str = None,
        items: List[DescribeGreyTagRouteResponseBodyDataAlbRulesItems] = None,
        service_id: str = None,
    ):
        self.condition = condition
        self.ingress_id = ingress_id
        self.items = items
        self.service_id = service_id

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.condition is not None:
            result['condition'] = self.condition
        if self.ingress_id is not None:
            result['ingressId'] = self.ingress_id
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        if self.service_id is not None:
            result['serviceId'] = self.service_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('condition') is not None:
            self.condition = m.get('condition')
        if m.get('ingressId') is not None:
            self.ingress_id = m.get('ingressId')
        self.items = []
        if m.get('items') is not None:
            for k in m.get('items'):
                temp_model = DescribeGreyTagRouteResponseBodyDataAlbRulesItems()
                self.items.append(temp_model.from_map(k))
        if m.get('serviceId') is not None:
            self.service_id = m.get('serviceId')
        return self


class DescribeGreyTagRouteResponseBodyDataDubboRulesItems(TeaModel):
    def __init__(
        self,
        cond: str = None,
        expr: str = None,
        index: int = None,
        name: str = None,
        operator: str = None,
        type: str = None,
        value: str = None,
    ):
        self.cond = cond
        self.expr = expr
        self.index = index
        self.name = name
        self.operator = operator
        self.type = type
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cond is not None:
            result['cond'] = self.cond
        if self.expr is not None:
            result['expr'] = self.expr
        if self.index is not None:
            result['index'] = self.index
        if self.name is not None:
            result['name'] = self.name
        if self.operator is not None:
            result['operator'] = self.operator
        if self.type is not None:
            result['type'] = self.type
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cond') is not None:
            self.cond = m.get('cond')
        if m.get('expr') is not None:
            self.expr = m.get('expr')
        if m.get('index') is not None:
            self.index = m.get('index')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('operator') is not None:
            self.operator = m.get('operator')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class DescribeGreyTagRouteResponseBodyDataDubboRules(TeaModel):
    def __init__(
        self,
        condition: str = None,
        group: str = None,
        items: List[DescribeGreyTagRouteResponseBodyDataDubboRulesItems] = None,
        method_name: str = None,
        service_name: str = None,
        version: str = None,
    ):
        self.condition = condition
        self.group = group
        self.items = items
        self.method_name = method_name
        self.service_name = service_name
        self.version = version

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.condition is not None:
            result['condition'] = self.condition
        if self.group is not None:
            result['group'] = self.group
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        if self.method_name is not None:
            result['methodName'] = self.method_name
        if self.service_name is not None:
            result['serviceName'] = self.service_name
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('condition') is not None:
            self.condition = m.get('condition')
        if m.get('group') is not None:
            self.group = m.get('group')
        self.items = []
        if m.get('items') is not None:
            for k in m.get('items'):
                temp_model = DescribeGreyTagRouteResponseBodyDataDubboRulesItems()
                self.items.append(temp_model.from_map(k))
        if m.get('methodName') is not None:
            self.method_name = m.get('methodName')
        if m.get('serviceName') is not None:
            self.service_name = m.get('serviceName')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class DescribeGreyTagRouteResponseBodyDataScRulesItems(TeaModel):
    def __init__(
        self,
        cond: str = None,
        expr: str = None,
        index: int = None,
        name: str = None,
        operator: str = None,
        type: str = None,
        value: str = None,
    ):
        self.cond = cond
        self.expr = expr
        self.index = index
        self.name = name
        self.operator = operator
        self.type = type
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cond is not None:
            result['cond'] = self.cond
        if self.expr is not None:
            result['expr'] = self.expr
        if self.index is not None:
            result['index'] = self.index
        if self.name is not None:
            result['name'] = self.name
        if self.operator is not None:
            result['operator'] = self.operator
        if self.type is not None:
            result['type'] = self.type
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cond') is not None:
            self.cond = m.get('cond')
        if m.get('expr') is not None:
            self.expr = m.get('expr')
        if m.get('index') is not None:
            self.index = m.get('index')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('operator') is not None:
            self.operator = m.get('operator')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class DescribeGreyTagRouteResponseBodyDataScRules(TeaModel):
    def __init__(
        self,
        condition: str = None,
        items: List[DescribeGreyTagRouteResponseBodyDataScRulesItems] = None,
        path: str = None,
    ):
        self.condition = condition
        self.items = items
        self.path = path

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.condition is not None:
            result['condition'] = self.condition
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        if self.path is not None:
            result['path'] = self.path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('condition') is not None:
            self.condition = m.get('condition')
        self.items = []
        if m.get('items') is not None:
            for k in m.get('items'):
                temp_model = DescribeGreyTagRouteResponseBodyDataScRulesItems()
                self.items.append(temp_model.from_map(k))
        if m.get('path') is not None:
            self.path = m.get('path')
        return self


class DescribeGreyTagRouteResponseBodyData(TeaModel):
    def __init__(
        self,
        alb_rules: List[DescribeGreyTagRouteResponseBodyDataAlbRules] = None,
        app_id: str = None,
        create_time: int = None,
        description: str = None,
        dubbo_rules: List[DescribeGreyTagRouteResponseBodyDataDubboRules] = None,
        grey_tag_route_id: int = None,
        name: str = None,
        sc_rules: List[DescribeGreyTagRouteResponseBodyDataScRules] = None,
        update_time: int = None,
    ):
        self.alb_rules = alb_rules
        self.app_id = app_id
        self.create_time = create_time
        self.description = description
        self.dubbo_rules = dubbo_rules
        self.grey_tag_route_id = grey_tag_route_id
        self.name = name
        self.sc_rules = sc_rules
        self.update_time = update_time

    def validate(self):
        if self.alb_rules:
            for k in self.alb_rules:
                if k:
                    k.validate()
        if self.dubbo_rules:
            for k in self.dubbo_rules:
                if k:
                    k.validate()
        if self.sc_rules:
            for k in self.sc_rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AlbRules'] = []
        if self.alb_rules is not None:
            for k in self.alb_rules:
                result['AlbRules'].append(k.to_map() if k else None)
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        result['DubboRules'] = []
        if self.dubbo_rules is not None:
            for k in self.dubbo_rules:
                result['DubboRules'].append(k.to_map() if k else None)
        if self.grey_tag_route_id is not None:
            result['GreyTagRouteId'] = self.grey_tag_route_id
        if self.name is not None:
            result['Name'] = self.name
        result['ScRules'] = []
        if self.sc_rules is not None:
            for k in self.sc_rules:
                result['ScRules'].append(k.to_map() if k else None)
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.alb_rules = []
        if m.get('AlbRules') is not None:
            for k in m.get('AlbRules'):
                temp_model = DescribeGreyTagRouteResponseBodyDataAlbRules()
                self.alb_rules.append(temp_model.from_map(k))
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        self.dubbo_rules = []
        if m.get('DubboRules') is not None:
            for k in m.get('DubboRules'):
                temp_model = DescribeGreyTagRouteResponseBodyDataDubboRules()
                self.dubbo_rules.append(temp_model.from_map(k))
        if m.get('GreyTagRouteId') is not None:
            self.grey_tag_route_id = m.get('GreyTagRouteId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        self.sc_rules = []
        if m.get('ScRules') is not None:
            for k in m.get('ScRules'):
                temp_model = DescribeGreyTagRouteResponseBodyDataScRules()
                self.sc_rules.append(temp_model.from_map(k))
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class DescribeGreyTagRouteResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: DescribeGreyTagRouteResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = DescribeGreyTagRouteResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class DescribeGreyTagRouteResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeGreyTagRouteResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DescribeGreyTagRouteResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeIngressRequest(TeaModel):
    def __init__(
        self,
        ingress_id: int = None,
    ):
        self.ingress_id = ingress_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ingress_id is not None:
            result['IngressId'] = self.ingress_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IngressId') is not None:
            self.ingress_id = m.get('IngressId')
        return self


class DescribeIngressResponseBodyDataDefaultRule(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        app_name: str = None,
        backend_protocol: str = None,
        container_port: int = None,
    ):
        self.app_id = app_id
        self.app_name = app_name
        self.backend_protocol = backend_protocol
        self.container_port = container_port

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.backend_protocol is not None:
            result['BackendProtocol'] = self.backend_protocol
        if self.container_port is not None:
            result['ContainerPort'] = self.container_port
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('BackendProtocol') is not None:
            self.backend_protocol = m.get('BackendProtocol')
        if m.get('ContainerPort') is not None:
            self.container_port = m.get('ContainerPort')
        return self


class DescribeIngressResponseBodyDataRules(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        app_name: str = None,
        backend_protocol: str = None,
        container_port: int = None,
        domain: str = None,
        path: str = None,
    ):
        self.app_id = app_id
        self.app_name = app_name
        self.backend_protocol = backend_protocol
        self.container_port = container_port
        self.domain = domain
        self.path = path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.backend_protocol is not None:
            result['BackendProtocol'] = self.backend_protocol
        if self.container_port is not None:
            result['ContainerPort'] = self.container_port
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.path is not None:
            result['Path'] = self.path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('BackendProtocol') is not None:
            self.backend_protocol = m.get('BackendProtocol')
        if m.get('ContainerPort') is not None:
            self.container_port = m.get('ContainerPort')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        return self


class DescribeIngressResponseBodyData(TeaModel):
    def __init__(
        self,
        cert_id: str = None,
        cert_ids: str = None,
        default_rule: DescribeIngressResponseBodyDataDefaultRule = None,
        description: str = None,
        id: int = None,
        listener_port: int = None,
        listener_protocol: str = None,
        load_balance_type: str = None,
        name: str = None,
        namespace_id: str = None,
        rules: List[DescribeIngressResponseBodyDataRules] = None,
        slb_id: str = None,
        slb_type: str = None,
    ):
        self.cert_id = cert_id
        self.cert_ids = cert_ids
        self.default_rule = default_rule
        self.description = description
        self.id = id
        self.listener_port = listener_port
        self.listener_protocol = listener_protocol
        self.load_balance_type = load_balance_type
        self.name = name
        self.namespace_id = namespace_id
        self.rules = rules
        # SLB ID。
        self.slb_id = slb_id
        self.slb_type = slb_type

    def validate(self):
        if self.default_rule:
            self.default_rule.validate()
        if self.rules:
            for k in self.rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_id is not None:
            result['CertId'] = self.cert_id
        if self.cert_ids is not None:
            result['CertIds'] = self.cert_ids
        if self.default_rule is not None:
            result['DefaultRule'] = self.default_rule.to_map()
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port
        if self.listener_protocol is not None:
            result['ListenerProtocol'] = self.listener_protocol
        if self.load_balance_type is not None:
            result['LoadBalanceType'] = self.load_balance_type
        if self.name is not None:
            result['Name'] = self.name
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        result['Rules'] = []
        if self.rules is not None:
            for k in self.rules:
                result['Rules'].append(k.to_map() if k else None)
        if self.slb_id is not None:
            result['SlbId'] = self.slb_id
        if self.slb_type is not None:
            result['SlbType'] = self.slb_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertId') is not None:
            self.cert_id = m.get('CertId')
        if m.get('CertIds') is not None:
            self.cert_ids = m.get('CertIds')
        if m.get('DefaultRule') is not None:
            temp_model = DescribeIngressResponseBodyDataDefaultRule()
            self.default_rule = temp_model.from_map(m['DefaultRule'])
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')
        if m.get('ListenerProtocol') is not None:
            self.listener_protocol = m.get('ListenerProtocol')
        if m.get('LoadBalanceType') is not None:
            self.load_balance_type = m.get('LoadBalanceType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        self.rules = []
        if m.get('Rules') is not None:
            for k in m.get('Rules'):
                temp_model = DescribeIngressResponseBodyDataRules()
                self.rules.append(temp_model.from_map(k))
        if m.get('SlbId') is not None:
            self.slb_id = m.get('SlbId')
        if m.get('SlbType') is not None:
            self.slb_type = m.get('SlbType')
        return self


class DescribeIngressResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: DescribeIngressResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = DescribeIngressResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class DescribeIngressResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeIngressResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DescribeIngressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstanceLogRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DescribeInstanceLogResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class DescribeInstanceLogResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeInstanceLogResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DescribeInstanceLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstanceSpecificationsResponseBodyData(TeaModel):
    def __init__(
        self,
        cpu: int = None,
        enable: bool = None,
        id: int = None,
        memory: int = None,
        spec_info: str = None,
        version: int = None,
    ):
        self.cpu = cpu
        self.enable = enable
        self.id = id
        self.memory = memory
        self.spec_info = spec_info
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.id is not None:
            result['Id'] = self.id
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.spec_info is not None:
            result['SpecInfo'] = self.spec_info
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('SpecInfo') is not None:
            self.spec_info = m.get('SpecInfo')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class DescribeInstanceSpecificationsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[DescribeInstanceSpecificationsResponseBodyData] = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = DescribeInstanceSpecificationsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class DescribeInstanceSpecificationsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeInstanceSpecificationsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DescribeInstanceSpecificationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeJobRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        job_id: str = None,
    ):
        self.app_id = app_id
        self.job_id = job_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class DescribeJobResponseBodyDataConfigMapMountDesc(TeaModel):
    def __init__(
        self,
        config_map_id: int = None,
        config_map_name: str = None,
        key: str = None,
        mount_path: str = None,
    ):
        # ConfigMap ID。
        self.config_map_id = config_map_id
        self.config_map_name = config_map_name
        self.key = key
        self.mount_path = mount_path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_map_id is not None:
            result['ConfigMapId'] = self.config_map_id
        if self.config_map_name is not None:
            result['ConfigMapName'] = self.config_map_name
        if self.key is not None:
            result['Key'] = self.key
        if self.mount_path is not None:
            result['MountPath'] = self.mount_path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigMapId') is not None:
            self.config_map_id = m.get('ConfigMapId')
        if m.get('ConfigMapName') is not None:
            self.config_map_name = m.get('ConfigMapName')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('MountPath') is not None:
            self.mount_path = m.get('MountPath')
        return self


class DescribeJobResponseBodyDataMountDesc(TeaModel):
    def __init__(
        self,
        mount_path: str = None,
        nas_path: str = None,
    ):
        self.mount_path = mount_path
        self.nas_path = nas_path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mount_path is not None:
            result['MountPath'] = self.mount_path
        if self.nas_path is not None:
            result['NasPath'] = self.nas_path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MountPath') is not None:
            self.mount_path = m.get('MountPath')
        if m.get('NasPath') is not None:
            self.nas_path = m.get('NasPath')
        return self


class DescribeJobResponseBodyDataOssMountDescs(TeaModel):
    def __init__(
        self,
        bucket_name: str = None,
        bucket_path: str = None,
        mount_path: str = None,
        read_only: bool = None,
    ):
        self.bucket_name = bucket_name
        self.bucket_path = bucket_path
        self.mount_path = mount_path
        self.read_only = read_only

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket_name is not None:
            result['bucketName'] = self.bucket_name
        if self.bucket_path is not None:
            result['bucketPath'] = self.bucket_path
        if self.mount_path is not None:
            result['mountPath'] = self.mount_path
        if self.read_only is not None:
            result['readOnly'] = self.read_only
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bucketName') is not None:
            self.bucket_name = m.get('bucketName')
        if m.get('bucketPath') is not None:
            self.bucket_path = m.get('bucketPath')
        if m.get('mountPath') is not None:
            self.mount_path = m.get('mountPath')
        if m.get('readOnly') is not None:
            self.read_only = m.get('readOnly')
        return self


class DescribeJobResponseBodyDataTags(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeJobResponseBodyData(TeaModel):
    def __init__(
        self,
        acr_assume_role_arn: str = None,
        acr_instance_id: str = None,
        app_description: str = None,
        app_id: str = None,
        app_name: str = None,
        backoff_limit: int = None,
        command: str = None,
        command_args: str = None,
        concurrency_policy: str = None,
        config_map_mount_desc: List[DescribeJobResponseBodyDataConfigMapMountDesc] = None,
        cpu: int = None,
        custom_host_alias: str = None,
        edas_container_version: str = None,
        envs: str = None,
        image_pull_secrets: str = None,
        image_url: str = None,
        jar_start_args: str = None,
        jar_start_options: str = None,
        jdk: str = None,
        memory: int = None,
        mount_desc: List[DescribeJobResponseBodyDataMountDesc] = None,
        mount_host: str = None,
        namespace_id: str = None,
        nas_configs: str = None,
        nas_id: str = None,
        oss_ak_id: str = None,
        oss_ak_secret: str = None,
        oss_mount_descs: List[DescribeJobResponseBodyDataOssMountDescs] = None,
        package_type: str = None,
        package_url: str = None,
        package_version: str = None,
        php_config: str = None,
        php_config_location: str = None,
        post_start: str = None,
        pre_stop: str = None,
        programming_language: str = None,
        public_web_hook_urls: List[str] = None,
        python: str = None,
        python_modules: str = None,
        ref_app_id: str = None,
        refed_app_ids: List[str] = None,
        region_id: str = None,
        replicas: int = None,
        security_group_id: str = None,
        slice: bool = None,
        slice_envs: str = None,
        sls_configs: str = None,
        suspend: bool = None,
        tags: List[DescribeJobResponseBodyDataTags] = None,
        termination_grace_period_seconds: int = None,
        timeout: int = None,
        timezone: str = None,
        tomcat_config: str = None,
        trigger_config: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
        vpc_web_hook_urls: List[str] = None,
        war_start_options: str = None,
        web_container: str = None,
    ):
        self.acr_assume_role_arn = acr_assume_role_arn
        self.acr_instance_id = acr_instance_id
        self.app_description = app_description
        self.app_id = app_id
        self.app_name = app_name
        self.backoff_limit = backoff_limit
        self.command = command
        self.command_args = command_args
        self.concurrency_policy = concurrency_policy
        self.config_map_mount_desc = config_map_mount_desc
        self.cpu = cpu
        self.custom_host_alias = custom_host_alias
        self.edas_container_version = edas_container_version
        self.envs = envs
        self.image_pull_secrets = image_pull_secrets
        self.image_url = image_url
        self.jar_start_args = jar_start_args
        self.jar_start_options = jar_start_options
        self.jdk = jdk
        self.memory = memory
        self.mount_desc = mount_desc
        self.mount_host = mount_host
        self.namespace_id = namespace_id
        self.nas_configs = nas_configs
        # NAS ID。
        self.nas_id = nas_id
        self.oss_ak_id = oss_ak_id
        self.oss_ak_secret = oss_ak_secret
        self.oss_mount_descs = oss_mount_descs
        self.package_type = package_type
        self.package_url = package_url
        self.package_version = package_version
        self.php_config = php_config
        self.php_config_location = php_config_location
        self.post_start = post_start
        self.pre_stop = pre_stop
        self.programming_language = programming_language
        self.public_web_hook_urls = public_web_hook_urls
        self.python = python
        self.python_modules = python_modules
        self.ref_app_id = ref_app_id
        self.refed_app_ids = refed_app_ids
        self.region_id = region_id
        self.replicas = replicas
        self.security_group_id = security_group_id
        self.slice = slice
        self.slice_envs = slice_envs
        self.sls_configs = sls_configs
        self.suspend = suspend
        self.tags = tags
        self.termination_grace_period_seconds = termination_grace_period_seconds
        self.timeout = timeout
        self.timezone = timezone
        self.tomcat_config = tomcat_config
        self.trigger_config = trigger_config
        # vSwitch ID。
        self.v_switch_id = v_switch_id
        # VPC ID。
        self.vpc_id = vpc_id
        self.vpc_web_hook_urls = vpc_web_hook_urls
        self.war_start_options = war_start_options
        self.web_container = web_container

    def validate(self):
        if self.config_map_mount_desc:
            for k in self.config_map_mount_desc:
                if k:
                    k.validate()
        if self.mount_desc:
            for k in self.mount_desc:
                if k:
                    k.validate()
        if self.oss_mount_descs:
            for k in self.oss_mount_descs:
                if k:
                    k.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acr_assume_role_arn is not None:
            result['AcrAssumeRoleArn'] = self.acr_assume_role_arn
        if self.acr_instance_id is not None:
            result['AcrInstanceId'] = self.acr_instance_id
        if self.app_description is not None:
            result['AppDescription'] = self.app_description
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.backoff_limit is not None:
            result['BackoffLimit'] = self.backoff_limit
        if self.command is not None:
            result['Command'] = self.command
        if self.command_args is not None:
            result['CommandArgs'] = self.command_args
        if self.concurrency_policy is not None:
            result['ConcurrencyPolicy'] = self.concurrency_policy
        result['ConfigMapMountDesc'] = []
        if self.config_map_mount_desc is not None:
            for k in self.config_map_mount_desc:
                result['ConfigMapMountDesc'].append(k.to_map() if k else None)
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.custom_host_alias is not None:
            result['CustomHostAlias'] = self.custom_host_alias
        if self.edas_container_version is not None:
            result['EdasContainerVersion'] = self.edas_container_version
        if self.envs is not None:
            result['Envs'] = self.envs
        if self.image_pull_secrets is not None:
            result['ImagePullSecrets'] = self.image_pull_secrets
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        if self.jar_start_args is not None:
            result['JarStartArgs'] = self.jar_start_args
        if self.jar_start_options is not None:
            result['JarStartOptions'] = self.jar_start_options
        if self.jdk is not None:
            result['Jdk'] = self.jdk
        if self.memory is not None:
            result['Memory'] = self.memory
        result['MountDesc'] = []
        if self.mount_desc is not None:
            for k in self.mount_desc:
                result['MountDesc'].append(k.to_map() if k else None)
        if self.mount_host is not None:
            result['MountHost'] = self.mount_host
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.nas_configs is not None:
            result['NasConfigs'] = self.nas_configs
        if self.nas_id is not None:
            result['NasId'] = self.nas_id
        if self.oss_ak_id is not None:
            result['OssAkId'] = self.oss_ak_id
        if self.oss_ak_secret is not None:
            result['OssAkSecret'] = self.oss_ak_secret
        result['OssMountDescs'] = []
        if self.oss_mount_descs is not None:
            for k in self.oss_mount_descs:
                result['OssMountDescs'].append(k.to_map() if k else None)
        if self.package_type is not None:
            result['PackageType'] = self.package_type
        if self.package_url is not None:
            result['PackageUrl'] = self.package_url
        if self.package_version is not None:
            result['PackageVersion'] = self.package_version
        if self.php_config is not None:
            result['PhpConfig'] = self.php_config
        if self.php_config_location is not None:
            result['PhpConfigLocation'] = self.php_config_location
        if self.post_start is not None:
            result['PostStart'] = self.post_start
        if self.pre_stop is not None:
            result['PreStop'] = self.pre_stop
        if self.programming_language is not None:
            result['ProgrammingLanguage'] = self.programming_language
        if self.public_web_hook_urls is not None:
            result['PublicWebHookUrls'] = self.public_web_hook_urls
        if self.python is not None:
            result['Python'] = self.python
        if self.python_modules is not None:
            result['PythonModules'] = self.python_modules
        if self.ref_app_id is not None:
            result['RefAppId'] = self.ref_app_id
        if self.refed_app_ids is not None:
            result['RefedAppIds'] = self.refed_app_ids
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.replicas is not None:
            result['Replicas'] = self.replicas
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.slice is not None:
            result['Slice'] = self.slice
        if self.slice_envs is not None:
            result['SliceEnvs'] = self.slice_envs
        if self.sls_configs is not None:
            result['SlsConfigs'] = self.sls_configs
        if self.suspend is not None:
            result['Suspend'] = self.suspend
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.termination_grace_period_seconds is not None:
            result['TerminationGracePeriodSeconds'] = self.termination_grace_period_seconds
        if self.timeout is not None:
            result['Timeout'] = self.timeout
        if self.timezone is not None:
            result['Timezone'] = self.timezone
        if self.tomcat_config is not None:
            result['TomcatConfig'] = self.tomcat_config
        if self.trigger_config is not None:
            result['TriggerConfig'] = self.trigger_config
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vpc_web_hook_urls is not None:
            result['VpcWebHookUrls'] = self.vpc_web_hook_urls
        if self.war_start_options is not None:
            result['WarStartOptions'] = self.war_start_options
        if self.web_container is not None:
            result['WebContainer'] = self.web_container
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcrAssumeRoleArn') is not None:
            self.acr_assume_role_arn = m.get('AcrAssumeRoleArn')
        if m.get('AcrInstanceId') is not None:
            self.acr_instance_id = m.get('AcrInstanceId')
        if m.get('AppDescription') is not None:
            self.app_description = m.get('AppDescription')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('BackoffLimit') is not None:
            self.backoff_limit = m.get('BackoffLimit')
        if m.get('Command') is not None:
            self.command = m.get('Command')
        if m.get('CommandArgs') is not None:
            self.command_args = m.get('CommandArgs')
        if m.get('ConcurrencyPolicy') is not None:
            self.concurrency_policy = m.get('ConcurrencyPolicy')
        self.config_map_mount_desc = []
        if m.get('ConfigMapMountDesc') is not None:
            for k in m.get('ConfigMapMountDesc'):
                temp_model = DescribeJobResponseBodyDataConfigMapMountDesc()
                self.config_map_mount_desc.append(temp_model.from_map(k))
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('CustomHostAlias') is not None:
            self.custom_host_alias = m.get('CustomHostAlias')
        if m.get('EdasContainerVersion') is not None:
            self.edas_container_version = m.get('EdasContainerVersion')
        if m.get('Envs') is not None:
            self.envs = m.get('Envs')
        if m.get('ImagePullSecrets') is not None:
            self.image_pull_secrets = m.get('ImagePullSecrets')
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        if m.get('JarStartArgs') is not None:
            self.jar_start_args = m.get('JarStartArgs')
        if m.get('JarStartOptions') is not None:
            self.jar_start_options = m.get('JarStartOptions')
        if m.get('Jdk') is not None:
            self.jdk = m.get('Jdk')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        self.mount_desc = []
        if m.get('MountDesc') is not None:
            for k in m.get('MountDesc'):
                temp_model = DescribeJobResponseBodyDataMountDesc()
                self.mount_desc.append(temp_model.from_map(k))
        if m.get('MountHost') is not None:
            self.mount_host = m.get('MountHost')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('NasConfigs') is not None:
            self.nas_configs = m.get('NasConfigs')
        if m.get('NasId') is not None:
            self.nas_id = m.get('NasId')
        if m.get('OssAkId') is not None:
            self.oss_ak_id = m.get('OssAkId')
        if m.get('OssAkSecret') is not None:
            self.oss_ak_secret = m.get('OssAkSecret')
        self.oss_mount_descs = []
        if m.get('OssMountDescs') is not None:
            for k in m.get('OssMountDescs'):
                temp_model = DescribeJobResponseBodyDataOssMountDescs()
                self.oss_mount_descs.append(temp_model.from_map(k))
        if m.get('PackageType') is not None:
            self.package_type = m.get('PackageType')
        if m.get('PackageUrl') is not None:
            self.package_url = m.get('PackageUrl')
        if m.get('PackageVersion') is not None:
            self.package_version = m.get('PackageVersion')
        if m.get('PhpConfig') is not None:
            self.php_config = m.get('PhpConfig')
        if m.get('PhpConfigLocation') is not None:
            self.php_config_location = m.get('PhpConfigLocation')
        if m.get('PostStart') is not None:
            self.post_start = m.get('PostStart')
        if m.get('PreStop') is not None:
            self.pre_stop = m.get('PreStop')
        if m.get('ProgrammingLanguage') is not None:
            self.programming_language = m.get('ProgrammingLanguage')
        if m.get('PublicWebHookUrls') is not None:
            self.public_web_hook_urls = m.get('PublicWebHookUrls')
        if m.get('Python') is not None:
            self.python = m.get('Python')
        if m.get('PythonModules') is not None:
            self.python_modules = m.get('PythonModules')
        if m.get('RefAppId') is not None:
            self.ref_app_id = m.get('RefAppId')
        if m.get('RefedAppIds') is not None:
            self.refed_app_ids = m.get('RefedAppIds')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Replicas') is not None:
            self.replicas = m.get('Replicas')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('Slice') is not None:
            self.slice = m.get('Slice')
        if m.get('SliceEnvs') is not None:
            self.slice_envs = m.get('SliceEnvs')
        if m.get('SlsConfigs') is not None:
            self.sls_configs = m.get('SlsConfigs')
        if m.get('Suspend') is not None:
            self.suspend = m.get('Suspend')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = DescribeJobResponseBodyDataTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('TerminationGracePeriodSeconds') is not None:
            self.termination_grace_period_seconds = m.get('TerminationGracePeriodSeconds')
        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')
        if m.get('Timezone') is not None:
            self.timezone = m.get('Timezone')
        if m.get('TomcatConfig') is not None:
            self.tomcat_config = m.get('TomcatConfig')
        if m.get('TriggerConfig') is not None:
            self.trigger_config = m.get('TriggerConfig')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VpcWebHookUrls') is not None:
            self.vpc_web_hook_urls = m.get('VpcWebHookUrls')
        if m.get('WarStartOptions') is not None:
            self.war_start_options = m.get('WarStartOptions')
        if m.get('WebContainer') is not None:
            self.web_container = m.get('WebContainer')
        return self


class DescribeJobResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: DescribeJobResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = DescribeJobResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class DescribeJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeJobResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DescribeJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeJobHistoryRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        current_page: int = None,
        page_size: int = None,
        state: str = None,
    ):
        self.app_id = app_id
        self.current_page = current_page
        self.page_size = page_size
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.state is not None:
            result['State'] = self.state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('State') is not None:
            self.state = m.get('State')
        return self


class DescribeJobHistoryResponseBodyDataJobs(TeaModel):
    def __init__(
        self,
        active: int = None,
        completion_time: int = None,
        failed: int = None,
        job_id: str = None,
        message: str = None,
        start_time: int = None,
        state: str = None,
        succeeded: int = None,
    ):
        self.active = active
        self.completion_time = completion_time
        self.failed = failed
        self.job_id = job_id
        self.message = message
        self.start_time = start_time
        self.state = state
        self.succeeded = succeeded

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active is not None:
            result['Active'] = self.active
        if self.completion_time is not None:
            result['CompletionTime'] = self.completion_time
        if self.failed is not None:
            result['Failed'] = self.failed
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.message is not None:
            result['Message'] = self.message
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.state is not None:
            result['State'] = self.state
        if self.succeeded is not None:
            result['Succeeded'] = self.succeeded
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Active') is not None:
            self.active = m.get('Active')
        if m.get('CompletionTime') is not None:
            self.completion_time = m.get('CompletionTime')
        if m.get('Failed') is not None:
            self.failed = m.get('Failed')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Succeeded') is not None:
            self.succeeded = m.get('Succeeded')
        return self


class DescribeJobHistoryResponseBodyData(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        jobs: List[DescribeJobHistoryResponseBodyDataJobs] = None,
        page_size: int = None,
        total_size: int = None,
    ):
        self.current_page = current_page
        self.jobs = jobs
        self.page_size = page_size
        self.total_size = total_size

    def validate(self):
        if self.jobs:
            for k in self.jobs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['Jobs'] = []
        if self.jobs is not None:
            for k in self.jobs:
                result['Jobs'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_size is not None:
            result['TotalSize'] = self.total_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.jobs = []
        if m.get('Jobs') is not None:
            for k in m.get('Jobs'):
                temp_model = DescribeJobHistoryResponseBodyDataJobs()
                self.jobs.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalSize') is not None:
            self.total_size = m.get('TotalSize')
        return self


class DescribeJobHistoryResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: DescribeJobHistoryResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = DescribeJobHistoryResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class DescribeJobHistoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeJobHistoryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DescribeJobHistoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeJobStatusRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        job_id: str = None,
    ):
        self.app_id = app_id
        self.job_id = job_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class DescribeJobStatusResponseBodyData(TeaModel):
    def __init__(
        self,
        active: int = None,
        completion_time: int = None,
        failed: int = None,
        job_id: str = None,
        message: str = None,
        start_time: int = None,
        state: str = None,
        succeeded: int = None,
    ):
        self.active = active
        self.completion_time = completion_time
        self.failed = failed
        self.job_id = job_id
        self.message = message
        self.start_time = start_time
        self.state = state
        self.succeeded = succeeded

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active is not None:
            result['Active'] = self.active
        if self.completion_time is not None:
            result['CompletionTime'] = self.completion_time
        if self.failed is not None:
            result['Failed'] = self.failed
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.message is not None:
            result['Message'] = self.message
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.state is not None:
            result['State'] = self.state
        if self.succeeded is not None:
            result['Succeeded'] = self.succeeded
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Active') is not None:
            self.active = m.get('Active')
        if m.get('CompletionTime') is not None:
            self.completion_time = m.get('CompletionTime')
        if m.get('Failed') is not None:
            self.failed = m.get('Failed')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Succeeded') is not None:
            self.succeeded = m.get('Succeeded')
        return self


class DescribeJobStatusResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: DescribeJobStatusResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = DescribeJobStatusResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class DescribeJobStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeJobStatusResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DescribeJobStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeNamespaceRequest(TeaModel):
    def __init__(
        self,
        name_space_short_id: str = None,
        namespace_id: str = None,
    ):
        self.name_space_short_id = name_space_short_id
        self.namespace_id = namespace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name_space_short_id is not None:
            result['NameSpaceShortId'] = self.name_space_short_id
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NameSpaceShortId') is not None:
            self.name_space_short_id = m.get('NameSpaceShortId')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        return self


class DescribeNamespaceResponseBodyData(TeaModel):
    def __init__(
        self,
        name_space_short_id: str = None,
        namespace_description: str = None,
        namespace_id: str = None,
        namespace_name: str = None,
        region_id: str = None,
    ):
        self.name_space_short_id = name_space_short_id
        self.namespace_description = namespace_description
        self.namespace_id = namespace_id
        self.namespace_name = namespace_name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name_space_short_id is not None:
            result['NameSpaceShortId'] = self.name_space_short_id
        if self.namespace_description is not None:
            result['NamespaceDescription'] = self.namespace_description
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.namespace_name is not None:
            result['NamespaceName'] = self.namespace_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NameSpaceShortId') is not None:
            self.name_space_short_id = m.get('NameSpaceShortId')
        if m.get('NamespaceDescription') is not None:
            self.namespace_description = m.get('NamespaceDescription')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('NamespaceName') is not None:
            self.namespace_name = m.get('NamespaceName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeNamespaceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: DescribeNamespaceResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = DescribeNamespaceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class DescribeNamespaceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeNamespaceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DescribeNamespaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeNamespaceListRequest(TeaModel):
    def __init__(
        self,
        contain_custom: bool = None,
        hybrid_cloud_exclude: bool = None,
    ):
        self.contain_custom = contain_custom
        self.hybrid_cloud_exclude = hybrid_cloud_exclude

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contain_custom is not None:
            result['ContainCustom'] = self.contain_custom
        if self.hybrid_cloud_exclude is not None:
            result['HybridCloudExclude'] = self.hybrid_cloud_exclude
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContainCustom') is not None:
            self.contain_custom = m.get('ContainCustom')
        if m.get('HybridCloudExclude') is not None:
            self.hybrid_cloud_exclude = m.get('HybridCloudExclude')
        return self


class DescribeNamespaceListResponseBodyData(TeaModel):
    def __init__(
        self,
        agent_install: str = None,
        current: bool = None,
        custom: bool = None,
        hybrid_cloud_enable: bool = None,
        name_space_short_id: str = None,
        namespace_id: str = None,
        namespace_name: str = None,
        region_id: str = None,
        security_group_id: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
    ):
        self.agent_install = agent_install
        self.current = current
        self.custom = custom
        self.hybrid_cloud_enable = hybrid_cloud_enable
        self.name_space_short_id = name_space_short_id
        self.namespace_id = namespace_id
        self.namespace_name = namespace_name
        self.region_id = region_id
        self.security_group_id = security_group_id
        # vSwitch ID。
        self.v_switch_id = v_switch_id
        # VPC ID。
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_install is not None:
            result['AgentInstall'] = self.agent_install
        if self.current is not None:
            result['Current'] = self.current
        if self.custom is not None:
            result['Custom'] = self.custom
        if self.hybrid_cloud_enable is not None:
            result['HybridCloudEnable'] = self.hybrid_cloud_enable
        if self.name_space_short_id is not None:
            result['NameSpaceShortId'] = self.name_space_short_id
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.namespace_name is not None:
            result['NamespaceName'] = self.namespace_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentInstall') is not None:
            self.agent_install = m.get('AgentInstall')
        if m.get('Current') is not None:
            self.current = m.get('Current')
        if m.get('Custom') is not None:
            self.custom = m.get('Custom')
        if m.get('HybridCloudEnable') is not None:
            self.hybrid_cloud_enable = m.get('HybridCloudEnable')
        if m.get('NameSpaceShortId') is not None:
            self.name_space_short_id = m.get('NameSpaceShortId')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('NamespaceName') is not None:
            self.namespace_name = m.get('NamespaceName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class DescribeNamespaceListResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[DescribeNamespaceListResponseBodyData] = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = DescribeNamespaceListResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class DescribeNamespaceListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeNamespaceListResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DescribeNamespaceListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeNamespaceResourcesRequest(TeaModel):
    def __init__(
        self,
        name_space_short_id: str = None,
        namespace_id: str = None,
    ):
        self.name_space_short_id = name_space_short_id
        self.namespace_id = namespace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name_space_short_id is not None:
            result['NameSpaceShortId'] = self.name_space_short_id
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NameSpaceShortId') is not None:
            self.name_space_short_id = m.get('NameSpaceShortId')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        return self


class DescribeNamespaceResourcesResponseBodyData(TeaModel):
    def __init__(
        self,
        app_count: int = None,
        belong_region: str = None,
        description: str = None,
        jump_server_app_id: str = None,
        jump_server_ip: str = None,
        last_change_order_id: str = None,
        last_change_order_running: bool = None,
        last_change_order_status: str = None,
        name_space_short_id: str = None,
        namespace_id: str = None,
        namespace_name: str = None,
        notification_expired: bool = None,
        security_group_id: str = None,
        tenant_id: str = None,
        user_id: str = None,
        v_switch_id: str = None,
        v_switch_name: str = None,
        vpc_id: str = None,
        vpc_name: str = None,
    ):
        self.app_count = app_count
        self.belong_region = belong_region
        self.description = description
        self.jump_server_app_id = jump_server_app_id
        self.jump_server_ip = jump_server_ip
        self.last_change_order_id = last_change_order_id
        self.last_change_order_running = last_change_order_running
        self.last_change_order_status = last_change_order_status
        self.name_space_short_id = name_space_short_id
        self.namespace_id = namespace_id
        self.namespace_name = namespace_name
        self.notification_expired = notification_expired
        self.security_group_id = security_group_id
        self.tenant_id = tenant_id
        self.user_id = user_id
        # vSwitch ID。
        self.v_switch_id = v_switch_id
        self.v_switch_name = v_switch_name
        # VPC ID。
        self.vpc_id = vpc_id
        self.vpc_name = vpc_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_count is not None:
            result['AppCount'] = self.app_count
        if self.belong_region is not None:
            result['BelongRegion'] = self.belong_region
        if self.description is not None:
            result['Description'] = self.description
        if self.jump_server_app_id is not None:
            result['JumpServerAppId'] = self.jump_server_app_id
        if self.jump_server_ip is not None:
            result['JumpServerIp'] = self.jump_server_ip
        if self.last_change_order_id is not None:
            result['LastChangeOrderId'] = self.last_change_order_id
        if self.last_change_order_running is not None:
            result['LastChangeOrderRunning'] = self.last_change_order_running
        if self.last_change_order_status is not None:
            result['LastChangeOrderStatus'] = self.last_change_order_status
        if self.name_space_short_id is not None:
            result['NameSpaceShortId'] = self.name_space_short_id
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.namespace_name is not None:
            result['NamespaceName'] = self.namespace_name
        if self.notification_expired is not None:
            result['NotificationExpired'] = self.notification_expired
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.v_switch_name is not None:
            result['VSwitchName'] = self.v_switch_name
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vpc_name is not None:
            result['VpcName'] = self.vpc_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCount') is not None:
            self.app_count = m.get('AppCount')
        if m.get('BelongRegion') is not None:
            self.belong_region = m.get('BelongRegion')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('JumpServerAppId') is not None:
            self.jump_server_app_id = m.get('JumpServerAppId')
        if m.get('JumpServerIp') is not None:
            self.jump_server_ip = m.get('JumpServerIp')
        if m.get('LastChangeOrderId') is not None:
            self.last_change_order_id = m.get('LastChangeOrderId')
        if m.get('LastChangeOrderRunning') is not None:
            self.last_change_order_running = m.get('LastChangeOrderRunning')
        if m.get('LastChangeOrderStatus') is not None:
            self.last_change_order_status = m.get('LastChangeOrderStatus')
        if m.get('NameSpaceShortId') is not None:
            self.name_space_short_id = m.get('NameSpaceShortId')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('NamespaceName') is not None:
            self.namespace_name = m.get('NamespaceName')
        if m.get('NotificationExpired') is not None:
            self.notification_expired = m.get('NotificationExpired')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VSwitchName') is not None:
            self.v_switch_name = m.get('VSwitchName')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VpcName') is not None:
            self.vpc_name = m.get('VpcName')
        return self


class DescribeNamespaceResourcesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: DescribeNamespaceResourcesResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = DescribeNamespaceResourcesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class DescribeNamespaceResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeNamespaceResourcesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DescribeNamespaceResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeNamespacesRequest(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
    ):
        self.current_page = current_page
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeNamespacesResponseBodyDataNamespaces(TeaModel):
    def __init__(
        self,
        access_key: str = None,
        address_server_host: str = None,
        name_space_short_id: str = None,
        namespace_description: str = None,
        namespace_id: str = None,
        namespace_name: str = None,
        region_id: str = None,
        secret_key: str = None,
        tenant_id: str = None,
    ):
        self.access_key = access_key
        self.address_server_host = address_server_host
        self.name_space_short_id = name_space_short_id
        self.namespace_description = namespace_description
        self.namespace_id = namespace_id
        self.namespace_name = namespace_name
        self.region_id = region_id
        self.secret_key = secret_key
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key is not None:
            result['AccessKey'] = self.access_key
        if self.address_server_host is not None:
            result['AddressServerHost'] = self.address_server_host
        if self.name_space_short_id is not None:
            result['NameSpaceShortId'] = self.name_space_short_id
        if self.namespace_description is not None:
            result['NamespaceDescription'] = self.namespace_description
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.namespace_name is not None:
            result['NamespaceName'] = self.namespace_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.secret_key is not None:
            result['SecretKey'] = self.secret_key
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessKey') is not None:
            self.access_key = m.get('AccessKey')
        if m.get('AddressServerHost') is not None:
            self.address_server_host = m.get('AddressServerHost')
        if m.get('NameSpaceShortId') is not None:
            self.name_space_short_id = m.get('NameSpaceShortId')
        if m.get('NamespaceDescription') is not None:
            self.namespace_description = m.get('NamespaceDescription')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('NamespaceName') is not None:
            self.namespace_name = m.get('NamespaceName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SecretKey') is not None:
            self.secret_key = m.get('SecretKey')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class DescribeNamespacesResponseBodyData(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        namespaces: List[DescribeNamespacesResponseBodyDataNamespaces] = None,
        page_size: int = None,
        total_size: int = None,
    ):
        self.current_page = current_page
        self.namespaces = namespaces
        self.page_size = page_size
        self.total_size = total_size

    def validate(self):
        if self.namespaces:
            for k in self.namespaces:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['Namespaces'] = []
        if self.namespaces is not None:
            for k in self.namespaces:
                result['Namespaces'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_size is not None:
            result['TotalSize'] = self.total_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.namespaces = []
        if m.get('Namespaces') is not None:
            for k in m.get('Namespaces'):
                temp_model = DescribeNamespacesResponseBodyDataNamespaces()
                self.namespaces.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalSize') is not None:
            self.total_size = m.get('TotalSize')
        return self


class DescribeNamespacesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: DescribeNamespacesResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = DescribeNamespacesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class DescribeNamespacesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeNamespacesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DescribeNamespacesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePipelineRequest(TeaModel):
    def __init__(
        self,
        pipeline_id: str = None,
    ):
        self.pipeline_id = pipeline_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pipeline_id is not None:
            result['PipelineId'] = self.pipeline_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PipelineId') is not None:
            self.pipeline_id = m.get('PipelineId')
        return self


class DescribePipelineResponseBodyDataStageListTaskList(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_ignore: int = None,
        error_message: str = None,
        message: str = None,
        show_manual_ignore: bool = None,
        stage_id: str = None,
        status: int = None,
        task_id: str = None,
        task_name: str = None,
    ):
        self.error_code = error_code
        self.error_ignore = error_ignore
        self.error_message = error_message
        self.message = message
        self.show_manual_ignore = show_manual_ignore
        self.stage_id = stage_id
        self.status = status
        self.task_id = task_id
        self.task_name = task_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_ignore is not None:
            result['ErrorIgnore'] = self.error_ignore
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.message is not None:
            result['Message'] = self.message
        if self.show_manual_ignore is not None:
            result['ShowManualIgnore'] = self.show_manual_ignore
        if self.stage_id is not None:
            result['StageId'] = self.stage_id
        if self.status is not None:
            result['Status'] = self.status
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorIgnore') is not None:
            self.error_ignore = m.get('ErrorIgnore')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('ShowManualIgnore') is not None:
            self.show_manual_ignore = m.get('ShowManualIgnore')
        if m.get('StageId') is not None:
            self.stage_id = m.get('StageId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        return self


class DescribePipelineResponseBodyDataStageList(TeaModel):
    def __init__(
        self,
        executor_type: int = None,
        stage_id: str = None,
        stage_name: str = None,
        status: int = None,
        task_list: List[DescribePipelineResponseBodyDataStageListTaskList] = None,
    ):
        self.executor_type = executor_type
        self.stage_id = stage_id
        self.stage_name = stage_name
        self.status = status
        self.task_list = task_list

    def validate(self):
        if self.task_list:
            for k in self.task_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.executor_type is not None:
            result['ExecutorType'] = self.executor_type
        if self.stage_id is not None:
            result['StageId'] = self.stage_id
        if self.stage_name is not None:
            result['StageName'] = self.stage_name
        if self.status is not None:
            result['Status'] = self.status
        result['TaskList'] = []
        if self.task_list is not None:
            for k in self.task_list:
                result['TaskList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExecutorType') is not None:
            self.executor_type = m.get('ExecutorType')
        if m.get('StageId') is not None:
            self.stage_id = m.get('StageId')
        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        self.task_list = []
        if m.get('TaskList') is not None:
            for k in m.get('TaskList'):
                temp_model = DescribePipelineResponseBodyDataStageListTaskList()
                self.task_list.append(temp_model.from_map(k))
        return self


class DescribePipelineResponseBodyData(TeaModel):
    def __init__(
        self,
        co_status: str = None,
        current_stage_id: str = None,
        next_pipeline_id: str = None,
        pipeline_id: str = None,
        pipeline_name: str = None,
        pipeline_status: int = None,
        show_batch: bool = None,
        stage_list: List[DescribePipelineResponseBodyDataStageList] = None,
    ):
        self.co_status = co_status
        self.current_stage_id = current_stage_id
        self.next_pipeline_id = next_pipeline_id
        self.pipeline_id = pipeline_id
        self.pipeline_name = pipeline_name
        self.pipeline_status = pipeline_status
        self.show_batch = show_batch
        self.stage_list = stage_list

    def validate(self):
        if self.stage_list:
            for k in self.stage_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.co_status is not None:
            result['CoStatus'] = self.co_status
        if self.current_stage_id is not None:
            result['CurrentStageId'] = self.current_stage_id
        if self.next_pipeline_id is not None:
            result['NextPipelineId'] = self.next_pipeline_id
        if self.pipeline_id is not None:
            result['PipelineId'] = self.pipeline_id
        if self.pipeline_name is not None:
            result['PipelineName'] = self.pipeline_name
        if self.pipeline_status is not None:
            result['PipelineStatus'] = self.pipeline_status
        if self.show_batch is not None:
            result['ShowBatch'] = self.show_batch
        result['StageList'] = []
        if self.stage_list is not None:
            for k in self.stage_list:
                result['StageList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CoStatus') is not None:
            self.co_status = m.get('CoStatus')
        if m.get('CurrentStageId') is not None:
            self.current_stage_id = m.get('CurrentStageId')
        if m.get('NextPipelineId') is not None:
            self.next_pipeline_id = m.get('NextPipelineId')
        if m.get('PipelineId') is not None:
            self.pipeline_id = m.get('PipelineId')
        if m.get('PipelineName') is not None:
            self.pipeline_name = m.get('PipelineName')
        if m.get('PipelineStatus') is not None:
            self.pipeline_status = m.get('PipelineStatus')
        if m.get('ShowBatch') is not None:
            self.show_batch = m.get('ShowBatch')
        self.stage_list = []
        if m.get('StageList') is not None:
            for k in m.get('StageList'):
                temp_model = DescribePipelineResponseBodyDataStageList()
                self.stage_list.append(temp_model.from_map(k))
        return self


class DescribePipelineResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: DescribePipelineResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = DescribePipelineResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class DescribePipelineResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribePipelineResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DescribePipelineResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRegionsResponseBodyRegionsRegionRecommendZones(TeaModel):
    def __init__(
        self,
        recommend_zone: List[str] = None,
    ):
        self.recommend_zone = recommend_zone

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.recommend_zone is not None:
            result['RecommendZone'] = self.recommend_zone
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RecommendZone') is not None:
            self.recommend_zone = m.get('RecommendZone')
        return self


class DescribeRegionsResponseBodyRegionsRegion(TeaModel):
    def __init__(
        self,
        local_name: str = None,
        recommend_zones: DescribeRegionsResponseBodyRegionsRegionRecommendZones = None,
        region_endpoint: str = None,
        region_id: str = None,
    ):
        self.local_name = local_name
        self.recommend_zones = recommend_zones
        self.region_endpoint = region_endpoint
        self.region_id = region_id

    def validate(self):
        if self.recommend_zones:
            self.recommend_zones.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.local_name is not None:
            result['LocalName'] = self.local_name
        if self.recommend_zones is not None:
            result['RecommendZones'] = self.recommend_zones.to_map()
        if self.region_endpoint is not None:
            result['RegionEndpoint'] = self.region_endpoint
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')
        if m.get('RecommendZones') is not None:
            temp_model = DescribeRegionsResponseBodyRegionsRegionRecommendZones()
            self.recommend_zones = temp_model.from_map(m['RecommendZones'])
        if m.get('RegionEndpoint') is not None:
            self.region_endpoint = m.get('RegionEndpoint')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeRegionsResponseBodyRegions(TeaModel):
    def __init__(
        self,
        region: List[DescribeRegionsResponseBodyRegionsRegion] = None,
    ):
        self.region = region

    def validate(self):
        if self.region:
            for k in self.region:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Region'] = []
        if self.region is not None:
            for k in self.region:
                result['Region'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.region = []
        if m.get('Region') is not None:
            for k in m.get('Region'):
                temp_model = DescribeRegionsResponseBodyRegionsRegion()
                self.region.append(temp_model.from_map(k))
        return self


class DescribeRegionsResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        regions: DescribeRegionsResponseBodyRegions = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.regions = regions
        self.request_id = request_id

    def validate(self):
        if self.regions:
            self.regions.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.regions is not None:
            result['Regions'] = self.regions.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Regions') is not None:
            temp_model = DescribeRegionsResponseBodyRegions()
            self.regions = temp_model.from_map(m['Regions'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeRegionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeRegionsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DescribeRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSecretRequest(TeaModel):
    def __init__(
        self,
        namespace_id: str = None,
        secret_id: int = None,
    ):
        self.namespace_id = namespace_id
        self.secret_id = secret_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.secret_id is not None:
            result['SecretId'] = self.secret_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('SecretId') is not None:
            self.secret_id = m.get('SecretId')
        return self


class DescribeSecretResponseBodyDataRelateApps(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        app_name: str = None,
    ):
        self.app_id = app_id
        self.app_name = app_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        return self


class DescribeSecretResponseBodyData(TeaModel):
    def __init__(
        self,
        create_time: int = None,
        namespace_id: str = None,
        relate_apps: List[DescribeSecretResponseBodyDataRelateApps] = None,
        secret_data: Dict[str, str] = None,
        secret_id: int = None,
        secret_name: str = None,
        secret_type: str = None,
        update_time: int = None,
    ):
        self.create_time = create_time
        self.namespace_id = namespace_id
        self.relate_apps = relate_apps
        self.secret_data = secret_data
        self.secret_id = secret_id
        self.secret_name = secret_name
        self.secret_type = secret_type
        self.update_time = update_time

    def validate(self):
        if self.relate_apps:
            for k in self.relate_apps:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        result['RelateApps'] = []
        if self.relate_apps is not None:
            for k in self.relate_apps:
                result['RelateApps'].append(k.to_map() if k else None)
        if self.secret_data is not None:
            result['SecretData'] = self.secret_data
        if self.secret_id is not None:
            result['SecretId'] = self.secret_id
        if self.secret_name is not None:
            result['SecretName'] = self.secret_name
        if self.secret_type is not None:
            result['SecretType'] = self.secret_type
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        self.relate_apps = []
        if m.get('RelateApps') is not None:
            for k in m.get('RelateApps'):
                temp_model = DescribeSecretResponseBodyDataRelateApps()
                self.relate_apps.append(temp_model.from_map(k))
        if m.get('SecretData') is not None:
            self.secret_data = m.get('SecretData')
        if m.get('SecretId') is not None:
            self.secret_id = m.get('SecretId')
        if m.get('SecretName') is not None:
            self.secret_name = m.get('SecretName')
        if m.get('SecretType') is not None:
            self.secret_type = m.get('SecretType')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class DescribeSecretResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: DescribeSecretResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = DescribeSecretResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class DescribeSecretResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeSecretResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DescribeSecretResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableApplicationScalingRuleRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        scaling_rule_name: str = None,
    ):
        self.app_id = app_id
        self.scaling_rule_name = scaling_rule_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.scaling_rule_name is not None:
            result['ScalingRuleName'] = self.scaling_rule_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ScalingRuleName') is not None:
            self.scaling_rule_name = m.get('ScalingRuleName')
        return self


class DisableApplicationScalingRuleResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class DisableApplicationScalingRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DisableApplicationScalingRuleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DisableApplicationScalingRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableApplicationScalingRuleRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        scaling_rule_name: str = None,
    ):
        self.app_id = app_id
        self.scaling_rule_name = scaling_rule_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.scaling_rule_name is not None:
            result['ScalingRuleName'] = self.scaling_rule_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ScalingRuleName') is not None:
            self.scaling_rule_name = m.get('ScalingRuleName')
        return self


class EnableApplicationScalingRuleResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class EnableApplicationScalingRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: EnableApplicationScalingRuleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = EnableApplicationScalingRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExecJobRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        command: str = None,
        command_args: str = None,
        envs: str = None,
        event_id: str = None,
        jar_start_args: str = None,
        jar_start_options: str = None,
        time: str = None,
        war_start_options: str = None,
    ):
        self.app_id = app_id
        self.command = command
        self.command_args = command_args
        self.envs = envs
        self.event_id = event_id
        self.jar_start_args = jar_start_args
        self.jar_start_options = jar_start_options
        self.time = time
        self.war_start_options = war_start_options

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.command is not None:
            result['Command'] = self.command
        if self.command_args is not None:
            result['CommandArgs'] = self.command_args
        if self.envs is not None:
            result['Envs'] = self.envs
        if self.event_id is not None:
            result['EventId'] = self.event_id
        if self.jar_start_args is not None:
            result['JarStartArgs'] = self.jar_start_args
        if self.jar_start_options is not None:
            result['JarStartOptions'] = self.jar_start_options
        if self.time is not None:
            result['Time'] = self.time
        if self.war_start_options is not None:
            result['WarStartOptions'] = self.war_start_options
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Command') is not None:
            self.command = m.get('Command')
        if m.get('CommandArgs') is not None:
            self.command_args = m.get('CommandArgs')
        if m.get('Envs') is not None:
            self.envs = m.get('Envs')
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        if m.get('JarStartArgs') is not None:
            self.jar_start_args = m.get('JarStartArgs')
        if m.get('JarStartOptions') is not None:
            self.jar_start_options = m.get('JarStartOptions')
        if m.get('Time') is not None:
            self.time = m.get('Time')
        if m.get('WarStartOptions') is not None:
            self.war_start_options = m.get('WarStartOptions')
        return self


class ExecJobResponseBodyData(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        msg: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
        self.msg = msg
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ExecJobResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ExecJobResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = ExecJobResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class ExecJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ExecJobResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = ExecJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAppEventsRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        current_page: int = None,
        event_type: str = None,
        namespace: str = None,
        object_kind: str = None,
        object_name: str = None,
        page_size: int = None,
        reason: str = None,
    ):
        self.app_id = app_id
        self.current_page = current_page
        self.event_type = event_type
        self.namespace = namespace
        self.object_kind = object_kind
        self.object_name = object_name
        self.page_size = page_size
        self.reason = reason

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.event_type is not None:
            result['EventType'] = self.event_type
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.object_kind is not None:
            result['ObjectKind'] = self.object_kind
        if self.object_name is not None:
            result['ObjectName'] = self.object_name
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.reason is not None:
            result['Reason'] = self.reason
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('ObjectKind') is not None:
            self.object_kind = m.get('ObjectKind')
        if m.get('ObjectName') is not None:
            self.object_name = m.get('ObjectName')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        return self


class ListAppEventsResponseBodyDataAppEventEntity(TeaModel):
    def __init__(
        self,
        event_type: str = None,
        first_timestamp: str = None,
        last_timestamp: str = None,
        message: str = None,
        object_kind: str = None,
        object_name: str = None,
        reason: str = None,
    ):
        self.event_type = event_type
        self.first_timestamp = first_timestamp
        self.last_timestamp = last_timestamp
        self.message = message
        self.object_kind = object_kind
        self.object_name = object_name
        self.reason = reason

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_type is not None:
            result['EventType'] = self.event_type
        if self.first_timestamp is not None:
            result['FirstTimestamp'] = self.first_timestamp
        if self.last_timestamp is not None:
            result['LastTimestamp'] = self.last_timestamp
        if self.message is not None:
            result['Message'] = self.message
        if self.object_kind is not None:
            result['ObjectKind'] = self.object_kind
        if self.object_name is not None:
            result['ObjectName'] = self.object_name
        if self.reason is not None:
            result['Reason'] = self.reason
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')
        if m.get('FirstTimestamp') is not None:
            self.first_timestamp = m.get('FirstTimestamp')
        if m.get('LastTimestamp') is not None:
            self.last_timestamp = m.get('LastTimestamp')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('ObjectKind') is not None:
            self.object_kind = m.get('ObjectKind')
        if m.get('ObjectName') is not None:
            self.object_name = m.get('ObjectName')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        return self


class ListAppEventsResponseBodyData(TeaModel):
    def __init__(
        self,
        app_event_entity: List[ListAppEventsResponseBodyDataAppEventEntity] = None,
        current_page: int = None,
        page_size: int = None,
        total_size: int = None,
    ):
        self.app_event_entity = app_event_entity
        self.current_page = current_page
        self.page_size = page_size
        self.total_size = total_size

    def validate(self):
        if self.app_event_entity:
            for k in self.app_event_entity:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AppEventEntity'] = []
        if self.app_event_entity is not None:
            for k in self.app_event_entity:
                result['AppEventEntity'].append(k.to_map() if k else None)
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_size is not None:
            result['TotalSize'] = self.total_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.app_event_entity = []
        if m.get('AppEventEntity') is not None:
            for k in m.get('AppEventEntity'):
                temp_model = ListAppEventsResponseBodyDataAppEventEntity()
                self.app_event_entity.append(temp_model.from_map(k))
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalSize') is not None:
            self.total_size = m.get('TotalSize')
        return self


class ListAppEventsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListAppEventsResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
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
        if m.get('Data') is not None:
            temp_model = ListAppEventsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListAppEventsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAppEventsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = ListAppEventsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAppServicesPageRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        page_number: int = None,
        page_size: int = None,
        service_type: str = None,
    ):
        self.app_id = app_id
        self.page_number = page_number
        self.page_size = page_size
        self.service_type = service_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        return self


class ListAppServicesPageResponseBodyDataResult(TeaModel):
    def __init__(
        self,
        edas_app_id: str = None,
        edas_app_name: str = None,
        group: str = None,
        instance_num: int = None,
        service_name: str = None,
        version: str = None,
    ):
        self.edas_app_id = edas_app_id
        self.edas_app_name = edas_app_name
        self.group = group
        self.instance_num = instance_num
        self.service_name = service_name
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.edas_app_id is not None:
            result['EdasAppId'] = self.edas_app_id
        if self.edas_app_name is not None:
            result['EdasAppName'] = self.edas_app_name
        if self.group is not None:
            result['Group'] = self.group
        if self.instance_num is not None:
            result['InstanceNum'] = self.instance_num
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EdasAppId') is not None:
            self.edas_app_id = m.get('EdasAppId')
        if m.get('EdasAppName') is not None:
            self.edas_app_name = m.get('EdasAppName')
        if m.get('Group') is not None:
            self.group = m.get('Group')
        if m.get('InstanceNum') is not None:
            self.instance_num = m.get('InstanceNum')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class ListAppServicesPageResponseBodyData(TeaModel):
    def __init__(
        self,
        current_page: str = None,
        page_number: str = None,
        page_size: str = None,
        result: List[ListAppServicesPageResponseBodyDataResult] = None,
        total_size: str = None,
    ):
        self.current_page = current_page
        self.page_number = page_number
        self.page_size = page_size
        self.result = result
        self.total_size = total_size

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.total_size is not None:
            result['TotalSize'] = self.total_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListAppServicesPageResponseBodyDataResult()
                self.result.append(temp_model.from_map(k))
        if m.get('TotalSize') is not None:
            self.total_size = m.get('TotalSize')
        return self


class ListAppServicesPageResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[ListAppServicesPageResponseBodyData] = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListAppServicesPageResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class ListAppServicesPageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAppServicesPageResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = ListAppServicesPageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAppVersionsRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
    ):
        self.app_id = app_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        return self


class ListAppVersionsResponseBodyData(TeaModel):
    def __init__(
        self,
        build_package_url: str = None,
        create_time: str = None,
        id: str = None,
        type: str = None,
        war_url: str = None,
    ):
        self.build_package_url = build_package_url
        self.create_time = create_time
        self.id = id
        self.type = type
        self.war_url = war_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.build_package_url is not None:
            result['BuildPackageUrl'] = self.build_package_url
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.id is not None:
            result['Id'] = self.id
        if self.type is not None:
            result['Type'] = self.type
        if self.war_url is not None:
            result['WarUrl'] = self.war_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BuildPackageUrl') is not None:
            self.build_package_url = m.get('BuildPackageUrl')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('WarUrl') is not None:
            self.war_url = m.get('WarUrl')
        return self


class ListAppVersionsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[ListAppVersionsResponseBodyData] = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
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
            for k in m.get('Data'):
                temp_model = ListAppVersionsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListAppVersionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAppVersionsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = ListAppVersionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListApplicationsRequest(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        current_page: int = None,
        field_type: str = None,
        field_value: str = None,
        namespace_id: str = None,
        order_by: str = None,
        page_size: int = None,
        reverse: bool = None,
        tags: str = None,
    ):
        self.app_name = app_name
        self.current_page = current_page
        self.field_type = field_type
        self.field_value = field_value
        self.namespace_id = namespace_id
        self.order_by = order_by
        self.page_size = page_size
        self.reverse = reverse
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.field_type is not None:
            result['FieldType'] = self.field_type
        if self.field_value is not None:
            result['FieldValue'] = self.field_value
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.order_by is not None:
            result['OrderBy'] = self.order_by
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.reverse is not None:
            result['Reverse'] = self.reverse
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('FieldType') is not None:
            self.field_type = m.get('FieldType')
        if m.get('FieldValue') is not None:
            self.field_value = m.get('FieldValue')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Reverse') is not None:
            self.reverse = m.get('Reverse')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        return self


class ListApplicationsResponseBodyDataApplicationsTags(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListApplicationsResponseBodyDataApplications(TeaModel):
    def __init__(
        self,
        app_deleting_status: bool = None,
        app_description: str = None,
        app_id: str = None,
        app_name: str = None,
        instances: int = None,
        namespace_id: str = None,
        region_id: str = None,
        running_instances: int = None,
        tags: List[ListApplicationsResponseBodyDataApplicationsTags] = None,
    ):
        self.app_deleting_status = app_deleting_status
        self.app_description = app_description
        self.app_id = app_id
        self.app_name = app_name
        self.instances = instances
        self.namespace_id = namespace_id
        self.region_id = region_id
        self.running_instances = running_instances
        self.tags = tags

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_deleting_status is not None:
            result['AppDeletingStatus'] = self.app_deleting_status
        if self.app_description is not None:
            result['AppDescription'] = self.app_description
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.instances is not None:
            result['Instances'] = self.instances
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.running_instances is not None:
            result['RunningInstances'] = self.running_instances
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppDeletingStatus') is not None:
            self.app_deleting_status = m.get('AppDeletingStatus')
        if m.get('AppDescription') is not None:
            self.app_description = m.get('AppDescription')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Instances') is not None:
            self.instances = m.get('Instances')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RunningInstances') is not None:
            self.running_instances = m.get('RunningInstances')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListApplicationsResponseBodyDataApplicationsTags()
                self.tags.append(temp_model.from_map(k))
        return self


class ListApplicationsResponseBodyData(TeaModel):
    def __init__(
        self,
        applications: List[ListApplicationsResponseBodyDataApplications] = None,
        current_page: int = None,
        page_size: int = None,
        total_size: int = None,
    ):
        self.applications = applications
        self.current_page = current_page
        self.page_size = page_size
        self.total_size = total_size

    def validate(self):
        if self.applications:
            for k in self.applications:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Applications'] = []
        if self.applications is not None:
            for k in self.applications:
                result['Applications'].append(k.to_map() if k else None)
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_size is not None:
            result['TotalSize'] = self.total_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.applications = []
        if m.get('Applications') is not None:
            for k in m.get('Applications'):
                temp_model = ListApplicationsResponseBodyDataApplications()
                self.applications.append(temp_model.from_map(k))
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalSize') is not None:
            self.total_size = m.get('TotalSize')
        return self


class ListApplicationsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        current_page: int = None,
        data: ListApplicationsResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_size: int = None,
    ):
        self.code = code
        self.current_page = current_page
        self.data = data
        self.error_code = error_code
        self.message = message
        self.page_size = page_size
        self.request_id = request_id
        self.success = success
        self.total_size = total_size

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_size is not None:
            result['TotalSize'] = self.total_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('Data') is not None:
            temp_model = ListApplicationsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalSize') is not None:
            self.total_size = m.get('TotalSize')
        return self


class ListApplicationsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListApplicationsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = ListApplicationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListChangeOrdersRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        co_status: str = None,
        co_type: str = None,
        current_page: int = None,
        key: str = None,
        page_size: int = None,
    ):
        self.app_id = app_id
        self.co_status = co_status
        self.co_type = co_type
        self.current_page = current_page
        self.key = key
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.co_status is not None:
            result['CoStatus'] = self.co_status
        if self.co_type is not None:
            result['CoType'] = self.co_type
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.key is not None:
            result['Key'] = self.key
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CoStatus') is not None:
            self.co_status = m.get('CoStatus')
        if m.get('CoType') is not None:
            self.co_type = m.get('CoType')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListChangeOrdersResponseBodyDataChangeOrderList(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        batch_count: int = None,
        batch_type: str = None,
        change_order_id: str = None,
        co_type: str = None,
        co_type_code: str = None,
        create_time: str = None,
        create_user_id: str = None,
        description: str = None,
        finish_time: str = None,
        group_id: str = None,
        source: str = None,
        status: int = None,
        user_id: str = None,
    ):
        self.app_id = app_id
        self.batch_count = batch_count
        self.batch_type = batch_type
        self.change_order_id = change_order_id
        self.co_type = co_type
        self.co_type_code = co_type_code
        self.create_time = create_time
        self.create_user_id = create_user_id
        self.description = description
        self.finish_time = finish_time
        self.group_id = group_id
        self.source = source
        self.status = status
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.batch_count is not None:
            result['BatchCount'] = self.batch_count
        if self.batch_type is not None:
            result['BatchType'] = self.batch_type
        if self.change_order_id is not None:
            result['ChangeOrderId'] = self.change_order_id
        if self.co_type is not None:
            result['CoType'] = self.co_type
        if self.co_type_code is not None:
            result['CoTypeCode'] = self.co_type_code
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_user_id is not None:
            result['CreateUserId'] = self.create_user_id
        if self.description is not None:
            result['Description'] = self.description
        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.source is not None:
            result['Source'] = self.source
        if self.status is not None:
            result['Status'] = self.status
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('BatchCount') is not None:
            self.batch_count = m.get('BatchCount')
        if m.get('BatchType') is not None:
            self.batch_type = m.get('BatchType')
        if m.get('ChangeOrderId') is not None:
            self.change_order_id = m.get('ChangeOrderId')
        if m.get('CoType') is not None:
            self.co_type = m.get('CoType')
        if m.get('CoTypeCode') is not None:
            self.co_type_code = m.get('CoTypeCode')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateUserId') is not None:
            self.create_user_id = m.get('CreateUserId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class ListChangeOrdersResponseBodyData(TeaModel):
    def __init__(
        self,
        change_order_list: List[ListChangeOrdersResponseBodyDataChangeOrderList] = None,
        current_page: int = None,
        page_size: int = None,
        total_size: int = None,
    ):
        self.change_order_list = change_order_list
        self.current_page = current_page
        self.page_size = page_size
        self.total_size = total_size

    def validate(self):
        if self.change_order_list:
            for k in self.change_order_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ChangeOrderList'] = []
        if self.change_order_list is not None:
            for k in self.change_order_list:
                result['ChangeOrderList'].append(k.to_map() if k else None)
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_size is not None:
            result['TotalSize'] = self.total_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.change_order_list = []
        if m.get('ChangeOrderList') is not None:
            for k in m.get('ChangeOrderList'):
                temp_model = ListChangeOrdersResponseBodyDataChangeOrderList()
                self.change_order_list.append(temp_model.from_map(k))
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalSize') is not None:
            self.total_size = m.get('TotalSize')
        return self


class ListChangeOrdersResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListChangeOrdersResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = ListChangeOrdersResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class ListChangeOrdersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListChangeOrdersResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = ListChangeOrdersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListConsumedServicesRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
    ):
        self.app_id = app_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        return self


class ListConsumedServicesResponseBodyData(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        group_2ip: str = None,
        groups: List[str] = None,
        ips: List[str] = None,
        name: str = None,
        type: str = None,
        version: str = None,
    ):
        self.app_id = app_id
        self.group_2ip = group_2ip
        self.groups = groups
        self.ips = ips
        self.name = name
        self.type = type
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.group_2ip is not None:
            result['Group2Ip'] = self.group_2ip
        if self.groups is not None:
            result['Groups'] = self.groups
        if self.ips is not None:
            result['Ips'] = self.ips
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Group2Ip') is not None:
            self.group_2ip = m.get('Group2Ip')
        if m.get('Groups') is not None:
            self.groups = m.get('Groups')
        if m.get('Ips') is not None:
            self.ips = m.get('Ips')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class ListConsumedServicesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[ListConsumedServicesResponseBodyData] = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListConsumedServicesResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class ListConsumedServicesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListConsumedServicesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = ListConsumedServicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListGreyTagRouteRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
    ):
        self.app_id = app_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        return self


class ListGreyTagRouteResponseBodyDataResultAlbRulesItems(TeaModel):
    def __init__(
        self,
        cond: str = None,
        expr: str = None,
        index: int = None,
        name: str = None,
        operator: str = None,
        type: str = None,
        value: str = None,
    ):
        self.cond = cond
        self.expr = expr
        self.index = index
        self.name = name
        self.operator = operator
        self.type = type
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cond is not None:
            result['cond'] = self.cond
        if self.expr is not None:
            result['expr'] = self.expr
        if self.index is not None:
            result['index'] = self.index
        if self.name is not None:
            result['name'] = self.name
        if self.operator is not None:
            result['operator'] = self.operator
        if self.type is not None:
            result['type'] = self.type
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cond') is not None:
            self.cond = m.get('cond')
        if m.get('expr') is not None:
            self.expr = m.get('expr')
        if m.get('index') is not None:
            self.index = m.get('index')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('operator') is not None:
            self.operator = m.get('operator')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class ListGreyTagRouteResponseBodyDataResultAlbRules(TeaModel):
    def __init__(
        self,
        condition: str = None,
        ingress_id: str = None,
        items: List[ListGreyTagRouteResponseBodyDataResultAlbRulesItems] = None,
        service_id: str = None,
    ):
        self.condition = condition
        self.ingress_id = ingress_id
        self.items = items
        self.service_id = service_id

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.condition is not None:
            result['condition'] = self.condition
        if self.ingress_id is not None:
            result['ingressId'] = self.ingress_id
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        if self.service_id is not None:
            result['serviceId'] = self.service_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('condition') is not None:
            self.condition = m.get('condition')
        if m.get('ingressId') is not None:
            self.ingress_id = m.get('ingressId')
        self.items = []
        if m.get('items') is not None:
            for k in m.get('items'):
                temp_model = ListGreyTagRouteResponseBodyDataResultAlbRulesItems()
                self.items.append(temp_model.from_map(k))
        if m.get('serviceId') is not None:
            self.service_id = m.get('serviceId')
        return self


class ListGreyTagRouteResponseBodyDataResultDubboRulesItems(TeaModel):
    def __init__(
        self,
        cond: str = None,
        expr: str = None,
        index: int = None,
        name: str = None,
        operator: str = None,
        type: str = None,
        value: str = None,
    ):
        self.cond = cond
        self.expr = expr
        self.index = index
        self.name = name
        self.operator = operator
        self.type = type
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cond is not None:
            result['cond'] = self.cond
        if self.expr is not None:
            result['expr'] = self.expr
        if self.index is not None:
            result['index'] = self.index
        if self.name is not None:
            result['name'] = self.name
        if self.operator is not None:
            result['operator'] = self.operator
        if self.type is not None:
            result['type'] = self.type
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cond') is not None:
            self.cond = m.get('cond')
        if m.get('expr') is not None:
            self.expr = m.get('expr')
        if m.get('index') is not None:
            self.index = m.get('index')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('operator') is not None:
            self.operator = m.get('operator')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class ListGreyTagRouteResponseBodyDataResultDubboRules(TeaModel):
    def __init__(
        self,
        condition: str = None,
        group: str = None,
        items: List[ListGreyTagRouteResponseBodyDataResultDubboRulesItems] = None,
        method_name: str = None,
        service_name: str = None,
        version: str = None,
    ):
        self.condition = condition
        self.group = group
        self.items = items
        self.method_name = method_name
        self.service_name = service_name
        self.version = version

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.condition is not None:
            result['condition'] = self.condition
        if self.group is not None:
            result['group'] = self.group
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        if self.method_name is not None:
            result['methodName'] = self.method_name
        if self.service_name is not None:
            result['serviceName'] = self.service_name
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('condition') is not None:
            self.condition = m.get('condition')
        if m.get('group') is not None:
            self.group = m.get('group')
        self.items = []
        if m.get('items') is not None:
            for k in m.get('items'):
                temp_model = ListGreyTagRouteResponseBodyDataResultDubboRulesItems()
                self.items.append(temp_model.from_map(k))
        if m.get('methodName') is not None:
            self.method_name = m.get('methodName')
        if m.get('serviceName') is not None:
            self.service_name = m.get('serviceName')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class ListGreyTagRouteResponseBodyDataResultScRulesItems(TeaModel):
    def __init__(
        self,
        cond: str = None,
        expr: str = None,
        index: int = None,
        name: str = None,
        operator: str = None,
        type: str = None,
        value: str = None,
    ):
        self.cond = cond
        self.expr = expr
        self.index = index
        self.name = name
        self.operator = operator
        self.type = type
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cond is not None:
            result['cond'] = self.cond
        if self.expr is not None:
            result['expr'] = self.expr
        if self.index is not None:
            result['index'] = self.index
        if self.name is not None:
            result['name'] = self.name
        if self.operator is not None:
            result['operator'] = self.operator
        if self.type is not None:
            result['type'] = self.type
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cond') is not None:
            self.cond = m.get('cond')
        if m.get('expr') is not None:
            self.expr = m.get('expr')
        if m.get('index') is not None:
            self.index = m.get('index')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('operator') is not None:
            self.operator = m.get('operator')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class ListGreyTagRouteResponseBodyDataResultScRules(TeaModel):
    def __init__(
        self,
        condition: str = None,
        items: List[ListGreyTagRouteResponseBodyDataResultScRulesItems] = None,
        path: str = None,
    ):
        self.condition = condition
        self.items = items
        self.path = path

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.condition is not None:
            result['condition'] = self.condition
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        if self.path is not None:
            result['path'] = self.path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('condition') is not None:
            self.condition = m.get('condition')
        self.items = []
        if m.get('items') is not None:
            for k in m.get('items'):
                temp_model = ListGreyTagRouteResponseBodyDataResultScRulesItems()
                self.items.append(temp_model.from_map(k))
        if m.get('path') is not None:
            self.path = m.get('path')
        return self


class ListGreyTagRouteResponseBodyDataResult(TeaModel):
    def __init__(
        self,
        alb_rules: List[ListGreyTagRouteResponseBodyDataResultAlbRules] = None,
        create_time: int = None,
        description: str = None,
        dubbo_rules: List[ListGreyTagRouteResponseBodyDataResultDubboRules] = None,
        grey_tag_route_id: int = None,
        name: str = None,
        sc_rules: List[ListGreyTagRouteResponseBodyDataResultScRules] = None,
        update_time: int = None,
    ):
        self.alb_rules = alb_rules
        self.create_time = create_time
        self.description = description
        self.dubbo_rules = dubbo_rules
        self.grey_tag_route_id = grey_tag_route_id
        self.name = name
        self.sc_rules = sc_rules
        self.update_time = update_time

    def validate(self):
        if self.alb_rules:
            for k in self.alb_rules:
                if k:
                    k.validate()
        if self.dubbo_rules:
            for k in self.dubbo_rules:
                if k:
                    k.validate()
        if self.sc_rules:
            for k in self.sc_rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AlbRules'] = []
        if self.alb_rules is not None:
            for k in self.alb_rules:
                result['AlbRules'].append(k.to_map() if k else None)
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        result['DubboRules'] = []
        if self.dubbo_rules is not None:
            for k in self.dubbo_rules:
                result['DubboRules'].append(k.to_map() if k else None)
        if self.grey_tag_route_id is not None:
            result['GreyTagRouteId'] = self.grey_tag_route_id
        if self.name is not None:
            result['Name'] = self.name
        result['ScRules'] = []
        if self.sc_rules is not None:
            for k in self.sc_rules:
                result['ScRules'].append(k.to_map() if k else None)
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.alb_rules = []
        if m.get('AlbRules') is not None:
            for k in m.get('AlbRules'):
                temp_model = ListGreyTagRouteResponseBodyDataResultAlbRules()
                self.alb_rules.append(temp_model.from_map(k))
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        self.dubbo_rules = []
        if m.get('DubboRules') is not None:
            for k in m.get('DubboRules'):
                temp_model = ListGreyTagRouteResponseBodyDataResultDubboRules()
                self.dubbo_rules.append(temp_model.from_map(k))
        if m.get('GreyTagRouteId') is not None:
            self.grey_tag_route_id = m.get('GreyTagRouteId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        self.sc_rules = []
        if m.get('ScRules') is not None:
            for k in m.get('ScRules'):
                temp_model = ListGreyTagRouteResponseBodyDataResultScRules()
                self.sc_rules.append(temp_model.from_map(k))
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class ListGreyTagRouteResponseBodyData(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        result: List[ListGreyTagRouteResponseBodyDataResult] = None,
        total_size: int = None,
    ):
        self.current_page = current_page
        self.page_size = page_size
        self.result = result
        self.total_size = total_size

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.total_size is not None:
            result['TotalSize'] = self.total_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListGreyTagRouteResponseBodyDataResult()
                self.result.append(temp_model.from_map(k))
        if m.get('TotalSize') is not None:
            self.total_size = m.get('TotalSize')
        return self


class ListGreyTagRouteResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListGreyTagRouteResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = ListGreyTagRouteResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class ListGreyTagRouteResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListGreyTagRouteResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = ListGreyTagRouteResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListIngressesRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        namespace_id: str = None,
    ):
        self.app_id = app_id
        self.namespace_id = namespace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        return self


class ListIngressesResponseBodyDataIngressList(TeaModel):
    def __init__(
        self,
        cert_id: str = None,
        cert_ids: str = None,
        description: str = None,
        id: int = None,
        listener_port: str = None,
        listener_protocol: str = None,
        load_balance_type: str = None,
        name: str = None,
        namespace_id: str = None,
        slb_id: str = None,
        slb_type: str = None,
    ):
        self.cert_id = cert_id
        self.cert_ids = cert_ids
        self.description = description
        self.id = id
        self.listener_port = listener_port
        self.listener_protocol = listener_protocol
        self.load_balance_type = load_balance_type
        self.name = name
        self.namespace_id = namespace_id
        # SLB ID。
        self.slb_id = slb_id
        self.slb_type = slb_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_id is not None:
            result['CertId'] = self.cert_id
        if self.cert_ids is not None:
            result['CertIds'] = self.cert_ids
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port
        if self.listener_protocol is not None:
            result['ListenerProtocol'] = self.listener_protocol
        if self.load_balance_type is not None:
            result['LoadBalanceType'] = self.load_balance_type
        if self.name is not None:
            result['Name'] = self.name
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.slb_id is not None:
            result['SlbId'] = self.slb_id
        if self.slb_type is not None:
            result['SlbType'] = self.slb_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertId') is not None:
            self.cert_id = m.get('CertId')
        if m.get('CertIds') is not None:
            self.cert_ids = m.get('CertIds')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')
        if m.get('ListenerProtocol') is not None:
            self.listener_protocol = m.get('ListenerProtocol')
        if m.get('LoadBalanceType') is not None:
            self.load_balance_type = m.get('LoadBalanceType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('SlbId') is not None:
            self.slb_id = m.get('SlbId')
        if m.get('SlbType') is not None:
            self.slb_type = m.get('SlbType')
        return self


class ListIngressesResponseBodyData(TeaModel):
    def __init__(
        self,
        ingress_list: List[ListIngressesResponseBodyDataIngressList] = None,
    ):
        self.ingress_list = ingress_list

    def validate(self):
        if self.ingress_list:
            for k in self.ingress_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['IngressList'] = []
        if self.ingress_list is not None:
            for k in self.ingress_list:
                result['IngressList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ingress_list = []
        if m.get('IngressList') is not None:
            for k in m.get('IngressList'):
                temp_model = ListIngressesResponseBodyDataIngressList()
                self.ingress_list.append(temp_model.from_map(k))
        return self


class ListIngressesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListIngressesResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = ListIngressesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class ListIngressesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListIngressesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = ListIngressesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListJobsRequest(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        current_page: int = None,
        field_type: str = None,
        field_value: str = None,
        namespace_id: str = None,
        order_by: str = None,
        page_size: int = None,
        reverse: bool = None,
        tags: str = None,
        workload: str = None,
    ):
        self.app_name = app_name
        self.current_page = current_page
        self.field_type = field_type
        self.field_value = field_value
        self.namespace_id = namespace_id
        self.order_by = order_by
        self.page_size = page_size
        self.reverse = reverse
        self.tags = tags
        self.workload = workload

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.field_type is not None:
            result['FieldType'] = self.field_type
        if self.field_value is not None:
            result['FieldValue'] = self.field_value
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.order_by is not None:
            result['OrderBy'] = self.order_by
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.reverse is not None:
            result['Reverse'] = self.reverse
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.workload is not None:
            result['Workload'] = self.workload
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('FieldType') is not None:
            self.field_type = m.get('FieldType')
        if m.get('FieldValue') is not None:
            self.field_value = m.get('FieldValue')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Reverse') is not None:
            self.reverse = m.get('Reverse')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('Workload') is not None:
            self.workload = m.get('Workload')
        return self


class ListJobsResponseBodyDataApplicationsTags(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListJobsResponseBodyDataApplications(TeaModel):
    def __init__(
        self,
        active: int = None,
        app_description: str = None,
        app_id: str = None,
        app_name: str = None,
        completion_time: int = None,
        failed: int = None,
        last_changeorder_state: str = None,
        last_job_state: str = None,
        last_start_time: int = None,
        namespace_id: str = None,
        region_id: str = None,
        succeeded: int = None,
        suspend: bool = None,
        tags: List[ListJobsResponseBodyDataApplicationsTags] = None,
        trigger_config: str = None,
    ):
        self.active = active
        self.app_description = app_description
        self.app_id = app_id
        self.app_name = app_name
        self.completion_time = completion_time
        self.failed = failed
        self.last_changeorder_state = last_changeorder_state
        self.last_job_state = last_job_state
        self.last_start_time = last_start_time
        self.namespace_id = namespace_id
        self.region_id = region_id
        self.succeeded = succeeded
        self.suspend = suspend
        self.tags = tags
        self.trigger_config = trigger_config

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active is not None:
            result['Active'] = self.active
        if self.app_description is not None:
            result['AppDescription'] = self.app_description
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.completion_time is not None:
            result['CompletionTime'] = self.completion_time
        if self.failed is not None:
            result['Failed'] = self.failed
        if self.last_changeorder_state is not None:
            result['LastChangeorderState'] = self.last_changeorder_state
        if self.last_job_state is not None:
            result['LastJobState'] = self.last_job_state
        if self.last_start_time is not None:
            result['LastStartTime'] = self.last_start_time
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.succeeded is not None:
            result['Succeeded'] = self.succeeded
        if self.suspend is not None:
            result['Suspend'] = self.suspend
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.trigger_config is not None:
            result['TriggerConfig'] = self.trigger_config
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Active') is not None:
            self.active = m.get('Active')
        if m.get('AppDescription') is not None:
            self.app_description = m.get('AppDescription')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('CompletionTime') is not None:
            self.completion_time = m.get('CompletionTime')
        if m.get('Failed') is not None:
            self.failed = m.get('Failed')
        if m.get('LastChangeorderState') is not None:
            self.last_changeorder_state = m.get('LastChangeorderState')
        if m.get('LastJobState') is not None:
            self.last_job_state = m.get('LastJobState')
        if m.get('LastStartTime') is not None:
            self.last_start_time = m.get('LastStartTime')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Succeeded') is not None:
            self.succeeded = m.get('Succeeded')
        if m.get('Suspend') is not None:
            self.suspend = m.get('Suspend')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListJobsResponseBodyDataApplicationsTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('TriggerConfig') is not None:
            self.trigger_config = m.get('TriggerConfig')
        return self


class ListJobsResponseBodyData(TeaModel):
    def __init__(
        self,
        applications: List[ListJobsResponseBodyDataApplications] = None,
        current_page: int = None,
        page_size: int = None,
        total_size: int = None,
    ):
        self.applications = applications
        self.current_page = current_page
        self.page_size = page_size
        self.total_size = total_size

    def validate(self):
        if self.applications:
            for k in self.applications:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Applications'] = []
        if self.applications is not None:
            for k in self.applications:
                result['Applications'].append(k.to_map() if k else None)
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_size is not None:
            result['TotalSize'] = self.total_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.applications = []
        if m.get('Applications') is not None:
            for k in m.get('Applications'):
                temp_model = ListJobsResponseBodyDataApplications()
                self.applications.append(temp_model.from_map(k))
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalSize') is not None:
            self.total_size = m.get('TotalSize')
        return self


class ListJobsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        current_page: int = None,
        data: ListJobsResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_size: int = None,
    ):
        self.code = code
        self.current_page = current_page
        self.data = data
        self.error_code = error_code
        self.message = message
        self.page_size = page_size
        self.request_id = request_id
        self.success = success
        self.total_size = total_size

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_size is not None:
            result['TotalSize'] = self.total_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('Data') is not None:
            temp_model = ListJobsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalSize') is not None:
            self.total_size = m.get('TotalSize')
        return self


class ListJobsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListJobsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = ListJobsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListLogConfigsRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        current_page: int = None,
        page_size: int = None,
    ):
        self.app_id = app_id
        self.current_page = current_page
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListLogConfigsResponseBodyDataLogConfigs(TeaModel):
    def __init__(
        self,
        config_name: str = None,
        create_time: str = None,
        log_dir: str = None,
        log_type: str = None,
        region_id: str = None,
        sls_log_store: str = None,
        sls_project: str = None,
        store_type: str = None,
    ):
        self.config_name = config_name
        self.create_time = create_time
        self.log_dir = log_dir
        self.log_type = log_type
        self.region_id = region_id
        self.sls_log_store = sls_log_store
        self.sls_project = sls_project
        self.store_type = store_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_name is not None:
            result['ConfigName'] = self.config_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.log_dir is not None:
            result['LogDir'] = self.log_dir
        if self.log_type is not None:
            result['LogType'] = self.log_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.sls_log_store is not None:
            result['SlsLogStore'] = self.sls_log_store
        if self.sls_project is not None:
            result['SlsProject'] = self.sls_project
        if self.store_type is not None:
            result['StoreType'] = self.store_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigName') is not None:
            self.config_name = m.get('ConfigName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('LogDir') is not None:
            self.log_dir = m.get('LogDir')
        if m.get('LogType') is not None:
            self.log_type = m.get('LogType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SlsLogStore') is not None:
            self.sls_log_store = m.get('SlsLogStore')
        if m.get('SlsProject') is not None:
            self.sls_project = m.get('SlsProject')
        if m.get('StoreType') is not None:
            self.store_type = m.get('StoreType')
        return self


class ListLogConfigsResponseBodyData(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        log_configs: List[ListLogConfigsResponseBodyDataLogConfigs] = None,
        page_size: int = None,
        total_size: int = None,
    ):
        self.current_page = current_page
        self.log_configs = log_configs
        self.page_size = page_size
        self.total_size = total_size

    def validate(self):
        if self.log_configs:
            for k in self.log_configs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['LogConfigs'] = []
        if self.log_configs is not None:
            for k in self.log_configs:
                result['LogConfigs'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_size is not None:
            result['TotalSize'] = self.total_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.log_configs = []
        if m.get('LogConfigs') is not None:
            for k in m.get('LogConfigs'):
                temp_model = ListLogConfigsResponseBodyDataLogConfigs()
                self.log_configs.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalSize') is not None:
            self.total_size = m.get('TotalSize')
        return self


class ListLogConfigsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListLogConfigsResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = ListLogConfigsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class ListLogConfigsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListLogConfigsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = ListLogConfigsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListNamespaceChangeOrdersRequest(TeaModel):
    def __init__(
        self,
        co_status: str = None,
        co_type: str = None,
        current_page: int = None,
        key: str = None,
        namespace_id: str = None,
        page_size: int = None,
    ):
        self.co_status = co_status
        self.co_type = co_type
        self.current_page = current_page
        self.key = key
        self.namespace_id = namespace_id
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.co_status is not None:
            result['CoStatus'] = self.co_status
        if self.co_type is not None:
            result['CoType'] = self.co_type
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.key is not None:
            result['Key'] = self.key
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CoStatus') is not None:
            self.co_status = m.get('CoStatus')
        if m.get('CoType') is not None:
            self.co_type = m.get('CoType')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListNamespaceChangeOrdersResponseBodyDataChangeOrderList(TeaModel):
    def __init__(
        self,
        batch_count: int = None,
        batch_type: str = None,
        change_order_id: str = None,
        co_type: str = None,
        co_type_code: str = None,
        create_time: str = None,
        create_user_id: str = None,
        description: str = None,
        finish_time: str = None,
        group_id: str = None,
        namespace_id: str = None,
        pipelines: str = None,
        source: str = None,
        status: int = None,
        user_id: str = None,
    ):
        self.batch_count = batch_count
        self.batch_type = batch_type
        self.change_order_id = change_order_id
        self.co_type = co_type
        self.co_type_code = co_type_code
        self.create_time = create_time
        self.create_user_id = create_user_id
        self.description = description
        self.finish_time = finish_time
        self.group_id = group_id
        self.namespace_id = namespace_id
        self.pipelines = pipelines
        self.source = source
        self.status = status
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.batch_count is not None:
            result['BatchCount'] = self.batch_count
        if self.batch_type is not None:
            result['BatchType'] = self.batch_type
        if self.change_order_id is not None:
            result['ChangeOrderId'] = self.change_order_id
        if self.co_type is not None:
            result['CoType'] = self.co_type
        if self.co_type_code is not None:
            result['CoTypeCode'] = self.co_type_code
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_user_id is not None:
            result['CreateUserId'] = self.create_user_id
        if self.description is not None:
            result['Description'] = self.description
        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.pipelines is not None:
            result['Pipelines'] = self.pipelines
        if self.source is not None:
            result['Source'] = self.source
        if self.status is not None:
            result['Status'] = self.status
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BatchCount') is not None:
            self.batch_count = m.get('BatchCount')
        if m.get('BatchType') is not None:
            self.batch_type = m.get('BatchType')
        if m.get('ChangeOrderId') is not None:
            self.change_order_id = m.get('ChangeOrderId')
        if m.get('CoType') is not None:
            self.co_type = m.get('CoType')
        if m.get('CoTypeCode') is not None:
            self.co_type_code = m.get('CoTypeCode')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateUserId') is not None:
            self.create_user_id = m.get('CreateUserId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('Pipelines') is not None:
            self.pipelines = m.get('Pipelines')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class ListNamespaceChangeOrdersResponseBodyData(TeaModel):
    def __init__(
        self,
        change_order_list: List[ListNamespaceChangeOrdersResponseBodyDataChangeOrderList] = None,
        current_page: int = None,
        page_size: int = None,
        total_size: int = None,
    ):
        self.change_order_list = change_order_list
        self.current_page = current_page
        self.page_size = page_size
        self.total_size = total_size

    def validate(self):
        if self.change_order_list:
            for k in self.change_order_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ChangeOrderList'] = []
        if self.change_order_list is not None:
            for k in self.change_order_list:
                result['ChangeOrderList'].append(k.to_map() if k else None)
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_size is not None:
            result['TotalSize'] = self.total_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.change_order_list = []
        if m.get('ChangeOrderList') is not None:
            for k in m.get('ChangeOrderList'):
                temp_model = ListNamespaceChangeOrdersResponseBodyDataChangeOrderList()
                self.change_order_list.append(temp_model.from_map(k))
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalSize') is not None:
            self.total_size = m.get('TotalSize')
        return self


class ListNamespaceChangeOrdersResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListNamespaceChangeOrdersResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = ListNamespaceChangeOrdersResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class ListNamespaceChangeOrdersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListNamespaceChangeOrdersResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = ListNamespaceChangeOrdersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListNamespacedConfigMapsRequest(TeaModel):
    def __init__(
        self,
        namespace_id: str = None,
    ):
        self.namespace_id = namespace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        return self


class ListNamespacedConfigMapsResponseBodyDataConfigMapsRelateApps(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        app_name: str = None,
    ):
        self.app_id = app_id
        self.app_name = app_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        return self


class ListNamespacedConfigMapsResponseBodyDataConfigMaps(TeaModel):
    def __init__(
        self,
        config_map_id: int = None,
        create_time: int = None,
        data: Dict[str, Any] = None,
        description: str = None,
        name: str = None,
        namespace_id: str = None,
        relate_apps: List[ListNamespacedConfigMapsResponseBodyDataConfigMapsRelateApps] = None,
        update_time: int = None,
    ):
        self.config_map_id = config_map_id
        self.create_time = create_time
        self.data = data
        self.description = description
        self.name = name
        self.namespace_id = namespace_id
        self.relate_apps = relate_apps
        self.update_time = update_time

    def validate(self):
        if self.relate_apps:
            for k in self.relate_apps:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_map_id is not None:
            result['ConfigMapId'] = self.config_map_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.data is not None:
            result['Data'] = self.data
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        result['RelateApps'] = []
        if self.relate_apps is not None:
            for k in self.relate_apps:
                result['RelateApps'].append(k.to_map() if k else None)
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigMapId') is not None:
            self.config_map_id = m.get('ConfigMapId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        self.relate_apps = []
        if m.get('RelateApps') is not None:
            for k in m.get('RelateApps'):
                temp_model = ListNamespacedConfigMapsResponseBodyDataConfigMapsRelateApps()
                self.relate_apps.append(temp_model.from_map(k))
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class ListNamespacedConfigMapsResponseBodyData(TeaModel):
    def __init__(
        self,
        config_maps: List[ListNamespacedConfigMapsResponseBodyDataConfigMaps] = None,
    ):
        self.config_maps = config_maps

    def validate(self):
        if self.config_maps:
            for k in self.config_maps:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ConfigMaps'] = []
        if self.config_maps is not None:
            for k in self.config_maps:
                result['ConfigMaps'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.config_maps = []
        if m.get('ConfigMaps') is not None:
            for k in m.get('ConfigMaps'):
                temp_model = ListNamespacedConfigMapsResponseBodyDataConfigMaps()
                self.config_maps.append(temp_model.from_map(k))
        return self


class ListNamespacedConfigMapsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListNamespacedConfigMapsResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = ListNamespacedConfigMapsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class ListNamespacedConfigMapsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListNamespacedConfigMapsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = ListNamespacedConfigMapsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPublishedServicesRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
    ):
        self.app_id = app_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        return self


class ListPublishedServicesResponseBodyData(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        group_2ip: str = None,
        groups: List[str] = None,
        ips: List[str] = None,
        name: str = None,
        type: str = None,
        version: str = None,
    ):
        self.app_id = app_id
        self.group_2ip = group_2ip
        self.groups = groups
        self.ips = ips
        self.name = name
        self.type = type
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.group_2ip is not None:
            result['Group2Ip'] = self.group_2ip
        if self.groups is not None:
            result['Groups'] = self.groups
        if self.ips is not None:
            result['Ips'] = self.ips
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Group2Ip') is not None:
            self.group_2ip = m.get('Group2Ip')
        if m.get('Groups') is not None:
            self.groups = m.get('Groups')
        if m.get('Ips') is not None:
            self.ips = m.get('Ips')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class ListPublishedServicesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[ListPublishedServicesResponseBodyData] = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListPublishedServicesResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class ListPublishedServicesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListPublishedServicesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = ListPublishedServicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSecretsRequest(TeaModel):
    def __init__(
        self,
        namespace_id: str = None,
    ):
        self.namespace_id = namespace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        return self


class ListSecretsResponseBodyDataSecretsRelateApps(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        app_name: str = None,
    ):
        self.app_id = app_id
        self.app_name = app_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        return self


class ListSecretsResponseBodyDataSecrets(TeaModel):
    def __init__(
        self,
        create_time: int = None,
        namespace_id: str = None,
        relate_apps: List[ListSecretsResponseBodyDataSecretsRelateApps] = None,
        secret_id: int = None,
        secret_name: str = None,
        secret_type: str = None,
        update_time: int = None,
    ):
        self.create_time = create_time
        self.namespace_id = namespace_id
        self.relate_apps = relate_apps
        self.secret_id = secret_id
        self.secret_name = secret_name
        self.secret_type = secret_type
        self.update_time = update_time

    def validate(self):
        if self.relate_apps:
            for k in self.relate_apps:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        result['RelateApps'] = []
        if self.relate_apps is not None:
            for k in self.relate_apps:
                result['RelateApps'].append(k.to_map() if k else None)
        if self.secret_id is not None:
            result['SecretId'] = self.secret_id
        if self.secret_name is not None:
            result['SecretName'] = self.secret_name
        if self.secret_type is not None:
            result['SecretType'] = self.secret_type
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        self.relate_apps = []
        if m.get('RelateApps') is not None:
            for k in m.get('RelateApps'):
                temp_model = ListSecretsResponseBodyDataSecretsRelateApps()
                self.relate_apps.append(temp_model.from_map(k))
        if m.get('SecretId') is not None:
            self.secret_id = m.get('SecretId')
        if m.get('SecretName') is not None:
            self.secret_name = m.get('SecretName')
        if m.get('SecretType') is not None:
            self.secret_type = m.get('SecretType')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class ListSecretsResponseBodyData(TeaModel):
    def __init__(
        self,
        secrets: List[ListSecretsResponseBodyDataSecrets] = None,
    ):
        self.secrets = secrets

    def validate(self):
        if self.secrets:
            for k in self.secrets:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Secrets'] = []
        if self.secrets is not None:
            for k in self.secrets:
                result['Secrets'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.secrets = []
        if m.get('Secrets') is not None:
            for k in m.get('Secrets'):
                temp_model = ListSecretsResponseBodyDataSecrets()
                self.secrets.append(temp_model.from_map(k))
        return self


class ListSecretsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListSecretsResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = ListSecretsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class ListSecretsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListSecretsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = ListSecretsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagResourcesRequest(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        region_id: str = None,
        resource_ids: str = None,
        resource_type: str = None,
        tags: str = None,
    ):
        self.next_token = next_token
        self.region_id = region_id
        self.resource_ids = resource_ids
        self.resource_type = resource_type
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_ids is not None:
            result['ResourceIds'] = self.resource_ids
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceIds') is not None:
            self.resource_ids = m.get('ResourceIds')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        return self


class ListTagResourcesResponseBodyDataTagResources(TeaModel):
    def __init__(
        self,
        resource_id: str = None,
        resource_type: str = None,
        tag_key: str = None,
        tag_value: str = None,
    ):
        self.resource_id = resource_id
        self.resource_type = resource_type
        self.tag_key = tag_key
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        return self


class ListTagResourcesResponseBodyData(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        tag_resources: List[ListTagResourcesResponseBodyDataTagResources] = None,
    ):
        self.next_token = next_token
        self.tag_resources = tag_resources

    def validate(self):
        if self.tag_resources:
            for k in self.tag_resources:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        result['TagResources'] = []
        if self.tag_resources is not None:
            for k in self.tag_resources:
                result['TagResources'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.tag_resources = []
        if m.get('TagResources') is not None:
            for k in m.get('TagResources'):
                temp_model = ListTagResourcesResponseBodyDataTagResources()
                self.tag_resources.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListTagResourcesResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = ListTagResourcesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class ListTagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTagResourcesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = ListTagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OpenSaeServiceResponseBody(TeaModel):
    def __init__(
        self,
        order_id: str = None,
        request_id: str = None,
    ):
        self.order_id = order_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class OpenSaeServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: OpenSaeServiceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = OpenSaeServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryResourceStaticsRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
    ):
        self.app_id = app_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        return self


class QueryResourceStaticsResponseBodyDataRealTimeRes(TeaModel):
    def __init__(
        self,
        cpu: float = None,
        memory: float = None,
    ):
        self.cpu = cpu
        self.memory = memory

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.memory is not None:
            result['Memory'] = self.memory
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        return self


class QueryResourceStaticsResponseBodyDataSummary(TeaModel):
    def __init__(
        self,
        cpu: float = None,
        memory: float = None,
    ):
        self.cpu = cpu
        self.memory = memory

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.memory is not None:
            result['Memory'] = self.memory
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        return self


class QueryResourceStaticsResponseBodyData(TeaModel):
    def __init__(
        self,
        real_time_res: QueryResourceStaticsResponseBodyDataRealTimeRes = None,
        summary: QueryResourceStaticsResponseBodyDataSummary = None,
    ):
        self.real_time_res = real_time_res
        self.summary = summary

    def validate(self):
        if self.real_time_res:
            self.real_time_res.validate()
        if self.summary:
            self.summary.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.real_time_res is not None:
            result['RealTimeRes'] = self.real_time_res.to_map()
        if self.summary is not None:
            result['Summary'] = self.summary.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RealTimeRes') is not None:
            temp_model = QueryResourceStaticsResponseBodyDataRealTimeRes()
            self.real_time_res = temp_model.from_map(m['RealTimeRes'])
        if m.get('Summary') is not None:
            temp_model = QueryResourceStaticsResponseBodyDataSummary()
            self.summary = temp_model.from_map(m['Summary'])
        return self


class QueryResourceStaticsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: QueryResourceStaticsResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = QueryResourceStaticsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class QueryResourceStaticsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryResourceStaticsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = QueryResourceStaticsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReduceApplicationCapacityByInstanceIdsRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        instance_ids: str = None,
    ):
        self.app_id = app_id
        self.instance_ids = instance_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        return self


class ReduceApplicationCapacityByInstanceIdsResponseBodyData(TeaModel):
    def __init__(
        self,
        change_order_id: str = None,
    ):
        self.change_order_id = change_order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.change_order_id is not None:
            result['ChangeOrderId'] = self.change_order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChangeOrderId') is not None:
            self.change_order_id = m.get('ChangeOrderId')
        return self


class ReduceApplicationCapacityByInstanceIdsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ReduceApplicationCapacityByInstanceIdsResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = ReduceApplicationCapacityByInstanceIdsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class ReduceApplicationCapacityByInstanceIdsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ReduceApplicationCapacityByInstanceIdsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = ReduceApplicationCapacityByInstanceIdsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RescaleApplicationRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        auto_enable_application_scaling_rule: bool = None,
        min_ready_instance_ratio: int = None,
        min_ready_instances: int = None,
        replicas: int = None,
    ):
        self.app_id = app_id
        self.auto_enable_application_scaling_rule = auto_enable_application_scaling_rule
        self.min_ready_instance_ratio = min_ready_instance_ratio
        self.min_ready_instances = min_ready_instances
        self.replicas = replicas

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.auto_enable_application_scaling_rule is not None:
            result['AutoEnableApplicationScalingRule'] = self.auto_enable_application_scaling_rule
        if self.min_ready_instance_ratio is not None:
            result['MinReadyInstanceRatio'] = self.min_ready_instance_ratio
        if self.min_ready_instances is not None:
            result['MinReadyInstances'] = self.min_ready_instances
        if self.replicas is not None:
            result['Replicas'] = self.replicas
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AutoEnableApplicationScalingRule') is not None:
            self.auto_enable_application_scaling_rule = m.get('AutoEnableApplicationScalingRule')
        if m.get('MinReadyInstanceRatio') is not None:
            self.min_ready_instance_ratio = m.get('MinReadyInstanceRatio')
        if m.get('MinReadyInstances') is not None:
            self.min_ready_instances = m.get('MinReadyInstances')
        if m.get('Replicas') is not None:
            self.replicas = m.get('Replicas')
        return self


class RescaleApplicationResponseBodyData(TeaModel):
    def __init__(
        self,
        change_order_id: str = None,
    ):
        self.change_order_id = change_order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.change_order_id is not None:
            result['ChangeOrderId'] = self.change_order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChangeOrderId') is not None:
            self.change_order_id = m.get('ChangeOrderId')
        return self


class RescaleApplicationResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: RescaleApplicationResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
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
        if m.get('Data') is not None:
            temp_model = RescaleApplicationResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RescaleApplicationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RescaleApplicationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = RescaleApplicationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RescaleApplicationVerticallyRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        cpu: str = None,
        memory: str = None,
    ):
        self.app_id = app_id
        self.cpu = cpu
        self.memory = memory

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.memory is not None:
            result['Memory'] = self.memory
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        return self


class RescaleApplicationVerticallyResponseBodyData(TeaModel):
    def __init__(
        self,
        change_order_id: str = None,
    ):
        self.change_order_id = change_order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.change_order_id is not None:
            result['ChangeOrderId'] = self.change_order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChangeOrderId') is not None:
            self.change_order_id = m.get('ChangeOrderId')
        return self


class RescaleApplicationVerticallyResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: RescaleApplicationVerticallyResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = RescaleApplicationVerticallyResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class RescaleApplicationVerticallyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RescaleApplicationVerticallyResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = RescaleApplicationVerticallyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RestartApplicationRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        min_ready_instance_ratio: int = None,
        min_ready_instances: int = None,
    ):
        self.app_id = app_id
        self.min_ready_instance_ratio = min_ready_instance_ratio
        self.min_ready_instances = min_ready_instances

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.min_ready_instance_ratio is not None:
            result['MinReadyInstanceRatio'] = self.min_ready_instance_ratio
        if self.min_ready_instances is not None:
            result['MinReadyInstances'] = self.min_ready_instances
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('MinReadyInstanceRatio') is not None:
            self.min_ready_instance_ratio = m.get('MinReadyInstanceRatio')
        if m.get('MinReadyInstances') is not None:
            self.min_ready_instances = m.get('MinReadyInstances')
        return self


class RestartApplicationResponseBodyData(TeaModel):
    def __init__(
        self,
        change_order_id: str = None,
    ):
        self.change_order_id = change_order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.change_order_id is not None:
            result['ChangeOrderId'] = self.change_order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChangeOrderId') is not None:
            self.change_order_id = m.get('ChangeOrderId')
        return self


class RestartApplicationResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: RestartApplicationResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = RestartApplicationResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class RestartApplicationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RestartApplicationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = RestartApplicationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RestartInstancesRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        instance_ids: str = None,
    ):
        self.app_id = app_id
        self.instance_ids = instance_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        return self


class RestartInstancesResponseBodyData(TeaModel):
    def __init__(
        self,
        change_order_id: str = None,
    ):
        self.change_order_id = change_order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.change_order_id is not None:
            result['ChangeOrderId'] = self.change_order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChangeOrderId') is not None:
            self.change_order_id = m.get('ChangeOrderId')
        return self


class RestartInstancesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: RestartInstancesResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = RestartInstancesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class RestartInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RestartInstancesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = RestartInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RollbackApplicationRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        auto_enable_application_scaling_rule: str = None,
        batch_wait_time: int = None,
        min_ready_instance_ratio: int = None,
        min_ready_instances: int = None,
        update_strategy: str = None,
        version_id: str = None,
    ):
        self.app_id = app_id
        self.auto_enable_application_scaling_rule = auto_enable_application_scaling_rule
        self.batch_wait_time = batch_wait_time
        self.min_ready_instance_ratio = min_ready_instance_ratio
        self.min_ready_instances = min_ready_instances
        self.update_strategy = update_strategy
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.auto_enable_application_scaling_rule is not None:
            result['AutoEnableApplicationScalingRule'] = self.auto_enable_application_scaling_rule
        if self.batch_wait_time is not None:
            result['BatchWaitTime'] = self.batch_wait_time
        if self.min_ready_instance_ratio is not None:
            result['MinReadyInstanceRatio'] = self.min_ready_instance_ratio
        if self.min_ready_instances is not None:
            result['MinReadyInstances'] = self.min_ready_instances
        if self.update_strategy is not None:
            result['UpdateStrategy'] = self.update_strategy
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AutoEnableApplicationScalingRule') is not None:
            self.auto_enable_application_scaling_rule = m.get('AutoEnableApplicationScalingRule')
        if m.get('BatchWaitTime') is not None:
            self.batch_wait_time = m.get('BatchWaitTime')
        if m.get('MinReadyInstanceRatio') is not None:
            self.min_ready_instance_ratio = m.get('MinReadyInstanceRatio')
        if m.get('MinReadyInstances') is not None:
            self.min_ready_instances = m.get('MinReadyInstances')
        if m.get('UpdateStrategy') is not None:
            self.update_strategy = m.get('UpdateStrategy')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        return self


class RollbackApplicationResponseBodyData(TeaModel):
    def __init__(
        self,
        change_order_id: str = None,
        is_need_approval: bool = None,
    ):
        self.change_order_id = change_order_id
        self.is_need_approval = is_need_approval

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.change_order_id is not None:
            result['ChangeOrderId'] = self.change_order_id
        if self.is_need_approval is not None:
            result['IsNeedApproval'] = self.is_need_approval
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChangeOrderId') is not None:
            self.change_order_id = m.get('ChangeOrderId')
        if m.get('IsNeedApproval') is not None:
            self.is_need_approval = m.get('IsNeedApproval')
        return self


class RollbackApplicationResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: RollbackApplicationResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = RollbackApplicationResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class RollbackApplicationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RollbackApplicationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = RollbackApplicationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartApplicationRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
    ):
        self.app_id = app_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        return self


class StartApplicationResponseBodyData(TeaModel):
    def __init__(
        self,
        change_order_id: str = None,
    ):
        self.change_order_id = change_order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.change_order_id is not None:
            result['ChangeOrderId'] = self.change_order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChangeOrderId') is not None:
            self.change_order_id = m.get('ChangeOrderId')
        return self


class StartApplicationResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: StartApplicationResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = StartApplicationResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class StartApplicationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StartApplicationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = StartApplicationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopApplicationRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
    ):
        self.app_id = app_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        return self


class StopApplicationResponseBodyData(TeaModel):
    def __init__(
        self,
        change_order_id: str = None,
    ):
        self.change_order_id = change_order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.change_order_id is not None:
            result['ChangeOrderId'] = self.change_order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChangeOrderId') is not None:
            self.change_order_id = m.get('ChangeOrderId')
        return self


class StopApplicationResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: StopApplicationResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = StopApplicationResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class StopApplicationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StopApplicationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = StopApplicationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SuspendJobRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        suspend: bool = None,
    ):
        self.app_id = app_id
        self.suspend = suspend

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.suspend is not None:
            result['Suspend'] = self.suspend
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Suspend') is not None:
            self.suspend = m.get('Suspend')
        return self


class SuspendJobResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class SuspendJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SuspendJobResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = SuspendJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TagResourcesRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        resource_ids: str = None,
        resource_type: str = None,
        tags: str = None,
    ):
        self.region_id = region_id
        self.resource_ids = resource_ids
        self.resource_type = resource_type
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_ids is not None:
            result['ResourceIds'] = self.resource_ids
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceIds') is not None:
            self.resource_ids = m.get('ResourceIds')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        return self


class TagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class TagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: TagResourcesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = TagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnbindSlbRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        internet: bool = None,
        intranet: bool = None,
    ):
        self.app_id = app_id
        self.internet = internet
        self.intranet = intranet

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.internet is not None:
            result['Internet'] = self.internet
        if self.intranet is not None:
            result['Intranet'] = self.intranet
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Internet') is not None:
            self.internet = m.get('Internet')
        if m.get('Intranet') is not None:
            self.intranet = m.get('Intranet')
        return self


class UnbindSlbResponseBodyData(TeaModel):
    def __init__(
        self,
        change_order_id: str = None,
    ):
        self.change_order_id = change_order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.change_order_id is not None:
            result['ChangeOrderId'] = self.change_order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChangeOrderId') is not None:
            self.change_order_id = m.get('ChangeOrderId')
        return self


class UnbindSlbResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: UnbindSlbResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = UnbindSlbResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class UnbindSlbResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UnbindSlbResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = UnbindSlbResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UntagResourcesRequest(TeaModel):
    def __init__(
        self,
        delete_all: bool = None,
        region_id: str = None,
        resource_ids: str = None,
        resource_type: str = None,
        tag_keys: str = None,
    ):
        self.delete_all = delete_all
        self.region_id = region_id
        self.resource_ids = resource_ids
        self.resource_type = resource_type
        self.tag_keys = tag_keys

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delete_all is not None:
            result['DeleteAll'] = self.delete_all
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_ids is not None:
            result['ResourceIds'] = self.resource_ids
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tag_keys is not None:
            result['TagKeys'] = self.tag_keys
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeleteAll') is not None:
            self.delete_all = m.get('DeleteAll')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceIds') is not None:
            self.resource_ids = m.get('ResourceIds')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TagKeys') is not None:
            self.tag_keys = m.get('TagKeys')
        return self


class UntagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class UntagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UntagResourcesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = UntagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAppSecurityGroupRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        security_group_id: str = None,
    ):
        self.app_id = app_id
        self.security_group_id = security_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        return self


class UpdateAppSecurityGroupResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class UpdateAppSecurityGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateAppSecurityGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = UpdateAppSecurityGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateApplicationDescriptionRequest(TeaModel):
    def __init__(
        self,
        app_description: str = None,
        app_id: str = None,
    ):
        self.app_description = app_description
        self.app_id = app_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_description is not None:
            result['AppDescription'] = self.app_description
        if self.app_id is not None:
            result['AppId'] = self.app_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppDescription') is not None:
            self.app_description = m.get('AppDescription')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        return self


class UpdateApplicationDescriptionResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class UpdateApplicationDescriptionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateApplicationDescriptionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = UpdateApplicationDescriptionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateApplicationScalingRuleRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        min_ready_instance_ratio: int = None,
        min_ready_instances: int = None,
        scaling_rule_metric: str = None,
        scaling_rule_name: str = None,
        scaling_rule_timer: str = None,
    ):
        self.app_id = app_id
        self.min_ready_instance_ratio = min_ready_instance_ratio
        self.min_ready_instances = min_ready_instances
        self.scaling_rule_metric = scaling_rule_metric
        self.scaling_rule_name = scaling_rule_name
        self.scaling_rule_timer = scaling_rule_timer

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.min_ready_instance_ratio is not None:
            result['MinReadyInstanceRatio'] = self.min_ready_instance_ratio
        if self.min_ready_instances is not None:
            result['MinReadyInstances'] = self.min_ready_instances
        if self.scaling_rule_metric is not None:
            result['ScalingRuleMetric'] = self.scaling_rule_metric
        if self.scaling_rule_name is not None:
            result['ScalingRuleName'] = self.scaling_rule_name
        if self.scaling_rule_timer is not None:
            result['ScalingRuleTimer'] = self.scaling_rule_timer
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('MinReadyInstanceRatio') is not None:
            self.min_ready_instance_ratio = m.get('MinReadyInstanceRatio')
        if m.get('MinReadyInstances') is not None:
            self.min_ready_instances = m.get('MinReadyInstances')
        if m.get('ScalingRuleMetric') is not None:
            self.scaling_rule_metric = m.get('ScalingRuleMetric')
        if m.get('ScalingRuleName') is not None:
            self.scaling_rule_name = m.get('ScalingRuleName')
        if m.get('ScalingRuleTimer') is not None:
            self.scaling_rule_timer = m.get('ScalingRuleTimer')
        return self


class UpdateApplicationScalingRuleResponseBodyDataMetricMetrics(TeaModel):
    def __init__(
        self,
        metric_target_average_utilization: int = None,
        metric_type: str = None,
    ):
        self.metric_target_average_utilization = metric_target_average_utilization
        self.metric_type = metric_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.metric_target_average_utilization is not None:
            result['MetricTargetAverageUtilization'] = self.metric_target_average_utilization
        if self.metric_type is not None:
            result['MetricType'] = self.metric_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MetricTargetAverageUtilization') is not None:
            self.metric_target_average_utilization = m.get('MetricTargetAverageUtilization')
        if m.get('MetricType') is not None:
            self.metric_type = m.get('MetricType')
        return self


class UpdateApplicationScalingRuleResponseBodyDataMetric(TeaModel):
    def __init__(
        self,
        max_replicas: int = None,
        metrics: List[UpdateApplicationScalingRuleResponseBodyDataMetricMetrics] = None,
        min_replicas: int = None,
    ):
        self.max_replicas = max_replicas
        self.metrics = metrics
        self.min_replicas = min_replicas

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
        if self.max_replicas is not None:
            result['MaxReplicas'] = self.max_replicas
        result['Metrics'] = []
        if self.metrics is not None:
            for k in self.metrics:
                result['Metrics'].append(k.to_map() if k else None)
        if self.min_replicas is not None:
            result['MinReplicas'] = self.min_replicas
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxReplicas') is not None:
            self.max_replicas = m.get('MaxReplicas')
        self.metrics = []
        if m.get('Metrics') is not None:
            for k in m.get('Metrics'):
                temp_model = UpdateApplicationScalingRuleResponseBodyDataMetricMetrics()
                self.metrics.append(temp_model.from_map(k))
        if m.get('MinReplicas') is not None:
            self.min_replicas = m.get('MinReplicas')
        return self


class UpdateApplicationScalingRuleResponseBodyDataTimerSchedules(TeaModel):
    def __init__(
        self,
        at_time: str = None,
        target_replicas: int = None,
    ):
        self.at_time = at_time
        self.target_replicas = target_replicas

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.at_time is not None:
            result['AtTime'] = self.at_time
        if self.target_replicas is not None:
            result['TargetReplicas'] = self.target_replicas
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AtTime') is not None:
            self.at_time = m.get('AtTime')
        if m.get('TargetReplicas') is not None:
            self.target_replicas = m.get('TargetReplicas')
        return self


class UpdateApplicationScalingRuleResponseBodyDataTimer(TeaModel):
    def __init__(
        self,
        begin_date: str = None,
        end_date: str = None,
        period: str = None,
        schedules: List[UpdateApplicationScalingRuleResponseBodyDataTimerSchedules] = None,
    ):
        self.begin_date = begin_date
        self.end_date = end_date
        self.period = period
        self.schedules = schedules

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
        if self.begin_date is not None:
            result['BeginDate'] = self.begin_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.period is not None:
            result['Period'] = self.period
        result['Schedules'] = []
        if self.schedules is not None:
            for k in self.schedules:
                result['Schedules'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginDate') is not None:
            self.begin_date = m.get('BeginDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        self.schedules = []
        if m.get('Schedules') is not None:
            for k in m.get('Schedules'):
                temp_model = UpdateApplicationScalingRuleResponseBodyDataTimerSchedules()
                self.schedules.append(temp_model.from_map(k))
        return self


class UpdateApplicationScalingRuleResponseBodyData(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        create_time: int = None,
        last_disable_time: int = None,
        metric: UpdateApplicationScalingRuleResponseBodyDataMetric = None,
        scale_rule_enabled: bool = None,
        scale_rule_name: str = None,
        scale_rule_type: str = None,
        timer: UpdateApplicationScalingRuleResponseBodyDataTimer = None,
        update_time: int = None,
    ):
        self.app_id = app_id
        self.create_time = create_time
        self.last_disable_time = last_disable_time
        self.metric = metric
        self.scale_rule_enabled = scale_rule_enabled
        self.scale_rule_name = scale_rule_name
        self.scale_rule_type = scale_rule_type
        self.timer = timer
        self.update_time = update_time

    def validate(self):
        if self.metric:
            self.metric.validate()
        if self.timer:
            self.timer.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.last_disable_time is not None:
            result['LastDisableTime'] = self.last_disable_time
        if self.metric is not None:
            result['Metric'] = self.metric.to_map()
        if self.scale_rule_enabled is not None:
            result['ScaleRuleEnabled'] = self.scale_rule_enabled
        if self.scale_rule_name is not None:
            result['ScaleRuleName'] = self.scale_rule_name
        if self.scale_rule_type is not None:
            result['ScaleRuleType'] = self.scale_rule_type
        if self.timer is not None:
            result['Timer'] = self.timer.to_map()
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('LastDisableTime') is not None:
            self.last_disable_time = m.get('LastDisableTime')
        if m.get('Metric') is not None:
            temp_model = UpdateApplicationScalingRuleResponseBodyDataMetric()
            self.metric = temp_model.from_map(m['Metric'])
        if m.get('ScaleRuleEnabled') is not None:
            self.scale_rule_enabled = m.get('ScaleRuleEnabled')
        if m.get('ScaleRuleName') is not None:
            self.scale_rule_name = m.get('ScaleRuleName')
        if m.get('ScaleRuleType') is not None:
            self.scale_rule_type = m.get('ScaleRuleType')
        if m.get('Timer') is not None:
            temp_model = UpdateApplicationScalingRuleResponseBodyDataTimer()
            self.timer = temp_model.from_map(m['Timer'])
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class UpdateApplicationScalingRuleResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: UpdateApplicationScalingRuleResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = UpdateApplicationScalingRuleResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class UpdateApplicationScalingRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateApplicationScalingRuleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = UpdateApplicationScalingRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateApplicationVswitchesRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        v_switch_id: str = None,
    ):
        self.app_id = app_id
        self.v_switch_id = v_switch_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        return self


class UpdateApplicationVswitchesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class UpdateApplicationVswitchesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateApplicationVswitchesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = UpdateApplicationVswitchesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateConfigMapRequest(TeaModel):
    def __init__(
        self,
        config_map_id: int = None,
        data: str = None,
        description: str = None,
    ):
        self.config_map_id = config_map_id
        self.data = data
        self.description = description

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_map_id is not None:
            result['ConfigMapId'] = self.config_map_id
        if self.data is not None:
            result['Data'] = self.data
        if self.description is not None:
            result['Description'] = self.description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigMapId') is not None:
            self.config_map_id = m.get('ConfigMapId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        return self


class UpdateConfigMapResponseBodyData(TeaModel):
    def __init__(
        self,
        config_map_id: str = None,
    ):
        self.config_map_id = config_map_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_map_id is not None:
            result['ConfigMapId'] = self.config_map_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigMapId') is not None:
            self.config_map_id = m.get('ConfigMapId')
        return self


class UpdateConfigMapResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: UpdateConfigMapResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = UpdateConfigMapResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class UpdateConfigMapResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateConfigMapResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = UpdateConfigMapResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateGreyTagRouteRequest(TeaModel):
    def __init__(
        self,
        alb_rules: str = None,
        description: str = None,
        dubbo_rules: str = None,
        grey_tag_route_id: int = None,
        sc_rules: str = None,
    ):
        self.alb_rules = alb_rules
        self.description = description
        self.dubbo_rules = dubbo_rules
        self.grey_tag_route_id = grey_tag_route_id
        self.sc_rules = sc_rules

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alb_rules is not None:
            result['AlbRules'] = self.alb_rules
        if self.description is not None:
            result['Description'] = self.description
        if self.dubbo_rules is not None:
            result['DubboRules'] = self.dubbo_rules
        if self.grey_tag_route_id is not None:
            result['GreyTagRouteId'] = self.grey_tag_route_id
        if self.sc_rules is not None:
            result['ScRules'] = self.sc_rules
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlbRules') is not None:
            self.alb_rules = m.get('AlbRules')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DubboRules') is not None:
            self.dubbo_rules = m.get('DubboRules')
        if m.get('GreyTagRouteId') is not None:
            self.grey_tag_route_id = m.get('GreyTagRouteId')
        if m.get('ScRules') is not None:
            self.sc_rules = m.get('ScRules')
        return self


class UpdateGreyTagRouteResponseBodyData(TeaModel):
    def __init__(
        self,
        grey_tag_route_id: int = None,
    ):
        self.grey_tag_route_id = grey_tag_route_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.grey_tag_route_id is not None:
            result['GreyTagRouteId'] = self.grey_tag_route_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GreyTagRouteId') is not None:
            self.grey_tag_route_id = m.get('GreyTagRouteId')
        return self


class UpdateGreyTagRouteResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: UpdateGreyTagRouteResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = UpdateGreyTagRouteResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class UpdateGreyTagRouteResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateGreyTagRouteResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = UpdateGreyTagRouteResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateIngressRequest(TeaModel):
    def __init__(
        self,
        cert_id: str = None,
        cert_ids: str = None,
        default_rule: str = None,
        description: str = None,
        ingress_id: int = None,
        listener_port: str = None,
        listener_protocol: str = None,
        load_balance_type: str = None,
        rules: str = None,
    ):
        self.cert_id = cert_id
        self.cert_ids = cert_ids
        self.default_rule = default_rule
        self.description = description
        self.ingress_id = ingress_id
        self.listener_port = listener_port
        self.listener_protocol = listener_protocol
        self.load_balance_type = load_balance_type
        self.rules = rules

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_id is not None:
            result['CertId'] = self.cert_id
        if self.cert_ids is not None:
            result['CertIds'] = self.cert_ids
        if self.default_rule is not None:
            result['DefaultRule'] = self.default_rule
        if self.description is not None:
            result['Description'] = self.description
        if self.ingress_id is not None:
            result['IngressId'] = self.ingress_id
        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port
        if self.listener_protocol is not None:
            result['ListenerProtocol'] = self.listener_protocol
        if self.load_balance_type is not None:
            result['LoadBalanceType'] = self.load_balance_type
        if self.rules is not None:
            result['Rules'] = self.rules
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertId') is not None:
            self.cert_id = m.get('CertId')
        if m.get('CertIds') is not None:
            self.cert_ids = m.get('CertIds')
        if m.get('DefaultRule') is not None:
            self.default_rule = m.get('DefaultRule')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('IngressId') is not None:
            self.ingress_id = m.get('IngressId')
        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')
        if m.get('ListenerProtocol') is not None:
            self.listener_protocol = m.get('ListenerProtocol')
        if m.get('LoadBalanceType') is not None:
            self.load_balance_type = m.get('LoadBalanceType')
        if m.get('Rules') is not None:
            self.rules = m.get('Rules')
        return self


class UpdateIngressResponseBodyData(TeaModel):
    def __init__(
        self,
        ingress_id: int = None,
    ):
        self.ingress_id = ingress_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ingress_id is not None:
            result['IngressId'] = self.ingress_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IngressId') is not None:
            self.ingress_id = m.get('IngressId')
        return self


class UpdateIngressResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: UpdateIngressResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = UpdateIngressResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class UpdateIngressResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateIngressResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = UpdateIngressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateJobRequest(TeaModel):
    def __init__(
        self,
        acr_assume_role_arn: str = None,
        acr_instance_id: str = None,
        app_id: str = None,
        backoff_limit: int = None,
        command: str = None,
        command_args: str = None,
        concurrency_policy: str = None,
        config_map_mount_desc: str = None,
        custom_host_alias: str = None,
        edas_container_version: str = None,
        enable_image_accl: bool = None,
        envs: str = None,
        image_pull_secrets: str = None,
        image_url: str = None,
        jar_start_args: str = None,
        jar_start_options: str = None,
        jdk: str = None,
        mount_desc: str = None,
        mount_host: str = None,
        nas_id: str = None,
        oss_ak_id: str = None,
        oss_ak_secret: str = None,
        oss_mount_descs: str = None,
        package_url: str = None,
        package_version: str = None,
        php: str = None,
        php_config: str = None,
        php_config_location: str = None,
        post_start: str = None,
        pre_stop: str = None,
        programming_language: str = None,
        python: str = None,
        python_modules: str = None,
        ref_app_id: str = None,
        replicas: str = None,
        slice: bool = None,
        slice_envs: str = None,
        sls_configs: str = None,
        termination_grace_period_seconds: int = None,
        timeout: int = None,
        timezone: str = None,
        tomcat_config: str = None,
        trigger_config: str = None,
        war_start_options: str = None,
        web_container: str = None,
    ):
        self.acr_assume_role_arn = acr_assume_role_arn
        self.acr_instance_id = acr_instance_id
        self.app_id = app_id
        self.backoff_limit = backoff_limit
        self.command = command
        self.command_args = command_args
        self.concurrency_policy = concurrency_policy
        self.config_map_mount_desc = config_map_mount_desc
        self.custom_host_alias = custom_host_alias
        self.edas_container_version = edas_container_version
        self.enable_image_accl = enable_image_accl
        self.envs = envs
        self.image_pull_secrets = image_pull_secrets
        self.image_url = image_url
        self.jar_start_args = jar_start_args
        self.jar_start_options = jar_start_options
        self.jdk = jdk
        self.mount_desc = mount_desc
        self.mount_host = mount_host
        self.nas_id = nas_id
        self.oss_ak_id = oss_ak_id
        self.oss_ak_secret = oss_ak_secret
        self.oss_mount_descs = oss_mount_descs
        self.package_url = package_url
        self.package_version = package_version
        self.php = php
        self.php_config = php_config
        self.php_config_location = php_config_location
        self.post_start = post_start
        self.pre_stop = pre_stop
        self.programming_language = programming_language
        self.python = python
        self.python_modules = python_modules
        self.ref_app_id = ref_app_id
        self.replicas = replicas
        self.slice = slice
        self.slice_envs = slice_envs
        self.sls_configs = sls_configs
        self.termination_grace_period_seconds = termination_grace_period_seconds
        self.timeout = timeout
        self.timezone = timezone
        self.tomcat_config = tomcat_config
        self.trigger_config = trigger_config
        self.war_start_options = war_start_options
        self.web_container = web_container

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acr_assume_role_arn is not None:
            result['AcrAssumeRoleArn'] = self.acr_assume_role_arn
        if self.acr_instance_id is not None:
            result['AcrInstanceId'] = self.acr_instance_id
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.backoff_limit is not None:
            result['BackoffLimit'] = self.backoff_limit
        if self.command is not None:
            result['Command'] = self.command
        if self.command_args is not None:
            result['CommandArgs'] = self.command_args
        if self.concurrency_policy is not None:
            result['ConcurrencyPolicy'] = self.concurrency_policy
        if self.config_map_mount_desc is not None:
            result['ConfigMapMountDesc'] = self.config_map_mount_desc
        if self.custom_host_alias is not None:
            result['CustomHostAlias'] = self.custom_host_alias
        if self.edas_container_version is not None:
            result['EdasContainerVersion'] = self.edas_container_version
        if self.enable_image_accl is not None:
            result['EnableImageAccl'] = self.enable_image_accl
        if self.envs is not None:
            result['Envs'] = self.envs
        if self.image_pull_secrets is not None:
            result['ImagePullSecrets'] = self.image_pull_secrets
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        if self.jar_start_args is not None:
            result['JarStartArgs'] = self.jar_start_args
        if self.jar_start_options is not None:
            result['JarStartOptions'] = self.jar_start_options
        if self.jdk is not None:
            result['Jdk'] = self.jdk
        if self.mount_desc is not None:
            result['MountDesc'] = self.mount_desc
        if self.mount_host is not None:
            result['MountHost'] = self.mount_host
        if self.nas_id is not None:
            result['NasId'] = self.nas_id
        if self.oss_ak_id is not None:
            result['OssAkId'] = self.oss_ak_id
        if self.oss_ak_secret is not None:
            result['OssAkSecret'] = self.oss_ak_secret
        if self.oss_mount_descs is not None:
            result['OssMountDescs'] = self.oss_mount_descs
        if self.package_url is not None:
            result['PackageUrl'] = self.package_url
        if self.package_version is not None:
            result['PackageVersion'] = self.package_version
        if self.php is not None:
            result['Php'] = self.php
        if self.php_config is not None:
            result['PhpConfig'] = self.php_config
        if self.php_config_location is not None:
            result['PhpConfigLocation'] = self.php_config_location
        if self.post_start is not None:
            result['PostStart'] = self.post_start
        if self.pre_stop is not None:
            result['PreStop'] = self.pre_stop
        if self.programming_language is not None:
            result['ProgrammingLanguage'] = self.programming_language
        if self.python is not None:
            result['Python'] = self.python
        if self.python_modules is not None:
            result['PythonModules'] = self.python_modules
        if self.ref_app_id is not None:
            result['RefAppId'] = self.ref_app_id
        if self.replicas is not None:
            result['Replicas'] = self.replicas
        if self.slice is not None:
            result['Slice'] = self.slice
        if self.slice_envs is not None:
            result['SliceEnvs'] = self.slice_envs
        if self.sls_configs is not None:
            result['SlsConfigs'] = self.sls_configs
        if self.termination_grace_period_seconds is not None:
            result['TerminationGracePeriodSeconds'] = self.termination_grace_period_seconds
        if self.timeout is not None:
            result['Timeout'] = self.timeout
        if self.timezone is not None:
            result['Timezone'] = self.timezone
        if self.tomcat_config is not None:
            result['TomcatConfig'] = self.tomcat_config
        if self.trigger_config is not None:
            result['TriggerConfig'] = self.trigger_config
        if self.war_start_options is not None:
            result['WarStartOptions'] = self.war_start_options
        if self.web_container is not None:
            result['WebContainer'] = self.web_container
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcrAssumeRoleArn') is not None:
            self.acr_assume_role_arn = m.get('AcrAssumeRoleArn')
        if m.get('AcrInstanceId') is not None:
            self.acr_instance_id = m.get('AcrInstanceId')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('BackoffLimit') is not None:
            self.backoff_limit = m.get('BackoffLimit')
        if m.get('Command') is not None:
            self.command = m.get('Command')
        if m.get('CommandArgs') is not None:
            self.command_args = m.get('CommandArgs')
        if m.get('ConcurrencyPolicy') is not None:
            self.concurrency_policy = m.get('ConcurrencyPolicy')
        if m.get('ConfigMapMountDesc') is not None:
            self.config_map_mount_desc = m.get('ConfigMapMountDesc')
        if m.get('CustomHostAlias') is not None:
            self.custom_host_alias = m.get('CustomHostAlias')
        if m.get('EdasContainerVersion') is not None:
            self.edas_container_version = m.get('EdasContainerVersion')
        if m.get('EnableImageAccl') is not None:
            self.enable_image_accl = m.get('EnableImageAccl')
        if m.get('Envs') is not None:
            self.envs = m.get('Envs')
        if m.get('ImagePullSecrets') is not None:
            self.image_pull_secrets = m.get('ImagePullSecrets')
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        if m.get('JarStartArgs') is not None:
            self.jar_start_args = m.get('JarStartArgs')
        if m.get('JarStartOptions') is not None:
            self.jar_start_options = m.get('JarStartOptions')
        if m.get('Jdk') is not None:
            self.jdk = m.get('Jdk')
        if m.get('MountDesc') is not None:
            self.mount_desc = m.get('MountDesc')
        if m.get('MountHost') is not None:
            self.mount_host = m.get('MountHost')
        if m.get('NasId') is not None:
            self.nas_id = m.get('NasId')
        if m.get('OssAkId') is not None:
            self.oss_ak_id = m.get('OssAkId')
        if m.get('OssAkSecret') is not None:
            self.oss_ak_secret = m.get('OssAkSecret')
        if m.get('OssMountDescs') is not None:
            self.oss_mount_descs = m.get('OssMountDescs')
        if m.get('PackageUrl') is not None:
            self.package_url = m.get('PackageUrl')
        if m.get('PackageVersion') is not None:
            self.package_version = m.get('PackageVersion')
        if m.get('Php') is not None:
            self.php = m.get('Php')
        if m.get('PhpConfig') is not None:
            self.php_config = m.get('PhpConfig')
        if m.get('PhpConfigLocation') is not None:
            self.php_config_location = m.get('PhpConfigLocation')
        if m.get('PostStart') is not None:
            self.post_start = m.get('PostStart')
        if m.get('PreStop') is not None:
            self.pre_stop = m.get('PreStop')
        if m.get('ProgrammingLanguage') is not None:
            self.programming_language = m.get('ProgrammingLanguage')
        if m.get('Python') is not None:
            self.python = m.get('Python')
        if m.get('PythonModules') is not None:
            self.python_modules = m.get('PythonModules')
        if m.get('RefAppId') is not None:
            self.ref_app_id = m.get('RefAppId')
        if m.get('Replicas') is not None:
            self.replicas = m.get('Replicas')
        if m.get('Slice') is not None:
            self.slice = m.get('Slice')
        if m.get('SliceEnvs') is not None:
            self.slice_envs = m.get('SliceEnvs')
        if m.get('SlsConfigs') is not None:
            self.sls_configs = m.get('SlsConfigs')
        if m.get('TerminationGracePeriodSeconds') is not None:
            self.termination_grace_period_seconds = m.get('TerminationGracePeriodSeconds')
        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')
        if m.get('Timezone') is not None:
            self.timezone = m.get('Timezone')
        if m.get('TomcatConfig') is not None:
            self.tomcat_config = m.get('TomcatConfig')
        if m.get('TriggerConfig') is not None:
            self.trigger_config = m.get('TriggerConfig')
        if m.get('WarStartOptions') is not None:
            self.war_start_options = m.get('WarStartOptions')
        if m.get('WebContainer') is not None:
            self.web_container = m.get('WebContainer')
        return self


class UpdateJobResponseBodyData(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        change_order_id: str = None,
    ):
        self.app_id = app_id
        self.change_order_id = change_order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.change_order_id is not None:
            result['ChangeOrderId'] = self.change_order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ChangeOrderId') is not None:
            self.change_order_id = m.get('ChangeOrderId')
        return self


class UpdateJobResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: UpdateJobResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = UpdateJobResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class UpdateJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateJobResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = UpdateJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateNamespaceRequest(TeaModel):
    def __init__(
        self,
        name_space_short_id: str = None,
        namespace_description: str = None,
        namespace_id: str = None,
        namespace_name: str = None,
    ):
        self.name_space_short_id = name_space_short_id
        self.namespace_description = namespace_description
        self.namespace_id = namespace_id
        self.namespace_name = namespace_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name_space_short_id is not None:
            result['NameSpaceShortId'] = self.name_space_short_id
        if self.namespace_description is not None:
            result['NamespaceDescription'] = self.namespace_description
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.namespace_name is not None:
            result['NamespaceName'] = self.namespace_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NameSpaceShortId') is not None:
            self.name_space_short_id = m.get('NameSpaceShortId')
        if m.get('NamespaceDescription') is not None:
            self.namespace_description = m.get('NamespaceDescription')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('NamespaceName') is not None:
            self.namespace_name = m.get('NamespaceName')
        return self


class UpdateNamespaceResponseBodyData(TeaModel):
    def __init__(
        self,
        name_space_short_id: str = None,
        namespace_description: str = None,
        namespace_id: str = None,
        namespace_name: str = None,
        region_id: str = None,
    ):
        self.name_space_short_id = name_space_short_id
        self.namespace_description = namespace_description
        self.namespace_id = namespace_id
        self.namespace_name = namespace_name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name_space_short_id is not None:
            result['NameSpaceShortId'] = self.name_space_short_id
        if self.namespace_description is not None:
            result['NamespaceDescription'] = self.namespace_description
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.namespace_name is not None:
            result['NamespaceName'] = self.namespace_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NameSpaceShortId') is not None:
            self.name_space_short_id = m.get('NameSpaceShortId')
        if m.get('NamespaceDescription') is not None:
            self.namespace_description = m.get('NamespaceDescription')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('NamespaceName') is not None:
            self.namespace_name = m.get('NamespaceName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class UpdateNamespaceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: UpdateNamespaceResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = UpdateNamespaceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class UpdateNamespaceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateNamespaceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = UpdateNamespaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateNamespaceVpcRequest(TeaModel):
    def __init__(
        self,
        name_space_short_id: str = None,
        namespace_id: str = None,
        vpc_id: str = None,
    ):
        self.name_space_short_id = name_space_short_id
        self.namespace_id = namespace_id
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name_space_short_id is not None:
            result['NameSpaceShortId'] = self.name_space_short_id
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NameSpaceShortId') is not None:
            self.name_space_short_id = m.get('NameSpaceShortId')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class UpdateNamespaceVpcResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class UpdateNamespaceVpcResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateNamespaceVpcResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = UpdateNamespaceVpcResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateSecretRequest(TeaModel):
    def __init__(
        self,
        namespace_id: str = None,
        secret_data: str = None,
        secret_id: int = None,
    ):
        self.namespace_id = namespace_id
        self.secret_data = secret_data
        self.secret_id = secret_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.secret_data is not None:
            result['SecretData'] = self.secret_data
        if self.secret_id is not None:
            result['SecretId'] = self.secret_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('SecretData') is not None:
            self.secret_data = m.get('SecretData')
        if m.get('SecretId') is not None:
            self.secret_id = m.get('SecretId')
        return self


class UpdateSecretResponseBodyData(TeaModel):
    def __init__(
        self,
        secret_id: int = None,
    ):
        self.secret_id = secret_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.secret_id is not None:
            result['SecretId'] = self.secret_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecretId') is not None:
            self.secret_id = m.get('SecretId')
        return self


class UpdateSecretResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: UpdateSecretResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = UpdateSecretResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class UpdateSecretResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateSecretResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = UpdateSecretResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


