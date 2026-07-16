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
        # The audit status. Valid values:
        # 
        # - **1**: Auditing is enabled.
        # 
        # - **0**: Auditing is disabled.
        self.audit_status = audit_status
        # The authorization status of the data asset instance.
        # 
        # - **0**: Unauthorized.
        # 
        # - **1**: Authorized.
        self.auth_status = auth_status
        # The page number. Default value: **1**.
        self.current_page = current_page
        # The database engine type. Valid values:
        # 
        # - **MySQL**
        # 
        # - **MariaDB**
        # 
        # - **Oracle**
        # 
        # - **PostgreSQL**
        # 
        # - **SQLServer**
        self.engine_type = engine_type
        # This parameter is deprecated.
        self.feature_type = feature_type
        # The instance ID.
        self.instance_id = instance_id
        # The language of the request and response. Valid values:
        # 
        # - **zh_cn**: Simplified Chinese. This is the default value.
        # 
        # - **en_us**: English.
        self.lang = lang
        # The number of entries per page in a paginated query. Default value: **10**.
        self.page_size = page_size
        # The name of the product to query. Valid values: MaxCompute, OSS, ADS, OTS, and RDS.
        self.product_code = product_code
        # The product type ID to query. Valid values:
        # 
        # - **1**: MaxCompute
        # 
        # - **2**: OSS
        # 
        # - **3**: ADS
        # 
        # - **4**: OTS
        # 
        # - **5**: RDS
        # 
        # - **6**: SELF_DB
        self.product_id = product_id
        # The keyword for the fuzzy search of data assets.
        self.search_key = search_key
        # The type of the fuzzy search for data assets. Valid values:
        # 
        # - **InstanceId**: The instance ID.
        # 
        # - **InstanceName**: The instance name.
        # 
        # - **DatabaseName**: The database name.
        self.search_type = search_type
        # The region where the asset is located. For more information, see [Supported regions](https://help.aliyun.com/document_detail/214257.html).
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

