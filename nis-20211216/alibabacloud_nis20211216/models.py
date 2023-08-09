# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class CreateAndAnalyzeNetworkPathRequest(TeaModel):
    def __init__(
        self,
        protocol: str = None,
        region_id: str = None,
        source_id: str = None,
        source_ip_address: str = None,
        source_port: int = None,
        source_type: str = None,
        target_id: str = None,
        target_ip_address: str = None,
        target_port: int = None,
        target_type: str = None,
    ):
        # The protocol type. Valid values:
        # 
        # *   **tcp**: Transmission Control Protocol (TCP)
        # *   **udp**: User Datagram Protocol (UDP)
        # *   **icmp**: Internet Control Message Protocol (ICMP)
        self.protocol = protocol
        # The ID of the region for which you want to initiate a task for analyzing network reachability.
        self.region_id = region_id
        # The ID of the source resource.
        self.source_id = source_id
        # The source IP address.
        self.source_ip_address = source_ip_address
        # The source port.
        self.source_port = source_port
        # The type of the source resource. Valid values:
        # 
        # *   **ecs**: the Elastic Compute Service (ECS) instance
        # *   **internetIp**: the public IP address
        # *   **vsw**: the vSwitch
        # *   **vpn**: the VPN gateway
        # *   **vbr**: the virtual border router (VBR)
        self.source_type = source_type
        # The ID of the destination resource.
        self.target_id = target_id
        # The destination IP address.
        self.target_ip_address = target_ip_address
        # The destination port.
        self.target_port = target_port
        # The type of the destination resource. Valid values:
        # 
        # *   **ecs**: the ECS instance
        # *   **internetIp**: the public IP address
        # *   **vsw**: the vSwitch
        # *   **vpn**: the VPN gateway
        # *   **vbr**: the VBR
        # *   **clb**: the Classic Load Balancer (CLB) instance
        self.target_type = target_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.source_id is not None:
            result['SourceId'] = self.source_id
        if self.source_ip_address is not None:
            result['SourceIpAddress'] = self.source_ip_address
        if self.source_port is not None:
            result['SourcePort'] = self.source_port
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.target_id is not None:
            result['TargetId'] = self.target_id
        if self.target_ip_address is not None:
            result['TargetIpAddress'] = self.target_ip_address
        if self.target_port is not None:
            result['TargetPort'] = self.target_port
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')
        if m.get('SourceIpAddress') is not None:
            self.source_ip_address = m.get('SourceIpAddress')
        if m.get('SourcePort') is not None:
            self.source_port = m.get('SourcePort')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('TargetId') is not None:
            self.target_id = m.get('TargetId')
        if m.get('TargetIpAddress') is not None:
            self.target_ip_address = m.get('TargetIpAddress')
        if m.get('TargetPort') is not None:
            self.target_port = m.get('TargetPort')
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        return self


class CreateAndAnalyzeNetworkPathResponseBody(TeaModel):
    def __init__(
        self,
        network_reachable_analysis_id: str = None,
        protocol: str = None,
        request_id: str = None,
        source_id: str = None,
        source_ip_address: str = None,
        source_port: str = None,
        source_type: str = None,
        target_id: str = None,
        target_ip_address: str = None,
        target_port: str = None,
        target_type: str = None,
    ):
        # The ID of the task for analyzing network reachability that you initiated.
        self.network_reachable_analysis_id = network_reachable_analysis_id
        # The protocol type.
        self.protocol = protocol
        # The request ID.
        self.request_id = request_id
        # The ID of the source resource.
        self.source_id = source_id
        # The source IP address.
        self.source_ip_address = source_ip_address
        # The source port.
        self.source_port = source_port
        # The type of the source resource.
        self.source_type = source_type
        # The ID of the destination resource.
        self.target_id = target_id
        # The destination IP address.
        self.target_ip_address = target_ip_address
        # The destination port.
        self.target_port = target_port
        # The type of the destination resource.
        self.target_type = target_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.network_reachable_analysis_id is not None:
            result['NetworkReachableAnalysisId'] = self.network_reachable_analysis_id
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.source_id is not None:
            result['SourceId'] = self.source_id
        if self.source_ip_address is not None:
            result['SourceIpAddress'] = self.source_ip_address
        if self.source_port is not None:
            result['SourcePort'] = self.source_port
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.target_id is not None:
            result['TargetId'] = self.target_id
        if self.target_ip_address is not None:
            result['TargetIpAddress'] = self.target_ip_address
        if self.target_port is not None:
            result['TargetPort'] = self.target_port
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NetworkReachableAnalysisId') is not None:
            self.network_reachable_analysis_id = m.get('NetworkReachableAnalysisId')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')
        if m.get('SourceIpAddress') is not None:
            self.source_ip_address = m.get('SourceIpAddress')
        if m.get('SourcePort') is not None:
            self.source_port = m.get('SourcePort')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('TargetId') is not None:
            self.target_id = m.get('TargetId')
        if m.get('TargetIpAddress') is not None:
            self.target_ip_address = m.get('TargetIpAddress')
        if m.get('TargetPort') is not None:
            self.target_port = m.get('TargetPort')
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        return self


class CreateAndAnalyzeNetworkPathResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateAndAnalyzeNetworkPathResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateAndAnalyzeNetworkPathResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateNetworkPathRequestTag(TeaModel):
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


class CreateNetworkPathRequest(TeaModel):
    def __init__(
        self,
        network_path_description: str = None,
        network_path_name: str = None,
        protocol: str = None,
        region_id: str = None,
        source_id: str = None,
        source_ip_address: str = None,
        source_port: int = None,
        source_type: str = None,
        tag: List[CreateNetworkPathRequestTag] = None,
        target_id: str = None,
        target_ip_address: str = None,
        target_port: int = None,
        target_type: str = None,
    ):
        # The description of the network path.
        self.network_path_description = network_path_description
        # The name of the network path.
        self.network_path_name = network_path_name
        # The protocol type. Valid values:
        # 
        # *   **tcp**: Transmission Control Protocol (TCP)
        # *   **udp**: User Datagram Protocol (UDP)
        # *   **icmp**: Internet Control Message Protocol (ICMP)
        self.protocol = protocol
        # The region ID of the network path that you want to create.
        self.region_id = region_id
        # The ID of the source resource.
        self.source_id = source_id
        # The source IP address.
        self.source_ip_address = source_ip_address
        # The source port.
        self.source_port = source_port
        # The type of the source resource. Valid values:
        # 
        # *   **ecs**: the Elastic Compute Service (ECS) instance
        # *   **internetIp**: the public IP address
        # *   **vsw**: the vSwitch
        # *   **vpn**: the VPN gateway
        # *   **vbr**: the virtual border router (VBR)
        self.source_type = source_type
        self.tag = tag
        # The ID of the destination resource.
        self.target_id = target_id
        # The destination IP address.
        self.target_ip_address = target_ip_address
        # The destination port.
        self.target_port = target_port
        # The type of the destination resource. Valid values:
        # 
        # *   **ecs**: the ECS instance
        # *   **internetIp**: the public IP address
        # *   **vsw**: the vSwitch
        # *   **vpn**: the VPN gateway
        # *   **vbr**: the VBR
        # *   **clb**: the Classic Load Balancer (CLB) instance
        self.target_type = target_type

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.network_path_description is not None:
            result['NetworkPathDescription'] = self.network_path_description
        if self.network_path_name is not None:
            result['NetworkPathName'] = self.network_path_name
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.source_id is not None:
            result['SourceId'] = self.source_id
        if self.source_ip_address is not None:
            result['SourceIpAddress'] = self.source_ip_address
        if self.source_port is not None:
            result['SourcePort'] = self.source_port
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.target_id is not None:
            result['TargetId'] = self.target_id
        if self.target_ip_address is not None:
            result['TargetIpAddress'] = self.target_ip_address
        if self.target_port is not None:
            result['TargetPort'] = self.target_port
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NetworkPathDescription') is not None:
            self.network_path_description = m.get('NetworkPathDescription')
        if m.get('NetworkPathName') is not None:
            self.network_path_name = m.get('NetworkPathName')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')
        if m.get('SourceIpAddress') is not None:
            self.source_ip_address = m.get('SourceIpAddress')
        if m.get('SourcePort') is not None:
            self.source_port = m.get('SourcePort')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = CreateNetworkPathRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('TargetId') is not None:
            self.target_id = m.get('TargetId')
        if m.get('TargetIpAddress') is not None:
            self.target_ip_address = m.get('TargetIpAddress')
        if m.get('TargetPort') is not None:
            self.target_port = m.get('TargetPort')
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        return self


class CreateNetworkPathResponseBody(TeaModel):
    def __init__(
        self,
        network_path_id: str = None,
        request_id: str = None,
    ):
        # The ID of the network path.
        self.network_path_id = network_path_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.network_path_id is not None:
            result['NetworkPathId'] = self.network_path_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NetworkPathId') is not None:
            self.network_path_id = m.get('NetworkPathId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateNetworkPathResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateNetworkPathResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateNetworkPathResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateNetworkReachableAnalysisRequestTag(TeaModel):
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


class CreateNetworkReachableAnalysisRequest(TeaModel):
    def __init__(
        self,
        network_path_id: str = None,
        region_id: str = None,
        tag: List[CreateNetworkReachableAnalysisRequestTag] = None,
    ):
        # The ID of the network path. You can call the **CreateNetworkPath** operation to obtain the ID of the network path.
        self.network_path_id = network_path_id
        # The ID of the region for which you want to create a task for analyzing network reachability.
        self.region_id = region_id
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.network_path_id is not None:
            result['NetworkPathId'] = self.network_path_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NetworkPathId') is not None:
            self.network_path_id = m.get('NetworkPathId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = CreateNetworkReachableAnalysisRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class CreateNetworkReachableAnalysisResponseBody(TeaModel):
    def __init__(
        self,
        network_reachable_analysis_id: str = None,
        request_id: str = None,
    ):
        # The ID of the task for analyzing network reachability.
        self.network_reachable_analysis_id = network_reachable_analysis_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.network_reachable_analysis_id is not None:
            result['NetworkReachableAnalysisId'] = self.network_reachable_analysis_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NetworkReachableAnalysisId') is not None:
            self.network_reachable_analysis_id = m.get('NetworkReachableAnalysisId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateNetworkReachableAnalysisResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateNetworkReachableAnalysisResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateNetworkReachableAnalysisResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteNetworkPathRequest(TeaModel):
    def __init__(
        self,
        network_path_ids: List[str] = None,
        region_id: str = None,
    ):
        # The IDs of network paths.
        self.network_path_ids = network_path_ids
        # The region ID of the network path that you want to delete.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.network_path_ids is not None:
            result['NetworkPathIds'] = self.network_path_ids
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NetworkPathIds') is not None:
            self.network_path_ids = m.get('NetworkPathIds')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteNetworkPathShrinkRequest(TeaModel):
    def __init__(
        self,
        network_path_ids_shrink: str = None,
        region_id: str = None,
    ):
        # The IDs of network paths.
        self.network_path_ids_shrink = network_path_ids_shrink
        # The region ID of the network path that you want to delete.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.network_path_ids_shrink is not None:
            result['NetworkPathIds'] = self.network_path_ids_shrink
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NetworkPathIds') is not None:
            self.network_path_ids_shrink = m.get('NetworkPathIds')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteNetworkPathResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
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


class DeleteNetworkPathResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteNetworkPathResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteNetworkPathResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteNetworkReachableAnalysisRequest(TeaModel):
    def __init__(
        self,
        network_reachable_analysis_ids: List[str] = None,
        region_id: str = None,
    ):
        # The IDs of the tasks for analyzing network reachability.
        self.network_reachable_analysis_ids = network_reachable_analysis_ids
        # The ID of the region for which you want to delete a task for analyzing network reachability.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.network_reachable_analysis_ids is not None:
            result['NetworkReachableAnalysisIds'] = self.network_reachable_analysis_ids
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NetworkReachableAnalysisIds') is not None:
            self.network_reachable_analysis_ids = m.get('NetworkReachableAnalysisIds')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteNetworkReachableAnalysisShrinkRequest(TeaModel):
    def __init__(
        self,
        network_reachable_analysis_ids_shrink: str = None,
        region_id: str = None,
    ):
        # The IDs of the tasks for analyzing network reachability.
        self.network_reachable_analysis_ids_shrink = network_reachable_analysis_ids_shrink
        # The ID of the region for which you want to delete a task for analyzing network reachability.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.network_reachable_analysis_ids_shrink is not None:
            result['NetworkReachableAnalysisIds'] = self.network_reachable_analysis_ids_shrink
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NetworkReachableAnalysisIds') is not None:
            self.network_reachable_analysis_ids_shrink = m.get('NetworkReachableAnalysisIds')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteNetworkReachableAnalysisResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
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


class DeleteNetworkReachableAnalysisResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteNetworkReachableAnalysisResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteNetworkReachableAnalysisResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetInternetTupleRequest(TeaModel):
    def __init__(
        self,
        account_ids: List[str] = None,
        begin_time: int = None,
        cloud_ip: str = None,
        cloud_isp: str = None,
        cloud_port: str = None,
        direction: str = None,
        end_time: int = None,
        instance_id: str = None,
        instance_list: List[str] = None,
        order_by: str = None,
        other_city: str = None,
        other_country: str = None,
        other_ip: str = None,
        other_isp: str = None,
        other_port: str = None,
        protocol: str = None,
        region_id: str = None,
        sort: str = None,
        top_n: int = None,
        tuple_type: int = None,
        use_multi_account: bool = None,
    ):
        self.account_ids = account_ids
        self.begin_time = begin_time
        self.cloud_ip = cloud_ip
        self.cloud_isp = cloud_isp
        self.cloud_port = cloud_port
        self.direction = direction
        self.end_time = end_time
        self.instance_id = instance_id
        self.instance_list = instance_list
        self.order_by = order_by
        self.other_city = other_city
        self.other_country = other_country
        self.other_ip = other_ip
        self.other_isp = other_isp
        self.other_port = other_port
        self.protocol = protocol
        self.region_id = region_id
        self.sort = sort
        self.top_n = top_n
        self.tuple_type = tuple_type
        self.use_multi_account = use_multi_account

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_ids is not None:
            result['AccountIds'] = self.account_ids
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.cloud_ip is not None:
            result['CloudIp'] = self.cloud_ip
        if self.cloud_isp is not None:
            result['CloudIsp'] = self.cloud_isp
        if self.cloud_port is not None:
            result['CloudPort'] = self.cloud_port
        if self.direction is not None:
            result['Direction'] = self.direction
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_list is not None:
            result['InstanceList'] = self.instance_list
        if self.order_by is not None:
            result['OrderBy'] = self.order_by
        if self.other_city is not None:
            result['OtherCity'] = self.other_city
        if self.other_country is not None:
            result['OtherCountry'] = self.other_country
        if self.other_ip is not None:
            result['OtherIp'] = self.other_ip
        if self.other_isp is not None:
            result['OtherIsp'] = self.other_isp
        if self.other_port is not None:
            result['OtherPort'] = self.other_port
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.sort is not None:
            result['Sort'] = self.sort
        if self.top_n is not None:
            result['TopN'] = self.top_n
        if self.tuple_type is not None:
            result['TupleType'] = self.tuple_type
        if self.use_multi_account is not None:
            result['UseMultiAccount'] = self.use_multi_account
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountIds') is not None:
            self.account_ids = m.get('AccountIds')
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('CloudIp') is not None:
            self.cloud_ip = m.get('CloudIp')
        if m.get('CloudIsp') is not None:
            self.cloud_isp = m.get('CloudIsp')
        if m.get('CloudPort') is not None:
            self.cloud_port = m.get('CloudPort')
        if m.get('Direction') is not None:
            self.direction = m.get('Direction')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceList') is not None:
            self.instance_list = m.get('InstanceList')
        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')
        if m.get('OtherCity') is not None:
            self.other_city = m.get('OtherCity')
        if m.get('OtherCountry') is not None:
            self.other_country = m.get('OtherCountry')
        if m.get('OtherIp') is not None:
            self.other_ip = m.get('OtherIp')
        if m.get('OtherIsp') is not None:
            self.other_isp = m.get('OtherIsp')
        if m.get('OtherPort') is not None:
            self.other_port = m.get('OtherPort')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Sort') is not None:
            self.sort = m.get('Sort')
        if m.get('TopN') is not None:
            self.top_n = m.get('TopN')
        if m.get('TupleType') is not None:
            self.tuple_type = m.get('TupleType')
        if m.get('UseMultiAccount') is not None:
            self.use_multi_account = m.get('UseMultiAccount')
        return self


class GetInternetTupleShrinkRequest(TeaModel):
    def __init__(
        self,
        account_ids: List[str] = None,
        begin_time: int = None,
        cloud_ip: str = None,
        cloud_isp: str = None,
        cloud_port: str = None,
        direction: str = None,
        end_time: int = None,
        instance_id: str = None,
        instance_list_shrink: str = None,
        order_by: str = None,
        other_city: str = None,
        other_country: str = None,
        other_ip: str = None,
        other_isp: str = None,
        other_port: str = None,
        protocol: str = None,
        region_id: str = None,
        sort: str = None,
        top_n: int = None,
        tuple_type: int = None,
        use_multi_account: bool = None,
    ):
        self.account_ids = account_ids
        self.begin_time = begin_time
        self.cloud_ip = cloud_ip
        self.cloud_isp = cloud_isp
        self.cloud_port = cloud_port
        self.direction = direction
        self.end_time = end_time
        self.instance_id = instance_id
        self.instance_list_shrink = instance_list_shrink
        self.order_by = order_by
        self.other_city = other_city
        self.other_country = other_country
        self.other_ip = other_ip
        self.other_isp = other_isp
        self.other_port = other_port
        self.protocol = protocol
        self.region_id = region_id
        self.sort = sort
        self.top_n = top_n
        self.tuple_type = tuple_type
        self.use_multi_account = use_multi_account

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_ids is not None:
            result['AccountIds'] = self.account_ids
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.cloud_ip is not None:
            result['CloudIp'] = self.cloud_ip
        if self.cloud_isp is not None:
            result['CloudIsp'] = self.cloud_isp
        if self.cloud_port is not None:
            result['CloudPort'] = self.cloud_port
        if self.direction is not None:
            result['Direction'] = self.direction
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_list_shrink is not None:
            result['InstanceList'] = self.instance_list_shrink
        if self.order_by is not None:
            result['OrderBy'] = self.order_by
        if self.other_city is not None:
            result['OtherCity'] = self.other_city
        if self.other_country is not None:
            result['OtherCountry'] = self.other_country
        if self.other_ip is not None:
            result['OtherIp'] = self.other_ip
        if self.other_isp is not None:
            result['OtherIsp'] = self.other_isp
        if self.other_port is not None:
            result['OtherPort'] = self.other_port
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.sort is not None:
            result['Sort'] = self.sort
        if self.top_n is not None:
            result['TopN'] = self.top_n
        if self.tuple_type is not None:
            result['TupleType'] = self.tuple_type
        if self.use_multi_account is not None:
            result['UseMultiAccount'] = self.use_multi_account
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountIds') is not None:
            self.account_ids = m.get('AccountIds')
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('CloudIp') is not None:
            self.cloud_ip = m.get('CloudIp')
        if m.get('CloudIsp') is not None:
            self.cloud_isp = m.get('CloudIsp')
        if m.get('CloudPort') is not None:
            self.cloud_port = m.get('CloudPort')
        if m.get('Direction') is not None:
            self.direction = m.get('Direction')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceList') is not None:
            self.instance_list_shrink = m.get('InstanceList')
        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')
        if m.get('OtherCity') is not None:
            self.other_city = m.get('OtherCity')
        if m.get('OtherCountry') is not None:
            self.other_country = m.get('OtherCountry')
        if m.get('OtherIp') is not None:
            self.other_ip = m.get('OtherIp')
        if m.get('OtherIsp') is not None:
            self.other_isp = m.get('OtherIsp')
        if m.get('OtherPort') is not None:
            self.other_port = m.get('OtherPort')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Sort') is not None:
            self.sort = m.get('Sort')
        if m.get('TopN') is not None:
            self.top_n = m.get('TopN')
        if m.get('TupleType') is not None:
            self.tuple_type = m.get('TupleType')
        if m.get('UseMultiAccount') is not None:
            self.use_multi_account = m.get('UseMultiAccount')
        return self


class GetInternetTupleResponseBodyData(TeaModel):
    def __init__(
        self,
        access_region: str = None,
        begin_time: str = None,
        byte_count: float = None,
        cloud_city: str = None,
        cloud_country: str = None,
        cloud_ip: str = None,
        cloud_isp: str = None,
        cloud_port: str = None,
        cloud_product: str = None,
        cloud_province: str = None,
        direction: str = None,
        in_byte_count: float = None,
        in_out_order_count: float = None,
        in_packet_count: float = None,
        in_retran_count: float = None,
        instance_id: str = None,
        other_city: str = None,
        other_country: str = None,
        other_ip: str = None,
        other_isp: str = None,
        other_port: str = None,
        other_product: str = None,
        other_province: str = None,
        out_byte_count: float = None,
        out_order_count: float = None,
        out_out_order_count: float = None,
        out_packet_count: float = None,
        out_retran_count: float = None,
        packet_count: float = None,
        protocol: str = None,
        retran_count: float = None,
        rtt: float = None,
    ):
        self.access_region = access_region
        self.begin_time = begin_time
        self.byte_count = byte_count
        self.cloud_city = cloud_city
        self.cloud_country = cloud_country
        self.cloud_ip = cloud_ip
        self.cloud_isp = cloud_isp
        self.cloud_port = cloud_port
        self.cloud_product = cloud_product
        self.cloud_province = cloud_province
        self.direction = direction
        self.in_byte_count = in_byte_count
        self.in_out_order_count = in_out_order_count
        self.in_packet_count = in_packet_count
        self.in_retran_count = in_retran_count
        self.instance_id = instance_id
        self.other_city = other_city
        self.other_country = other_country
        self.other_ip = other_ip
        self.other_isp = other_isp
        self.other_port = other_port
        self.other_product = other_product
        self.other_province = other_province
        self.out_byte_count = out_byte_count
        self.out_order_count = out_order_count
        self.out_out_order_count = out_out_order_count
        self.out_packet_count = out_packet_count
        self.out_retran_count = out_retran_count
        self.packet_count = packet_count
        self.protocol = protocol
        self.retran_count = retran_count
        self.rtt = rtt

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_region is not None:
            result['AccessRegion'] = self.access_region
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.byte_count is not None:
            result['ByteCount'] = self.byte_count
        if self.cloud_city is not None:
            result['CloudCity'] = self.cloud_city
        if self.cloud_country is not None:
            result['CloudCountry'] = self.cloud_country
        if self.cloud_ip is not None:
            result['CloudIp'] = self.cloud_ip
        if self.cloud_isp is not None:
            result['CloudIsp'] = self.cloud_isp
        if self.cloud_port is not None:
            result['CloudPort'] = self.cloud_port
        if self.cloud_product is not None:
            result['CloudProduct'] = self.cloud_product
        if self.cloud_province is not None:
            result['CloudProvince'] = self.cloud_province
        if self.direction is not None:
            result['Direction'] = self.direction
        if self.in_byte_count is not None:
            result['InByteCount'] = self.in_byte_count
        if self.in_out_order_count is not None:
            result['InOutOrderCount'] = self.in_out_order_count
        if self.in_packet_count is not None:
            result['InPacketCount'] = self.in_packet_count
        if self.in_retran_count is not None:
            result['InRetranCount'] = self.in_retran_count
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.other_city is not None:
            result['OtherCity'] = self.other_city
        if self.other_country is not None:
            result['OtherCountry'] = self.other_country
        if self.other_ip is not None:
            result['OtherIp'] = self.other_ip
        if self.other_isp is not None:
            result['OtherIsp'] = self.other_isp
        if self.other_port is not None:
            result['OtherPort'] = self.other_port
        if self.other_product is not None:
            result['OtherProduct'] = self.other_product
        if self.other_province is not None:
            result['OtherProvince'] = self.other_province
        if self.out_byte_count is not None:
            result['OutByteCount'] = self.out_byte_count
        if self.out_order_count is not None:
            result['OutOrderCount'] = self.out_order_count
        if self.out_out_order_count is not None:
            result['OutOutOrderCount'] = self.out_out_order_count
        if self.out_packet_count is not None:
            result['OutPacketCount'] = self.out_packet_count
        if self.out_retran_count is not None:
            result['OutRetranCount'] = self.out_retran_count
        if self.packet_count is not None:
            result['PacketCount'] = self.packet_count
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.retran_count is not None:
            result['RetranCount'] = self.retran_count
        if self.rtt is not None:
            result['Rtt'] = self.rtt
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessRegion') is not None:
            self.access_region = m.get('AccessRegion')
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('ByteCount') is not None:
            self.byte_count = m.get('ByteCount')
        if m.get('CloudCity') is not None:
            self.cloud_city = m.get('CloudCity')
        if m.get('CloudCountry') is not None:
            self.cloud_country = m.get('CloudCountry')
        if m.get('CloudIp') is not None:
            self.cloud_ip = m.get('CloudIp')
        if m.get('CloudIsp') is not None:
            self.cloud_isp = m.get('CloudIsp')
        if m.get('CloudPort') is not None:
            self.cloud_port = m.get('CloudPort')
        if m.get('CloudProduct') is not None:
            self.cloud_product = m.get('CloudProduct')
        if m.get('CloudProvince') is not None:
            self.cloud_province = m.get('CloudProvince')
        if m.get('Direction') is not None:
            self.direction = m.get('Direction')
        if m.get('InByteCount') is not None:
            self.in_byte_count = m.get('InByteCount')
        if m.get('InOutOrderCount') is not None:
            self.in_out_order_count = m.get('InOutOrderCount')
        if m.get('InPacketCount') is not None:
            self.in_packet_count = m.get('InPacketCount')
        if m.get('InRetranCount') is not None:
            self.in_retran_count = m.get('InRetranCount')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OtherCity') is not None:
            self.other_city = m.get('OtherCity')
        if m.get('OtherCountry') is not None:
            self.other_country = m.get('OtherCountry')
        if m.get('OtherIp') is not None:
            self.other_ip = m.get('OtherIp')
        if m.get('OtherIsp') is not None:
            self.other_isp = m.get('OtherIsp')
        if m.get('OtherPort') is not None:
            self.other_port = m.get('OtherPort')
        if m.get('OtherProduct') is not None:
            self.other_product = m.get('OtherProduct')
        if m.get('OtherProvince') is not None:
            self.other_province = m.get('OtherProvince')
        if m.get('OutByteCount') is not None:
            self.out_byte_count = m.get('OutByteCount')
        if m.get('OutOrderCount') is not None:
            self.out_order_count = m.get('OutOrderCount')
        if m.get('OutOutOrderCount') is not None:
            self.out_out_order_count = m.get('OutOutOrderCount')
        if m.get('OutPacketCount') is not None:
            self.out_packet_count = m.get('OutPacketCount')
        if m.get('OutRetranCount') is not None:
            self.out_retran_count = m.get('OutRetranCount')
        if m.get('PacketCount') is not None:
            self.packet_count = m.get('PacketCount')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('RetranCount') is not None:
            self.retran_count = m.get('RetranCount')
        if m.get('Rtt') is not None:
            self.rtt = m.get('Rtt')
        return self


class GetInternetTupleResponseBody(TeaModel):
    def __init__(
        self,
        data: List[GetInternetTupleResponseBodyData] = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetInternetTupleResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetInternetTupleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetInternetTupleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetInternetTupleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetNatTopNRequest(TeaModel):
    def __init__(
        self,
        begin_time: int = None,
        end_time: int = None,
        ip: str = None,
        nat_gateway_id: str = None,
        order_by: str = None,
        region_id: str = None,
        top_n: int = None,
    ):
        # The beginning of the time range to query in milliseconds. If you do not specify **EndTime**, the point in time specified by **BeginTime** is queried.
        self.begin_time = begin_time
        # The end of the time range to query in milliseconds. The time range specified by **BeginTime** and **EndTime** cannot exceed **86400000** milliseconds (24 hours).
        self.end_time = end_time
        # Query ranking statistics for a specific IP address. If you specify this parameter, you do not need to specify **TopN** or **OrderBy**.
        self.ip = ip
        # The ID of the NAT gateway.
        self.nat_gateway_id = nat_gateway_id
        # The metric that is used for real-time SNAT performance ranking. Valid values:
        # 
        # *   **InBps**: inbound data transfer. Unit: bit/s.
        # *   **OutBps**: outbound data transfer. Unit: bit/s.
        # *   **InPps**: inbound packet forwarding rate. Unit: packets per second.
        # *   **OutPps**: outbound packet forwarding rate. Unit: packets per second.
        # *   **NewSessionPerSecond**: new connection creation rate. Unit: connections per second.
        # *   **ActiveSessionCount**: number of concurrent connections. Unit: connections.
        self.order_by = order_by
        # The ID of the region in which the NAT gateway is deployed.
        self.region_id = region_id
        # The number of entries to return for real-time SNAT performance ranking. Valid values: **1 to 100**. Default value: **10**.
        self.top_n = top_n

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.nat_gateway_id is not None:
            result['NatGatewayId'] = self.nat_gateway_id
        if self.order_by is not None:
            result['OrderBy'] = self.order_by
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.top_n is not None:
            result['TopN'] = self.top_n
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('NatGatewayId') is not None:
            self.nat_gateway_id = m.get('NatGatewayId')
        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TopN') is not None:
            self.top_n = m.get('TopN')
        return self


class GetNatTopNResponseBodyNatGatewayTopN(TeaModel):
    def __init__(
        self,
        active_session_count: float = None,
        in_bps: float = None,
        in_flow_per_minute: float = None,
        in_pps: float = None,
        ip: str = None,
        new_session_per_second: float = None,
        out_bps: float = None,
        out_flow_per_minute: float = None,
        out_pps: float = None,
    ):
        # The number of concurrent connections. Unit: connections.
        self.active_session_count = active_session_count
        # The inbound data transfer. Unit: bit/s.
        self.in_bps = in_bps
        # This field is reserved and not in use.
        self.in_flow_per_minute = in_flow_per_minute
        # The inbound packet forwarding rate. Unit: packets per second.
        self.in_pps = in_pps
        # The IP address.
        self.ip = ip
        # The new connection creation rate. Unit: connections per second.
        self.new_session_per_second = new_session_per_second
        # The outbound data transfer. Unit: bit/s.
        self.out_bps = out_bps
        # This field is reserved and not in use.
        self.out_flow_per_minute = out_flow_per_minute
        # The outbound packet forwarding rate. Unit: packets per second.
        self.out_pps = out_pps

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active_session_count is not None:
            result['ActiveSessionCount'] = self.active_session_count
        if self.in_bps is not None:
            result['InBps'] = self.in_bps
        if self.in_flow_per_minute is not None:
            result['InFlowPerMinute'] = self.in_flow_per_minute
        if self.in_pps is not None:
            result['InPps'] = self.in_pps
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.new_session_per_second is not None:
            result['NewSessionPerSecond'] = self.new_session_per_second
        if self.out_bps is not None:
            result['OutBps'] = self.out_bps
        if self.out_flow_per_minute is not None:
            result['OutFlowPerMinute'] = self.out_flow_per_minute
        if self.out_pps is not None:
            result['OutPps'] = self.out_pps
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActiveSessionCount') is not None:
            self.active_session_count = m.get('ActiveSessionCount')
        if m.get('InBps') is not None:
            self.in_bps = m.get('InBps')
        if m.get('InFlowPerMinute') is not None:
            self.in_flow_per_minute = m.get('InFlowPerMinute')
        if m.get('InPps') is not None:
            self.in_pps = m.get('InPps')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('NewSessionPerSecond') is not None:
            self.new_session_per_second = m.get('NewSessionPerSecond')
        if m.get('OutBps') is not None:
            self.out_bps = m.get('OutBps')
        if m.get('OutFlowPerMinute') is not None:
            self.out_flow_per_minute = m.get('OutFlowPerMinute')
        if m.get('OutPps') is not None:
            self.out_pps = m.get('OutPps')
        return self


class GetNatTopNResponseBody(TeaModel):
    def __init__(
        self,
        is_top_nopen: bool = None,
        nat_gateway_top_n: List[GetNatTopNResponseBodyNatGatewayTopN] = None,
        request_id: str = None,
    ):
        # Indicates whether Network Intelligence Service (NIS) is activated. The NatGatewayTopN parameter returns an empty array when NIS is not activated.
        # 
        # *   **true**: activated
        # *   **false**: not activated
        self.is_top_nopen = is_top_nopen
        # An array of statistics about real-time SNAT performance ranking.
        self.nat_gateway_top_n = nat_gateway_top_n
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.nat_gateway_top_n:
            for k in self.nat_gateway_top_n:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_top_nopen is not None:
            result['IsTopNOpen'] = self.is_top_nopen
        result['NatGatewayTopN'] = []
        if self.nat_gateway_top_n is not None:
            for k in self.nat_gateway_top_n:
                result['NatGatewayTopN'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsTopNOpen') is not None:
            self.is_top_nopen = m.get('IsTopNOpen')
        self.nat_gateway_top_n = []
        if m.get('NatGatewayTopN') is not None:
            for k in m.get('NatGatewayTopN'):
                temp_model = GetNatTopNResponseBodyNatGatewayTopN()
                self.nat_gateway_top_n.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetNatTopNResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetNatTopNResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetNatTopNResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetNetworkReachableAnalysisRequest(TeaModel):
    def __init__(
        self,
        network_reachable_analysis_id: str = None,
        region_id: str = None,
    ):
        # The ID of the task for analyzing network reachability. You can call the **CreateNetworkRearchableAnalysis** operation to obtain the ID of the task for analyzing network reachability.
        self.network_reachable_analysis_id = network_reachable_analysis_id
        # The ID of the region for which you want to obtain the result of network reachability analysis.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.network_reachable_analysis_id is not None:
            result['NetworkReachableAnalysisId'] = self.network_reachable_analysis_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NetworkReachableAnalysisId') is not None:
            self.network_reachable_analysis_id = m.get('NetworkReachableAnalysisId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetNetworkReachableAnalysisResponseBody(TeaModel):
    def __init__(
        self,
        ali_uid: int = None,
        create_time: str = None,
        network_path_id: str = None,
        network_path_parameter: str = None,
        network_reachable_analysis_id: str = None,
        network_reachable_analysis_result: str = None,
        network_reachable_analysis_status: str = None,
        reachable: bool = None,
        request_id: str = None,
    ):
        # The unique ID (UID) of the Alibaba Cloud account.
        self.ali_uid = ali_uid
        # The time when the network path was created. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.create_time = create_time
        # The network path ID.
        self.network_path_id = network_path_id
        # The parameters of the network path.
        self.network_path_parameter = network_path_parameter
        # The ID of the task for analyzing network reachability.
        self.network_reachable_analysis_id = network_reachable_analysis_id
        # The result of network reachability analysis, which includes the network topology, error codes of network unreachability, and rules of network unreachability.
        self.network_reachable_analysis_result = network_reachable_analysis_result
        # The state of the task for analyzing network reachability. Valid values:
        # 
        # *   **init**: The task is in progress.
        # *   **finish**: The task is complete.
        # *   **error**: An analysis error occurred.
        # *   **timeout**: The task timed out.
        self.network_reachable_analysis_status = network_reachable_analysis_status
        # Indicates whether the network path is reachable. Valid values:
        # 
        # *   **true**: The network path is reachable.
        # *   **false**: The network path is unreachable.
        self.reachable = reachable
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.network_path_id is not None:
            result['NetworkPathId'] = self.network_path_id
        if self.network_path_parameter is not None:
            result['NetworkPathParameter'] = self.network_path_parameter
        if self.network_reachable_analysis_id is not None:
            result['NetworkReachableAnalysisId'] = self.network_reachable_analysis_id
        if self.network_reachable_analysis_result is not None:
            result['NetworkReachableAnalysisResult'] = self.network_reachable_analysis_result
        if self.network_reachable_analysis_status is not None:
            result['NetworkReachableAnalysisStatus'] = self.network_reachable_analysis_status
        if self.reachable is not None:
            result['Reachable'] = self.reachable
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('NetworkPathId') is not None:
            self.network_path_id = m.get('NetworkPathId')
        if m.get('NetworkPathParameter') is not None:
            self.network_path_parameter = m.get('NetworkPathParameter')
        if m.get('NetworkReachableAnalysisId') is not None:
            self.network_reachable_analysis_id = m.get('NetworkReachableAnalysisId')
        if m.get('NetworkReachableAnalysisResult') is not None:
            self.network_reachable_analysis_result = m.get('NetworkReachableAnalysisResult')
        if m.get('NetworkReachableAnalysisStatus') is not None:
            self.network_reachable_analysis_status = m.get('NetworkReachableAnalysisStatus')
        if m.get('Reachable') is not None:
            self.reachable = m.get('Reachable')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetNetworkReachableAnalysisResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetNetworkReachableAnalysisResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetNetworkReachableAnalysisResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


