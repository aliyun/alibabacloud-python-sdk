# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeInstanceSourcesRequest(DaraModel):
    def __init__(
        self,
        audit_status: int = None,
        auth_status: int = None,
        current_page: int = None,
        engine_type: str = None,
        feature_type: int = None,
        instance_id: str = None,
        lang: str = None,
        page_size: int = None,
        product_code: str = None,
        product_id: int = None,
        search_key: str = None,
        search_type: str = None,
        service_region_id: str = None,
    ):
        # Specifies whether to enable the security audit feature. Valid values:
        # 
        # *   **1**: yes
        # *   **0**: no
        self.audit_status = audit_status
        # Specifies whether DSC is authorized to access the data asset.
        # 
        # *   **0**: no
        # *   **1**: yes
        self.auth_status = auth_status
        # The number of the page to return. Default value: **1**.
        self.current_page = current_page
        # The engine type. Valid values:
        # 
        # *   **MySQL**
        # *   **MariaDB**
        # *   **Oracle**
        # *   **PostgreSQL**
        # *   **SQLServer**
        self.engine_type = engine_type
        # This parameter is deprecated.
        self.feature_type = feature_type
        # The ID of the instance.
        self.instance_id = instance_id
        # The language of the content within the request and response. Valid values:
        # 
        # *   **zh_cn**: Simplified Chinese (default)
        # *   **en_us**: English
        self.lang = lang
        # The number of entries to return on each page. Default value: **10**.
        self.page_size = page_size
        # The name of the service to which the data asset to query belongs. Valid values: **MaxCompute, OSS, ADS, OTS, and RDS**.
        self.product_code = product_code
        # The ID of the service to which the asset belongs. Valid values:
        # 
        # *   **1**: MaxCompute
        # *   **2**: Object Storage Service (OSS)
        # *   **3**: AnalyticDB for MySQL
        # *   **4**: Tablestore (OTS)
        # *   **5**: ApsaraDB RDS
        # *   **6**: self-managed databases
        self.product_id = product_id
        # The content based on which a fuzzy search is performed.
        self.search_key = search_key
        # The data asset type based on which a fuzzy search is performed.
        # 
        # *   **InstanceId**: the ID of the instance.
        # *   **InstanceName**: the name of the instance.
        # *   **DatabaseName**: the name of the database.
        self.search_type = search_type
        # The region in which the data asset resides. For more information, see [Supported regions](https://help.aliyun.com/document_detail/214257.html).
        self.service_region_id = service_region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.audit_status is not None:
            result['AuditStatus'] = self.audit_status

        if self.auth_status is not None:
            result['AuthStatus'] = self.auth_status

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.engine_type is not None:
            result['EngineType'] = self.engine_type

        if self.feature_type is not None:
            result['FeatureType'] = self.feature_type

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

        if m.get('FeatureType') is not None:
            self.feature_type = m.get('FeatureType')

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

