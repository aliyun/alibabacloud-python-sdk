# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List, Any


class CheckUpgradeItemRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        region_id: str = None,
        role_for: str = None,
        upgrade_item_id: str = None,
    ):
        self.lang = lang
        self.region_id = region_id
        self.role_for = role_for
        self.upgrade_item_id = upgrade_item_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.role_for is not None:
            result['RoleFor'] = self.role_for
        if self.upgrade_item_id is not None:
            result['UpgradeItemId'] = self.upgrade_item_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')
        if m.get('UpgradeItemId') is not None:
            self.upgrade_item_id = m.get('UpgradeItemId')
        return self


class CheckUpgradeItemResponseBodyUpgradeItem(TeaModel):
    def __init__(
        self,
        check_result: str = None,
        check_status: str = None,
        upgrade_item_id: str = None,
    ):
        self.check_result = check_result
        self.check_status = check_status
        self.upgrade_item_id = upgrade_item_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_result is not None:
            result['CheckResult'] = self.check_result
        if self.check_status is not None:
            result['CheckStatus'] = self.check_status
        if self.upgrade_item_id is not None:
            result['UpgradeItemId'] = self.upgrade_item_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckResult') is not None:
            self.check_result = m.get('CheckResult')
        if m.get('CheckStatus') is not None:
            self.check_status = m.get('CheckStatus')
        if m.get('UpgradeItemId') is not None:
            self.upgrade_item_id = m.get('UpgradeItemId')
        return self


class CheckUpgradeItemResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        upgrade_item: CheckUpgradeItemResponseBodyUpgradeItem = None,
    ):
        self.request_id = request_id
        self.upgrade_item = upgrade_item

    def validate(self):
        if self.upgrade_item:
            self.upgrade_item.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.upgrade_item is not None:
            result['UpgradeItem'] = self.upgrade_item.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UpgradeItem') is not None:
            temp_model = CheckUpgradeItemResponseBodyUpgradeItem()
            self.upgrade_item = temp_model.from_map(m['UpgradeItem'])
        return self


class CheckUpgradeItemResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CheckUpgradeItemResponseBody = None,
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
            temp_model = CheckUpgradeItemResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDataIngestionRequest(TeaModel):
    def __init__(
        self,
        capacity_count: int = None,
        data_ingestion_mode: str = None,
        data_ingestion_state_code: str = None,
        data_ingestion_type: str = None,
        data_source_editable: bool = None,
        data_source_id: str = None,
        lang: str = None,
        normalization_rule_editable: bool = None,
        normalization_rule_id: str = None,
        product_id: str = None,
        region_id: str = None,
        role_for: int = None,
        scan_data_source_id: str = None,
        stream_job_id: str = None,
        update_time: int = None,
    ):
        self.capacity_count = capacity_count
        self.data_ingestion_mode = data_ingestion_mode
        self.data_ingestion_state_code = data_ingestion_state_code
        self.data_ingestion_type = data_ingestion_type
        self.data_source_editable = data_source_editable
        self.data_source_id = data_source_id
        self.lang = lang
        self.normalization_rule_editable = normalization_rule_editable
        self.normalization_rule_id = normalization_rule_id
        self.product_id = product_id
        self.region_id = region_id
        self.role_for = role_for
        self.scan_data_source_id = scan_data_source_id
        self.stream_job_id = stream_job_id
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.capacity_count is not None:
            result['CapacityCount'] = self.capacity_count
        if self.data_ingestion_mode is not None:
            result['DataIngestionMode'] = self.data_ingestion_mode
        if self.data_ingestion_state_code is not None:
            result['DataIngestionStateCode'] = self.data_ingestion_state_code
        if self.data_ingestion_type is not None:
            result['DataIngestionType'] = self.data_ingestion_type
        if self.data_source_editable is not None:
            result['DataSourceEditable'] = self.data_source_editable
        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.normalization_rule_editable is not None:
            result['NormalizationRuleEditable'] = self.normalization_rule_editable
        if self.normalization_rule_id is not None:
            result['NormalizationRuleId'] = self.normalization_rule_id
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.role_for is not None:
            result['RoleFor'] = self.role_for
        if self.scan_data_source_id is not None:
            result['ScanDataSourceId'] = self.scan_data_source_id
        if self.stream_job_id is not None:
            result['StreamJobId'] = self.stream_job_id
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CapacityCount') is not None:
            self.capacity_count = m.get('CapacityCount')
        if m.get('DataIngestionMode') is not None:
            self.data_ingestion_mode = m.get('DataIngestionMode')
        if m.get('DataIngestionStateCode') is not None:
            self.data_ingestion_state_code = m.get('DataIngestionStateCode')
        if m.get('DataIngestionType') is not None:
            self.data_ingestion_type = m.get('DataIngestionType')
        if m.get('DataSourceEditable') is not None:
            self.data_source_editable = m.get('DataSourceEditable')
        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('NormalizationRuleEditable') is not None:
            self.normalization_rule_editable = m.get('NormalizationRuleEditable')
        if m.get('NormalizationRuleId') is not None:
            self.normalization_rule_id = m.get('NormalizationRuleId')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')
        if m.get('ScanDataSourceId') is not None:
            self.scan_data_source_id = m.get('ScanDataSourceId')
        if m.get('StreamJobId') is not None:
            self.stream_job_id = m.get('StreamJobId')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class CreateDataIngestionResponseBody(TeaModel):
    def __init__(
        self,
        data_ingestion_id: str = None,
        request_id: str = None,
    ):
        self.data_ingestion_id = data_ingestion_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_ingestion_id is not None:
            result['DataIngestionId'] = self.data_ingestion_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataIngestionId') is not None:
            self.data_ingestion_id = m.get('DataIngestionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateDataIngestionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateDataIngestionResponseBody = None,
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
            temp_model = CreateDataIngestionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDataSetRequestIpWhitelistRecognizers(TeaModel):
    def __init__(
        self,
        auto_recognize_status: str = None,
        ip_whitelist_recognizer_type: str = None,
        recognize_scope: str = None,
    ):
        self.auto_recognize_status = auto_recognize_status
        self.ip_whitelist_recognizer_type = ip_whitelist_recognizer_type
        self.recognize_scope = recognize_scope

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_recognize_status is not None:
            result['AutoRecognizeStatus'] = self.auto_recognize_status
        if self.ip_whitelist_recognizer_type is not None:
            result['IpWhitelistRecognizerType'] = self.ip_whitelist_recognizer_type
        if self.recognize_scope is not None:
            result['RecognizeScope'] = self.recognize_scope
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoRecognizeStatus') is not None:
            self.auto_recognize_status = m.get('AutoRecognizeStatus')
        if m.get('IpWhitelistRecognizerType') is not None:
            self.ip_whitelist_recognizer_type = m.get('IpWhitelistRecognizerType')
        if m.get('RecognizeScope') is not None:
            self.recognize_scope = m.get('RecognizeScope')
        return self


class CreateDataSetRequest(TeaModel):
    def __init__(
        self,
        data_set_description: str = None,
        data_set_field_key_name: str = None,
        data_set_file_name: str = None,
        data_set_name: str = None,
        data_set_status: int = None,
        data_set_type: str = None,
        ip_whitelist_recognizers: List[CreateDataSetRequestIpWhitelistRecognizers] = None,
        lang: str = None,
        region_id: str = None,
        role_for: int = None,
    ):
        self.data_set_description = data_set_description
        # This parameter is required.
        self.data_set_field_key_name = data_set_field_key_name
        # This parameter is required.
        self.data_set_file_name = data_set_file_name
        # This parameter is required.
        self.data_set_name = data_set_name
        self.data_set_status = data_set_status
        self.data_set_type = data_set_type
        self.ip_whitelist_recognizers = ip_whitelist_recognizers
        self.lang = lang
        self.region_id = region_id
        self.role_for = role_for

    def validate(self):
        if self.ip_whitelist_recognizers:
            for k in self.ip_whitelist_recognizers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_set_description is not None:
            result['DataSetDescription'] = self.data_set_description
        if self.data_set_field_key_name is not None:
            result['DataSetFieldKeyName'] = self.data_set_field_key_name
        if self.data_set_file_name is not None:
            result['DataSetFileName'] = self.data_set_file_name
        if self.data_set_name is not None:
            result['DataSetName'] = self.data_set_name
        if self.data_set_status is not None:
            result['DataSetStatus'] = self.data_set_status
        if self.data_set_type is not None:
            result['DataSetType'] = self.data_set_type
        result['IpWhitelistRecognizers'] = []
        if self.ip_whitelist_recognizers is not None:
            for k in self.ip_whitelist_recognizers:
                result['IpWhitelistRecognizers'].append(k.to_map() if k else None)
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.role_for is not None:
            result['RoleFor'] = self.role_for
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSetDescription') is not None:
            self.data_set_description = m.get('DataSetDescription')
        if m.get('DataSetFieldKeyName') is not None:
            self.data_set_field_key_name = m.get('DataSetFieldKeyName')
        if m.get('DataSetFileName') is not None:
            self.data_set_file_name = m.get('DataSetFileName')
        if m.get('DataSetName') is not None:
            self.data_set_name = m.get('DataSetName')
        if m.get('DataSetStatus') is not None:
            self.data_set_status = m.get('DataSetStatus')
        if m.get('DataSetType') is not None:
            self.data_set_type = m.get('DataSetType')
        self.ip_whitelist_recognizers = []
        if m.get('IpWhitelistRecognizers') is not None:
            for k in m.get('IpWhitelistRecognizers'):
                temp_model = CreateDataSetRequestIpWhitelistRecognizers()
                self.ip_whitelist_recognizers.append(temp_model.from_map(k))
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')
        return self


class CreateDataSetResponseBodyDataSetRecordStatistic(TeaModel):
    def __init__(
        self,
        data_set_id: str = None,
        new_data_set_record_count: int = None,
    ):
        self.data_set_id = data_set_id
        self.new_data_set_record_count = new_data_set_record_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_set_id is not None:
            result['DataSetId'] = self.data_set_id
        if self.new_data_set_record_count is not None:
            result['NewDataSetRecordCount'] = self.new_data_set_record_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSetId') is not None:
            self.data_set_id = m.get('DataSetId')
        if m.get('NewDataSetRecordCount') is not None:
            self.new_data_set_record_count = m.get('NewDataSetRecordCount')
        return self


class CreateDataSetResponseBody(TeaModel):
    def __init__(
        self,
        data_set_record_statistic: CreateDataSetResponseBodyDataSetRecordStatistic = None,
        request_id: str = None,
    ):
        self.data_set_record_statistic = data_set_record_statistic
        self.request_id = request_id

    def validate(self):
        if self.data_set_record_statistic:
            self.data_set_record_statistic.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_set_record_statistic is not None:
            result['DataSetRecordStatistic'] = self.data_set_record_statistic.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSetRecordStatistic') is not None:
            temp_model = CreateDataSetResponseBodyDataSetRecordStatistic()
            self.data_set_record_statistic = temp_model.from_map(m['DataSetRecordStatistic'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateDataSetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateDataSetResponseBody = None,
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
            temp_model = CreateDataSetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDataSourceRequestDataSourceStores(TeaModel):
    def __init__(
        self,
        create_time: int = None,
        data_source_store_from: str = None,
        data_source_store_id: str = None,
        data_source_store_status: str = None,
        log_project_name: str = None,
        log_region_id: str = None,
        log_store_name: str = None,
        update_time: int = None,
    ):
        self.create_time = create_time
        self.data_source_store_from = data_source_store_from
        self.data_source_store_id = data_source_store_id
        self.data_source_store_status = data_source_store_status
        self.log_project_name = log_project_name
        self.log_region_id = log_region_id
        self.log_store_name = log_store_name
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.data_source_store_from is not None:
            result['DataSourceStoreFrom'] = self.data_source_store_from
        if self.data_source_store_id is not None:
            result['DataSourceStoreId'] = self.data_source_store_id
        if self.data_source_store_status is not None:
            result['DataSourceStoreStatus'] = self.data_source_store_status
        if self.log_project_name is not None:
            result['LogProjectName'] = self.log_project_name
        if self.log_region_id is not None:
            result['LogRegionId'] = self.log_region_id
        if self.log_store_name is not None:
            result['LogStoreName'] = self.log_store_name
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DataSourceStoreFrom') is not None:
            self.data_source_store_from = m.get('DataSourceStoreFrom')
        if m.get('DataSourceStoreId') is not None:
            self.data_source_store_id = m.get('DataSourceStoreId')
        if m.get('DataSourceStoreStatus') is not None:
            self.data_source_store_status = m.get('DataSourceStoreStatus')
        if m.get('LogProjectName') is not None:
            self.log_project_name = m.get('LogProjectName')
        if m.get('LogRegionId') is not None:
            self.log_region_id = m.get('LogRegionId')
        if m.get('LogStoreName') is not None:
            self.log_store_name = m.get('LogStoreName')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class CreateDataSourceRequest(TeaModel):
    def __init__(
        self,
        data_source_from: str = None,
        data_source_ids: List[str] = None,
        data_source_name: str = None,
        data_source_recognize_enabled: bool = None,
        data_source_recognizer: str = None,
        data_source_references: List[str] = None,
        data_source_stores: List[CreateDataSourceRequestDataSourceStores] = None,
        data_source_template_id: str = None,
        data_source_type: str = None,
        lang: str = None,
        log_project_name: str = None,
        log_region_id: str = None,
        log_store_name: str = None,
        log_user_id: int = None,
        order: str = None,
        region_id: str = None,
        role_for: int = None,
        update_time: int = None,
    ):
        self.data_source_from = data_source_from
        self.data_source_ids = data_source_ids
        self.data_source_name = data_source_name
        self.data_source_recognize_enabled = data_source_recognize_enabled
        self.data_source_recognizer = data_source_recognizer
        self.data_source_references = data_source_references
        self.data_source_stores = data_source_stores
        self.data_source_template_id = data_source_template_id
        self.data_source_type = data_source_type
        self.lang = lang
        self.log_project_name = log_project_name
        self.log_region_id = log_region_id
        self.log_store_name = log_store_name
        self.log_user_id = log_user_id
        self.order = order
        self.region_id = region_id
        self.role_for = role_for
        self.update_time = update_time

    def validate(self):
        if self.data_source_stores:
            for k in self.data_source_stores:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_source_from is not None:
            result['DataSourceFrom'] = self.data_source_from
        if self.data_source_ids is not None:
            result['DataSourceIds'] = self.data_source_ids
        if self.data_source_name is not None:
            result['DataSourceName'] = self.data_source_name
        if self.data_source_recognize_enabled is not None:
            result['DataSourceRecognizeEnabled'] = self.data_source_recognize_enabled
        if self.data_source_recognizer is not None:
            result['DataSourceRecognizer'] = self.data_source_recognizer
        if self.data_source_references is not None:
            result['DataSourceReferences'] = self.data_source_references
        result['DataSourceStores'] = []
        if self.data_source_stores is not None:
            for k in self.data_source_stores:
                result['DataSourceStores'].append(k.to_map() if k else None)
        if self.data_source_template_id is not None:
            result['DataSourceTemplateId'] = self.data_source_template_id
        if self.data_source_type is not None:
            result['DataSourceType'] = self.data_source_type
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.log_project_name is not None:
            result['LogProjectName'] = self.log_project_name
        if self.log_region_id is not None:
            result['LogRegionId'] = self.log_region_id
        if self.log_store_name is not None:
            result['LogStoreName'] = self.log_store_name
        if self.log_user_id is not None:
            result['LogUserId'] = self.log_user_id
        if self.order is not None:
            result['Order'] = self.order
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.role_for is not None:
            result['RoleFor'] = self.role_for
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSourceFrom') is not None:
            self.data_source_from = m.get('DataSourceFrom')
        if m.get('DataSourceIds') is not None:
            self.data_source_ids = m.get('DataSourceIds')
        if m.get('DataSourceName') is not None:
            self.data_source_name = m.get('DataSourceName')
        if m.get('DataSourceRecognizeEnabled') is not None:
            self.data_source_recognize_enabled = m.get('DataSourceRecognizeEnabled')
        if m.get('DataSourceRecognizer') is not None:
            self.data_source_recognizer = m.get('DataSourceRecognizer')
        if m.get('DataSourceReferences') is not None:
            self.data_source_references = m.get('DataSourceReferences')
        self.data_source_stores = []
        if m.get('DataSourceStores') is not None:
            for k in m.get('DataSourceStores'):
                temp_model = CreateDataSourceRequestDataSourceStores()
                self.data_source_stores.append(temp_model.from_map(k))
        if m.get('DataSourceTemplateId') is not None:
            self.data_source_template_id = m.get('DataSourceTemplateId')
        if m.get('DataSourceType') is not None:
            self.data_source_type = m.get('DataSourceType')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('LogProjectName') is not None:
            self.log_project_name = m.get('LogProjectName')
        if m.get('LogRegionId') is not None:
            self.log_region_id = m.get('LogRegionId')
        if m.get('LogStoreName') is not None:
            self.log_store_name = m.get('LogStoreName')
        if m.get('LogUserId') is not None:
            self.log_user_id = m.get('LogUserId')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class CreateDataSourceShrinkRequestDataSourceStores(TeaModel):
    def __init__(
        self,
        create_time: int = None,
        data_source_store_from: str = None,
        data_source_store_id: str = None,
        data_source_store_status: str = None,
        log_project_name: str = None,
        log_region_id: str = None,
        log_store_name: str = None,
        update_time: int = None,
    ):
        self.create_time = create_time
        self.data_source_store_from = data_source_store_from
        self.data_source_store_id = data_source_store_id
        self.data_source_store_status = data_source_store_status
        self.log_project_name = log_project_name
        self.log_region_id = log_region_id
        self.log_store_name = log_store_name
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.data_source_store_from is not None:
            result['DataSourceStoreFrom'] = self.data_source_store_from
        if self.data_source_store_id is not None:
            result['DataSourceStoreId'] = self.data_source_store_id
        if self.data_source_store_status is not None:
            result['DataSourceStoreStatus'] = self.data_source_store_status
        if self.log_project_name is not None:
            result['LogProjectName'] = self.log_project_name
        if self.log_region_id is not None:
            result['LogRegionId'] = self.log_region_id
        if self.log_store_name is not None:
            result['LogStoreName'] = self.log_store_name
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DataSourceStoreFrom') is not None:
            self.data_source_store_from = m.get('DataSourceStoreFrom')
        if m.get('DataSourceStoreId') is not None:
            self.data_source_store_id = m.get('DataSourceStoreId')
        if m.get('DataSourceStoreStatus') is not None:
            self.data_source_store_status = m.get('DataSourceStoreStatus')
        if m.get('LogProjectName') is not None:
            self.log_project_name = m.get('LogProjectName')
        if m.get('LogRegionId') is not None:
            self.log_region_id = m.get('LogRegionId')
        if m.get('LogStoreName') is not None:
            self.log_store_name = m.get('LogStoreName')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class CreateDataSourceShrinkRequest(TeaModel):
    def __init__(
        self,
        data_source_from: str = None,
        data_source_ids_shrink: str = None,
        data_source_name: str = None,
        data_source_recognize_enabled: bool = None,
        data_source_recognizer: str = None,
        data_source_references_shrink: str = None,
        data_source_stores: List[CreateDataSourceShrinkRequestDataSourceStores] = None,
        data_source_template_id: str = None,
        data_source_type: str = None,
        lang: str = None,
        log_project_name: str = None,
        log_region_id: str = None,
        log_store_name: str = None,
        log_user_id: int = None,
        order: str = None,
        region_id: str = None,
        role_for: int = None,
        update_time: int = None,
    ):
        self.data_source_from = data_source_from
        self.data_source_ids_shrink = data_source_ids_shrink
        self.data_source_name = data_source_name
        self.data_source_recognize_enabled = data_source_recognize_enabled
        self.data_source_recognizer = data_source_recognizer
        self.data_source_references_shrink = data_source_references_shrink
        self.data_source_stores = data_source_stores
        self.data_source_template_id = data_source_template_id
        self.data_source_type = data_source_type
        self.lang = lang
        self.log_project_name = log_project_name
        self.log_region_id = log_region_id
        self.log_store_name = log_store_name
        self.log_user_id = log_user_id
        self.order = order
        self.region_id = region_id
        self.role_for = role_for
        self.update_time = update_time

    def validate(self):
        if self.data_source_stores:
            for k in self.data_source_stores:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_source_from is not None:
            result['DataSourceFrom'] = self.data_source_from
        if self.data_source_ids_shrink is not None:
            result['DataSourceIds'] = self.data_source_ids_shrink
        if self.data_source_name is not None:
            result['DataSourceName'] = self.data_source_name
        if self.data_source_recognize_enabled is not None:
            result['DataSourceRecognizeEnabled'] = self.data_source_recognize_enabled
        if self.data_source_recognizer is not None:
            result['DataSourceRecognizer'] = self.data_source_recognizer
        if self.data_source_references_shrink is not None:
            result['DataSourceReferences'] = self.data_source_references_shrink
        result['DataSourceStores'] = []
        if self.data_source_stores is not None:
            for k in self.data_source_stores:
                result['DataSourceStores'].append(k.to_map() if k else None)
        if self.data_source_template_id is not None:
            result['DataSourceTemplateId'] = self.data_source_template_id
        if self.data_source_type is not None:
            result['DataSourceType'] = self.data_source_type
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.log_project_name is not None:
            result['LogProjectName'] = self.log_project_name
        if self.log_region_id is not None:
            result['LogRegionId'] = self.log_region_id
        if self.log_store_name is not None:
            result['LogStoreName'] = self.log_store_name
        if self.log_user_id is not None:
            result['LogUserId'] = self.log_user_id
        if self.order is not None:
            result['Order'] = self.order
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.role_for is not None:
            result['RoleFor'] = self.role_for
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSourceFrom') is not None:
            self.data_source_from = m.get('DataSourceFrom')
        if m.get('DataSourceIds') is not None:
            self.data_source_ids_shrink = m.get('DataSourceIds')
        if m.get('DataSourceName') is not None:
            self.data_source_name = m.get('DataSourceName')
        if m.get('DataSourceRecognizeEnabled') is not None:
            self.data_source_recognize_enabled = m.get('DataSourceRecognizeEnabled')
        if m.get('DataSourceRecognizer') is not None:
            self.data_source_recognizer = m.get('DataSourceRecognizer')
        if m.get('DataSourceReferences') is not None:
            self.data_source_references_shrink = m.get('DataSourceReferences')
        self.data_source_stores = []
        if m.get('DataSourceStores') is not None:
            for k in m.get('DataSourceStores'):
                temp_model = CreateDataSourceShrinkRequestDataSourceStores()
                self.data_source_stores.append(temp_model.from_map(k))
        if m.get('DataSourceTemplateId') is not None:
            self.data_source_template_id = m.get('DataSourceTemplateId')
        if m.get('DataSourceType') is not None:
            self.data_source_type = m.get('DataSourceType')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('LogProjectName') is not None:
            self.log_project_name = m.get('LogProjectName')
        if m.get('LogRegionId') is not None:
            self.log_region_id = m.get('LogRegionId')
        if m.get('LogStoreName') is not None:
            self.log_store_name = m.get('LogStoreName')
        if m.get('LogUserId') is not None:
            self.log_user_id = m.get('LogUserId')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class CreateDataSourceResponseBody(TeaModel):
    def __init__(
        self,
        data_source_id: str = None,
        request_id: str = None,
    ):
        self.data_source_id = data_source_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateDataSourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateDataSourceResponseBody = None,
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
            temp_model = CreateDataSourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDetectionRuleRequest(TeaModel):
    def __init__(
        self,
        alert_att_ck: str = None,
        alert_level: str = None,
        alert_schema_id: str = None,
        alert_tactic_id: str = None,
        alert_threshold_count: int = None,
        alert_threshold_group: str = None,
        alert_threshold_period: str = None,
        alert_type: str = None,
        detection_expression_content: str = None,
        detection_expression_type: str = None,
        detection_rule_description: str = None,
        detection_rule_name: str = None,
        detection_rule_status: str = None,
        detection_rule_type: str = None,
        entity_mappings: str = None,
        incident_aggregation_expression: str = None,
        incident_aggregation_type: str = None,
        lang: str = None,
        log_category_id: str = None,
        log_schema_id: str = None,
        playbook_parameters: str = None,
        playbook_uuid: str = None,
        region_id: str = None,
        role_for: int = None,
        schedule_begin_time: int = None,
        schedule_expression: str = None,
        schedule_max_retries: int = None,
        schedule_max_timeout: int = None,
        schedule_type: str = None,
        schedule_window: str = None,
    ):
        self.alert_att_ck = alert_att_ck
        # This parameter is required.
        self.alert_level = alert_level
        # This parameter is required.
        self.alert_schema_id = alert_schema_id
        self.alert_tactic_id = alert_tactic_id
        self.alert_threshold_count = alert_threshold_count
        self.alert_threshold_group = alert_threshold_group
        self.alert_threshold_period = alert_threshold_period
        # This parameter is required.
        self.alert_type = alert_type
        self.detection_expression_content = detection_expression_content
        self.detection_expression_type = detection_expression_type
        self.detection_rule_description = detection_rule_description
        # This parameter is required.
        self.detection_rule_name = detection_rule_name
        self.detection_rule_status = detection_rule_status
        # This parameter is required.
        self.detection_rule_type = detection_rule_type
        self.entity_mappings = entity_mappings
        self.incident_aggregation_expression = incident_aggregation_expression
        self.incident_aggregation_type = incident_aggregation_type
        self.lang = lang
        self.log_category_id = log_category_id
        # This parameter is required.
        self.log_schema_id = log_schema_id
        self.playbook_parameters = playbook_parameters
        self.playbook_uuid = playbook_uuid
        self.region_id = region_id
        self.role_for = role_for
        self.schedule_begin_time = schedule_begin_time
        self.schedule_expression = schedule_expression
        self.schedule_max_retries = schedule_max_retries
        self.schedule_max_timeout = schedule_max_timeout
        self.schedule_type = schedule_type
        self.schedule_window = schedule_window

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_att_ck is not None:
            result['AlertAttCk'] = self.alert_att_ck
        if self.alert_level is not None:
            result['AlertLevel'] = self.alert_level
        if self.alert_schema_id is not None:
            result['AlertSchemaId'] = self.alert_schema_id
        if self.alert_tactic_id is not None:
            result['AlertTacticId'] = self.alert_tactic_id
        if self.alert_threshold_count is not None:
            result['AlertThresholdCount'] = self.alert_threshold_count
        if self.alert_threshold_group is not None:
            result['AlertThresholdGroup'] = self.alert_threshold_group
        if self.alert_threshold_period is not None:
            result['AlertThresholdPeriod'] = self.alert_threshold_period
        if self.alert_type is not None:
            result['AlertType'] = self.alert_type
        if self.detection_expression_content is not None:
            result['DetectionExpressionContent'] = self.detection_expression_content
        if self.detection_expression_type is not None:
            result['DetectionExpressionType'] = self.detection_expression_type
        if self.detection_rule_description is not None:
            result['DetectionRuleDescription'] = self.detection_rule_description
        if self.detection_rule_name is not None:
            result['DetectionRuleName'] = self.detection_rule_name
        if self.detection_rule_status is not None:
            result['DetectionRuleStatus'] = self.detection_rule_status
        if self.detection_rule_type is not None:
            result['DetectionRuleType'] = self.detection_rule_type
        if self.entity_mappings is not None:
            result['EntityMappings'] = self.entity_mappings
        if self.incident_aggregation_expression is not None:
            result['IncidentAggregationExpression'] = self.incident_aggregation_expression
        if self.incident_aggregation_type is not None:
            result['IncidentAggregationType'] = self.incident_aggregation_type
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.log_category_id is not None:
            result['LogCategoryId'] = self.log_category_id
        if self.log_schema_id is not None:
            result['LogSchemaId'] = self.log_schema_id
        if self.playbook_parameters is not None:
            result['PlaybookParameters'] = self.playbook_parameters
        if self.playbook_uuid is not None:
            result['PlaybookUuid'] = self.playbook_uuid
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.role_for is not None:
            result['RoleFor'] = self.role_for
        if self.schedule_begin_time is not None:
            result['ScheduleBeginTime'] = self.schedule_begin_time
        if self.schedule_expression is not None:
            result['ScheduleExpression'] = self.schedule_expression
        if self.schedule_max_retries is not None:
            result['ScheduleMaxRetries'] = self.schedule_max_retries
        if self.schedule_max_timeout is not None:
            result['ScheduleMaxTimeout'] = self.schedule_max_timeout
        if self.schedule_type is not None:
            result['ScheduleType'] = self.schedule_type
        if self.schedule_window is not None:
            result['ScheduleWindow'] = self.schedule_window
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertAttCk') is not None:
            self.alert_att_ck = m.get('AlertAttCk')
        if m.get('AlertLevel') is not None:
            self.alert_level = m.get('AlertLevel')
        if m.get('AlertSchemaId') is not None:
            self.alert_schema_id = m.get('AlertSchemaId')
        if m.get('AlertTacticId') is not None:
            self.alert_tactic_id = m.get('AlertTacticId')
        if m.get('AlertThresholdCount') is not None:
            self.alert_threshold_count = m.get('AlertThresholdCount')
        if m.get('AlertThresholdGroup') is not None:
            self.alert_threshold_group = m.get('AlertThresholdGroup')
        if m.get('AlertThresholdPeriod') is not None:
            self.alert_threshold_period = m.get('AlertThresholdPeriod')
        if m.get('AlertType') is not None:
            self.alert_type = m.get('AlertType')
        if m.get('DetectionExpressionContent') is not None:
            self.detection_expression_content = m.get('DetectionExpressionContent')
        if m.get('DetectionExpressionType') is not None:
            self.detection_expression_type = m.get('DetectionExpressionType')
        if m.get('DetectionRuleDescription') is not None:
            self.detection_rule_description = m.get('DetectionRuleDescription')
        if m.get('DetectionRuleName') is not None:
            self.detection_rule_name = m.get('DetectionRuleName')
        if m.get('DetectionRuleStatus') is not None:
            self.detection_rule_status = m.get('DetectionRuleStatus')
        if m.get('DetectionRuleType') is not None:
            self.detection_rule_type = m.get('DetectionRuleType')
        if m.get('EntityMappings') is not None:
            self.entity_mappings = m.get('EntityMappings')
        if m.get('IncidentAggregationExpression') is not None:
            self.incident_aggregation_expression = m.get('IncidentAggregationExpression')
        if m.get('IncidentAggregationType') is not None:
            self.incident_aggregation_type = m.get('IncidentAggregationType')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('LogCategoryId') is not None:
            self.log_category_id = m.get('LogCategoryId')
        if m.get('LogSchemaId') is not None:
            self.log_schema_id = m.get('LogSchemaId')
        if m.get('PlaybookParameters') is not None:
            self.playbook_parameters = m.get('PlaybookParameters')
        if m.get('PlaybookUuid') is not None:
            self.playbook_uuid = m.get('PlaybookUuid')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')
        if m.get('ScheduleBeginTime') is not None:
            self.schedule_begin_time = m.get('ScheduleBeginTime')
        if m.get('ScheduleExpression') is not None:
            self.schedule_expression = m.get('ScheduleExpression')
        if m.get('ScheduleMaxRetries') is not None:
            self.schedule_max_retries = m.get('ScheduleMaxRetries')
        if m.get('ScheduleMaxTimeout') is not None:
            self.schedule_max_timeout = m.get('ScheduleMaxTimeout')
        if m.get('ScheduleType') is not None:
            self.schedule_type = m.get('ScheduleType')
        if m.get('ScheduleWindow') is not None:
            self.schedule_window = m.get('ScheduleWindow')
        return self


class CreateDetectionRuleResponseBody(TeaModel):
    def __init__(
        self,
        detection_rule_id: str = None,
        request_id: str = None,
    ):
        self.detection_rule_id = detection_rule_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.detection_rule_id is not None:
            result['DetectionRuleId'] = self.detection_rule_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DetectionRuleId') is not None:
            self.detection_rule_id = m.get('DetectionRuleId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateDetectionRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateDetectionRuleResponseBody = None,
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
            temp_model = CreateDetectionRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateExportTaskRequest(TeaModel):
    def __init__(
        self,
        export_task_parameter: str = None,
        export_task_type: str = None,
        lang: str = None,
        region_id: str = None,
        role_for: int = None,
    ):
        self.export_task_parameter = export_task_parameter
        self.export_task_type = export_task_type
        self.lang = lang
        self.region_id = region_id
        self.role_for = role_for

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.export_task_parameter is not None:
            result['ExportTaskParameter'] = self.export_task_parameter
        if self.export_task_type is not None:
            result['ExportTaskType'] = self.export_task_type
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.role_for is not None:
            result['RoleFor'] = self.role_for
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExportTaskParameter') is not None:
            self.export_task_parameter = m.get('ExportTaskParameter')
        if m.get('ExportTaskType') is not None:
            self.export_task_type = m.get('ExportTaskType')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')
        return self


class CreateExportTaskResponseBody(TeaModel):
    def __init__(
        self,
        file_name: str = None,
        id: int = None,
        request_id: str = None,
    ):
        self.file_name = file_name
        self.id = id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.id is not None:
            result['Id'] = self.id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateExportTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateExportTaskResponseBody = None,
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
            temp_model = CreateExportTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateLogStoreRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        log_project_name: str = None,
        log_region_id: str = None,
        log_store_name: str = None,
        log_user_id: int = None,
        region_id: str = None,
        role_for: int = None,
    ):
        self.lang = lang
        self.log_project_name = log_project_name
        self.log_region_id = log_region_id
        self.log_store_name = log_store_name
        self.log_user_id = log_user_id
        self.region_id = region_id
        self.role_for = role_for

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.log_project_name is not None:
            result['LogProjectName'] = self.log_project_name
        if self.log_region_id is not None:
            result['LogRegionId'] = self.log_region_id
        if self.log_store_name is not None:
            result['LogStoreName'] = self.log_store_name
        if self.log_user_id is not None:
            result['LogUserId'] = self.log_user_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.role_for is not None:
            result['RoleFor'] = self.role_for
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('LogProjectName') is not None:
            self.log_project_name = m.get('LogProjectName')
        if m.get('LogRegionId') is not None:
            self.log_region_id = m.get('LogRegionId')
        if m.get('LogStoreName') is not None:
            self.log_store_name = m.get('LogStoreName')
        if m.get('LogUserId') is not None:
            self.log_user_id = m.get('LogUserId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')
        return self


class CreateLogStoreResponseBody(TeaModel):
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


class CreateLogStoreResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateLogStoreResponseBody = None,
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
            temp_model = CreateLogStoreResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateNormalizationRuleRequest(TeaModel):
    def __init__(
        self,
        extend_content_packed: str = None,
        lang: str = None,
        normalization_category_id: str = None,
        normalization_rule_description: str = None,
        normalization_rule_expression: str = None,
        normalization_rule_format: str = None,
        normalization_rule_ids: List[str] = None,
        normalization_rule_mode: str = None,
        normalization_rule_name: str = None,
        normalization_rule_type: str = None,
        normalization_rule_version: int = None,
        normalization_schema_id: str = None,
        order_field: str = None,
        product_id: str = None,
        region_id: str = None,
        role_for: int = None,
        vendor_id: str = None,
    ):
        self.extend_content_packed = extend_content_packed
        self.lang = lang
        self.normalization_category_id = normalization_category_id
        self.normalization_rule_description = normalization_rule_description
        self.normalization_rule_expression = normalization_rule_expression
        self.normalization_rule_format = normalization_rule_format
        self.normalization_rule_ids = normalization_rule_ids
        self.normalization_rule_mode = normalization_rule_mode
        self.normalization_rule_name = normalization_rule_name
        self.normalization_rule_type = normalization_rule_type
        self.normalization_rule_version = normalization_rule_version
        self.normalization_schema_id = normalization_schema_id
        self.order_field = order_field
        self.product_id = product_id
        self.region_id = region_id
        self.role_for = role_for
        self.vendor_id = vendor_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extend_content_packed is not None:
            result['ExtendContentPacked'] = self.extend_content_packed
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.normalization_category_id is not None:
            result['NormalizationCategoryId'] = self.normalization_category_id
        if self.normalization_rule_description is not None:
            result['NormalizationRuleDescription'] = self.normalization_rule_description
        if self.normalization_rule_expression is not None:
            result['NormalizationRuleExpression'] = self.normalization_rule_expression
        if self.normalization_rule_format is not None:
            result['NormalizationRuleFormat'] = self.normalization_rule_format
        if self.normalization_rule_ids is not None:
            result['NormalizationRuleIds'] = self.normalization_rule_ids
        if self.normalization_rule_mode is not None:
            result['NormalizationRuleMode'] = self.normalization_rule_mode
        if self.normalization_rule_name is not None:
            result['NormalizationRuleName'] = self.normalization_rule_name
        if self.normalization_rule_type is not None:
            result['NormalizationRuleType'] = self.normalization_rule_type
        if self.normalization_rule_version is not None:
            result['NormalizationRuleVersion'] = self.normalization_rule_version
        if self.normalization_schema_id is not None:
            result['NormalizationSchemaId'] = self.normalization_schema_id
        if self.order_field is not None:
            result['OrderField'] = self.order_field
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.role_for is not None:
            result['RoleFor'] = self.role_for
        if self.vendor_id is not None:
            result['VendorId'] = self.vendor_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExtendContentPacked') is not None:
            self.extend_content_packed = m.get('ExtendContentPacked')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('NormalizationCategoryId') is not None:
            self.normalization_category_id = m.get('NormalizationCategoryId')
        if m.get('NormalizationRuleDescription') is not None:
            self.normalization_rule_description = m.get('NormalizationRuleDescription')
        if m.get('NormalizationRuleExpression') is not None:
            self.normalization_rule_expression = m.get('NormalizationRuleExpression')
        if m.get('NormalizationRuleFormat') is not None:
            self.normalization_rule_format = m.get('NormalizationRuleFormat')
        if m.get('NormalizationRuleIds') is not None:
            self.normalization_rule_ids = m.get('NormalizationRuleIds')
        if m.get('NormalizationRuleMode') is not None:
            self.normalization_rule_mode = m.get('NormalizationRuleMode')
        if m.get('NormalizationRuleName') is not None:
            self.normalization_rule_name = m.get('NormalizationRuleName')
        if m.get('NormalizationRuleType') is not None:
            self.normalization_rule_type = m.get('NormalizationRuleType')
        if m.get('NormalizationRuleVersion') is not None:
            self.normalization_rule_version = m.get('NormalizationRuleVersion')
        if m.get('NormalizationSchemaId') is not None:
            self.normalization_schema_id = m.get('NormalizationSchemaId')
        if m.get('OrderField') is not None:
            self.order_field = m.get('OrderField')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')
        if m.get('VendorId') is not None:
            self.vendor_id = m.get('VendorId')
        return self


class CreateNormalizationRuleShrinkRequest(TeaModel):
    def __init__(
        self,
        extend_content_packed: str = None,
        lang: str = None,
        normalization_category_id: str = None,
        normalization_rule_description: str = None,
        normalization_rule_expression: str = None,
        normalization_rule_format: str = None,
        normalization_rule_ids_shrink: str = None,
        normalization_rule_mode: str = None,
        normalization_rule_name: str = None,
        normalization_rule_type: str = None,
        normalization_rule_version: int = None,
        normalization_schema_id: str = None,
        order_field: str = None,
        product_id: str = None,
        region_id: str = None,
        role_for: int = None,
        vendor_id: str = None,
    ):
        self.extend_content_packed = extend_content_packed
        self.lang = lang
        self.normalization_category_id = normalization_category_id
        self.normalization_rule_description = normalization_rule_description
        self.normalization_rule_expression = normalization_rule_expression
        self.normalization_rule_format = normalization_rule_format
        self.normalization_rule_ids_shrink = normalization_rule_ids_shrink
        self.normalization_rule_mode = normalization_rule_mode
        self.normalization_rule_name = normalization_rule_name
        self.normalization_rule_type = normalization_rule_type
        self.normalization_rule_version = normalization_rule_version
        self.normalization_schema_id = normalization_schema_id
        self.order_field = order_field
        self.product_id = product_id
        self.region_id = region_id
        self.role_for = role_for
        self.vendor_id = vendor_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extend_content_packed is not None:
            result['ExtendContentPacked'] = self.extend_content_packed
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.normalization_category_id is not None:
            result['NormalizationCategoryId'] = self.normalization_category_id
        if self.normalization_rule_description is not None:
            result['NormalizationRuleDescription'] = self.normalization_rule_description
        if self.normalization_rule_expression is not None:
            result['NormalizationRuleExpression'] = self.normalization_rule_expression
        if self.normalization_rule_format is not None:
            result['NormalizationRuleFormat'] = self.normalization_rule_format
        if self.normalization_rule_ids_shrink is not None:
            result['NormalizationRuleIds'] = self.normalization_rule_ids_shrink
        if self.normalization_rule_mode is not None:
            result['NormalizationRuleMode'] = self.normalization_rule_mode
        if self.normalization_rule_name is not None:
            result['NormalizationRuleName'] = self.normalization_rule_name
        if self.normalization_rule_type is not None:
            result['NormalizationRuleType'] = self.normalization_rule_type
        if self.normalization_rule_version is not None:
            result['NormalizationRuleVersion'] = self.normalization_rule_version
        if self.normalization_schema_id is not None:
            result['NormalizationSchemaId'] = self.normalization_schema_id
        if self.order_field is not None:
            result['OrderField'] = self.order_field
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.role_for is not None:
            result['RoleFor'] = self.role_for
        if self.vendor_id is not None:
            result['VendorId'] = self.vendor_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExtendContentPacked') is not None:
            self.extend_content_packed = m.get('ExtendContentPacked')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('NormalizationCategoryId') is not None:
            self.normalization_category_id = m.get('NormalizationCategoryId')
        if m.get('NormalizationRuleDescription') is not None:
            self.normalization_rule_description = m.get('NormalizationRuleDescription')
        if m.get('NormalizationRuleExpression') is not None:
            self.normalization_rule_expression = m.get('NormalizationRuleExpression')
        if m.get('NormalizationRuleFormat') is not None:
            self.normalization_rule_format = m.get('NormalizationRuleFormat')
        if m.get('NormalizationRuleIds') is not None:
            self.normalization_rule_ids_shrink = m.get('NormalizationRuleIds')
        if m.get('NormalizationRuleMode') is not None:
            self.normalization_rule_mode = m.get('NormalizationRuleMode')
        if m.get('NormalizationRuleName') is not None:
            self.normalization_rule_name = m.get('NormalizationRuleName')
        if m.get('NormalizationRuleType') is not None:
            self.normalization_rule_type = m.get('NormalizationRuleType')
        if m.get('NormalizationRuleVersion') is not None:
            self.normalization_rule_version = m.get('NormalizationRuleVersion')
        if m.get('NormalizationSchemaId') is not None:
            self.normalization_schema_id = m.get('NormalizationSchemaId')
        if m.get('OrderField') is not None:
            self.order_field = m.get('OrderField')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')
        if m.get('VendorId') is not None:
            self.vendor_id = m.get('VendorId')
        return self


class CreateNormalizationRuleResponseBody(TeaModel):
    def __init__(
        self,
        normalization_rule_id: str = None,
        request_id: str = None,
    ):
        self.normalization_rule_id = normalization_rule_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.normalization_rule_id is not None:
            result['NormalizationRuleId'] = self.normalization_rule_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NormalizationRuleId') is not None:
            self.normalization_rule_id = m.get('NormalizationRuleId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateNormalizationRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateNormalizationRuleResponseBody = None,
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
            temp_model = CreateNormalizationRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateProductRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        product_name: str = None,
        region_id: str = None,
        role_for: int = None,
        vendor_name: str = None,
    ):
        self.lang = lang
        self.product_name = product_name
        self.region_id = region_id
        self.role_for = role_for
        self.vendor_name = vendor_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.product_name is not None:
            result['ProductName'] = self.product_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.role_for is not None:
            result['RoleFor'] = self.role_for
        if self.vendor_name is not None:
            result['VendorName'] = self.vendor_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')
        if m.get('VendorName') is not None:
            self.vendor_name = m.get('VendorName')
        return self


class CreateProductResponseBody(TeaModel):
    def __init__(
        self,
        product_id: str = None,
        request_id: str = None,
    ):
        self.product_id = product_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateProductResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateProductResponseBody = None,
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
            temp_model = CreateProductResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateVendorRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        region_id: str = None,
        role_for: int = None,
        vendor_name: str = None,
    ):
        self.lang = lang
        self.region_id = region_id
        self.role_for = role_for
        self.vendor_name = vendor_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.role_for is not None:
            result['RoleFor'] = self.role_for
        if self.vendor_name is not None:
            result['VendorName'] = self.vendor_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')
        if m.get('VendorName') is not None:
            self.vendor_name = m.get('VendorName')
        return self


class CreateVendorResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        vendor_id: str = None,
    ):
        self.request_id = request_id
        self.vendor_id = vendor_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.vendor_id is not None:
            result['VendorId'] = self.vendor_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('VendorId') is not None:
            self.vendor_id = m.get('VendorId')
        return self


class CreateVendorResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateVendorResponseBody = None,
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
            temp_model = CreateVendorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDataIngestionRequest(TeaModel):
    def __init__(
        self,
        data_ingestion_id: str = None,
        lang: str = None,
        region_id: str = None,
        role_for: int = None,
    ):
        self.data_ingestion_id = data_ingestion_id
        self.lang = lang
        self.region_id = region_id
        self.role_for = role_for

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_ingestion_id is not None:
            result['DataIngestionId'] = self.data_ingestion_id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.role_for is not None:
            result['RoleFor'] = self.role_for
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataIngestionId') is not None:
            self.data_ingestion_id = m.get('DataIngestionId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')
        return self


class DeleteDataIngestionResponseBody(TeaModel):
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


class DeleteDataIngestionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteDataIngestionResponseBody = None,
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
            temp_model = DeleteDataIngestionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDataSetRequest(TeaModel):
    def __init__(
        self,
        data_set_id: str = None,
        lang: str = None,
        region_id: str = None,
        role_for: int = None,
    ):
        # This parameter is required.
        self.data_set_id = data_set_id
        self.lang = lang
        self.region_id = region_id
        self.role_for = role_for

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_set_id is not None:
            result['DataSetId'] = self.data_set_id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.role_for is not None:
            result['RoleFor'] = self.role_for
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSetId') is not None:
            self.data_set_id = m.get('DataSetId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')
        return self


class DeleteDataSetResponseBody(TeaModel):
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


class DeleteDataSetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteDataSetResponseBody = None,
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
            temp_model = DeleteDataSetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDataSetRecordRequest(TeaModel):
    def __init__(
        self,
        data_set_id: str = None,
        data_set_record_ids: str = None,
        lang: str = None,
        region_id: str = None,
        role_for: int = None,
    ):
        # This parameter is required.
        self.data_set_id = data_set_id
        # This parameter is required.
        self.data_set_record_ids = data_set_record_ids
        self.lang = lang
        self.region_id = region_id
        self.role_for = role_for

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_set_id is not None:
            result['DataSetId'] = self.data_set_id
        if self.data_set_record_ids is not None:
            result['DataSetRecordIds'] = self.data_set_record_ids
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.role_for is not None:
            result['RoleFor'] = self.role_for
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSetId') is not None:
            self.data_set_id = m.get('DataSetId')
        if m.get('DataSetRecordIds') is not None:
            self.data_set_record_ids = m.get('DataSetRecordIds')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')
        return self


class DeleteDataSetRecordResponseBody(TeaModel):
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


class DeleteDataSetRecordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteDataSetRecordResponseBody = None,
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
            temp_model = DeleteDataSetRecordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDataSourceRequest(TeaModel):
    def __init__(
        self,
        data_source_id: str = None,
        lang: str = None,
        region_id: str = None,
        role_for: int = None,
    ):
        self.data_source_id = data_source_id
        self.lang = lang
        self.region_id = region_id
        self.role_for = role_for

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.role_for is not None:
            result['RoleFor'] = self.role_for
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')
        return self


class DeleteDataSourceResponseBody(TeaModel):
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


class DeleteDetectionRuleRequest(TeaModel):
    def __init__(
        self,
        detection_rule_id: str = None,
        lang: str = None,
        region_id: str = None,
        role_for: int = None,
    ):
        # This parameter is required.
        self.detection_rule_id = detection_rule_id
        self.lang = lang
        self.region_id = region_id
        self.role_for = role_for

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.detection_rule_id is not None:
            result['DetectionRuleId'] = self.detection_rule_id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.role_for is not None:
            result['RoleFor'] = self.role_for
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DetectionRuleId') is not None:
            self.detection_rule_id = m.get('DetectionRuleId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')
        return self


class DeleteDetectionRuleResponseBody(TeaModel):
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


class DeleteDetectionRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteDetectionRuleResponseBody = None,
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
            temp_model = DeleteDetectionRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteLogStoreRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        log_project_name: str = None,
        log_region_id: str = None,
        log_store_name: str = None,
        log_user_id: int = None,
        region_id: str = None,
        role_for: int = None,
    ):
        self.lang = lang
        self.log_project_name = log_project_name
        self.log_region_id = log_region_id
        self.log_store_name = log_store_name
        self.log_user_id = log_user_id
        self.region_id = region_id
        self.role_for = role_for

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.log_project_name is not None:
            result['LogProjectName'] = self.log_project_name
        if self.log_region_id is not None:
            result['LogRegionId'] = self.log_region_id
        if self.log_store_name is not None:
            result['LogStoreName'] = self.log_store_name
        if self.log_user_id is not None:
            result['LogUserId'] = self.log_user_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.role_for is not None:
            result['RoleFor'] = self.role_for
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('LogProjectName') is not None:
            self.log_project_name = m.get('LogProjectName')
        if m.get('LogRegionId') is not None:
            self.log_region_id = m.get('LogRegionId')
        if m.get('LogStoreName') is not None:
            self.log_store_name = m.get('LogStoreName')
        if m.get('LogUserId') is not None:
            self.log_user_id = m.get('LogUserId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')
        return self


class DeleteLogStoreResponseBody(TeaModel):
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


class DeleteLogStoreResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteLogStoreResponseBody = None,
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
            temp_model = DeleteLogStoreResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteNormalizationRuleRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        normalization_rule_id: str = None,
        region_id: str = None,
        role_for: int = None,
    ):
        self.lang = lang
        self.normalization_rule_id = normalization_rule_id
        self.region_id = region_id
        self.role_for = role_for

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.normalization_rule_id is not None:
            result['NormalizationRuleId'] = self.normalization_rule_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.role_for is not None:
            result['RoleFor'] = self.role_for
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('NormalizationRuleId') is not None:
            self.normalization_rule_id = m.get('NormalizationRuleId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')
        return self


class DeleteNormalizationRuleResponseBody(TeaModel):
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


class DeleteNormalizationRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteNormalizationRuleResponseBody = None,
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
            temp_model = DeleteNormalizationRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteNormalizationRuleVersionRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        normalization_rule_id: str = None,
        normalization_rule_version: int = None,
        region_id: str = None,
        role_for: int = None,
    ):
        self.lang = lang
        self.normalization_rule_id = normalization_rule_id
        self.normalization_rule_version = normalization_rule_version
        self.region_id = region_id
        self.role_for = role_for

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.normalization_rule_id is not None:
            result['NormalizationRuleId'] = self.normalization_rule_id
        if self.normalization_rule_version is not None:
            result['NormalizationRuleVersion'] = self.normalization_rule_version
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.role_for is not None:
            result['RoleFor'] = self.role_for
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('NormalizationRuleId') is not None:
            self.normalization_rule_id = m.get('NormalizationRuleId')
        if m.get('NormalizationRuleVersion') is not None:
            self.normalization_rule_version = m.get('NormalizationRuleVersion')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')
        return self


class DeleteNormalizationRuleVersionResponseBody(TeaModel):
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


class DeleteNormalizationRuleVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteNormalizationRuleVersionResponseBody = None,
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
            temp_model = DeleteNormalizationRuleVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteProductRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        product_id: str = None,
        region_id: str = None,
        role_for: int = None,
    ):
        self.lang = lang
        self.product_id = product_id
        self.region_id = region_id
        self.role_for = role_for

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.role_for is not None:
            result['RoleFor'] = self.role_for
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')
        return self


class DeleteProductResponseBody(TeaModel):
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


class DeleteProductResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteProductResponseBody = None,
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
            temp_model = DeleteProductResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteVendorRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        region_id: str = None,
        role_for: int = None,
        vendor_id: str = None,
        vendor_name: str = None,
    ):
        self.lang = lang
        self.region_id = region_id
        self.role_for = role_for
        self.vendor_id = vendor_id
        self.vendor_name = vendor_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.role_for is not None:
            result['RoleFor'] = self.role_for
        if self.vendor_id is not None:
            result['VendorId'] = self.vendor_id
        if self.vendor_name is not None:
            result['VendorName'] = self.vendor_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')
        if m.get('VendorId') is not None:
            self.vendor_id = m.get('VendorId')
        if m.get('VendorName') is not None:
            self.vendor_name = m.get('VendorName')
        return self


class DeleteVendorResponseBody(TeaModel):
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


class DeleteVendorResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteVendorResponseBody = None,
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
            temp_model = DeleteVendorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableDataIngestionRequest(TeaModel):
    def __init__(
        self,
        data_ingestion_id: str = None,
        lang: str = None,
        region_id: str = None,
        role_for: int = None,
    ):
        self.data_ingestion_id = data_ingestion_id
        self.lang = lang
        self.region_id = region_id
        self.role_for = role_for

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_ingestion_id is not None:
            result['DataIngestionId'] = self.data_ingestion_id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.role_for is not None:
            result['RoleFor'] = self.role_for
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataIngestionId') is not None:
            self.data_ingestion_id = m.get('DataIngestionId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')
        return self


class DisableDataIngestionResponseBody(TeaModel):
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


class DisableDataIngestionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DisableDataIngestionResponseBody = None,
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
            temp_model = DisableDataIngestionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableDataIngestionRequest(TeaModel):
    def __init__(
        self,
        data_ingestion_id: str = None,
        lang: str = None,
        product_id: str = None,
        region_id: str = None,
        role_for: int = None,
    ):
        self.data_ingestion_id = data_ingestion_id
        self.lang = lang
        self.product_id = product_id
        self.region_id = region_id
        self.role_for = role_for

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_ingestion_id is not None:
            result['DataIngestionId'] = self.data_ingestion_id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.role_for is not None:
            result['RoleFor'] = self.role_for
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataIngestionId') is not None:
            self.data_ingestion_id = m.get('DataIngestionId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')
        return self


class EnableDataIngestionResponseBody(TeaModel):
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


class EnableDataIngestionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: EnableDataIngestionResponseBody = None,
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
            temp_model = EnableDataIngestionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExecuteLogQueryRequest(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        extend_content_packed: str = None,
        lang: str = None,
        log_project_name: str = None,
        log_query: str = None,
        log_region_id: str = None,
        log_store_name: str = None,
        log_user_id: int = None,
        normalization_schema_id: str = None,
        region_id: str = None,
        role_for: int = None,
        start_time: str = None,
    ):
        self.end_time = end_time
        self.extend_content_packed = extend_content_packed
        self.lang = lang
        self.log_project_name = log_project_name
        self.log_query = log_query
        self.log_region_id = log_region_id
        self.log_store_name = log_store_name
        self.log_user_id = log_user_id
        self.normalization_schema_id = normalization_schema_id
        self.region_id = region_id
        self.role_for = role_for
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
        if self.extend_content_packed is not None:
            result['ExtendContentPacked'] = self.extend_content_packed
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.log_project_name is not None:
            result['LogProjectName'] = self.log_project_name
        if self.log_query is not None:
            result['LogQuery'] = self.log_query
        if self.log_region_id is not None:
            result['LogRegionId'] = self.log_region_id
        if self.log_store_name is not None:
            result['LogStoreName'] = self.log_store_name
        if self.log_user_id is not None:
            result['LogUserId'] = self.log_user_id
        if self.normalization_schema_id is not None:
            result['NormalizationSchemaId'] = self.normalization_schema_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.role_for is not None:
            result['RoleFor'] = self.role_for
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('ExtendContentPacked') is not None:
            self.extend_content_packed = m.get('ExtendContentPacked')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('LogProjectName') is not None:
            self.log_project_name = m.get('LogProjectName')
        if m.get('LogQuery') is not None:
            self.log_query = m.get('LogQuery')
        if m.get('LogRegionId') is not None:
            self.log_region_id = m.get('LogRegionId')
        if m.get('LogStoreName') is not None:
            self.log_store_name = m.get('LogStoreName')
        if m.get('LogUserId') is not None:
            self.log_user_id = m.get('LogUserId')
        if m.get('NormalizationSchemaId') is not None:
            self.normalization_schema_id = m.get('NormalizationSchemaId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class ExecuteLogQueryResponseBody(TeaModel):
    def __init__(
        self,
        query_result: List[Any] = None,
        request_id: str = None,
    ):
        self.query_result = query_result
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.query_result is not None:
            result['QueryResult'] = self.query_result
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('QueryResult') is not None:
            self.query_result = m.get('QueryResult')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ExecuteLogQueryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ExecuteLogQueryResponseBody = None,
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
            temp_model = ExecuteLogQueryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExecuteUpgradeRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        region_id: str = None,
        role_for: str = None,
    ):
        self.lang = lang
        self.region_id = region_id
        self.role_for = role_for

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.role_for is not None:
            result['RoleFor'] = self.role_for
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')
        return self


class ExecuteUpgradeResponseBody(TeaModel):
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


class ExecuteUpgradeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ExecuteUpgradeResponseBody = None,
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
            temp_model = ExecuteUpgradeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDataBatchIngestionRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        region_id: str = None,
        role_for: int = None,
    ):
        self.lang = lang
        self.region_id = region_id
        self.role_for = role_for

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.role_for is not None:
            result['RoleFor'] = self.role_for
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')
        return self


class GetDataBatchIngestionResponseBodyDataBatchIngestionDataIngestions(TeaModel):
    def __init__(
        self,
        data_ingestion_id: str = None,
        data_ingestion_status: str = None,
        data_source_id: str = None,
        product_id: str = None,
        vendor_id: str = None,
    ):
        self.data_ingestion_id = data_ingestion_id
        self.data_ingestion_status = data_ingestion_status
        self.data_source_id = data_source_id
        self.product_id = product_id
        self.vendor_id = vendor_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_ingestion_id is not None:
            result['DataIngestionId'] = self.data_ingestion_id
        if self.data_ingestion_status is not None:
            result['DataIngestionStatus'] = self.data_ingestion_status
        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.vendor_id is not None:
            result['VendorId'] = self.vendor_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataIngestionId') is not None:
            self.data_ingestion_id = m.get('DataIngestionId')
        if m.get('DataIngestionStatus') is not None:
            self.data_ingestion_status = m.get('DataIngestionStatus')
        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('VendorId') is not None:
            self.vendor_id = m.get('VendorId')
        return self


class GetDataBatchIngestionResponseBodyDataBatchIngestion(TeaModel):
    def __init__(
        self,
        apsara_data_ingestion_ids: List[str] = None,
        auto_scan_new: str = None,
        data_batch_ingestion_effect_time: str = None,
        data_batch_ingestion_mode: str = None,
        data_batch_ingestion_set_time: str = None,
        data_batch_ingestion_status: str = None,
        data_ingestions: List[GetDataBatchIngestionResponseBodyDataBatchIngestionDataIngestions] = None,
        data_source_recognize_enabled: bool = None,
        log_user_ids: List[str] = None,
        recommend_data_ingestion_ids: List[str] = None,
    ):
        self.apsara_data_ingestion_ids = apsara_data_ingestion_ids
        self.auto_scan_new = auto_scan_new
        self.data_batch_ingestion_effect_time = data_batch_ingestion_effect_time
        self.data_batch_ingestion_mode = data_batch_ingestion_mode
        self.data_batch_ingestion_set_time = data_batch_ingestion_set_time
        self.data_batch_ingestion_status = data_batch_ingestion_status
        self.data_ingestions = data_ingestions
        self.data_source_recognize_enabled = data_source_recognize_enabled
        self.log_user_ids = log_user_ids
        self.recommend_data_ingestion_ids = recommend_data_ingestion_ids

    def validate(self):
        if self.data_ingestions:
            for k in self.data_ingestions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apsara_data_ingestion_ids is not None:
            result['ApsaraDataIngestionIds'] = self.apsara_data_ingestion_ids
        if self.auto_scan_new is not None:
            result['AutoScanNew'] = self.auto_scan_new
        if self.data_batch_ingestion_effect_time is not None:
            result['DataBatchIngestionEffectTime'] = self.data_batch_ingestion_effect_time
        if self.data_batch_ingestion_mode is not None:
            result['DataBatchIngestionMode'] = self.data_batch_ingestion_mode
        if self.data_batch_ingestion_set_time is not None:
            result['DataBatchIngestionSetTime'] = self.data_batch_ingestion_set_time
        if self.data_batch_ingestion_status is not None:
            result['DataBatchIngestionStatus'] = self.data_batch_ingestion_status
        result['DataIngestions'] = []
        if self.data_ingestions is not None:
            for k in self.data_ingestions:
                result['DataIngestions'].append(k.to_map() if k else None)
        if self.data_source_recognize_enabled is not None:
            result['DataSourceRecognizeEnabled'] = self.data_source_recognize_enabled
        if self.log_user_ids is not None:
            result['LogUserIds'] = self.log_user_ids
        if self.recommend_data_ingestion_ids is not None:
            result['RecommendDataIngestionIds'] = self.recommend_data_ingestion_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApsaraDataIngestionIds') is not None:
            self.apsara_data_ingestion_ids = m.get('ApsaraDataIngestionIds')
        if m.get('AutoScanNew') is not None:
            self.auto_scan_new = m.get('AutoScanNew')
        if m.get('DataBatchIngestionEffectTime') is not None:
            self.data_batch_ingestion_effect_time = m.get('DataBatchIngestionEffectTime')
        if m.get('DataBatchIngestionMode') is not None:
            self.data_batch_ingestion_mode = m.get('DataBatchIngestionMode')
        if m.get('DataBatchIngestionSetTime') is not None:
            self.data_batch_ingestion_set_time = m.get('DataBatchIngestionSetTime')
        if m.get('DataBatchIngestionStatus') is not None:
            self.data_batch_ingestion_status = m.get('DataBatchIngestionStatus')
        self.data_ingestions = []
        if m.get('DataIngestions') is not None:
            for k in m.get('DataIngestions'):
                temp_model = GetDataBatchIngestionResponseBodyDataBatchIngestionDataIngestions()
                self.data_ingestions.append(temp_model.from_map(k))
        if m.get('DataSourceRecognizeEnabled') is not None:
            self.data_source_recognize_enabled = m.get('DataSourceRecognizeEnabled')
        if m.get('LogUserIds') is not None:
            self.log_user_ids = m.get('LogUserIds')
        if m.get('RecommendDataIngestionIds') is not None:
            self.recommend_data_ingestion_ids = m.get('RecommendDataIngestionIds')
        return self


class GetDataBatchIngestionResponseBody(TeaModel):
    def __init__(
        self,
        data_batch_ingestion: GetDataBatchIngestionResponseBodyDataBatchIngestion = None,
        request_id: str = None,
    ):
        self.data_batch_ingestion = data_batch_ingestion
        self.request_id = request_id

    def validate(self):
        if self.data_batch_ingestion:
            self.data_batch_ingestion.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_batch_ingestion is not None:
            result['DataBatchIngestion'] = self.data_batch_ingestion.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataBatchIngestion') is not None:
            temp_model = GetDataBatchIngestionResponseBodyDataBatchIngestion()
            self.data_batch_ingestion = temp_model.from_map(m['DataBatchIngestion'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetDataBatchIngestionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDataBatchIngestionResponseBody = None,
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
            temp_model = GetDataBatchIngestionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDataStorageRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        region_id: str = None,
        role_for: int = None,
    ):
        self.lang = lang
        self.region_id = region_id
        self.role_for = role_for

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.role_for is not None:
            result['RoleFor'] = self.role_for
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')
        return self


class GetDataStorageResponseBodyDataNormalizationLogStores(TeaModel):
    def __init__(
        self,
        log_store_name: str = None,
        log_store_ttl: int = None,
    ):
        self.log_store_name = log_store_name
        self.log_store_ttl = log_store_ttl

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.log_store_name is not None:
            result['LogStoreName'] = self.log_store_name
        if self.log_store_ttl is not None:
            result['LogStoreTtl'] = self.log_store_ttl
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LogStoreName') is not None:
            self.log_store_name = m.get('LogStoreName')
        if m.get('LogStoreTtl') is not None:
            self.log_store_ttl = m.get('LogStoreTtl')
        return self


class GetDataStorageResponseBodyDataNormalizationLogViews(TeaModel):
    def __init__(
        self,
        activity_name: str = None,
        category_name: str = None,
        detection_rule_reference_count: int = None,
        detection_rule_reference_product_ids: List[str] = None,
        log_search_conditions: str = None,
        log_store_name: str = None,
        log_view_existed: bool = None,
        log_view_name: str = None,
    ):
        self.activity_name = activity_name
        self.category_name = category_name
        self.detection_rule_reference_count = detection_rule_reference_count
        self.detection_rule_reference_product_ids = detection_rule_reference_product_ids
        self.log_search_conditions = log_search_conditions
        self.log_store_name = log_store_name
        self.log_view_existed = log_view_existed
        self.log_view_name = log_view_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.activity_name is not None:
            result['ActivityName'] = self.activity_name
        if self.category_name is not None:
            result['CategoryName'] = self.category_name
        if self.detection_rule_reference_count is not None:
            result['DetectionRuleReferenceCount'] = self.detection_rule_reference_count
        if self.detection_rule_reference_product_ids is not None:
            result['DetectionRuleReferenceProductIds'] = self.detection_rule_reference_product_ids
        if self.log_search_conditions is not None:
            result['LogSearchConditions'] = self.log_search_conditions
        if self.log_store_name is not None:
            result['LogStoreName'] = self.log_store_name
        if self.log_view_existed is not None:
            result['LogViewExisted'] = self.log_view_existed
        if self.log_view_name is not None:
            result['LogViewName'] = self.log_view_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActivityName') is not None:
            self.activity_name = m.get('ActivityName')
        if m.get('CategoryName') is not None:
            self.category_name = m.get('CategoryName')
        if m.get('DetectionRuleReferenceCount') is not None:
            self.detection_rule_reference_count = m.get('DetectionRuleReferenceCount')
        if m.get('DetectionRuleReferenceProductIds') is not None:
            self.detection_rule_reference_product_ids = m.get('DetectionRuleReferenceProductIds')
        if m.get('LogSearchConditions') is not None:
            self.log_search_conditions = m.get('LogSearchConditions')
        if m.get('LogStoreName') is not None:
            self.log_store_name = m.get('LogStoreName')
        if m.get('LogViewExisted') is not None:
            self.log_view_existed = m.get('LogViewExisted')
        if m.get('LogViewName') is not None:
            self.log_view_name = m.get('LogViewName')
        return self


class GetDataStorageResponseBodyDataSasLogStores(TeaModel):
    def __init__(
        self,
        log_code: str = None,
        log_delivery_group: str = None,
        log_delivery_permission: str = None,
        log_delivery_status: str = None,
        log_delivery_update_time: str = None,
        log_name: str = None,
        log_search_conditions: str = None,
        log_store_existed: bool = None,
        log_store_name: str = None,
        log_store_ttl: int = None,
    ):
        self.log_code = log_code
        self.log_delivery_group = log_delivery_group
        self.log_delivery_permission = log_delivery_permission
        self.log_delivery_status = log_delivery_status
        self.log_delivery_update_time = log_delivery_update_time
        self.log_name = log_name
        self.log_search_conditions = log_search_conditions
        self.log_store_existed = log_store_existed
        self.log_store_name = log_store_name
        self.log_store_ttl = log_store_ttl

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.log_code is not None:
            result['LogCode'] = self.log_code
        if self.log_delivery_group is not None:
            result['LogDeliveryGroup'] = self.log_delivery_group
        if self.log_delivery_permission is not None:
            result['LogDeliveryPermission'] = self.log_delivery_permission
        if self.log_delivery_status is not None:
            result['LogDeliveryStatus'] = self.log_delivery_status
        if self.log_delivery_update_time is not None:
            result['LogDeliveryUpdateTime'] = self.log_delivery_update_time
        if self.log_name is not None:
            result['LogName'] = self.log_name
        if self.log_search_conditions is not None:
            result['LogSearchConditions'] = self.log_search_conditions
        if self.log_store_existed is not None:
            result['LogStoreExisted'] = self.log_store_existed
        if self.log_store_name is not None:
            result['LogStoreName'] = self.log_store_name
        if self.log_store_ttl is not None:
            result['LogStoreTtl'] = self.log_store_ttl
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LogCode') is not None:
            self.log_code = m.get('LogCode')
        if m.get('LogDeliveryGroup') is not None:
            self.log_delivery_group = m.get('LogDeliveryGroup')
        if m.get('LogDeliveryPermission') is not None:
            self.log_delivery_permission = m.get('LogDeliveryPermission')
        if m.get('LogDeliveryStatus') is not None:
            self.log_delivery_status = m.get('LogDeliveryStatus')
        if m.get('LogDeliveryUpdateTime') is not None:
            self.log_delivery_update_time = m.get('LogDeliveryUpdateTime')
        if m.get('LogName') is not None:
            self.log_name = m.get('LogName')
        if m.get('LogSearchConditions') is not None:
            self.log_search_conditions = m.get('LogSearchConditions')
        if m.get('LogStoreExisted') is not None:
            self.log_store_existed = m.get('LogStoreExisted')
        if m.get('LogStoreName') is not None:
            self.log_store_name = m.get('LogStoreName')
        if m.get('LogStoreTtl') is not None:
            self.log_store_ttl = m.get('LogStoreTtl')
        return self


class GetDataStorageResponseBodyData(TeaModel):
    def __init__(
        self,
        cold_storage_used_capacity: float = None,
        data_storage_region_id: str = None,
        data_storage_region_permission: str = None,
        data_storage_total_capacity: int = None,
        data_storage_used_capacity: float = None,
        data_storage_used_capacity_detail: str = None,
        log_project: str = None,
        normalization_log_stores: List[GetDataStorageResponseBodyDataNormalizationLogStores] = None,
        normalization_log_views: List[GetDataStorageResponseBodyDataNormalizationLogViews] = None,
        sas_log_stores: List[GetDataStorageResponseBodyDataSasLogStores] = None,
    ):
        self.cold_storage_used_capacity = cold_storage_used_capacity
        self.data_storage_region_id = data_storage_region_id
        self.data_storage_region_permission = data_storage_region_permission
        self.data_storage_total_capacity = data_storage_total_capacity
        self.data_storage_used_capacity = data_storage_used_capacity
        self.data_storage_used_capacity_detail = data_storage_used_capacity_detail
        self.log_project = log_project
        self.normalization_log_stores = normalization_log_stores
        self.normalization_log_views = normalization_log_views
        self.sas_log_stores = sas_log_stores

    def validate(self):
        if self.normalization_log_stores:
            for k in self.normalization_log_stores:
                if k:
                    k.validate()
        if self.normalization_log_views:
            for k in self.normalization_log_views:
                if k:
                    k.validate()
        if self.sas_log_stores:
            for k in self.sas_log_stores:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cold_storage_used_capacity is not None:
            result['ColdStorageUsedCapacity'] = self.cold_storage_used_capacity
        if self.data_storage_region_id is not None:
            result['DataStorageRegionId'] = self.data_storage_region_id
        if self.data_storage_region_permission is not None:
            result['DataStorageRegionPermission'] = self.data_storage_region_permission
        if self.data_storage_total_capacity is not None:
            result['DataStorageTotalCapacity'] = self.data_storage_total_capacity
        if self.data_storage_used_capacity is not None:
            result['DataStorageUsedCapacity'] = self.data_storage_used_capacity
        if self.data_storage_used_capacity_detail is not None:
            result['DataStorageUsedCapacityDetail'] = self.data_storage_used_capacity_detail
        if self.log_project is not None:
            result['LogProject'] = self.log_project
        result['NormalizationLogStores'] = []
        if self.normalization_log_stores is not None:
            for k in self.normalization_log_stores:
                result['NormalizationLogStores'].append(k.to_map() if k else None)
        result['NormalizationLogViews'] = []
        if self.normalization_log_views is not None:
            for k in self.normalization_log_views:
                result['NormalizationLogViews'].append(k.to_map() if k else None)
        result['SasLogStores'] = []
        if self.sas_log_stores is not None:
            for k in self.sas_log_stores:
                result['SasLogStores'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ColdStorageUsedCapacity') is not None:
            self.cold_storage_used_capacity = m.get('ColdStorageUsedCapacity')
        if m.get('DataStorageRegionId') is not None:
            self.data_storage_region_id = m.get('DataStorageRegionId')
        if m.get('DataStorageRegionPermission') is not None:
            self.data_storage_region_permission = m.get('DataStorageRegionPermission')
        if m.get('DataStorageTotalCapacity') is not None:
            self.data_storage_total_capacity = m.get('DataStorageTotalCapacity')
        if m.get('DataStorageUsedCapacity') is not None:
            self.data_storage_used_capacity = m.get('DataStorageUsedCapacity')
        if m.get('DataStorageUsedCapacityDetail') is not None:
            self.data_storage_used_capacity_detail = m.get('DataStorageUsedCapacityDetail')
        if m.get('LogProject') is not None:
            self.log_project = m.get('LogProject')
        self.normalization_log_stores = []
        if m.get('NormalizationLogStores') is not None:
            for k in m.get('NormalizationLogStores'):
                temp_model = GetDataStorageResponseBodyDataNormalizationLogStores()
                self.normalization_log_stores.append(temp_model.from_map(k))
        self.normalization_log_views = []
        if m.get('NormalizationLogViews') is not None:
            for k in m.get('NormalizationLogViews'):
                temp_model = GetDataStorageResponseBodyDataNormalizationLogViews()
                self.normalization_log_views.append(temp_model.from_map(k))
        self.sas_log_stores = []
        if m.get('SasLogStores') is not None:
            for k in m.get('SasLogStores'):
                temp_model = GetDataStorageResponseBodyDataSasLogStores()
                self.sas_log_stores.append(temp_model.from_map(k))
        return self


class GetDataStorageResponseBody(TeaModel):
    def __init__(
        self,
        data: GetDataStorageResponseBodyData = None,
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
            temp_model = GetDataStorageResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetDataStorageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDataStorageResponseBody = None,
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
            temp_model = GetDataStorageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDetectionStatisticRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        region_id: str = None,
        role_for: int = None,
    ):
        self.lang = lang
        self.region_id = region_id
        self.role_for = role_for

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.role_for is not None:
            result['RoleFor'] = self.role_for
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')
        return self


class GetDetectionStatisticResponseBodyDetectionStatistic(TeaModel):
    def __init__(
        self,
        detection_rule_online_count: int = None,
        detection_rule_template_count: int = None,
        detection_rule_test_count: int = None,
        graph_compute_rule_count: int = None,
        passthrough_rule_count: int = None,
        window_rule_count: int = None,
    ):
        self.detection_rule_online_count = detection_rule_online_count
        self.detection_rule_template_count = detection_rule_template_count
        self.detection_rule_test_count = detection_rule_test_count
        self.graph_compute_rule_count = graph_compute_rule_count
        self.passthrough_rule_count = passthrough_rule_count
        self.window_rule_count = window_rule_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.detection_rule_online_count is not None:
            result['DetectionRuleOnlineCount'] = self.detection_rule_online_count
        if self.detection_rule_template_count is not None:
            result['DetectionRuleTemplateCount'] = self.detection_rule_template_count
        if self.detection_rule_test_count is not None:
            result['DetectionRuleTestCount'] = self.detection_rule_test_count
        if self.graph_compute_rule_count is not None:
            result['GraphComputeRuleCount'] = self.graph_compute_rule_count
        if self.passthrough_rule_count is not None:
            result['PassthroughRuleCount'] = self.passthrough_rule_count
        if self.window_rule_count is not None:
            result['WindowRuleCount'] = self.window_rule_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DetectionRuleOnlineCount') is not None:
            self.detection_rule_online_count = m.get('DetectionRuleOnlineCount')
        if m.get('DetectionRuleTemplateCount') is not None:
            self.detection_rule_template_count = m.get('DetectionRuleTemplateCount')
        if m.get('DetectionRuleTestCount') is not None:
            self.detection_rule_test_count = m.get('DetectionRuleTestCount')
        if m.get('GraphComputeRuleCount') is not None:
            self.graph_compute_rule_count = m.get('GraphComputeRuleCount')
        if m.get('PassthroughRuleCount') is not None:
            self.passthrough_rule_count = m.get('PassthroughRuleCount')
        if m.get('WindowRuleCount') is not None:
            self.window_rule_count = m.get('WindowRuleCount')
        return self


class GetDetectionStatisticResponseBody(TeaModel):
    def __init__(
        self,
        detection_statistic: GetDetectionStatisticResponseBodyDetectionStatistic = None,
        request_id: str = None,
    ):
        self.detection_statistic = detection_statistic
        self.request_id = request_id

    def validate(self):
        if self.detection_statistic:
            self.detection_statistic.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.detection_statistic is not None:
            result['DetectionStatistic'] = self.detection_statistic.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DetectionStatistic') is not None:
            temp_model = GetDetectionStatisticResponseBodyDetectionStatistic()
            self.detection_statistic = temp_model.from_map(m['DetectionStatistic'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetDetectionStatisticResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDetectionStatisticResponseBody = None,
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
            temp_model = GetDetectionStatisticResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetExportTaskRequest(TeaModel):
    def __init__(
        self,
        export_id: int = None,
        lang: str = None,
        region_id: str = None,
        role_for: int = None,
    ):
        self.export_id = export_id
        self.lang = lang
        self.region_id = region_id
        self.role_for = role_for

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.export_id is not None:
            result['ExportId'] = self.export_id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.role_for is not None:
            result['RoleFor'] = self.role_for
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExportId') is not None:
            self.export_id = m.get('ExportId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')
        return self


class GetExportTaskResponseBody(TeaModel):
    def __init__(
        self,
        export_status: str = None,
        export_type: str = None,
        file_name: str = None,
        gmt_create: str = None,
        id: int = None,
        link: str = None,
        progress: int = None,
        request_id: str = None,
    ):
        self.export_status = export_status
        self.export_type = export_type
        self.file_name = file_name
        self.gmt_create = gmt_create
        self.id = id
        self.link = link
        self.progress = progress
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.export_status is not None:
            result['ExportStatus'] = self.export_status
        if self.export_type is not None:
            result['ExportType'] = self.export_type
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.id is not None:
            result['Id'] = self.id
        if self.link is not None:
            result['Link'] = self.link
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExportStatus') is not None:
            self.export_status = m.get('ExportStatus')
        if m.get('ExportType') is not None:
            self.export_type = m.get('ExportType')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Link') is not None:
            self.link = m.get('Link')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetExportTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetExportTaskResponseBody = None,
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
            temp_model = GetExportTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetIncidentRequest(TeaModel):
    def __init__(
        self,
        incident_uuid: str = None,
        lang: str = None,
        region_id: str = None,
        role_for: int = None,
    ):
        self.incident_uuid = incident_uuid
        self.lang = lang
        self.region_id = region_id
        self.role_for = role_for

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.incident_uuid is not None:
            result['IncidentUuid'] = self.incident_uuid
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.role_for is not None:
            result['RoleFor'] = self.role_for
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IncidentUuid') is not None:
            self.incident_uuid = m.get('IncidentUuid')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')
        return self


class GetIncidentResponseBodyIncident(TeaModel):
    def __init__(
        self,
        attck_tactics: Any = None,
        create_time: int = None,
        detection_rule_id: str = None,
        incident_aggregation_type: str = None,
        incident_description: str = None,
        incident_name: str = None,
        incident_remark: str = None,
        incident_status: int = None,
        incident_tags: str = None,
        incident_uuid: str = None,
        relate_alert_count: int = None,
        relate_asset_count: int = None,
        relate_data_source_ids: Any = None,
        relate_user_ids: Any = None,
        threat_level: str = None,
        threat_score: str = None,
        update_time: int = None,
    ):
        self.attck_tactics = attck_tactics
        self.create_time = create_time
        self.detection_rule_id = detection_rule_id
        self.incident_aggregation_type = incident_aggregation_type
        self.incident_description = incident_description
        self.incident_name = incident_name
        self.incident_remark = incident_remark
        self.incident_status = incident_status
        self.incident_tags = incident_tags
        self.incident_uuid = incident_uuid
        self.relate_alert_count = relate_alert_count
        self.relate_asset_count = relate_asset_count
        self.relate_data_source_ids = relate_data_source_ids
        self.relate_user_ids = relate_user_ids
        self.threat_level = threat_level
        self.threat_score = threat_score
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attck_tactics is not None:
            result['AttckTactics'] = self.attck_tactics
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.detection_rule_id is not None:
            result['DetectionRuleId'] = self.detection_rule_id
        if self.incident_aggregation_type is not None:
            result['IncidentAggregationType'] = self.incident_aggregation_type
        if self.incident_description is not None:
            result['IncidentDescription'] = self.incident_description
        if self.incident_name is not None:
            result['IncidentName'] = self.incident_name
        if self.incident_remark is not None:
            result['IncidentRemark'] = self.incident_remark
        if self.incident_status is not None:
            result['IncidentStatus'] = self.incident_status
        if self.incident_tags is not None:
            result['IncidentTags'] = self.incident_tags
        if self.incident_uuid is not None:
            result['IncidentUuid'] = self.incident_uuid
        if self.relate_alert_count is not None:
            result['RelateAlertCount'] = self.relate_alert_count
        if self.relate_asset_count is not None:
            result['RelateAssetCount'] = self.relate_asset_count
        if self.relate_data_source_ids is not None:
            result['RelateDataSourceIds'] = self.relate_data_source_ids
        if self.relate_user_ids is not None:
            result['RelateUserIds'] = self.relate_user_ids
        if self.threat_level is not None:
            result['ThreatLevel'] = self.threat_level
        if self.threat_score is not None:
            result['ThreatScore'] = self.threat_score
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttckTactics') is not None:
            self.attck_tactics = m.get('AttckTactics')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DetectionRuleId') is not None:
            self.detection_rule_id = m.get('DetectionRuleId')
        if m.get('IncidentAggregationType') is not None:
            self.incident_aggregation_type = m.get('IncidentAggregationType')
        if m.get('IncidentDescription') is not None:
            self.incident_description = m.get('IncidentDescription')
        if m.get('IncidentName') is not None:
            self.incident_name = m.get('IncidentName')
        if m.get('IncidentRemark') is not None:
            self.incident_remark = m.get('IncidentRemark')
        if m.get('IncidentStatus') is not None:
            self.incident_status = m.get('IncidentStatus')
        if m.get('IncidentTags') is not None:
            self.incident_tags = m.get('IncidentTags')
        if m.get('IncidentUuid') is not None:
            self.incident_uuid = m.get('IncidentUuid')
        if m.get('RelateAlertCount') is not None:
            self.relate_alert_count = m.get('RelateAlertCount')
        if m.get('RelateAssetCount') is not None:
            self.relate_asset_count = m.get('RelateAssetCount')
        if m.get('RelateDataSourceIds') is not None:
            self.relate_data_source_ids = m.get('RelateDataSourceIds')
        if m.get('RelateUserIds') is not None:
            self.relate_user_ids = m.get('RelateUserIds')
        if m.get('ThreatLevel') is not None:
            self.threat_level = m.get('ThreatLevel')
        if m.get('ThreatScore') is not None:
            self.threat_score = m.get('ThreatScore')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class GetIncidentResponseBody(TeaModel):
    def __init__(
        self,
        incident: GetIncidentResponseBodyIncident = None,
        request_id: str = None,
    ):
        self.incident = incident
        self.request_id = request_id

    def validate(self):
        if self.incident:
            self.incident.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.incident is not None:
            result['Incident'] = self.incident.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Incident') is not None:
            temp_model = GetIncidentResponseBodyIncident()
            self.incident = temp_model.from_map(m['Incident'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetIncidentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetIncidentResponseBody = None,
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
            temp_model = GetIncidentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLogTicketRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        log_user_id: int = None,
        region_id: str = None,
        role_for: int = None,
    ):
        self.lang = lang
        self.log_user_id = log_user_id
        self.region_id = region_id
        self.role_for = role_for

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.log_user_id is not None:
            result['LogUserId'] = self.log_user_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.role_for is not None:
            result['RoleFor'] = self.role_for
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('LogUserId') is not None:
            self.log_user_id = m.get('LogUserId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')
        return self


class GetLogTicketResponseBody(TeaModel):
    def __init__(
        self,
        log_ticket: str = None,
        request_id: str = None,
    ):
        self.log_ticket = log_ticket
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.log_ticket is not None:
            result['LogTicket'] = self.log_ticket
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LogTicket') is not None:
            self.log_ticket = m.get('LogTicket')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetLogTicketResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetLogTicketResponseBody = None,
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
            temp_model = GetLogTicketResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetNormalizationRuleRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        normalization_rule_id: str = None,
        region_id: str = None,
        role_for: int = None,
    ):
        self.lang = lang
        self.normalization_rule_id = normalization_rule_id
        self.region_id = region_id
        self.role_for = role_for

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.normalization_rule_id is not None:
            result['NormalizationRuleId'] = self.normalization_rule_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.role_for is not None:
            result['RoleFor'] = self.role_for
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('NormalizationRuleId') is not None:
            self.normalization_rule_id = m.get('NormalizationRuleId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')
        return self


class GetNormalizationRuleResponseBodyNormalizationRule(TeaModel):
    def __init__(
        self,
        create_time: int = None,
        extend_content_packed: str = None,
        normalization_category_id: str = None,
        normalization_rule_description: str = None,
        normalization_rule_expression: str = None,
        normalization_rule_format: str = None,
        normalization_rule_id: str = None,
        normalization_rule_ids: List[str] = None,
        normalization_rule_mode: str = None,
        normalization_rule_name: str = None,
        normalization_rule_status: str = None,
        normalization_rule_type: str = None,
        normalization_rule_version: int = None,
        normalization_schema_id: str = None,
        order_field: str = None,
        product_id: str = None,
        update_time: int = None,
        vendor_id: str = None,
    ):
        self.create_time = create_time
        self.extend_content_packed = extend_content_packed
        self.normalization_category_id = normalization_category_id
        self.normalization_rule_description = normalization_rule_description
        self.normalization_rule_expression = normalization_rule_expression
        self.normalization_rule_format = normalization_rule_format
        self.normalization_rule_id = normalization_rule_id
        self.normalization_rule_ids = normalization_rule_ids
        self.normalization_rule_mode = normalization_rule_mode
        self.normalization_rule_name = normalization_rule_name
        self.normalization_rule_status = normalization_rule_status
        self.normalization_rule_type = normalization_rule_type
        self.normalization_rule_version = normalization_rule_version
        self.normalization_schema_id = normalization_schema_id
        self.order_field = order_field
        self.product_id = product_id
        self.update_time = update_time
        self.vendor_id = vendor_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.extend_content_packed is not None:
            result['ExtendContentPacked'] = self.extend_content_packed
        if self.normalization_category_id is not None:
            result['NormalizationCategoryId'] = self.normalization_category_id
        if self.normalization_rule_description is not None:
            result['NormalizationRuleDescription'] = self.normalization_rule_description
        if self.normalization_rule_expression is not None:
            result['NormalizationRuleExpression'] = self.normalization_rule_expression
        if self.normalization_rule_format is not None:
            result['NormalizationRuleFormat'] = self.normalization_rule_format
        if self.normalization_rule_id is not None:
            result['NormalizationRuleId'] = self.normalization_rule_id
        if self.normalization_rule_ids is not None:
            result['NormalizationRuleIds'] = self.normalization_rule_ids
        if self.normalization_rule_mode is not None:
            result['NormalizationRuleMode'] = self.normalization_rule_mode
        if self.normalization_rule_name is not None:
            result['NormalizationRuleName'] = self.normalization_rule_name
        if self.normalization_rule_status is not None:
            result['NormalizationRuleStatus'] = self.normalization_rule_status
        if self.normalization_rule_type is not None:
            result['NormalizationRuleType'] = self.normalization_rule_type
        if self.normalization_rule_version is not None:
            result['NormalizationRuleVersion'] = self.normalization_rule_version
        if self.normalization_schema_id is not None:
            result['NormalizationSchemaId'] = self.normalization_schema_id
        if self.order_field is not None:
            result['OrderField'] = self.order_field
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.vendor_id is not None:
            result['VendorId'] = self.vendor_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ExtendContentPacked') is not None:
            self.extend_content_packed = m.get('ExtendContentPacked')
        if m.get('NormalizationCategoryId') is not None:
            self.normalization_category_id = m.get('NormalizationCategoryId')
        if m.get('NormalizationRuleDescription') is not None:
            self.normalization_rule_description = m.get('NormalizationRuleDescription')
        if m.get('NormalizationRuleExpression') is not None:
            self.normalization_rule_expression = m.get('NormalizationRuleExpression')
        if m.get('NormalizationRuleFormat') is not None:
            self.normalization_rule_format = m.get('NormalizationRuleFormat')
        if m.get('NormalizationRuleId') is not None:
            self.normalization_rule_id = m.get('NormalizationRuleId')
        if m.get('NormalizationRuleIds') is not None:
            self.normalization_rule_ids = m.get('NormalizationRuleIds')
        if m.get('NormalizationRuleMode') is not None:
            self.normalization_rule_mode = m.get('NormalizationRuleMode')
        if m.get('NormalizationRuleName') is not None:
            self.normalization_rule_name = m.get('NormalizationRuleName')
        if m.get('NormalizationRuleStatus') is not None:
            self.normalization_rule_status = m.get('NormalizationRuleStatus')
        if m.get('NormalizationRuleType') is not None:
            self.normalization_rule_type = m.get('NormalizationRuleType')
        if m.get('NormalizationRuleVersion') is not None:
            self.normalization_rule_version = m.get('NormalizationRuleVersion')
        if m.get('NormalizationSchemaId') is not None:
            self.normalization_schema_id = m.get('NormalizationSchemaId')
        if m.get('OrderField') is not None:
            self.order_field = m.get('OrderField')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('VendorId') is not None:
            self.vendor_id = m.get('VendorId')
        return self


class GetNormalizationRuleResponseBody(TeaModel):
    def __init__(
        self,
        normalization_rule: GetNormalizationRuleResponseBodyNormalizationRule = None,
        request_id: str = None,
    ):
        self.normalization_rule = normalization_rule
        self.request_id = request_id

    def validate(self):
        if self.normalization_rule:
            self.normalization_rule.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.normalization_rule is not None:
            result['NormalizationRule'] = self.normalization_rule.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NormalizationRule') is not None:
            temp_model = GetNormalizationRuleResponseBodyNormalizationRule()
            self.normalization_rule = temp_model.from_map(m['NormalizationRule'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetNormalizationRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetNormalizationRuleResponseBody = None,
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
            temp_model = GetNormalizationRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetNormalizationRuleVersionRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        normalization_rule_id: str = None,
        normalization_rule_version: int = None,
        region_id: str = None,
        role_for: int = None,
    ):
        self.lang = lang
        self.normalization_rule_id = normalization_rule_id
        self.normalization_rule_version = normalization_rule_version
        self.region_id = region_id
        self.role_for = role_for

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.normalization_rule_id is not None:
            result['NormalizationRuleId'] = self.normalization_rule_id
        if self.normalization_rule_version is not None:
            result['NormalizationRuleVersion'] = self.normalization_rule_version
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.role_for is not None:
            result['RoleFor'] = self.role_for
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('NormalizationRuleId') is not None:
            self.normalization_rule_id = m.get('NormalizationRuleId')
        if m.get('NormalizationRuleVersion') is not None:
            self.normalization_rule_version = m.get('NormalizationRuleVersion')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')
        return self


class GetNormalizationRuleVersionResponseBodyNormalizationRuleVersion(TeaModel):
    def __init__(
        self,
        create_time: int = None,
        normalization_category_id: str = None,
        normalization_rule_description: str = None,
        normalization_rule_expression: str = None,
        normalization_rule_format: str = None,
        normalization_rule_id: str = None,
        normalization_rule_name: str = None,
        normalization_rule_status: str = None,
        normalization_rule_type: str = None,
        normalization_rule_version: int = None,
        normalization_rule_version_name: str = None,
        normalization_schema_id: str = None,
        product_id: str = None,
        region_id: str = None,
        update_time: int = None,
        vendor_id: str = None,
    ):
        self.create_time = create_time
        self.normalization_category_id = normalization_category_id
        self.normalization_rule_description = normalization_rule_description
        self.normalization_rule_expression = normalization_rule_expression
        self.normalization_rule_format = normalization_rule_format
        self.normalization_rule_id = normalization_rule_id
        self.normalization_rule_name = normalization_rule_name
        self.normalization_rule_status = normalization_rule_status
        self.normalization_rule_type = normalization_rule_type
        self.normalization_rule_version = normalization_rule_version
        self.normalization_rule_version_name = normalization_rule_version_name
        self.normalization_schema_id = normalization_schema_id
        self.product_id = product_id
        self.region_id = region_id
        self.update_time = update_time
        self.vendor_id = vendor_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.normalization_category_id is not None:
            result['NormalizationCategoryId'] = self.normalization_category_id
        if self.normalization_rule_description is not None:
            result['NormalizationRuleDescription'] = self.normalization_rule_description
        if self.normalization_rule_expression is not None:
            result['NormalizationRuleExpression'] = self.normalization_rule_expression
        if self.normalization_rule_format is not None:
            result['NormalizationRuleFormat'] = self.normalization_rule_format
        if self.normalization_rule_id is not None:
            result['NormalizationRuleId'] = self.normalization_rule_id
        if self.normalization_rule_name is not None:
            result['NormalizationRuleName'] = self.normalization_rule_name
        if self.normalization_rule_status is not None:
            result['NormalizationRuleStatus'] = self.normalization_rule_status
        if self.normalization_rule_type is not None:
            result['NormalizationRuleType'] = self.normalization_rule_type
        if self.normalization_rule_version is not None:
            result['NormalizationRuleVersion'] = self.normalization_rule_version
        if self.normalization_rule_version_name is not None:
            result['NormalizationRuleVersionName'] = self.normalization_rule_version_name
        if self.normalization_schema_id is not None:
            result['NormalizationSchemaId'] = self.normalization_schema_id
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.vendor_id is not None:
            result['VendorId'] = self.vendor_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('NormalizationCategoryId') is not None:
            self.normalization_category_id = m.get('NormalizationCategoryId')
        if m.get('NormalizationRuleDescription') is not None:
            self.normalization_rule_description = m.get('NormalizationRuleDescription')
        if m.get('NormalizationRuleExpression') is not None:
            self.normalization_rule_expression = m.get('NormalizationRuleExpression')
        if m.get('NormalizationRuleFormat') is not None:
            self.normalization_rule_format = m.get('NormalizationRuleFormat')
        if m.get('NormalizationRuleId') is not None:
            self.normalization_rule_id = m.get('NormalizationRuleId')
        if m.get('NormalizationRuleName') is not None:
            self.normalization_rule_name = m.get('NormalizationRuleName')
        if m.get('NormalizationRuleStatus') is not None:
            self.normalization_rule_status = m.get('NormalizationRuleStatus')
        if m.get('NormalizationRuleType') is not None:
            self.normalization_rule_type = m.get('NormalizationRuleType')
        if m.get('NormalizationRuleVersion') is not None:
            self.normalization_rule_version = m.get('NormalizationRuleVersion')
        if m.get('NormalizationRuleVersionName') is not None:
            self.normalization_rule_version_name = m.get('NormalizationRuleVersionName')
        if m.get('NormalizationSchemaId') is not None:
            self.normalization_schema_id = m.get('NormalizationSchemaId')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('VendorId') is not None:
            self.vendor_id = m.get('VendorId')
        return self


class GetNormalizationRuleVersionResponseBody(TeaModel):
    def __init__(
        self,
        normalization_rule_version: GetNormalizationRuleVersionResponseBodyNormalizationRuleVersion = None,
        request_id: str = None,
    ):
        self.normalization_rule_version = normalization_rule_version
        self.request_id = request_id

    def validate(self):
        if self.normalization_rule_version:
            self.normalization_rule_version.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.normalization_rule_version is not None:
            result['NormalizationRuleVersion'] = self.normalization_rule_version.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NormalizationRuleVersion') is not None:
            temp_model = GetNormalizationRuleVersionResponseBodyNormalizationRuleVersion()
            self.normalization_rule_version = temp_model.from_map(m['NormalizationRuleVersion'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetNormalizationRuleVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetNormalizationRuleVersionResponseBody = None,
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
            temp_model = GetNormalizationRuleVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetNormalizationSchemaRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        normalization_schema_id: str = None,
        normalization_schema_type: str = None,
        region_id: str = None,
        role_for: int = None,
    ):
        self.lang = lang
        self.normalization_schema_id = normalization_schema_id
        self.normalization_schema_type = normalization_schema_type
        self.region_id = region_id
        self.role_for = role_for

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.normalization_schema_id is not None:
            result['NormalizationSchemaId'] = self.normalization_schema_id
        if self.normalization_schema_type is not None:
            result['NormalizationSchemaType'] = self.normalization_schema_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.role_for is not None:
            result['RoleFor'] = self.role_for
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('NormalizationSchemaId') is not None:
            self.normalization_schema_id = m.get('NormalizationSchemaId')
        if m.get('NormalizationSchemaType') is not None:
            self.normalization_schema_type = m.get('NormalizationSchemaType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')
        return self


class GetNormalizationSchemaResponseBodyNormalizationSchemaNormalizationFields(TeaModel):
    def __init__(
        self,
        normalization_field_description: str = None,
        normalization_field_example: str = None,
        normalization_field_name: str = None,
        normalization_field_requirement: bool = None,
        normalization_field_reserved: bool = None,
        normalization_field_type: str = None,
    ):
        self.normalization_field_description = normalization_field_description
        self.normalization_field_example = normalization_field_example
        self.normalization_field_name = normalization_field_name
        self.normalization_field_requirement = normalization_field_requirement
        self.normalization_field_reserved = normalization_field_reserved
        self.normalization_field_type = normalization_field_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.normalization_field_description is not None:
            result['NormalizationFieldDescription'] = self.normalization_field_description
        if self.normalization_field_example is not None:
            result['NormalizationFieldExample'] = self.normalization_field_example
        if self.normalization_field_name is not None:
            result['NormalizationFieldName'] = self.normalization_field_name
        if self.normalization_field_requirement is not None:
            result['NormalizationFieldRequirement'] = self.normalization_field_requirement
        if self.normalization_field_reserved is not None:
            result['NormalizationFieldReserved'] = self.normalization_field_reserved
        if self.normalization_field_type is not None:
            result['NormalizationFieldType'] = self.normalization_field_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NormalizationFieldDescription') is not None:
            self.normalization_field_description = m.get('NormalizationFieldDescription')
        if m.get('NormalizationFieldExample') is not None:
            self.normalization_field_example = m.get('NormalizationFieldExample')
        if m.get('NormalizationFieldName') is not None:
            self.normalization_field_name = m.get('NormalizationFieldName')
        if m.get('NormalizationFieldRequirement') is not None:
            self.normalization_field_requirement = m.get('NormalizationFieldRequirement')
        if m.get('NormalizationFieldReserved') is not None:
            self.normalization_field_reserved = m.get('NormalizationFieldReserved')
        if m.get('NormalizationFieldType') is not None:
            self.normalization_field_type = m.get('NormalizationFieldType')
        return self


class GetNormalizationSchemaResponseBodyNormalizationSchema(TeaModel):
    def __init__(
        self,
        create_time: int = None,
        normalization_category_id: str = None,
        normalization_fields: List[GetNormalizationSchemaResponseBodyNormalizationSchemaNormalizationFields] = None,
        normalization_schema_id: str = None,
        normalization_schema_name: str = None,
        normalization_schema_type: str = None,
        target_log_store: str = None,
        target_store_view: str = None,
        update_time: int = None,
    ):
        self.create_time = create_time
        self.normalization_category_id = normalization_category_id
        self.normalization_fields = normalization_fields
        self.normalization_schema_id = normalization_schema_id
        self.normalization_schema_name = normalization_schema_name
        self.normalization_schema_type = normalization_schema_type
        self.target_log_store = target_log_store
        self.target_store_view = target_store_view
        self.update_time = update_time

    def validate(self):
        if self.normalization_fields:
            for k in self.normalization_fields:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.normalization_category_id is not None:
            result['NormalizationCategoryId'] = self.normalization_category_id
        result['NormalizationFields'] = []
        if self.normalization_fields is not None:
            for k in self.normalization_fields:
                result['NormalizationFields'].append(k.to_map() if k else None)
        if self.normalization_schema_id is not None:
            result['NormalizationSchemaId'] = self.normalization_schema_id
        if self.normalization_schema_name is not None:
            result['NormalizationSchemaName'] = self.normalization_schema_name
        if self.normalization_schema_type is not None:
            result['NormalizationSchemaType'] = self.normalization_schema_type
        if self.target_log_store is not None:
            result['TargetLogStore'] = self.target_log_store
        if self.target_store_view is not None:
            result['TargetStoreView'] = self.target_store_view
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('NormalizationCategoryId') is not None:
            self.normalization_category_id = m.get('NormalizationCategoryId')
        self.normalization_fields = []
        if m.get('NormalizationFields') is not None:
            for k in m.get('NormalizationFields'):
                temp_model = GetNormalizationSchemaResponseBodyNormalizationSchemaNormalizationFields()
                self.normalization_fields.append(temp_model.from_map(k))
        if m.get('NormalizationSchemaId') is not None:
            self.normalization_schema_id = m.get('NormalizationSchemaId')
        if m.get('NormalizationSchemaName') is not None:
            self.normalization_schema_name = m.get('NormalizationSchemaName')
        if m.get('NormalizationSchemaType') is not None:
            self.normalization_schema_type = m.get('NormalizationSchemaType')
        if m.get('TargetLogStore') is not None:
            self.target_log_store = m.get('TargetLogStore')
        if m.get('TargetStoreView') is not None:
            self.target_store_view = m.get('TargetStoreView')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class GetNormalizationSchemaResponseBody(TeaModel):
    def __init__(
        self,
        normalization_schema: GetNormalizationSchemaResponseBodyNormalizationSchema = None,
        request_id: str = None,
    ):
        self.normalization_schema = normalization_schema
        self.request_id = request_id

    def validate(self):
        if self.normalization_schema:
            self.normalization_schema.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.normalization_schema is not None:
            result['NormalizationSchema'] = self.normalization_schema.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NormalizationSchema') is not None:
            temp_model = GetNormalizationSchemaResponseBodyNormalizationSchema()
            self.normalization_schema = temp_model.from_map(m['NormalizationSchema'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetNormalizationSchemaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetNormalizationSchemaResponseBody = None,
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
            temp_model = GetNormalizationSchemaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUserConfigRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        region_id: str = None,
        role_for: str = None,
    ):
        self.lang = lang
        self.region_id = region_id
        self.role_for = role_for

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.role_for is not None:
            result['RoleFor'] = self.role_for
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')
        return self


class GetUserConfigResponseBodyUser(TeaModel):
    def __init__(
        self,
        ctdr_version: str = None,
        data_storage_version: str = None,
        upgrade_ctdr_version: str = None,
        upgrade_status: str = None,
    ):
        self.ctdr_version = ctdr_version
        self.data_storage_version = data_storage_version
        self.upgrade_ctdr_version = upgrade_ctdr_version
        self.upgrade_status = upgrade_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ctdr_version is not None:
            result['CtdrVersion'] = self.ctdr_version
        if self.data_storage_version is not None:
            result['DataStorageVersion'] = self.data_storage_version
        if self.upgrade_ctdr_version is not None:
            result['UpgradeCtdrVersion'] = self.upgrade_ctdr_version
        if self.upgrade_status is not None:
            result['UpgradeStatus'] = self.upgrade_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CtdrVersion') is not None:
            self.ctdr_version = m.get('CtdrVersion')
        if m.get('DataStorageVersion') is not None:
            self.data_storage_version = m.get('DataStorageVersion')
        if m.get('UpgradeCtdrVersion') is not None:
            self.upgrade_ctdr_version = m.get('UpgradeCtdrVersion')
        if m.get('UpgradeStatus') is not None:
            self.upgrade_status = m.get('UpgradeStatus')
        return self


class GetUserConfigResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        user: GetUserConfigResponseBodyUser = None,
    ):
        self.request_id = request_id
        self.user = user

    def validate(self):
        if self.user:
            self.user.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.user is not None:
            result['User'] = self.user.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('User') is not None:
            temp_model = GetUserConfigResponseBodyUser()
            self.user = temp_model.from_map(m['User'])
        return self


class GetUserConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetUserConfigResponseBody = None,
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
            temp_model = GetUserConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDataIngestionTemplatesRequest(TeaModel):
    def __init__(
        self,
        data_ingestion_template_status: str = None,
        data_source_template_ids: str = None,
        lang: str = None,
        page_number: str = None,
        page_size: str = None,
        product_id: str = None,
        region_id: str = None,
        role_for: int = None,
    ):
        self.data_ingestion_template_status = data_ingestion_template_status
        self.data_source_template_ids = data_source_template_ids
        self.lang = lang
        self.page_number = page_number
        self.page_size = page_size
        self.product_id = product_id
        self.region_id = region_id
        self.role_for = role_for

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_ingestion_template_status is not None:
            result['DataIngestionTemplateStatus'] = self.data_ingestion_template_status
        if self.data_source_template_ids is not None:
            result['DataSourceTemplateIds'] = self.data_source_template_ids
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.role_for is not None:
            result['RoleFor'] = self.role_for
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataIngestionTemplateStatus') is not None:
            self.data_ingestion_template_status = m.get('DataIngestionTemplateStatus')
        if m.get('DataSourceTemplateIds') is not None:
            self.data_source_template_ids = m.get('DataSourceTemplateIds')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')
        return self


class ListDataIngestionTemplatesResponseBodyDataIngestionTemplates(TeaModel):
    def __init__(
        self,
        capacity_count: str = None,
        create_time: int = None,
        data_ingestion_mode: str = None,
        data_ingestion_status: str = None,
        data_ingestion_template_id: str = None,
        data_ingestion_template_name: str = None,
        data_ingestion_template_status: str = None,
        data_source_template_id: str = None,
        normalization_rule_id: str = None,
        normalization_rule_name: str = None,
        update_time: int = None,
    ):
        self.capacity_count = capacity_count
        self.create_time = create_time
        self.data_ingestion_mode = data_ingestion_mode
        self.data_ingestion_status = data_ingestion_status
        self.data_ingestion_template_id = data_ingestion_template_id
        self.data_ingestion_template_name = data_ingestion_template_name
        self.data_ingestion_template_status = data_ingestion_template_status
        self.data_source_template_id = data_source_template_id
        self.normalization_rule_id = normalization_rule_id
        self.normalization_rule_name = normalization_rule_name
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.capacity_count is not None:
            result['CapacityCount'] = self.capacity_count
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.data_ingestion_mode is not None:
            result['DataIngestionMode'] = self.data_ingestion_mode
        if self.data_ingestion_status is not None:
            result['DataIngestionStatus'] = self.data_ingestion_status
        if self.data_ingestion_template_id is not None:
            result['DataIngestionTemplateId'] = self.data_ingestion_template_id
        if self.data_ingestion_template_name is not None:
            result['DataIngestionTemplateName'] = self.data_ingestion_template_name
        if self.data_ingestion_template_status is not None:
            result['DataIngestionTemplateStatus'] = self.data_ingestion_template_status
        if self.data_source_template_id is not None:
            result['DataSourceTemplateId'] = self.data_source_template_id
        if self.normalization_rule_id is not None:
            result['NormalizationRuleId'] = self.normalization_rule_id
        if self.normalization_rule_name is not None:
            result['NormalizationRuleName'] = self.normalization_rule_name
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CapacityCount') is not None:
            self.capacity_count = m.get('CapacityCount')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DataIngestionMode') is not None:
            self.data_ingestion_mode = m.get('DataIngestionMode')
        if m.get('DataIngestionStatus') is not None:
            self.data_ingestion_status = m.get('DataIngestionStatus')
        if m.get('DataIngestionTemplateId') is not None:
            self.data_ingestion_template_id = m.get('DataIngestionTemplateId')
        if m.get('DataIngestionTemplateName') is not None:
            self.data_ingestion_template_name = m.get('DataIngestionTemplateName')
        if m.get('DataIngestionTemplateStatus') is not None:
            self.data_ingestion_template_status = m.get('DataIngestionTemplateStatus')
        if m.get('DataSourceTemplateId') is not None:
            self.data_source_template_id = m.get('DataSourceTemplateId')
        if m.get('NormalizationRuleId') is not None:
            self.normalization_rule_id = m.get('NormalizationRuleId')
        if m.get('NormalizationRuleName') is not None:
            self.normalization_rule_name = m.get('NormalizationRuleName')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class ListDataIngestionTemplatesResponseBody(TeaModel):
    def __init__(
        self,
        data_ingestion_templates: List[ListDataIngestionTemplatesResponseBodyDataIngestionTemplates] = None,
        page_number: str = None,
        page_size: str = None,
        request_id: str = None,
    ):
        self.data_ingestion_templates = data_ingestion_templates
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id

    def validate(self):
        if self.data_ingestion_templates:
            for k in self.data_ingestion_templates:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataIngestionTemplates'] = []
        if self.data_ingestion_templates is not None:
            for k in self.data_ingestion_templates:
                result['DataIngestionTemplates'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_ingestion_templates = []
        if m.get('DataIngestionTemplates') is not None:
            for k in m.get('DataIngestionTemplates'):
                temp_model = ListDataIngestionTemplatesResponseBodyDataIngestionTemplates()
                self.data_ingestion_templates.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListDataIngestionTemplatesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDataIngestionTemplatesResponseBody = None,
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
            temp_model = ListDataIngestionTemplatesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDataIngestionsRequest(TeaModel):
    def __init__(
        self,
        data_ingestion_ids: List[str] = None,
        data_ingestion_status: str = None,
        data_ingestion_template_ids: List[str] = None,
        lang: str = None,
        product_id: str = None,
        region_id: str = None,
        role_for: int = None,
    ):
        self.data_ingestion_ids = data_ingestion_ids
        self.data_ingestion_status = data_ingestion_status
        self.data_ingestion_template_ids = data_ingestion_template_ids
        self.lang = lang
        self.product_id = product_id
        self.region_id = region_id
        self.role_for = role_for

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_ingestion_ids is not None:
            result['DataIngestionIds'] = self.data_ingestion_ids
        if self.data_ingestion_status is not None:
            result['DataIngestionStatus'] = self.data_ingestion_status
        if self.data_ingestion_template_ids is not None:
            result['DataIngestionTemplateIds'] = self.data_ingestion_template_ids
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.role_for is not None:
            result['RoleFor'] = self.role_for
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataIngestionIds') is not None:
            self.data_ingestion_ids = m.get('DataIngestionIds')
        if m.get('DataIngestionStatus') is not None:
            self.data_ingestion_status = m.get('DataIngestionStatus')
        if m.get('DataIngestionTemplateIds') is not None:
            self.data_ingestion_template_ids = m.get('DataIngestionTemplateIds')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')
        return self


class ListDataIngestionsShrinkRequest(TeaModel):
    def __init__(
        self,
        data_ingestion_ids_shrink: str = None,
        data_ingestion_status: str = None,
        data_ingestion_template_ids_shrink: str = None,
        lang: str = None,
        product_id: str = None,
        region_id: str = None,
        role_for: int = None,
    ):
        self.data_ingestion_ids_shrink = data_ingestion_ids_shrink
        self.data_ingestion_status = data_ingestion_status
        self.data_ingestion_template_ids_shrink = data_ingestion_template_ids_shrink
        self.lang = lang
        self.product_id = product_id
        self.region_id = region_id
        self.role_for = role_for

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_ingestion_ids_shrink is not None:
            result['DataIngestionIds'] = self.data_ingestion_ids_shrink
        if self.data_ingestion_status is not None:
            result['DataIngestionStatus'] = self.data_ingestion_status
        if self.data_ingestion_template_ids_shrink is not None:
            result['DataIngestionTemplateIds'] = self.data_ingestion_template_ids_shrink
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.role_for is not None:
            result['RoleFor'] = self.role_for
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataIngestionIds') is not None:
            self.data_ingestion_ids_shrink = m.get('DataIngestionIds')
        if m.get('DataIngestionStatus') is not None:
            self.data_ingestion_status = m.get('DataIngestionStatus')
        if m.get('DataIngestionTemplateIds') is not None:
            self.data_ingestion_template_ids_shrink = m.get('DataIngestionTemplateIds')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')
        return self


class ListDataIngestionsResponseBodyDataIngestions(TeaModel):
    def __init__(
        self,
        active_time: int = None,
        capacity_count: int = None,
        create_time: int = None,
        data_ingestion_id: str = None,
        data_ingestion_mode: str = None,
        data_ingestion_mode_editable: bool = None,
        data_ingestion_state: str = None,
        data_ingestion_state_code: str = None,
        data_ingestion_status: str = None,
        data_ingestion_template_id: str = None,
        data_ingestion_type: str = None,
        data_source_editable: bool = None,
        data_source_id: str = None,
        normalization_rule_editable: bool = None,
        normalization_rule_id: str = None,
        realtime_data_source_id: str = None,
        scan_data_source_id: str = None,
        stream_job_id: str = None,
        update_time: int = None,
    ):
        self.active_time = active_time
        self.capacity_count = capacity_count
        self.create_time = create_time
        self.data_ingestion_id = data_ingestion_id
        self.data_ingestion_mode = data_ingestion_mode
        self.data_ingestion_mode_editable = data_ingestion_mode_editable
        self.data_ingestion_state = data_ingestion_state
        self.data_ingestion_state_code = data_ingestion_state_code
        self.data_ingestion_status = data_ingestion_status
        self.data_ingestion_template_id = data_ingestion_template_id
        self.data_ingestion_type = data_ingestion_type
        self.data_source_editable = data_source_editable
        self.data_source_id = data_source_id
        self.normalization_rule_editable = normalization_rule_editable
        self.normalization_rule_id = normalization_rule_id
        self.realtime_data_source_id = realtime_data_source_id
        self.scan_data_source_id = scan_data_source_id
        self.stream_job_id = stream_job_id
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active_time is not None:
            result['ActiveTime'] = self.active_time
        if self.capacity_count is not None:
            result['CapacityCount'] = self.capacity_count
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.data_ingestion_id is not None:
            result['DataIngestionId'] = self.data_ingestion_id
        if self.data_ingestion_mode is not None:
            result['DataIngestionMode'] = self.data_ingestion_mode
        if self.data_ingestion_mode_editable is not None:
            result['DataIngestionModeEditable'] = self.data_ingestion_mode_editable
        if self.data_ingestion_state is not None:
            result['DataIngestionState'] = self.data_ingestion_state
        if self.data_ingestion_state_code is not None:
            result['DataIngestionStateCode'] = self.data_ingestion_state_code
        if self.data_ingestion_status is not None:
            result['DataIngestionStatus'] = self.data_ingestion_status
        if self.data_ingestion_template_id is not None:
            result['DataIngestionTemplateId'] = self.data_ingestion_template_id
        if self.data_ingestion_type is not None:
            result['DataIngestionType'] = self.data_ingestion_type
        if self.data_source_editable is not None:
            result['DataSourceEditable'] = self.data_source_editable
        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id
        if self.normalization_rule_editable is not None:
            result['NormalizationRuleEditable'] = self.normalization_rule_editable
        if self.normalization_rule_id is not None:
            result['NormalizationRuleId'] = self.normalization_rule_id
        if self.realtime_data_source_id is not None:
            result['RealtimeDataSourceId'] = self.realtime_data_source_id
        if self.scan_data_source_id is not None:
            result['ScanDataSourceId'] = self.scan_data_source_id
        if self.stream_job_id is not None:
            result['StreamJobId'] = self.stream_job_id
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActiveTime') is not None:
            self.active_time = m.get('ActiveTime')
        if m.get('CapacityCount') is not None:
            self.capacity_count = m.get('CapacityCount')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DataIngestionId') is not None:
            self.data_ingestion_id = m.get('DataIngestionId')
        if m.get('DataIngestionMode') is not None:
            self.data_ingestion_mode = m.get('DataIngestionMode')
        if m.get('DataIngestionModeEditable') is not None:
            self.data_ingestion_mode_editable = m.get('DataIngestionModeEditable')
        if m.get('DataIngestionState') is not None:
            self.data_ingestion_state = m.get('DataIngestionState')
        if m.get('DataIngestionStateCode') is not None:
            self.data_ingestion_state_code = m.get('DataIngestionStateCode')
        if m.get('DataIngestionStatus') is not None:
            self.data_ingestion_status = m.get('DataIngestionStatus')
        if m.get('DataIngestionTemplateId') is not None:
            self.data_ingestion_template_id = m.get('DataIngestionTemplateId')
        if m.get('DataIngestionType') is not None:
            self.data_ingestion_type = m.get('DataIngestionType')
        if m.get('DataSourceEditable') is not None:
            self.data_source_editable = m.get('DataSourceEditable')
        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')
        if m.get('NormalizationRuleEditable') is not None:
            self.normalization_rule_editable = m.get('NormalizationRuleEditable')
        if m.get('NormalizationRuleId') is not None:
            self.normalization_rule_id = m.get('NormalizationRuleId')
        if m.get('RealtimeDataSourceId') is not None:
            self.realtime_data_source_id = m.get('RealtimeDataSourceId')
        if m.get('ScanDataSourceId') is not None:
            self.scan_data_source_id = m.get('ScanDataSourceId')
        if m.get('StreamJobId') is not None:
            self.stream_job_id = m.get('StreamJobId')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class ListDataIngestionsResponseBody(TeaModel):
    def __init__(
        self,
        data_ingestions: List[ListDataIngestionsResponseBodyDataIngestions] = None,
        request_id: str = None,
    ):
        self.data_ingestions = data_ingestions
        self.request_id = request_id

    def validate(self):
        if self.data_ingestions:
            for k in self.data_ingestions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataIngestions'] = []
        if self.data_ingestions is not None:
            for k in self.data_ingestions:
                result['DataIngestions'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_ingestions = []
        if m.get('DataIngestions') is not None:
            for k in m.get('DataIngestions'):
                temp_model = ListDataIngestionsResponseBodyDataIngestions()
                self.data_ingestions.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListDataIngestionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDataIngestionsResponseBody = None,
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
            temp_model = ListDataIngestionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDataSetRecordsRequest(TeaModel):
    def __init__(
        self,
        data_set_id: str = None,
        lang: str = None,
        max_results: int = None,
        next_token: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        role_for: int = None,
    ):
        # This parameter is required.
        self.data_set_id = data_set_id
        self.lang = lang
        self.max_results = max_results
        self.next_token = next_token
        # This parameter is required.
        self.page_number = page_number
        # This parameter is required.
        self.page_size = page_size
        self.region_id = region_id
        self.role_for = role_for

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_set_id is not None:
            result['DataSetId'] = self.data_set_id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.role_for is not None:
            result['RoleFor'] = self.role_for
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSetId') is not None:
            self.data_set_id = m.get('DataSetId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')
        return self


class ListDataSetRecordsResponseBodyDataSetRecords(TeaModel):
    def __init__(
        self,
        create_time: int = None,
        data_set_id: str = None,
        data_set_name: str = None,
        data_set_record_id: str = None,
        data_set_record_values: str = None,
        update_time: int = None,
    ):
        self.create_time = create_time
        self.data_set_id = data_set_id
        self.data_set_name = data_set_name
        self.data_set_record_id = data_set_record_id
        self.data_set_record_values = data_set_record_values
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.data_set_id is not None:
            result['DataSetId'] = self.data_set_id
        if self.data_set_name is not None:
            result['DataSetName'] = self.data_set_name
        if self.data_set_record_id is not None:
            result['DataSetRecordId'] = self.data_set_record_id
        if self.data_set_record_values is not None:
            result['DataSetRecordValues'] = self.data_set_record_values
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DataSetId') is not None:
            self.data_set_id = m.get('DataSetId')
        if m.get('DataSetName') is not None:
            self.data_set_name = m.get('DataSetName')
        if m.get('DataSetRecordId') is not None:
            self.data_set_record_id = m.get('DataSetRecordId')
        if m.get('DataSetRecordValues') is not None:
            self.data_set_record_values = m.get('DataSetRecordValues')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class ListDataSetRecordsResponseBody(TeaModel):
    def __init__(
        self,
        data_set_records: List[ListDataSetRecordsResponseBodyDataSetRecords] = None,
        max_results: int = None,
        next_token: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.data_set_records = data_set_records
        self.max_results = max_results
        self.next_token = next_token
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.data_set_records:
            for k in self.data_set_records:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataSetRecords'] = []
        if self.data_set_records is not None:
            for k in self.data_set_records:
                result['DataSetRecords'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_set_records = []
        if m.get('DataSetRecords') is not None:
            for k in m.get('DataSetRecords'):
                temp_model = ListDataSetRecordsResponseBodyDataSetRecords()
                self.data_set_records.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListDataSetRecordsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDataSetRecordsResponseBody = None,
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
            temp_model = ListDataSetRecordsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDataSetsRequest(TeaModel):
    def __init__(
        self,
        data_set_id: str = None,
        data_set_ids: List[str] = None,
        data_set_name: str = None,
        data_set_status: int = None,
        data_set_type: str = None,
        lang: str = None,
        max_results: int = None,
        next_token: str = None,
        order_direction: str = None,
        order_field_name: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        role_for: int = None,
    ):
        self.data_set_id = data_set_id
        self.data_set_ids = data_set_ids
        self.data_set_name = data_set_name
        self.data_set_status = data_set_status
        self.data_set_type = data_set_type
        self.lang = lang
        self.max_results = max_results
        self.next_token = next_token
        self.order_direction = order_direction
        self.order_field_name = order_field_name
        self.page_number = page_number
        self.page_size = page_size
        self.region_id = region_id
        self.role_for = role_for

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_set_id is not None:
            result['DataSetId'] = self.data_set_id
        if self.data_set_ids is not None:
            result['DataSetIds'] = self.data_set_ids
        if self.data_set_name is not None:
            result['DataSetName'] = self.data_set_name
        if self.data_set_status is not None:
            result['DataSetStatus'] = self.data_set_status
        if self.data_set_type is not None:
            result['DataSetType'] = self.data_set_type
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.order_direction is not None:
            result['OrderDirection'] = self.order_direction
        if self.order_field_name is not None:
            result['OrderFieldName'] = self.order_field_name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.role_for is not None:
            result['RoleFor'] = self.role_for
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSetId') is not None:
            self.data_set_id = m.get('DataSetId')
        if m.get('DataSetIds') is not None:
            self.data_set_ids = m.get('DataSetIds')
        if m.get('DataSetName') is not None:
            self.data_set_name = m.get('DataSetName')
        if m.get('DataSetStatus') is not None:
            self.data_set_status = m.get('DataSetStatus')
        if m.get('DataSetType') is not None:
            self.data_set_type = m.get('DataSetType')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OrderDirection') is not None:
            self.order_direction = m.get('OrderDirection')
        if m.get('OrderFieldName') is not None:
            self.order_field_name = m.get('OrderFieldName')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')
        return self


class ListDataSetsShrinkRequest(TeaModel):
    def __init__(
        self,
        data_set_id: str = None,
        data_set_ids_shrink: str = None,
        data_set_name: str = None,
        data_set_status: int = None,
        data_set_type: str = None,
        lang: str = None,
        max_results: int = None,
        next_token: str = None,
        order_direction: str = None,
        order_field_name: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        role_for: int = None,
    ):
        self.data_set_id = data_set_id
        self.data_set_ids_shrink = data_set_ids_shrink
        self.data_set_name = data_set_name
        self.data_set_status = data_set_status
        self.data_set_type = data_set_type
        self.lang = lang
        self.max_results = max_results
        self.next_token = next_token
        self.order_direction = order_direction
        self.order_field_name = order_field_name
        self.page_number = page_number
        self.page_size = page_size
        self.region_id = region_id
        self.role_for = role_for

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_set_id is not None:
            result['DataSetId'] = self.data_set_id
        if self.data_set_ids_shrink is not None:
            result['DataSetIds'] = self.data_set_ids_shrink
        if self.data_set_name is not None:
            result['DataSetName'] = self.data_set_name
        if self.data_set_status is not None:
            result['DataSetStatus'] = self.data_set_status
        if self.data_set_type is not None:
            result['DataSetType'] = self.data_set_type
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.order_direction is not None:
            result['OrderDirection'] = self.order_direction
        if self.order_field_name is not None:
            result['OrderFieldName'] = self.order_field_name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.role_for is not None:
            result['RoleFor'] = self.role_for
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSetId') is not None:
            self.data_set_id = m.get('DataSetId')
        if m.get('DataSetIds') is not None:
            self.data_set_ids_shrink = m.get('DataSetIds')
        if m.get('DataSetName') is not None:
            self.data_set_name = m.get('DataSetName')
        if m.get('DataSetStatus') is not None:
            self.data_set_status = m.get('DataSetStatus')
        if m.get('DataSetType') is not None:
            self.data_set_type = m.get('DataSetType')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OrderDirection') is not None:
            self.order_direction = m.get('OrderDirection')
        if m.get('OrderFieldName') is not None:
            self.order_field_name = m.get('OrderFieldName')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')
        return self


class ListDataSetsResponseBodyDataSetsDataSetReferences(TeaModel):
    def __init__(
        self,
        data_set_id: str = None,
        data_set_reference_id: str = None,
        data_set_reference_name: str = None,
        data_set_reference_type: str = None,
    ):
        self.data_set_id = data_set_id
        self.data_set_reference_id = data_set_reference_id
        self.data_set_reference_name = data_set_reference_name
        self.data_set_reference_type = data_set_reference_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_set_id is not None:
            result['DataSetId'] = self.data_set_id
        if self.data_set_reference_id is not None:
            result['DataSetReferenceId'] = self.data_set_reference_id
        if self.data_set_reference_name is not None:
            result['DataSetReferenceName'] = self.data_set_reference_name
        if self.data_set_reference_type is not None:
            result['DataSetReferenceType'] = self.data_set_reference_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSetId') is not None:
            self.data_set_id = m.get('DataSetId')
        if m.get('DataSetReferenceId') is not None:
            self.data_set_reference_id = m.get('DataSetReferenceId')
        if m.get('DataSetReferenceName') is not None:
            self.data_set_reference_name = m.get('DataSetReferenceName')
        if m.get('DataSetReferenceType') is not None:
            self.data_set_reference_type = m.get('DataSetReferenceType')
        return self


class ListDataSetsResponseBodyDataSetsIpWhitelistRecognizers(TeaModel):
    def __init__(
        self,
        auto_recognize_status: str = None,
        ip_whitelist_recognizer_type: str = None,
        recognize_scope: str = None,
        update_time: int = None,
    ):
        self.auto_recognize_status = auto_recognize_status
        self.ip_whitelist_recognizer_type = ip_whitelist_recognizer_type
        self.recognize_scope = recognize_scope
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_recognize_status is not None:
            result['AutoRecognizeStatus'] = self.auto_recognize_status
        if self.ip_whitelist_recognizer_type is not None:
            result['IpWhitelistRecognizerType'] = self.ip_whitelist_recognizer_type
        if self.recognize_scope is not None:
            result['RecognizeScope'] = self.recognize_scope
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoRecognizeStatus') is not None:
            self.auto_recognize_status = m.get('AutoRecognizeStatus')
        if m.get('IpWhitelistRecognizerType') is not None:
            self.ip_whitelist_recognizer_type = m.get('IpWhitelistRecognizerType')
        if m.get('RecognizeScope') is not None:
            self.recognize_scope = m.get('RecognizeScope')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class ListDataSetsResponseBodyDataSets(TeaModel):
    def __init__(
        self,
        create_time: int = None,
        data_set_description: str = None,
        data_set_field_key_name: str = None,
        data_set_field_names: str = None,
        data_set_file_name: str = None,
        data_set_id: str = None,
        data_set_name: str = None,
        data_set_references: List[ListDataSetsResponseBodyDataSetsDataSetReferences] = None,
        data_set_status: int = None,
        data_set_type: str = None,
        ip_whitelist_recognizers: List[ListDataSetsResponseBodyDataSetsIpWhitelistRecognizers] = None,
        update_time: int = None,
    ):
        self.create_time = create_time
        self.data_set_description = data_set_description
        self.data_set_field_key_name = data_set_field_key_name
        self.data_set_field_names = data_set_field_names
        self.data_set_file_name = data_set_file_name
        self.data_set_id = data_set_id
        self.data_set_name = data_set_name
        self.data_set_references = data_set_references
        self.data_set_status = data_set_status
        self.data_set_type = data_set_type
        self.ip_whitelist_recognizers = ip_whitelist_recognizers
        self.update_time = update_time

    def validate(self):
        if self.data_set_references:
            for k in self.data_set_references:
                if k:
                    k.validate()
        if self.ip_whitelist_recognizers:
            for k in self.ip_whitelist_recognizers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.data_set_description is not None:
            result['DataSetDescription'] = self.data_set_description
        if self.data_set_field_key_name is not None:
            result['DataSetFieldKeyName'] = self.data_set_field_key_name
        if self.data_set_field_names is not None:
            result['DataSetFieldNames'] = self.data_set_field_names
        if self.data_set_file_name is not None:
            result['DataSetFileName'] = self.data_set_file_name
        if self.data_set_id is not None:
            result['DataSetId'] = self.data_set_id
        if self.data_set_name is not None:
            result['DataSetName'] = self.data_set_name
        result['DataSetReferences'] = []
        if self.data_set_references is not None:
            for k in self.data_set_references:
                result['DataSetReferences'].append(k.to_map() if k else None)
        if self.data_set_status is not None:
            result['DataSetStatus'] = self.data_set_status
        if self.data_set_type is not None:
            result['DataSetType'] = self.data_set_type
        result['IpWhitelistRecognizers'] = []
        if self.ip_whitelist_recognizers is not None:
            for k in self.ip_whitelist_recognizers:
                result['IpWhitelistRecognizers'].append(k.to_map() if k else None)
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DataSetDescription') is not None:
            self.data_set_description = m.get('DataSetDescription')
        if m.get('DataSetFieldKeyName') is not None:
            self.data_set_field_key_name = m.get('DataSetFieldKeyName')
        if m.get('DataSetFieldNames') is not None:
            self.data_set_field_names = m.get('DataSetFieldNames')
        if m.get('DataSetFileName') is not None:
            self.data_set_file_name = m.get('DataSetFileName')
        if m.get('DataSetId') is not None:
            self.data_set_id = m.get('DataSetId')
        if m.get('DataSetName') is not None:
            self.data_set_name = m.get('DataSetName')
        self.data_set_references = []
        if m.get('DataSetReferences') is not None:
            for k in m.get('DataSetReferences'):
                temp_model = ListDataSetsResponseBodyDataSetsDataSetReferences()
                self.data_set_references.append(temp_model.from_map(k))
        if m.get('DataSetStatus') is not None:
            self.data_set_status = m.get('DataSetStatus')
        if m.get('DataSetType') is not None:
            self.data_set_type = m.get('DataSetType')
        self.ip_whitelist_recognizers = []
        if m.get('IpWhitelistRecognizers') is not None:
            for k in m.get('IpWhitelistRecognizers'):
                temp_model = ListDataSetsResponseBodyDataSetsIpWhitelistRecognizers()
                self.ip_whitelist_recognizers.append(temp_model.from_map(k))
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class ListDataSetsResponseBody(TeaModel):
    def __init__(
        self,
        data_sets: List[ListDataSetsResponseBodyDataSets] = None,
        max_results: int = None,
        next_token: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.data_sets = data_sets
        self.max_results = max_results
        self.next_token = next_token
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.data_sets:
            for k in self.data_sets:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataSets'] = []
        if self.data_sets is not None:
            for k in self.data_sets:
                result['DataSets'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_sets = []
        if m.get('DataSets') is not None:
            for k in m.get('DataSets'):
                temp_model = ListDataSetsResponseBodyDataSets()
                self.data_sets.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListDataSetsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDataSetsResponseBody = None,
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
            temp_model = ListDataSetsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDataSourceTemplatesRequest(TeaModel):
    def __init__(
        self,
        data_source_template_ids: List[str] = None,
        lang: str = None,
        page_number: str = None,
        page_size: str = None,
        region_id: str = None,
        role_for: int = None,
    ):
        self.data_source_template_ids = data_source_template_ids
        self.lang = lang
        self.page_number = page_number
        self.page_size = page_size
        self.region_id = region_id
        self.role_for = role_for

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_source_template_ids is not None:
            result['DataSourceTemplateIds'] = self.data_source_template_ids
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.role_for is not None:
            result['RoleFor'] = self.role_for
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSourceTemplateIds') is not None:
            self.data_source_template_ids = m.get('DataSourceTemplateIds')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')
        return self


class ListDataSourceTemplatesShrinkRequest(TeaModel):
    def __init__(
        self,
        data_source_template_ids_shrink: str = None,
        lang: str = None,
        page_number: str = None,
        page_size: str = None,
        region_id: str = None,
        role_for: int = None,
    ):
        self.data_source_template_ids_shrink = data_source_template_ids_shrink
        self.lang = lang
        self.page_number = page_number
        self.page_size = page_size
        self.region_id = region_id
        self.role_for = role_for

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_source_template_ids_shrink is not None:
            result['DataSourceTemplateIds'] = self.data_source_template_ids_shrink
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.role_for is not None:
            result['RoleFor'] = self.role_for
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSourceTemplateIds') is not None:
            self.data_source_template_ids_shrink = m.get('DataSourceTemplateIds')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')
        return self


class ListDataSourceTemplatesResponseBodyDataSourceTemplates(TeaModel):
    def __init__(
        self,
        auto_scan_new: str = None,
        create_time: int = None,
        data_source_from: str = None,
        data_source_recognize_enabled: bool = None,
        data_source_recognizer: str = None,
        data_source_template_id: str = None,
        data_source_template_name: str = None,
        log_project_pattern: str = None,
        log_region_ids: List[str] = None,
        log_store_pattern: str = None,
        log_user_ids: List[str] = None,
        update_time: int = None,
    ):
        self.auto_scan_new = auto_scan_new
        self.create_time = create_time
        self.data_source_from = data_source_from
        self.data_source_recognize_enabled = data_source_recognize_enabled
        self.data_source_recognizer = data_source_recognizer
        self.data_source_template_id = data_source_template_id
        self.data_source_template_name = data_source_template_name
        self.log_project_pattern = log_project_pattern
        self.log_region_ids = log_region_ids
        self.log_store_pattern = log_store_pattern
        self.log_user_ids = log_user_ids
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_scan_new is not None:
            result['AutoScanNew'] = self.auto_scan_new
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.data_source_from is not None:
            result['DataSourceFrom'] = self.data_source_from
        if self.data_source_recognize_enabled is not None:
            result['DataSourceRecognizeEnabled'] = self.data_source_recognize_enabled
        if self.data_source_recognizer is not None:
            result['DataSourceRecognizer'] = self.data_source_recognizer
        if self.data_source_template_id is not None:
            result['DataSourceTemplateId'] = self.data_source_template_id
        if self.data_source_template_name is not None:
            result['DataSourceTemplateName'] = self.data_source_template_name
        if self.log_project_pattern is not None:
            result['LogProjectPattern'] = self.log_project_pattern
        if self.log_region_ids is not None:
            result['LogRegionIds'] = self.log_region_ids
        if self.log_store_pattern is not None:
            result['LogStorePattern'] = self.log_store_pattern
        if self.log_user_ids is not None:
            result['LogUserIds'] = self.log_user_ids
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoScanNew') is not None:
            self.auto_scan_new = m.get('AutoScanNew')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DataSourceFrom') is not None:
            self.data_source_from = m.get('DataSourceFrom')
        if m.get('DataSourceRecognizeEnabled') is not None:
            self.data_source_recognize_enabled = m.get('DataSourceRecognizeEnabled')
        if m.get('DataSourceRecognizer') is not None:
            self.data_source_recognizer = m.get('DataSourceRecognizer')
        if m.get('DataSourceTemplateId') is not None:
            self.data_source_template_id = m.get('DataSourceTemplateId')
        if m.get('DataSourceTemplateName') is not None:
            self.data_source_template_name = m.get('DataSourceTemplateName')
        if m.get('LogProjectPattern') is not None:
            self.log_project_pattern = m.get('LogProjectPattern')
        if m.get('LogRegionIds') is not None:
            self.log_region_ids = m.get('LogRegionIds')
        if m.get('LogStorePattern') is not None:
            self.log_store_pattern = m.get('LogStorePattern')
        if m.get('LogUserIds') is not None:
            self.log_user_ids = m.get('LogUserIds')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class ListDataSourceTemplatesResponseBody(TeaModel):
    def __init__(
        self,
        data_source_templates: List[ListDataSourceTemplatesResponseBodyDataSourceTemplates] = None,
        page_number: str = None,
        page_size: str = None,
        request_id: str = None,
    ):
        self.data_source_templates = data_source_templates
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id

    def validate(self):
        if self.data_source_templates:
            for k in self.data_source_templates:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataSourceTemplates'] = []
        if self.data_source_templates is not None:
            for k in self.data_source_templates:
                result['DataSourceTemplates'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_source_templates = []
        if m.get('DataSourceTemplates') is not None:
            for k in m.get('DataSourceTemplates'):
                temp_model = ListDataSourceTemplatesResponseBodyDataSourceTemplates()
                self.data_source_templates.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListDataSourceTemplatesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDataSourceTemplatesResponseBody = None,
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
            temp_model = ListDataSourceTemplatesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDataSourcesRequest(TeaModel):
    def __init__(
        self,
        data_source_from: str = None,
        data_source_ids: List[str] = None,
        data_source_name: str = None,
        data_source_status: str = None,
        data_source_store_status: str = None,
        data_source_template_ids: List[str] = None,
        data_source_type: str = None,
        lang: str = None,
        log_project_name: str = None,
        log_region_id: str = None,
        log_store_name: str = None,
        log_user_ids: List[int] = None,
        max_results: int = None,
        next_token: str = None,
        order: str = None,
        order_field: str = None,
        page_number: str = None,
        page_size: str = None,
        region_id: str = None,
        role_for: int = None,
    ):
        self.data_source_from = data_source_from
        self.data_source_ids = data_source_ids
        self.data_source_name = data_source_name
        self.data_source_status = data_source_status
        self.data_source_store_status = data_source_store_status
        self.data_source_template_ids = data_source_template_ids
        self.data_source_type = data_source_type
        self.lang = lang
        self.log_project_name = log_project_name
        self.log_region_id = log_region_id
        self.log_store_name = log_store_name
        self.log_user_ids = log_user_ids
        self.max_results = max_results
        self.next_token = next_token
        self.order = order
        self.order_field = order_field
        self.page_number = page_number
        self.page_size = page_size
        self.region_id = region_id
        self.role_for = role_for

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_source_from is not None:
            result['DataSourceFrom'] = self.data_source_from
        if self.data_source_ids is not None:
            result['DataSourceIds'] = self.data_source_ids
        if self.data_source_name is not None:
            result['DataSourceName'] = self.data_source_name
        if self.data_source_status is not None:
            result['DataSourceStatus'] = self.data_source_status
        if self.data_source_store_status is not None:
            result['DataSourceStoreStatus'] = self.data_source_store_status
        if self.data_source_template_ids is not None:
            result['DataSourceTemplateIds'] = self.data_source_template_ids
        if self.data_source_type is not None:
            result['DataSourceType'] = self.data_source_type
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.log_project_name is not None:
            result['LogProjectName'] = self.log_project_name
        if self.log_region_id is not None:
            result['LogRegionId'] = self.log_region_id
        if self.log_store_name is not None:
            result['LogStoreName'] = self.log_store_name
        if self.log_user_ids is not None:
            result['LogUserIds'] = self.log_user_ids
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.order is not None:
            result['Order'] = self.order
        if self.order_field is not None:
            result['OrderField'] = self.order_field
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.role_for is not None:
            result['RoleFor'] = self.role_for
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSourceFrom') is not None:
            self.data_source_from = m.get('DataSourceFrom')
        if m.get('DataSourceIds') is not None:
            self.data_source_ids = m.get('DataSourceIds')
        if m.get('DataSourceName') is not None:
            self.data_source_name = m.get('DataSourceName')
        if m.get('DataSourceStatus') is not None:
            self.data_source_status = m.get('DataSourceStatus')
        if m.get('DataSourceStoreStatus') is not None:
            self.data_source_store_status = m.get('DataSourceStoreStatus')
        if m.get('DataSourceTemplateIds') is not None:
            self.data_source_template_ids = m.get('DataSourceTemplateIds')
        if m.get('DataSourceType') is not None:
            self.data_source_type = m.get('DataSourceType')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('LogProjectName') is not None:
            self.log_project_name = m.get('LogProjectName')
        if m.get('LogRegionId') is not None:
            self.log_region_id = m.get('LogRegionId')
        if m.get('LogStoreName') is not None:
            self.log_store_name = m.get('LogStoreName')
        if m.get('LogUserIds') is not None:
            self.log_user_ids = m.get('LogUserIds')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('OrderField') is not None:
            self.order_field = m.get('OrderField')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')
        return self


class ListDataSourcesShrinkRequest(TeaModel):
    def __init__(
        self,
        data_source_from: str = None,
        data_source_ids_shrink: str = None,
        data_source_name: str = None,
        data_source_status: str = None,
        data_source_store_status: str = None,
        data_source_template_ids_shrink: str = None,
        data_source_type: str = None,
        lang: str = None,
        log_project_name: str = None,
        log_region_id: str = None,
        log_store_name: str = None,
        log_user_ids_shrink: str = None,
        max_results: int = None,
        next_token: str = None,
        order: str = None,
        order_field: str = None,
        page_number: str = None,
        page_size: str = None,
        region_id: str = None,
        role_for: int = None,
    ):
        self.data_source_from = data_source_from
        self.data_source_ids_shrink = data_source_ids_shrink
        self.data_source_name = data_source_name
        self.data_source_status = data_source_status
        self.data_source_store_status = data_source_store_status
        self.data_source_template_ids_shrink = data_source_template_ids_shrink
        self.data_source_type = data_source_type
        self.lang = lang
        self.log_project_name = log_project_name
        self.log_region_id = log_region_id
        self.log_store_name = log_store_name
        self.log_user_ids_shrink = log_user_ids_shrink
        self.max_results = max_results
        self.next_token = next_token
        self.order = order
        self.order_field = order_field
        self.page_number = page_number
        self.page_size = page_size
        self.region_id = region_id
        self.role_for = role_for

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_source_from is not None:
            result['DataSourceFrom'] = self.data_source_from
        if self.data_source_ids_shrink is not None:
            result['DataSourceIds'] = self.data_source_ids_shrink
        if self.data_source_name is not None:
            result['DataSourceName'] = self.data_source_name
        if self.data_source_status is not None:
            result['DataSourceStatus'] = self.data_source_status
        if self.data_source_store_status is not None:
            result['DataSourceStoreStatus'] = self.data_source_store_status
        if self.data_source_template_ids_shrink is not None:
            result['DataSourceTemplateIds'] = self.data_source_template_ids_shrink
        if self.data_source_type is not None:
            result['DataSourceType'] = self.data_source_type
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.log_project_name is not None:
            result['LogProjectName'] = self.log_project_name
        if self.log_region_id is not None:
            result['LogRegionId'] = self.log_region_id
        if self.log_store_name is not None:
            result['LogStoreName'] = self.log_store_name
        if self.log_user_ids_shrink is not None:
            result['LogUserIds'] = self.log_user_ids_shrink
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.order is not None:
            result['Order'] = self.order
        if self.order_field is not None:
            result['OrderField'] = self.order_field
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.role_for is not None:
            result['RoleFor'] = self.role_for
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSourceFrom') is not None:
            self.data_source_from = m.get('DataSourceFrom')
        if m.get('DataSourceIds') is not None:
            self.data_source_ids_shrink = m.get('DataSourceIds')
        if m.get('DataSourceName') is not None:
            self.data_source_name = m.get('DataSourceName')
        if m.get('DataSourceStatus') is not None:
            self.data_source_status = m.get('DataSourceStatus')
        if m.get('DataSourceStoreStatus') is not None:
            self.data_source_store_status = m.get('DataSourceStoreStatus')
        if m.get('DataSourceTemplateIds') is not None:
            self.data_source_template_ids_shrink = m.get('DataSourceTemplateIds')
        if m.get('DataSourceType') is not None:
            self.data_source_type = m.get('DataSourceType')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('LogProjectName') is not None:
            self.log_project_name = m.get('LogProjectName')
        if m.get('LogRegionId') is not None:
            self.log_region_id = m.get('LogRegionId')
        if m.get('LogStoreName') is not None:
            self.log_store_name = m.get('LogStoreName')
        if m.get('LogUserIds') is not None:
            self.log_user_ids_shrink = m.get('LogUserIds')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('OrderField') is not None:
            self.order_field = m.get('OrderField')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')
        return self


class ListDataSourcesResponseBodyDataSourcesDataSourceReferences(TeaModel):
    def __init__(
        self,
        data_ingestion_id: str = None,
    ):
        self.data_ingestion_id = data_ingestion_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_ingestion_id is not None:
            result['DataIngestionId'] = self.data_ingestion_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataIngestionId') is not None:
            self.data_ingestion_id = m.get('DataIngestionId')
        return self


class ListDataSourcesResponseBodyDataSourcesDataSourceStores(TeaModel):
    def __init__(
        self,
        check_time: int = None,
        create_time: int = None,
        data_source_store_from: str = None,
        data_source_store_id: str = None,
        data_source_store_status: str = None,
        log_project_name: str = None,
        log_region_id: str = None,
        log_store_name: str = None,
        update_time: int = None,
    ):
        self.check_time = check_time
        self.create_time = create_time
        self.data_source_store_from = data_source_store_from
        self.data_source_store_id = data_source_store_id
        self.data_source_store_status = data_source_store_status
        self.log_project_name = log_project_name
        self.log_region_id = log_region_id
        self.log_store_name = log_store_name
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_time is not None:
            result['CheckTime'] = self.check_time
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.data_source_store_from is not None:
            result['DataSourceStoreFrom'] = self.data_source_store_from
        if self.data_source_store_id is not None:
            result['DataSourceStoreId'] = self.data_source_store_id
        if self.data_source_store_status is not None:
            result['DataSourceStoreStatus'] = self.data_source_store_status
        if self.log_project_name is not None:
            result['LogProjectName'] = self.log_project_name
        if self.log_region_id is not None:
            result['LogRegionId'] = self.log_region_id
        if self.log_store_name is not None:
            result['LogStoreName'] = self.log_store_name
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckTime') is not None:
            self.check_time = m.get('CheckTime')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DataSourceStoreFrom') is not None:
            self.data_source_store_from = m.get('DataSourceStoreFrom')
        if m.get('DataSourceStoreId') is not None:
            self.data_source_store_id = m.get('DataSourceStoreId')
        if m.get('DataSourceStoreStatus') is not None:
            self.data_source_store_status = m.get('DataSourceStoreStatus')
        if m.get('LogProjectName') is not None:
            self.log_project_name = m.get('LogProjectName')
        if m.get('LogRegionId') is not None:
            self.log_region_id = m.get('LogRegionId')
        if m.get('LogStoreName') is not None:
            self.log_store_name = m.get('LogStoreName')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class ListDataSourcesResponseBodyDataSources(TeaModel):
    def __init__(
        self,
        create_time: int = None,
        data_source_from: str = None,
        data_source_id: str = None,
        data_source_name: str = None,
        data_source_recognize_enabled: bool = None,
        data_source_recognizer: str = None,
        data_source_references: List[ListDataSourcesResponseBodyDataSourcesDataSourceReferences] = None,
        data_source_status: str = None,
        data_source_stores: List[ListDataSourcesResponseBodyDataSourcesDataSourceStores] = None,
        data_source_template_id: str = None,
        data_source_type: str = None,
        log_project_name: str = None,
        log_region_id: str = None,
        log_store_name: str = None,
        log_user_id: int = None,
        update_time: int = None,
    ):
        self.create_time = create_time
        self.data_source_from = data_source_from
        self.data_source_id = data_source_id
        self.data_source_name = data_source_name
        self.data_source_recognize_enabled = data_source_recognize_enabled
        self.data_source_recognizer = data_source_recognizer
        self.data_source_references = data_source_references
        self.data_source_status = data_source_status
        self.data_source_stores = data_source_stores
        self.data_source_template_id = data_source_template_id
        self.data_source_type = data_source_type
        self.log_project_name = log_project_name
        self.log_region_id = log_region_id
        self.log_store_name = log_store_name
        self.log_user_id = log_user_id
        self.update_time = update_time

    def validate(self):
        if self.data_source_references:
            for k in self.data_source_references:
                if k:
                    k.validate()
        if self.data_source_stores:
            for k in self.data_source_stores:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.data_source_from is not None:
            result['DataSourceFrom'] = self.data_source_from
        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id
        if self.data_source_name is not None:
            result['DataSourceName'] = self.data_source_name
        if self.data_source_recognize_enabled is not None:
            result['DataSourceRecognizeEnabled'] = self.data_source_recognize_enabled
        if self.data_source_recognizer is not None:
            result['DataSourceRecognizer'] = self.data_source_recognizer
        result['DataSourceReferences'] = []
        if self.data_source_references is not None:
            for k in self.data_source_references:
                result['DataSourceReferences'].append(k.to_map() if k else None)
        if self.data_source_status is not None:
            result['DataSourceStatus'] = self.data_source_status
        result['DataSourceStores'] = []
        if self.data_source_stores is not None:
            for k in self.data_source_stores:
                result['DataSourceStores'].append(k.to_map() if k else None)
        if self.data_source_template_id is not None:
            result['DataSourceTemplateId'] = self.data_source_template_id
        if self.data_source_type is not None:
            result['DataSourceType'] = self.data_source_type
        if self.log_project_name is not None:
            result['LogProjectName'] = self.log_project_name
        if self.log_region_id is not None:
            result['LogRegionId'] = self.log_region_id
        if self.log_store_name is not None:
            result['LogStoreName'] = self.log_store_name
        if self.log_user_id is not None:
            result['LogUserId'] = self.log_user_id
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DataSourceFrom') is not None:
            self.data_source_from = m.get('DataSourceFrom')
        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')
        if m.get('DataSourceName') is not None:
            self.data_source_name = m.get('DataSourceName')
        if m.get('DataSourceRecognizeEnabled') is not None:
            self.data_source_recognize_enabled = m.get('DataSourceRecognizeEnabled')
        if m.get('DataSourceRecognizer') is not None:
            self.data_source_recognizer = m.get('DataSourceRecognizer')
        self.data_source_references = []
        if m.get('DataSourceReferences') is not None:
            for k in m.get('DataSourceReferences'):
                temp_model = ListDataSourcesResponseBodyDataSourcesDataSourceReferences()
                self.data_source_references.append(temp_model.from_map(k))
        if m.get('DataSourceStatus') is not None:
            self.data_source_status = m.get('DataSourceStatus')
        self.data_source_stores = []
        if m.get('DataSourceStores') is not None:
            for k in m.get('DataSourceStores'):
                temp_model = ListDataSourcesResponseBodyDataSourcesDataSourceStores()
                self.data_source_stores.append(temp_model.from_map(k))
        if m.get('DataSourceTemplateId') is not None:
            self.data_source_template_id = m.get('DataSourceTemplateId')
        if m.get('DataSourceType') is not None:
            self.data_source_type = m.get('DataSourceType')
        if m.get('LogProjectName') is not None:
            self.log_project_name = m.get('LogProjectName')
        if m.get('LogRegionId') is not None:
            self.log_region_id = m.get('LogRegionId')
        if m.get('LogStoreName') is not None:
            self.log_store_name = m.get('LogStoreName')
        if m.get('LogUserId') is not None:
            self.log_user_id = m.get('LogUserId')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class ListDataSourcesResponseBody(TeaModel):
    def __init__(
        self,
        data_sources: List[ListDataSourcesResponseBodyDataSources] = None,
        max_results: int = None,
        next_token: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
        total_page: int = None,
    ):
        self.data_sources = data_sources
        self.max_results = max_results
        self.next_token = next_token
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count
        self.total_page = total_page

    def validate(self):
        if self.data_sources:
            for k in self.data_sources:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataSources'] = []
        if self.data_sources is not None:
            for k in self.data_sources:
                result['DataSources'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.total_page is not None:
            result['TotalPage'] = self.total_page
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_sources = []
        if m.get('DataSources') is not None:
            for k in m.get('DataSources'):
                temp_model = ListDataSourcesResponseBodyDataSources()
                self.data_sources.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')
        return self


class ListDataSourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDataSourcesResponseBody = None,
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
            temp_model = ListDataSourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDetectionRulesRequest(TeaModel):
    def __init__(
        self,
        alert_att_ck: str = None,
        alert_level: str = None,
        alert_tactic_id: str = None,
        alert_type: str = None,
        detection_expression_type: str = None,
        detection_rule_id: str = None,
        detection_rule_ids: List[str] = None,
        detection_rule_name: str = None,
        detection_rule_status: str = None,
        detection_rule_type: str = None,
        incident_aggregation_type: str = None,
        lang: str = None,
        log_category_id: str = None,
        log_schema_id: str = None,
        max_results: int = None,
        next_token: str = None,
        order_direction: str = None,
        order_field_name: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        role_for: int = None,
    ):
        self.alert_att_ck = alert_att_ck
        self.alert_level = alert_level
        self.alert_tactic_id = alert_tactic_id
        self.alert_type = alert_type
        self.detection_expression_type = detection_expression_type
        self.detection_rule_id = detection_rule_id
        self.detection_rule_ids = detection_rule_ids
        self.detection_rule_name = detection_rule_name
        self.detection_rule_status = detection_rule_status
        self.detection_rule_type = detection_rule_type
        self.incident_aggregation_type = incident_aggregation_type
        self.lang = lang
        self.log_category_id = log_category_id
        self.log_schema_id = log_schema_id
        self.max_results = max_results
        self.next_token = next_token
        self.order_direction = order_direction
        self.order_field_name = order_field_name
        self.page_number = page_number
        self.page_size = page_size
        self.region_id = region_id
        self.role_for = role_for

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_att_ck is not None:
            result['AlertAttCk'] = self.alert_att_ck
        if self.alert_level is not None:
            result['AlertLevel'] = self.alert_level
        if self.alert_tactic_id is not None:
            result['AlertTacticId'] = self.alert_tactic_id
        if self.alert_type is not None:
            result['AlertType'] = self.alert_type
        if self.detection_expression_type is not None:
            result['DetectionExpressionType'] = self.detection_expression_type
        if self.detection_rule_id is not None:
            result['DetectionRuleId'] = self.detection_rule_id
        if self.detection_rule_ids is not None:
            result['DetectionRuleIds'] = self.detection_rule_ids
        if self.detection_rule_name is not None:
            result['DetectionRuleName'] = self.detection_rule_name
        if self.detection_rule_status is not None:
            result['DetectionRuleStatus'] = self.detection_rule_status
        if self.detection_rule_type is not None:
            result['DetectionRuleType'] = self.detection_rule_type
        if self.incident_aggregation_type is not None:
            result['IncidentAggregationType'] = self.incident_aggregation_type
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.log_category_id is not None:
            result['LogCategoryId'] = self.log_category_id
        if self.log_schema_id is not None:
            result['LogSchemaId'] = self.log_schema_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.order_direction is not None:
            result['OrderDirection'] = self.order_direction
        if self.order_field_name is not None:
            result['OrderFieldName'] = self.order_field_name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.role_for is not None:
            result['RoleFor'] = self.role_for
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertAttCk') is not None:
            self.alert_att_ck = m.get('AlertAttCk')
        if m.get('AlertLevel') is not None:
            self.alert_level = m.get('AlertLevel')
        if m.get('AlertTacticId') is not None:
            self.alert_tactic_id = m.get('AlertTacticId')
        if m.get('AlertType') is not None:
            self.alert_type = m.get('AlertType')
        if m.get('DetectionExpressionType') is not None:
            self.detection_expression_type = m.get('DetectionExpressionType')
        if m.get('DetectionRuleId') is not None:
            self.detection_rule_id = m.get('DetectionRuleId')
        if m.get('DetectionRuleIds') is not None:
            self.detection_rule_ids = m.get('DetectionRuleIds')
        if m.get('DetectionRuleName') is not None:
            self.detection_rule_name = m.get('DetectionRuleName')
        if m.get('DetectionRuleStatus') is not None:
            self.detection_rule_status = m.get('DetectionRuleStatus')
        if m.get('DetectionRuleType') is not None:
            self.detection_rule_type = m.get('DetectionRuleType')
        if m.get('IncidentAggregationType') is not None:
            self.incident_aggregation_type = m.get('IncidentAggregationType')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('LogCategoryId') is not None:
            self.log_category_id = m.get('LogCategoryId')
        if m.get('LogSchemaId') is not None:
            self.log_schema_id = m.get('LogSchemaId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OrderDirection') is not None:
            self.order_direction = m.get('OrderDirection')
        if m.get('OrderFieldName') is not None:
            self.order_field_name = m.get('OrderFieldName')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')
        return self


class ListDetectionRulesShrinkRequest(TeaModel):
    def __init__(
        self,
        alert_att_ck: str = None,
        alert_level: str = None,
        alert_tactic_id: str = None,
        alert_type: str = None,
        detection_expression_type: str = None,
        detection_rule_id: str = None,
        detection_rule_ids_shrink: str = None,
        detection_rule_name: str = None,
        detection_rule_status: str = None,
        detection_rule_type: str = None,
        incident_aggregation_type: str = None,
        lang: str = None,
        log_category_id: str = None,
        log_schema_id: str = None,
        max_results: int = None,
        next_token: str = None,
        order_direction: str = None,
        order_field_name: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        role_for: int = None,
    ):
        self.alert_att_ck = alert_att_ck
        self.alert_level = alert_level
        self.alert_tactic_id = alert_tactic_id
        self.alert_type = alert_type
        self.detection_expression_type = detection_expression_type
        self.detection_rule_id = detection_rule_id
        self.detection_rule_ids_shrink = detection_rule_ids_shrink
        self.detection_rule_name = detection_rule_name
        self.detection_rule_status = detection_rule_status
        self.detection_rule_type = detection_rule_type
        self.incident_aggregation_type = incident_aggregation_type
        self.lang = lang
        self.log_category_id = log_category_id
        self.log_schema_id = log_schema_id
        self.max_results = max_results
        self.next_token = next_token
        self.order_direction = order_direction
        self.order_field_name = order_field_name
        self.page_number = page_number
        self.page_size = page_size
        self.region_id = region_id
        self.role_for = role_for

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_att_ck is not None:
            result['AlertAttCk'] = self.alert_att_ck
        if self.alert_level is not None:
            result['AlertLevel'] = self.alert_level
        if self.alert_tactic_id is not None:
            result['AlertTacticId'] = self.alert_tactic_id
        if self.alert_type is not None:
            result['AlertType'] = self.alert_type
        if self.detection_expression_type is not None:
            result['DetectionExpressionType'] = self.detection_expression_type
        if self.detection_rule_id is not None:
            result['DetectionRuleId'] = self.detection_rule_id
        if self.detection_rule_ids_shrink is not None:
            result['DetectionRuleIds'] = self.detection_rule_ids_shrink
        if self.detection_rule_name is not None:
            result['DetectionRuleName'] = self.detection_rule_name
        if self.detection_rule_status is not None:
            result['DetectionRuleStatus'] = self.detection_rule_status
        if self.detection_rule_type is not None:
            result['DetectionRuleType'] = self.detection_rule_type
        if self.incident_aggregation_type is not None:
            result['IncidentAggregationType'] = self.incident_aggregation_type
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.log_category_id is not None:
            result['LogCategoryId'] = self.log_category_id
        if self.log_schema_id is not None:
            result['LogSchemaId'] = self.log_schema_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.order_direction is not None:
            result['OrderDirection'] = self.order_direction
        if self.order_field_name is not None:
            result['OrderFieldName'] = self.order_field_name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.role_for is not None:
            result['RoleFor'] = self.role_for
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertAttCk') is not None:
            self.alert_att_ck = m.get('AlertAttCk')
        if m.get('AlertLevel') is not None:
            self.alert_level = m.get('AlertLevel')
        if m.get('AlertTacticId') is not None:
            self.alert_tactic_id = m.get('AlertTacticId')
        if m.get('AlertType') is not None:
            self.alert_type = m.get('AlertType')
        if m.get('DetectionExpressionType') is not None:
            self.detection_expression_type = m.get('DetectionExpressionType')
        if m.get('DetectionRuleId') is not None:
            self.detection_rule_id = m.get('DetectionRuleId')
        if m.get('DetectionRuleIds') is not None:
            self.detection_rule_ids_shrink = m.get('DetectionRuleIds')
        if m.get('DetectionRuleName') is not None:
            self.detection_rule_name = m.get('DetectionRuleName')
        if m.get('DetectionRuleStatus') is not None:
            self.detection_rule_status = m.get('DetectionRuleStatus')
        if m.get('DetectionRuleType') is not None:
            self.detection_rule_type = m.get('DetectionRuleType')
        if m.get('IncidentAggregationType') is not None:
            self.incident_aggregation_type = m.get('IncidentAggregationType')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('LogCategoryId') is not None:
            self.log_category_id = m.get('LogCategoryId')
        if m.get('LogSchemaId') is not None:
            self.log_schema_id = m.get('LogSchemaId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OrderDirection') is not None:
            self.order_direction = m.get('OrderDirection')
        if m.get('OrderFieldName') is not None:
            self.order_field_name = m.get('OrderFieldName')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')
        return self


class ListDetectionRulesResponseBodyDetectionRulesEntityMappingsNormalizationFieldMappings(TeaModel):
    def __init__(
        self,
        mapping_field_name: str = None,
        normalization_field_name: str = None,
        normalization_field_type: str = None,
    ):
        self.mapping_field_name = mapping_field_name
        self.normalization_field_name = normalization_field_name
        self.normalization_field_type = normalization_field_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mapping_field_name is not None:
            result['MappingFieldName'] = self.mapping_field_name
        if self.normalization_field_name is not None:
            result['NormalizationFieldName'] = self.normalization_field_name
        if self.normalization_field_type is not None:
            result['NormalizationFieldType'] = self.normalization_field_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MappingFieldName') is not None:
            self.mapping_field_name = m.get('MappingFieldName')
        if m.get('NormalizationFieldName') is not None:
            self.normalization_field_name = m.get('NormalizationFieldName')
        if m.get('NormalizationFieldType') is not None:
            self.normalization_field_type = m.get('NormalizationFieldType')
        return self


class ListDetectionRulesResponseBodyDetectionRulesEntityMappings(TeaModel):
    def __init__(
        self,
        normalization_field_mappings: List[ListDetectionRulesResponseBodyDetectionRulesEntityMappingsNormalizationFieldMappings] = None,
        normalization_schema_id: str = None,
    ):
        self.normalization_field_mappings = normalization_field_mappings
        self.normalization_schema_id = normalization_schema_id

    def validate(self):
        if self.normalization_field_mappings:
            for k in self.normalization_field_mappings:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['NormalizationFieldMappings'] = []
        if self.normalization_field_mappings is not None:
            for k in self.normalization_field_mappings:
                result['NormalizationFieldMappings'].append(k.to_map() if k else None)
        if self.normalization_schema_id is not None:
            result['NormalizationSchemaId'] = self.normalization_schema_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.normalization_field_mappings = []
        if m.get('NormalizationFieldMappings') is not None:
            for k in m.get('NormalizationFieldMappings'):
                temp_model = ListDetectionRulesResponseBodyDetectionRulesEntityMappingsNormalizationFieldMappings()
                self.normalization_field_mappings.append(temp_model.from_map(k))
        if m.get('NormalizationSchemaId') is not None:
            self.normalization_schema_id = m.get('NormalizationSchemaId')
        return self


class ListDetectionRulesResponseBodyDetectionRulesPlaybook(TeaModel):
    def __init__(
        self,
        config: str = None,
        flow: str = None,
    ):
        self.config = config
        self.flow = flow

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['Config'] = self.config
        if self.flow is not None:
            result['Flow'] = self.flow
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('Flow') is not None:
            self.flow = m.get('Flow')
        return self


class ListDetectionRulesResponseBodyDetectionRules(TeaModel):
    def __init__(
        self,
        alert_att_ck: str = None,
        alert_level: str = None,
        alert_schema_id: str = None,
        alert_tactic_id: str = None,
        alert_threshold_count: int = None,
        alert_threshold_group: str = None,
        alert_threshold_period: str = None,
        alert_type: str = None,
        create_time: int = None,
        detection_expression_content: str = None,
        detection_expression_type: str = None,
        detection_rule_description: str = None,
        detection_rule_id: str = None,
        detection_rule_name: str = None,
        detection_rule_status: str = None,
        detection_rule_type: str = None,
        entity_mappings: List[ListDetectionRulesResponseBodyDetectionRulesEntityMappings] = None,
        incident_aggregation_expression: str = None,
        incident_aggregation_type: str = None,
        log_category_id: str = None,
        log_schema_id: str = None,
        playbook: ListDetectionRulesResponseBodyDetectionRulesPlaybook = None,
        playbook_parameters: str = None,
        playbook_uuid: str = None,
        schedule_begin_time: int = None,
        schedule_expression: str = None,
        schedule_max_retries: int = None,
        schedule_max_timeout: int = None,
        schedule_type: str = None,
        schedule_window: str = None,
        update_time: int = None,
    ):
        self.alert_att_ck = alert_att_ck
        self.alert_level = alert_level
        self.alert_schema_id = alert_schema_id
        self.alert_tactic_id = alert_tactic_id
        self.alert_threshold_count = alert_threshold_count
        self.alert_threshold_group = alert_threshold_group
        self.alert_threshold_period = alert_threshold_period
        self.alert_type = alert_type
        self.create_time = create_time
        self.detection_expression_content = detection_expression_content
        self.detection_expression_type = detection_expression_type
        self.detection_rule_description = detection_rule_description
        self.detection_rule_id = detection_rule_id
        self.detection_rule_name = detection_rule_name
        self.detection_rule_status = detection_rule_status
        self.detection_rule_type = detection_rule_type
        self.entity_mappings = entity_mappings
        self.incident_aggregation_expression = incident_aggregation_expression
        self.incident_aggregation_type = incident_aggregation_type
        self.log_category_id = log_category_id
        self.log_schema_id = log_schema_id
        self.playbook = playbook
        self.playbook_parameters = playbook_parameters
        self.playbook_uuid = playbook_uuid
        self.schedule_begin_time = schedule_begin_time
        self.schedule_expression = schedule_expression
        self.schedule_max_retries = schedule_max_retries
        self.schedule_max_timeout = schedule_max_timeout
        self.schedule_type = schedule_type
        self.schedule_window = schedule_window
        self.update_time = update_time

    def validate(self):
        if self.entity_mappings:
            for k in self.entity_mappings:
                if k:
                    k.validate()
        if self.playbook:
            self.playbook.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_att_ck is not None:
            result['AlertAttCk'] = self.alert_att_ck
        if self.alert_level is not None:
            result['AlertLevel'] = self.alert_level
        if self.alert_schema_id is not None:
            result['AlertSchemaId'] = self.alert_schema_id
        if self.alert_tactic_id is not None:
            result['AlertTacticId'] = self.alert_tactic_id
        if self.alert_threshold_count is not None:
            result['AlertThresholdCount'] = self.alert_threshold_count
        if self.alert_threshold_group is not None:
            result['AlertThresholdGroup'] = self.alert_threshold_group
        if self.alert_threshold_period is not None:
            result['AlertThresholdPeriod'] = self.alert_threshold_period
        if self.alert_type is not None:
            result['AlertType'] = self.alert_type
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.detection_expression_content is not None:
            result['DetectionExpressionContent'] = self.detection_expression_content
        if self.detection_expression_type is not None:
            result['DetectionExpressionType'] = self.detection_expression_type
        if self.detection_rule_description is not None:
            result['DetectionRuleDescription'] = self.detection_rule_description
        if self.detection_rule_id is not None:
            result['DetectionRuleId'] = self.detection_rule_id
        if self.detection_rule_name is not None:
            result['DetectionRuleName'] = self.detection_rule_name
        if self.detection_rule_status is not None:
            result['DetectionRuleStatus'] = self.detection_rule_status
        if self.detection_rule_type is not None:
            result['DetectionRuleType'] = self.detection_rule_type
        result['EntityMappings'] = []
        if self.entity_mappings is not None:
            for k in self.entity_mappings:
                result['EntityMappings'].append(k.to_map() if k else None)
        if self.incident_aggregation_expression is not None:
            result['IncidentAggregationExpression'] = self.incident_aggregation_expression
        if self.incident_aggregation_type is not None:
            result['IncidentAggregationType'] = self.incident_aggregation_type
        if self.log_category_id is not None:
            result['LogCategoryId'] = self.log_category_id
        if self.log_schema_id is not None:
            result['LogSchemaId'] = self.log_schema_id
        if self.playbook is not None:
            result['Playbook'] = self.playbook.to_map()
        if self.playbook_parameters is not None:
            result['PlaybookParameters'] = self.playbook_parameters
        if self.playbook_uuid is not None:
            result['PlaybookUuid'] = self.playbook_uuid
        if self.schedule_begin_time is not None:
            result['ScheduleBeginTime'] = self.schedule_begin_time
        if self.schedule_expression is not None:
            result['ScheduleExpression'] = self.schedule_expression
        if self.schedule_max_retries is not None:
            result['ScheduleMaxRetries'] = self.schedule_max_retries
        if self.schedule_max_timeout is not None:
            result['ScheduleMaxTimeout'] = self.schedule_max_timeout
        if self.schedule_type is not None:
            result['ScheduleType'] = self.schedule_type
        if self.schedule_window is not None:
            result['ScheduleWindow'] = self.schedule_window
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertAttCk') is not None:
            self.alert_att_ck = m.get('AlertAttCk')
        if m.get('AlertLevel') is not None:
            self.alert_level = m.get('AlertLevel')
        if m.get('AlertSchemaId') is not None:
            self.alert_schema_id = m.get('AlertSchemaId')
        if m.get('AlertTacticId') is not None:
            self.alert_tactic_id = m.get('AlertTacticId')
        if m.get('AlertThresholdCount') is not None:
            self.alert_threshold_count = m.get('AlertThresholdCount')
        if m.get('AlertThresholdGroup') is not None:
            self.alert_threshold_group = m.get('AlertThresholdGroup')
        if m.get('AlertThresholdPeriod') is not None:
            self.alert_threshold_period = m.get('AlertThresholdPeriod')
        if m.get('AlertType') is not None:
            self.alert_type = m.get('AlertType')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DetectionExpressionContent') is not None:
            self.detection_expression_content = m.get('DetectionExpressionContent')
        if m.get('DetectionExpressionType') is not None:
            self.detection_expression_type = m.get('DetectionExpressionType')
        if m.get('DetectionRuleDescription') is not None:
            self.detection_rule_description = m.get('DetectionRuleDescription')
        if m.get('DetectionRuleId') is not None:
            self.detection_rule_id = m.get('DetectionRuleId')
        if m.get('DetectionRuleName') is not None:
            self.detection_rule_name = m.get('DetectionRuleName')
        if m.get('DetectionRuleStatus') is not None:
            self.detection_rule_status = m.get('DetectionRuleStatus')
        if m.get('DetectionRuleType') is not None:
            self.detection_rule_type = m.get('DetectionRuleType')
        self.entity_mappings = []
        if m.get('EntityMappings') is not None:
            for k in m.get('EntityMappings'):
                temp_model = ListDetectionRulesResponseBodyDetectionRulesEntityMappings()
                self.entity_mappings.append(temp_model.from_map(k))
        if m.get('IncidentAggregationExpression') is not None:
            self.incident_aggregation_expression = m.get('IncidentAggregationExpression')
        if m.get('IncidentAggregationType') is not None:
            self.incident_aggregation_type = m.get('IncidentAggregationType')
        if m.get('LogCategoryId') is not None:
            self.log_category_id = m.get('LogCategoryId')
        if m.get('LogSchemaId') is not None:
            self.log_schema_id = m.get('LogSchemaId')
        if m.get('Playbook') is not None:
            temp_model = ListDetectionRulesResponseBodyDetectionRulesPlaybook()
            self.playbook = temp_model.from_map(m['Playbook'])
        if m.get('PlaybookParameters') is not None:
            self.playbook_parameters = m.get('PlaybookParameters')
        if m.get('PlaybookUuid') is not None:
            self.playbook_uuid = m.get('PlaybookUuid')
        if m.get('ScheduleBeginTime') is not None:
            self.schedule_begin_time = m.get('ScheduleBeginTime')
        if m.get('ScheduleExpression') is not None:
            self.schedule_expression = m.get('ScheduleExpression')
        if m.get('ScheduleMaxRetries') is not None:
            self.schedule_max_retries = m.get('ScheduleMaxRetries')
        if m.get('ScheduleMaxTimeout') is not None:
            self.schedule_max_timeout = m.get('ScheduleMaxTimeout')
        if m.get('ScheduleType') is not None:
            self.schedule_type = m.get('ScheduleType')
        if m.get('ScheduleWindow') is not None:
            self.schedule_window = m.get('ScheduleWindow')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class ListDetectionRulesResponseBody(TeaModel):
    def __init__(
        self,
        detection_rules: List[ListDetectionRulesResponseBodyDetectionRules] = None,
        max_results: int = None,
        next_token: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.detection_rules = detection_rules
        self.max_results = max_results
        self.next_token = next_token
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.detection_rules:
            for k in self.detection_rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DetectionRules'] = []
        if self.detection_rules is not None:
            for k in self.detection_rules:
                result['DetectionRules'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.detection_rules = []
        if m.get('DetectionRules') is not None:
            for k in m.get('DetectionRules'):
                temp_model = ListDetectionRulesResponseBodyDetectionRules()
                self.detection_rules.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListDetectionRulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDetectionRulesResponseBody = None,
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
            temp_model = ListDetectionRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListIncidentsRequest(TeaModel):
    def __init__(
        self,
        alert_uuid: str = None,
        end_time: int = None,
        incident_name: str = None,
        incident_status: int = None,
        incident_tags: str = None,
        incident_uuids: List[str] = None,
        lang: str = None,
        max_results: int = None,
        next_token: str = None,
        order_direction: str = None,
        order_field_name: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        relate_asset_id: str = None,
        relate_entity_id: str = None,
        role_for: int = None,
        role_type: int = None,
        start_time: int = None,
        threat_level: List[str] = None,
    ):
        self.alert_uuid = alert_uuid
        self.end_time = end_time
        self.incident_name = incident_name
        self.incident_status = incident_status
        self.incident_tags = incident_tags
        self.incident_uuids = incident_uuids
        self.lang = lang
        self.max_results = max_results
        self.next_token = next_token
        self.order_direction = order_direction
        self.order_field_name = order_field_name
        # This parameter is required.
        self.page_number = page_number
        # This parameter is required.
        self.page_size = page_size
        self.region_id = region_id
        self.relate_asset_id = relate_asset_id
        self.relate_entity_id = relate_entity_id
        self.role_for = role_for
        self.role_type = role_type
        self.start_time = start_time
        self.threat_level = threat_level

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_uuid is not None:
            result['AlertUuid'] = self.alert_uuid
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.incident_name is not None:
            result['IncidentName'] = self.incident_name
        if self.incident_status is not None:
            result['IncidentStatus'] = self.incident_status
        if self.incident_tags is not None:
            result['IncidentTags'] = self.incident_tags
        if self.incident_uuids is not None:
            result['IncidentUuids'] = self.incident_uuids
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.order_direction is not None:
            result['OrderDirection'] = self.order_direction
        if self.order_field_name is not None:
            result['OrderFieldName'] = self.order_field_name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.relate_asset_id is not None:
            result['RelateAssetId'] = self.relate_asset_id
        if self.relate_entity_id is not None:
            result['RelateEntityId'] = self.relate_entity_id
        if self.role_for is not None:
            result['RoleFor'] = self.role_for
        if self.role_type is not None:
            result['RoleType'] = self.role_type
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.threat_level is not None:
            result['ThreatLevel'] = self.threat_level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertUuid') is not None:
            self.alert_uuid = m.get('AlertUuid')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('IncidentName') is not None:
            self.incident_name = m.get('IncidentName')
        if m.get('IncidentStatus') is not None:
            self.incident_status = m.get('IncidentStatus')
        if m.get('IncidentTags') is not None:
            self.incident_tags = m.get('IncidentTags')
        if m.get('IncidentUuids') is not None:
            self.incident_uuids = m.get('IncidentUuids')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OrderDirection') is not None:
            self.order_direction = m.get('OrderDirection')
        if m.get('OrderFieldName') is not None:
            self.order_field_name = m.get('OrderFieldName')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RelateAssetId') is not None:
            self.relate_asset_id = m.get('RelateAssetId')
        if m.get('RelateEntityId') is not None:
            self.relate_entity_id = m.get('RelateEntityId')
        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')
        if m.get('RoleType') is not None:
            self.role_type = m.get('RoleType')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('ThreatLevel') is not None:
            self.threat_level = m.get('ThreatLevel')
        return self


class ListIncidentsShrinkRequest(TeaModel):
    def __init__(
        self,
        alert_uuid: str = None,
        end_time: int = None,
        incident_name: str = None,
        incident_status: int = None,
        incident_tags: str = None,
        incident_uuids_shrink: str = None,
        lang: str = None,
        max_results: int = None,
        next_token: str = None,
        order_direction: str = None,
        order_field_name: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        relate_asset_id: str = None,
        relate_entity_id: str = None,
        role_for: int = None,
        role_type: int = None,
        start_time: int = None,
        threat_level: List[str] = None,
    ):
        self.alert_uuid = alert_uuid
        self.end_time = end_time
        self.incident_name = incident_name
        self.incident_status = incident_status
        self.incident_tags = incident_tags
        self.incident_uuids_shrink = incident_uuids_shrink
        self.lang = lang
        self.max_results = max_results
        self.next_token = next_token
        self.order_direction = order_direction
        self.order_field_name = order_field_name
        # This parameter is required.
        self.page_number = page_number
        # This parameter is required.
        self.page_size = page_size
        self.region_id = region_id
        self.relate_asset_id = relate_asset_id
        self.relate_entity_id = relate_entity_id
        self.role_for = role_for
        self.role_type = role_type
        self.start_time = start_time
        self.threat_level = threat_level

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_uuid is not None:
            result['AlertUuid'] = self.alert_uuid
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.incident_name is not None:
            result['IncidentName'] = self.incident_name
        if self.incident_status is not None:
            result['IncidentStatus'] = self.incident_status
        if self.incident_tags is not None:
            result['IncidentTags'] = self.incident_tags
        if self.incident_uuids_shrink is not None:
            result['IncidentUuids'] = self.incident_uuids_shrink
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.order_direction is not None:
            result['OrderDirection'] = self.order_direction
        if self.order_field_name is not None:
            result['OrderFieldName'] = self.order_field_name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.relate_asset_id is not None:
            result['RelateAssetId'] = self.relate_asset_id
        if self.relate_entity_id is not None:
            result['RelateEntityId'] = self.relate_entity_id
        if self.role_for is not None:
            result['RoleFor'] = self.role_for
        if self.role_type is not None:
            result['RoleType'] = self.role_type
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.threat_level is not None:
            result['ThreatLevel'] = self.threat_level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertUuid') is not None:
            self.alert_uuid = m.get('AlertUuid')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('IncidentName') is not None:
            self.incident_name = m.get('IncidentName')
        if m.get('IncidentStatus') is not None:
            self.incident_status = m.get('IncidentStatus')
        if m.get('IncidentTags') is not None:
            self.incident_tags = m.get('IncidentTags')
        if m.get('IncidentUuids') is not None:
            self.incident_uuids_shrink = m.get('IncidentUuids')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OrderDirection') is not None:
            self.order_direction = m.get('OrderDirection')
        if m.get('OrderFieldName') is not None:
            self.order_field_name = m.get('OrderFieldName')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RelateAssetId') is not None:
            self.relate_asset_id = m.get('RelateAssetId')
        if m.get('RelateEntityId') is not None:
            self.relate_entity_id = m.get('RelateEntityId')
        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')
        if m.get('RoleType') is not None:
            self.role_type = m.get('RoleType')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('ThreatLevel') is not None:
            self.threat_level = m.get('ThreatLevel')
        return self


class ListIncidentsResponseBodyIncidents(TeaModel):
    def __init__(
        self,
        create_time: int = None,
        incident_name: str = None,
        incident_remark: str = None,
        incident_status: int = None,
        incident_uuid: str = None,
        relate_alert_count: int = None,
        relate_asset_count: int = None,
        threat_level: str = None,
        update_time: int = None,
    ):
        self.create_time = create_time
        self.incident_name = incident_name
        self.incident_remark = incident_remark
        self.incident_status = incident_status
        self.incident_uuid = incident_uuid
        self.relate_alert_count = relate_alert_count
        self.relate_asset_count = relate_asset_count
        self.threat_level = threat_level
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.incident_name is not None:
            result['IncidentName'] = self.incident_name
        if self.incident_remark is not None:
            result['IncidentRemark'] = self.incident_remark
        if self.incident_status is not None:
            result['IncidentStatus'] = self.incident_status
        if self.incident_uuid is not None:
            result['IncidentUuid'] = self.incident_uuid
        if self.relate_alert_count is not None:
            result['RelateAlertCount'] = self.relate_alert_count
        if self.relate_asset_count is not None:
            result['RelateAssetCount'] = self.relate_asset_count
        if self.threat_level is not None:
            result['ThreatLevel'] = self.threat_level
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('IncidentName') is not None:
            self.incident_name = m.get('IncidentName')
        if m.get('IncidentRemark') is not None:
            self.incident_remark = m.get('IncidentRemark')
        if m.get('IncidentStatus') is not None:
            self.incident_status = m.get('IncidentStatus')
        if m.get('IncidentUuid') is not None:
            self.incident_uuid = m.get('IncidentUuid')
        if m.get('RelateAlertCount') is not None:
            self.relate_alert_count = m.get('RelateAlertCount')
        if m.get('RelateAssetCount') is not None:
            self.relate_asset_count = m.get('RelateAssetCount')
        if m.get('ThreatLevel') is not None:
            self.threat_level = m.get('ThreatLevel')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class ListIncidentsResponseBody(TeaModel):
    def __init__(
        self,
        incidents: List[ListIncidentsResponseBodyIncidents] = None,
        max_results: int = None,
        next_token: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.incidents = incidents
        self.max_results = max_results
        self.next_token = next_token
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.incidents:
            for k in self.incidents:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Incidents'] = []
        if self.incidents is not None:
            for k in self.incidents:
                result['Incidents'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.incidents = []
        if m.get('Incidents') is not None:
            for k in m.get('Incidents'):
                temp_model = ListIncidentsResponseBodyIncidents()
                self.incidents.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListIncidentsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListIncidentsResponseBody = None,
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
            temp_model = ListIncidentsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListLogProjectsRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        log_region_id: str = None,
        log_user_id: int = None,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
        role_for: int = None,
    ):
        self.lang = lang
        self.log_region_id = log_region_id
        self.log_user_id = log_user_id
        self.max_results = max_results
        self.next_token = next_token
        self.region_id = region_id
        self.role_for = role_for

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.log_region_id is not None:
            result['LogRegionId'] = self.log_region_id
        if self.log_user_id is not None:
            result['LogUserId'] = self.log_user_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.role_for is not None:
            result['RoleFor'] = self.role_for
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('LogRegionId') is not None:
            self.log_region_id = m.get('LogRegionId')
        if m.get('LogUserId') is not None:
            self.log_user_id = m.get('LogUserId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')
        return self


class ListLogProjectsResponseBody(TeaModel):
    def __init__(
        self,
        log_projects: List[str] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.log_projects = log_projects
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.log_projects is not None:
            result['LogProjects'] = self.log_projects
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LogProjects') is not None:
            self.log_projects = m.get('LogProjects')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListLogProjectsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListLogProjectsResponseBody = None,
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
            temp_model = ListLogProjectsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListLogRegionsRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        role_for: int = None,
    ):
        self.lang = lang
        self.role_for = role_for

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.role_for is not None:
            result['RoleFor'] = self.role_for
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')
        return self


class ListLogRegionsResponseBody(TeaModel):
    def __init__(
        self,
        log_regions: List[str] = None,
        request_id: str = None,
    ):
        self.log_regions = log_regions
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.log_regions is not None:
            result['LogRegions'] = self.log_regions
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LogRegions') is not None:
            self.log_regions = m.get('LogRegions')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListLogRegionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListLogRegionsResponseBody = None,
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
            temp_model = ListLogRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListLogStoresRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        log_project_name: str = None,
        log_region_id: str = None,
        log_user_id: int = None,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
        role_for: int = None,
    ):
        self.lang = lang
        self.log_project_name = log_project_name
        self.log_region_id = log_region_id
        self.log_user_id = log_user_id
        self.max_results = max_results
        self.next_token = next_token
        self.region_id = region_id
        self.role_for = role_for

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.log_project_name is not None:
            result['LogProjectName'] = self.log_project_name
        if self.log_region_id is not None:
            result['LogRegionId'] = self.log_region_id
        if self.log_user_id is not None:
            result['LogUserId'] = self.log_user_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.role_for is not None:
            result['RoleFor'] = self.role_for
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('LogProjectName') is not None:
            self.log_project_name = m.get('LogProjectName')
        if m.get('LogRegionId') is not None:
            self.log_region_id = m.get('LogRegionId')
        if m.get('LogUserId') is not None:
            self.log_user_id = m.get('LogUserId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')
        return self


class ListLogStoresResponseBody(TeaModel):
    def __init__(
        self,
        log_stores: List[str] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.log_stores = log_stores
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.log_stores is not None:
            result['LogStores'] = self.log_stores
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LogStores') is not None:
            self.log_stores = m.get('LogStores')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListLogStoresResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListLogStoresResponseBody = None,
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
            temp_model = ListLogStoresResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListNormalizationCategoriesRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        max_results: int = None,
        next_token: str = None,
        normalization_category_type: str = None,
        region_id: str = None,
        role_for: int = None,
    ):
        self.lang = lang
        self.max_results = max_results
        self.next_token = next_token
        self.normalization_category_type = normalization_category_type
        self.region_id = region_id
        self.role_for = role_for

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.normalization_category_type is not None:
            result['NormalizationCategoryType'] = self.normalization_category_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.role_for is not None:
            result['RoleFor'] = self.role_for
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('NormalizationCategoryType') is not None:
            self.normalization_category_type = m.get('NormalizationCategoryType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')
        return self


class ListNormalizationCategoriesResponseBodyNormalizationCategories(TeaModel):
    def __init__(
        self,
        normalization_category_id: str = None,
        normalization_category_name: str = None,
    ):
        self.normalization_category_id = normalization_category_id
        self.normalization_category_name = normalization_category_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.normalization_category_id is not None:
            result['NormalizationCategoryId'] = self.normalization_category_id
        if self.normalization_category_name is not None:
            result['NormalizationCategoryName'] = self.normalization_category_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NormalizationCategoryId') is not None:
            self.normalization_category_id = m.get('NormalizationCategoryId')
        if m.get('NormalizationCategoryName') is not None:
            self.normalization_category_name = m.get('NormalizationCategoryName')
        return self


class ListNormalizationCategoriesResponseBody(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        normalization_categories: List[ListNormalizationCategoriesResponseBodyNormalizationCategories] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.normalization_categories = normalization_categories
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.normalization_categories:
            for k in self.normalization_categories:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        result['NormalizationCategories'] = []
        if self.normalization_categories is not None:
            for k in self.normalization_categories:
                result['NormalizationCategories'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.normalization_categories = []
        if m.get('NormalizationCategories') is not None:
            for k in m.get('NormalizationCategories'):
                temp_model = ListNormalizationCategoriesResponseBodyNormalizationCategories()
                self.normalization_categories.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListNormalizationCategoriesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListNormalizationCategoriesResponseBody = None,
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
            temp_model = ListNormalizationCategoriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListNormalizationFieldsRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        max_results: int = None,
        name: str = None,
        next_token: str = None,
        region_id: str = None,
        role_for: int = None,
    ):
        self.lang = lang
        self.max_results = max_results
        self.name = name
        self.next_token = next_token
        self.region_id = region_id
        self.role_for = role_for

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.name is not None:
            result['Name'] = self.name
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.role_for is not None:
            result['RoleFor'] = self.role_for
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')
        return self


class ListNormalizationFieldsResponseBodyNormalizationFields(TeaModel):
    def __init__(
        self,
        normalization_category_id: str = None,
        normalization_field_description: str = None,
        normalization_field_example: str = None,
        normalization_field_name: str = None,
        normalization_field_requirement: bool = None,
        normalization_field_reserved: bool = None,
        normalization_field_type: str = None,
        normalization_schema_id: str = None,
    ):
        self.normalization_category_id = normalization_category_id
        self.normalization_field_description = normalization_field_description
        self.normalization_field_example = normalization_field_example
        self.normalization_field_name = normalization_field_name
        self.normalization_field_requirement = normalization_field_requirement
        self.normalization_field_reserved = normalization_field_reserved
        self.normalization_field_type = normalization_field_type
        self.normalization_schema_id = normalization_schema_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.normalization_category_id is not None:
            result['NormalizationCategoryId'] = self.normalization_category_id
        if self.normalization_field_description is not None:
            result['NormalizationFieldDescription'] = self.normalization_field_description
        if self.normalization_field_example is not None:
            result['NormalizationFieldExample'] = self.normalization_field_example
        if self.normalization_field_name is not None:
            result['NormalizationFieldName'] = self.normalization_field_name
        if self.normalization_field_requirement is not None:
            result['NormalizationFieldRequirement'] = self.normalization_field_requirement
        if self.normalization_field_reserved is not None:
            result['NormalizationFieldReserved'] = self.normalization_field_reserved
        if self.normalization_field_type is not None:
            result['NormalizationFieldType'] = self.normalization_field_type
        if self.normalization_schema_id is not None:
            result['NormalizationSchemaId'] = self.normalization_schema_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NormalizationCategoryId') is not None:
            self.normalization_category_id = m.get('NormalizationCategoryId')
        if m.get('NormalizationFieldDescription') is not None:
            self.normalization_field_description = m.get('NormalizationFieldDescription')
        if m.get('NormalizationFieldExample') is not None:
            self.normalization_field_example = m.get('NormalizationFieldExample')
        if m.get('NormalizationFieldName') is not None:
            self.normalization_field_name = m.get('NormalizationFieldName')
        if m.get('NormalizationFieldRequirement') is not None:
            self.normalization_field_requirement = m.get('NormalizationFieldRequirement')
        if m.get('NormalizationFieldReserved') is not None:
            self.normalization_field_reserved = m.get('NormalizationFieldReserved')
        if m.get('NormalizationFieldType') is not None:
            self.normalization_field_type = m.get('NormalizationFieldType')
        if m.get('NormalizationSchemaId') is not None:
            self.normalization_schema_id = m.get('NormalizationSchemaId')
        return self


class ListNormalizationFieldsResponseBody(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        normalization_fields: List[ListNormalizationFieldsResponseBodyNormalizationFields] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.normalization_fields = normalization_fields
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.normalization_fields:
            for k in self.normalization_fields:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        result['NormalizationFields'] = []
        if self.normalization_fields is not None:
            for k in self.normalization_fields:
                result['NormalizationFields'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.normalization_fields = []
        if m.get('NormalizationFields') is not None:
            for k in m.get('NormalizationFields'):
                temp_model = ListNormalizationFieldsResponseBodyNormalizationFields()
                self.normalization_fields.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListNormalizationFieldsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListNormalizationFieldsResponseBody = None,
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
            temp_model = ListNormalizationFieldsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListNormalizationRuleCapacitiesRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        max_results: int = None,
        next_token: str = None,
        normalization_rule_id: str = None,
        normalization_rule_ids: List[str] = None,
        region_id: str = None,
        role_for: int = None,
    ):
        self.lang = lang
        self.max_results = max_results
        self.next_token = next_token
        self.normalization_rule_id = normalization_rule_id
        self.normalization_rule_ids = normalization_rule_ids
        self.region_id = region_id
        self.role_for = role_for

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.normalization_rule_id is not None:
            result['NormalizationRuleId'] = self.normalization_rule_id
        if self.normalization_rule_ids is not None:
            result['NormalizationRuleIds'] = self.normalization_rule_ids
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.role_for is not None:
            result['RoleFor'] = self.role_for
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('NormalizationRuleId') is not None:
            self.normalization_rule_id = m.get('NormalizationRuleId')
        if m.get('NormalizationRuleIds') is not None:
            self.normalization_rule_ids = m.get('NormalizationRuleIds')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')
        return self


class ListNormalizationRuleCapacitiesShrinkRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        max_results: int = None,
        next_token: str = None,
        normalization_rule_id: str = None,
        normalization_rule_ids_shrink: str = None,
        region_id: str = None,
        role_for: int = None,
    ):
        self.lang = lang
        self.max_results = max_results
        self.next_token = next_token
        self.normalization_rule_id = normalization_rule_id
        self.normalization_rule_ids_shrink = normalization_rule_ids_shrink
        self.region_id = region_id
        self.role_for = role_for

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.normalization_rule_id is not None:
            result['NormalizationRuleId'] = self.normalization_rule_id
        if self.normalization_rule_ids_shrink is not None:
            result['NormalizationRuleIds'] = self.normalization_rule_ids_shrink
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.role_for is not None:
            result['RoleFor'] = self.role_for
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('NormalizationRuleId') is not None:
            self.normalization_rule_id = m.get('NormalizationRuleId')
        if m.get('NormalizationRuleIds') is not None:
            self.normalization_rule_ids_shrink = m.get('NormalizationRuleIds')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')
        return self


class ListNormalizationRuleCapacitiesResponseBodyNormalizationRuleCapacities(TeaModel):
    def __init__(
        self,
        capacities: List[str] = None,
        capacity_type: str = None,
        normalization_rule_id: str = None,
    ):
        self.capacities = capacities
        self.capacity_type = capacity_type
        self.normalization_rule_id = normalization_rule_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.capacities is not None:
            result['Capacities'] = self.capacities
        if self.capacity_type is not None:
            result['CapacityType'] = self.capacity_type
        if self.normalization_rule_id is not None:
            result['NormalizationRuleId'] = self.normalization_rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Capacities') is not None:
            self.capacities = m.get('Capacities')
        if m.get('CapacityType') is not None:
            self.capacity_type = m.get('CapacityType')
        if m.get('NormalizationRuleId') is not None:
            self.normalization_rule_id = m.get('NormalizationRuleId')
        return self


class ListNormalizationRuleCapacitiesResponseBody(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        normalization_rule_capacities: List[ListNormalizationRuleCapacitiesResponseBodyNormalizationRuleCapacities] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
        total_page: int = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.normalization_rule_capacities = normalization_rule_capacities
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count
        self.total_page = total_page

    def validate(self):
        if self.normalization_rule_capacities:
            for k in self.normalization_rule_capacities:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        result['NormalizationRuleCapacities'] = []
        if self.normalization_rule_capacities is not None:
            for k in self.normalization_rule_capacities:
                result['NormalizationRuleCapacities'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.total_page is not None:
            result['TotalPage'] = self.total_page
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.normalization_rule_capacities = []
        if m.get('NormalizationRuleCapacities') is not None:
            for k in m.get('NormalizationRuleCapacities'):
                temp_model = ListNormalizationRuleCapacitiesResponseBodyNormalizationRuleCapacities()
                self.normalization_rule_capacities.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')
        return self


class ListNormalizationRuleCapacitiesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListNormalizationRuleCapacitiesResponseBody = None,
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
            temp_model = ListNormalizationRuleCapacitiesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListNormalizationRuleVersionsRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        max_results: int = None,
        next_token: str = None,
        normalization_rule_id: str = None,
        region_id: str = None,
        role_for: int = None,
    ):
        self.lang = lang
        self.max_results = max_results
        self.next_token = next_token
        self.normalization_rule_id = normalization_rule_id
        self.region_id = region_id
        self.role_for = role_for

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.normalization_rule_id is not None:
            result['NormalizationRuleId'] = self.normalization_rule_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.role_for is not None:
            result['RoleFor'] = self.role_for
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('NormalizationRuleId') is not None:
            self.normalization_rule_id = m.get('NormalizationRuleId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')
        return self


class ListNormalizationRuleVersionsResponseBodyNormalizationRuleVersions(TeaModel):
    def __init__(
        self,
        create_time: int = None,
        normalization_rule_expression: str = None,
        normalization_rule_id: str = None,
        normalization_rule_version: int = None,
        update_time: int = None,
    ):
        self.create_time = create_time
        self.normalization_rule_expression = normalization_rule_expression
        self.normalization_rule_id = normalization_rule_id
        self.normalization_rule_version = normalization_rule_version
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.normalization_rule_expression is not None:
            result['NormalizationRuleExpression'] = self.normalization_rule_expression
        if self.normalization_rule_id is not None:
            result['NormalizationRuleId'] = self.normalization_rule_id
        if self.normalization_rule_version is not None:
            result['NormalizationRuleVersion'] = self.normalization_rule_version
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('NormalizationRuleExpression') is not None:
            self.normalization_rule_expression = m.get('NormalizationRuleExpression')
        if m.get('NormalizationRuleId') is not None:
            self.normalization_rule_id = m.get('NormalizationRuleId')
        if m.get('NormalizationRuleVersion') is not None:
            self.normalization_rule_version = m.get('NormalizationRuleVersion')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class ListNormalizationRuleVersionsResponseBody(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        normalization_rule_versions: List[ListNormalizationRuleVersionsResponseBodyNormalizationRuleVersions] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.normalization_rule_versions = normalization_rule_versions
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.normalization_rule_versions:
            for k in self.normalization_rule_versions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        result['NormalizationRuleVersions'] = []
        if self.normalization_rule_versions is not None:
            for k in self.normalization_rule_versions:
                result['NormalizationRuleVersions'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.normalization_rule_versions = []
        if m.get('NormalizationRuleVersions') is not None:
            for k in m.get('NormalizationRuleVersions'):
                temp_model = ListNormalizationRuleVersionsResponseBodyNormalizationRuleVersions()
                self.normalization_rule_versions.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListNormalizationRuleVersionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListNormalizationRuleVersionsResponseBody = None,
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
            temp_model = ListNormalizationRuleVersionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListNormalizationRulesRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        max_results: int = None,
        next_token: str = None,
        normalization_category_id: str = None,
        normalization_rule_ids: List[str] = None,
        normalization_rule_name: str = None,
        normalization_rule_type: str = None,
        normalization_schema_id: str = None,
        order_field: str = None,
        order_type: str = None,
        page_number: int = None,
        page_size: int = None,
        product_id: str = None,
        region_id: str = None,
        role_for: int = None,
        vendor_id: str = None,
    ):
        self.lang = lang
        self.max_results = max_results
        self.next_token = next_token
        self.normalization_category_id = normalization_category_id
        self.normalization_rule_ids = normalization_rule_ids
        self.normalization_rule_name = normalization_rule_name
        self.normalization_rule_type = normalization_rule_type
        self.normalization_schema_id = normalization_schema_id
        self.order_field = order_field
        self.order_type = order_type
        self.page_number = page_number
        self.page_size = page_size
        self.product_id = product_id
        self.region_id = region_id
        self.role_for = role_for
        self.vendor_id = vendor_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.normalization_category_id is not None:
            result['NormalizationCategoryId'] = self.normalization_category_id
        if self.normalization_rule_ids is not None:
            result['NormalizationRuleIds'] = self.normalization_rule_ids
        if self.normalization_rule_name is not None:
            result['NormalizationRuleName'] = self.normalization_rule_name
        if self.normalization_rule_type is not None:
            result['NormalizationRuleType'] = self.normalization_rule_type
        if self.normalization_schema_id is not None:
            result['NormalizationSchemaId'] = self.normalization_schema_id
        if self.order_field is not None:
            result['OrderField'] = self.order_field
        if self.order_type is not None:
            result['OrderType'] = self.order_type
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.role_for is not None:
            result['RoleFor'] = self.role_for
        if self.vendor_id is not None:
            result['VendorId'] = self.vendor_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('NormalizationCategoryId') is not None:
            self.normalization_category_id = m.get('NormalizationCategoryId')
        if m.get('NormalizationRuleIds') is not None:
            self.normalization_rule_ids = m.get('NormalizationRuleIds')
        if m.get('NormalizationRuleName') is not None:
            self.normalization_rule_name = m.get('NormalizationRuleName')
        if m.get('NormalizationRuleType') is not None:
            self.normalization_rule_type = m.get('NormalizationRuleType')
        if m.get('NormalizationSchemaId') is not None:
            self.normalization_schema_id = m.get('NormalizationSchemaId')
        if m.get('OrderField') is not None:
            self.order_field = m.get('OrderField')
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')
        if m.get('VendorId') is not None:
            self.vendor_id = m.get('VendorId')
        return self


class ListNormalizationRulesShrinkRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        max_results: int = None,
        next_token: str = None,
        normalization_category_id: str = None,
        normalization_rule_ids_shrink: str = None,
        normalization_rule_name: str = None,
        normalization_rule_type: str = None,
        normalization_schema_id: str = None,
        order_field: str = None,
        order_type: str = None,
        page_number: int = None,
        page_size: int = None,
        product_id: str = None,
        region_id: str = None,
        role_for: int = None,
        vendor_id: str = None,
    ):
        self.lang = lang
        self.max_results = max_results
        self.next_token = next_token
        self.normalization_category_id = normalization_category_id
        self.normalization_rule_ids_shrink = normalization_rule_ids_shrink
        self.normalization_rule_name = normalization_rule_name
        self.normalization_rule_type = normalization_rule_type
        self.normalization_schema_id = normalization_schema_id
        self.order_field = order_field
        self.order_type = order_type
        self.page_number = page_number
        self.page_size = page_size
        self.product_id = product_id
        self.region_id = region_id
        self.role_for = role_for
        self.vendor_id = vendor_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.normalization_category_id is not None:
            result['NormalizationCategoryId'] = self.normalization_category_id
        if self.normalization_rule_ids_shrink is not None:
            result['NormalizationRuleIds'] = self.normalization_rule_ids_shrink
        if self.normalization_rule_name is not None:
            result['NormalizationRuleName'] = self.normalization_rule_name
        if self.normalization_rule_type is not None:
            result['NormalizationRuleType'] = self.normalization_rule_type
        if self.normalization_schema_id is not None:
            result['NormalizationSchemaId'] = self.normalization_schema_id
        if self.order_field is not None:
            result['OrderField'] = self.order_field
        if self.order_type is not None:
            result['OrderType'] = self.order_type
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.role_for is not None:
            result['RoleFor'] = self.role_for
        if self.vendor_id is not None:
            result['VendorId'] = self.vendor_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('NormalizationCategoryId') is not None:
            self.normalization_category_id = m.get('NormalizationCategoryId')
        if m.get('NormalizationRuleIds') is not None:
            self.normalization_rule_ids_shrink = m.get('NormalizationRuleIds')
        if m.get('NormalizationRuleName') is not None:
            self.normalization_rule_name = m.get('NormalizationRuleName')
        if m.get('NormalizationRuleType') is not None:
            self.normalization_rule_type = m.get('NormalizationRuleType')
        if m.get('NormalizationSchemaId') is not None:
            self.normalization_schema_id = m.get('NormalizationSchemaId')
        if m.get('OrderField') is not None:
            self.order_field = m.get('OrderField')
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')
        if m.get('VendorId') is not None:
            self.vendor_id = m.get('VendorId')
        return self


class ListNormalizationRulesResponseBodyNormalizationRulesNormalizationRuleReferences(TeaModel):
    def __init__(
        self,
        data_ingestion_id: str = None,
    ):
        self.data_ingestion_id = data_ingestion_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_ingestion_id is not None:
            result['DataIngestionId'] = self.data_ingestion_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataIngestionId') is not None:
            self.data_ingestion_id = m.get('DataIngestionId')
        return self


class ListNormalizationRulesResponseBodyNormalizationRules(TeaModel):
    def __init__(
        self,
        create_time: int = None,
        extend_content_packed: str = None,
        normalization_category_id: str = None,
        normalization_rule_description: str = None,
        normalization_rule_expression: str = None,
        normalization_rule_format: str = None,
        normalization_rule_id: str = None,
        normalization_rule_mode: str = None,
        normalization_rule_name: str = None,
        normalization_rule_references: List[ListNormalizationRulesResponseBodyNormalizationRulesNormalizationRuleReferences] = None,
        normalization_rule_status: str = None,
        normalization_rule_type: str = None,
        normalization_rule_version: str = None,
        normalization_schema_id: str = None,
        product_id: str = None,
        update_time: int = None,
        vendor_id: str = None,
    ):
        self.create_time = create_time
        self.extend_content_packed = extend_content_packed
        self.normalization_category_id = normalization_category_id
        self.normalization_rule_description = normalization_rule_description
        self.normalization_rule_expression = normalization_rule_expression
        self.normalization_rule_format = normalization_rule_format
        self.normalization_rule_id = normalization_rule_id
        self.normalization_rule_mode = normalization_rule_mode
        self.normalization_rule_name = normalization_rule_name
        self.normalization_rule_references = normalization_rule_references
        self.normalization_rule_status = normalization_rule_status
        self.normalization_rule_type = normalization_rule_type
        self.normalization_rule_version = normalization_rule_version
        self.normalization_schema_id = normalization_schema_id
        self.product_id = product_id
        self.update_time = update_time
        self.vendor_id = vendor_id

    def validate(self):
        if self.normalization_rule_references:
            for k in self.normalization_rule_references:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.extend_content_packed is not None:
            result['ExtendContentPacked'] = self.extend_content_packed
        if self.normalization_category_id is not None:
            result['NormalizationCategoryId'] = self.normalization_category_id
        if self.normalization_rule_description is not None:
            result['NormalizationRuleDescription'] = self.normalization_rule_description
        if self.normalization_rule_expression is not None:
            result['NormalizationRuleExpression'] = self.normalization_rule_expression
        if self.normalization_rule_format is not None:
            result['NormalizationRuleFormat'] = self.normalization_rule_format
        if self.normalization_rule_id is not None:
            result['NormalizationRuleId'] = self.normalization_rule_id
        if self.normalization_rule_mode is not None:
            result['NormalizationRuleMode'] = self.normalization_rule_mode
        if self.normalization_rule_name is not None:
            result['NormalizationRuleName'] = self.normalization_rule_name
        result['NormalizationRuleReferences'] = []
        if self.normalization_rule_references is not None:
            for k in self.normalization_rule_references:
                result['NormalizationRuleReferences'].append(k.to_map() if k else None)
        if self.normalization_rule_status is not None:
            result['NormalizationRuleStatus'] = self.normalization_rule_status
        if self.normalization_rule_type is not None:
            result['NormalizationRuleType'] = self.normalization_rule_type
        if self.normalization_rule_version is not None:
            result['NormalizationRuleVersion'] = self.normalization_rule_version
        if self.normalization_schema_id is not None:
            result['NormalizationSchemaId'] = self.normalization_schema_id
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.vendor_id is not None:
            result['VendorId'] = self.vendor_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ExtendContentPacked') is not None:
            self.extend_content_packed = m.get('ExtendContentPacked')
        if m.get('NormalizationCategoryId') is not None:
            self.normalization_category_id = m.get('NormalizationCategoryId')
        if m.get('NormalizationRuleDescription') is not None:
            self.normalization_rule_description = m.get('NormalizationRuleDescription')
        if m.get('NormalizationRuleExpression') is not None:
            self.normalization_rule_expression = m.get('NormalizationRuleExpression')
        if m.get('NormalizationRuleFormat') is not None:
            self.normalization_rule_format = m.get('NormalizationRuleFormat')
        if m.get('NormalizationRuleId') is not None:
            self.normalization_rule_id = m.get('NormalizationRuleId')
        if m.get('NormalizationRuleMode') is not None:
            self.normalization_rule_mode = m.get('NormalizationRuleMode')
        if m.get('NormalizationRuleName') is not None:
            self.normalization_rule_name = m.get('NormalizationRuleName')
        self.normalization_rule_references = []
        if m.get('NormalizationRuleReferences') is not None:
            for k in m.get('NormalizationRuleReferences'):
                temp_model = ListNormalizationRulesResponseBodyNormalizationRulesNormalizationRuleReferences()
                self.normalization_rule_references.append(temp_model.from_map(k))
        if m.get('NormalizationRuleStatus') is not None:
            self.normalization_rule_status = m.get('NormalizationRuleStatus')
        if m.get('NormalizationRuleType') is not None:
            self.normalization_rule_type = m.get('NormalizationRuleType')
        if m.get('NormalizationRuleVersion') is not None:
            self.normalization_rule_version = m.get('NormalizationRuleVersion')
        if m.get('NormalizationSchemaId') is not None:
            self.normalization_schema_id = m.get('NormalizationSchemaId')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('VendorId') is not None:
            self.vendor_id = m.get('VendorId')
        return self


class ListNormalizationRulesResponseBody(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        normalization_rules: List[ListNormalizationRulesResponseBodyNormalizationRules] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
        total_page: int = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.normalization_rules = normalization_rules
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count
        self.total_page = total_page

    def validate(self):
        if self.normalization_rules:
            for k in self.normalization_rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        result['NormalizationRules'] = []
        if self.normalization_rules is not None:
            for k in self.normalization_rules:
                result['NormalizationRules'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.total_page is not None:
            result['TotalPage'] = self.total_page
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.normalization_rules = []
        if m.get('NormalizationRules') is not None:
            for k in m.get('NormalizationRules'):
                temp_model = ListNormalizationRulesResponseBodyNormalizationRules()
                self.normalization_rules.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')
        return self


class ListNormalizationRulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListNormalizationRulesResponseBody = None,
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
            temp_model = ListNormalizationRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListNormalizationSchemasRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        max_results: int = None,
        next_token: str = None,
        normalization_category_id: str = None,
        normalization_schema_type: str = None,
        region_id: str = None,
        role_for: int = None,
    ):
        self.lang = lang
        self.max_results = max_results
        self.next_token = next_token
        self.normalization_category_id = normalization_category_id
        self.normalization_schema_type = normalization_schema_type
        self.region_id = region_id
        self.role_for = role_for

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.normalization_category_id is not None:
            result['NormalizationCategoryId'] = self.normalization_category_id
        if self.normalization_schema_type is not None:
            result['NormalizationSchemaType'] = self.normalization_schema_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.role_for is not None:
            result['RoleFor'] = self.role_for
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('NormalizationCategoryId') is not None:
            self.normalization_category_id = m.get('NormalizationCategoryId')
        if m.get('NormalizationSchemaType') is not None:
            self.normalization_schema_type = m.get('NormalizationSchemaType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')
        return self


class ListNormalizationSchemasResponseBodyNormalizationSchemas(TeaModel):
    def __init__(
        self,
        normalization_category_id: str = None,
        normalization_schema_id: str = None,
        normalization_schema_name: str = None,
        normalization_schema_target_log_store: str = None,
    ):
        self.normalization_category_id = normalization_category_id
        self.normalization_schema_id = normalization_schema_id
        self.normalization_schema_name = normalization_schema_name
        self.normalization_schema_target_log_store = normalization_schema_target_log_store

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.normalization_category_id is not None:
            result['NormalizationCategoryId'] = self.normalization_category_id
        if self.normalization_schema_id is not None:
            result['NormalizationSchemaId'] = self.normalization_schema_id
        if self.normalization_schema_name is not None:
            result['NormalizationSchemaName'] = self.normalization_schema_name
        if self.normalization_schema_target_log_store is not None:
            result['NormalizationSchemaTargetLogStore'] = self.normalization_schema_target_log_store
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NormalizationCategoryId') is not None:
            self.normalization_category_id = m.get('NormalizationCategoryId')
        if m.get('NormalizationSchemaId') is not None:
            self.normalization_schema_id = m.get('NormalizationSchemaId')
        if m.get('NormalizationSchemaName') is not None:
            self.normalization_schema_name = m.get('NormalizationSchemaName')
        if m.get('NormalizationSchemaTargetLogStore') is not None:
            self.normalization_schema_target_log_store = m.get('NormalizationSchemaTargetLogStore')
        return self


class ListNormalizationSchemasResponseBody(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        normalization_schemas: List[ListNormalizationSchemasResponseBodyNormalizationSchemas] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.normalization_schemas = normalization_schemas
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.normalization_schemas:
            for k in self.normalization_schemas:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        result['NormalizationSchemas'] = []
        if self.normalization_schemas is not None:
            for k in self.normalization_schemas:
                result['NormalizationSchemas'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.normalization_schemas = []
        if m.get('NormalizationSchemas') is not None:
            for k in m.get('NormalizationSchemas'):
                temp_model = ListNormalizationSchemasResponseBodyNormalizationSchemas()
                self.normalization_schemas.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListNormalizationSchemasResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListNormalizationSchemasResponseBody = None,
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
            temp_model = ListNormalizationSchemasResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListProductsRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        max_results: int = None,
        next_token: str = None,
        product_ids: List[str] = None,
        product_name: str = None,
        product_type: str = None,
        region_id: str = None,
        role_for: int = None,
        vendor_id: str = None,
    ):
        self.lang = lang
        self.max_results = max_results
        self.next_token = next_token
        self.product_ids = product_ids
        self.product_name = product_name
        self.product_type = product_type
        self.region_id = region_id
        self.role_for = role_for
        self.vendor_id = vendor_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.product_ids is not None:
            result['ProductIds'] = self.product_ids
        if self.product_name is not None:
            result['ProductName'] = self.product_name
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.role_for is not None:
            result['RoleFor'] = self.role_for
        if self.vendor_id is not None:
            result['VendorId'] = self.vendor_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ProductIds') is not None:
            self.product_ids = m.get('ProductIds')
        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')
        if m.get('VendorId') is not None:
            self.vendor_id = m.get('VendorId')
        return self


class ListProductsShrinkRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        max_results: int = None,
        next_token: str = None,
        product_ids_shrink: str = None,
        product_name: str = None,
        product_type: str = None,
        region_id: str = None,
        role_for: int = None,
        vendor_id: str = None,
    ):
        self.lang = lang
        self.max_results = max_results
        self.next_token = next_token
        self.product_ids_shrink = product_ids_shrink
        self.product_name = product_name
        self.product_type = product_type
        self.region_id = region_id
        self.role_for = role_for
        self.vendor_id = vendor_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.product_ids_shrink is not None:
            result['ProductIds'] = self.product_ids_shrink
        if self.product_name is not None:
            result['ProductName'] = self.product_name
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.role_for is not None:
            result['RoleFor'] = self.role_for
        if self.vendor_id is not None:
            result['VendorId'] = self.vendor_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ProductIds') is not None:
            self.product_ids_shrink = m.get('ProductIds')
        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')
        if m.get('VendorId') is not None:
            self.vendor_id = m.get('VendorId')
        return self


class ListProductsResponseBodyProducts(TeaModel):
    def __init__(
        self,
        abnormal_data_ingestion_count: int = None,
        active_time: int = None,
        allow_add_data_ingestion: bool = None,
        create_time: int = None,
        data_ingestion_status: bool = None,
        enabled_data_ingestion_count: int = None,
        product_alias: str = None,
        product_id: str = None,
        product_name: str = None,
        product_type: str = None,
        total_data_ingestion_count: int = None,
        update_time: int = None,
        vendor_id: str = None,
        vendor_name: str = None,
    ):
        self.abnormal_data_ingestion_count = abnormal_data_ingestion_count
        self.active_time = active_time
        self.allow_add_data_ingestion = allow_add_data_ingestion
        self.create_time = create_time
        self.data_ingestion_status = data_ingestion_status
        self.enabled_data_ingestion_count = enabled_data_ingestion_count
        self.product_alias = product_alias
        self.product_id = product_id
        self.product_name = product_name
        self.product_type = product_type
        self.total_data_ingestion_count = total_data_ingestion_count
        self.update_time = update_time
        self.vendor_id = vendor_id
        self.vendor_name = vendor_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.abnormal_data_ingestion_count is not None:
            result['AbnormalDataIngestionCount'] = self.abnormal_data_ingestion_count
        if self.active_time is not None:
            result['ActiveTime'] = self.active_time
        if self.allow_add_data_ingestion is not None:
            result['AllowAddDataIngestion'] = self.allow_add_data_ingestion
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.data_ingestion_status is not None:
            result['DataIngestionStatus'] = self.data_ingestion_status
        if self.enabled_data_ingestion_count is not None:
            result['EnabledDataIngestionCount'] = self.enabled_data_ingestion_count
        if self.product_alias is not None:
            result['ProductAlias'] = self.product_alias
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.product_name is not None:
            result['ProductName'] = self.product_name
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.total_data_ingestion_count is not None:
            result['TotalDataIngestionCount'] = self.total_data_ingestion_count
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.vendor_id is not None:
            result['VendorId'] = self.vendor_id
        if self.vendor_name is not None:
            result['VendorName'] = self.vendor_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AbnormalDataIngestionCount') is not None:
            self.abnormal_data_ingestion_count = m.get('AbnormalDataIngestionCount')
        if m.get('ActiveTime') is not None:
            self.active_time = m.get('ActiveTime')
        if m.get('AllowAddDataIngestion') is not None:
            self.allow_add_data_ingestion = m.get('AllowAddDataIngestion')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DataIngestionStatus') is not None:
            self.data_ingestion_status = m.get('DataIngestionStatus')
        if m.get('EnabledDataIngestionCount') is not None:
            self.enabled_data_ingestion_count = m.get('EnabledDataIngestionCount')
        if m.get('ProductAlias') is not None:
            self.product_alias = m.get('ProductAlias')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('TotalDataIngestionCount') is not None:
            self.total_data_ingestion_count = m.get('TotalDataIngestionCount')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('VendorId') is not None:
            self.vendor_id = m.get('VendorId')
        if m.get('VendorName') is not None:
            self.vendor_name = m.get('VendorName')
        return self


class ListProductsResponseBody(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        products: List[ListProductsResponseBodyProducts] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.products = products
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.products:
            for k in self.products:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        result['Products'] = []
        if self.products is not None:
            for k in self.products:
                result['Products'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.products = []
        if m.get('Products') is not None:
            for k in m.get('Products'):
                temp_model = ListProductsResponseBodyProducts()
                self.products.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListProductsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListProductsResponseBody = None,
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
            temp_model = ListProductsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTrafficStatisticsRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        log_user_ids: List[int] = None,
        product_id: str = None,
        region_id: str = None,
        region_tag: int = None,
        role_for: int = None,
        traffic_statistic_period: str = None,
        traffic_statistic_period_type: str = None,
        traffic_statistic_type: str = None,
    ):
        self.lang = lang
        self.log_user_ids = log_user_ids
        self.product_id = product_id
        self.region_id = region_id
        self.region_tag = region_tag
        self.role_for = role_for
        self.traffic_statistic_period = traffic_statistic_period
        self.traffic_statistic_period_type = traffic_statistic_period_type
        self.traffic_statistic_type = traffic_statistic_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.log_user_ids is not None:
            result['LogUserIds'] = self.log_user_ids
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.region_tag is not None:
            result['RegionTag'] = self.region_tag
        if self.role_for is not None:
            result['RoleFor'] = self.role_for
        if self.traffic_statistic_period is not None:
            result['TrafficStatisticPeriod'] = self.traffic_statistic_period
        if self.traffic_statistic_period_type is not None:
            result['TrafficStatisticPeriodType'] = self.traffic_statistic_period_type
        if self.traffic_statistic_type is not None:
            result['TrafficStatisticType'] = self.traffic_statistic_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('LogUserIds') is not None:
            self.log_user_ids = m.get('LogUserIds')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RegionTag') is not None:
            self.region_tag = m.get('RegionTag')
        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')
        if m.get('TrafficStatisticPeriod') is not None:
            self.traffic_statistic_period = m.get('TrafficStatisticPeriod')
        if m.get('TrafficStatisticPeriodType') is not None:
            self.traffic_statistic_period_type = m.get('TrafficStatisticPeriodType')
        if m.get('TrafficStatisticType') is not None:
            self.traffic_statistic_type = m.get('TrafficStatisticType')
        return self


class ListTrafficStatisticsShrinkRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        log_user_ids_shrink: str = None,
        product_id: str = None,
        region_id: str = None,
        region_tag: int = None,
        role_for: int = None,
        traffic_statistic_period: str = None,
        traffic_statistic_period_type: str = None,
        traffic_statistic_type: str = None,
    ):
        self.lang = lang
        self.log_user_ids_shrink = log_user_ids_shrink
        self.product_id = product_id
        self.region_id = region_id
        self.region_tag = region_tag
        self.role_for = role_for
        self.traffic_statistic_period = traffic_statistic_period
        self.traffic_statistic_period_type = traffic_statistic_period_type
        self.traffic_statistic_type = traffic_statistic_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.log_user_ids_shrink is not None:
            result['LogUserIds'] = self.log_user_ids_shrink
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.region_tag is not None:
            result['RegionTag'] = self.region_tag
        if self.role_for is not None:
            result['RoleFor'] = self.role_for
        if self.traffic_statistic_period is not None:
            result['TrafficStatisticPeriod'] = self.traffic_statistic_period
        if self.traffic_statistic_period_type is not None:
            result['TrafficStatisticPeriodType'] = self.traffic_statistic_period_type
        if self.traffic_statistic_type is not None:
            result['TrafficStatisticType'] = self.traffic_statistic_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('LogUserIds') is not None:
            self.log_user_ids_shrink = m.get('LogUserIds')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RegionTag') is not None:
            self.region_tag = m.get('RegionTag')
        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')
        if m.get('TrafficStatisticPeriod') is not None:
            self.traffic_statistic_period = m.get('TrafficStatisticPeriod')
        if m.get('TrafficStatisticPeriodType') is not None:
            self.traffic_statistic_period_type = m.get('TrafficStatisticPeriodType')
        if m.get('TrafficStatisticType') is not None:
            self.traffic_statistic_type = m.get('TrafficStatisticType')
        return self


class ListTrafficStatisticsResponseBodyTrafficStatisticsTrafficStatisticData(TeaModel):
    def __init__(
        self,
        traffic_statistic_time: int = None,
        traffic_statistic_value: float = None,
    ):
        self.traffic_statistic_time = traffic_statistic_time
        self.traffic_statistic_value = traffic_statistic_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.traffic_statistic_time is not None:
            result['TrafficStatisticTime'] = self.traffic_statistic_time
        if self.traffic_statistic_value is not None:
            result['TrafficStatisticValue'] = self.traffic_statistic_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TrafficStatisticTime') is not None:
            self.traffic_statistic_time = m.get('TrafficStatisticTime')
        if m.get('TrafficStatisticValue') is not None:
            self.traffic_statistic_value = m.get('TrafficStatisticValue')
        return self


class ListTrafficStatisticsResponseBodyTrafficStatistics(TeaModel):
    def __init__(
        self,
        traffic_statistic_data: List[ListTrafficStatisticsResponseBodyTrafficStatisticsTrafficStatisticData] = None,
        traffic_statistic_target: str = None,
    ):
        self.traffic_statistic_data = traffic_statistic_data
        self.traffic_statistic_target = traffic_statistic_target

    def validate(self):
        if self.traffic_statistic_data:
            for k in self.traffic_statistic_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TrafficStatisticData'] = []
        if self.traffic_statistic_data is not None:
            for k in self.traffic_statistic_data:
                result['TrafficStatisticData'].append(k.to_map() if k else None)
        if self.traffic_statistic_target is not None:
            result['TrafficStatisticTarget'] = self.traffic_statistic_target
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.traffic_statistic_data = []
        if m.get('TrafficStatisticData') is not None:
            for k in m.get('TrafficStatisticData'):
                temp_model = ListTrafficStatisticsResponseBodyTrafficStatisticsTrafficStatisticData()
                self.traffic_statistic_data.append(temp_model.from_map(k))
        if m.get('TrafficStatisticTarget') is not None:
            self.traffic_statistic_target = m.get('TrafficStatisticTarget')
        return self


class ListTrafficStatisticsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        traffic_statistics: List[ListTrafficStatisticsResponseBodyTrafficStatistics] = None,
    ):
        self.request_id = request_id
        self.traffic_statistics = traffic_statistics

    def validate(self):
        if self.traffic_statistics:
            for k in self.traffic_statistics:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['TrafficStatistics'] = []
        if self.traffic_statistics is not None:
            for k in self.traffic_statistics:
                result['TrafficStatistics'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.traffic_statistics = []
        if m.get('TrafficStatistics') is not None:
            for k in m.get('TrafficStatistics'):
                temp_model = ListTrafficStatisticsResponseBodyTrafficStatistics()
                self.traffic_statistics.append(temp_model.from_map(k))
        return self


class ListTrafficStatisticsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTrafficStatisticsResponseBody = None,
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
            temp_model = ListTrafficStatisticsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUpgradeItemsRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
        role_for: str = None,
    ):
        self.lang = lang
        self.max_results = max_results
        self.next_token = next_token
        self.region_id = region_id
        self.role_for = role_for

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.role_for is not None:
            result['RoleFor'] = self.role_for
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')
        return self


class ListUpgradeItemsResponseBodyUpgradeItems(TeaModel):
    def __init__(
        self,
        upgrade_item_id: str = None,
    ):
        self.upgrade_item_id = upgrade_item_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.upgrade_item_id is not None:
            result['UpgradeItemId'] = self.upgrade_item_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UpgradeItemId') is not None:
            self.upgrade_item_id = m.get('UpgradeItemId')
        return self


class ListUpgradeItemsResponseBody(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
        upgrade_items: List[ListUpgradeItemsResponseBodyUpgradeItems] = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id
        self.total_count = total_count
        self.upgrade_items = upgrade_items

    def validate(self):
        if self.upgrade_items:
            for k in self.upgrade_items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['UpgradeItems'] = []
        if self.upgrade_items is not None:
            for k in self.upgrade_items:
                result['UpgradeItems'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.upgrade_items = []
        if m.get('UpgradeItems') is not None:
            for k in m.get('UpgradeItems'):
                temp_model = ListUpgradeItemsResponseBodyUpgradeItems()
                self.upgrade_items.append(temp_model.from_map(k))
        return self


class ListUpgradeItemsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListUpgradeItemsResponseBody = None,
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
            temp_model = ListUpgradeItemsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListVendorsRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
        role_for: int = None,
        vendor_ids: List[str] = None,
        vendor_name: str = None,
        vendor_type: str = None,
    ):
        self.lang = lang
        self.max_results = max_results
        self.next_token = next_token
        self.region_id = region_id
        self.role_for = role_for
        self.vendor_ids = vendor_ids
        self.vendor_name = vendor_name
        self.vendor_type = vendor_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.role_for is not None:
            result['RoleFor'] = self.role_for
        if self.vendor_ids is not None:
            result['VendorIds'] = self.vendor_ids
        if self.vendor_name is not None:
            result['VendorName'] = self.vendor_name
        if self.vendor_type is not None:
            result['VendorType'] = self.vendor_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')
        if m.get('VendorIds') is not None:
            self.vendor_ids = m.get('VendorIds')
        if m.get('VendorName') is not None:
            self.vendor_name = m.get('VendorName')
        if m.get('VendorType') is not None:
            self.vendor_type = m.get('VendorType')
        return self


class ListVendorsShrinkRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
        role_for: int = None,
        vendor_ids_shrink: str = None,
        vendor_name: str = None,
        vendor_type: str = None,
    ):
        self.lang = lang
        self.max_results = max_results
        self.next_token = next_token
        self.region_id = region_id
        self.role_for = role_for
        self.vendor_ids_shrink = vendor_ids_shrink
        self.vendor_name = vendor_name
        self.vendor_type = vendor_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.role_for is not None:
            result['RoleFor'] = self.role_for
        if self.vendor_ids_shrink is not None:
            result['VendorIds'] = self.vendor_ids_shrink
        if self.vendor_name is not None:
            result['VendorName'] = self.vendor_name
        if self.vendor_type is not None:
            result['VendorType'] = self.vendor_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')
        if m.get('VendorIds') is not None:
            self.vendor_ids_shrink = m.get('VendorIds')
        if m.get('VendorName') is not None:
            self.vendor_name = m.get('VendorName')
        if m.get('VendorType') is not None:
            self.vendor_type = m.get('VendorType')
        return self


class ListVendorsResponseBodyVendors(TeaModel):
    def __init__(
        self,
        create_time: int = None,
        update_time: int = None,
        vendor_id: str = None,
        vendor_name: str = None,
        vendor_type: str = None,
    ):
        self.create_time = create_time
        self.update_time = update_time
        self.vendor_id = vendor_id
        self.vendor_name = vendor_name
        self.vendor_type = vendor_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.vendor_id is not None:
            result['VendorId'] = self.vendor_id
        if self.vendor_name is not None:
            result['VendorName'] = self.vendor_name
        if self.vendor_type is not None:
            result['VendorType'] = self.vendor_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('VendorId') is not None:
            self.vendor_id = m.get('VendorId')
        if m.get('VendorName') is not None:
            self.vendor_name = m.get('VendorName')
        if m.get('VendorType') is not None:
            self.vendor_type = m.get('VendorType')
        return self


class ListVendorsResponseBody(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
        vendors: List[ListVendorsResponseBodyVendors] = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id
        self.total_count = total_count
        self.vendors = vendors

    def validate(self):
        if self.vendors:
            for k in self.vendors:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['Vendors'] = []
        if self.vendors is not None:
            for k in self.vendors:
                result['Vendors'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.vendors = []
        if m.get('Vendors') is not None:
            for k in m.get('Vendors'):
                temp_model = ListVendorsResponseBodyVendors()
                self.vendors.append(temp_model.from_map(k))
        return self


class ListVendorsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListVendorsResponseBody = None,
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
            temp_model = ListVendorsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResetDataStorageRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        region_id: str = None,
        role_for: int = None,
    ):
        self.lang = lang
        self.region_id = region_id
        self.role_for = role_for

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.role_for is not None:
            result['RoleFor'] = self.role_for
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')
        return self


class ResetDataStorageResponseBody(TeaModel):
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


class ResetDataStorageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ResetDataStorageResponseBody = None,
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
            temp_model = ResetDataStorageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetDefaultNormalizationRuleVersionRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        normalization_rule_id: str = None,
        normalization_rule_version: int = None,
        region_id: str = None,
        role_for: int = None,
    ):
        self.lang = lang
        self.normalization_rule_id = normalization_rule_id
        self.normalization_rule_version = normalization_rule_version
        self.region_id = region_id
        self.role_for = role_for

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.normalization_rule_id is not None:
            result['NormalizationRuleId'] = self.normalization_rule_id
        if self.normalization_rule_version is not None:
            result['NormalizationRuleVersion'] = self.normalization_rule_version
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.role_for is not None:
            result['RoleFor'] = self.role_for
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('NormalizationRuleId') is not None:
            self.normalization_rule_id = m.get('NormalizationRuleId')
        if m.get('NormalizationRuleVersion') is not None:
            self.normalization_rule_version = m.get('NormalizationRuleVersion')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')
        return self


class SetDefaultNormalizationRuleVersionResponseBodyNormalizationRuleVersion(TeaModel):
    def __init__(
        self,
        create_time: int = None,
        normalization_category_id: str = None,
        normalization_rule_description: str = None,
        normalization_rule_expression: str = None,
        normalization_rule_format: str = None,
        normalization_rule_id: str = None,
        normalization_rule_name: str = None,
        normalization_rule_status: str = None,
        normalization_rule_type: str = None,
        normalization_rule_version: int = None,
        normalization_schema_id: str = None,
        product_id: str = None,
        update_time: int = None,
        vendor_id: str = None,
    ):
        self.create_time = create_time
        self.normalization_category_id = normalization_category_id
        self.normalization_rule_description = normalization_rule_description
        self.normalization_rule_expression = normalization_rule_expression
        self.normalization_rule_format = normalization_rule_format
        self.normalization_rule_id = normalization_rule_id
        self.normalization_rule_name = normalization_rule_name
        self.normalization_rule_status = normalization_rule_status
        self.normalization_rule_type = normalization_rule_type
        self.normalization_rule_version = normalization_rule_version
        self.normalization_schema_id = normalization_schema_id
        self.product_id = product_id
        self.update_time = update_time
        self.vendor_id = vendor_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.normalization_category_id is not None:
            result['NormalizationCategoryId'] = self.normalization_category_id
        if self.normalization_rule_description is not None:
            result['NormalizationRuleDescription'] = self.normalization_rule_description
        if self.normalization_rule_expression is not None:
            result['NormalizationRuleExpression'] = self.normalization_rule_expression
        if self.normalization_rule_format is not None:
            result['NormalizationRuleFormat'] = self.normalization_rule_format
        if self.normalization_rule_id is not None:
            result['NormalizationRuleId'] = self.normalization_rule_id
        if self.normalization_rule_name is not None:
            result['NormalizationRuleName'] = self.normalization_rule_name
        if self.normalization_rule_status is not None:
            result['NormalizationRuleStatus'] = self.normalization_rule_status
        if self.normalization_rule_type is not None:
            result['NormalizationRuleType'] = self.normalization_rule_type
        if self.normalization_rule_version is not None:
            result['NormalizationRuleVersion'] = self.normalization_rule_version
        if self.normalization_schema_id is not None:
            result['NormalizationSchemaId'] = self.normalization_schema_id
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.vendor_id is not None:
            result['VendorId'] = self.vendor_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('NormalizationCategoryId') is not None:
            self.normalization_category_id = m.get('NormalizationCategoryId')
        if m.get('NormalizationRuleDescription') is not None:
            self.normalization_rule_description = m.get('NormalizationRuleDescription')
        if m.get('NormalizationRuleExpression') is not None:
            self.normalization_rule_expression = m.get('NormalizationRuleExpression')
        if m.get('NormalizationRuleFormat') is not None:
            self.normalization_rule_format = m.get('NormalizationRuleFormat')
        if m.get('NormalizationRuleId') is not None:
            self.normalization_rule_id = m.get('NormalizationRuleId')
        if m.get('NormalizationRuleName') is not None:
            self.normalization_rule_name = m.get('NormalizationRuleName')
        if m.get('NormalizationRuleStatus') is not None:
            self.normalization_rule_status = m.get('NormalizationRuleStatus')
        if m.get('NormalizationRuleType') is not None:
            self.normalization_rule_type = m.get('NormalizationRuleType')
        if m.get('NormalizationRuleVersion') is not None:
            self.normalization_rule_version = m.get('NormalizationRuleVersion')
        if m.get('NormalizationSchemaId') is not None:
            self.normalization_schema_id = m.get('NormalizationSchemaId')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('VendorId') is not None:
            self.vendor_id = m.get('VendorId')
        return self


class SetDefaultNormalizationRuleVersionResponseBody(TeaModel):
    def __init__(
        self,
        normalization_rule_version: SetDefaultNormalizationRuleVersionResponseBodyNormalizationRuleVersion = None,
        request_id: str = None,
    ):
        self.normalization_rule_version = normalization_rule_version
        self.request_id = request_id

    def validate(self):
        if self.normalization_rule_version:
            self.normalization_rule_version.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.normalization_rule_version is not None:
            result['NormalizationRuleVersion'] = self.normalization_rule_version.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NormalizationRuleVersion') is not None:
            temp_model = SetDefaultNormalizationRuleVersionResponseBodyNormalizationRuleVersion()
            self.normalization_rule_version = temp_model.from_map(m['NormalizationRuleVersion'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SetDefaultNormalizationRuleVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SetDefaultNormalizationRuleVersionResponseBody = None,
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
            temp_model = SetDefaultNormalizationRuleVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDataBatchIngestionRequest(TeaModel):
    def __init__(
        self,
        auto_scan_new: str = None,
        data_batch_ingestion_mode: str = None,
        data_ingestion_ids: List[str] = None,
        data_source_recognize_enabled: bool = None,
        lang: str = None,
        log_user_ids: List[int] = None,
        region_id: str = None,
        role_for: int = None,
    ):
        self.auto_scan_new = auto_scan_new
        self.data_batch_ingestion_mode = data_batch_ingestion_mode
        self.data_ingestion_ids = data_ingestion_ids
        self.data_source_recognize_enabled = data_source_recognize_enabled
        self.lang = lang
        self.log_user_ids = log_user_ids
        self.region_id = region_id
        self.role_for = role_for

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_scan_new is not None:
            result['AutoScanNew'] = self.auto_scan_new
        if self.data_batch_ingestion_mode is not None:
            result['DataBatchIngestionMode'] = self.data_batch_ingestion_mode
        if self.data_ingestion_ids is not None:
            result['DataIngestionIds'] = self.data_ingestion_ids
        if self.data_source_recognize_enabled is not None:
            result['DataSourceRecognizeEnabled'] = self.data_source_recognize_enabled
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.log_user_ids is not None:
            result['LogUserIds'] = self.log_user_ids
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.role_for is not None:
            result['RoleFor'] = self.role_for
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoScanNew') is not None:
            self.auto_scan_new = m.get('AutoScanNew')
        if m.get('DataBatchIngestionMode') is not None:
            self.data_batch_ingestion_mode = m.get('DataBatchIngestionMode')
        if m.get('DataIngestionIds') is not None:
            self.data_ingestion_ids = m.get('DataIngestionIds')
        if m.get('DataSourceRecognizeEnabled') is not None:
            self.data_source_recognize_enabled = m.get('DataSourceRecognizeEnabled')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('LogUserIds') is not None:
            self.log_user_ids = m.get('LogUserIds')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')
        return self


class UpdateDataBatchIngestionShrinkRequest(TeaModel):
    def __init__(
        self,
        auto_scan_new: str = None,
        data_batch_ingestion_mode: str = None,
        data_ingestion_ids_shrink: str = None,
        data_source_recognize_enabled: bool = None,
        lang: str = None,
        log_user_ids_shrink: str = None,
        region_id: str = None,
        role_for: int = None,
    ):
        self.auto_scan_new = auto_scan_new
        self.data_batch_ingestion_mode = data_batch_ingestion_mode
        self.data_ingestion_ids_shrink = data_ingestion_ids_shrink
        self.data_source_recognize_enabled = data_source_recognize_enabled
        self.lang = lang
        self.log_user_ids_shrink = log_user_ids_shrink
        self.region_id = region_id
        self.role_for = role_for

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_scan_new is not None:
            result['AutoScanNew'] = self.auto_scan_new
        if self.data_batch_ingestion_mode is not None:
            result['DataBatchIngestionMode'] = self.data_batch_ingestion_mode
        if self.data_ingestion_ids_shrink is not None:
            result['DataIngestionIds'] = self.data_ingestion_ids_shrink
        if self.data_source_recognize_enabled is not None:
            result['DataSourceRecognizeEnabled'] = self.data_source_recognize_enabled
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.log_user_ids_shrink is not None:
            result['LogUserIds'] = self.log_user_ids_shrink
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.role_for is not None:
            result['RoleFor'] = self.role_for
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoScanNew') is not None:
            self.auto_scan_new = m.get('AutoScanNew')
        if m.get('DataBatchIngestionMode') is not None:
            self.data_batch_ingestion_mode = m.get('DataBatchIngestionMode')
        if m.get('DataIngestionIds') is not None:
            self.data_ingestion_ids_shrink = m.get('DataIngestionIds')
        if m.get('DataSourceRecognizeEnabled') is not None:
            self.data_source_recognize_enabled = m.get('DataSourceRecognizeEnabled')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('LogUserIds') is not None:
            self.log_user_ids_shrink = m.get('LogUserIds')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')
        return self


class UpdateDataBatchIngestionResponseBody(TeaModel):
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


class UpdateDataBatchIngestionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateDataBatchIngestionResponseBody = None,
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
            temp_model = UpdateDataBatchIngestionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDataIngestionRequest(TeaModel):
    def __init__(
        self,
        data_ingestion_id: str = None,
        data_ingestion_mode: str = None,
        data_source_id: str = None,
        lang: str = None,
        normalization_rule_id: str = None,
        region_id: str = None,
        role_for: int = None,
    ):
        self.data_ingestion_id = data_ingestion_id
        self.data_ingestion_mode = data_ingestion_mode
        self.data_source_id = data_source_id
        self.lang = lang
        self.normalization_rule_id = normalization_rule_id
        self.region_id = region_id
        self.role_for = role_for

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_ingestion_id is not None:
            result['DataIngestionId'] = self.data_ingestion_id
        if self.data_ingestion_mode is not None:
            result['DataIngestionMode'] = self.data_ingestion_mode
        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.normalization_rule_id is not None:
            result['NormalizationRuleId'] = self.normalization_rule_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.role_for is not None:
            result['RoleFor'] = self.role_for
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataIngestionId') is not None:
            self.data_ingestion_id = m.get('DataIngestionId')
        if m.get('DataIngestionMode') is not None:
            self.data_ingestion_mode = m.get('DataIngestionMode')
        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('NormalizationRuleId') is not None:
            self.normalization_rule_id = m.get('NormalizationRuleId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')
        return self


class UpdateDataIngestionResponseBody(TeaModel):
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


class UpdateDataIngestionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateDataIngestionResponseBody = None,
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
            temp_model = UpdateDataIngestionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDataIngestionTemplateRequest(TeaModel):
    def __init__(
        self,
        data_ingestion_status: str = None,
        data_ingestion_template_id: str = None,
        data_ingestion_template_name: str = None,
        lang: str = None,
        normalization_rule_id: str = None,
        region_id: str = None,
        role_for: int = None,
    ):
        self.data_ingestion_status = data_ingestion_status
        self.data_ingestion_template_id = data_ingestion_template_id
        self.data_ingestion_template_name = data_ingestion_template_name
        self.lang = lang
        self.normalization_rule_id = normalization_rule_id
        self.region_id = region_id
        self.role_for = role_for

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_ingestion_status is not None:
            result['DataIngestionStatus'] = self.data_ingestion_status
        if self.data_ingestion_template_id is not None:
            result['DataIngestionTemplateId'] = self.data_ingestion_template_id
        if self.data_ingestion_template_name is not None:
            result['DataIngestionTemplateName'] = self.data_ingestion_template_name
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.normalization_rule_id is not None:
            result['NormalizationRuleId'] = self.normalization_rule_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.role_for is not None:
            result['RoleFor'] = self.role_for
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataIngestionStatus') is not None:
            self.data_ingestion_status = m.get('DataIngestionStatus')
        if m.get('DataIngestionTemplateId') is not None:
            self.data_ingestion_template_id = m.get('DataIngestionTemplateId')
        if m.get('DataIngestionTemplateName') is not None:
            self.data_ingestion_template_name = m.get('DataIngestionTemplateName')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('NormalizationRuleId') is not None:
            self.normalization_rule_id = m.get('NormalizationRuleId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')
        return self


class UpdateDataIngestionTemplateResponseBody(TeaModel):
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


class UpdateDataIngestionTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateDataIngestionTemplateResponseBody = None,
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
            temp_model = UpdateDataIngestionTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDataSetRequestIpWhitelistRecognizers(TeaModel):
    def __init__(
        self,
        auto_recognize_status: str = None,
        ip_whitelist_recognizer_type: str = None,
        recognize_scope: str = None,
    ):
        self.auto_recognize_status = auto_recognize_status
        self.ip_whitelist_recognizer_type = ip_whitelist_recognizer_type
        self.recognize_scope = recognize_scope

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_recognize_status is not None:
            result['AutoRecognizeStatus'] = self.auto_recognize_status
        if self.ip_whitelist_recognizer_type is not None:
            result['IpWhitelistRecognizerType'] = self.ip_whitelist_recognizer_type
        if self.recognize_scope is not None:
            result['RecognizeScope'] = self.recognize_scope
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoRecognizeStatus') is not None:
            self.auto_recognize_status = m.get('AutoRecognizeStatus')
        if m.get('IpWhitelistRecognizerType') is not None:
            self.ip_whitelist_recognizer_type = m.get('IpWhitelistRecognizerType')
        if m.get('RecognizeScope') is not None:
            self.recognize_scope = m.get('RecognizeScope')
        return self


class UpdateDataSetRequest(TeaModel):
    def __init__(
        self,
        data_set_description: str = None,
        data_set_file_name: str = None,
        data_set_id: str = None,
        data_set_name: str = None,
        data_set_status: int = None,
        ip_whitelist_recognizers: List[UpdateDataSetRequestIpWhitelistRecognizers] = None,
        lang: str = None,
        region_id: str = None,
        role_for: int = None,
    ):
        self.data_set_description = data_set_description
        self.data_set_file_name = data_set_file_name
        # This parameter is required.
        self.data_set_id = data_set_id
        self.data_set_name = data_set_name
        self.data_set_status = data_set_status
        self.ip_whitelist_recognizers = ip_whitelist_recognizers
        self.lang = lang
        self.region_id = region_id
        self.role_for = role_for

    def validate(self):
        if self.ip_whitelist_recognizers:
            for k in self.ip_whitelist_recognizers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_set_description is not None:
            result['DataSetDescription'] = self.data_set_description
        if self.data_set_file_name is not None:
            result['DataSetFileName'] = self.data_set_file_name
        if self.data_set_id is not None:
            result['DataSetId'] = self.data_set_id
        if self.data_set_name is not None:
            result['DataSetName'] = self.data_set_name
        if self.data_set_status is not None:
            result['DataSetStatus'] = self.data_set_status
        result['IpWhitelistRecognizers'] = []
        if self.ip_whitelist_recognizers is not None:
            for k in self.ip_whitelist_recognizers:
                result['IpWhitelistRecognizers'].append(k.to_map() if k else None)
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.role_for is not None:
            result['RoleFor'] = self.role_for
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSetDescription') is not None:
            self.data_set_description = m.get('DataSetDescription')
        if m.get('DataSetFileName') is not None:
            self.data_set_file_name = m.get('DataSetFileName')
        if m.get('DataSetId') is not None:
            self.data_set_id = m.get('DataSetId')
        if m.get('DataSetName') is not None:
            self.data_set_name = m.get('DataSetName')
        if m.get('DataSetStatus') is not None:
            self.data_set_status = m.get('DataSetStatus')
        self.ip_whitelist_recognizers = []
        if m.get('IpWhitelistRecognizers') is not None:
            for k in m.get('IpWhitelistRecognizers'):
                temp_model = UpdateDataSetRequestIpWhitelistRecognizers()
                self.ip_whitelist_recognizers.append(temp_model.from_map(k))
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')
        return self


class UpdateDataSetResponseBody(TeaModel):
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


class UpdateDataSetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateDataSetResponseBody = None,
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
            temp_model = UpdateDataSetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDataSetRecordRequest(TeaModel):
    def __init__(
        self,
        data_set_file_name: str = None,
        data_set_id: str = None,
        data_set_records: str = None,
        lang: str = None,
        region_id: str = None,
        role_for: int = None,
    ):
        self.data_set_file_name = data_set_file_name
        # This parameter is required.
        self.data_set_id = data_set_id
        self.data_set_records = data_set_records
        self.lang = lang
        self.region_id = region_id
        self.role_for = role_for

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_set_file_name is not None:
            result['DataSetFileName'] = self.data_set_file_name
        if self.data_set_id is not None:
            result['DataSetId'] = self.data_set_id
        if self.data_set_records is not None:
            result['DataSetRecords'] = self.data_set_records
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.role_for is not None:
            result['RoleFor'] = self.role_for
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSetFileName') is not None:
            self.data_set_file_name = m.get('DataSetFileName')
        if m.get('DataSetId') is not None:
            self.data_set_id = m.get('DataSetId')
        if m.get('DataSetRecords') is not None:
            self.data_set_records = m.get('DataSetRecords')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')
        return self


class UpdateDataSetRecordResponseBodyDataSetRecordStatistic(TeaModel):
    def __init__(
        self,
        new_data_set_record_count: int = None,
        update_data_set_record_count: int = None,
    ):
        self.new_data_set_record_count = new_data_set_record_count
        self.update_data_set_record_count = update_data_set_record_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.new_data_set_record_count is not None:
            result['NewDataSetRecordCount'] = self.new_data_set_record_count
        if self.update_data_set_record_count is not None:
            result['UpdateDataSetRecordCount'] = self.update_data_set_record_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NewDataSetRecordCount') is not None:
            self.new_data_set_record_count = m.get('NewDataSetRecordCount')
        if m.get('UpdateDataSetRecordCount') is not None:
            self.update_data_set_record_count = m.get('UpdateDataSetRecordCount')
        return self


class UpdateDataSetRecordResponseBody(TeaModel):
    def __init__(
        self,
        data_set_record_statistic: UpdateDataSetRecordResponseBodyDataSetRecordStatistic = None,
        request_id: str = None,
    ):
        self.data_set_record_statistic = data_set_record_statistic
        self.request_id = request_id

    def validate(self):
        if self.data_set_record_statistic:
            self.data_set_record_statistic.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_set_record_statistic is not None:
            result['DataSetRecordStatistic'] = self.data_set_record_statistic.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSetRecordStatistic') is not None:
            temp_model = UpdateDataSetRecordResponseBodyDataSetRecordStatistic()
            self.data_set_record_statistic = temp_model.from_map(m['DataSetRecordStatistic'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateDataSetRecordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateDataSetRecordResponseBody = None,
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
            temp_model = UpdateDataSetRecordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDataSourceRequestDataSourceStores(TeaModel):
    def __init__(
        self,
        data_source_store_from: str = None,
        data_source_store_id: str = None,
        log_project_name: str = None,
        log_region_id: str = None,
        log_store_name: str = None,
    ):
        self.data_source_store_from = data_source_store_from
        self.data_source_store_id = data_source_store_id
        self.log_project_name = log_project_name
        self.log_region_id = log_region_id
        self.log_store_name = log_store_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_source_store_from is not None:
            result['DataSourceStoreFrom'] = self.data_source_store_from
        if self.data_source_store_id is not None:
            result['DataSourceStoreId'] = self.data_source_store_id
        if self.log_project_name is not None:
            result['LogProjectName'] = self.log_project_name
        if self.log_region_id is not None:
            result['LogRegionId'] = self.log_region_id
        if self.log_store_name is not None:
            result['LogStoreName'] = self.log_store_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSourceStoreFrom') is not None:
            self.data_source_store_from = m.get('DataSourceStoreFrom')
        if m.get('DataSourceStoreId') is not None:
            self.data_source_store_id = m.get('DataSourceStoreId')
        if m.get('LogProjectName') is not None:
            self.log_project_name = m.get('LogProjectName')
        if m.get('LogRegionId') is not None:
            self.log_region_id = m.get('LogRegionId')
        if m.get('LogStoreName') is not None:
            self.log_store_name = m.get('LogStoreName')
        return self


class UpdateDataSourceRequest(TeaModel):
    def __init__(
        self,
        data_source_from: str = None,
        data_source_id: str = None,
        data_source_name: str = None,
        data_source_recognize_enabled: bool = None,
        data_source_stores: List[UpdateDataSourceRequestDataSourceStores] = None,
        lang: str = None,
        log_project_name: str = None,
        log_region_id: str = None,
        log_store_name: str = None,
        log_user_id: int = None,
        order_field: str = None,
        region_id: str = None,
        role_for: int = None,
    ):
        self.data_source_from = data_source_from
        self.data_source_id = data_source_id
        self.data_source_name = data_source_name
        self.data_source_recognize_enabled = data_source_recognize_enabled
        self.data_source_stores = data_source_stores
        self.lang = lang
        self.log_project_name = log_project_name
        self.log_region_id = log_region_id
        self.log_store_name = log_store_name
        self.log_user_id = log_user_id
        self.order_field = order_field
        self.region_id = region_id
        self.role_for = role_for

    def validate(self):
        if self.data_source_stores:
            for k in self.data_source_stores:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_source_from is not None:
            result['DataSourceFrom'] = self.data_source_from
        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id
        if self.data_source_name is not None:
            result['DataSourceName'] = self.data_source_name
        if self.data_source_recognize_enabled is not None:
            result['DataSourceRecognizeEnabled'] = self.data_source_recognize_enabled
        result['DataSourceStores'] = []
        if self.data_source_stores is not None:
            for k in self.data_source_stores:
                result['DataSourceStores'].append(k.to_map() if k else None)
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.log_project_name is not None:
            result['LogProjectName'] = self.log_project_name
        if self.log_region_id is not None:
            result['LogRegionId'] = self.log_region_id
        if self.log_store_name is not None:
            result['LogStoreName'] = self.log_store_name
        if self.log_user_id is not None:
            result['LogUserId'] = self.log_user_id
        if self.order_field is not None:
            result['OrderField'] = self.order_field
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.role_for is not None:
            result['RoleFor'] = self.role_for
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSourceFrom') is not None:
            self.data_source_from = m.get('DataSourceFrom')
        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')
        if m.get('DataSourceName') is not None:
            self.data_source_name = m.get('DataSourceName')
        if m.get('DataSourceRecognizeEnabled') is not None:
            self.data_source_recognize_enabled = m.get('DataSourceRecognizeEnabled')
        self.data_source_stores = []
        if m.get('DataSourceStores') is not None:
            for k in m.get('DataSourceStores'):
                temp_model = UpdateDataSourceRequestDataSourceStores()
                self.data_source_stores.append(temp_model.from_map(k))
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('LogProjectName') is not None:
            self.log_project_name = m.get('LogProjectName')
        if m.get('LogRegionId') is not None:
            self.log_region_id = m.get('LogRegionId')
        if m.get('LogStoreName') is not None:
            self.log_store_name = m.get('LogStoreName')
        if m.get('LogUserId') is not None:
            self.log_user_id = m.get('LogUserId')
        if m.get('OrderField') is not None:
            self.order_field = m.get('OrderField')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')
        return self


class UpdateDataSourceResponseBody(TeaModel):
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


class UpdateDataSourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateDataSourceResponseBody = None,
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
            temp_model = UpdateDataSourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDataSourceTemplateRequest(TeaModel):
    def __init__(
        self,
        auto_scan_new: str = None,
        data_source_recognize_enabled: bool = None,
        data_source_template_id: str = None,
        data_source_template_name: str = None,
        lang: str = None,
        log_project_pattern: str = None,
        log_region_ids: str = None,
        log_store_pattern: str = None,
        log_user_ids: List[str] = None,
        region_id: str = None,
        role_for: int = None,
    ):
        self.auto_scan_new = auto_scan_new
        self.data_source_recognize_enabled = data_source_recognize_enabled
        self.data_source_template_id = data_source_template_id
        self.data_source_template_name = data_source_template_name
        self.lang = lang
        self.log_project_pattern = log_project_pattern
        self.log_region_ids = log_region_ids
        self.log_store_pattern = log_store_pattern
        self.log_user_ids = log_user_ids
        self.region_id = region_id
        self.role_for = role_for

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_scan_new is not None:
            result['AutoScanNew'] = self.auto_scan_new
        if self.data_source_recognize_enabled is not None:
            result['DataSourceRecognizeEnabled'] = self.data_source_recognize_enabled
        if self.data_source_template_id is not None:
            result['DataSourceTemplateId'] = self.data_source_template_id
        if self.data_source_template_name is not None:
            result['DataSourceTemplateName'] = self.data_source_template_name
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.log_project_pattern is not None:
            result['LogProjectPattern'] = self.log_project_pattern
        if self.log_region_ids is not None:
            result['LogRegionIds'] = self.log_region_ids
        if self.log_store_pattern is not None:
            result['LogStorePattern'] = self.log_store_pattern
        if self.log_user_ids is not None:
            result['LogUserIds'] = self.log_user_ids
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.role_for is not None:
            result['RoleFor'] = self.role_for
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoScanNew') is not None:
            self.auto_scan_new = m.get('AutoScanNew')
        if m.get('DataSourceRecognizeEnabled') is not None:
            self.data_source_recognize_enabled = m.get('DataSourceRecognizeEnabled')
        if m.get('DataSourceTemplateId') is not None:
            self.data_source_template_id = m.get('DataSourceTemplateId')
        if m.get('DataSourceTemplateName') is not None:
            self.data_source_template_name = m.get('DataSourceTemplateName')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('LogProjectPattern') is not None:
            self.log_project_pattern = m.get('LogProjectPattern')
        if m.get('LogRegionIds') is not None:
            self.log_region_ids = m.get('LogRegionIds')
        if m.get('LogStorePattern') is not None:
            self.log_store_pattern = m.get('LogStorePattern')
        if m.get('LogUserIds') is not None:
            self.log_user_ids = m.get('LogUserIds')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')
        return self


class UpdateDataSourceTemplateShrinkRequest(TeaModel):
    def __init__(
        self,
        auto_scan_new: str = None,
        data_source_recognize_enabled: bool = None,
        data_source_template_id: str = None,
        data_source_template_name: str = None,
        lang: str = None,
        log_project_pattern: str = None,
        log_region_ids: str = None,
        log_store_pattern: str = None,
        log_user_ids_shrink: str = None,
        region_id: str = None,
        role_for: int = None,
    ):
        self.auto_scan_new = auto_scan_new
        self.data_source_recognize_enabled = data_source_recognize_enabled
        self.data_source_template_id = data_source_template_id
        self.data_source_template_name = data_source_template_name
        self.lang = lang
        self.log_project_pattern = log_project_pattern
        self.log_region_ids = log_region_ids
        self.log_store_pattern = log_store_pattern
        self.log_user_ids_shrink = log_user_ids_shrink
        self.region_id = region_id
        self.role_for = role_for

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_scan_new is not None:
            result['AutoScanNew'] = self.auto_scan_new
        if self.data_source_recognize_enabled is not None:
            result['DataSourceRecognizeEnabled'] = self.data_source_recognize_enabled
        if self.data_source_template_id is not None:
            result['DataSourceTemplateId'] = self.data_source_template_id
        if self.data_source_template_name is not None:
            result['DataSourceTemplateName'] = self.data_source_template_name
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.log_project_pattern is not None:
            result['LogProjectPattern'] = self.log_project_pattern
        if self.log_region_ids is not None:
            result['LogRegionIds'] = self.log_region_ids
        if self.log_store_pattern is not None:
            result['LogStorePattern'] = self.log_store_pattern
        if self.log_user_ids_shrink is not None:
            result['LogUserIds'] = self.log_user_ids_shrink
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.role_for is not None:
            result['RoleFor'] = self.role_for
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoScanNew') is not None:
            self.auto_scan_new = m.get('AutoScanNew')
        if m.get('DataSourceRecognizeEnabled') is not None:
            self.data_source_recognize_enabled = m.get('DataSourceRecognizeEnabled')
        if m.get('DataSourceTemplateId') is not None:
            self.data_source_template_id = m.get('DataSourceTemplateId')
        if m.get('DataSourceTemplateName') is not None:
            self.data_source_template_name = m.get('DataSourceTemplateName')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('LogProjectPattern') is not None:
            self.log_project_pattern = m.get('LogProjectPattern')
        if m.get('LogRegionIds') is not None:
            self.log_region_ids = m.get('LogRegionIds')
        if m.get('LogStorePattern') is not None:
            self.log_store_pattern = m.get('LogStorePattern')
        if m.get('LogUserIds') is not None:
            self.log_user_ids_shrink = m.get('LogUserIds')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')
        return self


class UpdateDataSourceTemplateResponseBody(TeaModel):
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


class UpdateDataSourceTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateDataSourceTemplateResponseBody = None,
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
            temp_model = UpdateDataSourceTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDataStorageRequest(TeaModel):
    def __init__(
        self,
        data_storage_region_id: str = None,
        delivery_status: str = None,
        lang: str = None,
        region_id: str = None,
        role_for: int = None,
    ):
        # This parameter is required.
        self.data_storage_region_id = data_storage_region_id
        self.delivery_status = delivery_status
        self.lang = lang
        self.region_id = region_id
        self.role_for = role_for

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_storage_region_id is not None:
            result['DataStorageRegionId'] = self.data_storage_region_id
        if self.delivery_status is not None:
            result['DeliveryStatus'] = self.delivery_status
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.role_for is not None:
            result['RoleFor'] = self.role_for
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataStorageRegionId') is not None:
            self.data_storage_region_id = m.get('DataStorageRegionId')
        if m.get('DeliveryStatus') is not None:
            self.delivery_status = m.get('DeliveryStatus')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')
        return self


class UpdateDataStorageResponseBody(TeaModel):
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


class UpdateDataStorageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateDataStorageResponseBody = None,
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
            temp_model = UpdateDataStorageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDataStorageDeliveryRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        log_code: str = None,
        log_delivery_status: str = None,
        region_id: str = None,
        role_for: int = None,
    ):
        self.lang = lang
        # This parameter is required.
        self.log_code = log_code
        self.log_delivery_status = log_delivery_status
        self.region_id = region_id
        self.role_for = role_for

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.log_code is not None:
            result['LogCode'] = self.log_code
        if self.log_delivery_status is not None:
            result['LogDeliveryStatus'] = self.log_delivery_status
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.role_for is not None:
            result['RoleFor'] = self.role_for
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('LogCode') is not None:
            self.log_code = m.get('LogCode')
        if m.get('LogDeliveryStatus') is not None:
            self.log_delivery_status = m.get('LogDeliveryStatus')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')
        return self


class UpdateDataStorageDeliveryResponseBody(TeaModel):
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


class UpdateDataStorageDeliveryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateDataStorageDeliveryResponseBody = None,
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
            temp_model = UpdateDataStorageDeliveryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDataStorageTtlRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        log_store_cold_ttl: str = None,
        log_store_hot_ttl: str = None,
        log_store_name: str = None,
        log_store_ttl: str = None,
        region_id: str = None,
        role_for: int = None,
    ):
        self.lang = lang
        self.log_store_cold_ttl = log_store_cold_ttl
        self.log_store_hot_ttl = log_store_hot_ttl
        self.log_store_name = log_store_name
        self.log_store_ttl = log_store_ttl
        self.region_id = region_id
        self.role_for = role_for

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.log_store_cold_ttl is not None:
            result['LogStoreColdTtl'] = self.log_store_cold_ttl
        if self.log_store_hot_ttl is not None:
            result['LogStoreHotTtl'] = self.log_store_hot_ttl
        if self.log_store_name is not None:
            result['LogStoreName'] = self.log_store_name
        if self.log_store_ttl is not None:
            result['LogStoreTtl'] = self.log_store_ttl
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.role_for is not None:
            result['RoleFor'] = self.role_for
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('LogStoreColdTtl') is not None:
            self.log_store_cold_ttl = m.get('LogStoreColdTtl')
        if m.get('LogStoreHotTtl') is not None:
            self.log_store_hot_ttl = m.get('LogStoreHotTtl')
        if m.get('LogStoreName') is not None:
            self.log_store_name = m.get('LogStoreName')
        if m.get('LogStoreTtl') is not None:
            self.log_store_ttl = m.get('LogStoreTtl')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')
        return self


class UpdateDataStorageTtlResponseBody(TeaModel):
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


class UpdateDataStorageTtlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateDataStorageTtlResponseBody = None,
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
            temp_model = UpdateDataStorageTtlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDetectionRuleRequest(TeaModel):
    def __init__(
        self,
        alert_att_ck: str = None,
        alert_level: str = None,
        alert_schema_id: str = None,
        alert_tactic_id: str = None,
        alert_threshold_count: int = None,
        alert_threshold_group: str = None,
        alert_threshold_period: str = None,
        alert_type: str = None,
        detection_expression_content: str = None,
        detection_expression_type: str = None,
        detection_rule_description: str = None,
        detection_rule_id: str = None,
        detection_rule_name: str = None,
        detection_rule_status: str = None,
        detection_rule_type: str = None,
        entity_mappings: str = None,
        incident_aggregation_expression: str = None,
        incident_aggregation_type: str = None,
        lang: str = None,
        log_category_id: str = None,
        log_schema_id: str = None,
        playbook_parameters: str = None,
        playbook_uuid: str = None,
        region_id: str = None,
        schedule_begin_time: int = None,
        schedule_expression: str = None,
        schedule_max_retries: int = None,
        schedule_max_timeout: int = None,
        schedule_type: str = None,
        schedule_window: str = None,
    ):
        self.alert_att_ck = alert_att_ck
        self.alert_level = alert_level
        self.alert_schema_id = alert_schema_id
        self.alert_tactic_id = alert_tactic_id
        self.alert_threshold_count = alert_threshold_count
        self.alert_threshold_group = alert_threshold_group
        self.alert_threshold_period = alert_threshold_period
        self.alert_type = alert_type
        self.detection_expression_content = detection_expression_content
        self.detection_expression_type = detection_expression_type
        self.detection_rule_description = detection_rule_description
        # This parameter is required.
        self.detection_rule_id = detection_rule_id
        self.detection_rule_name = detection_rule_name
        self.detection_rule_status = detection_rule_status
        # This parameter is required.
        self.detection_rule_type = detection_rule_type
        self.entity_mappings = entity_mappings
        self.incident_aggregation_expression = incident_aggregation_expression
        self.incident_aggregation_type = incident_aggregation_type
        self.lang = lang
        self.log_category_id = log_category_id
        self.log_schema_id = log_schema_id
        self.playbook_parameters = playbook_parameters
        self.playbook_uuid = playbook_uuid
        self.region_id = region_id
        self.schedule_begin_time = schedule_begin_time
        self.schedule_expression = schedule_expression
        self.schedule_max_retries = schedule_max_retries
        self.schedule_max_timeout = schedule_max_timeout
        self.schedule_type = schedule_type
        self.schedule_window = schedule_window

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_att_ck is not None:
            result['AlertAttCk'] = self.alert_att_ck
        if self.alert_level is not None:
            result['AlertLevel'] = self.alert_level
        if self.alert_schema_id is not None:
            result['AlertSchemaId'] = self.alert_schema_id
        if self.alert_tactic_id is not None:
            result['AlertTacticId'] = self.alert_tactic_id
        if self.alert_threshold_count is not None:
            result['AlertThresholdCount'] = self.alert_threshold_count
        if self.alert_threshold_group is not None:
            result['AlertThresholdGroup'] = self.alert_threshold_group
        if self.alert_threshold_period is not None:
            result['AlertThresholdPeriod'] = self.alert_threshold_period
        if self.alert_type is not None:
            result['AlertType'] = self.alert_type
        if self.detection_expression_content is not None:
            result['DetectionExpressionContent'] = self.detection_expression_content
        if self.detection_expression_type is not None:
            result['DetectionExpressionType'] = self.detection_expression_type
        if self.detection_rule_description is not None:
            result['DetectionRuleDescription'] = self.detection_rule_description
        if self.detection_rule_id is not None:
            result['DetectionRuleId'] = self.detection_rule_id
        if self.detection_rule_name is not None:
            result['DetectionRuleName'] = self.detection_rule_name
        if self.detection_rule_status is not None:
            result['DetectionRuleStatus'] = self.detection_rule_status
        if self.detection_rule_type is not None:
            result['DetectionRuleType'] = self.detection_rule_type
        if self.entity_mappings is not None:
            result['EntityMappings'] = self.entity_mappings
        if self.incident_aggregation_expression is not None:
            result['IncidentAggregationExpression'] = self.incident_aggregation_expression
        if self.incident_aggregation_type is not None:
            result['IncidentAggregationType'] = self.incident_aggregation_type
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.log_category_id is not None:
            result['LogCategoryId'] = self.log_category_id
        if self.log_schema_id is not None:
            result['LogSchemaId'] = self.log_schema_id
        if self.playbook_parameters is not None:
            result['PlaybookParameters'] = self.playbook_parameters
        if self.playbook_uuid is not None:
            result['PlaybookUuid'] = self.playbook_uuid
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.schedule_begin_time is not None:
            result['ScheduleBeginTime'] = self.schedule_begin_time
        if self.schedule_expression is not None:
            result['ScheduleExpression'] = self.schedule_expression
        if self.schedule_max_retries is not None:
            result['ScheduleMaxRetries'] = self.schedule_max_retries
        if self.schedule_max_timeout is not None:
            result['ScheduleMaxTimeout'] = self.schedule_max_timeout
        if self.schedule_type is not None:
            result['ScheduleType'] = self.schedule_type
        if self.schedule_window is not None:
            result['ScheduleWindow'] = self.schedule_window
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertAttCk') is not None:
            self.alert_att_ck = m.get('AlertAttCk')
        if m.get('AlertLevel') is not None:
            self.alert_level = m.get('AlertLevel')
        if m.get('AlertSchemaId') is not None:
            self.alert_schema_id = m.get('AlertSchemaId')
        if m.get('AlertTacticId') is not None:
            self.alert_tactic_id = m.get('AlertTacticId')
        if m.get('AlertThresholdCount') is not None:
            self.alert_threshold_count = m.get('AlertThresholdCount')
        if m.get('AlertThresholdGroup') is not None:
            self.alert_threshold_group = m.get('AlertThresholdGroup')
        if m.get('AlertThresholdPeriod') is not None:
            self.alert_threshold_period = m.get('AlertThresholdPeriod')
        if m.get('AlertType') is not None:
            self.alert_type = m.get('AlertType')
        if m.get('DetectionExpressionContent') is not None:
            self.detection_expression_content = m.get('DetectionExpressionContent')
        if m.get('DetectionExpressionType') is not None:
            self.detection_expression_type = m.get('DetectionExpressionType')
        if m.get('DetectionRuleDescription') is not None:
            self.detection_rule_description = m.get('DetectionRuleDescription')
        if m.get('DetectionRuleId') is not None:
            self.detection_rule_id = m.get('DetectionRuleId')
        if m.get('DetectionRuleName') is not None:
            self.detection_rule_name = m.get('DetectionRuleName')
        if m.get('DetectionRuleStatus') is not None:
            self.detection_rule_status = m.get('DetectionRuleStatus')
        if m.get('DetectionRuleType') is not None:
            self.detection_rule_type = m.get('DetectionRuleType')
        if m.get('EntityMappings') is not None:
            self.entity_mappings = m.get('EntityMappings')
        if m.get('IncidentAggregationExpression') is not None:
            self.incident_aggregation_expression = m.get('IncidentAggregationExpression')
        if m.get('IncidentAggregationType') is not None:
            self.incident_aggregation_type = m.get('IncidentAggregationType')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('LogCategoryId') is not None:
            self.log_category_id = m.get('LogCategoryId')
        if m.get('LogSchemaId') is not None:
            self.log_schema_id = m.get('LogSchemaId')
        if m.get('PlaybookParameters') is not None:
            self.playbook_parameters = m.get('PlaybookParameters')
        if m.get('PlaybookUuid') is not None:
            self.playbook_uuid = m.get('PlaybookUuid')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ScheduleBeginTime') is not None:
            self.schedule_begin_time = m.get('ScheduleBeginTime')
        if m.get('ScheduleExpression') is not None:
            self.schedule_expression = m.get('ScheduleExpression')
        if m.get('ScheduleMaxRetries') is not None:
            self.schedule_max_retries = m.get('ScheduleMaxRetries')
        if m.get('ScheduleMaxTimeout') is not None:
            self.schedule_max_timeout = m.get('ScheduleMaxTimeout')
        if m.get('ScheduleType') is not None:
            self.schedule_type = m.get('ScheduleType')
        if m.get('ScheduleWindow') is not None:
            self.schedule_window = m.get('ScheduleWindow')
        return self


class UpdateDetectionRuleResponseBody(TeaModel):
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


class UpdateDetectionRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateDetectionRuleResponseBody = None,
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
            temp_model = UpdateDetectionRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateNormalizationRuleRequest(TeaModel):
    def __init__(
        self,
        extend_content_packed: str = None,
        lang: str = None,
        normalization_rule_description: str = None,
        normalization_rule_expression: str = None,
        normalization_rule_format: str = None,
        normalization_rule_id: str = None,
        normalization_rule_ids: List[str] = None,
        normalization_rule_mode: str = None,
        normalization_rule_name: str = None,
        normalization_rule_type: str = None,
        normalization_schema_id: str = None,
        order_field: str = None,
        product_id: str = None,
        region_id: str = None,
        role_for: int = None,
        vendor_id: str = None,
    ):
        self.extend_content_packed = extend_content_packed
        self.lang = lang
        self.normalization_rule_description = normalization_rule_description
        self.normalization_rule_expression = normalization_rule_expression
        self.normalization_rule_format = normalization_rule_format
        self.normalization_rule_id = normalization_rule_id
        self.normalization_rule_ids = normalization_rule_ids
        self.normalization_rule_mode = normalization_rule_mode
        self.normalization_rule_name = normalization_rule_name
        self.normalization_rule_type = normalization_rule_type
        self.normalization_schema_id = normalization_schema_id
        self.order_field = order_field
        self.product_id = product_id
        self.region_id = region_id
        self.role_for = role_for
        self.vendor_id = vendor_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extend_content_packed is not None:
            result['ExtendContentPacked'] = self.extend_content_packed
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.normalization_rule_description is not None:
            result['NormalizationRuleDescription'] = self.normalization_rule_description
        if self.normalization_rule_expression is not None:
            result['NormalizationRuleExpression'] = self.normalization_rule_expression
        if self.normalization_rule_format is not None:
            result['NormalizationRuleFormat'] = self.normalization_rule_format
        if self.normalization_rule_id is not None:
            result['NormalizationRuleId'] = self.normalization_rule_id
        if self.normalization_rule_ids is not None:
            result['NormalizationRuleIds'] = self.normalization_rule_ids
        if self.normalization_rule_mode is not None:
            result['NormalizationRuleMode'] = self.normalization_rule_mode
        if self.normalization_rule_name is not None:
            result['NormalizationRuleName'] = self.normalization_rule_name
        if self.normalization_rule_type is not None:
            result['NormalizationRuleType'] = self.normalization_rule_type
        if self.normalization_schema_id is not None:
            result['NormalizationSchemaId'] = self.normalization_schema_id
        if self.order_field is not None:
            result['OrderField'] = self.order_field
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.role_for is not None:
            result['RoleFor'] = self.role_for
        if self.vendor_id is not None:
            result['VendorId'] = self.vendor_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExtendContentPacked') is not None:
            self.extend_content_packed = m.get('ExtendContentPacked')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('NormalizationRuleDescription') is not None:
            self.normalization_rule_description = m.get('NormalizationRuleDescription')
        if m.get('NormalizationRuleExpression') is not None:
            self.normalization_rule_expression = m.get('NormalizationRuleExpression')
        if m.get('NormalizationRuleFormat') is not None:
            self.normalization_rule_format = m.get('NormalizationRuleFormat')
        if m.get('NormalizationRuleId') is not None:
            self.normalization_rule_id = m.get('NormalizationRuleId')
        if m.get('NormalizationRuleIds') is not None:
            self.normalization_rule_ids = m.get('NormalizationRuleIds')
        if m.get('NormalizationRuleMode') is not None:
            self.normalization_rule_mode = m.get('NormalizationRuleMode')
        if m.get('NormalizationRuleName') is not None:
            self.normalization_rule_name = m.get('NormalizationRuleName')
        if m.get('NormalizationRuleType') is not None:
            self.normalization_rule_type = m.get('NormalizationRuleType')
        if m.get('NormalizationSchemaId') is not None:
            self.normalization_schema_id = m.get('NormalizationSchemaId')
        if m.get('OrderField') is not None:
            self.order_field = m.get('OrderField')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')
        if m.get('VendorId') is not None:
            self.vendor_id = m.get('VendorId')
        return self


class UpdateNormalizationRuleShrinkRequest(TeaModel):
    def __init__(
        self,
        extend_content_packed: str = None,
        lang: str = None,
        normalization_rule_description: str = None,
        normalization_rule_expression: str = None,
        normalization_rule_format: str = None,
        normalization_rule_id: str = None,
        normalization_rule_ids_shrink: str = None,
        normalization_rule_mode: str = None,
        normalization_rule_name: str = None,
        normalization_rule_type: str = None,
        normalization_schema_id: str = None,
        order_field: str = None,
        product_id: str = None,
        region_id: str = None,
        role_for: int = None,
        vendor_id: str = None,
    ):
        self.extend_content_packed = extend_content_packed
        self.lang = lang
        self.normalization_rule_description = normalization_rule_description
        self.normalization_rule_expression = normalization_rule_expression
        self.normalization_rule_format = normalization_rule_format
        self.normalization_rule_id = normalization_rule_id
        self.normalization_rule_ids_shrink = normalization_rule_ids_shrink
        self.normalization_rule_mode = normalization_rule_mode
        self.normalization_rule_name = normalization_rule_name
        self.normalization_rule_type = normalization_rule_type
        self.normalization_schema_id = normalization_schema_id
        self.order_field = order_field
        self.product_id = product_id
        self.region_id = region_id
        self.role_for = role_for
        self.vendor_id = vendor_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extend_content_packed is not None:
            result['ExtendContentPacked'] = self.extend_content_packed
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.normalization_rule_description is not None:
            result['NormalizationRuleDescription'] = self.normalization_rule_description
        if self.normalization_rule_expression is not None:
            result['NormalizationRuleExpression'] = self.normalization_rule_expression
        if self.normalization_rule_format is not None:
            result['NormalizationRuleFormat'] = self.normalization_rule_format
        if self.normalization_rule_id is not None:
            result['NormalizationRuleId'] = self.normalization_rule_id
        if self.normalization_rule_ids_shrink is not None:
            result['NormalizationRuleIds'] = self.normalization_rule_ids_shrink
        if self.normalization_rule_mode is not None:
            result['NormalizationRuleMode'] = self.normalization_rule_mode
        if self.normalization_rule_name is not None:
            result['NormalizationRuleName'] = self.normalization_rule_name
        if self.normalization_rule_type is not None:
            result['NormalizationRuleType'] = self.normalization_rule_type
        if self.normalization_schema_id is not None:
            result['NormalizationSchemaId'] = self.normalization_schema_id
        if self.order_field is not None:
            result['OrderField'] = self.order_field
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.role_for is not None:
            result['RoleFor'] = self.role_for
        if self.vendor_id is not None:
            result['VendorId'] = self.vendor_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExtendContentPacked') is not None:
            self.extend_content_packed = m.get('ExtendContentPacked')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('NormalizationRuleDescription') is not None:
            self.normalization_rule_description = m.get('NormalizationRuleDescription')
        if m.get('NormalizationRuleExpression') is not None:
            self.normalization_rule_expression = m.get('NormalizationRuleExpression')
        if m.get('NormalizationRuleFormat') is not None:
            self.normalization_rule_format = m.get('NormalizationRuleFormat')
        if m.get('NormalizationRuleId') is not None:
            self.normalization_rule_id = m.get('NormalizationRuleId')
        if m.get('NormalizationRuleIds') is not None:
            self.normalization_rule_ids_shrink = m.get('NormalizationRuleIds')
        if m.get('NormalizationRuleMode') is not None:
            self.normalization_rule_mode = m.get('NormalizationRuleMode')
        if m.get('NormalizationRuleName') is not None:
            self.normalization_rule_name = m.get('NormalizationRuleName')
        if m.get('NormalizationRuleType') is not None:
            self.normalization_rule_type = m.get('NormalizationRuleType')
        if m.get('NormalizationSchemaId') is not None:
            self.normalization_schema_id = m.get('NormalizationSchemaId')
        if m.get('OrderField') is not None:
            self.order_field = m.get('OrderField')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')
        if m.get('VendorId') is not None:
            self.vendor_id = m.get('VendorId')
        return self


class UpdateNormalizationRuleResponseBody(TeaModel):
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


class UpdateNormalizationRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateNormalizationRuleResponseBody = None,
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
            temp_model = UpdateNormalizationRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateProductRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        product_id: str = None,
        product_name: str = None,
        region_id: str = None,
        role_for: int = None,
        vendor_name: str = None,
    ):
        self.lang = lang
        self.product_id = product_id
        self.product_name = product_name
        self.region_id = region_id
        self.role_for = role_for
        self.vendor_name = vendor_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.product_name is not None:
            result['ProductName'] = self.product_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.role_for is not None:
            result['RoleFor'] = self.role_for
        if self.vendor_name is not None:
            result['VendorName'] = self.vendor_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')
        if m.get('VendorName') is not None:
            self.vendor_name = m.get('VendorName')
        return self


class UpdateProductResponseBody(TeaModel):
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


class UpdateProductResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateProductResponseBody = None,
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
            temp_model = UpdateProductResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateVendorRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        region_id: str = None,
        role_for: int = None,
        vendor_id: str = None,
        vendor_name: str = None,
    ):
        self.lang = lang
        self.region_id = region_id
        self.role_for = role_for
        self.vendor_id = vendor_id
        self.vendor_name = vendor_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.role_for is not None:
            result['RoleFor'] = self.role_for
        if self.vendor_id is not None:
            result['VendorId'] = self.vendor_id
        if self.vendor_name is not None:
            result['VendorName'] = self.vendor_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')
        if m.get('VendorId') is not None:
            self.vendor_id = m.get('VendorId')
        if m.get('VendorName') is not None:
            self.vendor_name = m.get('VendorName')
        return self


class UpdateVendorResponseBody(TeaModel):
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


class UpdateVendorResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateVendorResponseBody = None,
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
            temp_model = UpdateVendorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ValidateLogStoreRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        log_project_name: str = None,
        log_region_id: str = None,
        log_store_name: str = None,
        log_user_id: int = None,
        region_id: str = None,
        role_for: int = None,
    ):
        self.lang = lang
        self.log_project_name = log_project_name
        self.log_region_id = log_region_id
        self.log_store_name = log_store_name
        self.log_user_id = log_user_id
        self.region_id = region_id
        self.role_for = role_for

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.log_project_name is not None:
            result['LogProjectName'] = self.log_project_name
        if self.log_region_id is not None:
            result['LogRegionId'] = self.log_region_id
        if self.log_store_name is not None:
            result['LogStoreName'] = self.log_store_name
        if self.log_user_id is not None:
            result['LogUserId'] = self.log_user_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.role_for is not None:
            result['RoleFor'] = self.role_for
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('LogProjectName') is not None:
            self.log_project_name = m.get('LogProjectName')
        if m.get('LogRegionId') is not None:
            self.log_region_id = m.get('LogRegionId')
        if m.get('LogStoreName') is not None:
            self.log_store_name = m.get('LogStoreName')
        if m.get('LogUserId') is not None:
            self.log_user_id = m.get('LogUserId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')
        return self


class ValidateLogStoreResponseBody(TeaModel):
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


class ValidateLogStoreResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ValidateLogStoreResponseBody = None,
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
            temp_model = ValidateLogStoreResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ValidateNormalizationRuleRequest(TeaModel):
    def __init__(
        self,
        data: str = None,
        lang: str = None,
        normalization_category_id: str = None,
        normalization_schema_id: str = None,
        region_id: str = None,
        role_for: int = None,
    ):
        self.data = data
        self.lang = lang
        self.normalization_category_id = normalization_category_id
        self.normalization_schema_id = normalization_schema_id
        self.region_id = region_id
        self.role_for = role_for

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
        if self.normalization_category_id is not None:
            result['NormalizationCategoryId'] = self.normalization_category_id
        if self.normalization_schema_id is not None:
            result['NormalizationSchemaId'] = self.normalization_schema_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.role_for is not None:
            result['RoleFor'] = self.role_for
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('NormalizationCategoryId') is not None:
            self.normalization_category_id = m.get('NormalizationCategoryId')
        if m.get('NormalizationSchemaId') is not None:
            self.normalization_schema_id = m.get('NormalizationSchemaId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')
        return self


class ValidateNormalizationRuleResponseBodyValidateResult(TeaModel):
    def __init__(
        self,
        field_name: str = None,
        field_value: str = None,
        message: str = None,
        normalization_field_name: str = None,
        normalization_field_required: bool = None,
        result: int = None,
    ):
        self.field_name = field_name
        self.field_value = field_value
        self.message = message
        self.normalization_field_name = normalization_field_name
        self.normalization_field_required = normalization_field_required
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.field_name is not None:
            result['FieldName'] = self.field_name
        if self.field_value is not None:
            result['FieldValue'] = self.field_value
        if self.message is not None:
            result['Message'] = self.message
        if self.normalization_field_name is not None:
            result['NormalizationFieldName'] = self.normalization_field_name
        if self.normalization_field_required is not None:
            result['NormalizationFieldRequired'] = self.normalization_field_required
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FieldName') is not None:
            self.field_name = m.get('FieldName')
        if m.get('FieldValue') is not None:
            self.field_value = m.get('FieldValue')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('NormalizationFieldName') is not None:
            self.normalization_field_name = m.get('NormalizationFieldName')
        if m.get('NormalizationFieldRequired') is not None:
            self.normalization_field_required = m.get('NormalizationFieldRequired')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class ValidateNormalizationRuleResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        validate_result: List[ValidateNormalizationRuleResponseBodyValidateResult] = None,
    ):
        self.request_id = request_id
        self.validate_result = validate_result

    def validate(self):
        if self.validate_result:
            for k in self.validate_result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['ValidateResult'] = []
        if self.validate_result is not None:
            for k in self.validate_result:
                result['ValidateResult'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.validate_result = []
        if m.get('ValidateResult') is not None:
            for k in m.get('ValidateResult'):
                temp_model = ValidateNormalizationRuleResponseBodyValidateResult()
                self.validate_result.append(temp_model.from_map(k))
        return self


class ValidateNormalizationRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ValidateNormalizationRuleResponseBody = None,
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
            temp_model = ValidateNormalizationRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


