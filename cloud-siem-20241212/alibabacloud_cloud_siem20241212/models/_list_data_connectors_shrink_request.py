# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListDataConnectorsShrinkRequest(DaraModel):
    def __init__(
        self,
        data_connector_ids_shrink: str = None,
        data_connector_name: str = None,
        data_connector_status: str = None,
        data_connector_type: str = None,
        dest_data_source_id: str = None,
        lang: str = None,
        max_results: int = None,
        next_token: str = None,
        order_field: str = None,
        order_type: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        role_for: int = None,
        sls_ingestion_job_name: str = None,
        src_data_type: str = None,
    ):
        # The list of data connector IDs.
        self.data_connector_ids_shrink = data_connector_ids_shrink
        # The name of the data connector.
        self.data_connector_name = data_connector_name
        # The enabled status of the data connector. Valid values:
        # - "enabled": Enabled.
        # - "disabled" (default): Disabled.
        self.data_connector_status = data_connector_status
        # The type of the data connector. Valid values:
        # - oss
        # - s3
        # - kafka
        self.data_connector_type = data_connector_type
        # The ID of the destination data source. This parameter is required only for synchronization.
        self.dest_data_source_id = dest_data_source_id
        # The language of the response message. Valid values:
        # - **zh** (default): Chinese.
        # - **en**: English.
        # 
        # Note: This parameter is required in actual API calls. If this parameter is not provided, the service returns a 400 error with the message "The specified Lang can not be empty." Explicitly pass the language code.
        self.lang = lang
        # The maximum number of entries to return for a single query when you use the NextToken method. Valid values: 1 to 100. Default value: 50.
        self.max_results = max_results
        # The token used to query the next page. You do not need to specify this parameter for the first query or when no next page exists. If a next page exists, set this parameter to the NextToken value returned by the previous API call.
        self.next_token = next_token
        # The field used for sorting.
        # Currently, only sorting by updateTime is supported.
        # If OrderField is empty, the default order returned by the database is used.
        self.order_field = order_field
        # The sort order. Valid values:
        # - "asc"
        # - "desc" (default)
        self.order_type = order_type
        # The current page number. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Default value: 1000.
        self.page_size = page_size
        # The region where the data management center for threat analysis is located. Select the region of the management center based on the region where your assets are located. Valid values:
        # - cn-hangzhou: The assets are located in the Chinese mainland.
        # - ap-southeast-1: The assets are located outside the Chinese mainland.
        self.region_id = region_id
        # The ID of the user whose perspective the administrator assumes.
        self.role_for = role_for
        # The name of the Simple Log Service (SLS) data import job for the data connector.
        self.sls_ingestion_job_name = sls_ingestion_job_name
        # The source data type.
        self.src_data_type = src_data_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_connector_ids_shrink is not None:
            result['DataConnectorIds'] = self.data_connector_ids_shrink

        if self.data_connector_name is not None:
            result['DataConnectorName'] = self.data_connector_name

        if self.data_connector_status is not None:
            result['DataConnectorStatus'] = self.data_connector_status

        if self.data_connector_type is not None:
            result['DataConnectorType'] = self.data_connector_type

        if self.dest_data_source_id is not None:
            result['DestDataSourceId'] = self.dest_data_source_id

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.order_field is not None:
            result['OrderField'] = self.order_field

        if self.order_type is not None:
            result['OrderType'] = self.order_type

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.role_for is not None:
            result['RoleFor'] = self.role_for

        if self.sls_ingestion_job_name is not None:
            result['SlsIngestionJobName'] = self.sls_ingestion_job_name

        if self.src_data_type is not None:
            result['SrcDataType'] = self.src_data_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataConnectorIds') is not None:
            self.data_connector_ids_shrink = m.get('DataConnectorIds')

        if m.get('DataConnectorName') is not None:
            self.data_connector_name = m.get('DataConnectorName')

        if m.get('DataConnectorStatus') is not None:
            self.data_connector_status = m.get('DataConnectorStatus')

        if m.get('DataConnectorType') is not None:
            self.data_connector_type = m.get('DataConnectorType')

        if m.get('DestDataSourceId') is not None:
            self.dest_data_source_id = m.get('DestDataSourceId')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('OrderField') is not None:
            self.order_field = m.get('OrderField')

        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')

        if m.get('SlsIngestionJobName') is not None:
            self.sls_ingestion_job_name = m.get('SlsIngestionJobName')

        if m.get('SrcDataType') is not None:
            self.src_data_type = m.get('SrcDataType')

        return self

