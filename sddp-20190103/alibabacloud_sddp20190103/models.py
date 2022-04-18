# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class CreateConfigRequest(TeaModel):
    def __init__(
        self,
        code: str = None,
        description: str = None,
        lang: str = None,
        value: str = None,
    ):
        self.code = code
        self.description = description
        self.lang = lang
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.description is not None:
            result['Description'] = self.description
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateConfigResponseBody(TeaModel):
    def __init__(
        self,
        id: int = None,
        request_id: str = None,
    ):
        self.id = id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateConfigResponseBody = None,
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
            temp_model = CreateConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDataLimitRequest(TeaModel):
    def __init__(
        self,
        audit_status: int = None,
        auto_scan: int = None,
        engine_type: str = None,
        event_status: int = None,
        lang: str = None,
        log_store_day: int = None,
        ocr_status: int = None,
        parent_id: str = None,
        password: str = None,
        port: int = None,
        resource_type: int = None,
        service_region_id: str = None,
        user_name: str = None,
    ):
        self.audit_status = audit_status
        self.auto_scan = auto_scan
        self.engine_type = engine_type
        self.event_status = event_status
        self.lang = lang
        self.log_store_day = log_store_day
        self.ocr_status = ocr_status
        self.parent_id = parent_id
        self.password = password
        self.port = port
        self.resource_type = resource_type
        self.service_region_id = service_region_id
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audit_status is not None:
            result['AuditStatus'] = self.audit_status
        if self.auto_scan is not None:
            result['AutoScan'] = self.auto_scan
        if self.engine_type is not None:
            result['EngineType'] = self.engine_type
        if self.event_status is not None:
            result['EventStatus'] = self.event_status
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.log_store_day is not None:
            result['LogStoreDay'] = self.log_store_day
        if self.ocr_status is not None:
            result['OcrStatus'] = self.ocr_status
        if self.parent_id is not None:
            result['ParentId'] = self.parent_id
        if self.password is not None:
            result['Password'] = self.password
        if self.port is not None:
            result['Port'] = self.port
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.service_region_id is not None:
            result['ServiceRegionId'] = self.service_region_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuditStatus') is not None:
            self.audit_status = m.get('AuditStatus')
        if m.get('AutoScan') is not None:
            self.auto_scan = m.get('AutoScan')
        if m.get('EngineType') is not None:
            self.engine_type = m.get('EngineType')
        if m.get('EventStatus') is not None:
            self.event_status = m.get('EventStatus')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('LogStoreDay') is not None:
            self.log_store_day = m.get('LogStoreDay')
        if m.get('OcrStatus') is not None:
            self.ocr_status = m.get('OcrStatus')
        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ServiceRegionId') is not None:
            self.service_region_id = m.get('ServiceRegionId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class CreateDataLimitResponseBody(TeaModel):
    def __init__(
        self,
        id: int = None,
        request_id: str = None,
    ):
        self.id = id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateDataLimitResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateDataLimitResponseBody = None,
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
            temp_model = CreateDataLimitResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRuleRequest(TeaModel):
    def __init__(
        self,
        category: int = None,
        content: str = None,
        content_category: int = None,
        description: str = None,
        lang: str = None,
        name: str = None,
        product_code: str = None,
        product_id: int = None,
        risk_level_id: int = None,
        rule_type: int = None,
        stat_express: str = None,
        status: int = None,
        target: str = None,
        warn_level: int = None,
    ):
        self.category = category
        self.content = content
        self.content_category = content_category
        self.description = description
        self.lang = lang
        self.name = name
        self.product_code = product_code
        self.product_id = product_id
        self.risk_level_id = risk_level_id
        self.rule_type = rule_type
        self.stat_express = stat_express
        self.status = status
        self.target = target
        self.warn_level = warn_level

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.content is not None:
            result['Content'] = self.content
        if self.content_category is not None:
            result['ContentCategory'] = self.content_category
        if self.description is not None:
            result['Description'] = self.description
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.name is not None:
            result['Name'] = self.name
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.risk_level_id is not None:
            result['RiskLevelId'] = self.risk_level_id
        if self.rule_type is not None:
            result['RuleType'] = self.rule_type
        if self.stat_express is not None:
            result['StatExpress'] = self.stat_express
        if self.status is not None:
            result['Status'] = self.status
        if self.target is not None:
            result['Target'] = self.target
        if self.warn_level is not None:
            result['WarnLevel'] = self.warn_level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('ContentCategory') is not None:
            self.content_category = m.get('ContentCategory')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('RiskLevelId') is not None:
            self.risk_level_id = m.get('RiskLevelId')
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        if m.get('StatExpress') is not None:
            self.stat_express = m.get('StatExpress')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Target') is not None:
            self.target = m.get('Target')
        if m.get('WarnLevel') is not None:
            self.warn_level = m.get('WarnLevel')
        return self


class CreateRuleResponseBody(TeaModel):
    def __init__(
        self,
        id: int = None,
        request_id: str = None,
    ):
        self.id = id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateRuleResponseBody = None,
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
            temp_model = CreateRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateScanTaskRequest(TeaModel):
    def __init__(
        self,
        data_limit_id: int = None,
        interval_day: int = None,
        lang: str = None,
        oss_scan_path: str = None,
        resource_type: int = None,
        run_hour: int = None,
        run_minute: int = None,
        scan_range: int = None,
        scan_range_content: str = None,
        task_name: str = None,
        task_user_name: str = None,
    ):
        self.data_limit_id = data_limit_id
        self.interval_day = interval_day
        self.lang = lang
        self.oss_scan_path = oss_scan_path
        self.resource_type = resource_type
        self.run_hour = run_hour
        self.run_minute = run_minute
        self.scan_range = scan_range
        self.scan_range_content = scan_range_content
        self.task_name = task_name
        self.task_user_name = task_user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_limit_id is not None:
            result['DataLimitId'] = self.data_limit_id
        if self.interval_day is not None:
            result['IntervalDay'] = self.interval_day
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.oss_scan_path is not None:
            result['OssScanPath'] = self.oss_scan_path
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.run_hour is not None:
            result['RunHour'] = self.run_hour
        if self.run_minute is not None:
            result['RunMinute'] = self.run_minute
        if self.scan_range is not None:
            result['ScanRange'] = self.scan_range
        if self.scan_range_content is not None:
            result['ScanRangeContent'] = self.scan_range_content
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.task_user_name is not None:
            result['TaskUserName'] = self.task_user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataLimitId') is not None:
            self.data_limit_id = m.get('DataLimitId')
        if m.get('IntervalDay') is not None:
            self.interval_day = m.get('IntervalDay')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('OssScanPath') is not None:
            self.oss_scan_path = m.get('OssScanPath')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('RunHour') is not None:
            self.run_hour = m.get('RunHour')
        if m.get('RunMinute') is not None:
            self.run_minute = m.get('RunMinute')
        if m.get('ScanRange') is not None:
            self.scan_range = m.get('ScanRange')
        if m.get('ScanRangeContent') is not None:
            self.scan_range_content = m.get('ScanRangeContent')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('TaskUserName') is not None:
            self.task_user_name = m.get('TaskUserName')
        return self


class CreateScanTaskResponseBody(TeaModel):
    def __init__(
        self,
        id: int = None,
        request_id: str = None,
    ):
        self.id = id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateScanTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateScanTaskResponseBody = None,
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
            temp_model = CreateScanTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSlrRoleRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
    ):
        self.lang = lang

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        return self


class CreateSlrRoleResponseBody(TeaModel):
    def __init__(
        self,
        has_permission: bool = None,
        request_id: str = None,
    ):
        self.has_permission = has_permission
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.has_permission is not None:
            result['HasPermission'] = self.has_permission
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HasPermission') is not None:
            self.has_permission = m.get('HasPermission')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateSlrRoleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateSlrRoleResponseBody = None,
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
            temp_model = CreateSlrRoleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDataLimitRequest(TeaModel):
    def __init__(
        self,
        id: int = None,
        lang: str = None,
    ):
        self.id = id
        self.lang = lang

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.lang is not None:
            result['Lang'] = self.lang
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        return self


class DeleteDataLimitResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteDataLimitResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteDataLimitResponseBody = None,
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
            temp_model = DeleteDataLimitResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteRuleRequest(TeaModel):
    def __init__(
        self,
        id: int = None,
        lang: str = None,
    ):
        self.id = id
        self.lang = lang

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.lang is not None:
            result['Lang'] = self.lang
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        return self


class DeleteRuleResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteRuleResponseBody = None,
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
            temp_model = DeleteRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCategoryTemplateRuleListRequest(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        lang: str = None,
        page_size: int = None,
        risk_level_id: int = None,
        status: int = None,
    ):
        self.current_page = current_page
        self.lang = lang
        self.page_size = page_size
        self.risk_level_id = risk_level_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.risk_level_id is not None:
            result['RiskLevelId'] = self.risk_level_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RiskLevelId') is not None:
            self.risk_level_id = m.get('RiskLevelId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeCategoryTemplateRuleListResponseBodyItems(TeaModel):
    def __init__(
        self,
        description: str = None,
        id: int = None,
        identification_rule_ids: str = None,
        identification_scope: str = None,
        name: str = None,
        risk_level_id: int = None,
        status: int = None,
    ):
        self.description = description
        self.id = id
        self.identification_rule_ids = identification_rule_ids
        self.identification_scope = identification_scope
        self.name = name
        self.risk_level_id = risk_level_id
        self.status = status

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
        if self.identification_rule_ids is not None:
            result['IdentificationRuleIds'] = self.identification_rule_ids
        if self.identification_scope is not None:
            result['IdentificationScope'] = self.identification_scope
        if self.name is not None:
            result['Name'] = self.name
        if self.risk_level_id is not None:
            result['RiskLevelId'] = self.risk_level_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdentificationRuleIds') is not None:
            self.identification_rule_ids = m.get('IdentificationRuleIds')
        if m.get('IdentificationScope') is not None:
            self.identification_scope = m.get('IdentificationScope')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RiskLevelId') is not None:
            self.risk_level_id = m.get('RiskLevelId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeCategoryTemplateRuleListResponseBody(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        items: List[DescribeCategoryTemplateRuleListResponseBodyItems] = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.current_page = current_page
        self.items = items
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

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
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = DescribeCategoryTemplateRuleListResponseBodyItems()
                self.items.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeCategoryTemplateRuleListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeCategoryTemplateRuleListResponseBody = None,
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
            temp_model = DescribeCategoryTemplateRuleListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeColumnsRequest(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        instance_id: int = None,
        instance_name: str = None,
        lang: str = None,
        name: str = None,
        page_size: int = None,
        product_code: str = None,
        risk_level_id: int = None,
        rule_id: int = None,
        rule_name: str = None,
        sens_level_name: str = None,
        table_id: int = None,
        table_name: str = None,
    ):
        self.current_page = current_page
        self.instance_id = instance_id
        self.instance_name = instance_name
        self.lang = lang
        self.name = name
        self.page_size = page_size
        self.product_code = product_code
        self.risk_level_id = risk_level_id
        self.rule_id = rule_id
        self.rule_name = rule_name
        self.sens_level_name = sens_level_name
        self.table_id = table_id
        self.table_name = table_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.name is not None:
            result['Name'] = self.name
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.risk_level_id is not None:
            result['RiskLevelId'] = self.risk_level_id
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.sens_level_name is not None:
            result['SensLevelName'] = self.sens_level_name
        if self.table_id is not None:
            result['TableId'] = self.table_id
        if self.table_name is not None:
            result['TableName'] = self.table_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('RiskLevelId') is not None:
            self.risk_level_id = m.get('RiskLevelId')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('SensLevelName') is not None:
            self.sens_level_name = m.get('SensLevelName')
        if m.get('TableId') is not None:
            self.table_id = m.get('TableId')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        return self


class DescribeColumnsResponseBodyItems(TeaModel):
    def __init__(
        self,
        creation_time: int = None,
        data_type: str = None,
        id: str = None,
        instance_id: int = None,
        instance_name: str = None,
        name: str = None,
        odps_risk_level_name: str = None,
        odps_risk_level_value: int = None,
        product_code: str = None,
        revision_id: int = None,
        revision_status: int = None,
        risk_level_id: int = None,
        risk_level_name: str = None,
        rule_id: int = None,
        rule_name: str = None,
        sens_level_name: str = None,
        sensitive: bool = None,
        table_id: int = None,
        table_name: str = None,
    ):
        self.creation_time = creation_time
        self.data_type = data_type
        self.id = id
        self.instance_id = instance_id
        self.instance_name = instance_name
        self.name = name
        self.odps_risk_level_name = odps_risk_level_name
        self.odps_risk_level_value = odps_risk_level_value
        self.product_code = product_code
        self.revision_id = revision_id
        self.revision_status = revision_status
        self.risk_level_id = risk_level_id
        self.risk_level_name = risk_level_name
        self.rule_id = rule_id
        self.rule_name = rule_name
        self.sens_level_name = sens_level_name
        self.sensitive = sensitive
        self.table_id = table_id
        self.table_name = table_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.data_type is not None:
            result['DataType'] = self.data_type
        if self.id is not None:
            result['Id'] = self.id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.name is not None:
            result['Name'] = self.name
        if self.odps_risk_level_name is not None:
            result['OdpsRiskLevelName'] = self.odps_risk_level_name
        if self.odps_risk_level_value is not None:
            result['OdpsRiskLevelValue'] = self.odps_risk_level_value
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.revision_id is not None:
            result['RevisionId'] = self.revision_id
        if self.revision_status is not None:
            result['RevisionStatus'] = self.revision_status
        if self.risk_level_id is not None:
            result['RiskLevelId'] = self.risk_level_id
        if self.risk_level_name is not None:
            result['RiskLevelName'] = self.risk_level_name
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.sens_level_name is not None:
            result['SensLevelName'] = self.sens_level_name
        if self.sensitive is not None:
            result['Sensitive'] = self.sensitive
        if self.table_id is not None:
            result['TableId'] = self.table_id
        if self.table_name is not None:
            result['TableName'] = self.table_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OdpsRiskLevelName') is not None:
            self.odps_risk_level_name = m.get('OdpsRiskLevelName')
        if m.get('OdpsRiskLevelValue') is not None:
            self.odps_risk_level_value = m.get('OdpsRiskLevelValue')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('RevisionId') is not None:
            self.revision_id = m.get('RevisionId')
        if m.get('RevisionStatus') is not None:
            self.revision_status = m.get('RevisionStatus')
        if m.get('RiskLevelId') is not None:
            self.risk_level_id = m.get('RiskLevelId')
        if m.get('RiskLevelName') is not None:
            self.risk_level_name = m.get('RiskLevelName')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('SensLevelName') is not None:
            self.sens_level_name = m.get('SensLevelName')
        if m.get('Sensitive') is not None:
            self.sensitive = m.get('Sensitive')
        if m.get('TableId') is not None:
            self.table_id = m.get('TableId')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        return self


class DescribeColumnsResponseBody(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        items: List[DescribeColumnsResponseBodyItems] = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.current_page = current_page
        self.items = items
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

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
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = DescribeColumnsResponseBodyItems()
                self.items.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeColumnsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeColumnsResponseBody = None,
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
            temp_model = DescribeColumnsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeConfigsRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
    ):
        self.lang = lang

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        return self


class DescribeConfigsResponseBodyConfigList(TeaModel):
    def __init__(
        self,
        code: str = None,
        default_value: str = None,
        description: str = None,
        id: int = None,
        value: str = None,
    ):
        self.code = code
        self.default_value = default_value
        self.description = description
        self.id = id
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.default_value is not None:
            result['DefaultValue'] = self.default_value
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DefaultValue') is not None:
            self.default_value = m.get('DefaultValue')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeConfigsResponseBody(TeaModel):
    def __init__(
        self,
        config_list: List[DescribeConfigsResponseBodyConfigList] = None,
        request_id: str = None,
    ):
        self.config_list = config_list
        self.request_id = request_id

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
        result['ConfigList'] = []
        if self.config_list is not None:
            for k in self.config_list:
                result['ConfigList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.config_list = []
        if m.get('ConfigList') is not None:
            for k in m.get('ConfigList'):
                temp_model = DescribeConfigsResponseBodyConfigList()
                self.config_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeConfigsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeConfigsResponseBody = None,
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
            temp_model = DescribeConfigsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDataAssetsRequest(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        lang: str = None,
        name: str = None,
        page_size: int = None,
        range_id: int = None,
        risk_levels: str = None,
        rule_id: int = None,
    ):
        self.current_page = current_page
        self.lang = lang
        self.name = name
        self.page_size = page_size
        self.range_id = range_id
        self.risk_levels = risk_levels
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.name is not None:
            result['Name'] = self.name
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.range_id is not None:
            result['RangeId'] = self.range_id
        if self.risk_levels is not None:
            result['RiskLevels'] = self.risk_levels
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RangeId') is not None:
            self.range_id = m.get('RangeId')
        if m.get('RiskLevels') is not None:
            self.risk_levels = m.get('RiskLevels')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class DescribeDataAssetsResponseBodyItems(TeaModel):
    def __init__(
        self,
        acl: str = None,
        creation_time: int = None,
        data_type: str = None,
        id: str = None,
        labelsec: bool = None,
        name: str = None,
        object_key: str = None,
        odps_risk_level_name: str = None,
        owner: str = None,
        product_code: str = None,
        product_id: str = None,
        protection: bool = None,
        risk_level_id: int = None,
        risk_level_name: str = None,
        rule_name: str = None,
        sensitive: bool = None,
        sensitive_count: int = None,
        sensitive_ratio: str = None,
        total_count: int = None,
    ):
        self.acl = acl
        self.creation_time = creation_time
        self.data_type = data_type
        self.id = id
        self.labelsec = labelsec
        self.name = name
        self.object_key = object_key
        self.odps_risk_level_name = odps_risk_level_name
        self.owner = owner
        self.product_code = product_code
        self.product_id = product_id
        self.protection = protection
        self.risk_level_id = risk_level_id
        self.risk_level_name = risk_level_name
        self.rule_name = rule_name
        self.sensitive = sensitive
        self.sensitive_count = sensitive_count
        self.sensitive_ratio = sensitive_ratio
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl is not None:
            result['Acl'] = self.acl
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.data_type is not None:
            result['DataType'] = self.data_type
        if self.id is not None:
            result['Id'] = self.id
        if self.labelsec is not None:
            result['Labelsec'] = self.labelsec
        if self.name is not None:
            result['Name'] = self.name
        if self.object_key is not None:
            result['ObjectKey'] = self.object_key
        if self.odps_risk_level_name is not None:
            result['OdpsRiskLevelName'] = self.odps_risk_level_name
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.protection is not None:
            result['Protection'] = self.protection
        if self.risk_level_id is not None:
            result['RiskLevelId'] = self.risk_level_id
        if self.risk_level_name is not None:
            result['RiskLevelName'] = self.risk_level_name
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.sensitive is not None:
            result['Sensitive'] = self.sensitive
        if self.sensitive_count is not None:
            result['SensitiveCount'] = self.sensitive_count
        if self.sensitive_ratio is not None:
            result['SensitiveRatio'] = self.sensitive_ratio
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Acl') is not None:
            self.acl = m.get('Acl')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Labelsec') is not None:
            self.labelsec = m.get('Labelsec')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ObjectKey') is not None:
            self.object_key = m.get('ObjectKey')
        if m.get('OdpsRiskLevelName') is not None:
            self.odps_risk_level_name = m.get('OdpsRiskLevelName')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('Protection') is not None:
            self.protection = m.get('Protection')
        if m.get('RiskLevelId') is not None:
            self.risk_level_id = m.get('RiskLevelId')
        if m.get('RiskLevelName') is not None:
            self.risk_level_name = m.get('RiskLevelName')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('Sensitive') is not None:
            self.sensitive = m.get('Sensitive')
        if m.get('SensitiveCount') is not None:
            self.sensitive_count = m.get('SensitiveCount')
        if m.get('SensitiveRatio') is not None:
            self.sensitive_ratio = m.get('SensitiveRatio')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeDataAssetsResponseBody(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        items: List[DescribeDataAssetsResponseBodyItems] = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.current_page = current_page
        self.items = items
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

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
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = DescribeDataAssetsResponseBodyItems()
                self.items.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeDataAssetsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDataAssetsResponseBody = None,
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
            temp_model = DescribeDataAssetsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDataLimitDetailRequest(TeaModel):
    def __init__(
        self,
        id: int = None,
        lang: str = None,
        network_type: int = None,
    ):
        self.id = id
        self.lang = lang
        self.network_type = network_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
        return self


class DescribeDataLimitDetailResponseBodyDataLimit(TeaModel):
    def __init__(
        self,
        check_status: int = None,
        check_status_name: str = None,
        gmt_create: int = None,
        id: int = None,
        local_name: str = None,
        parent_id: str = None,
        port: int = None,
        region_id: str = None,
        resource_type: int = None,
        resource_type_code: str = None,
        user_name: str = None,
    ):
        self.check_status = check_status
        self.check_status_name = check_status_name
        self.gmt_create = gmt_create
        self.id = id
        self.local_name = local_name
        self.parent_id = parent_id
        self.port = port
        self.region_id = region_id
        self.resource_type = resource_type
        self.resource_type_code = resource_type_code
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_status is not None:
            result['CheckStatus'] = self.check_status
        if self.check_status_name is not None:
            result['CheckStatusName'] = self.check_status_name
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.id is not None:
            result['Id'] = self.id
        if self.local_name is not None:
            result['LocalName'] = self.local_name
        if self.parent_id is not None:
            result['ParentId'] = self.parent_id
        if self.port is not None:
            result['Port'] = self.port
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.resource_type_code is not None:
            result['ResourceTypeCode'] = self.resource_type_code
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckStatus') is not None:
            self.check_status = m.get('CheckStatus')
        if m.get('CheckStatusName') is not None:
            self.check_status_name = m.get('CheckStatusName')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')
        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ResourceTypeCode') is not None:
            self.resource_type_code = m.get('ResourceTypeCode')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class DescribeDataLimitDetailResponseBody(TeaModel):
    def __init__(
        self,
        data_limit: DescribeDataLimitDetailResponseBodyDataLimit = None,
        request_id: str = None,
    ):
        self.data_limit = data_limit
        self.request_id = request_id

    def validate(self):
        if self.data_limit:
            self.data_limit.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_limit is not None:
            result['DataLimit'] = self.data_limit.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataLimit') is not None:
            temp_model = DescribeDataLimitDetailResponseBodyDataLimit()
            self.data_limit = temp_model.from_map(m['DataLimit'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDataLimitDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDataLimitDetailResponseBody = None,
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
            temp_model = DescribeDataLimitDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDataLimitSetRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        parent_id: str = None,
        resource_type: int = None,
    ):
        self.lang = lang
        self.parent_id = parent_id
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.parent_id is not None:
            result['ParentId'] = self.parent_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class DescribeDataLimitSetResponseBodyDataLimitSetDataLimitList(TeaModel):
    def __init__(
        self,
        check_status: int = None,
        check_status_name: str = None,
        connector: str = None,
        gmt_create: int = None,
        id: int = None,
        local_name: str = None,
        parent_id: str = None,
        region_id: str = None,
        resource_type: int = None,
        resource_type_code: str = None,
        user_name: str = None,
    ):
        self.check_status = check_status
        self.check_status_name = check_status_name
        self.connector = connector
        self.gmt_create = gmt_create
        self.id = id
        self.local_name = local_name
        self.parent_id = parent_id
        self.region_id = region_id
        self.resource_type = resource_type
        self.resource_type_code = resource_type_code
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_status is not None:
            result['CheckStatus'] = self.check_status
        if self.check_status_name is not None:
            result['CheckStatusName'] = self.check_status_name
        if self.connector is not None:
            result['Connector'] = self.connector
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.id is not None:
            result['Id'] = self.id
        if self.local_name is not None:
            result['LocalName'] = self.local_name
        if self.parent_id is not None:
            result['ParentId'] = self.parent_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.resource_type_code is not None:
            result['ResourceTypeCode'] = self.resource_type_code
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckStatus') is not None:
            self.check_status = m.get('CheckStatus')
        if m.get('CheckStatusName') is not None:
            self.check_status_name = m.get('CheckStatusName')
        if m.get('Connector') is not None:
            self.connector = m.get('Connector')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')
        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ResourceTypeCode') is not None:
            self.resource_type_code = m.get('ResourceTypeCode')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class DescribeDataLimitSetResponseBodyDataLimitSetOssBucketList(TeaModel):
    def __init__(
        self,
        bucket_name: str = None,
        region_id: str = None,
    ):
        self.bucket_name = bucket_name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeDataLimitSetResponseBodyDataLimitSetRegionList(TeaModel):
    def __init__(
        self,
        local_name: str = None,
        region_id: str = None,
    ):
        self.local_name = local_name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.local_name is not None:
            result['LocalName'] = self.local_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeDataLimitSetResponseBodyDataLimitSet(TeaModel):
    def __init__(
        self,
        data_limit_list: List[DescribeDataLimitSetResponseBodyDataLimitSetDataLimitList] = None,
        oss_bucket_list: List[DescribeDataLimitSetResponseBodyDataLimitSetOssBucketList] = None,
        region_list: List[DescribeDataLimitSetResponseBodyDataLimitSetRegionList] = None,
        resource_type: int = None,
        resource_type_code: str = None,
        total_count: int = None,
    ):
        self.data_limit_list = data_limit_list
        self.oss_bucket_list = oss_bucket_list
        self.region_list = region_list
        self.resource_type = resource_type
        self.resource_type_code = resource_type_code
        self.total_count = total_count

    def validate(self):
        if self.data_limit_list:
            for k in self.data_limit_list:
                if k:
                    k.validate()
        if self.oss_bucket_list:
            for k in self.oss_bucket_list:
                if k:
                    k.validate()
        if self.region_list:
            for k in self.region_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataLimitList'] = []
        if self.data_limit_list is not None:
            for k in self.data_limit_list:
                result['DataLimitList'].append(k.to_map() if k else None)
        result['OssBucketList'] = []
        if self.oss_bucket_list is not None:
            for k in self.oss_bucket_list:
                result['OssBucketList'].append(k.to_map() if k else None)
        result['RegionList'] = []
        if self.region_list is not None:
            for k in self.region_list:
                result['RegionList'].append(k.to_map() if k else None)
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.resource_type_code is not None:
            result['ResourceTypeCode'] = self.resource_type_code
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_limit_list = []
        if m.get('DataLimitList') is not None:
            for k in m.get('DataLimitList'):
                temp_model = DescribeDataLimitSetResponseBodyDataLimitSetDataLimitList()
                self.data_limit_list.append(temp_model.from_map(k))
        self.oss_bucket_list = []
        if m.get('OssBucketList') is not None:
            for k in m.get('OssBucketList'):
                temp_model = DescribeDataLimitSetResponseBodyDataLimitSetOssBucketList()
                self.oss_bucket_list.append(temp_model.from_map(k))
        self.region_list = []
        if m.get('RegionList') is not None:
            for k in m.get('RegionList'):
                temp_model = DescribeDataLimitSetResponseBodyDataLimitSetRegionList()
                self.region_list.append(temp_model.from_map(k))
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ResourceTypeCode') is not None:
            self.resource_type_code = m.get('ResourceTypeCode')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeDataLimitSetResponseBody(TeaModel):
    def __init__(
        self,
        data_limit_set: DescribeDataLimitSetResponseBodyDataLimitSet = None,
        request_id: str = None,
    ):
        self.data_limit_set = data_limit_set
        self.request_id = request_id

    def validate(self):
        if self.data_limit_set:
            self.data_limit_set.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_limit_set is not None:
            result['DataLimitSet'] = self.data_limit_set.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataLimitSet') is not None:
            temp_model = DescribeDataLimitSetResponseBodyDataLimitSet()
            self.data_limit_set = temp_model.from_map(m['DataLimitSet'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDataLimitSetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDataLimitSetResponseBody = None,
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
            temp_model = DescribeDataLimitSetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDataLimitsRequest(TeaModel):
    def __init__(
        self,
        audit_status: int = None,
        check_status: int = None,
        current_page: int = None,
        datamask_status: int = None,
        enable: int = None,
        end_time: int = None,
        engine_type: str = None,
        lang: str = None,
        page_size: int = None,
        parent_id: str = None,
        resource_type: int = None,
        service_region_id: str = None,
        start_time: int = None,
    ):
        self.audit_status = audit_status
        self.check_status = check_status
        self.current_page = current_page
        self.datamask_status = datamask_status
        self.enable = enable
        self.end_time = end_time
        self.engine_type = engine_type
        self.lang = lang
        self.page_size = page_size
        self.parent_id = parent_id
        self.resource_type = resource_type
        self.service_region_id = service_region_id
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audit_status is not None:
            result['AuditStatus'] = self.audit_status
        if self.check_status is not None:
            result['CheckStatus'] = self.check_status
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.datamask_status is not None:
            result['DatamaskStatus'] = self.datamask_status
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.engine_type is not None:
            result['EngineType'] = self.engine_type
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.parent_id is not None:
            result['ParentId'] = self.parent_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.service_region_id is not None:
            result['ServiceRegionId'] = self.service_region_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuditStatus') is not None:
            self.audit_status = m.get('AuditStatus')
        if m.get('CheckStatus') is not None:
            self.check_status = m.get('CheckStatus')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('DatamaskStatus') is not None:
            self.datamask_status = m.get('DatamaskStatus')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('EngineType') is not None:
            self.engine_type = m.get('EngineType')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ServiceRegionId') is not None:
            self.service_region_id = m.get('ServiceRegionId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDataLimitsResponseBodyItems(TeaModel):
    def __init__(
        self,
        audit_status: int = None,
        auto_scan: int = None,
        check_status: int = None,
        check_status_name: str = None,
        datamask_status: int = None,
        db_version: str = None,
        enable: int = None,
        engine_type: str = None,
        error_code: str = None,
        error_message: str = None,
        event_status: int = None,
        gmt_create: int = None,
        id: int = None,
        instance_description: str = None,
        instance_id: str = None,
        last_finished_time: int = None,
        local_name: str = None,
        log_store_day: int = None,
        next_start_time: int = None,
        ocr_status: int = None,
        parent_id: str = None,
        port: int = None,
        process_status: int = None,
        process_total_count: int = None,
        region_id: str = None,
        resource_type: int = None,
        resource_type_code: str = None,
        sampling_size: int = None,
        support_audit: bool = None,
        support_datamask: bool = None,
        support_event: bool = None,
        support_ocr: bool = None,
        support_scan: bool = None,
        tenant_name: str = None,
        total_count: int = None,
        user_name: str = None,
    ):
        self.audit_status = audit_status
        self.auto_scan = auto_scan
        self.check_status = check_status
        self.check_status_name = check_status_name
        self.datamask_status = datamask_status
        self.db_version = db_version
        self.enable = enable
        self.engine_type = engine_type
        self.error_code = error_code
        self.error_message = error_message
        self.event_status = event_status
        self.gmt_create = gmt_create
        self.id = id
        self.instance_description = instance_description
        self.instance_id = instance_id
        self.last_finished_time = last_finished_time
        self.local_name = local_name
        self.log_store_day = log_store_day
        self.next_start_time = next_start_time
        self.ocr_status = ocr_status
        self.parent_id = parent_id
        self.port = port
        self.process_status = process_status
        self.process_total_count = process_total_count
        self.region_id = region_id
        self.resource_type = resource_type
        self.resource_type_code = resource_type_code
        self.sampling_size = sampling_size
        self.support_audit = support_audit
        self.support_datamask = support_datamask
        self.support_event = support_event
        self.support_ocr = support_ocr
        self.support_scan = support_scan
        self.tenant_name = tenant_name
        self.total_count = total_count
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audit_status is not None:
            result['AuditStatus'] = self.audit_status
        if self.auto_scan is not None:
            result['AutoScan'] = self.auto_scan
        if self.check_status is not None:
            result['CheckStatus'] = self.check_status
        if self.check_status_name is not None:
            result['CheckStatusName'] = self.check_status_name
        if self.datamask_status is not None:
            result['DatamaskStatus'] = self.datamask_status
        if self.db_version is not None:
            result['DbVersion'] = self.db_version
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.engine_type is not None:
            result['EngineType'] = self.engine_type
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.event_status is not None:
            result['EventStatus'] = self.event_status
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.id is not None:
            result['Id'] = self.id
        if self.instance_description is not None:
            result['InstanceDescription'] = self.instance_description
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.last_finished_time is not None:
            result['LastFinishedTime'] = self.last_finished_time
        if self.local_name is not None:
            result['LocalName'] = self.local_name
        if self.log_store_day is not None:
            result['LogStoreDay'] = self.log_store_day
        if self.next_start_time is not None:
            result['NextStartTime'] = self.next_start_time
        if self.ocr_status is not None:
            result['OcrStatus'] = self.ocr_status
        if self.parent_id is not None:
            result['ParentId'] = self.parent_id
        if self.port is not None:
            result['Port'] = self.port
        if self.process_status is not None:
            result['ProcessStatus'] = self.process_status
        if self.process_total_count is not None:
            result['ProcessTotalCount'] = self.process_total_count
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.resource_type_code is not None:
            result['ResourceTypeCode'] = self.resource_type_code
        if self.sampling_size is not None:
            result['SamplingSize'] = self.sampling_size
        if self.support_audit is not None:
            result['SupportAudit'] = self.support_audit
        if self.support_datamask is not None:
            result['SupportDatamask'] = self.support_datamask
        if self.support_event is not None:
            result['SupportEvent'] = self.support_event
        if self.support_ocr is not None:
            result['SupportOcr'] = self.support_ocr
        if self.support_scan is not None:
            result['SupportScan'] = self.support_scan
        if self.tenant_name is not None:
            result['TenantName'] = self.tenant_name
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuditStatus') is not None:
            self.audit_status = m.get('AuditStatus')
        if m.get('AutoScan') is not None:
            self.auto_scan = m.get('AutoScan')
        if m.get('CheckStatus') is not None:
            self.check_status = m.get('CheckStatus')
        if m.get('CheckStatusName') is not None:
            self.check_status_name = m.get('CheckStatusName')
        if m.get('DatamaskStatus') is not None:
            self.datamask_status = m.get('DatamaskStatus')
        if m.get('DbVersion') is not None:
            self.db_version = m.get('DbVersion')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('EngineType') is not None:
            self.engine_type = m.get('EngineType')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('EventStatus') is not None:
            self.event_status = m.get('EventStatus')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InstanceDescription') is not None:
            self.instance_description = m.get('InstanceDescription')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('LastFinishedTime') is not None:
            self.last_finished_time = m.get('LastFinishedTime')
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')
        if m.get('LogStoreDay') is not None:
            self.log_store_day = m.get('LogStoreDay')
        if m.get('NextStartTime') is not None:
            self.next_start_time = m.get('NextStartTime')
        if m.get('OcrStatus') is not None:
            self.ocr_status = m.get('OcrStatus')
        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('ProcessStatus') is not None:
            self.process_status = m.get('ProcessStatus')
        if m.get('ProcessTotalCount') is not None:
            self.process_total_count = m.get('ProcessTotalCount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ResourceTypeCode') is not None:
            self.resource_type_code = m.get('ResourceTypeCode')
        if m.get('SamplingSize') is not None:
            self.sampling_size = m.get('SamplingSize')
        if m.get('SupportAudit') is not None:
            self.support_audit = m.get('SupportAudit')
        if m.get('SupportDatamask') is not None:
            self.support_datamask = m.get('SupportDatamask')
        if m.get('SupportEvent') is not None:
            self.support_event = m.get('SupportEvent')
        if m.get('SupportOcr') is not None:
            self.support_ocr = m.get('SupportOcr')
        if m.get('SupportScan') is not None:
            self.support_scan = m.get('SupportScan')
        if m.get('TenantName') is not None:
            self.tenant_name = m.get('TenantName')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class DescribeDataLimitsResponseBody(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        items: List[DescribeDataLimitsResponseBodyItems] = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.current_page = current_page
        self.items = items
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

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
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = DescribeDataLimitsResponseBodyItems()
                self.items.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeDataLimitsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDataLimitsResponseBody = None,
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
            temp_model = DescribeDataLimitsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDataMaskingRunHistoryRequest(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        dst_type: int = None,
        end_time: int = None,
        lang: str = None,
        main_process_id: int = None,
        page_size: int = None,
        src_table_name: str = None,
        src_type: int = None,
        start_time: int = None,
        status: int = None,
        task_id: str = None,
    ):
        self.current_page = current_page
        self.dst_type = dst_type
        self.end_time = end_time
        self.lang = lang
        self.main_process_id = main_process_id
        self.page_size = page_size
        self.src_table_name = src_table_name
        self.src_type = src_type
        self.start_time = start_time
        self.status = status
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.dst_type is not None:
            result['DstType'] = self.dst_type
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.main_process_id is not None:
            result['MainProcessId'] = self.main_process_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.src_table_name is not None:
            result['SrcTableName'] = self.src_table_name
        if self.src_type is not None:
            result['SrcType'] = self.src_type
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('DstType') is not None:
            self.dst_type = m.get('DstType')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('MainProcessId') is not None:
            self.main_process_id = m.get('MainProcessId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SrcTableName') is not None:
            self.src_table_name = m.get('SrcTableName')
        if m.get('SrcType') is not None:
            self.src_type = m.get('SrcType')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DescribeDataMaskingRunHistoryResponseBodyItems(TeaModel):
    def __init__(
        self,
        conflict_count: int = None,
        dst_type: int = None,
        dst_type_code: str = None,
        end_time: int = None,
        fail_code: str = None,
        fail_msg: str = None,
        has_download_file: int = None,
        has_sub_process: int = None,
        id: int = None,
        masking_count: int = None,
        percentage: int = None,
        run_index: int = None,
        src_table_name: str = None,
        src_type: int = None,
        src_type_code: str = None,
        start_time: int = None,
        status: int = None,
        task_id: str = None,
        type: int = None,
    ):
        self.conflict_count = conflict_count
        self.dst_type = dst_type
        self.dst_type_code = dst_type_code
        self.end_time = end_time
        self.fail_code = fail_code
        self.fail_msg = fail_msg
        self.has_download_file = has_download_file
        self.has_sub_process = has_sub_process
        self.id = id
        self.masking_count = masking_count
        self.percentage = percentage
        self.run_index = run_index
        self.src_table_name = src_table_name
        self.src_type = src_type
        self.src_type_code = src_type_code
        self.start_time = start_time
        self.status = status
        self.task_id = task_id
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.conflict_count is not None:
            result['ConflictCount'] = self.conflict_count
        if self.dst_type is not None:
            result['DstType'] = self.dst_type
        if self.dst_type_code is not None:
            result['DstTypeCode'] = self.dst_type_code
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.fail_code is not None:
            result['FailCode'] = self.fail_code
        if self.fail_msg is not None:
            result['FailMsg'] = self.fail_msg
        if self.has_download_file is not None:
            result['HasDownloadFile'] = self.has_download_file
        if self.has_sub_process is not None:
            result['HasSubProcess'] = self.has_sub_process
        if self.id is not None:
            result['Id'] = self.id
        if self.masking_count is not None:
            result['MaskingCount'] = self.masking_count
        if self.percentage is not None:
            result['Percentage'] = self.percentage
        if self.run_index is not None:
            result['RunIndex'] = self.run_index
        if self.src_table_name is not None:
            result['SrcTableName'] = self.src_table_name
        if self.src_type is not None:
            result['SrcType'] = self.src_type
        if self.src_type_code is not None:
            result['SrcTypeCode'] = self.src_type_code
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConflictCount') is not None:
            self.conflict_count = m.get('ConflictCount')
        if m.get('DstType') is not None:
            self.dst_type = m.get('DstType')
        if m.get('DstTypeCode') is not None:
            self.dst_type_code = m.get('DstTypeCode')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('FailCode') is not None:
            self.fail_code = m.get('FailCode')
        if m.get('FailMsg') is not None:
            self.fail_msg = m.get('FailMsg')
        if m.get('HasDownloadFile') is not None:
            self.has_download_file = m.get('HasDownloadFile')
        if m.get('HasSubProcess') is not None:
            self.has_sub_process = m.get('HasSubProcess')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('MaskingCount') is not None:
            self.masking_count = m.get('MaskingCount')
        if m.get('Percentage') is not None:
            self.percentage = m.get('Percentage')
        if m.get('RunIndex') is not None:
            self.run_index = m.get('RunIndex')
        if m.get('SrcTableName') is not None:
            self.src_table_name = m.get('SrcTableName')
        if m.get('SrcType') is not None:
            self.src_type = m.get('SrcType')
        if m.get('SrcTypeCode') is not None:
            self.src_type_code = m.get('SrcTypeCode')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeDataMaskingRunHistoryResponseBody(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        items: List[DescribeDataMaskingRunHistoryResponseBodyItems] = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.current_page = current_page
        self.items = items
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

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
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = DescribeDataMaskingRunHistoryResponseBodyItems()
                self.items.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeDataMaskingRunHistoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDataMaskingRunHistoryResponseBody = None,
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
            temp_model = DescribeDataMaskingRunHistoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDataMaskingTasksRequest(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        dst_type: int = None,
        end_time: int = None,
        lang: str = None,
        page_size: int = None,
        search_key: str = None,
        start_time: int = None,
    ):
        self.current_page = current_page
        self.dst_type = dst_type
        self.end_time = end_time
        self.lang = lang
        self.page_size = page_size
        self.search_key = search_key
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
        if self.dst_type is not None:
            result['DstType'] = self.dst_type
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.search_key is not None:
            result['SearchKey'] = self.search_key
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('DstType') is not None:
            self.dst_type = m.get('DstType')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SearchKey') is not None:
            self.search_key = m.get('SearchKey')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDataMaskingTasksResponseBodyItems(TeaModel):
    def __init__(
        self,
        dst_path: str = None,
        dst_type: int = None,
        dst_type_code: str = None,
        gmt_create: int = None,
        has_unfinish_process: bool = None,
        id: int = None,
        original_table: bool = None,
        owner: str = None,
        run_count: int = None,
        src_path: str = None,
        src_type: int = None,
        src_type_code: str = None,
        status: int = None,
        task_id: str = None,
        task_name: str = None,
        trigger_type: int = None,
    ):
        self.dst_path = dst_path
        self.dst_type = dst_type
        self.dst_type_code = dst_type_code
        self.gmt_create = gmt_create
        self.has_unfinish_process = has_unfinish_process
        self.id = id
        self.original_table = original_table
        self.owner = owner
        self.run_count = run_count
        self.src_path = src_path
        self.src_type = src_type
        self.src_type_code = src_type_code
        self.status = status
        self.task_id = task_id
        self.task_name = task_name
        self.trigger_type = trigger_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dst_path is not None:
            result['DstPath'] = self.dst_path
        if self.dst_type is not None:
            result['DstType'] = self.dst_type
        if self.dst_type_code is not None:
            result['DstTypeCode'] = self.dst_type_code
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.has_unfinish_process is not None:
            result['HasUnfinishProcess'] = self.has_unfinish_process
        if self.id is not None:
            result['Id'] = self.id
        if self.original_table is not None:
            result['OriginalTable'] = self.original_table
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.run_count is not None:
            result['RunCount'] = self.run_count
        if self.src_path is not None:
            result['SrcPath'] = self.src_path
        if self.src_type is not None:
            result['SrcType'] = self.src_type
        if self.src_type_code is not None:
            result['SrcTypeCode'] = self.src_type_code
        if self.status is not None:
            result['Status'] = self.status
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.trigger_type is not None:
            result['TriggerType'] = self.trigger_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DstPath') is not None:
            self.dst_path = m.get('DstPath')
        if m.get('DstType') is not None:
            self.dst_type = m.get('DstType')
        if m.get('DstTypeCode') is not None:
            self.dst_type_code = m.get('DstTypeCode')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('HasUnfinishProcess') is not None:
            self.has_unfinish_process = m.get('HasUnfinishProcess')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OriginalTable') is not None:
            self.original_table = m.get('OriginalTable')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('RunCount') is not None:
            self.run_count = m.get('RunCount')
        if m.get('SrcPath') is not None:
            self.src_path = m.get('SrcPath')
        if m.get('SrcType') is not None:
            self.src_type = m.get('SrcType')
        if m.get('SrcTypeCode') is not None:
            self.src_type_code = m.get('SrcTypeCode')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('TriggerType') is not None:
            self.trigger_type = m.get('TriggerType')
        return self


class DescribeDataMaskingTasksResponseBody(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        items: List[DescribeDataMaskingTasksResponseBodyItems] = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.current_page = current_page
        self.items = items
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

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
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = DescribeDataMaskingTasksResponseBodyItems()
                self.items.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeDataMaskingTasksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDataMaskingTasksResponseBody = None,
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
            temp_model = DescribeDataMaskingTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeEventDetailRequest(TeaModel):
    def __init__(
        self,
        id: int = None,
        lang: str = None,
    ):
        self.id = id
        self.lang = lang

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.lang is not None:
            result['Lang'] = self.lang
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        return self


class DescribeEventDetailResponseBodyEventDetailChartData(TeaModel):
    def __init__(
        self,
        x: List[str] = None,
        y: List[str] = None,
    ):
        self.x = x
        self.y = y

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.x is not None:
            result['X'] = self.x
        if self.y is not None:
            result['Y'] = self.y
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('X') is not None:
            self.x = m.get('X')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        return self


class DescribeEventDetailResponseBodyEventDetailChart(TeaModel):
    def __init__(
        self,
        data: DescribeEventDetailResponseBodyEventDetailChartData = None,
        label: str = None,
        type: str = None,
        xlabel: str = None,
        ylabel: str = None,
    ):
        self.data = data
        self.label = label
        self.type = type
        self.xlabel = xlabel
        self.ylabel = ylabel

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
        if self.label is not None:
            result['Label'] = self.label
        if self.type is not None:
            result['Type'] = self.type
        if self.xlabel is not None:
            result['XLabel'] = self.xlabel
        if self.ylabel is not None:
            result['YLabel'] = self.ylabel
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = DescribeEventDetailResponseBodyEventDetailChartData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('XLabel') is not None:
            self.xlabel = m.get('XLabel')
        if m.get('YLabel') is not None:
            self.ylabel = m.get('YLabel')
        return self


class DescribeEventDetailResponseBodyEventDetailContent(TeaModel):
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


class DescribeEventDetailResponseBodyEventDetailResourceInfo(TeaModel):
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


class DescribeEventDetailResponseBodyEventDetail(TeaModel):
    def __init__(
        self,
        chart: List[DescribeEventDetailResponseBodyEventDetailChart] = None,
        content: List[DescribeEventDetailResponseBodyEventDetailContent] = None,
        resource_info: List[DescribeEventDetailResponseBodyEventDetailResourceInfo] = None,
    ):
        self.chart = chart
        self.content = content
        self.resource_info = resource_info

    def validate(self):
        if self.chart:
            for k in self.chart:
                if k:
                    k.validate()
        if self.content:
            for k in self.content:
                if k:
                    k.validate()
        if self.resource_info:
            for k in self.resource_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Chart'] = []
        if self.chart is not None:
            for k in self.chart:
                result['Chart'].append(k.to_map() if k else None)
        result['Content'] = []
        if self.content is not None:
            for k in self.content:
                result['Content'].append(k.to_map() if k else None)
        result['ResourceInfo'] = []
        if self.resource_info is not None:
            for k in self.resource_info:
                result['ResourceInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.chart = []
        if m.get('Chart') is not None:
            for k in m.get('Chart'):
                temp_model = DescribeEventDetailResponseBodyEventDetailChart()
                self.chart.append(temp_model.from_map(k))
        self.content = []
        if m.get('Content') is not None:
            for k in m.get('Content'):
                temp_model = DescribeEventDetailResponseBodyEventDetailContent()
                self.content.append(temp_model.from_map(k))
        self.resource_info = []
        if m.get('ResourceInfo') is not None:
            for k in m.get('ResourceInfo'):
                temp_model = DescribeEventDetailResponseBodyEventDetailResourceInfo()
                self.resource_info.append(temp_model.from_map(k))
        return self


class DescribeEventDetailResponseBodyEventHandleInfoList(TeaModel):
    def __init__(
        self,
        current_value: str = None,
        disable_time: int = None,
        enable_time: int = None,
        handler_name: str = None,
        handler_type: str = None,
        handler_value: int = None,
        id: int = None,
        status: int = None,
    ):
        self.current_value = current_value
        self.disable_time = disable_time
        self.enable_time = enable_time
        self.handler_name = handler_name
        self.handler_type = handler_type
        self.handler_value = handler_value
        self.id = id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_value is not None:
            result['CurrentValue'] = self.current_value
        if self.disable_time is not None:
            result['DisableTime'] = self.disable_time
        if self.enable_time is not None:
            result['EnableTime'] = self.enable_time
        if self.handler_name is not None:
            result['HandlerName'] = self.handler_name
        if self.handler_type is not None:
            result['HandlerType'] = self.handler_type
        if self.handler_value is not None:
            result['HandlerValue'] = self.handler_value
        if self.id is not None:
            result['Id'] = self.id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentValue') is not None:
            self.current_value = m.get('CurrentValue')
        if m.get('DisableTime') is not None:
            self.disable_time = m.get('DisableTime')
        if m.get('EnableTime') is not None:
            self.enable_time = m.get('EnableTime')
        if m.get('HandlerName') is not None:
            self.handler_name = m.get('HandlerName')
        if m.get('HandlerType') is not None:
            self.handler_type = m.get('HandlerType')
        if m.get('HandlerValue') is not None:
            self.handler_value = m.get('HandlerValue')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeEventDetailResponseBodyEvent(TeaModel):
    def __init__(
        self,
        alert_time: int = None,
        backed: bool = None,
        data_instance: str = None,
        deal_display_name: str = None,
        deal_login_name: str = None,
        deal_reason: str = None,
        deal_time: int = None,
        deal_user_id: int = None,
        detail: DescribeEventDetailResponseBodyEventDetail = None,
        display_name: str = None,
        event_time: int = None,
        handle_info_list: List[DescribeEventDetailResponseBodyEventHandleInfoList] = None,
        id: int = None,
        log_detail: str = None,
        login_name: str = None,
        product_code: str = None,
        status: int = None,
        status_name: str = None,
        sub_type_code: str = None,
        sub_type_name: str = None,
        type_code: str = None,
        type_name: str = None,
        user_id: int = None,
    ):
        self.alert_time = alert_time
        self.backed = backed
        self.data_instance = data_instance
        self.deal_display_name = deal_display_name
        self.deal_login_name = deal_login_name
        self.deal_reason = deal_reason
        self.deal_time = deal_time
        self.deal_user_id = deal_user_id
        self.detail = detail
        self.display_name = display_name
        self.event_time = event_time
        self.handle_info_list = handle_info_list
        self.id = id
        self.log_detail = log_detail
        self.login_name = login_name
        self.product_code = product_code
        self.status = status
        self.status_name = status_name
        self.sub_type_code = sub_type_code
        self.sub_type_name = sub_type_name
        self.type_code = type_code
        self.type_name = type_name
        self.user_id = user_id

    def validate(self):
        if self.detail:
            self.detail.validate()
        if self.handle_info_list:
            for k in self.handle_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_time is not None:
            result['AlertTime'] = self.alert_time
        if self.backed is not None:
            result['Backed'] = self.backed
        if self.data_instance is not None:
            result['DataInstance'] = self.data_instance
        if self.deal_display_name is not None:
            result['DealDisplayName'] = self.deal_display_name
        if self.deal_login_name is not None:
            result['DealLoginName'] = self.deal_login_name
        if self.deal_reason is not None:
            result['DealReason'] = self.deal_reason
        if self.deal_time is not None:
            result['DealTime'] = self.deal_time
        if self.deal_user_id is not None:
            result['DealUserId'] = self.deal_user_id
        if self.detail is not None:
            result['Detail'] = self.detail.to_map()
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.event_time is not None:
            result['EventTime'] = self.event_time
        result['HandleInfoList'] = []
        if self.handle_info_list is not None:
            for k in self.handle_info_list:
                result['HandleInfoList'].append(k.to_map() if k else None)
        if self.id is not None:
            result['Id'] = self.id
        if self.log_detail is not None:
            result['LogDetail'] = self.log_detail
        if self.login_name is not None:
            result['LoginName'] = self.login_name
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.status is not None:
            result['Status'] = self.status
        if self.status_name is not None:
            result['StatusName'] = self.status_name
        if self.sub_type_code is not None:
            result['SubTypeCode'] = self.sub_type_code
        if self.sub_type_name is not None:
            result['SubTypeName'] = self.sub_type_name
        if self.type_code is not None:
            result['TypeCode'] = self.type_code
        if self.type_name is not None:
            result['TypeName'] = self.type_name
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertTime') is not None:
            self.alert_time = m.get('AlertTime')
        if m.get('Backed') is not None:
            self.backed = m.get('Backed')
        if m.get('DataInstance') is not None:
            self.data_instance = m.get('DataInstance')
        if m.get('DealDisplayName') is not None:
            self.deal_display_name = m.get('DealDisplayName')
        if m.get('DealLoginName') is not None:
            self.deal_login_name = m.get('DealLoginName')
        if m.get('DealReason') is not None:
            self.deal_reason = m.get('DealReason')
        if m.get('DealTime') is not None:
            self.deal_time = m.get('DealTime')
        if m.get('DealUserId') is not None:
            self.deal_user_id = m.get('DealUserId')
        if m.get('Detail') is not None:
            temp_model = DescribeEventDetailResponseBodyEventDetail()
            self.detail = temp_model.from_map(m['Detail'])
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('EventTime') is not None:
            self.event_time = m.get('EventTime')
        self.handle_info_list = []
        if m.get('HandleInfoList') is not None:
            for k in m.get('HandleInfoList'):
                temp_model = DescribeEventDetailResponseBodyEventHandleInfoList()
                self.handle_info_list.append(temp_model.from_map(k))
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LogDetail') is not None:
            self.log_detail = m.get('LogDetail')
        if m.get('LoginName') is not None:
            self.login_name = m.get('LoginName')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StatusName') is not None:
            self.status_name = m.get('StatusName')
        if m.get('SubTypeCode') is not None:
            self.sub_type_code = m.get('SubTypeCode')
        if m.get('SubTypeName') is not None:
            self.sub_type_name = m.get('SubTypeName')
        if m.get('TypeCode') is not None:
            self.type_code = m.get('TypeCode')
        if m.get('TypeName') is not None:
            self.type_name = m.get('TypeName')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class DescribeEventDetailResponseBody(TeaModel):
    def __init__(
        self,
        event: DescribeEventDetailResponseBodyEvent = None,
        request_id: str = None,
    ):
        self.event = event
        self.request_id = request_id

    def validate(self):
        if self.event:
            self.event.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event is not None:
            result['Event'] = self.event.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Event') is not None:
            temp_model = DescribeEventDetailResponseBodyEvent()
            self.event = temp_model.from_map(m['Event'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeEventDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeEventDetailResponseBody = None,
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
            temp_model = DescribeEventDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeEventTypesRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        parent_type_id: int = None,
        resource_id: int = None,
        status: int = None,
    ):
        self.lang = lang
        self.parent_type_id = parent_type_id
        self.resource_id = resource_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.parent_type_id is not None:
            result['ParentTypeId'] = self.parent_type_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('ParentTypeId') is not None:
            self.parent_type_id = m.get('ParentTypeId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeEventTypesResponseBodyEventTypeListSubTypeList(TeaModel):
    def __init__(
        self,
        adapted_product: str = None,
        code: str = None,
        config_code: str = None,
        config_content_type: int = None,
        config_description: str = None,
        config_value: str = None,
        description: str = None,
        event_hit_count: int = None,
        id: int = None,
        name: str = None,
        status: int = None,
    ):
        self.adapted_product = adapted_product
        self.code = code
        self.config_code = config_code
        self.config_content_type = config_content_type
        self.config_description = config_description
        self.config_value = config_value
        self.description = description
        self.event_hit_count = event_hit_count
        self.id = id
        self.name = name
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.adapted_product is not None:
            result['AdaptedProduct'] = self.adapted_product
        if self.code is not None:
            result['Code'] = self.code
        if self.config_code is not None:
            result['ConfigCode'] = self.config_code
        if self.config_content_type is not None:
            result['ConfigContentType'] = self.config_content_type
        if self.config_description is not None:
            result['ConfigDescription'] = self.config_description
        if self.config_value is not None:
            result['ConfigValue'] = self.config_value
        if self.description is not None:
            result['Description'] = self.description
        if self.event_hit_count is not None:
            result['EventHitCount'] = self.event_hit_count
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdaptedProduct') is not None:
            self.adapted_product = m.get('AdaptedProduct')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ConfigCode') is not None:
            self.config_code = m.get('ConfigCode')
        if m.get('ConfigContentType') is not None:
            self.config_content_type = m.get('ConfigContentType')
        if m.get('ConfigDescription') is not None:
            self.config_description = m.get('ConfigDescription')
        if m.get('ConfigValue') is not None:
            self.config_value = m.get('ConfigValue')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EventHitCount') is not None:
            self.event_hit_count = m.get('EventHitCount')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeEventTypesResponseBodyEventTypeList(TeaModel):
    def __init__(
        self,
        code: str = None,
        description: str = None,
        id: int = None,
        name: str = None,
        sub_type_list: List[DescribeEventTypesResponseBodyEventTypeListSubTypeList] = None,
    ):
        self.code = code
        self.description = description
        self.id = id
        self.name = name
        self.sub_type_list = sub_type_list

    def validate(self):
        if self.sub_type_list:
            for k in self.sub_type_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        result['SubTypeList'] = []
        if self.sub_type_list is not None:
            for k in self.sub_type_list:
                result['SubTypeList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        self.sub_type_list = []
        if m.get('SubTypeList') is not None:
            for k in m.get('SubTypeList'):
                temp_model = DescribeEventTypesResponseBodyEventTypeListSubTypeList()
                self.sub_type_list.append(temp_model.from_map(k))
        return self


class DescribeEventTypesResponseBody(TeaModel):
    def __init__(
        self,
        event_type_list: List[DescribeEventTypesResponseBodyEventTypeList] = None,
        request_id: str = None,
    ):
        self.event_type_list = event_type_list
        self.request_id = request_id

    def validate(self):
        if self.event_type_list:
            for k in self.event_type_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['EventTypeList'] = []
        if self.event_type_list is not None:
            for k in self.event_type_list:
                result['EventTypeList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.event_type_list = []
        if m.get('EventTypeList') is not None:
            for k in m.get('EventTypeList'):
                temp_model = DescribeEventTypesResponseBodyEventTypeList()
                self.event_type_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeEventTypesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeEventTypesResponseBody = None,
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
            temp_model = DescribeEventTypesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeEventsRequest(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        deal_user_id: str = None,
        end_time: str = None,
        id: int = None,
        instance_name: str = None,
        lang: str = None,
        page_size: int = None,
        product_code: str = None,
        start_time: str = None,
        status: str = None,
        sub_type_code: str = None,
        target_product_code: str = None,
        type_code: str = None,
        user_id: int = None,
        user_name: str = None,
    ):
        self.current_page = current_page
        self.deal_user_id = deal_user_id
        self.end_time = end_time
        self.id = id
        self.instance_name = instance_name
        self.lang = lang
        self.page_size = page_size
        self.product_code = product_code
        self.start_time = start_time
        self.status = status
        self.sub_type_code = sub_type_code
        self.target_product_code = target_product_code
        self.type_code = type_code
        self.user_id = user_id
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.deal_user_id is not None:
            result['DealUserId'] = self.deal_user_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.id is not None:
            result['Id'] = self.id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.sub_type_code is not None:
            result['SubTypeCode'] = self.sub_type_code
        if self.target_product_code is not None:
            result['TargetProductCode'] = self.target_product_code
        if self.type_code is not None:
            result['TypeCode'] = self.type_code
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('DealUserId') is not None:
            self.deal_user_id = m.get('DealUserId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubTypeCode') is not None:
            self.sub_type_code = m.get('SubTypeCode')
        if m.get('TargetProductCode') is not None:
            self.target_product_code = m.get('TargetProductCode')
        if m.get('TypeCode') is not None:
            self.type_code = m.get('TypeCode')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class DescribeEventsResponseBodyItems(TeaModel):
    def __init__(
        self,
        alert_time: int = None,
        backed: bool = None,
        deal_display_name: str = None,
        deal_login_name: str = None,
        deal_time: int = None,
        deal_user_id: int = None,
        display_name: str = None,
        event_time: int = None,
        id: int = None,
        login_name: str = None,
        product_code: str = None,
        status: int = None,
        status_name: str = None,
        sub_type_code: str = None,
        sub_type_name: str = None,
        target_product_code: str = None,
        type_code: str = None,
        type_name: str = None,
        user_id: int = None,
        warn_level: int = None,
    ):
        self.alert_time = alert_time
        self.backed = backed
        self.deal_display_name = deal_display_name
        self.deal_login_name = deal_login_name
        self.deal_time = deal_time
        self.deal_user_id = deal_user_id
        self.display_name = display_name
        self.event_time = event_time
        self.id = id
        self.login_name = login_name
        self.product_code = product_code
        self.status = status
        self.status_name = status_name
        self.sub_type_code = sub_type_code
        self.sub_type_name = sub_type_name
        self.target_product_code = target_product_code
        self.type_code = type_code
        self.type_name = type_name
        self.user_id = user_id
        self.warn_level = warn_level

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_time is not None:
            result['AlertTime'] = self.alert_time
        if self.backed is not None:
            result['Backed'] = self.backed
        if self.deal_display_name is not None:
            result['DealDisplayName'] = self.deal_display_name
        if self.deal_login_name is not None:
            result['DealLoginName'] = self.deal_login_name
        if self.deal_time is not None:
            result['DealTime'] = self.deal_time
        if self.deal_user_id is not None:
            result['DealUserId'] = self.deal_user_id
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.event_time is not None:
            result['EventTime'] = self.event_time
        if self.id is not None:
            result['Id'] = self.id
        if self.login_name is not None:
            result['LoginName'] = self.login_name
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.status is not None:
            result['Status'] = self.status
        if self.status_name is not None:
            result['StatusName'] = self.status_name
        if self.sub_type_code is not None:
            result['SubTypeCode'] = self.sub_type_code
        if self.sub_type_name is not None:
            result['SubTypeName'] = self.sub_type_name
        if self.target_product_code is not None:
            result['TargetProductCode'] = self.target_product_code
        if self.type_code is not None:
            result['TypeCode'] = self.type_code
        if self.type_name is not None:
            result['TypeName'] = self.type_name
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.warn_level is not None:
            result['WarnLevel'] = self.warn_level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertTime') is not None:
            self.alert_time = m.get('AlertTime')
        if m.get('Backed') is not None:
            self.backed = m.get('Backed')
        if m.get('DealDisplayName') is not None:
            self.deal_display_name = m.get('DealDisplayName')
        if m.get('DealLoginName') is not None:
            self.deal_login_name = m.get('DealLoginName')
        if m.get('DealTime') is not None:
            self.deal_time = m.get('DealTime')
        if m.get('DealUserId') is not None:
            self.deal_user_id = m.get('DealUserId')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('EventTime') is not None:
            self.event_time = m.get('EventTime')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LoginName') is not None:
            self.login_name = m.get('LoginName')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StatusName') is not None:
            self.status_name = m.get('StatusName')
        if m.get('SubTypeCode') is not None:
            self.sub_type_code = m.get('SubTypeCode')
        if m.get('SubTypeName') is not None:
            self.sub_type_name = m.get('SubTypeName')
        if m.get('TargetProductCode') is not None:
            self.target_product_code = m.get('TargetProductCode')
        if m.get('TypeCode') is not None:
            self.type_code = m.get('TypeCode')
        if m.get('TypeName') is not None:
            self.type_name = m.get('TypeName')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('WarnLevel') is not None:
            self.warn_level = m.get('WarnLevel')
        return self


class DescribeEventsResponseBody(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        items: List[DescribeEventsResponseBodyItems] = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.current_page = current_page
        self.items = items
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

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
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = DescribeEventsResponseBodyItems()
                self.items.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeEventsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeEventsResponseBody = None,
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
            temp_model = DescribeEventsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstanceSourcesRequest(TeaModel):
    def __init__(
        self,
        audit_status: int = None,
        auth_status: int = None,
        current_page: int = None,
        engine_type: str = None,
        instance_id: str = None,
        lang: str = None,
        page_size: int = None,
        product_code: str = None,
        product_id: int = None,
        search_key: str = None,
        search_type: str = None,
        service_region_id: str = None,
    ):
        self.audit_status = audit_status
        self.auth_status = auth_status
        self.current_page = current_page
        self.engine_type = engine_type
        self.instance_id = instance_id
        self.lang = lang
        self.page_size = page_size
        self.product_code = product_code
        self.product_id = product_id
        self.search_key = search_key
        self.search_type = search_type
        self.service_region_id = service_region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audit_status is not None:
            result['AuditStatus'] = self.audit_status
        if self.auth_status is not None:
            result['AuthStatus'] = self.auth_status
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.engine_type is not None:
            result['EngineType'] = self.engine_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.search_key is not None:
            result['SearchKey'] = self.search_key
        if self.search_type is not None:
            result['SearchType'] = self.search_type
        if self.service_region_id is not None:
            result['ServiceRegionId'] = self.service_region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuditStatus') is not None:
            self.audit_status = m.get('AuditStatus')
        if m.get('AuthStatus') is not None:
            self.auth_status = m.get('AuthStatus')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('EngineType') is not None:
            self.engine_type = m.get('EngineType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('SearchKey') is not None:
            self.search_key = m.get('SearchKey')
        if m.get('SearchType') is not None:
            self.search_type = m.get('SearchType')
        if m.get('ServiceRegionId') is not None:
            self.service_region_id = m.get('ServiceRegionId')
        return self


class DescribeInstanceSourcesResponseBodyItems(TeaModel):
    def __init__(
        self,
        audit_status: int = None,
        auto_scan: int = None,
        can_modify_user_name: bool = None,
        check_status: int = None,
        datamask_status: int = None,
        db_name: str = None,
        enable: int = None,
        engine_type: str = None,
        error_message: str = None,
        gmt_create: int = None,
        id: int = None,
        instance_description: str = None,
        instance_id: str = None,
        instance_size: int = None,
        last_modify_time: int = None,
        last_modify_user_id: str = None,
        log_store_day: int = None,
        password_status: int = None,
        product_id: int = None,
        region_id: str = None,
        region_name: str = None,
        sampling_size: int = None,
        tenant_id: str = None,
        tenant_name: str = None,
        user_name: str = None,
    ):
        self.audit_status = audit_status
        self.auto_scan = auto_scan
        self.can_modify_user_name = can_modify_user_name
        self.check_status = check_status
        self.datamask_status = datamask_status
        self.db_name = db_name
        self.enable = enable
        self.engine_type = engine_type
        self.error_message = error_message
        self.gmt_create = gmt_create
        self.id = id
        self.instance_description = instance_description
        self.instance_id = instance_id
        self.instance_size = instance_size
        self.last_modify_time = last_modify_time
        self.last_modify_user_id = last_modify_user_id
        self.log_store_day = log_store_day
        self.password_status = password_status
        self.product_id = product_id
        self.region_id = region_id
        self.region_name = region_name
        self.sampling_size = sampling_size
        self.tenant_id = tenant_id
        self.tenant_name = tenant_name
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audit_status is not None:
            result['AuditStatus'] = self.audit_status
        if self.auto_scan is not None:
            result['AutoScan'] = self.auto_scan
        if self.can_modify_user_name is not None:
            result['CanModifyUserName'] = self.can_modify_user_name
        if self.check_status is not None:
            result['CheckStatus'] = self.check_status
        if self.datamask_status is not None:
            result['DatamaskStatus'] = self.datamask_status
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.engine_type is not None:
            result['EngineType'] = self.engine_type
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.id is not None:
            result['Id'] = self.id
        if self.instance_description is not None:
            result['InstanceDescription'] = self.instance_description
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_size is not None:
            result['InstanceSize'] = self.instance_size
        if self.last_modify_time is not None:
            result['LastModifyTime'] = self.last_modify_time
        if self.last_modify_user_id is not None:
            result['LastModifyUserId'] = self.last_modify_user_id
        if self.log_store_day is not None:
            result['LogStoreDay'] = self.log_store_day
        if self.password_status is not None:
            result['PasswordStatus'] = self.password_status
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.region_name is not None:
            result['RegionName'] = self.region_name
        if self.sampling_size is not None:
            result['SamplingSize'] = self.sampling_size
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.tenant_name is not None:
            result['TenantName'] = self.tenant_name
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuditStatus') is not None:
            self.audit_status = m.get('AuditStatus')
        if m.get('AutoScan') is not None:
            self.auto_scan = m.get('AutoScan')
        if m.get('CanModifyUserName') is not None:
            self.can_modify_user_name = m.get('CanModifyUserName')
        if m.get('CheckStatus') is not None:
            self.check_status = m.get('CheckStatus')
        if m.get('DatamaskStatus') is not None:
            self.datamask_status = m.get('DatamaskStatus')
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('EngineType') is not None:
            self.engine_type = m.get('EngineType')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InstanceDescription') is not None:
            self.instance_description = m.get('InstanceDescription')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceSize') is not None:
            self.instance_size = m.get('InstanceSize')
        if m.get('LastModifyTime') is not None:
            self.last_modify_time = m.get('LastModifyTime')
        if m.get('LastModifyUserId') is not None:
            self.last_modify_user_id = m.get('LastModifyUserId')
        if m.get('LogStoreDay') is not None:
            self.log_store_day = m.get('LogStoreDay')
        if m.get('PasswordStatus') is not None:
            self.password_status = m.get('PasswordStatus')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RegionName') is not None:
            self.region_name = m.get('RegionName')
        if m.get('SamplingSize') is not None:
            self.sampling_size = m.get('SamplingSize')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('TenantName') is not None:
            self.tenant_name = m.get('TenantName')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class DescribeInstanceSourcesResponseBody(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        items: List[DescribeInstanceSourcesResponseBodyItems] = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.current_page = current_page
        self.items = items
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

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
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = DescribeInstanceSourcesResponseBodyItems()
                self.items.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeInstanceSourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeInstanceSourcesResponseBody = None,
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
            temp_model = DescribeInstanceSourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstancesRequest(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        feature_type: int = None,
        lang: str = None,
        name: str = None,
        page_size: int = None,
        product_code: str = None,
        product_id: int = None,
        risk_level_id: int = None,
        rule_id: int = None,
        service_region_id: str = None,
    ):
        self.current_page = current_page
        self.feature_type = feature_type
        self.lang = lang
        self.name = name
        self.page_size = page_size
        self.product_code = product_code
        self.product_id = product_id
        self.risk_level_id = risk_level_id
        self.rule_id = rule_id
        self.service_region_id = service_region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.feature_type is not None:
            result['FeatureType'] = self.feature_type
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.name is not None:
            result['Name'] = self.name
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.risk_level_id is not None:
            result['RiskLevelId'] = self.risk_level_id
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.service_region_id is not None:
            result['ServiceRegionId'] = self.service_region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('FeatureType') is not None:
            self.feature_type = m.get('FeatureType')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('RiskLevelId') is not None:
            self.risk_level_id = m.get('RiskLevelId')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('ServiceRegionId') is not None:
            self.service_region_id = m.get('ServiceRegionId')
        return self


class DescribeInstancesResponseBodyItems(TeaModel):
    def __init__(
        self,
        creation_time: int = None,
        depart_name: str = None,
        id: int = None,
        instance_description: str = None,
        labelsec: bool = None,
        last_finish_time: int = None,
        name: str = None,
        odps_risk_level_name: str = None,
        owner: str = None,
        product_code: str = None,
        product_id: str = None,
        protection: bool = None,
        risk_level_id: int = None,
        risk_level_name: str = None,
        rule_name: str = None,
        sensitive: bool = None,
        sensitive_count: int = None,
        tenant_name: str = None,
        total_count: int = None,
    ):
        self.creation_time = creation_time
        self.depart_name = depart_name
        self.id = id
        self.instance_description = instance_description
        self.labelsec = labelsec
        self.last_finish_time = last_finish_time
        self.name = name
        self.odps_risk_level_name = odps_risk_level_name
        self.owner = owner
        self.product_code = product_code
        self.product_id = product_id
        self.protection = protection
        self.risk_level_id = risk_level_id
        self.risk_level_name = risk_level_name
        self.rule_name = rule_name
        self.sensitive = sensitive
        self.sensitive_count = sensitive_count
        self.tenant_name = tenant_name
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.depart_name is not None:
            result['DepartName'] = self.depart_name
        if self.id is not None:
            result['Id'] = self.id
        if self.instance_description is not None:
            result['InstanceDescription'] = self.instance_description
        if self.labelsec is not None:
            result['Labelsec'] = self.labelsec
        if self.last_finish_time is not None:
            result['LastFinishTime'] = self.last_finish_time
        if self.name is not None:
            result['Name'] = self.name
        if self.odps_risk_level_name is not None:
            result['OdpsRiskLevelName'] = self.odps_risk_level_name
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.protection is not None:
            result['Protection'] = self.protection
        if self.risk_level_id is not None:
            result['RiskLevelId'] = self.risk_level_id
        if self.risk_level_name is not None:
            result['RiskLevelName'] = self.risk_level_name
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.sensitive is not None:
            result['Sensitive'] = self.sensitive
        if self.sensitive_count is not None:
            result['SensitiveCount'] = self.sensitive_count
        if self.tenant_name is not None:
            result['TenantName'] = self.tenant_name
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('DepartName') is not None:
            self.depart_name = m.get('DepartName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InstanceDescription') is not None:
            self.instance_description = m.get('InstanceDescription')
        if m.get('Labelsec') is not None:
            self.labelsec = m.get('Labelsec')
        if m.get('LastFinishTime') is not None:
            self.last_finish_time = m.get('LastFinishTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OdpsRiskLevelName') is not None:
            self.odps_risk_level_name = m.get('OdpsRiskLevelName')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('Protection') is not None:
            self.protection = m.get('Protection')
        if m.get('RiskLevelId') is not None:
            self.risk_level_id = m.get('RiskLevelId')
        if m.get('RiskLevelName') is not None:
            self.risk_level_name = m.get('RiskLevelName')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('Sensitive') is not None:
            self.sensitive = m.get('Sensitive')
        if m.get('SensitiveCount') is not None:
            self.sensitive_count = m.get('SensitiveCount')
        if m.get('TenantName') is not None:
            self.tenant_name = m.get('TenantName')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeInstancesResponseBody(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        items: List[DescribeInstancesResponseBodyItems] = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.current_page = current_page
        self.items = items
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

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
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = DescribeInstancesResponseBodyItems()
                self.items.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeInstancesResponseBody = None,
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
            temp_model = DescribeInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeOssObjectDetailRequest(TeaModel):
    def __init__(
        self,
        id: int = None,
        lang: str = None,
    ):
        self.id = id
        self.lang = lang

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.lang is not None:
            result['Lang'] = self.lang
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        return self


class DescribeOssObjectDetailResponseBodyOssObjectDetailRuleList(TeaModel):
    def __init__(
        self,
        category_name: str = None,
        count: int = None,
        risk_level_id: int = None,
        risk_level_name: str = None,
        rule_name: str = None,
    ):
        self.category_name = category_name
        self.count = count
        self.risk_level_id = risk_level_id
        self.risk_level_name = risk_level_name
        self.rule_name = rule_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_name is not None:
            result['CategoryName'] = self.category_name
        if self.count is not None:
            result['Count'] = self.count
        if self.risk_level_id is not None:
            result['RiskLevelId'] = self.risk_level_id
        if self.risk_level_name is not None:
            result['RiskLevelName'] = self.risk_level_name
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryName') is not None:
            self.category_name = m.get('CategoryName')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('RiskLevelId') is not None:
            self.risk_level_id = m.get('RiskLevelId')
        if m.get('RiskLevelName') is not None:
            self.risk_level_name = m.get('RiskLevelName')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        return self


class DescribeOssObjectDetailResponseBodyOssObjectDetail(TeaModel):
    def __init__(
        self,
        bucket_name: str = None,
        category_name: str = None,
        name: str = None,
        region_id: str = None,
        risk_level_name: str = None,
        rule_list: List[DescribeOssObjectDetailResponseBodyOssObjectDetailRuleList] = None,
    ):
        self.bucket_name = bucket_name
        self.category_name = category_name
        self.name = name
        self.region_id = region_id
        self.risk_level_name = risk_level_name
        self.rule_list = rule_list

    def validate(self):
        if self.rule_list:
            for k in self.rule_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.category_name is not None:
            result['CategoryName'] = self.category_name
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.risk_level_name is not None:
            result['RiskLevelName'] = self.risk_level_name
        result['RuleList'] = []
        if self.rule_list is not None:
            for k in self.rule_list:
                result['RuleList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('CategoryName') is not None:
            self.category_name = m.get('CategoryName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RiskLevelName') is not None:
            self.risk_level_name = m.get('RiskLevelName')
        self.rule_list = []
        if m.get('RuleList') is not None:
            for k in m.get('RuleList'):
                temp_model = DescribeOssObjectDetailResponseBodyOssObjectDetailRuleList()
                self.rule_list.append(temp_model.from_map(k))
        return self


class DescribeOssObjectDetailResponseBody(TeaModel):
    def __init__(
        self,
        oss_object_detail: DescribeOssObjectDetailResponseBodyOssObjectDetail = None,
        request_id: str = None,
    ):
        self.oss_object_detail = oss_object_detail
        self.request_id = request_id

    def validate(self):
        if self.oss_object_detail:
            self.oss_object_detail.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.oss_object_detail is not None:
            result['OssObjectDetail'] = self.oss_object_detail.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OssObjectDetail') is not None:
            temp_model = DescribeOssObjectDetailResponseBodyOssObjectDetail()
            self.oss_object_detail = temp_model.from_map(m['OssObjectDetail'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeOssObjectDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeOssObjectDetailResponseBody = None,
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
            temp_model = DescribeOssObjectDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeOssObjectsRequest(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        instance_id: str = None,
        lang: str = None,
        last_scan_time_end: int = None,
        last_scan_time_start: int = None,
        name: str = None,
        page_size: int = None,
        risk_level_id: int = None,
        rule_id: int = None,
        service_region_id: str = None,
    ):
        self.current_page = current_page
        self.instance_id = instance_id
        self.lang = lang
        self.last_scan_time_end = last_scan_time_end
        self.last_scan_time_start = last_scan_time_start
        self.name = name
        self.page_size = page_size
        self.risk_level_id = risk_level_id
        self.rule_id = rule_id
        self.service_region_id = service_region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.last_scan_time_end is not None:
            result['LastScanTimeEnd'] = self.last_scan_time_end
        if self.last_scan_time_start is not None:
            result['LastScanTimeStart'] = self.last_scan_time_start
        if self.name is not None:
            result['Name'] = self.name
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.risk_level_id is not None:
            result['RiskLevelId'] = self.risk_level_id
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.service_region_id is not None:
            result['ServiceRegionId'] = self.service_region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('LastScanTimeEnd') is not None:
            self.last_scan_time_end = m.get('LastScanTimeEnd')
        if m.get('LastScanTimeStart') is not None:
            self.last_scan_time_start = m.get('LastScanTimeStart')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RiskLevelId') is not None:
            self.risk_level_id = m.get('RiskLevelId')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('ServiceRegionId') is not None:
            self.service_region_id = m.get('ServiceRegionId')
        return self


class DescribeOssObjectsResponseBodyItemsRuleList(TeaModel):
    def __init__(
        self,
        count: int = None,
        name: str = None,
        risk_level_id: int = None,
    ):
        self.count = count
        self.name = name
        self.risk_level_id = risk_level_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.name is not None:
            result['Name'] = self.name
        if self.risk_level_id is not None:
            result['RiskLevelId'] = self.risk_level_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RiskLevelId') is not None:
            self.risk_level_id = m.get('RiskLevelId')
        return self


class DescribeOssObjectsResponseBodyItems(TeaModel):
    def __init__(
        self,
        bucket_name: str = None,
        category: int = None,
        category_name: str = None,
        file_id: str = None,
        id: str = None,
        instance_id: int = None,
        name: str = None,
        region_id: str = None,
        risk_level_id: int = None,
        risk_level_name: str = None,
        rule_count: int = None,
        rule_list: List[DescribeOssObjectsResponseBodyItemsRuleList] = None,
        sensitive_count: int = None,
        size: int = None,
    ):
        self.bucket_name = bucket_name
        self.category = category
        self.category_name = category_name
        self.file_id = file_id
        self.id = id
        self.instance_id = instance_id
        self.name = name
        self.region_id = region_id
        self.risk_level_id = risk_level_id
        self.risk_level_name = risk_level_name
        self.rule_count = rule_count
        self.rule_list = rule_list
        self.sensitive_count = sensitive_count
        self.size = size

    def validate(self):
        if self.rule_list:
            for k in self.rule_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.category is not None:
            result['Category'] = self.category
        if self.category_name is not None:
            result['CategoryName'] = self.category_name
        if self.file_id is not None:
            result['FileId'] = self.file_id
        if self.id is not None:
            result['Id'] = self.id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.risk_level_id is not None:
            result['RiskLevelId'] = self.risk_level_id
        if self.risk_level_name is not None:
            result['RiskLevelName'] = self.risk_level_name
        if self.rule_count is not None:
            result['RuleCount'] = self.rule_count
        result['RuleList'] = []
        if self.rule_list is not None:
            for k in self.rule_list:
                result['RuleList'].append(k.to_map() if k else None)
        if self.sensitive_count is not None:
            result['SensitiveCount'] = self.sensitive_count
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('CategoryName') is not None:
            self.category_name = m.get('CategoryName')
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RiskLevelId') is not None:
            self.risk_level_id = m.get('RiskLevelId')
        if m.get('RiskLevelName') is not None:
            self.risk_level_name = m.get('RiskLevelName')
        if m.get('RuleCount') is not None:
            self.rule_count = m.get('RuleCount')
        self.rule_list = []
        if m.get('RuleList') is not None:
            for k in m.get('RuleList'):
                temp_model = DescribeOssObjectsResponseBodyItemsRuleList()
                self.rule_list.append(temp_model.from_map(k))
        if m.get('SensitiveCount') is not None:
            self.sensitive_count = m.get('SensitiveCount')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class DescribeOssObjectsResponseBody(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        items: List[DescribeOssObjectsResponseBodyItems] = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.current_page = current_page
        self.items = items
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

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
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = DescribeOssObjectsResponseBodyItems()
                self.items.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeOssObjectsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeOssObjectsResponseBody = None,
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
            temp_model = DescribeOssObjectsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePackagesRequest(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        instance_id: int = None,
        lang: str = None,
        name: str = None,
        page_size: int = None,
        product_id: int = None,
        risk_level_id: int = None,
        rule_id: int = None,
    ):
        self.current_page = current_page
        self.instance_id = instance_id
        self.lang = lang
        self.name = name
        self.page_size = page_size
        self.product_id = product_id
        self.risk_level_id = risk_level_id
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.name is not None:
            result['Name'] = self.name
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.risk_level_id is not None:
            result['RiskLevelId'] = self.risk_level_id
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('RiskLevelId') is not None:
            self.risk_level_id = m.get('RiskLevelId')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class DescribePackagesResponseBodyItems(TeaModel):
    def __init__(
        self,
        creation_time: int = None,
        id: int = None,
        instance_id: int = None,
        name: str = None,
        owner: str = None,
        risk_level_id: int = None,
        risk_level_name: str = None,
        sensitive: bool = None,
        sensitive_count: int = None,
        total_count: int = None,
    ):
        self.creation_time = creation_time
        self.id = id
        self.instance_id = instance_id
        self.name = name
        self.owner = owner
        self.risk_level_id = risk_level_id
        self.risk_level_name = risk_level_name
        self.sensitive = sensitive
        self.sensitive_count = sensitive_count
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.id is not None:
            result['Id'] = self.id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.name is not None:
            result['Name'] = self.name
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.risk_level_id is not None:
            result['RiskLevelId'] = self.risk_level_id
        if self.risk_level_name is not None:
            result['RiskLevelName'] = self.risk_level_name
        if self.sensitive is not None:
            result['Sensitive'] = self.sensitive
        if self.sensitive_count is not None:
            result['SensitiveCount'] = self.sensitive_count
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('RiskLevelId') is not None:
            self.risk_level_id = m.get('RiskLevelId')
        if m.get('RiskLevelName') is not None:
            self.risk_level_name = m.get('RiskLevelName')
        if m.get('Sensitive') is not None:
            self.sensitive = m.get('Sensitive')
        if m.get('SensitiveCount') is not None:
            self.sensitive_count = m.get('SensitiveCount')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribePackagesResponseBody(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        items: List[DescribePackagesResponseBodyItems] = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.current_page = current_page
        self.items = items
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

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
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = DescribePackagesResponseBodyItems()
                self.items.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribePackagesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribePackagesResponseBody = None,
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
            temp_model = DescribePackagesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRiskLevelsRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
    ):
        self.lang = lang

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        return self


class DescribeRiskLevelsResponseBodyRiskLevelList(TeaModel):
    def __init__(
        self,
        description: str = None,
        id: int = None,
        name: str = None,
        reference_num: int = None,
    ):
        self.description = description
        self.id = id
        self.name = name
        self.reference_num = reference_num

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
        if self.name is not None:
            result['Name'] = self.name
        if self.reference_num is not None:
            result['ReferenceNum'] = self.reference_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ReferenceNum') is not None:
            self.reference_num = m.get('ReferenceNum')
        return self


class DescribeRiskLevelsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        risk_level_list: List[DescribeRiskLevelsResponseBodyRiskLevelList] = None,
    ):
        self.request_id = request_id
        self.risk_level_list = risk_level_list

    def validate(self):
        if self.risk_level_list:
            for k in self.risk_level_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['RiskLevelList'] = []
        if self.risk_level_list is not None:
            for k in self.risk_level_list:
                result['RiskLevelList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.risk_level_list = []
        if m.get('RiskLevelList') is not None:
            for k in m.get('RiskLevelList'):
                temp_model = DescribeRiskLevelsResponseBodyRiskLevelList()
                self.risk_level_list.append(temp_model.from_map(k))
        return self


class DescribeRiskLevelsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeRiskLevelsResponseBody = None,
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
            temp_model = DescribeRiskLevelsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRulesRequest(TeaModel):
    def __init__(
        self,
        category: int = None,
        content_category: int = None,
        current_page: int = None,
        custom_type: int = None,
        group_id: str = None,
        keyword_compatible: bool = None,
        lang: str = None,
        name: str = None,
        page_size: int = None,
        product_code: int = None,
        product_id: int = None,
        risk_level_id: int = None,
        rule_type: int = None,
        status: int = None,
        warn_level: int = None,
    ):
        self.category = category
        self.content_category = content_category
        self.current_page = current_page
        self.custom_type = custom_type
        self.group_id = group_id
        self.keyword_compatible = keyword_compatible
        self.lang = lang
        self.name = name
        self.page_size = page_size
        self.product_code = product_code
        self.product_id = product_id
        self.risk_level_id = risk_level_id
        self.rule_type = rule_type
        self.status = status
        self.warn_level = warn_level

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.content_category is not None:
            result['ContentCategory'] = self.content_category
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.custom_type is not None:
            result['CustomType'] = self.custom_type
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.keyword_compatible is not None:
            result['KeywordCompatible'] = self.keyword_compatible
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.name is not None:
            result['Name'] = self.name
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.risk_level_id is not None:
            result['RiskLevelId'] = self.risk_level_id
        if self.rule_type is not None:
            result['RuleType'] = self.rule_type
        if self.status is not None:
            result['Status'] = self.status
        if self.warn_level is not None:
            result['WarnLevel'] = self.warn_level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('ContentCategory') is not None:
            self.content_category = m.get('ContentCategory')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('CustomType') is not None:
            self.custom_type = m.get('CustomType')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('KeywordCompatible') is not None:
            self.keyword_compatible = m.get('KeywordCompatible')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('RiskLevelId') is not None:
            self.risk_level_id = m.get('RiskLevelId')
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('WarnLevel') is not None:
            self.warn_level = m.get('WarnLevel')
        return self


class DescribeRulesResponseBodyItems(TeaModel):
    def __init__(
        self,
        category: int = None,
        category_name: str = None,
        content: str = None,
        content_category: str = None,
        custom_type: int = None,
        description: str = None,
        display_name: str = None,
        gmt_create: int = None,
        gmt_modified: int = None,
        group_id: str = None,
        hit_total_count: int = None,
        id: int = None,
        login_name: str = None,
        major_key: str = None,
        name: str = None,
        product_code: str = None,
        product_id: int = None,
        risk_level_id: int = None,
        risk_level_name: str = None,
        stat_express: str = None,
        status: int = None,
        target: str = None,
        user_id: int = None,
        warn_level: int = None,
    ):
        self.category = category
        self.category_name = category_name
        self.content = content
        self.content_category = content_category
        self.custom_type = custom_type
        self.description = description
        self.display_name = display_name
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.group_id = group_id
        self.hit_total_count = hit_total_count
        self.id = id
        self.login_name = login_name
        self.major_key = major_key
        self.name = name
        self.product_code = product_code
        self.product_id = product_id
        self.risk_level_id = risk_level_id
        self.risk_level_name = risk_level_name
        self.stat_express = stat_express
        self.status = status
        self.target = target
        self.user_id = user_id
        self.warn_level = warn_level

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.category_name is not None:
            result['CategoryName'] = self.category_name
        if self.content is not None:
            result['Content'] = self.content
        if self.content_category is not None:
            result['ContentCategory'] = self.content_category
        if self.custom_type is not None:
            result['CustomType'] = self.custom_type
        if self.description is not None:
            result['Description'] = self.description
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.hit_total_count is not None:
            result['HitTotalCount'] = self.hit_total_count
        if self.id is not None:
            result['Id'] = self.id
        if self.login_name is not None:
            result['LoginName'] = self.login_name
        if self.major_key is not None:
            result['MajorKey'] = self.major_key
        if self.name is not None:
            result['Name'] = self.name
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.risk_level_id is not None:
            result['RiskLevelId'] = self.risk_level_id
        if self.risk_level_name is not None:
            result['RiskLevelName'] = self.risk_level_name
        if self.stat_express is not None:
            result['StatExpress'] = self.stat_express
        if self.status is not None:
            result['Status'] = self.status
        if self.target is not None:
            result['Target'] = self.target
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.warn_level is not None:
            result['WarnLevel'] = self.warn_level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('CategoryName') is not None:
            self.category_name = m.get('CategoryName')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('ContentCategory') is not None:
            self.content_category = m.get('ContentCategory')
        if m.get('CustomType') is not None:
            self.custom_type = m.get('CustomType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('HitTotalCount') is not None:
            self.hit_total_count = m.get('HitTotalCount')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LoginName') is not None:
            self.login_name = m.get('LoginName')
        if m.get('MajorKey') is not None:
            self.major_key = m.get('MajorKey')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('RiskLevelId') is not None:
            self.risk_level_id = m.get('RiskLevelId')
        if m.get('RiskLevelName') is not None:
            self.risk_level_name = m.get('RiskLevelName')
        if m.get('StatExpress') is not None:
            self.stat_express = m.get('StatExpress')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Target') is not None:
            self.target = m.get('Target')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('WarnLevel') is not None:
            self.warn_level = m.get('WarnLevel')
        return self


class DescribeRulesResponseBody(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        items: List[DescribeRulesResponseBodyItems] = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.current_page = current_page
        self.items = items
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

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
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = DescribeRulesResponseBodyItems()
                self.items.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeRulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeRulesResponseBody = None,
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
            temp_model = DescribeRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTablesRequest(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        instance_id: int = None,
        lang: str = None,
        name: str = None,
        package_id: int = None,
        page_size: int = None,
        product_code: str = None,
        product_id: int = None,
        risk_level_id: int = None,
        rule_id: int = None,
        service_region_id: str = None,
    ):
        self.current_page = current_page
        self.instance_id = instance_id
        self.lang = lang
        self.name = name
        self.package_id = package_id
        self.page_size = page_size
        self.product_code = product_code
        self.product_id = product_id
        self.risk_level_id = risk_level_id
        self.rule_id = rule_id
        self.service_region_id = service_region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.name is not None:
            result['Name'] = self.name
        if self.package_id is not None:
            result['PackageId'] = self.package_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.risk_level_id is not None:
            result['RiskLevelId'] = self.risk_level_id
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.service_region_id is not None:
            result['ServiceRegionId'] = self.service_region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PackageId') is not None:
            self.package_id = m.get('PackageId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('RiskLevelId') is not None:
            self.risk_level_id = m.get('RiskLevelId')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('ServiceRegionId') is not None:
            self.service_region_id = m.get('ServiceRegionId')
        return self


class DescribeTablesResponseBodyItemsRuleList(TeaModel):
    def __init__(
        self,
        count: int = None,
        name: str = None,
        risk_level_id: int = None,
    ):
        self.count = count
        self.name = name
        self.risk_level_id = risk_level_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.name is not None:
            result['Name'] = self.name
        if self.risk_level_id is not None:
            result['RiskLevelId'] = self.risk_level_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RiskLevelId') is not None:
            self.risk_level_id = m.get('RiskLevelId')
        return self


class DescribeTablesResponseBodyItems(TeaModel):
    def __init__(
        self,
        creation_time: int = None,
        id: int = None,
        instance_description: str = None,
        instance_id: int = None,
        instance_name: str = None,
        name: str = None,
        owner: str = None,
        product_code: str = None,
        product_id: str = None,
        risk_level_id: int = None,
        risk_level_name: str = None,
        rule_list: List[DescribeTablesResponseBodyItemsRuleList] = None,
        sensitive: bool = None,
        sensitive_count: int = None,
        sensitive_ratio: str = None,
        tenant_name: str = None,
        total_count: int = None,
    ):
        self.creation_time = creation_time
        self.id = id
        self.instance_description = instance_description
        self.instance_id = instance_id
        self.instance_name = instance_name
        self.name = name
        self.owner = owner
        self.product_code = product_code
        self.product_id = product_id
        self.risk_level_id = risk_level_id
        self.risk_level_name = risk_level_name
        self.rule_list = rule_list
        self.sensitive = sensitive
        self.sensitive_count = sensitive_count
        self.sensitive_ratio = sensitive_ratio
        self.tenant_name = tenant_name
        self.total_count = total_count

    def validate(self):
        if self.rule_list:
            for k in self.rule_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.id is not None:
            result['Id'] = self.id
        if self.instance_description is not None:
            result['InstanceDescription'] = self.instance_description
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.name is not None:
            result['Name'] = self.name
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.risk_level_id is not None:
            result['RiskLevelId'] = self.risk_level_id
        if self.risk_level_name is not None:
            result['RiskLevelName'] = self.risk_level_name
        result['RuleList'] = []
        if self.rule_list is not None:
            for k in self.rule_list:
                result['RuleList'].append(k.to_map() if k else None)
        if self.sensitive is not None:
            result['Sensitive'] = self.sensitive
        if self.sensitive_count is not None:
            result['SensitiveCount'] = self.sensitive_count
        if self.sensitive_ratio is not None:
            result['SensitiveRatio'] = self.sensitive_ratio
        if self.tenant_name is not None:
            result['TenantName'] = self.tenant_name
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InstanceDescription') is not None:
            self.instance_description = m.get('InstanceDescription')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('RiskLevelId') is not None:
            self.risk_level_id = m.get('RiskLevelId')
        if m.get('RiskLevelName') is not None:
            self.risk_level_name = m.get('RiskLevelName')
        self.rule_list = []
        if m.get('RuleList') is not None:
            for k in m.get('RuleList'):
                temp_model = DescribeTablesResponseBodyItemsRuleList()
                self.rule_list.append(temp_model.from_map(k))
        if m.get('Sensitive') is not None:
            self.sensitive = m.get('Sensitive')
        if m.get('SensitiveCount') is not None:
            self.sensitive_count = m.get('SensitiveCount')
        if m.get('SensitiveRatio') is not None:
            self.sensitive_ratio = m.get('SensitiveRatio')
        if m.get('TenantName') is not None:
            self.tenant_name = m.get('TenantName')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeTablesResponseBody(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        items: List[DescribeTablesResponseBodyItems] = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.current_page = current_page
        self.items = items
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

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
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = DescribeTablesResponseBodyItems()
                self.items.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeTablesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeTablesResponseBody = None,
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
            temp_model = DescribeTablesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUserStatusRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
    ):
        self.lang = lang

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        return self


class DescribeUserStatusResponseBodyUserStatus(TeaModel):
    def __init__(
        self,
        access_key_id: str = None,
        authed: bool = None,
        charge_type: str = None,
        instance_id: str = None,
        instance_num: int = None,
        lab_status: int = None,
        purchased: bool = None,
        remain_days: int = None,
        trail: bool = None,
        use_instance_num: int = None,
        use_oss_size: int = None,
    ):
        self.access_key_id = access_key_id
        self.authed = authed
        self.charge_type = charge_type
        self.instance_id = instance_id
        self.instance_num = instance_num
        self.lab_status = lab_status
        self.purchased = purchased
        self.remain_days = remain_days
        self.trail = trail
        self.use_instance_num = use_instance_num
        self.use_oss_size = use_oss_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key_id is not None:
            result['AccessKeyId'] = self.access_key_id
        if self.authed is not None:
            result['Authed'] = self.authed
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_num is not None:
            result['InstanceNum'] = self.instance_num
        if self.lab_status is not None:
            result['LabStatus'] = self.lab_status
        if self.purchased is not None:
            result['Purchased'] = self.purchased
        if self.remain_days is not None:
            result['RemainDays'] = self.remain_days
        if self.trail is not None:
            result['Trail'] = self.trail
        if self.use_instance_num is not None:
            result['UseInstanceNum'] = self.use_instance_num
        if self.use_oss_size is not None:
            result['UseOssSize'] = self.use_oss_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessKeyId') is not None:
            self.access_key_id = m.get('AccessKeyId')
        if m.get('Authed') is not None:
            self.authed = m.get('Authed')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceNum') is not None:
            self.instance_num = m.get('InstanceNum')
        if m.get('LabStatus') is not None:
            self.lab_status = m.get('LabStatus')
        if m.get('Purchased') is not None:
            self.purchased = m.get('Purchased')
        if m.get('RemainDays') is not None:
            self.remain_days = m.get('RemainDays')
        if m.get('Trail') is not None:
            self.trail = m.get('Trail')
        if m.get('UseInstanceNum') is not None:
            self.use_instance_num = m.get('UseInstanceNum')
        if m.get('UseOssSize') is not None:
            self.use_oss_size = m.get('UseOssSize')
        return self


class DescribeUserStatusResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        user_status: DescribeUserStatusResponseBodyUserStatus = None,
    ):
        self.request_id = request_id
        self.user_status = user_status

    def validate(self):
        if self.user_status:
            self.user_status.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.user_status is not None:
            result['UserStatus'] = self.user_status.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UserStatus') is not None:
            temp_model = DescribeUserStatusResponseBodyUserStatus()
            self.user_status = temp_model.from_map(m['UserStatus'])
        return self


class DescribeUserStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeUserStatusResponseBody = None,
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
            temp_model = DescribeUserStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableUserConfigRequest(TeaModel):
    def __init__(
        self,
        code: str = None,
        lang: str = None,
    ):
        self.code = code
        self.lang = lang

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.lang is not None:
            result['Lang'] = self.lang
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        return self


class DisableUserConfigResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DisableUserConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DisableUserConfigResponseBody = None,
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
            temp_model = DisableUserConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExecDatamaskRequest(TeaModel):
    def __init__(
        self,
        data: str = None,
        lang: str = None,
        template_id: int = None,
    ):
        self.data = data
        self.lang = lang
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class ExecDatamaskResponseBody(TeaModel):
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


class ExecDatamaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ExecDatamaskResponseBody = None,
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
            temp_model = ExecDatamaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ManualTriggerMaskingProcessRequest(TeaModel):
    def __init__(
        self,
        id: int = None,
        lang: str = None,
    ):
        self.id = id
        self.lang = lang

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.lang is not None:
            result['Lang'] = self.lang
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        return self


class ManualTriggerMaskingProcessResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ManualTriggerMaskingProcessResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ManualTriggerMaskingProcessResponseBody = None,
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
            temp_model = ManualTriggerMaskingProcessResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDataLimitRequest(TeaModel):
    def __init__(
        self,
        audit_status: int = None,
        auto_scan: int = None,
        engine_type: str = None,
        id: int = None,
        lang: str = None,
        log_store_day: int = None,
        modify_password: bool = None,
        password: str = None,
        port: int = None,
        resource_type: int = None,
        service_region_id: str = None,
        user_name: str = None,
    ):
        self.audit_status = audit_status
        self.auto_scan = auto_scan
        self.engine_type = engine_type
        self.id = id
        self.lang = lang
        self.log_store_day = log_store_day
        self.modify_password = modify_password
        self.password = password
        self.port = port
        self.resource_type = resource_type
        self.service_region_id = service_region_id
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audit_status is not None:
            result['AuditStatus'] = self.audit_status
        if self.auto_scan is not None:
            result['AutoScan'] = self.auto_scan
        if self.engine_type is not None:
            result['EngineType'] = self.engine_type
        if self.id is not None:
            result['Id'] = self.id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.log_store_day is not None:
            result['LogStoreDay'] = self.log_store_day
        if self.modify_password is not None:
            result['ModifyPassword'] = self.modify_password
        if self.password is not None:
            result['Password'] = self.password
        if self.port is not None:
            result['Port'] = self.port
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.service_region_id is not None:
            result['ServiceRegionId'] = self.service_region_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuditStatus') is not None:
            self.audit_status = m.get('AuditStatus')
        if m.get('AutoScan') is not None:
            self.auto_scan = m.get('AutoScan')
        if m.get('EngineType') is not None:
            self.engine_type = m.get('EngineType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('LogStoreDay') is not None:
            self.log_store_day = m.get('LogStoreDay')
        if m.get('ModifyPassword') is not None:
            self.modify_password = m.get('ModifyPassword')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ServiceRegionId') is not None:
            self.service_region_id = m.get('ServiceRegionId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class ModifyDataLimitResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyDataLimitResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyDataLimitResponseBody = None,
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
            temp_model = ModifyDataLimitResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDefaultLevelRequest(TeaModel):
    def __init__(
        self,
        default_id: int = None,
        lang: str = None,
        sensitive_ids: str = None,
    ):
        self.default_id = default_id
        self.lang = lang
        self.sensitive_ids = sensitive_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.default_id is not None:
            result['DefaultId'] = self.default_id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.sensitive_ids is not None:
            result['SensitiveIds'] = self.sensitive_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultId') is not None:
            self.default_id = m.get('DefaultId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('SensitiveIds') is not None:
            self.sensitive_ids = m.get('SensitiveIds')
        return self


class ModifyDefaultLevelResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyDefaultLevelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyDefaultLevelResponseBody = None,
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
            temp_model = ModifyDefaultLevelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyEventStatusRequest(TeaModel):
    def __init__(
        self,
        backed: bool = None,
        deal_reason: str = None,
        id: int = None,
        lang: str = None,
        status: int = None,
    ):
        self.backed = backed
        self.deal_reason = deal_reason
        self.id = id
        self.lang = lang
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backed is not None:
            result['Backed'] = self.backed
        if self.deal_reason is not None:
            result['DealReason'] = self.deal_reason
        if self.id is not None:
            result['Id'] = self.id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Backed') is not None:
            self.backed = m.get('Backed')
        if m.get('DealReason') is not None:
            self.deal_reason = m.get('DealReason')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ModifyEventStatusResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyEventStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyEventStatusResponseBody = None,
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
            temp_model = ModifyEventStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyEventTypeStatusRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        sub_type_ids: str = None,
    ):
        self.lang = lang
        self.sub_type_ids = sub_type_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.sub_type_ids is not None:
            result['SubTypeIds'] = self.sub_type_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('SubTypeIds') is not None:
            self.sub_type_ids = m.get('SubTypeIds')
        return self


class ModifyEventTypeStatusResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyEventTypeStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyEventTypeStatusResponseBody = None,
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
            temp_model = ModifyEventTypeStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyReportTaskStatusRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        report_task_status: int = None,
    ):
        self.lang = lang
        self.report_task_status = report_task_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.report_task_status is not None:
            result['ReportTaskStatus'] = self.report_task_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('ReportTaskStatus') is not None:
            self.report_task_status = m.get('ReportTaskStatus')
        return self


class ModifyReportTaskStatusResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyReportTaskStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyReportTaskStatusResponseBody = None,
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
            temp_model = ModifyReportTaskStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyRuleRequest(TeaModel):
    def __init__(
        self,
        category: int = None,
        content: str = None,
        id: int = None,
        lang: str = None,
        name: str = None,
        product_code: str = None,
        product_id: int = None,
        risk_level_id: int = None,
        rule_type: int = None,
        warn_level: int = None,
    ):
        self.category = category
        self.content = content
        self.id = id
        self.lang = lang
        self.name = name
        self.product_code = product_code
        self.product_id = product_id
        self.risk_level_id = risk_level_id
        self.rule_type = rule_type
        self.warn_level = warn_level

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.content is not None:
            result['Content'] = self.content
        if self.id is not None:
            result['Id'] = self.id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.name is not None:
            result['Name'] = self.name
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.risk_level_id is not None:
            result['RiskLevelId'] = self.risk_level_id
        if self.rule_type is not None:
            result['RuleType'] = self.rule_type
        if self.warn_level is not None:
            result['WarnLevel'] = self.warn_level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('RiskLevelId') is not None:
            self.risk_level_id = m.get('RiskLevelId')
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        if m.get('WarnLevel') is not None:
            self.warn_level = m.get('WarnLevel')
        return self


class ModifyRuleResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyRuleResponseBody = None,
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
            temp_model = ModifyRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyRuleStatusRequest(TeaModel):
    def __init__(
        self,
        id: int = None,
        ids: str = None,
        lang: str = None,
        status: int = None,
    ):
        self.id = id
        self.ids = ids
        self.lang = lang
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
        if self.ids is not None:
            result['Ids'] = self.ids
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Ids') is not None:
            self.ids = m.get('Ids')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ModifyRuleStatusResponseBody(TeaModel):
    def __init__(
        self,
        failed_ids: str = None,
        request_id: str = None,
    ):
        self.failed_ids = failed_ids
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.failed_ids is not None:
            result['FailedIds'] = self.failed_ids
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FailedIds') is not None:
            self.failed_ids = m.get('FailedIds')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyRuleStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyRuleStatusResponseBody = None,
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
            temp_model = ModifyRuleStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopMaskingProcessRequest(TeaModel):
    def __init__(
        self,
        id: int = None,
        lang: str = None,
    ):
        self.id = id
        self.lang = lang

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.lang is not None:
            result['Lang'] = self.lang
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        return self


class StopMaskingProcessResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StopMaskingProcessResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StopMaskingProcessResponseBody = None,
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
            temp_model = StopMaskingProcessResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


