# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListDataSourcesRequest(DaraModel):
    def __init__(
        self,
        connect_status: str = None,
        current_page: int = None,
        data_asset_id: str = None,
        data_source_id: str = None,
        db_name: str = None,
        engine_type: str = None,
        identify_status: str = None,
        instance_id: str = None,
        lang: str = None,
        max_results: int = None,
        next_token: str = None,
        page_size: int = None,
        port: int = None,
        product_code: str = None,
        product_id: int = None,
        source_ip: str = None,
    ):
        # The connection status of the data source. Valid values:
        # - UnConnected: Not connected.
        # - Processing: Connecting.
        # - Success: Connected.
        # - Failed: Connection failed.
        self.connect_status = connect_status
        # The current page number. Pages start from 1.
        self.current_page = current_page
        # The identifier of the data asset in Data Security Center.
        self.data_asset_id = data_asset_id
        # The identifier of the data source in Data Security Center. You can obtain the value from the Items[].DataSourceId parameter in the response of the ListDataSources operation.
        self.data_source_id = data_source_id
        # The name of the database.
        self.db_name = db_name
        # The engine type. Valid values:
        # - **MySQL**
        # - **MariaDB**
        # - **Oracle**
        # - **PostgreSQL**
        # - **SQLServer**
        self.engine_type = engine_type
        # The status of the data source detection switch. Valid values:
        # - Enable: Submitted for enabling.
        # - Enabling: Enabling.
        # - Enabled: Enabled.
        # - EnableFailed: Enabling failed.
        # - Disable: Submitted for disabling.
        # - Disabling: Disabling.
        # - Disabled: Disabled.
        # - DisableFailed: Disabling failed.
        self.identify_status = identify_status
        # The database instance identity. You can obtain the value from the Items[].InstanceId parameter in the response of the ListDataMaskingInstances operation.
        self.instance_id = instance_id
        # The language of the response message. Valid values:
        # - zh: Chinese.
        # - en: English.
        self.lang = lang
        # A reserved pagination parameter. The ListDataSources operation uses CurrentPage and PageSize for pagination. Omit this parameter when you call the operation.
        self.max_results = max_results
        # A reserved pagination cursor parameter. The ListDataSources operation uses CurrentPage and PageSize for pagination. Omit this parameter when you call the operation.
        self.next_token = next_token
        # The number of entries to return on each page. Keep other filter conditions consistent when you query the next page.
        self.page_size = page_size
        # The port for the database connection.
        self.port = port
        # The code of the cloud service. Column encryption supports ApsaraDB RDS, PolarDB, and PolarDB-X 2.0. If this parameter is specified together with ProductId, the values must match.
        self.product_code = product_code
        # The identifier of the cloud service type. 5: ApsaraDB RDS; 8: PolarDB; 27: PolarDB-X 2.0. If this parameter is specified together with ProductCode, the values must match.
        self.product_id = product_id
        # The source IP address of the call.
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.connect_status is not None:
            result['ConnectStatus'] = self.connect_status

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.data_asset_id is not None:
            result['DataAssetId'] = self.data_asset_id

        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id

        if self.db_name is not None:
            result['DbName'] = self.db_name

        if self.engine_type is not None:
            result['EngineType'] = self.engine_type

        if self.identify_status is not None:
            result['IdentifyStatus'] = self.identify_status

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.port is not None:
            result['Port'] = self.port

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.product_id is not None:
            result['ProductId'] = self.product_id

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectStatus') is not None:
            self.connect_status = m.get('ConnectStatus')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('DataAssetId') is not None:
            self.data_asset_id = m.get('DataAssetId')

        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')

        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')

        if m.get('EngineType') is not None:
            self.engine_type = m.get('EngineType')

        if m.get('IdentifyStatus') is not None:
            self.identify_status = m.get('IdentifyStatus')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        return self

