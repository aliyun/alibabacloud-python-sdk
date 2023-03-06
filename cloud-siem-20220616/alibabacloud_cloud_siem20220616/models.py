# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict


class BatchJobCheckRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        submit_id: str = None,
    ):
        self.region_id = region_id
        self.submit_id = submit_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.submit_id is not None:
            result['SubmitId'] = self.submit_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SubmitId') is not None:
            self.submit_id = m.get('SubmitId')
        return self


class BatchJobCheckResponseBodyDataErrTaskListProductListLogList(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        log_code: str = None,
        log_store_name_pattern: str = None,
        product_code: str = None,
        project_name_pattern: str = None,
        region_code: str = None,
    ):
        self.error_code = error_code
        self.log_code = log_code
        self.log_store_name_pattern = log_store_name_pattern
        self.product_code = product_code
        self.project_name_pattern = project_name_pattern
        self.region_code = region_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.log_code is not None:
            result['LogCode'] = self.log_code
        if self.log_store_name_pattern is not None:
            result['LogStoreNamePattern'] = self.log_store_name_pattern
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.project_name_pattern is not None:
            result['ProjectNamePattern'] = self.project_name_pattern
        if self.region_code is not None:
            result['RegionCode'] = self.region_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('LogCode') is not None:
            self.log_code = m.get('LogCode')
        if m.get('LogStoreNamePattern') is not None:
            self.log_store_name_pattern = m.get('LogStoreNamePattern')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ProjectNamePattern') is not None:
            self.project_name_pattern = m.get('ProjectNamePattern')
        if m.get('RegionCode') is not None:
            self.region_code = m.get('RegionCode')
        return self


class BatchJobCheckResponseBodyDataErrTaskListProductList(TeaModel):
    def __init__(
        self,
        log_list: List[BatchJobCheckResponseBodyDataErrTaskListProductListLogList] = None,
        product_code: str = None,
    ):
        self.log_list = log_list
        self.product_code = product_code

    def validate(self):
        if self.log_list:
            for k in self.log_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['LogList'] = []
        if self.log_list is not None:
            for k in self.log_list:
                result['LogList'].append(k.to_map() if k else None)
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.log_list = []
        if m.get('LogList') is not None:
            for k in m.get('LogList'):
                temp_model = BatchJobCheckResponseBodyDataErrTaskListProductListLogList()
                self.log_list.append(temp_model.from_map(k))
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        return self


class BatchJobCheckResponseBodyDataErrTaskList(TeaModel):
    def __init__(
        self,
        product_list: List[BatchJobCheckResponseBodyDataErrTaskListProductList] = None,
        user_id: int = None,
    ):
        self.product_list = product_list
        self.user_id = user_id

    def validate(self):
        if self.product_list:
            for k in self.product_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ProductList'] = []
        if self.product_list is not None:
            for k in self.product_list:
                result['ProductList'].append(k.to_map() if k else None)
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.product_list = []
        if m.get('ProductList') is not None:
            for k in m.get('ProductList'):
                temp_model = BatchJobCheckResponseBodyDataErrTaskListProductList()
                self.product_list.append(temp_model.from_map(k))
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class BatchJobCheckResponseBodyData(TeaModel):
    def __init__(
        self,
        config_id: str = None,
        err_task_list: List[BatchJobCheckResponseBodyDataErrTaskList] = None,
        failed_count: int = None,
        finish_count: int = None,
        folder_id: str = None,
        task_count: int = None,
        task_status: str = None,
    ):
        self.config_id = config_id
        self.err_task_list = err_task_list
        self.failed_count = failed_count
        self.finish_count = finish_count
        self.folder_id = folder_id
        self.task_count = task_count
        self.task_status = task_status

    def validate(self):
        if self.err_task_list:
            for k in self.err_task_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_id is not None:
            result['ConfigId'] = self.config_id
        result['ErrTaskList'] = []
        if self.err_task_list is not None:
            for k in self.err_task_list:
                result['ErrTaskList'].append(k.to_map() if k else None)
        if self.failed_count is not None:
            result['FailedCount'] = self.failed_count
        if self.finish_count is not None:
            result['FinishCount'] = self.finish_count
        if self.folder_id is not None:
            result['FolderId'] = self.folder_id
        if self.task_count is not None:
            result['TaskCount'] = self.task_count
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')
        self.err_task_list = []
        if m.get('ErrTaskList') is not None:
            for k in m.get('ErrTaskList'):
                temp_model = BatchJobCheckResponseBodyDataErrTaskList()
                self.err_task_list.append(temp_model.from_map(k))
        if m.get('FailedCount') is not None:
            self.failed_count = m.get('FailedCount')
        if m.get('FinishCount') is not None:
            self.finish_count = m.get('FinishCount')
        if m.get('FolderId') is not None:
            self.folder_id = m.get('FolderId')
        if m.get('TaskCount') is not None:
            self.task_count = m.get('TaskCount')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        return self


class BatchJobCheckResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: BatchJobCheckResponseBodyData = None,
        err_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.err_code = err_code
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
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
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
            temp_model = BatchJobCheckResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class BatchJobCheckResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BatchJobCheckResponseBody = None,
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
            temp_model = BatchJobCheckResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchJobSubmitRequest(TeaModel):
    def __init__(
        self,
        json_config: str = None,
        region_id: str = None,
    ):
        self.json_config = json_config
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.json_config is not None:
            result['JsonConfig'] = self.json_config
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JsonConfig') is not None:
            self.json_config = m.get('JsonConfig')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class BatchJobSubmitResponseBodyDataConfigListProductListLogList(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        log_code: str = None,
        log_store_name_pattern: str = None,
        product_code: str = None,
        project_name_pattern: str = None,
        region_code: str = None,
    ):
        self.error_code = error_code
        self.log_code = log_code
        self.log_store_name_pattern = log_store_name_pattern
        self.product_code = product_code
        self.project_name_pattern = project_name_pattern
        self.region_code = region_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.log_code is not None:
            result['LogCode'] = self.log_code
        if self.log_store_name_pattern is not None:
            result['LogStoreNamePattern'] = self.log_store_name_pattern
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.project_name_pattern is not None:
            result['ProjectNamePattern'] = self.project_name_pattern
        if self.region_code is not None:
            result['RegionCode'] = self.region_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('LogCode') is not None:
            self.log_code = m.get('LogCode')
        if m.get('LogStoreNamePattern') is not None:
            self.log_store_name_pattern = m.get('LogStoreNamePattern')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ProjectNamePattern') is not None:
            self.project_name_pattern = m.get('ProjectNamePattern')
        if m.get('RegionCode') is not None:
            self.region_code = m.get('RegionCode')
        return self


class BatchJobSubmitResponseBodyDataConfigListProductList(TeaModel):
    def __init__(
        self,
        log_list: List[BatchJobSubmitResponseBodyDataConfigListProductListLogList] = None,
        product_code: str = None,
    ):
        self.log_list = log_list
        self.product_code = product_code

    def validate(self):
        if self.log_list:
            for k in self.log_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['LogList'] = []
        if self.log_list is not None:
            for k in self.log_list:
                result['LogList'].append(k.to_map() if k else None)
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.log_list = []
        if m.get('LogList') is not None:
            for k in m.get('LogList'):
                temp_model = BatchJobSubmitResponseBodyDataConfigListProductListLogList()
                self.log_list.append(temp_model.from_map(k))
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        return self


class BatchJobSubmitResponseBodyDataConfigList(TeaModel):
    def __init__(
        self,
        product_list: List[BatchJobSubmitResponseBodyDataConfigListProductList] = None,
        user_id: int = None,
    ):
        self.product_list = product_list
        self.user_id = user_id

    def validate(self):
        if self.product_list:
            for k in self.product_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ProductList'] = []
        if self.product_list is not None:
            for k in self.product_list:
                result['ProductList'].append(k.to_map() if k else None)
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.product_list = []
        if m.get('ProductList') is not None:
            for k in m.get('ProductList'):
                temp_model = BatchJobSubmitResponseBodyDataConfigListProductList()
                self.product_list.append(temp_model.from_map(k))
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class BatchJobSubmitResponseBodyData(TeaModel):
    def __init__(
        self,
        config_id: str = None,
        config_list: List[BatchJobSubmitResponseBodyDataConfigList] = None,
        submit_id: str = None,
        task_count: int = None,
    ):
        self.config_id = config_id
        self.config_list = config_list
        self.submit_id = submit_id
        self.task_count = task_count

    def validate(self):
        if self.config_list:
            for k in self.config_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_id is not None:
            result['ConfigId'] = self.config_id
        result['ConfigList'] = []
        if self.config_list is not None:
            for k in self.config_list:
                result['ConfigList'].append(k.to_map() if k else None)
        if self.submit_id is not None:
            result['SubmitId'] = self.submit_id
        if self.task_count is not None:
            result['TaskCount'] = self.task_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')
        self.config_list = []
        if m.get('ConfigList') is not None:
            for k in m.get('ConfigList'):
                temp_model = BatchJobSubmitResponseBodyDataConfigList()
                self.config_list.append(temp_model.from_map(k))
        if m.get('SubmitId') is not None:
            self.submit_id = m.get('SubmitId')
        if m.get('TaskCount') is not None:
            self.task_count = m.get('TaskCount')
        return self


class BatchJobSubmitResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: BatchJobSubmitResponseBodyData = None,
        err_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.err_code = err_code
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
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
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
            temp_model = BatchJobSubmitResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class BatchJobSubmitResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BatchJobSubmitResponseBody = None,
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
            temp_model = BatchJobSubmitResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SendMessageRequest(TeaModel):
    def __init__(
        self,
        channel_type: int = None,
        receive_uid: int = None,
        region_id: str = None,
    ):
        self.channel_type = channel_type
        self.receive_uid = receive_uid
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel_type is not None:
            result['ChannelType'] = self.channel_type
        if self.receive_uid is not None:
            result['ReceiveUid'] = self.receive_uid
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChannelType') is not None:
            self.channel_type = m.get('ChannelType')
        if m.get('ReceiveUid') is not None:
            self.receive_uid = m.get('ReceiveUid')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class SendMessageResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: bool = None,
        err_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.err_code = err_code
        self.message = message
        self.request_id = request_id
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
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
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
            self.data = m.get('Data')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SendMessageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SendMessageResponseBody = None,
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
            temp_model = SendMessageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


