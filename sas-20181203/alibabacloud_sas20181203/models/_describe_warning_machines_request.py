# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeWarningMachinesRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        container_field_name: str = None,
        container_field_value: str = None,
        current_page: int = None,
        group_id: int = None,
        have_risk: int = None,
        lang: str = None,
        machine_name: str = None,
        page_size: int = None,
        risk_id: int = None,
        source_ip: str = None,
        strategy_id: int = None,
        target_type: str = None,
        uuids: str = None,
    ):
        # The ID of the container cluster.
        # 
        # > You can call the [DescribeGroupedContainerInstances](~~DescribeGroupedContainerInstances~~) operation to query the IDs of container clusters.
        self.cluster_id = cluster_id
        # The name of the field that is used to search for the container. Valid values:
        # 
        # *   **CONTAINER_ID**: the ID of the container
        # *   **IMAGE**: the name of the image
        # *   **NAMESPACE**: the namespace
        # *   **NODE_NAME**: the name of the node
        # *   **POD_IP**: the IP address of the pod
        # *   **HOST_IP**: the IP address of the host
        # *   **INSTANCE_ID**: the ID of the instance
        self.container_field_name = container_field_name
        # The value of the field that is used to search for the container.
        self.container_field_value = container_field_value
        # The number of the page to return. Default value: **1**.
        self.current_page = current_page
        # The ID of the asset group.
        # 
        # > You can call the [DescribeAllGroups](https://help.aliyun.com/document_detail/130972.html) operation to query the IDs of asset groups.
        self.group_id = group_id
        # Specifies whether risks were detected. Valid values:
        # 
        # *   **1**: yes
        # *   **0**: no
        self.have_risk = have_risk
        # The language of the content within the request and response. Default value: **zh**. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        self.lang = lang
        # The name of the server on which the baseline check is performed.
        self.machine_name = machine_name
        # The number of entries per page. Default value: **10**, which indicates that 10 entries of server information are displayed on each page. A maximum of 100 entries can be returned per page.
        self.page_size = page_size
        # The ID of the risk item.
        # 
        # > You can call the [DescribeCheckWarningSummary](~~DescribeCheckWarningSummary~~) operation to query the IDs of risk items.
        # 
        # This parameter is required.
        self.risk_id = risk_id
        # The source IP address of the request.
        self.source_ip = source_ip
        # The ID of the baseline check policy.
        self.strategy_id = strategy_id
        # The type of the query condition. Valid values:
        # 
        # *   **containerId**: the ID of the container
        # *   **uuid**: the UUID of the asset
        self.target_type = target_type
        # The UUID of the server on which the baseline check is performed. Separate multiple UUIDs with commas (,).
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

        if self.have_risk is not None:
            result['HaveRisk'] = self.have_risk

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.machine_name is not None:
            result['MachineName'] = self.machine_name

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.risk_id is not None:
            result['RiskId'] = self.risk_id

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        if self.strategy_id is not None:
            result['StrategyId'] = self.strategy_id

        if self.target_type is not None:
            result['TargetType'] = self.target_type

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

        if m.get('HaveRisk') is not None:
            self.have_risk = m.get('HaveRisk')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('MachineName') is not None:
            self.machine_name = m.get('MachineName')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RiskId') is not None:
            self.risk_id = m.get('RiskId')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        if m.get('StrategyId') is not None:
            self.strategy_id = m.get('StrategyId')

        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')

        if m.get('Uuids') is not None:
            self.uuids = m.get('Uuids')

        return self

