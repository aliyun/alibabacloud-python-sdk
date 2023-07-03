# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class CreateAsyncPredictRequest(TeaModel):
    def __init__(
        self,
        content: str = None,
        detail_tag: str = None,
        fetch_content: str = None,
        file_content: str = None,
        file_type: str = None,
        file_url: str = None,
        model_id: int = None,
        model_version: str = None,
        service_name: str = None,
        service_version: str = None,
        top_k: int = None,
    ):
        self.content = content
        self.detail_tag = detail_tag
        self.fetch_content = fetch_content
        self.file_content = file_content
        self.file_type = file_type
        self.file_url = file_url
        self.model_id = model_id
        self.model_version = model_version
        self.service_name = service_name
        self.service_version = service_version
        self.top_k = top_k

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.detail_tag is not None:
            result['DetailTag'] = self.detail_tag
        if self.fetch_content is not None:
            result['FetchContent'] = self.fetch_content
        if self.file_content is not None:
            result['FileContent'] = self.file_content
        if self.file_type is not None:
            result['FileType'] = self.file_type
        if self.file_url is not None:
            result['FileUrl'] = self.file_url
        if self.model_id is not None:
            result['ModelId'] = self.model_id
        if self.model_version is not None:
            result['ModelVersion'] = self.model_version
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.service_version is not None:
            result['ServiceVersion'] = self.service_version
        if self.top_k is not None:
            result['TopK'] = self.top_k
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('DetailTag') is not None:
            self.detail_tag = m.get('DetailTag')
        if m.get('FetchContent') is not None:
            self.fetch_content = m.get('FetchContent')
        if m.get('FileContent') is not None:
            self.file_content = m.get('FileContent')
        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')
        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')
        if m.get('ModelVersion') is not None:
            self.model_version = m.get('ModelVersion')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('ServiceVersion') is not None:
            self.service_version = m.get('ServiceVersion')
        if m.get('TopK') is not None:
            self.top_k = m.get('TopK')
        return self


class CreateAsyncPredictResponseBody(TeaModel):
    def __init__(
        self,
        async_predict_id: int = None,
        request_id: str = None,
    ):
        self.async_predict_id = async_predict_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.async_predict_id is not None:
            result['AsyncPredictId'] = self.async_predict_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AsyncPredictId') is not None:
            self.async_predict_id = m.get('AsyncPredictId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateAsyncPredictResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateAsyncPredictResponseBody = None,
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
            temp_model = CreateAsyncPredictResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FindUserReport4AlinlpRequest(TeaModel):
    def __init__(
        self,
        begin_time: str = None,
        customer_user_parent_id: int = None,
        end_time: str = None,
        model_type: str = None,
        type: str = None,
    ):
        self.begin_time = begin_time
        self.customer_user_parent_id = customer_user_parent_id
        self.end_time = end_time
        self.model_type = model_type
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.customer_user_parent_id is not None:
            result['CustomerUserParentId'] = self.customer_user_parent_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.model_type is not None:
            result['ModelType'] = self.model_type
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('CustomerUserParentId') is not None:
            self.customer_user_parent_id = m.get('CustomerUserParentId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('ModelType') is not None:
            self.model_type = m.get('ModelType')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class FindUserReport4AlinlpResponseBodyData(TeaModel):
    def __init__(
        self,
        fail_count: int = None,
        qps_max: int = None,
        rpt_time: str = None,
        success_count: int = None,
        total_count: int = None,
    ):
        self.fail_count = fail_count
        self.qps_max = qps_max
        self.rpt_time = rpt_time
        self.success_count = success_count
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fail_count is not None:
            result['FailCount'] = self.fail_count
        if self.qps_max is not None:
            result['QpsMax'] = self.qps_max
        if self.rpt_time is not None:
            result['RptTime'] = self.rpt_time
        if self.success_count is not None:
            result['SuccessCount'] = self.success_count
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FailCount') is not None:
            self.fail_count = m.get('FailCount')
        if m.get('QpsMax') is not None:
            self.qps_max = m.get('QpsMax')
        if m.get('RptTime') is not None:
            self.rpt_time = m.get('RptTime')
        if m.get('SuccessCount') is not None:
            self.success_count = m.get('SuccessCount')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class FindUserReport4AlinlpResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[FindUserReport4AlinlpResponseBodyData] = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.request_id = request_id

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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = FindUserReport4AlinlpResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class FindUserReport4AlinlpResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: FindUserReport4AlinlpResponseBody = None,
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
            temp_model = FindUserReport4AlinlpResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAsyncPredictRequest(TeaModel):
    def __init__(
        self,
        async_predict_id: int = None,
    ):
        self.async_predict_id = async_predict_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.async_predict_id is not None:
            result['AsyncPredictId'] = self.async_predict_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AsyncPredictId') is not None:
            self.async_predict_id = m.get('AsyncPredictId')
        return self


class GetAsyncPredictResponseBody(TeaModel):
    def __init__(
        self,
        async_predict_id: int = None,
        content: str = None,
        request_id: str = None,
        status: int = None,
    ):
        self.async_predict_id = async_predict_id
        self.content = content
        self.request_id = request_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.async_predict_id is not None:
            result['AsyncPredictId'] = self.async_predict_id
        if self.content is not None:
            result['Content'] = self.content
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AsyncPredictId') is not None:
            self.async_predict_id = m.get('AsyncPredictId')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetAsyncPredictResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAsyncPredictResponseBody = None,
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
            temp_model = GetAsyncPredictResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPredictResultRequest(TeaModel):
    def __init__(
        self,
        content: str = None,
        detail_tag: str = None,
        model_id: int = None,
        model_version: str = None,
        top_k: int = None,
    ):
        self.content = content
        self.detail_tag = detail_tag
        self.model_id = model_id
        self.model_version = model_version
        self.top_k = top_k

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.detail_tag is not None:
            result['DetailTag'] = self.detail_tag
        if self.model_id is not None:
            result['ModelId'] = self.model_id
        if self.model_version is not None:
            result['ModelVersion'] = self.model_version
        if self.top_k is not None:
            result['TopK'] = self.top_k
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('DetailTag') is not None:
            self.detail_tag = m.get('DetailTag')
        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')
        if m.get('ModelVersion') is not None:
            self.model_version = m.get('ModelVersion')
        if m.get('TopK') is not None:
            self.top_k = m.get('TopK')
        return self


class GetPredictResultResponseBody(TeaModel):
    def __init__(
        self,
        content: str = None,
        request_id: str = None,
    ):
        self.content = content
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetPredictResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetPredictResultResponseBody = None,
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
            temp_model = GetPredictResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RunPreTrainServiceRequest(TeaModel):
    def __init__(
        self,
        predict_content: str = None,
        service_name: str = None,
        service_version: str = None,
    ):
        self.predict_content = predict_content
        self.service_name = service_name
        self.service_version = service_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.predict_content is not None:
            result['PredictContent'] = self.predict_content
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.service_version is not None:
            result['ServiceVersion'] = self.service_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PredictContent') is not None:
            self.predict_content = m.get('PredictContent')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('ServiceVersion') is not None:
            self.service_version = m.get('ServiceVersion')
        return self


class RunPreTrainServiceResponseBody(TeaModel):
    def __init__(
        self,
        billing_count: int = None,
        predict_result: str = None,
        request_id: str = None,
    ):
        self.billing_count = billing_count
        self.predict_result = predict_result
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.billing_count is not None:
            result['BillingCount'] = self.billing_count
        if self.predict_result is not None:
            result['PredictResult'] = self.predict_result
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BillingCount') is not None:
            self.billing_count = m.get('BillingCount')
        if m.get('PredictResult') is not None:
            self.predict_result = m.get('PredictResult')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RunPreTrainServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RunPreTrainServiceResponseBody = None,
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
            temp_model = RunPreTrainServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RunPreTrainServiceNewRequest(TeaModel):
    def __init__(
        self,
        predict_content: str = None,
        service_name: str = None,
        service_version: str = None,
    ):
        self.predict_content = predict_content
        self.service_name = service_name
        self.service_version = service_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.predict_content is not None:
            result['PredictContent'] = self.predict_content
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.service_version is not None:
            result['ServiceVersion'] = self.service_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PredictContent') is not None:
            self.predict_content = m.get('PredictContent')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('ServiceVersion') is not None:
            self.service_version = m.get('ServiceVersion')
        return self


class RunPreTrainServiceNewResponseBody(TeaModel):
    def __init__(
        self,
        billing_count: int = None,
        predict_result: str = None,
        request_id: str = None,
    ):
        self.billing_count = billing_count
        self.predict_result = predict_result
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.billing_count is not None:
            result['BillingCount'] = self.billing_count
        if self.predict_result is not None:
            result['PredictResult'] = self.predict_result
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BillingCount') is not None:
            self.billing_count = m.get('BillingCount')
        if m.get('PredictResult') is not None:
            self.predict_result = m.get('PredictResult')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RunPreTrainServiceNewResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RunPreTrainServiceNewResponseBody = None,
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
            temp_model = RunPreTrainServiceNewResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


