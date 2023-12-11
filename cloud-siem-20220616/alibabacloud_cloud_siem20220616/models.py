# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict, Any


class DataProductListLogMapValueExtraParameters(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The ID of the extended parameter.
        self.key = key
        # The value of the extended parameter.
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


class DataProductListLogMapValue(TeaModel):
    def __init__(
        self,
        log_code: str = None,
        log_name: str = None,
        log_name_en: str = None,
        log_name_key: str = None,
        status: bool = None,
        can_operate_or_not: bool = None,
        topic: str = None,
        extra_parameters: List[DataProductListLogMapValueExtraParameters] = None,
    ):
        # The code of the log.
        self.log_code = log_code
        # This parameter is deprecated.
        self.log_name = log_name
        # This parameter is deprecated.
        self.log_name_en = log_name_en
        # The language code of the log that is used to indicate the language in which the log is displayed.
        self.log_name_key = log_name_key
        # The status of the log delivery. Valid values:
        # 
        # *   true: The logs are being delivered.
        # *   false: The log delivery feature is disabled.
        self.status = status
        # Indicates whether the log delivery feature can be enabled or disabled. The feature can be enabled or disabled only by the administrator of the threat analysis feature. Valid values:
        # 
        # *   true
        # *   false
        self.can_operate_or_not = can_operate_or_not
        # The topic of the log in the Logstore. The value is an index field in the Logstore that can be used to distinguish different logs.
        self.topic = topic
        # The extended parameter.
        self.extra_parameters = extra_parameters

    def validate(self):
        if self.extra_parameters:
            for k in self.extra_parameters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.log_code is not None:
            result['LogCode'] = self.log_code
        if self.log_name is not None:
            result['LogName'] = self.log_name
        if self.log_name_en is not None:
            result['LogNameEn'] = self.log_name_en
        if self.log_name_key is not None:
            result['LogNameKey'] = self.log_name_key
        if self.status is not None:
            result['Status'] = self.status
        if self.can_operate_or_not is not None:
            result['CanOperateOrNot'] = self.can_operate_or_not
        if self.topic is not None:
            result['Topic'] = self.topic
        result['ExtraParameters'] = []
        if self.extra_parameters is not None:
            for k in self.extra_parameters:
                result['ExtraParameters'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LogCode') is not None:
            self.log_code = m.get('LogCode')
        if m.get('LogName') is not None:
            self.log_name = m.get('LogName')
        if m.get('LogNameEn') is not None:
            self.log_name_en = m.get('LogNameEn')
        if m.get('LogNameKey') is not None:
            self.log_name_key = m.get('LogNameKey')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('CanOperateOrNot') is not None:
            self.can_operate_or_not = m.get('CanOperateOrNot')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        self.extra_parameters = []
        if m.get('ExtraParameters') is not None:
            for k in m.get('ExtraParameters'):
                temp_model = DataProductListLogMapValueExtraParameters()
                self.extra_parameters.append(temp_model.from_map(k))
        return self


class AddDataSourceRequest(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        cloud_code: str = None,
        data_source_instance_name: str = None,
        data_source_instance_params: str = None,
        data_source_instance_remark: str = None,
        data_source_type: str = None,
        region_id: str = None,
    ):
        self.account_id = account_id
        self.cloud_code = cloud_code
        self.data_source_instance_name = data_source_instance_name
        self.data_source_instance_params = data_source_instance_params
        self.data_source_instance_remark = data_source_instance_remark
        self.data_source_type = data_source_type
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.cloud_code is not None:
            result['CloudCode'] = self.cloud_code
        if self.data_source_instance_name is not None:
            result['DataSourceInstanceName'] = self.data_source_instance_name
        if self.data_source_instance_params is not None:
            result['DataSourceInstanceParams'] = self.data_source_instance_params
        if self.data_source_instance_remark is not None:
            result['DataSourceInstanceRemark'] = self.data_source_instance_remark
        if self.data_source_type is not None:
            result['DataSourceType'] = self.data_source_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('CloudCode') is not None:
            self.cloud_code = m.get('CloudCode')
        if m.get('DataSourceInstanceName') is not None:
            self.data_source_instance_name = m.get('DataSourceInstanceName')
        if m.get('DataSourceInstanceParams') is not None:
            self.data_source_instance_params = m.get('DataSourceInstanceParams')
        if m.get('DataSourceInstanceRemark') is not None:
            self.data_source_instance_remark = m.get('DataSourceInstanceRemark')
        if m.get('DataSourceType') is not None:
            self.data_source_type = m.get('DataSourceType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class AddDataSourceResponseBodyData(TeaModel):
    def __init__(
        self,
        count: int = None,
        data_source_instance_id: str = None,
    ):
        self.count = count
        self.data_source_instance_id = data_source_instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.data_source_instance_id is not None:
            result['DataSourceInstanceId'] = self.data_source_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('DataSourceInstanceId') is not None:
            self.data_source_instance_id = m.get('DataSourceInstanceId')
        return self


class AddDataSourceResponseBody(TeaModel):
    def __init__(
        self,
        data: AddDataSourceResponseBodyData = None,
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
            temp_model = AddDataSourceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AddDataSourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddDataSourceResponseBody = None,
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
            temp_model = AddDataSourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddDataSourceLogRequest(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        cloud_code: str = None,
        data_source_instance_id: str = None,
        data_source_instance_logs: str = None,
        log_code: str = None,
        region_id: str = None,
    ):
        self.account_id = account_id
        self.cloud_code = cloud_code
        self.data_source_instance_id = data_source_instance_id
        self.data_source_instance_logs = data_source_instance_logs
        self.log_code = log_code
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.cloud_code is not None:
            result['CloudCode'] = self.cloud_code
        if self.data_source_instance_id is not None:
            result['DataSourceInstanceId'] = self.data_source_instance_id
        if self.data_source_instance_logs is not None:
            result['DataSourceInstanceLogs'] = self.data_source_instance_logs
        if self.log_code is not None:
            result['LogCode'] = self.log_code
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('CloudCode') is not None:
            self.cloud_code = m.get('CloudCode')
        if m.get('DataSourceInstanceId') is not None:
            self.data_source_instance_id = m.get('DataSourceInstanceId')
        if m.get('DataSourceInstanceLogs') is not None:
            self.data_source_instance_logs = m.get('DataSourceInstanceLogs')
        if m.get('LogCode') is not None:
            self.log_code = m.get('LogCode')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class AddDataSourceLogResponseBodyData(TeaModel):
    def __init__(
        self,
        count: int = None,
        log_instance_id: str = None,
    ):
        self.count = count
        self.log_instance_id = log_instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.log_instance_id is not None:
            result['LogInstanceId'] = self.log_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('LogInstanceId') is not None:
            self.log_instance_id = m.get('LogInstanceId')
        return self


class AddDataSourceLogResponseBody(TeaModel):
    def __init__(
        self,
        data: AddDataSourceLogResponseBodyData = None,
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
            temp_model = AddDataSourceLogResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AddDataSourceLogResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddDataSourceLogResponseBody = None,
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
            temp_model = AddDataSourceLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddUserRequest(TeaModel):
    def __init__(
        self,
        added_user_id: int = None,
        region_id: str = None,
    ):
        self.added_user_id = added_user_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.added_user_id is not None:
            result['AddedUserId'] = self.added_user_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddedUserId') is not None:
            self.added_user_id = m.get('AddedUserId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class AddUserResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
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


class AddUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddUserResponseBody = None,
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
            temp_model = AddUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddUserSourceLogConfigRequest(TeaModel):
    def __init__(
        self,
        deleted: int = None,
        dis_play_line: str = None,
        region_id: str = None,
        source_log_code: str = None,
        source_log_info: str = None,
        source_prod_code: str = None,
        sub_user_id: int = None,
    ):
        self.deleted = deleted
        self.dis_play_line = dis_play_line
        self.region_id = region_id
        self.source_log_code = source_log_code
        self.source_log_info = source_log_info
        self.source_prod_code = source_prod_code
        self.sub_user_id = sub_user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.deleted is not None:
            result['Deleted'] = self.deleted
        if self.dis_play_line is not None:
            result['DisPlayLine'] = self.dis_play_line
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.source_log_code is not None:
            result['SourceLogCode'] = self.source_log_code
        if self.source_log_info is not None:
            result['SourceLogInfo'] = self.source_log_info
        if self.source_prod_code is not None:
            result['SourceProdCode'] = self.source_prod_code
        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')
        if m.get('DisPlayLine') is not None:
            self.dis_play_line = m.get('DisPlayLine')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SourceLogCode') is not None:
            self.source_log_code = m.get('SourceLogCode')
        if m.get('SourceLogInfo') is not None:
            self.source_log_info = m.get('SourceLogInfo')
        if m.get('SourceProdCode') is not None:
            self.source_prod_code = m.get('SourceProdCode')
        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')
        return self


class AddUserSourceLogConfigResponseBodyData(TeaModel):
    def __init__(
        self,
        diplay_line: str = None,
        displayed: bool = None,
        imported: bool = None,
        main_user_id: int = None,
        source_log_code: str = None,
        source_prod_code: str = None,
        sub_user_id: int = None,
        sub_user_name: str = None,
    ):
        self.diplay_line = diplay_line
        self.displayed = displayed
        self.imported = imported
        self.main_user_id = main_user_id
        self.source_log_code = source_log_code
        self.source_prod_code = source_prod_code
        self.sub_user_id = sub_user_id
        self.sub_user_name = sub_user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.diplay_line is not None:
            result['DiplayLine'] = self.diplay_line
        if self.displayed is not None:
            result['Displayed'] = self.displayed
        if self.imported is not None:
            result['Imported'] = self.imported
        if self.main_user_id is not None:
            result['MainUserId'] = self.main_user_id
        if self.source_log_code is not None:
            result['SourceLogCode'] = self.source_log_code
        if self.source_prod_code is not None:
            result['SourceProdCode'] = self.source_prod_code
        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id
        if self.sub_user_name is not None:
            result['SubUserName'] = self.sub_user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiplayLine') is not None:
            self.diplay_line = m.get('DiplayLine')
        if m.get('Displayed') is not None:
            self.displayed = m.get('Displayed')
        if m.get('Imported') is not None:
            self.imported = m.get('Imported')
        if m.get('MainUserId') is not None:
            self.main_user_id = m.get('MainUserId')
        if m.get('SourceLogCode') is not None:
            self.source_log_code = m.get('SourceLogCode')
        if m.get('SourceProdCode') is not None:
            self.source_prod_code = m.get('SourceProdCode')
        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')
        if m.get('SubUserName') is not None:
            self.sub_user_name = m.get('SubUserName')
        return self


class AddUserSourceLogConfigResponseBody(TeaModel):
    def __init__(
        self,
        data: AddUserSourceLogConfigResponseBodyData = None,
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
            temp_model = AddUserSourceLogConfigResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AddUserSourceLogConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddUserSourceLogConfigResponseBody = None,
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
            temp_model = AddUserSourceLogConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


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


class CloseDeliveryRequest(TeaModel):
    def __init__(
        self,
        log_code: str = None,
        product_code: str = None,
        region_id: str = None,
    ):
        # The log code of the cloud service, such as the code of the process log for Security Center. You can obtain the log code from the response of the ListDelivery operation.
        self.log_code = log_code
        # The code of the cloud service. Valid values:
        # 
        # *   qcloud_waf
        # *   qlcoud_cfw
        # *   hcloud_waf
        # *   hcloud_cfw
        # *   ddos
        # *   sas
        # *   cfw
        # *   config
        # *   csk
        # *   fc
        # *   rds
        # *   nas
        # *   apigateway
        # *   cdn
        # *   mongodb
        # *   eip
        # *   slb
        # *   vpc
        # *   actiontrail
        # *   waf
        # *   bastionhost
        # *   oss
        # *   polardb
        self.product_code = product_code
        # The region in which the data management center of the threat analysis feature resides. Specify this parameter based on the region where your assets reside. Valid values:
        # 
        # *   cn-hangzhou: Your assets reside in regions inside the Chinese mainland or in the China (Hong Kong) region.
        # *   ap-southeast-1: Your assets reside in regions outside the Chinese mainland, excluding the China (Hong Kong) region.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.log_code is not None:
            result['LogCode'] = self.log_code
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LogCode') is not None:
            self.log_code = m.get('LogCode')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CloseDeliveryResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: bool = None,
        dy_code: str = None,
        dy_message: str = None,
        err_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code.
        self.code = code
        # Indicates whether the threat analysis feature was disabled. Valid values:
        # 
        # *   true
        # *   false
        self.data = data
        # The dynamic error code.
        self.dy_code = dy_code
        # The dynamic message.
        self.dy_message = dy_message
        # The error code.
        self.err_code = err_code
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
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
        if self.dy_code is not None:
            result['DyCode'] = self.dy_code
        if self.dy_message is not None:
            result['DyMessage'] = self.dy_message
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
        if m.get('DyCode') is not None:
            self.dy_code = m.get('DyCode')
        if m.get('DyMessage') is not None:
            self.dy_message = m.get('DyMessage')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CloseDeliveryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CloseDeliveryResponseBody = None,
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
            temp_model = CloseDeliveryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAutomateResponseConfigRequest(TeaModel):
    def __init__(
        self,
        id: int = None,
        region_id: str = None,
    ):
        self.id = id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteAutomateResponseConfigResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
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
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteAutomateResponseConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteAutomateResponseConfigResponseBody = None,
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
            temp_model = DeleteAutomateResponseConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteBindAccountRequest(TeaModel):
    def __init__(
        self,
        access_id: str = None,
        account_id: str = None,
        bind_id: int = None,
        cloud_code: str = None,
        region_id: str = None,
    ):
        self.access_id = access_id
        self.account_id = account_id
        self.bind_id = bind_id
        self.cloud_code = cloud_code
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_id is not None:
            result['AccessId'] = self.access_id
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.bind_id is not None:
            result['BindId'] = self.bind_id
        if self.cloud_code is not None:
            result['CloudCode'] = self.cloud_code
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessId') is not None:
            self.access_id = m.get('AccessId')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('BindId') is not None:
            self.bind_id = m.get('BindId')
        if m.get('CloudCode') is not None:
            self.cloud_code = m.get('CloudCode')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteBindAccountResponseBodyData(TeaModel):
    def __init__(
        self,
        count: int = None,
    ):
        self.count = count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class DeleteBindAccountResponseBody(TeaModel):
    def __init__(
        self,
        data: DeleteBindAccountResponseBodyData = None,
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
            temp_model = DeleteBindAccountResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteBindAccountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteBindAccountResponseBody = None,
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
            temp_model = DeleteBindAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteCustomizeRuleRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        rule_id: int = None,
    ):
        self.region_id = region_id
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class DeleteCustomizeRuleResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
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
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteCustomizeRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteCustomizeRuleResponseBody = None,
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
            temp_model = DeleteCustomizeRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDataSourceRequest(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        cloud_code: str = None,
        data_source_instance_id: str = None,
        region_id: str = None,
    ):
        self.account_id = account_id
        self.cloud_code = cloud_code
        self.data_source_instance_id = data_source_instance_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.cloud_code is not None:
            result['CloudCode'] = self.cloud_code
        if self.data_source_instance_id is not None:
            result['DataSourceInstanceId'] = self.data_source_instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('CloudCode') is not None:
            self.cloud_code = m.get('CloudCode')
        if m.get('DataSourceInstanceId') is not None:
            self.data_source_instance_id = m.get('DataSourceInstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteDataSourceResponseBodyData(TeaModel):
    def __init__(
        self,
        count: int = None,
    ):
        self.count = count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class DeleteDataSourceResponseBody(TeaModel):
    def __init__(
        self,
        data: DeleteDataSourceResponseBodyData = None,
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
            temp_model = DeleteDataSourceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteDataSourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteDataSourceResponseBody = None,
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
            temp_model = DeleteDataSourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDataSourceLogRequest(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        cloud_code: str = None,
        data_source_instance_id: str = None,
        log_instance_id: str = None,
        region_id: str = None,
    ):
        self.account_id = account_id
        self.cloud_code = cloud_code
        self.data_source_instance_id = data_source_instance_id
        self.log_instance_id = log_instance_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.cloud_code is not None:
            result['CloudCode'] = self.cloud_code
        if self.data_source_instance_id is not None:
            result['DataSourceInstanceId'] = self.data_source_instance_id
        if self.log_instance_id is not None:
            result['LogInstanceId'] = self.log_instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('CloudCode') is not None:
            self.cloud_code = m.get('CloudCode')
        if m.get('DataSourceInstanceId') is not None:
            self.data_source_instance_id = m.get('DataSourceInstanceId')
        if m.get('LogInstanceId') is not None:
            self.log_instance_id = m.get('LogInstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteDataSourceLogResponseBodyData(TeaModel):
    def __init__(
        self,
        count: int = None,
        log_instance_id: str = None,
    ):
        self.count = count
        self.log_instance_id = log_instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.log_instance_id is not None:
            result['LogInstanceId'] = self.log_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('LogInstanceId') is not None:
            self.log_instance_id = m.get('LogInstanceId')
        return self


class DeleteDataSourceLogResponseBody(TeaModel):
    def __init__(
        self,
        data: DeleteDataSourceLogResponseBodyData = None,
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
            temp_model = DeleteDataSourceLogResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteDataSourceLogResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteDataSourceLogResponseBody = None,
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
            temp_model = DeleteDataSourceLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteQuickQueryRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        search_name: str = None,
    ):
        # The region in which the data management center of the threat analysis feature resides. Specify this parameter based on the region where your assets reside. Valid values:
        # 
        # *   cn-hangzhou: Your assets reside in regions inside the Chinese mainland or in the China (Hong Kong) region.
        # *   ap-southeast-1: Your assets reside in regions outside the Chinese mainland, excluding the China (Hong Kong) region.
        self.region_id = region_id
        # The name of the saved search.
        self.search_name = search_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.search_name is not None:
            result['SearchName'] = self.search_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SearchName') is not None:
            self.search_name = m.get('SearchName')
        return self


class DeleteQuickQueryResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: bool = None,
        dy_code: str = None,
        dy_message: str = None,
        err_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code.
        self.code = code
        # Indicates whether the saved search is deleted. Valid values:
        # 
        # *   true
        # *   false
        self.data = data
        # The dynamic error code.
        self.dy_code = dy_code
        # The dynamic message.
        self.dy_message = dy_message
        # The error code.
        self.err_code = err_code
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
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
        if self.dy_code is not None:
            result['DyCode'] = self.dy_code
        if self.dy_message is not None:
            result['DyMessage'] = self.dy_message
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
        if m.get('DyCode') is not None:
            self.dy_code = m.get('DyCode')
        if m.get('DyMessage') is not None:
            self.dy_message = m.get('DyMessage')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteQuickQueryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteQuickQueryResponseBody = None,
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
            temp_model = DeleteQuickQueryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteUserRequest(TeaModel):
    def __init__(
        self,
        added_user_id: int = None,
        region_id: str = None,
    ):
        self.added_user_id = added_user_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.added_user_id is not None:
            result['AddedUserId'] = self.added_user_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddedUserId') is not None:
            self.added_user_id = m.get('AddedUserId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteUserResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
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


class DeleteUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteUserResponseBody = None,
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
            temp_model = DeleteUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteWhiteRuleListRequest(TeaModel):
    def __init__(
        self,
        id: int = None,
        region_id: str = None,
    ):
        self.id = id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteWhiteRuleListResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: Any = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
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
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteWhiteRuleListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteWhiteRuleListResponseBody = None,
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
            temp_model = DeleteWhiteRuleListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAggregateFunctionRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
    ):
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeAggregateFunctionResponseBodyData(TeaModel):
    def __init__(
        self,
        function: str = None,
        function_name: str = None,
    ):
        self.function = function
        self.function_name = function_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.function is not None:
            result['Function'] = self.function
        if self.function_name is not None:
            result['FunctionName'] = self.function_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Function') is not None:
            self.function = m.get('Function')
        if m.get('FunctionName') is not None:
            self.function_name = m.get('FunctionName')
        return self


class DescribeAggregateFunctionResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: List[DescribeAggregateFunctionResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
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
                temp_model = DescribeAggregateFunctionResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeAggregateFunctionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAggregateFunctionResponseBody = None,
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
            temp_model = DescribeAggregateFunctionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAlertSceneRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
    ):
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeAlertSceneResponseBodyDataTargets(TeaModel):
    def __init__(
        self,
        name: str = None,
        type: str = None,
        value: str = None,
        values: List[str] = None,
    ):
        self.name = name
        self.type = type
        self.value = value
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        if self.value is not None:
            result['Value'] = self.value
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class DescribeAlertSceneResponseBodyData(TeaModel):
    def __init__(
        self,
        alert_name: str = None,
        alert_name_id: str = None,
        alert_tile: str = None,
        alert_tile_id: str = None,
        alert_type: str = None,
        alert_type_id: str = None,
        targets: List[DescribeAlertSceneResponseBodyDataTargets] = None,
    ):
        self.alert_name = alert_name
        self.alert_name_id = alert_name_id
        self.alert_tile = alert_tile
        self.alert_tile_id = alert_tile_id
        self.alert_type = alert_type
        self.alert_type_id = alert_type_id
        self.targets = targets

    def validate(self):
        if self.targets:
            for k in self.targets:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_name is not None:
            result['AlertName'] = self.alert_name
        if self.alert_name_id is not None:
            result['AlertNameId'] = self.alert_name_id
        if self.alert_tile is not None:
            result['AlertTile'] = self.alert_tile
        if self.alert_tile_id is not None:
            result['AlertTileId'] = self.alert_tile_id
        if self.alert_type is not None:
            result['AlertType'] = self.alert_type
        if self.alert_type_id is not None:
            result['AlertTypeId'] = self.alert_type_id
        result['Targets'] = []
        if self.targets is not None:
            for k in self.targets:
                result['Targets'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertName') is not None:
            self.alert_name = m.get('AlertName')
        if m.get('AlertNameId') is not None:
            self.alert_name_id = m.get('AlertNameId')
        if m.get('AlertTile') is not None:
            self.alert_tile = m.get('AlertTile')
        if m.get('AlertTileId') is not None:
            self.alert_tile_id = m.get('AlertTileId')
        if m.get('AlertType') is not None:
            self.alert_type = m.get('AlertType')
        if m.get('AlertTypeId') is not None:
            self.alert_type_id = m.get('AlertTypeId')
        self.targets = []
        if m.get('Targets') is not None:
            for k in m.get('Targets'):
                temp_model = DescribeAlertSceneResponseBodyDataTargets()
                self.targets.append(temp_model.from_map(k))
        return self


class DescribeAlertSceneResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: List[DescribeAlertSceneResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
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
                temp_model = DescribeAlertSceneResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeAlertSceneResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAlertSceneResponseBody = None,
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
            temp_model = DescribeAlertSceneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAlertSceneByEventRequest(TeaModel):
    def __init__(
        self,
        incident_uuid: str = None,
        region_id: str = None,
    ):
        self.incident_uuid = incident_uuid
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.incident_uuid is not None:
            result['IncidentUuid'] = self.incident_uuid
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IncidentUuid') is not None:
            self.incident_uuid = m.get('IncidentUuid')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeAlertSceneByEventResponseBodyDataTargets(TeaModel):
    def __init__(
        self,
        name: str = None,
        type: str = None,
        value: str = None,
        values: List[str] = None,
    ):
        self.name = name
        self.type = type
        self.value = value
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        if self.value is not None:
            result['Value'] = self.value
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class DescribeAlertSceneByEventResponseBodyData(TeaModel):
    def __init__(
        self,
        alert_name: str = None,
        alert_name_id: str = None,
        alert_tile: str = None,
        alert_tile_id: str = None,
        alert_type: str = None,
        alert_type_id: str = None,
        targets: List[DescribeAlertSceneByEventResponseBodyDataTargets] = None,
    ):
        self.alert_name = alert_name
        self.alert_name_id = alert_name_id
        self.alert_tile = alert_tile
        self.alert_tile_id = alert_tile_id
        self.alert_type = alert_type
        self.alert_type_id = alert_type_id
        self.targets = targets

    def validate(self):
        if self.targets:
            for k in self.targets:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_name is not None:
            result['AlertName'] = self.alert_name
        if self.alert_name_id is not None:
            result['AlertNameId'] = self.alert_name_id
        if self.alert_tile is not None:
            result['AlertTile'] = self.alert_tile
        if self.alert_tile_id is not None:
            result['AlertTileId'] = self.alert_tile_id
        if self.alert_type is not None:
            result['AlertType'] = self.alert_type
        if self.alert_type_id is not None:
            result['AlertTypeId'] = self.alert_type_id
        result['Targets'] = []
        if self.targets is not None:
            for k in self.targets:
                result['Targets'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertName') is not None:
            self.alert_name = m.get('AlertName')
        if m.get('AlertNameId') is not None:
            self.alert_name_id = m.get('AlertNameId')
        if m.get('AlertTile') is not None:
            self.alert_tile = m.get('AlertTile')
        if m.get('AlertTileId') is not None:
            self.alert_tile_id = m.get('AlertTileId')
        if m.get('AlertType') is not None:
            self.alert_type = m.get('AlertType')
        if m.get('AlertTypeId') is not None:
            self.alert_type_id = m.get('AlertTypeId')
        self.targets = []
        if m.get('Targets') is not None:
            for k in m.get('Targets'):
                temp_model = DescribeAlertSceneByEventResponseBodyDataTargets()
                self.targets.append(temp_model.from_map(k))
        return self


class DescribeAlertSceneByEventResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: List[DescribeAlertSceneByEventResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
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
                temp_model = DescribeAlertSceneByEventResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeAlertSceneByEventResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAlertSceneByEventResponseBody = None,
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
            temp_model = DescribeAlertSceneByEventResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAlertSourceRequest(TeaModel):
    def __init__(
        self,
        end_time: int = None,
        level: List[str] = None,
        region_id: str = None,
        start_time: int = None,
    ):
        self.end_time = end_time
        self.level = level
        self.region_id = region_id
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.level is not None:
            result['Level'] = self.level
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeAlertSourceResponseBodyData(TeaModel):
    def __init__(
        self,
        source: str = None,
        source_name: str = None,
    ):
        self.source = source
        self.source_name = source_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source is not None:
            result['Source'] = self.source
        if self.source_name is not None:
            result['SourceName'] = self.source_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('SourceName') is not None:
            self.source_name = m.get('SourceName')
        return self


class DescribeAlertSourceResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: List[DescribeAlertSourceResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
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
                temp_model = DescribeAlertSourceResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeAlertSourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAlertSourceResponseBody = None,
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
            temp_model = DescribeAlertSourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAlertSourceWithEventRequest(TeaModel):
    def __init__(
        self,
        incident_uuid: str = None,
        region_id: str = None,
    ):
        self.incident_uuid = incident_uuid
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.incident_uuid is not None:
            result['IncidentUuid'] = self.incident_uuid
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IncidentUuid') is not None:
            self.incident_uuid = m.get('IncidentUuid')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeAlertSourceWithEventResponseBodyData(TeaModel):
    def __init__(
        self,
        source: str = None,
        source_name: str = None,
    ):
        self.source = source
        self.source_name = source_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source is not None:
            result['Source'] = self.source
        if self.source_name is not None:
            result['SourceName'] = self.source_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('SourceName') is not None:
            self.source_name = m.get('SourceName')
        return self


class DescribeAlertSourceWithEventResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: List[DescribeAlertSourceWithEventResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
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
                temp_model = DescribeAlertSourceWithEventResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeAlertSourceWithEventResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAlertSourceWithEventResponseBody = None,
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
            temp_model = DescribeAlertSourceWithEventResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAlertTypeRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
    ):
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeAlertTypeResponseBodyData(TeaModel):
    def __init__(
        self,
        alert_type: str = None,
        alert_type_mds: str = None,
    ):
        self.alert_type = alert_type
        self.alert_type_mds = alert_type_mds

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_type is not None:
            result['AlertType'] = self.alert_type
        if self.alert_type_mds is not None:
            result['AlertTypeMds'] = self.alert_type_mds
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertType') is not None:
            self.alert_type = m.get('AlertType')
        if m.get('AlertTypeMds') is not None:
            self.alert_type_mds = m.get('AlertTypeMds')
        return self


class DescribeAlertTypeResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: List[DescribeAlertTypeResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
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
                temp_model = DescribeAlertTypeResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeAlertTypeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAlertTypeResponseBody = None,
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
            temp_model = DescribeAlertTypeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAlertsRequest(TeaModel):
    def __init__(
        self,
        alert_title: str = None,
        alert_uuid: str = None,
        current_page: int = None,
        end_time: int = None,
        is_defend: str = None,
        level: List[str] = None,
        page_size: int = None,
        region_id: str = None,
        source: str = None,
        start_time: int = None,
        sub_user_id: str = None,
    ):
        self.alert_title = alert_title
        self.alert_uuid = alert_uuid
        self.current_page = current_page
        self.end_time = end_time
        self.is_defend = is_defend
        self.level = level
        self.page_size = page_size
        self.region_id = region_id
        self.source = source
        self.start_time = start_time
        self.sub_user_id = sub_user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_title is not None:
            result['AlertTitle'] = self.alert_title
        if self.alert_uuid is not None:
            result['AlertUuid'] = self.alert_uuid
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.is_defend is not None:
            result['IsDefend'] = self.is_defend
        if self.level is not None:
            result['Level'] = self.level
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.source is not None:
            result['Source'] = self.source
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertTitle') is not None:
            self.alert_title = m.get('AlertTitle')
        if m.get('AlertUuid') is not None:
            self.alert_uuid = m.get('AlertUuid')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('IsDefend') is not None:
            self.is_defend = m.get('IsDefend')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')
        return self


class DescribeAlertsResponseBodyDataPageInfo(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.current_page = current_page
        self.page_size = page_size
        self.total_count = total_count

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
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeAlertsResponseBodyDataResponseDataAlertInfoList(TeaModel):
    def __init__(
        self,
        key: str = None,
        key_name: str = None,
        values: str = None,
    ):
        self.key = key
        self.key_name = key_name
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.key_name is not None:
            result['KeyName'] = self.key_name
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('KeyName') is not None:
            self.key_name = m.get('KeyName')
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class DescribeAlertsResponseBodyDataResponseData(TeaModel):
    def __init__(
        self,
        alert_desc: str = None,
        alert_desc_code: str = None,
        alert_desc_en: str = None,
        alert_detail: str = None,
        alert_info_list: List[DescribeAlertsResponseBodyDataResponseDataAlertInfoList] = None,
        alert_level: str = None,
        alert_name: str = None,
        alert_name_code: str = None,
        alert_name_en: str = None,
        alert_src_prod: str = None,
        alert_src_prod_module: str = None,
        alert_title: str = None,
        alert_title_en: str = None,
        alert_type: str = None,
        alert_type_code: str = None,
        alert_type_en: str = None,
        alert_uuid: str = None,
        asset_list: str = None,
        att_ck: str = None,
        cloud_code: str = None,
        end_time: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        incident_uuid: str = None,
        is_defend: str = None,
        log_time: str = None,
        log_uuid: str = None,
        main_user_id: int = None,
        occur_time: str = None,
        start_time: str = None,
        sub_user_id: int = None,
    ):
        self.alert_desc = alert_desc
        self.alert_desc_code = alert_desc_code
        self.alert_desc_en = alert_desc_en
        self.alert_detail = alert_detail
        self.alert_info_list = alert_info_list
        self.alert_level = alert_level
        self.alert_name = alert_name
        self.alert_name_code = alert_name_code
        self.alert_name_en = alert_name_en
        self.alert_src_prod = alert_src_prod
        self.alert_src_prod_module = alert_src_prod_module
        self.alert_title = alert_title
        self.alert_title_en = alert_title_en
        self.alert_type = alert_type
        self.alert_type_code = alert_type_code
        self.alert_type_en = alert_type_en
        self.alert_uuid = alert_uuid
        self.asset_list = asset_list
        self.att_ck = att_ck
        self.cloud_code = cloud_code
        self.end_time = end_time
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.incident_uuid = incident_uuid
        self.is_defend = is_defend
        self.log_time = log_time
        self.log_uuid = log_uuid
        self.main_user_id = main_user_id
        self.occur_time = occur_time
        self.start_time = start_time
        self.sub_user_id = sub_user_id

    def validate(self):
        if self.alert_info_list:
            for k in self.alert_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_desc is not None:
            result['AlertDesc'] = self.alert_desc
        if self.alert_desc_code is not None:
            result['AlertDescCode'] = self.alert_desc_code
        if self.alert_desc_en is not None:
            result['AlertDescEn'] = self.alert_desc_en
        if self.alert_detail is not None:
            result['AlertDetail'] = self.alert_detail
        result['AlertInfoList'] = []
        if self.alert_info_list is not None:
            for k in self.alert_info_list:
                result['AlertInfoList'].append(k.to_map() if k else None)
        if self.alert_level is not None:
            result['AlertLevel'] = self.alert_level
        if self.alert_name is not None:
            result['AlertName'] = self.alert_name
        if self.alert_name_code is not None:
            result['AlertNameCode'] = self.alert_name_code
        if self.alert_name_en is not None:
            result['AlertNameEn'] = self.alert_name_en
        if self.alert_src_prod is not None:
            result['AlertSrcProd'] = self.alert_src_prod
        if self.alert_src_prod_module is not None:
            result['AlertSrcProdModule'] = self.alert_src_prod_module
        if self.alert_title is not None:
            result['AlertTitle'] = self.alert_title
        if self.alert_title_en is not None:
            result['AlertTitleEn'] = self.alert_title_en
        if self.alert_type is not None:
            result['AlertType'] = self.alert_type
        if self.alert_type_code is not None:
            result['AlertTypeCode'] = self.alert_type_code
        if self.alert_type_en is not None:
            result['AlertTypeEn'] = self.alert_type_en
        if self.alert_uuid is not None:
            result['AlertUuid'] = self.alert_uuid
        if self.asset_list is not None:
            result['AssetList'] = self.asset_list
        if self.att_ck is not None:
            result['AttCk'] = self.att_ck
        if self.cloud_code is not None:
            result['CloudCode'] = self.cloud_code
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        if self.incident_uuid is not None:
            result['IncidentUuid'] = self.incident_uuid
        if self.is_defend is not None:
            result['IsDefend'] = self.is_defend
        if self.log_time is not None:
            result['LogTime'] = self.log_time
        if self.log_uuid is not None:
            result['LogUuid'] = self.log_uuid
        if self.main_user_id is not None:
            result['MainUserId'] = self.main_user_id
        if self.occur_time is not None:
            result['OccurTime'] = self.occur_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertDesc') is not None:
            self.alert_desc = m.get('AlertDesc')
        if m.get('AlertDescCode') is not None:
            self.alert_desc_code = m.get('AlertDescCode')
        if m.get('AlertDescEn') is not None:
            self.alert_desc_en = m.get('AlertDescEn')
        if m.get('AlertDetail') is not None:
            self.alert_detail = m.get('AlertDetail')
        self.alert_info_list = []
        if m.get('AlertInfoList') is not None:
            for k in m.get('AlertInfoList'):
                temp_model = DescribeAlertsResponseBodyDataResponseDataAlertInfoList()
                self.alert_info_list.append(temp_model.from_map(k))
        if m.get('AlertLevel') is not None:
            self.alert_level = m.get('AlertLevel')
        if m.get('AlertName') is not None:
            self.alert_name = m.get('AlertName')
        if m.get('AlertNameCode') is not None:
            self.alert_name_code = m.get('AlertNameCode')
        if m.get('AlertNameEn') is not None:
            self.alert_name_en = m.get('AlertNameEn')
        if m.get('AlertSrcProd') is not None:
            self.alert_src_prod = m.get('AlertSrcProd')
        if m.get('AlertSrcProdModule') is not None:
            self.alert_src_prod_module = m.get('AlertSrcProdModule')
        if m.get('AlertTitle') is not None:
            self.alert_title = m.get('AlertTitle')
        if m.get('AlertTitleEn') is not None:
            self.alert_title_en = m.get('AlertTitleEn')
        if m.get('AlertType') is not None:
            self.alert_type = m.get('AlertType')
        if m.get('AlertTypeCode') is not None:
            self.alert_type_code = m.get('AlertTypeCode')
        if m.get('AlertTypeEn') is not None:
            self.alert_type_en = m.get('AlertTypeEn')
        if m.get('AlertUuid') is not None:
            self.alert_uuid = m.get('AlertUuid')
        if m.get('AssetList') is not None:
            self.asset_list = m.get('AssetList')
        if m.get('AttCk') is not None:
            self.att_ck = m.get('AttCk')
        if m.get('CloudCode') is not None:
            self.cloud_code = m.get('CloudCode')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IncidentUuid') is not None:
            self.incident_uuid = m.get('IncidentUuid')
        if m.get('IsDefend') is not None:
            self.is_defend = m.get('IsDefend')
        if m.get('LogTime') is not None:
            self.log_time = m.get('LogTime')
        if m.get('LogUuid') is not None:
            self.log_uuid = m.get('LogUuid')
        if m.get('MainUserId') is not None:
            self.main_user_id = m.get('MainUserId')
        if m.get('OccurTime') is not None:
            self.occur_time = m.get('OccurTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')
        return self


class DescribeAlertsResponseBodyData(TeaModel):
    def __init__(
        self,
        page_info: DescribeAlertsResponseBodyDataPageInfo = None,
        response_data: List[DescribeAlertsResponseBodyDataResponseData] = None,
    ):
        self.page_info = page_info
        self.response_data = response_data

    def validate(self):
        if self.page_info:
            self.page_info.validate()
        if self.response_data:
            for k in self.response_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()
        result['ResponseData'] = []
        if self.response_data is not None:
            for k in self.response_data:
                result['ResponseData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageInfo') is not None:
            temp_model = DescribeAlertsResponseBodyDataPageInfo()
            self.page_info = temp_model.from_map(m['PageInfo'])
        self.response_data = []
        if m.get('ResponseData') is not None:
            for k in m.get('ResponseData'):
                temp_model = DescribeAlertsResponseBodyDataResponseData()
                self.response_data.append(temp_model.from_map(k))
        return self


class DescribeAlertsResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: DescribeAlertsResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
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
            temp_model = DescribeAlertsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeAlertsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAlertsResponseBody = None,
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
            temp_model = DescribeAlertsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAlertsCountRequest(TeaModel):
    def __init__(
        self,
        end_time: int = None,
        region_id: str = None,
        start_time: int = None,
    ):
        self.end_time = end_time
        self.region_id = region_id
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeAlertsCountResponseBodyData(TeaModel):
    def __init__(
        self,
        all: int = None,
        high: int = None,
        low: int = None,
        medium: int = None,
        product_num: int = None,
    ):
        self.all = all
        self.high = high
        self.low = low
        self.medium = medium
        self.product_num = product_num

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all is not None:
            result['All'] = self.all
        if self.high is not None:
            result['High'] = self.high
        if self.low is not None:
            result['Low'] = self.low
        if self.medium is not None:
            result['Medium'] = self.medium
        if self.product_num is not None:
            result['ProductNum'] = self.product_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('All') is not None:
            self.all = m.get('All')
        if m.get('High') is not None:
            self.high = m.get('High')
        if m.get('Low') is not None:
            self.low = m.get('Low')
        if m.get('Medium') is not None:
            self.medium = m.get('Medium')
        if m.get('ProductNum') is not None:
            self.product_num = m.get('ProductNum')
        return self


class DescribeAlertsCountResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: DescribeAlertsCountResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
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
            temp_model = DescribeAlertsCountResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeAlertsCountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAlertsCountResponseBody = None,
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
            temp_model = DescribeAlertsCountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAlertsWithEntityRequest(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        entity_id: int = None,
        incident_uuid: str = None,
        page_size: int = None,
        region_id: str = None,
        sophon_task_id: str = None,
    ):
        self.current_page = current_page
        self.entity_id = entity_id
        self.incident_uuid = incident_uuid
        self.page_size = page_size
        self.region_id = region_id
        self.sophon_task_id = sophon_task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        if self.incident_uuid is not None:
            result['IncidentUuid'] = self.incident_uuid
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.sophon_task_id is not None:
            result['SophonTaskId'] = self.sophon_task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        if m.get('IncidentUuid') is not None:
            self.incident_uuid = m.get('IncidentUuid')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SophonTaskId') is not None:
            self.sophon_task_id = m.get('SophonTaskId')
        return self


class DescribeAlertsWithEntityResponseBodyDataPageInfo(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.current_page = current_page
        self.page_size = page_size
        self.total_count = total_count

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
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeAlertsWithEntityResponseBodyDataResponseDataAlertInfoList(TeaModel):
    def __init__(
        self,
        key: str = None,
        key_name: str = None,
        values: str = None,
    ):
        self.key = key
        self.key_name = key_name
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.key_name is not None:
            result['KeyName'] = self.key_name
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('KeyName') is not None:
            self.key_name = m.get('KeyName')
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class DescribeAlertsWithEntityResponseBodyDataResponseData(TeaModel):
    def __init__(
        self,
        alert_desc: str = None,
        alert_desc_code: str = None,
        alert_desc_en: str = None,
        alert_detail: str = None,
        alert_info_list: List[DescribeAlertsWithEntityResponseBodyDataResponseDataAlertInfoList] = None,
        alert_level: str = None,
        alert_name: str = None,
        alert_name_code: str = None,
        alert_name_en: str = None,
        alert_src_prod: str = None,
        alert_src_prod_module: str = None,
        alert_title: str = None,
        alert_title_en: str = None,
        alert_type: str = None,
        alert_type_code: str = None,
        alert_type_en: str = None,
        alert_uuid: str = None,
        asset_list: str = None,
        att_ck: str = None,
        cloud_code: str = None,
        end_time: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        incident_uuid: str = None,
        is_defend: str = None,
        log_time: str = None,
        log_uuid: str = None,
        main_user_id: int = None,
        occur_time: str = None,
        start_time: str = None,
        sub_user_id: int = None,
    ):
        self.alert_desc = alert_desc
        self.alert_desc_code = alert_desc_code
        self.alert_desc_en = alert_desc_en
        self.alert_detail = alert_detail
        self.alert_info_list = alert_info_list
        self.alert_level = alert_level
        self.alert_name = alert_name
        self.alert_name_code = alert_name_code
        self.alert_name_en = alert_name_en
        self.alert_src_prod = alert_src_prod
        self.alert_src_prod_module = alert_src_prod_module
        self.alert_title = alert_title
        self.alert_title_en = alert_title_en
        self.alert_type = alert_type
        self.alert_type_code = alert_type_code
        self.alert_type_en = alert_type_en
        self.alert_uuid = alert_uuid
        self.asset_list = asset_list
        self.att_ck = att_ck
        self.cloud_code = cloud_code
        self.end_time = end_time
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.incident_uuid = incident_uuid
        self.is_defend = is_defend
        self.log_time = log_time
        self.log_uuid = log_uuid
        self.main_user_id = main_user_id
        self.occur_time = occur_time
        self.start_time = start_time
        self.sub_user_id = sub_user_id

    def validate(self):
        if self.alert_info_list:
            for k in self.alert_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_desc is not None:
            result['AlertDesc'] = self.alert_desc
        if self.alert_desc_code is not None:
            result['AlertDescCode'] = self.alert_desc_code
        if self.alert_desc_en is not None:
            result['AlertDescEn'] = self.alert_desc_en
        if self.alert_detail is not None:
            result['AlertDetail'] = self.alert_detail
        result['AlertInfoList'] = []
        if self.alert_info_list is not None:
            for k in self.alert_info_list:
                result['AlertInfoList'].append(k.to_map() if k else None)
        if self.alert_level is not None:
            result['AlertLevel'] = self.alert_level
        if self.alert_name is not None:
            result['AlertName'] = self.alert_name
        if self.alert_name_code is not None:
            result['AlertNameCode'] = self.alert_name_code
        if self.alert_name_en is not None:
            result['AlertNameEn'] = self.alert_name_en
        if self.alert_src_prod is not None:
            result['AlertSrcProd'] = self.alert_src_prod
        if self.alert_src_prod_module is not None:
            result['AlertSrcProdModule'] = self.alert_src_prod_module
        if self.alert_title is not None:
            result['AlertTitle'] = self.alert_title
        if self.alert_title_en is not None:
            result['AlertTitleEn'] = self.alert_title_en
        if self.alert_type is not None:
            result['AlertType'] = self.alert_type
        if self.alert_type_code is not None:
            result['AlertTypeCode'] = self.alert_type_code
        if self.alert_type_en is not None:
            result['AlertTypeEn'] = self.alert_type_en
        if self.alert_uuid is not None:
            result['AlertUuid'] = self.alert_uuid
        if self.asset_list is not None:
            result['AssetList'] = self.asset_list
        if self.att_ck is not None:
            result['AttCk'] = self.att_ck
        if self.cloud_code is not None:
            result['CloudCode'] = self.cloud_code
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        if self.incident_uuid is not None:
            result['IncidentUuid'] = self.incident_uuid
        if self.is_defend is not None:
            result['IsDefend'] = self.is_defend
        if self.log_time is not None:
            result['LogTime'] = self.log_time
        if self.log_uuid is not None:
            result['LogUuid'] = self.log_uuid
        if self.main_user_id is not None:
            result['MainUserId'] = self.main_user_id
        if self.occur_time is not None:
            result['OccurTime'] = self.occur_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertDesc') is not None:
            self.alert_desc = m.get('AlertDesc')
        if m.get('AlertDescCode') is not None:
            self.alert_desc_code = m.get('AlertDescCode')
        if m.get('AlertDescEn') is not None:
            self.alert_desc_en = m.get('AlertDescEn')
        if m.get('AlertDetail') is not None:
            self.alert_detail = m.get('AlertDetail')
        self.alert_info_list = []
        if m.get('AlertInfoList') is not None:
            for k in m.get('AlertInfoList'):
                temp_model = DescribeAlertsWithEntityResponseBodyDataResponseDataAlertInfoList()
                self.alert_info_list.append(temp_model.from_map(k))
        if m.get('AlertLevel') is not None:
            self.alert_level = m.get('AlertLevel')
        if m.get('AlertName') is not None:
            self.alert_name = m.get('AlertName')
        if m.get('AlertNameCode') is not None:
            self.alert_name_code = m.get('AlertNameCode')
        if m.get('AlertNameEn') is not None:
            self.alert_name_en = m.get('AlertNameEn')
        if m.get('AlertSrcProd') is not None:
            self.alert_src_prod = m.get('AlertSrcProd')
        if m.get('AlertSrcProdModule') is not None:
            self.alert_src_prod_module = m.get('AlertSrcProdModule')
        if m.get('AlertTitle') is not None:
            self.alert_title = m.get('AlertTitle')
        if m.get('AlertTitleEn') is not None:
            self.alert_title_en = m.get('AlertTitleEn')
        if m.get('AlertType') is not None:
            self.alert_type = m.get('AlertType')
        if m.get('AlertTypeCode') is not None:
            self.alert_type_code = m.get('AlertTypeCode')
        if m.get('AlertTypeEn') is not None:
            self.alert_type_en = m.get('AlertTypeEn')
        if m.get('AlertUuid') is not None:
            self.alert_uuid = m.get('AlertUuid')
        if m.get('AssetList') is not None:
            self.asset_list = m.get('AssetList')
        if m.get('AttCk') is not None:
            self.att_ck = m.get('AttCk')
        if m.get('CloudCode') is not None:
            self.cloud_code = m.get('CloudCode')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IncidentUuid') is not None:
            self.incident_uuid = m.get('IncidentUuid')
        if m.get('IsDefend') is not None:
            self.is_defend = m.get('IsDefend')
        if m.get('LogTime') is not None:
            self.log_time = m.get('LogTime')
        if m.get('LogUuid') is not None:
            self.log_uuid = m.get('LogUuid')
        if m.get('MainUserId') is not None:
            self.main_user_id = m.get('MainUserId')
        if m.get('OccurTime') is not None:
            self.occur_time = m.get('OccurTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')
        return self


class DescribeAlertsWithEntityResponseBodyData(TeaModel):
    def __init__(
        self,
        page_info: DescribeAlertsWithEntityResponseBodyDataPageInfo = None,
        response_data: List[DescribeAlertsWithEntityResponseBodyDataResponseData] = None,
    ):
        self.page_info = page_info
        self.response_data = response_data

    def validate(self):
        if self.page_info:
            self.page_info.validate()
        if self.response_data:
            for k in self.response_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()
        result['ResponseData'] = []
        if self.response_data is not None:
            for k in self.response_data:
                result['ResponseData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageInfo') is not None:
            temp_model = DescribeAlertsWithEntityResponseBodyDataPageInfo()
            self.page_info = temp_model.from_map(m['PageInfo'])
        self.response_data = []
        if m.get('ResponseData') is not None:
            for k in m.get('ResponseData'):
                temp_model = DescribeAlertsWithEntityResponseBodyDataResponseData()
                self.response_data.append(temp_model.from_map(k))
        return self


class DescribeAlertsWithEntityResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: DescribeAlertsWithEntityResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
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
            temp_model = DescribeAlertsWithEntityResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeAlertsWithEntityResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAlertsWithEntityResponseBody = None,
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
            temp_model = DescribeAlertsWithEntityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAlertsWithEventRequest(TeaModel):
    def __init__(
        self,
        alert_title: str = None,
        current_page: int = None,
        incident_uuid: str = None,
        is_defend: str = None,
        level: List[str] = None,
        page_size: int = None,
        region_id: str = None,
        source: str = None,
        sub_user_id: int = None,
    ):
        self.alert_title = alert_title
        self.current_page = current_page
        self.incident_uuid = incident_uuid
        self.is_defend = is_defend
        self.level = level
        self.page_size = page_size
        self.region_id = region_id
        self.source = source
        self.sub_user_id = sub_user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_title is not None:
            result['AlertTitle'] = self.alert_title
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.incident_uuid is not None:
            result['IncidentUuid'] = self.incident_uuid
        if self.is_defend is not None:
            result['IsDefend'] = self.is_defend
        if self.level is not None:
            result['Level'] = self.level
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.source is not None:
            result['Source'] = self.source
        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertTitle') is not None:
            self.alert_title = m.get('AlertTitle')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('IncidentUuid') is not None:
            self.incident_uuid = m.get('IncidentUuid')
        if m.get('IsDefend') is not None:
            self.is_defend = m.get('IsDefend')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')
        return self


class DescribeAlertsWithEventResponseBodyDataPageInfo(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.current_page = current_page
        self.page_size = page_size
        self.total_count = total_count

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
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeAlertsWithEventResponseBodyDataResponseDataAlertInfoList(TeaModel):
    def __init__(
        self,
        key: str = None,
        key_name: str = None,
        values: str = None,
    ):
        self.key = key
        self.key_name = key_name
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.key_name is not None:
            result['KeyName'] = self.key_name
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('KeyName') is not None:
            self.key_name = m.get('KeyName')
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class DescribeAlertsWithEventResponseBodyDataResponseData(TeaModel):
    def __init__(
        self,
        alert_desc: str = None,
        alert_desc_code: str = None,
        alert_desc_en: str = None,
        alert_detail: str = None,
        alert_info_list: List[DescribeAlertsWithEventResponseBodyDataResponseDataAlertInfoList] = None,
        alert_level: str = None,
        alert_name: str = None,
        alert_name_code: str = None,
        alert_name_en: str = None,
        alert_src_prod: str = None,
        alert_src_prod_module: str = None,
        alert_title: str = None,
        alert_title_en: str = None,
        alert_type: str = None,
        alert_type_code: str = None,
        alert_type_en: str = None,
        alert_uuid: str = None,
        asset_list: str = None,
        att_ck: str = None,
        cloud_code: str = None,
        end_time: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        incident_uuid: str = None,
        is_defend: str = None,
        log_time: str = None,
        log_uuid: str = None,
        main_user_id: int = None,
        occur_time: str = None,
        start_time: str = None,
        sub_user_id: int = None,
    ):
        self.alert_desc = alert_desc
        self.alert_desc_code = alert_desc_code
        self.alert_desc_en = alert_desc_en
        self.alert_detail = alert_detail
        self.alert_info_list = alert_info_list
        self.alert_level = alert_level
        self.alert_name = alert_name
        self.alert_name_code = alert_name_code
        self.alert_name_en = alert_name_en
        self.alert_src_prod = alert_src_prod
        self.alert_src_prod_module = alert_src_prod_module
        self.alert_title = alert_title
        self.alert_title_en = alert_title_en
        self.alert_type = alert_type
        self.alert_type_code = alert_type_code
        self.alert_type_en = alert_type_en
        self.alert_uuid = alert_uuid
        self.asset_list = asset_list
        self.att_ck = att_ck
        self.cloud_code = cloud_code
        self.end_time = end_time
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.incident_uuid = incident_uuid
        self.is_defend = is_defend
        self.log_time = log_time
        self.log_uuid = log_uuid
        self.main_user_id = main_user_id
        self.occur_time = occur_time
        self.start_time = start_time
        self.sub_user_id = sub_user_id

    def validate(self):
        if self.alert_info_list:
            for k in self.alert_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_desc is not None:
            result['AlertDesc'] = self.alert_desc
        if self.alert_desc_code is not None:
            result['AlertDescCode'] = self.alert_desc_code
        if self.alert_desc_en is not None:
            result['AlertDescEn'] = self.alert_desc_en
        if self.alert_detail is not None:
            result['AlertDetail'] = self.alert_detail
        result['AlertInfoList'] = []
        if self.alert_info_list is not None:
            for k in self.alert_info_list:
                result['AlertInfoList'].append(k.to_map() if k else None)
        if self.alert_level is not None:
            result['AlertLevel'] = self.alert_level
        if self.alert_name is not None:
            result['AlertName'] = self.alert_name
        if self.alert_name_code is not None:
            result['AlertNameCode'] = self.alert_name_code
        if self.alert_name_en is not None:
            result['AlertNameEn'] = self.alert_name_en
        if self.alert_src_prod is not None:
            result['AlertSrcProd'] = self.alert_src_prod
        if self.alert_src_prod_module is not None:
            result['AlertSrcProdModule'] = self.alert_src_prod_module
        if self.alert_title is not None:
            result['AlertTitle'] = self.alert_title
        if self.alert_title_en is not None:
            result['AlertTitleEn'] = self.alert_title_en
        if self.alert_type is not None:
            result['AlertType'] = self.alert_type
        if self.alert_type_code is not None:
            result['AlertTypeCode'] = self.alert_type_code
        if self.alert_type_en is not None:
            result['AlertTypeEn'] = self.alert_type_en
        if self.alert_uuid is not None:
            result['AlertUuid'] = self.alert_uuid
        if self.asset_list is not None:
            result['AssetList'] = self.asset_list
        if self.att_ck is not None:
            result['AttCk'] = self.att_ck
        if self.cloud_code is not None:
            result['CloudCode'] = self.cloud_code
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        if self.incident_uuid is not None:
            result['IncidentUuid'] = self.incident_uuid
        if self.is_defend is not None:
            result['IsDefend'] = self.is_defend
        if self.log_time is not None:
            result['LogTime'] = self.log_time
        if self.log_uuid is not None:
            result['LogUuid'] = self.log_uuid
        if self.main_user_id is not None:
            result['MainUserId'] = self.main_user_id
        if self.occur_time is not None:
            result['OccurTime'] = self.occur_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertDesc') is not None:
            self.alert_desc = m.get('AlertDesc')
        if m.get('AlertDescCode') is not None:
            self.alert_desc_code = m.get('AlertDescCode')
        if m.get('AlertDescEn') is not None:
            self.alert_desc_en = m.get('AlertDescEn')
        if m.get('AlertDetail') is not None:
            self.alert_detail = m.get('AlertDetail')
        self.alert_info_list = []
        if m.get('AlertInfoList') is not None:
            for k in m.get('AlertInfoList'):
                temp_model = DescribeAlertsWithEventResponseBodyDataResponseDataAlertInfoList()
                self.alert_info_list.append(temp_model.from_map(k))
        if m.get('AlertLevel') is not None:
            self.alert_level = m.get('AlertLevel')
        if m.get('AlertName') is not None:
            self.alert_name = m.get('AlertName')
        if m.get('AlertNameCode') is not None:
            self.alert_name_code = m.get('AlertNameCode')
        if m.get('AlertNameEn') is not None:
            self.alert_name_en = m.get('AlertNameEn')
        if m.get('AlertSrcProd') is not None:
            self.alert_src_prod = m.get('AlertSrcProd')
        if m.get('AlertSrcProdModule') is not None:
            self.alert_src_prod_module = m.get('AlertSrcProdModule')
        if m.get('AlertTitle') is not None:
            self.alert_title = m.get('AlertTitle')
        if m.get('AlertTitleEn') is not None:
            self.alert_title_en = m.get('AlertTitleEn')
        if m.get('AlertType') is not None:
            self.alert_type = m.get('AlertType')
        if m.get('AlertTypeCode') is not None:
            self.alert_type_code = m.get('AlertTypeCode')
        if m.get('AlertTypeEn') is not None:
            self.alert_type_en = m.get('AlertTypeEn')
        if m.get('AlertUuid') is not None:
            self.alert_uuid = m.get('AlertUuid')
        if m.get('AssetList') is not None:
            self.asset_list = m.get('AssetList')
        if m.get('AttCk') is not None:
            self.att_ck = m.get('AttCk')
        if m.get('CloudCode') is not None:
            self.cloud_code = m.get('CloudCode')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IncidentUuid') is not None:
            self.incident_uuid = m.get('IncidentUuid')
        if m.get('IsDefend') is not None:
            self.is_defend = m.get('IsDefend')
        if m.get('LogTime') is not None:
            self.log_time = m.get('LogTime')
        if m.get('LogUuid') is not None:
            self.log_uuid = m.get('LogUuid')
        if m.get('MainUserId') is not None:
            self.main_user_id = m.get('MainUserId')
        if m.get('OccurTime') is not None:
            self.occur_time = m.get('OccurTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')
        return self


class DescribeAlertsWithEventResponseBodyData(TeaModel):
    def __init__(
        self,
        page_info: DescribeAlertsWithEventResponseBodyDataPageInfo = None,
        response_data: List[DescribeAlertsWithEventResponseBodyDataResponseData] = None,
    ):
        self.page_info = page_info
        self.response_data = response_data

    def validate(self):
        if self.page_info:
            self.page_info.validate()
        if self.response_data:
            for k in self.response_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()
        result['ResponseData'] = []
        if self.response_data is not None:
            for k in self.response_data:
                result['ResponseData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageInfo') is not None:
            temp_model = DescribeAlertsWithEventResponseBodyDataPageInfo()
            self.page_info = temp_model.from_map(m['PageInfo'])
        self.response_data = []
        if m.get('ResponseData') is not None:
            for k in m.get('ResponseData'):
                temp_model = DescribeAlertsWithEventResponseBodyDataResponseData()
                self.response_data.append(temp_model.from_map(k))
        return self


class DescribeAlertsWithEventResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: DescribeAlertsWithEventResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
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
            temp_model = DescribeAlertsWithEventResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeAlertsWithEventResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAlertsWithEventResponseBody = None,
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
            temp_model = DescribeAlertsWithEventResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAttackTimeLineRequest(TeaModel):
    def __init__(
        self,
        asset_name: str = None,
        end_time: int = None,
        incident_uuid: str = None,
        region_id: str = None,
        start_time: int = None,
    ):
        self.asset_name = asset_name
        self.end_time = end_time
        self.incident_uuid = incident_uuid
        self.region_id = region_id
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.asset_name is not None:
            result['AssetName'] = self.asset_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.incident_uuid is not None:
            result['IncidentUuid'] = self.incident_uuid
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssetName') is not None:
            self.asset_name = m.get('AssetName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('IncidentUuid') is not None:
            self.incident_uuid = m.get('IncidentUuid')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeAttackTimeLineResponseBodyData(TeaModel):
    def __init__(
        self,
        alert_level: str = None,
        alert_name: str = None,
        alert_name_code: str = None,
        alert_name_en: str = None,
        alert_src_prod: str = None,
        alert_src_prod_module: str = None,
        alert_time: int = None,
        alert_title: str = None,
        alert_title_en: str = None,
        alert_type: str = None,
        alert_type_code: str = None,
        alert_type_en: str = None,
        alert_uuid: str = None,
        asset_id: str = None,
        asset_list: str = None,
        asset_name: str = None,
        att_ck: str = None,
        cloud_code: str = None,
        incident_uuid: str = None,
        log_time: str = None,
    ):
        self.alert_level = alert_level
        self.alert_name = alert_name
        self.alert_name_code = alert_name_code
        self.alert_name_en = alert_name_en
        self.alert_src_prod = alert_src_prod
        self.alert_src_prod_module = alert_src_prod_module
        self.alert_time = alert_time
        self.alert_title = alert_title
        self.alert_title_en = alert_title_en
        self.alert_type = alert_type
        self.alert_type_code = alert_type_code
        self.alert_type_en = alert_type_en
        self.alert_uuid = alert_uuid
        self.asset_id = asset_id
        self.asset_list = asset_list
        self.asset_name = asset_name
        self.att_ck = att_ck
        self.cloud_code = cloud_code
        self.incident_uuid = incident_uuid
        self.log_time = log_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_level is not None:
            result['AlertLevel'] = self.alert_level
        if self.alert_name is not None:
            result['AlertName'] = self.alert_name
        if self.alert_name_code is not None:
            result['AlertNameCode'] = self.alert_name_code
        if self.alert_name_en is not None:
            result['AlertNameEn'] = self.alert_name_en
        if self.alert_src_prod is not None:
            result['AlertSrcProd'] = self.alert_src_prod
        if self.alert_src_prod_module is not None:
            result['AlertSrcProdModule'] = self.alert_src_prod_module
        if self.alert_time is not None:
            result['AlertTime'] = self.alert_time
        if self.alert_title is not None:
            result['AlertTitle'] = self.alert_title
        if self.alert_title_en is not None:
            result['AlertTitleEn'] = self.alert_title_en
        if self.alert_type is not None:
            result['AlertType'] = self.alert_type
        if self.alert_type_code is not None:
            result['AlertTypeCode'] = self.alert_type_code
        if self.alert_type_en is not None:
            result['AlertTypeEn'] = self.alert_type_en
        if self.alert_uuid is not None:
            result['AlertUuid'] = self.alert_uuid
        if self.asset_id is not None:
            result['AssetId'] = self.asset_id
        if self.asset_list is not None:
            result['AssetList'] = self.asset_list
        if self.asset_name is not None:
            result['AssetName'] = self.asset_name
        if self.att_ck is not None:
            result['AttCk'] = self.att_ck
        if self.cloud_code is not None:
            result['CloudCode'] = self.cloud_code
        if self.incident_uuid is not None:
            result['IncidentUuid'] = self.incident_uuid
        if self.log_time is not None:
            result['LogTime'] = self.log_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertLevel') is not None:
            self.alert_level = m.get('AlertLevel')
        if m.get('AlertName') is not None:
            self.alert_name = m.get('AlertName')
        if m.get('AlertNameCode') is not None:
            self.alert_name_code = m.get('AlertNameCode')
        if m.get('AlertNameEn') is not None:
            self.alert_name_en = m.get('AlertNameEn')
        if m.get('AlertSrcProd') is not None:
            self.alert_src_prod = m.get('AlertSrcProd')
        if m.get('AlertSrcProdModule') is not None:
            self.alert_src_prod_module = m.get('AlertSrcProdModule')
        if m.get('AlertTime') is not None:
            self.alert_time = m.get('AlertTime')
        if m.get('AlertTitle') is not None:
            self.alert_title = m.get('AlertTitle')
        if m.get('AlertTitleEn') is not None:
            self.alert_title_en = m.get('AlertTitleEn')
        if m.get('AlertType') is not None:
            self.alert_type = m.get('AlertType')
        if m.get('AlertTypeCode') is not None:
            self.alert_type_code = m.get('AlertTypeCode')
        if m.get('AlertTypeEn') is not None:
            self.alert_type_en = m.get('AlertTypeEn')
        if m.get('AlertUuid') is not None:
            self.alert_uuid = m.get('AlertUuid')
        if m.get('AssetId') is not None:
            self.asset_id = m.get('AssetId')
        if m.get('AssetList') is not None:
            self.asset_list = m.get('AssetList')
        if m.get('AssetName') is not None:
            self.asset_name = m.get('AssetName')
        if m.get('AttCk') is not None:
            self.att_ck = m.get('AttCk')
        if m.get('CloudCode') is not None:
            self.cloud_code = m.get('CloudCode')
        if m.get('IncidentUuid') is not None:
            self.incident_uuid = m.get('IncidentUuid')
        if m.get('LogTime') is not None:
            self.log_time = m.get('LogTime')
        return self


class DescribeAttackTimeLineResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: List[DescribeAttackTimeLineResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
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
                temp_model = DescribeAttackTimeLineResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeAttackTimeLineResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAttackTimeLineResponseBody = None,
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
            temp_model = DescribeAttackTimeLineResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAuthRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
    ):
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeAuthResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
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


class DescribeAuthResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAuthResponseBody = None,
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
            temp_model = DescribeAuthResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAutomateResponseConfigCounterRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
    ):
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeAutomateResponseConfigCounterResponseBodyData(TeaModel):
    def __init__(
        self,
        all: int = None,
        online: int = None,
    ):
        self.all = all
        self.online = online

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all is not None:
            result['All'] = self.all
        if self.online is not None:
            result['Online'] = self.online
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('All') is not None:
            self.all = m.get('All')
        if m.get('Online') is not None:
            self.online = m.get('Online')
        return self


class DescribeAutomateResponseConfigCounterResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: DescribeAutomateResponseConfigCounterResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
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
            temp_model = DescribeAutomateResponseConfigCounterResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeAutomateResponseConfigCounterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAutomateResponseConfigCounterResponseBody = None,
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
            temp_model = DescribeAutomateResponseConfigCounterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAutomateResponseConfigFeatureRequest(TeaModel):
    def __init__(
        self,
        auto_response_type: str = None,
        region_id: str = None,
    ):
        self.auto_response_type = auto_response_type
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_response_type is not None:
            result['AutoResponseType'] = self.auto_response_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoResponseType') is not None:
            self.auto_response_type = m.get('AutoResponseType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeAutomateResponseConfigFeatureResponseBodyDataRightValueEnums(TeaModel):
    def __init__(
        self,
        value: str = None,
        value_mds: str = None,
    ):
        self.value = value
        self.value_mds = value_mds

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.value is not None:
            result['Value'] = self.value
        if self.value_mds is not None:
            result['ValueMds'] = self.value_mds
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('ValueMds') is not None:
            self.value_mds = m.get('ValueMds')
        return self


class DescribeAutomateResponseConfigFeatureResponseBodyDataSupportOperators(TeaModel):
    def __init__(
        self,
        has_right_value: bool = None,
        index: int = None,
        operator: str = None,
        operator_desc_cn: str = None,
        operator_desc_en: str = None,
        operator_name: str = None,
        support_data_type: str = None,
        support_tag: List[str] = None,
    ):
        self.has_right_value = has_right_value
        self.index = index
        self.operator = operator
        self.operator_desc_cn = operator_desc_cn
        self.operator_desc_en = operator_desc_en
        self.operator_name = operator_name
        self.support_data_type = support_data_type
        self.support_tag = support_tag

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.has_right_value is not None:
            result['HasRightValue'] = self.has_right_value
        if self.index is not None:
            result['Index'] = self.index
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.operator_desc_cn is not None:
            result['OperatorDescCn'] = self.operator_desc_cn
        if self.operator_desc_en is not None:
            result['OperatorDescEn'] = self.operator_desc_en
        if self.operator_name is not None:
            result['OperatorName'] = self.operator_name
        if self.support_data_type is not None:
            result['SupportDataType'] = self.support_data_type
        if self.support_tag is not None:
            result['SupportTag'] = self.support_tag
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HasRightValue') is not None:
            self.has_right_value = m.get('HasRightValue')
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('OperatorDescCn') is not None:
            self.operator_desc_cn = m.get('OperatorDescCn')
        if m.get('OperatorDescEn') is not None:
            self.operator_desc_en = m.get('OperatorDescEn')
        if m.get('OperatorName') is not None:
            self.operator_name = m.get('OperatorName')
        if m.get('SupportDataType') is not None:
            self.support_data_type = m.get('SupportDataType')
        if m.get('SupportTag') is not None:
            self.support_tag = m.get('SupportTag')
        return self


class DescribeAutomateResponseConfigFeatureResponseBodyData(TeaModel):
    def __init__(
        self,
        data_type: str = None,
        feature: str = None,
        right_value_enums: List[DescribeAutomateResponseConfigFeatureResponseBodyDataRightValueEnums] = None,
        support_operators: List[DescribeAutomateResponseConfigFeatureResponseBodyDataSupportOperators] = None,
    ):
        self.data_type = data_type
        self.feature = feature
        self.right_value_enums = right_value_enums
        self.support_operators = support_operators

    def validate(self):
        if self.right_value_enums:
            for k in self.right_value_enums:
                if k:
                    k.validate()
        if self.support_operators:
            for k in self.support_operators:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_type is not None:
            result['DataType'] = self.data_type
        if self.feature is not None:
            result['Feature'] = self.feature
        result['RightValueEnums'] = []
        if self.right_value_enums is not None:
            for k in self.right_value_enums:
                result['RightValueEnums'].append(k.to_map() if k else None)
        result['SupportOperators'] = []
        if self.support_operators is not None:
            for k in self.support_operators:
                result['SupportOperators'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        if m.get('Feature') is not None:
            self.feature = m.get('Feature')
        self.right_value_enums = []
        if m.get('RightValueEnums') is not None:
            for k in m.get('RightValueEnums'):
                temp_model = DescribeAutomateResponseConfigFeatureResponseBodyDataRightValueEnums()
                self.right_value_enums.append(temp_model.from_map(k))
        self.support_operators = []
        if m.get('SupportOperators') is not None:
            for k in m.get('SupportOperators'):
                temp_model = DescribeAutomateResponseConfigFeatureResponseBodyDataSupportOperators()
                self.support_operators.append(temp_model.from_map(k))
        return self


class DescribeAutomateResponseConfigFeatureResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: List[DescribeAutomateResponseConfigFeatureResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
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
                temp_model = DescribeAutomateResponseConfigFeatureResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeAutomateResponseConfigFeatureResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAutomateResponseConfigFeatureResponseBody = None,
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
            temp_model = DescribeAutomateResponseConfigFeatureResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAutomateResponseConfigPlayBooksRequest(TeaModel):
    def __init__(
        self,
        auto_response_type: str = None,
        entity_type: str = None,
        region_id: str = None,
    ):
        self.auto_response_type = auto_response_type
        self.entity_type = entity_type
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_response_type is not None:
            result['AutoResponseType'] = self.auto_response_type
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoResponseType') is not None:
            self.auto_response_type = m.get('AutoResponseType')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeAutomateResponseConfigPlayBooksResponseBodyData(TeaModel):
    def __init__(
        self,
        description: str = None,
        display_name: str = None,
        name: str = None,
        param_type: str = None,
        uuid: str = None,
    ):
        self.description = description
        self.display_name = display_name
        self.name = name
        self.param_type = param_type
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.name is not None:
            result['Name'] = self.name
        if self.param_type is not None:
            result['ParamType'] = self.param_type
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ParamType') is not None:
            self.param_type = m.get('ParamType')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class DescribeAutomateResponseConfigPlayBooksResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: List[DescribeAutomateResponseConfigPlayBooksResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
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
                temp_model = DescribeAutomateResponseConfigPlayBooksResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeAutomateResponseConfigPlayBooksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAutomateResponseConfigPlayBooksResponseBody = None,
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
            temp_model = DescribeAutomateResponseConfigPlayBooksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCloudSiemAssetsRequest(TeaModel):
    def __init__(
        self,
        asset_type: str = None,
        current_page: int = None,
        incident_uuid: str = None,
        page_size: int = None,
        region_id: str = None,
    ):
        self.asset_type = asset_type
        self.current_page = current_page
        self.incident_uuid = incident_uuid
        self.page_size = page_size
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.asset_type is not None:
            result['AssetType'] = self.asset_type
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.incident_uuid is not None:
            result['IncidentUuid'] = self.incident_uuid
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssetType') is not None:
            self.asset_type = m.get('AssetType')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('IncidentUuid') is not None:
            self.incident_uuid = m.get('IncidentUuid')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeCloudSiemAssetsResponseBodyDataPageInfo(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.current_page = current_page
        self.page_size = page_size
        self.total_count = total_count

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
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeCloudSiemAssetsResponseBodyDataResponseDataAssetInfo(TeaModel):
    def __init__(
        self,
        key: str = None,
        key_name: str = None,
        values: str = None,
    ):
        self.key = key
        self.key_name = key_name
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.key_name is not None:
            result['KeyName'] = self.key_name
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('KeyName') is not None:
            self.key_name = m.get('KeyName')
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class DescribeCloudSiemAssetsResponseBodyDataResponseData(TeaModel):
    def __init__(
        self,
        alert_uuid: str = None,
        aliuid: int = None,
        asset_id: str = None,
        asset_info: List[DescribeCloudSiemAssetsResponseBodyDataResponseDataAssetInfo] = None,
        asset_name: str = None,
        asset_type: str = None,
        cloud_code: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        incident_uuid: str = None,
        sub_user_id: int = None,
    ):
        self.alert_uuid = alert_uuid
        self.aliuid = aliuid
        self.asset_id = asset_id
        self.asset_info = asset_info
        self.asset_name = asset_name
        self.asset_type = asset_type
        self.cloud_code = cloud_code
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.incident_uuid = incident_uuid
        self.sub_user_id = sub_user_id

    def validate(self):
        if self.asset_info:
            for k in self.asset_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_uuid is not None:
            result['AlertUuid'] = self.alert_uuid
        if self.aliuid is not None:
            result['Aliuid'] = self.aliuid
        if self.asset_id is not None:
            result['AssetId'] = self.asset_id
        result['AssetInfo'] = []
        if self.asset_info is not None:
            for k in self.asset_info:
                result['AssetInfo'].append(k.to_map() if k else None)
        if self.asset_name is not None:
            result['AssetName'] = self.asset_name
        if self.asset_type is not None:
            result['AssetType'] = self.asset_type
        if self.cloud_code is not None:
            result['CloudCode'] = self.cloud_code
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        if self.incident_uuid is not None:
            result['IncidentUuid'] = self.incident_uuid
        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertUuid') is not None:
            self.alert_uuid = m.get('AlertUuid')
        if m.get('Aliuid') is not None:
            self.aliuid = m.get('Aliuid')
        if m.get('AssetId') is not None:
            self.asset_id = m.get('AssetId')
        self.asset_info = []
        if m.get('AssetInfo') is not None:
            for k in m.get('AssetInfo'):
                temp_model = DescribeCloudSiemAssetsResponseBodyDataResponseDataAssetInfo()
                self.asset_info.append(temp_model.from_map(k))
        if m.get('AssetName') is not None:
            self.asset_name = m.get('AssetName')
        if m.get('AssetType') is not None:
            self.asset_type = m.get('AssetType')
        if m.get('CloudCode') is not None:
            self.cloud_code = m.get('CloudCode')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IncidentUuid') is not None:
            self.incident_uuid = m.get('IncidentUuid')
        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')
        return self


class DescribeCloudSiemAssetsResponseBodyData(TeaModel):
    def __init__(
        self,
        page_info: DescribeCloudSiemAssetsResponseBodyDataPageInfo = None,
        response_data: List[DescribeCloudSiemAssetsResponseBodyDataResponseData] = None,
    ):
        self.page_info = page_info
        self.response_data = response_data

    def validate(self):
        if self.page_info:
            self.page_info.validate()
        if self.response_data:
            for k in self.response_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()
        result['ResponseData'] = []
        if self.response_data is not None:
            for k in self.response_data:
                result['ResponseData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageInfo') is not None:
            temp_model = DescribeCloudSiemAssetsResponseBodyDataPageInfo()
            self.page_info = temp_model.from_map(m['PageInfo'])
        self.response_data = []
        if m.get('ResponseData') is not None:
            for k in m.get('ResponseData'):
                temp_model = DescribeCloudSiemAssetsResponseBodyDataResponseData()
                self.response_data.append(temp_model.from_map(k))
        return self


class DescribeCloudSiemAssetsResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: DescribeCloudSiemAssetsResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
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
            temp_model = DescribeCloudSiemAssetsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeCloudSiemAssetsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeCloudSiemAssetsResponseBody = None,
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
            temp_model = DescribeCloudSiemAssetsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCloudSiemAssetsCounterRequest(TeaModel):
    def __init__(
        self,
        incident_uuid: str = None,
        region_id: str = None,
    ):
        self.incident_uuid = incident_uuid
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.incident_uuid is not None:
            result['IncidentUuid'] = self.incident_uuid
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IncidentUuid') is not None:
            self.incident_uuid = m.get('IncidentUuid')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeCloudSiemAssetsCounterResponseBodyData(TeaModel):
    def __init__(
        self,
        asset_num: int = None,
        asset_type: str = None,
    ):
        self.asset_num = asset_num
        self.asset_type = asset_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.asset_num is not None:
            result['AssetNum'] = self.asset_num
        if self.asset_type is not None:
            result['AssetType'] = self.asset_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssetNum') is not None:
            self.asset_num = m.get('AssetNum')
        if m.get('AssetType') is not None:
            self.asset_type = m.get('AssetType')
        return self


class DescribeCloudSiemAssetsCounterResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: List[DescribeCloudSiemAssetsCounterResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
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
                temp_model = DescribeCloudSiemAssetsCounterResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeCloudSiemAssetsCounterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeCloudSiemAssetsCounterResponseBody = None,
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
            temp_model = DescribeCloudSiemAssetsCounterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCloudSiemEventDetailRequest(TeaModel):
    def __init__(
        self,
        incident_uuid: str = None,
        region_id: str = None,
    ):
        self.incident_uuid = incident_uuid
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.incident_uuid is not None:
            result['IncidentUuid'] = self.incident_uuid
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IncidentUuid') is not None:
            self.incident_uuid = m.get('IncidentUuid')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeCloudSiemEventDetailResponseBodyData(TeaModel):
    def __init__(
        self,
        alert_num: int = None,
        aliuid: int = None,
        asset_num: int = None,
        att_ck_labels: List[str] = None,
        data_sources: List[str] = None,
        description: str = None,
        description_en: str = None,
        ext_content: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        incident_name: str = None,
        incident_name_en: str = None,
        incident_uuid: str = None,
        remark: str = None,
        status: int = None,
        threat_level: str = None,
        threat_score: float = None,
    ):
        self.alert_num = alert_num
        self.aliuid = aliuid
        self.asset_num = asset_num
        self.att_ck_labels = att_ck_labels
        self.data_sources = data_sources
        self.description = description
        self.description_en = description_en
        self.ext_content = ext_content
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.incident_name = incident_name
        self.incident_name_en = incident_name_en
        self.incident_uuid = incident_uuid
        self.remark = remark
        self.status = status
        self.threat_level = threat_level
        self.threat_score = threat_score

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_num is not None:
            result['AlertNum'] = self.alert_num
        if self.aliuid is not None:
            result['Aliuid'] = self.aliuid
        if self.asset_num is not None:
            result['AssetNum'] = self.asset_num
        if self.att_ck_labels is not None:
            result['AttCkLabels'] = self.att_ck_labels
        if self.data_sources is not None:
            result['DataSources'] = self.data_sources
        if self.description is not None:
            result['Description'] = self.description
        if self.description_en is not None:
            result['DescriptionEn'] = self.description_en
        if self.ext_content is not None:
            result['ExtContent'] = self.ext_content
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.incident_name is not None:
            result['IncidentName'] = self.incident_name
        if self.incident_name_en is not None:
            result['IncidentNameEn'] = self.incident_name_en
        if self.incident_uuid is not None:
            result['IncidentUuid'] = self.incident_uuid
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.status is not None:
            result['Status'] = self.status
        if self.threat_level is not None:
            result['ThreatLevel'] = self.threat_level
        if self.threat_score is not None:
            result['ThreatScore'] = self.threat_score
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertNum') is not None:
            self.alert_num = m.get('AlertNum')
        if m.get('Aliuid') is not None:
            self.aliuid = m.get('Aliuid')
        if m.get('AssetNum') is not None:
            self.asset_num = m.get('AssetNum')
        if m.get('AttCkLabels') is not None:
            self.att_ck_labels = m.get('AttCkLabels')
        if m.get('DataSources') is not None:
            self.data_sources = m.get('DataSources')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DescriptionEn') is not None:
            self.description_en = m.get('DescriptionEn')
        if m.get('ExtContent') is not None:
            self.ext_content = m.get('ExtContent')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('IncidentName') is not None:
            self.incident_name = m.get('IncidentName')
        if m.get('IncidentNameEn') is not None:
            self.incident_name_en = m.get('IncidentNameEn')
        if m.get('IncidentUuid') is not None:
            self.incident_uuid = m.get('IncidentUuid')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ThreatLevel') is not None:
            self.threat_level = m.get('ThreatLevel')
        if m.get('ThreatScore') is not None:
            self.threat_score = m.get('ThreatScore')
        return self


class DescribeCloudSiemEventDetailResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: DescribeCloudSiemEventDetailResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
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
            temp_model = DescribeCloudSiemEventDetailResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeCloudSiemEventDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeCloudSiemEventDetailResponseBody = None,
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
            temp_model = DescribeCloudSiemEventDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCloudSiemEventsRequest(TeaModel):
    def __init__(
        self,
        asset_id: str = None,
        current_page: int = None,
        end_time: int = None,
        event_name: str = None,
        incident_uuid: str = None,
        order: str = None,
        order_field: str = None,
        page_size: int = None,
        region_id: str = None,
        start_time: int = None,
        status: int = None,
        thread_level: List[str] = None,
    ):
        self.asset_id = asset_id
        self.current_page = current_page
        self.end_time = end_time
        self.event_name = event_name
        self.incident_uuid = incident_uuid
        self.order = order
        self.order_field = order_field
        self.page_size = page_size
        self.region_id = region_id
        self.start_time = start_time
        self.status = status
        self.thread_level = thread_level

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.asset_id is not None:
            result['AssetId'] = self.asset_id
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.event_name is not None:
            result['EventName'] = self.event_name
        if self.incident_uuid is not None:
            result['IncidentUuid'] = self.incident_uuid
        if self.order is not None:
            result['Order'] = self.order
        if self.order_field is not None:
            result['OrderField'] = self.order_field
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.thread_level is not None:
            result['ThreadLevel'] = self.thread_level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssetId') is not None:
            self.asset_id = m.get('AssetId')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('EventName') is not None:
            self.event_name = m.get('EventName')
        if m.get('IncidentUuid') is not None:
            self.incident_uuid = m.get('IncidentUuid')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('OrderField') is not None:
            self.order_field = m.get('OrderField')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ThreadLevel') is not None:
            self.thread_level = m.get('ThreadLevel')
        return self


class DescribeCloudSiemEventsResponseBodyDataPageInfo(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.current_page = current_page
        self.page_size = page_size
        self.total_count = total_count

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
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeCloudSiemEventsResponseBodyDataResponseData(TeaModel):
    def __init__(
        self,
        alert_num: int = None,
        aliuid: int = None,
        asset_num: int = None,
        att_ck_labels: List[str] = None,
        data_sources: List[str] = None,
        description: str = None,
        description_en: str = None,
        ext_content: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        incident_name: str = None,
        incident_name_en: str = None,
        incident_uuid: str = None,
        remark: str = None,
        status: int = None,
        threat_level: str = None,
        threat_score: float = None,
    ):
        self.alert_num = alert_num
        self.aliuid = aliuid
        self.asset_num = asset_num
        self.att_ck_labels = att_ck_labels
        self.data_sources = data_sources
        self.description = description
        self.description_en = description_en
        self.ext_content = ext_content
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.incident_name = incident_name
        self.incident_name_en = incident_name_en
        self.incident_uuid = incident_uuid
        self.remark = remark
        self.status = status
        self.threat_level = threat_level
        self.threat_score = threat_score

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_num is not None:
            result['AlertNum'] = self.alert_num
        if self.aliuid is not None:
            result['Aliuid'] = self.aliuid
        if self.asset_num is not None:
            result['AssetNum'] = self.asset_num
        if self.att_ck_labels is not None:
            result['AttCkLabels'] = self.att_ck_labels
        if self.data_sources is not None:
            result['DataSources'] = self.data_sources
        if self.description is not None:
            result['Description'] = self.description
        if self.description_en is not None:
            result['DescriptionEn'] = self.description_en
        if self.ext_content is not None:
            result['ExtContent'] = self.ext_content
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.incident_name is not None:
            result['IncidentName'] = self.incident_name
        if self.incident_name_en is not None:
            result['IncidentNameEn'] = self.incident_name_en
        if self.incident_uuid is not None:
            result['IncidentUuid'] = self.incident_uuid
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.status is not None:
            result['Status'] = self.status
        if self.threat_level is not None:
            result['ThreatLevel'] = self.threat_level
        if self.threat_score is not None:
            result['ThreatScore'] = self.threat_score
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertNum') is not None:
            self.alert_num = m.get('AlertNum')
        if m.get('Aliuid') is not None:
            self.aliuid = m.get('Aliuid')
        if m.get('AssetNum') is not None:
            self.asset_num = m.get('AssetNum')
        if m.get('AttCkLabels') is not None:
            self.att_ck_labels = m.get('AttCkLabels')
        if m.get('DataSources') is not None:
            self.data_sources = m.get('DataSources')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DescriptionEn') is not None:
            self.description_en = m.get('DescriptionEn')
        if m.get('ExtContent') is not None:
            self.ext_content = m.get('ExtContent')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('IncidentName') is not None:
            self.incident_name = m.get('IncidentName')
        if m.get('IncidentNameEn') is not None:
            self.incident_name_en = m.get('IncidentNameEn')
        if m.get('IncidentUuid') is not None:
            self.incident_uuid = m.get('IncidentUuid')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ThreatLevel') is not None:
            self.threat_level = m.get('ThreatLevel')
        if m.get('ThreatScore') is not None:
            self.threat_score = m.get('ThreatScore')
        return self


class DescribeCloudSiemEventsResponseBodyData(TeaModel):
    def __init__(
        self,
        page_info: DescribeCloudSiemEventsResponseBodyDataPageInfo = None,
        response_data: List[DescribeCloudSiemEventsResponseBodyDataResponseData] = None,
    ):
        self.page_info = page_info
        self.response_data = response_data

    def validate(self):
        if self.page_info:
            self.page_info.validate()
        if self.response_data:
            for k in self.response_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()
        result['ResponseData'] = []
        if self.response_data is not None:
            for k in self.response_data:
                result['ResponseData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageInfo') is not None:
            temp_model = DescribeCloudSiemEventsResponseBodyDataPageInfo()
            self.page_info = temp_model.from_map(m['PageInfo'])
        self.response_data = []
        if m.get('ResponseData') is not None:
            for k in m.get('ResponseData'):
                temp_model = DescribeCloudSiemEventsResponseBodyDataResponseData()
                self.response_data.append(temp_model.from_map(k))
        return self


class DescribeCloudSiemEventsResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: DescribeCloudSiemEventsResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
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
            temp_model = DescribeCloudSiemEventsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeCloudSiemEventsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeCloudSiemEventsResponseBody = None,
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
            temp_model = DescribeCloudSiemEventsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCsImportedProdStatusByUserRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        source_log_prod: str = None,
        user_id: int = None,
    ):
        self.region_id = region_id
        self.source_log_prod = source_log_prod
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.source_log_prod is not None:
            result['SourceLogProd'] = self.source_log_prod
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SourceLogProd') is not None:
            self.source_log_prod = m.get('SourceLogProd')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class DescribeCsImportedProdStatusByUserResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
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


class DescribeCsImportedProdStatusByUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeCsImportedProdStatusByUserResponseBody = None,
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
            temp_model = DescribeCsImportedProdStatusByUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCustomizeRuleRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        rule_id: int = None,
    ):
        self.region_id = region_id
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class DescribeCustomizeRuleResponseBodyData(TeaModel):
    def __init__(
        self,
        alert_type: str = None,
        alert_type_mds: str = None,
        aliuid: int = None,
        event_transfer_ext: str = None,
        event_transfer_switch: int = None,
        event_transfer_type: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        log_source: str = None,
        log_source_mds: str = None,
        log_type: str = None,
        log_type_mds: str = None,
        query_cycle: str = None,
        rule_condition: str = None,
        rule_desc: str = None,
        rule_group: str = None,
        rule_name: str = None,
        rule_threshold: str = None,
        rule_type: str = None,
        status: int = None,
        threat_level: str = None,
    ):
        self.alert_type = alert_type
        self.alert_type_mds = alert_type_mds
        self.aliuid = aliuid
        self.event_transfer_ext = event_transfer_ext
        self.event_transfer_switch = event_transfer_switch
        self.event_transfer_type = event_transfer_type
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.log_source = log_source
        self.log_source_mds = log_source_mds
        self.log_type = log_type
        self.log_type_mds = log_type_mds
        self.query_cycle = query_cycle
        self.rule_condition = rule_condition
        self.rule_desc = rule_desc
        self.rule_group = rule_group
        self.rule_name = rule_name
        self.rule_threshold = rule_threshold
        self.rule_type = rule_type
        self.status = status
        self.threat_level = threat_level

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_type is not None:
            result['AlertType'] = self.alert_type
        if self.alert_type_mds is not None:
            result['AlertTypeMds'] = self.alert_type_mds
        if self.aliuid is not None:
            result['Aliuid'] = self.aliuid
        if self.event_transfer_ext is not None:
            result['EventTransferExt'] = self.event_transfer_ext
        if self.event_transfer_switch is not None:
            result['EventTransferSwitch'] = self.event_transfer_switch
        if self.event_transfer_type is not None:
            result['EventTransferType'] = self.event_transfer_type
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        if self.log_source is not None:
            result['LogSource'] = self.log_source
        if self.log_source_mds is not None:
            result['LogSourceMds'] = self.log_source_mds
        if self.log_type is not None:
            result['LogType'] = self.log_type
        if self.log_type_mds is not None:
            result['LogTypeMds'] = self.log_type_mds
        if self.query_cycle is not None:
            result['QueryCycle'] = self.query_cycle
        if self.rule_condition is not None:
            result['RuleCondition'] = self.rule_condition
        if self.rule_desc is not None:
            result['RuleDesc'] = self.rule_desc
        if self.rule_group is not None:
            result['RuleGroup'] = self.rule_group
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.rule_threshold is not None:
            result['RuleThreshold'] = self.rule_threshold
        if self.rule_type is not None:
            result['RuleType'] = self.rule_type
        if self.status is not None:
            result['Status'] = self.status
        if self.threat_level is not None:
            result['ThreatLevel'] = self.threat_level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertType') is not None:
            self.alert_type = m.get('AlertType')
        if m.get('AlertTypeMds') is not None:
            self.alert_type_mds = m.get('AlertTypeMds')
        if m.get('Aliuid') is not None:
            self.aliuid = m.get('Aliuid')
        if m.get('EventTransferExt') is not None:
            self.event_transfer_ext = m.get('EventTransferExt')
        if m.get('EventTransferSwitch') is not None:
            self.event_transfer_switch = m.get('EventTransferSwitch')
        if m.get('EventTransferType') is not None:
            self.event_transfer_type = m.get('EventTransferType')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LogSource') is not None:
            self.log_source = m.get('LogSource')
        if m.get('LogSourceMds') is not None:
            self.log_source_mds = m.get('LogSourceMds')
        if m.get('LogType') is not None:
            self.log_type = m.get('LogType')
        if m.get('LogTypeMds') is not None:
            self.log_type_mds = m.get('LogTypeMds')
        if m.get('QueryCycle') is not None:
            self.query_cycle = m.get('QueryCycle')
        if m.get('RuleCondition') is not None:
            self.rule_condition = m.get('RuleCondition')
        if m.get('RuleDesc') is not None:
            self.rule_desc = m.get('RuleDesc')
        if m.get('RuleGroup') is not None:
            self.rule_group = m.get('RuleGroup')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('RuleThreshold') is not None:
            self.rule_threshold = m.get('RuleThreshold')
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ThreatLevel') is not None:
            self.threat_level = m.get('ThreatLevel')
        return self


class DescribeCustomizeRuleResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: DescribeCustomizeRuleResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
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
            temp_model = DescribeCustomizeRuleResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeCustomizeRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeCustomizeRuleResponseBody = None,
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
            temp_model = DescribeCustomizeRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCustomizeRuleCountRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
    ):
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeCustomizeRuleCountResponseBodyData(TeaModel):
    def __init__(
        self,
        high_rule_num: int = None,
        in_use_rule_num: int = None,
        low_rule_num: int = None,
        medium_rule_num: int = None,
    ):
        self.high_rule_num = high_rule_num
        self.in_use_rule_num = in_use_rule_num
        self.low_rule_num = low_rule_num
        self.medium_rule_num = medium_rule_num

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.high_rule_num is not None:
            result['HighRuleNum'] = self.high_rule_num
        if self.in_use_rule_num is not None:
            result['InUseRuleNum'] = self.in_use_rule_num
        if self.low_rule_num is not None:
            result['LowRuleNum'] = self.low_rule_num
        if self.medium_rule_num is not None:
            result['MediumRuleNum'] = self.medium_rule_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HighRuleNum') is not None:
            self.high_rule_num = m.get('HighRuleNum')
        if m.get('InUseRuleNum') is not None:
            self.in_use_rule_num = m.get('InUseRuleNum')
        if m.get('LowRuleNum') is not None:
            self.low_rule_num = m.get('LowRuleNum')
        if m.get('MediumRuleNum') is not None:
            self.medium_rule_num = m.get('MediumRuleNum')
        return self


class DescribeCustomizeRuleCountResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: DescribeCustomizeRuleCountResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
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
            temp_model = DescribeCustomizeRuleCountResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeCustomizeRuleCountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeCustomizeRuleCountResponseBody = None,
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
            temp_model = DescribeCustomizeRuleCountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCustomizeRuleTestRequest(TeaModel):
    def __init__(
        self,
        id: int = None,
        region_id: str = None,
    ):
        self.id = id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeCustomizeRuleTestResponseBodyData(TeaModel):
    def __init__(
        self,
        id: int = None,
        simulate_data: str = None,
        status: int = None,
    ):
        self.id = id
        self.simulate_data = simulate_data
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.simulate_data is not None:
            result['SimulateData'] = self.simulate_data
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('SimulateData') is not None:
            self.simulate_data = m.get('SimulateData')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeCustomizeRuleTestResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: DescribeCustomizeRuleTestResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
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
            temp_model = DescribeCustomizeRuleTestResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeCustomizeRuleTestResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeCustomizeRuleTestResponseBody = None,
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
            temp_model = DescribeCustomizeRuleTestResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCustomizeRuleTestHistogramRequest(TeaModel):
    def __init__(
        self,
        id: int = None,
        region_id: str = None,
    ):
        self.id = id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeCustomizeRuleTestHistogramResponseBodyData(TeaModel):
    def __init__(
        self,
        count: int = None,
        from_: int = None,
        to: int = None,
    ):
        self.count = count
        self.from_ = from_
        self.to = to

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.from_ is not None:
            result['From'] = self.from_
        if self.to is not None:
            result['To'] = self.to
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('From') is not None:
            self.from_ = m.get('From')
        if m.get('To') is not None:
            self.to = m.get('To')
        return self


class DescribeCustomizeRuleTestHistogramResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: List[DescribeCustomizeRuleTestHistogramResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
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
                temp_model = DescribeCustomizeRuleTestHistogramResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeCustomizeRuleTestHistogramResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeCustomizeRuleTestHistogramResponseBody = None,
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
            temp_model = DescribeCustomizeRuleTestHistogramResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDataSourceInstanceRequest(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        cloud_code: str = None,
        data_source_instance_id: str = None,
        region_id: str = None,
    ):
        self.account_id = account_id
        self.cloud_code = cloud_code
        self.data_source_instance_id = data_source_instance_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.cloud_code is not None:
            result['CloudCode'] = self.cloud_code
        if self.data_source_instance_id is not None:
            result['DataSourceInstanceId'] = self.data_source_instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('CloudCode') is not None:
            self.cloud_code = m.get('CloudCode')
        if m.get('DataSourceInstanceId') is not None:
            self.data_source_instance_id = m.get('DataSourceInstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeDataSourceInstanceResponseBodyDataDataSourceInstanceParams(TeaModel):
    def __init__(
        self,
        para_code: str = None,
        para_value: str = None,
    ):
        self.para_code = para_code
        self.para_value = para_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.para_code is not None:
            result['ParaCode'] = self.para_code
        if self.para_value is not None:
            result['ParaValue'] = self.para_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParaCode') is not None:
            self.para_code = m.get('ParaCode')
        if m.get('ParaValue') is not None:
            self.para_value = m.get('ParaValue')
        return self


class DescribeDataSourceInstanceResponseBodyData(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        cloud_code: str = None,
        data_source_instance_id: str = None,
        data_source_instance_params: List[DescribeDataSourceInstanceResponseBodyDataDataSourceInstanceParams] = None,
    ):
        self.account_id = account_id
        self.cloud_code = cloud_code
        self.data_source_instance_id = data_source_instance_id
        self.data_source_instance_params = data_source_instance_params

    def validate(self):
        if self.data_source_instance_params:
            for k in self.data_source_instance_params:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.cloud_code is not None:
            result['CloudCode'] = self.cloud_code
        if self.data_source_instance_id is not None:
            result['DataSourceInstanceId'] = self.data_source_instance_id
        result['DataSourceInstanceParams'] = []
        if self.data_source_instance_params is not None:
            for k in self.data_source_instance_params:
                result['DataSourceInstanceParams'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('CloudCode') is not None:
            self.cloud_code = m.get('CloudCode')
        if m.get('DataSourceInstanceId') is not None:
            self.data_source_instance_id = m.get('DataSourceInstanceId')
        self.data_source_instance_params = []
        if m.get('DataSourceInstanceParams') is not None:
            for k in m.get('DataSourceInstanceParams'):
                temp_model = DescribeDataSourceInstanceResponseBodyDataDataSourceInstanceParams()
                self.data_source_instance_params.append(temp_model.from_map(k))
        return self


class DescribeDataSourceInstanceResponseBody(TeaModel):
    def __init__(
        self,
        data: DescribeDataSourceInstanceResponseBodyData = None,
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
            temp_model = DescribeDataSourceInstanceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDataSourceInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDataSourceInstanceResponseBody = None,
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
            temp_model = DescribeDataSourceInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDataSourceParametersRequest(TeaModel):
    def __init__(
        self,
        cloud_code: str = None,
        data_source_type: str = None,
        region_id: str = None,
    ):
        self.cloud_code = cloud_code
        self.data_source_type = data_source_type
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cloud_code is not None:
            result['CloudCode'] = self.cloud_code
        if self.data_source_type is not None:
            result['DataSourceType'] = self.data_source_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CloudCode') is not None:
            self.cloud_code = m.get('CloudCode')
        if m.get('DataSourceType') is not None:
            self.data_source_type = m.get('DataSourceType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeDataSourceParametersResponseBodyDataParamValue(TeaModel):
    def __init__(
        self,
        label: str = None,
        value: str = None,
    ):
        self.label = label
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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


class DescribeDataSourceParametersResponseBodyData(TeaModel):
    def __init__(
        self,
        can_editted: int = None,
        cloud_code: str = None,
        data_source_type: str = None,
        default_value: str = None,
        disabled: bool = None,
        format_check: str = None,
        hit: str = None,
        para_code: str = None,
        para_level: int = None,
        para_name: str = None,
        para_type: str = None,
        param_value: List[DescribeDataSourceParametersResponseBodyDataParamValue] = None,
        required: int = None,
        title: str = None,
    ):
        self.can_editted = can_editted
        self.cloud_code = cloud_code
        self.data_source_type = data_source_type
        self.default_value = default_value
        self.disabled = disabled
        self.format_check = format_check
        self.hit = hit
        self.para_code = para_code
        self.para_level = para_level
        self.para_name = para_name
        self.para_type = para_type
        self.param_value = param_value
        self.required = required
        self.title = title

    def validate(self):
        if self.param_value:
            for k in self.param_value:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.can_editted is not None:
            result['CanEditted'] = self.can_editted
        if self.cloud_code is not None:
            result['CloudCode'] = self.cloud_code
        if self.data_source_type is not None:
            result['DataSourceType'] = self.data_source_type
        if self.default_value is not None:
            result['DefaultValue'] = self.default_value
        if self.disabled is not None:
            result['Disabled'] = self.disabled
        if self.format_check is not None:
            result['FormatCheck'] = self.format_check
        if self.hit is not None:
            result['Hit'] = self.hit
        if self.para_code is not None:
            result['ParaCode'] = self.para_code
        if self.para_level is not None:
            result['ParaLevel'] = self.para_level
        if self.para_name is not None:
            result['ParaName'] = self.para_name
        if self.para_type is not None:
            result['ParaType'] = self.para_type
        result['ParamValue'] = []
        if self.param_value is not None:
            for k in self.param_value:
                result['ParamValue'].append(k.to_map() if k else None)
        if self.required is not None:
            result['Required'] = self.required
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CanEditted') is not None:
            self.can_editted = m.get('CanEditted')
        if m.get('CloudCode') is not None:
            self.cloud_code = m.get('CloudCode')
        if m.get('DataSourceType') is not None:
            self.data_source_type = m.get('DataSourceType')
        if m.get('DefaultValue') is not None:
            self.default_value = m.get('DefaultValue')
        if m.get('Disabled') is not None:
            self.disabled = m.get('Disabled')
        if m.get('FormatCheck') is not None:
            self.format_check = m.get('FormatCheck')
        if m.get('Hit') is not None:
            self.hit = m.get('Hit')
        if m.get('ParaCode') is not None:
            self.para_code = m.get('ParaCode')
        if m.get('ParaLevel') is not None:
            self.para_level = m.get('ParaLevel')
        if m.get('ParaName') is not None:
            self.para_name = m.get('ParaName')
        if m.get('ParaType') is not None:
            self.para_type = m.get('ParaType')
        self.param_value = []
        if m.get('ParamValue') is not None:
            for k in m.get('ParamValue'):
                temp_model = DescribeDataSourceParametersResponseBodyDataParamValue()
                self.param_value.append(temp_model.from_map(k))
        if m.get('Required') is not None:
            self.required = m.get('Required')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class DescribeDataSourceParametersResponseBody(TeaModel):
    def __init__(
        self,
        data: List[DescribeDataSourceParametersResponseBodyData] = None,
        request_id: str = None,
    ):
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
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = DescribeDataSourceParametersResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDataSourceParametersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDataSourceParametersResponseBody = None,
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
            temp_model = DescribeDataSourceParametersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDisposeAndPlaybookRequest(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        entity_type: str = None,
        incident_uuid: str = None,
        page_size: int = None,
        region_id: str = None,
    ):
        self.current_page = current_page
        self.entity_type = entity_type
        self.incident_uuid = incident_uuid
        self.page_size = page_size
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.incident_uuid is not None:
            result['IncidentUuid'] = self.incident_uuid
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('IncidentUuid') is not None:
            self.incident_uuid = m.get('IncidentUuid')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeDisposeAndPlaybookResponseBodyDataPageInfo(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.current_page = current_page
        self.page_size = page_size
        self.total_count = total_count

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
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeDisposeAndPlaybookResponseBodyDataResponseDataPlaybookList(TeaModel):
    def __init__(
        self,
        description: str = None,
        display_name: str = None,
        name: str = None,
        op_code: str = None,
        op_level: str = None,
        task_config: str = None,
        waf_playbook: bool = None,
    ):
        self.description = description
        self.display_name = display_name
        self.name = name
        self.op_code = op_code
        self.op_level = op_level
        self.task_config = task_config
        self.waf_playbook = waf_playbook

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.name is not None:
            result['Name'] = self.name
        if self.op_code is not None:
            result['OpCode'] = self.op_code
        if self.op_level is not None:
            result['OpLevel'] = self.op_level
        if self.task_config is not None:
            result['TaskConfig'] = self.task_config
        if self.waf_playbook is not None:
            result['WafPlaybook'] = self.waf_playbook
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OpCode') is not None:
            self.op_code = m.get('OpCode')
        if m.get('OpLevel') is not None:
            self.op_level = m.get('OpLevel')
        if m.get('TaskConfig') is not None:
            self.task_config = m.get('TaskConfig')
        if m.get('WafPlaybook') is not None:
            self.waf_playbook = m.get('WafPlaybook')
        return self


class DescribeDisposeAndPlaybookResponseBodyDataResponseData(TeaModel):
    def __init__(
        self,
        alert_num: int = None,
        dispose: str = None,
        entity_id: int = None,
        entity_info: Dict[str, Any] = None,
        opcode_map: Dict[str, str] = None,
        opcode_set: List[str] = None,
        playbook_list: List[DescribeDisposeAndPlaybookResponseBodyDataResponseDataPlaybookList] = None,
        scope: List[Any] = None,
    ):
        self.alert_num = alert_num
        self.dispose = dispose
        self.entity_id = entity_id
        self.entity_info = entity_info
        self.opcode_map = opcode_map
        self.opcode_set = opcode_set
        self.playbook_list = playbook_list
        self.scope = scope

    def validate(self):
        if self.playbook_list:
            for k in self.playbook_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_num is not None:
            result['AlertNum'] = self.alert_num
        if self.dispose is not None:
            result['Dispose'] = self.dispose
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        if self.entity_info is not None:
            result['EntityInfo'] = self.entity_info
        if self.opcode_map is not None:
            result['OpcodeMap'] = self.opcode_map
        if self.opcode_set is not None:
            result['OpcodeSet'] = self.opcode_set
        result['PlaybookList'] = []
        if self.playbook_list is not None:
            for k in self.playbook_list:
                result['PlaybookList'].append(k.to_map() if k else None)
        if self.scope is not None:
            result['Scope'] = self.scope
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertNum') is not None:
            self.alert_num = m.get('AlertNum')
        if m.get('Dispose') is not None:
            self.dispose = m.get('Dispose')
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        if m.get('EntityInfo') is not None:
            self.entity_info = m.get('EntityInfo')
        if m.get('OpcodeMap') is not None:
            self.opcode_map = m.get('OpcodeMap')
        if m.get('OpcodeSet') is not None:
            self.opcode_set = m.get('OpcodeSet')
        self.playbook_list = []
        if m.get('PlaybookList') is not None:
            for k in m.get('PlaybookList'):
                temp_model = DescribeDisposeAndPlaybookResponseBodyDataResponseDataPlaybookList()
                self.playbook_list.append(temp_model.from_map(k))
        if m.get('Scope') is not None:
            self.scope = m.get('Scope')
        return self


class DescribeDisposeAndPlaybookResponseBodyData(TeaModel):
    def __init__(
        self,
        page_info: DescribeDisposeAndPlaybookResponseBodyDataPageInfo = None,
        response_data: List[DescribeDisposeAndPlaybookResponseBodyDataResponseData] = None,
    ):
        self.page_info = page_info
        self.response_data = response_data

    def validate(self):
        if self.page_info:
            self.page_info.validate()
        if self.response_data:
            for k in self.response_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()
        result['ResponseData'] = []
        if self.response_data is not None:
            for k in self.response_data:
                result['ResponseData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageInfo') is not None:
            temp_model = DescribeDisposeAndPlaybookResponseBodyDataPageInfo()
            self.page_info = temp_model.from_map(m['PageInfo'])
        self.response_data = []
        if m.get('ResponseData') is not None:
            for k in m.get('ResponseData'):
                temp_model = DescribeDisposeAndPlaybookResponseBodyDataResponseData()
                self.response_data.append(temp_model.from_map(k))
        return self


class DescribeDisposeAndPlaybookResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: DescribeDisposeAndPlaybookResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
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
            temp_model = DescribeDisposeAndPlaybookResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeDisposeAndPlaybookResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDisposeAndPlaybookResponseBody = None,
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
            temp_model = DescribeDisposeAndPlaybookResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDisposeStrategyPlaybookRequest(TeaModel):
    def __init__(
        self,
        end_time: int = None,
        region_id: str = None,
        start_time: int = None,
    ):
        self.end_time = end_time
        self.region_id = region_id
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDisposeStrategyPlaybookResponseBodyData(TeaModel):
    def __init__(
        self,
        playbook_name: str = None,
        playbook_uuid: str = None,
    ):
        self.playbook_name = playbook_name
        self.playbook_uuid = playbook_uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.playbook_name is not None:
            result['PlaybookName'] = self.playbook_name
        if self.playbook_uuid is not None:
            result['PlaybookUuid'] = self.playbook_uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PlaybookName') is not None:
            self.playbook_name = m.get('PlaybookName')
        if m.get('PlaybookUuid') is not None:
            self.playbook_uuid = m.get('PlaybookUuid')
        return self


class DescribeDisposeStrategyPlaybookResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: List[DescribeDisposeStrategyPlaybookResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
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
                temp_model = DescribeDisposeStrategyPlaybookResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeDisposeStrategyPlaybookResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDisposeStrategyPlaybookResponseBody = None,
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
            temp_model = DescribeDisposeStrategyPlaybookResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeEntityInfoRequest(TeaModel):
    def __init__(
        self,
        entity_id: int = None,
        entity_identity: str = None,
        incident_uuid: str = None,
        region_id: str = None,
        sophon_task_id: str = None,
    ):
        self.entity_id = entity_id
        self.entity_identity = entity_identity
        self.incident_uuid = incident_uuid
        self.region_id = region_id
        self.sophon_task_id = sophon_task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        if self.entity_identity is not None:
            result['EntityIdentity'] = self.entity_identity
        if self.incident_uuid is not None:
            result['IncidentUuid'] = self.incident_uuid
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.sophon_task_id is not None:
            result['SophonTaskId'] = self.sophon_task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        if m.get('EntityIdentity') is not None:
            self.entity_identity = m.get('EntityIdentity')
        if m.get('IncidentUuid') is not None:
            self.incident_uuid = m.get('IncidentUuid')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SophonTaskId') is not None:
            self.sophon_task_id = m.get('SophonTaskId')
        return self


class DescribeEntityInfoResponseBodyData(TeaModel):
    def __init__(
        self,
        entity_id: int = None,
        entity_info: Dict[str, Any] = None,
        entity_type: str = None,
        tip_info: Dict[str, Any] = None,
    ):
        self.entity_id = entity_id
        self.entity_info = entity_info
        self.entity_type = entity_type
        self.tip_info = tip_info

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        if self.entity_info is not None:
            result['EntityInfo'] = self.entity_info
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.tip_info is not None:
            result['TipInfo'] = self.tip_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        if m.get('EntityInfo') is not None:
            self.entity_info = m.get('EntityInfo')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('TipInfo') is not None:
            self.tip_info = m.get('TipInfo')
        return self


class DescribeEntityInfoResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: DescribeEntityInfoResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
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
            temp_model = DescribeEntityInfoResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeEntityInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeEntityInfoResponseBody = None,
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
            temp_model = DescribeEntityInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeEventCountByThreatLevelRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
    ):
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeEventCountByThreatLevelResponseBodyData(TeaModel):
    def __init__(
        self,
        event_num: int = None,
        high_level_event_num: int = None,
        low_level_event_num: int = None,
        medium_level_event_num: int = None,
        undeal_event_num: int = None,
    ):
        self.event_num = event_num
        self.high_level_event_num = high_level_event_num
        self.low_level_event_num = low_level_event_num
        self.medium_level_event_num = medium_level_event_num
        self.undeal_event_num = undeal_event_num

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_num is not None:
            result['EventNum'] = self.event_num
        if self.high_level_event_num is not None:
            result['HighLevelEventNum'] = self.high_level_event_num
        if self.low_level_event_num is not None:
            result['LowLevelEventNum'] = self.low_level_event_num
        if self.medium_level_event_num is not None:
            result['MediumLevelEventNum'] = self.medium_level_event_num
        if self.undeal_event_num is not None:
            result['UndealEventNum'] = self.undeal_event_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventNum') is not None:
            self.event_num = m.get('EventNum')
        if m.get('HighLevelEventNum') is not None:
            self.high_level_event_num = m.get('HighLevelEventNum')
        if m.get('LowLevelEventNum') is not None:
            self.low_level_event_num = m.get('LowLevelEventNum')
        if m.get('MediumLevelEventNum') is not None:
            self.medium_level_event_num = m.get('MediumLevelEventNum')
        if m.get('UndealEventNum') is not None:
            self.undeal_event_num = m.get('UndealEventNum')
        return self


class DescribeEventCountByThreatLevelResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: DescribeEventCountByThreatLevelResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
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
            temp_model = DescribeEventCountByThreatLevelResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeEventCountByThreatLevelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeEventCountByThreatLevelResponseBody = None,
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
            temp_model = DescribeEventCountByThreatLevelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeEventDisposeRequest(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        incident_uuid: str = None,
        page_size: int = None,
        region_id: str = None,
    ):
        self.current_page = current_page
        self.incident_uuid = incident_uuid
        self.page_size = page_size
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.incident_uuid is not None:
            result['IncidentUuid'] = self.incident_uuid
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('IncidentUuid') is not None:
            self.incident_uuid = m.get('IncidentUuid')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeEventDisposeResponseBodyDataReceiverInfo(TeaModel):
    def __init__(
        self,
        channel: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        incident_uuid: str = None,
        message_title: str = None,
        receiver: str = None,
        status: int = None,
    ):
        self.channel = channel
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.incident_uuid = incident_uuid
        self.message_title = message_title
        self.receiver = receiver
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel is not None:
            result['Channel'] = self.channel
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        if self.incident_uuid is not None:
            result['IncidentUuid'] = self.incident_uuid
        if self.message_title is not None:
            result['MessageTitle'] = self.message_title
        if self.receiver is not None:
            result['Receiver'] = self.receiver
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Channel') is not None:
            self.channel = m.get('Channel')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IncidentUuid') is not None:
            self.incident_uuid = m.get('IncidentUuid')
        if m.get('MessageTitle') is not None:
            self.message_title = m.get('MessageTitle')
        if m.get('Receiver') is not None:
            self.receiver = m.get('Receiver')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeEventDisposeResponseBodyData(TeaModel):
    def __init__(
        self,
        event_dispose: List[Any] = None,
        receiver_info: DescribeEventDisposeResponseBodyDataReceiverInfo = None,
        remark: str = None,
        status: int = None,
    ):
        self.event_dispose = event_dispose
        self.receiver_info = receiver_info
        self.remark = remark
        self.status = status

    def validate(self):
        if self.receiver_info:
            self.receiver_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_dispose is not None:
            result['EventDispose'] = self.event_dispose
        if self.receiver_info is not None:
            result['ReceiverInfo'] = self.receiver_info.to_map()
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventDispose') is not None:
            self.event_dispose = m.get('EventDispose')
        if m.get('ReceiverInfo') is not None:
            temp_model = DescribeEventDisposeResponseBodyDataReceiverInfo()
            self.receiver_info = temp_model.from_map(m['ReceiverInfo'])
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeEventDisposeResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: DescribeEventDisposeResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
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
            temp_model = DescribeEventDisposeResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeEventDisposeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeEventDisposeResponseBody = None,
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
            temp_model = DescribeEventDisposeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeImportedLogCountRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
    ):
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeImportedLogCountResponseBodyData(TeaModel):
    def __init__(
        self,
        imported_log_count: int = None,
        total_log_count: int = None,
        un_imported_log_count: int = None,
    ):
        self.imported_log_count = imported_log_count
        self.total_log_count = total_log_count
        self.un_imported_log_count = un_imported_log_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.imported_log_count is not None:
            result['ImportedLogCount'] = self.imported_log_count
        if self.total_log_count is not None:
            result['TotalLogCount'] = self.total_log_count
        if self.un_imported_log_count is not None:
            result['UnImportedLogCount'] = self.un_imported_log_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImportedLogCount') is not None:
            self.imported_log_count = m.get('ImportedLogCount')
        if m.get('TotalLogCount') is not None:
            self.total_log_count = m.get('TotalLogCount')
        if m.get('UnImportedLogCount') is not None:
            self.un_imported_log_count = m.get('UnImportedLogCount')
        return self


class DescribeImportedLogCountResponseBody(TeaModel):
    def __init__(
        self,
        data: DescribeImportedLogCountResponseBodyData = None,
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
            temp_model = DescribeImportedLogCountResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeImportedLogCountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeImportedLogCountResponseBody = None,
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
            temp_model = DescribeImportedLogCountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeJobStatusRequest(TeaModel):
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


class DescribeJobStatusResponseBodyDataErrTaskListProductListLogList(TeaModel):
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


class DescribeJobStatusResponseBodyDataErrTaskListProductList(TeaModel):
    def __init__(
        self,
        log_list: List[DescribeJobStatusResponseBodyDataErrTaskListProductListLogList] = None,
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
                temp_model = DescribeJobStatusResponseBodyDataErrTaskListProductListLogList()
                self.log_list.append(temp_model.from_map(k))
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        return self


class DescribeJobStatusResponseBodyDataErrTaskList(TeaModel):
    def __init__(
        self,
        product_list: List[DescribeJobStatusResponseBodyDataErrTaskListProductList] = None,
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
                temp_model = DescribeJobStatusResponseBodyDataErrTaskListProductList()
                self.product_list.append(temp_model.from_map(k))
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class DescribeJobStatusResponseBodyData(TeaModel):
    def __init__(
        self,
        config_id: str = None,
        err_task_list: List[DescribeJobStatusResponseBodyDataErrTaskList] = None,
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
                temp_model = DescribeJobStatusResponseBodyDataErrTaskList()
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


class DescribeJobStatusResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: DescribeJobStatusResponseBodyData = None,
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
            temp_model = DescribeJobStatusResponseBodyData()
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


class DescribeLogFieldsRequest(TeaModel):
    def __init__(
        self,
        log_source: str = None,
        log_type: str = None,
        region_id: str = None,
    ):
        self.log_source = log_source
        self.log_type = log_type
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.log_source is not None:
            result['LogSource'] = self.log_source
        if self.log_type is not None:
            result['LogType'] = self.log_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LogSource') is not None:
            self.log_source = m.get('LogSource')
        if m.get('LogType') is not None:
            self.log_type = m.get('LogType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeLogFieldsResponseBodyData(TeaModel):
    def __init__(
        self,
        activity_name: str = None,
        field_desc: str = None,
        field_name: str = None,
        field_type: str = None,
        log_code: str = None,
    ):
        self.activity_name = activity_name
        self.field_desc = field_desc
        self.field_name = field_name
        self.field_type = field_type
        self.log_code = log_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.activity_name is not None:
            result['ActivityName'] = self.activity_name
        if self.field_desc is not None:
            result['FieldDesc'] = self.field_desc
        if self.field_name is not None:
            result['FieldName'] = self.field_name
        if self.field_type is not None:
            result['FieldType'] = self.field_type
        if self.log_code is not None:
            result['LogCode'] = self.log_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActivityName') is not None:
            self.activity_name = m.get('ActivityName')
        if m.get('FieldDesc') is not None:
            self.field_desc = m.get('FieldDesc')
        if m.get('FieldName') is not None:
            self.field_name = m.get('FieldName')
        if m.get('FieldType') is not None:
            self.field_type = m.get('FieldType')
        if m.get('LogCode') is not None:
            self.log_code = m.get('LogCode')
        return self


class DescribeLogFieldsResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: List[DescribeLogFieldsResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
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
                temp_model = DescribeLogFieldsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeLogFieldsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeLogFieldsResponseBody = None,
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
            temp_model = DescribeLogFieldsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeLogSourceRequest(TeaModel):
    def __init__(
        self,
        log_type: str = None,
        region_id: str = None,
    ):
        self.log_type = log_type
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.log_type is not None:
            result['LogType'] = self.log_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LogType') is not None:
            self.log_type = m.get('LogType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeLogSourceResponseBodyData(TeaModel):
    def __init__(
        self,
        log_source: str = None,
        log_source_name: str = None,
    ):
        self.log_source = log_source
        self.log_source_name = log_source_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.log_source is not None:
            result['LogSource'] = self.log_source
        if self.log_source_name is not None:
            result['LogSourceName'] = self.log_source_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LogSource') is not None:
            self.log_source = m.get('LogSource')
        if m.get('LogSourceName') is not None:
            self.log_source_name = m.get('LogSourceName')
        return self


class DescribeLogSourceResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: List[DescribeLogSourceResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
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
                temp_model = DescribeLogSourceResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeLogSourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeLogSourceResponseBody = None,
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
            temp_model = DescribeLogSourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeLogStoreRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
    ):
        # The region in which the data management center of the threat analysis feature resides. Specify this parameter based on the region where your assets reside. Valid values:
        # 
        # *   cn-hangzhou: Your assets reside in regions inside the Chinese mainland or in the China (Hong Kong) region.
        # *   ap-southeast-1: Your assets reside in regions outside the Chinese mainland, excluding the China (Hong Kong) region.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeLogStoreResponseBodyData(TeaModel):
    def __init__(
        self,
        append_meta: bool = None,
        auto_split: bool = None,
        enable_tracking: bool = None,
        log_store_name: str = None,
        max_split_shard: int = None,
        shard_count: int = None,
        ttl: int = None,
    ):
        # Indicates whether the following time points are added after the log arrives: the time points when the public IP address of the client and the log arrive. Valid values:
        # 
        # *   true
        # *   false
        self.append_meta = append_meta
        # Indicates whether the automatic sharding feature is enabled. Valid values:
        # 
        # *   true
        # *   false
        self.auto_split = auto_split
        # Indicates whether the web tracking feature is enabled to collect user information from browsers, iOS applications, or Android applications. Valid values:
        # 
        # *   true
        # *   false
        self.enable_tracking = enable_tracking
        # The name of the Logstore in Simple Log Service.
        self.log_store_name = log_store_name
        # The maximum number of shards that can be generated by using the automatic sharding feature.
        self.max_split_shard = max_split_shard
        # The number of shards in Log Service.
        self.shard_count = shard_count
        # The retention period of data. Unit: day.
        self.ttl = ttl

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.append_meta is not None:
            result['AppendMeta'] = self.append_meta
        if self.auto_split is not None:
            result['AutoSplit'] = self.auto_split
        if self.enable_tracking is not None:
            result['EnableTracking'] = self.enable_tracking
        if self.log_store_name is not None:
            result['LogStoreName'] = self.log_store_name
        if self.max_split_shard is not None:
            result['MaxSplitShard'] = self.max_split_shard
        if self.shard_count is not None:
            result['ShardCount'] = self.shard_count
        if self.ttl is not None:
            result['Ttl'] = self.ttl
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppendMeta') is not None:
            self.append_meta = m.get('AppendMeta')
        if m.get('AutoSplit') is not None:
            self.auto_split = m.get('AutoSplit')
        if m.get('EnableTracking') is not None:
            self.enable_tracking = m.get('EnableTracking')
        if m.get('LogStoreName') is not None:
            self.log_store_name = m.get('LogStoreName')
        if m.get('MaxSplitShard') is not None:
            self.max_split_shard = m.get('MaxSplitShard')
        if m.get('ShardCount') is not None:
            self.shard_count = m.get('ShardCount')
        if m.get('Ttl') is not None:
            self.ttl = m.get('Ttl')
        return self


class DescribeLogStoreResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: DescribeLogStoreResponseBodyData = None,
        dy_code: str = None,
        dy_message: str = None,
        err_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code.
        self.code = code
        # The response of the threat analysis feature.
        self.data = data
        # The dynamic error code.
        self.dy_code = dy_code
        # The dynamic message.
        self.dy_message = dy_message
        # The error code.
        self.err_code = err_code
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
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
        if self.dy_code is not None:
            result['DyCode'] = self.dy_code
        if self.dy_message is not None:
            result['DyMessage'] = self.dy_message
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
            temp_model = DescribeLogStoreResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('DyCode') is not None:
            self.dy_code = m.get('DyCode')
        if m.get('DyMessage') is not None:
            self.dy_message = m.get('DyMessage')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeLogStoreResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeLogStoreResponseBody = None,
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
            temp_model = DescribeLogStoreResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeLogTypeRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
    ):
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeLogTypeResponseBodyData(TeaModel):
    def __init__(
        self,
        log_type: str = None,
        log_type_name: str = None,
    ):
        self.log_type = log_type
        self.log_type_name = log_type_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.log_type is not None:
            result['LogType'] = self.log_type
        if self.log_type_name is not None:
            result['LogTypeName'] = self.log_type_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LogType') is not None:
            self.log_type = m.get('LogType')
        if m.get('LogTypeName') is not None:
            self.log_type_name = m.get('LogTypeName')
        return self


class DescribeLogTypeResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: List[DescribeLogTypeResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
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
                temp_model = DescribeLogTypeResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeLogTypeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeLogTypeResponseBody = None,
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
            temp_model = DescribeLogTypeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeOperatorsRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        scene_type: str = None,
    ):
        self.region_id = region_id
        self.scene_type = scene_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.scene_type is not None:
            result['SceneType'] = self.scene_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SceneType') is not None:
            self.scene_type = m.get('SceneType')
        return self


class DescribeOperatorsResponseBodyData(TeaModel):
    def __init__(
        self,
        index: int = None,
        operator: str = None,
        operator_desc_cn: str = None,
        operator_desc_en: str = None,
        operator_name: str = None,
        support_data_type: str = None,
        support_tag: List[str] = None,
    ):
        self.index = index
        self.operator = operator
        self.operator_desc_cn = operator_desc_cn
        self.operator_desc_en = operator_desc_en
        self.operator_name = operator_name
        self.support_data_type = support_data_type
        self.support_tag = support_tag

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.index is not None:
            result['Index'] = self.index
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.operator_desc_cn is not None:
            result['OperatorDescCn'] = self.operator_desc_cn
        if self.operator_desc_en is not None:
            result['OperatorDescEn'] = self.operator_desc_en
        if self.operator_name is not None:
            result['OperatorName'] = self.operator_name
        if self.support_data_type is not None:
            result['SupportDataType'] = self.support_data_type
        if self.support_tag is not None:
            result['SupportTag'] = self.support_tag
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('OperatorDescCn') is not None:
            self.operator_desc_cn = m.get('OperatorDescCn')
        if m.get('OperatorDescEn') is not None:
            self.operator_desc_en = m.get('OperatorDescEn')
        if m.get('OperatorName') is not None:
            self.operator_name = m.get('OperatorName')
        if m.get('SupportDataType') is not None:
            self.support_data_type = m.get('SupportDataType')
        if m.get('SupportTag') is not None:
            self.support_tag = m.get('SupportTag')
        return self


class DescribeOperatorsResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: List[DescribeOperatorsResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
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
                temp_model = DescribeOperatorsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeOperatorsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeOperatorsResponseBody = None,
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
            temp_model = DescribeOperatorsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeProdCountRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
    ):
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeProdCountResponseBodyData(TeaModel):
    def __init__(
        self,
        aliyun_prod_count: int = None,
        hcloud_prod_count: int = None,
        qcloud_prod_count: int = None,
    ):
        self.aliyun_prod_count = aliyun_prod_count
        self.hcloud_prod_count = hcloud_prod_count
        self.qcloud_prod_count = qcloud_prod_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aliyun_prod_count is not None:
            result['AliyunProdCount'] = self.aliyun_prod_count
        if self.hcloud_prod_count is not None:
            result['HcloudProdCount'] = self.hcloud_prod_count
        if self.qcloud_prod_count is not None:
            result['QcloudProdCount'] = self.qcloud_prod_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliyunProdCount') is not None:
            self.aliyun_prod_count = m.get('AliyunProdCount')
        if m.get('HcloudProdCount') is not None:
            self.hcloud_prod_count = m.get('HcloudProdCount')
        if m.get('QcloudProdCount') is not None:
            self.qcloud_prod_count = m.get('QcloudProdCount')
        return self


class DescribeProdCountResponseBody(TeaModel):
    def __init__(
        self,
        data: DescribeProdCountResponseBodyData = None,
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
            temp_model = DescribeProdCountResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeProdCountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeProdCountResponseBody = None,
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
            temp_model = DescribeProdCountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeScopeUsersRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
    ):
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeScopeUsersResponseBodyData(TeaModel):
    def __init__(
        self,
        ali_uid: int = None,
        domains: List[str] = None,
        instance_id: str = None,
        user_name: str = None,
    ):
        self.ali_uid = ali_uid
        self.domains = domains
        self.instance_id = instance_id
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.domains is not None:
            result['Domains'] = self.domains
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('Domains') is not None:
            self.domains = m.get('Domains')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class DescribeScopeUsersResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: List[DescribeScopeUsersResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
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
                temp_model = DescribeScopeUsersResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeScopeUsersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeScopeUsersResponseBody = None,
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
            temp_model = DescribeScopeUsersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeServiceStatusRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
    ):
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeServiceStatusResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
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


class DescribeServiceStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeServiceStatusResponseBody = None,
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
            temp_model = DescribeServiceStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeStorageRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
    ):
        # The region in which the data management center of the threat analysis feature resides. Specify this parameter based on the region where your assets reside. Valid values:
        # 
        # *   cn-hangzhou: Your assets reside in regions inside the Chinese mainland or in the China (Hong Kong) region.
        # *   ap-southeast-1: Your assets reside in regions outside the Chinese mainland, excluding the China (Hong Kong) region.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeStorageResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: bool = None,
        dy_code: str = None,
        dy_message: str = None,
        err_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code.
        self.code = code
        # Indicates whether the projects and Logstores that are created for the threat analysis feature exist in Simple Log Service. Valid values:
        # 
        # *   true
        # *   false
        self.data = data
        # The dynamic error code.
        self.dy_code = dy_code
        # The dynamic message.
        self.dy_message = dy_message
        # The error code.
        self.err_code = err_code
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
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
        if self.dy_code is not None:
            result['DyCode'] = self.dy_code
        if self.dy_message is not None:
            result['DyMessage'] = self.dy_message
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
        if m.get('DyCode') is not None:
            self.dy_code = m.get('DyCode')
        if m.get('DyMessage') is not None:
            self.dy_message = m.get('DyMessage')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeStorageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeStorageResponseBody = None,
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
            temp_model = DescribeStorageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUserBuyStatusRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        sub_user_id: int = None,
    ):
        self.region_id = region_id
        self.sub_user_id = sub_user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')
        return self


class DescribeUserBuyStatusResponseBodyData(TeaModel):
    def __init__(
        self,
        can_buy: bool = None,
        capacity: int = None,
        duration_days: int = None,
        end_time: int = None,
        main_user_id: int = None,
        main_user_name: str = None,
        master_user_id: int = None,
        master_user_name: str = None,
        sas_instance_id: str = None,
        sub_user_id: int = None,
        sub_user_name: str = None,
    ):
        self.can_buy = can_buy
        self.capacity = capacity
        self.duration_days = duration_days
        self.end_time = end_time
        self.main_user_id = main_user_id
        self.main_user_name = main_user_name
        self.master_user_id = master_user_id
        self.master_user_name = master_user_name
        self.sas_instance_id = sas_instance_id
        self.sub_user_id = sub_user_id
        self.sub_user_name = sub_user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.can_buy is not None:
            result['CanBuy'] = self.can_buy
        if self.capacity is not None:
            result['Capacity'] = self.capacity
        if self.duration_days is not None:
            result['DurationDays'] = self.duration_days
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.main_user_id is not None:
            result['MainUserId'] = self.main_user_id
        if self.main_user_name is not None:
            result['MainUserName'] = self.main_user_name
        if self.master_user_id is not None:
            result['MasterUserId'] = self.master_user_id
        if self.master_user_name is not None:
            result['MasterUserName'] = self.master_user_name
        if self.sas_instance_id is not None:
            result['SasInstanceId'] = self.sas_instance_id
        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id
        if self.sub_user_name is not None:
            result['SubUserName'] = self.sub_user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CanBuy') is not None:
            self.can_buy = m.get('CanBuy')
        if m.get('Capacity') is not None:
            self.capacity = m.get('Capacity')
        if m.get('DurationDays') is not None:
            self.duration_days = m.get('DurationDays')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('MainUserId') is not None:
            self.main_user_id = m.get('MainUserId')
        if m.get('MainUserName') is not None:
            self.main_user_name = m.get('MainUserName')
        if m.get('MasterUserId') is not None:
            self.master_user_id = m.get('MasterUserId')
        if m.get('MasterUserName') is not None:
            self.master_user_name = m.get('MasterUserName')
        if m.get('SasInstanceId') is not None:
            self.sas_instance_id = m.get('SasInstanceId')
        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')
        if m.get('SubUserName') is not None:
            self.sub_user_name = m.get('SubUserName')
        return self


class DescribeUserBuyStatusResponseBody(TeaModel):
    def __init__(
        self,
        data: DescribeUserBuyStatusResponseBodyData = None,
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
            temp_model = DescribeUserBuyStatusResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeUserBuyStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeUserBuyStatusResponseBody = None,
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
            temp_model = DescribeUserBuyStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeWafScopeRequest(TeaModel):
    def __init__(
        self,
        entity_id: int = None,
        region_id: str = None,
    ):
        self.entity_id = entity_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeWafScopeResponseBodyData(TeaModel):
    def __init__(
        self,
        aliuid: int = None,
        domains: List[str] = None,
        instance_id: str = None,
    ):
        self.aliuid = aliuid
        self.domains = domains
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aliuid is not None:
            result['Aliuid'] = self.aliuid
        if self.domains is not None:
            result['Domains'] = self.domains
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Aliuid') is not None:
            self.aliuid = m.get('Aliuid')
        if m.get('Domains') is not None:
            self.domains = m.get('Domains')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DescribeWafScopeResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: List[DescribeWafScopeResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
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
                temp_model = DescribeWafScopeResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeWafScopeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeWafScopeResponseBody = None,
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
            temp_model = DescribeWafScopeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeWhiteRuleListRequest(TeaModel):
    def __init__(
        self,
        alert_name: str = None,
        alert_type: str = None,
        current_page: int = None,
        incident_uuid: str = None,
        page_size: int = None,
        region_id: str = None,
    ):
        self.alert_name = alert_name
        self.alert_type = alert_type
        self.current_page = current_page
        self.incident_uuid = incident_uuid
        self.page_size = page_size
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_name is not None:
            result['AlertName'] = self.alert_name
        if self.alert_type is not None:
            result['AlertType'] = self.alert_type
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.incident_uuid is not None:
            result['IncidentUuid'] = self.incident_uuid
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertName') is not None:
            self.alert_name = m.get('AlertName')
        if m.get('AlertType') is not None:
            self.alert_type = m.get('AlertType')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('IncidentUuid') is not None:
            self.incident_uuid = m.get('IncidentUuid')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeWhiteRuleListResponseBodyDataPageInfo(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.current_page = current_page
        self.page_size = page_size
        self.total_count = total_count

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
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeWhiteRuleListResponseBodyDataResponseDataExpressionConditionsLeft(TeaModel):
    def __init__(
        self,
        is_var: bool = None,
        modifier: str = None,
        modifier_param: Dict[str, Any] = None,
        type: str = None,
        value: str = None,
    ):
        self.is_var = is_var
        self.modifier = modifier
        self.modifier_param = modifier_param
        self.type = type
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_var is not None:
            result['IsVar'] = self.is_var
        if self.modifier is not None:
            result['Modifier'] = self.modifier
        if self.modifier_param is not None:
            result['ModifierParam'] = self.modifier_param
        if self.type is not None:
            result['Type'] = self.type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsVar') is not None:
            self.is_var = m.get('IsVar')
        if m.get('Modifier') is not None:
            self.modifier = m.get('Modifier')
        if m.get('ModifierParam') is not None:
            self.modifier_param = m.get('ModifierParam')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeWhiteRuleListResponseBodyDataResponseDataExpressionConditionsRight(TeaModel):
    def __init__(
        self,
        is_var: bool = None,
        modifier: str = None,
        modifier_param: Dict[str, Any] = None,
        type: str = None,
        value: str = None,
    ):
        self.is_var = is_var
        self.modifier = modifier
        self.modifier_param = modifier_param
        self.type = type
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_var is not None:
            result['IsVar'] = self.is_var
        if self.modifier is not None:
            result['Modifier'] = self.modifier
        if self.modifier_param is not None:
            result['ModifierParam'] = self.modifier_param
        if self.type is not None:
            result['Type'] = self.type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsVar') is not None:
            self.is_var = m.get('IsVar')
        if m.get('Modifier') is not None:
            self.modifier = m.get('Modifier')
        if m.get('ModifierParam') is not None:
            self.modifier_param = m.get('ModifierParam')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeWhiteRuleListResponseBodyDataResponseDataExpressionConditions(TeaModel):
    def __init__(
        self,
        is_not: bool = None,
        item_id: int = None,
        left: DescribeWhiteRuleListResponseBodyDataResponseDataExpressionConditionsLeft = None,
        operator: str = None,
        right: DescribeWhiteRuleListResponseBodyDataResponseDataExpressionConditionsRight = None,
    ):
        self.is_not = is_not
        self.item_id = item_id
        self.left = left
        self.operator = operator
        self.right = right

    def validate(self):
        if self.left:
            self.left.validate()
        if self.right:
            self.right.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_not is not None:
            result['IsNot'] = self.is_not
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.left is not None:
            result['Left'] = self.left.to_map()
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.right is not None:
            result['Right'] = self.right.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsNot') is not None:
            self.is_not = m.get('IsNot')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('Left') is not None:
            temp_model = DescribeWhiteRuleListResponseBodyDataResponseDataExpressionConditionsLeft()
            self.left = temp_model.from_map(m['Left'])
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('Right') is not None:
            temp_model = DescribeWhiteRuleListResponseBodyDataResponseDataExpressionConditionsRight()
            self.right = temp_model.from_map(m['Right'])
        return self


class DescribeWhiteRuleListResponseBodyDataResponseDataExpression(TeaModel):
    def __init__(
        self,
        conditions: List[DescribeWhiteRuleListResponseBodyDataResponseDataExpressionConditions] = None,
        logic: str = None,
    ):
        self.conditions = conditions
        self.logic = logic

    def validate(self):
        if self.conditions:
            for k in self.conditions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Conditions'] = []
        if self.conditions is not None:
            for k in self.conditions:
                result['Conditions'].append(k.to_map() if k else None)
        if self.logic is not None:
            result['Logic'] = self.logic
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.conditions = []
        if m.get('Conditions') is not None:
            for k in m.get('Conditions'):
                temp_model = DescribeWhiteRuleListResponseBodyDataResponseDataExpressionConditions()
                self.conditions.append(temp_model.from_map(k))
        if m.get('Logic') is not None:
            self.logic = m.get('Logic')
        return self


class DescribeWhiteRuleListResponseBodyDataResponseData(TeaModel):
    def __init__(
        self,
        alert_name: str = None,
        alert_name_id: str = None,
        alert_type: str = None,
        alert_type_id: str = None,
        alert_uuid: str = None,
        aliuid: int = None,
        expression: DescribeWhiteRuleListResponseBodyDataResponseDataExpression = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        incident_uuid: str = None,
        status: int = None,
        sub_aliuid: int = None,
    ):
        self.alert_name = alert_name
        self.alert_name_id = alert_name_id
        self.alert_type = alert_type
        self.alert_type_id = alert_type_id
        self.alert_uuid = alert_uuid
        self.aliuid = aliuid
        self.expression = expression
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.incident_uuid = incident_uuid
        self.status = status
        self.sub_aliuid = sub_aliuid

    def validate(self):
        if self.expression:
            self.expression.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_name is not None:
            result['AlertName'] = self.alert_name
        if self.alert_name_id is not None:
            result['AlertNameId'] = self.alert_name_id
        if self.alert_type is not None:
            result['AlertType'] = self.alert_type
        if self.alert_type_id is not None:
            result['AlertTypeId'] = self.alert_type_id
        if self.alert_uuid is not None:
            result['AlertUuid'] = self.alert_uuid
        if self.aliuid is not None:
            result['Aliuid'] = self.aliuid
        if self.expression is not None:
            result['Expression'] = self.expression.to_map()
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        if self.incident_uuid is not None:
            result['IncidentUuid'] = self.incident_uuid
        if self.status is not None:
            result['Status'] = self.status
        if self.sub_aliuid is not None:
            result['SubAliuid'] = self.sub_aliuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertName') is not None:
            self.alert_name = m.get('AlertName')
        if m.get('AlertNameId') is not None:
            self.alert_name_id = m.get('AlertNameId')
        if m.get('AlertType') is not None:
            self.alert_type = m.get('AlertType')
        if m.get('AlertTypeId') is not None:
            self.alert_type_id = m.get('AlertTypeId')
        if m.get('AlertUuid') is not None:
            self.alert_uuid = m.get('AlertUuid')
        if m.get('Aliuid') is not None:
            self.aliuid = m.get('Aliuid')
        if m.get('Expression') is not None:
            temp_model = DescribeWhiteRuleListResponseBodyDataResponseDataExpression()
            self.expression = temp_model.from_map(m['Expression'])
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IncidentUuid') is not None:
            self.incident_uuid = m.get('IncidentUuid')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubAliuid') is not None:
            self.sub_aliuid = m.get('SubAliuid')
        return self


class DescribeWhiteRuleListResponseBodyData(TeaModel):
    def __init__(
        self,
        page_info: DescribeWhiteRuleListResponseBodyDataPageInfo = None,
        response_data: List[DescribeWhiteRuleListResponseBodyDataResponseData] = None,
    ):
        self.page_info = page_info
        self.response_data = response_data

    def validate(self):
        if self.page_info:
            self.page_info.validate()
        if self.response_data:
            for k in self.response_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()
        result['ResponseData'] = []
        if self.response_data is not None:
            for k in self.response_data:
                result['ResponseData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageInfo') is not None:
            temp_model = DescribeWhiteRuleListResponseBodyDataPageInfo()
            self.page_info = temp_model.from_map(m['PageInfo'])
        self.response_data = []
        if m.get('ResponseData') is not None:
            for k in m.get('ResponseData'):
                temp_model = DescribeWhiteRuleListResponseBodyDataResponseData()
                self.response_data.append(temp_model.from_map(k))
        return self


class DescribeWhiteRuleListResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: DescribeWhiteRuleListResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
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
            temp_model = DescribeWhiteRuleListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeWhiteRuleListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeWhiteRuleListResponseBody = None,
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
            temp_model = DescribeWhiteRuleListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DoQuickFieldRequest(TeaModel):
    def __init__(
        self,
        from_: int = None,
        index: str = None,
        page: int = None,
        region_id: str = None,
        reverse: bool = None,
        size: int = None,
        to: int = None,
    ):
        # The time when the quick analysis starts. This value is a UNIX timestamp representing the number of seconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.from_ = from_
        # The index field.
        self.index = index
        # The number of pages to return. Default value: 1.
        self.page = page
        # The region in which the data management center of the threat analysis feature resides. Specify this parameter based on the region where your assets reside. Valid values:
        # 
        # *   cn-hangzhou: Your assets reside in regions inside the Chinese mainland or in the China (Hong Kong) region.
        # *   ap-southeast-1: Your assets reside in regions outside the Chinese mainland, excluding the China (Hong Kong) region.
        self.region_id = region_id
        # The sorting of the query and analysis results. By default, the results are sorted in descending order.
        self.reverse = reverse
        # The number of entries per page. Default value: 10.
        self.size = size
        # The time when the quick analysis ends. This value is a UNIX timestamp representing the number of seconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.to = to

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.from_ is not None:
            result['From'] = self.from_
        if self.index is not None:
            result['Index'] = self.index
        if self.page is not None:
            result['Page'] = self.page
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.reverse is not None:
            result['Reverse'] = self.reverse
        if self.size is not None:
            result['Size'] = self.size
        if self.to is not None:
            result['To'] = self.to
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('From') is not None:
            self.from_ = m.get('From')
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Reverse') is not None:
            self.reverse = m.get('Reverse')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('To') is not None:
            self.to = m.get('To')
        return self


class DoQuickFieldResponseBodyData(TeaModel):
    def __init__(
        self,
        agg_queryd: str = None,
        complete_or_not: bool = None,
        count: int = None,
        has_sql: bool = None,
        keys: List[str] = None,
        limited: int = None,
        logs: List[Any] = None,
        pquery: str = None,
        processed_rows: int = None,
        query_mode: int = None,
        where_query: str = None,
    ):
        # This parameter is deprecated.
        self.agg_queryd = agg_queryd
        # Indicates whether the quick analysis was successful. Valid values:
        # 
        # *   true
        # *   false
        self.complete_or_not = complete_or_not
        # The number of entries returned.
        self.count = count
        # This parameter is deprecated.
        self.has_sql = has_sql
        # This parameter is deprecated.
        self.keys = keys
        # This parameter is deprecated.
        self.limited = limited
        # The logs queried by using the quick analysis feature.
        self.logs = logs
        # This parameter is deprecated.
        self.pquery = pquery
        # The number of entries queried.
        self.processed_rows = processed_rows
        # This parameter is deprecated.
        self.query_mode = query_mode
        # This parameter is deprecated.
        self.where_query = where_query

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agg_queryd is not None:
            result['AggQueryd'] = self.agg_queryd
        if self.complete_or_not is not None:
            result['CompleteOrNot'] = self.complete_or_not
        if self.count is not None:
            result['Count'] = self.count
        if self.has_sql is not None:
            result['HasSQL'] = self.has_sql
        if self.keys is not None:
            result['Keys'] = self.keys
        if self.limited is not None:
            result['Limited'] = self.limited
        if self.logs is not None:
            result['Logs'] = self.logs
        if self.pquery is not None:
            result['PQuery'] = self.pquery
        if self.processed_rows is not None:
            result['ProcessedRows'] = self.processed_rows
        if self.query_mode is not None:
            result['QueryMode'] = self.query_mode
        if self.where_query is not None:
            result['WhereQuery'] = self.where_query
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AggQueryd') is not None:
            self.agg_queryd = m.get('AggQueryd')
        if m.get('CompleteOrNot') is not None:
            self.complete_or_not = m.get('CompleteOrNot')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('HasSQL') is not None:
            self.has_sql = m.get('HasSQL')
        if m.get('Keys') is not None:
            self.keys = m.get('Keys')
        if m.get('Limited') is not None:
            self.limited = m.get('Limited')
        if m.get('Logs') is not None:
            self.logs = m.get('Logs')
        if m.get('PQuery') is not None:
            self.pquery = m.get('PQuery')
        if m.get('ProcessedRows') is not None:
            self.processed_rows = m.get('ProcessedRows')
        if m.get('QueryMode') is not None:
            self.query_mode = m.get('QueryMode')
        if m.get('WhereQuery') is not None:
            self.where_query = m.get('WhereQuery')
        return self


class DoQuickFieldResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: DoQuickFieldResponseBodyData = None,
        dy_code: str = None,
        dy_message: str = None,
        err_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code.
        self.code = code
        # The response of the quick analysis.
        self.data = data
        # The dynamic error code.
        self.dy_code = dy_code
        # The dynamic message.
        self.dy_message = dy_message
        # The error code.
        self.err_code = err_code
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
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
        if self.dy_code is not None:
            result['DyCode'] = self.dy_code
        if self.dy_message is not None:
            result['DyMessage'] = self.dy_message
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
            temp_model = DoQuickFieldResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('DyCode') is not None:
            self.dy_code = m.get('DyCode')
        if m.get('DyMessage') is not None:
            self.dy_message = m.get('DyMessage')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DoQuickFieldResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DoQuickFieldResponseBody = None,
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
            temp_model = DoQuickFieldResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DoSelfDelegateRequest(TeaModel):
    def __init__(
        self,
        ali_uid: int = None,
        delegate_or_not: int = None,
        region_id: str = None,
    ):
        # The Alibaba Cloud account of an ordinary member of the threat analysis feature.
        self.ali_uid = ali_uid
        # Specifies whether to use a delegated administrator account. Valid values:
        # 
        # *   1: use a delegated administrator account.
        # *   0: do not use a delegated administrator account.
        self.delegate_or_not = delegate_or_not
        # The region in which the data management center of the threat analysis feature resides. Specify this parameter based on the region where your assets reside. Valid values:
        # 
        # *   cn-hangzhou: Your assets reside in regions inside the Chinese mainland or in the China (Hong Kong) region.
        # *   ap-southeast-1: Your assets reside in regions outside the Chinese mainland, excluding the China (Hong Kong) region.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.delegate_or_not is not None:
            result['DelegateOrNot'] = self.delegate_or_not
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('DelegateOrNot') is not None:
            self.delegate_or_not = m.get('DelegateOrNot')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DoSelfDelegateResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: bool = None,
        dy_code: str = None,
        dy_message: str = None,
        err_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code.
        self.code = code
        # Indicates whether a regular member is authorized. Valid values:
        # 
        # *   true: The member is authorized.
        # *   false: The authorization is canceled.
        self.data = data
        # The dynamic error code.
        self.dy_code = dy_code
        # The dynamic message.
        self.dy_message = dy_message
        # The error code.
        self.err_code = err_code
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
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
        if self.dy_code is not None:
            result['DyCode'] = self.dy_code
        if self.dy_message is not None:
            result['DyMessage'] = self.dy_message
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
        if m.get('DyCode') is not None:
            self.dy_code = m.get('DyCode')
        if m.get('DyMessage') is not None:
            self.dy_message = m.get('DyMessage')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DoSelfDelegateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DoSelfDelegateResponseBody = None,
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
            temp_model = DoSelfDelegateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableAccessForCloudSiemRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
    ):
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class EnableAccessForCloudSiemResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
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


class EnableAccessForCloudSiemResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: EnableAccessForCloudSiemResponseBody = None,
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
            temp_model = EnableAccessForCloudSiemResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableServiceForCloudSiemRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
    ):
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class EnableServiceForCloudSiemResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
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


class EnableServiceForCloudSiemResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: EnableServiceForCloudSiemResponseBody = None,
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
            temp_model = EnableServiceForCloudSiemResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCapacityRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
    ):
        # The region in which the data management center of the threat analysis feature resides. Specify this parameter based on the region where your assets reside. Valid values:
        # 
        # *   cn-hangzhou: Your assets reside in regions inside the Chinese mainland or in the China (Hong Kong) region.
        # *   ap-southeast-1: Your assets reside in regions outside the Chinese mainland, excluding the China (Hong Kong) region.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetCapacityResponseBodyData(TeaModel):
    def __init__(
        self,
        exist_log_store: bool = None,
        preserved_capacity: int = None,
        used_capacity: float = None,
    ):
        # Indicates whether the Logstores for the threat analysis feature exist on the user side. Valid values:
        # 
        # *   true: The logs are in the normal state. The log analysis feature is available.
        # *   false: The logs are being cleared. The log analysis feature is unavailable.
        self.exist_log_store = exist_log_store
        # The purchased storage capacity of the threat analysis feature. Unit: GB.
        self.preserved_capacity = preserved_capacity
        # The billable storage capacity of the threat analysis feature. Unit: GB.
        self.used_capacity = used_capacity

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exist_log_store is not None:
            result['ExistLogStore'] = self.exist_log_store
        if self.preserved_capacity is not None:
            result['PreservedCapacity'] = self.preserved_capacity
        if self.used_capacity is not None:
            result['UsedCapacity'] = self.used_capacity
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExistLogStore') is not None:
            self.exist_log_store = m.get('ExistLogStore')
        if m.get('PreservedCapacity') is not None:
            self.preserved_capacity = m.get('PreservedCapacity')
        if m.get('UsedCapacity') is not None:
            self.used_capacity = m.get('UsedCapacity')
        return self


class GetCapacityResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: GetCapacityResponseBodyData = None,
        dy_code: str = None,
        dy_message: str = None,
        err_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code.
        self.code = code
        # The information about the storage capacity.
        self.data = data
        # The dynamic error code.
        self.dy_code = dy_code
        # The dynamic message.
        self.dy_message = dy_message
        # The error code.
        self.err_code = err_code
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
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
        if self.dy_code is not None:
            result['DyCode'] = self.dy_code
        if self.dy_message is not None:
            result['DyMessage'] = self.dy_message
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
            temp_model = GetCapacityResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('DyCode') is not None:
            self.dy_code = m.get('DyCode')
        if m.get('DyMessage') is not None:
            self.dy_message = m.get('DyMessage')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetCapacityResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetCapacityResponseBody = None,
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
            temp_model = GetCapacityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetHistogramsRequest(TeaModel):
    def __init__(
        self,
        from_: int = None,
        query: str = None,
        region_id: str = None,
        to: int = None,
    ):
        # The start time of the subinterval. The value is a UNIX timestamp representing the number of seconds that have elapsed since the epoch time January 1, 1970, 00:00:00 UTC. The time range that is specified in this operation is a left-closed, right-open interval. The interval includes the start time specified by the from parameter, but does not include the end time specified by the to parameter. If you specify the same value for the from and to parameters, the interval is invalid, and an error message is returned.
        self.from_ = from_
        # The SQL statement. Only search statements are supported. Analytic statements are not supported. For more information about the syntax and limits of search statements, see [Log search overview](https://help.aliyun.com/zh/sls/user-guide/search-syntax?spm=a2c4g.11186623.0.i2#concept-tnd-1jq-zdb).
        self.query = query
        # The region in which the data management center of the threat analysis feature resides. Specify this parameter based on the region where your assets reside. Valid values:
        # 
        # *   cn-hangzhou: Your assets reside in regions inside the Chinese mainland or in the China (Hong Kong) region.
        # *   ap-southeast-1: Your assets reside in regions outside the Chinese mainland, excluding the China (Hong Kong) region.
        self.region_id = region_id
        # The end time of the subinterval. The value is a UNIX timestamp representing the number of seconds that have elapsed since the epoch time January 1, 1970, 00:00:00 UTC. The time range that is specified in this operation is a left-closed, right-open interval. The interval includes the start time specified by the from parameter, but does not include the end time specified by the to parameter. If you specify the same value for the from and to parameters, the interval is invalid, and an error message is returned.
        self.to = to

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.from_ is not None:
            result['From'] = self.from_
        if self.query is not None:
            result['Query'] = self.query
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.to is not None:
            result['To'] = self.to
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('From') is not None:
            self.from_ = m.get('From')
        if m.get('Query') is not None:
            self.query = m.get('Query')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('To') is not None:
            self.to = m.get('To')
        return self


class GetHistogramsResponseBodyDataHistograms(TeaModel):
    def __init__(
        self,
        completed_or_not: bool = None,
        count: int = None,
        from_: int = None,
        to: int = None,
    ):
        # Indicates whether the query results within the subinterval is complete. Valid values:
        # 
        # *   true: The query is complete and the returned result is complete.
        # *   false: The query is complete but the returned result is incomplete. You must repeat the request to obtain the complete result.
        self.completed_or_not = completed_or_not
        # The number of logs within the subinterval.
        self.count = count
        # The start time of the subinterval. The value is a UNIX timestamp representing the number of seconds that have elapsed since the epoch time January 1, 1970, 00:00:00 UTC.
        self.from_ = from_
        # The end time of the subinterval. The value is a UNIX timestamp representing the number of seconds that have elapsed since the epoch time January 1, 1970, 00:00:00 UTC.
        self.to = to

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.completed_or_not is not None:
            result['CompletedOrNot'] = self.completed_or_not
        if self.count is not None:
            result['Count'] = self.count
        if self.from_ is not None:
            result['From'] = self.from_
        if self.to is not None:
            result['To'] = self.to
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompletedOrNot') is not None:
            self.completed_or_not = m.get('CompletedOrNot')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('From') is not None:
            self.from_ = m.get('From')
        if m.get('To') is not None:
            self.to = m.get('To')
        return self


class GetHistogramsResponseBodyData(TeaModel):
    def __init__(
        self,
        histograms: List[GetHistogramsResponseBodyDataHistograms] = None,
        server: str = None,
        total_count: int = None,
    ):
        # The distribution of logs.
        self.histograms = histograms
        # The name of the server.
        self.server = server
        # The number of logs that are generated within the subinterval.
        self.total_count = total_count

    def validate(self):
        if self.histograms:
            for k in self.histograms:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Histograms'] = []
        if self.histograms is not None:
            for k in self.histograms:
                result['Histograms'].append(k.to_map() if k else None)
        if self.server is not None:
            result['Server'] = self.server
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.histograms = []
        if m.get('Histograms') is not None:
            for k in m.get('Histograms'):
                temp_model = GetHistogramsResponseBodyDataHistograms()
                self.histograms.append(temp_model.from_map(k))
        if m.get('Server') is not None:
            self.server = m.get('Server')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class GetHistogramsResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: GetHistogramsResponseBodyData = None,
        dy_code: str = None,
        dy_message: str = None,
        err_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code.
        self.code = code
        # The data of the charts.
        self.data = data
        # The dynamic error code.
        self.dy_code = dy_code
        # The dynamic message.
        self.dy_message = dy_message
        # The error code.
        self.err_code = err_code
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
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
        if self.dy_code is not None:
            result['DyCode'] = self.dy_code
        if self.dy_message is not None:
            result['DyMessage'] = self.dy_message
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
            temp_model = GetHistogramsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('DyCode') is not None:
            self.dy_code = m.get('DyCode')
        if m.get('DyMessage') is not None:
            self.dy_message = m.get('DyMessage')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetHistogramsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetHistogramsResponseBody = None,
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
            temp_model = GetHistogramsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLogsRequest(TeaModel):
    def __init__(
        self,
        from_: int = None,
        page_index: int = None,
        page_size: int = None,
        query: str = None,
        region_id: str = None,
        reverse_or_not: bool = None,
        to: int = None,
        total: int = None,
    ):
        # The time when the query starts. The value is a UNIX timestamp representing the number of seconds that have elapsed since the epoch time January 1, 1970, 00:00:00 UTC.
        self.from_ = from_
        # The page number. Pages start from page 1.
        self.page_index = page_index
        # The number of entries per page. Valid values: 0 to 100.
        self.page_size = page_size
        # The search statement or the analytic statement. For more information, see [Log search overview](https://help.aliyun.com/zh/sls/user-guide/log-analysis-overview?spm=a2c4g.11186623.0.i1#t13103.html) and [Log analysis overview](https://help.aliyun.com/zh/sls/user-guide/search-syntax?spm=a2c4g.11186623.0.i0#concept-tnd-1jq-zdb).
        self.query = query
        # The region in which the data management center of the threat analysis feature resides. Specify this parameter based on the region where your assets reside. Valid values:
        # 
        # *   cn-hangzhou: Your assets reside in regions inside the Chinese mainland or in the China (Hong Kong) region.
        # *   ap-southeast-1: Your assets reside in regions outside the Chinese mainland, excluding the China (Hong Kong) region.
        self.region_id = region_id
        # Specifies whether to sort the results of the log query by time in minutes in descending order. Default value: true. Valid values:
        # 
        # *   true
        # *   false
        self.reverse_or_not = reverse_or_not
        # The time when the query ends. The value is a UNIX timestamp representing the number of seconds that have elapsed since the epoch time January 1, 1970, 00:00:00 UTC.
        self.to = to
        # The total number of entries returned.
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.from_ is not None:
            result['From'] = self.from_
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.query is not None:
            result['Query'] = self.query
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.reverse_or_not is not None:
            result['ReverseOrNot'] = self.reverse_or_not
        if self.to is not None:
            result['To'] = self.to
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('From') is not None:
            self.from_ = m.get('From')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Query') is not None:
            self.query = m.get('Query')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ReverseOrNot') is not None:
            self.reverse_or_not = m.get('ReverseOrNot')
        if m.get('To') is not None:
            self.to = m.get('To')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class GetLogsResponseBodyDataPageInfo(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The page number. Pages start from page 1.
        self.current_page = current_page
        # The number of entries per page.
        self.page_size = page_size
        # The total number of entries.
        self.total_count = total_count

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
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class GetLogsResponseBodyDataResponseData(TeaModel):
    def __init__(
        self,
        complete_or_not: bool = None,
        cost: int = None,
        count: int = None,
        has_sql: bool = None,
        keys: List[str] = None,
        lines: List[Any] = None,
    ):
        # The status of the log query. Valid values:
        # 
        # *   true: The query is complete and the returned result is complete.
        # *   false: The query is complete but the returned result is incomplete. You must resend the request to obtain the complete result.
        self.complete_or_not = complete_or_not
        # The time period of the log query. Unit: milliseconds.
        self.cost = cost
        # The number of entries returned.
        self.count = count
        # Indicated whether an analytic statement is contained. Valid values:
        # 
        # *   true
        # *   false
        self.has_sql = has_sql
        # The index fields of the logs.
        self.keys = keys
        # The raw data generated in the query.
        self.lines = lines

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.complete_or_not is not None:
            result['CompleteOrNot'] = self.complete_or_not
        if self.cost is not None:
            result['Cost'] = self.cost
        if self.count is not None:
            result['Count'] = self.count
        if self.has_sql is not None:
            result['HasSql'] = self.has_sql
        if self.keys is not None:
            result['Keys'] = self.keys
        if self.lines is not None:
            result['Lines'] = self.lines
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompleteOrNot') is not None:
            self.complete_or_not = m.get('CompleteOrNot')
        if m.get('Cost') is not None:
            self.cost = m.get('Cost')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('HasSql') is not None:
            self.has_sql = m.get('HasSql')
        if m.get('Keys') is not None:
            self.keys = m.get('Keys')
        if m.get('Lines') is not None:
            self.lines = m.get('Lines')
        return self


class GetLogsResponseBodyData(TeaModel):
    def __init__(
        self,
        page_info: GetLogsResponseBodyDataPageInfo = None,
        response_data: GetLogsResponseBodyDataResponseData = None,
    ):
        # The result on the current page.
        self.page_info = page_info
        # The log.
        self.response_data = response_data

    def validate(self):
        if self.page_info:
            self.page_info.validate()
        if self.response_data:
            self.response_data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()
        if self.response_data is not None:
            result['ResponseData'] = self.response_data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageInfo') is not None:
            temp_model = GetLogsResponseBodyDataPageInfo()
            self.page_info = temp_model.from_map(m['PageInfo'])
        if m.get('ResponseData') is not None:
            temp_model = GetLogsResponseBodyDataResponseData()
            self.response_data = temp_model.from_map(m['ResponseData'])
        return self


class GetLogsResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: GetLogsResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code.
        self.code = code
        # The results of the log query.
        self.data = data
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
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
            temp_model = GetLogsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetLogsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetLogsResponseBody = None,
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
            temp_model = GetLogsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetQuickQueryRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        search_name: str = None,
    ):
        # The data management center of the threat analysis feature. Specify this parameter based on the region where your assets reside. Valid values:
        # 
        # *   cn-hangzhou: Your assets reside in regions in the Chinese mainland or in the China (Hong Kong) region.
        # *   ap-southeast-1: Your assets reside in regions outside the Chinese mainland, excluding the China (Hong Kong) region.
        self.region_id = region_id
        # The name of the saved search.
        self.search_name = search_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.search_name is not None:
            result['SearchName'] = self.search_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SearchName') is not None:
            self.search_name = m.get('SearchName')
        return self


class GetQuickQueryResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: str = None,
        dy_code: str = None,
        dy_message: str = None,
        err_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code.
        self.code = code
        # The query statement.
        self.data = data
        # The dynamic error code.
        self.dy_code = dy_code
        # The dynamic message.
        self.dy_message = dy_message
        # The error code.
        self.err_code = err_code
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
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
        if self.dy_code is not None:
            result['DyCode'] = self.dy_code
        if self.dy_message is not None:
            result['DyMessage'] = self.dy_message
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
        if m.get('DyCode') is not None:
            self.dy_code = m.get('DyCode')
        if m.get('DyMessage') is not None:
            self.dy_message = m.get('DyMessage')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetQuickQueryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetQuickQueryResponseBody = None,
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
            temp_model = GetQuickQueryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetStorageRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
    ):
        # The region in which the data management center of the threat analysis feature resides. Specify this parameter based on the region where your assets reside. Valid values:
        # 
        # *   cn-hangzhou: Your assets reside in regions inside the Chinese mainland or in the China (Hong Kong) region.
        # *   ap-southeast-1: Your assets reside in regions outside the Chinese mainland, excluding the China (Hong Kong) region.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetStorageResponseBodyData(TeaModel):
    def __init__(
        self,
        can_operate: bool = None,
        display_region: bool = None,
        region: str = None,
        ttl: int = None,
    ):
        # Indicates whether the storage region can be changed for once. Default value: false Valid values:
        # 
        # *   true
        # *   false
        self.can_operate = can_operate
        # Indicates whether the storage region can be changed. Default value: false Valid values:
        # 
        # *   true
        # *   false
        self.display_region = display_region
        # The region in which the logs are stored. Default value: cn-shanghai. Valid values: cn-shanghai for the China site and ap-southeast-1 for the international site.
        self.region = region
        # The storage period of logs. Unit: day. Default value: 180. Valid values: 30 to 3000.
        self.ttl = ttl

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.can_operate is not None:
            result['CanOperate'] = self.can_operate
        if self.display_region is not None:
            result['DisplayRegion'] = self.display_region
        if self.region is not None:
            result['Region'] = self.region
        if self.ttl is not None:
            result['Ttl'] = self.ttl
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CanOperate') is not None:
            self.can_operate = m.get('CanOperate')
        if m.get('DisplayRegion') is not None:
            self.display_region = m.get('DisplayRegion')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Ttl') is not None:
            self.ttl = m.get('Ttl')
        return self


class GetStorageResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: GetStorageResponseBodyData = None,
        dy_code: str = None,
        dy_message: str = None,
        err_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code.
        self.code = code
        # The information about the storage.
        self.data = data
        # The dynamic error code.
        self.dy_code = dy_code
        # The dynamic message.
        self.dy_message = dy_message
        # The error code.
        self.err_code = err_code
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
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
        if self.dy_code is not None:
            result['DyCode'] = self.dy_code
        if self.dy_message is not None:
            result['DyMessage'] = self.dy_message
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
            temp_model = GetStorageResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('DyCode') is not None:
            self.dy_code = m.get('DyCode')
        if m.get('DyMessage') is not None:
            self.dy_message = m.get('DyMessage')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetStorageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetStorageResponseBody = None,
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
            temp_model = GetStorageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAccountAccessIdRequest(TeaModel):
    def __init__(
        self,
        cloud_code: str = None,
        region_id: str = None,
    ):
        self.cloud_code = cloud_code
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cloud_code is not None:
            result['CloudCode'] = self.cloud_code
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CloudCode') is not None:
            self.cloud_code = m.get('CloudCode')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListAccountAccessIdResponseBodyData(TeaModel):
    def __init__(
        self,
        access_id: str = None,
        access_id_md_5: str = None,
        account_id: str = None,
        account_str: str = None,
        bound: int = None,
        cloud_code: str = None,
        sub_user_id: int = None,
    ):
        self.access_id = access_id
        self.access_id_md_5 = access_id_md_5
        self.account_id = account_id
        self.account_str = account_str
        self.bound = bound
        self.cloud_code = cloud_code
        self.sub_user_id = sub_user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_id is not None:
            result['AccessId'] = self.access_id
        if self.access_id_md_5 is not None:
            result['AccessIdMd5'] = self.access_id_md_5
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.account_str is not None:
            result['AccountStr'] = self.account_str
        if self.bound is not None:
            result['Bound'] = self.bound
        if self.cloud_code is not None:
            result['CloudCode'] = self.cloud_code
        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessId') is not None:
            self.access_id = m.get('AccessId')
        if m.get('AccessIdMd5') is not None:
            self.access_id_md_5 = m.get('AccessIdMd5')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('AccountStr') is not None:
            self.account_str = m.get('AccountStr')
        if m.get('Bound') is not None:
            self.bound = m.get('Bound')
        if m.get('CloudCode') is not None:
            self.cloud_code = m.get('CloudCode')
        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')
        return self


class ListAccountAccessIdResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: List[ListAccountAccessIdResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
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
                temp_model = ListAccountAccessIdResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListAccountAccessIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAccountAccessIdResponseBody = None,
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
            temp_model = ListAccountAccessIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAccountsByLogRequest(TeaModel):
    def __init__(
        self,
        cloud_code: str = None,
        log_codes: List[str] = None,
        prod_code: str = None,
        region_id: str = None,
    ):
        self.cloud_code = cloud_code
        self.log_codes = log_codes
        self.prod_code = prod_code
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cloud_code is not None:
            result['CloudCode'] = self.cloud_code
        if self.log_codes is not None:
            result['LogCodes'] = self.log_codes
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CloudCode') is not None:
            self.cloud_code = m.get('CloudCode')
        if m.get('LogCodes') is not None:
            self.log_codes = m.get('LogCodes')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListAccountsByLogResponseBodyData(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        account_name: str = None,
        imported: int = None,
        log_code: str = None,
        main_user_id: int = None,
        prod_code: str = None,
        sub_user_id: int = None,
    ):
        self.account_id = account_id
        self.account_name = account_name
        self.imported = imported
        self.log_code = log_code
        self.main_user_id = main_user_id
        self.prod_code = prod_code
        self.sub_user_id = sub_user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.imported is not None:
            result['Imported'] = self.imported
        if self.log_code is not None:
            result['LogCode'] = self.log_code
        if self.main_user_id is not None:
            result['MainUserId'] = self.main_user_id
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('Imported') is not None:
            self.imported = m.get('Imported')
        if m.get('LogCode') is not None:
            self.log_code = m.get('LogCode')
        if m.get('MainUserId') is not None:
            self.main_user_id = m.get('MainUserId')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')
        return self


class ListAccountsByLogResponseBody(TeaModel):
    def __init__(
        self,
        data: List[ListAccountsByLogResponseBodyData] = None,
        request_id: str = None,
    ):
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
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListAccountsByLogResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListAccountsByLogResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAccountsByLogResponseBody = None,
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
            temp_model = ListAccountsByLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAllProdsRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
    ):
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListAllProdsResponseBodyDataProdList(TeaModel):
    def __init__(
        self,
        cloud_code: str = None,
        imported_log_count: int = None,
        modify_time: str = None,
        prod_code: str = None,
        total_log_count: int = None,
    ):
        self.cloud_code = cloud_code
        self.imported_log_count = imported_log_count
        self.modify_time = modify_time
        self.prod_code = prod_code
        self.total_log_count = total_log_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cloud_code is not None:
            result['CloudCode'] = self.cloud_code
        if self.imported_log_count is not None:
            result['ImportedLogCount'] = self.imported_log_count
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.total_log_count is not None:
            result['TotalLogCount'] = self.total_log_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CloudCode') is not None:
            self.cloud_code = m.get('CloudCode')
        if m.get('ImportedLogCount') is not None:
            self.imported_log_count = m.get('ImportedLogCount')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('TotalLogCount') is not None:
            self.total_log_count = m.get('TotalLogCount')
        return self


class ListAllProdsResponseBodyData(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        prod_list: List[ListAllProdsResponseBodyDataProdList] = None,
        total_count: int = None,
    ):
        self.current_page = current_page
        self.page_size = page_size
        self.prod_list = prod_list
        self.total_count = total_count

    def validate(self):
        if self.prod_list:
            for k in self.prod_list:
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
        result['ProdList'] = []
        if self.prod_list is not None:
            for k in self.prod_list:
                result['ProdList'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.prod_list = []
        if m.get('ProdList') is not None:
            for k in m.get('ProdList'):
                temp_model = ListAllProdsResponseBodyDataProdList()
                self.prod_list.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListAllProdsResponseBody(TeaModel):
    def __init__(
        self,
        data: ListAllProdsResponseBodyData = None,
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
            temp_model = ListAllProdsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListAllProdsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAllProdsResponseBody = None,
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
            temp_model = ListAllProdsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAutomateResponseConfigsRequest(TeaModel):
    def __init__(
        self,
        action_type: str = None,
        auto_response_type: str = None,
        current_page: int = None,
        id: int = None,
        page_size: int = None,
        playbook_uuid: str = None,
        region_id: str = None,
        rule_name: str = None,
        status: int = None,
        sub_user_id: int = None,
    ):
        self.action_type = action_type
        self.auto_response_type = auto_response_type
        self.current_page = current_page
        self.id = id
        self.page_size = page_size
        self.playbook_uuid = playbook_uuid
        self.region_id = region_id
        self.rule_name = rule_name
        self.status = status
        self.sub_user_id = sub_user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_type is not None:
            result['ActionType'] = self.action_type
        if self.auto_response_type is not None:
            result['AutoResponseType'] = self.auto_response_type
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.id is not None:
            result['Id'] = self.id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.playbook_uuid is not None:
            result['PlaybookUuid'] = self.playbook_uuid
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.status is not None:
            result['Status'] = self.status
        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionType') is not None:
            self.action_type = m.get('ActionType')
        if m.get('AutoResponseType') is not None:
            self.auto_response_type = m.get('AutoResponseType')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PlaybookUuid') is not None:
            self.playbook_uuid = m.get('PlaybookUuid')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')
        return self


class ListAutomateResponseConfigsResponseBodyDataPageInfo(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.current_page = current_page
        self.page_size = page_size
        self.total_count = total_count

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
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListAutomateResponseConfigsResponseBodyDataResponseData(TeaModel):
    def __init__(
        self,
        action_config: str = None,
        action_type: str = None,
        aliuid: int = None,
        auto_response_type: str = None,
        execution_condition: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        rule_name: str = None,
        status: int = None,
        sub_user_id: int = None,
    ):
        self.action_config = action_config
        self.action_type = action_type
        self.aliuid = aliuid
        self.auto_response_type = auto_response_type
        self.execution_condition = execution_condition
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.rule_name = rule_name
        self.status = status
        self.sub_user_id = sub_user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_config is not None:
            result['ActionConfig'] = self.action_config
        if self.action_type is not None:
            result['ActionType'] = self.action_type
        if self.aliuid is not None:
            result['Aliuid'] = self.aliuid
        if self.auto_response_type is not None:
            result['AutoResponseType'] = self.auto_response_type
        if self.execution_condition is not None:
            result['ExecutionCondition'] = self.execution_condition
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.status is not None:
            result['Status'] = self.status
        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionConfig') is not None:
            self.action_config = m.get('ActionConfig')
        if m.get('ActionType') is not None:
            self.action_type = m.get('ActionType')
        if m.get('Aliuid') is not None:
            self.aliuid = m.get('Aliuid')
        if m.get('AutoResponseType') is not None:
            self.auto_response_type = m.get('AutoResponseType')
        if m.get('ExecutionCondition') is not None:
            self.execution_condition = m.get('ExecutionCondition')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')
        return self


class ListAutomateResponseConfigsResponseBodyData(TeaModel):
    def __init__(
        self,
        page_info: ListAutomateResponseConfigsResponseBodyDataPageInfo = None,
        response_data: List[ListAutomateResponseConfigsResponseBodyDataResponseData] = None,
    ):
        self.page_info = page_info
        self.response_data = response_data

    def validate(self):
        if self.page_info:
            self.page_info.validate()
        if self.response_data:
            for k in self.response_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()
        result['ResponseData'] = []
        if self.response_data is not None:
            for k in self.response_data:
                result['ResponseData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageInfo') is not None:
            temp_model = ListAutomateResponseConfigsResponseBodyDataPageInfo()
            self.page_info = temp_model.from_map(m['PageInfo'])
        self.response_data = []
        if m.get('ResponseData') is not None:
            for k in m.get('ResponseData'):
                temp_model = ListAutomateResponseConfigsResponseBodyDataResponseData()
                self.response_data.append(temp_model.from_map(k))
        return self


class ListAutomateResponseConfigsResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: ListAutomateResponseConfigsResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
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
            temp_model = ListAutomateResponseConfigsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListAutomateResponseConfigsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAutomateResponseConfigsResponseBody = None,
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
            temp_model = ListAutomateResponseConfigsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListBindAccountRequest(TeaModel):
    def __init__(
        self,
        cloud_code: str = None,
        region_id: str = None,
    ):
        self.cloud_code = cloud_code
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cloud_code is not None:
            result['CloudCode'] = self.cloud_code
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CloudCode') is not None:
            self.cloud_code = m.get('CloudCode')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListBindAccountResponseBodyData(TeaModel):
    def __init__(
        self,
        access_id: str = None,
        account_id: str = None,
        account_name: str = None,
        bind_id: int = None,
        cloud_code: str = None,
        create_user: str = None,
        data_source_count: int = None,
        modify_time: str = None,
    ):
        self.access_id = access_id
        self.account_id = account_id
        self.account_name = account_name
        self.bind_id = bind_id
        self.cloud_code = cloud_code
        self.create_user = create_user
        self.data_source_count = data_source_count
        self.modify_time = modify_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_id is not None:
            result['AccessId'] = self.access_id
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.bind_id is not None:
            result['BindId'] = self.bind_id
        if self.cloud_code is not None:
            result['CloudCode'] = self.cloud_code
        if self.create_user is not None:
            result['CreateUser'] = self.create_user
        if self.data_source_count is not None:
            result['DataSourceCount'] = self.data_source_count
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessId') is not None:
            self.access_id = m.get('AccessId')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('BindId') is not None:
            self.bind_id = m.get('BindId')
        if m.get('CloudCode') is not None:
            self.cloud_code = m.get('CloudCode')
        if m.get('CreateUser') is not None:
            self.create_user = m.get('CreateUser')
        if m.get('DataSourceCount') is not None:
            self.data_source_count = m.get('DataSourceCount')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        return self


class ListBindAccountResponseBody(TeaModel):
    def __init__(
        self,
        data: List[ListBindAccountResponseBodyData] = None,
        request_id: str = None,
    ):
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
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListBindAccountResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListBindAccountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListBindAccountResponseBody = None,
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
            temp_model = ListBindAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListBindDataSourcesRequest(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        cloud_code: str = None,
        region_id: str = None,
    ):
        self.account_id = account_id
        self.cloud_code = cloud_code
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.cloud_code is not None:
            result['CloudCode'] = self.cloud_code
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('CloudCode') is not None:
            self.cloud_code = m.get('CloudCode')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListBindDataSourcesResponseBodyData(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        account_name: str = None,
        cloud_code: str = None,
        data_source_instance_id: str = None,
        data_source_name: str = None,
        data_source_remark: str = None,
        data_source_type: str = None,
        log_count: int = None,
        task_count: int = None,
    ):
        self.account_id = account_id
        self.account_name = account_name
        self.cloud_code = cloud_code
        self.data_source_instance_id = data_source_instance_id
        self.data_source_name = data_source_name
        self.data_source_remark = data_source_remark
        self.data_source_type = data_source_type
        self.log_count = log_count
        self.task_count = task_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.cloud_code is not None:
            result['CloudCode'] = self.cloud_code
        if self.data_source_instance_id is not None:
            result['DataSourceInstanceId'] = self.data_source_instance_id
        if self.data_source_name is not None:
            result['DataSourceName'] = self.data_source_name
        if self.data_source_remark is not None:
            result['DataSourceRemark'] = self.data_source_remark
        if self.data_source_type is not None:
            result['DataSourceType'] = self.data_source_type
        if self.log_count is not None:
            result['LogCount'] = self.log_count
        if self.task_count is not None:
            result['TaskCount'] = self.task_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('CloudCode') is not None:
            self.cloud_code = m.get('CloudCode')
        if m.get('DataSourceInstanceId') is not None:
            self.data_source_instance_id = m.get('DataSourceInstanceId')
        if m.get('DataSourceName') is not None:
            self.data_source_name = m.get('DataSourceName')
        if m.get('DataSourceRemark') is not None:
            self.data_source_remark = m.get('DataSourceRemark')
        if m.get('DataSourceType') is not None:
            self.data_source_type = m.get('DataSourceType')
        if m.get('LogCount') is not None:
            self.log_count = m.get('LogCount')
        if m.get('TaskCount') is not None:
            self.task_count = m.get('TaskCount')
        return self


class ListBindDataSourcesResponseBody(TeaModel):
    def __init__(
        self,
        data: List[ListBindDataSourcesResponseBodyData] = None,
        request_id: str = None,
    ):
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
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListBindDataSourcesResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListBindDataSourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListBindDataSourcesResponseBody = None,
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
            temp_model = ListBindDataSourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCloudSiemCustomizeRulesRequest(TeaModel):
    def __init__(
        self,
        alert_type: str = None,
        current_page: int = None,
        end_time: int = None,
        id: str = None,
        page_size: int = None,
        region_id: str = None,
        rule_name: str = None,
        rule_type: str = None,
        start_time: int = None,
        status: int = None,
        threat_level: List[str] = None,
    ):
        self.alert_type = alert_type
        self.current_page = current_page
        self.end_time = end_time
        self.id = id
        self.page_size = page_size
        self.region_id = region_id
        self.rule_name = rule_name
        self.rule_type = rule_type
        self.start_time = start_time
        self.status = status
        self.threat_level = threat_level

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_type is not None:
            result['AlertType'] = self.alert_type
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.id is not None:
            result['Id'] = self.id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.rule_type is not None:
            result['RuleType'] = self.rule_type
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.threat_level is not None:
            result['ThreatLevel'] = self.threat_level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertType') is not None:
            self.alert_type = m.get('AlertType')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ThreatLevel') is not None:
            self.threat_level = m.get('ThreatLevel')
        return self


class ListCloudSiemCustomizeRulesResponseBodyDataPageInfo(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.current_page = current_page
        self.page_size = page_size
        self.total_count = total_count

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
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListCloudSiemCustomizeRulesResponseBodyDataResponseData(TeaModel):
    def __init__(
        self,
        alert_type: str = None,
        alert_type_mds: str = None,
        aliuid: int = None,
        event_transfer_ext: str = None,
        event_transfer_switch: int = None,
        event_transfer_type: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        log_source: str = None,
        log_source_mds: str = None,
        log_type: str = None,
        log_type_mds: str = None,
        query_cycle: str = None,
        rule_condition: str = None,
        rule_desc: str = None,
        rule_group: str = None,
        rule_name: str = None,
        rule_threshold: str = None,
        rule_type: str = None,
        status: int = None,
        threat_level: str = None,
    ):
        self.alert_type = alert_type
        self.alert_type_mds = alert_type_mds
        self.aliuid = aliuid
        self.event_transfer_ext = event_transfer_ext
        self.event_transfer_switch = event_transfer_switch
        self.event_transfer_type = event_transfer_type
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.log_source = log_source
        self.log_source_mds = log_source_mds
        self.log_type = log_type
        self.log_type_mds = log_type_mds
        self.query_cycle = query_cycle
        self.rule_condition = rule_condition
        self.rule_desc = rule_desc
        self.rule_group = rule_group
        self.rule_name = rule_name
        self.rule_threshold = rule_threshold
        self.rule_type = rule_type
        self.status = status
        self.threat_level = threat_level

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_type is not None:
            result['AlertType'] = self.alert_type
        if self.alert_type_mds is not None:
            result['AlertTypeMds'] = self.alert_type_mds
        if self.aliuid is not None:
            result['Aliuid'] = self.aliuid
        if self.event_transfer_ext is not None:
            result['EventTransferExt'] = self.event_transfer_ext
        if self.event_transfer_switch is not None:
            result['EventTransferSwitch'] = self.event_transfer_switch
        if self.event_transfer_type is not None:
            result['EventTransferType'] = self.event_transfer_type
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        if self.log_source is not None:
            result['LogSource'] = self.log_source
        if self.log_source_mds is not None:
            result['LogSourceMds'] = self.log_source_mds
        if self.log_type is not None:
            result['LogType'] = self.log_type
        if self.log_type_mds is not None:
            result['LogTypeMds'] = self.log_type_mds
        if self.query_cycle is not None:
            result['QueryCycle'] = self.query_cycle
        if self.rule_condition is not None:
            result['RuleCondition'] = self.rule_condition
        if self.rule_desc is not None:
            result['RuleDesc'] = self.rule_desc
        if self.rule_group is not None:
            result['RuleGroup'] = self.rule_group
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.rule_threshold is not None:
            result['RuleThreshold'] = self.rule_threshold
        if self.rule_type is not None:
            result['RuleType'] = self.rule_type
        if self.status is not None:
            result['Status'] = self.status
        if self.threat_level is not None:
            result['ThreatLevel'] = self.threat_level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertType') is not None:
            self.alert_type = m.get('AlertType')
        if m.get('AlertTypeMds') is not None:
            self.alert_type_mds = m.get('AlertTypeMds')
        if m.get('Aliuid') is not None:
            self.aliuid = m.get('Aliuid')
        if m.get('EventTransferExt') is not None:
            self.event_transfer_ext = m.get('EventTransferExt')
        if m.get('EventTransferSwitch') is not None:
            self.event_transfer_switch = m.get('EventTransferSwitch')
        if m.get('EventTransferType') is not None:
            self.event_transfer_type = m.get('EventTransferType')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LogSource') is not None:
            self.log_source = m.get('LogSource')
        if m.get('LogSourceMds') is not None:
            self.log_source_mds = m.get('LogSourceMds')
        if m.get('LogType') is not None:
            self.log_type = m.get('LogType')
        if m.get('LogTypeMds') is not None:
            self.log_type_mds = m.get('LogTypeMds')
        if m.get('QueryCycle') is not None:
            self.query_cycle = m.get('QueryCycle')
        if m.get('RuleCondition') is not None:
            self.rule_condition = m.get('RuleCondition')
        if m.get('RuleDesc') is not None:
            self.rule_desc = m.get('RuleDesc')
        if m.get('RuleGroup') is not None:
            self.rule_group = m.get('RuleGroup')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('RuleThreshold') is not None:
            self.rule_threshold = m.get('RuleThreshold')
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ThreatLevel') is not None:
            self.threat_level = m.get('ThreatLevel')
        return self


class ListCloudSiemCustomizeRulesResponseBodyData(TeaModel):
    def __init__(
        self,
        page_info: ListCloudSiemCustomizeRulesResponseBodyDataPageInfo = None,
        response_data: List[ListCloudSiemCustomizeRulesResponseBodyDataResponseData] = None,
    ):
        self.page_info = page_info
        self.response_data = response_data

    def validate(self):
        if self.page_info:
            self.page_info.validate()
        if self.response_data:
            for k in self.response_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()
        result['ResponseData'] = []
        if self.response_data is not None:
            for k in self.response_data:
                result['ResponseData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageInfo') is not None:
            temp_model = ListCloudSiemCustomizeRulesResponseBodyDataPageInfo()
            self.page_info = temp_model.from_map(m['PageInfo'])
        self.response_data = []
        if m.get('ResponseData') is not None:
            for k in m.get('ResponseData'):
                temp_model = ListCloudSiemCustomizeRulesResponseBodyDataResponseData()
                self.response_data.append(temp_model.from_map(k))
        return self


class ListCloudSiemCustomizeRulesResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: ListCloudSiemCustomizeRulesResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
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
            temp_model = ListCloudSiemCustomizeRulesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListCloudSiemCustomizeRulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListCloudSiemCustomizeRulesResponseBody = None,
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
            temp_model = ListCloudSiemCustomizeRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCloudSiemPredefinedRulesRequest(TeaModel):
    def __init__(
        self,
        alert_type: str = None,
        current_page: int = None,
        end_time: int = None,
        id: str = None,
        page_size: int = None,
        region_id: str = None,
        rule_name: str = None,
        rule_type: str = None,
        start_time: int = None,
        status: int = None,
        threat_level: List[str] = None,
    ):
        self.alert_type = alert_type
        self.current_page = current_page
        self.end_time = end_time
        self.id = id
        self.page_size = page_size
        self.region_id = region_id
        self.rule_name = rule_name
        self.rule_type = rule_type
        self.start_time = start_time
        self.status = status
        self.threat_level = threat_level

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_type is not None:
            result['AlertType'] = self.alert_type
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.id is not None:
            result['Id'] = self.id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.rule_type is not None:
            result['RuleType'] = self.rule_type
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.threat_level is not None:
            result['ThreatLevel'] = self.threat_level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertType') is not None:
            self.alert_type = m.get('AlertType')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ThreatLevel') is not None:
            self.threat_level = m.get('ThreatLevel')
        return self


class ListCloudSiemPredefinedRulesResponseBodyDataPageInfo(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.current_page = current_page
        self.page_size = page_size
        self.total_count = total_count

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
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListCloudSiemPredefinedRulesResponseBodyDataResponseData(TeaModel):
    def __init__(
        self,
        alert_type: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        rule_desc_mds: str = None,
        rule_name: str = None,
        rule_name_mds: str = None,
        source: str = None,
        status: int = None,
        threat_level: str = None,
    ):
        self.alert_type = alert_type
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.rule_desc_mds = rule_desc_mds
        self.rule_name = rule_name
        self.rule_name_mds = rule_name_mds
        self.source = source
        self.status = status
        self.threat_level = threat_level

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_type is not None:
            result['AlertType'] = self.alert_type
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        if self.rule_desc_mds is not None:
            result['RuleDescMds'] = self.rule_desc_mds
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.rule_name_mds is not None:
            result['RuleNameMds'] = self.rule_name_mds
        if self.source is not None:
            result['Source'] = self.source
        if self.status is not None:
            result['Status'] = self.status
        if self.threat_level is not None:
            result['ThreatLevel'] = self.threat_level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertType') is not None:
            self.alert_type = m.get('AlertType')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RuleDescMds') is not None:
            self.rule_desc_mds = m.get('RuleDescMds')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('RuleNameMds') is not None:
            self.rule_name_mds = m.get('RuleNameMds')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ThreatLevel') is not None:
            self.threat_level = m.get('ThreatLevel')
        return self


class ListCloudSiemPredefinedRulesResponseBodyData(TeaModel):
    def __init__(
        self,
        page_info: ListCloudSiemPredefinedRulesResponseBodyDataPageInfo = None,
        response_data: List[ListCloudSiemPredefinedRulesResponseBodyDataResponseData] = None,
    ):
        self.page_info = page_info
        self.response_data = response_data

    def validate(self):
        if self.page_info:
            self.page_info.validate()
        if self.response_data:
            for k in self.response_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()
        result['ResponseData'] = []
        if self.response_data is not None:
            for k in self.response_data:
                result['ResponseData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageInfo') is not None:
            temp_model = ListCloudSiemPredefinedRulesResponseBodyDataPageInfo()
            self.page_info = temp_model.from_map(m['PageInfo'])
        self.response_data = []
        if m.get('ResponseData') is not None:
            for k in m.get('ResponseData'):
                temp_model = ListCloudSiemPredefinedRulesResponseBodyDataResponseData()
                self.response_data.append(temp_model.from_map(k))
        return self


class ListCloudSiemPredefinedRulesResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: ListCloudSiemPredefinedRulesResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
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
            temp_model = ListCloudSiemPredefinedRulesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListCloudSiemPredefinedRulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListCloudSiemPredefinedRulesResponseBody = None,
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
            temp_model = ListCloudSiemPredefinedRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCustomizeRuleTestResultRequest(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        id: int = None,
        page_size: int = None,
        region_id: str = None,
    ):
        self.current_page = current_page
        self.id = id
        self.page_size = page_size
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.id is not None:
            result['Id'] = self.id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListCustomizeRuleTestResultResponseBodyDataPageInfo(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.current_page = current_page
        self.page_size = page_size
        self.total_count = total_count

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
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListCustomizeRuleTestResultResponseBodyDataResponseData(TeaModel):
    def __init__(
        self,
        alert_desc: str = None,
        alert_detail: str = None,
        alert_src_prod: str = None,
        alert_src_prod_module: str = None,
        att_ck: str = None,
        event_name: str = None,
        event_type: str = None,
        level: str = None,
        log_source: str = None,
        log_time: str = None,
        log_type: str = None,
        main_user_id: str = None,
        online_status: str = None,
        sub_user_id: str = None,
        uuid: str = None,
    ):
        self.alert_desc = alert_desc
        self.alert_detail = alert_detail
        self.alert_src_prod = alert_src_prod
        self.alert_src_prod_module = alert_src_prod_module
        self.att_ck = att_ck
        self.event_name = event_name
        self.event_type = event_type
        self.level = level
        self.log_source = log_source
        self.log_time = log_time
        self.log_type = log_type
        self.main_user_id = main_user_id
        self.online_status = online_status
        self.sub_user_id = sub_user_id
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_desc is not None:
            result['AlertDesc'] = self.alert_desc
        if self.alert_detail is not None:
            result['AlertDetail'] = self.alert_detail
        if self.alert_src_prod is not None:
            result['AlertSrcProd'] = self.alert_src_prod
        if self.alert_src_prod_module is not None:
            result['AlertSrcProdModule'] = self.alert_src_prod_module
        if self.att_ck is not None:
            result['AttCk'] = self.att_ck
        if self.event_name is not None:
            result['EventName'] = self.event_name
        if self.event_type is not None:
            result['EventType'] = self.event_type
        if self.level is not None:
            result['Level'] = self.level
        if self.log_source is not None:
            result['LogSource'] = self.log_source
        if self.log_time is not None:
            result['LogTime'] = self.log_time
        if self.log_type is not None:
            result['LogType'] = self.log_type
        if self.main_user_id is not None:
            result['MainUserId'] = self.main_user_id
        if self.online_status is not None:
            result['OnlineStatus'] = self.online_status
        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertDesc') is not None:
            self.alert_desc = m.get('AlertDesc')
        if m.get('AlertDetail') is not None:
            self.alert_detail = m.get('AlertDetail')
        if m.get('AlertSrcProd') is not None:
            self.alert_src_prod = m.get('AlertSrcProd')
        if m.get('AlertSrcProdModule') is not None:
            self.alert_src_prod_module = m.get('AlertSrcProdModule')
        if m.get('AttCk') is not None:
            self.att_ck = m.get('AttCk')
        if m.get('EventName') is not None:
            self.event_name = m.get('EventName')
        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('LogSource') is not None:
            self.log_source = m.get('LogSource')
        if m.get('LogTime') is not None:
            self.log_time = m.get('LogTime')
        if m.get('LogType') is not None:
            self.log_type = m.get('LogType')
        if m.get('MainUserId') is not None:
            self.main_user_id = m.get('MainUserId')
        if m.get('OnlineStatus') is not None:
            self.online_status = m.get('OnlineStatus')
        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class ListCustomizeRuleTestResultResponseBodyData(TeaModel):
    def __init__(
        self,
        page_info: ListCustomizeRuleTestResultResponseBodyDataPageInfo = None,
        response_data: List[ListCustomizeRuleTestResultResponseBodyDataResponseData] = None,
    ):
        self.page_info = page_info
        self.response_data = response_data

    def validate(self):
        if self.page_info:
            self.page_info.validate()
        if self.response_data:
            for k in self.response_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()
        result['ResponseData'] = []
        if self.response_data is not None:
            for k in self.response_data:
                result['ResponseData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageInfo') is not None:
            temp_model = ListCustomizeRuleTestResultResponseBodyDataPageInfo()
            self.page_info = temp_model.from_map(m['PageInfo'])
        self.response_data = []
        if m.get('ResponseData') is not None:
            for k in m.get('ResponseData'):
                temp_model = ListCustomizeRuleTestResultResponseBodyDataResponseData()
                self.response_data.append(temp_model.from_map(k))
        return self


class ListCustomizeRuleTestResultResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: ListCustomizeRuleTestResultResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
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
            temp_model = ListCustomizeRuleTestResultResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListCustomizeRuleTestResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListCustomizeRuleTestResultResponseBody = None,
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
            temp_model = ListCustomizeRuleTestResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDataSourceLogsRequest(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        cloud_code: str = None,
        data_source_instance_id: str = None,
        region_id: str = None,
    ):
        self.account_id = account_id
        self.cloud_code = cloud_code
        self.data_source_instance_id = data_source_instance_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.cloud_code is not None:
            result['CloudCode'] = self.cloud_code
        if self.data_source_instance_id is not None:
            result['DataSourceInstanceId'] = self.data_source_instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('CloudCode') is not None:
            self.cloud_code = m.get('CloudCode')
        if m.get('DataSourceInstanceId') is not None:
            self.data_source_instance_id = m.get('DataSourceInstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListDataSourceLogsResponseBodyDataDataSourceInstanceLogsLogParams(TeaModel):
    def __init__(
        self,
        para_code: str = None,
        para_value: str = None,
    ):
        self.para_code = para_code
        self.para_value = para_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.para_code is not None:
            result['ParaCode'] = self.para_code
        if self.para_value is not None:
            result['ParaValue'] = self.para_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParaCode') is not None:
            self.para_code = m.get('ParaCode')
        if m.get('ParaValue') is not None:
            self.para_value = m.get('ParaValue')
        return self


class ListDataSourceLogsResponseBodyDataDataSourceInstanceLogs(TeaModel):
    def __init__(
        self,
        log_code: str = None,
        log_instance_id: str = None,
        log_mds_code: str = None,
        log_params: List[ListDataSourceLogsResponseBodyDataDataSourceInstanceLogsLogParams] = None,
        task_status: int = None,
    ):
        self.log_code = log_code
        self.log_instance_id = log_instance_id
        self.log_mds_code = log_mds_code
        self.log_params = log_params
        self.task_status = task_status

    def validate(self):
        if self.log_params:
            for k in self.log_params:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.log_code is not None:
            result['LogCode'] = self.log_code
        if self.log_instance_id is not None:
            result['LogInstanceId'] = self.log_instance_id
        if self.log_mds_code is not None:
            result['LogMdsCode'] = self.log_mds_code
        result['LogParams'] = []
        if self.log_params is not None:
            for k in self.log_params:
                result['LogParams'].append(k.to_map() if k else None)
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LogCode') is not None:
            self.log_code = m.get('LogCode')
        if m.get('LogInstanceId') is not None:
            self.log_instance_id = m.get('LogInstanceId')
        if m.get('LogMdsCode') is not None:
            self.log_mds_code = m.get('LogMdsCode')
        self.log_params = []
        if m.get('LogParams') is not None:
            for k in m.get('LogParams'):
                temp_model = ListDataSourceLogsResponseBodyDataDataSourceInstanceLogsLogParams()
                self.log_params.append(temp_model.from_map(k))
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        return self


class ListDataSourceLogsResponseBodyData(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        cloud_code: str = None,
        data_source_instance_id: str = None,
        data_source_instance_logs: List[ListDataSourceLogsResponseBodyDataDataSourceInstanceLogs] = None,
        data_source_instance_name: str = None,
        data_source_instance_remark: str = None,
        sub_user_id: int = None,
    ):
        self.account_id = account_id
        self.cloud_code = cloud_code
        self.data_source_instance_id = data_source_instance_id
        self.data_source_instance_logs = data_source_instance_logs
        self.data_source_instance_name = data_source_instance_name
        self.data_source_instance_remark = data_source_instance_remark
        self.sub_user_id = sub_user_id

    def validate(self):
        if self.data_source_instance_logs:
            for k in self.data_source_instance_logs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.cloud_code is not None:
            result['CloudCode'] = self.cloud_code
        if self.data_source_instance_id is not None:
            result['DataSourceInstanceId'] = self.data_source_instance_id
        result['DataSourceInstanceLogs'] = []
        if self.data_source_instance_logs is not None:
            for k in self.data_source_instance_logs:
                result['DataSourceInstanceLogs'].append(k.to_map() if k else None)
        if self.data_source_instance_name is not None:
            result['DataSourceInstanceName'] = self.data_source_instance_name
        if self.data_source_instance_remark is not None:
            result['DataSourceInstanceRemark'] = self.data_source_instance_remark
        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('CloudCode') is not None:
            self.cloud_code = m.get('CloudCode')
        if m.get('DataSourceInstanceId') is not None:
            self.data_source_instance_id = m.get('DataSourceInstanceId')
        self.data_source_instance_logs = []
        if m.get('DataSourceInstanceLogs') is not None:
            for k in m.get('DataSourceInstanceLogs'):
                temp_model = ListDataSourceLogsResponseBodyDataDataSourceInstanceLogs()
                self.data_source_instance_logs.append(temp_model.from_map(k))
        if m.get('DataSourceInstanceName') is not None:
            self.data_source_instance_name = m.get('DataSourceInstanceName')
        if m.get('DataSourceInstanceRemark') is not None:
            self.data_source_instance_remark = m.get('DataSourceInstanceRemark')
        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')
        return self


class ListDataSourceLogsResponseBody(TeaModel):
    def __init__(
        self,
        data: ListDataSourceLogsResponseBodyData = None,
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
            temp_model = ListDataSourceLogsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListDataSourceLogsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDataSourceLogsResponseBody = None,
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
            temp_model = ListDataSourceLogsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDataSourceTypesRequest(TeaModel):
    def __init__(
        self,
        cloud_code: str = None,
        region_id: str = None,
    ):
        self.cloud_code = cloud_code
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cloud_code is not None:
            result['CloudCode'] = self.cloud_code
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CloudCode') is not None:
            self.cloud_code = m.get('CloudCode')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListDataSourceTypesResponseBodyData(TeaModel):
    def __init__(
        self,
        cloud_code: str = None,
        data_source_type: str = None,
    ):
        self.cloud_code = cloud_code
        self.data_source_type = data_source_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cloud_code is not None:
            result['CloudCode'] = self.cloud_code
        if self.data_source_type is not None:
            result['DataSourceType'] = self.data_source_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CloudCode') is not None:
            self.cloud_code = m.get('CloudCode')
        if m.get('DataSourceType') is not None:
            self.data_source_type = m.get('DataSourceType')
        return self


class ListDataSourceTypesResponseBody(TeaModel):
    def __init__(
        self,
        data: List[ListDataSourceTypesResponseBodyData] = None,
        request_id: str = None,
    ):
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
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListDataSourceTypesResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListDataSourceTypesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDataSourceTypesResponseBody = None,
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
            temp_model = ListDataSourceTypesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDeliveryRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
    ):
        # The region in which the data management center of the threat analysis feature resides. Specify this parameter based on the region where your assets reside. Valid values:
        # 
        # *   cn-hangzhou: Your assets reside in regions inside the Chinese mainland or in the China (Hong Kong) region.
        # *   ap-southeast-1: Your assets reside in regions outside the Chinese mainland, excluding the China (Hong Kong) region.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListDeliveryResponseBodyDataProductListLogListExtraParameters(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The ID of the extended parameter.
        self.key = key
        # The value of the extended parameter.
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


class ListDeliveryResponseBodyDataProductListLogList(TeaModel):
    def __init__(
        self,
        can_operate_or_not: bool = None,
        extra_parameters: List[ListDeliveryResponseBodyDataProductListLogListExtraParameters] = None,
        log_code: str = None,
        log_name: str = None,
        log_name_en: str = None,
        log_name_key: str = None,
        status: bool = None,
        topic: str = None,
    ):
        # Indicates whether the log delivery feature can be enabled or disabled. The feature can be enabled or disabled only by the administrator of the threat analysis feature. Valid values:
        # 
        # *   true
        # *   false
        self.can_operate_or_not = can_operate_or_not
        # The extended parameter.
        self.extra_parameters = extra_parameters
        # The code of the log.
        self.log_code = log_code
        # This parameter is deprecated.
        self.log_name = log_name
        # This parameter is deprecated.
        self.log_name_en = log_name_en
        # The language code of the log that is used to indicate the language in which the log is displayed.
        self.log_name_key = log_name_key
        # The status of the log delivery. Valid values:
        # 
        # *   true: The logs are being delivered.
        # *   false: The log delivery feature is disabled.
        self.status = status
        # The topic of the log in the Logstore. The value is an index field in the Logstore that can be used to distinguish different logs.
        self.topic = topic

    def validate(self):
        if self.extra_parameters:
            for k in self.extra_parameters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.can_operate_or_not is not None:
            result['CanOperateOrNot'] = self.can_operate_or_not
        result['ExtraParameters'] = []
        if self.extra_parameters is not None:
            for k in self.extra_parameters:
                result['ExtraParameters'].append(k.to_map() if k else None)
        if self.log_code is not None:
            result['LogCode'] = self.log_code
        if self.log_name is not None:
            result['LogName'] = self.log_name
        if self.log_name_en is not None:
            result['LogNameEn'] = self.log_name_en
        if self.log_name_key is not None:
            result['LogNameKey'] = self.log_name_key
        if self.status is not None:
            result['Status'] = self.status
        if self.topic is not None:
            result['Topic'] = self.topic
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CanOperateOrNot') is not None:
            self.can_operate_or_not = m.get('CanOperateOrNot')
        self.extra_parameters = []
        if m.get('ExtraParameters') is not None:
            for k in m.get('ExtraParameters'):
                temp_model = ListDeliveryResponseBodyDataProductListLogListExtraParameters()
                self.extra_parameters.append(temp_model.from_map(k))
        if m.get('LogCode') is not None:
            self.log_code = m.get('LogCode')
        if m.get('LogName') is not None:
            self.log_name = m.get('LogName')
        if m.get('LogNameEn') is not None:
            self.log_name_en = m.get('LogNameEn')
        if m.get('LogNameKey') is not None:
            self.log_name_key = m.get('LogNameKey')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        return self


class ListDeliveryResponseBodyDataProductList(TeaModel):
    def __init__(
        self,
        log_list: List[ListDeliveryResponseBodyDataProductListLogList] = None,
        log_map: Dict[str, List[DataProductListLogMapValue]] = None,
        product_code: str = None,
        product_name: str = None,
    ):
        # The logs of the cloud services.
        self.log_list = log_list
        # The log group. For example, in Security Center, the logs of hosts and networks are stored in different groups. Key indicates the group information, and value indicates the logs in the group.
        self.log_map = log_map
        # The code of the cloud service. Valid values:
        # 
        # *   qcloud_waf
        # *   qlcoud_cfw
        # *   hcloud_waf
        # *   hcloud_cfw
        # *   ddos
        # *   sas
        # *   cfw
        # *   config
        # *   csk
        # *   fc
        # *   rds
        # *   nas
        # *   apigateway
        # *   cdn
        # *   mongodb
        # *   eip
        # *   slb
        # *   vpc
        # *   actiontrail
        # *   waf
        # *   bastionhost
        # *   oss
        # *   polardb
        self.product_code = product_code
        # This parameter is deprecated.
        self.product_name = product_name

    def validate(self):
        if self.log_list:
            for k in self.log_list:
                if k:
                    k.validate()
        if self.log_map:
            for v in self.log_map.values():
                for k1 in v:
                    if k1:
                        k1.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['LogList'] = []
        if self.log_list is not None:
            for k in self.log_list:
                result['LogList'].append(k.to_map() if k else None)
        result['LogMap'] = {}
        if self.log_map is not None:
            for k, v in self.log_map.items():
                l1 = []
                for k1 in v:
                    l1.append(k1.to_map() if k1 else None)
                result['logMap'][k] = l1
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.product_name is not None:
            result['ProductName'] = self.product_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.log_list = []
        if m.get('LogList') is not None:
            for k in m.get('LogList'):
                temp_model = ListDeliveryResponseBodyDataProductListLogList()
                self.log_list.append(temp_model.from_map(k))
        self.log_map = {}
        if m.get('LogMap') is not None:
            for k, v in m.get('LogMap').items():
                l1 = []
                for k1 in v:
                    temp_model = DataProductListLogMapValue()
                    l1.append(temp_model.from_map(k1))
                self.log_map['k'] = l1
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')
        return self


class ListDeliveryResponseBodyData(TeaModel):
    def __init__(
        self,
        dashboard_url: str = None,
        display_switch_or_not: bool = None,
        log_store_name: str = None,
        product_list: List[ListDeliveryResponseBodyDataProductList] = None,
        project_name: str = None,
        search_url: str = None,
    ):
        # The URL that is displayed in charts.
        self.dashboard_url = dashboard_url
        # Indicates whether the log delivery switch is displayed. Default value: true. Valid values:
        # 
        # *   true
        # *   false
        self.display_switch_or_not = display_switch_or_not
        # The name of the Logstore for the threat analysis feature on the user side. The value is in the cloud_siem format.
        self.log_store_name = log_store_name
        # The cloud services.
        self.product_list = product_list
        # The name of the project for the threat analysis feature in Simple Log service on the user side. The value is in the aliyun-cloudsiem-data-${aliUid}-${region} format.
        self.project_name = project_name
        # The URL that is used for log analysis.
        self.search_url = search_url

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
        if self.dashboard_url is not None:
            result['DashboardUrl'] = self.dashboard_url
        if self.display_switch_or_not is not None:
            result['DisplaySwitchOrNot'] = self.display_switch_or_not
        if self.log_store_name is not None:
            result['LogStoreName'] = self.log_store_name
        result['ProductList'] = []
        if self.product_list is not None:
            for k in self.product_list:
                result['ProductList'].append(k.to_map() if k else None)
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.search_url is not None:
            result['SearchUrl'] = self.search_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DashboardUrl') is not None:
            self.dashboard_url = m.get('DashboardUrl')
        if m.get('DisplaySwitchOrNot') is not None:
            self.display_switch_or_not = m.get('DisplaySwitchOrNot')
        if m.get('LogStoreName') is not None:
            self.log_store_name = m.get('LogStoreName')
        self.product_list = []
        if m.get('ProductList') is not None:
            for k in m.get('ProductList'):
                temp_model = ListDeliveryResponseBodyDataProductList()
                self.product_list.append(temp_model.from_map(k))
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('SearchUrl') is not None:
            self.search_url = m.get('SearchUrl')
        return self


class ListDeliveryResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: ListDeliveryResponseBodyData = None,
        dy_code: str = None,
        dy_message: str = None,
        err_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code.
        # 
        # Valid values:
        # 
        # *   200
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   500
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.code = code
        # The response parameters.
        self.data = data
        # The dynamic error code.
        self.dy_code = dy_code
        # The dynamic error message.
        self.dy_message = dy_message
        # The error code.
        self.err_code = err_code
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        # 
        # Valid values:
        # 
        # *   True
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   False
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
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
        if self.dy_code is not None:
            result['DyCode'] = self.dy_code
        if self.dy_message is not None:
            result['DyMessage'] = self.dy_message
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
            temp_model = ListDeliveryResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('DyCode') is not None:
            self.dy_code = m.get('DyCode')
        if m.get('DyMessage') is not None:
            self.dy_message = m.get('DyMessage')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListDeliveryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDeliveryResponseBody = None,
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
            temp_model = ListDeliveryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDisposeStrategyRequest(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        effective_status: int = None,
        end_time: int = None,
        entity_identity: str = None,
        entity_type: str = None,
        order: str = None,
        order_field: str = None,
        page_size: int = None,
        playbook_name: str = None,
        playbook_types: str = None,
        playbook_uuid: str = None,
        region_id: str = None,
        sophon_task_id: str = None,
        start_time: int = None,
    ):
        self.current_page = current_page
        self.effective_status = effective_status
        self.end_time = end_time
        self.entity_identity = entity_identity
        self.entity_type = entity_type
        self.order = order
        self.order_field = order_field
        self.page_size = page_size
        self.playbook_name = playbook_name
        self.playbook_types = playbook_types
        self.playbook_uuid = playbook_uuid
        self.region_id = region_id
        self.sophon_task_id = sophon_task_id
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.effective_status is not None:
            result['EffectiveStatus'] = self.effective_status
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.entity_identity is not None:
            result['EntityIdentity'] = self.entity_identity
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.order is not None:
            result['Order'] = self.order
        if self.order_field is not None:
            result['OrderField'] = self.order_field
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.playbook_name is not None:
            result['PlaybookName'] = self.playbook_name
        if self.playbook_types is not None:
            result['PlaybookTypes'] = self.playbook_types
        if self.playbook_uuid is not None:
            result['PlaybookUuid'] = self.playbook_uuid
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.sophon_task_id is not None:
            result['SophonTaskId'] = self.sophon_task_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('EffectiveStatus') is not None:
            self.effective_status = m.get('EffectiveStatus')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('EntityIdentity') is not None:
            self.entity_identity = m.get('EntityIdentity')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('OrderField') is not None:
            self.order_field = m.get('OrderField')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PlaybookName') is not None:
            self.playbook_name = m.get('PlaybookName')
        if m.get('PlaybookTypes') is not None:
            self.playbook_types = m.get('PlaybookTypes')
        if m.get('PlaybookUuid') is not None:
            self.playbook_uuid = m.get('PlaybookUuid')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SophonTaskId') is not None:
            self.sophon_task_id = m.get('SophonTaskId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class ListDisposeStrategyResponseBodyDataPageInfo(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.current_page = current_page
        self.page_size = page_size
        self.total_count = total_count

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
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListDisposeStrategyResponseBodyDataResponseData(TeaModel):
    def __init__(
        self,
        alert_uuid: str = None,
        aliuid: int = None,
        effective_status: int = None,
        entity: List[Any] = None,
        entity_id: int = None,
        entity_type: str = None,
        error_message: str = None,
        finish_time: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        incident_name: str = None,
        incident_uuid: str = None,
        playbook_name: str = None,
        playbook_type: str = None,
        playbook_uuid: str = None,
        scope: List[Any] = None,
        sophon_task_id: str = None,
        status: int = None,
        sub_aliuid: int = None,
        task_param: str = None,
    ):
        self.alert_uuid = alert_uuid
        self.aliuid = aliuid
        self.effective_status = effective_status
        self.entity = entity
        self.entity_id = entity_id
        self.entity_type = entity_type
        self.error_message = error_message
        self.finish_time = finish_time
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.incident_name = incident_name
        self.incident_uuid = incident_uuid
        self.playbook_name = playbook_name
        self.playbook_type = playbook_type
        self.playbook_uuid = playbook_uuid
        self.scope = scope
        self.sophon_task_id = sophon_task_id
        self.status = status
        self.sub_aliuid = sub_aliuid
        self.task_param = task_param

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_uuid is not None:
            result['AlertUuid'] = self.alert_uuid
        if self.aliuid is not None:
            result['Aliuid'] = self.aliuid
        if self.effective_status is not None:
            result['EffectiveStatus'] = self.effective_status
        if self.entity is not None:
            result['Entity'] = self.entity
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        if self.incident_name is not None:
            result['IncidentName'] = self.incident_name
        if self.incident_uuid is not None:
            result['IncidentUuid'] = self.incident_uuid
        if self.playbook_name is not None:
            result['PlaybookName'] = self.playbook_name
        if self.playbook_type is not None:
            result['PlaybookType'] = self.playbook_type
        if self.playbook_uuid is not None:
            result['PlaybookUuid'] = self.playbook_uuid
        if self.scope is not None:
            result['Scope'] = self.scope
        if self.sophon_task_id is not None:
            result['SophonTaskId'] = self.sophon_task_id
        if self.status is not None:
            result['Status'] = self.status
        if self.sub_aliuid is not None:
            result['SubAliuid'] = self.sub_aliuid
        if self.task_param is not None:
            result['TaskParam'] = self.task_param
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertUuid') is not None:
            self.alert_uuid = m.get('AlertUuid')
        if m.get('Aliuid') is not None:
            self.aliuid = m.get('Aliuid')
        if m.get('EffectiveStatus') is not None:
            self.effective_status = m.get('EffectiveStatus')
        if m.get('Entity') is not None:
            self.entity = m.get('Entity')
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IncidentName') is not None:
            self.incident_name = m.get('IncidentName')
        if m.get('IncidentUuid') is not None:
            self.incident_uuid = m.get('IncidentUuid')
        if m.get('PlaybookName') is not None:
            self.playbook_name = m.get('PlaybookName')
        if m.get('PlaybookType') is not None:
            self.playbook_type = m.get('PlaybookType')
        if m.get('PlaybookUuid') is not None:
            self.playbook_uuid = m.get('PlaybookUuid')
        if m.get('Scope') is not None:
            self.scope = m.get('Scope')
        if m.get('SophonTaskId') is not None:
            self.sophon_task_id = m.get('SophonTaskId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubAliuid') is not None:
            self.sub_aliuid = m.get('SubAliuid')
        if m.get('TaskParam') is not None:
            self.task_param = m.get('TaskParam')
        return self


class ListDisposeStrategyResponseBodyData(TeaModel):
    def __init__(
        self,
        page_info: ListDisposeStrategyResponseBodyDataPageInfo = None,
        response_data: List[ListDisposeStrategyResponseBodyDataResponseData] = None,
    ):
        self.page_info = page_info
        self.response_data = response_data

    def validate(self):
        if self.page_info:
            self.page_info.validate()
        if self.response_data:
            for k in self.response_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()
        result['ResponseData'] = []
        if self.response_data is not None:
            for k in self.response_data:
                result['ResponseData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageInfo') is not None:
            temp_model = ListDisposeStrategyResponseBodyDataPageInfo()
            self.page_info = temp_model.from_map(m['PageInfo'])
        self.response_data = []
        if m.get('ResponseData') is not None:
            for k in m.get('ResponseData'):
                temp_model = ListDisposeStrategyResponseBodyDataResponseData()
                self.response_data.append(temp_model.from_map(k))
        return self


class ListDisposeStrategyResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: ListDisposeStrategyResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
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
            temp_model = ListDisposeStrategyResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListDisposeStrategyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDisposeStrategyResponseBody = None,
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
            temp_model = ListDisposeStrategyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListImportedLogsByProdRequest(TeaModel):
    def __init__(
        self,
        cloud_code: str = None,
        prod_code: str = None,
        region_id: str = None,
    ):
        self.cloud_code = cloud_code
        self.prod_code = prod_code
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cloud_code is not None:
            result['CloudCode'] = self.cloud_code
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CloudCode') is not None:
            self.cloud_code = m.get('CloudCode')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListImportedLogsByProdResponseBodyData(TeaModel):
    def __init__(
        self,
        auto_imported: int = None,
        cloud_code: str = None,
        imported: int = None,
        imported_user_count: int = None,
        log_code: str = None,
        log_mds_code: str = None,
        modify_time: str = None,
        prod_code: str = None,
        total_user_count: int = None,
        un_imported_user_count: int = None,
    ):
        self.auto_imported = auto_imported
        self.cloud_code = cloud_code
        self.imported = imported
        self.imported_user_count = imported_user_count
        self.log_code = log_code
        self.log_mds_code = log_mds_code
        self.modify_time = modify_time
        self.prod_code = prod_code
        self.total_user_count = total_user_count
        self.un_imported_user_count = un_imported_user_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_imported is not None:
            result['AutoImported'] = self.auto_imported
        if self.cloud_code is not None:
            result['CloudCode'] = self.cloud_code
        if self.imported is not None:
            result['Imported'] = self.imported
        if self.imported_user_count is not None:
            result['ImportedUserCount'] = self.imported_user_count
        if self.log_code is not None:
            result['LogCode'] = self.log_code
        if self.log_mds_code is not None:
            result['LogMdsCode'] = self.log_mds_code
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.total_user_count is not None:
            result['TotalUserCount'] = self.total_user_count
        if self.un_imported_user_count is not None:
            result['UnImportedUserCount'] = self.un_imported_user_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoImported') is not None:
            self.auto_imported = m.get('AutoImported')
        if m.get('CloudCode') is not None:
            self.cloud_code = m.get('CloudCode')
        if m.get('Imported') is not None:
            self.imported = m.get('Imported')
        if m.get('ImportedUserCount') is not None:
            self.imported_user_count = m.get('ImportedUserCount')
        if m.get('LogCode') is not None:
            self.log_code = m.get('LogCode')
        if m.get('LogMdsCode') is not None:
            self.log_mds_code = m.get('LogMdsCode')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('TotalUserCount') is not None:
            self.total_user_count = m.get('TotalUserCount')
        if m.get('UnImportedUserCount') is not None:
            self.un_imported_user_count = m.get('UnImportedUserCount')
        return self


class ListImportedLogsByProdResponseBody(TeaModel):
    def __init__(
        self,
        data: List[ListImportedLogsByProdResponseBodyData] = None,
        request_id: str = None,
    ):
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
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListImportedLogsByProdResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListImportedLogsByProdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListImportedLogsByProdResponseBody = None,
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
            temp_model = ListImportedLogsByProdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListOperationRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
    ):
        # The data management center of the threat analysis feature. Specify this parameter based on the region where your assets reside. Valid values:
        # 
        # *   cn-hangzhou: Your assets reside in regions in the Chinese mainland or in the China (Hong Kong) region.
        # *   ap-southeast-1: Your assets reside in regions outside the Chinese mainland, excluding the China (Hong Kong) region.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListOperationResponseBodyData(TeaModel):
    def __init__(
        self,
        admin_or_not: bool = None,
        operation_list: List[str] = None,
    ):
        # Indicates whether the user is an administrator. Valid values:
        # 
        # *   true
        # *   false
        self.admin_or_not = admin_or_not
        # The resources on which the permissions are granted.
        self.operation_list = operation_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.admin_or_not is not None:
            result['AdminOrNot'] = self.admin_or_not
        if self.operation_list is not None:
            result['OperationList'] = self.operation_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdminOrNot') is not None:
            self.admin_or_not = m.get('AdminOrNot')
        if m.get('OperationList') is not None:
            self.operation_list = m.get('OperationList')
        return self


class ListOperationResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: ListOperationResponseBodyData = None,
        dy_code: str = None,
        dy_message: str = None,
        err_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code.
        self.code = code
        # The response parameters.
        self.data = data
        # The dynamic error code.
        self.dy_code = dy_code
        # The dynamic message.
        self.dy_message = dy_message
        # The error code.
        self.err_code = err_code
        # The message returned.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
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
        if self.dy_code is not None:
            result['DyCode'] = self.dy_code
        if self.dy_message is not None:
            result['DyMessage'] = self.dy_message
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
            temp_model = ListOperationResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('DyCode') is not None:
            self.dy_code = m.get('DyCode')
        if m.get('DyMessage') is not None:
            self.dy_message = m.get('DyMessage')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListOperationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListOperationResponseBody = None,
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
            temp_model = ListOperationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListProjectLogStoresRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        source_log_code: str = None,
        source_prod_code: str = None,
        sub_user_id: int = None,
    ):
        self.region_id = region_id
        self.source_log_code = source_log_code
        self.source_prod_code = source_prod_code
        self.sub_user_id = sub_user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.source_log_code is not None:
            result['SourceLogCode'] = self.source_log_code
        if self.source_prod_code is not None:
            result['SourceProdCode'] = self.source_prod_code
        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SourceLogCode') is not None:
            self.source_log_code = m.get('SourceLogCode')
        if m.get('SourceProdCode') is not None:
            self.source_prod_code = m.get('SourceProdCode')
        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')
        return self


class ListProjectLogStoresResponseBodyData(TeaModel):
    def __init__(
        self,
        end_point: str = None,
        local_name: str = None,
        log_store: str = None,
        main_user_id: int = None,
        project: str = None,
        region_id: str = None,
        sub_user_id: int = None,
        sub_user_name: str = None,
    ):
        self.end_point = end_point
        self.local_name = local_name
        self.log_store = log_store
        self.main_user_id = main_user_id
        self.project = project
        self.region_id = region_id
        self.sub_user_id = sub_user_id
        self.sub_user_name = sub_user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_point is not None:
            result['EndPoint'] = self.end_point
        if self.local_name is not None:
            result['LocalName'] = self.local_name
        if self.log_store is not None:
            result['LogStore'] = self.log_store
        if self.main_user_id is not None:
            result['MainUserId'] = self.main_user_id
        if self.project is not None:
            result['Project'] = self.project
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id
        if self.sub_user_name is not None:
            result['SubUserName'] = self.sub_user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndPoint') is not None:
            self.end_point = m.get('EndPoint')
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')
        if m.get('LogStore') is not None:
            self.log_store = m.get('LogStore')
        if m.get('MainUserId') is not None:
            self.main_user_id = m.get('MainUserId')
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')
        if m.get('SubUserName') is not None:
            self.sub_user_name = m.get('SubUserName')
        return self


class ListProjectLogStoresResponseBody(TeaModel):
    def __init__(
        self,
        data: List[ListProjectLogStoresResponseBodyData] = None,
        request_id: str = None,
    ):
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
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListProjectLogStoresResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListProjectLogStoresResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListProjectLogStoresResponseBody = None,
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
            temp_model = ListProjectLogStoresResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListQuickQueryRequest(TeaModel):
    def __init__(
        self,
        offset: int = None,
        page_size: int = None,
        region_id: str = None,
    ):
        # The line from which the query starts. Default value: 0.
        self.offset = offset
        # The number of entries per page. Valid values: 1 to 500.
        self.page_size = page_size
        # The region in which the data management center of the threat analysis feature resides. Specify this parameter based on the region where your assets reside. Valid values:
        # 
        # *   cn-hangzhou: Your assets reside in regions inside the Chinese mainland or in the China (Hong Kong) region.
        # *   ap-southeast-1: Your assets reside in regions outside the Chinese mainland, excluding the China (Hong Kong) region.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.offset is not None:
            result['Offset'] = self.offset
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Offset') is not None:
            self.offset = m.get('Offset')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListQuickQueryResponseBodyDataQuickQueryList(TeaModel):
    def __init__(
        self,
        display_name: str = None,
        query: str = None,
        search_name: str = None,
    ):
        # The alias of the saved search.
        self.display_name = display_name
        # The query statement corresponding to the saved search.
        self.query = query
        # The name of the saved search.
        self.search_name = search_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.query is not None:
            result['Query'] = self.query
        if self.search_name is not None:
            result['SearchName'] = self.search_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Query') is not None:
            self.query = m.get('Query')
        if m.get('SearchName') is not None:
            self.search_name = m.get('SearchName')
        return self


class ListQuickQueryResponseBodyData(TeaModel):
    def __init__(
        self,
        count: int = None,
        quick_query_list: List[ListQuickQueryResponseBodyDataQuickQueryList] = None,
        total: int = None,
    ):
        # The number of saved searches per page.
        self.count = count
        # The saved search.
        self.quick_query_list = quick_query_list
        # The total number of saved searches that meet the query conditions.
        self.total = total

    def validate(self):
        if self.quick_query_list:
            for k in self.quick_query_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        result['QuickQueryList'] = []
        if self.quick_query_list is not None:
            for k in self.quick_query_list:
                result['QuickQueryList'].append(k.to_map() if k else None)
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        self.quick_query_list = []
        if m.get('QuickQueryList') is not None:
            for k in m.get('QuickQueryList'):
                temp_model = ListQuickQueryResponseBodyDataQuickQueryList()
                self.quick_query_list.append(temp_model.from_map(k))
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListQuickQueryResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: ListQuickQueryResponseBodyData = None,
        dy_code: str = None,
        dy_message: str = None,
        err_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code.
        self.code = code
        # The response parameters.
        self.data = data
        # The dynamic error code.
        self.dy_code = dy_code
        # The dynamic message.
        self.dy_message = dy_message
        # The error code.
        self.err_code = err_code
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
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
        if self.dy_code is not None:
            result['DyCode'] = self.dy_code
        if self.dy_message is not None:
            result['DyMessage'] = self.dy_message
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
            temp_model = ListQuickQueryResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('DyCode') is not None:
            self.dy_code = m.get('DyCode')
        if m.get('DyMessage') is not None:
            self.dy_message = m.get('DyMessage')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListQuickQueryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListQuickQueryResponseBody = None,
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
            temp_model = ListQuickQueryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRdUsersRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
    ):
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListRdUsersResponseBodyData(TeaModel):
    def __init__(
        self,
        delegated_or_not: bool = None,
        joined: bool = None,
        joined_time: str = None,
        main_user_id: int = None,
        sub_user_id: int = None,
        sub_user_name: str = None,
    ):
        self.delegated_or_not = delegated_or_not
        self.joined = joined
        self.joined_time = joined_time
        self.main_user_id = main_user_id
        self.sub_user_id = sub_user_id
        self.sub_user_name = sub_user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delegated_or_not is not None:
            result['DelegatedOrNot'] = self.delegated_or_not
        if self.joined is not None:
            result['Joined'] = self.joined
        if self.joined_time is not None:
            result['JoinedTime'] = self.joined_time
        if self.main_user_id is not None:
            result['MainUserId'] = self.main_user_id
        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id
        if self.sub_user_name is not None:
            result['SubUserName'] = self.sub_user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DelegatedOrNot') is not None:
            self.delegated_or_not = m.get('DelegatedOrNot')
        if m.get('Joined') is not None:
            self.joined = m.get('Joined')
        if m.get('JoinedTime') is not None:
            self.joined_time = m.get('JoinedTime')
        if m.get('MainUserId') is not None:
            self.main_user_id = m.get('MainUserId')
        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')
        if m.get('SubUserName') is not None:
            self.sub_user_name = m.get('SubUserName')
        return self


class ListRdUsersResponseBody(TeaModel):
    def __init__(
        self,
        data: List[ListRdUsersResponseBodyData] = None,
        request_id: str = None,
    ):
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
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListRdUsersResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListRdUsersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListRdUsersResponseBody = None,
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
            temp_model = ListRdUsersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUserProdLogsRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        source_log_code: str = None,
        source_prod_code: str = None,
    ):
        self.region_id = region_id
        self.source_log_code = source_log_code
        self.source_prod_code = source_prod_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.source_log_code is not None:
            result['SourceLogCode'] = self.source_log_code
        if self.source_prod_code is not None:
            result['SourceProdCode'] = self.source_prod_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SourceLogCode') is not None:
            self.source_log_code = m.get('SourceLogCode')
        if m.get('SourceProdCode') is not None:
            self.source_prod_code = m.get('SourceProdCode')
        return self


class ListUserProdLogsResponseBodyData(TeaModel):
    def __init__(
        self,
        display_line: str = None,
        displayed: bool = None,
        imported: bool = None,
        is_deleted: int = None,
        main_user_id: int = None,
        source_log_code: str = None,
        source_log_info: str = None,
        source_prod_code: str = None,
        sub_user_id: int = None,
        sub_user_name: str = None,
    ):
        self.display_line = display_line
        self.displayed = displayed
        self.imported = imported
        self.is_deleted = is_deleted
        self.main_user_id = main_user_id
        self.source_log_code = source_log_code
        self.source_log_info = source_log_info
        self.source_prod_code = source_prod_code
        self.sub_user_id = sub_user_id
        self.sub_user_name = sub_user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display_line is not None:
            result['DisplayLine'] = self.display_line
        if self.displayed is not None:
            result['Displayed'] = self.displayed
        if self.imported is not None:
            result['Imported'] = self.imported
        if self.is_deleted is not None:
            result['IsDeleted'] = self.is_deleted
        if self.main_user_id is not None:
            result['MainUserId'] = self.main_user_id
        if self.source_log_code is not None:
            result['SourceLogCode'] = self.source_log_code
        if self.source_log_info is not None:
            result['SourceLogInfo'] = self.source_log_info
        if self.source_prod_code is not None:
            result['SourceProdCode'] = self.source_prod_code
        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id
        if self.sub_user_name is not None:
            result['SubUserName'] = self.sub_user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayLine') is not None:
            self.display_line = m.get('DisplayLine')
        if m.get('Displayed') is not None:
            self.displayed = m.get('Displayed')
        if m.get('Imported') is not None:
            self.imported = m.get('Imported')
        if m.get('IsDeleted') is not None:
            self.is_deleted = m.get('IsDeleted')
        if m.get('MainUserId') is not None:
            self.main_user_id = m.get('MainUserId')
        if m.get('SourceLogCode') is not None:
            self.source_log_code = m.get('SourceLogCode')
        if m.get('SourceLogInfo') is not None:
            self.source_log_info = m.get('SourceLogInfo')
        if m.get('SourceProdCode') is not None:
            self.source_prod_code = m.get('SourceProdCode')
        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')
        if m.get('SubUserName') is not None:
            self.sub_user_name = m.get('SubUserName')
        return self


class ListUserProdLogsResponseBody(TeaModel):
    def __init__(
        self,
        data: List[ListUserProdLogsResponseBodyData] = None,
        request_id: str = None,
    ):
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
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListUserProdLogsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListUserProdLogsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListUserProdLogsResponseBody = None,
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
            temp_model = ListUserProdLogsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUsersByProdRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        source_prod_code: str = None,
    ):
        self.region_id = region_id
        self.source_prod_code = source_prod_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.source_prod_code is not None:
            result['SourceProdCode'] = self.source_prod_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SourceProdCode') is not None:
            self.source_prod_code = m.get('SourceProdCode')
        return self


class ListUsersByProdResponseBodyData(TeaModel):
    def __init__(
        self,
        cloud_code: str = None,
        imported: bool = None,
        log_mds_code: str = None,
        main_user_id: int = None,
        source_log_code: str = None,
        source_log_name: str = None,
        source_prod_code: str = None,
        sub_user_id: int = None,
        sub_user_name: str = None,
    ):
        self.cloud_code = cloud_code
        self.imported = imported
        self.log_mds_code = log_mds_code
        self.main_user_id = main_user_id
        self.source_log_code = source_log_code
        self.source_log_name = source_log_name
        self.source_prod_code = source_prod_code
        self.sub_user_id = sub_user_id
        self.sub_user_name = sub_user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cloud_code is not None:
            result['CloudCode'] = self.cloud_code
        if self.imported is not None:
            result['Imported'] = self.imported
        if self.log_mds_code is not None:
            result['LogMdsCode'] = self.log_mds_code
        if self.main_user_id is not None:
            result['MainUserId'] = self.main_user_id
        if self.source_log_code is not None:
            result['SourceLogCode'] = self.source_log_code
        if self.source_log_name is not None:
            result['SourceLogName'] = self.source_log_name
        if self.source_prod_code is not None:
            result['SourceProdCode'] = self.source_prod_code
        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id
        if self.sub_user_name is not None:
            result['SubUserName'] = self.sub_user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CloudCode') is not None:
            self.cloud_code = m.get('CloudCode')
        if m.get('Imported') is not None:
            self.imported = m.get('Imported')
        if m.get('LogMdsCode') is not None:
            self.log_mds_code = m.get('LogMdsCode')
        if m.get('MainUserId') is not None:
            self.main_user_id = m.get('MainUserId')
        if m.get('SourceLogCode') is not None:
            self.source_log_code = m.get('SourceLogCode')
        if m.get('SourceLogName') is not None:
            self.source_log_name = m.get('SourceLogName')
        if m.get('SourceProdCode') is not None:
            self.source_prod_code = m.get('SourceProdCode')
        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')
        if m.get('SubUserName') is not None:
            self.sub_user_name = m.get('SubUserName')
        return self


class ListUsersByProdResponseBody(TeaModel):
    def __init__(
        self,
        data: List[ListUsersByProdResponseBodyData] = None,
        request_id: str = None,
    ):
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
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListUsersByProdResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListUsersByProdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListUsersByProdResponseBody = None,
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
            temp_model = ListUsersByProdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyBindAccountRequest(TeaModel):
    def __init__(
        self,
        access_id: str = None,
        account_id: str = None,
        account_name: str = None,
        bind_id: int = None,
        cloud_code: str = None,
        region_id: str = None,
    ):
        self.access_id = access_id
        self.account_id = account_id
        self.account_name = account_name
        self.bind_id = bind_id
        self.cloud_code = cloud_code
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_id is not None:
            result['AccessId'] = self.access_id
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.bind_id is not None:
            result['BindId'] = self.bind_id
        if self.cloud_code is not None:
            result['CloudCode'] = self.cloud_code
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessId') is not None:
            self.access_id = m.get('AccessId')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('BindId') is not None:
            self.bind_id = m.get('BindId')
        if m.get('CloudCode') is not None:
            self.cloud_code = m.get('CloudCode')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ModifyBindAccountResponseBodyData(TeaModel):
    def __init__(
        self,
        count: int = None,
    ):
        self.count = count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class ModifyBindAccountResponseBody(TeaModel):
    def __init__(
        self,
        data: ModifyBindAccountResponseBodyData = None,
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
            temp_model = ModifyBindAccountResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyBindAccountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyBindAccountResponseBody = None,
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
            temp_model = ModifyBindAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDataSourceRequest(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        cloud_code: str = None,
        data_source_instance_id: str = None,
        data_source_instance_name: str = None,
        data_source_instance_params: str = None,
        data_source_instance_remark: str = None,
        data_source_type: str = None,
        region_id: str = None,
    ):
        self.account_id = account_id
        self.cloud_code = cloud_code
        self.data_source_instance_id = data_source_instance_id
        self.data_source_instance_name = data_source_instance_name
        self.data_source_instance_params = data_source_instance_params
        self.data_source_instance_remark = data_source_instance_remark
        self.data_source_type = data_source_type
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.cloud_code is not None:
            result['CloudCode'] = self.cloud_code
        if self.data_source_instance_id is not None:
            result['DataSourceInstanceId'] = self.data_source_instance_id
        if self.data_source_instance_name is not None:
            result['DataSourceInstanceName'] = self.data_source_instance_name
        if self.data_source_instance_params is not None:
            result['DataSourceInstanceParams'] = self.data_source_instance_params
        if self.data_source_instance_remark is not None:
            result['DataSourceInstanceRemark'] = self.data_source_instance_remark
        if self.data_source_type is not None:
            result['DataSourceType'] = self.data_source_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('CloudCode') is not None:
            self.cloud_code = m.get('CloudCode')
        if m.get('DataSourceInstanceId') is not None:
            self.data_source_instance_id = m.get('DataSourceInstanceId')
        if m.get('DataSourceInstanceName') is not None:
            self.data_source_instance_name = m.get('DataSourceInstanceName')
        if m.get('DataSourceInstanceParams') is not None:
            self.data_source_instance_params = m.get('DataSourceInstanceParams')
        if m.get('DataSourceInstanceRemark') is not None:
            self.data_source_instance_remark = m.get('DataSourceInstanceRemark')
        if m.get('DataSourceType') is not None:
            self.data_source_type = m.get('DataSourceType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ModifyDataSourceResponseBodyData(TeaModel):
    def __init__(
        self,
        count: int = None,
        data_source_instance_id: str = None,
    ):
        self.count = count
        self.data_source_instance_id = data_source_instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.data_source_instance_id is not None:
            result['DataSourceInstanceId'] = self.data_source_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('DataSourceInstanceId') is not None:
            self.data_source_instance_id = m.get('DataSourceInstanceId')
        return self


class ModifyDataSourceResponseBody(TeaModel):
    def __init__(
        self,
        data: ModifyDataSourceResponseBodyData = None,
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
            temp_model = ModifyDataSourceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyDataSourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyDataSourceResponseBody = None,
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
            temp_model = ModifyDataSourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDataSourceLogRequest(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        cloud_code: str = None,
        data_source_instance_id: str = None,
        data_source_instance_logs: str = None,
        data_source_type: str = None,
        log_code: str = None,
        log_instance_id: str = None,
        region_id: str = None,
    ):
        self.account_id = account_id
        self.cloud_code = cloud_code
        self.data_source_instance_id = data_source_instance_id
        self.data_source_instance_logs = data_source_instance_logs
        self.data_source_type = data_source_type
        self.log_code = log_code
        self.log_instance_id = log_instance_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.cloud_code is not None:
            result['CloudCode'] = self.cloud_code
        if self.data_source_instance_id is not None:
            result['DataSourceInstanceId'] = self.data_source_instance_id
        if self.data_source_instance_logs is not None:
            result['DataSourceInstanceLogs'] = self.data_source_instance_logs
        if self.data_source_type is not None:
            result['DataSourceType'] = self.data_source_type
        if self.log_code is not None:
            result['LogCode'] = self.log_code
        if self.log_instance_id is not None:
            result['LogInstanceId'] = self.log_instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('CloudCode') is not None:
            self.cloud_code = m.get('CloudCode')
        if m.get('DataSourceInstanceId') is not None:
            self.data_source_instance_id = m.get('DataSourceInstanceId')
        if m.get('DataSourceInstanceLogs') is not None:
            self.data_source_instance_logs = m.get('DataSourceInstanceLogs')
        if m.get('DataSourceType') is not None:
            self.data_source_type = m.get('DataSourceType')
        if m.get('LogCode') is not None:
            self.log_code = m.get('LogCode')
        if m.get('LogInstanceId') is not None:
            self.log_instance_id = m.get('LogInstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ModifyDataSourceLogResponseBodyData(TeaModel):
    def __init__(
        self,
        count: int = None,
        log_instance_id: str = None,
    ):
        self.count = count
        self.log_instance_id = log_instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.log_instance_id is not None:
            result['LogInstanceId'] = self.log_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('LogInstanceId') is not None:
            self.log_instance_id = m.get('LogInstanceId')
        return self


class ModifyDataSourceLogResponseBody(TeaModel):
    def __init__(
        self,
        data: ModifyDataSourceLogResponseBodyData = None,
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
            temp_model = ModifyDataSourceLogResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyDataSourceLogResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyDataSourceLogResponseBody = None,
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
            temp_model = ModifyDataSourceLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OpenDeliveryRequest(TeaModel):
    def __init__(
        self,
        log_code: str = None,
        product_code: str = None,
        region_id: str = None,
    ):
        # The log code of the cloud service, such as the code of the process log for Security Center. If you leave this parameter empty, operations are performed on all logs of the cloud service.
        self.log_code = log_code
        # The code of the cloud service. Valid values:
        # 
        # *   qcloud_waf
        # *   qlcoud_cfw
        # *   hcloud_waf
        # *   hcloud_cfw
        # *   ddos
        # *   sas
        # *   cfw
        # *   config
        # *   csk
        # *   fc
        # *   rds
        # *   nas
        # *   apigateway
        # *   cdn
        # *   mongodb
        # *   eip
        # *   slb
        # *   vpc
        # *   actiontrail
        # *   waf
        # *   bastionhost
        # *   oss
        # *   polardb
        self.product_code = product_code
        # The region in which the data management center of the threat analysis feature resides. Specify this parameter based on the region where your assets reside. Valid values:
        # 
        # *   cn-hangzhou: Your assets reside in regions inside the Chinese mainland or in the China (Hong Kong) region.
        # *   ap-southeast-1: Your assets reside in regions outside the Chinese mainland, excluding the China (Hong Kong) region.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.log_code is not None:
            result['LogCode'] = self.log_code
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LogCode') is not None:
            self.log_code = m.get('LogCode')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class OpenDeliveryResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: bool = None,
        dy_code: str = None,
        dy_message: str = None,
        err_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code.
        self.code = code
        # Indicates whether the log delivery feature is enabled. Valid values:
        # 
        # *   true
        # *   false
        self.data = data
        # The dynamic error code.
        self.dy_code = dy_code
        # The dynamic message.
        self.dy_message = dy_message
        # The error code.
        self.err_code = err_code
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
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
        if self.dy_code is not None:
            result['DyCode'] = self.dy_code
        if self.dy_message is not None:
            result['DyMessage'] = self.dy_message
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
        if m.get('DyCode') is not None:
            self.dy_code = m.get('DyCode')
        if m.get('DyMessage') is not None:
            self.dy_message = m.get('DyMessage')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class OpenDeliveryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: OpenDeliveryResponseBody = None,
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
            temp_model = OpenDeliveryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PostAutomateResponseConfigRequest(TeaModel):
    def __init__(
        self,
        action_config: str = None,
        action_type: str = None,
        auto_response_type: str = None,
        execution_condition: str = None,
        id: int = None,
        region_id: str = None,
        rule_name: str = None,
        sub_user_id: int = None,
    ):
        self.action_config = action_config
        self.action_type = action_type
        self.auto_response_type = auto_response_type
        self.execution_condition = execution_condition
        self.id = id
        self.region_id = region_id
        self.rule_name = rule_name
        self.sub_user_id = sub_user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_config is not None:
            result['ActionConfig'] = self.action_config
        if self.action_type is not None:
            result['ActionType'] = self.action_type
        if self.auto_response_type is not None:
            result['AutoResponseType'] = self.auto_response_type
        if self.execution_condition is not None:
            result['ExecutionCondition'] = self.execution_condition
        if self.id is not None:
            result['Id'] = self.id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionConfig') is not None:
            self.action_config = m.get('ActionConfig')
        if m.get('ActionType') is not None:
            self.action_type = m.get('ActionType')
        if m.get('AutoResponseType') is not None:
            self.auto_response_type = m.get('AutoResponseType')
        if m.get('ExecutionCondition') is not None:
            self.execution_condition = m.get('ExecutionCondition')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')
        return self


class PostAutomateResponseConfigResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
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
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class PostAutomateResponseConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PostAutomateResponseConfigResponseBody = None,
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
            temp_model = PostAutomateResponseConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PostCustomizeRuleRequest(TeaModel):
    def __init__(
        self,
        alert_type: str = None,
        alert_type_mds: str = None,
        event_transfer_ext: str = None,
        event_transfer_switch: int = None,
        event_transfer_type: str = None,
        id: int = None,
        log_source: str = None,
        log_source_mds: str = None,
        log_type: str = None,
        log_type_mds: str = None,
        query_cycle: str = None,
        region_id: str = None,
        rule_condition: str = None,
        rule_desc: str = None,
        rule_group: str = None,
        rule_name: str = None,
        rule_threshold: str = None,
        threat_level: str = None,
    ):
        self.alert_type = alert_type
        self.alert_type_mds = alert_type_mds
        self.event_transfer_ext = event_transfer_ext
        self.event_transfer_switch = event_transfer_switch
        self.event_transfer_type = event_transfer_type
        self.id = id
        self.log_source = log_source
        self.log_source_mds = log_source_mds
        self.log_type = log_type
        self.log_type_mds = log_type_mds
        self.query_cycle = query_cycle
        self.region_id = region_id
        self.rule_condition = rule_condition
        self.rule_desc = rule_desc
        self.rule_group = rule_group
        self.rule_name = rule_name
        self.rule_threshold = rule_threshold
        self.threat_level = threat_level

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_type is not None:
            result['AlertType'] = self.alert_type
        if self.alert_type_mds is not None:
            result['AlertTypeMds'] = self.alert_type_mds
        if self.event_transfer_ext is not None:
            result['EventTransferExt'] = self.event_transfer_ext
        if self.event_transfer_switch is not None:
            result['EventTransferSwitch'] = self.event_transfer_switch
        if self.event_transfer_type is not None:
            result['EventTransferType'] = self.event_transfer_type
        if self.id is not None:
            result['Id'] = self.id
        if self.log_source is not None:
            result['LogSource'] = self.log_source
        if self.log_source_mds is not None:
            result['LogSourceMds'] = self.log_source_mds
        if self.log_type is not None:
            result['LogType'] = self.log_type
        if self.log_type_mds is not None:
            result['LogTypeMds'] = self.log_type_mds
        if self.query_cycle is not None:
            result['QueryCycle'] = self.query_cycle
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.rule_condition is not None:
            result['RuleCondition'] = self.rule_condition
        if self.rule_desc is not None:
            result['RuleDesc'] = self.rule_desc
        if self.rule_group is not None:
            result['RuleGroup'] = self.rule_group
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.rule_threshold is not None:
            result['RuleThreshold'] = self.rule_threshold
        if self.threat_level is not None:
            result['ThreatLevel'] = self.threat_level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertType') is not None:
            self.alert_type = m.get('AlertType')
        if m.get('AlertTypeMds') is not None:
            self.alert_type_mds = m.get('AlertTypeMds')
        if m.get('EventTransferExt') is not None:
            self.event_transfer_ext = m.get('EventTransferExt')
        if m.get('EventTransferSwitch') is not None:
            self.event_transfer_switch = m.get('EventTransferSwitch')
        if m.get('EventTransferType') is not None:
            self.event_transfer_type = m.get('EventTransferType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LogSource') is not None:
            self.log_source = m.get('LogSource')
        if m.get('LogSourceMds') is not None:
            self.log_source_mds = m.get('LogSourceMds')
        if m.get('LogType') is not None:
            self.log_type = m.get('LogType')
        if m.get('LogTypeMds') is not None:
            self.log_type_mds = m.get('LogTypeMds')
        if m.get('QueryCycle') is not None:
            self.query_cycle = m.get('QueryCycle')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RuleCondition') is not None:
            self.rule_condition = m.get('RuleCondition')
        if m.get('RuleDesc') is not None:
            self.rule_desc = m.get('RuleDesc')
        if m.get('RuleGroup') is not None:
            self.rule_group = m.get('RuleGroup')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('RuleThreshold') is not None:
            self.rule_threshold = m.get('RuleThreshold')
        if m.get('ThreatLevel') is not None:
            self.threat_level = m.get('ThreatLevel')
        return self


class PostCustomizeRuleResponseBodyData(TeaModel):
    def __init__(
        self,
        alert_type: str = None,
        alert_type_mds: str = None,
        aliuid: int = None,
        event_transfer_ext: str = None,
        event_transfer_switch: int = None,
        event_transfer_type: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        log_source: str = None,
        log_source_mds: str = None,
        log_type: str = None,
        log_type_mds: str = None,
        query_cycle: str = None,
        rule_condition: str = None,
        rule_desc: str = None,
        rule_group: str = None,
        rule_name: str = None,
        rule_threshold: str = None,
        rule_type: str = None,
        status: int = None,
        threat_level: str = None,
    ):
        self.alert_type = alert_type
        self.alert_type_mds = alert_type_mds
        self.aliuid = aliuid
        self.event_transfer_ext = event_transfer_ext
        self.event_transfer_switch = event_transfer_switch
        self.event_transfer_type = event_transfer_type
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.log_source = log_source
        self.log_source_mds = log_source_mds
        self.log_type = log_type
        self.log_type_mds = log_type_mds
        self.query_cycle = query_cycle
        self.rule_condition = rule_condition
        self.rule_desc = rule_desc
        self.rule_group = rule_group
        self.rule_name = rule_name
        self.rule_threshold = rule_threshold
        self.rule_type = rule_type
        self.status = status
        self.threat_level = threat_level

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_type is not None:
            result['AlertType'] = self.alert_type
        if self.alert_type_mds is not None:
            result['AlertTypeMds'] = self.alert_type_mds
        if self.aliuid is not None:
            result['Aliuid'] = self.aliuid
        if self.event_transfer_ext is not None:
            result['EventTransferExt'] = self.event_transfer_ext
        if self.event_transfer_switch is not None:
            result['EventTransferSwitch'] = self.event_transfer_switch
        if self.event_transfer_type is not None:
            result['EventTransferType'] = self.event_transfer_type
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        if self.log_source is not None:
            result['LogSource'] = self.log_source
        if self.log_source_mds is not None:
            result['LogSourceMds'] = self.log_source_mds
        if self.log_type is not None:
            result['LogType'] = self.log_type
        if self.log_type_mds is not None:
            result['LogTypeMds'] = self.log_type_mds
        if self.query_cycle is not None:
            result['QueryCycle'] = self.query_cycle
        if self.rule_condition is not None:
            result['RuleCondition'] = self.rule_condition
        if self.rule_desc is not None:
            result['RuleDesc'] = self.rule_desc
        if self.rule_group is not None:
            result['RuleGroup'] = self.rule_group
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.rule_threshold is not None:
            result['RuleThreshold'] = self.rule_threshold
        if self.rule_type is not None:
            result['RuleType'] = self.rule_type
        if self.status is not None:
            result['Status'] = self.status
        if self.threat_level is not None:
            result['ThreatLevel'] = self.threat_level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertType') is not None:
            self.alert_type = m.get('AlertType')
        if m.get('AlertTypeMds') is not None:
            self.alert_type_mds = m.get('AlertTypeMds')
        if m.get('Aliuid') is not None:
            self.aliuid = m.get('Aliuid')
        if m.get('EventTransferExt') is not None:
            self.event_transfer_ext = m.get('EventTransferExt')
        if m.get('EventTransferSwitch') is not None:
            self.event_transfer_switch = m.get('EventTransferSwitch')
        if m.get('EventTransferType') is not None:
            self.event_transfer_type = m.get('EventTransferType')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LogSource') is not None:
            self.log_source = m.get('LogSource')
        if m.get('LogSourceMds') is not None:
            self.log_source_mds = m.get('LogSourceMds')
        if m.get('LogType') is not None:
            self.log_type = m.get('LogType')
        if m.get('LogTypeMds') is not None:
            self.log_type_mds = m.get('LogTypeMds')
        if m.get('QueryCycle') is not None:
            self.query_cycle = m.get('QueryCycle')
        if m.get('RuleCondition') is not None:
            self.rule_condition = m.get('RuleCondition')
        if m.get('RuleDesc') is not None:
            self.rule_desc = m.get('RuleDesc')
        if m.get('RuleGroup') is not None:
            self.rule_group = m.get('RuleGroup')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('RuleThreshold') is not None:
            self.rule_threshold = m.get('RuleThreshold')
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ThreatLevel') is not None:
            self.threat_level = m.get('ThreatLevel')
        return self


class PostCustomizeRuleResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: PostCustomizeRuleResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
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
            temp_model = PostCustomizeRuleResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class PostCustomizeRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PostCustomizeRuleResponseBody = None,
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
            temp_model = PostCustomizeRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PostCustomizeRuleTestRequest(TeaModel):
    def __init__(
        self,
        id: int = None,
        region_id: str = None,
        simulated_data: str = None,
        test_type: str = None,
    ):
        self.id = id
        self.region_id = region_id
        self.simulated_data = simulated_data
        self.test_type = test_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.simulated_data is not None:
            result['SimulatedData'] = self.simulated_data
        if self.test_type is not None:
            result['TestType'] = self.test_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SimulatedData') is not None:
            self.simulated_data = m.get('SimulatedData')
        if m.get('TestType') is not None:
            self.test_type = m.get('TestType')
        return self


class PostCustomizeRuleTestResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: Any = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
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
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class PostCustomizeRuleTestResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PostCustomizeRuleTestResponseBody = None,
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
            temp_model = PostCustomizeRuleTestResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PostEventDisposeAndWhiteruleListRequest(TeaModel):
    def __init__(
        self,
        event_dispose: str = None,
        incident_uuid: str = None,
        receiver_info: str = None,
        region_id: str = None,
        remark: str = None,
        status: int = None,
    ):
        self.event_dispose = event_dispose
        self.incident_uuid = incident_uuid
        self.receiver_info = receiver_info
        self.region_id = region_id
        self.remark = remark
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_dispose is not None:
            result['EventDispose'] = self.event_dispose
        if self.incident_uuid is not None:
            result['IncidentUuid'] = self.incident_uuid
        if self.receiver_info is not None:
            result['ReceiverInfo'] = self.receiver_info
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventDispose') is not None:
            self.event_dispose = m.get('EventDispose')
        if m.get('IncidentUuid') is not None:
            self.incident_uuid = m.get('IncidentUuid')
        if m.get('ReceiverInfo') is not None:
            self.receiver_info = m.get('ReceiverInfo')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class PostEventDisposeAndWhiteruleListResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
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
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class PostEventDisposeAndWhiteruleListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PostEventDisposeAndWhiteruleListResponseBody = None,
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
            temp_model = PostEventDisposeAndWhiteruleListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PostEventWhiteruleListRequest(TeaModel):
    def __init__(
        self,
        incident_uuid: str = None,
        region_id: str = None,
        whiterule_list: str = None,
    ):
        self.incident_uuid = incident_uuid
        self.region_id = region_id
        self.whiterule_list = whiterule_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.incident_uuid is not None:
            result['IncidentUuid'] = self.incident_uuid
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.whiterule_list is not None:
            result['WhiteruleList'] = self.whiterule_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IncidentUuid') is not None:
            self.incident_uuid = m.get('IncidentUuid')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('WhiteruleList') is not None:
            self.whiterule_list = m.get('WhiteruleList')
        return self


class PostEventWhiteruleListResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
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
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class PostEventWhiteruleListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PostEventWhiteruleListResponseBody = None,
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
            temp_model = PostEventWhiteruleListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PostFinishCustomizeRuleTestRequest(TeaModel):
    def __init__(
        self,
        id: int = None,
        region_id: str = None,
    ):
        self.id = id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class PostFinishCustomizeRuleTestResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: Any = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
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
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class PostFinishCustomizeRuleTestResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PostFinishCustomizeRuleTestResponseBody = None,
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
            temp_model = PostFinishCustomizeRuleTestResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PostRuleStatusChangeRequest(TeaModel):
    def __init__(
        self,
        ids: str = None,
        in_use: bool = None,
        region_id: str = None,
        rule_type: str = None,
    ):
        self.ids = ids
        self.in_use = in_use
        self.region_id = region_id
        self.rule_type = rule_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ids is not None:
            result['Ids'] = self.ids
        if self.in_use is not None:
            result['InUse'] = self.in_use
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.rule_type is not None:
            result['RuleType'] = self.rule_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ids') is not None:
            self.ids = m.get('Ids')
        if m.get('InUse') is not None:
            self.in_use = m.get('InUse')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        return self


class PostRuleStatusChangeResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: Any = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
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
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class PostRuleStatusChangeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PostRuleStatusChangeResponseBody = None,
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
            temp_model = PostRuleStatusChangeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RestoreCapacityRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
    ):
        # The data management center of the threat analysis feature. Specify this parameter based on the region where your assets reside. Valid values:
        # 
        # *   cn-hangzhou: Your assets reside in regions in the Chinese mainland or in the China (Hong Kong) region.
        # *   ap-southeast-1: Your assets reside in regions outside the Chinese mainland, excluding the China (Hong Kong) region.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class RestoreCapacityResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: bool = None,
        dy_code: str = None,
        dy_message: str = None,
        err_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code.
        self.code = code
        # Indicates whether the release command has been sent. Valid values:
        # 
        # *   true: The command has been sent and the storage space is being released.
        # *   false: The command failed to be sent.
        self.data = data
        # The dynamic error code.
        self.dy_code = dy_code
        # The dynamic message.
        self.dy_message = dy_message
        # The error code.
        self.err_code = err_code
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
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
        if self.dy_code is not None:
            result['DyCode'] = self.dy_code
        if self.dy_message is not None:
            result['DyMessage'] = self.dy_message
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
        if m.get('DyCode') is not None:
            self.dy_code = m.get('DyCode')
        if m.get('DyMessage') is not None:
            self.dy_message = m.get('DyMessage')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RestoreCapacityResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RestoreCapacityResponseBody = None,
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
            temp_model = RestoreCapacityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveQuickQueryRequest(TeaModel):
    def __init__(
        self,
        display_name: str = None,
        query: str = None,
        region_id: str = None,
    ):
        # The name of the saved search.
        self.display_name = display_name
        # The query statement.
        self.query = query
        # The data management center of the threat analysis feature. Specify this parameter based on the region where your assets reside. Valid values:
        # 
        # *   cn-hangzhou: Your assets reside in regions in the Chinese mainland or in the China (Hong Kong) region.
        # *   ap-southeast-1: Your assets reside in regions outside the Chinese mainland, excluding the China (Hong Kong) region.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.query is not None:
            result['Query'] = self.query
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Query') is not None:
            self.query = m.get('Query')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class SaveQuickQueryResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: bool = None,
        dy_code: str = None,
        dy_message: str = None,
        err_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code.
        self.code = code
        # Indicates whether the query statement is saved as a saved search. Valid values:
        # 
        # *   true
        # *   false
        self.data = data
        # The dynamic error code.
        self.dy_code = dy_code
        # The dynamic message.
        self.dy_message = dy_message
        # The error code.
        self.err_code = err_code
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
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
        if self.dy_code is not None:
            result['DyCode'] = self.dy_code
        if self.dy_message is not None:
            result['DyMessage'] = self.dy_message
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
        if m.get('DyCode') is not None:
            self.dy_code = m.get('DyCode')
        if m.get('DyMessage') is not None:
            self.dy_message = m.get('DyMessage')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SaveQuickQueryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SaveQuickQueryResponseBody = None,
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
            temp_model = SaveQuickQueryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetStorageRequest(TeaModel):
    def __init__(
        self,
        region: str = None,
        region_id: str = None,
        ttl: int = None,
    ):
        # The storage region of logs. By default, the region of the data management center is used and cannot be changed. cn-shanghai is used for the China data management center, and ap-southeast-1 is used for the Outside China data management center. To change the region, contact the technical support of threat analysis.
        self.region = region
        # The data management center of the threat analysis feature. Specify this parameter based on the region where your assets reside. Valid values:
        # 
        # *   cn-hangzhou: Your assets reside in regions in the Chinese mainland or in the China (Hong Kong) region.
        # *   ap-southeast-1: Your assets reside in regions outside the Chinese mainland, excluding the China (Hong Kong) region.
        self.region_id = region_id
        # The storage duration of logs. Default value: 180. Minimum value: 30. Maximum value: 3000. Unit: days.
        self.ttl = ttl

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region is not None:
            result['Region'] = self.region
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.ttl is not None:
            result['Ttl'] = self.ttl
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Ttl') is not None:
            self.ttl = m.get('Ttl')
        return self


class SetStorageResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: bool = None,
        dy_code: str = None,
        dy_message: str = None,
        err_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code.
        self.code = code
        # Indicates whether the settings are saved. Valid values:
        # 
        # *   true
        # *   false
        self.data = data
        # The dynamic error code.
        self.dy_code = dy_code
        # The dynamic message.
        self.dy_message = dy_message
        # The error code.
        self.err_code = err_code
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
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
        if self.dy_code is not None:
            result['DyCode'] = self.dy_code
        if self.dy_message is not None:
            result['DyMessage'] = self.dy_message
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
        if m.get('DyCode') is not None:
            self.dy_code = m.get('DyCode')
        if m.get('DyMessage') is not None:
            self.dy_message = m.get('DyMessage')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SetStorageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SetStorageResponseBody = None,
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
            temp_model = SetStorageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ShowQuickAnalysisRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
    ):
        # The data management center of the threat analysis feature. Specify this parameter based on the region where your assets reside. Valid values:
        # 
        # *   cn-hangzhou: Your assets reside in regions in the Chinese mainland or in the China (Hong Kong) region.
        # *   ap-southeast-1: Your assets reside in regions outside the Chinese mainland, excluding the China (Hong Kong) region.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ShowQuickAnalysisResponseBodyData(TeaModel):
    def __init__(
        self,
        index_list: List[str] = None,
    ):
        # The index fields of the logs.
        self.index_list = index_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.index_list is not None:
            result['IndexList'] = self.index_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IndexList') is not None:
            self.index_list = m.get('IndexList')
        return self


class ShowQuickAnalysisResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: ShowQuickAnalysisResponseBodyData = None,
        dy_code: str = None,
        dy_message: str = None,
        err_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code.
        self.code = code
        # The index fields.
        self.data = data
        # The dynamic error code.
        self.dy_code = dy_code
        # The dynamic message.
        self.dy_message = dy_message
        # The error code.
        self.err_code = err_code
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
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
        if self.dy_code is not None:
            result['DyCode'] = self.dy_code
        if self.dy_message is not None:
            result['DyMessage'] = self.dy_message
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
            temp_model = ShowQuickAnalysisResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('DyCode') is not None:
            self.dy_code = m.get('DyCode')
        if m.get('DyMessage') is not None:
            self.dy_message = m.get('DyMessage')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ShowQuickAnalysisResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ShowQuickAnalysisResponseBody = None,
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
            temp_model = ShowQuickAnalysisResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitImportLogTasksRequest(TeaModel):
    def __init__(
        self,
        accounts: str = None,
        auto_imported: int = None,
        cloud_code: str = None,
        log_codes: str = None,
        prod_code: str = None,
        region_id: str = None,
    ):
        self.accounts = accounts
        self.auto_imported = auto_imported
        self.cloud_code = cloud_code
        self.log_codes = log_codes
        self.prod_code = prod_code
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accounts is not None:
            result['Accounts'] = self.accounts
        if self.auto_imported is not None:
            result['AutoImported'] = self.auto_imported
        if self.cloud_code is not None:
            result['CloudCode'] = self.cloud_code
        if self.log_codes is not None:
            result['LogCodes'] = self.log_codes
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accounts') is not None:
            self.accounts = m.get('Accounts')
        if m.get('AutoImported') is not None:
            self.auto_imported = m.get('AutoImported')
        if m.get('CloudCode') is not None:
            self.cloud_code = m.get('CloudCode')
        if m.get('LogCodes') is not None:
            self.log_codes = m.get('LogCodes')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class SubmitImportLogTasksResponseBodyData(TeaModel):
    def __init__(
        self,
        count: int = None,
    ):
        self.count = count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class SubmitImportLogTasksResponseBody(TeaModel):
    def __init__(
        self,
        data: SubmitImportLogTasksResponseBodyData = None,
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
            temp_model = SubmitImportLogTasksResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SubmitImportLogTasksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SubmitImportLogTasksResponseBody = None,
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
            temp_model = SubmitImportLogTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitJobsRequest(TeaModel):
    def __init__(
        self,
        json_param: str = None,
        region_id: str = None,
    ):
        self.json_param = json_param
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.json_param is not None:
            result['JsonParam'] = self.json_param
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JsonParam') is not None:
            self.json_param = m.get('JsonParam')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class SubmitJobsResponseBody(TeaModel):
    def __init__(
        self,
        data: int = None,
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


class SubmitJobsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SubmitJobsResponseBody = None,
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
            temp_model = SubmitJobsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAutomateResponseConfigStatusRequest(TeaModel):
    def __init__(
        self,
        ids: str = None,
        in_use: bool = None,
        region_id: str = None,
    ):
        self.ids = ids
        self.in_use = in_use
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ids is not None:
            result['Ids'] = self.ids
        if self.in_use is not None:
            result['InUse'] = self.in_use
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ids') is not None:
            self.ids = m.get('Ids')
        if m.get('InUse') is not None:
            self.in_use = m.get('InUse')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class UpdateAutomateResponseConfigStatusResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
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
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateAutomateResponseConfigStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateAutomateResponseConfigStatusResponseBody = None,
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
            temp_model = UpdateAutomateResponseConfigStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateWhiteRuleListRequest(TeaModel):
    def __init__(
        self,
        expression: str = None,
        incident_uuid: str = None,
        region_id: str = None,
        white_rule_id: int = None,
    ):
        self.expression = expression
        self.incident_uuid = incident_uuid
        self.region_id = region_id
        self.white_rule_id = white_rule_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expression is not None:
            result['Expression'] = self.expression
        if self.incident_uuid is not None:
            result['IncidentUuid'] = self.incident_uuid
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.white_rule_id is not None:
            result['WhiteRuleId'] = self.white_rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Expression') is not None:
            self.expression = m.get('Expression')
        if m.get('IncidentUuid') is not None:
            self.incident_uuid = m.get('IncidentUuid')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('WhiteRuleId') is not None:
            self.white_rule_id = m.get('WhiteRuleId')
        return self


class UpdateWhiteRuleListResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: Any = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
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
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateWhiteRuleListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateWhiteRuleListResponseBody = None,
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
            temp_model = UpdateWhiteRuleListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


