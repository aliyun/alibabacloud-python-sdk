# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class FindContainerNetworkConnectRequest(DaraModel):
    def __init__(
        self,
        criteria_type: str = None,
        current_page: int = None,
        dst_node: main_models.FindContainerNetworkConnectRequestDstNode = None,
        end_time: int = None,
        page_size: int = None,
        src_node: main_models.FindContainerNetworkConnectRequestSrcNode = None,
        start_time: int = None,
    ):
        # The type of the information that you want to query. Valid values:
        # 
        # *   **EDGE**: connection information
        self.criteria_type = criteria_type
        # The number of the page to return. Default value: **1**.
        self.current_page = current_page
        # The information about the destination node.
        self.dst_node = dst_node
        # The end time of the network connection.
        self.end_time = end_time
        # The number of entries to return on each page. Default value: 20. If you leave this parameter empty, 20 entries are returned on each page.
        # 
        # > We recommend that you do not leave this parameter empty.
        self.page_size = page_size
        # The information about the source node.
        self.src_node = src_node
        # The start time of the network connection.
        self.start_time = start_time

    def validate(self):
        if self.dst_node:
            self.dst_node.validate()
        if self.src_node:
            self.src_node.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.criteria_type is not None:
            result['CriteriaType'] = self.criteria_type

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.dst_node is not None:
            result['DstNode'] = self.dst_node.to_map()

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.src_node is not None:
            result['SrcNode'] = self.src_node.to_map()

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CriteriaType') is not None:
            self.criteria_type = m.get('CriteriaType')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('DstNode') is not None:
            temp_model = main_models.FindContainerNetworkConnectRequestDstNode()
            self.dst_node = temp_model.from_map(m.get('DstNode'))

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SrcNode') is not None:
            temp_model = main_models.FindContainerNetworkConnectRequestSrcNode()
            self.src_node = temp_model.from_map(m.get('SrcNode'))

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

class FindContainerNetworkConnectRequestSrcNode(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        cluster_id: str = None,
        namespace: str = None,
        node_ids: List[str] = None,
        node_type: str = None,
        pod_name: str = None,
    ):
        # The name of the container application.
        self.app_name = app_name
        # The ID of the container cluster.
        # 
        # > You can call the [DescribeGroupedContainerInstances](~~DescribeGroupedContainerInstances~~) operation to query the IDs of container clusters.
        self.cluster_id = cluster_id
        # The namespace of the cluster.
        self.namespace = namespace
        # The node IDs.
        self.node_ids = node_ids
        # The type of the node. Valid values:
        # 
        # *   **app**: application, which indicates that the node type is application.
        self.node_type = node_type
        # The name of the pod.
        self.pod_name = pod_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.node_ids is not None:
            result['NodeIds'] = self.node_ids

        if self.node_type is not None:
            result['NodeType'] = self.node_type

        if self.pod_name is not None:
            result['PodName'] = self.pod_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('NodeIds') is not None:
            self.node_ids = m.get('NodeIds')

        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')

        if m.get('PodName') is not None:
            self.pod_name = m.get('PodName')

        return self

class FindContainerNetworkConnectRequestDstNode(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        cluster_id: str = None,
        namespace: str = None,
        node_ids: List[str] = None,
        node_type: str = None,
        pod_name: str = None,
    ):
        # The name of the container application.
        self.app_name = app_name
        # The ID of the container cluster.
        # 
        # > You can call the [DescribeGroupedContainerInstances](~~DescribeGroupedContainerInstances~~) operation to query the IDs of container clusters.
        self.cluster_id = cluster_id
        # The namespace of the cluster.
        self.namespace = namespace
        # The node IDs.
        self.node_ids = node_ids
        # The type of the node. Valid values:
        # 
        # *   **app**: application, which indicates that the node type is application.
        self.node_type = node_type
        # The name of the pod.
        self.pod_name = pod_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.node_ids is not None:
            result['NodeIds'] = self.node_ids

        if self.node_type is not None:
            result['NodeType'] = self.node_type

        if self.pod_name is not None:
            result['PodName'] = self.pod_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('NodeIds') is not None:
            self.node_ids = m.get('NodeIds')

        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')

        if m.get('PodName') is not None:
            self.pod_name = m.get('PodName')

        return self

