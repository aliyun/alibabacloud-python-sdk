# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloud_siem20241212 import models as main_models
from darabonba.model import DaraModel

class ListDataConnectorsResponseBody(DaraModel):
    def __init__(
        self,
        data_connector: List[main_models.ListDataConnectorsResponseBodyDataConnector] = None,
        max_results: int = None,
        next_token: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The list of collectors.
        self.data_connector = data_connector
        # The maximum number of records returned in this request.
        self.max_results = max_results
        # The token for the next query.
        self.next_token = next_token
        # The current page number.
        self.page_number = page_number
        # The number of records per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of records.
        self.total_count = total_count

    def validate(self):
        if self.data_connector:
            for v1 in self.data_connector:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DataConnector'] = []
        if self.data_connector is not None:
            for k1 in self.data_connector:
                result['DataConnector'].append(k1.to_map() if k1 else None)

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
        self.data_connector = []
        if m.get('DataConnector') is not None:
            for k1 in m.get('DataConnector'):
                temp_model = main_models.ListDataConnectorsResponseBodyDataConnector()
                self.data_connector.append(temp_model.from_map(k1))

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

class ListDataConnectorsResponseBodyDataConnector(DaraModel):
    def __init__(
        self,
        auth_config_id: str = None,
        auth_config_product: str = None,
        auth_config_vendor: str = None,
        creation_time: int = None,
        data_connector_config: str = None,
        data_connector_id: str = None,
        data_connector_name: str = None,
        data_connector_status: str = None,
        data_connector_type: str = None,
        dest_data_source_id: str = None,
        log_project_name: str = None,
        log_region_id: str = None,
        log_store_name: str = None,
        sls_ingestion_job_name: str = None,
        sls_ingestion_job_state: str = None,
        src_data_type: str = None,
        update_time: int = None,
    ):
        # The configuration item ID of the collector access object in the multi-cloud configuration.
        self.auth_config_id = auth_config_id
        # The cloud product of the authentication configuration.
        self.auth_config_product = auth_config_product
        # The cloud vendor of the authentication configuration.
        self.auth_config_vendor = auth_config_vendor
        # The creation time.
        self.creation_time = creation_time
        # The collector configuration information.
        self.data_connector_config = data_connector_config
        # The collector ID.
        self.data_connector_id = data_connector_id
        # The data connector name.
        self.data_connector_name = data_connector_name
        # The connector status.
        self.data_connector_status = data_connector_status
        # The connector type.
        self.data_connector_type = data_connector_type
        # The destination data source ID. This parameter is required only for synchronization.
        self.dest_data_source_id = dest_data_source_id
        # The Simple Log Service project name.
        self.log_project_name = log_project_name
        # The log storage region ID.
        self.log_region_id = log_region_id
        # The Simple Log Service Logstore name.
        self.log_store_name = log_store_name
        # The name of the SLS data import job associated with the collector.
        self.sls_ingestion_job_name = sls_ingestion_job_name
        # The status of the SLS data import job associated with the collector.
        self.sls_ingestion_job_state = sls_ingestion_job_state
        # The source data type.
        self.src_data_type = src_data_type
        # The update time.
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_config_id is not None:
            result['AuthConfigId'] = self.auth_config_id

        if self.auth_config_product is not None:
            result['AuthConfigProduct'] = self.auth_config_product

        if self.auth_config_vendor is not None:
            result['AuthConfigVendor'] = self.auth_config_vendor

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.data_connector_config is not None:
            result['DataConnectorConfig'] = self.data_connector_config

        if self.data_connector_id is not None:
            result['DataConnectorId'] = self.data_connector_id

        if self.data_connector_name is not None:
            result['DataConnectorName'] = self.data_connector_name

        if self.data_connector_status is not None:
            result['DataConnectorStatus'] = self.data_connector_status

        if self.data_connector_type is not None:
            result['DataConnectorType'] = self.data_connector_type

        if self.dest_data_source_id is not None:
            result['DestDataSourceId'] = self.dest_data_source_id

        if self.log_project_name is not None:
            result['LogProjectName'] = self.log_project_name

        if self.log_region_id is not None:
            result['LogRegionId'] = self.log_region_id

        if self.log_store_name is not None:
            result['LogStoreName'] = self.log_store_name

        if self.sls_ingestion_job_name is not None:
            result['SlsIngestionJobName'] = self.sls_ingestion_job_name

        if self.sls_ingestion_job_state is not None:
            result['SlsIngestionJobState'] = self.sls_ingestion_job_state

        if self.src_data_type is not None:
            result['SrcDataType'] = self.src_data_type

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthConfigId') is not None:
            self.auth_config_id = m.get('AuthConfigId')

        if m.get('AuthConfigProduct') is not None:
            self.auth_config_product = m.get('AuthConfigProduct')

        if m.get('AuthConfigVendor') is not None:
            self.auth_config_vendor = m.get('AuthConfigVendor')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('DataConnectorConfig') is not None:
            self.data_connector_config = m.get('DataConnectorConfig')

        if m.get('DataConnectorId') is not None:
            self.data_connector_id = m.get('DataConnectorId')

        if m.get('DataConnectorName') is not None:
            self.data_connector_name = m.get('DataConnectorName')

        if m.get('DataConnectorStatus') is not None:
            self.data_connector_status = m.get('DataConnectorStatus')

        if m.get('DataConnectorType') is not None:
            self.data_connector_type = m.get('DataConnectorType')

        if m.get('DestDataSourceId') is not None:
            self.dest_data_source_id = m.get('DestDataSourceId')

        if m.get('LogProjectName') is not None:
            self.log_project_name = m.get('LogProjectName')

        if m.get('LogRegionId') is not None:
            self.log_region_id = m.get('LogRegionId')

        if m.get('LogStoreName') is not None:
            self.log_store_name = m.get('LogStoreName')

        if m.get('SlsIngestionJobName') is not None:
            self.sls_ingestion_job_name = m.get('SlsIngestionJobName')

        if m.get('SlsIngestionJobState') is not None:
            self.sls_ingestion_job_state = m.get('SlsIngestionJobState')

        if m.get('SrcDataType') is not None:
            self.src_data_type = m.get('SrcDataType')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

