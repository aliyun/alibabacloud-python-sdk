# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_elasticsearch20170613 import models as main_models
from darabonba.model import DaraModel

class ListDataTasksResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[main_models.ListDataTasksResponseBodyResult] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The return results.
        self.result = result

    def validate(self):
        if self.result:
            for v1 in self.result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['Result'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.result = []
        if m.get('Result') is not None:
            for k1 in m.get('Result'):
                temp_model = main_models.ListDataTasksResponseBodyResult()
                self.result.append(temp_model.from_map(k1))

        return self

class ListDataTasksResponseBodyResult(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        sink_cluster: main_models.ListDataTasksResponseBodyResultSinkCluster = None,
        source_cluster: main_models.ListDataTasksResponseBodyResultSourceCluster = None,
        status: str = None,
        task_id: str = None,
    ):
        # The time when the site monitoring task was created.
        self.create_time = create_time
        # The information of the target cluster.
        self.sink_cluster = sink_cluster
        # The information about the source cluster.
        self.source_cluster = source_cluster
        # The status of the task.
        self.status = status
        # The ID of the task.
        self.task_id = task_id

    def validate(self):
        if self.sink_cluster:
            self.sink_cluster.validate()
        if self.source_cluster:
            self.source_cluster.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.sink_cluster is not None:
            result['sinkCluster'] = self.sink_cluster.to_map()

        if self.source_cluster is not None:
            result['sourceCluster'] = self.source_cluster.to_map()

        if self.status is not None:
            result['status'] = self.status

        if self.task_id is not None:
            result['taskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('sinkCluster') is not None:
            temp_model = main_models.ListDataTasksResponseBodyResultSinkCluster()
            self.sink_cluster = temp_model.from_map(m.get('sinkCluster'))

        if m.get('sourceCluster') is not None:
            temp_model = main_models.ListDataTasksResponseBodyResultSourceCluster()
            self.source_cluster = temp_model.from_map(m.get('sourceCluster'))

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')

        return self

class ListDataTasksResponseBodyResultSourceCluster(DaraModel):
    def __init__(
        self,
        data_source_type: str = None,
        index: str = None,
        mapping: str = None,
        routing: str = None,
        settings: str = None,
        type: str = None,
    ):
        # The type of the source cluster. Default value: elasticsearch.
        self.data_source_type = data_source_type
        # The index whose data you want to migrate.
        self.index = index
        # The Mapping configuration of the cluster.
        self.mapping = mapping
        # The routing field to index the table. It is set to the primary key by default.
        self.routing = routing
        # The Settings of the cluster.
        self.settings = settings
        # The type of the destination index.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_source_type is not None:
            result['dataSourceType'] = self.data_source_type

        if self.index is not None:
            result['index'] = self.index

        if self.mapping is not None:
            result['mapping'] = self.mapping

        if self.routing is not None:
            result['routing'] = self.routing

        if self.settings is not None:
            result['settings'] = self.settings

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dataSourceType') is not None:
            self.data_source_type = m.get('dataSourceType')

        if m.get('index') is not None:
            self.index = m.get('index')

        if m.get('mapping') is not None:
            self.mapping = m.get('mapping')

        if m.get('routing') is not None:
            self.routing = m.get('routing')

        if m.get('settings') is not None:
            self.settings = m.get('settings')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class ListDataTasksResponseBodyResultSinkCluster(DaraModel):
    def __init__(
        self,
        data_source_type: str = None,
        endpoint: str = None,
        index: str = None,
        type: str = None,
        vpc_id: str = None,
        vpc_instance_id: str = None,
        vpc_instance_port: str = None,
    ):
        # The type of the target cluster. Default value: elasticsearch.
        self.data_source_type = data_source_type
        # The public network access address of the target cluster.
        self.endpoint = endpoint
        # The target index.
        self.index = index
        # The type of the destination index.
        self.type = type
        # The ID of the VPC to which the cluster belongs.
        self.vpc_id = vpc_id
        # The instance ID or Server Load Balancer (SLB) ID of the current cluster.
        self.vpc_instance_id = vpc_instance_id
        # The access port number of the cluster.
        self.vpc_instance_port = vpc_instance_port

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_source_type is not None:
            result['dataSourceType'] = self.data_source_type

        if self.endpoint is not None:
            result['endpoint'] = self.endpoint

        if self.index is not None:
            result['index'] = self.index

        if self.type is not None:
            result['type'] = self.type

        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id

        if self.vpc_instance_id is not None:
            result['vpcInstanceId'] = self.vpc_instance_id

        if self.vpc_instance_port is not None:
            result['vpcInstancePort'] = self.vpc_instance_port

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dataSourceType') is not None:
            self.data_source_type = m.get('dataSourceType')

        if m.get('endpoint') is not None:
            self.endpoint = m.get('endpoint')

        if m.get('index') is not None:
            self.index = m.get('index')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')

        if m.get('vpcInstanceId') is not None:
            self.vpc_instance_id = m.get('vpcInstanceId')

        if m.get('vpcInstancePort') is not None:
            self.vpc_instance_port = m.get('vpcInstancePort')

        return self

