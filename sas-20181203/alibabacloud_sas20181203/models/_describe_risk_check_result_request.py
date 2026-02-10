# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeRiskCheckResultRequest(DaraModel):
    def __init__(
        self,
        asset_type: str = None,
        current_page: int = None,
        group_id: int = None,
        item_ids: List[str] = None,
        lang: str = None,
        name: str = None,
        page_size: int = None,
        query_flag: str = None,
        resource_owner_id: int = None,
        risk_level: str = None,
        source_ip: str = None,
        status: str = None,
    ):
        # The cloud service whose configuration check results you want to query. For more information about the check items for the cloud service, see the check item table in the "Response parameters" section of this topic.
        self.asset_type = asset_type
        # The number of the page to return. Default value: **1**.
        self.current_page = current_page
        # The type of the check item that you want to query. Valid values:
        # 
        # *   **1**: identity authentication and permissions
        # *   **2**: network access control
        # *   **3**: log audit
        # *   **4**: data security
        # *   **5**: monitoring and alerting
        # *   **6**: basic security protection
        # 
        # > If you do not specify this parameter, all types of check items are queried.
        self.group_id = group_id
        # An array that consists of the IDs of check items. For more information about the check item, see the check item table in the "Response parameters" section of this topic.
        self.item_ids = item_ids
        # The language of the content within the request and response. Default value: **zh**. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        self.lang = lang
        # The name of the check item. For more information about the check item, see the check item table in the "Response parameters" section of this topic.
        self.name = name
        # The number of entries to return on each page. Default value: **20**.
        self.page_size = page_size
        # Specifies whether the check item is supported by the edition of Security Center that you purchase. Valid values:
        # 
        # *   **enabled**: yes
        # *   **disabled**: no
        self.query_flag = query_flag
        self.resource_owner_id = resource_owner_id
        # The risk level of the check item that you want to query. Valid values:
        # 
        # *   **high**
        # *   **medium**
        # *   **low**
        self.risk_level = risk_level
        # The source IP address of the request.
        self.source_ip = source_ip
        # The status of the check results. Valid values:
        # 
        # *   **pass**
        # *   **failed**
        # *   **running**
        # *   **waiting**
        # *   **ignored**
        # *   **falsePositive**
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.asset_type is not None:
            result['AssetType'] = self.asset_type

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.item_ids is not None:
            result['ItemIds'] = self.item_ids

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.name is not None:
            result['Name'] = self.name

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.query_flag is not None:
            result['QueryFlag'] = self.query_flag

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssetType') is not None:
            self.asset_type = m.get('AssetType')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('ItemIds') is not None:
            self.item_ids = m.get('ItemIds')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('QueryFlag') is not None:
            self.query_flag = m.get('QueryFlag')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

