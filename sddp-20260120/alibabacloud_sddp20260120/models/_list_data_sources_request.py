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
        identify_status: str = None,
        instance_id: str = None,
        lang: str = None,
        max_results: int = None,
        next_token: str = None,
        page_size: int = None,
        product_code: str = None,
        product_id: int = None,
        source_ip: str = None,
    ):
        self.connect_status = connect_status
        self.current_page = current_page
        self.data_asset_id = data_asset_id
        self.data_source_id = data_source_id
        self.db_name = db_name
        self.identify_status = identify_status
        self.instance_id = instance_id
        self.lang = lang
        self.max_results = max_results
        self.next_token = next_token
        self.page_size = page_size
        self.product_code = product_code
        self.product_id = product_id
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

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        return self

