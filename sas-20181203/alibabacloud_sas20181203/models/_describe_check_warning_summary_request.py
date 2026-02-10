# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeCheckWarningSummaryRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        container_field_name: str = None,
        container_field_value: str = None,
        current_page: int = None,
        group_id: int = None,
        lang: str = None,
        page_size: int = None,
        risk_name: str = None,
        risk_status: int = None,
        source_ip: str = None,
        status: str = None,
        strategy_id: int = None,
        target_type: str = None,
        type_name: str = None,
        uuids: str = None,
    ):
        # The ID of the container cluster.
        # 
        # >  You can call the [DescribeGroupedContainerInstances](~~DescribeGroupedContainerInstances~~) operation to query the IDs of container clusters.
        self.cluster_id = cluster_id
        # The name of the container field. Valid values:
        # 
        # *   **clusterId**: the ID of the cluster
        # *   **image**: the name of the image
        # *   **imageId**: the ID of the image
        # *   **namespace**: the namespace
        self.container_field_name = container_field_name
        # The value of the container field.
        self.container_field_value = container_field_value
        # The number of the page to return.
        self.current_page = current_page
        # The ID of the asset group.
        # 
        # > You can call the [DescribeAllGroups](~~DescribeAllGroups~~) operation to query the IDs of asset groups.
        self.group_id = group_id
        # The language of the content within the request and the response. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        self.lang = lang
        # The number of entries to return on each page.
        self.page_size = page_size
        # The name of the risk item.
        self.risk_name = risk_name
        # The status of the baseline check. Valid values:
        # 
        # *   **1**: failed
        # *   **3**: passed
        self.risk_status = risk_status
        # The source IP address of the request.
        self.source_ip = source_ip
        # The status of the check item. Valid values:
        # 
        # *   **1**: failed
        # *   **2**: verifying
        # *   **3**: passed
        # *   **5**: expired
        # *   **6**: ignored
        self.status = status
        # The ID of the baseline check policy.
        self.strategy_id = strategy_id
        # The type of the query condition. Valid values:
        # 
        # *   **uuid**: the ID of an asset
        self.target_type = target_type
        # The level-1 type of check items.
        # 
        # >  You can call the [DescribeRiskType](~~DescribeRiskType~~) operation to query the level-1 types of check items.
        self.type_name = type_name
        # The UUID of the asset.
        # 
        # >  You can call the [DescribeCloudCenterInstances](~~DescribeCloudCenterInstances~~) operation to query the UUIDs of assets.
        self.uuids = uuids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.container_field_name is not None:
            result['ContainerFieldName'] = self.container_field_name

        if self.container_field_value is not None:
            result['ContainerFieldValue'] = self.container_field_value

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.risk_name is not None:
            result['RiskName'] = self.risk_name

        if self.risk_status is not None:
            result['RiskStatus'] = self.risk_status

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        if self.status is not None:
            result['Status'] = self.status

        if self.strategy_id is not None:
            result['StrategyId'] = self.strategy_id

        if self.target_type is not None:
            result['TargetType'] = self.target_type

        if self.type_name is not None:
            result['TypeName'] = self.type_name

        if self.uuids is not None:
            result['Uuids'] = self.uuids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('ContainerFieldName') is not None:
            self.container_field_name = m.get('ContainerFieldName')

        if m.get('ContainerFieldValue') is not None:
            self.container_field_value = m.get('ContainerFieldValue')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RiskName') is not None:
            self.risk_name = m.get('RiskName')

        if m.get('RiskStatus') is not None:
            self.risk_status = m.get('RiskStatus')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StrategyId') is not None:
            self.strategy_id = m.get('StrategyId')

        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')

        if m.get('TypeName') is not None:
            self.type_name = m.get('TypeName')

        if m.get('Uuids') is not None:
            self.uuids = m.get('Uuids')

        return self

