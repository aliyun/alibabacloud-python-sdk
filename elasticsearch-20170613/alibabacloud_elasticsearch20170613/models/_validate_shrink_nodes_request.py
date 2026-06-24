# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_elasticsearch20170613 import models as main_models
from darabonba.model import DaraModel

class ValidateShrinkNodesRequest(DaraModel):
    def __init__(
        self,
        body: List[main_models.ValidateShrinkNodesRequestBody] = None,
        count: int = None,
        ignore_status: bool = None,
        node_type: str = None,
    ):
        # The request body.
        self.body = body
        # The number of nodes.
        self.count = count
        # Specifies whether to ignore the cluster health status.
        # 
        # - true: ignores the cluster health status.
        # - false (default): does not ignore the cluster health status.
        self.ignore_status = ignore_status
        # The type of nodes to scale in. Valid values:
        # 
        # - WORKER: hot node
        # - WORKER_WARM: warm node
        # 
        # This parameter is required.
        self.node_type = node_type

    def validate(self):
        if self.body:
            for v1 in self.body:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['body'] = []
        if self.body is not None:
            for k1 in self.body:
                result['body'].append(k1.to_map() if k1 else None)

        if self.count is not None:
            result['count'] = self.count

        if self.ignore_status is not None:
            result['ignoreStatus'] = self.ignore_status

        if self.node_type is not None:
            result['nodeType'] = self.node_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.body = []
        if m.get('body') is not None:
            for k1 in m.get('body'):
                temp_model = main_models.ValidateShrinkNodesRequestBody()
                self.body.append(temp_model.from_map(k1))

        if m.get('count') is not None:
            self.count = m.get('count')

        if m.get('ignoreStatus') is not None:
            self.ignore_status = m.get('ignoreStatus')

        if m.get('nodeType') is not None:
            self.node_type = m.get('nodeType')

        return self

class ValidateShrinkNodesRequestBody(DaraModel):
    def __init__(
        self,
        host: str = None,
        host_name: str = None,
        node_type: str = None,
        port: int = None,
        zone_id: str = None,
    ):
        # The IP address of the node.
        self.host = host
        # The node name of the cloud-native ACK-based cluster. You can call the [ListAllNode](https://help.aliyun.com/document_detail/183958.html) operation to obtain the node name.
        self.host_name = host_name
        # The node type. Valid values:
        # 
        # - WORKER: hot node
        # - WORKER_WARM: warm node
        self.node_type = node_type
        # The access port number of the node.
        self.port = port
        # The zone ID of the node in the instance. For example, the zone ID of China (Shanghai) Zone C is cn-shanghai-c.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.host is not None:
            result['host'] = self.host

        if self.host_name is not None:
            result['hostName'] = self.host_name

        if self.node_type is not None:
            result['nodeType'] = self.node_type

        if self.port is not None:
            result['port'] = self.port

        if self.zone_id is not None:
            result['zoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('host') is not None:
            self.host = m.get('host')

        if m.get('hostName') is not None:
            self.host_name = m.get('hostName')

        if m.get('nodeType') is not None:
            self.node_type = m.get('nodeType')

        if m.get('port') is not None:
            self.port = m.get('port')

        if m.get('zoneId') is not None:
            self.zone_id = m.get('zoneId')

        return self

