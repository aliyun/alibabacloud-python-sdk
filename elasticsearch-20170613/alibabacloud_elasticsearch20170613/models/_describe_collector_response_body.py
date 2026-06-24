# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_elasticsearch20170613 import models as main_models
from darabonba.model import DaraModel

class DescribeCollectorResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: main_models.DescribeCollectorResponseBodyResult = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The returned result.
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result is not None:
            result['Result'] = self.result.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Result') is not None:
            temp_model = main_models.DescribeCollectorResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        return self

class DescribeCollectorResponseBodyResult(DaraModel):
    def __init__(
        self,
        collector_paths: List[str] = None,
        configs: List[main_models.DescribeCollectorResponseBodyResultConfigs] = None,
        dry_run: bool = None,
        extend_configs: List[main_models.DescribeCollectorResponseBodyResultExtendConfigs] = None,
        gmt_created_time: str = None,
        gmt_update_time: str = None,
        name: str = None,
        owner_id: str = None,
        res_id: str = None,
        res_type: str = None,
        res_version: str = None,
        status: str = None,
        vpc_id: str = None,
    ):
        self.collector_paths = collector_paths
        # The configuration file information of the collector.
        self.configs = configs
        # Specifies whether to perform only a dry run without creating the collector. Valid values:
        # 
        # - true: Only validates the request without creating the collector.
        # - false: Validates the request and creates the collector.
        self.dry_run = dry_run
        # The extended configurations of the collector.
        self.extend_configs = extend_configs
        # The time when the collector was created.
        self.gmt_created_time = gmt_created_time
        # The time when the collector was last updated.
        self.gmt_update_time = gmt_update_time
        # The collector name.
        self.name = name
        # The account ID.
        self.owner_id = owner_id
        # The collector instance ID.
        self.res_id = res_id
        # The collector type. Valid values: fileBeat, metricBeat, heartBeat, and auditBeat.
        self.res_type = res_type
        # The collector version.
        self.res_version = res_version
        # The collector status. Valid values:
        # 
        # - activing: being activated
        # - active: activated.
        self.status = status
        # The ID of the virtual private cloud (VPC) where the collector resides.
        self.vpc_id = vpc_id

    def validate(self):
        if self.configs:
            for v1 in self.configs:
                 if v1:
                    v1.validate()
        if self.extend_configs:
            for v1 in self.extend_configs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.collector_paths is not None:
            result['collectorPaths'] = self.collector_paths

        result['configs'] = []
        if self.configs is not None:
            for k1 in self.configs:
                result['configs'].append(k1.to_map() if k1 else None)

        if self.dry_run is not None:
            result['dryRun'] = self.dry_run

        result['extendConfigs'] = []
        if self.extend_configs is not None:
            for k1 in self.extend_configs:
                result['extendConfigs'].append(k1.to_map() if k1 else None)

        if self.gmt_created_time is not None:
            result['gmtCreatedTime'] = self.gmt_created_time

        if self.gmt_update_time is not None:
            result['gmtUpdateTime'] = self.gmt_update_time

        if self.name is not None:
            result['name'] = self.name

        if self.owner_id is not None:
            result['ownerId'] = self.owner_id

        if self.res_id is not None:
            result['resId'] = self.res_id

        if self.res_type is not None:
            result['resType'] = self.res_type

        if self.res_version is not None:
            result['resVersion'] = self.res_version

        if self.status is not None:
            result['status'] = self.status

        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('collectorPaths') is not None:
            self.collector_paths = m.get('collectorPaths')

        self.configs = []
        if m.get('configs') is not None:
            for k1 in m.get('configs'):
                temp_model = main_models.DescribeCollectorResponseBodyResultConfigs()
                self.configs.append(temp_model.from_map(k1))

        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')

        self.extend_configs = []
        if m.get('extendConfigs') is not None:
            for k1 in m.get('extendConfigs'):
                temp_model = main_models.DescribeCollectorResponseBodyResultExtendConfigs()
                self.extend_configs.append(temp_model.from_map(k1))

        if m.get('gmtCreatedTime') is not None:
            self.gmt_created_time = m.get('gmtCreatedTime')

        if m.get('gmtUpdateTime') is not None:
            self.gmt_update_time = m.get('gmtUpdateTime')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('ownerId') is not None:
            self.owner_id = m.get('ownerId')

        if m.get('resId') is not None:
            self.res_id = m.get('resId')

        if m.get('resType') is not None:
            self.res_type = m.get('resType')

        if m.get('resVersion') is not None:
            self.res_version = m.get('resVersion')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')

        return self

class DescribeCollectorResponseBodyResultExtendConfigs(DaraModel):
    def __init__(
        self,
        config_type: str = None,
        enable_monitoring: bool = None,
        group_id: str = None,
        host: str = None,
        hosts: List[str] = None,
        instance_id: str = None,
        instance_type: str = None,
        kibana_host: str = None,
        machines: List[main_models.DescribeCollectorResponseBodyResultExtendConfigsMachines] = None,
        protocol: str = None,
        success_pods_count: str = None,
        total_pods_count: str = None,
        type: str = None,
        user_name: str = None,
    ):
        # The configuration type. Valid values:
        # 
        # - collectorTargetInstance: the collector Output
        # - collectorDeployMachine: the deployment machine of the collector
        # - collectorElasticsearchForKibana: the Elasticsearch instance that supports Kibana Dashboard.
        self.config_type = config_type
        # Indicates whether Monitoring is enabled. This parameter is displayed when **configType** is set to **collectorTargetInstance**. Valid values:
        # 
        # - true: Enabled.
        # 
        # - false: Not enabled.
        self.enable_monitoring = enable_monitoring
        # The machine group ID. This parameter is displayed when **configType** is set to **collectorDeployMachine**.
        self.group_id = group_id
        # The private endpoint of Kibana after Kibana Dashboard is enabled. This parameter is displayed when **configType** is set to **collectorElasticsearchForKibana**.
        self.host = host
        self.hosts = hosts
        # The ID of the instance associated with the collector. When **configType** is set to **collectorTargetInstance**, this parameter indicates the instance ID of the collector Output. When **configType** is set to **collectorDeployMachines** and **type** is set to **ACKCluster**, this parameter indicates the ACK (Container Kubernetes) cluster ID.
        self.instance_id = instance_id
        # The type of instance specified in the collector Output. Valid values: elasticsearch and logstash. This parameter is displayed when **configType** is set to **collectorTargetInstance**.
        self.instance_type = instance_type
        # The public network access address of Kibana after Kibana Dashboard is enabled. This parameter is displayed when **configType** is set to **collectorElasticsearchForKibana**.
        self.kibana_host = kibana_host
        # The list of ECS machines on which the collector is deployed. This parameter is displayed when **configType** is set to **collectorDeployMachines** and **type** is set to **ECSInstanceId**.
        self.machines = machines
        # The transport protocol, which must be the same as the access protocol of the instance specified in the collector Output. Valid values: HTTP and HTTPS. This parameter is displayed when **configType** is set to **collectorTargetInstance**.
        self.protocol = protocol
        # The number of pods in the ACK cluster from which data is successfully collected.
        self.success_pods_count = success_pods_count
        # The total number of pods in the ACK cluster from which data is collected.
        self.total_pods_count = total_pods_count
        # The type of machine on which the collector is deployed. This parameter is displayed when **configType** is set to **collectorDeployMachine**. Valid values:
        # 
        # - ECSInstanceId: ECS
        # - ACKCluster: Container Kubernetes.
        self.type = type
        # The username used to access the instance specified in the collector Output. Default value: elastic. This parameter is displayed when **configType** is set to **collectorTargetInstance** or **collectorElasticsearchForKibana**.
        self.user_name = user_name

    def validate(self):
        if self.machines:
            for v1 in self.machines:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_type is not None:
            result['configType'] = self.config_type

        if self.enable_monitoring is not None:
            result['enableMonitoring'] = self.enable_monitoring

        if self.group_id is not None:
            result['groupId'] = self.group_id

        if self.host is not None:
            result['host'] = self.host

        if self.hosts is not None:
            result['hosts'] = self.hosts

        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        if self.instance_type is not None:
            result['instanceType'] = self.instance_type

        if self.kibana_host is not None:
            result['kibanaHost'] = self.kibana_host

        result['machines'] = []
        if self.machines is not None:
            for k1 in self.machines:
                result['machines'].append(k1.to_map() if k1 else None)

        if self.protocol is not None:
            result['protocol'] = self.protocol

        if self.success_pods_count is not None:
            result['successPodsCount'] = self.success_pods_count

        if self.total_pods_count is not None:
            result['totalPodsCount'] = self.total_pods_count

        if self.type is not None:
            result['type'] = self.type

        if self.user_name is not None:
            result['userName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('configType') is not None:
            self.config_type = m.get('configType')

        if m.get('enableMonitoring') is not None:
            self.enable_monitoring = m.get('enableMonitoring')

        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')

        if m.get('host') is not None:
            self.host = m.get('host')

        if m.get('hosts') is not None:
            self.hosts = m.get('hosts')

        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        if m.get('instanceType') is not None:
            self.instance_type = m.get('instanceType')

        if m.get('kibanaHost') is not None:
            self.kibana_host = m.get('kibanaHost')

        self.machines = []
        if m.get('machines') is not None:
            for k1 in m.get('machines'):
                temp_model = main_models.DescribeCollectorResponseBodyResultExtendConfigsMachines()
                self.machines.append(temp_model.from_map(k1))

        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')

        if m.get('successPodsCount') is not None:
            self.success_pods_count = m.get('successPodsCount')

        if m.get('totalPodsCount') is not None:
            self.total_pods_count = m.get('totalPodsCount')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('userName') is not None:
            self.user_name = m.get('userName')

        return self

class DescribeCollectorResponseBodyResultExtendConfigsMachines(DaraModel):
    def __init__(
        self,
        agent_status: str = None,
        instance_id: str = None,
    ):
        # The status of the collector on the ECS instance. Valid values:
        # 
        # - heartOk: The heartbeat is normal.
        # - heartLost: The heartbeat is abnormal.
        # - uninstalled: Not installed.
        # - failed: Installation failed.
        self.agent_status = agent_status
        # The list of ECS instance IDs.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_status is not None:
            result['agentStatus'] = self.agent_status

        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentStatus') is not None:
            self.agent_status = m.get('agentStatus')

        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        return self

class DescribeCollectorResponseBodyResultConfigs(DaraModel):
    def __init__(
        self,
        content: str = None,
        file_name: str = None,
    ):
        # The file content.
        self.content = content
        # The file name.
        self.file_name = file_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['content'] = self.content

        if self.file_name is not None:
            result['fileName'] = self.file_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')

        return self

