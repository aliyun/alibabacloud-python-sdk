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
        # The list of collector IDs.
        self.data_connector_ids_shrink = data_connector_ids_shrink
        # The collector name.
        self.data_connector_name = data_connector_name
        # The collector status. Valid values:
        # - "enabled": enabled.
        # - "disabled" (default): disabled.
        self.data_connector_status = data_connector_status
        # The collector type. Valid values:
        # - oss
        # - s3
        # - kafka
        self.data_connector_type = data_connector_type
        # The destination data source ID. This parameter is required only for synchronization.
        self.dest_data_source_id = dest_data_source_id
        # The language of the response. Valid values:
        # - **zh** (default): Chinese.
        # - **en**: English.
        self.lang = lang
        # The maximum number of results to return when you use the NextToken-based pagination method. Valid values: 1 to 100. Default value: 50.
        self.max_results = max_results
        # The pagination token. You do not need to set this parameter for the first request or if no more results exist. If more results exist, set this parameter to the NextToken value returned by the previous API call.
        self.next_token = next_token
        # The sort field. Currently, only sorting by updateTime is supported. If OrderField is left empty, the default order returned by the database is used.
        self.order_field = order_field
        # The sort order. Valid values:
        # - "asc": ascending order.
        # - "desc" (default): descending order.
        self.order_type = order_type
        # The current page number. Default value: 1.
        self.page_number = page_number
        # The number of records per page. Default value: 1000.
        self.page_size = page_size
        # The region where the threat analysis data management center resides. Specify the management center region based on the region of your assets. Valid values:
        # - cn-hangzhou: The assets reside in the Chinese mainland.
        # - ap-southeast-1: The assets reside outside China.
        self.region_id = region_id
        # The user ID that the administrator switches to when viewing as another member.
        self.role_for = role_for
        # The name of the Simple Log Service (SLS) data import job for the collector.
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

