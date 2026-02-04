# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloud_siem20241212 import models as main_models
from darabonba.model import DaraModel

class ListDataSourcesResponseBody(DaraModel):
    def __init__(
        self,
        data_sources: List[main_models.ListDataSourcesResponseBodyDataSources] = None,
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
            for v1 in self.data_sources:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DataSources'] = []
        if self.data_sources is not None:
            for k1 in self.data_sources:
                result['DataSources'].append(k1.to_map() if k1 else None)

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
            for k1 in m.get('DataSources'):
                temp_model = main_models.ListDataSourcesResponseBodyDataSources()
                self.data_sources.append(temp_model.from_map(k1))

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

class ListDataSourcesResponseBodyDataSources(DaraModel):
    def __init__(
        self,
        create_time: int = None,
        data_source_from: str = None,
        data_source_id: str = None,
        data_source_name: str = None,
        data_source_recognize_enabled: bool = None,
        data_source_recognizer: str = None,
        data_source_references: List[main_models.ListDataSourcesResponseBodyDataSourcesDataSourceReferences] = None,
        data_source_status: str = None,
        data_source_stores: List[main_models.ListDataSourcesResponseBodyDataSourcesDataSourceStores] = None,
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
            for v1 in self.data_source_references:
                 if v1:
                    v1.validate()
        if self.data_source_stores:
            for v1 in self.data_source_stores:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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
            for k1 in self.data_source_references:
                result['DataSourceReferences'].append(k1.to_map() if k1 else None)

        if self.data_source_status is not None:
            result['DataSourceStatus'] = self.data_source_status

        result['DataSourceStores'] = []
        if self.data_source_stores is not None:
            for k1 in self.data_source_stores:
                result['DataSourceStores'].append(k1.to_map() if k1 else None)

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
            for k1 in m.get('DataSourceReferences'):
                temp_model = main_models.ListDataSourcesResponseBodyDataSourcesDataSourceReferences()
                self.data_source_references.append(temp_model.from_map(k1))

        if m.get('DataSourceStatus') is not None:
            self.data_source_status = m.get('DataSourceStatus')

        self.data_source_stores = []
        if m.get('DataSourceStores') is not None:
            for k1 in m.get('DataSourceStores'):
                temp_model = main_models.ListDataSourcesResponseBodyDataSourcesDataSourceStores()
                self.data_source_stores.append(temp_model.from_map(k1))

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

class ListDataSourcesResponseBodyDataSourcesDataSourceStores(DaraModel):
    def __init__(
        self,
        check_time: int = None,
        create_time: int = None,
        data_source_store_from: str = None,
        data_source_store_id: str = None,
        data_source_store_status: str = None,
        data_source_store_status_code: str = None,
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
        self.data_source_store_status_code = data_source_store_status_code
        self.log_project_name = log_project_name
        self.log_region_id = log_region_id
        self.log_store_name = log_store_name
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

        if self.data_source_store_status_code is not None:
            result['DataSourceStoreStatusCode'] = self.data_source_store_status_code

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

        if m.get('DataSourceStoreStatusCode') is not None:
            self.data_source_store_status_code = m.get('DataSourceStoreStatusCode')

        if m.get('LogProjectName') is not None:
            self.log_project_name = m.get('LogProjectName')

        if m.get('LogRegionId') is not None:
            self.log_region_id = m.get('LogRegionId')

        if m.get('LogStoreName') is not None:
            self.log_store_name = m.get('LogStoreName')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

class ListDataSourcesResponseBodyDataSourcesDataSourceReferences(DaraModel):
    def __init__(
        self,
        data_ingestion_id: str = None,
    ):
        self.data_ingestion_id = data_ingestion_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_ingestion_id is not None:
            result['DataIngestionId'] = self.data_ingestion_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataIngestionId') is not None:
            self.data_ingestion_id = m.get('DataIngestionId')

        return self

