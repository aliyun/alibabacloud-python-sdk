# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_elasticsearch20170613 import models as main_models
from darabonba.model import DaraModel

class ListEcsInstancesResponseBody(DaraModel):
    def __init__(
        self,
        headers: main_models.ListEcsInstancesResponseBodyHeaders = None,
        request_id: str = None,
        result: List[main_models.ListEcsInstancesResponseBodyResult] = None,
    ):
        # The response headers.
        self.headers = headers
        # The request ID.
        self.request_id = request_id
        # The returned results.
        self.result = result

    def validate(self):
        if self.headers:
            self.headers.validate()
        if self.result:
            for v1 in self.result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.headers is not None:
            result['Headers'] = self.headers.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['Result'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Headers') is not None:
            temp_model = main_models.ListEcsInstancesResponseBodyHeaders()
            self.headers = temp_model.from_map(m.get('Headers'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.result = []
        if m.get('Result') is not None:
            for k1 in m.get('Result'):
                temp_model = main_models.ListEcsInstancesResponseBodyResult()
                self.result.append(temp_model.from_map(k1))

        return self

class ListEcsInstancesResponseBodyResult(DaraModel):
    def __init__(
        self,
        cloud_assistant_status: str = None,
        collectors: List[main_models.ListEcsInstancesResponseBodyResultCollectors] = None,
        ecs_instance_id: str = None,
        ecs_instance_name: str = None,
        ip_address: List[main_models.ListEcsInstancesResponseBodyResultIpAddress] = None,
        os_type: str = None,
        status: str = None,
        tags: str = None,
    ):
        # The installation status of Cloud Assistant. Valid values:
        # 
        # - true: Installed.
        # - false: Not installed.
        self.cloud_assistant_status = cloud_assistant_status
        # The list of collectors deployed on the ECS instance.
        self.collectors = collectors
        # The ECS instance ID.
        self.ecs_instance_id = ecs_instance_id
        # The name of the ECS instance.
        self.ecs_instance_name = ecs_instance_name
        # The IP address information of the ECS instance.
        self.ip_address = ip_address
        # The operating system type of the ECS instance. Valid values:
        # 
        # - windows: Windows operating system.
        # - linux: Linux operating system.
        self.os_type = os_type
        # The status of the ECS instance. Valid values:
        # 
        # - running: Running.
        # - starting: Starting.
        # - stopping: Stopping.
        # - stopped: Stopped.
        self.status = status
        # The tag information of the ECS instance.
        self.tags = tags

    def validate(self):
        if self.collectors:
            for v1 in self.collectors:
                 if v1:
                    v1.validate()
        if self.ip_address:
            for v1 in self.ip_address:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cloud_assistant_status is not None:
            result['cloudAssistantStatus'] = self.cloud_assistant_status

        result['collectors'] = []
        if self.collectors is not None:
            for k1 in self.collectors:
                result['collectors'].append(k1.to_map() if k1 else None)

        if self.ecs_instance_id is not None:
            result['ecsInstanceId'] = self.ecs_instance_id

        if self.ecs_instance_name is not None:
            result['ecsInstanceName'] = self.ecs_instance_name

        result['ipAddress'] = []
        if self.ip_address is not None:
            for k1 in self.ip_address:
                result['ipAddress'].append(k1.to_map() if k1 else None)

        if self.os_type is not None:
            result['osType'] = self.os_type

        if self.status is not None:
            result['status'] = self.status

        if self.tags is not None:
            result['tags'] = self.tags

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cloudAssistantStatus') is not None:
            self.cloud_assistant_status = m.get('cloudAssistantStatus')

        self.collectors = []
        if m.get('collectors') is not None:
            for k1 in m.get('collectors'):
                temp_model = main_models.ListEcsInstancesResponseBodyResultCollectors()
                self.collectors.append(temp_model.from_map(k1))

        if m.get('ecsInstanceId') is not None:
            self.ecs_instance_id = m.get('ecsInstanceId')

        if m.get('ecsInstanceName') is not None:
            self.ecs_instance_name = m.get('ecsInstanceName')

        self.ip_address = []
        if m.get('ipAddress') is not None:
            for k1 in m.get('ipAddress'):
                temp_model = main_models.ListEcsInstancesResponseBodyResultIpAddress()
                self.ip_address.append(temp_model.from_map(k1))

        if m.get('osType') is not None:
            self.os_type = m.get('osType')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('tags') is not None:
            self.tags = m.get('tags')

        return self

class ListEcsInstancesResponseBodyResultIpAddress(DaraModel):
    def __init__(
        self,
        host: str = None,
        ip_type: str = None,
    ):
        # The IP address.
        self.host = host
        # The IP address type. Valid values:
        # 
        # - public: public IP address.
        # - private: private network address.
        self.ip_type = ip_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.host is not None:
            result['host'] = self.host

        if self.ip_type is not None:
            result['ipType'] = self.ip_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('host') is not None:
            self.host = m.get('host')

        if m.get('ipType') is not None:
            self.ip_type = m.get('ipType')

        return self

class ListEcsInstancesResponseBodyResultCollectors(DaraModel):
    def __init__(
        self,
        collector_paths: List[str] = None,
        configs: List[main_models.ListEcsInstancesResponseBodyResultCollectorsConfigs] = None,
        dry_run: bool = None,
        extend_configs: List[main_models.ListEcsInstancesResponseBodyResultCollectorsExtendConfigs] = None,
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
        # Indicates whether the collector is only validated without being created. Valid values:
        # 
        # - true: Only validates without creating.
        # - false: Validates and creates.
        self.dry_run = dry_run
        # The extended configuration information.
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
        # The collector version. When the machine type for collector deployment is ECS, only **6.8.5_with_community** is supported.
        self.res_version = res_version
        # The collector status. Valid values:
        # 
        # - activing: Taking effect.
        # - active: Active.
        self.status = status
        # The ID of the VPC where the collector resides.
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
                temp_model = main_models.ListEcsInstancesResponseBodyResultCollectorsConfigs()
                self.configs.append(temp_model.from_map(k1))

        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')

        self.extend_configs = []
        if m.get('extendConfigs') is not None:
            for k1 in m.get('extendConfigs'):
                temp_model = main_models.ListEcsInstancesResponseBodyResultCollectorsExtendConfigs()
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

class ListEcsInstancesResponseBodyResultCollectorsExtendConfigs(DaraModel):
    def __init__(
        self,
        config_type: str = None,
        enable_monitoring: bool = None,
        group_id: str = None,
        hosts: List[str] = None,
        instance_id: str = None,
        instance_type: str = None,
        machines: List[main_models.ListEcsInstancesResponseBodyResultCollectorsExtendConfigsMachines] = None,
        protocol: str = None,
        type: str = None,
        user_name: str = None,
    ):
        # The configuration type. Valid values:
        # 
        # - collectorTargetInstance: the collector Output.
        # - collectorDeployMachine: the deployment machine of the collector.
        # - collectorElasticsearchForKibana: the Elasticsearch instance information that supports Kibana dashboards.
        self.config_type = config_type
        # Indicates whether Monitoring is enabled. This parameter is displayed when configType is set to collectorTargetInstance and instanceType is set to elasticsearch. Valid values:
        # 
        # - true: Enabled.
        # - false: Not enabled.
        self.enable_monitoring = enable_monitoring
        # The machine group ID. This parameter is displayed when configType is set to collectorDeployMachine.
        self.group_id = group_id
        self.hosts = hosts
        # The ID of the instance associated with the collector. When configType is set to collectorTargetInstance, this is the instance ID of the collector Output. When configType is set to collectorDeployMachines and type is set to ACKCluster, this is the ACK (Container Service for Kubernetes) cluster ID.
        self.instance_id = instance_id
        # The type of the instance specified by the collector Output. Valid values: elasticsearch and logstash. This parameter is displayed when configType is set to collectorTargetInstance.
        self.instance_type = instance_type
        # The list of ECS machines on which the collector is deployed. This parameter is displayed when configType is set to collectorDeployMachines and type is set to ECSInstanceId.
        self.machines = machines
        # The transmission protocol, which must be consistent with the access protocol of the instance specified by the collector Output. Valid values: HTTP and HTTPS. This parameter is displayed when configType is set to collectorTargetInstance.
        self.protocol = protocol
        # The type of machine on which the collector is deployed. This parameter is displayed when configType is set to collectorDeployMachine. Valid values:
        # 
        # - ECSInstanceId: ECS
        # - ACKCluster: Container Service for Kubernetes.
        self.type = type
        # The username used to access the instance specified by the collector Output. Default value: elastic. This parameter is displayed when configType is set to collectorTargetInstance or collectorElasticsearchForKibana.
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

        if self.hosts is not None:
            result['hosts'] = self.hosts

        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        if self.instance_type is not None:
            result['instanceType'] = self.instance_type

        result['machines'] = []
        if self.machines is not None:
            for k1 in self.machines:
                result['machines'].append(k1.to_map() if k1 else None)

        if self.protocol is not None:
            result['protocol'] = self.protocol

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

        if m.get('hosts') is not None:
            self.hosts = m.get('hosts')

        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        if m.get('instanceType') is not None:
            self.instance_type = m.get('instanceType')

        self.machines = []
        if m.get('machines') is not None:
            for k1 in m.get('machines'):
                temp_model = main_models.ListEcsInstancesResponseBodyResultCollectorsExtendConfigsMachines()
                self.machines.append(temp_model.from_map(k1))

        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('userName') is not None:
            self.user_name = m.get('userName')

        return self

class ListEcsInstancesResponseBodyResultCollectorsExtendConfigsMachines(DaraModel):
    def __init__(
        self,
        agent_status: str = None,
        instance_id: str = None,
    ):
        # The status of each collector on the ECS instance. Valid values:
        # 
        # - heartOk: The heartbeat is normal.
        # - heartLost: The heartbeat is abnormal.
        # - uninstalled: Not installed.
        # - failed: Installation failed.
        self.agent_status = agent_status
        # The list of ECS machine IDs.
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

class ListEcsInstancesResponseBodyResultCollectorsConfigs(DaraModel):
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

class ListEcsInstancesResponseBodyHeaders(DaraModel):
    def __init__(
        self,
        x_total_count: int = None,
    ):
        # The total number of returned records.
        self.x_total_count = x_total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.x_total_count is not None:
            result['X-Total-Count'] = self.x_total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('X-Total-Count') is not None:
            self.x_total_count = m.get('X-Total-Count')

        return self

