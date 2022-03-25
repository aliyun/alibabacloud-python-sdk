# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List, Any


class LogstashEndpointList(TeaModel):
    def __init__(
        self,
        host: str = None,
        port: int = None,
        zone_id: str = None,
    ):
        # Host
        self.host = host
        # Port
        self.port = port
        # ZoneId
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host is not None:
            result['host'] = self.host
        if self.port is not None:
            result['port'] = self.port
        if self.zone_id is not None:
            result['zoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('host') is not None:
            self.host = m.get('host')
        if m.get('port') is not None:
            self.port = m.get('port')
        if m.get('zoneId') is not None:
            self.zone_id = m.get('zoneId')
        return self


class LogstashNetworkConfig(TeaModel):
    def __init__(
        self,
        type: str = None,
        vpc_id: str = None,
        vs_area: str = None,
        vswitch_id: str = None,
    ):
        # Type
        self.type = type
        # VpcId
        self.vpc_id = vpc_id
        # VsArea
        self.vs_area = vs_area
        # VswitchId
        self.vswitch_id = vswitch_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['type'] = self.type
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        if self.vs_area is not None:
            result['vsArea'] = self.vs_area
        if self.vswitch_id is not None:
            result['vswitchId'] = self.vswitch_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        if m.get('vsArea') is not None:
            self.vs_area = m.get('vsArea')
        if m.get('vswitchId') is not None:
            self.vswitch_id = m.get('vswitchId')
        return self


class LogstashNodeSpec(TeaModel):
    def __init__(
        self,
        disk: int = None,
        disk_type: str = None,
        spec: str = None,
    ):
        # Disk
        self.disk = disk
        # DiskType
        self.disk_type = disk_type
        # Spec
        self.spec = spec

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.disk is not None:
            result['disk'] = self.disk
        if self.disk_type is not None:
            result['diskType'] = self.disk_type
        if self.spec is not None:
            result['spec'] = self.spec
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('disk') is not None:
            self.disk = m.get('disk')
        if m.get('diskType') is not None:
            self.disk_type = m.get('diskType')
        if m.get('spec') is not None:
            self.spec = m.get('spec')
        return self


class LogstashTags(TeaModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # TagKey
        self.tag_key = tag_key
        # TagValue
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_key is not None:
            result['tagKey'] = self.tag_key
        if self.tag_value is not None:
            result['tagValue'] = self.tag_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('tagKey') is not None:
            self.tag_key = m.get('tagKey')
        if m.get('tagValue') is not None:
            self.tag_value = m.get('tagValue')
        return self


class LogstashZoneInfos(TeaModel):
    def __init__(
        self,
        status: str = None,
        zone_id: str = None,
    ):
        # Status
        self.status = status
        # ZoneId
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['status'] = self.status
        if self.zone_id is not None:
            result['zoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('zoneId') is not None:
            self.zone_id = m.get('zoneId')
        return self


class Logstash(TeaModel):
    def __init__(
        self,
        config: Dict[str, str] = None,
        created_at: str = None,
        data_node: bool = None,
        description: str = None,
        end_time: int = None,
        endpoint_list: List[LogstashEndpointList] = None,
        instance_id: str = None,
        network_config: LogstashNetworkConfig = None,
        node_amount: int = None,
        node_spec: LogstashNodeSpec = None,
        payment_type: str = None,
        protocol: str = None,
        resource_group_id: str = None,
        status: str = None,
        tags: List[LogstashTags] = None,
        updated_at: str = None,
        version: str = None,
        zone_count: int = None,
        zone_infos: List[LogstashZoneInfos] = None,
    ):
        # Config
        self.config = config
        # CreatedAt
        self.created_at = created_at
        # DataNode
        self.data_node = data_node
        # Description
        self.description = description
        # EndTime
        self.end_time = end_time
        # EndpointList
        self.endpoint_list = endpoint_list
        # InstanceId
        self.instance_id = instance_id
        # NetworkConfig
        self.network_config = network_config
        # NodeAmount
        self.node_amount = node_amount
        # NodeSpec
        self.node_spec = node_spec
        # PaymentType
        self.payment_type = payment_type
        # Protocol
        self.protocol = protocol
        # ResourceGroupId
        self.resource_group_id = resource_group_id
        # Status
        self.status = status
        # Tags
        self.tags = tags
        # UpdatedAt
        self.updated_at = updated_at
        # Version
        self.version = version
        # ZoneCount
        self.zone_count = zone_count
        # ZoneInfos
        self.zone_infos = zone_infos

    def validate(self):
        if self.endpoint_list:
            for k in self.endpoint_list:
                if k:
                    k.validate()
        if self.network_config:
            self.network_config.validate()
        if self.node_spec:
            self.node_spec.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()
        if self.zone_infos:
            for k in self.zone_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['config'] = self.config
        if self.created_at is not None:
            result['createdAt'] = self.created_at
        if self.data_node is not None:
            result['dataNode'] = self.data_node
        if self.description is not None:
            result['description'] = self.description
        if self.end_time is not None:
            result['endTime'] = self.end_time
        result['endpointList'] = []
        if self.endpoint_list is not None:
            for k in self.endpoint_list:
                result['endpointList'].append(k.to_map() if k else None)
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.network_config is not None:
            result['networkConfig'] = self.network_config.to_map()
        if self.node_amount is not None:
            result['nodeAmount'] = self.node_amount
        if self.node_spec is not None:
            result['nodeSpec'] = self.node_spec.to_map()
        if self.payment_type is not None:
            result['paymentType'] = self.payment_type
        if self.protocol is not None:
            result['protocol'] = self.protocol
        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id
        if self.status is not None:
            result['status'] = self.status
        result['tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['tags'].append(k.to_map() if k else None)
        if self.updated_at is not None:
            result['updatedAt'] = self.updated_at
        if self.version is not None:
            result['version'] = self.version
        if self.zone_count is not None:
            result['zoneCount'] = self.zone_count
        result['zoneInfos'] = []
        if self.zone_infos is not None:
            for k in self.zone_infos:
                result['zoneInfos'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('config') is not None:
            self.config = m.get('config')
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')
        if m.get('dataNode') is not None:
            self.data_node = m.get('dataNode')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        self.endpoint_list = []
        if m.get('endpointList') is not None:
            for k in m.get('endpointList'):
                temp_model = LogstashEndpointList()
                self.endpoint_list.append(temp_model.from_map(k))
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('networkConfig') is not None:
            temp_model = LogstashNetworkConfig()
            self.network_config = temp_model.from_map(m['networkConfig'])
        if m.get('nodeAmount') is not None:
            self.node_amount = m.get('nodeAmount')
        if m.get('nodeSpec') is not None:
            temp_model = LogstashNodeSpec()
            self.node_spec = temp_model.from_map(m['nodeSpec'])
        if m.get('paymentType') is not None:
            self.payment_type = m.get('paymentType')
        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')
        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')
        if m.get('status') is not None:
            self.status = m.get('status')
        self.tags = []
        if m.get('tags') is not None:
            for k in m.get('tags'):
                temp_model = LogstashTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')
        if m.get('version') is not None:
            self.version = m.get('version')
        if m.get('zoneCount') is not None:
            self.zone_count = m.get('zoneCount')
        self.zone_infos = []
        if m.get('zoneInfos') is not None:
            for k in m.get('zoneInfos'):
                temp_model = LogstashZoneInfos()
                self.zone_infos.append(temp_model.from_map(k))
        return self


class ActivateZonesRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
    ):
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        return self


class ActivateZonesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class ActivateZonesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ActivateZonesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ActivateZonesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddConnectableClusterRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
    ):
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        return self


class AddConnectableClusterResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class AddConnectableClusterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddConnectableClusterResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AddConnectableClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddSnapshotRepoResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class AddSnapshotRepoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddSnapshotRepoResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AddSnapshotRepoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelDeletionRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
    ):
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        return self


class CancelDeletionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class CancelDeletionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CancelDeletionResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CancelDeletionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelLogstashDeletionRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
    ):
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        return self


class CancelLogstashDeletionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class CancelLogstashDeletionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CancelLogstashDeletionResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CancelLogstashDeletionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelTaskRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        task_type: str = None,
    ):
        self.client_token = client_token
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.task_type is not None:
            result['taskType'] = self.task_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('taskType') is not None:
            self.task_type = m.get('taskType')
        return self


class CancelTaskResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class CancelTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CancelTaskResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CancelTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CapacityPlanRequestDataInfo(TeaModel):
    def __init__(
        self,
        code: str = None,
        size: int = None,
        total_count: int = None,
        type: str = None,
        unit: str = None,
    ):
        self.code = code
        self.size = size
        self.total_count = total_count
        self.type = type
        self.unit = unit

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.size is not None:
            result['size'] = self.size
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        if self.type is not None:
            result['type'] = self.type
        if self.unit is not None:
            result['unit'] = self.unit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('unit') is not None:
            self.unit = m.get('unit')
        return self


class CapacityPlanRequestMetric(TeaModel):
    def __init__(
        self,
        average_qps: int = None,
        code: str = None,
        concurrent: int = None,
        peak_qps: int = None,
        response_time: int = None,
        throughput: int = None,
        type: str = None,
    ):
        self.average_qps = average_qps
        self.code = code
        self.concurrent = concurrent
        self.peak_qps = peak_qps
        self.response_time = response_time
        self.throughput = throughput
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.average_qps is not None:
            result['averageQps'] = self.average_qps
        if self.code is not None:
            result['code'] = self.code
        if self.concurrent is not None:
            result['concurrent'] = self.concurrent
        if self.peak_qps is not None:
            result['peakQps'] = self.peak_qps
        if self.response_time is not None:
            result['responseTime'] = self.response_time
        if self.throughput is not None:
            result['throughput'] = self.throughput
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('averageQps') is not None:
            self.average_qps = m.get('averageQps')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('concurrent') is not None:
            self.concurrent = m.get('concurrent')
        if m.get('peakQps') is not None:
            self.peak_qps = m.get('peakQps')
        if m.get('responseTime') is not None:
            self.response_time = m.get('responseTime')
        if m.get('throughput') is not None:
            self.throughput = m.get('throughput')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class CapacityPlanRequest(TeaModel):
    def __init__(
        self,
        complex_query_available: bool = None,
        data_info: List[CapacityPlanRequestDataInfo] = None,
        metric: List[CapacityPlanRequestMetric] = None,
        usage_scenario: str = None,
    ):
        self.complex_query_available = complex_query_available
        self.data_info = data_info
        self.metric = metric
        self.usage_scenario = usage_scenario

    def validate(self):
        if self.data_info:
            for k in self.data_info:
                if k:
                    k.validate()
        if self.metric:
            for k in self.metric:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.complex_query_available is not None:
            result['complexQueryAvailable'] = self.complex_query_available
        result['dataInfo'] = []
        if self.data_info is not None:
            for k in self.data_info:
                result['dataInfo'].append(k.to_map() if k else None)
        result['metric'] = []
        if self.metric is not None:
            for k in self.metric:
                result['metric'].append(k.to_map() if k else None)
        if self.usage_scenario is not None:
            result['usageScenario'] = self.usage_scenario
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('complexQueryAvailable') is not None:
            self.complex_query_available = m.get('complexQueryAvailable')
        self.data_info = []
        if m.get('dataInfo') is not None:
            for k in m.get('dataInfo'):
                temp_model = CapacityPlanRequestDataInfo()
                self.data_info.append(temp_model.from_map(k))
        self.metric = []
        if m.get('metric') is not None:
            for k in m.get('metric'):
                temp_model = CapacityPlanRequestMetric()
                self.metric.append(temp_model.from_map(k))
        if m.get('usageScenario') is not None:
            self.usage_scenario = m.get('usageScenario')
        return self


class CapacityPlanResponseBodyResultExtendConfigs(TeaModel):
    def __init__(
        self,
        config_type: str = None,
        disk: int = None,
        disk_type: str = None,
    ):
        self.config_type = config_type
        self.disk = disk
        self.disk_type = disk_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_type is not None:
            result['ConfigType'] = self.config_type
        if self.disk is not None:
            result['Disk'] = self.disk
        if self.disk_type is not None:
            result['DiskType'] = self.disk_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigType') is not None:
            self.config_type = m.get('ConfigType')
        if m.get('Disk') is not None:
            self.disk = m.get('Disk')
        if m.get('DiskType') is not None:
            self.disk_type = m.get('DiskType')
        return self


class CapacityPlanResponseBodyResultNodeConfigurations(TeaModel):
    def __init__(
        self,
        amount: int = None,
        cpu: int = None,
        disk: int = None,
        disk_type: str = None,
        memory: int = None,
        node_type: str = None,
    ):
        self.amount = amount
        self.cpu = cpu
        self.disk = disk
        self.disk_type = disk_type
        self.memory = memory
        self.node_type = node_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.disk is not None:
            result['Disk'] = self.disk
        if self.disk_type is not None:
            result['DiskType'] = self.disk_type
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.node_type is not None:
            result['NodeType'] = self.node_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('Disk') is not None:
            self.disk = m.get('Disk')
        if m.get('DiskType') is not None:
            self.disk_type = m.get('DiskType')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')
        return self


class CapacityPlanResponseBodyResult(TeaModel):
    def __init__(
        self,
        extend_configs: List[CapacityPlanResponseBodyResultExtendConfigs] = None,
        instance_category: str = None,
        node_configurations: List[CapacityPlanResponseBodyResultNodeConfigurations] = None,
        oversized_cluster: bool = None,
    ):
        self.extend_configs = extend_configs
        self.instance_category = instance_category
        self.node_configurations = node_configurations
        self.oversized_cluster = oversized_cluster

    def validate(self):
        if self.extend_configs:
            for k in self.extend_configs:
                if k:
                    k.validate()
        if self.node_configurations:
            for k in self.node_configurations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ExtendConfigs'] = []
        if self.extend_configs is not None:
            for k in self.extend_configs:
                result['ExtendConfigs'].append(k.to_map() if k else None)
        if self.instance_category is not None:
            result['InstanceCategory'] = self.instance_category
        result['NodeConfigurations'] = []
        if self.node_configurations is not None:
            for k in self.node_configurations:
                result['NodeConfigurations'].append(k.to_map() if k else None)
        if self.oversized_cluster is not None:
            result['OversizedCluster'] = self.oversized_cluster
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.extend_configs = []
        if m.get('ExtendConfigs') is not None:
            for k in m.get('ExtendConfigs'):
                temp_model = CapacityPlanResponseBodyResultExtendConfigs()
                self.extend_configs.append(temp_model.from_map(k))
        if m.get('InstanceCategory') is not None:
            self.instance_category = m.get('InstanceCategory')
        self.node_configurations = []
        if m.get('NodeConfigurations') is not None:
            for k in m.get('NodeConfigurations'):
                temp_model = CapacityPlanResponseBodyResultNodeConfigurations()
                self.node_configurations.append(temp_model.from_map(k))
        if m.get('OversizedCluster') is not None:
            self.oversized_cluster = m.get('OversizedCluster')
        return self


class CapacityPlanResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: CapacityPlanResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = CapacityPlanResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class CapacityPlanResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CapacityPlanResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CapacityPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CloseDiagnosisRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        lang: str = None,
    ):
        self.client_token = client_token
        self.lang = lang

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.lang is not None:
            result['lang'] = self.lang
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('lang') is not None:
            self.lang = m.get('lang')
        return self


class CloseDiagnosisResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class CloseDiagnosisResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CloseDiagnosisResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CloseDiagnosisResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CloseHttpsRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
    ):
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        return self


class CloseHttpsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class CloseHttpsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CloseHttpsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CloseHttpsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CloseManagedIndexRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
    ):
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class CloseManagedIndexResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class CloseManagedIndexResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CloseManagedIndexResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CloseManagedIndexResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCollectorRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
    ):
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        return self


class CreateCollectorResponseBodyResult(TeaModel):
    def __init__(
        self,
        res_id: str = None,
    ):
        self.res_id = res_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.res_id is not None:
            result['resId'] = self.res_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('resId') is not None:
            self.res_id = m.get('resId')
        return self


class CreateCollectorResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: CreateCollectorResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = CreateCollectorResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class CreateCollectorResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateCollectorResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateCollectorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateComponentIndexRequestTemplate(TeaModel):
    def __init__(
        self,
        aliases: Dict[str, Any] = None,
        mappings: Dict[str, Any] = None,
        settings: Dict[str, Any] = None,
    ):
        self.aliases = aliases
        self.mappings = mappings
        self.settings = settings

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aliases is not None:
            result['aliases'] = self.aliases
        if self.mappings is not None:
            result['mappings'] = self.mappings
        if self.settings is not None:
            result['settings'] = self.settings
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('aliases') is not None:
            self.aliases = m.get('aliases')
        if m.get('mappings') is not None:
            self.mappings = m.get('mappings')
        if m.get('settings') is not None:
            self.settings = m.get('settings')
        return self


class CreateComponentIndexRequest(TeaModel):
    def __init__(
        self,
        meta: Dict[str, Any] = None,
        template: CreateComponentIndexRequestTemplate = None,
    ):
        self.meta = meta
        self.template = template

    def validate(self):
        if self.template:
            self.template.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.meta is not None:
            result['_meta'] = self.meta
        if self.template is not None:
            result['template'] = self.template.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('_meta') is not None:
            self.meta = m.get('_meta')
        if m.get('template') is not None:
            temp_model = CreateComponentIndexRequestTemplate()
            self.template = temp_model.from_map(m['template'])
        return self


class CreateComponentIndexResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class CreateComponentIndexResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateComponentIndexResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateComponentIndexResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDataStreamRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
    ):
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class CreateDataStreamResponseBodyResult(TeaModel):
    def __init__(
        self,
        name: str = None,
    ):
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class CreateDataStreamResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: CreateDataStreamResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = CreateDataStreamResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class CreateDataStreamResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateDataStreamResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateDataStreamResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDataTasksRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
    ):
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class CreateDataTasksResponseBodyResultSinkCluster(TeaModel):
    def __init__(
        self,
        data_source_type: str = None,
        index: str = None,
        mapping: str = None,
        password: str = None,
        routing: str = None,
        settings: str = None,
        type: str = None,
        username: str = None,
        vpc_id: str = None,
        vpc_instance_id: str = None,
        vpc_instance_port: str = None,
    ):
        self.data_source_type = data_source_type
        self.index = index
        self.mapping = mapping
        self.password = password
        self.routing = routing
        self.settings = settings
        self.type = type
        self.username = username
        self.vpc_id = vpc_id
        self.vpc_instance_id = vpc_instance_id
        self.vpc_instance_port = vpc_instance_port

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_source_type is not None:
            result['dataSourceType'] = self.data_source_type
        if self.index is not None:
            result['index'] = self.index
        if self.mapping is not None:
            result['mapping'] = self.mapping
        if self.password is not None:
            result['password'] = self.password
        if self.routing is not None:
            result['routing'] = self.routing
        if self.settings is not None:
            result['settings'] = self.settings
        if self.type is not None:
            result['type'] = self.type
        if self.username is not None:
            result['username'] = self.username
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
        if m.get('index') is not None:
            self.index = m.get('index')
        if m.get('mapping') is not None:
            self.mapping = m.get('mapping')
        if m.get('password') is not None:
            self.password = m.get('password')
        if m.get('routing') is not None:
            self.routing = m.get('routing')
        if m.get('settings') is not None:
            self.settings = m.get('settings')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('username') is not None:
            self.username = m.get('username')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        if m.get('vpcInstanceId') is not None:
            self.vpc_instance_id = m.get('vpcInstanceId')
        if m.get('vpcInstancePort') is not None:
            self.vpc_instance_port = m.get('vpcInstancePort')
        return self


class CreateDataTasksResponseBodyResultSourceCluster(TeaModel):
    def __init__(
        self,
        data_source_type: str = None,
        endpoint: str = None,
        index: str = None,
        password: str = None,
        type: str = None,
        username: str = None,
        vpc_id: str = None,
        vpc_instance_id: str = None,
        vpc_instance_port: int = None,
    ):
        self.data_source_type = data_source_type
        self.endpoint = endpoint
        self.index = index
        self.password = password
        self.type = type
        self.username = username
        self.vpc_id = vpc_id
        self.vpc_instance_id = vpc_instance_id
        self.vpc_instance_port = vpc_instance_port

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_source_type is not None:
            result['dataSourceType'] = self.data_source_type
        if self.endpoint is not None:
            result['endpoint'] = self.endpoint
        if self.index is not None:
            result['index'] = self.index
        if self.password is not None:
            result['password'] = self.password
        if self.type is not None:
            result['type'] = self.type
        if self.username is not None:
            result['username'] = self.username
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
        if m.get('password') is not None:
            self.password = m.get('password')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('username') is not None:
            self.username = m.get('username')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        if m.get('vpcInstanceId') is not None:
            self.vpc_instance_id = m.get('vpcInstanceId')
        if m.get('vpcInstancePort') is not None:
            self.vpc_instance_port = m.get('vpcInstancePort')
        return self


class CreateDataTasksResponseBodyResult(TeaModel):
    def __init__(
        self,
        sink_cluster: CreateDataTasksResponseBodyResultSinkCluster = None,
        source_cluster: CreateDataTasksResponseBodyResultSourceCluster = None,
    ):
        self.sink_cluster = sink_cluster
        self.source_cluster = source_cluster

    def validate(self):
        if self.sink_cluster:
            self.sink_cluster.validate()
        if self.source_cluster:
            self.source_cluster.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sink_cluster is not None:
            result['sinkCluster'] = self.sink_cluster.to_map()
        if self.source_cluster is not None:
            result['sourceCluster'] = self.source_cluster.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('sinkCluster') is not None:
            temp_model = CreateDataTasksResponseBodyResultSinkCluster()
            self.sink_cluster = temp_model.from_map(m['sinkCluster'])
        if m.get('sourceCluster') is not None:
            temp_model = CreateDataTasksResponseBodyResultSourceCluster()
            self.source_cluster = temp_model.from_map(m['sourceCluster'])
        return self


class CreateDataTasksResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[CreateDataTasksResponseBodyResult] = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = CreateDataTasksResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class CreateDataTasksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateDataTasksResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateDataTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateILMPolicyRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
    ):
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class CreateILMPolicyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: str = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class CreateILMPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateILMPolicyResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateILMPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateIndexTemplateRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
    ):
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class CreateIndexTemplateResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: str = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class CreateIndexTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateIndexTemplateResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateIndexTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateLogstashRequestNetworkConfig(TeaModel):
    def __init__(
        self,
        type: str = None,
        vpc_id: str = None,
        vs_area: str = None,
        vswitch_id: str = None,
    ):
        self.type = type
        self.vpc_id = vpc_id
        self.vs_area = vs_area
        self.vswitch_id = vswitch_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['type'] = self.type
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        if self.vs_area is not None:
            result['vsArea'] = self.vs_area
        if self.vswitch_id is not None:
            result['vswitchId'] = self.vswitch_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        if m.get('vsArea') is not None:
            self.vs_area = m.get('vsArea')
        if m.get('vswitchId') is not None:
            self.vswitch_id = m.get('vswitchId')
        return self


class CreateLogstashRequestNodeSpec(TeaModel):
    def __init__(
        self,
        disk: int = None,
        disk_type: str = None,
        spec: str = None,
    ):
        self.disk = disk
        self.disk_type = disk_type
        self.spec = spec

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.disk is not None:
            result['disk'] = self.disk
        if self.disk_type is not None:
            result['diskType'] = self.disk_type
        if self.spec is not None:
            result['spec'] = self.spec
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('disk') is not None:
            self.disk = m.get('disk')
        if m.get('diskType') is not None:
            self.disk_type = m.get('diskType')
        if m.get('spec') is not None:
            self.spec = m.get('spec')
        return self


class CreateLogstashRequestPaymentInfo(TeaModel):
    def __init__(
        self,
        auto_renew_duration: int = None,
        duration: int = None,
        is_auto_renew: bool = None,
        pricing_cycle: str = None,
    ):
        # 自动续费包月周期
        self.auto_renew_duration = auto_renew_duration
        # 包月周期
        self.duration = duration
        # 是否自动续费
        self.is_auto_renew = is_auto_renew
        # 日期单位
        self.pricing_cycle = pricing_cycle

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_renew_duration is not None:
            result['autoRenewDuration'] = self.auto_renew_duration
        if self.duration is not None:
            result['duration'] = self.duration
        if self.is_auto_renew is not None:
            result['isAutoRenew'] = self.is_auto_renew
        if self.pricing_cycle is not None:
            result['pricingCycle'] = self.pricing_cycle
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('autoRenewDuration') is not None:
            self.auto_renew_duration = m.get('autoRenewDuration')
        if m.get('duration') is not None:
            self.duration = m.get('duration')
        if m.get('isAutoRenew') is not None:
            self.is_auto_renew = m.get('isAutoRenew')
        if m.get('pricingCycle') is not None:
            self.pricing_cycle = m.get('pricingCycle')
        return self


class CreateLogstashRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        network_config: CreateLogstashRequestNetworkConfig = None,
        node_amount: int = None,
        node_spec: CreateLogstashRequestNodeSpec = None,
        payment_info: CreateLogstashRequestPaymentInfo = None,
        payment_type: str = None,
        version: str = None,
        client_token: str = None,
    ):
        self.description = description
        self.network_config = network_config
        self.node_amount = node_amount
        self.node_spec = node_spec
        self.payment_info = payment_info
        self.payment_type = payment_type
        self.version = version
        self.client_token = client_token

    def validate(self):
        if self.network_config:
            self.network_config.validate()
        if self.node_spec:
            self.node_spec.validate()
        if self.payment_info:
            self.payment_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.network_config is not None:
            result['networkConfig'] = self.network_config.to_map()
        if self.node_amount is not None:
            result['nodeAmount'] = self.node_amount
        if self.node_spec is not None:
            result['nodeSpec'] = self.node_spec.to_map()
        if self.payment_info is not None:
            result['paymentInfo'] = self.payment_info.to_map()
        if self.payment_type is not None:
            result['paymentType'] = self.payment_type
        if self.version is not None:
            result['version'] = self.version
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('networkConfig') is not None:
            temp_model = CreateLogstashRequestNetworkConfig()
            self.network_config = temp_model.from_map(m['networkConfig'])
        if m.get('nodeAmount') is not None:
            self.node_amount = m.get('nodeAmount')
        if m.get('nodeSpec') is not None:
            temp_model = CreateLogstashRequestNodeSpec()
            self.node_spec = temp_model.from_map(m['nodeSpec'])
        if m.get('paymentInfo') is not None:
            temp_model = CreateLogstashRequestPaymentInfo()
            self.payment_info = temp_model.from_map(m['paymentInfo'])
        if m.get('paymentType') is not None:
            self.payment_type = m.get('paymentType')
        if m.get('version') is not None:
            self.version = m.get('version')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        return self


class CreateLogstashResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: Logstash = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = Logstash()
            self.result = temp_model.from_map(m['Result'])
        return self


class CreateLogstashResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateLogstashResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateLogstashResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatePipelinesRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        trigger: bool = None,
    ):
        self.client_token = client_token
        self.trigger = trigger

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.trigger is not None:
            result['trigger'] = self.trigger
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('trigger') is not None:
            self.trigger = m.get('trigger')
        return self


class CreatePipelinesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class CreatePipelinesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreatePipelinesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreatePipelinesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSnapshotRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
    ):
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class CreateSnapshotResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class CreateSnapshotResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateSnapshotResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateSnapshotResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateVpcEndpointRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        service_id: str = None,
        zone_id: str = None,
        dry_run: bool = None,
    ):
        self.client_token = client_token
        # 终端节点服务ID
        self.service_id = service_id
        # 可用区ID
        self.zone_id = zone_id
        self.dry_run = dry_run

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.service_id is not None:
            result['serviceId'] = self.service_id
        if self.zone_id is not None:
            result['zoneId'] = self.zone_id
        if self.dry_run is not None:
            result['dryRun'] = self.dry_run
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('serviceId') is not None:
            self.service_id = m.get('serviceId')
        if m.get('zoneId') is not None:
            self.zone_id = m.get('zoneId')
        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')
        return self


class CreateVpcEndpointResponseBodyResult(TeaModel):
    def __init__(
        self,
        endpoint_domain: str = None,
        endpoint_id: str = None,
        endpoint_name: str = None,
        service_id: str = None,
    ):
        self.endpoint_domain = endpoint_domain
        self.endpoint_id = endpoint_id
        self.endpoint_name = endpoint_name
        self.service_id = service_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint_domain is not None:
            result['endpointDomain'] = self.endpoint_domain
        if self.endpoint_id is not None:
            result['endpointId'] = self.endpoint_id
        if self.endpoint_name is not None:
            result['endpointName'] = self.endpoint_name
        if self.service_id is not None:
            result['serviceId'] = self.service_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endpointDomain') is not None:
            self.endpoint_domain = m.get('endpointDomain')
        if m.get('endpointId') is not None:
            self.endpoint_id = m.get('endpointId')
        if m.get('endpointName') is not None:
            self.endpoint_name = m.get('endpointName')
        if m.get('serviceId') is not None:
            self.service_id = m.get('serviceId')
        return self


class CreateVpcEndpointResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: CreateVpcEndpointResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = CreateVpcEndpointResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class CreateVpcEndpointResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateVpcEndpointResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateVpcEndpointResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeactivateZonesRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
    ):
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        return self


class DeactivateZonesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class DeactivateZonesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeactivateZonesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeactivateZonesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteCollectorRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
    ):
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class DeleteCollectorResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class DeleteCollectorResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteCollectorResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteCollectorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteComponentIndexResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class DeleteComponentIndexResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteComponentIndexResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteComponentIndexResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteConnectedClusterRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        connected_instance_id: str = None,
    ):
        self.client_token = client_token
        self.connected_instance_id = connected_instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.connected_instance_id is not None:
            result['connectedInstanceId'] = self.connected_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('connectedInstanceId') is not None:
            self.connected_instance_id = m.get('connectedInstanceId')
        return self


class DeleteConnectedClusterResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class DeleteConnectedClusterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteConnectedClusterResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteConnectedClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDataStreamRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
    ):
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class DeleteDataStreamResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class DeleteDataStreamResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteDataStreamResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteDataStreamResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDataTaskRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        task_id: str = None,
    ):
        self.client_token = client_token
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.task_id is not None:
            result['taskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        return self


class DeleteDataTaskResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class DeleteDataTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteDataTaskResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteDataTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDeprecatedTemplateResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class DeleteDeprecatedTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteDeprecatedTemplateResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteDeprecatedTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteILMPolicyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class DeleteILMPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteILMPolicyResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteILMPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteIndexTemplateResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class DeleteIndexTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteIndexTemplateResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteIndexTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteInstanceRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        delete_type: str = None,
    ):
        self.client_token = client_token
        self.delete_type = delete_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.delete_type is not None:
            result['deleteType'] = self.delete_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('deleteType') is not None:
            self.delete_type = m.get('deleteType')
        return self


class DeleteInstanceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteInstanceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteLogstashRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        delete_type: str = None,
    ):
        self.client_token = client_token
        self.delete_type = delete_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.delete_type is not None:
            result['deleteType'] = self.delete_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('deleteType') is not None:
            self.delete_type = m.get('deleteType')
        return self


class DeleteLogstashResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteLogstashResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteLogstashResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteLogstashResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeletePipelinesRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        pipeline_ids: str = None,
    ):
        self.client_token = client_token
        self.pipeline_ids = pipeline_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.pipeline_ids is not None:
            result['pipelineIds'] = self.pipeline_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('pipelineIds') is not None:
            self.pipeline_ids = m.get('pipelineIds')
        return self


class DeletePipelinesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class DeletePipelinesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeletePipelinesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeletePipelinesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSnapshotRepoRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        repo_path: str = None,
    ):
        self.client_token = client_token
        self.repo_path = repo_path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.repo_path is not None:
            result['repoPath'] = self.repo_path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('repoPath') is not None:
            self.repo_path = m.get('repoPath')
        return self


class DeleteSnapshotRepoResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class DeleteSnapshotRepoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteSnapshotRepoResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteSnapshotRepoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteVpcEndpointRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
    ):
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class DeleteVpcEndpointResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class DeleteVpcEndpointResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteVpcEndpointResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteVpcEndpointResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAckOperatorResponseBodyResult(TeaModel):
    def __init__(
        self,
        status: str = None,
        version: str = None,
    ):
        self.status = status
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['status'] = self.status
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class DescribeAckOperatorResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: DescribeAckOperatorResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = DescribeAckOperatorResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class DescribeAckOperatorResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeAckOperatorResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeAckOperatorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeApmResponseBodyResult(TeaModel):
    def __init__(
        self,
        apm_server_domain: str = None,
        created_at: str = None,
        deployed_replica: int = None,
        description: str = None,
        end_time: int = None,
        instance_id: str = None,
        node_amount: int = None,
        output_es: str = None,
        output_esuser_name: str = None,
        owner_id: str = None,
        payment_type: str = None,
        region: str = None,
        replica: int = None,
        resource_spec: str = None,
        status: str = None,
        version: str = None,
        vpc_id: str = None,
        vs_area: str = None,
        vswitch_id: str = None,
    ):
        self.apm_server_domain = apm_server_domain
        self.created_at = created_at
        self.deployed_replica = deployed_replica
        self.description = description
        self.end_time = end_time
        self.instance_id = instance_id
        self.node_amount = node_amount
        self.output_es = output_es
        self.output_esuser_name = output_esuser_name
        self.owner_id = owner_id
        self.payment_type = payment_type
        self.region = region
        self.replica = replica
        self.resource_spec = resource_spec
        self.status = status
        self.version = version
        self.vpc_id = vpc_id
        self.vs_area = vs_area
        self.vswitch_id = vswitch_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apm_server_domain is not None:
            result['apmServerDomain'] = self.apm_server_domain
        if self.created_at is not None:
            result['createdAt'] = self.created_at
        if self.deployed_replica is not None:
            result['deployedReplica'] = self.deployed_replica
        if self.description is not None:
            result['description'] = self.description
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.node_amount is not None:
            result['nodeAmount'] = self.node_amount
        if self.output_es is not None:
            result['outputES'] = self.output_es
        if self.output_esuser_name is not None:
            result['outputESUserName'] = self.output_esuser_name
        if self.owner_id is not None:
            result['ownerId'] = self.owner_id
        if self.payment_type is not None:
            result['paymentType'] = self.payment_type
        if self.region is not None:
            result['region'] = self.region
        if self.replica is not None:
            result['replica'] = self.replica
        if self.resource_spec is not None:
            result['resourceSpec'] = self.resource_spec
        if self.status is not None:
            result['status'] = self.status
        if self.version is not None:
            result['version'] = self.version
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        if self.vs_area is not None:
            result['vsArea'] = self.vs_area
        if self.vswitch_id is not None:
            result['vswitchId'] = self.vswitch_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apmServerDomain') is not None:
            self.apm_server_domain = m.get('apmServerDomain')
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')
        if m.get('deployedReplica') is not None:
            self.deployed_replica = m.get('deployedReplica')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('nodeAmount') is not None:
            self.node_amount = m.get('nodeAmount')
        if m.get('outputES') is not None:
            self.output_es = m.get('outputES')
        if m.get('outputESUserName') is not None:
            self.output_esuser_name = m.get('outputESUserName')
        if m.get('ownerId') is not None:
            self.owner_id = m.get('ownerId')
        if m.get('paymentType') is not None:
            self.payment_type = m.get('paymentType')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('replica') is not None:
            self.replica = m.get('replica')
        if m.get('resourceSpec') is not None:
            self.resource_spec = m.get('resourceSpec')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('version') is not None:
            self.version = m.get('version')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        if m.get('vsArea') is not None:
            self.vs_area = m.get('vsArea')
        if m.get('vswitchId') is not None:
            self.vswitch_id = m.get('vswitchId')
        return self


class DescribeApmResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: DescribeApmResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = DescribeApmResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class DescribeApmResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeApmResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeApmResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCollectorResponseBodyResultConfigs(TeaModel):
    def __init__(
        self,
        content: str = None,
        file_name: str = None,
    ):
        self.content = content
        self.file_name = file_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class DescribeCollectorResponseBodyResultExtendConfigsMachines(TeaModel):
    def __init__(
        self,
        agent_status: str = None,
        instance_id: str = None,
    ):
        self.agent_status = agent_status
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class DescribeCollectorResponseBodyResultExtendConfigs(TeaModel):
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
        machines: List[DescribeCollectorResponseBodyResultExtendConfigsMachines] = None,
        protocol: str = None,
        success_pods_count: str = None,
        total_pods_count: str = None,
        type: str = None,
        user_name: str = None,
    ):
        self.config_type = config_type
        self.enable_monitoring = enable_monitoring
        self.group_id = group_id
        self.host = host
        self.hosts = hosts
        self.instance_id = instance_id
        self.instance_type = instance_type
        self.kibana_host = kibana_host
        self.machines = machines
        self.protocol = protocol
        self.success_pods_count = success_pods_count
        self.total_pods_count = total_pods_count
        self.type = type
        self.user_name = user_name

    def validate(self):
        if self.machines:
            for k in self.machines:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            for k in self.machines:
                result['machines'].append(k.to_map() if k else None)
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
            for k in m.get('machines'):
                temp_model = DescribeCollectorResponseBodyResultExtendConfigsMachines()
                self.machines.append(temp_model.from_map(k))
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


class DescribeCollectorResponseBodyResult(TeaModel):
    def __init__(
        self,
        collector_paths: List[str] = None,
        configs: List[DescribeCollectorResponseBodyResultConfigs] = None,
        dry_run: bool = None,
        extend_configs: List[DescribeCollectorResponseBodyResultExtendConfigs] = None,
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
        self.configs = configs
        self.dry_run = dry_run
        self.extend_configs = extend_configs
        self.gmt_created_time = gmt_created_time
        self.gmt_update_time = gmt_update_time
        self.name = name
        self.owner_id = owner_id
        self.res_id = res_id
        self.res_type = res_type
        self.res_version = res_version
        self.status = status
        self.vpc_id = vpc_id

    def validate(self):
        if self.configs:
            for k in self.configs:
                if k:
                    k.validate()
        if self.extend_configs:
            for k in self.extend_configs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.collector_paths is not None:
            result['collectorPaths'] = self.collector_paths
        result['configs'] = []
        if self.configs is not None:
            for k in self.configs:
                result['configs'].append(k.to_map() if k else None)
        if self.dry_run is not None:
            result['dryRun'] = self.dry_run
        result['extendConfigs'] = []
        if self.extend_configs is not None:
            for k in self.extend_configs:
                result['extendConfigs'].append(k.to_map() if k else None)
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
            for k in m.get('configs'):
                temp_model = DescribeCollectorResponseBodyResultConfigs()
                self.configs.append(temp_model.from_map(k))
        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')
        self.extend_configs = []
        if m.get('extendConfigs') is not None:
            for k in m.get('extendConfigs'):
                temp_model = DescribeCollectorResponseBodyResultExtendConfigs()
                self.extend_configs.append(temp_model.from_map(k))
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


class DescribeCollectorResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: DescribeCollectorResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = DescribeCollectorResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class DescribeCollectorResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeCollectorResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeCollectorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeComponentIndexResponseBodyResultTemplate(TeaModel):
    def __init__(
        self,
        aliases: Dict[str, Any] = None,
        mappings: Dict[str, Any] = None,
        settings: Dict[str, Any] = None,
    ):
        self.aliases = aliases
        self.mappings = mappings
        self.settings = settings

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aliases is not None:
            result['aliases'] = self.aliases
        if self.mappings is not None:
            result['mappings'] = self.mappings
        if self.settings is not None:
            result['settings'] = self.settings
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('aliases') is not None:
            self.aliases = m.get('aliases')
        if m.get('mappings') is not None:
            self.mappings = m.get('mappings')
        if m.get('settings') is not None:
            self.settings = m.get('settings')
        return self


class DescribeComponentIndexResponseBodyResult(TeaModel):
    def __init__(
        self,
        meta: Dict[str, Any] = None,
        template: DescribeComponentIndexResponseBodyResultTemplate = None,
    ):
        self.meta = meta
        self.template = template

    def validate(self):
        if self.template:
            self.template.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.meta is not None:
            result['_meta'] = self.meta
        if self.template is not None:
            result['template'] = self.template.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('_meta') is not None:
            self.meta = m.get('_meta')
        if m.get('template') is not None:
            temp_model = DescribeComponentIndexResponseBodyResultTemplate()
            self.template = temp_model.from_map(m['template'])
        return self


class DescribeComponentIndexResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: DescribeComponentIndexResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = DescribeComponentIndexResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class DescribeComponentIndexResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeComponentIndexResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeComponentIndexResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeConnectableClustersRequest(TeaModel):
    def __init__(
        self,
        already_set_items: bool = None,
    ):
        self.already_set_items = already_set_items

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.already_set_items is not None:
            result['alreadySetItems'] = self.already_set_items
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alreadySetItems') is not None:
            self.already_set_items = m.get('alreadySetItems')
        return self


class DescribeConnectableClustersResponseBodyResult(TeaModel):
    def __init__(
        self,
        instances: str = None,
        network_type: str = None,
    ):
        self.instances = instances
        self.network_type = network_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instances is not None:
            result['instances'] = self.instances
        if self.network_type is not None:
            result['networkType'] = self.network_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('instances') is not None:
            self.instances = m.get('instances')
        if m.get('networkType') is not None:
            self.network_type = m.get('networkType')
        return self


class DescribeConnectableClustersResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[DescribeConnectableClustersResponseBodyResult] = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = DescribeConnectableClustersResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class DescribeConnectableClustersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeConnectableClustersResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeConnectableClustersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDeprecatedTemplateResponseBodyResultTemplate(TeaModel):
    def __init__(
        self,
        aliases: str = None,
        mappings: str = None,
        settings: str = None,
    ):
        self.aliases = aliases
        self.mappings = mappings
        self.settings = settings

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aliases is not None:
            result['aliases'] = self.aliases
        if self.mappings is not None:
            result['mappings'] = self.mappings
        if self.settings is not None:
            result['settings'] = self.settings
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('aliases') is not None:
            self.aliases = m.get('aliases')
        if m.get('mappings') is not None:
            self.mappings = m.get('mappings')
        if m.get('settings') is not None:
            self.settings = m.get('settings')
        return self


class DescribeDeprecatedTemplateResponseBodyResult(TeaModel):
    def __init__(
        self,
        data_stream: bool = None,
        index_patterns: List[str] = None,
        index_template: str = None,
        order: int = None,
        template: DescribeDeprecatedTemplateResponseBodyResultTemplate = None,
        version: str = None,
    ):
        self.data_stream = data_stream
        self.index_patterns = index_patterns
        self.index_template = index_template
        self.order = order
        self.template = template
        self.version = version

    def validate(self):
        if self.template:
            self.template.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_stream is not None:
            result['dataStream'] = self.data_stream
        if self.index_patterns is not None:
            result['indexPatterns'] = self.index_patterns
        if self.index_template is not None:
            result['indexTemplate'] = self.index_template
        if self.order is not None:
            result['order'] = self.order
        if self.template is not None:
            result['template'] = self.template.to_map()
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dataStream') is not None:
            self.data_stream = m.get('dataStream')
        if m.get('indexPatterns') is not None:
            self.index_patterns = m.get('indexPatterns')
        if m.get('indexTemplate') is not None:
            self.index_template = m.get('indexTemplate')
        if m.get('order') is not None:
            self.order = m.get('order')
        if m.get('template') is not None:
            temp_model = DescribeDeprecatedTemplateResponseBodyResultTemplate()
            self.template = temp_model.from_map(m['template'])
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class DescribeDeprecatedTemplateResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: DescribeDeprecatedTemplateResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = DescribeDeprecatedTemplateResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class DescribeDeprecatedTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDeprecatedTemplateResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeDeprecatedTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDiagnoseReportRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
    ):
        self.lang = lang

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['lang'] = self.lang
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('lang') is not None:
            self.lang = m.get('lang')
        return self


class DescribeDiagnoseReportResponseBodyResultDiagnoseItemsDetail(TeaModel):
    def __init__(
        self,
        desc: str = None,
        name: str = None,
        result: str = None,
        suggest: str = None,
        type: str = None,
    ):
        self.desc = desc
        self.name = name
        self.result = result
        self.suggest = suggest
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.desc is not None:
            result['desc'] = self.desc
        if self.name is not None:
            result['name'] = self.name
        if self.result is not None:
            result['result'] = self.result
        if self.suggest is not None:
            result['suggest'] = self.suggest
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('desc') is not None:
            self.desc = m.get('desc')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('result') is not None:
            self.result = m.get('result')
        if m.get('suggest') is not None:
            self.suggest = m.get('suggest')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class DescribeDiagnoseReportResponseBodyResultDiagnoseItems(TeaModel):
    def __init__(
        self,
        detail: DescribeDiagnoseReportResponseBodyResultDiagnoseItemsDetail = None,
        health: str = None,
        item: str = None,
    ):
        self.detail = detail
        self.health = health
        self.item = item

    def validate(self):
        if self.detail:
            self.detail.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.detail is not None:
            result['detail'] = self.detail.to_map()
        if self.health is not None:
            result['health'] = self.health
        if self.item is not None:
            result['item'] = self.item
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('detail') is not None:
            temp_model = DescribeDiagnoseReportResponseBodyResultDiagnoseItemsDetail()
            self.detail = temp_model.from_map(m['detail'])
        if m.get('health') is not None:
            self.health = m.get('health')
        if m.get('item') is not None:
            self.item = m.get('item')
        return self


class DescribeDiagnoseReportResponseBodyResult(TeaModel):
    def __init__(
        self,
        create_time: int = None,
        diagnose_items: List[DescribeDiagnoseReportResponseBodyResultDiagnoseItems] = None,
        health: str = None,
        instance_id: str = None,
        report_id: str = None,
        state: str = None,
        trigger: str = None,
    ):
        self.create_time = create_time
        self.diagnose_items = diagnose_items
        self.health = health
        self.instance_id = instance_id
        self.report_id = report_id
        self.state = state
        self.trigger = trigger

    def validate(self):
        if self.diagnose_items:
            for k in self.diagnose_items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        result['diagnoseItems'] = []
        if self.diagnose_items is not None:
            for k in self.diagnose_items:
                result['diagnoseItems'].append(k.to_map() if k else None)
        if self.health is not None:
            result['health'] = self.health
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.report_id is not None:
            result['reportId'] = self.report_id
        if self.state is not None:
            result['state'] = self.state
        if self.trigger is not None:
            result['trigger'] = self.trigger
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        self.diagnose_items = []
        if m.get('diagnoseItems') is not None:
            for k in m.get('diagnoseItems'):
                temp_model = DescribeDiagnoseReportResponseBodyResultDiagnoseItems()
                self.diagnose_items.append(temp_model.from_map(k))
        if m.get('health') is not None:
            self.health = m.get('health')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('reportId') is not None:
            self.report_id = m.get('reportId')
        if m.get('state') is not None:
            self.state = m.get('state')
        if m.get('trigger') is not None:
            self.trigger = m.get('trigger')
        return self


class DescribeDiagnoseReportResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: DescribeDiagnoseReportResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = DescribeDiagnoseReportResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class DescribeDiagnoseReportResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDiagnoseReportResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeDiagnoseReportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDiagnosisSettingsRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
    ):
        self.lang = lang

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['lang'] = self.lang
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('lang') is not None:
            self.lang = m.get('lang')
        return self


class DescribeDiagnosisSettingsResponseBodyResult(TeaModel):
    def __init__(
        self,
        scene: str = None,
        update_time: int = None,
    ):
        self.scene = scene
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scene is not None:
            result['scene'] = self.scene
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('scene') is not None:
            self.scene = m.get('scene')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        return self


class DescribeDiagnosisSettingsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: DescribeDiagnosisSettingsResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = DescribeDiagnosisSettingsResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class DescribeDiagnosisSettingsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDiagnosisSettingsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeDiagnosisSettingsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeElasticsearchHealthResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class DescribeElasticsearchHealthResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeElasticsearchHealthResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeElasticsearchHealthResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeILMPolicyResponseBodyResult(TeaModel):
    def __init__(
        self,
        name: str = None,
        phases: Dict[str, Any] = None,
    ):
        self.name = name
        self.phases = phases

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.phases is not None:
            result['phases'] = self.phases
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('phases') is not None:
            self.phases = m.get('phases')
        return self


class DescribeILMPolicyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: DescribeILMPolicyResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = DescribeILMPolicyResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class DescribeILMPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeILMPolicyResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeILMPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeIndexTemplateResponseBodyResultTemplate(TeaModel):
    def __init__(
        self,
        aliases: str = None,
        mappings: str = None,
        settings: str = None,
    ):
        self.aliases = aliases
        self.mappings = mappings
        self.settings = settings

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aliases is not None:
            result['aliases'] = self.aliases
        if self.mappings is not None:
            result['mappings'] = self.mappings
        if self.settings is not None:
            result['settings'] = self.settings
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('aliases') is not None:
            self.aliases = m.get('aliases')
        if m.get('mappings') is not None:
            self.mappings = m.get('mappings')
        if m.get('settings') is not None:
            self.settings = m.get('settings')
        return self


class DescribeIndexTemplateResponseBodyResult(TeaModel):
    def __init__(
        self,
        data_stream: bool = None,
        ilm_policy: str = None,
        index_patterns: List[str] = None,
        index_template: str = None,
        priority: int = None,
        template: DescribeIndexTemplateResponseBodyResultTemplate = None,
    ):
        self.data_stream = data_stream
        self.ilm_policy = ilm_policy
        self.index_patterns = index_patterns
        self.index_template = index_template
        self.priority = priority
        self.template = template

    def validate(self):
        if self.template:
            self.template.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_stream is not None:
            result['dataStream'] = self.data_stream
        if self.ilm_policy is not None:
            result['ilmPolicy'] = self.ilm_policy
        if self.index_patterns is not None:
            result['indexPatterns'] = self.index_patterns
        if self.index_template is not None:
            result['indexTemplate'] = self.index_template
        if self.priority is not None:
            result['priority'] = self.priority
        if self.template is not None:
            result['template'] = self.template.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dataStream') is not None:
            self.data_stream = m.get('dataStream')
        if m.get('ilmPolicy') is not None:
            self.ilm_policy = m.get('ilmPolicy')
        if m.get('indexPatterns') is not None:
            self.index_patterns = m.get('indexPatterns')
        if m.get('indexTemplate') is not None:
            self.index_template = m.get('indexTemplate')
        if m.get('priority') is not None:
            self.priority = m.get('priority')
        if m.get('template') is not None:
            temp_model = DescribeIndexTemplateResponseBodyResultTemplate()
            self.template = temp_model.from_map(m['template'])
        return self


class DescribeIndexTemplateResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: DescribeIndexTemplateResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = DescribeIndexTemplateResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class DescribeIndexTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeIndexTemplateResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeIndexTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstanceResponseBodyResultAdvancedSetting(TeaModel):
    def __init__(
        self,
        gc_name: str = None,
    ):
        self.gc_name = gc_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gc_name is not None:
            result['gcName'] = self.gc_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('gcName') is not None:
            self.gc_name = m.get('gcName')
        return self


class DescribeInstanceResponseBodyResultAliwsDicts(TeaModel):
    def __init__(
        self,
        file_size: int = None,
        name: str = None,
        source_type: str = None,
        type: str = None,
    ):
        self.file_size = file_size
        self.name = name
        self.source_type = source_type
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_size is not None:
            result['fileSize'] = self.file_size
        if self.name is not None:
            result['name'] = self.name
        if self.source_type is not None:
            result['sourceType'] = self.source_type
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fileSize') is not None:
            self.file_size = m.get('fileSize')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class DescribeInstanceResponseBodyResultClientNodeConfiguration(TeaModel):
    def __init__(
        self,
        amount: int = None,
        disk: int = None,
        disk_type: str = None,
        spec: str = None,
    ):
        self.amount = amount
        self.disk = disk
        self.disk_type = disk_type
        self.spec = spec

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.amount is not None:
            result['amount'] = self.amount
        if self.disk is not None:
            result['disk'] = self.disk
        if self.disk_type is not None:
            result['diskType'] = self.disk_type
        if self.spec is not None:
            result['spec'] = self.spec
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('amount') is not None:
            self.amount = m.get('amount')
        if m.get('disk') is not None:
            self.disk = m.get('disk')
        if m.get('diskType') is not None:
            self.disk_type = m.get('diskType')
        if m.get('spec') is not None:
            self.spec = m.get('spec')
        return self


class DescribeInstanceResponseBodyResultDictList(TeaModel):
    def __init__(
        self,
        file_size: int = None,
        name: str = None,
        source_type: str = None,
        type: str = None,
    ):
        self.file_size = file_size
        self.name = name
        self.source_type = source_type
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_size is not None:
            result['fileSize'] = self.file_size
        if self.name is not None:
            result['name'] = self.name
        if self.source_type is not None:
            result['sourceType'] = self.source_type
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fileSize') is not None:
            self.file_size = m.get('fileSize')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class DescribeInstanceResponseBodyResultElasticDataNodeConfiguration(TeaModel):
    def __init__(
        self,
        amount: int = None,
        disk: int = None,
        disk_encryption: bool = None,
        disk_type: str = None,
        spec: str = None,
    ):
        self.amount = amount
        self.disk = disk
        self.disk_encryption = disk_encryption
        self.disk_type = disk_type
        self.spec = spec

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.amount is not None:
            result['amount'] = self.amount
        if self.disk is not None:
            result['disk'] = self.disk
        if self.disk_encryption is not None:
            result['diskEncryption'] = self.disk_encryption
        if self.disk_type is not None:
            result['diskType'] = self.disk_type
        if self.spec is not None:
            result['spec'] = self.spec
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('amount') is not None:
            self.amount = m.get('amount')
        if m.get('disk') is not None:
            self.disk = m.get('disk')
        if m.get('diskEncryption') is not None:
            self.disk_encryption = m.get('diskEncryption')
        if m.get('diskType') is not None:
            self.disk_type = m.get('diskType')
        if m.get('spec') is not None:
            self.spec = m.get('spec')
        return self


class DescribeInstanceResponseBodyResultKibanaConfiguration(TeaModel):
    def __init__(
        self,
        amount: int = None,
        spec: str = None,
    ):
        self.amount = amount
        self.spec = spec

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.amount is not None:
            result['amount'] = self.amount
        if self.spec is not None:
            result['spec'] = self.spec
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('amount') is not None:
            self.amount = m.get('amount')
        if m.get('spec') is not None:
            self.spec = m.get('spec')
        return self


class DescribeInstanceResponseBodyResultMasterConfiguration(TeaModel):
    def __init__(
        self,
        amount: int = None,
        disk: int = None,
        disk_type: str = None,
        spec: str = None,
    ):
        self.amount = amount
        self.disk = disk
        self.disk_type = disk_type
        self.spec = spec

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.amount is not None:
            result['amount'] = self.amount
        if self.disk is not None:
            result['disk'] = self.disk
        if self.disk_type is not None:
            result['diskType'] = self.disk_type
        if self.spec is not None:
            result['spec'] = self.spec
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('amount') is not None:
            self.amount = m.get('amount')
        if m.get('disk') is not None:
            self.disk = m.get('disk')
        if m.get('diskType') is not None:
            self.disk_type = m.get('diskType')
        if m.get('spec') is not None:
            self.spec = m.get('spec')
        return self


class DescribeInstanceResponseBodyResultNetworkConfigWhiteIpGroupList(TeaModel):
    def __init__(
        self,
        group_name: str = None,
        ips: List[str] = None,
        white_ip_type: str = None,
    ):
        self.group_name = group_name
        self.ips = ips
        self.white_ip_type = white_ip_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_name is not None:
            result['groupName'] = self.group_name
        if self.ips is not None:
            result['ips'] = self.ips
        if self.white_ip_type is not None:
            result['whiteIpType'] = self.white_ip_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('groupName') is not None:
            self.group_name = m.get('groupName')
        if m.get('ips') is not None:
            self.ips = m.get('ips')
        if m.get('whiteIpType') is not None:
            self.white_ip_type = m.get('whiteIpType')
        return self


class DescribeInstanceResponseBodyResultNetworkConfig(TeaModel):
    def __init__(
        self,
        type: str = None,
        vpc_id: str = None,
        vs_area: str = None,
        vswitch_id: str = None,
        white_ip_group_list: List[DescribeInstanceResponseBodyResultNetworkConfigWhiteIpGroupList] = None,
    ):
        self.type = type
        self.vpc_id = vpc_id
        self.vs_area = vs_area
        self.vswitch_id = vswitch_id
        self.white_ip_group_list = white_ip_group_list

    def validate(self):
        if self.white_ip_group_list:
            for k in self.white_ip_group_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['type'] = self.type
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        if self.vs_area is not None:
            result['vsArea'] = self.vs_area
        if self.vswitch_id is not None:
            result['vswitchId'] = self.vswitch_id
        result['whiteIpGroupList'] = []
        if self.white_ip_group_list is not None:
            for k in self.white_ip_group_list:
                result['whiteIpGroupList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        if m.get('vsArea') is not None:
            self.vs_area = m.get('vsArea')
        if m.get('vswitchId') is not None:
            self.vswitch_id = m.get('vswitchId')
        self.white_ip_group_list = []
        if m.get('whiteIpGroupList') is not None:
            for k in m.get('whiteIpGroupList'):
                temp_model = DescribeInstanceResponseBodyResultNetworkConfigWhiteIpGroupList()
                self.white_ip_group_list.append(temp_model.from_map(k))
        return self


class DescribeInstanceResponseBodyResultNodeSpec(TeaModel):
    def __init__(
        self,
        disk: int = None,
        disk_encryption: bool = None,
        disk_type: str = None,
        spec: str = None,
    ):
        self.disk = disk
        self.disk_encryption = disk_encryption
        self.disk_type = disk_type
        self.spec = spec

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.disk is not None:
            result['disk'] = self.disk
        if self.disk_encryption is not None:
            result['diskEncryption'] = self.disk_encryption
        if self.disk_type is not None:
            result['diskType'] = self.disk_type
        if self.spec is not None:
            result['spec'] = self.spec
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('disk') is not None:
            self.disk = m.get('disk')
        if m.get('diskEncryption') is not None:
            self.disk_encryption = m.get('diskEncryption')
        if m.get('diskType') is not None:
            self.disk_type = m.get('diskType')
        if m.get('spec') is not None:
            self.spec = m.get('spec')
        return self


class DescribeInstanceResponseBodyResultSynonymsDicts(TeaModel):
    def __init__(
        self,
        file_size: int = None,
        name: str = None,
        source_type: str = None,
        type: str = None,
    ):
        self.file_size = file_size
        self.name = name
        self.source_type = source_type
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_size is not None:
            result['fileSize'] = self.file_size
        if self.name is not None:
            result['name'] = self.name
        if self.source_type is not None:
            result['sourceType'] = self.source_type
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fileSize') is not None:
            self.file_size = m.get('fileSize')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class DescribeInstanceResponseBodyResultTags(TeaModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        self.tag_key = tag_key
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_key is not None:
            result['tagKey'] = self.tag_key
        if self.tag_value is not None:
            result['tagValue'] = self.tag_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('tagKey') is not None:
            self.tag_key = m.get('tagKey')
        if m.get('tagValue') is not None:
            self.tag_value = m.get('tagValue')
        return self


class DescribeInstanceResponseBodyResultWarmNodeConfiguration(TeaModel):
    def __init__(
        self,
        amount: int = None,
        disk: int = None,
        disk_encryption: bool = None,
        disk_type: str = None,
        spec: str = None,
    ):
        self.amount = amount
        self.disk = disk
        self.disk_encryption = disk_encryption
        self.disk_type = disk_type
        self.spec = spec

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.amount is not None:
            result['amount'] = self.amount
        if self.disk is not None:
            result['disk'] = self.disk
        if self.disk_encryption is not None:
            result['diskEncryption'] = self.disk_encryption
        if self.disk_type is not None:
            result['diskType'] = self.disk_type
        if self.spec is not None:
            result['spec'] = self.spec
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('amount') is not None:
            self.amount = m.get('amount')
        if m.get('disk') is not None:
            self.disk = m.get('disk')
        if m.get('diskEncryption') is not None:
            self.disk_encryption = m.get('diskEncryption')
        if m.get('diskType') is not None:
            self.disk_type = m.get('diskType')
        if m.get('spec') is not None:
            self.spec = m.get('spec')
        return self


class DescribeInstanceResponseBodyResultZoneInfos(TeaModel):
    def __init__(
        self,
        status: str = None,
        zone_id: str = None,
    ):
        self.status = status
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['status'] = self.status
        if self.zone_id is not None:
            result['zoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('zoneId') is not None:
            self.zone_id = m.get('zoneId')
        return self


class DescribeInstanceResponseBodyResult(TeaModel):
    def __init__(
        self,
        advanced_dedicate_master: bool = None,
        advanced_setting: DescribeInstanceResponseBodyResultAdvancedSetting = None,
        aliws_dicts: List[DescribeInstanceResponseBodyResultAliwsDicts] = None,
        client_node_configuration: DescribeInstanceResponseBodyResultClientNodeConfiguration = None,
        created_at: str = None,
        dedicate_master: bool = None,
        description: str = None,
        dict_list: List[DescribeInstanceResponseBodyResultDictList] = None,
        domain: str = None,
        elastic_data_node_configuration: DescribeInstanceResponseBodyResultElasticDataNodeConfiguration = None,
        enable_kibana_private_network: bool = None,
        enable_kibana_public_network: bool = None,
        enable_public: bool = None,
        es_config: Dict[str, Any] = None,
        es_ipblacklist: List[str] = None,
        es_ipwhitelist: List[str] = None,
        es_version: str = None,
        extend_configs: List[Dict[str, Any]] = None,
        have_client_node: bool = None,
        have_kibana: bool = None,
        instance_id: str = None,
        is_new_deployment: bool = None,
        kibana_configuration: DescribeInstanceResponseBodyResultKibanaConfiguration = None,
        kibana_domain: str = None,
        kibana_ipwhitelist: List[str] = None,
        kibana_port: int = None,
        kibana_private_ipwhitelist: List[str] = None,
        master_configuration: DescribeInstanceResponseBodyResultMasterConfiguration = None,
        network_config: DescribeInstanceResponseBodyResultNetworkConfig = None,
        node_amount: int = None,
        node_spec: DescribeInstanceResponseBodyResultNodeSpec = None,
        payment_type: str = None,
        port: int = None,
        postpaid_service_status: str = None,
        private_network_ip_white_list: List[str] = None,
        protocol: str = None,
        public_domain: str = None,
        public_ip_whitelist: List[str] = None,
        public_port: int = None,
        resource_group_id: str = None,
        service_vpc: bool = None,
        status: str = None,
        synonyms_dicts: List[DescribeInstanceResponseBodyResultSynonymsDicts] = None,
        tags: List[DescribeInstanceResponseBodyResultTags] = None,
        updated_at: str = None,
        vpc_instance_id: str = None,
        warm_node: bool = None,
        warm_node_configuration: DescribeInstanceResponseBodyResultWarmNodeConfiguration = None,
        zone_count: int = None,
        zone_infos: List[DescribeInstanceResponseBodyResultZoneInfos] = None,
    ):
        self.advanced_dedicate_master = advanced_dedicate_master
        self.advanced_setting = advanced_setting
        self.aliws_dicts = aliws_dicts
        self.client_node_configuration = client_node_configuration
        self.created_at = created_at
        self.dedicate_master = dedicate_master
        self.description = description
        self.dict_list = dict_list
        self.domain = domain
        self.elastic_data_node_configuration = elastic_data_node_configuration
        self.enable_kibana_private_network = enable_kibana_private_network
        self.enable_kibana_public_network = enable_kibana_public_network
        self.enable_public = enable_public
        self.es_config = es_config
        self.es_ipblacklist = es_ipblacklist
        self.es_ipwhitelist = es_ipwhitelist
        self.es_version = es_version
        self.extend_configs = extend_configs
        self.have_client_node = have_client_node
        self.have_kibana = have_kibana
        self.instance_id = instance_id
        self.is_new_deployment = is_new_deployment
        self.kibana_configuration = kibana_configuration
        self.kibana_domain = kibana_domain
        self.kibana_ipwhitelist = kibana_ipwhitelist
        self.kibana_port = kibana_port
        self.kibana_private_ipwhitelist = kibana_private_ipwhitelist
        self.master_configuration = master_configuration
        self.network_config = network_config
        self.node_amount = node_amount
        self.node_spec = node_spec
        self.payment_type = payment_type
        self.port = port
        self.postpaid_service_status = postpaid_service_status
        self.private_network_ip_white_list = private_network_ip_white_list
        self.protocol = protocol
        self.public_domain = public_domain
        self.public_ip_whitelist = public_ip_whitelist
        self.public_port = public_port
        self.resource_group_id = resource_group_id
        self.service_vpc = service_vpc
        self.status = status
        self.synonyms_dicts = synonyms_dicts
        self.tags = tags
        self.updated_at = updated_at
        self.vpc_instance_id = vpc_instance_id
        self.warm_node = warm_node
        self.warm_node_configuration = warm_node_configuration
        self.zone_count = zone_count
        self.zone_infos = zone_infos

    def validate(self):
        if self.advanced_setting:
            self.advanced_setting.validate()
        if self.aliws_dicts:
            for k in self.aliws_dicts:
                if k:
                    k.validate()
        if self.client_node_configuration:
            self.client_node_configuration.validate()
        if self.dict_list:
            for k in self.dict_list:
                if k:
                    k.validate()
        if self.elastic_data_node_configuration:
            self.elastic_data_node_configuration.validate()
        if self.kibana_configuration:
            self.kibana_configuration.validate()
        if self.master_configuration:
            self.master_configuration.validate()
        if self.network_config:
            self.network_config.validate()
        if self.node_spec:
            self.node_spec.validate()
        if self.synonyms_dicts:
            for k in self.synonyms_dicts:
                if k:
                    k.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()
        if self.warm_node_configuration:
            self.warm_node_configuration.validate()
        if self.zone_infos:
            for k in self.zone_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.advanced_dedicate_master is not None:
            result['advancedDedicateMaster'] = self.advanced_dedicate_master
        if self.advanced_setting is not None:
            result['advancedSetting'] = self.advanced_setting.to_map()
        result['aliwsDicts'] = []
        if self.aliws_dicts is not None:
            for k in self.aliws_dicts:
                result['aliwsDicts'].append(k.to_map() if k else None)
        if self.client_node_configuration is not None:
            result['clientNodeConfiguration'] = self.client_node_configuration.to_map()
        if self.created_at is not None:
            result['createdAt'] = self.created_at
        if self.dedicate_master is not None:
            result['dedicateMaster'] = self.dedicate_master
        if self.description is not None:
            result['description'] = self.description
        result['dictList'] = []
        if self.dict_list is not None:
            for k in self.dict_list:
                result['dictList'].append(k.to_map() if k else None)
        if self.domain is not None:
            result['domain'] = self.domain
        if self.elastic_data_node_configuration is not None:
            result['elasticDataNodeConfiguration'] = self.elastic_data_node_configuration.to_map()
        if self.enable_kibana_private_network is not None:
            result['enableKibanaPrivateNetwork'] = self.enable_kibana_private_network
        if self.enable_kibana_public_network is not None:
            result['enableKibanaPublicNetwork'] = self.enable_kibana_public_network
        if self.enable_public is not None:
            result['enablePublic'] = self.enable_public
        if self.es_config is not None:
            result['esConfig'] = self.es_config
        if self.es_ipblacklist is not None:
            result['esIPBlacklist'] = self.es_ipblacklist
        if self.es_ipwhitelist is not None:
            result['esIPWhitelist'] = self.es_ipwhitelist
        if self.es_version is not None:
            result['esVersion'] = self.es_version
        if self.extend_configs is not None:
            result['extendConfigs'] = self.extend_configs
        if self.have_client_node is not None:
            result['haveClientNode'] = self.have_client_node
        if self.have_kibana is not None:
            result['haveKibana'] = self.have_kibana
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.is_new_deployment is not None:
            result['isNewDeployment'] = self.is_new_deployment
        if self.kibana_configuration is not None:
            result['kibanaConfiguration'] = self.kibana_configuration.to_map()
        if self.kibana_domain is not None:
            result['kibanaDomain'] = self.kibana_domain
        if self.kibana_ipwhitelist is not None:
            result['kibanaIPWhitelist'] = self.kibana_ipwhitelist
        if self.kibana_port is not None:
            result['kibanaPort'] = self.kibana_port
        if self.kibana_private_ipwhitelist is not None:
            result['kibanaPrivateIPWhitelist'] = self.kibana_private_ipwhitelist
        if self.master_configuration is not None:
            result['masterConfiguration'] = self.master_configuration.to_map()
        if self.network_config is not None:
            result['networkConfig'] = self.network_config.to_map()
        if self.node_amount is not None:
            result['nodeAmount'] = self.node_amount
        if self.node_spec is not None:
            result['nodeSpec'] = self.node_spec.to_map()
        if self.payment_type is not None:
            result['paymentType'] = self.payment_type
        if self.port is not None:
            result['port'] = self.port
        if self.postpaid_service_status is not None:
            result['postpaidServiceStatus'] = self.postpaid_service_status
        if self.private_network_ip_white_list is not None:
            result['privateNetworkIpWhiteList'] = self.private_network_ip_white_list
        if self.protocol is not None:
            result['protocol'] = self.protocol
        if self.public_domain is not None:
            result['publicDomain'] = self.public_domain
        if self.public_ip_whitelist is not None:
            result['publicIpWhitelist'] = self.public_ip_whitelist
        if self.public_port is not None:
            result['publicPort'] = self.public_port
        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id
        if self.service_vpc is not None:
            result['serviceVpc'] = self.service_vpc
        if self.status is not None:
            result['status'] = self.status
        result['synonymsDicts'] = []
        if self.synonyms_dicts is not None:
            for k in self.synonyms_dicts:
                result['synonymsDicts'].append(k.to_map() if k else None)
        result['tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['tags'].append(k.to_map() if k else None)
        if self.updated_at is not None:
            result['updatedAt'] = self.updated_at
        if self.vpc_instance_id is not None:
            result['vpcInstanceId'] = self.vpc_instance_id
        if self.warm_node is not None:
            result['warmNode'] = self.warm_node
        if self.warm_node_configuration is not None:
            result['warmNodeConfiguration'] = self.warm_node_configuration.to_map()
        if self.zone_count is not None:
            result['zoneCount'] = self.zone_count
        result['zoneInfos'] = []
        if self.zone_infos is not None:
            for k in self.zone_infos:
                result['zoneInfos'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('advancedDedicateMaster') is not None:
            self.advanced_dedicate_master = m.get('advancedDedicateMaster')
        if m.get('advancedSetting') is not None:
            temp_model = DescribeInstanceResponseBodyResultAdvancedSetting()
            self.advanced_setting = temp_model.from_map(m['advancedSetting'])
        self.aliws_dicts = []
        if m.get('aliwsDicts') is not None:
            for k in m.get('aliwsDicts'):
                temp_model = DescribeInstanceResponseBodyResultAliwsDicts()
                self.aliws_dicts.append(temp_model.from_map(k))
        if m.get('clientNodeConfiguration') is not None:
            temp_model = DescribeInstanceResponseBodyResultClientNodeConfiguration()
            self.client_node_configuration = temp_model.from_map(m['clientNodeConfiguration'])
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')
        if m.get('dedicateMaster') is not None:
            self.dedicate_master = m.get('dedicateMaster')
        if m.get('description') is not None:
            self.description = m.get('description')
        self.dict_list = []
        if m.get('dictList') is not None:
            for k in m.get('dictList'):
                temp_model = DescribeInstanceResponseBodyResultDictList()
                self.dict_list.append(temp_model.from_map(k))
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('elasticDataNodeConfiguration') is not None:
            temp_model = DescribeInstanceResponseBodyResultElasticDataNodeConfiguration()
            self.elastic_data_node_configuration = temp_model.from_map(m['elasticDataNodeConfiguration'])
        if m.get('enableKibanaPrivateNetwork') is not None:
            self.enable_kibana_private_network = m.get('enableKibanaPrivateNetwork')
        if m.get('enableKibanaPublicNetwork') is not None:
            self.enable_kibana_public_network = m.get('enableKibanaPublicNetwork')
        if m.get('enablePublic') is not None:
            self.enable_public = m.get('enablePublic')
        if m.get('esConfig') is not None:
            self.es_config = m.get('esConfig')
        if m.get('esIPBlacklist') is not None:
            self.es_ipblacklist = m.get('esIPBlacklist')
        if m.get('esIPWhitelist') is not None:
            self.es_ipwhitelist = m.get('esIPWhitelist')
        if m.get('esVersion') is not None:
            self.es_version = m.get('esVersion')
        if m.get('extendConfigs') is not None:
            self.extend_configs = m.get('extendConfigs')
        if m.get('haveClientNode') is not None:
            self.have_client_node = m.get('haveClientNode')
        if m.get('haveKibana') is not None:
            self.have_kibana = m.get('haveKibana')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('isNewDeployment') is not None:
            self.is_new_deployment = m.get('isNewDeployment')
        if m.get('kibanaConfiguration') is not None:
            temp_model = DescribeInstanceResponseBodyResultKibanaConfiguration()
            self.kibana_configuration = temp_model.from_map(m['kibanaConfiguration'])
        if m.get('kibanaDomain') is not None:
            self.kibana_domain = m.get('kibanaDomain')
        if m.get('kibanaIPWhitelist') is not None:
            self.kibana_ipwhitelist = m.get('kibanaIPWhitelist')
        if m.get('kibanaPort') is not None:
            self.kibana_port = m.get('kibanaPort')
        if m.get('kibanaPrivateIPWhitelist') is not None:
            self.kibana_private_ipwhitelist = m.get('kibanaPrivateIPWhitelist')
        if m.get('masterConfiguration') is not None:
            temp_model = DescribeInstanceResponseBodyResultMasterConfiguration()
            self.master_configuration = temp_model.from_map(m['masterConfiguration'])
        if m.get('networkConfig') is not None:
            temp_model = DescribeInstanceResponseBodyResultNetworkConfig()
            self.network_config = temp_model.from_map(m['networkConfig'])
        if m.get('nodeAmount') is not None:
            self.node_amount = m.get('nodeAmount')
        if m.get('nodeSpec') is not None:
            temp_model = DescribeInstanceResponseBodyResultNodeSpec()
            self.node_spec = temp_model.from_map(m['nodeSpec'])
        if m.get('paymentType') is not None:
            self.payment_type = m.get('paymentType')
        if m.get('port') is not None:
            self.port = m.get('port')
        if m.get('postpaidServiceStatus') is not None:
            self.postpaid_service_status = m.get('postpaidServiceStatus')
        if m.get('privateNetworkIpWhiteList') is not None:
            self.private_network_ip_white_list = m.get('privateNetworkIpWhiteList')
        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')
        if m.get('publicDomain') is not None:
            self.public_domain = m.get('publicDomain')
        if m.get('publicIpWhitelist') is not None:
            self.public_ip_whitelist = m.get('publicIpWhitelist')
        if m.get('publicPort') is not None:
            self.public_port = m.get('publicPort')
        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')
        if m.get('serviceVpc') is not None:
            self.service_vpc = m.get('serviceVpc')
        if m.get('status') is not None:
            self.status = m.get('status')
        self.synonyms_dicts = []
        if m.get('synonymsDicts') is not None:
            for k in m.get('synonymsDicts'):
                temp_model = DescribeInstanceResponseBodyResultSynonymsDicts()
                self.synonyms_dicts.append(temp_model.from_map(k))
        self.tags = []
        if m.get('tags') is not None:
            for k in m.get('tags'):
                temp_model = DescribeInstanceResponseBodyResultTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')
        if m.get('vpcInstanceId') is not None:
            self.vpc_instance_id = m.get('vpcInstanceId')
        if m.get('warmNode') is not None:
            self.warm_node = m.get('warmNode')
        if m.get('warmNodeConfiguration') is not None:
            temp_model = DescribeInstanceResponseBodyResultWarmNodeConfiguration()
            self.warm_node_configuration = temp_model.from_map(m['warmNodeConfiguration'])
        if m.get('zoneCount') is not None:
            self.zone_count = m.get('zoneCount')
        self.zone_infos = []
        if m.get('zoneInfos') is not None:
            for k in m.get('zoneInfos'):
                temp_model = DescribeInstanceResponseBodyResultZoneInfos()
                self.zone_infos.append(temp_model.from_map(k))
        return self


class DescribeInstanceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: DescribeInstanceResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = DescribeInstanceResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class DescribeInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeInstanceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeKibanaSettingsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: Dict[str, Any] = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class DescribeKibanaSettingsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeKibanaSettingsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeKibanaSettingsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeLogstashResponseBodyResultTags(TeaModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        self.tag_key = tag_key
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_key is not None:
            result['tagKey'] = self.tag_key
        if self.tag_value is not None:
            result['tagValue'] = self.tag_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('tagKey') is not None:
            self.tag_key = m.get('tagKey')
        if m.get('tagValue') is not None:
            self.tag_value = m.get('tagValue')
        return self


class DescribeLogstashResponseBodyResultZoneInfos(TeaModel):
    def __init__(
        self,
        status: str = None,
        zone_id: str = None,
    ):
        self.status = status
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['status'] = self.status
        if self.zone_id is not None:
            result['zoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('zoneId') is not None:
            self.zone_id = m.get('zoneId')
        return self


class DescribeLogstashResponseBodyResultEndpointList(TeaModel):
    def __init__(
        self,
        host: str = None,
        port: str = None,
        zone_id: str = None,
    ):
        self.host = host
        self.port = port
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host is not None:
            result['host'] = self.host
        if self.port is not None:
            result['port'] = self.port
        if self.zone_id is not None:
            result['zoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('host') is not None:
            self.host = m.get('host')
        if m.get('port') is not None:
            self.port = m.get('port')
        if m.get('zoneId') is not None:
            self.zone_id = m.get('zoneId')
        return self


class DescribeLogstashResponseBodyResultNetworkConfig(TeaModel):
    def __init__(
        self,
        type: str = None,
        vpc_id: str = None,
        vs_area: str = None,
        vswitch_id: str = None,
    ):
        self.type = type
        self.vpc_id = vpc_id
        self.vs_area = vs_area
        self.vswitch_id = vswitch_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['type'] = self.type
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        if self.vs_area is not None:
            result['vsArea'] = self.vs_area
        if self.vswitch_id is not None:
            result['vswitchId'] = self.vswitch_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        if m.get('vsArea') is not None:
            self.vs_area = m.get('vsArea')
        if m.get('vswitchId') is not None:
            self.vswitch_id = m.get('vswitchId')
        return self


class DescribeLogstashResponseBodyResultNodeSpec(TeaModel):
    def __init__(
        self,
        disk: int = None,
        disk_encryption: bool = None,
        disk_type: str = None,
        spec: str = None,
    ):
        self.disk = disk
        self.disk_encryption = disk_encryption
        self.disk_type = disk_type
        self.spec = spec

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.disk is not None:
            result['disk'] = self.disk
        if self.disk_encryption is not None:
            result['diskEncryption'] = self.disk_encryption
        if self.disk_type is not None:
            result['diskType'] = self.disk_type
        if self.spec is not None:
            result['spec'] = self.spec
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('disk') is not None:
            self.disk = m.get('disk')
        if m.get('diskEncryption') is not None:
            self.disk_encryption = m.get('diskEncryption')
        if m.get('diskType') is not None:
            self.disk_type = m.get('diskType')
        if m.get('spec') is not None:
            self.spec = m.get('spec')
        return self


class DescribeLogstashResponseBodyResult(TeaModel):
    def __init__(
        self,
        extend_configs: List[Dict[str, Any]] = None,
        resource_group_id: str = None,
        tags: List[DescribeLogstashResponseBodyResultTags] = None,
        zone_infos: List[DescribeLogstashResponseBodyResultZoneInfos] = None,
        config: Dict[str, Any] = None,
        created_at: str = None,
        description: str = None,
        endpoint_list: List[DescribeLogstashResponseBodyResultEndpointList] = None,
        instance_id: str = None,
        network_config: DescribeLogstashResponseBodyResultNetworkConfig = None,
        node_amount: int = None,
        node_spec: DescribeLogstashResponseBodyResultNodeSpec = None,
        payment_type: str = None,
        status: str = None,
        updated_at: str = None,
        version: str = None,
        vpc_instance_id: str = None,
    ):
        self.extend_configs = extend_configs
        self.resource_group_id = resource_group_id
        self.tags = tags
        self.zone_infos = zone_infos
        self.config = config
        self.created_at = created_at
        self.description = description
        self.endpoint_list = endpoint_list
        self.instance_id = instance_id
        self.network_config = network_config
        self.node_amount = node_amount
        self.node_spec = node_spec
        self.payment_type = payment_type
        self.status = status
        self.updated_at = updated_at
        self.version = version
        self.vpc_instance_id = vpc_instance_id

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()
        if self.zone_infos:
            for k in self.zone_infos:
                if k:
                    k.validate()
        if self.endpoint_list:
            for k in self.endpoint_list:
                if k:
                    k.validate()
        if self.network_config:
            self.network_config.validate()
        if self.node_spec:
            self.node_spec.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extend_configs is not None:
            result['ExtendConfigs'] = self.extend_configs
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        result['ZoneInfos'] = []
        if self.zone_infos is not None:
            for k in self.zone_infos:
                result['ZoneInfos'].append(k.to_map() if k else None)
        if self.config is not None:
            result['config'] = self.config
        if self.created_at is not None:
            result['createdAt'] = self.created_at
        if self.description is not None:
            result['description'] = self.description
        result['endpointList'] = []
        if self.endpoint_list is not None:
            for k in self.endpoint_list:
                result['endpointList'].append(k.to_map() if k else None)
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.network_config is not None:
            result['networkConfig'] = self.network_config.to_map()
        if self.node_amount is not None:
            result['nodeAmount'] = self.node_amount
        if self.node_spec is not None:
            result['nodeSpec'] = self.node_spec.to_map()
        if self.payment_type is not None:
            result['paymentType'] = self.payment_type
        if self.status is not None:
            result['status'] = self.status
        if self.updated_at is not None:
            result['updatedAt'] = self.updated_at
        if self.version is not None:
            result['version'] = self.version
        if self.vpc_instance_id is not None:
            result['vpcInstanceId'] = self.vpc_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExtendConfigs') is not None:
            self.extend_configs = m.get('ExtendConfigs')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = DescribeLogstashResponseBodyResultTags()
                self.tags.append(temp_model.from_map(k))
        self.zone_infos = []
        if m.get('ZoneInfos') is not None:
            for k in m.get('ZoneInfos'):
                temp_model = DescribeLogstashResponseBodyResultZoneInfos()
                self.zone_infos.append(temp_model.from_map(k))
        if m.get('config') is not None:
            self.config = m.get('config')
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')
        if m.get('description') is not None:
            self.description = m.get('description')
        self.endpoint_list = []
        if m.get('endpointList') is not None:
            for k in m.get('endpointList'):
                temp_model = DescribeLogstashResponseBodyResultEndpointList()
                self.endpoint_list.append(temp_model.from_map(k))
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('networkConfig') is not None:
            temp_model = DescribeLogstashResponseBodyResultNetworkConfig()
            self.network_config = temp_model.from_map(m['networkConfig'])
        if m.get('nodeAmount') is not None:
            self.node_amount = m.get('nodeAmount')
        if m.get('nodeSpec') is not None:
            temp_model = DescribeLogstashResponseBodyResultNodeSpec()
            self.node_spec = temp_model.from_map(m['nodeSpec'])
        if m.get('paymentType') is not None:
            self.payment_type = m.get('paymentType')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')
        if m.get('version') is not None:
            self.version = m.get('version')
        if m.get('vpcInstanceId') is not None:
            self.vpc_instance_id = m.get('vpcInstanceId')
        return self


class DescribeLogstashResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: DescribeLogstashResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = DescribeLogstashResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class DescribeLogstashResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeLogstashResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeLogstashResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePipelineResponseBodyResult(TeaModel):
    def __init__(
        self,
        batch_delay: int = None,
        batch_size: int = None,
        config: str = None,
        description: str = None,
        gmt_created_time: str = None,
        gmt_update_time: str = None,
        pipeline_id: str = None,
        pipeline_status: str = None,
        queue_check_point_writes: int = None,
        queue_max_bytes: int = None,
        queue_type: str = None,
        workers: int = None,
    ):
        self.batch_delay = batch_delay
        self.batch_size = batch_size
        self.config = config
        self.description = description
        self.gmt_created_time = gmt_created_time
        self.gmt_update_time = gmt_update_time
        self.pipeline_id = pipeline_id
        self.pipeline_status = pipeline_status
        self.queue_check_point_writes = queue_check_point_writes
        self.queue_max_bytes = queue_max_bytes
        self.queue_type = queue_type
        self.workers = workers

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.batch_delay is not None:
            result['batchDelay'] = self.batch_delay
        if self.batch_size is not None:
            result['batchSize'] = self.batch_size
        if self.config is not None:
            result['config'] = self.config
        if self.description is not None:
            result['description'] = self.description
        if self.gmt_created_time is not None:
            result['gmtCreatedTime'] = self.gmt_created_time
        if self.gmt_update_time is not None:
            result['gmtUpdateTime'] = self.gmt_update_time
        if self.pipeline_id is not None:
            result['pipelineId'] = self.pipeline_id
        if self.pipeline_status is not None:
            result['pipelineStatus'] = self.pipeline_status
        if self.queue_check_point_writes is not None:
            result['queueCheckPointWrites'] = self.queue_check_point_writes
        if self.queue_max_bytes is not None:
            result['queueMaxBytes'] = self.queue_max_bytes
        if self.queue_type is not None:
            result['queueType'] = self.queue_type
        if self.workers is not None:
            result['workers'] = self.workers
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('batchDelay') is not None:
            self.batch_delay = m.get('batchDelay')
        if m.get('batchSize') is not None:
            self.batch_size = m.get('batchSize')
        if m.get('config') is not None:
            self.config = m.get('config')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('gmtCreatedTime') is not None:
            self.gmt_created_time = m.get('gmtCreatedTime')
        if m.get('gmtUpdateTime') is not None:
            self.gmt_update_time = m.get('gmtUpdateTime')
        if m.get('pipelineId') is not None:
            self.pipeline_id = m.get('pipelineId')
        if m.get('pipelineStatus') is not None:
            self.pipeline_status = m.get('pipelineStatus')
        if m.get('queueCheckPointWrites') is not None:
            self.queue_check_point_writes = m.get('queueCheckPointWrites')
        if m.get('queueMaxBytes') is not None:
            self.queue_max_bytes = m.get('queueMaxBytes')
        if m.get('queueType') is not None:
            self.queue_type = m.get('queueType')
        if m.get('workers') is not None:
            self.workers = m.get('workers')
        return self


class DescribePipelineResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: DescribePipelineResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = DescribePipelineResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class DescribePipelineResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribePipelineResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribePipelineResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePipelineManagementConfigRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
    ):
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        return self


class DescribePipelineManagementConfigResponseBodyResult(TeaModel):
    def __init__(
        self,
        endpoints: str = None,
        es_instance_id: str = None,
        pipeline_ids: List[str] = None,
        pipeline_management_type: str = None,
        user_name: str = None,
    ):
        self.endpoints = endpoints
        self.es_instance_id = es_instance_id
        self.pipeline_ids = pipeline_ids
        self.pipeline_management_type = pipeline_management_type
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoints is not None:
            result['endpoints'] = self.endpoints
        if self.es_instance_id is not None:
            result['esInstanceId'] = self.es_instance_id
        if self.pipeline_ids is not None:
            result['pipelineIds'] = self.pipeline_ids
        if self.pipeline_management_type is not None:
            result['pipelineManagementType'] = self.pipeline_management_type
        if self.user_name is not None:
            result['userName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endpoints') is not None:
            self.endpoints = m.get('endpoints')
        if m.get('esInstanceId') is not None:
            self.es_instance_id = m.get('esInstanceId')
        if m.get('pipelineIds') is not None:
            self.pipeline_ids = m.get('pipelineIds')
        if m.get('pipelineManagementType') is not None:
            self.pipeline_management_type = m.get('pipelineManagementType')
        if m.get('userName') is not None:
            self.user_name = m.get('userName')
        return self


class DescribePipelineManagementConfigResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: DescribePipelineManagementConfigResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = DescribePipelineManagementConfigResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class DescribePipelineManagementConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribePipelineManagementConfigResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribePipelineManagementConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRegionsResponseBodyResult(TeaModel):
    def __init__(
        self,
        console_endpoint: str = None,
        local_name: str = None,
        region_endpoint: str = None,
        region_id: str = None,
        status: str = None,
    ):
        self.console_endpoint = console_endpoint
        self.local_name = local_name
        self.region_endpoint = region_endpoint
        self.region_id = region_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.console_endpoint is not None:
            result['consoleEndpoint'] = self.console_endpoint
        if self.local_name is not None:
            result['localName'] = self.local_name
        if self.region_endpoint is not None:
            result['regionEndpoint'] = self.region_endpoint
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('consoleEndpoint') is not None:
            self.console_endpoint = m.get('consoleEndpoint')
        if m.get('localName') is not None:
            self.local_name = m.get('localName')
        if m.get('regionEndpoint') is not None:
            self.region_endpoint = m.get('regionEndpoint')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class DescribeRegionsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[DescribeRegionsResponseBodyResult] = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = DescribeRegionsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class DescribeRegionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeRegionsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSnapshotSettingResponseBodyResult(TeaModel):
    def __init__(
        self,
        enable: bool = None,
        quartz_regex: str = None,
    ):
        self.enable = enable
        self.quartz_regex = quartz_regex

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.quartz_regex is not None:
            result['QuartzRegex'] = self.quartz_regex
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('QuartzRegex') is not None:
            self.quartz_regex = m.get('QuartzRegex')
        return self


class DescribeSnapshotSettingResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: DescribeSnapshotSettingResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = DescribeSnapshotSettingResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class DescribeSnapshotSettingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeSnapshotSettingResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeSnapshotSettingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTemplatesResponseBodyResult(TeaModel):
    def __init__(
        self,
        content: str = None,
        template_name: str = None,
    ):
        self.content = content
        self.template_name = template_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['content'] = self.content
        if self.template_name is not None:
            result['templateName'] = self.template_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('templateName') is not None:
            self.template_name = m.get('templateName')
        return self


class DescribeTemplatesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[DescribeTemplatesResponseBodyResult] = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = DescribeTemplatesResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class DescribeTemplatesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeTemplatesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeTemplatesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeXpackMonitorConfigResponseBodyResult(TeaModel):
    def __init__(
        self,
        enable: bool = None,
        endpoints: List[str] = None,
        es_instance_id: str = None,
        pipeline_ids: List[str] = None,
        user_name: str = None,
    ):
        self.enable = enable
        self.endpoints = endpoints
        self.es_instance_id = es_instance_id
        self.pipeline_ids = pipeline_ids
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable is not None:
            result['enable'] = self.enable
        if self.endpoints is not None:
            result['endpoints'] = self.endpoints
        if self.es_instance_id is not None:
            result['esInstanceId'] = self.es_instance_id
        if self.pipeline_ids is not None:
            result['pipelineIds'] = self.pipeline_ids
        if self.user_name is not None:
            result['userName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enable') is not None:
            self.enable = m.get('enable')
        if m.get('endpoints') is not None:
            self.endpoints = m.get('endpoints')
        if m.get('esInstanceId') is not None:
            self.es_instance_id = m.get('esInstanceId')
        if m.get('pipelineIds') is not None:
            self.pipeline_ids = m.get('pipelineIds')
        if m.get('userName') is not None:
            self.user_name = m.get('userName')
        return self


class DescribeXpackMonitorConfigResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: DescribeXpackMonitorConfigResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = DescribeXpackMonitorConfigResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class DescribeXpackMonitorConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeXpackMonitorConfigResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeXpackMonitorConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DiagnoseInstanceRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        lang: str = None,
    ):
        self.client_token = client_token
        self.lang = lang

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.lang is not None:
            result['lang'] = self.lang
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('lang') is not None:
            self.lang = m.get('lang')
        return self


class DiagnoseInstanceResponseBodyResultDiagnoseItems(TeaModel):
    def __init__(
        self,
        item: str = None,
    ):
        self.item = item

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.item is not None:
            result['item'] = self.item
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('item') is not None:
            self.item = m.get('item')
        return self


class DiagnoseInstanceResponseBodyResult(TeaModel):
    def __init__(
        self,
        create_time: int = None,
        diagnose_items: List[DiagnoseInstanceResponseBodyResultDiagnoseItems] = None,
        instance_id: str = None,
        report_id: str = None,
        state: str = None,
    ):
        self.create_time = create_time
        self.diagnose_items = diagnose_items
        self.instance_id = instance_id
        self.report_id = report_id
        self.state = state

    def validate(self):
        if self.diagnose_items:
            for k in self.diagnose_items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        result['diagnoseItems'] = []
        if self.diagnose_items is not None:
            for k in self.diagnose_items:
                result['diagnoseItems'].append(k.to_map() if k else None)
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.report_id is not None:
            result['reportId'] = self.report_id
        if self.state is not None:
            result['state'] = self.state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        self.diagnose_items = []
        if m.get('diagnoseItems') is not None:
            for k in m.get('diagnoseItems'):
                temp_model = DiagnoseInstanceResponseBodyResultDiagnoseItems()
                self.diagnose_items.append(temp_model.from_map(k))
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('reportId') is not None:
            self.report_id = m.get('reportId')
        if m.get('state') is not None:
            self.state = m.get('state')
        return self


class DiagnoseInstanceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: DiagnoseInstanceResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = DiagnoseInstanceResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class DiagnoseInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DiagnoseInstanceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DiagnoseInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EstimatedLogstashRestartTimeRequest(TeaModel):
    def __init__(
        self,
        force: bool = None,
    ):
        self.force = force

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.force is not None:
            result['force'] = self.force
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('force') is not None:
            self.force = m.get('force')
        return self


class EstimatedLogstashRestartTimeResponseBodyResult(TeaModel):
    def __init__(
        self,
        unit: str = None,
        value: int = None,
    ):
        self.unit = unit
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.unit is not None:
            result['unit'] = self.unit
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('unit') is not None:
            self.unit = m.get('unit')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class EstimatedLogstashRestartTimeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: EstimatedLogstashRestartTimeResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = EstimatedLogstashRestartTimeResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class EstimatedLogstashRestartTimeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: EstimatedLogstashRestartTimeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = EstimatedLogstashRestartTimeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EstimatedRestartTimeRequest(TeaModel):
    def __init__(
        self,
        force: bool = None,
    ):
        self.force = force

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.force is not None:
            result['force'] = self.force
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('force') is not None:
            self.force = m.get('force')
        return self


class EstimatedRestartTimeResponseBodyResult(TeaModel):
    def __init__(
        self,
        unit: str = None,
        value: int = None,
    ):
        self.unit = unit
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.unit is not None:
            result['unit'] = self.unit
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('unit') is not None:
            self.unit = m.get('unit')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class EstimatedRestartTimeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: EstimatedRestartTimeResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = EstimatedRestartTimeResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class EstimatedRestartTimeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: EstimatedRestartTimeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = EstimatedRestartTimeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetClusterDataInformationResponseBodyResultMetaInfo(TeaModel):
    def __init__(
        self,
        fields: List[str] = None,
        indices: List[str] = None,
        mapping: str = None,
        settings: str = None,
        type_name: List[str] = None,
    ):
        self.fields = fields
        self.indices = indices
        self.mapping = mapping
        self.settings = settings
        self.type_name = type_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fields is not None:
            result['fields'] = self.fields
        if self.indices is not None:
            result['indices'] = self.indices
        if self.mapping is not None:
            result['mapping'] = self.mapping
        if self.settings is not None:
            result['settings'] = self.settings
        if self.type_name is not None:
            result['typeName'] = self.type_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fields') is not None:
            self.fields = m.get('fields')
        if m.get('indices') is not None:
            self.indices = m.get('indices')
        if m.get('mapping') is not None:
            self.mapping = m.get('mapping')
        if m.get('settings') is not None:
            self.settings = m.get('settings')
        if m.get('typeName') is not None:
            self.type_name = m.get('typeName')
        return self


class GetClusterDataInformationResponseBodyResult(TeaModel):
    def __init__(
        self,
        connectable: bool = None,
        meta_info: GetClusterDataInformationResponseBodyResultMetaInfo = None,
    ):
        self.connectable = connectable
        self.meta_info = meta_info

    def validate(self):
        if self.meta_info:
            self.meta_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connectable is not None:
            result['connectable'] = self.connectable
        if self.meta_info is not None:
            result['metaInfo'] = self.meta_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('connectable') is not None:
            self.connectable = m.get('connectable')
        if m.get('metaInfo') is not None:
            temp_model = GetClusterDataInformationResponseBodyResultMetaInfo()
            self.meta_info = temp_model.from_map(m['metaInfo'])
        return self


class GetClusterDataInformationResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: GetClusterDataInformationResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = GetClusterDataInformationResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class GetClusterDataInformationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetClusterDataInformationResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetClusterDataInformationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetElastictaskResponseBodyResultElasticExpansionTask(TeaModel):
    def __init__(
        self,
        cron_expression: str = None,
        elastic_node_count: int = None,
        replica_count: int = None,
        target_indices: List[str] = None,
        trigger_type: str = None,
    ):
        self.cron_expression = cron_expression
        self.elastic_node_count = elastic_node_count
        self.replica_count = replica_count
        self.target_indices = target_indices
        self.trigger_type = trigger_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cron_expression is not None:
            result['cronExpression'] = self.cron_expression
        if self.elastic_node_count is not None:
            result['elasticNodeCount'] = self.elastic_node_count
        if self.replica_count is not None:
            result['replicaCount'] = self.replica_count
        if self.target_indices is not None:
            result['targetIndices'] = self.target_indices
        if self.trigger_type is not None:
            result['triggerType'] = self.trigger_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cronExpression') is not None:
            self.cron_expression = m.get('cronExpression')
        if m.get('elasticNodeCount') is not None:
            self.elastic_node_count = m.get('elasticNodeCount')
        if m.get('replicaCount') is not None:
            self.replica_count = m.get('replicaCount')
        if m.get('targetIndices') is not None:
            self.target_indices = m.get('targetIndices')
        if m.get('triggerType') is not None:
            self.trigger_type = m.get('triggerType')
        return self


class GetElastictaskResponseBodyResultElasticShrinkTask(TeaModel):
    def __init__(
        self,
        cron_expression: str = None,
        elastic_node_count: int = None,
        replica_count: int = None,
        target_indices: List[str] = None,
        trigger_type: str = None,
    ):
        self.cron_expression = cron_expression
        self.elastic_node_count = elastic_node_count
        self.replica_count = replica_count
        self.target_indices = target_indices
        self.trigger_type = trigger_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cron_expression is not None:
            result['cronExpression'] = self.cron_expression
        if self.elastic_node_count is not None:
            result['elasticNodeCount'] = self.elastic_node_count
        if self.replica_count is not None:
            result['replicaCount'] = self.replica_count
        if self.target_indices is not None:
            result['targetIndices'] = self.target_indices
        if self.trigger_type is not None:
            result['triggerType'] = self.trigger_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cronExpression') is not None:
            self.cron_expression = m.get('cronExpression')
        if m.get('elasticNodeCount') is not None:
            self.elastic_node_count = m.get('elasticNodeCount')
        if m.get('replicaCount') is not None:
            self.replica_count = m.get('replicaCount')
        if m.get('targetIndices') is not None:
            self.target_indices = m.get('targetIndices')
        if m.get('triggerType') is not None:
            self.trigger_type = m.get('triggerType')
        return self


class GetElastictaskResponseBodyResult(TeaModel):
    def __init__(
        self,
        elastic_expansion_task: GetElastictaskResponseBodyResultElasticExpansionTask = None,
        elastic_shrink_task: GetElastictaskResponseBodyResultElasticShrinkTask = None,
    ):
        self.elastic_expansion_task = elastic_expansion_task
        self.elastic_shrink_task = elastic_shrink_task

    def validate(self):
        if self.elastic_expansion_task:
            self.elastic_expansion_task.validate()
        if self.elastic_shrink_task:
            self.elastic_shrink_task.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.elastic_expansion_task is not None:
            result['elasticExpansionTask'] = self.elastic_expansion_task.to_map()
        if self.elastic_shrink_task is not None:
            result['elasticShrinkTask'] = self.elastic_shrink_task.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('elasticExpansionTask') is not None:
            temp_model = GetElastictaskResponseBodyResultElasticExpansionTask()
            self.elastic_expansion_task = temp_model.from_map(m['elasticExpansionTask'])
        if m.get('elasticShrinkTask') is not None:
            temp_model = GetElastictaskResponseBodyResultElasticShrinkTask()
            self.elastic_shrink_task = temp_model.from_map(m['elasticShrinkTask'])
        return self


class GetElastictaskResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: GetElastictaskResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = GetElastictaskResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class GetElastictaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetElastictaskResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetElastictaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetEmonGrafanaAlertsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetEmonGrafanaAlertsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetEmonGrafanaAlertsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetEmonGrafanaAlertsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetEmonGrafanaDashboardsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetEmonGrafanaDashboardsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetEmonGrafanaDashboardsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetEmonGrafanaDashboardsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetEmonMonitorDataResponseBodyResult(TeaModel):
    def __init__(
        self,
        dps: Dict[str, Any] = None,
        integrity: float = None,
        message_watermark: int = None,
        metric: str = None,
        summary: float = None,
        tags: Dict[str, Any] = None,
    ):
        self.dps = dps
        self.integrity = integrity
        self.message_watermark = message_watermark
        self.metric = metric
        self.summary = summary
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dps is not None:
            result['dps'] = self.dps
        if self.integrity is not None:
            result['integrity'] = self.integrity
        if self.message_watermark is not None:
            result['messageWatermark'] = self.message_watermark
        if self.metric is not None:
            result['metric'] = self.metric
        if self.summary is not None:
            result['summary'] = self.summary
        if self.tags is not None:
            result['tags'] = self.tags
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dps') is not None:
            self.dps = m.get('dps')
        if m.get('integrity') is not None:
            self.integrity = m.get('integrity')
        if m.get('messageWatermark') is not None:
            self.message_watermark = m.get('messageWatermark')
        if m.get('metric') is not None:
            self.metric = m.get('metric')
        if m.get('summary') is not None:
            self.summary = m.get('summary')
        if m.get('tags') is not None:
            self.tags = m.get('tags')
        return self


class GetEmonMonitorDataResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: List[GetEmonMonitorDataResponseBodyResult] = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result = result
        self.success = success

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = GetEmonMonitorDataResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetEmonMonitorDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetEmonMonitorDataResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetEmonMonitorDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOpenStoreUsageResponseBodyResult(TeaModel):
    def __init__(
        self,
        current_usage: int = None,
        last_day_usage: int = None,
    ):
        # 当前使用量
        self.current_usage = current_usage
        # 昨日使用容量
        self.last_day_usage = last_day_usage

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_usage is not None:
            result['currentUsage'] = self.current_usage
        if self.last_day_usage is not None:
            result['lastDayUsage'] = self.last_day_usage
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('currentUsage') is not None:
            self.current_usage = m.get('currentUsage')
        if m.get('lastDayUsage') is not None:
            self.last_day_usage = m.get('lastDayUsage')
        return self


class GetOpenStoreUsageResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: GetOpenStoreUsageResponseBodyResult = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = GetOpenStoreUsageResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class GetOpenStoreUsageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetOpenStoreUsageResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetOpenStoreUsageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRegionConfigurationRequest(TeaModel):
    def __init__(
        self,
        zone_id: str = None,
    ):
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.zone_id is not None:
            result['zoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('zoneId') is not None:
            self.zone_id = m.get('zoneId')
        return self


class GetRegionConfigurationResponseBodyResultClientNodeAmountRange(TeaModel):
    def __init__(
        self,
        max_amount: int = None,
        min_amount: int = None,
    ):
        self.max_amount = max_amount
        self.min_amount = min_amount

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_amount is not None:
            result['maxAmount'] = self.max_amount
        if self.min_amount is not None:
            result['minAmount'] = self.min_amount
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxAmount') is not None:
            self.max_amount = m.get('maxAmount')
        if m.get('minAmount') is not None:
            self.min_amount = m.get('minAmount')
        return self


class GetRegionConfigurationResponseBodyResultClientNodeDiskList(TeaModel):
    def __init__(
        self,
        disk_type: str = None,
        max_size: int = None,
        min_size: int = None,
        scale_limit: int = None,
    ):
        self.disk_type = disk_type
        self.max_size = max_size
        self.min_size = min_size
        self.scale_limit = scale_limit

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.disk_type is not None:
            result['diskType'] = self.disk_type
        if self.max_size is not None:
            result['maxSize'] = self.max_size
        if self.min_size is not None:
            result['minSize'] = self.min_size
        if self.scale_limit is not None:
            result['scaleLimit'] = self.scale_limit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('diskType') is not None:
            self.disk_type = m.get('diskType')
        if m.get('maxSize') is not None:
            self.max_size = m.get('maxSize')
        if m.get('minSize') is not None:
            self.min_size = m.get('minSize')
        if m.get('scaleLimit') is not None:
            self.scale_limit = m.get('scaleLimit')
        return self


class GetRegionConfigurationResponseBodyResultDataDiskList(TeaModel):
    def __init__(
        self,
        disk_type: str = None,
        max_size: int = None,
        min_size: int = None,
        scale_limit: int = None,
        value_limit_set: List[str] = None,
    ):
        self.disk_type = disk_type
        self.max_size = max_size
        self.min_size = min_size
        self.scale_limit = scale_limit
        self.value_limit_set = value_limit_set

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.disk_type is not None:
            result['diskType'] = self.disk_type
        if self.max_size is not None:
            result['maxSize'] = self.max_size
        if self.min_size is not None:
            result['minSize'] = self.min_size
        if self.scale_limit is not None:
            result['scaleLimit'] = self.scale_limit
        if self.value_limit_set is not None:
            result['valueLimitSet'] = self.value_limit_set
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('diskType') is not None:
            self.disk_type = m.get('diskType')
        if m.get('maxSize') is not None:
            self.max_size = m.get('maxSize')
        if m.get('minSize') is not None:
            self.min_size = m.get('minSize')
        if m.get('scaleLimit') is not None:
            self.scale_limit = m.get('scaleLimit')
        if m.get('valueLimitSet') is not None:
            self.value_limit_set = m.get('valueLimitSet')
        return self


class GetRegionConfigurationResponseBodyResultElasticNodePropertiesAmountRange(TeaModel):
    def __init__(
        self,
        max_amount: int = None,
        min_amount: int = None,
    ):
        self.max_amount = max_amount
        self.min_amount = min_amount

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_amount is not None:
            result['maxAmount'] = self.max_amount
        if self.min_amount is not None:
            result['minAmount'] = self.min_amount
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxAmount') is not None:
            self.max_amount = m.get('maxAmount')
        if m.get('minAmount') is not None:
            self.min_amount = m.get('minAmount')
        return self


class GetRegionConfigurationResponseBodyResultElasticNodePropertiesDiskList(TeaModel):
    def __init__(
        self,
        disk_encryption: bool = None,
        disk_type: str = None,
        max_size: int = None,
        min_size: int = None,
        scale_limit: int = None,
        value_limit_set: List[str] = None,
    ):
        self.disk_encryption = disk_encryption
        self.disk_type = disk_type
        self.max_size = max_size
        self.min_size = min_size
        self.scale_limit = scale_limit
        self.value_limit_set = value_limit_set

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.disk_encryption is not None:
            result['diskEncryption'] = self.disk_encryption
        if self.disk_type is not None:
            result['diskType'] = self.disk_type
        if self.max_size is not None:
            result['maxSize'] = self.max_size
        if self.min_size is not None:
            result['minSize'] = self.min_size
        if self.scale_limit is not None:
            result['scaleLimit'] = self.scale_limit
        if self.value_limit_set is not None:
            result['valueLimitSet'] = self.value_limit_set
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('diskEncryption') is not None:
            self.disk_encryption = m.get('diskEncryption')
        if m.get('diskType') is not None:
            self.disk_type = m.get('diskType')
        if m.get('maxSize') is not None:
            self.max_size = m.get('maxSize')
        if m.get('minSize') is not None:
            self.min_size = m.get('minSize')
        if m.get('scaleLimit') is not None:
            self.scale_limit = m.get('scaleLimit')
        if m.get('valueLimitSet') is not None:
            self.value_limit_set = m.get('valueLimitSet')
        return self


class GetRegionConfigurationResponseBodyResultElasticNodeProperties(TeaModel):
    def __init__(
        self,
        amount_range: GetRegionConfigurationResponseBodyResultElasticNodePropertiesAmountRange = None,
        disk_list: List[GetRegionConfigurationResponseBodyResultElasticNodePropertiesDiskList] = None,
        spec: List[str] = None,
    ):
        self.amount_range = amount_range
        self.disk_list = disk_list
        self.spec = spec

    def validate(self):
        if self.amount_range:
            self.amount_range.validate()
        if self.disk_list:
            for k in self.disk_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.amount_range is not None:
            result['amountRange'] = self.amount_range.to_map()
        result['diskList'] = []
        if self.disk_list is not None:
            for k in self.disk_list:
                result['diskList'].append(k.to_map() if k else None)
        if self.spec is not None:
            result['spec'] = self.spec
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('amountRange') is not None:
            temp_model = GetRegionConfigurationResponseBodyResultElasticNodePropertiesAmountRange()
            self.amount_range = temp_model.from_map(m['amountRange'])
        self.disk_list = []
        if m.get('diskList') is not None:
            for k in m.get('diskList'):
                temp_model = GetRegionConfigurationResponseBodyResultElasticNodePropertiesDiskList()
                self.disk_list.append(temp_model.from_map(k))
        if m.get('spec') is not None:
            self.spec = m.get('spec')
        return self


class GetRegionConfigurationResponseBodyResultEsVersionsLatestList(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class GetRegionConfigurationResponseBodyResultJvmConfine(TeaModel):
    def __init__(
        self,
        memory: int = None,
        support_es_versions: List[str] = None,
        support_gcs: List[str] = None,
    ):
        self.memory = memory
        self.support_es_versions = support_es_versions
        self.support_gcs = support_gcs

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.memory is not None:
            result['memory'] = self.memory
        if self.support_es_versions is not None:
            result['supportEsVersions'] = self.support_es_versions
        if self.support_gcs is not None:
            result['supportGcs'] = self.support_gcs
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('memory') is not None:
            self.memory = m.get('memory')
        if m.get('supportEsVersions') is not None:
            self.support_es_versions = m.get('supportEsVersions')
        if m.get('supportGcs') is not None:
            self.support_gcs = m.get('supportGcs')
        return self


class GetRegionConfigurationResponseBodyResultKibanaNodePropertiesAmountRange(TeaModel):
    def __init__(
        self,
        max_amount: int = None,
        min_amount: int = None,
    ):
        self.max_amount = max_amount
        self.min_amount = min_amount

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_amount is not None:
            result['maxAmount'] = self.max_amount
        if self.min_amount is not None:
            result['minAmount'] = self.min_amount
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxAmount') is not None:
            self.max_amount = m.get('maxAmount')
        if m.get('minAmount') is not None:
            self.min_amount = m.get('minAmount')
        return self


class GetRegionConfigurationResponseBodyResultKibanaNodeProperties(TeaModel):
    def __init__(
        self,
        amount_range: GetRegionConfigurationResponseBodyResultKibanaNodePropertiesAmountRange = None,
        spec: List[str] = None,
    ):
        self.amount_range = amount_range
        self.spec = spec

    def validate(self):
        if self.amount_range:
            self.amount_range.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.amount_range is not None:
            result['amountRange'] = self.amount_range.to_map()
        if self.spec is not None:
            result['spec'] = self.spec
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('amountRange') is not None:
            temp_model = GetRegionConfigurationResponseBodyResultKibanaNodePropertiesAmountRange()
            self.amount_range = temp_model.from_map(m['amountRange'])
        if m.get('spec') is not None:
            self.spec = m.get('spec')
        return self


class GetRegionConfigurationResponseBodyResultMasterDiskList(TeaModel):
    def __init__(
        self,
        disk_type: str = None,
        max_size: int = None,
        min_size: int = None,
        scale_limit: int = None,
    ):
        self.disk_type = disk_type
        self.max_size = max_size
        self.min_size = min_size
        self.scale_limit = scale_limit

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.disk_type is not None:
            result['diskType'] = self.disk_type
        if self.max_size is not None:
            result['maxSize'] = self.max_size
        if self.min_size is not None:
            result['minSize'] = self.min_size
        if self.scale_limit is not None:
            result['scaleLimit'] = self.scale_limit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('diskType') is not None:
            self.disk_type = m.get('diskType')
        if m.get('maxSize') is not None:
            self.max_size = m.get('maxSize')
        if m.get('minSize') is not None:
            self.min_size = m.get('minSize')
        if m.get('scaleLimit') is not None:
            self.scale_limit = m.get('scaleLimit')
        return self


class GetRegionConfigurationResponseBodyResultNode(TeaModel):
    def __init__(
        self,
        max_amount: int = None,
        min_amount: int = None,
    ):
        self.max_amount = max_amount
        self.min_amount = min_amount

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_amount is not None:
            result['maxAmount'] = self.max_amount
        if self.min_amount is not None:
            result['minAmount'] = self.min_amount
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxAmount') is not None:
            self.max_amount = m.get('maxAmount')
        if m.get('minAmount') is not None:
            self.min_amount = m.get('minAmount')
        return self


class GetRegionConfigurationResponseBodyResultNodeSpecList(TeaModel):
    def __init__(
        self,
        cpu_count: int = None,
        disk: int = None,
        disk_type: str = None,
        enable: bool = None,
        memory_size: int = None,
        spec: str = None,
        spec_group_type: str = None,
    ):
        self.cpu_count = cpu_count
        self.disk = disk
        self.disk_type = disk_type
        self.enable = enable
        self.memory_size = memory_size
        self.spec = spec
        self.spec_group_type = spec_group_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu_count is not None:
            result['cpuCount'] = self.cpu_count
        if self.disk is not None:
            result['disk'] = self.disk
        if self.disk_type is not None:
            result['diskType'] = self.disk_type
        if self.enable is not None:
            result['enable'] = self.enable
        if self.memory_size is not None:
            result['memorySize'] = self.memory_size
        if self.spec is not None:
            result['spec'] = self.spec
        if self.spec_group_type is not None:
            result['specGroupType'] = self.spec_group_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cpuCount') is not None:
            self.cpu_count = m.get('cpuCount')
        if m.get('disk') is not None:
            self.disk = m.get('disk')
        if m.get('diskType') is not None:
            self.disk_type = m.get('diskType')
        if m.get('enable') is not None:
            self.enable = m.get('enable')
        if m.get('memorySize') is not None:
            self.memory_size = m.get('memorySize')
        if m.get('spec') is not None:
            self.spec = m.get('spec')
        if m.get('specGroupType') is not None:
            self.spec_group_type = m.get('specGroupType')
        return self


class GetRegionConfigurationResponseBodyResultSupportVersionsSupportVersionList(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class GetRegionConfigurationResponseBodyResultSupportVersions(TeaModel):
    def __init__(
        self,
        instance_category: str = None,
        support_version_list: List[GetRegionConfigurationResponseBodyResultSupportVersionsSupportVersionList] = None,
    ):
        self.instance_category = instance_category
        self.support_version_list = support_version_list

    def validate(self):
        if self.support_version_list:
            for k in self.support_version_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_category is not None:
            result['instanceCategory'] = self.instance_category
        result['supportVersionList'] = []
        if self.support_version_list is not None:
            for k in self.support_version_list:
                result['supportVersionList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('instanceCategory') is not None:
            self.instance_category = m.get('instanceCategory')
        self.support_version_list = []
        if m.get('supportVersionList') is not None:
            for k in m.get('supportVersionList'):
                temp_model = GetRegionConfigurationResponseBodyResultSupportVersionsSupportVersionList()
                self.support_version_list.append(temp_model.from_map(k))
        return self


class GetRegionConfigurationResponseBodyResultWarmNodePropertiesAmountRange(TeaModel):
    def __init__(
        self,
        max_amount: int = None,
        min_amount: int = None,
    ):
        self.max_amount = max_amount
        self.min_amount = min_amount

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_amount is not None:
            result['maxAmount'] = self.max_amount
        if self.min_amount is not None:
            result['minAmount'] = self.min_amount
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxAmount') is not None:
            self.max_amount = m.get('maxAmount')
        if m.get('minAmount') is not None:
            self.min_amount = m.get('minAmount')
        return self


class GetRegionConfigurationResponseBodyResultWarmNodePropertiesDiskList(TeaModel):
    def __init__(
        self,
        disk_encryption: bool = None,
        disk_type: str = None,
        max_size: int = None,
        min_size: int = None,
        scale_limit: int = None,
        value_limit_set: List[str] = None,
    ):
        self.disk_encryption = disk_encryption
        self.disk_type = disk_type
        self.max_size = max_size
        self.min_size = min_size
        self.scale_limit = scale_limit
        self.value_limit_set = value_limit_set

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.disk_encryption is not None:
            result['diskEncryption'] = self.disk_encryption
        if self.disk_type is not None:
            result['diskType'] = self.disk_type
        if self.max_size is not None:
            result['maxSize'] = self.max_size
        if self.min_size is not None:
            result['minSize'] = self.min_size
        if self.scale_limit is not None:
            result['scaleLimit'] = self.scale_limit
        if self.value_limit_set is not None:
            result['valueLimitSet'] = self.value_limit_set
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('diskEncryption') is not None:
            self.disk_encryption = m.get('diskEncryption')
        if m.get('diskType') is not None:
            self.disk_type = m.get('diskType')
        if m.get('maxSize') is not None:
            self.max_size = m.get('maxSize')
        if m.get('minSize') is not None:
            self.min_size = m.get('minSize')
        if m.get('scaleLimit') is not None:
            self.scale_limit = m.get('scaleLimit')
        if m.get('valueLimitSet') is not None:
            self.value_limit_set = m.get('valueLimitSet')
        return self


class GetRegionConfigurationResponseBodyResultWarmNodeProperties(TeaModel):
    def __init__(
        self,
        amount_range: GetRegionConfigurationResponseBodyResultWarmNodePropertiesAmountRange = None,
        disk_list: List[GetRegionConfigurationResponseBodyResultWarmNodePropertiesDiskList] = None,
        spec: List[str] = None,
    ):
        self.amount_range = amount_range
        self.disk_list = disk_list
        self.spec = spec

    def validate(self):
        if self.amount_range:
            self.amount_range.validate()
        if self.disk_list:
            for k in self.disk_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.amount_range is not None:
            result['amountRange'] = self.amount_range.to_map()
        result['diskList'] = []
        if self.disk_list is not None:
            for k in self.disk_list:
                result['diskList'].append(k.to_map() if k else None)
        if self.spec is not None:
            result['spec'] = self.spec
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('amountRange') is not None:
            temp_model = GetRegionConfigurationResponseBodyResultWarmNodePropertiesAmountRange()
            self.amount_range = temp_model.from_map(m['amountRange'])
        self.disk_list = []
        if m.get('diskList') is not None:
            for k in m.get('diskList'):
                temp_model = GetRegionConfigurationResponseBodyResultWarmNodePropertiesDiskList()
                self.disk_list.append(temp_model.from_map(k))
        if m.get('spec') is not None:
            self.spec = m.get('spec')
        return self


class GetRegionConfigurationResponseBodyResult(TeaModel):
    def __init__(
        self,
        client_node_amount_range: GetRegionConfigurationResponseBodyResultClientNodeAmountRange = None,
        client_node_disk_list: List[GetRegionConfigurationResponseBodyResultClientNodeDiskList] = None,
        client_node_spec: List[str] = None,
        create_url: str = None,
        data_disk_list: List[GetRegionConfigurationResponseBodyResultDataDiskList] = None,
        elastic_node_properties: GetRegionConfigurationResponseBodyResultElasticNodeProperties = None,
        env: str = None,
        es_versions: List[str] = None,
        es_versions_latest_list: List[GetRegionConfigurationResponseBodyResultEsVersionsLatestList] = None,
        instance_support_nodes: List[str] = None,
        jvm_confine: GetRegionConfigurationResponseBodyResultJvmConfine = None,
        kibana_node_properties: GetRegionConfigurationResponseBodyResultKibanaNodeProperties = None,
        master_disk_list: List[GetRegionConfigurationResponseBodyResultMasterDiskList] = None,
        master_spec: List[str] = None,
        node: GetRegionConfigurationResponseBodyResultNode = None,
        node_spec_list: List[GetRegionConfigurationResponseBodyResultNodeSpecList] = None,
        region_id: str = None,
        support_versions: List[GetRegionConfigurationResponseBodyResultSupportVersions] = None,
        warm_node_properties: GetRegionConfigurationResponseBodyResultWarmNodeProperties = None,
        zones: List[str] = None,
    ):
        self.client_node_amount_range = client_node_amount_range
        self.client_node_disk_list = client_node_disk_list
        self.client_node_spec = client_node_spec
        self.create_url = create_url
        self.data_disk_list = data_disk_list
        self.elastic_node_properties = elastic_node_properties
        self.env = env
        self.es_versions = es_versions
        self.es_versions_latest_list = es_versions_latest_list
        self.instance_support_nodes = instance_support_nodes
        self.jvm_confine = jvm_confine
        self.kibana_node_properties = kibana_node_properties
        self.master_disk_list = master_disk_list
        self.master_spec = master_spec
        self.node = node
        self.node_spec_list = node_spec_list
        self.region_id = region_id
        self.support_versions = support_versions
        self.warm_node_properties = warm_node_properties
        self.zones = zones

    def validate(self):
        if self.client_node_amount_range:
            self.client_node_amount_range.validate()
        if self.client_node_disk_list:
            for k in self.client_node_disk_list:
                if k:
                    k.validate()
        if self.data_disk_list:
            for k in self.data_disk_list:
                if k:
                    k.validate()
        if self.elastic_node_properties:
            self.elastic_node_properties.validate()
        if self.es_versions_latest_list:
            for k in self.es_versions_latest_list:
                if k:
                    k.validate()
        if self.jvm_confine:
            self.jvm_confine.validate()
        if self.kibana_node_properties:
            self.kibana_node_properties.validate()
        if self.master_disk_list:
            for k in self.master_disk_list:
                if k:
                    k.validate()
        if self.node:
            self.node.validate()
        if self.node_spec_list:
            for k in self.node_spec_list:
                if k:
                    k.validate()
        if self.support_versions:
            for k in self.support_versions:
                if k:
                    k.validate()
        if self.warm_node_properties:
            self.warm_node_properties.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_node_amount_range is not None:
            result['clientNodeAmountRange'] = self.client_node_amount_range.to_map()
        result['clientNodeDiskList'] = []
        if self.client_node_disk_list is not None:
            for k in self.client_node_disk_list:
                result['clientNodeDiskList'].append(k.to_map() if k else None)
        if self.client_node_spec is not None:
            result['clientNodeSpec'] = self.client_node_spec
        if self.create_url is not None:
            result['createUrl'] = self.create_url
        result['dataDiskList'] = []
        if self.data_disk_list is not None:
            for k in self.data_disk_list:
                result['dataDiskList'].append(k.to_map() if k else None)
        if self.elastic_node_properties is not None:
            result['elasticNodeProperties'] = self.elastic_node_properties.to_map()
        if self.env is not None:
            result['env'] = self.env
        if self.es_versions is not None:
            result['esVersions'] = self.es_versions
        result['esVersionsLatestList'] = []
        if self.es_versions_latest_list is not None:
            for k in self.es_versions_latest_list:
                result['esVersionsLatestList'].append(k.to_map() if k else None)
        if self.instance_support_nodes is not None:
            result['instanceSupportNodes'] = self.instance_support_nodes
        if self.jvm_confine is not None:
            result['jvmConfine'] = self.jvm_confine.to_map()
        if self.kibana_node_properties is not None:
            result['kibanaNodeProperties'] = self.kibana_node_properties.to_map()
        result['masterDiskList'] = []
        if self.master_disk_list is not None:
            for k in self.master_disk_list:
                result['masterDiskList'].append(k.to_map() if k else None)
        if self.master_spec is not None:
            result['masterSpec'] = self.master_spec
        if self.node is not None:
            result['node'] = self.node.to_map()
        result['nodeSpecList'] = []
        if self.node_spec_list is not None:
            for k in self.node_spec_list:
                result['nodeSpecList'].append(k.to_map() if k else None)
        if self.region_id is not None:
            result['regionId'] = self.region_id
        result['supportVersions'] = []
        if self.support_versions is not None:
            for k in self.support_versions:
                result['supportVersions'].append(k.to_map() if k else None)
        if self.warm_node_properties is not None:
            result['warmNodeProperties'] = self.warm_node_properties.to_map()
        if self.zones is not None:
            result['zones'] = self.zones
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientNodeAmountRange') is not None:
            temp_model = GetRegionConfigurationResponseBodyResultClientNodeAmountRange()
            self.client_node_amount_range = temp_model.from_map(m['clientNodeAmountRange'])
        self.client_node_disk_list = []
        if m.get('clientNodeDiskList') is not None:
            for k in m.get('clientNodeDiskList'):
                temp_model = GetRegionConfigurationResponseBodyResultClientNodeDiskList()
                self.client_node_disk_list.append(temp_model.from_map(k))
        if m.get('clientNodeSpec') is not None:
            self.client_node_spec = m.get('clientNodeSpec')
        if m.get('createUrl') is not None:
            self.create_url = m.get('createUrl')
        self.data_disk_list = []
        if m.get('dataDiskList') is not None:
            for k in m.get('dataDiskList'):
                temp_model = GetRegionConfigurationResponseBodyResultDataDiskList()
                self.data_disk_list.append(temp_model.from_map(k))
        if m.get('elasticNodeProperties') is not None:
            temp_model = GetRegionConfigurationResponseBodyResultElasticNodeProperties()
            self.elastic_node_properties = temp_model.from_map(m['elasticNodeProperties'])
        if m.get('env') is not None:
            self.env = m.get('env')
        if m.get('esVersions') is not None:
            self.es_versions = m.get('esVersions')
        self.es_versions_latest_list = []
        if m.get('esVersionsLatestList') is not None:
            for k in m.get('esVersionsLatestList'):
                temp_model = GetRegionConfigurationResponseBodyResultEsVersionsLatestList()
                self.es_versions_latest_list.append(temp_model.from_map(k))
        if m.get('instanceSupportNodes') is not None:
            self.instance_support_nodes = m.get('instanceSupportNodes')
        if m.get('jvmConfine') is not None:
            temp_model = GetRegionConfigurationResponseBodyResultJvmConfine()
            self.jvm_confine = temp_model.from_map(m['jvmConfine'])
        if m.get('kibanaNodeProperties') is not None:
            temp_model = GetRegionConfigurationResponseBodyResultKibanaNodeProperties()
            self.kibana_node_properties = temp_model.from_map(m['kibanaNodeProperties'])
        self.master_disk_list = []
        if m.get('masterDiskList') is not None:
            for k in m.get('masterDiskList'):
                temp_model = GetRegionConfigurationResponseBodyResultMasterDiskList()
                self.master_disk_list.append(temp_model.from_map(k))
        if m.get('masterSpec') is not None:
            self.master_spec = m.get('masterSpec')
        if m.get('node') is not None:
            temp_model = GetRegionConfigurationResponseBodyResultNode()
            self.node = temp_model.from_map(m['node'])
        self.node_spec_list = []
        if m.get('nodeSpecList') is not None:
            for k in m.get('nodeSpecList'):
                temp_model = GetRegionConfigurationResponseBodyResultNodeSpecList()
                self.node_spec_list.append(temp_model.from_map(k))
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        self.support_versions = []
        if m.get('supportVersions') is not None:
            for k in m.get('supportVersions'):
                temp_model = GetRegionConfigurationResponseBodyResultSupportVersions()
                self.support_versions.append(temp_model.from_map(k))
        if m.get('warmNodeProperties') is not None:
            temp_model = GetRegionConfigurationResponseBodyResultWarmNodeProperties()
            self.warm_node_properties = temp_model.from_map(m['warmNodeProperties'])
        if m.get('zones') is not None:
            self.zones = m.get('zones')
        return self


class GetRegionConfigurationResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: GetRegionConfigurationResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = GetRegionConfigurationResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class GetRegionConfigurationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetRegionConfigurationResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetRegionConfigurationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSuggestShrinkableNodesRequest(TeaModel):
    def __init__(
        self,
        count: int = None,
        ignore_status: bool = None,
        node_type: str = None,
    ):
        self.count = count
        self.ignore_status = ignore_status
        self.node_type = node_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['count'] = self.count
        if self.ignore_status is not None:
            result['ignoreStatus'] = self.ignore_status
        if self.node_type is not None:
            result['nodeType'] = self.node_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('count') is not None:
            self.count = m.get('count')
        if m.get('ignoreStatus') is not None:
            self.ignore_status = m.get('ignoreStatus')
        if m.get('nodeType') is not None:
            self.node_type = m.get('nodeType')
        return self


class GetSuggestShrinkableNodesResponseBodyResult(TeaModel):
    def __init__(
        self,
        host: str = None,
        port: int = None,
    ):
        self.host = host
        self.port = port

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host is not None:
            result['host'] = self.host
        if self.port is not None:
            result['port'] = self.port
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('host') is not None:
            self.host = m.get('host')
        if m.get('port') is not None:
            self.port = m.get('port')
        return self


class GetSuggestShrinkableNodesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[GetSuggestShrinkableNodesResponseBodyResult] = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = GetSuggestShrinkableNodesResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class GetSuggestShrinkableNodesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetSuggestShrinkableNodesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetSuggestShrinkableNodesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTransferableNodesRequest(TeaModel):
    def __init__(
        self,
        count: int = None,
        node_type: str = None,
    ):
        self.count = count
        self.node_type = node_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['count'] = self.count
        if self.node_type is not None:
            result['nodeType'] = self.node_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('count') is not None:
            self.count = m.get('count')
        if m.get('nodeType') is not None:
            self.node_type = m.get('nodeType')
        return self


class GetTransferableNodesResponseBodyResult(TeaModel):
    def __init__(
        self,
        host: str = None,
        port: int = None,
    ):
        self.host = host
        self.port = port

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host is not None:
            result['host'] = self.host
        if self.port is not None:
            result['port'] = self.port
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('host') is not None:
            self.host = m.get('host')
        if m.get('port') is not None:
            self.port = m.get('port')
        return self


class GetTransferableNodesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[GetTransferableNodesResponseBodyResult] = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = GetTransferableNodesResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class GetTransferableNodesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetTransferableNodesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetTransferableNodesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InitializeOperationRoleRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
    ):
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class InitializeOperationRoleResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class InitializeOperationRoleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: InitializeOperationRoleResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = InitializeOperationRoleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InstallAckOperatorRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
    ):
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class InstallAckOperatorResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class InstallAckOperatorResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: InstallAckOperatorResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = InstallAckOperatorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InstallKibanaSystemPluginRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
    ):
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        return self


class InstallKibanaSystemPluginResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[str] = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class InstallKibanaSystemPluginResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: InstallKibanaSystemPluginResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = InstallKibanaSystemPluginResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InstallLogstashSystemPluginRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
    ):
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        return self


class InstallLogstashSystemPluginResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[str] = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class InstallLogstashSystemPluginResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: InstallLogstashSystemPluginResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = InstallLogstashSystemPluginResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InstallSystemPluginRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
    ):
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        return self


class InstallSystemPluginResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[str] = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class InstallSystemPluginResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: InstallSystemPluginResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = InstallSystemPluginResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InstallUserPluginsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[str] = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class InstallUserPluginsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: InstallUserPluginsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = InstallUserPluginsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InterruptElasticsearchTaskRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
    ):
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        return self


class InterruptElasticsearchTaskResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: bool = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class InterruptElasticsearchTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: InterruptElasticsearchTaskResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = InterruptElasticsearchTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InterruptLogstashTaskRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
    ):
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        return self


class InterruptLogstashTaskResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: bool = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class InterruptLogstashTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: InterruptLogstashTaskResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = InterruptLogstashTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAckClustersRequest(TeaModel):
    def __init__(
        self,
        page: int = None,
        size: int = None,
        vpc_id: str = None,
    ):
        self.page = page
        self.size = size
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page is not None:
            result['page'] = self.page
        if self.size is not None:
            result['size'] = self.size
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        return self


class ListAckClustersResponseBodyResult(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        cluster_type: str = None,
        name: str = None,
        vpc_id: str = None,
    ):
        self.cluster_id = cluster_id
        self.cluster_type = cluster_type
        self.name = name
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['clusterId'] = self.cluster_id
        if self.cluster_type is not None:
            result['clusterType'] = self.cluster_type
        if self.name is not None:
            result['name'] = self.name
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clusterId') is not None:
            self.cluster_id = m.get('clusterId')
        if m.get('clusterType') is not None:
            self.cluster_type = m.get('clusterType')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        return self


class ListAckClustersResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[ListAckClustersResponseBodyResult] = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListAckClustersResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListAckClustersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListAckClustersResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListAckClustersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAckNamespacesRequest(TeaModel):
    def __init__(
        self,
        page: int = None,
        size: int = None,
    ):
        self.page = page
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page is not None:
            result['page'] = self.page
        if self.size is not None:
            result['size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('size') is not None:
            self.size = m.get('size')
        return self


class ListAckNamespacesResponseBodyResult(TeaModel):
    def __init__(
        self,
        namespace: str = None,
        status: str = None,
    ):
        self.namespace = namespace
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class ListAckNamespacesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[ListAckNamespacesResponseBodyResult] = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListAckNamespacesResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListAckNamespacesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListAckNamespacesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListAckNamespacesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAllNodeRequest(TeaModel):
    def __init__(
        self,
        extended: bool = None,
    ):
        self.extended = extended

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extended is not None:
            result['extended'] = self.extended
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('extended') is not None:
            self.extended = m.get('extended')
        return self


class ListAllNodeResponseBodyResult(TeaModel):
    def __init__(
        self,
        cpu_percent: str = None,
        disk_used_percent: str = None,
        health: str = None,
        heap_percent: str = None,
        host: str = None,
        load_one_m: str = None,
        node_type: str = None,
        port: int = None,
        zone_id: str = None,
    ):
        self.cpu_percent = cpu_percent
        self.disk_used_percent = disk_used_percent
        self.health = health
        self.heap_percent = heap_percent
        self.host = host
        self.load_one_m = load_one_m
        self.node_type = node_type
        self.port = port
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu_percent is not None:
            result['cpuPercent'] = self.cpu_percent
        if self.disk_used_percent is not None:
            result['diskUsedPercent'] = self.disk_used_percent
        if self.health is not None:
            result['health'] = self.health
        if self.heap_percent is not None:
            result['heapPercent'] = self.heap_percent
        if self.host is not None:
            result['host'] = self.host
        if self.load_one_m is not None:
            result['loadOneM'] = self.load_one_m
        if self.node_type is not None:
            result['nodeType'] = self.node_type
        if self.port is not None:
            result['port'] = self.port
        if self.zone_id is not None:
            result['zoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cpuPercent') is not None:
            self.cpu_percent = m.get('cpuPercent')
        if m.get('diskUsedPercent') is not None:
            self.disk_used_percent = m.get('diskUsedPercent')
        if m.get('health') is not None:
            self.health = m.get('health')
        if m.get('heapPercent') is not None:
            self.heap_percent = m.get('heapPercent')
        if m.get('host') is not None:
            self.host = m.get('host')
        if m.get('loadOneM') is not None:
            self.load_one_m = m.get('loadOneM')
        if m.get('nodeType') is not None:
            self.node_type = m.get('nodeType')
        if m.get('port') is not None:
            self.port = m.get('port')
        if m.get('zoneId') is not None:
            self.zone_id = m.get('zoneId')
        return self


class ListAllNodeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[ListAllNodeResponseBodyResult] = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListAllNodeResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListAllNodeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListAllNodeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListAllNodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAlternativeSnapshotReposRequest(TeaModel):
    def __init__(
        self,
        already_set_items: bool = None,
    ):
        self.already_set_items = already_set_items

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.already_set_items is not None:
            result['alreadySetItems'] = self.already_set_items
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alreadySetItems') is not None:
            self.already_set_items = m.get('alreadySetItems')
        return self


class ListAlternativeSnapshotReposResponseBodyResult(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        repo_path: str = None,
    ):
        self.instance_id = instance_id
        self.repo_path = repo_path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.repo_path is not None:
            result['repoPath'] = self.repo_path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('repoPath') is not None:
            self.repo_path = m.get('repoPath')
        return self


class ListAlternativeSnapshotReposResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[ListAlternativeSnapshotReposResponseBodyResult] = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListAlternativeSnapshotReposResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListAlternativeSnapshotReposResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListAlternativeSnapshotReposResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListAlternativeSnapshotReposResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListApmRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        instance_id: str = None,
        output: str = None,
        page: int = None,
        size: int = None,
    ):
        self.description = description
        self.instance_id = instance_id
        self.output = output
        self.page = page
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.output is not None:
            result['output'] = self.output
        if self.page is not None:
            result['page'] = self.page
        if self.size is not None:
            result['size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('output') is not None:
            self.output = m.get('output')
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('size') is not None:
            self.size = m.get('size')
        return self


class ListApmResponseBodyHeaders(TeaModel):
    def __init__(
        self,
        x_total_count: int = None,
    ):
        self.x_total_count = x_total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.x_total_count is not None:
            result['X-Total-Count'] = self.x_total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('X-Total-Count') is not None:
            self.x_total_count = m.get('X-Total-Count')
        return self


class ListApmResponseBodyResult(TeaModel):
    def __init__(
        self,
        created_at: str = None,
        deployed_replica: int = None,
        description: str = None,
        instance_id: str = None,
        node_amount: int = None,
        output_es: str = None,
        output_esuser_name: str = None,
        owner_id: str = None,
        payment_type: str = None,
        region: str = None,
        replica: int = None,
        resource_spec: str = None,
        status: str = None,
        version: str = None,
        vpc_id: str = None,
        vs_area: str = None,
        vswitch_id: str = None,
    ):
        self.created_at = created_at
        self.deployed_replica = deployed_replica
        self.description = description
        self.instance_id = instance_id
        self.node_amount = node_amount
        self.output_es = output_es
        self.output_esuser_name = output_esuser_name
        self.owner_id = owner_id
        self.payment_type = payment_type
        self.region = region
        self.replica = replica
        self.resource_spec = resource_spec
        self.status = status
        self.version = version
        self.vpc_id = vpc_id
        self.vs_area = vs_area
        self.vswitch_id = vswitch_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_at is not None:
            result['createdAt'] = self.created_at
        if self.deployed_replica is not None:
            result['deployedReplica'] = self.deployed_replica
        if self.description is not None:
            result['description'] = self.description
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.node_amount is not None:
            result['nodeAmount'] = self.node_amount
        if self.output_es is not None:
            result['outputES'] = self.output_es
        if self.output_esuser_name is not None:
            result['outputESUserName'] = self.output_esuser_name
        if self.owner_id is not None:
            result['ownerId'] = self.owner_id
        if self.payment_type is not None:
            result['paymentType'] = self.payment_type
        if self.region is not None:
            result['region'] = self.region
        if self.replica is not None:
            result['replica'] = self.replica
        if self.resource_spec is not None:
            result['resourceSpec'] = self.resource_spec
        if self.status is not None:
            result['status'] = self.status
        if self.version is not None:
            result['version'] = self.version
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        if self.vs_area is not None:
            result['vsArea'] = self.vs_area
        if self.vswitch_id is not None:
            result['vswitchId'] = self.vswitch_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')
        if m.get('deployedReplica') is not None:
            self.deployed_replica = m.get('deployedReplica')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('nodeAmount') is not None:
            self.node_amount = m.get('nodeAmount')
        if m.get('outputES') is not None:
            self.output_es = m.get('outputES')
        if m.get('outputESUserName') is not None:
            self.output_esuser_name = m.get('outputESUserName')
        if m.get('ownerId') is not None:
            self.owner_id = m.get('ownerId')
        if m.get('paymentType') is not None:
            self.payment_type = m.get('paymentType')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('replica') is not None:
            self.replica = m.get('replica')
        if m.get('resourceSpec') is not None:
            self.resource_spec = m.get('resourceSpec')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('version') is not None:
            self.version = m.get('version')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        if m.get('vsArea') is not None:
            self.vs_area = m.get('vsArea')
        if m.get('vswitchId') is not None:
            self.vswitch_id = m.get('vswitchId')
        return self


class ListApmResponseBody(TeaModel):
    def __init__(
        self,
        headers: ListApmResponseBodyHeaders = None,
        request_id: str = None,
        result: List[ListApmResponseBodyResult] = None,
    ):
        self.headers = headers
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.headers:
            self.headers.validate()
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['Headers'] = self.headers.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Headers') is not None:
            temp_model = ListApmResponseBodyHeaders()
            self.headers = temp_model.from_map(m['Headers'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListApmResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListApmResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListApmResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListApmResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAvailableEsInstanceIdsResponseBodyResult(TeaModel):
    def __init__(
        self,
        description: str = None,
        endpoint: str = None,
        es_instance_id: str = None,
        kibana_endpoint: str = None,
    ):
        self.description = description
        self.endpoint = endpoint
        self.es_instance_id = es_instance_id
        self.kibana_endpoint = kibana_endpoint

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.endpoint is not None:
            result['endpoint'] = self.endpoint
        if self.es_instance_id is not None:
            result['esInstanceId'] = self.es_instance_id
        if self.kibana_endpoint is not None:
            result['kibanaEndpoint'] = self.kibana_endpoint
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('endpoint') is not None:
            self.endpoint = m.get('endpoint')
        if m.get('esInstanceId') is not None:
            self.es_instance_id = m.get('esInstanceId')
        if m.get('kibanaEndpoint') is not None:
            self.kibana_endpoint = m.get('kibanaEndpoint')
        return self


class ListAvailableEsInstanceIdsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[ListAvailableEsInstanceIdsResponseBodyResult] = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListAvailableEsInstanceIdsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListAvailableEsInstanceIdsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListAvailableEsInstanceIdsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListAvailableEsInstanceIdsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCollectorsRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        name: str = None,
        page: int = None,
        res_id: str = None,
        size: int = None,
        source_type: str = None,
    ):
        self.instance_id = instance_id
        self.name = name
        self.page = page
        self.res_id = res_id
        self.size = size
        self.source_type = source_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.name is not None:
            result['name'] = self.name
        if self.page is not None:
            result['page'] = self.page
        if self.res_id is not None:
            result['resId'] = self.res_id
        if self.size is not None:
            result['size'] = self.size
        if self.source_type is not None:
            result['sourceType'] = self.source_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('resId') is not None:
            self.res_id = m.get('resId')
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')
        return self


class ListCollectorsResponseBodyHeaders(TeaModel):
    def __init__(
        self,
        x_total_count: int = None,
    ):
        self.x_total_count = x_total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.x_total_count is not None:
            result['X-Total-Count'] = self.x_total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('X-Total-Count') is not None:
            self.x_total_count = m.get('X-Total-Count')
        return self


class ListCollectorsResponseBodyResultConfigs(TeaModel):
    def __init__(
        self,
        content: str = None,
        file_name: str = None,
    ):
        self.content = content
        self.file_name = file_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ListCollectorsResponseBodyResultExtendConfigsMachines(TeaModel):
    def __init__(
        self,
        agent_status: str = None,
        instance_id: str = None,
    ):
        self.agent_status = agent_status
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ListCollectorsResponseBodyResultExtendConfigs(TeaModel):
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
        machines: List[ListCollectorsResponseBodyResultExtendConfigsMachines] = None,
        protocol: str = None,
        success_pods_count: str = None,
        total_pods_count: str = None,
        type: str = None,
        user_name: str = None,
    ):
        self.config_type = config_type
        self.enable_monitoring = enable_monitoring
        self.group_id = group_id
        self.host = host
        self.hosts = hosts
        self.instance_id = instance_id
        self.instance_type = instance_type
        self.kibana_host = kibana_host
        self.machines = machines
        self.protocol = protocol
        self.success_pods_count = success_pods_count
        self.total_pods_count = total_pods_count
        self.type = type
        self.user_name = user_name

    def validate(self):
        if self.machines:
            for k in self.machines:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            for k in self.machines:
                result['machines'].append(k.to_map() if k else None)
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
            for k in m.get('machines'):
                temp_model = ListCollectorsResponseBodyResultExtendConfigsMachines()
                self.machines.append(temp_model.from_map(k))
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


class ListCollectorsResponseBodyResult(TeaModel):
    def __init__(
        self,
        collector_paths: List[str] = None,
        configs: List[ListCollectorsResponseBodyResultConfigs] = None,
        dry_run: bool = None,
        extend_configs: List[ListCollectorsResponseBodyResultExtendConfigs] = None,
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
        self.configs = configs
        self.dry_run = dry_run
        self.extend_configs = extend_configs
        self.gmt_created_time = gmt_created_time
        self.gmt_update_time = gmt_update_time
        self.name = name
        self.owner_id = owner_id
        self.res_id = res_id
        self.res_type = res_type
        self.res_version = res_version
        self.status = status
        self.vpc_id = vpc_id

    def validate(self):
        if self.configs:
            for k in self.configs:
                if k:
                    k.validate()
        if self.extend_configs:
            for k in self.extend_configs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.collector_paths is not None:
            result['collectorPaths'] = self.collector_paths
        result['configs'] = []
        if self.configs is not None:
            for k in self.configs:
                result['configs'].append(k.to_map() if k else None)
        if self.dry_run is not None:
            result['dryRun'] = self.dry_run
        result['extendConfigs'] = []
        if self.extend_configs is not None:
            for k in self.extend_configs:
                result['extendConfigs'].append(k.to_map() if k else None)
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
            for k in m.get('configs'):
                temp_model = ListCollectorsResponseBodyResultConfigs()
                self.configs.append(temp_model.from_map(k))
        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')
        self.extend_configs = []
        if m.get('extendConfigs') is not None:
            for k in m.get('extendConfigs'):
                temp_model = ListCollectorsResponseBodyResultExtendConfigs()
                self.extend_configs.append(temp_model.from_map(k))
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


class ListCollectorsResponseBody(TeaModel):
    def __init__(
        self,
        headers: ListCollectorsResponseBodyHeaders = None,
        request_id: str = None,
        result: List[ListCollectorsResponseBodyResult] = None,
    ):
        self.headers = headers
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.headers:
            self.headers.validate()
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['Headers'] = self.headers.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Headers') is not None:
            temp_model = ListCollectorsResponseBodyHeaders()
            self.headers = temp_model.from_map(m['Headers'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListCollectorsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListCollectorsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListCollectorsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListCollectorsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListComponentIndicesRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        page: int = None,
        size: int = None,
    ):
        self.name = name
        self.page = page
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.page is not None:
            result['page'] = self.page
        if self.size is not None:
            result['size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('size') is not None:
            self.size = m.get('size')
        return self


class ListComponentIndicesResponseBodyHeaders(TeaModel):
    def __init__(
        self,
        x_total_count: int = None,
    ):
        self.x_total_count = x_total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.x_total_count is not None:
            result['X-Total-Count'] = self.x_total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('X-Total-Count') is not None:
            self.x_total_count = m.get('X-Total-Count')
        return self


class ListComponentIndicesResponseBodyResultContentTemplateSettingsIndexLifecycle(TeaModel):
    def __init__(
        self,
        name: str = None,
    ):
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class ListComponentIndicesResponseBodyResultContentTemplateSettingsIndex(TeaModel):
    def __init__(
        self,
        codec: str = None,
        lifecycle: ListComponentIndicesResponseBodyResultContentTemplateSettingsIndexLifecycle = None,
    ):
        self.codec = codec
        self.lifecycle = lifecycle

    def validate(self):
        if self.lifecycle:
            self.lifecycle.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.codec is not None:
            result['codec'] = self.codec
        if self.lifecycle is not None:
            result['lifecycle'] = self.lifecycle.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('codec') is not None:
            self.codec = m.get('codec')
        if m.get('lifecycle') is not None:
            temp_model = ListComponentIndicesResponseBodyResultContentTemplateSettingsIndexLifecycle()
            self.lifecycle = temp_model.from_map(m['lifecycle'])
        return self


class ListComponentIndicesResponseBodyResultContentTemplateSettings(TeaModel):
    def __init__(
        self,
        index: ListComponentIndicesResponseBodyResultContentTemplateSettingsIndex = None,
    ):
        self.index = index

    def validate(self):
        if self.index:
            self.index.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.index is not None:
            result['index'] = self.index.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('index') is not None:
            temp_model = ListComponentIndicesResponseBodyResultContentTemplateSettingsIndex()
            self.index = temp_model.from_map(m['index'])
        return self


class ListComponentIndicesResponseBodyResultContentTemplate(TeaModel):
    def __init__(
        self,
        settings: ListComponentIndicesResponseBodyResultContentTemplateSettings = None,
    ):
        self.settings = settings

    def validate(self):
        if self.settings:
            self.settings.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.settings is not None:
            result['settings'] = self.settings.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('settings') is not None:
            temp_model = ListComponentIndicesResponseBodyResultContentTemplateSettings()
            self.settings = temp_model.from_map(m['settings'])
        return self


class ListComponentIndicesResponseBodyResultContent(TeaModel):
    def __init__(
        self,
        meta: Dict[str, Any] = None,
        template: ListComponentIndicesResponseBodyResultContentTemplate = None,
        version: int = None,
    ):
        self.meta = meta
        self.template = template
        self.version = version

    def validate(self):
        if self.template:
            self.template.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.meta is not None:
            result['_meta'] = self.meta
        if self.template is not None:
            result['template'] = self.template.to_map()
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('_meta') is not None:
            self.meta = m.get('_meta')
        if m.get('template') is not None:
            temp_model = ListComponentIndicesResponseBodyResultContentTemplate()
            self.template = temp_model.from_map(m['template'])
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class ListComponentIndicesResponseBodyResult(TeaModel):
    def __init__(
        self,
        composed: List[str] = None,
        content: ListComponentIndicesResponseBodyResultContent = None,
        name: str = None,
    ):
        self.composed = composed
        self.content = content
        self.name = name

    def validate(self):
        if self.content:
            self.content.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.composed is not None:
            result['composed'] = self.composed
        if self.content is not None:
            result['content'] = self.content.to_map()
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('composed') is not None:
            self.composed = m.get('composed')
        if m.get('content') is not None:
            temp_model = ListComponentIndicesResponseBodyResultContent()
            self.content = temp_model.from_map(m['content'])
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class ListComponentIndicesResponseBody(TeaModel):
    def __init__(
        self,
        headers: ListComponentIndicesResponseBodyHeaders = None,
        request_id: str = None,
        result: List[ListComponentIndicesResponseBodyResult] = None,
    ):
        self.headers = headers
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.headers:
            self.headers.validate()
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['Headers'] = self.headers.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Headers') is not None:
            temp_model = ListComponentIndicesResponseBodyHeaders()
            self.headers = temp_model.from_map(m['Headers'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListComponentIndicesResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListComponentIndicesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListComponentIndicesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListComponentIndicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListConnectedClustersResponseBodyResultResult(TeaModel):
    def __init__(
        self,
        instances: str = None,
        network_type: str = None,
    ):
        self.instances = instances
        self.network_type = network_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instances is not None:
            result['instances'] = self.instances
        if self.network_type is not None:
            result['networkType'] = self.network_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('instances') is not None:
            self.instances = m.get('instances')
        if m.get('networkType') is not None:
            self.network_type = m.get('networkType')
        return self


class ListConnectedClustersResponseBodyResult(TeaModel):
    def __init__(
        self,
        result: List[ListConnectedClustersResponseBodyResultResult] = None,
    ):
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListConnectedClustersResponseBodyResultResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListConnectedClustersResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: ListConnectedClustersResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = ListConnectedClustersResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class ListConnectedClustersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListConnectedClustersResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListConnectedClustersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDataStreamsRequest(TeaModel):
    def __init__(
        self,
        is_managed: bool = None,
        name: str = None,
    ):
        self.is_managed = is_managed
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_managed is not None:
            result['isManaged'] = self.is_managed
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('isManaged') is not None:
            self.is_managed = m.get('isManaged')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class ListDataStreamsResponseBodyHeaders(TeaModel):
    def __init__(
        self,
        x_managed_count: int = None,
        x_managed_storage_size: int = None,
    ):
        self.x_managed_count = x_managed_count
        self.x_managed_storage_size = x_managed_storage_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.x_managed_count is not None:
            result['X-Managed-Count'] = self.x_managed_count
        if self.x_managed_storage_size is not None:
            result['X-Managed-StorageSize'] = self.x_managed_storage_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('X-Managed-Count') is not None:
            self.x_managed_count = m.get('X-Managed-Count')
        if m.get('X-Managed-StorageSize') is not None:
            self.x_managed_storage_size = m.get('X-Managed-StorageSize')
        return self


class ListDataStreamsResponseBodyResultIndices(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        health: str = None,
        is_managed: bool = None,
        managed_status: str = None,
        name: str = None,
        size: int = None,
    ):
        self.create_time = create_time
        self.health = health
        self.is_managed = is_managed
        self.managed_status = managed_status
        self.name = name
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.health is not None:
            result['health'] = self.health
        if self.is_managed is not None:
            result['isManaged'] = self.is_managed
        if self.managed_status is not None:
            result['managedStatus'] = self.managed_status
        if self.name is not None:
            result['name'] = self.name
        if self.size is not None:
            result['size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('health') is not None:
            self.health = m.get('health')
        if m.get('isManaged') is not None:
            self.is_managed = m.get('isManaged')
        if m.get('managedStatus') is not None:
            self.managed_status = m.get('managedStatus')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('size') is not None:
            self.size = m.get('size')
        return self


class ListDataStreamsResponseBodyResult(TeaModel):
    def __init__(
        self,
        health: str = None,
        ilm_policy_name: str = None,
        index_template_name: str = None,
        indices: List[ListDataStreamsResponseBodyResultIndices] = None,
        managed_storage_size: int = None,
        name: str = None,
        total_storage_size: int = None,
    ):
        self.health = health
        self.ilm_policy_name = ilm_policy_name
        self.index_template_name = index_template_name
        self.indices = indices
        self.managed_storage_size = managed_storage_size
        self.name = name
        self.total_storage_size = total_storage_size

    def validate(self):
        if self.indices:
            for k in self.indices:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.health is not None:
            result['health'] = self.health
        if self.ilm_policy_name is not None:
            result['ilmPolicyName'] = self.ilm_policy_name
        if self.index_template_name is not None:
            result['indexTemplateName'] = self.index_template_name
        result['indices'] = []
        if self.indices is not None:
            for k in self.indices:
                result['indices'].append(k.to_map() if k else None)
        if self.managed_storage_size is not None:
            result['managedStorageSize'] = self.managed_storage_size
        if self.name is not None:
            result['name'] = self.name
        if self.total_storage_size is not None:
            result['totalStorageSize'] = self.total_storage_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('health') is not None:
            self.health = m.get('health')
        if m.get('ilmPolicyName') is not None:
            self.ilm_policy_name = m.get('ilmPolicyName')
        if m.get('indexTemplateName') is not None:
            self.index_template_name = m.get('indexTemplateName')
        self.indices = []
        if m.get('indices') is not None:
            for k in m.get('indices'):
                temp_model = ListDataStreamsResponseBodyResultIndices()
                self.indices.append(temp_model.from_map(k))
        if m.get('managedStorageSize') is not None:
            self.managed_storage_size = m.get('managedStorageSize')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('totalStorageSize') is not None:
            self.total_storage_size = m.get('totalStorageSize')
        return self


class ListDataStreamsResponseBody(TeaModel):
    def __init__(
        self,
        headers: ListDataStreamsResponseBodyHeaders = None,
        request_id: str = None,
        result: List[ListDataStreamsResponseBodyResult] = None,
    ):
        self.headers = headers
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.headers:
            self.headers.validate()
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['Headers'] = self.headers.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Headers') is not None:
            temp_model = ListDataStreamsResponseBodyHeaders()
            self.headers = temp_model.from_map(m['Headers'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListDataStreamsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListDataStreamsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListDataStreamsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListDataStreamsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDataTasksResponseBodyResultSinkCluster(TeaModel):
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
        self.data_source_type = data_source_type
        self.endpoint = endpoint
        self.index = index
        self.type = type
        self.vpc_id = vpc_id
        self.vpc_instance_id = vpc_instance_id
        self.vpc_instance_port = vpc_instance_port

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ListDataTasksResponseBodyResultSourceCluster(TeaModel):
    def __init__(
        self,
        data_source_type: str = None,
        index: str = None,
        mapping: str = None,
        routing: str = None,
        settings: str = None,
        type: str = None,
    ):
        self.data_source_type = data_source_type
        self.index = index
        self.mapping = mapping
        self.routing = routing
        self.settings = settings
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ListDataTasksResponseBodyResult(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        sink_cluster: ListDataTasksResponseBodyResultSinkCluster = None,
        source_cluster: ListDataTasksResponseBodyResultSourceCluster = None,
        status: str = None,
        task_id: str = None,
    ):
        self.create_time = create_time
        self.sink_cluster = sink_cluster
        self.source_cluster = source_cluster
        self.status = status
        self.task_id = task_id

    def validate(self):
        if self.sink_cluster:
            self.sink_cluster.validate()
        if self.source_cluster:
            self.source_cluster.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = ListDataTasksResponseBodyResultSinkCluster()
            self.sink_cluster = temp_model.from_map(m['sinkCluster'])
        if m.get('sourceCluster') is not None:
            temp_model = ListDataTasksResponseBodyResultSourceCluster()
            self.source_cluster = temp_model.from_map(m['sourceCluster'])
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        return self


class ListDataTasksResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[ListDataTasksResponseBodyResult] = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListDataTasksResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListDataTasksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListDataTasksResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListDataTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDefaultCollectorConfigurationsRequest(TeaModel):
    def __init__(
        self,
        res_type: str = None,
        res_version: str = None,
        source_type: str = None,
    ):
        self.res_type = res_type
        self.res_version = res_version
        self.source_type = source_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.res_type is not None:
            result['resType'] = self.res_type
        if self.res_version is not None:
            result['resVersion'] = self.res_version
        if self.source_type is not None:
            result['sourceType'] = self.source_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('resType') is not None:
            self.res_type = m.get('resType')
        if m.get('resVersion') is not None:
            self.res_version = m.get('resVersion')
        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')
        return self


class ListDefaultCollectorConfigurationsResponseBodyResult(TeaModel):
    def __init__(
        self,
        content: str = None,
        file_name: str = None,
    ):
        self.content = content
        self.file_name = file_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ListDefaultCollectorConfigurationsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[ListDefaultCollectorConfigurationsResponseBodyResult] = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListDefaultCollectorConfigurationsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListDefaultCollectorConfigurationsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListDefaultCollectorConfigurationsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListDefaultCollectorConfigurationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDeprecatedTemplatesRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        page: int = None,
        size: int = None,
    ):
        self.name = name
        self.page = page
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.page is not None:
            result['page'] = self.page
        if self.size is not None:
            result['size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('size') is not None:
            self.size = m.get('size')
        return self


class ListDeprecatedTemplatesResponseBodyHeaders(TeaModel):
    def __init__(
        self,
        x_total_count: int = None,
    ):
        self.x_total_count = x_total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.x_total_count is not None:
            result['X-Total-Count'] = self.x_total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('X-Total-Count') is not None:
            self.x_total_count = m.get('X-Total-Count')
        return self


class ListDeprecatedTemplatesResponseBodyResultTemplate(TeaModel):
    def __init__(
        self,
        aliases: str = None,
        mappings: str = None,
        settings: str = None,
    ):
        self.aliases = aliases
        self.mappings = mappings
        self.settings = settings

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aliases is not None:
            result['aliases'] = self.aliases
        if self.mappings is not None:
            result['mappings'] = self.mappings
        if self.settings is not None:
            result['settings'] = self.settings
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('aliases') is not None:
            self.aliases = m.get('aliases')
        if m.get('mappings') is not None:
            self.mappings = m.get('mappings')
        if m.get('settings') is not None:
            self.settings = m.get('settings')
        return self


class ListDeprecatedTemplatesResponseBodyResult(TeaModel):
    def __init__(
        self,
        data_stream: bool = None,
        index_patterns: List[str] = None,
        index_template: str = None,
        order: int = None,
        template: ListDeprecatedTemplatesResponseBodyResultTemplate = None,
        version: str = None,
    ):
        self.data_stream = data_stream
        self.index_patterns = index_patterns
        self.index_template = index_template
        self.order = order
        self.template = template
        self.version = version

    def validate(self):
        if self.template:
            self.template.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_stream is not None:
            result['dataStream'] = self.data_stream
        if self.index_patterns is not None:
            result['indexPatterns'] = self.index_patterns
        if self.index_template is not None:
            result['indexTemplate'] = self.index_template
        if self.order is not None:
            result['order'] = self.order
        if self.template is not None:
            result['template'] = self.template.to_map()
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dataStream') is not None:
            self.data_stream = m.get('dataStream')
        if m.get('indexPatterns') is not None:
            self.index_patterns = m.get('indexPatterns')
        if m.get('indexTemplate') is not None:
            self.index_template = m.get('indexTemplate')
        if m.get('order') is not None:
            self.order = m.get('order')
        if m.get('template') is not None:
            temp_model = ListDeprecatedTemplatesResponseBodyResultTemplate()
            self.template = temp_model.from_map(m['template'])
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class ListDeprecatedTemplatesResponseBody(TeaModel):
    def __init__(
        self,
        headers: ListDeprecatedTemplatesResponseBodyHeaders = None,
        request_id: str = None,
        result: List[ListDeprecatedTemplatesResponseBodyResult] = None,
    ):
        self.headers = headers
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.headers:
            self.headers.validate()
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['Headers'] = self.headers.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Headers') is not None:
            temp_model = ListDeprecatedTemplatesResponseBodyHeaders()
            self.headers = temp_model.from_map(m['Headers'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListDeprecatedTemplatesResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListDeprecatedTemplatesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListDeprecatedTemplatesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListDeprecatedTemplatesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDiagnoseIndicesRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
    ):
        self.lang = lang

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['lang'] = self.lang
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('lang') is not None:
            self.lang = m.get('lang')
        return self


class ListDiagnoseIndicesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[str] = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class ListDiagnoseIndicesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListDiagnoseIndicesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListDiagnoseIndicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDiagnoseReportRequest(TeaModel):
    def __init__(
        self,
        detail: bool = None,
        end_time: int = None,
        lang: str = None,
        page: int = None,
        size: int = None,
        start_time: int = None,
        trigger: str = None,
    ):
        self.detail = detail
        self.end_time = end_time
        self.lang = lang
        self.page = page
        self.size = size
        self.start_time = start_time
        self.trigger = trigger

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.detail is not None:
            result['detail'] = self.detail
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.lang is not None:
            result['lang'] = self.lang
        if self.page is not None:
            result['page'] = self.page
        if self.size is not None:
            result['size'] = self.size
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.trigger is not None:
            result['trigger'] = self.trigger
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('detail') is not None:
            self.detail = m.get('detail')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('lang') is not None:
            self.lang = m.get('lang')
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('trigger') is not None:
            self.trigger = m.get('trigger')
        return self


class ListDiagnoseReportResponseBodyHeaders(TeaModel):
    def __init__(
        self,
        x_total_count: int = None,
    ):
        self.x_total_count = x_total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.x_total_count is not None:
            result['X-Total-Count'] = self.x_total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('X-Total-Count') is not None:
            self.x_total_count = m.get('X-Total-Count')
        return self


class ListDiagnoseReportResponseBodyResultDiagnoseItemsDetail(TeaModel):
    def __init__(
        self,
        desc: str = None,
        name: str = None,
        result: str = None,
        suggest: str = None,
        type: str = None,
    ):
        self.desc = desc
        self.name = name
        self.result = result
        self.suggest = suggest
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.desc is not None:
            result['desc'] = self.desc
        if self.name is not None:
            result['name'] = self.name
        if self.result is not None:
            result['result'] = self.result
        if self.suggest is not None:
            result['suggest'] = self.suggest
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('desc') is not None:
            self.desc = m.get('desc')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('result') is not None:
            self.result = m.get('result')
        if m.get('suggest') is not None:
            self.suggest = m.get('suggest')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ListDiagnoseReportResponseBodyResultDiagnoseItems(TeaModel):
    def __init__(
        self,
        detail: ListDiagnoseReportResponseBodyResultDiagnoseItemsDetail = None,
        health: str = None,
        item: str = None,
    ):
        self.detail = detail
        self.health = health
        self.item = item

    def validate(self):
        if self.detail:
            self.detail.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.detail is not None:
            result['detail'] = self.detail.to_map()
        if self.health is not None:
            result['health'] = self.health
        if self.item is not None:
            result['item'] = self.item
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('detail') is not None:
            temp_model = ListDiagnoseReportResponseBodyResultDiagnoseItemsDetail()
            self.detail = temp_model.from_map(m['detail'])
        if m.get('health') is not None:
            self.health = m.get('health')
        if m.get('item') is not None:
            self.item = m.get('item')
        return self


class ListDiagnoseReportResponseBodyResult(TeaModel):
    def __init__(
        self,
        create_time: int = None,
        diagnose_items: List[ListDiagnoseReportResponseBodyResultDiagnoseItems] = None,
        health: str = None,
        instance_id: str = None,
        report_id: str = None,
        state: str = None,
        trigger: str = None,
    ):
        self.create_time = create_time
        self.diagnose_items = diagnose_items
        self.health = health
        self.instance_id = instance_id
        self.report_id = report_id
        self.state = state
        self.trigger = trigger

    def validate(self):
        if self.diagnose_items:
            for k in self.diagnose_items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        result['diagnoseItems'] = []
        if self.diagnose_items is not None:
            for k in self.diagnose_items:
                result['diagnoseItems'].append(k.to_map() if k else None)
        if self.health is not None:
            result['health'] = self.health
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.report_id is not None:
            result['reportId'] = self.report_id
        if self.state is not None:
            result['state'] = self.state
        if self.trigger is not None:
            result['trigger'] = self.trigger
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        self.diagnose_items = []
        if m.get('diagnoseItems') is not None:
            for k in m.get('diagnoseItems'):
                temp_model = ListDiagnoseReportResponseBodyResultDiagnoseItems()
                self.diagnose_items.append(temp_model.from_map(k))
        if m.get('health') is not None:
            self.health = m.get('health')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('reportId') is not None:
            self.report_id = m.get('reportId')
        if m.get('state') is not None:
            self.state = m.get('state')
        if m.get('trigger') is not None:
            self.trigger = m.get('trigger')
        return self


class ListDiagnoseReportResponseBody(TeaModel):
    def __init__(
        self,
        headers: ListDiagnoseReportResponseBodyHeaders = None,
        request_id: str = None,
        result: List[ListDiagnoseReportResponseBodyResult] = None,
    ):
        self.headers = headers
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.headers:
            self.headers.validate()
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['Headers'] = self.headers.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Headers') is not None:
            temp_model = ListDiagnoseReportResponseBodyHeaders()
            self.headers = temp_model.from_map(m['Headers'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListDiagnoseReportResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListDiagnoseReportResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListDiagnoseReportResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListDiagnoseReportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDiagnoseReportIdsRequest(TeaModel):
    def __init__(
        self,
        end_time: int = None,
        lang: str = None,
        page: int = None,
        size: int = None,
        start_time: int = None,
        trigger: str = None,
    ):
        self.end_time = end_time
        self.lang = lang
        self.page = page
        self.size = size
        self.start_time = start_time
        self.trigger = trigger

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.lang is not None:
            result['lang'] = self.lang
        if self.page is not None:
            result['page'] = self.page
        if self.size is not None:
            result['size'] = self.size
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.trigger is not None:
            result['trigger'] = self.trigger
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('lang') is not None:
            self.lang = m.get('lang')
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('trigger') is not None:
            self.trigger = m.get('trigger')
        return self


class ListDiagnoseReportIdsResponseBodyHeaders(TeaModel):
    def __init__(
        self,
        x_total_count: int = None,
    ):
        self.x_total_count = x_total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.x_total_count is not None:
            result['X-Total-Count'] = self.x_total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('X-Total-Count') is not None:
            self.x_total_count = m.get('X-Total-Count')
        return self


class ListDiagnoseReportIdsResponseBody(TeaModel):
    def __init__(
        self,
        headers: ListDiagnoseReportIdsResponseBodyHeaders = None,
        request_id: str = None,
        result: List[str] = None,
    ):
        self.headers = headers
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.headers:
            self.headers.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['Headers'] = self.headers.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Headers') is not None:
            temp_model = ListDiagnoseReportIdsResponseBodyHeaders()
            self.headers = temp_model.from_map(m['Headers'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class ListDiagnoseReportIdsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListDiagnoseReportIdsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListDiagnoseReportIdsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDictInformationRequest(TeaModel):
    def __init__(
        self,
        analyzer_type: str = None,
        bucket_name: str = None,
        key: str = None,
    ):
        self.analyzer_type = analyzer_type
        self.bucket_name = bucket_name
        self.key = key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.analyzer_type is not None:
            result['analyzerType'] = self.analyzer_type
        if self.bucket_name is not None:
            result['bucketName'] = self.bucket_name
        if self.key is not None:
            result['key'] = self.key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('analyzerType') is not None:
            self.analyzer_type = m.get('analyzerType')
        if m.get('bucketName') is not None:
            self.bucket_name = m.get('bucketName')
        if m.get('key') is not None:
            self.key = m.get('key')
        return self


class ListDictInformationResponseBodyResultOssObject(TeaModel):
    def __init__(
        self,
        bucket_name: str = None,
        etag: str = None,
        key: str = None,
    ):
        self.bucket_name = bucket_name
        self.etag = etag
        self.key = key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket_name is not None:
            result['bucketName'] = self.bucket_name
        if self.etag is not None:
            result['etag'] = self.etag
        if self.key is not None:
            result['key'] = self.key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bucketName') is not None:
            self.bucket_name = m.get('bucketName')
        if m.get('etag') is not None:
            self.etag = m.get('etag')
        if m.get('key') is not None:
            self.key = m.get('key')
        return self


class ListDictInformationResponseBodyResult(TeaModel):
    def __init__(
        self,
        file_size: int = None,
        oss_object: ListDictInformationResponseBodyResultOssObject = None,
        type: str = None,
    ):
        self.file_size = file_size
        self.oss_object = oss_object
        self.type = type

    def validate(self):
        if self.oss_object:
            self.oss_object.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_size is not None:
            result['fileSize'] = self.file_size
        if self.oss_object is not None:
            result['ossObject'] = self.oss_object.to_map()
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fileSize') is not None:
            self.file_size = m.get('fileSize')
        if m.get('ossObject') is not None:
            temp_model = ListDictInformationResponseBodyResultOssObject()
            self.oss_object = temp_model.from_map(m['ossObject'])
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ListDictInformationResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: ListDictInformationResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = ListDictInformationResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class ListDictInformationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListDictInformationResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListDictInformationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDictsRequest(TeaModel):
    def __init__(
        self,
        analyzer_type: str = None,
        name: str = None,
    ):
        self.analyzer_type = analyzer_type
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.analyzer_type is not None:
            result['analyzerType'] = self.analyzer_type
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('analyzerType') is not None:
            self.analyzer_type = m.get('analyzerType')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class ListDictsResponseBodyHeaders(TeaModel):
    def __init__(
        self,
        x_total_count: int = None,
    ):
        self.x_total_count = x_total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.x_total_count is not None:
            result['X-Total-Count'] = self.x_total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('X-Total-Count') is not None:
            self.x_total_count = m.get('X-Total-Count')
        return self


class ListDictsResponseBodyResult(TeaModel):
    def __init__(
        self,
        download_url: str = None,
        file_size: int = None,
        name: str = None,
        source_type: str = None,
        type: str = None,
    ):
        self.download_url = download_url
        self.file_size = file_size
        self.name = name
        self.source_type = source_type
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.download_url is not None:
            result['downloadUrl'] = self.download_url
        if self.file_size is not None:
            result['fileSize'] = self.file_size
        if self.name is not None:
            result['name'] = self.name
        if self.source_type is not None:
            result['sourceType'] = self.source_type
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('downloadUrl') is not None:
            self.download_url = m.get('downloadUrl')
        if m.get('fileSize') is not None:
            self.file_size = m.get('fileSize')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ListDictsResponseBody(TeaModel):
    def __init__(
        self,
        headers: ListDictsResponseBodyHeaders = None,
        request_id: str = None,
        result: List[ListDictsResponseBodyResult] = None,
    ):
        self.headers = headers
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.headers:
            self.headers.validate()
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['Headers'] = self.headers.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Headers') is not None:
            temp_model = ListDictsResponseBodyHeaders()
            self.headers = temp_model.from_map(m['Headers'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListDictsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListDictsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListDictsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListDictsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListEcsInstancesRequest(TeaModel):
    def __init__(
        self,
        ecs_instance_ids: str = None,
        ecs_instance_name: str = None,
        page: int = None,
        size: int = None,
        tags: str = None,
        vpc_id: str = None,
    ):
        self.ecs_instance_ids = ecs_instance_ids
        self.ecs_instance_name = ecs_instance_name
        self.page = page
        self.size = size
        self.tags = tags
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ecs_instance_ids is not None:
            result['ecsInstanceIds'] = self.ecs_instance_ids
        if self.ecs_instance_name is not None:
            result['ecsInstanceName'] = self.ecs_instance_name
        if self.page is not None:
            result['page'] = self.page
        if self.size is not None:
            result['size'] = self.size
        if self.tags is not None:
            result['tags'] = self.tags
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ecsInstanceIds') is not None:
            self.ecs_instance_ids = m.get('ecsInstanceIds')
        if m.get('ecsInstanceName') is not None:
            self.ecs_instance_name = m.get('ecsInstanceName')
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('tags') is not None:
            self.tags = m.get('tags')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        return self


class ListEcsInstancesResponseBodyHeaders(TeaModel):
    def __init__(
        self,
        x_total_count: int = None,
    ):
        self.x_total_count = x_total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.x_total_count is not None:
            result['X-Total-Count'] = self.x_total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('X-Total-Count') is not None:
            self.x_total_count = m.get('X-Total-Count')
        return self


class ListEcsInstancesResponseBodyResultCollectorsConfigs(TeaModel):
    def __init__(
        self,
        content: str = None,
        file_name: str = None,
    ):
        self.content = content
        self.file_name = file_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ListEcsInstancesResponseBodyResultCollectorsExtendConfigsMachines(TeaModel):
    def __init__(
        self,
        agent_status: str = None,
        instance_id: str = None,
    ):
        self.agent_status = agent_status
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ListEcsInstancesResponseBodyResultCollectorsExtendConfigs(TeaModel):
    def __init__(
        self,
        config_type: str = None,
        enable_monitoring: bool = None,
        group_id: str = None,
        hosts: List[str] = None,
        instance_id: str = None,
        instance_type: str = None,
        machines: List[ListEcsInstancesResponseBodyResultCollectorsExtendConfigsMachines] = None,
        protocol: str = None,
        type: str = None,
        user_name: str = None,
    ):
        self.config_type = config_type
        self.enable_monitoring = enable_monitoring
        self.group_id = group_id
        self.hosts = hosts
        self.instance_id = instance_id
        self.instance_type = instance_type
        self.machines = machines
        self.protocol = protocol
        self.type = type
        self.user_name = user_name

    def validate(self):
        if self.machines:
            for k in self.machines:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            for k in self.machines:
                result['machines'].append(k.to_map() if k else None)
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
            for k in m.get('machines'):
                temp_model = ListEcsInstancesResponseBodyResultCollectorsExtendConfigsMachines()
                self.machines.append(temp_model.from_map(k))
        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('userName') is not None:
            self.user_name = m.get('userName')
        return self


class ListEcsInstancesResponseBodyResultCollectors(TeaModel):
    def __init__(
        self,
        collector_paths: List[str] = None,
        configs: List[ListEcsInstancesResponseBodyResultCollectorsConfigs] = None,
        dry_run: bool = None,
        extend_configs: List[ListEcsInstancesResponseBodyResultCollectorsExtendConfigs] = None,
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
        self.configs = configs
        self.dry_run = dry_run
        self.extend_configs = extend_configs
        self.gmt_created_time = gmt_created_time
        self.gmt_update_time = gmt_update_time
        self.name = name
        self.owner_id = owner_id
        self.res_id = res_id
        self.res_type = res_type
        self.res_version = res_version
        self.status = status
        self.vpc_id = vpc_id

    def validate(self):
        if self.configs:
            for k in self.configs:
                if k:
                    k.validate()
        if self.extend_configs:
            for k in self.extend_configs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.collector_paths is not None:
            result['collectorPaths'] = self.collector_paths
        result['configs'] = []
        if self.configs is not None:
            for k in self.configs:
                result['configs'].append(k.to_map() if k else None)
        if self.dry_run is not None:
            result['dryRun'] = self.dry_run
        result['extendConfigs'] = []
        if self.extend_configs is not None:
            for k in self.extend_configs:
                result['extendConfigs'].append(k.to_map() if k else None)
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
            for k in m.get('configs'):
                temp_model = ListEcsInstancesResponseBodyResultCollectorsConfigs()
                self.configs.append(temp_model.from_map(k))
        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')
        self.extend_configs = []
        if m.get('extendConfigs') is not None:
            for k in m.get('extendConfigs'):
                temp_model = ListEcsInstancesResponseBodyResultCollectorsExtendConfigs()
                self.extend_configs.append(temp_model.from_map(k))
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


class ListEcsInstancesResponseBodyResultIpAddress(TeaModel):
    def __init__(
        self,
        host: str = None,
        ip_type: str = None,
    ):
        self.host = host
        self.ip_type = ip_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ListEcsInstancesResponseBodyResult(TeaModel):
    def __init__(
        self,
        cloud_assistant_status: str = None,
        collectors: List[ListEcsInstancesResponseBodyResultCollectors] = None,
        ecs_instance_id: str = None,
        ecs_instance_name: str = None,
        ip_address: List[ListEcsInstancesResponseBodyResultIpAddress] = None,
        os_type: str = None,
        status: str = None,
        tags: str = None,
    ):
        self.cloud_assistant_status = cloud_assistant_status
        self.collectors = collectors
        self.ecs_instance_id = ecs_instance_id
        self.ecs_instance_name = ecs_instance_name
        self.ip_address = ip_address
        self.os_type = os_type
        self.status = status
        self.tags = tags

    def validate(self):
        if self.collectors:
            for k in self.collectors:
                if k:
                    k.validate()
        if self.ip_address:
            for k in self.ip_address:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cloud_assistant_status is not None:
            result['cloudAssistantStatus'] = self.cloud_assistant_status
        result['collectors'] = []
        if self.collectors is not None:
            for k in self.collectors:
                result['collectors'].append(k.to_map() if k else None)
        if self.ecs_instance_id is not None:
            result['ecsInstanceId'] = self.ecs_instance_id
        if self.ecs_instance_name is not None:
            result['ecsInstanceName'] = self.ecs_instance_name
        result['ipAddress'] = []
        if self.ip_address is not None:
            for k in self.ip_address:
                result['ipAddress'].append(k.to_map() if k else None)
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
            for k in m.get('collectors'):
                temp_model = ListEcsInstancesResponseBodyResultCollectors()
                self.collectors.append(temp_model.from_map(k))
        if m.get('ecsInstanceId') is not None:
            self.ecs_instance_id = m.get('ecsInstanceId')
        if m.get('ecsInstanceName') is not None:
            self.ecs_instance_name = m.get('ecsInstanceName')
        self.ip_address = []
        if m.get('ipAddress') is not None:
            for k in m.get('ipAddress'):
                temp_model = ListEcsInstancesResponseBodyResultIpAddress()
                self.ip_address.append(temp_model.from_map(k))
        if m.get('osType') is not None:
            self.os_type = m.get('osType')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('tags') is not None:
            self.tags = m.get('tags')
        return self


class ListEcsInstancesResponseBody(TeaModel):
    def __init__(
        self,
        headers: ListEcsInstancesResponseBodyHeaders = None,
        request_id: str = None,
        result: List[ListEcsInstancesResponseBodyResult] = None,
    ):
        self.headers = headers
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.headers:
            self.headers.validate()
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['Headers'] = self.headers.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Headers') is not None:
            temp_model = ListEcsInstancesResponseBodyHeaders()
            self.headers = temp_model.from_map(m['Headers'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListEcsInstancesResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListEcsInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListEcsInstancesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListEcsInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListExtendfilesResponseBodyResult(TeaModel):
    def __init__(
        self,
        file_path: str = None,
        file_size: int = None,
        name: str = None,
        source_type: str = None,
    ):
        self.file_path = file_path
        self.file_size = file_size
        self.name = name
        self.source_type = source_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_path is not None:
            result['filePath'] = self.file_path
        if self.file_size is not None:
            result['fileSize'] = self.file_size
        if self.name is not None:
            result['name'] = self.name
        if self.source_type is not None:
            result['sourceType'] = self.source_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('filePath') is not None:
            self.file_path = m.get('filePath')
        if m.get('fileSize') is not None:
            self.file_size = m.get('fileSize')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')
        return self


class ListExtendfilesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[ListExtendfilesResponseBodyResult] = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListExtendfilesResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListExtendfilesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListExtendfilesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListExtendfilesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListILMPoliciesRequest(TeaModel):
    def __init__(
        self,
        policy_name: str = None,
    ):
        self.policy_name = policy_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_name is not None:
            result['policyName'] = self.policy_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('policyName') is not None:
            self.policy_name = m.get('policyName')
        return self


class ListILMPoliciesResponseBodyResult(TeaModel):
    def __init__(
        self,
        name: str = None,
        phases: Dict[str, Any] = None,
    ):
        self.name = name
        self.phases = phases

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.phases is not None:
            result['phases'] = self.phases
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('phases') is not None:
            self.phases = m.get('phases')
        return self


class ListILMPoliciesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[ListILMPoliciesResponseBodyResult] = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListILMPoliciesResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListILMPoliciesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListILMPoliciesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListILMPoliciesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListIndexTemplatesRequest(TeaModel):
    def __init__(
        self,
        index_template: str = None,
        page: int = None,
        size: int = None,
    ):
        self.index_template = index_template
        self.page = page
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.index_template is not None:
            result['indexTemplate'] = self.index_template
        if self.page is not None:
            result['page'] = self.page
        if self.size is not None:
            result['size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('indexTemplate') is not None:
            self.index_template = m.get('indexTemplate')
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('size') is not None:
            self.size = m.get('size')
        return self


class ListIndexTemplatesResponseBodyResultTemplate(TeaModel):
    def __init__(
        self,
        aliases: str = None,
        mappings: str = None,
        settings: str = None,
    ):
        self.aliases = aliases
        self.mappings = mappings
        self.settings = settings

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aliases is not None:
            result['aliases'] = self.aliases
        if self.mappings is not None:
            result['mappings'] = self.mappings
        if self.settings is not None:
            result['settings'] = self.settings
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('aliases') is not None:
            self.aliases = m.get('aliases')
        if m.get('mappings') is not None:
            self.mappings = m.get('mappings')
        if m.get('settings') is not None:
            self.settings = m.get('settings')
        return self


class ListIndexTemplatesResponseBodyResult(TeaModel):
    def __init__(
        self,
        data_stream: bool = None,
        ilm_policy: str = None,
        index_patterns: List[str] = None,
        index_template: str = None,
        priority: int = None,
        template: ListIndexTemplatesResponseBodyResultTemplate = None,
    ):
        self.data_stream = data_stream
        self.ilm_policy = ilm_policy
        self.index_patterns = index_patterns
        self.index_template = index_template
        self.priority = priority
        self.template = template

    def validate(self):
        if self.template:
            self.template.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_stream is not None:
            result['dataStream'] = self.data_stream
        if self.ilm_policy is not None:
            result['ilmPolicy'] = self.ilm_policy
        if self.index_patterns is not None:
            result['indexPatterns'] = self.index_patterns
        if self.index_template is not None:
            result['indexTemplate'] = self.index_template
        if self.priority is not None:
            result['priority'] = self.priority
        if self.template is not None:
            result['template'] = self.template.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dataStream') is not None:
            self.data_stream = m.get('dataStream')
        if m.get('ilmPolicy') is not None:
            self.ilm_policy = m.get('ilmPolicy')
        if m.get('indexPatterns') is not None:
            self.index_patterns = m.get('indexPatterns')
        if m.get('indexTemplate') is not None:
            self.index_template = m.get('indexTemplate')
        if m.get('priority') is not None:
            self.priority = m.get('priority')
        if m.get('template') is not None:
            temp_model = ListIndexTemplatesResponseBodyResultTemplate()
            self.template = temp_model.from_map(m['template'])
        return self


class ListIndexTemplatesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[ListIndexTemplatesResponseBodyResult] = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListIndexTemplatesResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListIndexTemplatesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListIndexTemplatesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListIndexTemplatesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInstanceRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        es_version: str = None,
        instance_category: str = None,
        instance_id: str = None,
        page: int = None,
        payment_type: str = None,
        resource_group_id: str = None,
        size: int = None,
        tags: str = None,
        vpc_id: str = None,
        zone_id: str = None,
    ):
        self.description = description
        self.es_version = es_version
        self.instance_category = instance_category
        self.instance_id = instance_id
        self.page = page
        self.payment_type = payment_type
        self.resource_group_id = resource_group_id
        self.size = size
        self.tags = tags
        self.vpc_id = vpc_id
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.es_version is not None:
            result['esVersion'] = self.es_version
        if self.instance_category is not None:
            result['instanceCategory'] = self.instance_category
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.page is not None:
            result['page'] = self.page
        if self.payment_type is not None:
            result['paymentType'] = self.payment_type
        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id
        if self.size is not None:
            result['size'] = self.size
        if self.tags is not None:
            result['tags'] = self.tags
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        if self.zone_id is not None:
            result['zoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('esVersion') is not None:
            self.es_version = m.get('esVersion')
        if m.get('instanceCategory') is not None:
            self.instance_category = m.get('instanceCategory')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('paymentType') is not None:
            self.payment_type = m.get('paymentType')
        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('tags') is not None:
            self.tags = m.get('tags')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        if m.get('zoneId') is not None:
            self.zone_id = m.get('zoneId')
        return self


class ListInstanceResponseBodyHeaders(TeaModel):
    def __init__(
        self,
        x_total_count: int = None,
    ):
        self.x_total_count = x_total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.x_total_count is not None:
            result['X-Total-Count'] = self.x_total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('X-Total-Count') is not None:
            self.x_total_count = m.get('X-Total-Count')
        return self


class ListInstanceResponseBodyResultClientNodeConfiguration(TeaModel):
    def __init__(
        self,
        amount: int = None,
        disk: int = None,
        disk_type: str = None,
        spec: str = None,
    ):
        self.amount = amount
        self.disk = disk
        self.disk_type = disk_type
        self.spec = spec

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.amount is not None:
            result['amount'] = self.amount
        if self.disk is not None:
            result['disk'] = self.disk
        if self.disk_type is not None:
            result['diskType'] = self.disk_type
        if self.spec is not None:
            result['spec'] = self.spec
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('amount') is not None:
            self.amount = m.get('amount')
        if m.get('disk') is not None:
            self.disk = m.get('disk')
        if m.get('diskType') is not None:
            self.disk_type = m.get('diskType')
        if m.get('spec') is not None:
            self.spec = m.get('spec')
        return self


class ListInstanceResponseBodyResultElasticDataNodeConfiguration(TeaModel):
    def __init__(
        self,
        amount: int = None,
        disk: int = None,
        disk_encryption: bool = None,
        disk_type: str = None,
        spec: str = None,
    ):
        self.amount = amount
        self.disk = disk
        self.disk_encryption = disk_encryption
        self.disk_type = disk_type
        self.spec = spec

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.amount is not None:
            result['amount'] = self.amount
        if self.disk is not None:
            result['disk'] = self.disk
        if self.disk_encryption is not None:
            result['diskEncryption'] = self.disk_encryption
        if self.disk_type is not None:
            result['diskType'] = self.disk_type
        if self.spec is not None:
            result['spec'] = self.spec
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('amount') is not None:
            self.amount = m.get('amount')
        if m.get('disk') is not None:
            self.disk = m.get('disk')
        if m.get('diskEncryption') is not None:
            self.disk_encryption = m.get('diskEncryption')
        if m.get('diskType') is not None:
            self.disk_type = m.get('diskType')
        if m.get('spec') is not None:
            self.spec = m.get('spec')
        return self


class ListInstanceResponseBodyResultKibanaConfiguration(TeaModel):
    def __init__(
        self,
        amount: int = None,
        disk: int = None,
        disk_type: str = None,
        spec: str = None,
    ):
        self.amount = amount
        self.disk = disk
        self.disk_type = disk_type
        self.spec = spec

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.amount is not None:
            result['amount'] = self.amount
        if self.disk is not None:
            result['disk'] = self.disk
        if self.disk_type is not None:
            result['diskType'] = self.disk_type
        if self.spec is not None:
            result['spec'] = self.spec
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('amount') is not None:
            self.amount = m.get('amount')
        if m.get('disk') is not None:
            self.disk = m.get('disk')
        if m.get('diskType') is not None:
            self.disk_type = m.get('diskType')
        if m.get('spec') is not None:
            self.spec = m.get('spec')
        return self


class ListInstanceResponseBodyResultMasterConfiguration(TeaModel):
    def __init__(
        self,
        amount: int = None,
        disk: int = None,
        disk_type: str = None,
        spec: str = None,
    ):
        self.amount = amount
        self.disk = disk
        self.disk_type = disk_type
        self.spec = spec

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.amount is not None:
            result['amount'] = self.amount
        if self.disk is not None:
            result['disk'] = self.disk
        if self.disk_type is not None:
            result['diskType'] = self.disk_type
        if self.spec is not None:
            result['spec'] = self.spec
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('amount') is not None:
            self.amount = m.get('amount')
        if m.get('disk') is not None:
            self.disk = m.get('disk')
        if m.get('diskType') is not None:
            self.disk_type = m.get('diskType')
        if m.get('spec') is not None:
            self.spec = m.get('spec')
        return self


class ListInstanceResponseBodyResultNetworkConfig(TeaModel):
    def __init__(
        self,
        type: str = None,
        vpc_id: str = None,
        vs_area: str = None,
        vswitch_id: str = None,
    ):
        self.type = type
        self.vpc_id = vpc_id
        self.vs_area = vs_area
        self.vswitch_id = vswitch_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['type'] = self.type
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        if self.vs_area is not None:
            result['vsArea'] = self.vs_area
        if self.vswitch_id is not None:
            result['vswitchId'] = self.vswitch_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        if m.get('vsArea') is not None:
            self.vs_area = m.get('vsArea')
        if m.get('vswitchId') is not None:
            self.vswitch_id = m.get('vswitchId')
        return self


class ListInstanceResponseBodyResultNodeSpec(TeaModel):
    def __init__(
        self,
        disk: int = None,
        disk_encryption: bool = None,
        disk_type: str = None,
        spec: str = None,
    ):
        self.disk = disk
        self.disk_encryption = disk_encryption
        self.disk_type = disk_type
        self.spec = spec

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.disk is not None:
            result['disk'] = self.disk
        if self.disk_encryption is not None:
            result['diskEncryption'] = self.disk_encryption
        if self.disk_type is not None:
            result['diskType'] = self.disk_type
        if self.spec is not None:
            result['spec'] = self.spec
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('disk') is not None:
            self.disk = m.get('disk')
        if m.get('diskEncryption') is not None:
            self.disk_encryption = m.get('diskEncryption')
        if m.get('diskType') is not None:
            self.disk_type = m.get('diskType')
        if m.get('spec') is not None:
            self.spec = m.get('spec')
        return self


class ListInstanceResponseBodyResultTags(TeaModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        self.tag_key = tag_key
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_key is not None:
            result['tagKey'] = self.tag_key
        if self.tag_value is not None:
            result['tagValue'] = self.tag_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('tagKey') is not None:
            self.tag_key = m.get('tagKey')
        if m.get('tagValue') is not None:
            self.tag_value = m.get('tagValue')
        return self


class ListInstanceResponseBodyResult(TeaModel):
    def __init__(
        self,
        advanced_dedicate_master: bool = None,
        client_node_configuration: ListInstanceResponseBodyResultClientNodeConfiguration = None,
        created_at: str = None,
        dedicate_master: bool = None,
        description: str = None,
        elastic_data_node_configuration: ListInstanceResponseBodyResultElasticDataNodeConfiguration = None,
        es_version: str = None,
        extend_configs: List[Dict[str, Any]] = None,
        instance_id: str = None,
        is_new_deployment: str = None,
        kibana_configuration: ListInstanceResponseBodyResultKibanaConfiguration = None,
        master_configuration: ListInstanceResponseBodyResultMasterConfiguration = None,
        network_config: ListInstanceResponseBodyResultNetworkConfig = None,
        node_amount: int = None,
        node_spec: ListInstanceResponseBodyResultNodeSpec = None,
        payment_type: str = None,
        postpaid_service_status: str = None,
        resource_group_id: str = None,
        service_vpc: bool = None,
        status: str = None,
        tags: List[ListInstanceResponseBodyResultTags] = None,
        updated_at: str = None,
    ):
        self.advanced_dedicate_master = advanced_dedicate_master
        self.client_node_configuration = client_node_configuration
        self.created_at = created_at
        self.dedicate_master = dedicate_master
        self.description = description
        self.elastic_data_node_configuration = elastic_data_node_configuration
        self.es_version = es_version
        self.extend_configs = extend_configs
        self.instance_id = instance_id
        self.is_new_deployment = is_new_deployment
        self.kibana_configuration = kibana_configuration
        self.master_configuration = master_configuration
        self.network_config = network_config
        self.node_amount = node_amount
        self.node_spec = node_spec
        self.payment_type = payment_type
        self.postpaid_service_status = postpaid_service_status
        self.resource_group_id = resource_group_id
        self.service_vpc = service_vpc
        self.status = status
        self.tags = tags
        self.updated_at = updated_at

    def validate(self):
        if self.client_node_configuration:
            self.client_node_configuration.validate()
        if self.elastic_data_node_configuration:
            self.elastic_data_node_configuration.validate()
        if self.kibana_configuration:
            self.kibana_configuration.validate()
        if self.master_configuration:
            self.master_configuration.validate()
        if self.network_config:
            self.network_config.validate()
        if self.node_spec:
            self.node_spec.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.advanced_dedicate_master is not None:
            result['advancedDedicateMaster'] = self.advanced_dedicate_master
        if self.client_node_configuration is not None:
            result['clientNodeConfiguration'] = self.client_node_configuration.to_map()
        if self.created_at is not None:
            result['createdAt'] = self.created_at
        if self.dedicate_master is not None:
            result['dedicateMaster'] = self.dedicate_master
        if self.description is not None:
            result['description'] = self.description
        if self.elastic_data_node_configuration is not None:
            result['elasticDataNodeConfiguration'] = self.elastic_data_node_configuration.to_map()
        if self.es_version is not None:
            result['esVersion'] = self.es_version
        if self.extend_configs is not None:
            result['extendConfigs'] = self.extend_configs
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.is_new_deployment is not None:
            result['isNewDeployment'] = self.is_new_deployment
        if self.kibana_configuration is not None:
            result['kibanaConfiguration'] = self.kibana_configuration.to_map()
        if self.master_configuration is not None:
            result['masterConfiguration'] = self.master_configuration.to_map()
        if self.network_config is not None:
            result['networkConfig'] = self.network_config.to_map()
        if self.node_amount is not None:
            result['nodeAmount'] = self.node_amount
        if self.node_spec is not None:
            result['nodeSpec'] = self.node_spec.to_map()
        if self.payment_type is not None:
            result['paymentType'] = self.payment_type
        if self.postpaid_service_status is not None:
            result['postpaidServiceStatus'] = self.postpaid_service_status
        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id
        if self.service_vpc is not None:
            result['serviceVpc'] = self.service_vpc
        if self.status is not None:
            result['status'] = self.status
        result['tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['tags'].append(k.to_map() if k else None)
        if self.updated_at is not None:
            result['updatedAt'] = self.updated_at
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('advancedDedicateMaster') is not None:
            self.advanced_dedicate_master = m.get('advancedDedicateMaster')
        if m.get('clientNodeConfiguration') is not None:
            temp_model = ListInstanceResponseBodyResultClientNodeConfiguration()
            self.client_node_configuration = temp_model.from_map(m['clientNodeConfiguration'])
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')
        if m.get('dedicateMaster') is not None:
            self.dedicate_master = m.get('dedicateMaster')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('elasticDataNodeConfiguration') is not None:
            temp_model = ListInstanceResponseBodyResultElasticDataNodeConfiguration()
            self.elastic_data_node_configuration = temp_model.from_map(m['elasticDataNodeConfiguration'])
        if m.get('esVersion') is not None:
            self.es_version = m.get('esVersion')
        if m.get('extendConfigs') is not None:
            self.extend_configs = m.get('extendConfigs')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('isNewDeployment') is not None:
            self.is_new_deployment = m.get('isNewDeployment')
        if m.get('kibanaConfiguration') is not None:
            temp_model = ListInstanceResponseBodyResultKibanaConfiguration()
            self.kibana_configuration = temp_model.from_map(m['kibanaConfiguration'])
        if m.get('masterConfiguration') is not None:
            temp_model = ListInstanceResponseBodyResultMasterConfiguration()
            self.master_configuration = temp_model.from_map(m['masterConfiguration'])
        if m.get('networkConfig') is not None:
            temp_model = ListInstanceResponseBodyResultNetworkConfig()
            self.network_config = temp_model.from_map(m['networkConfig'])
        if m.get('nodeAmount') is not None:
            self.node_amount = m.get('nodeAmount')
        if m.get('nodeSpec') is not None:
            temp_model = ListInstanceResponseBodyResultNodeSpec()
            self.node_spec = temp_model.from_map(m['nodeSpec'])
        if m.get('paymentType') is not None:
            self.payment_type = m.get('paymentType')
        if m.get('postpaidServiceStatus') is not None:
            self.postpaid_service_status = m.get('postpaidServiceStatus')
        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')
        if m.get('serviceVpc') is not None:
            self.service_vpc = m.get('serviceVpc')
        if m.get('status') is not None:
            self.status = m.get('status')
        self.tags = []
        if m.get('tags') is not None:
            for k in m.get('tags'):
                temp_model = ListInstanceResponseBodyResultTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')
        return self


class ListInstanceResponseBody(TeaModel):
    def __init__(
        self,
        headers: ListInstanceResponseBodyHeaders = None,
        request_id: str = None,
        result: List[ListInstanceResponseBodyResult] = None,
    ):
        self.headers = headers
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.headers:
            self.headers.validate()
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['Headers'] = self.headers.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Headers') is not None:
            temp_model = ListInstanceResponseBodyHeaders()
            self.headers = temp_model.from_map(m['Headers'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListInstanceResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListInstanceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInstanceHistoryEventsRequestBody(TeaModel):
    def __init__(
        self,
        desc: bool = None,
        sort_field: str = None,
    ):
        self.desc = desc
        self.sort_field = sort_field

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.desc is not None:
            result['desc'] = self.desc
        if self.sort_field is not None:
            result['sortField'] = self.sort_field
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('desc') is not None:
            self.desc = m.get('desc')
        if m.get('sortField') is not None:
            self.sort_field = m.get('sortField')
        return self


class ListInstanceHistoryEventsRequest(TeaModel):
    def __init__(
        self,
        body: List[ListInstanceHistoryEventsRequestBody] = None,
        event_create_end_time: str = None,
        event_create_start_time: str = None,
        event_execute_end_time: str = None,
        event_execute_start_time: str = None,
        event_finash_end_time: str = None,
        event_finash_start_time: str = None,
        event_level: str = None,
        event_type: str = None,
        instance_id: str = None,
        node_ip: str = None,
    ):
        self.body = body
        self.event_create_end_time = event_create_end_time
        self.event_create_start_time = event_create_start_time
        self.event_execute_end_time = event_execute_end_time
        self.event_execute_start_time = event_execute_start_time
        self.event_finash_end_time = event_finash_end_time
        self.event_finash_start_time = event_finash_start_time
        self.event_level = event_level
        self.event_type = event_type
        self.instance_id = instance_id
        self.node_ip = node_ip

    def validate(self):
        if self.body:
            for k in self.body:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['body'] = []
        if self.body is not None:
            for k in self.body:
                result['body'].append(k.to_map() if k else None)
        if self.event_create_end_time is not None:
            result['eventCreateEndTime'] = self.event_create_end_time
        if self.event_create_start_time is not None:
            result['eventCreateStartTime'] = self.event_create_start_time
        if self.event_execute_end_time is not None:
            result['eventExecuteEndTime'] = self.event_execute_end_time
        if self.event_execute_start_time is not None:
            result['eventExecuteStartTime'] = self.event_execute_start_time
        if self.event_finash_end_time is not None:
            result['eventFinashEndTime'] = self.event_finash_end_time
        if self.event_finash_start_time is not None:
            result['eventFinashStartTime'] = self.event_finash_start_time
        if self.event_level is not None:
            result['eventLevel'] = self.event_level
        if self.event_type is not None:
            result['eventType'] = self.event_type
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.node_ip is not None:
            result['nodeIP'] = self.node_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.body = []
        if m.get('body') is not None:
            for k in m.get('body'):
                temp_model = ListInstanceHistoryEventsRequestBody()
                self.body.append(temp_model.from_map(k))
        if m.get('eventCreateEndTime') is not None:
            self.event_create_end_time = m.get('eventCreateEndTime')
        if m.get('eventCreateStartTime') is not None:
            self.event_create_start_time = m.get('eventCreateStartTime')
        if m.get('eventExecuteEndTime') is not None:
            self.event_execute_end_time = m.get('eventExecuteEndTime')
        if m.get('eventExecuteStartTime') is not None:
            self.event_execute_start_time = m.get('eventExecuteStartTime')
        if m.get('eventFinashEndTime') is not None:
            self.event_finash_end_time = m.get('eventFinashEndTime')
        if m.get('eventFinashStartTime') is not None:
            self.event_finash_start_time = m.get('eventFinashStartTime')
        if m.get('eventLevel') is not None:
            self.event_level = m.get('eventLevel')
        if m.get('eventType') is not None:
            self.event_type = m.get('eventType')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('nodeIP') is not None:
            self.node_ip = m.get('nodeIP')
        return self


class ListInstanceHistoryEventsResponseBodyHeaders(TeaModel):
    def __init__(
        self,
        x_total_count: int = None,
        x_total_failed: int = None,
        x_total_success: int = None,
    ):
        self.x_total_count = x_total_count
        self.x_total_failed = x_total_failed
        self.x_total_success = x_total_success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.x_total_count is not None:
            result['X-Total-Count'] = self.x_total_count
        if self.x_total_failed is not None:
            result['X-Total-Failed'] = self.x_total_failed
        if self.x_total_success is not None:
            result['X-Total-Success'] = self.x_total_success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('X-Total-Count') is not None:
            self.x_total_count = m.get('X-Total-Count')
        if m.get('X-Total-Failed') is not None:
            self.x_total_failed = m.get('X-Total-Failed')
        if m.get('X-Total-Success') is not None:
            self.x_total_success = m.get('X-Total-Success')
        return self


class ListInstanceHistoryEventsResponseBodyResult(TeaModel):
    def __init__(
        self,
        action_list: List[str] = None,
        event_create_time: str = None,
        event_cycle_status: str = None,
        event_execute_time: str = None,
        event_finash_time: str = None,
        event_level: str = None,
        event_type: str = None,
        instance_id: str = None,
        node_ip: str = None,
        region_id: str = None,
    ):
        self.action_list = action_list
        self.event_create_time = event_create_time
        self.event_cycle_status = event_cycle_status
        self.event_execute_time = event_execute_time
        self.event_finash_time = event_finash_time
        self.event_level = event_level
        self.event_type = event_type
        self.instance_id = instance_id
        self.node_ip = node_ip
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_list is not None:
            result['actionList'] = self.action_list
        if self.event_create_time is not None:
            result['eventCreateTime'] = self.event_create_time
        if self.event_cycle_status is not None:
            result['eventCycleStatus'] = self.event_cycle_status
        if self.event_execute_time is not None:
            result['eventExecuteTime'] = self.event_execute_time
        if self.event_finash_time is not None:
            result['eventFinashTime'] = self.event_finash_time
        if self.event_level is not None:
            result['eventLevel'] = self.event_level
        if self.event_type is not None:
            result['eventType'] = self.event_type
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.node_ip is not None:
            result['nodeIP'] = self.node_ip
        if self.region_id is not None:
            result['regionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('actionList') is not None:
            self.action_list = m.get('actionList')
        if m.get('eventCreateTime') is not None:
            self.event_create_time = m.get('eventCreateTime')
        if m.get('eventCycleStatus') is not None:
            self.event_cycle_status = m.get('eventCycleStatus')
        if m.get('eventExecuteTime') is not None:
            self.event_execute_time = m.get('eventExecuteTime')
        if m.get('eventFinashTime') is not None:
            self.event_finash_time = m.get('eventFinashTime')
        if m.get('eventLevel') is not None:
            self.event_level = m.get('eventLevel')
        if m.get('eventType') is not None:
            self.event_type = m.get('eventType')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('nodeIP') is not None:
            self.node_ip = m.get('nodeIP')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        return self


class ListInstanceHistoryEventsResponseBody(TeaModel):
    def __init__(
        self,
        headers: ListInstanceHistoryEventsResponseBodyHeaders = None,
        request_id: str = None,
        result: List[ListInstanceHistoryEventsResponseBodyResult] = None,
    ):
        self.headers = headers
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.headers:
            self.headers.validate()
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['Headers'] = self.headers.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Headers') is not None:
            temp_model = ListInstanceHistoryEventsResponseBodyHeaders()
            self.headers = temp_model.from_map(m['Headers'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListInstanceHistoryEventsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListInstanceHistoryEventsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListInstanceHistoryEventsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListInstanceHistoryEventsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInstanceIndicesRequest(TeaModel):
    def __init__(
        self,
        all: bool = None,
        is_managed: bool = None,
        is_openstore: bool = None,
        name: str = None,
        page: int = None,
        size: int = None,
    ):
        self.all = all
        self.is_managed = is_managed
        self.is_openstore = is_openstore
        self.name = name
        self.page = page
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all is not None:
            result['all'] = self.all
        if self.is_managed is not None:
            result['isManaged'] = self.is_managed
        if self.is_openstore is not None:
            result['isOpenstore'] = self.is_openstore
        if self.name is not None:
            result['name'] = self.name
        if self.page is not None:
            result['page'] = self.page
        if self.size is not None:
            result['size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('all') is not None:
            self.all = m.get('all')
        if m.get('isManaged') is not None:
            self.is_managed = m.get('isManaged')
        if m.get('isOpenstore') is not None:
            self.is_openstore = m.get('isOpenstore')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('size') is not None:
            self.size = m.get('size')
        return self


class ListInstanceIndicesResponseBodyHeaders(TeaModel):
    def __init__(
        self,
        x_managed_count: int = None,
        x_managed_storage_size: int = None,
        x_osscount: int = None,
        x_ossstorage_size: int = None,
    ):
        self.x_managed_count = x_managed_count
        self.x_managed_storage_size = x_managed_storage_size
        self.x_osscount = x_osscount
        self.x_ossstorage_size = x_ossstorage_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.x_managed_count is not None:
            result['X-Managed-Count'] = self.x_managed_count
        if self.x_managed_storage_size is not None:
            result['X-Managed-StorageSize'] = self.x_managed_storage_size
        if self.x_osscount is not None:
            result['X-OSS-Count'] = self.x_osscount
        if self.x_ossstorage_size is not None:
            result['X-OSS-StorageSize'] = self.x_ossstorage_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('X-Managed-Count') is not None:
            self.x_managed_count = m.get('X-Managed-Count')
        if m.get('X-Managed-StorageSize') is not None:
            self.x_managed_storage_size = m.get('X-Managed-StorageSize')
        if m.get('X-OSS-Count') is not None:
            self.x_osscount = m.get('X-OSS-Count')
        if m.get('X-OSS-StorageSize') is not None:
            self.x_ossstorage_size = m.get('X-OSS-StorageSize')
        return self


class ListInstanceIndicesResponseBodyResult(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        health: str = None,
        ilm_explain: str = None,
        is_managed: str = None,
        managed_status: str = None,
        name: str = None,
        phase: str = None,
        size: int = None,
    ):
        self.create_time = create_time
        self.health = health
        self.ilm_explain = ilm_explain
        self.is_managed = is_managed
        self.managed_status = managed_status
        self.name = name
        self.phase = phase
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.health is not None:
            result['health'] = self.health
        if self.ilm_explain is not None:
            result['ilmExplain'] = self.ilm_explain
        if self.is_managed is not None:
            result['isManaged'] = self.is_managed
        if self.managed_status is not None:
            result['managedStatus'] = self.managed_status
        if self.name is not None:
            result['name'] = self.name
        if self.phase is not None:
            result['phase'] = self.phase
        if self.size is not None:
            result['size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('health') is not None:
            self.health = m.get('health')
        if m.get('ilmExplain') is not None:
            self.ilm_explain = m.get('ilmExplain')
        if m.get('isManaged') is not None:
            self.is_managed = m.get('isManaged')
        if m.get('managedStatus') is not None:
            self.managed_status = m.get('managedStatus')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('phase') is not None:
            self.phase = m.get('phase')
        if m.get('size') is not None:
            self.size = m.get('size')
        return self


class ListInstanceIndicesResponseBody(TeaModel):
    def __init__(
        self,
        headers: ListInstanceIndicesResponseBodyHeaders = None,
        request_id: str = None,
        result: List[ListInstanceIndicesResponseBodyResult] = None,
    ):
        self.headers = headers
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.headers:
            self.headers.validate()
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['Headers'] = self.headers.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Headers') is not None:
            temp_model = ListInstanceIndicesResponseBodyHeaders()
            self.headers = temp_model.from_map(m['Headers'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListInstanceIndicesResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListInstanceIndicesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListInstanceIndicesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListInstanceIndicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListKibanaPluginsRequest(TeaModel):
    def __init__(
        self,
        page: str = None,
        size: int = None,
    ):
        self.page = page
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page is not None:
            result['page'] = self.page
        if self.size is not None:
            result['size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('size') is not None:
            self.size = m.get('size')
        return self


class ListKibanaPluginsResponseBodyHeaders(TeaModel):
    def __init__(
        self,
        x_total_count: int = None,
    ):
        self.x_total_count = x_total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.x_total_count is not None:
            result['X-Total-Count'] = self.x_total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('X-Total-Count') is not None:
            self.x_total_count = m.get('X-Total-Count')
        return self


class ListKibanaPluginsResponseBodyResult(TeaModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        source: str = None,
        specification_url: str = None,
        state: str = None,
    ):
        self.description = description
        self.name = name
        self.source = source
        self.specification_url = specification_url
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.name is not None:
            result['name'] = self.name
        if self.source is not None:
            result['source'] = self.source
        if self.specification_url is not None:
            result['specificationUrl'] = self.specification_url
        if self.state is not None:
            result['state'] = self.state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('source') is not None:
            self.source = m.get('source')
        if m.get('specificationUrl') is not None:
            self.specification_url = m.get('specificationUrl')
        if m.get('state') is not None:
            self.state = m.get('state')
        return self


class ListKibanaPluginsResponseBody(TeaModel):
    def __init__(
        self,
        headers: ListKibanaPluginsResponseBodyHeaders = None,
        request_id: str = None,
        result: List[ListKibanaPluginsResponseBodyResult] = None,
    ):
        self.headers = headers
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.headers:
            self.headers.validate()
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['Headers'] = self.headers.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Headers') is not None:
            temp_model = ListKibanaPluginsResponseBodyHeaders()
            self.headers = temp_model.from_map(m['Headers'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListKibanaPluginsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListKibanaPluginsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListKibanaPluginsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListKibanaPluginsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListLogstashRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        instance_id: str = None,
        owner_id: str = None,
        page: int = None,
        resource_group_id: str = None,
        size: int = None,
        version: str = None,
    ):
        self.description = description
        self.instance_id = instance_id
        self.owner_id = owner_id
        self.page = page
        self.resource_group_id = resource_group_id
        self.size = size
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.owner_id is not None:
            result['ownerId'] = self.owner_id
        if self.page is not None:
            result['page'] = self.page
        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id
        if self.size is not None:
            result['size'] = self.size
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('ownerId') is not None:
            self.owner_id = m.get('ownerId')
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class ListLogstashResponseBodyHeaders(TeaModel):
    def __init__(
        self,
        x_total_count: int = None,
    ):
        self.x_total_count = x_total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.x_total_count is not None:
            result['X-Total-Count'] = self.x_total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('X-Total-Count') is not None:
            self.x_total_count = m.get('X-Total-Count')
        return self


class ListLogstashResponseBody(TeaModel):
    def __init__(
        self,
        headers: ListLogstashResponseBodyHeaders = None,
        request_id: str = None,
        result: List[Logstash] = None,
    ):
        self.headers = headers
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.headers:
            self.headers.validate()
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['Headers'] = self.headers.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Headers') is not None:
            temp_model = ListLogstashResponseBodyHeaders()
            self.headers = temp_model.from_map(m['Headers'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = Logstash()
                self.result.append(temp_model.from_map(k))
        return self


class ListLogstashResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListLogstashResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListLogstashResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListLogstashLogRequest(TeaModel):
    def __init__(
        self,
        begin_time: int = None,
        end_time: int = None,
        page: int = None,
        query: str = None,
        size: int = None,
        type: str = None,
    ):
        self.begin_time = begin_time
        self.end_time = end_time
        self.page = page
        self.query = query
        self.size = size
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_time is not None:
            result['beginTime'] = self.begin_time
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.page is not None:
            result['page'] = self.page
        if self.query is not None:
            result['query'] = self.query
        if self.size is not None:
            result['size'] = self.size
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('beginTime') is not None:
            self.begin_time = m.get('beginTime')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('query') is not None:
            self.query = m.get('query')
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ListLogstashLogResponseBodyResult(TeaModel):
    def __init__(
        self,
        content: str = None,
        host: str = None,
        instance_id: str = None,
        level: str = None,
        timestamp: int = None,
    ):
        self.content = content
        self.host = host
        self.instance_id = instance_id
        self.level = level
        self.timestamp = timestamp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['content'] = self.content
        if self.host is not None:
            result['host'] = self.host
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.level is not None:
            result['level'] = self.level
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('host') is not None:
            self.host = m.get('host')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('level') is not None:
            self.level = m.get('level')
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')
        return self


class ListLogstashLogResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[ListLogstashLogResponseBodyResult] = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListLogstashLogResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListLogstashLogResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListLogstashLogResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListLogstashLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListLogstashPluginsRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        page: int = None,
        size: int = None,
        source: str = None,
    ):
        self.name = name
        self.page = page
        self.size = size
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.page is not None:
            result['page'] = self.page
        if self.size is not None:
            result['size'] = self.size
        if self.source is not None:
            result['source'] = self.source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('source') is not None:
            self.source = m.get('source')
        return self


class ListLogstashPluginsResponseBodyResult(TeaModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        source: str = None,
        specification_url: str = None,
        state: str = None,
    ):
        self.description = description
        self.name = name
        self.source = source
        self.specification_url = specification_url
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.name is not None:
            result['name'] = self.name
        if self.source is not None:
            result['source'] = self.source
        if self.specification_url is not None:
            result['specificationUrl'] = self.specification_url
        if self.state is not None:
            result['state'] = self.state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('source') is not None:
            self.source = m.get('source')
        if m.get('specificationUrl') is not None:
            self.specification_url = m.get('specificationUrl')
        if m.get('state') is not None:
            self.state = m.get('state')
        return self


class ListLogstashPluginsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[ListLogstashPluginsResponseBodyResult] = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListLogstashPluginsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListLogstashPluginsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListLogstashPluginsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListLogstashPluginsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListNodesRequest(TeaModel):
    def __init__(
        self,
        ecs_instance_ids: str = None,
        ecs_instance_name: str = None,
        page: int = None,
        size: int = None,
        tags: str = None,
    ):
        self.ecs_instance_ids = ecs_instance_ids
        self.ecs_instance_name = ecs_instance_name
        self.page = page
        self.size = size
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ecs_instance_ids is not None:
            result['ecsInstanceIds'] = self.ecs_instance_ids
        if self.ecs_instance_name is not None:
            result['ecsInstanceName'] = self.ecs_instance_name
        if self.page is not None:
            result['page'] = self.page
        if self.size is not None:
            result['size'] = self.size
        if self.tags is not None:
            result['tags'] = self.tags
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ecsInstanceIds') is not None:
            self.ecs_instance_ids = m.get('ecsInstanceIds')
        if m.get('ecsInstanceName') is not None:
            self.ecs_instance_name = m.get('ecsInstanceName')
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('tags') is not None:
            self.tags = m.get('tags')
        return self


class ListNodesResponseBodyHeaders(TeaModel):
    def __init__(
        self,
        x_total_count: int = None,
    ):
        self.x_total_count = x_total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.x_total_count is not None:
            result['X-Total-Count'] = self.x_total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('X-Total-Count') is not None:
            self.x_total_count = m.get('X-Total-Count')
        return self


class ListNodesResponseBodyResultIpAddress(TeaModel):
    def __init__(
        self,
        host: str = None,
        ip_type: str = None,
    ):
        self.host = host
        self.ip_type = ip_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ListNodesResponseBodyResultTags(TeaModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        self.tag_key = tag_key
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_key is not None:
            result['tagKey'] = self.tag_key
        if self.tag_value is not None:
            result['tagValue'] = self.tag_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('tagKey') is not None:
            self.tag_key = m.get('tagKey')
        if m.get('tagValue') is not None:
            self.tag_value = m.get('tagValue')
        return self


class ListNodesResponseBodyResult(TeaModel):
    def __init__(
        self,
        agent_status: str = None,
        cloud_assistant_status: str = None,
        ecs_instance_id: str = None,
        ecs_instance_name: str = None,
        ip_address: List[ListNodesResponseBodyResultIpAddress] = None,
        os_type: str = None,
        status: str = None,
        tags: List[ListNodesResponseBodyResultTags] = None,
    ):
        self.agent_status = agent_status
        self.cloud_assistant_status = cloud_assistant_status
        self.ecs_instance_id = ecs_instance_id
        self.ecs_instance_name = ecs_instance_name
        self.ip_address = ip_address
        self.os_type = os_type
        self.status = status
        self.tags = tags

    def validate(self):
        if self.ip_address:
            for k in self.ip_address:
                if k:
                    k.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_status is not None:
            result['agentStatus'] = self.agent_status
        if self.cloud_assistant_status is not None:
            result['cloudAssistantStatus'] = self.cloud_assistant_status
        if self.ecs_instance_id is not None:
            result['ecsInstanceId'] = self.ecs_instance_id
        if self.ecs_instance_name is not None:
            result['ecsInstanceName'] = self.ecs_instance_name
        result['ipAddress'] = []
        if self.ip_address is not None:
            for k in self.ip_address:
                result['ipAddress'].append(k.to_map() if k else None)
        if self.os_type is not None:
            result['osType'] = self.os_type
        if self.status is not None:
            result['status'] = self.status
        result['tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentStatus') is not None:
            self.agent_status = m.get('agentStatus')
        if m.get('cloudAssistantStatus') is not None:
            self.cloud_assistant_status = m.get('cloudAssistantStatus')
        if m.get('ecsInstanceId') is not None:
            self.ecs_instance_id = m.get('ecsInstanceId')
        if m.get('ecsInstanceName') is not None:
            self.ecs_instance_name = m.get('ecsInstanceName')
        self.ip_address = []
        if m.get('ipAddress') is not None:
            for k in m.get('ipAddress'):
                temp_model = ListNodesResponseBodyResultIpAddress()
                self.ip_address.append(temp_model.from_map(k))
        if m.get('osType') is not None:
            self.os_type = m.get('osType')
        if m.get('status') is not None:
            self.status = m.get('status')
        self.tags = []
        if m.get('tags') is not None:
            for k in m.get('tags'):
                temp_model = ListNodesResponseBodyResultTags()
                self.tags.append(temp_model.from_map(k))
        return self


class ListNodesResponseBody(TeaModel):
    def __init__(
        self,
        headers: ListNodesResponseBodyHeaders = None,
        request_id: str = None,
        result: List[ListNodesResponseBodyResult] = None,
    ):
        self.headers = headers
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.headers:
            self.headers.validate()
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['Headers'] = self.headers.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Headers') is not None:
            temp_model = ListNodesResponseBodyHeaders()
            self.headers = temp_model.from_map(m['Headers'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListNodesResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListNodesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListNodesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListNodesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPipelineRequest(TeaModel):
    def __init__(
        self,
        page: int = None,
        pipeline_id: str = None,
        size: int = None,
    ):
        self.page = page
        self.pipeline_id = pipeline_id
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page is not None:
            result['page'] = self.page
        if self.pipeline_id is not None:
            result['pipelineId'] = self.pipeline_id
        if self.size is not None:
            result['size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('pipelineId') is not None:
            self.pipeline_id = m.get('pipelineId')
        if m.get('size') is not None:
            self.size = m.get('size')
        return self


class ListPipelineResponseBodyHeaders(TeaModel):
    def __init__(
        self,
        x_total_count: int = None,
    ):
        self.x_total_count = x_total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.x_total_count is not None:
            result['X-Total-Count'] = self.x_total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('X-Total-Count') is not None:
            self.x_total_count = m.get('X-Total-Count')
        return self


class ListPipelineResponseBodyResult(TeaModel):
    def __init__(
        self,
        gmt_created_time: str = None,
        gmt_update_time: str = None,
        pipeline_id: str = None,
        pipeline_status: str = None,
    ):
        self.gmt_created_time = gmt_created_time
        self.gmt_update_time = gmt_update_time
        self.pipeline_id = pipeline_id
        self.pipeline_status = pipeline_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_created_time is not None:
            result['gmtCreatedTime'] = self.gmt_created_time
        if self.gmt_update_time is not None:
            result['gmtUpdateTime'] = self.gmt_update_time
        if self.pipeline_id is not None:
            result['pipelineId'] = self.pipeline_id
        if self.pipeline_status is not None:
            result['pipelineStatus'] = self.pipeline_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('gmtCreatedTime') is not None:
            self.gmt_created_time = m.get('gmtCreatedTime')
        if m.get('gmtUpdateTime') is not None:
            self.gmt_update_time = m.get('gmtUpdateTime')
        if m.get('pipelineId') is not None:
            self.pipeline_id = m.get('pipelineId')
        if m.get('pipelineStatus') is not None:
            self.pipeline_status = m.get('pipelineStatus')
        return self


class ListPipelineResponseBody(TeaModel):
    def __init__(
        self,
        headers: ListPipelineResponseBodyHeaders = None,
        request_id: str = None,
        result: List[ListPipelineResponseBodyResult] = None,
    ):
        self.headers = headers
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.headers:
            self.headers.validate()
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['Headers'] = self.headers.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Headers') is not None:
            temp_model = ListPipelineResponseBodyHeaders()
            self.headers = temp_model.from_map(m['Headers'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListPipelineResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListPipelineResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListPipelineResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListPipelineResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPipelineIdsResponseBodyResult(TeaModel):
    def __init__(
        self,
        available: bool = None,
        code: str = None,
        message: str = None,
        pipeline_id: str = None,
    ):
        self.available = available
        self.code = code
        self.message = message
        self.pipeline_id = pipeline_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.available is not None:
            result['available'] = self.available
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.pipeline_id is not None:
            result['pipelineId'] = self.pipeline_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('available') is not None:
            self.available = m.get('available')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('pipelineId') is not None:
            self.pipeline_id = m.get('pipelineId')
        return self


class ListPipelineIdsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[ListPipelineIdsResponseBodyResult] = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListPipelineIdsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListPipelineIdsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListPipelineIdsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListPipelineIdsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPluginsRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        page: str = None,
        size: int = None,
        source: str = None,
    ):
        self.name = name
        self.page = page
        self.size = size
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.page is not None:
            result['page'] = self.page
        if self.size is not None:
            result['size'] = self.size
        if self.source is not None:
            result['source'] = self.source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('source') is not None:
            self.source = m.get('source')
        return self


class ListPluginsResponseBodyHeaders(TeaModel):
    def __init__(
        self,
        x_total_count: int = None,
    ):
        self.x_total_count = x_total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.x_total_count is not None:
            result['X-Total-Count'] = self.x_total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('X-Total-Count') is not None:
            self.x_total_count = m.get('X-Total-Count')
        return self


class ListPluginsResponseBodyResult(TeaModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        source: str = None,
        specification_url: str = None,
        state: str = None,
    ):
        self.description = description
        self.name = name
        self.source = source
        self.specification_url = specification_url
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.name is not None:
            result['name'] = self.name
        if self.source is not None:
            result['source'] = self.source
        if self.specification_url is not None:
            result['specificationUrl'] = self.specification_url
        if self.state is not None:
            result['state'] = self.state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('source') is not None:
            self.source = m.get('source')
        if m.get('specificationUrl') is not None:
            self.specification_url = m.get('specificationUrl')
        if m.get('state') is not None:
            self.state = m.get('state')
        return self


class ListPluginsResponseBody(TeaModel):
    def __init__(
        self,
        headers: ListPluginsResponseBodyHeaders = None,
        request_id: str = None,
        result: List[ListPluginsResponseBodyResult] = None,
    ):
        self.headers = headers
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.headers:
            self.headers.validate()
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['Headers'] = self.headers.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Headers') is not None:
            temp_model = ListPluginsResponseBodyHeaders()
            self.headers = temp_model.from_map(m['Headers'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListPluginsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListPluginsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListPluginsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListPluginsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSearchLogRequest(TeaModel):
    def __init__(
        self,
        begin_time: int = None,
        end_time: int = None,
        page: int = None,
        query: str = None,
        size: int = None,
        type: str = None,
    ):
        self.begin_time = begin_time
        self.end_time = end_time
        self.page = page
        self.query = query
        self.size = size
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_time is not None:
            result['beginTime'] = self.begin_time
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.page is not None:
            result['page'] = self.page
        if self.query is not None:
            result['query'] = self.query
        if self.size is not None:
            result['size'] = self.size
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('beginTime') is not None:
            self.begin_time = m.get('beginTime')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('query') is not None:
            self.query = m.get('query')
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ListSearchLogResponseBodyHeaders(TeaModel):
    def __init__(
        self,
        x_total_count: int = None,
    ):
        self.x_total_count = x_total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.x_total_count is not None:
            result['X-Total-Count'] = self.x_total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('X-Total-Count') is not None:
            self.x_total_count = m.get('X-Total-Count')
        return self


class ListSearchLogResponseBodyResult(TeaModel):
    def __init__(
        self,
        content: str = None,
        content_collection: Dict[str, Any] = None,
        host: str = None,
        instance_id: str = None,
        level: str = None,
        timestamp: int = None,
    ):
        self.content = content
        self.content_collection = content_collection
        self.host = host
        self.instance_id = instance_id
        self.level = level
        self.timestamp = timestamp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['content'] = self.content
        if self.content_collection is not None:
            result['contentCollection'] = self.content_collection
        if self.host is not None:
            result['host'] = self.host
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.level is not None:
            result['level'] = self.level
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('contentCollection') is not None:
            self.content_collection = m.get('contentCollection')
        if m.get('host') is not None:
            self.host = m.get('host')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('level') is not None:
            self.level = m.get('level')
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')
        return self


class ListSearchLogResponseBody(TeaModel):
    def __init__(
        self,
        headers: ListSearchLogResponseBodyHeaders = None,
        request_id: str = None,
        result: List[ListSearchLogResponseBodyResult] = None,
    ):
        self.headers = headers
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.headers:
            self.headers.validate()
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['Headers'] = self.headers.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Headers') is not None:
            temp_model = ListSearchLogResponseBodyHeaders()
            self.headers = temp_model.from_map(m['Headers'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListSearchLogResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListSearchLogResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListSearchLogResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListSearchLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListShardRecoveriesRequest(TeaModel):
    def __init__(
        self,
        active_only: bool = None,
    ):
        self.active_only = active_only

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active_only is not None:
            result['activeOnly'] = self.active_only
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('activeOnly') is not None:
            self.active_only = m.get('activeOnly')
        return self


class ListShardRecoveriesResponseBodyResult(TeaModel):
    def __init__(
        self,
        bytes_percent: str = None,
        bytes_total: int = None,
        files_percent: str = None,
        files_total: int = None,
        index: str = None,
        source_host: str = None,
        source_node: str = None,
        stage: str = None,
        target_host: str = None,
        target_node: str = None,
        translog_ops: int = None,
        translog_ops_percent: str = None,
    ):
        self.bytes_percent = bytes_percent
        self.bytes_total = bytes_total
        self.files_percent = files_percent
        self.files_total = files_total
        self.index = index
        self.source_host = source_host
        self.source_node = source_node
        self.stage = stage
        self.target_host = target_host
        self.target_node = target_node
        self.translog_ops = translog_ops
        self.translog_ops_percent = translog_ops_percent

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bytes_percent is not None:
            result['bytesPercent'] = self.bytes_percent
        if self.bytes_total is not None:
            result['bytesTotal'] = self.bytes_total
        if self.files_percent is not None:
            result['filesPercent'] = self.files_percent
        if self.files_total is not None:
            result['filesTotal'] = self.files_total
        if self.index is not None:
            result['index'] = self.index
        if self.source_host is not None:
            result['sourceHost'] = self.source_host
        if self.source_node is not None:
            result['sourceNode'] = self.source_node
        if self.stage is not None:
            result['stage'] = self.stage
        if self.target_host is not None:
            result['targetHost'] = self.target_host
        if self.target_node is not None:
            result['targetNode'] = self.target_node
        if self.translog_ops is not None:
            result['translogOps'] = self.translog_ops
        if self.translog_ops_percent is not None:
            result['translogOpsPercent'] = self.translog_ops_percent
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bytesPercent') is not None:
            self.bytes_percent = m.get('bytesPercent')
        if m.get('bytesTotal') is not None:
            self.bytes_total = m.get('bytesTotal')
        if m.get('filesPercent') is not None:
            self.files_percent = m.get('filesPercent')
        if m.get('filesTotal') is not None:
            self.files_total = m.get('filesTotal')
        if m.get('index') is not None:
            self.index = m.get('index')
        if m.get('sourceHost') is not None:
            self.source_host = m.get('sourceHost')
        if m.get('sourceNode') is not None:
            self.source_node = m.get('sourceNode')
        if m.get('stage') is not None:
            self.stage = m.get('stage')
        if m.get('targetHost') is not None:
            self.target_host = m.get('targetHost')
        if m.get('targetNode') is not None:
            self.target_node = m.get('targetNode')
        if m.get('translogOps') is not None:
            self.translog_ops = m.get('translogOps')
        if m.get('translogOpsPercent') is not None:
            self.translog_ops_percent = m.get('translogOpsPercent')
        return self


class ListShardRecoveriesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[ListShardRecoveriesResponseBodyResult] = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListShardRecoveriesResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListShardRecoveriesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListShardRecoveriesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListShardRecoveriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSnapshotReposByInstanceIdResponseBodyResult(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        repo_path: str = None,
        snap_warehouse: str = None,
        status: str = None,
    ):
        self.instance_id = instance_id
        self.repo_path = repo_path
        self.snap_warehouse = snap_warehouse
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.repo_path is not None:
            result['repoPath'] = self.repo_path
        if self.snap_warehouse is not None:
            result['snapWarehouse'] = self.snap_warehouse
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('repoPath') is not None:
            self.repo_path = m.get('repoPath')
        if m.get('snapWarehouse') is not None:
            self.snap_warehouse = m.get('snapWarehouse')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class ListSnapshotReposByInstanceIdResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[ListSnapshotReposByInstanceIdResponseBodyResult] = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListSnapshotReposByInstanceIdResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListSnapshotReposByInstanceIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListSnapshotReposByInstanceIdResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListSnapshotReposByInstanceIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagResourcesRequest(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        page: int = None,
        resource_ids: str = None,
        resource_type: str = None,
        size: int = None,
        tags: str = None,
    ):
        self.next_token = next_token
        self.page = page
        self.resource_ids = resource_ids
        self.resource_type = resource_type
        self.size = size
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.page is not None:
            result['Page'] = self.page
        if self.resource_ids is not None:
            result['ResourceIds'] = self.resource_ids
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.size is not None:
            result['Size'] = self.size
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('ResourceIds') is not None:
            self.resource_ids = m.get('ResourceIds')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        return self


class ListTagResourcesResponseBodyHeaders(TeaModel):
    def __init__(
        self,
        x_total_count: int = None,
    ):
        self.x_total_count = x_total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.x_total_count is not None:
            result['X-Total-Count'] = self.x_total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('X-Total-Count') is not None:
            self.x_total_count = m.get('X-Total-Count')
        return self


class ListTagResourcesResponseBodyTagResourcesTagResource(TeaModel):
    def __init__(
        self,
        resource_id: str = None,
        resource_type: str = None,
        tag_key: str = None,
        tag_value: str = None,
    ):
        self.resource_id = resource_id
        self.resource_type = resource_type
        self.tag_key = tag_key
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        return self


class ListTagResourcesResponseBodyTagResources(TeaModel):
    def __init__(
        self,
        tag_resource: List[ListTagResourcesResponseBodyTagResourcesTagResource] = None,
    ):
        self.tag_resource = tag_resource

    def validate(self):
        if self.tag_resource:
            for k in self.tag_resource:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TagResource'] = []
        if self.tag_resource is not None:
            for k in self.tag_resource:
                result['TagResource'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag_resource = []
        if m.get('TagResource') is not None:
            for k in m.get('TagResource'):
                temp_model = ListTagResourcesResponseBodyTagResourcesTagResource()
                self.tag_resource.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        headers: ListTagResourcesResponseBodyHeaders = None,
        page_size: int = None,
        request_id: str = None,
        tag_resources: ListTagResourcesResponseBodyTagResources = None,
    ):
        self.headers = headers
        self.page_size = page_size
        self.request_id = request_id
        self.tag_resources = tag_resources

    def validate(self):
        if self.headers:
            self.headers.validate()
        if self.tag_resources:
            self.tag_resources.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['Headers'] = self.headers.to_map()
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tag_resources is not None:
            result['TagResources'] = self.tag_resources.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Headers') is not None:
            temp_model = ListTagResourcesResponseBodyHeaders()
            self.headers = temp_model.from_map(m['Headers'])
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TagResources') is not None:
            temp_model = ListTagResourcesResponseBodyTagResources()
            self.tag_resources = temp_model.from_map(m['TagResources'])
        return self


class ListTagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListTagResourcesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListTagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagsRequest(TeaModel):
    def __init__(
        self,
        page_size: int = None,
        resource_type: str = None,
    ):
        self.page_size = page_size
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        return self


class ListTagsResponseBodyResult(TeaModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        self.tag_key = tag_key
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        return self


class ListTagsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[ListTagsResponseBodyResult] = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListTagsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListTagsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListTagsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListTagsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListVpcEndpointsRequest(TeaModel):
    def __init__(
        self,
        page: int = None,
        size: int = None,
    ):
        self.page = page
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page is not None:
            result['page'] = self.page
        if self.size is not None:
            result['size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('size') is not None:
            self.size = m.get('size')
        return self


class ListVpcEndpointsResponseBodyResult(TeaModel):
    def __init__(
        self,
        connection_status: str = None,
        create_time: str = None,
        endpoint_business_status: str = None,
        endpoint_domain: str = None,
        endpoint_id: str = None,
        endpoint_name: str = None,
        endpoint_status: str = None,
        service_id: str = None,
        service_name: str = None,
    ):
        self.connection_status = connection_status
        self.create_time = create_time
        self.endpoint_business_status = endpoint_business_status
        self.endpoint_domain = endpoint_domain
        self.endpoint_id = endpoint_id
        self.endpoint_name = endpoint_name
        self.endpoint_status = endpoint_status
        self.service_id = service_id
        self.service_name = service_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connection_status is not None:
            result['connectionStatus'] = self.connection_status
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.endpoint_business_status is not None:
            result['endpointBusinessStatus'] = self.endpoint_business_status
        if self.endpoint_domain is not None:
            result['endpointDomain'] = self.endpoint_domain
        if self.endpoint_id is not None:
            result['endpointId'] = self.endpoint_id
        if self.endpoint_name is not None:
            result['endpointName'] = self.endpoint_name
        if self.endpoint_status is not None:
            result['endpointStatus'] = self.endpoint_status
        if self.service_id is not None:
            result['serviceId'] = self.service_id
        if self.service_name is not None:
            result['serviceName'] = self.service_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('connectionStatus') is not None:
            self.connection_status = m.get('connectionStatus')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('endpointBusinessStatus') is not None:
            self.endpoint_business_status = m.get('endpointBusinessStatus')
        if m.get('endpointDomain') is not None:
            self.endpoint_domain = m.get('endpointDomain')
        if m.get('endpointId') is not None:
            self.endpoint_id = m.get('endpointId')
        if m.get('endpointName') is not None:
            self.endpoint_name = m.get('endpointName')
        if m.get('endpointStatus') is not None:
            self.endpoint_status = m.get('endpointStatus')
        if m.get('serviceId') is not None:
            self.service_id = m.get('serviceId')
        if m.get('serviceName') is not None:
            self.service_name = m.get('serviceName')
        return self


class ListVpcEndpointsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[ListVpcEndpointsResponseBodyResult] = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListVpcEndpointsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListVpcEndpointsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListVpcEndpointsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListVpcEndpointsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class MigrateToOtherZoneRequest(TeaModel):
    def __init__(
        self,
        dry_run: bool = None,
    ):
        self.dry_run = dry_run

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dry_run is not None:
            result['dryRun'] = self.dry_run
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')
        return self


class MigrateToOtherZoneResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class MigrateToOtherZoneResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: MigrateToOtherZoneResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = MigrateToOtherZoneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDeployMachineRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
    ):
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class ModifyDeployMachineResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class ModifyDeployMachineResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyDeployMachineResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyDeployMachineResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyElastictaskResponseBodyResultElasticExpansionTask(TeaModel):
    def __init__(
        self,
        cron_expression: str = None,
        elastic_node_count: int = None,
        replica_count: int = None,
        target_indices: List[str] = None,
        trigger_type: str = None,
    ):
        self.cron_expression = cron_expression
        self.elastic_node_count = elastic_node_count
        self.replica_count = replica_count
        self.target_indices = target_indices
        self.trigger_type = trigger_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cron_expression is not None:
            result['cronExpression'] = self.cron_expression
        if self.elastic_node_count is not None:
            result['elasticNodeCount'] = self.elastic_node_count
        if self.replica_count is not None:
            result['replicaCount'] = self.replica_count
        if self.target_indices is not None:
            result['targetIndices'] = self.target_indices
        if self.trigger_type is not None:
            result['triggerType'] = self.trigger_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cronExpression') is not None:
            self.cron_expression = m.get('cronExpression')
        if m.get('elasticNodeCount') is not None:
            self.elastic_node_count = m.get('elasticNodeCount')
        if m.get('replicaCount') is not None:
            self.replica_count = m.get('replicaCount')
        if m.get('targetIndices') is not None:
            self.target_indices = m.get('targetIndices')
        if m.get('triggerType') is not None:
            self.trigger_type = m.get('triggerType')
        return self


class ModifyElastictaskResponseBodyResultElasticShrinkTask(TeaModel):
    def __init__(
        self,
        cron_expression: str = None,
        elastic_node_count: int = None,
        replica_count: int = None,
        target_indices: List[str] = None,
        trigger_type: str = None,
    ):
        self.cron_expression = cron_expression
        self.elastic_node_count = elastic_node_count
        self.replica_count = replica_count
        self.target_indices = target_indices
        self.trigger_type = trigger_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cron_expression is not None:
            result['cronExpression'] = self.cron_expression
        if self.elastic_node_count is not None:
            result['elasticNodeCount'] = self.elastic_node_count
        if self.replica_count is not None:
            result['replicaCount'] = self.replica_count
        if self.target_indices is not None:
            result['targetIndices'] = self.target_indices
        if self.trigger_type is not None:
            result['triggerType'] = self.trigger_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cronExpression') is not None:
            self.cron_expression = m.get('cronExpression')
        if m.get('elasticNodeCount') is not None:
            self.elastic_node_count = m.get('elasticNodeCount')
        if m.get('replicaCount') is not None:
            self.replica_count = m.get('replicaCount')
        if m.get('targetIndices') is not None:
            self.target_indices = m.get('targetIndices')
        if m.get('triggerType') is not None:
            self.trigger_type = m.get('triggerType')
        return self


class ModifyElastictaskResponseBodyResult(TeaModel):
    def __init__(
        self,
        elastic_expansion_task: ModifyElastictaskResponseBodyResultElasticExpansionTask = None,
        elastic_shrink_task: ModifyElastictaskResponseBodyResultElasticShrinkTask = None,
    ):
        self.elastic_expansion_task = elastic_expansion_task
        self.elastic_shrink_task = elastic_shrink_task

    def validate(self):
        if self.elastic_expansion_task:
            self.elastic_expansion_task.validate()
        if self.elastic_shrink_task:
            self.elastic_shrink_task.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.elastic_expansion_task is not None:
            result['elasticExpansionTask'] = self.elastic_expansion_task.to_map()
        if self.elastic_shrink_task is not None:
            result['elasticShrinkTask'] = self.elastic_shrink_task.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('elasticExpansionTask') is not None:
            temp_model = ModifyElastictaskResponseBodyResultElasticExpansionTask()
            self.elastic_expansion_task = temp_model.from_map(m['elasticExpansionTask'])
        if m.get('elasticShrinkTask') is not None:
            temp_model = ModifyElastictaskResponseBodyResultElasticShrinkTask()
            self.elastic_shrink_task = temp_model.from_map(m['elasticShrinkTask'])
        return self


class ModifyElastictaskResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: ModifyElastictaskResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = ModifyElastictaskResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class ModifyElastictaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyElastictaskResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyElastictaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyInstanceMaintainTimeRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
    ):
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class ModifyInstanceMaintainTimeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class ModifyInstanceMaintainTimeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyInstanceMaintainTimeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyInstanceMaintainTimeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyWhiteIpsRequestWhiteIpGroup(TeaModel):
    def __init__(
        self,
        group_name: str = None,
        ips: List[str] = None,
        white_ip_type: str = None,
    ):
        # 白名单组的组名。如果选填了whiteIpGroup参数，则该参数必填。
        self.group_name = group_name
        # 白名单组中的IP列表。如果选填了whiteIpGroup参数，则该参数必填。
        self.ips = ips
        # ip白名单的类型
        self.white_ip_type = white_ip_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_name is not None:
            result['groupName'] = self.group_name
        if self.ips is not None:
            result['ips'] = self.ips
        if self.white_ip_type is not None:
            result['whiteIpType'] = self.white_ip_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('groupName') is not None:
            self.group_name = m.get('groupName')
        if m.get('ips') is not None:
            self.ips = m.get('ips')
        if m.get('whiteIpType') is not None:
            self.white_ip_type = m.get('whiteIpType')
        return self


class ModifyWhiteIpsRequest(TeaModel):
    def __init__(
        self,
        modify_mode: str = None,
        network_type: str = None,
        node_type: str = None,
        white_ip_group: ModifyWhiteIpsRequestWhiteIpGroup = None,
        white_ip_list: List[str] = None,
        client_token: str = None,
    ):
        # 修改方式，取值含义如下：
        # 
        # Cover（默认值）：使用ips参数的值覆盖原IP白名单。
        # 
        # Append：在原IP白名单中增加ips参数中输入的IP地址。
        # 
        # Delete：Delete：在原IP白名单中删除ips参数中输入的IP地址，至少需要保留一个IP地址。
        self.modify_mode = modify_mode
        # 网络类型。可选值：PRIVATE（私网）、PUBLIC（公网）。如果选填了whiteIpList参数，则该参数必填。
        self.network_type = network_type
        # 节点类型。可选值：WORKER（Elasticsearch集群）、KIBANA（Kibana集群）。如果选填了whiteIpList参数，则该参数必填。
        self.node_type = node_type
        # 以白名单组whiteIpGroup传参方式，更新实例白名单安全配置。仅支持更新一个白名单组。
        self.white_ip_group = white_ip_group
        # 白名单列表。whiteIpGroup为空时可用，更改默认分组白名单
        self.white_ip_list = white_ip_list
        self.client_token = client_token

    def validate(self):
        if self.white_ip_group:
            self.white_ip_group.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.modify_mode is not None:
            result['modifyMode'] = self.modify_mode
        if self.network_type is not None:
            result['networkType'] = self.network_type
        if self.node_type is not None:
            result['nodeType'] = self.node_type
        if self.white_ip_group is not None:
            result['whiteIpGroup'] = self.white_ip_group.to_map()
        if self.white_ip_list is not None:
            result['whiteIpList'] = self.white_ip_list
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('modifyMode') is not None:
            self.modify_mode = m.get('modifyMode')
        if m.get('networkType') is not None:
            self.network_type = m.get('networkType')
        if m.get('nodeType') is not None:
            self.node_type = m.get('nodeType')
        if m.get('whiteIpGroup') is not None:
            temp_model = ModifyWhiteIpsRequestWhiteIpGroup()
            self.white_ip_group = temp_model.from_map(m['whiteIpGroup'])
        if m.get('whiteIpList') is not None:
            self.white_ip_list = m.get('whiteIpList')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        return self


class ModifyWhiteIpsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class ModifyWhiteIpsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyWhiteIpsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyWhiteIpsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class MoveResourceGroupRequest(TeaModel):
    def __init__(
        self,
        resource_group_id: str = None,
        client_token: str = None,
    ):
        self.resource_group_id = resource_group_id
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        return self


class MoveResourceGroupResponseBodyResultDictList(TeaModel):
    def __init__(
        self,
        file_size: int = None,
        name: str = None,
        source_type: str = None,
        type: str = None,
    ):
        self.file_size = file_size
        self.name = name
        self.source_type = source_type
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_size is not None:
            result['fileSize'] = self.file_size
        if self.name is not None:
            result['name'] = self.name
        if self.source_type is not None:
            result['sourceType'] = self.source_type
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fileSize') is not None:
            self.file_size = m.get('fileSize')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class MoveResourceGroupResponseBodyResultKibanaConfiguration(TeaModel):
    def __init__(
        self,
        amount: int = None,
        disk: int = None,
        disk_type: str = None,
        spec: str = None,
    ):
        self.amount = amount
        self.disk = disk
        self.disk_type = disk_type
        self.spec = spec

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.amount is not None:
            result['amount'] = self.amount
        if self.disk is not None:
            result['disk'] = self.disk
        if self.disk_type is not None:
            result['diskType'] = self.disk_type
        if self.spec is not None:
            result['spec'] = self.spec
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('amount') is not None:
            self.amount = m.get('amount')
        if m.get('disk') is not None:
            self.disk = m.get('disk')
        if m.get('diskType') is not None:
            self.disk_type = m.get('diskType')
        if m.get('spec') is not None:
            self.spec = m.get('spec')
        return self


class MoveResourceGroupResponseBodyResultMasterConfiguration(TeaModel):
    def __init__(
        self,
        amount: int = None,
        disk: int = None,
        disk_type: str = None,
        spec: str = None,
    ):
        self.amount = amount
        self.disk = disk
        self.disk_type = disk_type
        self.spec = spec

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.amount is not None:
            result['amount'] = self.amount
        if self.disk is not None:
            result['disk'] = self.disk
        if self.disk_type is not None:
            result['diskType'] = self.disk_type
        if self.spec is not None:
            result['spec'] = self.spec
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('amount') is not None:
            self.amount = m.get('amount')
        if m.get('disk') is not None:
            self.disk = m.get('disk')
        if m.get('diskType') is not None:
            self.disk_type = m.get('diskType')
        if m.get('spec') is not None:
            self.spec = m.get('spec')
        return self


class MoveResourceGroupResponseBodyResultNetworkConfig(TeaModel):
    def __init__(
        self,
        type: str = None,
        vpc_id: str = None,
        vs_area: str = None,
        vswitch_id: str = None,
    ):
        self.type = type
        self.vpc_id = vpc_id
        self.vs_area = vs_area
        self.vswitch_id = vswitch_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['type'] = self.type
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        if self.vs_area is not None:
            result['vsArea'] = self.vs_area
        if self.vswitch_id is not None:
            result['vswitchId'] = self.vswitch_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        if m.get('vsArea') is not None:
            self.vs_area = m.get('vsArea')
        if m.get('vswitchId') is not None:
            self.vswitch_id = m.get('vswitchId')
        return self


class MoveResourceGroupResponseBodyResultNodeSpec(TeaModel):
    def __init__(
        self,
        disk: int = None,
        disk_type: str = None,
        spec: str = None,
    ):
        self.disk = disk
        self.disk_type = disk_type
        self.spec = spec

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.disk is not None:
            result['disk'] = self.disk
        if self.disk_type is not None:
            result['diskType'] = self.disk_type
        if self.spec is not None:
            result['spec'] = self.spec
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('disk') is not None:
            self.disk = m.get('disk')
        if m.get('diskType') is not None:
            self.disk_type = m.get('diskType')
        if m.get('spec') is not None:
            self.spec = m.get('spec')
        return self


class MoveResourceGroupResponseBodyResultSynonymsDicts(TeaModel):
    def __init__(
        self,
        file_size: int = None,
        name: str = None,
        source_type: str = None,
        type: str = None,
    ):
        self.file_size = file_size
        self.name = name
        self.source_type = source_type
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_size is not None:
            result['fileSize'] = self.file_size
        if self.name is not None:
            result['name'] = self.name
        if self.source_type is not None:
            result['sourceType'] = self.source_type
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fileSize') is not None:
            self.file_size = m.get('fileSize')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class MoveResourceGroupResponseBodyResult(TeaModel):
    def __init__(
        self,
        created_at: str = None,
        description: str = None,
        dict_list: List[MoveResourceGroupResponseBodyResultDictList] = None,
        domain: str = None,
        es_version: str = None,
        instance_id: str = None,
        kibana_configuration: MoveResourceGroupResponseBodyResultKibanaConfiguration = None,
        kibana_domain: str = None,
        kibana_port: int = None,
        master_configuration: MoveResourceGroupResponseBodyResultMasterConfiguration = None,
        network_config: MoveResourceGroupResponseBodyResultNetworkConfig = None,
        node_amount: int = None,
        node_spec: MoveResourceGroupResponseBodyResultNodeSpec = None,
        payment_type: str = None,
        public_domain: str = None,
        public_port: int = None,
        status: str = None,
        synonyms_dicts: List[MoveResourceGroupResponseBodyResultSynonymsDicts] = None,
        updated_at: str = None,
    ):
        self.created_at = created_at
        self.description = description
        self.dict_list = dict_list
        self.domain = domain
        self.es_version = es_version
        self.instance_id = instance_id
        self.kibana_configuration = kibana_configuration
        self.kibana_domain = kibana_domain
        self.kibana_port = kibana_port
        self.master_configuration = master_configuration
        self.network_config = network_config
        self.node_amount = node_amount
        self.node_spec = node_spec
        self.payment_type = payment_type
        self.public_domain = public_domain
        self.public_port = public_port
        self.status = status
        self.synonyms_dicts = synonyms_dicts
        self.updated_at = updated_at

    def validate(self):
        if self.dict_list:
            for k in self.dict_list:
                if k:
                    k.validate()
        if self.kibana_configuration:
            self.kibana_configuration.validate()
        if self.master_configuration:
            self.master_configuration.validate()
        if self.network_config:
            self.network_config.validate()
        if self.node_spec:
            self.node_spec.validate()
        if self.synonyms_dicts:
            for k in self.synonyms_dicts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_at is not None:
            result['createdAt'] = self.created_at
        if self.description is not None:
            result['description'] = self.description
        result['dictList'] = []
        if self.dict_list is not None:
            for k in self.dict_list:
                result['dictList'].append(k.to_map() if k else None)
        if self.domain is not None:
            result['domain'] = self.domain
        if self.es_version is not None:
            result['esVersion'] = self.es_version
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.kibana_configuration is not None:
            result['kibanaConfiguration'] = self.kibana_configuration.to_map()
        if self.kibana_domain is not None:
            result['kibanaDomain'] = self.kibana_domain
        if self.kibana_port is not None:
            result['kibanaPort'] = self.kibana_port
        if self.master_configuration is not None:
            result['masterConfiguration'] = self.master_configuration.to_map()
        if self.network_config is not None:
            result['networkConfig'] = self.network_config.to_map()
        if self.node_amount is not None:
            result['nodeAmount'] = self.node_amount
        if self.node_spec is not None:
            result['nodeSpec'] = self.node_spec.to_map()
        if self.payment_type is not None:
            result['paymentType'] = self.payment_type
        if self.public_domain is not None:
            result['publicDomain'] = self.public_domain
        if self.public_port is not None:
            result['publicPort'] = self.public_port
        if self.status is not None:
            result['status'] = self.status
        result['synonymsDicts'] = []
        if self.synonyms_dicts is not None:
            for k in self.synonyms_dicts:
                result['synonymsDicts'].append(k.to_map() if k else None)
        if self.updated_at is not None:
            result['updatedAt'] = self.updated_at
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')
        if m.get('description') is not None:
            self.description = m.get('description')
        self.dict_list = []
        if m.get('dictList') is not None:
            for k in m.get('dictList'):
                temp_model = MoveResourceGroupResponseBodyResultDictList()
                self.dict_list.append(temp_model.from_map(k))
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('esVersion') is not None:
            self.es_version = m.get('esVersion')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('kibanaConfiguration') is not None:
            temp_model = MoveResourceGroupResponseBodyResultKibanaConfiguration()
            self.kibana_configuration = temp_model.from_map(m['kibanaConfiguration'])
        if m.get('kibanaDomain') is not None:
            self.kibana_domain = m.get('kibanaDomain')
        if m.get('kibanaPort') is not None:
            self.kibana_port = m.get('kibanaPort')
        if m.get('masterConfiguration') is not None:
            temp_model = MoveResourceGroupResponseBodyResultMasterConfiguration()
            self.master_configuration = temp_model.from_map(m['masterConfiguration'])
        if m.get('networkConfig') is not None:
            temp_model = MoveResourceGroupResponseBodyResultNetworkConfig()
            self.network_config = temp_model.from_map(m['networkConfig'])
        if m.get('nodeAmount') is not None:
            self.node_amount = m.get('nodeAmount')
        if m.get('nodeSpec') is not None:
            temp_model = MoveResourceGroupResponseBodyResultNodeSpec()
            self.node_spec = temp_model.from_map(m['nodeSpec'])
        if m.get('paymentType') is not None:
            self.payment_type = m.get('paymentType')
        if m.get('publicDomain') is not None:
            self.public_domain = m.get('publicDomain')
        if m.get('publicPort') is not None:
            self.public_port = m.get('publicPort')
        if m.get('status') is not None:
            self.status = m.get('status')
        self.synonyms_dicts = []
        if m.get('synonymsDicts') is not None:
            for k in m.get('synonymsDicts'):
                temp_model = MoveResourceGroupResponseBodyResultSynonymsDicts()
                self.synonyms_dicts.append(temp_model.from_map(k))
        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')
        return self


class MoveResourceGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: MoveResourceGroupResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = MoveResourceGroupResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class MoveResourceGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: MoveResourceGroupResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = MoveResourceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OpenDiagnosisRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        lang: str = None,
    ):
        self.client_token = client_token
        self.lang = lang

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.lang is not None:
            result['lang'] = self.lang
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('lang') is not None:
            self.lang = m.get('lang')
        return self


class OpenDiagnosisResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class OpenDiagnosisResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: OpenDiagnosisResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = OpenDiagnosisResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OpenHttpsRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
    ):
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        return self


class OpenHttpsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class OpenHttpsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: OpenHttpsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = OpenHttpsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PostEmonTryAlarmRuleResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class PostEmonTryAlarmRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: PostEmonTryAlarmRuleResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = PostEmonTryAlarmRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecommendTemplatesRequest(TeaModel):
    def __init__(
        self,
        usage_scenario: str = None,
    ):
        self.usage_scenario = usage_scenario

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.usage_scenario is not None:
            result['usageScenario'] = self.usage_scenario
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('usageScenario') is not None:
            self.usage_scenario = m.get('usageScenario')
        return self


class RecommendTemplatesResponseBodyResult(TeaModel):
    def __init__(
        self,
        content: str = None,
        template_name: str = None,
    ):
        self.content = content
        self.template_name = template_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['content'] = self.content
        if self.template_name is not None:
            result['templateName'] = self.template_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('templateName') is not None:
            self.template_name = m.get('templateName')
        return self


class RecommendTemplatesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[RecommendTemplatesResponseBodyResult] = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = RecommendTemplatesResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class RecommendTemplatesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RecommendTemplatesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RecommendTemplatesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReinstallCollectorRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
    ):
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class ReinstallCollectorResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class ReinstallCollectorResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ReinstallCollectorResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ReinstallCollectorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveApmResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class RemoveApmResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RemoveApmResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RemoveApmResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RenewInstanceRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
    ):
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        return self


class RenewInstanceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class RenewInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RenewInstanceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RenewInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RenewLogstashRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
    ):
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        return self


class RenewLogstashResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class RenewLogstashResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RenewLogstashResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RenewLogstashResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RestartCollectorRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
    ):
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class RestartCollectorResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class RestartCollectorResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RestartCollectorResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RestartCollectorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RestartInstanceRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        force: bool = None,
    ):
        self.client_token = client_token
        self.force = force

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.force is not None:
            result['force'] = self.force
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('force') is not None:
            self.force = m.get('force')
        return self


class RestartInstanceResponseBodyResultDictList(TeaModel):
    def __init__(
        self,
        file_size: int = None,
        name: str = None,
        source_type: str = None,
        type: str = None,
    ):
        self.file_size = file_size
        self.name = name
        self.source_type = source_type
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_size is not None:
            result['fileSize'] = self.file_size
        if self.name is not None:
            result['name'] = self.name
        if self.source_type is not None:
            result['sourceType'] = self.source_type
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fileSize') is not None:
            self.file_size = m.get('fileSize')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class RestartInstanceResponseBodyResultKibanaConfiguration(TeaModel):
    def __init__(
        self,
        amount: int = None,
        disk: int = None,
        disk_type: str = None,
        spec: str = None,
    ):
        self.amount = amount
        self.disk = disk
        self.disk_type = disk_type
        self.spec = spec

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.amount is not None:
            result['amount'] = self.amount
        if self.disk is not None:
            result['disk'] = self.disk
        if self.disk_type is not None:
            result['diskType'] = self.disk_type
        if self.spec is not None:
            result['spec'] = self.spec
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('amount') is not None:
            self.amount = m.get('amount')
        if m.get('disk') is not None:
            self.disk = m.get('disk')
        if m.get('diskType') is not None:
            self.disk_type = m.get('diskType')
        if m.get('spec') is not None:
            self.spec = m.get('spec')
        return self


class RestartInstanceResponseBodyResultMasterConfiguration(TeaModel):
    def __init__(
        self,
        amount: int = None,
        disk: int = None,
        disk_type: str = None,
        spec: str = None,
    ):
        self.amount = amount
        self.disk = disk
        self.disk_type = disk_type
        self.spec = spec

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.amount is not None:
            result['amount'] = self.amount
        if self.disk is not None:
            result['disk'] = self.disk
        if self.disk_type is not None:
            result['diskType'] = self.disk_type
        if self.spec is not None:
            result['spec'] = self.spec
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('amount') is not None:
            self.amount = m.get('amount')
        if m.get('disk') is not None:
            self.disk = m.get('disk')
        if m.get('diskType') is not None:
            self.disk_type = m.get('diskType')
        if m.get('spec') is not None:
            self.spec = m.get('spec')
        return self


class RestartInstanceResponseBodyResultNetworkConfig(TeaModel):
    def __init__(
        self,
        type: str = None,
        vpc_id: str = None,
        vs_area: str = None,
        vswitch_id: str = None,
    ):
        self.type = type
        self.vpc_id = vpc_id
        self.vs_area = vs_area
        self.vswitch_id = vswitch_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['type'] = self.type
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        if self.vs_area is not None:
            result['vsArea'] = self.vs_area
        if self.vswitch_id is not None:
            result['vswitchId'] = self.vswitch_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        if m.get('vsArea') is not None:
            self.vs_area = m.get('vsArea')
        if m.get('vswitchId') is not None:
            self.vswitch_id = m.get('vswitchId')
        return self


class RestartInstanceResponseBodyResultNodeSpec(TeaModel):
    def __init__(
        self,
        disk: int = None,
        disk_type: str = None,
        spec: str = None,
    ):
        self.disk = disk
        self.disk_type = disk_type
        self.spec = spec

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.disk is not None:
            result['disk'] = self.disk
        if self.disk_type is not None:
            result['diskType'] = self.disk_type
        if self.spec is not None:
            result['spec'] = self.spec
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('disk') is not None:
            self.disk = m.get('disk')
        if m.get('diskType') is not None:
            self.disk_type = m.get('diskType')
        if m.get('spec') is not None:
            self.spec = m.get('spec')
        return self


class RestartInstanceResponseBodyResultSynonymsDicts(TeaModel):
    def __init__(
        self,
        file_size: int = None,
        name: str = None,
        source_type: str = None,
        type: str = None,
    ):
        self.file_size = file_size
        self.name = name
        self.source_type = source_type
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_size is not None:
            result['fileSize'] = self.file_size
        if self.name is not None:
            result['name'] = self.name
        if self.source_type is not None:
            result['sourceType'] = self.source_type
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fileSize') is not None:
            self.file_size = m.get('fileSize')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class RestartInstanceResponseBodyResult(TeaModel):
    def __init__(
        self,
        created_at: str = None,
        description: str = None,
        dict_list: List[RestartInstanceResponseBodyResultDictList] = None,
        domain: str = None,
        es_version: str = None,
        instance_id: str = None,
        kibana_configuration: RestartInstanceResponseBodyResultKibanaConfiguration = None,
        kibana_domain: str = None,
        kibana_port: int = None,
        master_configuration: RestartInstanceResponseBodyResultMasterConfiguration = None,
        network_config: RestartInstanceResponseBodyResultNetworkConfig = None,
        node_amount: int = None,
        node_spec: RestartInstanceResponseBodyResultNodeSpec = None,
        payment_type: str = None,
        public_domain: str = None,
        public_port: int = None,
        status: str = None,
        synonyms_dicts: List[RestartInstanceResponseBodyResultSynonymsDicts] = None,
        updated_at: str = None,
    ):
        self.created_at = created_at
        self.description = description
        self.dict_list = dict_list
        self.domain = domain
        self.es_version = es_version
        self.instance_id = instance_id
        self.kibana_configuration = kibana_configuration
        self.kibana_domain = kibana_domain
        self.kibana_port = kibana_port
        self.master_configuration = master_configuration
        self.network_config = network_config
        self.node_amount = node_amount
        self.node_spec = node_spec
        self.payment_type = payment_type
        self.public_domain = public_domain
        self.public_port = public_port
        self.status = status
        self.synonyms_dicts = synonyms_dicts
        self.updated_at = updated_at

    def validate(self):
        if self.dict_list:
            for k in self.dict_list:
                if k:
                    k.validate()
        if self.kibana_configuration:
            self.kibana_configuration.validate()
        if self.master_configuration:
            self.master_configuration.validate()
        if self.network_config:
            self.network_config.validate()
        if self.node_spec:
            self.node_spec.validate()
        if self.synonyms_dicts:
            for k in self.synonyms_dicts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_at is not None:
            result['createdAt'] = self.created_at
        if self.description is not None:
            result['description'] = self.description
        result['dictList'] = []
        if self.dict_list is not None:
            for k in self.dict_list:
                result['dictList'].append(k.to_map() if k else None)
        if self.domain is not None:
            result['domain'] = self.domain
        if self.es_version is not None:
            result['esVersion'] = self.es_version
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.kibana_configuration is not None:
            result['kibanaConfiguration'] = self.kibana_configuration.to_map()
        if self.kibana_domain is not None:
            result['kibanaDomain'] = self.kibana_domain
        if self.kibana_port is not None:
            result['kibanaPort'] = self.kibana_port
        if self.master_configuration is not None:
            result['masterConfiguration'] = self.master_configuration.to_map()
        if self.network_config is not None:
            result['networkConfig'] = self.network_config.to_map()
        if self.node_amount is not None:
            result['nodeAmount'] = self.node_amount
        if self.node_spec is not None:
            result['nodeSpec'] = self.node_spec.to_map()
        if self.payment_type is not None:
            result['paymentType'] = self.payment_type
        if self.public_domain is not None:
            result['publicDomain'] = self.public_domain
        if self.public_port is not None:
            result['publicPort'] = self.public_port
        if self.status is not None:
            result['status'] = self.status
        result['synonymsDicts'] = []
        if self.synonyms_dicts is not None:
            for k in self.synonyms_dicts:
                result['synonymsDicts'].append(k.to_map() if k else None)
        if self.updated_at is not None:
            result['updatedAt'] = self.updated_at
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')
        if m.get('description') is not None:
            self.description = m.get('description')
        self.dict_list = []
        if m.get('dictList') is not None:
            for k in m.get('dictList'):
                temp_model = RestartInstanceResponseBodyResultDictList()
                self.dict_list.append(temp_model.from_map(k))
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('esVersion') is not None:
            self.es_version = m.get('esVersion')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('kibanaConfiguration') is not None:
            temp_model = RestartInstanceResponseBodyResultKibanaConfiguration()
            self.kibana_configuration = temp_model.from_map(m['kibanaConfiguration'])
        if m.get('kibanaDomain') is not None:
            self.kibana_domain = m.get('kibanaDomain')
        if m.get('kibanaPort') is not None:
            self.kibana_port = m.get('kibanaPort')
        if m.get('masterConfiguration') is not None:
            temp_model = RestartInstanceResponseBodyResultMasterConfiguration()
            self.master_configuration = temp_model.from_map(m['masterConfiguration'])
        if m.get('networkConfig') is not None:
            temp_model = RestartInstanceResponseBodyResultNetworkConfig()
            self.network_config = temp_model.from_map(m['networkConfig'])
        if m.get('nodeAmount') is not None:
            self.node_amount = m.get('nodeAmount')
        if m.get('nodeSpec') is not None:
            temp_model = RestartInstanceResponseBodyResultNodeSpec()
            self.node_spec = temp_model.from_map(m['nodeSpec'])
        if m.get('paymentType') is not None:
            self.payment_type = m.get('paymentType')
        if m.get('publicDomain') is not None:
            self.public_domain = m.get('publicDomain')
        if m.get('publicPort') is not None:
            self.public_port = m.get('publicPort')
        if m.get('status') is not None:
            self.status = m.get('status')
        self.synonyms_dicts = []
        if m.get('synonymsDicts') is not None:
            for k in m.get('synonymsDicts'):
                temp_model = RestartInstanceResponseBodyResultSynonymsDicts()
                self.synonyms_dicts.append(temp_model.from_map(k))
        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')
        return self


class RestartInstanceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: RestartInstanceResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = RestartInstanceResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class RestartInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RestartInstanceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RestartInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RestartLogstashRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        force: bool = None,
    ):
        self.client_token = client_token
        self.force = force

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.force is not None:
            result['force'] = self.force
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('force') is not None:
            self.force = m.get('force')
        return self


class RestartLogstashResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RestartLogstashResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RestartLogstashResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RestartLogstashResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResumeElasticsearchTaskRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
    ):
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        return self


class ResumeElasticsearchTaskResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class ResumeElasticsearchTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ResumeElasticsearchTaskResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ResumeElasticsearchTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResumeLogstashTaskRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
    ):
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        return self


class ResumeLogstashTaskResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: bool = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class ResumeLogstashTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ResumeLogstashTaskResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ResumeLogstashTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RolloverDataStreamRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
    ):
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class RolloverDataStreamResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class RolloverDataStreamResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RolloverDataStreamResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RolloverDataStreamResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RunPipelinesRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
    ):
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class RunPipelinesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class RunPipelinesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RunPipelinesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RunPipelinesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ShrinkNodeRequestBody(TeaModel):
    def __init__(
        self,
        host: str = None,
        port: int = None,
        zone_id: str = None,
    ):
        self.host = host
        self.port = port
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host is not None:
            result['host'] = self.host
        if self.port is not None:
            result['port'] = self.port
        if self.zone_id is not None:
            result['zoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('host') is not None:
            self.host = m.get('host')
        if m.get('port') is not None:
            self.port = m.get('port')
        if m.get('zoneId') is not None:
            self.zone_id = m.get('zoneId')
        return self


class ShrinkNodeRequest(TeaModel):
    def __init__(
        self,
        body: List[ShrinkNodeRequestBody] = None,
        client_token: str = None,
        ignore_status: bool = None,
        node_type: str = None,
    ):
        self.body = body
        self.client_token = client_token
        self.ignore_status = ignore_status
        self.node_type = node_type

    def validate(self):
        if self.body:
            for k in self.body:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['body'] = []
        if self.body is not None:
            for k in self.body:
                result['body'].append(k.to_map() if k else None)
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.ignore_status is not None:
            result['ignoreStatus'] = self.ignore_status
        if self.node_type is not None:
            result['nodeType'] = self.node_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.body = []
        if m.get('body') is not None:
            for k in m.get('body'):
                temp_model = ShrinkNodeRequestBody()
                self.body.append(temp_model.from_map(k))
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('ignoreStatus') is not None:
            self.ignore_status = m.get('ignoreStatus')
        if m.get('nodeType') is not None:
            self.node_type = m.get('nodeType')
        return self


class ShrinkNodeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class ShrinkNodeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ShrinkNodeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ShrinkNodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartApmResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class StartApmResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StartApmResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = StartApmResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartCollectorRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
    ):
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class StartCollectorResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class StartCollectorResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StartCollectorResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = StartCollectorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopApmResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class StopApmResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StopApmResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = StopApmResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopCollectorRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
    ):
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class StopCollectorResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class StopCollectorResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StopCollectorResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = StopCollectorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopPipelinesRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
    ):
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class StopPipelinesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class StopPipelinesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StopPipelinesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = StopPipelinesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TagResourcesRequestTags(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class TagResourcesRequest(TeaModel):
    def __init__(
        self,
        resource_ids: List[str] = None,
        resource_type: str = None,
        tags: List[TagResourcesRequestTags] = None,
    ):
        self.resource_ids = resource_ids
        self.resource_type = resource_type
        self.tags = tags

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_ids is not None:
            result['ResourceIds'] = self.resource_ids
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceIds') is not None:
            self.resource_ids = m.get('ResourceIds')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = TagResourcesRequestTags()
                self.tags.append(temp_model.from_map(k))
        return self


class TagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class TagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: TagResourcesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = TagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TransferNodeRequestBody(TeaModel):
    def __init__(
        self,
        host: str = None,
        port: int = None,
        zone_id: str = None,
    ):
        self.host = host
        self.port = port
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host is not None:
            result['host'] = self.host
        if self.port is not None:
            result['port'] = self.port
        if self.zone_id is not None:
            result['zoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('host') is not None:
            self.host = m.get('host')
        if m.get('port') is not None:
            self.port = m.get('port')
        if m.get('zoneId') is not None:
            self.zone_id = m.get('zoneId')
        return self


class TransferNodeRequest(TeaModel):
    def __init__(
        self,
        body: List[TransferNodeRequestBody] = None,
        client_token: str = None,
        node_type: str = None,
    ):
        self.body = body
        self.client_token = client_token
        self.node_type = node_type

    def validate(self):
        if self.body:
            for k in self.body:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['body'] = []
        if self.body is not None:
            for k in self.body:
                result['body'].append(k.to_map() if k else None)
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.node_type is not None:
            result['nodeType'] = self.node_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.body = []
        if m.get('body') is not None:
            for k in m.get('body'):
                temp_model = TransferNodeRequestBody()
                self.body.append(temp_model.from_map(k))
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('nodeType') is not None:
            self.node_type = m.get('nodeType')
        return self


class TransferNodeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class TransferNodeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: TransferNodeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = TransferNodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TriggerNetworkRequest(TeaModel):
    def __init__(
        self,
        action_type: str = None,
        network_type: str = None,
        node_type: str = None,
        client_token: str = None,
    ):
        # 动作类型。CLOSE：关闭; OPEN：开启
        self.action_type = action_type
        # 网络类型。PUBLIC：公网；PRIVATE：私网
        self.network_type = network_type
        # 实例类型。KIBANA kibana公私网/WORKER 集群公私网
        self.node_type = node_type
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_type is not None:
            result['actionType'] = self.action_type
        if self.network_type is not None:
            result['networkType'] = self.network_type
        if self.node_type is not None:
            result['nodeType'] = self.node_type
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('actionType') is not None:
            self.action_type = m.get('actionType')
        if m.get('networkType') is not None:
            self.network_type = m.get('networkType')
        if m.get('nodeType') is not None:
            self.node_type = m.get('nodeType')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        return self


class TriggerNetworkResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class TriggerNetworkResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: TriggerNetworkResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = TriggerNetworkResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UninstallKibanaPluginRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
    ):
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        return self


class UninstallKibanaPluginResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[str] = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class UninstallKibanaPluginResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UninstallKibanaPluginResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UninstallKibanaPluginResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UninstallLogstashPluginRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
    ):
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        return self


class UninstallLogstashPluginResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[str] = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class UninstallLogstashPluginResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UninstallLogstashPluginResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UninstallLogstashPluginResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UninstallPluginRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
    ):
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        return self


class UninstallPluginResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[str] = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class UninstallPluginResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UninstallPluginResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UninstallPluginResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UntagResourcesRequest(TeaModel):
    def __init__(
        self,
        all: bool = None,
        resource_ids: str = None,
        resource_type: str = None,
        tag_keys: str = None,
    ):
        self.all = all
        self.resource_ids = resource_ids
        self.resource_type = resource_type
        self.tag_keys = tag_keys

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all is not None:
            result['All'] = self.all
        if self.resource_ids is not None:
            result['ResourceIds'] = self.resource_ids
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tag_keys is not None:
            result['TagKeys'] = self.tag_keys
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('All') is not None:
            self.all = m.get('All')
        if m.get('ResourceIds') is not None:
            self.resource_ids = m.get('ResourceIds')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TagKeys') is not None:
            self.tag_keys = m.get('TagKeys')
        return self


class UntagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class UntagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UntagResourcesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UntagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAdminPasswordRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
    ):
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        return self


class UpdateAdminPasswordResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateAdminPasswordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateAdminPasswordResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateAdminPasswordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAdvancedSettingRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
    ):
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        return self


class UpdateAdvancedSettingResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class UpdateAdvancedSettingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateAdvancedSettingResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateAdvancedSettingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAliwsDictRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
    ):
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        return self


class UpdateAliwsDictResponseBodyResult(TeaModel):
    def __init__(
        self,
        file_size: int = None,
        name: str = None,
        source_type: str = None,
        type: str = None,
    ):
        self.file_size = file_size
        self.name = name
        self.source_type = source_type
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_size is not None:
            result['fileSize'] = self.file_size
        if self.name is not None:
            result['name'] = self.name
        if self.source_type is not None:
            result['sourceType'] = self.source_type
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fileSize') is not None:
            self.file_size = m.get('fileSize')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class UpdateAliwsDictResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[UpdateAliwsDictResponseBodyResult] = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = UpdateAliwsDictResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class UpdateAliwsDictResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateAliwsDictResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateAliwsDictResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateApmRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        output_es: str = None,
        output_espassword: str = None,
        output_esuser_name: str = None,
        token: str = None,
    ):
        # apm实例名
        self.description = description
        # es实例id
        self.output_es = output_es
        # es实例密码
        self.output_espassword = output_espassword
        # es实例用户名
        self.output_esuser_name = output_esuser_name
        # apm server密码
        self.token = token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.output_es is not None:
            result['outputES'] = self.output_es
        if self.output_espassword is not None:
            result['outputESPassword'] = self.output_espassword
        if self.output_esuser_name is not None:
            result['outputESUserName'] = self.output_esuser_name
        if self.token is not None:
            result['token'] = self.token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('outputES') is not None:
            self.output_es = m.get('outputES')
        if m.get('outputESPassword') is not None:
            self.output_espassword = m.get('outputESPassword')
        if m.get('outputESUserName') is not None:
            self.output_esuser_name = m.get('outputESUserName')
        if m.get('token') is not None:
            self.token = m.get('token')
        return self


class UpdateApmResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class UpdateApmResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateApmResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateApmResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateBlackIpsRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        es_ipblacklist: List[str] = None,
    ):
        self.client_token = client_token
        self.es_ipblacklist = es_ipblacklist

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.es_ipblacklist is not None:
            result['esIPBlacklist'] = self.es_ipblacklist
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('esIPBlacklist') is not None:
            self.es_ipblacklist = m.get('esIPBlacklist')
        return self


class UpdateBlackIpsResponseBodyResult(TeaModel):
    def __init__(
        self,
        es_ipblacklist: List[str] = None,
    ):
        self.es_ipblacklist = es_ipblacklist

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.es_ipblacklist is not None:
            result['esIPBlacklist'] = self.es_ipblacklist
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('esIPBlacklist') is not None:
            self.es_ipblacklist = m.get('esIPBlacklist')
        return self


class UpdateBlackIpsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: UpdateBlackIpsResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = UpdateBlackIpsResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class UpdateBlackIpsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateBlackIpsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateBlackIpsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateCollectorRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
    ):
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class UpdateCollectorResponseBodyResultConfigs(TeaModel):
    def __init__(
        self,
        content: str = None,
        file_name: str = None,
    ):
        self.content = content
        self.file_name = file_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class UpdateCollectorResponseBodyResultExtendConfigsMachines(TeaModel):
    def __init__(
        self,
        agent_status: str = None,
        instance_id: str = None,
    ):
        self.agent_status = agent_status
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class UpdateCollectorResponseBodyResultExtendConfigs(TeaModel):
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
        machines: List[UpdateCollectorResponseBodyResultExtendConfigsMachines] = None,
        protocol: str = None,
        success_pods_count: str = None,
        total_pods_count: str = None,
        type: str = None,
        user_name: str = None,
    ):
        self.config_type = config_type
        self.enable_monitoring = enable_monitoring
        self.group_id = group_id
        self.host = host
        self.hosts = hosts
        self.instance_id = instance_id
        self.instance_type = instance_type
        self.kibana_host = kibana_host
        self.machines = machines
        self.protocol = protocol
        self.success_pods_count = success_pods_count
        self.total_pods_count = total_pods_count
        self.type = type
        self.user_name = user_name

    def validate(self):
        if self.machines:
            for k in self.machines:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            for k in self.machines:
                result['machines'].append(k.to_map() if k else None)
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
            for k in m.get('machines'):
                temp_model = UpdateCollectorResponseBodyResultExtendConfigsMachines()
                self.machines.append(temp_model.from_map(k))
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


class UpdateCollectorResponseBodyResult(TeaModel):
    def __init__(
        self,
        collector_paths: List[str] = None,
        configs: List[UpdateCollectorResponseBodyResultConfigs] = None,
        dry_run: bool = None,
        extend_configs: List[UpdateCollectorResponseBodyResultExtendConfigs] = None,
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
        self.configs = configs
        self.dry_run = dry_run
        self.extend_configs = extend_configs
        self.gmt_created_time = gmt_created_time
        self.gmt_update_time = gmt_update_time
        self.name = name
        self.owner_id = owner_id
        self.res_id = res_id
        self.res_type = res_type
        self.res_version = res_version
        self.status = status
        self.vpc_id = vpc_id

    def validate(self):
        if self.configs:
            for k in self.configs:
                if k:
                    k.validate()
        if self.extend_configs:
            for k in self.extend_configs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.collector_paths is not None:
            result['collectorPaths'] = self.collector_paths
        result['configs'] = []
        if self.configs is not None:
            for k in self.configs:
                result['configs'].append(k.to_map() if k else None)
        if self.dry_run is not None:
            result['dryRun'] = self.dry_run
        result['extendConfigs'] = []
        if self.extend_configs is not None:
            for k in self.extend_configs:
                result['extendConfigs'].append(k.to_map() if k else None)
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
            for k in m.get('configs'):
                temp_model = UpdateCollectorResponseBodyResultConfigs()
                self.configs.append(temp_model.from_map(k))
        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')
        self.extend_configs = []
        if m.get('extendConfigs') is not None:
            for k in m.get('extendConfigs'):
                temp_model = UpdateCollectorResponseBodyResultExtendConfigs()
                self.extend_configs.append(temp_model.from_map(k))
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


class UpdateCollectorResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: UpdateCollectorResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = UpdateCollectorResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class UpdateCollectorResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateCollectorResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateCollectorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateCollectorNameRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
    ):
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class UpdateCollectorNameResponseBodyResultConfigs(TeaModel):
    def __init__(
        self,
        content: str = None,
        file_name: str = None,
    ):
        self.content = content
        self.file_name = file_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class UpdateCollectorNameResponseBodyResultExtendConfigsMachines(TeaModel):
    def __init__(
        self,
        agent_status: str = None,
        instance_id: str = None,
    ):
        self.agent_status = agent_status
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class UpdateCollectorNameResponseBodyResultExtendConfigs(TeaModel):
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
        machines: List[UpdateCollectorNameResponseBodyResultExtendConfigsMachines] = None,
        protocol: str = None,
        success_pods_count: str = None,
        total_pods_count: str = None,
        type: str = None,
        user_name: str = None,
    ):
        self.config_type = config_type
        self.enable_monitoring = enable_monitoring
        self.group_id = group_id
        self.host = host
        self.hosts = hosts
        self.instance_id = instance_id
        self.instance_type = instance_type
        self.kibana_host = kibana_host
        self.machines = machines
        self.protocol = protocol
        self.success_pods_count = success_pods_count
        self.total_pods_count = total_pods_count
        self.type = type
        self.user_name = user_name

    def validate(self):
        if self.machines:
            for k in self.machines:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            for k in self.machines:
                result['machines'].append(k.to_map() if k else None)
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
            for k in m.get('machines'):
                temp_model = UpdateCollectorNameResponseBodyResultExtendConfigsMachines()
                self.machines.append(temp_model.from_map(k))
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


class UpdateCollectorNameResponseBodyResult(TeaModel):
    def __init__(
        self,
        collector_paths: List[str] = None,
        configs: List[UpdateCollectorNameResponseBodyResultConfigs] = None,
        dry_run: bool = None,
        extend_configs: List[UpdateCollectorNameResponseBodyResultExtendConfigs] = None,
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
        self.configs = configs
        self.dry_run = dry_run
        self.extend_configs = extend_configs
        self.gmt_created_time = gmt_created_time
        self.gmt_update_time = gmt_update_time
        self.name = name
        self.owner_id = owner_id
        self.res_id = res_id
        self.res_type = res_type
        self.res_version = res_version
        self.status = status
        self.vpc_id = vpc_id

    def validate(self):
        if self.configs:
            for k in self.configs:
                if k:
                    k.validate()
        if self.extend_configs:
            for k in self.extend_configs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.collector_paths is not None:
            result['collectorPaths'] = self.collector_paths
        result['configs'] = []
        if self.configs is not None:
            for k in self.configs:
                result['configs'].append(k.to_map() if k else None)
        if self.dry_run is not None:
            result['dryRun'] = self.dry_run
        result['extendConfigs'] = []
        if self.extend_configs is not None:
            for k in self.extend_configs:
                result['extendConfigs'].append(k.to_map() if k else None)
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
            for k in m.get('configs'):
                temp_model = UpdateCollectorNameResponseBodyResultConfigs()
                self.configs.append(temp_model.from_map(k))
        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')
        self.extend_configs = []
        if m.get('extendConfigs') is not None:
            for k in m.get('extendConfigs'):
                temp_model = UpdateCollectorNameResponseBodyResultExtendConfigs()
                self.extend_configs.append(temp_model.from_map(k))
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


class UpdateCollectorNameResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: UpdateCollectorNameResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = UpdateCollectorNameResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class UpdateCollectorNameResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateCollectorNameResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateCollectorNameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateComponentIndexRequestTemplate(TeaModel):
    def __init__(
        self,
        aliases: Dict[str, Any] = None,
        mappings: Dict[str, Any] = None,
        settings: Dict[str, Any] = None,
    ):
        self.aliases = aliases
        self.mappings = mappings
        self.settings = settings

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aliases is not None:
            result['aliases'] = self.aliases
        if self.mappings is not None:
            result['mappings'] = self.mappings
        if self.settings is not None:
            result['settings'] = self.settings
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('aliases') is not None:
            self.aliases = m.get('aliases')
        if m.get('mappings') is not None:
            self.mappings = m.get('mappings')
        if m.get('settings') is not None:
            self.settings = m.get('settings')
        return self


class UpdateComponentIndexRequest(TeaModel):
    def __init__(
        self,
        meta: Dict[str, Any] = None,
        template: UpdateComponentIndexRequestTemplate = None,
    ):
        self.meta = meta
        self.template = template

    def validate(self):
        if self.template:
            self.template.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.meta is not None:
            result['_meta'] = self.meta
        if self.template is not None:
            result['template'] = self.template.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('_meta') is not None:
            self.meta = m.get('_meta')
        if m.get('template') is not None:
            temp_model = UpdateComponentIndexRequestTemplate()
            self.template = temp_model.from_map(m['template'])
        return self


class UpdateComponentIndexResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class UpdateComponentIndexResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateComponentIndexResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateComponentIndexResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDescriptionRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        client_token: str = None,
    ):
        self.description = description
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        return self


class UpdateDescriptionResponseBodyResult(TeaModel):
    def __init__(
        self,
        description: str = None,
    ):
        self.description = description

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        return self


class UpdateDescriptionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: UpdateDescriptionResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = UpdateDescriptionResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class UpdateDescriptionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateDescriptionResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateDescriptionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDiagnosisSettingsRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        lang: str = None,
    ):
        self.client_token = client_token
        self.lang = lang

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.lang is not None:
            result['lang'] = self.lang
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('lang') is not None:
            self.lang = m.get('lang')
        return self


class UpdateDiagnosisSettingsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class UpdateDiagnosisSettingsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateDiagnosisSettingsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateDiagnosisSettingsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDictRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
    ):
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        return self


class UpdateDictResponseBodyResult(TeaModel):
    def __init__(
        self,
        file_size: int = None,
        name: str = None,
        source_type: str = None,
        type: str = None,
    ):
        self.file_size = file_size
        self.name = name
        self.source_type = source_type
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_size is not None:
            result['fileSize'] = self.file_size
        if self.name is not None:
            result['name'] = self.name
        if self.source_type is not None:
            result['sourceType'] = self.source_type
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fileSize') is not None:
            self.file_size = m.get('fileSize')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class UpdateDictResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[UpdateDictResponseBodyResult] = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = UpdateDictResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class UpdateDictResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateDictResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateDictResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateExtendConfigRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
    ):
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class UpdateExtendConfigResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class UpdateExtendConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateExtendConfigResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateExtendConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateExtendfilesRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
    ):
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class UpdateExtendfilesResponseBodyResult(TeaModel):
    def __init__(
        self,
        file_size: int = None,
        name: str = None,
        source_type: str = None,
    ):
        self.file_size = file_size
        self.name = name
        self.source_type = source_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_size is not None:
            result['fileSize'] = self.file_size
        if self.name is not None:
            result['name'] = self.name
        if self.source_type is not None:
            result['sourceType'] = self.source_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fileSize') is not None:
            self.file_size = m.get('fileSize')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')
        return self


class UpdateExtendfilesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[UpdateExtendfilesResponseBodyResult] = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = UpdateExtendfilesResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class UpdateExtendfilesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateExtendfilesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateExtendfilesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateHotIkDictsRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
    ):
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        return self


class UpdateHotIkDictsResponseBodyResult(TeaModel):
    def __init__(
        self,
        file_size: int = None,
        name: str = None,
        source_type: str = None,
        type: str = None,
    ):
        self.file_size = file_size
        self.name = name
        self.source_type = source_type
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_size is not None:
            result['fileSize'] = self.file_size
        if self.name is not None:
            result['name'] = self.name
        if self.source_type is not None:
            result['sourceType'] = self.source_type
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fileSize') is not None:
            self.file_size = m.get('fileSize')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class UpdateHotIkDictsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[UpdateHotIkDictsResponseBodyResult] = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = UpdateHotIkDictsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class UpdateHotIkDictsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateHotIkDictsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateHotIkDictsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateILMPolicyRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
    ):
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class UpdateILMPolicyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: str = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class UpdateILMPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateILMPolicyResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateILMPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateIndexTemplateRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
    ):
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class UpdateIndexTemplateResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: str = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class UpdateIndexTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateIndexTemplateResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateIndexTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateInstanceRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        ignore_status: bool = None,
        order_action_type: str = None,
    ):
        self.client_token = client_token
        self.ignore_status = ignore_status
        self.order_action_type = order_action_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.ignore_status is not None:
            result['ignoreStatus'] = self.ignore_status
        if self.order_action_type is not None:
            result['orderActionType'] = self.order_action_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('ignoreStatus') is not None:
            self.ignore_status = m.get('ignoreStatus')
        if m.get('orderActionType') is not None:
            self.order_action_type = m.get('orderActionType')
        return self


class UpdateInstanceResponseBodyResultDictList(TeaModel):
    def __init__(
        self,
        file_size: int = None,
        name: str = None,
        source_type: str = None,
        type: str = None,
    ):
        self.file_size = file_size
        self.name = name
        self.source_type = source_type
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_size is not None:
            result['fileSize'] = self.file_size
        if self.name is not None:
            result['name'] = self.name
        if self.source_type is not None:
            result['sourceType'] = self.source_type
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fileSize') is not None:
            self.file_size = m.get('fileSize')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class UpdateInstanceResponseBodyResultKibanaConfiguration(TeaModel):
    def __init__(
        self,
        amount: int = None,
        disk: int = None,
        disk_type: str = None,
        spec: str = None,
    ):
        self.amount = amount
        self.disk = disk
        self.disk_type = disk_type
        self.spec = spec

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.amount is not None:
            result['amount'] = self.amount
        if self.disk is not None:
            result['disk'] = self.disk
        if self.disk_type is not None:
            result['diskType'] = self.disk_type
        if self.spec is not None:
            result['spec'] = self.spec
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('amount') is not None:
            self.amount = m.get('amount')
        if m.get('disk') is not None:
            self.disk = m.get('disk')
        if m.get('diskType') is not None:
            self.disk_type = m.get('diskType')
        if m.get('spec') is not None:
            self.spec = m.get('spec')
        return self


class UpdateInstanceResponseBodyResultMasterConfiguration(TeaModel):
    def __init__(
        self,
        amount: int = None,
        disk: int = None,
        disk_type: str = None,
        spec: str = None,
    ):
        self.amount = amount
        self.disk = disk
        self.disk_type = disk_type
        self.spec = spec

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.amount is not None:
            result['amount'] = self.amount
        if self.disk is not None:
            result['disk'] = self.disk
        if self.disk_type is not None:
            result['diskType'] = self.disk_type
        if self.spec is not None:
            result['spec'] = self.spec
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('amount') is not None:
            self.amount = m.get('amount')
        if m.get('disk') is not None:
            self.disk = m.get('disk')
        if m.get('diskType') is not None:
            self.disk_type = m.get('diskType')
        if m.get('spec') is not None:
            self.spec = m.get('spec')
        return self


class UpdateInstanceResponseBodyResultNetworkConfig(TeaModel):
    def __init__(
        self,
        type: str = None,
        vpc_id: str = None,
        vs_area: str = None,
        vswitch_id: str = None,
    ):
        self.type = type
        self.vpc_id = vpc_id
        self.vs_area = vs_area
        self.vswitch_id = vswitch_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['type'] = self.type
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        if self.vs_area is not None:
            result['vsArea'] = self.vs_area
        if self.vswitch_id is not None:
            result['vswitchId'] = self.vswitch_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        if m.get('vsArea') is not None:
            self.vs_area = m.get('vsArea')
        if m.get('vswitchId') is not None:
            self.vswitch_id = m.get('vswitchId')
        return self


class UpdateInstanceResponseBodyResultNodeSpec(TeaModel):
    def __init__(
        self,
        disk: int = None,
        disk_type: str = None,
        spec: str = None,
    ):
        self.disk = disk
        self.disk_type = disk_type
        self.spec = spec

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.disk is not None:
            result['disk'] = self.disk
        if self.disk_type is not None:
            result['diskType'] = self.disk_type
        if self.spec is not None:
            result['spec'] = self.spec
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('disk') is not None:
            self.disk = m.get('disk')
        if m.get('diskType') is not None:
            self.disk_type = m.get('diskType')
        if m.get('spec') is not None:
            self.spec = m.get('spec')
        return self


class UpdateInstanceResponseBodyResultSynonymsDicts(TeaModel):
    def __init__(
        self,
        file_size: int = None,
        name: str = None,
        source_type: str = None,
        type: str = None,
    ):
        self.file_size = file_size
        self.name = name
        self.source_type = source_type
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_size is not None:
            result['fileSize'] = self.file_size
        if self.name is not None:
            result['name'] = self.name
        if self.source_type is not None:
            result['sourceType'] = self.source_type
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fileSize') is not None:
            self.file_size = m.get('fileSize')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class UpdateInstanceResponseBodyResult(TeaModel):
    def __init__(
        self,
        created_at: str = None,
        description: str = None,
        dict_list: List[UpdateInstanceResponseBodyResultDictList] = None,
        domain: str = None,
        es_version: str = None,
        instance_id: str = None,
        kibana_configuration: UpdateInstanceResponseBodyResultKibanaConfiguration = None,
        kibana_domain: str = None,
        kibana_port: int = None,
        master_configuration: UpdateInstanceResponseBodyResultMasterConfiguration = None,
        network_config: UpdateInstanceResponseBodyResultNetworkConfig = None,
        node_amount: int = None,
        node_spec: UpdateInstanceResponseBodyResultNodeSpec = None,
        payment_type: str = None,
        public_domain: str = None,
        public_port: int = None,
        status: str = None,
        synonyms_dicts: List[UpdateInstanceResponseBodyResultSynonymsDicts] = None,
        updated_at: str = None,
    ):
        self.created_at = created_at
        self.description = description
        self.dict_list = dict_list
        self.domain = domain
        self.es_version = es_version
        self.instance_id = instance_id
        self.kibana_configuration = kibana_configuration
        self.kibana_domain = kibana_domain
        self.kibana_port = kibana_port
        self.master_configuration = master_configuration
        self.network_config = network_config
        self.node_amount = node_amount
        self.node_spec = node_spec
        self.payment_type = payment_type
        self.public_domain = public_domain
        self.public_port = public_port
        self.status = status
        self.synonyms_dicts = synonyms_dicts
        self.updated_at = updated_at

    def validate(self):
        if self.dict_list:
            for k in self.dict_list:
                if k:
                    k.validate()
        if self.kibana_configuration:
            self.kibana_configuration.validate()
        if self.master_configuration:
            self.master_configuration.validate()
        if self.network_config:
            self.network_config.validate()
        if self.node_spec:
            self.node_spec.validate()
        if self.synonyms_dicts:
            for k in self.synonyms_dicts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_at is not None:
            result['createdAt'] = self.created_at
        if self.description is not None:
            result['description'] = self.description
        result['dictList'] = []
        if self.dict_list is not None:
            for k in self.dict_list:
                result['dictList'].append(k.to_map() if k else None)
        if self.domain is not None:
            result['domain'] = self.domain
        if self.es_version is not None:
            result['esVersion'] = self.es_version
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.kibana_configuration is not None:
            result['kibanaConfiguration'] = self.kibana_configuration.to_map()
        if self.kibana_domain is not None:
            result['kibanaDomain'] = self.kibana_domain
        if self.kibana_port is not None:
            result['kibanaPort'] = self.kibana_port
        if self.master_configuration is not None:
            result['masterConfiguration'] = self.master_configuration.to_map()
        if self.network_config is not None:
            result['networkConfig'] = self.network_config.to_map()
        if self.node_amount is not None:
            result['nodeAmount'] = self.node_amount
        if self.node_spec is not None:
            result['nodeSpec'] = self.node_spec.to_map()
        if self.payment_type is not None:
            result['paymentType'] = self.payment_type
        if self.public_domain is not None:
            result['publicDomain'] = self.public_domain
        if self.public_port is not None:
            result['publicPort'] = self.public_port
        if self.status is not None:
            result['status'] = self.status
        result['synonymsDicts'] = []
        if self.synonyms_dicts is not None:
            for k in self.synonyms_dicts:
                result['synonymsDicts'].append(k.to_map() if k else None)
        if self.updated_at is not None:
            result['updatedAt'] = self.updated_at
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')
        if m.get('description') is not None:
            self.description = m.get('description')
        self.dict_list = []
        if m.get('dictList') is not None:
            for k in m.get('dictList'):
                temp_model = UpdateInstanceResponseBodyResultDictList()
                self.dict_list.append(temp_model.from_map(k))
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('esVersion') is not None:
            self.es_version = m.get('esVersion')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('kibanaConfiguration') is not None:
            temp_model = UpdateInstanceResponseBodyResultKibanaConfiguration()
            self.kibana_configuration = temp_model.from_map(m['kibanaConfiguration'])
        if m.get('kibanaDomain') is not None:
            self.kibana_domain = m.get('kibanaDomain')
        if m.get('kibanaPort') is not None:
            self.kibana_port = m.get('kibanaPort')
        if m.get('masterConfiguration') is not None:
            temp_model = UpdateInstanceResponseBodyResultMasterConfiguration()
            self.master_configuration = temp_model.from_map(m['masterConfiguration'])
        if m.get('networkConfig') is not None:
            temp_model = UpdateInstanceResponseBodyResultNetworkConfig()
            self.network_config = temp_model.from_map(m['networkConfig'])
        if m.get('nodeAmount') is not None:
            self.node_amount = m.get('nodeAmount')
        if m.get('nodeSpec') is not None:
            temp_model = UpdateInstanceResponseBodyResultNodeSpec()
            self.node_spec = temp_model.from_map(m['nodeSpec'])
        if m.get('paymentType') is not None:
            self.payment_type = m.get('paymentType')
        if m.get('publicDomain') is not None:
            self.public_domain = m.get('publicDomain')
        if m.get('publicPort') is not None:
            self.public_port = m.get('publicPort')
        if m.get('status') is not None:
            self.status = m.get('status')
        self.synonyms_dicts = []
        if m.get('synonymsDicts') is not None:
            for k in m.get('synonymsDicts'):
                temp_model = UpdateInstanceResponseBodyResultSynonymsDicts()
                self.synonyms_dicts.append(temp_model.from_map(k))
        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')
        return self


class UpdateInstanceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: UpdateInstanceResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = UpdateInstanceResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class UpdateInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateInstanceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateInstanceChargeTypeRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
    ):
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        return self


class UpdateInstanceChargeTypeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class UpdateInstanceChargeTypeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateInstanceChargeTypeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateInstanceChargeTypeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateInstanceSettingsRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
    ):
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        return self


class UpdateInstanceSettingsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateInstanceSettingsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateInstanceSettingsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateInstanceSettingsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateKibanaSettingsRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
    ):
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        return self


class UpdateKibanaSettingsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class UpdateKibanaSettingsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateKibanaSettingsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateKibanaSettingsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateKibanaWhiteIpsRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        modify_mode: str = None,
    ):
        self.client_token = client_token
        self.modify_mode = modify_mode

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.modify_mode is not None:
            result['modifyMode'] = self.modify_mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('modifyMode') is not None:
            self.modify_mode = m.get('modifyMode')
        return self


class UpdateKibanaWhiteIpsResponseBodyResult(TeaModel):
    def __init__(
        self,
        kibana_ipwhitelist: List[str] = None,
        kibana_private_ipwhitelist: List[str] = None,
    ):
        self.kibana_ipwhitelist = kibana_ipwhitelist
        self.kibana_private_ipwhitelist = kibana_private_ipwhitelist

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.kibana_ipwhitelist is not None:
            result['kibanaIPWhitelist'] = self.kibana_ipwhitelist
        if self.kibana_private_ipwhitelist is not None:
            result['kibanaPrivateIPWhitelist'] = self.kibana_private_ipwhitelist
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('kibanaIPWhitelist') is not None:
            self.kibana_ipwhitelist = m.get('kibanaIPWhitelist')
        if m.get('kibanaPrivateIPWhitelist') is not None:
            self.kibana_private_ipwhitelist = m.get('kibanaPrivateIPWhitelist')
        return self


class UpdateKibanaWhiteIpsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: UpdateKibanaWhiteIpsResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = UpdateKibanaWhiteIpsResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class UpdateKibanaWhiteIpsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateKibanaWhiteIpsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateKibanaWhiteIpsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateLogstashRequestNodeSpec(TeaModel):
    def __init__(
        self,
        disk: int = None,
        disk_type: str = None,
        spec: str = None,
    ):
        self.disk = disk
        self.disk_type = disk_type
        self.spec = spec

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.disk is not None:
            result['disk'] = self.disk
        if self.disk_type is not None:
            result['diskType'] = self.disk_type
        if self.spec is not None:
            result['spec'] = self.spec
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('disk') is not None:
            self.disk = m.get('disk')
        if m.get('diskType') is not None:
            self.disk_type = m.get('diskType')
        if m.get('spec') is not None:
            self.spec = m.get('spec')
        return self


class UpdateLogstashRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        node_amount: int = None,
        node_spec: UpdateLogstashRequestNodeSpec = None,
        client_token: str = None,
    ):
        self.description = description
        self.node_amount = node_amount
        self.node_spec = node_spec
        self.client_token = client_token

    def validate(self):
        if self.node_spec:
            self.node_spec.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.node_amount is not None:
            result['nodeAmount'] = self.node_amount
        if self.node_spec is not None:
            result['nodeSpec'] = self.node_spec.to_map()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('nodeAmount') is not None:
            self.node_amount = m.get('nodeAmount')
        if m.get('nodeSpec') is not None:
            temp_model = UpdateLogstashRequestNodeSpec()
            self.node_spec = temp_model.from_map(m['nodeSpec'])
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        return self


class UpdateLogstashResponseBody(TeaModel):
    def __init__(
        self,
        request_id: Logstash = None,
        result: bool = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.request_id:
            self.request_id.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id.to_map()
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            temp_model = Logstash()
            self.request_id = temp_model.from_map(m['RequestId'])
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class UpdateLogstashResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateLogstashResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateLogstashResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateLogstashChargeTypeRequestPaymentInfo(TeaModel):
    def __init__(
        self,
        duration: int = None,
        pricing_cycle: str = None,
    ):
        self.duration = duration
        self.pricing_cycle = pricing_cycle

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.duration is not None:
            result['duration'] = self.duration
        if self.pricing_cycle is not None:
            result['pricingCycle'] = self.pricing_cycle
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('duration') is not None:
            self.duration = m.get('duration')
        if m.get('pricingCycle') is not None:
            self.pricing_cycle = m.get('pricingCycle')
        return self


class UpdateLogstashChargeTypeRequest(TeaModel):
    def __init__(
        self,
        payment_info: UpdateLogstashChargeTypeRequestPaymentInfo = None,
        payment_type: str = None,
        client_token: str = None,
    ):
        self.payment_info = payment_info
        self.payment_type = payment_type
        self.client_token = client_token

    def validate(self):
        if self.payment_info:
            self.payment_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.payment_info is not None:
            result['paymentInfo'] = self.payment_info.to_map()
        if self.payment_type is not None:
            result['paymentType'] = self.payment_type
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('paymentInfo') is not None:
            temp_model = UpdateLogstashChargeTypeRequestPaymentInfo()
            self.payment_info = temp_model.from_map(m['paymentInfo'])
        if m.get('paymentType') is not None:
            self.payment_type = m.get('paymentType')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        return self


class UpdateLogstashChargeTypeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: Logstash = None,
        result: bool = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.request_id:
            self.request_id.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id.to_map()
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            temp_model = Logstash()
            self.request_id = temp_model.from_map(m['RequestId'])
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class UpdateLogstashChargeTypeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateLogstashChargeTypeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateLogstashChargeTypeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateLogstashDescriptionRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        client_token: str = None,
    ):
        self.description = description
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        return self


class UpdateLogstashDescriptionResponseBodyResult(TeaModel):
    def __init__(
        self,
        description: str = None,
    ):
        self.description = description

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        return self


class UpdateLogstashDescriptionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: UpdateLogstashDescriptionResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = UpdateLogstashDescriptionResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class UpdateLogstashDescriptionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateLogstashDescriptionResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateLogstashDescriptionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateLogstashSettingsRequest(TeaModel):
    def __init__(
        self,
        body: Dict[str, Any] = None,
        client_token: str = None,
    ):
        self.body = body
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            self.body = m.get('body')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        return self


class UpdateLogstashSettingsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: Logstash = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = Logstash()
            self.result = temp_model.from_map(m['Result'])
        return self


class UpdateLogstashSettingsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateLogstashSettingsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateLogstashSettingsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdatePipelineManagementConfigRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
    ):
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        return self


class UpdatePipelineManagementConfigResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class UpdatePipelineManagementConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdatePipelineManagementConfigResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdatePipelineManagementConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdatePipelinesRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        trigger: bool = None,
    ):
        self.client_token = client_token
        self.trigger = trigger

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.trigger is not None:
            result['trigger'] = self.trigger
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('trigger') is not None:
            self.trigger = m.get('trigger')
        return self


class UpdatePipelinesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class UpdatePipelinesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdatePipelinesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdatePipelinesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdatePrivateNetworkWhiteIpsRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        modify_mode: str = None,
    ):
        self.client_token = client_token
        self.modify_mode = modify_mode

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.modify_mode is not None:
            result['modifyMode'] = self.modify_mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('modifyMode') is not None:
            self.modify_mode = m.get('modifyMode')
        return self


class UpdatePrivateNetworkWhiteIpsResponseBodyResult(TeaModel):
    def __init__(
        self,
        private_network_ip_white_list: List[str] = None,
    ):
        self.private_network_ip_white_list = private_network_ip_white_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.private_network_ip_white_list is not None:
            result['privateNetworkIpWhiteList'] = self.private_network_ip_white_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('privateNetworkIpWhiteList') is not None:
            self.private_network_ip_white_list = m.get('privateNetworkIpWhiteList')
        return self


class UpdatePrivateNetworkWhiteIpsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: UpdatePrivateNetworkWhiteIpsResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = UpdatePrivateNetworkWhiteIpsResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class UpdatePrivateNetworkWhiteIpsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdatePrivateNetworkWhiteIpsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdatePrivateNetworkWhiteIpsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdatePublicNetworkRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
    ):
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        return self


class UpdatePublicNetworkResponseBodyResult(TeaModel):
    def __init__(
        self,
        enable_public: bool = None,
    ):
        self.enable_public = enable_public

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_public is not None:
            result['enablePublic'] = self.enable_public
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enablePublic') is not None:
            self.enable_public = m.get('enablePublic')
        return self


class UpdatePublicNetworkResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: UpdatePublicNetworkResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = UpdatePublicNetworkResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class UpdatePublicNetworkResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdatePublicNetworkResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdatePublicNetworkResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdatePublicWhiteIpsRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        modify_mode: str = None,
    ):
        self.client_token = client_token
        self.modify_mode = modify_mode

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.modify_mode is not None:
            result['modifyMode'] = self.modify_mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('modifyMode') is not None:
            self.modify_mode = m.get('modifyMode')
        return self


class UpdatePublicWhiteIpsResponseBodyResult(TeaModel):
    def __init__(
        self,
        public_ip_whitelist: List[str] = None,
    ):
        self.public_ip_whitelist = public_ip_whitelist

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.public_ip_whitelist is not None:
            result['publicIpWhitelist'] = self.public_ip_whitelist
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('publicIpWhitelist') is not None:
            self.public_ip_whitelist = m.get('publicIpWhitelist')
        return self


class UpdatePublicWhiteIpsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: UpdatePublicWhiteIpsResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = UpdatePublicWhiteIpsResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class UpdatePublicWhiteIpsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdatePublicWhiteIpsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdatePublicWhiteIpsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateReadWritePolicyRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
    ):
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class UpdateReadWritePolicyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class UpdateReadWritePolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateReadWritePolicyResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateReadWritePolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateSnapshotSettingResponseBodyResult(TeaModel):
    def __init__(
        self,
        enable: bool = None,
        quartz_regex: str = None,
    ):
        self.enable = enable
        self.quartz_regex = quartz_regex

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable is not None:
            result['enable'] = self.enable
        if self.quartz_regex is not None:
            result['quartzRegex'] = self.quartz_regex
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enable') is not None:
            self.enable = m.get('enable')
        if m.get('quartzRegex') is not None:
            self.quartz_regex = m.get('quartzRegex')
        return self


class UpdateSnapshotSettingResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: UpdateSnapshotSettingResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = UpdateSnapshotSettingResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class UpdateSnapshotSettingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateSnapshotSettingResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateSnapshotSettingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateSynonymsDictsRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
    ):
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        return self


class UpdateSynonymsDictsResponseBodyResult(TeaModel):
    def __init__(
        self,
        file_size: int = None,
        name: str = None,
        source_type: str = None,
        type: str = None,
    ):
        self.file_size = file_size
        self.name = name
        self.source_type = source_type
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_size is not None:
            result['fileSize'] = self.file_size
        if self.name is not None:
            result['name'] = self.name
        if self.source_type is not None:
            result['sourceType'] = self.source_type
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fileSize') is not None:
            self.file_size = m.get('fileSize')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class UpdateSynonymsDictsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[UpdateSynonymsDictsResponseBodyResult] = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = UpdateSynonymsDictsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class UpdateSynonymsDictsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateSynonymsDictsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateSynonymsDictsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateTemplateRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
    ):
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class UpdateTemplateResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class UpdateTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateTemplateResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateWhiteIpsRequestWhiteIpGroup(TeaModel):
    def __init__(
        self,
        group_name: str = None,
        ips: List[str] = None,
        white_ip_type: str = None,
    ):
        self.group_name = group_name
        self.ips = ips
        self.white_ip_type = white_ip_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_name is not None:
            result['groupName'] = self.group_name
        if self.ips is not None:
            result['ips'] = self.ips
        if self.white_ip_type is not None:
            result['whiteIpType'] = self.white_ip_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('groupName') is not None:
            self.group_name = m.get('groupName')
        if m.get('ips') is not None:
            self.ips = m.get('ips')
        if m.get('whiteIpType') is not None:
            self.white_ip_type = m.get('whiteIpType')
        return self


class UpdateWhiteIpsRequest(TeaModel):
    def __init__(
        self,
        es_ipwhitelist: List[str] = None,
        white_ip_group: UpdateWhiteIpsRequestWhiteIpGroup = None,
        client_token: str = None,
        modify_mode: str = None,
    ):
        self.es_ipwhitelist = es_ipwhitelist
        self.white_ip_group = white_ip_group
        self.client_token = client_token
        self.modify_mode = modify_mode

    def validate(self):
        if self.white_ip_group:
            self.white_ip_group.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.es_ipwhitelist is not None:
            result['esIPWhitelist'] = self.es_ipwhitelist
        if self.white_ip_group is not None:
            result['whiteIpGroup'] = self.white_ip_group.to_map()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.modify_mode is not None:
            result['modifyMode'] = self.modify_mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('esIPWhitelist') is not None:
            self.es_ipwhitelist = m.get('esIPWhitelist')
        if m.get('whiteIpGroup') is not None:
            temp_model = UpdateWhiteIpsRequestWhiteIpGroup()
            self.white_ip_group = temp_model.from_map(m['whiteIpGroup'])
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('modifyMode') is not None:
            self.modify_mode = m.get('modifyMode')
        return self


class UpdateWhiteIpsResponseBodyResultNetworkConfigWhiteIpGroupList(TeaModel):
    def __init__(
        self,
        group_name: str = None,
        ips: List[str] = None,
        white_ip_type: str = None,
    ):
        self.group_name = group_name
        self.ips = ips
        self.white_ip_type = white_ip_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_name is not None:
            result['groupName'] = self.group_name
        if self.ips is not None:
            result['ips'] = self.ips
        if self.white_ip_type is not None:
            result['whiteIpType'] = self.white_ip_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('groupName') is not None:
            self.group_name = m.get('groupName')
        if m.get('ips') is not None:
            self.ips = m.get('ips')
        if m.get('whiteIpType') is not None:
            self.white_ip_type = m.get('whiteIpType')
        return self


class UpdateWhiteIpsResponseBodyResultNetworkConfig(TeaModel):
    def __init__(
        self,
        white_ip_group_list: List[UpdateWhiteIpsResponseBodyResultNetworkConfigWhiteIpGroupList] = None,
    ):
        self.white_ip_group_list = white_ip_group_list

    def validate(self):
        if self.white_ip_group_list:
            for k in self.white_ip_group_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['whiteIpGroupList'] = []
        if self.white_ip_group_list is not None:
            for k in self.white_ip_group_list:
                result['whiteIpGroupList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.white_ip_group_list = []
        if m.get('whiteIpGroupList') is not None:
            for k in m.get('whiteIpGroupList'):
                temp_model = UpdateWhiteIpsResponseBodyResultNetworkConfigWhiteIpGroupList()
                self.white_ip_group_list.append(temp_model.from_map(k))
        return self


class UpdateWhiteIpsResponseBodyResult(TeaModel):
    def __init__(
        self,
        es_ipwhitelist: List[str] = None,
        network_config: UpdateWhiteIpsResponseBodyResultNetworkConfig = None,
    ):
        self.es_ipwhitelist = es_ipwhitelist
        self.network_config = network_config

    def validate(self):
        if self.network_config:
            self.network_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.es_ipwhitelist is not None:
            result['esIPWhitelist'] = self.es_ipwhitelist
        if self.network_config is not None:
            result['networkConfig'] = self.network_config.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('esIPWhitelist') is not None:
            self.es_ipwhitelist = m.get('esIPWhitelist')
        if m.get('networkConfig') is not None:
            temp_model = UpdateWhiteIpsResponseBodyResultNetworkConfig()
            self.network_config = temp_model.from_map(m['networkConfig'])
        return self


class UpdateWhiteIpsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: UpdateWhiteIpsResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = UpdateWhiteIpsResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class UpdateWhiteIpsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateWhiteIpsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateWhiteIpsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateXpackMonitorConfigRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
    ):
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class UpdateXpackMonitorConfigResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class UpdateXpackMonitorConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateXpackMonitorConfigResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateXpackMonitorConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpgradeEngineVersionRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        type: str = None,
        version: str = None,
    ):
        self.client_token = client_token
        self.dry_run = dry_run
        self.type = type
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.dry_run is not None:
            result['dryRun'] = self.dry_run
        if self.type is not None:
            result['type'] = self.type
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class UpgradeEngineVersionResponseBodyResultValidateResult(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_msg: str = None,
        error_type: str = None,
    ):
        self.error_code = error_code
        self.error_msg = error_msg
        self.error_type = error_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg
        if self.error_type is not None:
            result['errorType'] = self.error_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')
        if m.get('errorType') is not None:
            self.error_type = m.get('errorType')
        return self


class UpgradeEngineVersionResponseBodyResult(TeaModel):
    def __init__(
        self,
        status: str = None,
        validate_result: UpgradeEngineVersionResponseBodyResultValidateResult = None,
        validate_type: str = None,
    ):
        self.status = status
        self.validate_result = validate_result
        self.validate_type = validate_type

    def validate(self):
        if self.validate_result:
            self.validate_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['status'] = self.status
        if self.validate_result is not None:
            result['validateResult'] = self.validate_result.to_map()
        if self.validate_type is not None:
            result['validateType'] = self.validate_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('validateResult') is not None:
            temp_model = UpgradeEngineVersionResponseBodyResultValidateResult()
            self.validate_result = temp_model.from_map(m['validateResult'])
        if m.get('validateType') is not None:
            self.validate_type = m.get('validateType')
        return self


class UpgradeEngineVersionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: UpgradeEngineVersionResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = UpgradeEngineVersionResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class UpgradeEngineVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpgradeEngineVersionResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpgradeEngineVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ValidateConnectionRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
    ):
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class ValidateConnectionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class ValidateConnectionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ValidateConnectionResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ValidateConnectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ValidateShrinkNodesRequestBody(TeaModel):
    def __init__(
        self,
        host: str = None,
        port: int = None,
        zone_id: str = None,
    ):
        self.host = host
        self.port = port
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host is not None:
            result['host'] = self.host
        if self.port is not None:
            result['port'] = self.port
        if self.zone_id is not None:
            result['zoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('host') is not None:
            self.host = m.get('host')
        if m.get('port') is not None:
            self.port = m.get('port')
        if m.get('zoneId') is not None:
            self.zone_id = m.get('zoneId')
        return self


class ValidateShrinkNodesRequest(TeaModel):
    def __init__(
        self,
        body: List[ValidateShrinkNodesRequestBody] = None,
        ignore_status: bool = None,
        node_type: str = None,
    ):
        self.body = body
        self.ignore_status = ignore_status
        self.node_type = node_type

    def validate(self):
        if self.body:
            for k in self.body:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['body'] = []
        if self.body is not None:
            for k in self.body:
                result['body'].append(k.to_map() if k else None)
        if self.ignore_status is not None:
            result['ignoreStatus'] = self.ignore_status
        if self.node_type is not None:
            result['nodeType'] = self.node_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.body = []
        if m.get('body') is not None:
            for k in m.get('body'):
                temp_model = ValidateShrinkNodesRequestBody()
                self.body.append(temp_model.from_map(k))
        if m.get('ignoreStatus') is not None:
            self.ignore_status = m.get('ignoreStatus')
        if m.get('nodeType') is not None:
            self.node_type = m.get('nodeType')
        return self


class ValidateShrinkNodesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class ValidateShrinkNodesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ValidateShrinkNodesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ValidateShrinkNodesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ValidateSlrPermissionRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        rolename: str = None,
    ):
        self.client_token = client_token
        self.rolename = rolename

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.rolename is not None:
            result['rolename'] = self.rolename
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('rolename') is not None:
            self.rolename = m.get('rolename')
        return self


class ValidateSlrPermissionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class ValidateSlrPermissionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ValidateSlrPermissionResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ValidateSlrPermissionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ValidateTransferableNodesRequestBody(TeaModel):
    def __init__(
        self,
        host: str = None,
        port: int = None,
        zone_id: str = None,
    ):
        self.host = host
        self.port = port
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host is not None:
            result['host'] = self.host
        if self.port is not None:
            result['port'] = self.port
        if self.zone_id is not None:
            result['zoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('host') is not None:
            self.host = m.get('host')
        if m.get('port') is not None:
            self.port = m.get('port')
        if m.get('zoneId') is not None:
            self.zone_id = m.get('zoneId')
        return self


class ValidateTransferableNodesRequest(TeaModel):
    def __init__(
        self,
        body: List[ValidateTransferableNodesRequestBody] = None,
        node_type: str = None,
    ):
        self.body = body
        self.node_type = node_type

    def validate(self):
        if self.body:
            for k in self.body:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['body'] = []
        if self.body is not None:
            for k in self.body:
                result['body'].append(k.to_map() if k else None)
        if self.node_type is not None:
            result['nodeType'] = self.node_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.body = []
        if m.get('body') is not None:
            for k in m.get('body'):
                temp_model = ValidateTransferableNodesRequestBody()
                self.body.append(temp_model.from_map(k))
        if m.get('nodeType') is not None:
            self.node_type = m.get('nodeType')
        return self


class ValidateTransferableNodesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class ValidateTransferableNodesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ValidateTransferableNodesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ValidateTransferableNodesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateInstanceRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
    ):
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        return self


class CreateInstanceResponseBodyResult(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        return self


class CreateInstanceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: CreateInstanceResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = CreateInstanceResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class CreateInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateInstanceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


