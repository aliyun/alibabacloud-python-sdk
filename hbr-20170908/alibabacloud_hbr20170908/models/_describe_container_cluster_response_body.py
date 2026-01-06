# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_hbr20170908 import models as main_models
from darabonba.model import DaraModel

class DescribeContainerClusterResponseBody(DaraModel):
    def __init__(
        self,
        clusters: List[main_models.DescribeContainerClusterResponseBodyClusters] = None,
        code: str = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        # The information of clusters.
        self.clusters = clusters
        # The HTTP status code. The status code 200 indicates that the call is successful.
        self.code = code
        # The message that is returned. If the call is successful, "successful" is returned. If the call fails, an error message is returned.
        self.message = message
        # The page number of the returned page. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries returned on each page. Valid values: 1 to 99. Default value: 10.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the call is successful. Valid values:
        # 
        # *   true: The call is successful.
        # *   false: The call fails.
        self.success = success
        # The total number of returned entries.
        self.total_count = total_count

    def validate(self):
        if self.clusters:
            for v1 in self.clusters:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Clusters'] = []
        if self.clusters is not None:
            for k1 in self.clusters:
                result['Clusters'].append(k1.to_map() if k1 else None)

        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.clusters = []
        if m.get('Clusters') is not None:
            for k1 in m.get('Clusters'):
                temp_model = main_models.DescribeContainerClusterResponseBodyClusters()
                self.clusters.append(temp_model.from_map(k1))

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeContainerClusterResponseBodyClusters(DaraModel):
    def __init__(
        self,
        agent_status: str = None,
        cluster_id: str = None,
        cluster_type: str = None,
        description: str = None,
        identifier: str = None,
        name: str = None,
        network_type: str = None,
        token: str = None,
    ):
        # The status of the client. Valid values:
        # 
        # *   **MISS**: The client is disconnected.
        # *   **UNKNOWN**: The client is in an unknown state.
        # *   **READY**: The client is ready.
        self.agent_status = agent_status
        # The ID of the cluster.
        self.cluster_id = cluster_id
        # The type of the cluster. Valid value: ACK, which indicates ACK clusters.
        self.cluster_type = cluster_type
        # The description.
        self.description = description
        # The identifier of the cluster.
        self.identifier = identifier
        # The name of the instance.
        self.name = name
        # The network type of the cluster. Valid values:
        # 
        # *   **CLASSIC**: the classic network
        # *   **VPC**: virtual private cloud (VPC)
        self.network_type = network_type
        # The token that is used to register the Hybrid Backup Recovery (HBR) client in the cluster.
        self.token = token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_status is not None:
            result['AgentStatus'] = self.agent_status

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type

        if self.description is not None:
            result['Description'] = self.description

        if self.identifier is not None:
            result['Identifier'] = self.identifier

        if self.name is not None:
            result['Name'] = self.name

        if self.network_type is not None:
            result['NetworkType'] = self.network_type

        if self.token is not None:
            result['Token'] = self.token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentStatus') is not None:
            self.agent_status = m.get('AgentStatus')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Identifier') is not None:
            self.identifier = m.get('Identifier')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')

        if m.get('Token') is not None:
            self.token = m.get('Token')

        return self

